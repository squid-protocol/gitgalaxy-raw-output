# ARCHITECTURAL_BRIEF: reveal.js
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_web/reveal.js` |
| **Timestamp** | `2026-08-03T20:06:56.623593+00:00` |
| **Scan Duration** | `0.54s` |
| **Git Branch** | `master` |
| **Git Commit** | `8bbbcf83104b817f5882a0e04772b9f9e26b265b` |
| **Git Remote** | `https://github.com/hakimel/reveal.js.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 80 malicious artifacts.

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
| Total Artifacts | 228 |
| Analyzed Artifacts (Scanned) | 135 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 93 |
| Total LOC | 15322 |
| Volatility Index | 0.007 |
| % Scanned of codebase = | 59.2% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5203 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.5303 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.4849 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 10 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 45 | 3681 | 33.3% |
| JAVASCRIPT | 35 | 4266 | 25.9% |
| CSS | 25 | 2991 | 18.5% |
| HTML | 15 | 3389 | 11.1% |
| JSON | 6 | 995 | 4.4% |
| MARKDOWN | 6 | 0 | 4.4% |
| PLAINTEXT | 3 | 0 | 2.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.38`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 86 | 63.7% |
| file_cluster_13 | 18 | 13.3% |
| file_cluster_4 | 10 | 7.4% |
| file_cluster_17 | 6 | 4.4% |
| file_cluster_0 | 3 | 2.2% |
| file_cluster_2 | 2 | 1.5% |
| file_cluster_16 | 1 | 0.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 9 | 6.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 93*

**Composition by Extension & Reason:**
- `.css`: 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 17x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 4 exceeds 500 chars)
- `.mjs`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.woff`: 5x Excluded (Explicitly Denied Extension: '.woff')
- `.yml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 2x Excluded (Explicitly Denied Extension: '.png')
- `.json`: 1x Excluded (Massive Static Asset Blob: 3895 LOC), 1x Excluded (Massive Static Asset Blob: 3959 LOC)
- `.scss`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.wav`: 1x Excluded (Explicitly Denied Extension: '.wav')
- `.mp4`: 1x Excluded (Explicitly Denied Extension: '.mp4')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 89.9 | 18.6 | 7.6 | 0.0 |
| Error & Exception Exposure | 0.0 | 98.0 | 20.2 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 4.5 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 12.2 | 2.3 | 2.3 |
| API Exposure | 0.0 | 16.0 | 4.2 | 4.3 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 15.9 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 29.1 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 9.7 | 0.2 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 94.2 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.6 | 0.2 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 78.9 | 10.3 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 32.4 | 17.9 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 5.1 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 6.6 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 2.4 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `demo.html` (Hits: 98)
- `examples/auto-animate.html` (Hits: 39)
- `examples/lightbox.html` (Hits: 32)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **util.ts** (`js/utils/util.ts`) — 12 inbound connections
2. **reveal.js** (`js/reveal.js`) — 11 inbound connections
3. **types.ts** (`react/src/types.ts`) — 9 inbound connections
4. **reveal-context.ts** (`react/src/reveal-context.ts`) — 8 inbound connections
5. **constants.ts** (`js/utils/constants.ts`) — 6 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **reveal.js** (`js/reveal.js`) — 25 outbound dependencies
2. **demo.html** (`demo.html`) — 10 outbound dependencies
3. **index.ts** (`react/src/index.ts`) — 9 outbound dependencies
4. **markdown.html** (`examples/markdown.html`) — 8 outbound dependencies
5. **scroll.html** (`examples/scroll.html`) — 8 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `onTouchMove` (@ `js/controllers/touch.js`) -> Impact: **158.1** | LOC: 122
  * *Intent:* /** * Handler for the 'touchstart' event, enables support for * swipe and pinch gestures. *
- `checkResponsiveScrollView` (@ `js/reveal.js`) -> Impact: **142.0** | LOC: 380
- `escapeForHTML` (@ `react/src/utils/markdown.ts`) -> Impact: **123.0** | LOC: 141
- `addAttributes` (@ `react/src/utils/markdown.ts`) -> Impact: **96.1** | LOC: 61
- `addAttributes` (@ `plugin/markdown/plugin.js`) -> Impact: **95.0** | LOC: 39
  * *Intent:* /** * Check if a node value has the attributes pattern. * If yes, extract it and add that value as one or several attributes * to the target element. ...
- `sync` (@ `js/controllers/backgrounds.js`) -> Impact: **92.3** | LOC: 87
- `Plugin` (@ `plugin/notes/plugin.js`) -> Impact: **88.2** | LOC: 205
  * *Intent:* /**
- `activate` (@ `js/controllers/printview.js`) -> Impact: **65.1** | LOC: 210
- `getStatusText` (@ `js/reveal.js`) -> Impact: **55.8** | LOC: 43
  * *Intent:* // Force a layout when the whole page, incl fonts, has loaded
- `update` (@ `js/controllers/backgrounds.js`) -> Impact: **52.8** | LOC: 76

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `dispatchStateToMainWindow` (@ `plugin/notes/speaker-view.html`) -> **O(2^N) [Recursive]**
- `readURL` (@ `js/controllers/location.js`) -> **O(2^N) [Recursive]**
  * *Intent:* /**
- `activate` (@ `js/controllers/overview.js`) -> **O(2^N) [Recursive]**
- `preventIframeAutoFocus` (@ `js/controllers/slidecontent.js`) -> **O(2^N) [Recursive]**
- `onTouchMove` (@ `js/controllers/touch.js`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * Handler for the 'touchstart' event, enables support for * swipe and pinch gestures. *
- `getStatusText` (@ `js/reveal.js`) -> **O(2^N) [Recursive]**
  * *Intent:* // Force a layout when the whole page, incl fonts, has loaded
- `setState` (@ `js/reveal.js`) -> **O(2^N) [Recursive]**
- `destroy` (@ `js/reveal.js`) -> **O(2^N) [Recursive]**
- `getState` (@ `js/reveal.js`) -> **O(2^N) [Recursive]**
- `stopEmbeddedContent` (@ `js/reveal.js`) -> **O(2^N) [Recursive]**
  * *Intent:* /**

### Highest Data Gravity (Database Complexity)
- `onTouchMove` (@ `js/controllers/touch.js`) -> DB Complexity: **35**
  * *Intent:* /** * Handler for the 'touchstart' event, enables support for * swipe and pinch gestures. *
- `run` (@ `js/controllers/autoanimate.js`) -> DB Complexity: **34**
- `syncPages` (@ `js/controllers/scrollview.js`) -> DB Complexity: **31**
- `activate` (@ `js/controllers/scrollview.js`) -> DB Complexity: **28**
- `constructor` (@ `js/components/playback.js`) -> DB Complexity: **24**
  * *Intent:* /** * UI component that lets the use control auto-slide * playback via play/pause. */
