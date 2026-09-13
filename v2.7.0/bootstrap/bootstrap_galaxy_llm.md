# ARCHITECTURAL_BRIEF: bootstrap
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/twbs/bootstrap.git` |
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
| Total Artifacts | 790 |
| Analyzed Artifacts (Scanned) | 171 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 619 |
| Total LOC | 25641 |
| Volatility Index | 0.006 |
| % Scanned of codebase = | 21.6% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2529 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3809 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.2724 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 4 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CSS | 95 | 7749 | 55.6% |
| JAVASCRIPT | 63 | 17353 | 36.8% |
| HTML | 6 | 462 | 3.5% |
| MARKDOWN | 4 | 0 | 2.3% |
| JSON | 1 | 32 | 0.6% |
| YAML | 1 | 45 | 0.6% |
| PLAINTEXT | 1 | 0 | 0.6% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 166 | 97.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 5 | 2.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 619*

**Composition by Extension & Reason:**
- `.png`: 111x Excluded (Explicitly Denied Extension: '.png')
- `.mdx`: 110x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.astro`: 104x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 53x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.map`: 48x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.css`: 47x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 32x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.scss`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Zero-Density Threshold (LOC: 63, Signals: 0), 1x Zero-Density Threshold (LOC: 57, Signals: 0)
- `.ts`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 20135 LOC)
- `.mjs`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 2x Excluded (Saturation: Line 41 exceeds 500 chars), 1x Excluded (Saturation: Line 31 exceeds 500 chars), 1x Excluded (Saturation: Line 32 exceeds 500 chars)
- `.svg`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 58.2 | 8.9 | 3.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.5 | 24.4 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 62.2 | 3.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 2.3 | 1.2 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 81.7 | 8.7 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 10.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 15.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 15.5 | 0.4 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 74.7 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 16.6 | 0.2 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 35.7 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 20 | 14 | 0 | `js/tests/unit/dom/selector-engine.spec.js` |
| cleanup | 59 | 26 | 1 | `js/tests/unit/tooltip.spec.js` |
| guards | 386 | 66 | 6 | `js/src/dropdown.js` |
| danger | 838 | 47 | 11 | `js/tests/unit/dropdown.spec.js` |
| concurrency | 602 | 21 | 4 | `js/tests/unit/dropdown.spec.js` |
| connectivity | 183 | 49 | 5 | `js/index.esm.js` |
| io | 89 | 10 | 0 | `js/tests/visual/dropdown.html` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 135 | 19 | 1 | `js/tests/unit/dropdown.spec.js` |
| serialization | 2 | 2 | 0 | `js/src/dom/manipulator.js` |
| regex | 19 | 10 | 0 | `js/src/util/index.js` |
| events | 896 | 46 | 11 | `js/tests/unit/dropdown.spec.js` |
| tests | 2687 | 26 | 50 | `js/tests/unit/dropdown.spec.js` |
| docs | 120 | 36 | 3 | `js/src/toast.js` |
| debt | 47 | 25 | 1 | `js/src/carousel.js` |
| mutation | 5538 | 67 | 79 | `js/tests/unit/dropdown.spec.js` |
| dead_code | 40 | 24 | 1 | `js/tests/unit/tooltip.spec.js` |
| credential | 0 | 0 | 0 | - |
| threat | 110 | 24 | 2 | `js/tests/unit/offcanvas.spec.js` |
| ml_ai | 2 | 1 | 0 | `scss/_functions.scss` |
| ui | 256 | 51 | 4 | `js/tests/unit/tooltip.spec.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `js/tests/visual/dropdown.html` (Hits: 62)
- `js/tests/visual/carousel.html` (Hits: 8)
- `js/tests/visual/alert.html` (Hits: 6)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **index.js** (`js/src/util/index.js`) — 31 inbound connections
2. **event-handler.js** (`js/src/dom/event-handler.js`) — 28 inbound connections
3. **fixture.js** (`js/tests/helpers/fixture.js`) — 25 inbound connections
4. **base-component.js** (`js/src/base-component.js`) — 13 inbound connections
5. **selector-engine.js** (`js/src/dom/selector-engine.js`) — 13 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **bootstrap.scss** (`scss/bootstrap.scss`) — 40 outbound dependencies
2. **_mixins.scss** (`scss/_mixins.scss`) — 25 outbound dependencies
3. **bootstrap-grid.scss** (`scss/bootstrap-grid.scss`) — 14 outbound dependencies
4. **index.esm.js** (`js/index.esm.js`) — 12 outbound dependencies
5. **index.umd.js** (`js/index.umd.js`) — 12 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `onSlid2` (@ `js/tests/unit/carousel.spec.js`) -> Impact: **63.0** | LOC: 779
- `expectDone` (@ `js/tests/unit/tab.spec.js`) -> Impact: **61.2** | LOC: 904
- `addHandler` (@ `js/src/dom/event-handler.js`) -> Impact: **34.0** | LOC: 44
- `parseSelector` (@ `js/src/util/index.js`) -> Impact: **31.0** | LOC: 83
  * *Intent:* /** * Properly escape IDs selectors to handle weird IDs * @param {string} selector * @returns {string} */
