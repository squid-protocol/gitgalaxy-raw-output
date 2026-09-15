# ARCHITECTURAL_BRIEF: jquery
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/jquery/jquery.git` |
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
| Total Artifacts | 351 |
| Analyzed Artifacts (Scanned) | 295 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 56 |
| Total LOC | 34254 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 84.0% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.693 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3391 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.531 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 19 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 214 | 31614 | 72.5% |
| HTML | 61 | 2209 | 20.7% |
| PLAINTEXT | 7 | 1 | 2.4% |
| MARKDOWN | 5 | 0 | 1.7% |
| XML | 3 | 0 | 1.0% |
| PHP | 2 | 275 | 0.7% |
| CSS | 2 | 128 | 0.7% |
| YAML | 1 | 27 | 0.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Flat Modular Platform` (z +1.87; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 55%, Callbacks & Closures Files 18%, Declarative / Non-Code 8%, Defensive Guards Files 7%, Large Core Modules 4%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 283 | 95.9% |
| Unknown | 1 | 0.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 11 | 3.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 56*

**Composition by Extension & Reason:**
- `.js`: 28x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 11486 LOC)
- `.sh`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cjs`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jpg`: 1x Excluded (Explicitly Denied Extension: '.jpg')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 97.2 | 16.6 | 2.8 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.6 | 38.6 | 48.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 8.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 6.7 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 85.7 | 10.4 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 9.6 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 22.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 72.9 | 0.6 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 66.4 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.7 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 67.3 | 2.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 46.0 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 16 | 7 | 0 | `test/unit/css.js` |
| cleanup | 22 | 13 | 0 | `test/unit/selector.js` |
| guards | 1264 | 108 | 11 | `src/selector.js` |
| danger | 885 | 84 | 4 | `test/unit/ajax.js` |
| concurrency | 459 | 56 | 3 | `test/unit/deferred.js` |
| connectivity | 637 | 179 | 2 | `test/data/qunit-fixture.html` |
| io | 302 | 68 | 3 | `test/data/mock.php` |
| crypto | 0 | 0 | 0 | - |
| ipc | 1 | 1 | 0 | `test/data/event/onbeforeunload.html` |
| time | 91 | 32 | 1 | `test/unit/effects.js` |
| serialization | 21 | 9 | 0 | `test/middleware-mockserver.cjs` |
| regex | 139 | 50 | 1 | `test/unit/manipulation.js` |
| events | 1971 | 81 | 4 | `test/unit/event.js` |
| tests | 7086 | 37 | 1 | `test/unit/selector.js` |
| docs | 79 | 61 | 1 | `src/selector.js` |
| debt | 257 | 32 | 1 | `test/unit/ajax.js` |
| mutation | 8779 | 248 | 63 | `test/unit/manipulation.js` |
| dead_code | 145 | 57 | 1 | `test/middleware-mockserver.cjs` |
| credential | 2 | 1 | 0 | `test/unit/serialize.js` |
| threat | 92 | 37 | 1 | `test/unit/core.js` |
| ml_ai | 1 | 1 | 0 | `test/data/mock.php` |
| ui | 257 | 34 | 1 | `test/unit/manipulation.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `test/data/mock.php` (Hits: 65)
- `test/data/qunit-fixture.html` (Hits: 47)
- `test/index.html` (Hits: 12)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **iframeTest.js** (`test/data/iframeTest.js`) — 44 inbound connections
2. **document.js** (`src/var/document.js`) — 13 inbound connections
3. **whitespace.js** (`src/var/whitespace.js`) — 11 inbound connections
4. **arr.js** (`src/var/arr.js`) — 10 inbound connections
5. **isIE.js** (`src/var/isIE.js`) — 10 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **selector.js** (`src/selector.js`) — 23 outbound dependencies
2. **css.js** (`src/css.js`) — 16 outbound dependencies
3. **core.js** (`src/core.js`) — 14 outbound dependencies
4. **manipulation.js** (`src/manipulation.js`) — 14 outbound dependencies
5. **selector-native.js** (`src/selector-native.js`) — 13 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `ajax` **(Many-Argument Workhorses)** (@ `src/ajax.js`) -> Impact: **205.1** | LOC: 464
  * *Intent:* // Main method
- `trigger` **(Many-Argument Workhorses)** (@ `src/event/trigger.js`) -> Impact: **130.2** | LOC: 144
- `CHILD` **(Many-Argument Workhorses)** (@ `src/selector.js`) -> Impact: **125.6** | LOC: 111
- `defaultPrefilter` **(Many-Argument Workhorses)** (@ `src/effects.js`) -> Impact: **104.3** | LOC: 167
- `find` **(Many-Argument Workhorses)** (@ `src/selector.js`) -> Impact: **98.0** | LOC: 126
- `setMatcher` **(Many-Argument Workhorses)** (@ `src/selector.js`) -> Impact: **94.9** | LOC: 98
- `superMatcher` **(Many-Argument Workhorses)** (@ `src/selector.js`) -> Impact: **91.4** | LOC: 113
- `remove` **(Many-Argument Workhorses)** (@ `src/event.js`) -> Impact: **89.3** | LOC: 72
  * *Intent:* // Detach an event or set of events from an element
- `done` **(Many-Argument Workhorses)** (@ `src/ajax.js`) -> Impact: **80.2** | LOC: 129
  * *Intent:* // Callback for when everything is done
- `add` **(Many-Argument Workhorses)** (@ `src/event.js`) -> Impact: **74.1** | LOC: 110

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `test/unit` | 24 | 6974.46 | 21.32% | 0.0% |
| `src` | 23 | 6288.02 | 58.55% | 40.65% |
| `__monolith__` | 11 | 5070.86 | 0.42% | 0.97% |
| `test/data` | 38 | 1381.59 | 2.85% | 0.0% |
| `test` | 6 | 489.12 | 6.13% | 0.0% |
| `src/attributes` | 4 | 434.02 | 70.8% | 15.28% |
| `src/core` | 15 | 400.66 | 31.35% | 14.62% |
| `test/data/offset` | 8 | 383.98 | 0.27% | 0.0% |
| `src/css` | 8 | 320.26 | 39.89% | 9.14% |
| `src/manipulation` | 6 | 310.94 | 35.94% | 15.88% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/ajax/script.js` -> **99.9831%** Exposure
- `src/data.js` -> **98.8079%** Exposure
- `src/traversing.js` -> **98.5573%** Exposure
- `src/callbacks.js` -> **96.3861%** Exposure
- `src/deprecated.js` -> **95.2574%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/ajax.js` -> **100.0%** Exposure
- `src/ajax/jsonp.js` -> **100.0%** Exposure
- `src/ajax/load.js` -> **100.0%** Exposure
- `src/attributes/classes.js` -> **100.0%** Exposure
- `src/attributes/val.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `test/unit/ajax.js` -> **0** Orphaned Functions | **79** Duplicates
- `test/middleware-mockserver.cjs` -> **23** Orphaned Functions | **0** Duplicates
- `test/unit/effects.js` -> **3** Orphaned Functions | **8** Duplicates
- `test/unit/core.js` -> **0** Orphaned Functions | **10** Duplicates
- `test/unit/event.js` -> **6** Orphaned Functions | **4** Duplicates

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
- **Unknown Dependencies:** `99` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/ajax.js` (JAVASCRIPT) -> Cumulative Risk: **708.84**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.99)
- **Magnitude:** 894.2 | **LOC:** 889 | **CtrlFlow:** 34.5% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (96.643%)
- **Heaviest Functions:** `ajax` (Many-Argument Workhorses, Impact: 205.1), `done` (Many-Argument Workhorses, Impact: 80.2), `ajaxConvert` (Many-Argument Workhorses, Impact: 65.1)

### 2. `src/ajax/xhr.js` (JAVASCRIPT) -> Cumulative Risk: **696.29**
- **Archetype:** `file_cluster_8` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +1.55)
- **Magnitude:** 83.34 | **LOC:** 115 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9798%), Concurrency (93.7373%)
- **Heaviest Functions:** `send` (Many-Argument Workhorses, Impact: 37.3), `callback` (Defensive Guards, Impact: 14.2), `abort` (Callbacks & Closures, Impact: 2.2)

### 3. `src/callbacks.js` (JAVASCRIPT) -> Cumulative Risk: **666.54**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z -0.23)
- **Magnitude:** 215.18 | **LOC:** 231 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (96.3861%)
- **Heaviest Functions:** `Callbacks` (Compute Cores, Impact: 56.3), `add` (Defensive Guards, Impact: 14.4), `fire` (I/O & Config Routines, Impact: 12.2)

### 4. `src/core.js` (JAVASCRIPT) -> Cumulative Risk: **640.52**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.24)
- **Magnitude:** 315.26 | **LOC:** 420 | **CtrlFlow:** 28.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (87.0393%)
- **Heaviest Functions:** `extend` (Defensive Guards, Impact: 27.6), `map` (Many-Argument Workhorses, Impact: 15.5), `each` (Defensive Guards, Impact: 13.1)

### 5. `src/selector-native.js` (JAVASCRIPT) -> Cumulative Risk: **640.09**
- **Archetype:** `file_cluster_4` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +1.19)
- **Magnitude:** 110.84 | **LOC:** 152 | **CtrlFlow:** 28.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (86.4182%)
- **Heaviest Functions:** `find` (Many-Argument Workhorses, Impact: 62.3), `matches` (Callbacks & Closures, Impact: 1.9), `matchesSelector` (Callbacks & Closures, Impact: 1.9)

### 6. `src/effects/Tween.js` (JAVASCRIPT) -> Cumulative Risk: **639.76**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.01)
- **Magnitude:** 110.96 | **LOC:** 111 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (98.0216%)
- **Heaviest Functions:** `run` (Compute Cores, Impact: 11.1), `init` (Many-Argument Workhorses, Impact: 11.0), `set` (Defensive Guards, Impact: 10.6)

### 7. `src/traversing.js` (JAVASCRIPT) -> Cumulative Risk: **632.73**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.01)
- **Magnitude:** 133.1 | **LOC:** 194 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9766%), Tech Debt (98.5573%)
- **Heaviest Functions:** `closest` (Defensive Guards, Impact: 20.5), `fn[ name ]` (Defensive Guards, Impact: 13.4), `index` (Defensive Guards, Impact: 9.4)

### 8. `src/queue/delay.js` (JAVASCRIPT) -> Cumulative Risk: **628.52**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.59)
- **Magnitude:** 26.86 | **LOC:** 18 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9254%), Tech Debt (95.2574%)
- **Heaviest Functions:** `delay` (Callbacks & Closures, Impact: 7.5), `stop` (Callbacks & Closures, Impact: 1.1)

### 9. `src/event/trigger.js` (JAVASCRIPT) -> Cumulative Risk: **614.44**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.25)
- **Magnitude:** 251.86 | **LOC:** 193 | **CtrlFlow:** 42.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (97.9023%)
- **Heaviest Functions:** `trigger` (Many-Argument Workhorses, Impact: 130.2), `triggerHandler` (Callbacks & Closures, Impact: 3.8), `simulate` (Callbacks & Closures, Impact: 2.6)

### 10. `src/effects.js` (JAVASCRIPT) -> Cumulative Risk: **612.97**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.00)
- **Magnitude:** 759.54 | **LOC:** 688 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (96.9386%)
- **Heaviest Functions:** `defaultPrefilter` (Many-Argument Workhorses, Impact: 104.3), `Animation` (Many-Argument Workhorses, Impact: 44.0), `stop` (Defensive Guards, Impact: 40.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.197
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/selector.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1363.7 | **LOC:** 1377 | **CtrlFlow:** 37.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.9128%), Tech Debt (19.241%)
**Top Internal Functions/Classes:**
  * `CHILD` **(Many-Argument Workhorses)** (Impact: 125.6)
  * `find` **(Many-Argument Workhorses)** (Impact: 98.0)
  * `setMatcher` **(Many-Argument Workhorses)** (Impact: 94.9)
  * `superMatcher` **(Many-Argument Workhorses)** (Impact: 91.4)
  * `matcherFromGroupMatchers` **(Compute Cores)** (Impact: 68.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 163 instances
* *State Mutation (weighted view):* 503
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 345`, `structural_boundaries: 185`, `args: 77`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 177`, `unreferenced_by_name: 9`
* *Architecture:* `api: 1`, `import: 23`
* *Defense:* `safety: 94`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.197
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 22):` core.js, nodeName.js, createCache.js, filterMatchExpr.js, preFilter.js, rbuggyQSA.js, selectorError.js, testContext.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/unit/ajax.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1144.68 | **LOC:** 4142 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (11.5983%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `beforeSend` **(Defensive Guards)** (Impact: 17.9)
  * `beforeSend` **(Defensive Guards)** (Impact: 12.7)
  * `request` **(Callbacks & Closures)** (Impact: 9.5)
  * `beforeSend` **(Defensive Guards)** (Impact: 9.2)
  * `success` **(Tests & Verification)** (Impact: 8.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 17 instances
* *Amplified Cascading Flux:* 43 instances
* *Concurrency (weighted view):* 147
* *State Mutation (weighted view):* 219
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 309`, `structural_boundaries: 338`, `args: 625`, `func_start: 331`
* *Risk/State:* `safety_bypasses: 67`, `high_risk_execution: 1`, `state_mutation: 133`, `fragile_debt: 4`, `duplicate_logic: 79`
* *Architecture:* `io: 3`, `api: 3`, `concurrency: 62`
* *Defense:* `safety: 60`, `test: 601`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.197
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ajax.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 894.2 | **LOC:** 889 | **CtrlFlow:** 34.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (96.643%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ajax` **(Many-Argument Workhorses)** (Impact: 205.1)
    * *Intent:* // Main method
  * `done` **(Many-Argument Workhorses)** (Impact: 80.2)
    * *Intent:* // Callback for when everything is done
  * `ajaxConvert` **(Many-Argument Workhorses)** (Impact: 65.1)
    * *Intent:* /* Chain conversions given the request and the original response * Also sets the responseXXX fields ...
  * `ajaxHandleResponses` **(Many-Argument Workhorses)** (Impact: 36.7)
    * *Intent:* /* Handles responses to an ajax request: * - finds the right dataType (mediates between content-type...
  * `inspectPrefiltersOrTransports` **(Defensive Guards)** (Impact: 21.4)
    * *Intent:* // Base inspection function for prefilters and transports
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 120 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 362
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 181`, `structural_boundaries: 59`, `args: 24`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 122`, `dead_code: 2`
* *Architecture:* `api: 7`, `concurrency: 3`, `import: 6`
* *Defense:* `safety: 48`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.197
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` location.js, nonce.js, rquery.js, core.js, createElement.js, rnothtmlwhite.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/event.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 823.44 | **LOC:** 881 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.6996%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `remove` **(Many-Argument Workhorses)** (Impact: 89.3)
    * *Intent:* // Detach an event or set of events from an element
  * `add` **(Many-Argument Workhorses)** (Impact: 74.1)
  * `on` **(Many-Argument Workhorses)** (Impact: 45.3)
  * `leverageNative` **(Many-Argument Workhorses)** (Impact: 30.9)
    * *Intent:* // Ensure the presence of an event listener that handles manually-triggered // synthetic events by i...
  * `dispatch` **(Compute Cores)** (Impact: 30.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 120 instances
* *State Mutation (weighted view):* 364
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 171`, `structural_boundaries: 69`, `args: 38`, `func_start: 32`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 124`
* *Architecture:* `api: 1`, `import: 9`
* *Defense:* `safety: 42`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.197
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` core.js, nodeName.js, acceptData.js, dataPriv.js, documentElement.js, isIE.js, rcheckableType.js, rnothtmlwhite.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/unit/manipulation.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 807.66 | **LOC:** 3227 | **CtrlFlow:** 6.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (34.6324%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testAppendForObject` **(Many-Argument Workhorses)** (Impact: 31.6)
  * `testAppend` **(Many-Argument Workhorses)** (Impact: 21.1)
  * `testReplaceWith` **(Tests & Verification)** (Impact: 6.9)
  * `htmlPrefilter` **(Callbacks & Closures)** (Impact: 4.6)
  * `assertSpecialCharsSupport` **(Defensive Guards)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 95 instances
* *Concurrency (weighted view):* 88
* *State Mutation (weighted view):* 562
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 239`, `args: 271`, `func_start: 36`
* *Risk/State:* `safety_bypasses: 66`, `high_risk_execution: 1`, `state_mutation: 372`, `fragile_debt: 7`, `unreferenced_by_name: 3`
* *Architecture:* `concurrency: 18`
* *Defense:* `safety: 31`, `test: 784`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.197
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/effects.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 759.54 | **LOC:** 688 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.0555%), Tech Debt (21.5798%)
**Top Internal Functions/Classes:**
  * `defaultPrefilter` **(Many-Argument Workhorses)** (Impact: 104.3)
  * `Animation` **(Many-Argument Workhorses)** (Impact: 44.0)
  * `stop` **(Defensive Guards)** (Impact: 40.6)
  * `speed` **(Defensive Guards)** (Impact: 40.1)
  * `finish` **(Defensive Guards)** (Impact: 19.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 120 instances
* *Concurrency (weighted view):* 9
* *State Mutation (weighted view):* 367
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 148`, `structural_boundaries: 72`, `args: 39`, `func_start: 27`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 127`, `planned_debt: 1`, `unreferenced_by_name: 3`
* *Architecture:* `api: 1`, `concurrency: 4`, `import: 10`
* *Defense:* `safety: 41`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.197
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` core.js, adjustCSS.js, cssCamelCase.js, showHide.js, cssExpand.js, isHiddenWithinTree.js, dataPriv.js, document.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/unit/event.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 746.68 | **LOC:** 3636 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (23.987%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `wrapperRemoveEvent` **(Callbacks & Closures)** (Impact: 6.2)
  * `handler` **(Defensive Guards)** (Impact: 6.0)
  * `handler` **(Defensive Guards)** (Impact: 6.0)
  * `handlerWithData` **(Defensive Guards)** (Impact: 6.0)
  * `addEventListener` **(Defensive Guards)** (Impact: 5.8)
    * *Intent:* // Support: Firefox 124+ // In Firefox, alert displayed just before blurring an element // dispatche...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 58 instances
* *Concurrency (weighted view):* 101
* *State Mutation (weighted view):* 456
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 167`, `args: 412`, `func_start: 70`
* *Risk/State:* `safety_bypasses: 59`, `state_mutation: 340`, `dead_code: 2`, `planned_debt: 4`, `fragile_debt: 3`, `duplicate_logic: 4`, `unreferenced_by_name: 6`
* *Architecture:* `concurrency: 21`
* *Defense:* `safety: 49`, `test: 663`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.197
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/unit/deferred.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 731.78 | **LOC:** 1146 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.9847%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onFulfilled` **(Callbacks & Closures)** (Impact: 4.9)
  * `onFulfilled` **(Callbacks & Closures)** (Impact: 4.9)
  * `onRejected` **(Callbacks & Closures)** (Impact: 4.8)
  * `onRejected` **(Callbacks & Closures)** (Impact: 4.8)
  * `createDeferred` **(Interface Declarations)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 80 instances
* *Amplified Cascading Flux:* 9 instances
* *Concurrency (weighted view):* 498
* *State Mutation (weighted view):* 173
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 94`, `args: 192`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 155`, `fragile_debt: 1`, `duplicate_logic: 3`
* *Architecture:* `concurrency: 98`
* *Defense:* `safety: 18`, `test: 208`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.197
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/unit/effects.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 603.62 | **LOC:** 2616 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (21.1218%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `progress` **(Callbacks & Closures)** (Impact: 7.5)
  * `step` **(Defensive Guards)** (Impact: 7.4)
  * `step` **(Defensive Guards)** (Impact: 7.3)
  * `progress` **(Tests & Verification)** (Impact: 6.5)
  * `step` **(Defensive Guards)** (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 67 instances
* *Concurrency (weighted view):* 55
* *State Mutation (weighted view):* 355
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 155`, `args: 311`, `func_start: 79`
* *Risk/State:* `safety_bypasses: 27`, `high_risk_execution: 1`, `state_mutation: 221`, `planned_debt: 1`, `fragile_debt: 7`, `duplicate_logic: 8`, `unreferenced_by_name: 3`
* *Architecture:* `concurrency: 15`
* *Defense:* `safety: 64`, `test: 480`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.197
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/unit/css.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 470.7 | **LOC:** 1914 | **CtrlFlow:** 6.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (31.9745%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `add` **(Many-Argument Workhorses)** (Impact: 4.8)
  * `getUnits` **(State Mutators)** (Impact: 2.0)
  * `round` **(Callbacks & Closures)** (Impact: 1.9)
  * `hide` **(Callbacks & Closures)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 92 instances
* *Concurrency (weighted view):* 8
* *State Mutation (weighted view):* 423
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 160`, `args: 95`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 23`, `high_risk_execution: 2`, `state_mutation: 239`, `dead_code: 1`, `fragile_debt: 3`
* *Architecture:* `concurrency: 3`
* *Defense:* `safety: 20`, `test: 408`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.197
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/unit/core.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 419.9 | **LOC:** 1632 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.4803%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `iframeDone` **(Callbacks & Closures)** (Impact: 3.8)
  * `callback` **(Callbacks & Closures)** (Impact: 3.8)
  * `callback` **(Callbacks & Closures)** (Impact: 3.2)
  * `Two` **(Callbacks & Closures)** (Impact: 1.9)
  * `callback` **(Callbacks & Closures)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 76 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 21
* *State Mutation (weighted view):* 330
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 81`, `args: 129`, `func_start: 25`
* *Risk/State:* `safety_bypasses: 34`, `high_risk_execution: 1`, `state_mutation: 178`, `dead_code: 1`, `planned_debt: 3`, `fragile_debt: 9`, `duplicate_logic: 10`
* *Architecture:* `io: 2`, `api: 2`, `concurrency: 6`
* *Defense:* `safety: 54`, `doc: 1`, `test: 475`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.197
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/unit/selector.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 405.58 | **LOC:** 2555 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (10.3693%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `assertNoMatch` **(Defensive Guards)** (Impact: 12.7)
  * `testLang` **(Many-Argument Workhorses)** (Impact: 8.6)
  * `mixCase` **(Callbacks & Closures)** (Impact: 4.7)
  * `getUniqueSortFixtures` **(I/O & Config Routines)** (Impact: 4.0)
  * `get` **(Callbacks & Closures)** (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 70 instances
* *High Risk Execution (weighted view):* 3
* *Concurrency (weighted view):* 19
* *State Mutation (weighted view):* 299
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 153`, `structural_boundaries: 102`, `args: 93`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 118`, `high_risk_execution: 4`, `state_mutation: 159`, `dead_code: 2`, `fragile_debt: 2`, `unreferenced_by_name: 1`
* *Architecture:* `concurrency: 4`
* *Defense:* `safety: 27`, `doc: 2`, `test: 882`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.197
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/css.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 386.76 | **LOC:** 405 | **CtrlFlow:** 35.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.5502%), Tech Debt (36.0517%)
**Top Internal Functions/Classes:**
  * `style` **(Many-Argument Workhorses)** (Impact: 68.6)
    * *Intent:* // Get and set the style property on a DOM Node
  * `boxModelAdjustment` **(Many-Argument Workhorses)** (Impact: 43.2)
  * `getWidthOrHeight` **(Many-Argument Workhorses)** (Impact: 37.6)
  * `css` **(Many-Argument Workhorses)** (Impact: 31.0)
  * `set` **(Many-Argument Workhorses)** (Impact: 15.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 51 instances
* *State Mutation (weighted view):* 154
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 53`, `args: 13`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 52`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 16`
* *Defense:* `safety: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.197
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` core.js, access.js, nodeName.js, adjustCSS.js, cssCamelCase.js, curCSS.js, finalPropName.js, isAutoPx.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/data/testinit.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 336.8 | **LOC:** 447 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.8827%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ajaxTest` **(Many-Argument Workhorses)** (Impact: 46.2)
    * *Intent:* // Ajax testing helper
  * `loadTests` **(I/O & Config Routines)** (Impact: 17.7)
  * `testIframe` **(Many-Argument Workhorses)** (Impact: 17.1)
  * `callIfDefined` **(Defensive Guards)** (Impact: 11.0)
  * `loadDep` **(I/O & Config Routines)** (Impact: 7.2)
    * *Intent:* // Ensure load order (to preserve test numbers)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 41 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 36
* *State Mutation (weighted view):* 135
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 36`, `args: 31`, `func_start: 20`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 53`, `planned_debt: 1`
* *Architecture:* `api: 10`, `concurrency: 6`, `import: 2`
* *Defense:* `safety: 13`, `doc: 6`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.131
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003401
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `test/unit/attributes.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 326.52 | **LOC:** 1901 | **CtrlFlow:** 6.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.0635%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testVal` **(Tests & Verification)** (Impact: 14.0)
  * `testAddClass` **(Tests & Verification)** (Impact: 9.2)
  * `testToggleClass` **(Tests & Verification)** (Impact: 8.4)
  * `testFalseSetter` **(Tests & Verification)** (Impact: 6.0)
  * `testRemoveClass` **(Tests & Verification)** (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 51 instances
* *State Mutation (weighted view):* 238
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 207`, `args: 122`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 66`, `state_mutation: 136`, `dead_code: 3`, `fragile_debt: 13`
* *Architecture:* `concurrency: 2`
* *Defense:* `safety: 34`, `test: 549`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.197
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/deferred.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 325.54 | **LOC:** 393 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.6764%), Tech Debt (28.5422%)
**Top Internal Functions/Classes:**
  * `Deferred` **(Defensive Guards)** (Impact: 60.1)
  * `then` **(Many-Argument Workhorses)** (Impact: 52.2)
  * `resolve` **(Many-Argument Workhorses)** (Impact: 48.7)
  * `adoptValue` **(Defensive Guards)** (Impact: 17.1)
  * `mightThrow` **(I/O & Config Routines)** (Impact: 15.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 24 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 76
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 29`, `args: 24`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 28`, `unreferenced_by_name: 3`
* *Architecture:* `api: 1`, `concurrency: 3`, `import: 2`
* *Defense:* `safety: 32`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.197
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` core.js, slice.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/core.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 315.26 | **LOC:** 420 | **CtrlFlow:** 28.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.38%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `extend` **(Defensive Guards)** (Impact: 27.6)
  * `map` **(Many-Argument Workhorses)** (Impact: 15.5)
    * *Intent:* // arg is for internal usage only
  * `each` **(Defensive Guards)** (Impact: 13.1)
  * `text` **(Defensive Guards)** (Impact: 12.8)
    * *Intent:* // Retrieve the text value of an array of DOM nodes
  * `contains` **(Defensive Guards)** (Impact: 12.7)
    * *Intent:* // Note: an element does not contain itself
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 42 instances
* *State Mutation (weighted view):* 129
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 79`, `args: 32`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 45`, `dead_code: 1`
* *Architecture:* `api: 16`, `import: 14`
* *Defense:* `safety: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.197
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` DOMEval.js, isArrayLike.js, ObjectFunctionString.js, arr.js, class2type.js, flat.js, fnToString.js, getProto.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/data/qunit-fixture.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 282.68 | **LOC:** 310 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 105`, `args: 167`, `class_start: 9`
* *Risk/State:* None
* *Architecture:* `io: 47`, `api: 262`
* *Defense:* `safety: 69`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.197
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/middleware-mockserver.cjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 274.12 | **LOC:** 426 | **CtrlFlow:** 15.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (20.4982%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `jsonp` **(Defensive Guards)** (Impact: 21.2)
  * `script` **(Compute Cores)** (Impact: 15.1)
  * `json` **(State Mutators)** (Impact: 9.6)
  * `errorWithScript` **(Compute Cores)** (Impact: 9.3)
  * `xml` **(Defensive Guards)** (Impact: 8.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 14 instances
* *Concurrency (weighted view):* 38
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 18`, `args: 51`, `func_start: 36`
* *Risk/State:* `state_mutation: 17`, `unreferenced_by_name: 23`
* *Architecture:* `io: 3`, `api: 1`, `concurrency: 13`, `import: 4`
* *Defense:* `safety: 14`, `doc: 4`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.197
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` multiparty, node:fs, node:url, raw-body
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/manipulation.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 270.68 | **LOC:** 336 | **CtrlFlow:** 27.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.0585%), Tech Debt (27.0127%)
**Top Internal Functions/Classes:**
  * `clone` **(Many-Argument Workhorses)** (Impact: 32.4)
  * `html` **(Defensive Guards)** (Impact: 18.9)
  * `remove` **(Many-Argument Workhorses)** (Impact: 17.0)
  * `cleanData` **(Compute Cores)** (Impact: 14.4)
  * `cloneCopyEvent` **(Compute Cores)** (Impact: 11.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 39 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 117
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 57`, `args: 28`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `state_mutation: 39`, `unreferenced_by_name: 3`
* *Architecture:* `api: 1`, `import: 14`
* *Defense:* `safety: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.197
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` core.js, access.js, isAttached.js, nodeName.js, acceptData.js, dataPriv.js, dataUser.js, domManip.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/event/trigger.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 251.86 | **LOC:** 193 | **CtrlFlow:** 42.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (97.1828%), Tech Debt (39.357%)
**Top Internal Functions/Classes:**
  * `trigger` **(Many-Argument Workhorses)** (Impact: 130.2)
  * `triggerHandler` **(Callbacks & Closures)** (Impact: 3.8)
  * `simulate` **(Callbacks & Closures)** (Impact: 2.6)
    * *Intent:* // Piggyback on a donor event to simulate a different one // Used only for `focus(in | out)` events
  * `trigger` **(Callbacks & Closures)** (Impact: 2.0)
  * `stopPropagationCallback` **(Callbacks & Closures)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 36 instances
* *State Mutation (weighted view):* 109
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 22`, `args: 6`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 37`, `unreferenced_by_name: 2`
* *Architecture:* `import: 6`
* *Defense:* `safety: 10`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.197
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` core.js, acceptData.js, dataPriv.js, document.js, hasOwn.js, isWindow.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/data/mock.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 236.2 | **LOC:** 328 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (23.8066%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `script` **(Defensive Guards)** (Impact: 12.7)
  * `jsonp` **(Defensive Guards)** (Impact: 10.6)
  * `json` **(Defensive Guards)** (Impact: 7.8)
  * `etag` **(Defensive Guards)** (Impact: 6.5)
  * `ims` **(Defensive Guards)** (Impact: 6.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 73
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 49`, `args: 34`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 29`
* *Architecture:* `io: 65`, `api: 25`, `import: 5`
* *Defense:* `safety: 20`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.197
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` -trusted-types-for 'script', .html', PHP errors in http response
error_reporting( 0
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/callbacks.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 215.18 | **LOC:** 231 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.8486%), Tech Debt (96.3861%)
**Top Internal Functions/Classes:**
  * `Callbacks` **(Compute Cores)** (Impact: 56.3)
    * *Intent:* * * Possible options: * * once: will ensure the callback list can only be fired once (like a Deferre...
  * `add` **(Defensive Guards)** (Impact: 14.4)
    * *Intent:* // Add a callback or a collection of callbacks to the list
  * `fire` **(I/O & Config Routines)** (Impact: 12.2)
  * `add` **(Defensive Guards)** (Impact: 12.0)
  * `fireWith` **(Compute Cores)** (Impact: 9.2)
    * *Intent:* // Call all callbacks with the given context and arguments
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 28 instances
* *State Mutation (weighted view):* 86
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 21`, `args: 18`, `func_start: 16`
* *Risk/State:* `state_mutation: 30`, `unreferenced_by_name: 7`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 6`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.197
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` core.js, toType.js, rnothtmlwhite.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/offset.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 173.96 | **LOC:** 202 | **CtrlFlow:** 30.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.8135%), Tech Debt (23.4296%)
**Top Internal Functions/Classes:**
  * `setOffset` **(Many-Argument Workhorses)** (Impact: 28.4)
  * `fn[ method ]` **(Defensive Guards)** (Impact: 15.4)
  * `position` **(Defensive Guards)** (Impact: 15.2)
    * *Intent:* // position() relates an element's margin box to its offset parent's padding box // This corresponds...
  * `offset` **(Callbacks & Closures)** (Impact: 8.8)
    * *Intent:* // offset() relates an element's border box to the document origin
  * `offsetParent` **(Callbacks & Closures)** (Impact: 4.5)
    * *Intent:* // This method will return documentElement in the following cases: // 1) For the element inside the ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 98
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 25`, `args: 9`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 34`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `safety: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.197
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` core.js, access.js, documentElement.js, isWindow.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `test/unit/manipulation.js` -> **Michał Gołębiowski-Owczarek** (100.0% isolated ownership) | Magnitude: 807.66
- `test/unit/event.js` -> **Michał Gołębiowski-Owczarek** (100.0% isolated ownership) | Magnitude: 746.68
- `test/unit/css.js` -> **Apoorv Darshan** (100.0% isolated ownership) | Magnitude: 470.7
- `test/unit/selector.js` -> **Michał Gołębiowski-Owczarek** (100.0% isolated ownership) | Magnitude: 405.58
- `test/middleware-mockserver.cjs` -> **Apoorv Darshan** (100.0% isolated ownership) | Magnitude: 274.12

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/data/Data.js` -> **Severity: 0.037** (Bridge: 0.0004 * Flux: 100.0%)
- `src/manipulation/buildFragment.js` -> **Severity: 0.037** (Bridge: 0.0004 * Flux: 100.0%)
- `src/core/access.js` -> **Severity: 0.024** (Bridge: 0.0002 * Flux: 100.0%)
- `src/manipulation/setGlobalEval.js` -> **Severity: 0.012** (Bridge: 0.0001 * Flux: 99.1837%)
- `src/selector/tokenize.js` -> **Severity: 0.01** (Bridge: 0.0001 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `test/data/iframeTest.js` -> **Severity: 9.604** (Embedded: 0.1497 * Error Risk: 64.1725%)
- `src/core/access.js` -> **Severity: 2.09** (Embedded: 0.0238 * Error Risk: 87.7764%)
- `src/core/toType.js` -> **Severity: 1.726** (Embedded: 0.0306 * Error Risk: 56.3934%)
- `src/data/Data.js` -> **Severity: 1.597** (Embedded: 0.0213 * Error Risk: 75.008%)
- `src/selector/tokenize.js` -> **Severity: 1.002** (Embedded: 0.0102 * Error Risk: 98.1549%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `test/data/iframeTest.js` -> **Severity: 7659.7** (Blast Radius: 76.597 * Doc Risk: 100.0%)
- `src/data/Data.js` -> **Severity: 1230.4** (Blast Radius: 12.304 * Doc Risk: 100.0%)
- `src/core/toType.js` -> **Severity: 1048.4** (Blast Radius: 10.484 * Doc Risk: 100.0%)
- `src/core/camelCase.js` -> **Severity: 830.3** (Blast Radius: 8.303 * Doc Risk: 100.0%)
- `test/node_smoke_tests/module/lib/ensure_jquery.js` -> **Severity: 751.9** (Blast Radius: 7.519 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
