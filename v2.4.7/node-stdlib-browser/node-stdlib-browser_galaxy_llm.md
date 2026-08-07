# ARCHITECTURAL_BRIEF: node-stdlib-browser
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/npm_top_200/node-stdlib-browser` |
| **Timestamp** | `2026-08-07T05:16:07.356273+00:00` |
| **Scan Duration** | `0.18s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 22 malicious artifacts.

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
| Total Artifacts | 52 |
| Analyzed Artifacts (Scanned) | 28 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 24 |
| Total LOC | 2193 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 53.8% |
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
| JAVASCRIPT | 12 | 1573 | 42.9% |
| TYPESCRIPT | 10 | 620 | 35.7% |
| MARKDOWN | 3 | 0 | 10.7% |
| PLAINTEXT | 3 | 0 | 10.7% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `3.833`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 10 | 35.7% |
| file_cluster_8 | 6 | 21.4% |
| file_cluster_4 | 4 | 14.3% |
| file_cluster_11 | 2 | 7.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 6 | 21.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 24*

**Composition by Extension & Reason:**
- `.map`: 20x Excluded (Unsupported Extension: '.map'), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 4.1 | 79.7 | 24.5 | 9.8 | 5.0 |
| Error & Exception Exposure | 0.0 | 94.4 | 31.0 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 20.7 | 0.0 | 0.0 |
| Testing Exposure | 0.5 | 80.0 | 9.2 | 2.3 | 2.3 |
| API Exposure | 2.8 | 18.4 | 10.5 | 9.2 | 6.3 |
| Concurrency Exposure | 0.0 | 98.8 | 17.8 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 33.8 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 6.6 | 1.6 | 0.0 | 0.0 |
| Specification Exposure | 20.0 | 100.0 | 91.8 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 11.9 | 100.0 | 56.7 | 40.6 | 100.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/cjs/proxy/url.js` (Hits: 21)
- `package/esm/proxy/url.js` (Hits: 21)
- `package/cjs/index.d.ts` (Hits: 20)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **CHANGELOG.md** (`package/CHANGELOG.md`) — 0 inbound connections
2. **LICENSE.md** (`package/LICENSE.md`) — 0 inbound connections
3. **README.md** (`package/README.md`) — 0 inbound connections
4. **index.d.ts** (`package/cjs/index.d.ts`) — 0 inbound connections
5. **process.d.ts** (`package/cjs/proxy/process.d.ts`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.js** (`package/cjs/index.js`) — 3 outbound dependencies
2. **process.d.ts** (`package/cjs/proxy/process.d.ts`) — 2 outbound dependencies
3. **querystring.d.ts** (`package/cjs/proxy/querystring.d.ts`) — 2 outbound dependencies
4. **process.d.ts** (`package/esm/proxy/process.d.ts`) — 2 outbound dependencies
5. **querystring.d.ts** (`package/esm/proxy/querystring.d.ts`) — 2 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `parse` (@ `package/cjs/proxy/url.js`) -> Impact: **372.5** | LOC: 450
  * *Intent:* // protocols that can allow "unsafe" and "unwise" chars.
- `parse` (@ `package/esm/proxy/url.js`) -> Impact: **371.9** | LOC: 437
  * *Intent:* // protocols that can allow "unsafe" and "unwise" chars.
- `format` (@ `package/cjs/proxy/url.js`) -> Impact: **65.0** | LOC: 52
  * *Intent:* // if we still have not hit it, then the entire thing is a host.
- `format` (@ `package/esm/proxy/url.js`) -> Impact: **65.0** | LOC: 52
  * *Intent:* // if we still have not hit it, then the entire thing is a host.
- `resolveObject` (@ `package/cjs/proxy/url.js`) -> Impact: **48.2** | LOC: 64
- `resolveObject` (@ `package/esm/proxy/url.js`) -> Impact: **48.2** | LOC: 64
- `formatImportWithOverloads` (@ `package/cjs/proxy/url.js`) -> Impact: **22.2** | LOC: 28
- `formatImportWithOverloads` (@ `package/esm/proxy/url.js`) -> Impact: **22.2** | LOC: 28
- `resolvePath` (@ `package/cjs/index.js`) -> Impact: **21.5** | LOC: 15
  * *Intent:* /**
- `_interopDefaultLegacy` (@ `package/cjs/index.js`) -> Impact: **12.1** | LOC: 1

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `package/cjs/proxy` | 6 | 1107.52 | 29.26% | 33.86% |
| `package/esm/proxy` | 6 | 1046.52 | 29.79% | 17.87% |
| `package/cjs/proxy/process` | 2 | 100.16 | 24.21% | 32.94% |
| `package/esm/proxy/process` | 2 | 86.8 | 38.03% | 40.08% |
| `package/cjs` | 3 | 84.88 | 9.83% | 0.0% |
| `package/esm` | 3 | 52.3 | 6.5% | 0.0% |
| `package` | 4 | 12.24 | 0.0% | 0.0% |
| `package/helpers/rollup` | 1 | 9.48 | 5.4% | 0.0% |
| `package/helpers/webpack` | 1 | 3.34 | 5.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `package/cjs/proxy/querystring.js` -> **100.0%** Exposure
- `package/cjs/proxy/url.d.ts` -> **84.1131%** Exposure
- `package/esm/proxy/url.d.ts` -> **84.1131%** Exposure
- `package/esm/proxy/process/browser.js` -> **80.1565%** Exposure
- `package/cjs/proxy/process/browser.js` -> **65.8787%** Exposure
### Highest State Flux (Mutation/Volatility)
- `package/cjs/proxy/url.js` -> **100.0%** Exposure
- `package/esm/proxy/process.js` -> **100.0%** Exposure
- `package/esm/proxy/process/browser.js` -> **100.0%** Exposure
- `package/esm/proxy/url.js` -> **100.0%** Exposure
- `package/cjs/proxy/process.js` -> **94.1179%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/cjs/proxy/querystring.js` -> **0** Orphaned Functions | **4** Duplicates
- `package/cjs/proxy/url.d.ts` -> **2** Orphaned Functions | **0** Duplicates
- `package/esm/proxy/url.d.ts` -> **2** Orphaned Functions | **0** Duplicates
- `package/cjs/proxy/process/browser.js` -> **1** Orphaned Functions | **0** Duplicates
- `package/esm/proxy/process/browser.js` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`package/cjs/proxy/url.js`** -> AI Confidence: **99.11%**
2. **`package/cjs/index.js`** -> AI Confidence: **99.09%**
3. **`package/cjs/proxy/process.js`** -> AI Confidence: **99.06%**
4. **`package/cjs/proxy/process/browser.js`** -> AI Confidence: **99.06%**
5. **`package/helpers/rollup/plugin.js`** -> AI Confidence: **99.06%**
6. **`package/esm/proxy/url.js`** -> AI Confidence: **99.03%**
7. **`package/cjs/proxy/process/browser.d.ts`** -> AI Confidence: **98.89%**
8. **`package/esm/proxy/process/browser.d.ts`** -> AI Confidence: **98.89%**
9. **`package/esm/proxy/process.js`** -> AI Confidence: **98.89%**
10. **`package/esm/proxy/process/browser.js`** -> AI Confidence: **98.89%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `25` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `package/esm/proxy/process/browser.js` (JAVASCRIPT) -> Cumulative Risk: **696.52**
- **Archetype:** `file_cluster_4` (Distance: 13.263 IQR)
- **Magnitude:** 85.44 | **LOC:** 262 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.9933%), Concurrency (98.8278%)
- **Heaviest Functions:** `runClearTimeout` (Impact: 3.9)