- `getActiveId` (@ `js/tests/unit/carousel.spec.js`) -> Impact: **30.8** | LOC: 416
- `off` (@ `js/src/dom/event-handler.js`) -> Impact: **28.6** | LOC: 35
- `el` (@ `js/tests/unit/util/index.spec.js`) -> Impact: **28.3** | LOC: 199
- `expectedDone` (@ `js/tests/unit/tooltip.spec.js`) -> Impact: **26.4** | LOC: 347
- `clearMenus` (@ `js/src/dropdown.js`) -> Impact: **25.9** | LOC: 37
- `restorePointerEvents` (@ `js/tests/unit/carousel.spec.js`) -> Impact: **24.6** | LOC: 272

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `js/tests/unit` | 13 | 3726.5 | 27.16% | 0.0% |
| `js/src` | 13 | 1405.02 | 19.83% | 6.57% |
| `js/tests/visual` | 6 | 540.28 | 0.0% | 0.0% |
| `js/tests/unit/util` | 9 | 522.12 | 24.64% | 0.0% |
| `js/src/util` | 9 | 506.36 | 17.29% | 11.11% |
| `js/src/dom` | 4 | 397.4 | 37.55% | 9.69% |
| `js/tests/unit/dom` | 4 | 349.22 | 25.28% | 0.0% |
| `js/tests` | 3 | 91.92 | 7.97% | 0.0% |
| `__monolith__` | 7 | 59.64 | 0.73% | 0.0% |
| `js` | 2 | 43.76 | 6.65% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `scss/helpers/_color-bg.scss` -> **62.2459%** Exposure
- `scss/helpers/_colored-links.scss` -> **62.2459%** Exposure
- `js/src/util/component-functions.js` -> **50.0%** Exposure
- `js/src/util/config.js` -> **50.0%** Exposure
- `scss/mixins/_breakpoints.scss` -> **39.0501%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `js/src/util/backdrop.js` -> **100.0%** Exposure
- `js/src/util/focustrap.js` -> **100.0%** Exposure
- `js/src/util/index.js` -> **100.0%** Exposure
- `js/src/util/swipe.js` -> **100.0%** Exposure
- `js/src/util/template-factory.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `js/tests/unit/scrollspy.spec.js` -> **2** Orphaned Functions | **3** Duplicates
- `js/tests/unit/dom/event-handler.spec.js` -> **2** Orphaned Functions | **2** Duplicates
- `js/tests/unit/tooltip.spec.js` -> **4** Orphaned Functions | **0** Duplicates
- `js/tests/unit/modal.spec.js` -> **3** Orphaned Functions | **0** Duplicates
- `js/tests/unit/util/backdrop.spec.js` -> **3** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `134` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `js/tests/unit/util/focustrap.spec.js` (JAVASCRIPT) -> Cumulative Risk: **536.98**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 61.52 | **LOC:** 219 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9682%)
- **Heaviest Functions:** `focusInListener` (Impact: 4.5), `focusInListener` (Impact: 3.5), `focusInListener` (Impact: 3.2)

### 2. `js/src/dom/selector-engine.js` (JAVASCRIPT) -> Cumulative Risk: **528.63**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 81.28 | **LOC:** 127 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.7916%), Documentation (95.6522%), Safety Score (75.8103%)
- **Heaviest Functions:** `getSelector` (Impact: 16.9), `prev` (Impact: 5.8), `next` (Impact: 5.8)

### 3. `js/tests/helpers/fixture.js` (JAVASCRIPT) -> Cumulative Risk: **508.45**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 29.66 | **LOC:** 48 | **CtrlFlow:** 7.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (89.4999%)
- **Heaviest Functions:** `each` (Impact: 3.1), `getFixture` (Impact: 2.9), `clearBodyAndDocument` (Impact: 2.4)

### 4. `js/src/tooltip.js` (JAVASCRIPT) -> Cumulative Risk: **498.81**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 287.66 | **LOC:** 634 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9077%), Documentation (98.0%), Safety Score (67.5388%)
- **Heaviest Functions:** `show` (Impact: 13.8), `_setListeners` (Impact: 13.1), `hide` (Impact: 9.1)

### 5. `js/src/carousel.js` (JAVASCRIPT) -> Cumulative Risk: **493.75**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 192.9 | **LOC:** 475 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (97.3684%), State Flux (89.4477%), Concurrency (66.0756%)
- **Heaviest Functions:** `_slide` (Impact: 20.9), `triggerEvent` (Impact: 10.5), `to` (Impact: 9.5)

### 6. `js/src/scrollspy.js` (JAVASCRIPT) -> Cumulative Risk: **480.11**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 150.88 | **LOC:** 297 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9873%), Documentation (95.0%), Safety Score (77.6991%)
- **Heaviest Functions:** `_observerCallback` (Impact: 14.6), `activate` (Impact: 14.5), `jQueryInterface` (Impact: 7.8)

### 7. `js/src/base-component.js` (JAVASCRIPT) -> Cumulative Risk: **473.99**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 45.14 | **LOC:** 87 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9977%), Documentation (92.8571%), Safety Score (82.2493%)
- **Heaviest Functions:** `getOrCreateInstance` (Impact: 5.3), `constructor` (Impact: 4.1), `dispose` (Impact: 2.4)

### 8. `js/tests/unit/util/index.spec.js` (JAVASCRIPT) -> Cumulative Risk: **473.45**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 162.0 | **LOC:** 721 | **CtrlFlow:** 7.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (75.72%)
- **Heaviest Functions:** `el` (Impact: 28.3), `functionBar` (Impact: 20.6), `el` (Impact: 3.9)

### 9. `js/src/dom/event-handler.js` (JAVASCRIPT) -> Cumulative Risk: **472.45**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 245.12 | **LOC:** 318 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.8805%), Documentation (96.7742%), Safety Score (62.5964%)
- **Heaviest Functions:** `addHandler` (Impact: 34.0), `off` (Impact: 28.6), `trigger` (Impact: 19.9)

### 10. `js/src/toast.js` (JAVASCRIPT) -> Cumulative Risk: **469.52**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 83.36 | **LOC:** 225 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (92.8729%), Documentation (88.8889%), Concurrency (66.744%)
- **Heaviest Functions:** `_onInteraction` (Impact: 18.9), `jQueryInterface` (Impact: 4.9), `_maybeScheduleHide` (Impact: 4.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `js/tests/unit/dropdown.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 673.98 | **LOC:** 2437 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.8025%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 18.2)
  * `expectDropdownToBeOpened` (Impact: 13.3)
  * `handleArrowUp` (Impact: 6.3)
  * `expectDropdownToBeOpened` (Impact: 2.7)
  * `expectDropdownToBeOpened` (Impact: 2.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 65 instances
* *Amplified Cascading Flux:* 27 instances
* *High Risk Execution (weighted view):* 81
* *Concurrency (weighted view):* 412
* *State Mutation (weighted view):* 173
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 704`, `args: 290`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 83`, `state_mutation: 119`, `planned_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `concurrency: 87`, `import: 4`
* *Defense:* `safety: 2`, `test: 296`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.978
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` event-handler.js, dropdown.js, index.js, fixture.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/tests/unit/tooltip.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 515.58 | **LOC:** 1586 | **CtrlFlow:** 2.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.0901%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `expectedDone` (Impact: 26.4)
  * `assertDone` (Impact: 14.3)
  * `tip` (Impact: 13.6)
  * `firstCallback` (Impact: 9.1)
  * `title` (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Race Conditions:* 41 instances
* *Amplified Cascading Flux:* 25 instances
* *High Risk Execution (weighted view):* 80
* *Concurrency (weighted view):* 264
* *State Mutation (weighted view):* 148
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 313`, `args: 234`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 84`, `state_mutation: 98`, `unreferenced_by_name: 4`
* *Architecture:* `concurrency: 59`, `import: 4`
* *Defense:* `safety: 4`, `test: 273`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.978
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` event-handler.js, tooltip.js, index.js, fixture.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/tests/unit/carousel.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 480.08 | **LOC:** 1573 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.5388%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onSlid2` (Impact: 63.0)
  * `getActiveId` (Impact: 30.8)
  * `restorePointerEvents` (Impact: 24.6)
  * `doneTest` (Impact: 2.8)
  * `onSlide2` (Impact: 2.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Amplified Race Conditions:* 26 instances
* *Amplified Cascading Flux:* 30 instances
* *High Risk Execution (weighted view):* 58
* *Concurrency (weighted view):* 166
* *State Mutation (weighted view):* 160
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 388`, `args: 143`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 63`, `state_mutation: 100`, `unreferenced_by_name: 2`
* *Architecture:* `concurrency: 36`, `import: 5`
* *Defense:* `safety: 5`, `test: 215`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.978
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` carousel.js, event-handler.js, index.js, swipe.js, fixture.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/tests/unit/modal.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 479.7 | **LOC:** 1330 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.6246%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `expectedDone` (Impact: 19.1)
  * `shownCallback` (Impact: 15.7)
  * `showListener` (Impact: 12.3)
  * `hideCallback` (Impact: 10.9)
  * `hideListener` (Impact: 9.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 39 instances
* *Amplified Cascading Flux:* 21 instances
* *Concurrency (weighted view):* 250
* *State Mutation (weighted view):* 121
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 373`, `args: 205`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 57`, `state_mutation: 79`, `unreferenced_by_name: 3`
* *Architecture:* `concurrency: 55`, `import: 4`
* *Defense:* `test: 184`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.978
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` event-handler.js, modal.js, scrollbar.js, fixture.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/tests/unit/tab.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 326.12 | **LOC:** 1253 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.0935%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `expectDone` (Impact: 61.2)
  * `expectDone` (Impact: 7.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 20 instances
* *Amplified Cascading Flux:* 20 instances
* *Concurrency (weighted view):* 128
* *State Mutation (weighted view):* 109
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 367`, `args: 123`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 46`, `state_mutation: 69`
* *Architecture:* `concurrency: 28`, `import: 2`
* *Defense:* `test: 179`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.978
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` tab.js, fixture.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/tests/unit/offcanvas.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 293.96 | **LOC:** 915 | **CtrlFlow:** 3.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.0708%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `expectEnd` (Impact: 22.6)
  * `expectEnd` (Impact: 10.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 22 instances
* *Amplified Cascading Flux:* 22 instances
* *Concurrency (weighted view):* 136
* *State Mutation (weighted view):* 111
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 211`, `args: 132`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 47`, `state_mutation: 67`
* *Architecture:* `concurrency: 26`, `import: 5`
* *Defense:* `test: 165`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.978
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` event-handler.js, offcanvas.js, index.js, scrollbar.js, fixture.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/src/tooltip.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 287.66 | **LOC:** 634 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.2128%), Tech Debt (11.6674%)
**Top Internal Functions/Classes:**
  * `show` (Impact: 13.8)
  * `_setListeners` (Impact: 13.1)
  * `hide` (Impact: 9.1)
  * `_configAfterMerge` (Impact: 8.1)
  * `_getConfig` (Impact: 8.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 34 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 111
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 62`, `args: 49`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `state_mutation: 43`, `dead_code: 1`, `planned_debt: 3`
* *Architecture:* `api: 10`, `concurrency: 1`, `import: 7`
* *Defense:* `safety: 28`, `doc: 4`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.262
  * `Choke Point (Betweenness):` 0.001539 | `Ripple Effect (Closeness):` 0.036994
  * `Imports (Out-Degree: 6):` base-component.js, event-handler.js, manipulator.js, index.js, sanitizer.js, template-factory.js, core
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `js/tests/unit/collapse.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 274.24 | **LOC:** 1063 | **CtrlFlow:** 2.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.4592%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `expectEnd` (Impact: 17.6)
  * `expectEnd` (Impact: 9.1)
  * `target2Shown` (Impact: 9.1)
  * `el` (Impact: 7.3)
  * `handlerNestedCollapseOne` (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 20 instances
* *Amplified Cascading Flux:* 16 instances
* *High Risk Execution (weighted view):* 39
* *Concurrency (weighted view):* 122
* *State Mutation (weighted view):* 86
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 245`, `args: 123`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 40`, `state_mutation: 54`, `unreferenced_by_name: 1`
* *Architecture:* `concurrency: 22`, `import: 3`
* *Defense:* `safety: 1`, `test: 182`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.978
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` collapse.js, event-handler.js, fixture.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/src/dom/event-handler.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 245.12 | **LOC:** 318 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.5932%), Tech Debt (12.1177%)
**Top Internal Functions/Classes:**
  * `addHandler` (Impact: 34.0)
  * `off` (Impact: 28.6)
  * `trigger` (Impact: 19.9)
  * `wrapFunction` (Impact: 15.8)
  * `bootstrapDelegationHandler` (Impact: 13.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 55
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 35`, `args: 21`, `func_start: 19`
* *Risk/State:* `state_mutation: 19`, `planned_debt: 1`
* *Architecture:* `api: 6`, `import: 1`
* *Defense:* `safety: 19`, `doc: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 41.137
  * `Choke Point (Betweenness):` 9e-05 | `Ripple Effect (Closeness):` 0.176668
  * `Imports (Out-Degree: 1):` index.js
  * `Imported By (In-Degree: 28):` (Excluded from Brief to save tokens)

### `js/tests/unit/scrollspy.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 223.3 | **LOC:** 981 | **CtrlFlow:** 2.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.7509%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `expectToBeCloseToArray` (Impact: 18.7)
    * *Intent:* // See https://stackoverflow.com/a/45592926
  * `testElementIsActiveAfterScroll` (Impact: 12.9)
  * `active` (Impact: 4.3)
  * `activeId` (Impact: 3.6)
  * `getElementScrollSpy` (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 11 instances
* *Amplified Cascading Flux:* 11 instances
* *Concurrency (weighted view):* 69
* *State Mutation (weighted view):* 77
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 221`, `args: 94`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 37`, `state_mutation: 55`, `duplicate_logic: 3`, `unreferenced_by_name: 2`
* *Architecture:* `concurrency: 14`, `import: 3`
* *Defense:* `safety: 2`, `test: 122`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.978
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` event-handler.js, scrollspy.js, fixture.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/tests/unit/toast.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 204.48 | **LOC:** 673 | **CtrlFlow:** 2.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.8977%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `assertDone` (Impact: 23.5)
  * `expected` (Impact: 8.8)
  * `assertDone` (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 15 instances
* *Amplified Cascading Flux:* 10 instances
* *Concurrency (weighted view):* 98
* *State Mutation (weighted view):* 59
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 154`, `args: 97`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 28`, `state_mutation: 39`, `unreferenced_by_name: 1`
* *Architecture:* `concurrency: 23`, `import: 2`
* *Defense:* `test: 94`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.978
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` toast.js, fixture.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/src/carousel.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 192.9 | **LOC:** 475 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.3842%), Tech Debt (20.0913%)
**Top Internal Functions/Classes:**
  * `_slide` (Impact: 20.9)
  * `triggerEvent` (Impact: 10.5)
  * `to` (Impact: 9.5)
  * `jQueryInterface` (Impact: 9.4)
    * *Intent:* // Static
  * `_directionToOrder` (Impact: 6.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 9 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 38
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 56`, `args: 43`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `state_mutation: 20`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `api: 7`, `concurrency: 2`, `import: 6`
* *Defense:* `safety: 17`, `doc: 5`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.218
  * `Choke Point (Betweenness):` 0.000265 | `Ripple Effect (Closeness):` 0.017341
  * `Imports (Out-Degree: 6):` base-component.js, event-handler.js, manipulator.js, selector-engine.js, index.js, swipe.js
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `js/tests/unit/dom/event-handler.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 179.64 | **LOC:** 481 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.1645%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handler` (Impact: 11.8)
  * `handler` (Impact: 4.1)
  * `moveMouse` (Impact: 3.8)
  * `handler` (Impact: 2.2)
  * `oneListener` (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 105
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 108`, `args: 73`, `func_start: 7`
* *Risk/State:* `high_risk_execution: 17`, `state_mutation: 32`, `duplicate_logic: 2`, `unreferenced_by_name: 2`
* *Architecture:* `concurrency: 25`, `import: 3`
* *Defense:* `test: 59`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.978
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` event-handler.js, index.js, fixture.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/src/dropdown.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 172.18 | **LOC:** 456 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (19.9896%), Tech Debt (13.9901%)
**Top Internal Functions/Classes:**
  * `clearMenus` (Impact: 25.9)
  * `dataApiKeydownHandler` (Impact: 16.1)
  * `_getPlacement` (Impact: 9.4)
  * `show` (Impact: 8.7)
  * `_completeHide` (Impact: 8.3)
    * *Intent:* // Private
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 47`, `args: 26`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `state_mutation: 15`, `dead_code: 1`, `planned_debt: 3`
* *Architecture:* `api: 6`, `import: 6`
* *Defense:* `safety: 31`, `doc: 5`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.387
  * `Choke Point (Betweenness):` 0.000228 | `Ripple Effect (Closeness):` 0.017341
  * `Imports (Out-Degree: 5):` base-component.js, event-handler.js, manipulator.js, selector-engine.js, index.js, core
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `js/tests/visual/dropdown.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 169.33 | **LOC:** 206 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 75`, `args: 38`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `io: 62`, `api: 6`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.978
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` bootstrap.min.css, bootstrap.bundle.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/tests/unit/util/index.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 162.0 | **LOC:** 721 | **CtrlFlow:** 7.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (26.7041%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `el` (Impact: 28.3)
  * `functionBar` (Impact: 20.6)
  * `el` (Impact: 3.9)
  * `functionFoo` (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 21 instances
* *High Risk Execution (weighted view):* 25
* *Concurrency (weighted view):* 21
* *State Mutation (weighted view):* 75
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 156`, `args: 93`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 27`, `state_mutation: 33`, `unreferenced_by_name: 2`
* *Architecture:* `concurrency: 11`, `import: 3`
* *Defense:* `safety: 1`, `test: 182`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.978
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` index.js, fixture.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/src/util/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 155.34 | **LOC:** 307 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.4081%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parseSelector` (Impact: 31.0)
    * *Intent:* /** * Properly escape IDs selectors to handle weird IDs * @param {string} selector * @returns {strin...
  * `getNextActiveElement` (Impact: 15.4)
    * *Intent:* /** * Return the previous/next element of a list. * * @param {array} list The list of elements * @pa...
  * `isVisible` (Impact: 12.7)
  * `findShadowRoot` (Impact: 9.7)
  * `isDisabled` (Impact: 9.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 63`, `args: 25`, `func_start: 21`
* *Risk/State:* `state_mutation: 13`, `dead_code: 1`
* *Architecture:* `api: 4`, `concurrency: 1`
* *Defense:* `safety: 29`, `doc: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 105.611
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.208815
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 31):` (Excluded from Brief to save tokens)

### `js/src/scrollspy.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 150.88 | **LOC:** 297 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (31.8774%), Tech Debt (24.0131%)
**Top Internal Functions/Classes:**
  * `_observerCallback` (Impact: 14.6)
    * *Intent:* // The logic of selection
  * `activate` (Impact: 14.5)
  * `jQueryInterface` (Impact: 7.8)
    * *Intent:* // Static
  * `_activateParents` (Impact: 6.5)
  * `_configAfterMerge` (Impact: 6.3)
    * *Intent:* // Private
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 58
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 30`, `args: 22`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `state_mutation: 22`, `dead_code: 3`, `planned_debt: 4`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* `safety: 8`, `doc: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.669
  * `Choke Point (Betweenness):` 0.000222 | `Ripple Effect (Closeness):` 0.017341
  * `Imports (Out-Degree: 4):` base-component.js, event-handler.js, selector-engine.js, index.js
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `js/src/modal.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 132.76 | **LOC:** 379 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.2116%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_addEventListeners` (Impact: 10.9)
  * `_adjustDialog` (Impact: 7.8)
    * *Intent:* /** * The following methods are used to handle overflowing modals */
  * `_showElement` (Impact: 7.4)
  * `show` (Impact: 6.9)
  * `_triggerBackdropTransition` (Impact: 6.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 45`, `args: 33`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `state_mutation: 25`, `dead_code: 1`
* *Architecture:* `api: 6`, `import: 8`
* *Defense:* `safety: 9`, `doc: 6`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.472
  * `Choke Point (Betweenness):` 0.000676 | `Ripple Effect (Closeness):` 0.024085
  * `Imports (Out-Degree: 8):` base-component.js, event-handler.js, selector-engine.js, backdrop.js, component-functions.js, focustrap.js, index.js, scrollbar.js
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `js/tests/unit/popover.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 132.36 | **LOC:** 512 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.4522%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `content` (Impact: 2.1)
  * `title` (Impact: 1.6)
  * `content` (Impact: 1.6)
  * `title` (Impact: 1.1)
  * `title` (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 72
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 116`, `args: 80`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 25`, `state_mutation: 38`
* *Architecture:* `concurrency: 12`, `import: 3`
* *Defense:* `test: 106`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.978
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` event-handler.js, popover.js, fixture.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/tests/unit/util/scrollbar.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 117.72 | **LOC:** 364 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (52.4309%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `isScrollBarHidden` (Impact: 23.4)
    * *Intent:* // iOS, Android devices and macOS browsers hide scrollbar by default and show it only while scrollin...
  * `hasMarginAttr` (Impact: 7.8)
  * `windowCalculations` (Impact: 1.8)
  * `parseIntDecimal` (Impact: 1.5)
  * `getPaddingX` (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 67
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 53`, `args: 34`, `func_start: 11`
* *Risk/State:* `high_risk_execution: 11`, `state_mutation: 35`, `unreferenced_by_name: 2`
* *Architecture:* `import: 3`
* *Defense:* `safety: 3`, `test: 76`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.978
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` manipulator.js, scrollbar.js, fixture.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/src/collapse.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 111.34 | **LOC:** 298 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.0424%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 11.8)
  * `show` (Impact: 10.7)
  * `hide` (Impact: 9.0)
  * `jQueryInterface` (Impact: 8.0)
    * *Intent:* // Static
  * `_addAriaAndCollapsedClass` (Impact: 5.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 30`, `args: 22`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `state_mutation: 20`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* `safety: 11`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.669
  * `Choke Point (Betweenness):` 0.000222 | `Ripple Effect (Closeness):` 0.017341
  * `Imports (Out-Degree: 4):` base-component.js, event-handler.js, selector-engine.js, index.js
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `js/src/tab.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 108.68 | **LOC:** 316 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.5063%), Tech Debt (15.6799%)
**Top Internal Functions/Classes:**
  * `_keydown` (Impact: 9.6)
  * `jQueryInterface` (Impact: 7.8)
    * *Intent:* // Static
  * `show` (Impact: 7.1)
    * *Intent:* // Public
  * `_activate` (Impact: 6.4)
    * *Intent:* // Private
  * `_deactivate` (Impact: 6.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 35`, `args: 26`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `state_mutation: 6`, `planned_debt: 2`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `safety: 8`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.232
  * `Choke Point (Betweenness):` 0.000273 | `Ripple Effect (Closeness):` 0.017341
  * `Imports (Out-Degree: 4):` base-component.js, event-handler.js, selector-engine.js, index.js
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `js/tests/unit/dom/selector-engine.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 88.16 | **LOC:** 415 | **CtrlFlow:** 4.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.695%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 67
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 103`, `args: 48`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 34`, `state_mutation: 39`
* *Architecture:* `import: 2`
* *Defense:* `test: 82`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.978
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` selector-engine.js, fixture.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/tests/visual/carousel.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 84.68 | **LOC:** 66 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 20`, `args: 24`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `io: 8`, `api: 2`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.978
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` bootstrap.min.css, bootstrap.bundle.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `js/src/base-component.js` -> **Severity: 0.23** (Bridge: 0.0023 * Flux: 99.9977%)
- `js/src/tooltip.js` -> **Severity: 0.154** (Bridge: 0.0015 * Flux: 99.9077%)
- `js/src/modal.js` -> **Severity: 0.067** (Bridge: 0.0007 * Flux: 99.4578%)
- `js/src/offcanvas.js` -> **Severity: 0.046** (Bridge: 0.0007 * Flux: 69.3404%)
- `js/src/util/template-factory.js` -> **Severity: 0.043** (Bridge: 0.0004 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `js/tests/helpers/fixture.js` -> **Severity: 12.934** (Embedded: 0.1445 * Error Risk: 89.4999%)
- `js/src/dom/event-handler.js` -> **Severity: 11.059** (Embedded: 0.1767 * Error Risk: 62.5964%)
- `js/src/base-component.js` -> **Severity: 8.959** (Embedded: 0.1089 * Error Risk: 82.2493%)
- `js/src/dom/selector-engine.js` -> **Severity: 8.476** (Embedded: 0.1118 * Error Risk: 75.8103%)
- `js/src/util/index.js` -> **Severity: 7.799** (Embedded: 0.2088 * Error Risk: 37.3498%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `js/src/util/index.js` -> **Severity: 6864.715** (Blast Radius: 105.611 * Doc Risk: 65.0%)
- `js/src/dom/event-handler.js` -> **Severity: 3981.0** (Blast Radius: 41.137 * Doc Risk: 96.7742%)
- `js/tests/helpers/fixture.js` -> **Severity: 3463.3** (Blast Radius: 34.633 * Doc Risk: 100.0%)
- `js/src/dom/selector-engine.js` -> **Severity: 2087.035** (Blast Radius: 21.819 * Doc Risk: 95.6522%)
- `js/src/dom/manipulator.js` -> **Severity: 1818.09** (Blast Radius: 20.201 * Doc Risk: 90.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