- `createProgressBar` (@ `js/controllers/scrollview.js`) -> DB Complexity: **23**
- `update` (@ `js/controllers/fragments.js`) -> DB Complexity: **22**
- `activate` (@ `js/controllers/printview.js`) -> DB Complexity: **21**
- `render` (@ `js/controllers/controls.js`) -> DB Complexity: **20**
- `create` (@ `js/controllers/backgrounds.js`) -> DB Complexity: **19**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `js/controllers` | 19 | 3368.2 | 48.4% | 6.53% |
| `examples` | 12 | 586.26 | 1.55% | 0.0% |
| `js` | 4 | 546.29 | 16.8% | 29.52% |
| `plugin/notes` | 4 | 517.84 | 18.67% | 8.52% |
| `plugin/markdown` | 3 | 373.57 | 31.05% | 3.31% |
| `plugin/math` | 7 | 220.66 | 29.9% | 0.0% |
| `scripts` | 5 | 152.94 | 34.72% | 0.0% |
| `plugin/zoom` | 3 | 139.14 | 15.31% | 24.39% |
| `plugin/search` | 3 | 117.39 | 27.99% | 0.0% |
| `__monolith__` | 9 | 111.05 | 4.4% | 1.16% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `js/controllers/slidecontent.js` -> **99.9979%** Exposure
- `js/reveal.d.ts` -> **94.5687%** Exposure
- `react/src/components/deck.tsx` -> **84.1131%** Exposure
- `plugin/zoom/plugin.js` -> **73.1684%** Exposure
- `react/src/components/markdown.tsx` -> **43.0999%** Exposure
### Highest State Flux (Mutation/Volatility)
- `js/components/playback.js` -> **100.0%** Exposure
- `js/controllers/autoanimate.js` -> **100.0%** Exposure
- `js/controllers/controls.js` -> **100.0%** Exposure
- `js/controllers/focus.js` -> **100.0%** Exposure
- `js/controllers/fragments.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `css/reveal.scss` -> **0** Orphaned Functions | **11** Duplicates
- `js/reveal.d.ts` -> **6** Orphaned Functions | **0** Duplicates
- `plugin/notes/speaker-view.html` -> **0** Orphaned Functions | **5** Duplicates
- `js/controllers/slidecontent.js` -> **0** Orphaned Functions | **5** Duplicates
- `js/reveal.js` -> **0** Orphaned Functions | **4** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`js/controllers/keyboard.js`** -> AI Confidence: **99.29%**
2. **`js/controllers/pointer.js`** -> AI Confidence: **99.29%**
3. **`js/config.ts`** -> AI Confidence: **99.29%**
4. **`js/reveal.js`** -> AI Confidence: **99.25%**
5. **`react/demo/src/demo-app.tsx`** -> AI Confidence: **99.18%**
6. **`js/controllers/location.js`** -> AI Confidence: **99.17%**
7. **`js/controllers/overlay.js`** -> AI Confidence: **99.17%**
8. **`js/controllers/touch.js`** -> AI Confidence: **99.17%**
9. **`plugin/markdown/plugin.js`** -> AI Confidence: **99.17%**
10. **`js/controllers/backgrounds.js`** -> AI Confidence: **99.11%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `demo.html` -> **100.0%** Exposure
- `examples/scroll.html` -> **100.0%** Exposure
- `js/controllers/backgrounds.js` -> **100.0%** Exposure
- `js/reveal.js` -> **100.0%** Exposure
- `plugin/math/mathjax4.js` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `js/controllers/backgrounds.js` -> **100.0%** Exposure
- `plugin/markdown/plugin.js` -> **100.0%** Exposure
- `react/src/components/markdown.tsx` -> **100.0%** Exposure
- `plugin/notes/speaker-view.html` -> **0.0697%** Exposure
### Algorithmic DoS Exposure
- `plugin/notes/speaker-view.html` -> **100.0%** Exposure
- `js/controllers/fragments.js` -> **100.0%** Exposure
- `js/controllers/printview.js` -> **100.0%** Exposure
- `plugin/math/mathjax3.js` -> **100.0%** Exposure
- `plugin/math/mathjax4.js` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `151` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `js/controllers/backgrounds.js` (JAVASCRIPT) -> Cumulative Risk: **672.65**
- **Archetype:** `file_cluster_8` (Distance: 12.491 IQR)
- **Magnitude:** 289.76 | **LOC:** 471 | **CtrlFlow:** 69.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%), State Flux (99.9999%)
- **Heaviest Functions:** `sync` (Impact: 92.3), `update` (Impact: 52.8), `getContrastClass` (Impact: 21.8)

### 2. `plugin/markdown/plugin.js` (JAVASCRIPT) -> Cumulative Risk: **662.33**
- **Archetype:** `file_cluster_8` (Distance: 12.034 IQR)
- **Magnitude:** 352.3 | **LOC:** 488 | **CtrlFlow:** 71.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Injection Surface (100.0%), Logic Bomb (99.701%), State Flux (99.4129%)
- **Heaviest Functions:** `addAttributes` (Impact: 95.0), `Plugin` (Impact: 47.1), `escapeForHTML` (Impact: 47.0)

### 3. `js/controllers/printview.js` (JAVASCRIPT) -> Cumulative Risk: **645.92**
- **Archetype:** `file_cluster_4` (Distance: 11.952 IQR)
- **Magnitude:** 189.66 | **LOC:** 239 | **CtrlFlow:** 55.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.9942%)
- **Heaviest Functions:** `activate` (Impact: 65.1), `constructor` (Impact: 2.2), `isActive` (Impact: 1.7)

### 4. `plugin/math/mathjax3.js` (JAVASCRIPT) -> Cumulative Risk: **591.1**
- **Archetype:** `file_cluster_4` (Distance: 10.954 IQR)
- **Magnitude:** 41.34 | **LOC:** 78 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.8595%), Concurrency (99.8456%)
- **Heaviest Functions:** `MathJax3` (Impact: 24.3)

### 5. `plugin/math/mathjax4.js` (JAVASCRIPT) -> Cumulative Risk: **586.05**
- **Archetype:** `file_cluster_4` (Distance: 10.807 IQR)
- **Magnitude:** 46.0 | **LOC:** 82 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Concurrency (99.9961%)
- **Heaviest Functions:** `MathJax4` (Impact: 27.9)

### 6. `js/controllers/jumptoslide.js` (JAVASCRIPT) -> Cumulative Risk: **575.46**
- **Archetype:** `file_cluster_4` (Distance: 13.791 IQR)
- **Magnitude:** 196.54 | **LOC:** 197 | **CtrlFlow:** 54.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.2758%), Safety Score (87.4464%)
- **Heaviest Functions:** `jump` (Impact: 20.7), `onKeyDown` (Impact: 8.6), `search` (Impact: 6.8)

### 7. `js/controllers/slidecontent.js` (JAVASCRIPT) -> Cumulative Risk: **557.99**
- **Archetype:** `file_cluster_4` (Distance: 13.612 IQR)
- **Magnitude:** 218.88 | **LOC:** 747 | **CtrlFlow:** 65.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9999%), Tech Debt (99.9979%)
- **Heaviest Functions:** `shouldPreload` (Impact: 37.0), `preventIframeAutoFocus` (Impact: 25.1), `startEmbeddedMedia` (Impact: 17.0)

### 8. `plugin/notes/plugin.js` (JAVASCRIPT) -> Cumulative Risk: **541.86**
- **Archetype:** `file_cluster_8` (Distance: 12.1 IQR)
- **Magnitude:** 118.98 | **LOC:** 272 | **CtrlFlow:** 62.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Concurrency (99.9033%), State Flux (92.1882%)
- **Heaviest Functions:** `Plugin` (Impact: 88.2)

### 9. `js/controllers/fragments.js` (JAVASCRIPT) -> Cumulative Risk: **524.95**
- **Archetype:** `file_cluster_17` (Distance: 14.095 IQR)
- **Magnitude:** 293.6 | **LOC:** 375 | **CtrlFlow:** 50.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Safety Score (81.4918%)
- **Heaviest Functions:** `update` (Impact: 49.5), `goto` (Impact: 19.4), `sort` (Impact: 11.0)

### 10. `js/reveal.js` (JAVASCRIPT) -> Cumulative Risk: **498.89**
- **Archetype:** `file_cluster_13` (Distance: 12.603 IQR)
- **Magnitude:** 539.0 | **LOC:** 2962 | **CtrlFlow:** 59.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), State Flux (95.1564%), Verification (80.0%)
- **Heaviest Functions:** `checkResponsiveScrollView` (Impact: 142.0), `getStatusText` (Impact: 55.8), `setState` (Impact: 27.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `js/reveal.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.603 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.337 IQR)
- **Top Global Matches:** file_cluster_13: 12.603, file_cluster_8: 12.619, file_cluster_7: 12.875
- **Magnitude:** 539.0 | **LOC:** 2962 | **CtrlFlow:** 59.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (22.4861%), Tech Debt (23.5188%)
**Top Internal Functions/Classes:**
  * `checkResponsiveScrollView` (Impact: 142.0 | O(N^1) | DB: 12)
  * `getStatusText` (Impact: 55.8 | O(2^N) | DB: 4)
    * *Intent:* // Force a layout when the whole page, incl fonts, has loaded
  * `setState` (Impact: 27.8 | O(2^N) | DB: 3)
  * `cueAutoSlide` (Impact: 24.2 | O(N^1) | DB: 4)
  * `destroy` (Impact: 16.9 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 111`, `args: 67`, `func_start: 92`
* *Risk/State:* `state_mutation: 110`, `duplicate_logic: 4`
* *Architecture:* `api: 4`, `concurrency: 2`, `import: 25`
* *Defense:* `safety: 52`, `doc: 71`, `immutability_locks: 11`, `cleanup: 25`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 88.45
  * `Choke Point (Betweenness):` 0.030861 | `Ripple Effect (Closeness):` 0.113119
  * `Imports (Out-Degree: 22):` scrollview, location, playback, overview, constants, overlay, device, config.ts...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `js/controllers/scrollview.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.816 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.91 IQR)