### 2. `package/esm/proxy/process.js` (JAVASCRIPT) -> Cumulative Risk: **639.58**
- **Archetype:** `file_cluster_4` (Distance: 13.242 IQR)
- **Magnitude:** 86.44 | **LOC:** 262 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.9955%), Concurrency (98.8278%)
- **Heaviest Functions:** `runClearTimeout` (Impact: 3.9)

### 3. `package/cjs/proxy/process/browser.js` (JAVASCRIPT) -> Cumulative Risk: **626.34**
- **Archetype:** `file_cluster_4` (Distance: 11.729 IQR)
- **Magnitude:** 98.8 | **LOC:** 283 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (97.0497%), State Flux (94.1179%)
- **Heaviest Functions:** `runClearTimeout` (Impact: 3.9)

### 4. `package/cjs/proxy/process.js` (JAVASCRIPT) -> Cumulative Risk: **579.55**
- **Archetype:** `file_cluster_4` (Distance: 11.711 IQR)
- **Magnitude:** 99.8 | **LOC:** 283 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (97.0497%), State Flux (94.1179%)
- **Heaviest Functions:** `runClearTimeout` (Impact: 3.9)

### 5. `package/cjs/proxy/url.js` (JAVASCRIPT) -> Cumulative Risk: **529.02**
- **Archetype:** `file_cluster_11` (Distance: 14.383 IQR)
- **Magnitude:** 980.36 | **LOC:** 1073 | **CtrlFlow:** 70.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (94.3262%), Verification (80.0%)
- **Heaviest Functions:** `parse` (Impact: 372.5), `format` (Impact: 65.0), `resolveObject` (Impact: 48.2)

