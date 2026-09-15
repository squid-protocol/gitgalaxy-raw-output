# ARCHITECTURAL_BRIEF: node-stdlib-browser
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
| Total Artifacts | 54 |
| Analyzed Artifacts (Scanned) | 30 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 24 |
| Total LOC | 3329 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 55.6% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | n/a (not computed) | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | n/a (not computed) | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 14 | 2709 | 46.7% |
| TYPESCRIPT | 10 | 620 | 33.3% |
| MARKDOWN | 3 | 0 | 10.0% |
| PLAINTEXT | 3 | 0 | 10.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Small Flat Repo` (z +0.30; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 27%, Defensive Guards Files 17%, Large Core Modules 17%, State Mutators Files 13%, Callbacks & Closures Files 10%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 24 | 80.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 6 | 20.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 24*

**Composition by Extension & Reason:**
- `.map`: 20x Excluded (Unsupported Extension: '.map'), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 84.0 | 26.3 | 5.7 | 4.3 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.2 | 38.2 | 25.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 98.2 | 16.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 8.9 | 2.4 | 2.3 |
| Connectivity (formerly API Exposure) | 2.8 | 97.9 | 20.4 | 12.2 | 3.5 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 20.8 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 36.9 | 9.7 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 12.2 | 2.6 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 83.3 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 68.2 | 93.8 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 6 | 4 | 1 | `package/cjs/proxy/url.d.ts` |
| cleanup | 8 | 4 | 2 | `package/cjs/proxy/process.js` |
| guards | 284 | 10 | 21 | `package/cjs/proxy/url.js` |
| danger | 60 | 8 | 4 | `package/cjs/proxy/url.js` |
| concurrency | 69 | 5 | 16 | `package/cjs/proxy/process.js` |
| connectivity | 448 | 24 | 51 | `package/cjs/proxy/process.js` |
| io | 52 | 8 | 4 | `package/cjs/index.d.ts` |
| crypto | 0 | 0 | 0 | - |
| ipc | 24 | 4 | 4 | `package/cjs/index.d.ts` |
| time | 64 | 4 | 16 | `package/cjs/proxy/process.js` |
| serialization | 0 | 0 | 0 | - |
| regex | 50 | 6 | 1 | `package/cjs/proxy/url.js` |
| events | 120 | 8 | 25 | `package/esm/proxy/process.js` |
| tests | 22 | 2 | 0 | `package/cjs/index.js` |
| docs | 63 | 12 | 7 | `package/cjs/proxy/url.js` |
| debt | 6 | 6 | 1 | `package/cjs/proxy/process.js` |
| mutation | 1478 | 20 | 125 | `package/cjs/proxy/url.js` |
| dead_code | 31 | 11 | 3 | `package/cjs/proxy/url.js` |
| credential | 0 | 0 | 0 | - |
| threat | 79 | 12 | 10 | `package/cjs/proxy/url.js` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/cjs/index.d.ts` (Hits: 20)
- `package/esm/index.d.ts` (Hits: 20)
- `package/cjs/index.js` (Hits: 4)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
No file in this repository is imported by another file that GitGalaxy could resolve, so there is no blast-radius ranking to report. That is itself a finding: either the codebase genuinely has no internal dependency structure (a collection of scripts, documents or configuration rather than a coupled system), or its import style is one the engine does not resolve for this language. Do not infer that any file is load-bearing from this section.


### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **README.md** (`package/README.md`) — 8 outbound dependencies
2. **plugin.js** (`package/helpers/esbuild/plugin.js`) — 4 outbound dependencies
3. **index.js** (`package/cjs/index.js`) — 3 outbound dependencies
4. **process.d.ts** (`package/cjs/proxy/process.d.ts`) — 2 outbound dependencies
5. **querystring.d.ts** (`package/cjs/proxy/querystring.d.ts`) — 2 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `resolveObject` **(Compute Cores)** (@ `package/cjs/proxy/url.js`) -> Impact: **175.0** | LOC: 275
- `resolveObject` **(Compute Cores)** (@ `package/esm/proxy/url.js`) -> Impact: **175.0** | LOC: 275
- `parse` **(Many-Argument Workhorses)** (@ `package/cjs/proxy/url.js`) -> Impact: **162.1** | LOC: 281
- `parse` **(Many-Argument Workhorses)** (@ `package/esm/proxy/url.js`) -> Impact: **162.1** | LOC: 281
- `format` **(Defensive Guards)** (@ `package/cjs/proxy/url.js`) -> Impact: **38.8** | LOC: 55
- `format` **(Defensive Guards)** (@ `package/esm/proxy/url.js`) -> Impact: **38.8** | LOC: 55
- `formatImportWithOverloads` **(Defensive Guards)** (@ `package/cjs/proxy/url.js`) -> Impact: **22.2** | LOC: 28
  * *Intent:* /** * @type {( * ((urlObject: URL, options?: URLFormatOptions) => string) & * ((urlObject: UrlObject | string, options?: never) => string) * )} */
