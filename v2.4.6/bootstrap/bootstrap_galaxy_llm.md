# ARCHITECTURAL_BRIEF: bootstrap
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_web/bootstrap` |
| **Timestamp** | `2026-08-03T20:00:54.887016+00:00` |
| **Scan Duration** | `0.68s` |
| **Git Branch** | `main` |
| **Git Commit** | `060ff24924a2be67feb309b121b32559a549d02c` |
| **Git Remote** | `https://github.com/twbs/bootstrap.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 37 malicious artifacts.

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
| Total Artifacts | 790 |
| Analyzed Artifacts (Scanned) | 141 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 649 |
| Total LOC | 9956 |
| Volatility Index | 0.007 |
| % Scanned of codebase = | 17.8% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.42 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1667 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.8 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CSS | 91 | 5995 | 64.5% |
| JAVASCRIPT | 37 | 3418 | 26.2% |
| HTML | 6 | 466 | 4.3% |
| MARKDOWN | 4 | 0 | 2.8% |
| JSON | 1 | 32 | 0.7% |
| YAML | 1 | 45 | 0.7% |
| PLAINTEXT | 1 | 0 | 0.7% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.906`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 112 | 79.4% |
| file_cluster_13 | 18 | 12.8% |
| file_cluster_0 | 3 | 2.1% |
| file_cluster_17 | 2 | 1.4% |
| file_cluster_2 | 1 | 0.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 5 | 3.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 649*

**Composition by Extension & Reason:**
- `.png`: 111x Excluded (Explicitly Denied Extension: '.png')
- `.mdx`: 110x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.astro`: 104x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 79x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.map`: 48x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.css`: 47x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 32x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.scss`: 31x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 20135 LOC)
- `.mjs`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 2x Excluded (Saturation: Line 41 exceeds 500 chars), 1x Excluded (Saturation: Line 31 exceeds 500 chars), 1x Excluded (Saturation: Line 32 exceeds 500 chars)
- `.svg`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 74.7 | 12.8 | 6.1 | 5.0 |
| Error & Exception Exposure | 0.0 | 88.6 | 8.7 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 10.3 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 8.7 | 2.3 | 2.3 |
| API Exposure | 0.0 | 16.8 | 1.8 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 70.2 | 0.8 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 15.4 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 11.7 | 0.3 | 0.0 | 0.0 |
| Specification Exposure | 13.3 | 100.0 | 88.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 4.3 | 0.2 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 21.9 | 0.4 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 37.9 | 26.7 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 6.7 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 1.5 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `js/tests/visual/dropdown.html` (Hits: 61)
- `js/tests/visual/carousel.html` (Hits: 7)
- `scss/tests/sass-true/runner.js` (Hits: 6)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **tooltip.js** (`js/src/tooltip.js`) — 2 inbound connections
2. **modal.js** (`js/src/modal.js`) — 1 inbound connections
3. **offcanvas.js** (`js/src/offcanvas.js`) — 1 inbound connections
4. **backdrop.js** (`js/src/util/backdrop.js`) — 1 inbound connections
5. **CODE_OF_CONDUCT.md** (`CODE_OF_CONDUCT.md`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **bootstrap.scss** (`scss/bootstrap.scss`) — 40 outbound dependencies
2. **_mixins.scss** (`scss/_mixins.scss`) — 25 outbound dependencies
3. **bootstrap-grid.scss** (`scss/bootstrap-grid.scss`) — 14 outbound dependencies
4. **index.esm.js** (`js/index.esm.js`) — 12 outbound dependencies
5. **index.umd.js** (`js/index.umd.js`) — 12 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `parseSelector` (@ `js/src/util/index.js`) -> Impact: **140.7** | LOC: 181
  * *Intent:* /** * -------------------------------------------------------------------------- * Bootstrap util/index.js * Licensed under MIT (https://github.com/tw...
- `addHandler` (@ `js/src/dom/event-handler.js`) -> Impact: **50.0** | LOC: 44
- `show` (@ `js/src/tooltip.js`) -> Impact: **47.3** | LOC: 40
- `off` (@ `js/src/dom/event-handler.js`) -> Impact: **42.0** | LOC: 35
- `trigger` (@ `js/src/dom/event-handler.js`) -> Impact: **38.0** | LOC: 39
- `clearMenus` (@ `js/src/dropdown.js`) -> Impact: **37.8** | LOC: 29
- `_onInteraction` (@ `js/src/toast.js`) -> Impact: **35.3** | LOC: 31
- `sanitizeHtml` (@ `js/src/util/sanitizer.js`) -> Impact: **34.6** | LOC: 33
- `_setListeners` (@ `js/src/tooltip.js`) -> Impact: **33.2** | LOC: 41
- `dataApiKeydownHandler` (@ `js/src/dropdown.js`) -> Impact: **28.0** | LOC: 40

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `show` (@ `js/src/tooltip.js`) -> **O(2^N) [Recursive]**
- `next` (@ `js/src/dom/selector-engine.js`) -> **O(2^N) [Recursive]**
- `show` (@ `js/src/offcanvas.js`) -> **O(2^N) [Recursive]**
- `hide` (@ `js/src/offcanvas.js`) -> **O(2^N) [Recursive]**
- `_activate` (@ `js/src/tab.js`) -> **O(2^N) [Recursive]**
- `_deactivate` (@ `js/src/tab.js`) -> **O(2^N) [Recursive]**
- `NAME` (@ `js/src/alert.js`) -> **O(2^N) [Recursive]**
- `constructor` (@ `js/src/base-component.js`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * Constants
- `VERSION` (@ `js/src/base-component.js`) -> **O(2^N) [Recursive]**
- `NAME` (@ `js/src/button.js`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `show` (@ `js/src/collapse.js`) -> DB Complexity: **25**
- `hide` (@ `js/src/collapse.js`) -> DB Complexity: **22**
- `show` (@ `js/src/tooltip.js`) -> DB Complexity: **20**
- `_setListeners` (@ `js/src/tooltip.js`) -> DB Complexity: **20**
- `_showElement` (@ `js/src/modal.js`) -> DB Complexity: **18**
- `show` (@ `js/src/offcanvas.js`) -> DB Complexity: **18**
- `_addEventListeners` (@ `js/src/modal.js`) -> DB Complexity: **15**
- `hide` (@ `js/src/offcanvas.js`) -> DB Complexity: **15**
- `show` (@ `js/src/toast.js`) -> DB Complexity: **15**
- `constructor` (@ `js/src/tooltip.js`) -> DB Complexity: **14**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `js/src` | 13 | 2207.92 | 43.74% | 10.77% |
| `js/src/util` | 9 | 797.7 | 38.59% | 5.07% |
| `js/src/dom` | 4 | 425.6 | 38.6% | 8.08% |
| `js/tests/visual` | 6 | 122.32 | 1.03% | 0.0% |
| `js/tests` | 3 | 70.02 | 4.2% | 0.0% |
| `__monolith__` | 7 | 59.64 | 2.55% | 0.0% |
| `js` | 2 | 43.76 | 7.4% | 0.0% |
| `scss` | 42 | 33.86 | 5.01% | 11.67% |
| `js/tests/integration` | 2 | 30.38 | 5.0% | 0.0% |
| `js/tests/helpers` | 1 | 26.16 | 48.36% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `scss/helpers/_color-bg.scss` -> **100.0%** Exposure
- `scss/mixins/_breakpoints.scss` -> **100.0%** Exposure
- `scss/mixins/_color-mode.scss` -> **100.0%** Exposure
- `scss/mixins/_color-scheme.scss` -> **100.0%** Exposure
- `scss/_placeholders.scss` -> **99.9997%** Exposure
### Highest State Flux (Mutation/Volatility)
- `js/src/base-component.js` -> **100.0%** Exposure
- `js/src/collapse.js` -> **100.0%** Exposure
- `js/src/modal.js` -> **100.0%** Exposure
- `js/src/offcanvas.js` -> **100.0%** Exposure
- `js/src/scrollspy.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `js/tests/helpers/fixture.js` -> **4** Orphaned Functions | **0** Duplicates
- `scss/mixins/_breakpoints.scss` -> **0** Orphaned Functions | **4** Duplicates
- `scss/_spinners.scss` -> **1** Orphaned Functions | **2** Duplicates
- `js/tests/karma.conf.js` -> **2** Orphaned Functions | **0** Duplicates
- `scss/_placeholders.scss` -> **0** Orphaned Functions | **2** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`js/tests/karma.conf.js`** -> AI Confidence: **99.39%**
2. **`js/index.esm.js`** -> AI Confidence: **99.31%**
3. **`js/src/tooltip.js`** -> AI Confidence: **99.31%**
4. **`js/src/offcanvas.js`** -> AI Confidence: **99.24%**
5. **`js/src/modal.js`** -> AI Confidence: **99.15%**
6. **`js/src/dropdown.js`** -> AI Confidence: **99.13%**
7. **`js/index.umd.js`** -> AI Confidence: **99.09%**
8. **`js/src/collapse.js`** -> AI Confidence: **99.06%**
9. **`js/src/dom/data.js`** -> AI Confidence: **99.06%**
10. **`js/src/dom/event-handler.js`** -> AI Confidence: **99.06%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `js/src/tooltip.js` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `js/src/util/backdrop.js` -> **100.0%** Exposure
- `js/src/util/template-factory.js` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `js/src/collapse.js` -> **100.0%** Exposure
- `js/src/modal.js` -> **100.0%** Exposure
- `js/src/offcanvas.js` -> **100.0%** Exposure
- `js/src/tooltip.js` -> **100.0%** Exposure
- `js/src/util/backdrop.js` -> **99.9976%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `134` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `js/src/tooltip.js` (JAVASCRIPT) -> Cumulative Risk: **702.23**
- **Archetype:** `file_cluster_13` (Distance: 13.927 IQR)
- **Magnitude:** 475.36 | **LOC:** 634 | **CtrlFlow:** 54.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `show` (Impact: 47.3), `_setListeners` (Impact: 33.2), `_configAfterMerge` (Impact: 11.6)