### 6. `package/esm/proxy/url.js` (JAVASCRIPT) -> Cumulative Risk: **524.99**
- **Archetype:** `file_cluster_11` (Distance: 14.383 IQR)
- **Magnitude:** 942.32 | **LOC:** 1051 | **CtrlFlow:** 70.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (94.3874%), Verification (80.0%)
- **Heaviest Functions:** `parse` (Impact: 371.9), `format` (Impact: 65.0), `resolveObject` (Impact: 48.2)

### 7. `package/cjs/proxy/querystring.js` (JAVASCRIPT) -> Cumulative Risk: **427.15**
- **Archetype:** `file_cluster_8` (Distance: 9.869 IQR)
- **Magnitude:** 16.74 | **LOC:** 56 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Safety Score (58.6235%), Stability (50.0%)
- **Heaviest Functions:** `qsEscape` (Impact: 1.9), `qsUnescape` (Impact: 1.9), `get` (Impact: 1.8)

### 8. `package/cjs/proxy/url.d.ts` (TYPESCRIPT) -> Cumulative Risk: **366.35**
- **Archetype:** `file_cluster_13` (Distance: 8.665 IQR)
- **Magnitude:** 3.56 | **LOC:** 50 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (84.1131%), Stability (50.0%)
- **Heaviest Functions:** `revokeObjectURL` (Impact: 3.8), `toString` (Impact: 1.8)

### 9. `package/esm/proxy/url.d.ts` (TYPESCRIPT) -> Cumulative Risk: **366.35**
- **Archetype:** `file_cluster_13` (Distance: 8.665 IQR)
- **Magnitude:** 3.56 | **LOC:** 50 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (84.1131%), Stability (50.0%)
- **Heaviest Functions:** `revokeObjectURL` (Impact: 3.8), `toString` (Impact: 1.8)