- **Top Global Matches:** file_cluster_17: 13.816, file_cluster_4: 14.031, file_cluster_13: 14.149
- **Magnitude:** 489.38 | **LOC:** 924 | **CtrlFlow:** 61.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 31
- **Risk Profile:** Cognitive Load (47.4197%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `syncPages` (Impact: 44.0 | O(N^1) | DB: 31)
  * `activate` (Impact: 31.9 | O(N^1) | DB: 28)
  * `toggle` (Impact: 10.5 | O(N^1) | DB: 5)
  * `activatePage` (Impact: 9.6 | O(N^1) | DB: 3)
    * *Intent:* /** * Creates scroll triggers for the auto-animate steps in the * given page. *
  * `deactivatePage` (Impact: 8.6 | O(N^1))
    * *Intent:* /** * Helper method for creating a page definition and adding * required fields. A "page" is a slide...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 44`, `args: 49`, `func_start: 37`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 289`, `dead_code: 1`
* *Architecture:* `io: 4`, `api: 7`, `concurrency: 12`, `import: 2`
* *Defense:* `safety: 16`, `doc: 28`, `immutability_locks: 33`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.074035
  * `Imports (Out-Degree: 2):` constants, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `plugin/notes/speaker-view.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.367 IQR)
- **Top Global Matches:** file_cluster_8: 11.367, file_cluster_0: 11.443, file_cluster_4: 11.525
- **Magnitude:** 393.14 | **LOC:** 911 | **CtrlFlow:** 45.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (37.633%), Tech Debt (34.0896%)
**Top Internal Functions/Classes:**
  * `getTimings` (Impact: 46.1 | O(N^2) | DB: 13)
  * `setupTimer` (Impact: 45.0 | O(N^2) | DB: 14)
    * *Intent:* /** * Create the timer and clock and start updating them
  * `handleStateMessage` (Impact: 17.2 | O(N^1) | DB: 10)
    * *Intent:* /**
  * `setupIframes` (Impact: 10.4 | O(N^1) | DB: 5)
    * *Intent:* /**
  * `clearTimeout` (Impact: 10.1 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 98`, `args: 56`, `func_start: 57`, `class_start: 42`
* *Risk/State:* `safety_bypasses: 18`, `high_risk_execution: 6`, `state_mutation: 126`, `duplicate_logic: 5`
* *Architecture:* `io: 4`, `api: 5`, `concurrency: 42`
* *Defense:* `safety: 19`, `doc: 15`, `immutability_locks: 3`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.829
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/controllers/touch.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.697 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.561 IQR)
- **Top Global Matches:** file_cluster_13: 14.697, file_cluster_8: 14.761, file_cluster_11: 14.924
- **Magnitude:** 369.76 | **LOC:** 273 | **CtrlFlow:** 74.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 35
- **Risk Profile:** Cognitive Load (47.3703%), Tech Debt (24.0736%)
**Top Internal Functions/Classes:**
  * `onTouchMove` (Impact: 158.1 | O(2^N) | DB: 35)
    * *Intent:* /** * Handler for the 'touchstart' event, enables support for * swipe and pinch gestures. *
  * `isSwipePrevented` (Impact: 10.7 | O(N^1))
  * `bind` (Impact: 8.3 | O(N^1) | DB: 11)
  * `onTouchStart` (Impact: 4.5 | O(N^1) | DB: 5)
  * `constructor` (Impact: 2.9 | O(N^1) | DB: 17)
    * *Intent:* /** * Controls all touch interactions and navigations for * a presentation.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 16`, `args: 10`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 177`, `fragile_debt: 1`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* `safety: 14`, `doc: 16`, `immutability_locks: 1`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.074035
  * `Imports (Out-Degree: 2):` device, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `plugin/markdown/plugin.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.034 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.764 IQR)
- **Top Global Matches:** file_cluster_8: 12.034, file_cluster_4: 12.254, file_cluster_17: 12.288
- **Magnitude:** 352.3 | **LOC:** 488 | **CtrlFlow:** 71.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (52.686%), Tech Debt (9.9223%)
**Top Internal Functions/Classes:**
  * `addAttributes` (Impact: 95.0 | O(2^N) | DB: 5)
    * *Intent:* /** * Check if a node value has the attributes pattern. * If yes, extract it and add that value as o...
  * `Plugin` (Impact: 47.1 | O(N^1) | DB: 5)
  * `escapeForHTML` (Impact: 47.0 | O(2^N) | DB: 6)
  * `loadExternalMarkdown` (Impact: 26.7 | O(N^1) | DB: 6)
  * `addAttributeInElement` (Impact: 19.1 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 42`, `args: 26`, `func_start: 24`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 5`, `state_mutation: 76`, `planned_debt: 1`
* *Architecture:* `io: 4`, `api: 2`, `concurrency: 12`, `import: 2`
* *Defense:* `safety: 27`, `doc: 9`, `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.829
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` marked, marked-smartypants
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/markdown.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.646 IQR)
- **Top Global Matches:** file_cluster_8: 6.646, file_cluster_7: 7.762, file_cluster_1: 7.94
- **Magnitude:** 330.96 | **LOC:** 176 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.9016%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 19`, `args: 17`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`
* *Architecture:* `io: 5`, `api: 1`, `import: 3`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.829
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` white.css, reveal.js, notes.js, math.js, monokai.css, highlight.js, markdown.js, reveal.css
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/controllers/fragments.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.095 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.074 IQR)
- **Top Global Matches:** file_cluster_17: 14.095, file_cluster_8: 14.152, file_cluster_13: 14.258
- **Magnitude:** 293.6 | **LOC:** 375 | **CtrlFlow:** 50.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (44.9766%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `update` (Impact: 49.5 | O(N^2) | DB: 22)
  * `goto` (Impact: 19.4 | O(N^1) | DB: 16)
  * `sort` (Impact: 11.0 | O(N^1) | DB: 7)
  * `configure` (Impact: 7.4 | O(N^1) | DB: 2)
  * `availableRoutes` (Impact: 6.5 | O(N^1) | DB: 5)
    * *Intent:* /** * Reverse of #disable(). Only called if fragments have
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 36`, `args: 18`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `state_mutation: 176`
* *Architecture:* `api: 6`, `import: 1`
* *Defense:* `safety: 11`, `doc: 26`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.074035
  * `Imports (Out-Degree: 1):` util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/controllers/backgrounds.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.491 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.074 IQR)
- **Top Global Matches:** file_cluster_8: 12.491, file_cluster_17: 12.587, file_cluster_4: 12.622
- **Magnitude:** 289.76 | **LOC:** 471 | **CtrlFlow:** 69.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (42.2569%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `sync` (Impact: 92.3 | O(N^3) | DB: 4)
  * `update` (Impact: 52.8 | O(N^1) | DB: 14)
  * `getContrastClass` (Impact: 21.8 | O(N^1) | DB: 2)
  * `create` (Impact: 6.6 | O(N^1) | DB: 19)
  * `bubbleSlideContrastClassToElement` (Impact: 5.8 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 24`, `args: 15`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 85`
* *Architecture:* `io: 1`, `api: 7`, `concurrency: 6`, `import: 2`
* *Defense:* `safety: 7`, `doc: 14`, `immutability_locks: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.829
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` color, util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/controllers/keyboard.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.579 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.516 IQR)
- **Top Global Matches:** file_cluster_8: 14.579, file_cluster_13: 14.691, file_cluster_17: 14.786
- **Magnitude:** 264.26 | **LOC:** 415 | **CtrlFlow:** 89.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (49.0012%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onDocumentKeyDown` (Impact: 25.6 | O(N^1) | DB: 8)
    * *Intent:* /** * Registers a new shortcut to include in the help overlay *
  * `addKeyBinding` (Impact: 7.8 | O(N^1) | DB: 2)
    * *Intent:* /** * Stops listening for keyboard events.
  * `configure` (Impact: 6.3 | O(N^1) | DB: 14)
  * `enterFullscreen` (Impact: 5.4 | O(N^1) | DB: 2)
  * `constructor` (Impact: 2.7 | O(N^1) | DB: 5)
    * *Intent:* /** * Handles all reveal.js keyboard interactions. */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 12`, `args: 11`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 189`
* *Architecture:* `api: 10`, `import: 1`
* *Defense:* `safety: 35`, `doc: 13`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.074035
  * `Imports (Out-Degree: 1):` util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/controllers/slidecontent.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.612 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.813 IQR)