### 2. `js/src/toast.js` (JAVASCRIPT) -> Cumulative Risk: **570.73**
- **Archetype:** `file_cluster_13` (Distance: 13.232 IQR)
- **Magnitude:** 209.46 | **LOC:** 225 | **CtrlFlow:** 45.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (83.7346%), Verification (80.0%)
- **Heaviest Functions:** `_onInteraction` (Impact: 35.3), `jQueryInterface` (Impact: 8.4), `_maybeScheduleHide` (Impact: 6.3)

### 3. `js/src/util/backdrop.js` (JAVASCRIPT) -> Cumulative Risk: **568.77**
- **Archetype:** `file_cluster_13` (Distance: 12.991 IQR)
- **Magnitude:** 121.18 | **LOC:** 152 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Injection Surface (100.0%), Algorithmic Dos (99.9976%)
- **Heaviest Functions:** `_getElement` (Impact: 7.0), `show` (Impact: 5.2), `Default` (Impact: 4.2)

### 4. `js/src/util/template-factory.js` (JAVASCRIPT) -> Cumulative Risk: **564.26**
- **Archetype:** `file_cluster_8` (Distance: 11.563 IQR)
- **Magnitude:** 108.44 | **LOC:** 161 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Injection Surface (100.0%), Verification (80.0%)
- **Heaviest Functions:** `_setContent` (Impact: 11.3), `toHtml` (Impact: 5.1), `Default` (Impact: 4.2)