### 10. `package/cjs/index.js` (JAVASCRIPT) -> Cumulative Risk: **310.14**
- **Archetype:** `file_cluster_13` (Distance: 11.922 IQR)
- **Magnitude:** 81.64 | **LOC:** 148 | **CtrlFlow:** 51.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (60.2349%), State Flux (57.3405%), Stability (50.0%)
- **Heaviest Functions:** `resolvePath` (Impact: 21.5), `_interopDefaultLegacy` (Impact: 12.1), `_globalThis` (Impact: 9.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `package/cjs/proxy/url.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.383 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.816 IQR)
- **Top Global Matches:** file_cluster_11: 14.383, file_cluster_13: 14.474, file_cluster_8: 14.494
- **Magnitude:** 980.36 | **LOC:** 1073 | **CtrlFlow:** 70.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.6939%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 372.5)
    * *Intent:* // protocols that can allow "unsafe" and "unwise" chars.
  * `format` (Impact: 65.0)
    * *Intent:* // if we still have not hit it, then the entire thing is a host.
  * `resolveObject` (Impact: 48.2)
  * `formatImportWithOverloads` (Impact: 22.2)
  * `_interopDefaultLegacy` (Impact: 12.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 191`, `structural_boundaries: 81`, `args: 16`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 392`, `dead_code: 1`
* *Architecture:* `io: 21`, `api: 15`, `import: 2`
* *Defense:* `safety: 54`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 35.714
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` qs, punycode
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/proxy/url.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.383 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.862 IQR)
- **Top Global Matches:** file_cluster_11: 14.383, file_cluster_8: 14.456, file_cluster_13: 14.465
- **Magnitude:** 942.32 | **LOC:** 1051 | **CtrlFlow:** 70.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.909%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 371.9)
    * *Intent:* // protocols that can allow "unsafe" and "unwise" chars.
  * `format` (Impact: 65.0)
    * *Intent:* // if we still have not hit it, then the entire thing is a host.
  * `resolveObject` (Impact: 48.2)
  * `formatImportWithOverloads` (Impact: 22.2)
  * `urlParse` (Impact: 8.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 184`, `structural_boundaries: 79`, `args: 15`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 378`, `dead_code: 1`
* *Architecture:* `io: 21`, `api: 4`, `import: 2`
* *Defense:* `safety: 52`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 35.714
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` qs, punycode
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/proxy/process.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.711 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 5.295 IQR)
- **Top Global Matches:** file_cluster_4: 11.711, file_cluster_8: 11.929, file_cluster_0: 11.937
- **Magnitude:** 99.8 | **LOC:** 283 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.4267%), Tech Debt (19.0407%)
**Top Internal Functions/Classes:**
  * `runClearTimeout` (Impact: 3.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 9`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 12`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 74`, `concurrency: 8`
* *Defense:* `safety: 6`, `doc: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 35.714
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/proxy/process/browser.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.729 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 5.338 IQR)
- **Top Global Matches:** file_cluster_4: 11.729, file_cluster_0: 11.945, file_cluster_8: 11.945
- **Magnitude:** 98.8 | **LOC:** 283 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.4267%), Tech Debt (65.8787%)
**Top Internal Functions/Classes:**
  * `runClearTimeout` (Impact: 3.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 9`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 12`, `dead_code: 1`, `planned_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 73`, `concurrency: 8`
* *Defense:* `safety: 6`, `doc: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 35.714
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/proxy/process.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.242 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.827 IQR)
- **Top Global Matches:** file_cluster_4: 13.242, file_cluster_11: 13.554, file_cluster_0: 13.6
- **Magnitude:** 86.44 | **LOC:** 262 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.0609%), Tech Debt (23.1244%)
**Top Internal Functions/Classes:**
  * `runClearTimeout` (Impact: 3.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 29`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 33`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 40`, `concurrency: 8`
* *Defense:* `safety: 6`, `doc: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 35.714
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/proxy/process/browser.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.263 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.88 IQR)
- **Top Global Matches:** file_cluster_4: 13.263, file_cluster_11: 13.57, file_cluster_0: 13.61
- **Magnitude:** 85.44 | **LOC:** 262 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.0609%), Tech Debt (80.1565%)
**Top Internal Functions/Classes:**
  * `runClearTimeout` (Impact: 3.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 29`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 33`, `dead_code: 1`, `planned_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 39`, `concurrency: 8`
* *Defense:* `safety: 6`, `doc: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 35.714
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.922 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 5.974 IQR)
- **Top Global Matches:** file_cluster_13: 11.922, file_cluster_8: 11.988, file_cluster_0: 12.111
- **Magnitude:** 81.64 | **LOC:** 148 | **CtrlFlow:** 51.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (25.3788%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `resolvePath` (Impact: 21.5)
    * *Intent:* /**
  * `_interopDefaultLegacy` (Impact: 12.1)
  * `_globalThis` (Impact: 9.7)
  * `get` (Impact: 3.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 20`, `args: 4`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 31`
* *Architecture:* `io: 17`, `api: 1`, `import: 3`
* *Defense:* `safety: 9`, `doc: 14`, `test: 3`, `immutability_locks: 45`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 35.714
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pkg-dir, u, create-require
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.755 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 5.828 IQR)
- **Top Global Matches:** file_cluster_8: 10.755, file_cluster_13: 10.942, file_cluster_7: 11.06
- **Magnitude:** 49.06 | **LOC:** 141 | **CtrlFlow:** 36.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.3679%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `resolvePath` (Impact: 11.1)
    * *Intent:* /**
  * `_globalThis` (Impact: 9.7)
  * `get` (Impact: 3.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 19`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 21`
* *Architecture:* `io: 17`, `api: 1`, `import: 2`
* *Defense:* `safety: 4`, `doc: 14`, `test: 3`, `immutability_locks: 45`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 35.714
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pkg-dir, create-require
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/proxy/querystring.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.869 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 4.341 IQR)
- **Top Global Matches:** file_cluster_8: 9.869, file_cluster_12: 10.185, file_cluster_7: 10.212
- **Magnitude:** 16.74 | **LOC:** 56 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.6443%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `qsEscape` (Impact: 1.9)
    * *Intent:* /** * @typedef {import('querystring').escape} qsEscape * @typedef {import('querystring').unescape} q...
  * `qsUnescape` (Impact: 1.9)
    * *Intent:* /** * @typedef {import('querystring').escape} qsEscape * @typedef {import('querystring').unescape} q...
  * `get` (Impact: 1.8)
  * `get` (Impact: 1.8)
  * `get` (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 8`, `args: 6`, `func_start: 6`
* *Risk/State:* `state_mutation: 2`, `duplicate_logic: 4`
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 35.714
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` querystring, querystring-es3
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/helpers/rollup/plugin.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.074 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.579 IQR)
- **Top Global Matches:** file_cluster_8: 10.074, file_cluster_7: 10.491, file_cluster_1: 10.731
- **Magnitude:** 9.48 | **LOC:** 35 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.3962%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handleCircularDependancyWarning` (Impact: 8.0)
    * *Intent:* /** * @typedef {import('rollup')} rollup * @typedef {import('rollup').WarningHandlerWithDefault} rol...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 3`, `args: 2`, `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 1`
* *Defense:* `safety: 3`, `doc: 5`, `test: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 35.714
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` rollup
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/proxy/querystring.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.73%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.853 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 3.471 IQR)
- **Top Global Matches:** file_cluster_13: 9.853, file_cluster_8: 9.952, file_cluster_7: 10.179
- **Magnitude:** 7.14 | **LOC:** 33 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.9505%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `qsEscape` (Impact: 1.9)
    * *Intent:* /** * @typedef {import('querystring').escape} qsEscape * @typedef {import('querystring').unescape} q...
  * `qsUnescape` (Impact: 1.9)
    * *Intent:* /** * @typedef {import('querystring').escape} qsEscape * @typedef {import('querystring').unescape} q...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 6`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 35.714
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` querystring, querystring-es3
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 7.06 | **LOC:** 353 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 35.714
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/proxy/process.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.45 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.639 IQR)
- **Top Global Matches:** file_cluster_13: 9.45, file_cluster_8: 9.805, file_cluster_1: 10.172
- **Magnitude:** 5.81 | **LOC:** 73 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.25%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `uvCounters` (Impact: 2.0)
  * `exit` (Impact: 1.9)
  * `emitWarning` (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 72`, `args: 7`, `func_start: 7`
* *Risk/State:* None
* *Architecture:* `api: 51`, `import: 19`
* *Defense:* `safety: 7`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 35.714
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` events, process
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/proxy/process.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.45 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.639 IQR)
- **Top Global Matches:** file_cluster_13: 9.45, file_cluster_8: 9.805, file_cluster_1: 10.172
- **Magnitude:** 5.81 | **LOC:** 73 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.25%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `uvCounters` (Impact: 2.0)
  * `exit` (Impact: 1.9)
  * `emitWarning` (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 72`, `args: 7`, `func_start: 7`
* *Risk/State:* None
* *Architecture:* `api: 51`, `import: 19`
* *Defense:* `safety: 7`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 35.714
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` events, process
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/proxy/url.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.665 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.043 IQR)
- **Top Global Matches:** file_cluster_13: 8.665, file_cluster_8: 9.074, file_cluster_16: 9.773
- **Magnitude:** 3.56 | **LOC:** 50 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.584%), Tech Debt (84.1131%)
**Top Internal Functions/Classes:**
  * `revokeObjectURL` (Impact: 3.8)
  * `toString` (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 61`, `args: 7`, `func_start: 3`
* *Risk/State:* `orphaned_logic: 2`
* *Architecture:* `io: 1`, `api: 29`, `import: 12`
* *Defense:* `safety: 2`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 35.714
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` url
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/proxy/url.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.665 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.043 IQR)
- **Top Global Matches:** file_cluster_13: 8.665, file_cluster_8: 9.074, file_cluster_16: 9.773
- **Magnitude:** 3.56 | **LOC:** 50 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.584%), Tech Debt (84.1131%)
**Top Internal Functions/Classes:**
  * `revokeObjectURL` (Impact: 3.8)
  * `toString` (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 61`, `args: 7`, `func_start: 3`
* *Risk/State:* `orphaned_logic: 2`
* *Architecture:* `io: 1`, `api: 29`, `import: 12`
* *Defense:* `safety: 2`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 35.714
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` url
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/helpers/webpack/plugin.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.303 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.055 IQR)
- **Top Global Matches:** file_cluster_8: 7.303, file_cluster_13: 8.135, file_cluster_7: 8.403
- **Magnitude:** 3.34 | **LOC:** 17 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `NodeProtocolUrlPlugin` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`, `args: 2`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 35.714
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` webpack
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/package.json` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 2.88 | **LOC:** 144 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 35.714
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/index.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.588 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.654 IQR)
- **Top Global Matches:** file_cluster_8: 5.588, file_cluster_7: 6.977, file_cluster_1: 7.121
- **Magnitude:** 2.24 | **LOC:** 170 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.1231%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 13`
* *Risk/State:* None
* *Architecture:* `io: 20`, `api: 4`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 35.714
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/index.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.588 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.654 IQR)
- **Top Global Matches:** file_cluster_8: 5.588, file_cluster_7: 6.977, file_cluster_1: 7.121
- **Magnitude:** 2.24 | **LOC:** 170 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.1231%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 13`
* *Risk/State:* None
* *Architecture:* `io: 20`, `api: 4`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 35.714
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/proxy/process/browser.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_13` (Drift: 6.546 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.661 IQR)
- **Top Global Matches:** file_cluster_13: 6.546, file_cluster_8: 7.122, file_cluster_7: 8.17
- **Magnitude:** 1.36 | **LOC:** 4 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 3`
* *Risk/State:* None
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 35.714
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` process.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/proxy/process/browser.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_13` (Drift: 6.546 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.661 IQR)
- **Top Global Matches:** file_cluster_13: 6.546, file_cluster_8: 7.122, file_cluster_7: 8.17
- **Magnitude:** 1.36 | **LOC:** 4 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 3`
* *Risk/State:* None
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 35.714
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` process.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/CHANGELOG.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.3 | **LOC:** 65 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 35.714
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/proxy/querystring.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 7.694 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.03 IQR)
- **Top Global Matches:** file_cluster_13: 7.694, file_cluster_8: 7.841, file_cluster_7: 8.788
- **Magnitude:** 1.25 | **LOC:** 21 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.9756%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `qsUnescape` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 22`, `args: 2`, `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 10`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 35.714
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` querystring, querystring-es3
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/proxy/querystring.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 7.694 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.03 IQR)
- **Top Global Matches:** file_cluster_13: 7.694, file_cluster_8: 7.841, file_cluster_7: 8.788
- **Magnitude:** 1.25 | **LOC:** 21 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.9756%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `qsUnescape` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 22`, `args: 2`, `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 10`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 35.714
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` querystring, querystring-es3
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `package/esm/proxy/url.js` (JAVASCRIPT) | Magnitude: 942.32 | Delta: **0.073 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 393, state_mutation: 378, branch: 184, structural_boundaries: 79
- `package/cjs/proxy/url.js` (JAVASCRIPT) | Magnitude: 980.36 | Delta: **0.091 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 393, state_mutation: 392, branch: 191, structural_boundaries: 81

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `package/cjs/index.js` (JAVASCRIPT) | Magnitude: 81.64 | Delta: **0.066 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 74, immutability_locks: 45, state_mutation: 31, branch: 21
- `package/esm/proxy/querystring.js` (JAVASCRIPT) | Magnitude: 7.14 | Delta: **0.099 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 8, doc: 7, structural_boundaries: 6, args: 2
- `package/cjs/proxy/querystring.d.ts` (TYPESCRIPT) | Magnitude: 1.25 | Delta: **0.147 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 22, api: 10, import: 6, indent_spaces: 6
- `package/esm/proxy/querystring.d.ts` (TYPESCRIPT) | Magnitude: 1.25 | Delta: **0.147 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 22, api: 10, import: 6, indent_spaces: 6
- `package/cjs/proxy/process.d.ts` (TYPESCRIPT) | Magnitude: 5.81 | Delta: **0.355 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 72, api: 51, indent_spaces: 34, import: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `package/cjs/proxy/process/browser.js` (JAVASCRIPT) | Magnitude: 98.8 | Delta: **0.216 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: api: 73, indent_spaces: 50, events: 16, state_mutation: 12
- `package/cjs/proxy/process.js` (JAVASCRIPT) | Magnitude: 99.8 | Delta: **0.218 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: api: 74, indent_spaces: 50, events: 16, state_mutation: 12
- `package/esm/proxy/process/browser.js` (JAVASCRIPT) | Magnitude: 85.44 | Delta: **0.307 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 50, api: 39, state_mutation: 33, structural_boundaries: 29
- `package/esm/proxy/process.js` (JAVASCRIPT) | Magnitude: 86.44 | Delta: **0.312 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 50, api: 40, state_mutation: 33, structural_boundaries: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `package/esm/index.js` (JAVASCRIPT) | Magnitude: 49.06 | Delta: **0.187 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 74, immutability_locks: 45, state_mutation: 21, structural_boundaries: 19
- `package/cjs/proxy/querystring.js` (JAVASCRIPT) | Magnitude: 16.74 | Delta: **0.316 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 8, indent_tabs: 8, indent_spaces: 8, doc: 7
- `package/helpers/rollup/plugin.js` (JAVASCRIPT) | Magnitude: 9.48 | Delta: **0.417 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 20, doc: 5, branch: 3, structural_boundaries: 3
- `package/helpers/webpack/plugin.js` (JAVASCRIPT) | Magnitude: 3.34 | Delta: **0.832 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 6, structural_boundaries: 2, args: 2, immutability_locks: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/cjs/proxy/process.d.ts` -> **Severity: 3571.4** (Blast Radius: 35.714 * Doc Risk: 100.0%)
- `package/cjs/proxy/url.d.ts` -> **Severity: 3571.4** (Blast Radius: 35.714 * Doc Risk: 100.0%)
- `package/esm/proxy/process.d.ts` -> **Severity: 3571.4** (Blast Radius: 35.714 * Doc Risk: 100.0%)
- `package/esm/proxy/url.d.ts` -> **Severity: 3571.4** (Blast Radius: 35.714 * Doc Risk: 100.0%)
- `package/cjs/proxy/process.js` -> **Severity: 3571.4** (Blast Radius: 35.714 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
