# ARCHITECTURAL_BRIEF: avvio
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
| Total Artifacts | 9 |
| Analyzed Artifacts (Scanned) | 6 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3 |
| Total LOC | 619 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 66.7% |
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
| JAVASCRIPT | 3 | 548 | 50.0% |
| MARKDOWN | 1 | 0 | 16.7% |
| TYPESCRIPT | 1 | 71 | 16.7% |
| PLAINTEXT | 1 | 0 | 16.7% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 4 | 66.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 33.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3*

**Composition by Extension & Reason:**
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 85.5 | 30.6 | 18.5 | 85.5 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 81.1 | 48.9 | 57.3 | 81.1 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 97.0 | 28.8 | 9.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 2.8 | 2.0 | 2.5 | 2.8 |
| Connectivity (formerly API Exposure) | 0.0 | 3.5 | 2.2 | 2.6 | 2.2 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 99.9 | 59.7 | 69.4 | 99.9 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 32.6 | 15.3 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 5.4 | 1.4 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 75.0 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 47.4 | 44.8 | 44.5 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 5 | 2 | 1 | `package/index.d.ts` |
| cleanup | 4 | 1 | 0 | `package/boot.js` |
| guards | 55 | 1 | 0 | `package/boot.js` |
| danger | 19 | 3 | 2 | `package/boot.js` |
| concurrency | 27 | 3 | 12 | `package/boot.js` |
| connectivity | 3 | 3 | 1 | `package/boot.js` |
| io | 0 | 0 | 0 | - |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 9 | 2 | 3 | `package/examples/example.js` |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 14 | 3 | 5 | `package/boot.js` |
| tests | 0 | 0 | 0 | - |
| docs | 8 | 2 | 2 | `package/boot.js` |
| debt | 9 | 1 | 0 | `package/examples/example.js` |
| mutation | 149 | 4 | 7 | `package/boot.js` |
| dead_code | 9 | 2 | 4 | `package/boot.js` |
| credential | 0 | 0 | 0 | - |
| threat | 32 | 1 | 0 | `package/boot.js` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/README.md` (Hits: 0)
- `package/boot.js` (Hits: 0)
- `package/eslint.config.js` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
No file in this repository is imported by another file that GitGalaxy could resolve, so there is no blast-radius ranking to report. That is itself a finding: either the codebase genuinely has no internal dependency structure (a collection of scripts, documents or configuration rather than a coupled system), or its import style is one the engine does not resolve for this language. Do not infer that any file is load-bearing from this section.


### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **boot.js** (`package/boot.js`) — 13 outbound dependencies
2. **eslint.config.js** (`package/eslint.config.js`) — 1 outbound dependencies
3. **example.js** (`package/examples/example.js`) — 1 outbound dependencies
4. **index.d.ts** (`package/index.d.ts`) — 1 outbound dependencies
5. **README.md** (`package/README.md`) — 0 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `Boot` (@ `package/boot.js`) -> Impact: **38.6** | LOC: 93
- `avvio` (@ `package/index.d.ts`) -> Impact: **34.5** | LOC: 90
- `closeWithCbOrNextTick` (@ `package/boot.js`) -> Impact: **27.6** | LOC: 32
- `encapsulateThreeParam` (@ `package/boot.js`) -> Impact: **27.6** | LOC: 33
- `_encapsulateThreeParam` (@ `package/boot.js`) -> Impact: **27.4** | LOC: 28
- `encapsulateTwoParam` (@ `package/boot.js`) -> Impact: **20.5** | LOC: 28
- `_encapsulateTwoParam` (@ `package/boot.js`) -> Impact: **20.3** | LOC: 25
- `_addPlugin` (@ `package/boot.js`) -> Impact: **19.8** | LOC: 35
- `_loadPlugin` (@ `package/boot.js`) -> Impact: **19.6** | LOC: 45
  * *Intent:* /** * @callback LoadPluginCallback * @param {Error} [err] */ /** * Load a plugin * * @param {Plugin} plugin * @param {LoadPluginCallback} callback */
- `_expose` (@ `package/boot.js`) -> Impact: **18.8** | LOC: 75

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `package` | 5 | 680.49 | 20.08% | 23.02% |
| `package/examples` | 1 | 38.94 | 22.13% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `package/index.d.ts` -> **97.0284%** Exposure
- `package/boot.js` -> **18.0572%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `package/boot.js` -> **100.0%** Exposure
- `package/eslint.config.js` -> **16.7982%** Exposure
- `package/index.d.ts` -> **13.7452%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/boot.js` -> **4** Orphaned Functions | **0** Duplicates
- `package/index.d.ts` -> **4** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `5` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `package/boot.js` (JAVASCRIPT) -> Cumulative Risk: **589.49**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 647.62 | **LOC:** 622 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.91%), Cognitive Load (85.483%)
- **Heaviest Functions:** `Boot` (Impact: 38.6), `closeWithCbOrNextTick` (Impact: 27.6), `encapsulateThreeParam` (Impact: 27.6)

