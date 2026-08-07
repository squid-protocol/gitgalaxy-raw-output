# ARCHITECTURAL_BRIEF: reveal.js
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_web/reveal.js` |
| **Timestamp** | `2026-08-07T04:27:42.589019+00:00` |
| **Scan Duration** | `0.5s` |
| **Git Branch** | `master` |
| **Git Commit** | `8bbbcf83104b817f5882a0e04772b9f9e26b265b` |
| **Git Remote** | `https://github.com/hakimel/reveal.js.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 80 malicious artifacts.

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
| Cognitive Load Exposure | 0.0 | 89.9 | 18.4 | 7.6 | 0.0 |
| Error & Exception Exposure | 0.0 | 99.4 | 30.2 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 13.8 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 14.0 | 2.3 | 2.3 |
| API Exposure | 0.0 | 16.0 | 4.4 | 4.3 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 14.9 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 29.1 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 9.7 | 0.2 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 94.2 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.6 | 0.2 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 78.9 | 10.3 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 28.8 | 17.9 | 11.9 |
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

- `checkResponsiveScrollView` (@ `js/reveal.js`) -> Impact: **142.0** | LOC: 380
- `slide` (@ `js/reveal.js`) -> Impact: **129.9** | LOC: 273
- `onTouchMove` (@ `js/controllers/touch.js`) -> Impact: **82.1** | LOC: 122
  * *Intent:* /** * Handler for the 'touchstart' event, enables support for * swipe and pinch gestures. *
- `escapeForHTML` (@ `react/src/utils/markdown.ts`) -> Impact: **65.0** | LOC: 141
- `Plugin` (@ `plugin/notes/plugin.js`) -> Impact: **62.2** | LOC: 205
  * *Intent:* /**
- `getMarkdownFromSlide` (@ `plugin/markdown/plugin.js`) -> Impact: **59.3** | LOC: 68
  * *Intent:* // The reveal.js instance this plugin is attached to
- `update` (@ `js/controllers/backgrounds.js`) -> Impact: **52.8** | LOC: 76
- `addAttributes` (@ `react/src/utils/markdown.ts`) -> Impact: **49.6** | LOC: 61
- `addAttributes` (@ `plugin/markdown/plugin.js`) -> Impact: **48.5** | LOC: 39
  * *Intent:* /** * Check if a node value has the attributes pattern. * If yes, extract it and add that value as one or several attributes * to the target element. ...
- `sync` (@ `js/controllers/backgrounds.js`) -> Impact: **48.4** | LOC: 87

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `js/controllers` | 19 | 3344.9 | 48.54% | 21.07% |
| `js` | 4 | 840.59 | 16.52% | 48.63% |
| `plugin/notes` | 4 | 710.84 | 16.79% | 49.97% |
| `examples` | 12 | 582.66 | 1.55% | 0.0% |
| `plugin/markdown` | 3 | 449.67 | 29.32% | 25.91% |
| `plugin/math` | 7 | 298.16 | 28.48% | 42.84% |
| `plugin/search` | 3 | 162.79 | 26.93% | 28.59% |
| `scripts` | 5 | 155.34 | 34.72% | 0.0% |
| `plugin/zoom` | 3 | 143.64 | 15.31% | 32.83% |
| `react/src/components` | 12 | 108.28 | 15.65% | 22.76% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `js/controllers/slidecontent.js` -> **100.0%** Exposure
- `plugin/math/mathjax2.js` -> **100.0%** Exposure
- `plugin/notes/plugin.js` -> **99.9825%** Exposure
- `plugin/math/mathjax3.js` -> **99.9689%** Exposure
- `plugin/math/mathjax4.js` -> **99.9447%** Exposure
### Highest State Flux (Mutation/Volatility)
- `js/components/playback.js` -> **100.0%** Exposure
- `js/controllers/autoanimate.js` -> **100.0%** Exposure
- `js/controllers/controls.js` -> **100.0%** Exposure
- `js/controllers/focus.js` -> **100.0%** Exposure
- `js/controllers/fragments.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `react/src/components/deck.test.tsx` -> **0** Orphaned Functions | **46** Duplicates
- `js/reveal.js` -> **0** Orphaned Functions | **31** Duplicates
- `plugin/notes/speaker-view.html` -> **0** Orphaned Functions | **27** Duplicates
- `react/src/components/slide.test.tsx` -> **0** Orphaned Functions | **21** Duplicates
- `react/src/components/fragment.test.tsx` -> **0** Orphaned Functions | **15** Duplicates

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `151` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `js/controllers/slidecontent.js` (JAVASCRIPT) -> Cumulative Risk: **610.3**
- **Archetype:** `file_cluster_4` (Distance: 13.586 IQR)
- **Magnitude:** 238.78 | **LOC:** 747 | **CtrlFlow:** 65.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9999%), Concurrency (99.9132%)
- **Heaviest Functions:** `shouldPreload` (Impact: 37.0), `startEmbeddedMedia` (Impact: 17.0), `preventIframeAutoFocus` (Impact: 13.2)

### 2. `js/controllers/scrollview.js` (JAVASCRIPT) -> Cumulative Risk: **598.22**
- **Archetype:** `file_cluster_17` (Distance: 13.803 IQR)
- **Magnitude:** 549.38 | **LOC:** 924 | **CtrlFlow:** 61.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (95.9414%), Tech Debt (86.0272%)
- **Heaviest Functions:** `syncPages` (Impact: 44.0), `createPageElement` (Impact: 32.0), `activate` (Impact: 31.9)

### 3. `js/controllers/jumptoslide.js` (JAVASCRIPT) -> Cumulative Risk: **581.38**
- **Archetype:** `file_cluster_4` (Distance: 13.788 IQR)
- **Magnitude:** 202.44 | **LOC:** 197 | **CtrlFlow:** 54.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.2758%), Safety Score (97.3539%)
- **Heaviest Functions:** `jump` (Impact: 20.7), `onKeyDown` (Impact: 8.6), `search` (Impact: 6.8)

### 4. `plugin/markdown/plugin.js` (JAVASCRIPT) -> Cumulative Risk: **579.24**
- **Archetype:** `file_cluster_8` (Distance: 12.016 IQR)
- **Magnitude:** 428.4 | **LOC:** 488 | **CtrlFlow:** 71.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.4129%), Verification (80.0%), Tech Debt (77.73%)
- **Heaviest Functions:** `getMarkdownFromSlide` (Impact: 59.3), `addAttributes` (Impact: 48.5), `Plugin` (Impact: 47.1)

### 5. `plugin/math/mathjax2.js` (JAVASCRIPT) -> Cumulative Risk: **578.06**
- **Archetype:** `file_cluster_0` (Distance: 12.488 IQR)
- **Magnitude:** 94.72 | **LOC:** 90 | **CtrlFlow:** 31.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (82.0456%)
- **Heaviest Functions:** `MathJax2` (Impact: 18.0), `finish` (Impact: 14.3), `init` (Impact: 13.7)

### 6. `plugin/notes/plugin.js` (JAVASCRIPT) -> Cumulative Risk: **576.81**
- **Archetype:** `file_cluster_8` (Distance: 12.138 IQR)
- **Magnitude:** 196.28 | **LOC:** 272 | **CtrlFlow:** 62.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9825%), Concurrency (92.759%), State Flux (92.1882%)
- **Heaviest Functions:** `Plugin` (Impact: 62.2), `onPostMessage` (Impact: 25.6), `post` (Impact: 22.8)

### 7. `plugin/search/plugin.js` (JAVASCRIPT) -> Cumulative Risk: **569.49**
- **Archetype:** `file_cluster_8` (Distance: 11.96 IQR)
- **Magnitude:** 155.96 | **LOC:** 245 | **CtrlFlow:** 51.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Safety Score (88.8315%), Tech Debt (85.7768%)
- **Heaviest Functions:** `Plugin` (Impact: 37.2), `doSearch` (Impact: 15.5), `render` (Impact: 11.0)

### 8. `js/controllers/printview.js` (JAVASCRIPT) -> Cumulative Risk: **566.96**
- **Archetype:** `file_cluster_4` (Distance: 11.946 IQR)
- **Magnitude:** 178.26 | **LOC:** 239 | **CtrlFlow:** 55.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9942%), Safety Score (84.134%)
- **Heaviest Functions:** `activate` (Impact: 46.9), `createStyleSheet` (Impact: 4.7), `constructor` (Impact: 2.2)

### 9. `plugin/math/mathjax4.js` (JAVASCRIPT) -> Cumulative Risk: **550.65**
- **Archetype:** `file_cluster_4` (Distance: 10.789 IQR)
- **Magnitude:** 49.8 | **LOC:** 82 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9447%), State Flux (99.7725%), Concurrency (76.1333%)
- **Heaviest Functions:** `MathJax4` (Impact: 10.6), `init` (Impact: 5.6), `loadScript` (Impact: 4.4)

### 10. `js/controllers/backgrounds.js` (JAVASCRIPT) -> Cumulative Risk: **545.98**
- **Archetype:** `file_cluster_8` (Distance: 12.419 IQR)
- **Magnitude:** 257.96 | **LOC:** 471 | **CtrlFlow:** 69.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9998%), Safety Score (84.4465%), Verification (80.0%)
- **Heaviest Functions:** `update` (Impact: 52.8), `sync` (Impact: 48.4), `getContrastClass` (Impact: 21.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `js/reveal.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.536 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.519 IQR)
- **Top Global Matches:** file_cluster_13: 12.536, file_cluster_8: 12.569, file_cluster_7: 12.821
- **Magnitude:** 833.9 | **LOC:** 2962 | **CtrlFlow:** 59.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (21.3996%), Tech Debt (99.9333%)
**Top Internal Functions/Classes:**
  * `checkResponsiveScrollView` (Impact: 142.0)
  * `slide` (Impact: 129.9)
  * `shuffle` (Impact: 47.4)
  * `getStatusText` (Impact: 29.0)
    * *Intent:* // Force a layout when the whole page, incl fonts, has loaded
  * `cueAutoSlide` (Impact: 24.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 111`, `args: 67`, `func_start: 92`
* *Risk/State:* `state_mutation: 106`, `duplicate_logic: 31`
* *Architecture:* `api: 6`, `concurrency: 2`, `import: 25`
* *Defense:* `safety: 52`, `doc: 71`, `immutability_locks: 11`, `cleanup: 25`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 88.45
  * `Choke Point (Betweenness):` 0.030861 | `Ripple Effect (Closeness):` 0.113119
  * `Imports (Out-Degree: 22):` progress, scrollview, overview, pointer, util, fragments, slidenumber, touch...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `js/controllers/scrollview.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.803 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.852 IQR)
- **Top Global Matches:** file_cluster_17: 13.803, file_cluster_4: 14.016, file_cluster_13: 14.142
- **Magnitude:** 549.38 | **LOC:** 924 | **CtrlFlow:** 61.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.1107%), Tech Debt (86.0272%)
**Top Internal Functions/Classes:**
  * `syncPages` (Impact: 44.0)
  * `createPageElement` (Impact: 32.0)
  * `activate` (Impact: 31.9)
  * `toggle` (Impact: 10.5)
  * `activatePage` (Impact: 9.6)
    * *Intent:* /** * Creates scroll triggers for the auto-animate steps in the * given page. *
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 44`, `args: 49`, `func_start: 37`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 289`, `dead_code: 1`, `duplicate_logic: 6`
* *Architecture:* `io: 4`, `api: 7`, `concurrency: 12`, `import: 2`
* *Defense:* `safety: 16`, `doc: 28`, `immutability_locks: 33`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.074035
  * `Imports (Out-Degree: 2):` constants, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `plugin/notes/speaker-view.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.346 IQR)
- **Top Global Matches:** file_cluster_8: 11.346, file_cluster_0: 11.404, file_cluster_4: 11.48
- **Magnitude:** 508.84 | **LOC:** 911 | **CtrlFlow:** 45.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.7745%), Tech Debt (99.8775%)
**Top Internal Functions/Classes:**
  * `setupTimer` (Impact: 32.0)
    * *Intent:* /** * Create the timer and clock and start updating them
  * `getTimings` (Impact: 31.6)
  * `callRevealApi` (Impact: 28.3)
  * `callRevealApi` (Impact: 28.2)
  * `handleStateMessage` (Impact: 17.2)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 98`, `args: 56`, `func_start: 57`, `class_start: 42`
* *Risk/State:* `safety_bypasses: 18`, `high_risk_execution: 7`, `state_mutation: 124`, `duplicate_logic: 27`
* *Architecture:* `io: 4`, `api: 5`, `concurrency: 42`
* *Defense:* `safety: 19`, `doc: 15`, `immutability_locks: 3`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.829
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `plugin/markdown/plugin.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.016 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.789 IQR)
- **Top Global Matches:** file_cluster_8: 12.016, file_cluster_4: 12.213, file_cluster_17: 12.256
- **Magnitude:** 428.4 | **LOC:** 488 | **CtrlFlow:** 71.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (47.487%), Tech Debt (77.73%)
**Top Internal Functions/Classes:**
  * `getMarkdownFromSlide` (Impact: 59.3)
    * *Intent:* // The reveal.js instance this plugin is attached to
  * `addAttributes` (Impact: 48.5)
    * *Intent:* /** * Check if a node value has the attributes pattern. * If yes, extract it and add that value as o...
  * `Plugin` (Impact: 47.1)
  * `getSlidifyOptions` (Impact: 31.9)
    * *Intent:* /** * Given a markdown slide section element, this will * return all arguments that aren't related t...
  * `loadExternalMarkdown` (Impact: 26.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 42`, `args: 26`, `func_start: 24`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 5`, `state_mutation: 76`, `planned_debt: 1`, `duplicate_logic: 3`
* *Architecture:* `io: 4`, `api: 3`, `concurrency: 12`, `import: 2`
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
- **Risk Profile:** Cognitive Load (5.9016%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 19`, `args: 17`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`
* *Architecture:* `io: 5`, `api: 1`, `import: 3`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.829
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` reveal.css, notes.js, white.css, monokai.css, reveal.js, highlight.js, math.js, markdown.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/controllers/touch.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.703 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.561 IQR)
- **Top Global Matches:** file_cluster_13: 14.703, file_cluster_8: 14.768, file_cluster_11: 14.93
- **Magnitude:** 319.66 | **LOC:** 273 | **CtrlFlow:** 74.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.495%), Tech Debt (24.0736%)
**Top Internal Functions/Classes:**
  * `onTouchMove` (Impact: 82.1)
    * *Intent:* /** * Handler for the 'touchstart' event, enables support for * swipe and pinch gestures. *
  * `isSwipePrevented` (Impact: 10.7)
  * `bind` (Impact: 8.3)
  * `onTouchEnd` (Impact: 6.7)
  * `onPointerDown` (Impact: 6.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 16`, `args: 10`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 177`, `fragile_debt: 1`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* `safety: 14`, `doc: 16`, `immutability_locks: 1`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.074035
  * `Imports (Out-Degree: 2):` util, device
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/controllers/fragments.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.079 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 3.963 IQR)
- **Top Global Matches:** file_cluster_17: 14.079, file_cluster_8: 14.149, file_cluster_13: 14.247
- **Magnitude:** 277.2 | **LOC:** 375 | **CtrlFlow:** 50.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.3143%), Tech Debt (59.7422%)
**Top Internal Functions/Classes:**
  * `update` (Impact: 29.3)
  * `goto` (Impact: 19.4)
  * `sort` (Impact: 11.0)
  * `configure` (Impact: 7.4)
  * `availableRoutes` (Impact: 6.5)
    * *Intent:* /** * Reverse of #disable(). Only called if fragments have
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 36`, `args: 18`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `state_mutation: 176`, `duplicate_logic: 2`
* *Architecture:* `api: 6`, `import: 1`
* *Defense:* `safety: 11`, `doc: 26`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.074035
  * `Imports (Out-Degree: 1):` util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/controllers/keyboard.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.579 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.516 IQR)
- **Top Global Matches:** file_cluster_8: 14.579, file_cluster_13: 14.691, file_cluster_17: 14.786
- **Magnitude:** 264.26 | **LOC:** 415 | **CtrlFlow:** 89.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.0012%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onDocumentKeyDown` (Impact: 25.6)
    * *Intent:* /** * Registers a new shortcut to include in the help overlay *
  * `addKeyBinding` (Impact: 7.8)
    * *Intent:* /** * Stops listening for keyboard events.
  * `configure` (Impact: 6.3)
  * `enterFullscreen` (Impact: 5.4)
  * `constructor` (Impact: 2.7)
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

### `js/controllers/backgrounds.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.419 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.078 IQR)
- **Top Global Matches:** file_cluster_8: 12.419, file_cluster_17: 12.509, file_cluster_4: 12.539
- **Magnitude:** 257.96 | **LOC:** 471 | **CtrlFlow:** 69.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.8274%), Tech Debt (56.9001%)
**Top Internal Functions/Classes:**
  * `update` (Impact: 52.8)
  * `sync` (Impact: 48.4)
  * `getContrastClass` (Impact: 21.8)
  * `queryAll` (Impact: 10.9)
    * *Intent:* /** * Updates the background elements to reflect the current * slide. * * @param {boolean} includeAl...
  * `create` (Impact: 6.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 24`, `args: 15`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 81`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 8`, `concurrency: 6`, `import: 2`
* *Defense:* `safety: 7`, `doc: 14`, `immutability_locks: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.829
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` color, util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/controllers/slidecontent.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.586 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.947 IQR)
- **Top Global Matches:** file_cluster_4: 13.586, file_cluster_17: 13.679, file_cluster_13: 13.845
- **Magnitude:** 238.78 | **LOC:** 747 | **CtrlFlow:** 65.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.8729%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `shouldPreload` (Impact: 37.0)
  * `startEmbeddedMedia` (Impact: 17.0)
  * `preventIframeAutoFocus` (Impact: 13.2)
  * `ensureMobileMediaPlaying` (Impact: 9.1)
  * `queryAll` (Impact: 7.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 24`, `args: 20`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `state_mutation: 69`, `fragile_debt: 1`, `duplicate_logic: 7`
* *Architecture:* `api: 5`, `concurrency: 21`, `import: 3`
* *Defense:* `safety: 19`, `doc: 11`, `immutability_locks: 8`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.074035
  * `Imports (Out-Degree: 2):` util, device, fitty
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/controllers/jumptoslide.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.788 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.026 IQR)
- **Top Global Matches:** file_cluster_4: 13.788, file_cluster_8: 14.029, file_cluster_13: 14.097
- **Magnitude:** 202.44 | **LOC:** 197 | **CtrlFlow:** 54.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.6108%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `jump` (Impact: 20.7)
  * `onKeyDown` (Impact: 8.6)
  * `search` (Impact: 6.8)
  * `clearTimeout` (Impact: 5.9)
  * `hide` (Impact: 3.4)
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

### `plugin/notes/plugin.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.138 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.874 IQR)
- **Top Global Matches:** file_cluster_8: 12.138, file_cluster_4: 12.148, file_cluster_13: 12.152
- **Magnitude:** 196.28 | **LOC:** 272 | **CtrlFlow:** 62.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (22.5221%), Tech Debt (99.9825%)
**Top Internal Functions/Classes:**
  * `Plugin` (Impact: 62.2)
    * *Intent:* /**
  * `onPostMessage` (Impact: 25.6)
  * `post` (Impact: 22.8)
  * `openSpeakerWindow` (Impact: 9.7)
    * *Intent:* /** * Handles opening of and synchronization with the reveal.js * notes window. * * Handshake proces...
  * `reconnectSpeakerWindow` (Impact: 9.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 19`, `args: 13`, `func_start: 18`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 18`, `duplicate_logic: 6`
* *Architecture:* `api: 3`, `concurrency: 9`, `import: 2`
* *Defense:* `safety: 16`, `doc: 8`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.829
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` marked, speaker-view.html?raw
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/controllers/printview.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.946 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.31 IQR)
- **Top Global Matches:** file_cluster_4: 11.946, file_cluster_17: 12.445, file_cluster_8: 12.692
- **Magnitude:** 178.26 | **LOC:** 239 | **CtrlFlow:** 55.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.8229%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `activate` (Impact: 46.9)
  * `createStyleSheet` (Impact: 4.7)
  * `constructor` (Impact: 2.2)
    * *Intent:* /** * Setups up our presentation for printing/exporting to PDF. */
  * `queryAll` (Impact: 2.1)
  * `isActive` (Impact: 1.7)
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
- **Global Archetype:** `file_cluster_17` (Drift: 13.513 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.502 IQR)
- **Top Global Matches:** file_cluster_17: 13.513, file_cluster_8: 13.589, file_cluster_13: 13.71
- **Magnitude:** 172.52 | **LOC:** 627 | **CtrlFlow:** 34.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.0734%), Tech Debt (73.607%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 34.3)
  * `findAutoAnimateMatches` (Impact: 26.1)
  * `reset` (Impact: 5.2)
  * `autoAnimateElements` (Impact: 3.2)
    * *Intent:* // Flag the navigation direction, needed for fragment buildup
  * `getLocalBoundingBox` (Impact: 2.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 43`, `args: 20`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 89`, `duplicate_logic: 2`
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* `safety: 13`, `doc: 21`, `immutability_locks: 8`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.074035
  * `Imports (Out-Degree: 1):` util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `plugin/search/plugin.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.96 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.19 IQR)
- **Top Global Matches:** file_cluster_8: 11.96, file_cluster_17: 11.987, file_cluster_0: 12.046
- **Magnitude:** 155.96 | **LOC:** 245 | **CtrlFlow:** 51.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (69.9254%), Tech Debt (85.7768%)
**Top Internal Functions/Classes:**
  * `Plugin` (Impact: 37.2)
    * *Intent:* /*! * Handles finding a text string anywhere in the slides and showing the next occurrence to the us...
  * `doSearch` (Impact: 15.5)
  * `render` (Impact: 11.0)
  * `init` (Impact: 7.6)
  * `toggleSearch` (Impact: 7.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 24`, `args: 11`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `state_mutation: 51`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 3`
* *Defense:* `safety: 3`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.829
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `plugin/zoom/plugin.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.189 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.805 IQR)
- **Top Global Matches:** file_cluster_8: 12.189, file_cluster_15: 12.425, file_cluster_7: 12.503
- **Magnitude:** 140.44 | **LOC:** 265 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (35.0825%), Tech Debt (98.5049%)
**Top Internal Functions/Classes:**
  * `magnify` (Impact: 23.7)
    * *Intent:* // Monitor mouse movement for panning
  * `to` (Impact: 22.3)
  * `pan` (Impact: 13.3)
  * `init` (Impact: 13.1)
  * `getScrollOffset` (Impact: 5.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 19`, `args: 16`, `func_start: 14`
* *Risk/State:* `state_mutation: 41`, `duplicate_logic: 4`
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
- **Risk Profile:** Cognitive Load (63.1056%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onSlidesClicked` (Impact: 40.3)
  * `setState` (Impact: 17.1)
  * `close` (Impact: 3.6)
    * *Intent:* /**
  * `getState` (Impact: 1.7)
  * `destroy` (Impact: 1.7)
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
- **Risk Profile:** Cognitive Load (35.6056%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `update` (Impact: 6.5)
  * `onProgressClicked` (Impact: 4.9)
  * `bind` (Impact: 4.6)
  * `unbind` (Impact: 4.6)
  * `configure` (Impact: 3.7)
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

### `js/controllers/controls.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.872 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.416 IQR)
- **Top Global Matches:** file_cluster_13: 12.872, file_cluster_8: 12.882, file_cluster_0: 13.234
- **Magnitude:** 109.16 | **LOC:** 290 | **CtrlFlow:** 40.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.2219%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `configure` (Impact: 9.3)
  * `render` (Impact: 5.7)
  * `onEnterFullscreen` (Impact: 4.4)
  * `constructor` (Impact: 2.6)
    * *Intent:* /** * Manages our presentation controls. This includes both * the built-in control arrows as well as...
  * `onNavigateUpClicked` (Impact: 2.4)
    * *Intent:* // Listen to both touch and click events, in case the device
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 13`, `args: 9`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 70`
* *Architecture:* `api: 4`, `import: 2`
* *Defense:* `safety: 2`, `doc: 2`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.074035
  * `Imports (Out-Degree: 2):` util, device
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/controllers/notes.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.043 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.036 IQR)
- **Top Global Matches:** file_cluster_8: 14.043, file_cluster_17: 14.057, file_cluster_7: 14.152
- **Magnitude:** 106.44 | **LOC:** 126 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.9785%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `update` (Impact: 10.4)
  * `updateVisibility` (Impact: 9.2)
  * `getSlideNotes` (Impact: 6.0)
    * *Intent:* /**
  * `configure` (Impact: 5.5)
  * `constructor` (Impact: 2.2)
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
- **Global Archetype:** `file_cluster_13` (Drift: 13.583 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.065 IQR)
- **Top Global Matches:** file_cluster_13: 13.583, file_cluster_8: 13.813, file_cluster_0: 13.845
- **Magnitude:** 104.84 | **LOC:** 255 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.8018%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `activate` (Impact: 22.9)
  * `onSlideClicked` (Impact: 15.3)
  * `toggle` (Impact: 10.5)
  * `constructor` (Impact: 2.5)
    * *Intent:* /** * Handles all logic related to the overview mode * (birds-eye view of all slides).
  * `isActive` (Impact: 1.7)
    * *Intent:* // Clicking on an overview slide navigates to it
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 7`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 48`
* *Architecture:* `api: 3`, `import: 2`
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
- **Risk Profile:** Cognitive Load (46.1364%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onDocumentMouseScroll` (Impact: 12.8)
  * `configure` (Impact: 9.8)
  * `showCursor` (Impact: 3.2)
  * `constructor` (Impact: 2.9)
    * *Intent:* /** * Handles hiding of the pointer/cursor when inactive. */
  * `onDocumentCursorActive` (Impact: 2.5)
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
- **Risk Profile:** Cognitive Load (46.9177%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onDocumentPointerDown` (Impact: 6.4)
  * `configure` (Impact: 5.7)
  * `focus` (Impact: 3.3)
  * `blur` (Impact: 3.3)
  * `bind` (Impact: 3.2)
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

### `plugin/math/mathjax2.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.488 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 4.658 IQR)
- **Top Global Matches:** file_cluster_0: 12.488, file_cluster_11: 12.64, file_cluster_8: 12.654
- **Magnitude:** 94.72 | **LOC:** 90 | **CtrlFlow:** 31.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (55.7909%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `MathJax2` (Impact: 18.0)
    * *Intent:* /**
  * `finish` (Impact: 14.3)
  * `init` (Impact: 13.7)
  * `loadScript` (Impact: 6.6)
  * `finish` (Impact: 3.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 15`, `args: 7`, `func_start: 7`
* *Risk/State:* `state_mutation: 27`, `duplicate_logic: 4`
* *Architecture:* `io: 1`, `api: 4`
* *Defense:* `safety: 3`, `doc: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.855
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.007463
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `plugin/math/katex.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.836 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.673 IQR)
- **Top Global Matches:** file_cluster_4: 11.836, file_cluster_8: 12.053, file_cluster_15: 12.247
- **Magnitude:** 81.52 | **LOC:** 97 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (54.3158%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `KaTeX` (Impact: 16.0)
    * *Intent:* /**
  * `init` (Impact: 12.0)
  * `loadScripts` (Impact: 4.2)
  * `loadScript` (Impact: 2.2)
  * `loadCss` (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 21`, `args: 7`, `func_start: 8`
* *Risk/State:* `state_mutation: 34`
* *Architecture:* `io: 1`, `api: 5`, `concurrency: 3`
* *Defense:* `doc: 2`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.855
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.007463
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `demo.html` (HTML) | Magnitude: 39.46 | Delta: **0.079 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 605, structural_boundaries: 187, io: 98, args: 95
- `plugin/math/mathjax2.js` (JAVASCRIPT) | Magnitude: 94.72 | Delta: **0.152 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 49, state_mutation: 27, structural_boundaries: 15, branch: 7
- `js/utils/util.ts` (TYPESCRIPT) | Magnitude: 20.04 | Delta: **0.281 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 125, structural_boundaries: 60, state_mutation: 49, branch: 46

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `js/controllers/controls.js` (JAVASCRIPT) | Magnitude: 109.16 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 74, state_mutation: 70, structural_boundaries: 13, func_start: 10
- `react/src/components/stack.test.tsx` (TYPESCRIPT) | Magnitude: 2.72 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 34, args: 11, func_start: 11, test: 11
- `js/reveal.js` (JAVASCRIPT) | Magnitude: 833.9 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 763, branch: 160, structural_boundaries: 111, state_mutation: 106
- `js/controllers/focus.js` (JAVASCRIPT) | Magnitude: 95.74 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: state_mutation: 58, indent_tabs: 52, args: 10, func_start: 10
- `scripts/zip.js` (JAVASCRIPT) | Magnitude: 46.84 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 102, immutability_locks: 30, structural_boundaries: 26, state_mutation: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `plugin/math/index.ts` (TYPESCRIPT) | Magnitude: 6.22 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 23, indent_tabs: 8, api: 6, class_start: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `react/src/components/deck.tsx` (TYPESCRIPT) | Magnitude: 14.07 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 156, structural_boundaries: 46, branch: 35, state_mutation: 33
- `js/controllers/fragments.js` (JAVASCRIPT) | Magnitude: 277.2 | Delta: **0.07 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 187, state_mutation: 176, branch: 37, structural_boundaries: 36
- `js/controllers/autoanimate.js` (JAVASCRIPT) | Magnitude: 172.52 | Delta: **0.076 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 143, state_mutation: 89, structural_boundaries: 43, branch: 23
- `js/controllers/overlay.js` (JAVASCRIPT) | Magnitude: 134.86 | Delta: **0.18 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 72, state_mutation: 65, branch: 26, structural_boundaries: 10
- `js/controllers/scrollview.js` (JAVASCRIPT) | Magnitude: 549.38 | Delta: **0.213 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 351, state_mutation: 289, branch: 69, args: 49

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `react/src/components/code.test.tsx` (TYPESCRIPT) | Magnitude: 6.0 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 114, args: 29, func_start: 26, test: 22
- `react/src/components/deck.test.tsx` (TYPESCRIPT) | Magnitude: 42.47 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 392, concurrency: 269, args: 139, structural_boundaries: 112

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `js/controllers/plugins.js` (JAVASCRIPT) | Magnitude: 23.84 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 19, state_mutation: 9, structural_boundaries: 7, concurrency: 6
- `js/controllers/pointer.js` (JAVASCRIPT) | Magnitude: 97.2 | Delta: **0.085 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: state_mutation: 56, indent_tabs: 48, branch: 11, doc: 8
- `js/controllers/slidecontent.js` (JAVASCRIPT) | Magnitude: 238.78 | Delta: **0.093 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 159, state_mutation: 69, branch: 46, structural_boundaries: 24
- `plugin/math/mathjax3.js` (JAVASCRIPT) | Magnitude: 48.04 | Delta: **0.162 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 12, state_mutation: 12, args: 8
- `plugin/math/katex.js` (JAVASCRIPT) | Magnitude: 81.52 | Delta: **0.217 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 59, state_mutation: 34, structural_boundaries: 21, func_start: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `react/src/__tests__/setup.ts` (TYPESCRIPT) | Magnitude: 1.05 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 1, decorators: 1
- `plugin/notes/plugin.js` (JAVASCRIPT) | Magnitude: 196.28 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 133, branch: 31, structural_boundaries: 19, func_start: 18
- `react/src/components/slide.tsx` (TYPESCRIPT) | Magnitude: 3.58 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 87, state_mutation: 18, structural_boundaries: 14, immutability_locks: 9
- `js/controllers/notes.js` (JAVASCRIPT) | Magnitude: 106.44 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 57, indent_tabs: 55, branch: 16, structural_boundaries: 10
- `react/src/components/fragment.test.tsx` (TYPESCRIPT) | Magnitude: 5.76 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 96, args: 33, func_start: 33, test: 31

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `js/reveal.d.ts` -> Churn: **53.47%** | Cog Load: 6.8883% | Debt: 94.5687%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `js/reveal.js` -> **Hakim El Hattab** (100.0% isolated ownership) | Magnitude: 833.9
- `plugin/markdown/plugin.js` -> **Hakim El Hattab** (100.0% isolated ownership) | Magnitude: 428.4
- `examples/markdown.html` -> **Hakim El Hattab** (100.0% isolated ownership) | Magnitude: 330.96
- `plugin/notes/plugin.js` -> **Hakim El Hattab** (100.0% isolated ownership) | Magnitude: 196.28
- `plugin/search/plugin.js` -> **Hakim El Hattab** (100.0% isolated ownership) | Magnitude: 155.96

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `js/reveal.js` -> **Severity: 2.905** (Bridge: 0.0309 * Flux: 94.1398%)
- `react/src/components/slide.tsx` -> **Severity: 0.266** (Bridge: 0.0027 * Flux: 100.0%)
- `js/controllers/plugins.js` -> **Severity: 0.14** (Bridge: 0.0014 * Flux: 99.9999%)
- `react/src/components/deck.tsx` -> **Severity: 0.034** (Bridge: 0.0003 * Flux: 99.6686%)
- `react/src/components/fragment.tsx` -> **Severity: 0.029** (Bridge: 0.0014 * Flux: 20.6894%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `js/utils/util.ts` -> **Severity: 10.124** (Embedded: 0.1307 * Error Risk: 77.4611%)
- `js/controllers/notes.js` -> **Severity: 7.522** (Embedded: 0.0765 * Error Risk: 98.3739%)
- `js/controllers/progress.js` -> **Severity: 7.362** (Embedded: 0.074 * Error Risk: 99.4347%)
- `js/controllers/touch.js` -> **Severity: 7.257** (Embedded: 0.074 * Error Risk: 98.0181%)
- `js/controllers/pointer.js` -> **Severity: 7.232** (Embedded: 0.074 * Error Risk: 97.681%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `react/src/types.ts` -> **Severity: 3904.1** (Blast Radius: 39.041 * Doc Risk: 100.0%)
- `js/utils/util.ts` -> **Severity: 3670.328** (Blast Radius: 59.369 * Doc Risk: 61.8223%)
- `js/utils/constants.ts` -> **Severity: 2622.462** (Blast Radius: 32.782 * Doc Risk: 79.997%)
- `js/reveal.js` -> **Severity: 1581.521** (Blast Radius: 88.45 * Doc Risk: 17.8804%)
- `plugin/vite-plugin-dts.ts` -> **Severity: 1303.8** (Blast Radius: 13.038 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