- `formatImportWithOverloads` **(Defensive Guards)** (@ `package/esm/proxy/url.js`) -> Impact: **22.2** | LOC: 28
  * *Intent:* /** * @type {( * ((urlObject: URL, options?: URLFormatOptions) => string) & * ((urlObject: UrlObject | string, options?: never) => string) * )} */
- `resolvePath` **(Compute Cores)** (@ `package/cjs/index.js`) -> Impact: **21.2** | LOC: 112
  * *Intent:* /** * @param {string} path */
- `normalizeArray` **(Defensive Guards)** (@ `package/cjs/proxy/url.js`) -> Impact: **16.8** | LOC: 25
  * *Intent:* // in all copies or substantial portions of the Software. // // THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS // OR IMPLIED,...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `package/cjs/proxy` | 6 | 1609.4 | 36.84% | 19.88% |
| `package/esm/proxy` | 6 | 1454.4 | 31.02% | 19.96% |
| `package/cjs/proxy/process` | 2 | 314.08 | 44.16% | 6.07% |
| `package/esm/proxy/process` | 2 | 225.72 | 43.93% | 6.3% |
| `package/cjs` | 3 | 53.76 | 4.45% | 7.87% |
| `package/helpers/esbuild` | 2 | 44.48 | 9.73% | 36.55% |
| `package/esm` | 3 | 37.08 | 3.71% | 8.12% |
| `package` | 4 | 12.24 | 0.0% | 0.0% |
| `package/helpers/rollup` | 1 | 10.48 | 4.36% | 0.0% |
| `package/helpers/webpack` | 1 | 4.64 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `package/cjs/proxy/url.d.ts` -> **98.2014%** Exposure
- `package/esm/proxy/url.d.ts` -> **98.2014%** Exposure
- `package/helpers/esbuild/plugin.js` -> **73.1059%** Exposure
- `package/esm/index.js` -> **24.3642%** Exposure
- `package/cjs/index.js` -> **23.6089%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `package/cjs/proxy/process.js` -> **100.0%** Exposure
- `package/cjs/proxy/process/browser.js` -> **100.0%** Exposure
- `package/cjs/proxy/url.js` -> **100.0%** Exposure
- `package/esm/proxy/url.js` -> **100.0%** Exposure
- `package/esm/proxy/process.js` -> **99.9999%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/cjs/proxy/url.d.ts` -> **3** Orphaned Functions | **0** Duplicates
- `package/esm/proxy/url.d.ts` -> **3** Orphaned Functions | **0** Duplicates
- `package/cjs/index.js` -> **1** Orphaned Functions | **0** Duplicates
- `package/esm/index.js` -> **1** Orphaned Functions | **0** Duplicates
- `package/helpers/esbuild/plugin.js` -> **1** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `38` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `package/cjs/proxy/process.js` (JAVASCRIPT) -> Cumulative Risk: **750.22**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.97)
- **Magnitude:** 313.4 | **LOC:** 283 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9923%)
- **Heaviest Functions:** `runClearTimeout` (Defensive Guards, Impact: 8.4), `runTimeout` (Defensive Guards, Impact: 8.3), `nextTick` (Defensive Guards, Impact: 7.7)

### 2. `package/esm/proxy/process.js` (JAVASCRIPT) -> Cumulative Risk: **725.52**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.95)
- **Magnitude:** 225.04 | **LOC:** 262 | **CtrlFlow:** 11.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Concurrency (99.9967%)
- **Heaviest Functions:** `runClearTimeout` (Defensive Guards, Impact: 8.4), `runTimeout` (Defensive Guards, Impact: 8.3), `nextTick` (Defensive Guards, Impact: 7.7)

### 3. `package/cjs/proxy/process/browser.js` (JAVASCRIPT) -> Cumulative Risk: **667.55**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.97)
- **Magnitude:** 313.4 | **LOC:** 283 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9923%)
- **Heaviest Functions:** `runClearTimeout` (Defensive Guards, Impact: 8.4), `runTimeout` (Defensive Guards, Impact: 8.3), `nextTick` (Defensive Guards, Impact: 7.7)

### 4. `package/esm/proxy/process/browser.js` (JAVASCRIPT) -> Cumulative Risk: **653.17**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.95)
- **Magnitude:** 225.04 | **LOC:** 262 | **CtrlFlow:** 11.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Concurrency (99.9967%)
- **Heaviest Functions:** `runClearTimeout` (Defensive Guards, Impact: 8.4), `runTimeout` (Defensive Guards, Impact: 8.3), `nextTick` (Defensive Guards, Impact: 7.7)

### 5. `package/cjs/proxy/url.js` (JAVASCRIPT) -> Cumulative Risk: **644.05**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z -0.43)
- **Magnitude:** 1267.28 | **LOC:** 1073 | **CtrlFlow:** 43.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.1577%), Verification (80.0%)
- **Heaviest Functions:** `resolveObject` (Compute Cores, Impact: 175.0), `parse` (Many-Argument Workhorses, Impact: 162.1), `format` (Defensive Guards, Impact: 38.8)

### 6. `package/esm/proxy/url.js` (JAVASCRIPT) -> Cumulative Risk: **610.05**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z -0.33)
- **Magnitude:** 1218.44 | **LOC:** 1051 | **CtrlFlow:** 43.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.0716%), Verification (80.0%)
- **Heaviest Functions:** `resolveObject` (Compute Cores, Impact: 175.0), `parse` (Many-Argument Workhorses, Impact: 162.1), `format` (Defensive Guards, Impact: 38.8)

### 7. `package/cjs/proxy/querystring.js` (JAVASCRIPT) -> Cumulative Risk: **482.61**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.15)
- **Magnitude:** 23.34 | **LOC:** 56 | **CtrlFlow:** 2.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9254%), Safety Score (81.6293%), Documentation (66.6667%)
- **Heaviest Functions:** `qsEscape` (Interface Declarations, Impact: 1.6), `qsUnescape` (Interface Declarations, Impact: 1.6), `get` (Callbacks & Closures, Impact: 1.1)

### 8. `package/helpers/esbuild/plugin.js` (JAVASCRIPT) -> Cumulative Risk: **479.99**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z -0.62)
- **Magnitude:** 32.7 | **LOC:** 43 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Tech Debt (73.1059%), Safety Score (65.3461%)
- **Heaviest Functions:** `setup` (Callbacks & Closures, Impact: 2.4), `plugin` (Callbacks & Closures, Impact: 1.7)

### 9. `package/cjs/proxy/url.d.ts` (TYPESCRIPT) -> Cumulative Risk: **379.91**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `State Mutators Files` (z -0.13)
- **Magnitude:** 1.7 | **LOC:** 50 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (98.2014%), Stability (50.0%)
- **Heaviest Functions:** `createObjectURL` (State Mutators, Impact: 1.5), `revokeObjectURL` (Interface Declarations, Impact: 1.5), `toString` (State Mutators, Impact: 1.1)

### 10. `package/esm/proxy/url.d.ts` (TYPESCRIPT) -> Cumulative Risk: **379.91**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `State Mutators Files` (z -0.13)
- **Magnitude:** 1.7 | **LOC:** 50 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (98.2014%), Stability (50.0%)
- **Heaviest Functions:** `createObjectURL` (State Mutators, Impact: 1.5), `revokeObjectURL` (Interface Declarations, Impact: 1.5), `toString` (State Mutators, Impact: 1.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `package/cjs/proxy/url.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1267.28 | **LOC:** 1073 | **CtrlFlow:** 43.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.8939%), Tech Debt (8.9385%)
**Top Internal Functions/Classes:**
  * `resolveObject` **(Compute Cores)** (Impact: 175.0)
  * `parse` **(Many-Argument Workhorses)** (Impact: 162.1)
  * `format` **(Defensive Guards)** (Impact: 38.8)
  * `formatImportWithOverloads` **(Defensive Guards)** (Impact: 22.2)
    * *Intent:* /** * @type {( * ((urlObject: URL, options?: URLFormatOptions) => string) & * ((urlObject: UrlObject...
  * `normalizeArray` **(Defensive Guards)** (Impact: 16.8)
    * *Intent:* // in all copies or substantial portions of the Software. // // THE SOFTWARE IS PROVIDED "AS IS", WI...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 233 instances
* *State Mutation (weighted view):* 719
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 301`, `structural_boundaries: 154`, `args: 26`, `func_start: 29`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 253`, `dead_code: 5`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 12`, `import: 2`
* *Defense:* `safety: 92`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 33.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` punycode, qs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/proxy/url.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1218.44 | **LOC:** 1051 | **CtrlFlow:** 43.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.4242%), Tech Debt (8.9748%)
**Top Internal Functions/Classes:**
  * `resolveObject` **(Compute Cores)** (Impact: 175.0)
  * `parse` **(Many-Argument Workhorses)** (Impact: 162.1)
  * `format` **(Defensive Guards)** (Impact: 38.8)
  * `formatImportWithOverloads` **(Defensive Guards)** (Impact: 22.2)
    * *Intent:* /** * @type {( * ((urlObject: URL, options?: URLFormatOptions) => string) & * ((urlObject: UrlObject...
  * `normalizeArray` **(Defensive Guards)** (Impact: 16.8)
    * *Intent:* // in all copies or substantial portions of the Software. // // THE SOFTWARE IS PROVIDED "AS IS", WI...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 225 instances
* *State Mutation (weighted view):* 690
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 294`, `structural_boundaries: 152`, `args: 25`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 240`, `dead_code: 5`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 1`, `import: 2`
* *Defense:* `safety: 90`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 33.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` punycode, qs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/proxy/process.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 313.4 | **LOC:** 283 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.9615%), Tech Debt (12.1408%)
**Top Internal Functions/Classes:**
  * `runClearTimeout` **(Defensive Guards)** (Impact: 8.4)
  * `runTimeout` **(Defensive Guards)** (Impact: 8.3)
  * `nextTick` **(Defensive Guards)** (Impact: 7.7)
  * `cleanUpNextTick` **(I/O & Config Routines)** (Impact: 6.7)
  * `drainQueue` **(I/O & Config Routines)** (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 31 instances
* *Concurrency (weighted view):* 38
* *State Mutation (weighted view):* 144
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 43`, `args: 16`, `func_start: 16`
* *Risk/State:* `state_mutation: 82`, `dead_code: 3`, `planned_debt: 1`
* *Architecture:* `api: 75`, `concurrency: 8`
* *Defense:* `safety: 21`, `doc: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 33.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/proxy/process/browser.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 313.4 | **LOC:** 283 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.9615%), Tech Debt (12.1408%)
**Top Internal Functions/Classes:**
  * `runClearTimeout` **(Defensive Guards)** (Impact: 8.4)
  * `runTimeout` **(Defensive Guards)** (Impact: 8.3)
  * `nextTick` **(Defensive Guards)** (Impact: 7.7)
  * `cleanUpNextTick` **(I/O & Config Routines)** (Impact: 6.7)
  * `drainQueue` **(I/O & Config Routines)** (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 31 instances
* *Concurrency (weighted view):* 38
* *State Mutation (weighted view):* 144
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 43`, `args: 16`, `func_start: 16`
* *Risk/State:* `state_mutation: 82`, `dead_code: 3`, `planned_debt: 1`
* *Architecture:* `api: 75`, `concurrency: 8`
* *Defense:* `safety: 21`, `doc: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 33.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/proxy/process.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 225.04 | **LOC:** 262 | **CtrlFlow:** 11.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.5074%), Tech Debt (12.5985%)
**Top Internal Functions/Classes:**
  * `runClearTimeout` **(Defensive Guards)** (Impact: 8.4)
  * `runTimeout` **(Defensive Guards)** (Impact: 8.3)
  * `nextTick` **(Defensive Guards)** (Impact: 7.7)
  * `cleanUpNextTick` **(I/O & Config Routines)** (Impact: 6.7)
  * `drainQueue` **(I/O & Config Routines)** (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 22 instances
* *Concurrency (weighted view):* 38
* *State Mutation (weighted view):* 90
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 63`, `args: 16`, `func_start: 16`
* *Risk/State:* `state_mutation: 46`, `dead_code: 3`, `planned_debt: 1`
* *Architecture:* `api: 41`, `concurrency: 8`
* *Defense:* `safety: 21`, `doc: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 33.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/proxy/process/browser.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 225.04 | **LOC:** 262 | **CtrlFlow:** 11.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.5074%), Tech Debt (12.5985%)
**Top Internal Functions/Classes:**
  * `runClearTimeout` **(Defensive Guards)** (Impact: 8.4)
  * `runTimeout` **(Defensive Guards)** (Impact: 8.3)
  * `nextTick` **(Defensive Guards)** (Impact: 7.7)
  * `cleanUpNextTick` **(I/O & Config Routines)** (Impact: 6.7)
  * `drainQueue` **(I/O & Config Routines)** (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 22 instances
* *Concurrency (weighted view):* 38
* *State Mutation (weighted view):* 90
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 63`, `args: 16`, `func_start: 16`
* *Risk/State:* `state_mutation: 46`, `dead_code: 3`, `planned_debt: 1`
* *Architecture:* `api: 41`, `concurrency: 8`
* *Defense:* `safety: 21`, `doc: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 33.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 51.64 | **LOC:** 148 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.2348%), Tech Debt (23.6089%)
**Top Internal Functions/Classes:**
  * `resolvePath` **(Compute Cores)** (Impact: 21.2)
    * *Intent:* /** * @param {string} path */
  * `_interopDefaultLegacy` **(Defensive Guards)** (Impact: 8.5)
  * `_globalThis` **(Defensive Guards)** (Impact: 8.1)
  * `get` **(Interface Declarations)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 20`, `args: 4`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 4`, `unreferenced_by_name: 1`
