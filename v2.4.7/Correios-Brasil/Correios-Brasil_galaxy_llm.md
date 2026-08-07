# ARCHITECTURAL_BRIEF: Correios-Brasil
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/Correios-Brasil` |
| **Timestamp** | `2026-08-07T03:29:22.119030+00:00` |
| **Scan Duration** | `0.15s` |
| **Git Branch** | `master` |
| **Git Commit** | `03eef682886174627cc559163a25b7180c642e54` |
| **Git Remote** | `https://github.com/FinotiLucas/Correios-Brasil.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 8 malicious artifacts.

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
| Total Artifacts | 25 |
| Analyzed Artifacts (Scanned) | 12 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 13 |
| Total LOC | 159 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 48.0% |
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
| TYPESCRIPT | 6 | 98 | 50.0% |
| PLAINTEXT | 2 | 0 | 16.7% |
| JAVASCRIPT | 2 | 40 | 16.7% |
| MARKDOWN | 1 | 0 | 8.3% |
| JSON | 1 | 21 | 8.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.614`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 6 | 50.0% |
| file_cluster_13 | 3 | 25.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 25.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 13*

**Composition by Extension & Reason:**
- `no_extension`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xml`: 1x Excluded (Saturation: Line 2 exceeds 500 chars)
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 2.5 | 28.2 | 8.3 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 80.0 | 16.9 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 11.1 | 0.0 | 0.0 |
| Testing Exposure | 0.6 | 2.5 | 1.7 | 2.0 | 0.6 |
| API Exposure | 0.0 | 8.5 | 4.9 | 5.6 | 5.8 |
| Concurrency Exposure | 0.0 | 78.0 | 8.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 23.1 | 2.6 | 0.0 | 0.0 |
| Specification Exposure | 26.7 | 100.0 | 71.9 | 80.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 4.0 | 25.7 | 16.3 | 17.4 | 11.9 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `lib/utils/request.ts` (Hits: 9)
- `lib/utils/URL.ts` (Hits: 6)
- `README.md` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **rastreio.txt** (`tests/static/rastreio.txt`) — 1 inbound connections
2. **README.md** (`README.md`) — 0 inbound connections
3. **index.ts** (`lib/index.ts`) — 0 inbound connections
4. **URL.ts** (`lib/utils/URL.ts`) — 0 inbound connections
5. **formatter.ts** (`lib/utils/formatter.ts`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **rollup.config.js** (`rollup.config.js`) — 6 outbound dependencies
2. **index.ts** (`lib/index.ts`) — 3 outbound dependencies
3. **request.ts** (`lib/utils/request.ts`) — 3 outbound dependencies
4. **parser.ts** (`lib/utils/parser.ts`) — 2 outbound dependencies
5. **README.md** (`README.md`) — 0 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `sanitization` (@ `lib/utils/validation.ts`) -> Impact: **4.3** | LOC: 6
- `request` (@ `lib/utils/request.ts`) -> Impact: **4.0** | LOC: 11
- `formatDateTime` (@ `lib/utils/formatter.ts`) -> Impact: **2.6** | LOC: 12
- `formatStatus` (@ `lib/utils/formatter.ts`) -> Impact: **2.5** | LOC: 9
- `formatLocal` (@ `lib/utils/formatter.ts`) -> Impact: **2.5** | LOC: 9
- `formatOrigin` (@ `lib/utils/formatter.ts`) -> Impact: **2.5** | LOC: 9
  * *Intent:* /** * @param {string} str * Função responsável formatar o Local de entrega de uma encomenda
- `formatDestiny` (@ `lib/utils/formatter.ts`) -> Impact: **2.5** | LOC: 9
- `convertArrayBufferToString` (@ `lib/utils/parser.ts`) -> Impact: **2.3** | LOC: 6
- `convertXMLStringToJson` (@ `lib/utils/parser.ts`) -> Impact: **2.1** | LOC: 3
- `reject` (@ `lib/utils/request.ts`) -> Impact: **1.7** | LOC: 5

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 5 | 42.26 | 4.74% | 0.0% |
| `tests/static` | 1 | 10.72 | 0.0% | 0.0% |
| `lib/utils` | 5 | 5.54 | 9.15% | 20.0% |
| `lib` | 1 | 1.31 | 5.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `lib/utils/formatter.ts` -> **99.9918%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `lib/utils/formatter.ts` -> **5** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`rollup.config.js`** -> AI Confidence: **98.96%**
2. **`lib/utils/request.ts`** -> AI Confidence: **98.89%**
3. **`lib/index.ts`** -> AI Confidence: **98.88%**
4. **`lib/utils/URL.ts`** -> AI Confidence: **98.85%**
5. **`lib/utils/validation.ts`** -> AI Confidence: **98.85%**
6. **`lib/utils/formatter.ts`** -> AI Confidence: **98.84%**
7. **`lib/utils/parser.ts`** -> AI Confidence: **98.84%**
8. **`prettier.config.js`** -> AI Confidence: **98.84%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `10` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `lib/utils/request.ts` (TYPESCRIPT) -> Cumulative Risk: **317.98**
- **Archetype:** `file_cluster_13` (Distance: 9.171 IQR)
- **Magnitude:** 1.03 | **LOC:** 27 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (80.0%), Concurrency (77.9938%), Cognitive Load (28.2388%)
- **Heaviest Functions:** `request` (Impact: 4.0), `reject` (Impact: 1.7), `axios` (Impact: 1.1)

### 2. `lib/utils/formatter.ts` (TYPESCRIPT) -> Cumulative Risk: **232.39**
- **Archetype:** `file_cluster_8` (Distance: 8.357 IQR)
- **Magnitude:** 1.84 | **LOC:** 68 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9918%), Documentation (18.9753%), Api Exposure (8.4635%)
- **Heaviest Functions:** `formatDateTime` (Impact: 2.6), `formatStatus` (Impact: 2.5), `formatLocal` (Impact: 2.5)

### 3. `lib/utils/parser.ts` (TYPESCRIPT) -> Cumulative Risk: **189.24**
- **Archetype:** `file_cluster_8` (Distance: 7.727 IQR)
- **Magnitude:** 0.56 | **LOC:** 16 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (80.0%), Safety Score (71.6667%), Documentation (25.6657%), Cognitive Load (5.0%)
- **Heaviest Functions:** `convertArrayBufferToString` (Impact: 2.3), `convertXMLStringToJson` (Impact: 2.1)

### 4. `rollup.config.js` (JAVASCRIPT) -> Cumulative Risk: **148.36**
- **Archetype:** `file_cluster_13` (Distance: 10.925 IQR)
- **Magnitude:** 4.0 | **LOC:** 43 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Dead Code (23.1475%), Documentation (11.9203%), Cognitive Load (7.2908%)
- **Heaviest Functions:** `typescript` (Impact: 1.2), `commonjs` (Impact: 1.1)

### 5. `lib/utils/URL.ts` (TYPESCRIPT) -> Cumulative Risk: **92.94**
- **Archetype:** `file_cluster_8` (Distance: 5.865 IQR)
- **Magnitude:** 1.57 | **LOC:** 11 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (60.0%), Documentation (20.9775%), Api Exposure (5.5789%), Cognitive Load (5.0%)

### 6. `lib/utils/validation.ts` (TYPESCRIPT) -> Cumulative Risk: **76.11**
- **Archetype:** `file_cluster_8` (Distance: 7.446 IQR)
- **Magnitude:** 0.54 | **LOC:** 9 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (46.6667%), Documentation (17.4159%), Api Exposure (5.7813%), Cognitive Load (5.0%)
- **Heaviest Functions:** `sanitization` (Impact: 4.3)

### 7. `lib/index.ts` (TYPESCRIPT) -> Cumulative Risk: **49.19**
- **Archetype:** `file_cluster_13` (Distance: 6.854 IQR)
- **Magnitude:** 1.31 | **LOC:** 6 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (26.6667%), Documentation (11.1315%), Api Exposure (5.7813%), Cognitive Load (5.0%)

### 8. `prettier.config.js` (JAVASCRIPT) -> Cumulative Risk: **48.85**
- **Archetype:** `file_cluster_8` (Distance: 5.013 IQR)
- **Magnitude:** 13.6 | **LOC:** 6 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (33.3333%), Api Exposure (5.7813%), Cognitive Load (5.0%), Documentation (3.9734%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `tsconfig.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 15.42 | **LOC:** 22 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.4293%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 77.821
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `prettier.config.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.013 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 1.363 IQR)
- **Top Global Matches:** file_cluster_8: 5.013, file_cluster_7: 6.487, file_cluster_1: 6.708
- **Magnitude:** 13.6 | **LOC:** 6 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 77.821
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/static/rastreio.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 10.72 | **LOC:** 536 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 143.969
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.090909
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 7.54 | **LOC:** 377 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 77.821
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rollup.config.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.925 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.755 IQR)
- **Top Global Matches:** file_cluster_13: 10.925, file_cluster_0: 10.952, file_cluster_8: 11.21
- **Magnitude:** 4.0 | **LOC:** 43 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.2908%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `typescript` (Impact: 1.2)
  * `commonjs` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 6`, `func_start: 4`
* *Risk/State:* `dead_code: 1`
* *Architecture:* `api: 1`, `import: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 77.821
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` plugin-node-resolve, plugin-commonjs, rollup-plugin-dts, plugin-typescript, package.json, rollup-plugin-terser
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/utils/formatter.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.357 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.497 IQR)
- **Top Global Matches:** file_cluster_8: 8.357, file_cluster_7: 8.817, file_cluster_1: 9.027
- **Magnitude:** 1.84 | **LOC:** 68 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.4899%), Tech Debt (99.9918%)
**Top Internal Functions/Classes:**
  * `formatDateTime` (Impact: 2.6)
  * `formatStatus` (Impact: 2.5)
  * `formatLocal` (Impact: 2.5)
  * `formatOrigin` (Impact: 2.5)
    * *Intent:* /** * @param {string} str * Função responsável formatar o Local de entrega de uma encomenda
  * `formatDestiny` (Impact: 2.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 10`, `args: 5`, `func_start: 5`
* *Risk/State:* `orphaned_logic: 5`
* *Architecture:* `api: 5`
* *Defense:* `doc: 10`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 77.821
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package.json` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.7 | **LOC:** 85 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 77.821
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/utils/URL.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.865 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.811 IQR)
- **Top Global Matches:** file_cluster_8: 5.865, file_cluster_7: 7.147, file_cluster_1: 7.409
- **Magnitude:** 1.57 | **LOC:** 11 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 2`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `io: 6`, `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 77.821
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/index.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_13` (Drift: 6.854 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.677 IQR)
- **Top Global Matches:** file_cluster_13: 6.854, file_cluster_8: 7.316, file_cluster_7: 8.329
- **Magnitude:** 1.31 | **LOC:** 6 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 77.821
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` cep, precos, rastreio
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/utils/request.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.171 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 6.65 IQR)
- **Top Global Matches:** file_cluster_13: 9.171, file_cluster_8: 9.23, file_cluster_4: 9.496
- **Magnitude:** 1.03 | **LOC:** 27 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (28.2388%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `request` (Impact: 4.0)
  * `reject` (Impact: 1.7)
  * `axios` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 10`, `args: 6`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`
* *Architecture:* `io: 9`, `api: 1`, `concurrency: 2`, `import: 3`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 77.821
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` http, axios, https
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/utils/parser.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.727 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.038 IQR)
- **Top Global Matches:** file_cluster_8: 7.727, file_cluster_13: 7.972, file_cluster_7: 8.734
- **Magnitude:** 0.56 | **LOC:** 16 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `convertArrayBufferToString` (Impact: 2.3)
  * `convertXMLStringToJson` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 5`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 77.821
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` xml-js, iconv-lite
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/utils/validation.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.446 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.318 IQR)
- **Top Global Matches:** file_cluster_8: 7.446, file_cluster_7: 8.434, file_cluster_1: 8.747
- **Magnitude:** 0.54 | **LOC:** 9 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `sanitization` (Impact: 4.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 2`, `args: 1`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 77.821
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `rollup.config.js` (JAVASCRIPT) | Magnitude: 4.0 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 6, import: 5, func_start: 4
- `lib/utils/request.ts` (TYPESCRIPT) | Magnitude: 1.03 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 10, io: 9, branch: 6
- `lib/index.ts` (TYPESCRIPT) | Magnitude: 1.31 | Delta: **0.462 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, import: 3, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `lib/utils/parser.ts` (TYPESCRIPT) | Magnitude: 0.56 | Delta: **0.245 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, indent_spaces: 4, args: 2, func_start: 2
- `lib/utils/formatter.ts` (TYPESCRIPT) | Magnitude: 1.84 | Delta: **0.46 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 32, regex_execution: 17, structural_boundaries: 10, doc: 10

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `lib/utils/parser.ts` -> **Severity: 1997.33** (Blast Radius: 77.821 * Doc Risk: 25.6657%)
- `lib/utils/request.ts` -> **Severity: 1956.786** (Blast Radius: 77.821 * Doc Risk: 25.1447%)
- `lib/utils/URL.ts` -> **Severity: 1632.49** (Blast Radius: 77.821 * Doc Risk: 20.9775%)
- `lib/utils/formatter.ts` -> **Severity: 1476.677** (Blast Radius: 77.821 * Doc Risk: 18.9753%)
- `lib/utils/validation.ts` -> **Severity: 1355.323** (Blast Radius: 77.821 * Doc Risk: 17.4159%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