- **Top Global Matches:** file_cluster_4: 13.612, file_cluster_17: 13.638, file_cluster_13: 13.8
- **Magnitude:** 218.88 | **LOC:** 747 | **CtrlFlow:** 65.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (45.6127%), Tech Debt (99.9979%)
**Top Internal Functions/Classes:**
  * `shouldPreload` (Impact: 37.0 | O(N^1) | DB: 9)
  * `preventIframeAutoFocus` (Impact: 25.1 | O(2^N) | DB: 2)
  * `startEmbeddedMedia` (Impact: 17.0 | O(N^1) | DB: 1)
  * `ensureMobileMediaPlaying` (Impact: 9.1 | O(N^1))
  * `queryAll` (Impact: 7.4 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 24`, `args: 20`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `state_mutation: 69`, `fragile_debt: 1`, `duplicate_logic: 5`
* *Architecture:* `api: 5`, `concurrency: 16`, `import: 3`
* *Defense:* `safety: 19`, `doc: 11`, `immutability_locks: 8`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.074035
  * `Imports (Out-Degree: 2):` fitty, device, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/controllers/jumptoslide.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.791 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.026 IQR)
- **Top Global Matches:** file_cluster_4: 13.791, file_cluster_8: 14.031, file_cluster_13: 14.1
- **Magnitude:** 196.54 | **LOC:** 197 | **CtrlFlow:** 54.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (69.7253%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `jump` (Impact: 20.7 | O(N^1) | DB: 15)
  * `onKeyDown` (Impact: 8.6 | O(N^1) | DB: 2)
  * `search` (Impact: 6.8 | O(N^1) | DB: 2)
  * `hide` (Impact: 3.4 | O(N^1) | DB: 5)
  * `constructor` (Impact: 2.5 | O(N^1) | DB: 7)
    * *Intent:* /** * Makes it possible to jump to a slide by entering its * slide number or id.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 16`, `args: 17`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `state_mutation: 118`
* *Architecture:* `api: 5`, `concurrency: 12`, `import: 1`
* *Defense:* `safety: 5`, `doc: 4`, `immutability_locks: 4`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.074035
  * `Imports (Out-Degree: 1):` constants
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/controllers/printview.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.952 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.31 IQR)
- **Top Global Matches:** file_cluster_4: 11.952, file_cluster_17: 12.45, file_cluster_8: 12.698
- **Magnitude:** 189.66 | **LOC:** 239 | **CtrlFlow:** 55.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (80.7254%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `activate` (Impact: 65.1 | O(N^2) | DB: 21)
  * `constructor` (Impact: 2.2 | O(N^1) | DB: 1)
    * *Intent:* /** * Setups up our presentation for printing/exporting to PDF. */
  * `isActive` (Impact: 1.7 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 17`, `args: 12`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 51`
* *Architecture:* `api: 4`, `concurrency: 63`, `import: 2`
* *Defense:* `safety: 6`, `doc: 3`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.074035
  * `Imports (Out-Degree: 2):` constants, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/controllers/autoanimate.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.626 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.605 IQR)
- **Top Global Matches:** file_cluster_17: 13.626, file_cluster_8: 13.695, file_cluster_13: 13.827
- **Magnitude:** 165.32 | **LOC:** 627 | **CtrlFlow:** 34.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 34
- **Risk Profile:** Cognitive Load (32.7493%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 34.3 | O(N^1) | DB: 34)
  * `findAutoAnimateMatches` (Impact: 26.1 | O(N^1) | DB: 6)
  * `getLocalBoundingBox` (Impact: 2.6 | O(N^1) | DB: 1)
  * `constructor` (Impact: 2.2 | O(N^1) | DB: 1)
    * *Intent:* /** * Automatically animates matching elements across * slides with the [data-auto-animate] attribut...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 43`, `args: 20`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 95`
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `safety: 13`, `doc: 21`, `immutability_locks: 8`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.074035
  * `Imports (Out-Degree: 1):` util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `plugin/zoom/plugin.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.196 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.643 IQR)
- **Top Global Matches:** file_cluster_8: 12.196, file_cluster_15: 12.432, file_cluster_7: 12.51
- **Magnitude:** 135.94 | **LOC:** 265 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (35.0825%), Tech Debt (73.1684%)
**Top Internal Functions/Classes:**
  * `magnify` (Impact: 23.7 | O(N^1) | DB: 2)
    * *Intent:* // Monitor mouse movement for panning
  * `to` (Impact: 22.3 | O(N^1) | DB: 2)
  * `pan` (Impact: 13.3 | O(N^1) | DB: 1)
  * `init` (Impact: 13.1 | O(N^1) | DB: 3)
  * `getScrollOffset` (Impact: 5.5 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 19`, `args: 16`, `func_start: 14`
* *Risk/State:* `state_mutation: 41`, `duplicate_logic: 2`
* *Architecture:* `api: 3`, `concurrency: 2`
* *Defense:* `safety: 12`, `doc: 7`, `immutability_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.829
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/controllers/overlay.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.037 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.044 IQR)
- **Top Global Matches:** file_cluster_17: 13.037, file_cluster_2: 13.217, file_cluster_8: 13.242
- **Magnitude:** 134.86 | **LOC:** 391 | **CtrlFlow:** 72.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (63.1056%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onSlidesClicked` (Impact: 40.3 | O(N^1) | DB: 12)
  * `setState` (Impact: 17.1 | O(N^1) | DB: 7)
  * `close` (Impact: 3.6 | O(N^1) | DB: 5)
    * *Intent:* /**
  * `getState` (Impact: 1.7 | O(N^1) | DB: 1)
  * `destroy` (Impact: 1.7 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 10`, `args: 6`, `func_start: 5`
* *Risk/State:* `state_mutation: 65`
* *Architecture:* `io: 1`, `api: 4`
* *Defense:* `safety: 3`, `doc: 2`, `immutability_locks: 5`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.074035
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/controllers/progress.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.055 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.502 IQR)
- **Top Global Matches:** file_cluster_8: 14.055, file_cluster_7: 14.212, file_cluster_13: 14.319
- **Magnitude:** 121.06 | **LOC:** 110 | **CtrlFlow:** 55.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (35.6056%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `update` (Impact: 6.5 | O(N^1) | DB: 6)
  * `onProgressClicked` (Impact: 4.9 | O(N^1) | DB: 10)
  * `bind` (Impact: 4.6 | O(N^1) | DB: 4)
  * `unbind` (Impact: 4.6 | O(N^1) | DB: 4)
  * `configure` (Impact: 3.7 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 8`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 81`
* *Architecture:* `api: 7`
* *Defense:* `doc: 5`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.074035
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `plugin/notes/plugin.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.1 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.499 IQR)
- **Top Global Matches:** file_cluster_8: 12.1, file_cluster_13: 12.168, file_cluster_4: 12.183
- **Magnitude:** 118.98 | **LOC:** 272 | **CtrlFlow:** 62.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (26.1825%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Plugin` (Impact: 88.2 | O(N^2) | DB: 16)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 19`, `args: 13`, `func_start: 18`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 18`
* *Architecture:* `api: 1`, `concurrency: 9`, `import: 2`
* *Defense:* `safety: 16`, `doc: 8`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.829
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` marked, speaker-view.html?raw
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `plugin/search/plugin.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.962 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 2.967 IQR)
- **Top Global Matches:** file_cluster_8: 11.962, file_cluster_17: 12.007, file_cluster_0: 12.061
- **Magnitude:** 110.56 | **LOC:** 245 | **CtrlFlow:** 51.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (73.1059%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Plugin` (Impact: 37.2 | O(N^1) | DB: 16)
    * *Intent:* /*! * Handles finding a text string anywhere in the slides and showing the next occurrence to the us...
  * `init` (Impact: 7.6 | O(N^1))
  * `remove` (Impact: 4.6 | O(N^1) | DB: 2)
    * *Intent:* // Original JavaScript code by Chirp Internet: www.chirp.com.au // Please acknowledge use of this co...
  * `apply` (Impact: 4.6 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 24`, `args: 11`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `state_mutation: 51`, `dead_code: 1`
* *Architecture:* `api: 3`
* *Defense:* `safety: 3`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.829
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/controllers/controls.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.872 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.416 IQR)
- **Top Global Matches:** file_cluster_13: 12.872, file_cluster_8: 12.882, file_cluster_0: 13.234
- **Magnitude:** 109.16 | **LOC:** 290 | **CtrlFlow:** 40.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (70.9215%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `configure` (Impact: 9.3 | O(N^1) | DB: 4)
  * `render` (Impact: 5.7 | O(N^1) | DB: 20)
  * `onEnterFullscreen` (Impact: 4.4 | O(N^1) | DB: 2)
  * `constructor` (Impact: 2.6 | O(N^1) | DB: 15)
    * *Intent:* /** * Manages our presentation controls. This includes both * the built-in control arrows as well as...
  * `onNavigateUpClicked` (Impact: 2.4 | O(N^1) | DB: 2)
    * *Intent:* // Listen to both touch and click events, in case the device
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 13`, `args: 9`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 70`
* *Architecture:* `api: 4`, `import: 2`
* *Defense:* `safety: 2`, `doc: 2`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.074035
  * `Imports (Out-Degree: 2):` device, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/controllers/notes.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.043 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.036 IQR)
- **Top Global Matches:** file_cluster_8: 14.043, file_cluster_17: 14.057, file_cluster_7: 14.152
- **Magnitude:** 106.44 | **LOC:** 126 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (43.8532%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `update` (Impact: 10.4 | O(N^1) | DB: 7)
  * `updateVisibility` (Impact: 9.2 | O(N^1) | DB: 6)
  * `getSlideNotes` (Impact: 6.0 | O(N^1) | DB: 2)
    * *Intent:* /**
  * `configure` (Impact: 5.5 | O(N^1) | DB: 1)
  * `constructor` (Impact: 2.2 | O(N^1) | DB: 1)
    * *Intent:* /** * Handles the showing of speaker notes */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 10`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 57`
* *Architecture:* `api: 8`
* *Defense:* `safety: 2`, `doc: 10`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 12.042
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.076462
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `js/controllers/overview.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.635 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.073 IQR)
- **Top Global Matches:** file_cluster_13: 13.635, file_cluster_8: 13.851, file_cluster_0: 13.902
- **Magnitude:** 98.14 | **LOC:** 255 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (39.8018%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `activate` (Impact: 42.7 | O(2^N) | DB: 16)
  * `constructor` (Impact: 2.5 | O(N^1) | DB: 4)
    * *Intent:* /** * Handles all logic related to the overview mode * (birds-eye view of all slides).
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 7`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 50`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `safety: 2`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.074035
  * `Imports (Out-Degree: 2):` constants, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/controllers/pointer.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.9 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.971 IQR)
- **Top Global Matches:** file_cluster_4: 13.9, file_cluster_2: 13.985, file_cluster_8: 14.081
- **Magnitude:** 97.2 | **LOC:** 127 | **CtrlFlow:** 78.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (46.1364%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onDocumentMouseScroll` (Impact: 12.8 | O(N^1) | DB: 5)
  * `configure` (Impact: 9.8 | O(N^1) | DB: 7)
  * `showCursor` (Impact: 3.2 | O(N^1) | DB: 3)
  * `constructor` (Impact: 2.9 | O(N^1) | DB: 8)
    * *Intent:* /** * Handles hiding of the pointer/cursor when inactive. */
  * `onDocumentCursorActive` (Impact: 2.5 | O(N^1) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 3`, `args: 5`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 56`
* *Architecture:* `api: 3`, `concurrency: 6`
* *Defense:* `doc: 8`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.074035
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/controllers/focus.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.983 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.489 IQR)
- **Top Global Matches:** file_cluster_13: 13.983, file_cluster_2: 14.017, file_cluster_17: 14.087
- **Magnitude:** 95.74 | **LOC:** 103 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (46.9177%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onDocumentPointerDown` (Impact: 6.4 | O(N^1) | DB: 3)
  * `configure` (Impact: 5.7 | O(N^1) | DB: 3)
  * `focus` (Impact: 3.3 | O(N^1) | DB: 4)
  * `blur` (Impact: 3.3 | O(N^1) | DB: 4)
  * `bind` (Impact: 3.2 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 5`, `args: 10`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 58`
* *Architecture:* `api: 5`, `import: 1`
* *Defense:* `safety: 4`, `doc: 2`, `immutability_locks: 2`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.074035
  * `Imports (Out-Degree: 1):` util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/controllers/location.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_4` (Drift: 15.022 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.584 IQR)
- **Top Global Matches:** file_cluster_4: 15.022, file_cluster_0: 15.364, file_cluster_8: 15.452
- **Magnitude:** 91.62 | **LOC:** 249 | **CtrlFlow:** 76.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (49.3024%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `readURL` (Impact: 42.0 | O(2^N) | DB: 15)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 4`, `args: 2`, `func_start: 3`
* *Risk/State:* `state_mutation: 43`
* *Architecture:* `concurrency: 6`
* *Defense:* `safety: 5`, `doc: 3`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.074035
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/auto-animate.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.11 IQR)
- **Top Global Matches:** file_cluster_8: 7.11, file_cluster_0: 7.758, file_cluster_7: 8.138
- **Magnitude:** 68.54 | **LOC:** 443 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 90`, `args: 75`
* *Risk/State:* None
* *Architecture:* `io: 39`, `api: 45`, `import: 3`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.829
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` reveal.js, black.css, monokai.css, highlight.js, reveal.css
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `demo.html` (HTML) | Magnitude: 43.06 | Delta: **0.079 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 605, structural_boundaries: 187, io: 98, args: 95
- `plugin/math/mathjax2.js` (JAVASCRIPT) | Magnitude: 48.02 | Delta: **0.092 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 49, state_mutation: 27, structural_boundaries: 15, branch: 7
- `js/utils/util.ts` (TYPESCRIPT) | Magnitude: 21.88 | Delta: **0.282 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 125, structural_boundaries: 60, state_mutation: 49, branch: 46

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `react/src/components/stack.test.tsx` (TYPESCRIPT) | Magnitude: 1.16 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 34, args: 11, func_start: 11, test: 11
- `js/controllers/controls.js` (JAVASCRIPT) | Magnitude: 109.16 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 74, state_mutation: 70, structural_boundaries: 13, func_start: 10
- `js/reveal.js` (JAVASCRIPT) | Magnitude: 539.0 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 763, branch: 160, structural_boundaries: 111, state_mutation: 110
- `js/controllers/focus.js` (JAVASCRIPT) | Magnitude: 95.74 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: state_mutation: 58, indent_tabs: 52, args: 10, func_start: 10
- `scripts/zip.js` (JAVASCRIPT) | Magnitude: 46.84 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 102, immutability_locks: 30, structural_boundaries: 26, state_mutation: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `plugin/math/index.ts` (TYPESCRIPT) | Magnitude: 6.22 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 23, indent_tabs: 8, api: 6, class_start: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `react/src/components/deck.tsx` (TYPESCRIPT) | Magnitude: 12.68 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 156, structural_boundaries: 46, branch: 35, state_mutation: 33
- `js/controllers/fragments.js` (JAVASCRIPT) | Magnitude: 293.6 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 187, state_mutation: 176, branch: 37, structural_boundaries: 36
- `js/controllers/autoanimate.js` (JAVASCRIPT) | Magnitude: 165.32 | Delta: **0.069 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 143, state_mutation: 95, structural_boundaries: 43, branch: 23
- `js/controllers/overlay.js` (JAVASCRIPT) | Magnitude: 134.86 | Delta: **0.18 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 72, state_mutation: 65, branch: 26, structural_boundaries: 10
- `js/controllers/scrollview.js` (JAVASCRIPT) | Magnitude: 489.38 | Delta: **0.215 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 351, state_mutation: 289, branch: 69, args: 49

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `react/src/components/code.test.tsx` (TYPESCRIPT) | Magnitude: 3.05 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 114, args: 29, func_start: 26, test: 22
- `react/src/components/deck.test.tsx` (TYPESCRIPT) | Magnitude: 32.29 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 392, concurrency: 269, args: 139, structural_boundaries: 112

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `js/controllers/slidecontent.js` (JAVASCRIPT) | Magnitude: 218.88 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 159, state_mutation: 69, branch: 46, structural_boundaries: 24
- `js/controllers/plugins.js` (JAVASCRIPT) | Magnitude: 23.84 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 19, state_mutation: 9, structural_boundaries: 7, concurrency: 6
- `js/controllers/pointer.js` (JAVASCRIPT) | Magnitude: 97.2 | Delta: **0.085 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: state_mutation: 56, indent_tabs: 48, branch: 11, doc: 8
- `plugin/math/mathjax3.js` (JAVASCRIPT) | Magnitude: 41.34 | Delta: **0.097 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 12, state_mutation: 12, args: 8
- `plugin/math/mathjax4.js` (JAVASCRIPT) | Magnitude: 46.0 | Delta: **0.229 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 53, structural_boundaries: 13, state_mutation: 12, args: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `react/src/__tests__/setup.ts` (TYPESCRIPT) | Magnitude: 1.05 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 1, decorators: 1
- `react/src/components/slide.tsx` (TYPESCRIPT) | Magnitude: 3.58 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 87, state_mutation: 18, structural_boundaries: 14, immutability_locks: 9
- `js/controllers/notes.js` (JAVASCRIPT) | Magnitude: 106.44 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 57, indent_tabs: 55, branch: 16, structural_boundaries: 10
- `js/reveal.d.ts` (TYPESCRIPT) | Magnitude: 2.91 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 121, indent_tabs: 105, args: 42, func_start: 39
- `react/src/components/fragment.test.tsx` (TYPESCRIPT) | Magnitude: 1.83 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 96, args: 33, func_start: 33, test: 31

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `js/reveal.d.ts` -> Churn: **53.47%** | Cog Load: 6.8883% | Debt: 94.5687%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `js/reveal.js` -> **Hakim El Hattab** (100.0% isolated ownership) | Magnitude: 539.0
- `plugin/markdown/plugin.js` -> **Hakim El Hattab** (100.0% isolated ownership) | Magnitude: 352.3
- `examples/markdown.html` -> **Hakim El Hattab** (100.0% isolated ownership) | Magnitude: 330.96
- `plugin/zoom/plugin.js` -> **Hakim El Hattab** (100.0% isolated ownership) | Magnitude: 135.94
- `plugin/notes/plugin.js` -> **Hakim El Hattab** (100.0% isolated ownership) | Magnitude: 118.98

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `js/reveal.js` -> **Severity: 2.937** (Bridge: 0.0309 * Flux: 95.1564%)
- `react/src/components/slide.tsx` -> **Severity: 0.266** (Bridge: 0.0027 * Flux: 100.0%)
- `js/controllers/plugins.js` -> **Severity: 0.14** (Bridge: 0.0014 * Flux: 99.9999%)
- `react/src/components/deck.tsx` -> **Severity: 0.034** (Bridge: 0.0003 * Flux: 99.6686%)
- `react/src/components/fragment.tsx` -> **Severity: 0.029** (Bridge: 0.0014 * Flux: 20.6894%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `js/utils/util.ts` -> **Severity: 10.124** (Embedded: 0.1307 * Error Risk: 77.4611%)
- `js/controllers/progress.js` -> **Severity: 7.259** (Embedded: 0.074 * Error Risk: 98.0477%)
- `js/controllers/notes.js` -> **Severity: 7.119** (Embedded: 0.0765 * Error Risk: 93.1029%)
- `js/controllers/touch.js` -> **Severity: 6.851** (Embedded: 0.074 * Error Risk: 92.5335%)
- `js/controllers/pointer.js` -> **Severity: 6.541** (Embedded: 0.074 * Error Risk: 88.3529%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `js/utils/util.ts` -> **Severity: 3933.149** (Blast Radius: 59.369 * Doc Risk: 66.2492%)
- `react/src/types.ts` -> **Severity: 3904.1** (Blast Radius: 39.041 * Doc Risk: 100.0%)
- `js/utils/constants.ts` -> **Severity: 2622.56** (Blast Radius: 32.782 * Doc Risk: 80.0%)
- `js/reveal.js` -> **Severity: 1581.521** (Blast Radius: 88.45 * Doc Risk: 17.8804%)
- `plugin/vite-plugin-dts.ts` -> **Severity: 1303.8** (Blast Radius: 13.038 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