### 5. `js/src/modal.js` (JAVASCRIPT) -> Cumulative Risk: **557.76**
- **Archetype:** `file_cluster_13` (Distance: 13.029 IQR)
- **Magnitude:** 271.0 | **LOC:** 379 | **CtrlFlow:** 36.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Safety Score (80.4239%)
- **Heaviest Functions:** `_addEventListeners` (Impact: 21.0), `show` (Impact: 12.5), `_showElement` (Impact: 10.2)

### 6. `js/src/collapse.js` (JAVASCRIPT) -> Cumulative Risk: **526.85**
- **Archetype:** `file_cluster_17` (Distance: 13.379 IQR)
- **Magnitude:** 275.04 | **LOC:** 298 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Verification (80.0%)
- **Heaviest Functions:** `show` (Impact: 19.7), `constructor` (Impact: 17.0), `hide` (Impact: 16.8)

### 7. `js/src/offcanvas.js` (JAVASCRIPT) -> Cumulative Risk: **507.78**
- **Archetype:** `file_cluster_13` (Distance: 12.957 IQR)
- **Magnitude:** 239.38 | **LOC:** 283 | **CtrlFlow:** 40.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Verification (80.0%)
- **Heaviest Functions:** `show` (Impact: 27.2), `hide` (Impact: 18.5), `jQueryInterface` (Impact: 13.7)

### 8. `js/src/tab.js` (JAVASCRIPT) -> Cumulative Risk: **484.11**
- **Archetype:** `file_cluster_8` (Distance: 12.443 IQR)
- **Magnitude:** 222.48 | **LOC:** 316 | **CtrlFlow:** 49.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9997%), Algorithmic Dos (89.0261%), Verification (80.0%)
- **Heaviest Functions:** `_activate` (Impact: 16.8), `_deactivate` (Impact: 16.8), `jQueryInterface` (Impact: 13.7)

### 9. `js/src/dom/selector-engine.js` (JAVASCRIPT) -> Cumulative Risk: **478.15**
- **Archetype:** `file_cluster_8` (Distance: 11.019 IQR)
- **Magnitude:** 102.88 | **LOC:** 127 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.7655%), Verification (80.0%), Documentation (69.6657%)
- **Heaviest Functions:** `getSelector` (Impact: 20.3), `next` (Impact: 16.2), `prev` (Impact: 8.4)