### 2. `package/index.d.ts` (TYPESCRIPT) -> Cumulative Risk: **418.31**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 2.75 | **LOC:** 96 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (97.0284%), Safety Score (50.0824%), Stability (50.0%)
- **Heaviest Functions:** `avvio` (Impact: 34.5), `avvio` (Impact: 2.9), `override` (Impact: 2.4)

### 3. `package/examples/example.js` (JAVASCRIPT) -> Cumulative Risk: **369.25**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 38.94 | **LOC:** 73 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (97.1174%), Stability (50.0%)
- **Heaviest Functions:** `a` (Impact: 6.2), `b` (Impact: 6.2), `c` (Impact: 6.2)

### 4. `package/eslint.config.js` (JAVASCRIPT) -> Cumulative Risk: **137.19**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 14.6 | **LOC:** 7 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Safety Score (64.5656%), Stability (50.0%), State Flux (16.7982%), Api Exposure (3.5258%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `package/boot.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 647.62 | **LOC:** 622 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (85.483%), Tech Debt (18.0572%)
**Top Internal Functions/Classes:**
  * `Boot` (Impact: 38.6)
  * `closeWithCbOrNextTick` (Impact: 27.6)
  * `encapsulateThreeParam` (Impact: 27.6)
  * `_encapsulateThreeParam` (Impact: 27.4)
  * `encapsulateTwoParam` (Impact: 20.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 69 instances
* *Concurrency (weighted view):* 57
* *State Mutation (weighted view):* 224
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 118`, `structural_boundaries: 55`, `args: 59`, `func_start: 40`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 86`, `dead_code: 1`, `unreferenced_by_name: 4`
* *Architecture:* `api: 1`, `concurrency: 12`, `import: 13`
* *Defense:* `safety: 55`, `doc: 6`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 166.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` debug, errors, execute-with-thenable, is-bundled-or-typescript-plugin, is-promise-like, plugin, symbols, thenify...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/examples/example.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 38.94 | **LOC:** 73 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.1307%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `a` (Impact: 6.2)
  * `b` (Impact: 6.2)
  * `c` (Impact: 6.2)
  * `duplicate` (Impact: 4.3)
  * `a` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 4`, `args: 14`, `func_start: 8`
* *Risk/State:* None
* *Architecture:* `concurrency: 6`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 166.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ..
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/eslint.config.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 14.6 | **LOC:** 7 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 166.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` neostandard
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 14.02 | **LOC:** 701 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 166.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/index.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2.75 | **LOC:** 96 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.9102%), Tech Debt (97.0284%)
**Top Internal Functions/Classes:**
  * `avvio` (Impact: 34.5)
  * `avvio` (Impact: 2.9)
  * `override` (Impact: 2.4)
  * `on` (Impact: 1.8)
  * `on` (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 57`, `args: 22`, `func_start: 10`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1`, `unreferenced_by_name: 4`
* *Architecture:* `api: 1`, `concurrency: 2`, `import: 1`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 166.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:events
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/package.json` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.5 | **LOC:** 75 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 166.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/examples/example.js` -> **Severity: 16666.7** (Blast Radius: 166.667 * Doc Risk: 100.0%)
- `package/index.d.ts` -> **Severity: 7500.015** (Blast Radius: 166.667 * Doc Risk: 45.0%)
- `package/boot.js` -> **Severity: 7424.265** (Blast Radius: 166.667 * Doc Risk: 44.5455%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