* *Architecture:* `io: 4`, `api: 1`, `import: 3`
* *Defense:* `safety: 9`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 33.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` create-require, pkg-dir, u
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 34.96 | **LOC:** 141 | **CtrlFlow:** 7.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.0168%), Tech Debt (24.3642%)
**Top Internal Functions/Classes:**
  * `resolvePath` **(Compute Cores)** (Impact: 14.1)
    * *Intent:* /** * @param {string} path */
  * `_globalThis` **(Defensive Guards)** (Impact: 8.1)
  * `get` **(Interface Declarations)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 19`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 3`, `unreferenced_by_name: 1`
* *Architecture:* `io: 4`, `api: 1`, `import: 2`
* *Defense:* `safety: 4`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 33.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` create-require, pkg-dir
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/helpers/esbuild/plugin.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 32.7 | **LOC:** 43 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (73.1059%)
**Top Internal Functions/Classes:**
  * `setup` **(Callbacks & Closures)** (Impact: 2.4)
  * `plugin` **(Callbacks & Closures)** (Impact: 1.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Concurrency (weighted view):* 25
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 8`, `args: 5`, `func_start: 3`
* *Risk/State:* `state_mutation: 2`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `concurrency: 5`, `import: 2`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 33.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .., browser-resolve, esbuild, util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/proxy/querystring.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 23.34 | **LOC:** 56 | **CtrlFlow:** 2.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.5529%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `qsEscape` **(Interface Declarations)** (Impact: 1.6)
    * *Intent:* /** * @typedef {import('querystring').escape} qsEscape * @typedef {import('querystring').unescape} q...
  * `qsUnescape` **(Interface Declarations)** (Impact: 1.6)
    * *Intent:* /** * @type {qsUnescape} */
  * `get` **(Callbacks & Closures)** (Impact: 1.1)
  * `get` **(Callbacks & Closures)** (Impact: 1.1)
  * `get` **(Callbacks & Closures)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 8`, `args: 6`, `func_start: 6`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 33.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` querystring, querystring-es3
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/helpers/esbuild/shim.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 11.78 | **LOC:** 25 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (19.4699%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_globalThis` **(Defensive Guards)** (Impact: 8.1)
  * `get` **(Interface Declarations)** (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 12`, `args: 2`, `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 33.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` buffer, process
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/helpers/rollup/plugin.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 10.48 | **LOC:** 35 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.3557%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handleCircularDependancyWarning` **(Defensive Guards)** (Impact: 8.0)
    * *Intent:* /** * @typedef {import('rollup')} rollup * @typedef {import('rollup').WarningHandlerWithDefault} rol...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 3`, `args: 2`, `func_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`
* *Defense:* `safety: 3`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 33.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` rollup
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 33.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` example, buffer.js, console.js, dns.js, net.js, process.js, tls.js, tty.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/proxy/querystring.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 5.54 | **LOC:** 33 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.5587%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `qsEscape` **(Interface Declarations)** (Impact: 1.6)
    * *Intent:* /** * @typedef {import('querystring').escape} qsEscape * @typedef {import('querystring').unescape} q...
  * `qsUnescape` **(Interface Declarations)** (Impact: 1.6)
    * *Intent:* /** * @type {qsUnescape} */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 6`, `args: 2`, `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 33.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` querystring, querystring-es3
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/helpers/webpack/plugin.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 4.64 | **LOC:** 17 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `NodeProtocolUrlPlugin` **(Callbacks & Closures)** (Impact: 1.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`, `args: 2`, `func_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 33.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` webpack
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/proxy/process.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3.01 | **LOC:** 73 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.25%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `emitWarning` **(Interface Declarations)** (Impact: 1.1)
  * `exit` **(Interface Declarations)** (Impact: 1.1)
  * `kill` **(Interface Declarations)** (Impact: 1.1)
  * `dlopen` **(Interface Declarations)** (Impact: 1.1)
  * `uptime` **(Interface Declarations)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 79`, `args: 7`, `func_start: 7`
* *Risk/State:* None
* *Architecture:* `api: 51`, `import: 19`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 33.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` events, process
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/proxy/process.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3.01 | **LOC:** 73 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.25%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `emitWarning` **(Interface Declarations)** (Impact: 1.1)
  * `exit` **(Interface Declarations)** (Impact: 1.1)
  * `kill` **(Interface Declarations)** (Impact: 1.1)
  * `dlopen` **(Interface Declarations)** (Impact: 1.1)
  * `uptime` **(Interface Declarations)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 79`, `args: 7`, `func_start: 7`
* *Risk/State:* None
* *Architecture:* `api: 51`, `import: 19`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 33.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` events, process
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 33.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/proxy/url.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1.7 | **LOC:** 50 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.0573%), Tech Debt (98.2014%)
**Top Internal Functions/Classes:**
  * `createObjectURL` **(State Mutators)** (Impact: 1.5)
  * `revokeObjectURL` **(Interface Declarations)** (Impact: 1.5)
  * `toString` **(State Mutators)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 63`, `args: 7`, `func_start: 3`
* *Risk/State:* `unreferenced_by_name: 3`
* *Architecture:* `io: 1`, `api: 29`, `import: 12`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 33.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` url
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/proxy/url.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1.7 | **LOC:** 50 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.0573%), Tech Debt (98.2014%)
**Top Internal Functions/Classes:**
  * `createObjectURL` **(State Mutators)** (Impact: 1.5)
  * `revokeObjectURL` **(Interface Declarations)** (Impact: 1.5)
  * `toString` **(State Mutators)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 63`, `args: 7`, `func_start: 3`
* *Risk/State:* `unreferenced_by_name: 3`
* *Architecture:* `io: 1`, `api: 29`, `import: 12`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 33.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` url
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 33.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/index.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1.12 | **LOC:** 170 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.1231%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 13`
* *Risk/State:* None
* *Architecture:* `io: 20`, `api: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 33.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/index.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1.12 | **LOC:** 170 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.1231%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 13`
* *Risk/State:* None
* *Architecture:* `io: 20`, `api: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 33.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/LICENSE.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 19 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 33.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/package.json` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 33.333
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

- `package/cjs/proxy/process.d.ts` -> **Severity: 3333.3** (Blast Radius: 33.333 * Doc Risk: 100.0%)
- `package/cjs/proxy/querystring.d.ts` -> **Severity: 3333.3** (Blast Radius: 33.333 * Doc Risk: 100.0%)
- `package/cjs/proxy/url.d.ts` -> **Severity: 3333.3** (Blast Radius: 33.333 * Doc Risk: 100.0%)
- `package/esm/proxy/process.d.ts` -> **Severity: 3333.3** (Blast Radius: 33.333 * Doc Risk: 100.0%)
- `package/esm/proxy/querystring.d.ts` -> **Severity: 3333.3** (Blast Radius: 33.333 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