### 10. `js/src/util/swipe.js` (JAVASCRIPT) -> Cumulative Risk: **451.71**
- **Archetype:** `file_cluster_13` (Distance: 13.228 IQR)
- **Magnitude:** 157.8 | **LOC:** 147 | **CtrlFlow:** 43.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (88.6402%), Verification (80.0%)
- **Heaviest Functions:** `_handleSwipe` (Impact: 6.5), `constructor` (Impact: 5.8), `_start` (Impact: 4.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `js/src/tooltip.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.927 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.912 IQR)
- **Top Global Matches:** file_cluster_13: 13.927, file_cluster_11: 14.017, file_cluster_8: 14.095
- **Magnitude:** 475.36 | **LOC:** 634 | **CtrlFlow:** 54.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (62.5631%), Tech Debt (10.1514%)
**Top Internal Functions/Classes:**
  * `show` (Impact: 47.3 | O(2^N) | DB: 20)
  * `_setListeners` (Impact: 33.2 | O(N^3) | DB: 20)
  * `_configAfterMerge` (Impact: 11.6 | O(N^2))
  * `_getConfig` (Impact: 11.5 | O(N^2) | DB: 4)
  * `_enter` (Impact: 9.2 | O(N^2) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 39`, `args: 28`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `state_mutation: 271`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 7`, `concurrency: 6`, `import: 7`
* *Defense:* `safety: 23`, `doc: 4`, `immutability_locks: 43`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 14.861
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.014286
  * `Imports (Out-Degree: 0):` manipulator.js, index.js, event-handler.js, sanitizer.js, base-component.js, template-factory.js, core
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `js/src/collapse.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.379 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.745 IQR)
- **Top Global Matches:** file_cluster_17: 13.379, file_cluster_8: 13.439, file_cluster_13: 13.462
- **Magnitude:** 275.04 | **LOC:** 298 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (53.3292%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `show` (Impact: 19.7 | O(N^2) | DB: 25)
  * `constructor` (Impact: 17.0 | O(N^2) | DB: 12)
  * `hide` (Impact: 16.8 | O(N^2) | DB: 22)
  * `jQueryInterface` (Impact: 13.9 | O(N^2) | DB: 1)
  * `_initializeChildren` (Impact: 9.2 | O(N^2) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 30`, `args: 22`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `state_mutation: 159`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* `safety: 11`, `doc: 5`, `immutability_locks: 44`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.966
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` base-component.js, event-handler.js, index.js, selector-engine.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/src/modal.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.029 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.554 IQR)
- **Top Global Matches:** file_cluster_13: 13.029, file_cluster_8: 13.266, file_cluster_11: 13.278
- **Magnitude:** 271.0 | **LOC:** 379 | **CtrlFlow:** 36.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (72.2094%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_addEventListeners` (Impact: 21.0 | O(N^2) | DB: 15)
  * `show` (Impact: 12.5 | O(2^N) | DB: 10)
  * `_showElement` (Impact: 10.2 | O(N^2) | DB: 18)
  * `hide` (Impact: 6.6 | O(N^1) | DB: 11)
  * `Default` (Impact: 4.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 40`, `args: 26`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `state_mutation: 180`, `dead_code: 1`
* *Architecture:* `api: 3`, `import: 8`
* *Defense:* `safety: 4`, `doc: 4`, `immutability_locks: 34`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.94
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.007143
  * `Imports (Out-Degree: 0):` backdrop.js, focustrap.js, index.js, scrollbar.js, event-handler.js, selector-engine.js, component-functions.js, base-component.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/src/offcanvas.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.957 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.017 IQR)
- **Top Global Matches:** file_cluster_13: 12.957, file_cluster_8: 13.105, file_cluster_17: 13.296
- **Magnitude:** 239.38 | **LOC:** 283 | **CtrlFlow:** 40.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (50.1039%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `show` (Impact: 27.2 | O(2^N) | DB: 18)
  * `hide` (Impact: 18.5 | O(2^N) | DB: 15)
  * `jQueryInterface` (Impact: 13.7 | O(N^2) | DB: 1)
  * `_initializeBackDrop` (Impact: 7.4 | O(N^2) | DB: 5)
  * `_addEventListeners` (Impact: 7.1 | O(N^2) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 38`, `args: 21`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `state_mutation: 137`
* *Architecture:* `api: 2`, `import: 8`
* *Defense:* `safety: 8`, `doc: 5`, `immutability_locks: 34`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.94
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.007143
  * `Imports (Out-Degree: 0):` backdrop.js, focustrap.js, index.js, scrollbar.js, event-handler.js, selector-engine.js, component-functions.js, base-component.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/src/dom/event-handler.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.732 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.335 IQR)
- **Top Global Matches:** file_cluster_8: 10.732, file_cluster_13: 11.308, file_cluster_7: 11.315
- **Magnitude:** 236.42 | **LOC:** 318 | **CtrlFlow:** 62.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (25.6868%), Tech Debt (11.0557%)
**Top Internal Functions/Classes:**
  * `addHandler` (Impact: 50.0 | O(N^2) | DB: 1)
  * `off` (Impact: 42.0 | O(N^2))
  * `trigger` (Impact: 38.0 | O(2^N) | DB: 4)
  * `bootstrapDelegationHandler` (Impact: 22.1 | O(N^2) | DB: 1)
  * `removeNamespacedHandlers` (Impact: 9.4 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 34`, `args: 21`, `func_start: 29`
* *Risk/State:* `state_mutation: 24`, `planned_debt: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 19`, `doc: 3`, `immutability_locks: 34`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.966
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/src/tab.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.443 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.675 IQR)
- **Top Global Matches:** file_cluster_8: 12.443, file_cluster_13: 12.555, file_cluster_17: 12.664
- **Magnitude:** 222.48 | **LOC:** 316 | **CtrlFlow:** 49.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (50.4349%), Tech Debt (14.1965%)
**Top Internal Functions/Classes:**
  * `_activate` (Impact: 16.8 | O(2^N) | DB: 5)
  * `_deactivate` (Impact: 16.8 | O(2^N) | DB: 3)
  * `jQueryInterface` (Impact: 13.7 | O(N^2) | DB: 1)
  * `show` (Impact: 9.6 | O(N^1) | DB: 5)
  * `_keydown` (Impact: 9.6 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 35`, `args: 26`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `state_mutation: 103`, `planned_debt: 2`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `safety: 8`, `doc: 6`, `immutability_locks: 46`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.966
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` base-component.js, event-handler.js, index.js, selector-engine.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/src/toast.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.232 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.044 IQR)
- **Top Global Matches:** file_cluster_13: 13.232, file_cluster_8: 13.315, file_cluster_4: 13.4
- **Magnitude:** 209.46 | **LOC:** 225 | **CtrlFlow:** 45.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (51.8988%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_onInteraction` (Impact: 35.3 | O(N^2) | DB: 6)
  * `jQueryInterface` (Impact: 8.4 | O(N^2) | DB: 1)
  * `_maybeScheduleHide` (Impact: 6.3 | O(N^1) | DB: 6)
  * `dispose` (Impact: 6.1 | O(2^N) | DB: 3)
  * `show` (Impact: 5.5 | O(N^1) | DB: 15)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 28`, `args: 21`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `state_mutation: 111`
* *Architecture:* `api: 3`, `concurrency: 6`, `import: 4`
* *Defense:* `safety: 5`, `doc: 8`, `immutability_locks: 23`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.966
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` base-component.js, event-handler.js, index.js, component-functions.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/src/dropdown.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.058 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.178 IQR)
- **Top Global Matches:** file_cluster_13: 12.058, file_cluster_8: 12.118, file_cluster_11: 12.336
- **Magnitude:** 166.0 | **LOC:** 456 | **CtrlFlow:** 62.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (45.7331%), Tech Debt (15.8869%)
**Top Internal Functions/Classes:**
  * `clearMenus` (Impact: 37.8 | O(N^2))
  * `dataApiKeydownHandler` (Impact: 28.0 | O(N^2) | DB: 1)
  * `jQueryInterface` (Impact: 8.5 | O(N^2) | DB: 1)
  * `show` (Impact: 6.8 | O(N^1) | DB: 5)
  * `constructor` (Impact: 5.7 | O(N^1) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 22`, `args: 11`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 57`, `planned_debt: 2`
* *Architecture:* `api: 3`, `import: 6`
* *Defense:* `safety: 12`, `doc: 5`, `immutability_locks: 51`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.966
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` manipulator.js, index.js, event-handler.js, selector-engine.js, base-component.js, core
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/src/util/swipe.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.228 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.749 IQR)
- **Top Global Matches:** file_cluster_13: 13.228, file_cluster_8: 13.341, file_cluster_1: 13.588
- **Magnitude:** 157.8 | **LOC:** 147 | **CtrlFlow:** 43.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (52.6147%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_handleSwipe` (Impact: 6.5 | O(N^1) | DB: 5)
  * `constructor` (Impact: 5.8 | O(N^1) | DB: 6)
  * `_start` (Impact: 4.8 | O(N^1) | DB: 4)
  * `_initEvents` (Impact: 4.8 | O(N^1) | DB: 13)
  * `_move` (Impact: 4.5 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 21`, `args: 17`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `state_mutation: 101`
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* `safety: 2`, `doc: 3`, `immutability_locks: 15`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.966
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.js, config.js, event-handler.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/src/util/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.556 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.005 IQR)
- **Top Global Matches:** file_cluster_8: 11.556, file_cluster_17: 11.805, file_cluster_15: 11.813
- **Magnitude:** 150.48 | **LOC:** 307 | **CtrlFlow:** 46.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (11.7409%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parseSelector` (Impact: 140.7 | O(2^N) | DB: 5)
    * *Intent:* /** * -------------------------------------------------------------------------- * Bootstrap util/in...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 42`, `args: 13`, `func_start: 12`
* *Risk/State:* `state_mutation: 6`, `dead_code: 1`
* *Architecture:* `io: 1`, `api: 1`
* *Defense:* `safety: 20`, `doc: 12`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.966
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/src/util/backdrop.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.991 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.917 IQR)
- **Top Global Matches:** file_cluster_13: 12.991, file_cluster_8: 13.188, file_cluster_11: 13.279
- **Magnitude:** 121.18 | **LOC:** 152 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (47.1555%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_getElement` (Impact: 7.0 | O(N^2) | DB: 6)
  * `show` (Impact: 5.2 | O(N^1) | DB: 6)
  * `Default` (Impact: 4.2 | O(2^N))
    * *Intent:* /** * Class definition */
  * `DefaultType` (Impact: 4.2 | O(2^N))
  * `NAME` (Impact: 4.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 19`, `args: 14`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `state_mutation: 75`, `dead_code: 1`
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `doc: 3`, `immutability_locks: 9`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 12.888
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.007143
  * `Imports (Out-Degree: 0):` index.js, config.js, event-handler.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/src/scrollspy.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.452 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.444 IQR)
- **Top Global Matches:** file_cluster_13: 12.452, file_cluster_11: 12.636, file_cluster_8: 12.637
- **Magnitude:** 115.66 | **LOC:** 297 | **CtrlFlow:** 41.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (31.4855%), Tech Debt (42.8589%)
**Top Internal Functions/Classes:**
  * `_maybeEnableSmoothScroll` (Impact: 11.9 | O(N^2) | DB: 6)
    * *Intent:* // TODO: v6 Only for backwards compatibility reasons. Use rootMargin only
  * `refresh` (Impact: 6.4 | O(N^1) | DB: 8)
  * `_configAfterMerge` (Impact: 6.3 | O(N^1))
  * `constructor` (Impact: 4.2 | O(N^1) | DB: 9)
  * `Default` (Impact: 4.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 18`, `args: 11`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 66`, `planned_debt: 4`
* *Architecture:* `api: 3`, `import: 4`
* *Defense:* `safety: 3`, `doc: 7`, `immutability_locks: 25`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.966
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` base-component.js, event-handler.js, index.js, selector-engine.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/src/util/template-factory.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.86%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.563 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.743 IQR)
- **Top Global Matches:** file_cluster_8: 11.563, file_cluster_13: 11.609, file_cluster_17: 11.933
- **Magnitude:** 108.44 | **LOC:** 161 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (74.7035%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_setContent` (Impact: 11.3 | O(N^1) | DB: 4)
  * `toHtml` (Impact: 5.1 | O(N^1) | DB: 6)
  * `Default` (Impact: 4.2 | O(2^N))
    * *Intent:* /** * Class definition
  * `DefaultType` (Impact: 4.2 | O(2^N))
  * `NAME` (Impact: 4.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 25`, `args: 15`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 51`
* *Architecture:* `api: 5`, `import: 4`
* *Defense:* `doc: 3`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.966
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.js, sanitizer.js, selector-engine.js, config.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/src/dom/selector-engine.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.019 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.154 IQR)
- **Top Global Matches:** file_cluster_8: 11.019, file_cluster_17: 11.037, file_cluster_13: 11.288
- **Magnitude:** 102.88 | **LOC:** 127 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (66.5404%), Tech Debt (21.2567%)
**Top Internal Functions/Classes:**
  * `getSelector` (Impact: 20.3 | O(N^1) | DB: 2)
    * *Intent:* /** * -------------------------------------------------------------------------- * Bootstrap dom/sel...
  * `next` (Impact: 16.2 | O(2^N) | DB: 1)
  * `prev` (Impact: 8.4 | O(N^2) | DB: 1)
  * `parents` (Impact: 7.5 | O(2^N) | DB: 2)
  * `getSelectorFromElement` (Impact: 4.7 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 27`, `args: 15`, `func_start: 11`
* *Risk/State:* `state_mutation: 21`, `planned_debt: 1`
* *Architecture:* `api: 6`, `import: 1`
* *Defense:* `safety: 2`, `doc: 1`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.966
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/src/util/focustrap.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.247 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.879 IQR)
- **Top Global Matches:** file_cluster_13: 12.247, file_cluster_8: 12.381, file_cluster_1: 12.684
- **Magnitude:** 75.82 | **LOC:** 116 | **CtrlFlow:** 44.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (47.9819%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_handleFocusin` (Impact: 12.2 | O(N^1) | DB: 2)
  * `activate` (Impact: 5.0 | O(N^1) | DB: 6)
  * `_handleKeydown` (Impact: 4.6 | O(N^1) | DB: 1)
  * `Default` (Impact: 4.2 | O(2^N))
    * *Intent:* /** * Class definition */
  * `DefaultType` (Impact: 4.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 16`, `args: 10`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 31`
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `safety: 5`, `doc: 3`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.966
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` config.js, selector-engine.js, event-handler.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/src/base-component.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.986 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.183 IQR)
- **Top Global Matches:** file_cluster_13: 12.986, file_cluster_8: 13.335, file_cluster_7: 13.638
- **Magnitude:** 74.94 | **LOC:** 87 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (44.6354%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 7.6 | O(2^N) | DB: 6)
    * *Intent:* /** * Constants
  * `VERSION` (Impact: 4.2 | O(2^N))
  * `dispose` (Impact: 3.2 | O(N^1) | DB: 4)
  * `_queueCallback` (Impact: 2.1 | O(N^1))
  * `DATA_KEY` (Impact: 2.1 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 16`, `args: 10`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 41`
* *Architecture:* `api: 5`, `import: 4`
* *Defense:* `safety: 2`, `doc: 3`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.966
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` event-handler.js, config.js, data.js, index.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/src/util/scrollbar.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.903 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.436 IQR)
- **Top Global Matches:** file_cluster_13: 11.903, file_cluster_8: 11.951, file_cluster_17: 12.282
- **Magnitude:** 72.72 | **LOC:** 115 | **CtrlFlow:** 31.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (42.996%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_setElementAttributes` (Impact: 9.7 | O(N^2) | DB: 4)
  * `_resetElementAttributes` (Impact: 5.9 | O(N^2) | DB: 1)
  * `_applyManipulationCallback` (Impact: 5.7 | O(N^1) | DB: 1)
  * `_saveInitialAttribute` (Impact: 3.8 | O(N^1))
  * `hide` (Impact: 1.9 | O(N^1) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 15`, `args: 15`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `state_mutation: 31`
* *Architecture:* `api: 5`, `import: 3`
* *Defense:* `safety: 2`, `doc: 3`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.966
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.js, selector-engine.js, manipulator.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/tests/karma.conf.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.169 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 4.315 IQR)
- **Top Global Matches:** file_cluster_8: 10.169, file_cluster_13: 10.274, file_cluster_7: 10.575
- **Magnitude:** 51.02 | **LOC:** 170 | **CtrlFlow:** 72.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (12.6132%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `postDetection` (Impact: 12.3 | O(N^1))
  * `istanbul` (Impact: 1.9 | O(N^2))
  * `exports` (Impact: 1.9 | O(N^1) | DB: 1)
  * `babel` (Impact: 1.8 | O(N^2))
  * `replace` (Impact: 1.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 5`, `args: 2`, `func_start: 6`
* *Risk/State:* `state_mutation: 26`, `orphaned_logic: 2`
* *Architecture:* `io: 3`, `api: 1`, `import: 7`
* *Defense:* `safety: 1`, `doc: 6`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.966
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ip, node:path, plugin-node-resolve, plugin-replace, browsers.js, plugin-babel, rollup-plugin-istanbul
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/src/util/config.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.102 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.373 IQR)
- **Top Global Matches:** file_cluster_13: 12.102, file_cluster_8: 12.257, file_cluster_11: 12.491
- **Magnitude:** 50.76 | **LOC:** 66 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (23.855%), Tech Debt (45.6506%)
**Top Internal Functions/Classes:**
  * `_typeCheckConfig` (Impact: 11.0 | O(N^2) | DB: 2)
  * `_mergeConfigObj` (Impact: 9.2 | O(N^1) | DB: 1)
  * `NAME` (Impact: 8.2 | O(2^N))
  * `Default` (Impact: 2.1 | O(N^1))
  * `DefaultType` (Impact: 2.1 | O(N^1))
    * *Intent:* /** * Class definition */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 9`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 12`, `planned_debt: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `safety: 4`, `doc: 2`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.966
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.js, manipulator.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/src/carousel.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.187 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.904 IQR)
- **Top Global Matches:** file_cluster_8: 10.187, file_cluster_13: 10.227, file_cluster_7: 10.659
- **Magnitude:** 48.66 | **LOC:** 475 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (28.7561%), Tech Debt (56.9001%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 4.3 | O(N^1) | DB: 10)
  * `Default` (Impact: 4.2 | O(2^N))
  * `DefaultType` (Impact: 4.2 | O(2^N))
  * `NAME` (Impact: 4.2 | O(2^N))
  * `nextWhenVisible` (Impact: 2.0 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 15`, `args: 7`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 23`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `api: 3`, `import: 6`
* *Defense:* `safety: 1`, `doc: 4`, `immutability_locks: 38`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.966
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` manipulator.js, index.js, swipe.js, event-handler.js, selector-engine.js, base-component.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/src/dom/data.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.017 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.351 IQR)
- **Top Global Matches:** file_cluster_13: 12.017, file_cluster_8: 12.132, file_cluster_7: 12.454
- **Magnitude:** 46.1 | **LOC:** 56 | **CtrlFlow:** 53.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (36.5529%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `set` (Impact: 16.9 | O(2^N) | DB: 2)
    * *Intent:* /** * -------------------------------------------------------------------------- * Bootstrap dom/dat...
  * `get` (Impact: 10.7 | O(2^N))
    * *Intent:* // eslint-disable-next-line no-console
  * `remove` (Impact: 5.9 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 7`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 10`
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `safety: 2`, `doc: 2`, `immutability_locks: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.966
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/src/popover.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.526 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.568 IQR)
- **Top Global Matches:** file_cluster_8: 11.526, file_cluster_13: 11.535, file_cluster_7: 11.897
- **Magnitude:** 45.56 | **LOC:** 98 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (25.5951%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `jQueryInterface` (Impact: 8.5 | O(N^2) | DB: 1)
  * `Default` (Impact: 4.2 | O(2^N))
  * `DefaultType` (Impact: 4.2 | O(2^N))
    * *Intent:* /**
  * `NAME` (Impact: 4.2 | O(2^N))
  * `_isWithContent` (Impact: 3.0 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 17`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 13`
* *Architecture:* `api: 4`, `import: 2`
* *Defense:* `safety: 4`, `doc: 4`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.966
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` tooltip.js, index.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/src/util/sanitizer.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.797 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.284 IQR)
- **Top Global Matches:** file_cluster_8: 7.797, file_cluster_7: 8.53, file_cluster_1: 8.851
- **Magnitude:** 45.18 | **LOC:** 117 | **CtrlFlow:** 58.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (11.3093%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `sanitizeHtml` (Impact: 34.6 | O(N^2))
  * `allowedAttribute` (Impact: 5.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 12`, `args: 4`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `api: 3`
* *Defense:* `safety: 3`, `doc: 2`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.966
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/src/alert.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.798 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 6.182 IQR)
- **Top Global Matches:** file_cluster_13: 12.798, file_cluster_8: 13.276, file_cluster_11: 13.335
- **Magnitude:** 43.9 | **LOC:** 88 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (41.6009%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `jQueryInterface` (Impact: 13.7 | O(N^2) | DB: 1)
  * `NAME` (Impact: 4.2 | O(2^N))
  * `close` (Impact: 3.4 | O(N^1) | DB: 6)
    * *Intent:* /** * Class definition
  * `_destroyElement` (Impact: 1.7 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 12`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 18`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `safety: 4`, `doc: 5`, `immutability_locks: 10`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.966
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` base-component.js, event-handler.js, index.js, component-functions.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/src/dom/manipulator.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.011 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.44 IQR)
- **Top Global Matches:** file_cluster_8: 11.011, file_cluster_17: 11.369, file_cluster_7: 11.596
- **Magnitude:** 40.2 | **LOC:** 72 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (25.6246%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `normalizeData` (Impact: 16.9 | O(N^1) | DB: 2)
    * *Intent:* /** * --------------------------------------------------------------------------
  * `getDataAttributes` (Impact: 6.5 | O(N^1) | DB: 1)
  * `setDataAttribute` (Impact: 2.1 | O(N^1))
  * `normalizeDataKey` (Impact: 1.9 | O(N^1))
  * `removeDataAttribute` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 15`, `args: 8`, `func_start: 6`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 5`
* *Defense:* `safety: 9`, `doc: 1`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.966
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `js/tests/visual/alert.html` (HTML) | Magnitude: 20.86 | Delta: **0.077 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 39, decorators: 17, structural_boundaries: 13, args: 10
- `js/tests/visual/dropdown.html` (HTML) | Magnitude: 24.88 | Delta: **0.202 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 190, decorators: 125, structural_boundaries: 75, io: 61
- `js/tests/visual/carousel.html` (HTML) | Magnitude: 20.22 | Delta: **0.211 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 55, args: 24, structural_boundaries: 20, decorators: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `js/src/util/scrollbar.js` (JAVASCRIPT) | Magnitude: 72.72 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 66, state_mutation: 31, structural_boundaries: 15, args: 15
- `js/src/dropdown.js` (JAVASCRIPT) | Magnitude: 166.0 | Delta: **0.06 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 123, state_mutation: 57, immutability_locks: 51, branch: 37
- `js/src/toast.js` (JAVASCRIPT) | Magnitude: 209.46 | Delta: **0.083 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 125, state_mutation: 111, structural_boundaries: 28, branch: 23
- `js/src/tooltip.js` (JAVASCRIPT) | Magnitude: 475.36 | Delta: **0.09 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 273, state_mutation: 271, branch: 47, immutability_locks: 43
- `js/src/util/swipe.js` (JAVASCRIPT) | Magnitude: 157.8 | Delta: **0.113 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 101, indent_spaces: 79, structural_boundaries: 21, args: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `js/src/collapse.js` (JAVASCRIPT) | Magnitude: 275.04 | Delta: **0.06 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 168, state_mutation: 159, immutability_locks: 44, branch: 35
- `js/tests/integration/bundle-modularity.js` (JAVASCRIPT) | Magnitude: 13.12 | Delta: **0.14 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, args: 2, globals: 2, indent_spaces: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `js/tests/visual/toast.html` (HTML) | Magnitude: 22.26 | Delta: **0.185 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 57, structural_boundaries: 22, decorators: 21, args: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `js/src/popover.js` (JAVASCRIPT) | Magnitude: 45.56 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 17, state_mutation: 13, args: 8
- `scss/_mixins.scss` (CSS) | Magnitude: 0.78 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: import: 25
- `scss/_helpers.scss` (CSS) | Magnitude: 0.76 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: import: 12
- `scss/_forms.scss` (CSS) | Magnitude: 0.73 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: import: 9
- `js/src/dom/selector-engine.js` (JAVASCRIPT) | Magnitude: 102.88 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 78, structural_boundaries: 27, branch: 21, state_mutation: 21

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `js/src/dropdown.js` -> **Mark Otto** (100.0% isolated ownership) | Magnitude: 166.0
- `js/src/base-component.js` -> **Mark Otto** (100.0% isolated ownership) | Magnitude: 74.94

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `js/src/tooltip.js` -> **Severity: 1.108** (Embedded: 0.0143 * Error Risk: 77.525%)
- `js/src/modal.js` -> **Severity: 0.574** (Embedded: 0.0071 * Error Risk: 80.4239%)
- `js/src/util/backdrop.js` -> **Severity: 0.493** (Embedded: 0.0071 * Error Risk: 68.9526%)
- `js/src/offcanvas.js` -> **Severity: 0.439** (Embedded: 0.0071 * Error Risk: 61.4703%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `js/src/base-component.js` -> **Severity: 696.6** (Blast Radius: 6.966 * Doc Risk: 100.0%)
- `js/src/dom/manipulator.js` -> **Severity: 632.742** (Blast Radius: 6.966 * Doc Risk: 90.8329%)
- `js/index.esm.js` -> **Severity: 557.28** (Blast Radius: 6.966 * Doc Risk: 80.0%)
- `js/src/dom/selector-engine.js` -> **Severity: 485.291** (Blast Radius: 6.966 * Doc Risk: 69.6657%)
- `js/src/util/component-functions.js` -> **Severity: 428.637** (Blast Radius: 6.966 * Doc Risk: 61.5327%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
