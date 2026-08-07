# ARCHITECTURAL_BRIEF: jquery
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_web/jquery` |
| **Timestamp** | `2026-08-07T04:26:24.445374+00:00` |
| **Scan Duration** | `0.38s` |
| **Git Branch** | `main` |
| **Git Commit** | `b43c8046f5196186fcba0860dae1680f42797f93` |
| **Git Remote** | `https://github.com/jquery/jquery.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 140 malicious artifacts.

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
| Total Artifacts | 351 |
| Analyzed Artifacts (Scanned) | 151 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 200 |
| Total LOC | 6189 |
| Volatility Index | 0.007 |
| % Scanned of codebase = | 43.0% |
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
| JAVASCRIPT | 140 | 6161 | 92.7% |
| PLAINTEXT | 5 | 1 | 3.3% |
| MARKDOWN | 5 | 0 | 3.3% |
| YAML | 1 | 27 | 0.7% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.185`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 69 | 45.7% |
| file_cluster_13 | 64 | 42.4% |
| file_cluster_17 | 4 | 2.6% |
| file_cluster_9 | 2 | 1.3% |
| Unknown | 1 | 0.7% |
| file_cluster_11 | 1 | 0.7% |
| file_cluster_4 | 1 | 0.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 9 | 6.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 200*

**Composition by Extension & Reason:**
- `.js`: 88x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 59x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cjs`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 11486 LOC)
- `.sh`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xhtml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.php`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.css`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jpg`: 1x Excluded (Explicitly Denied Extension: '.jpg')
- `.svg`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.log`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 3.9 | 93.1 | 25.7 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 98.1 | 61.7 | 72.8 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 28.6 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 15.2 | 1.6 | 80.0 |
| API Exposure | 0.0 | 9.2 | 4.3 | 5.8 | 5.8 |
| Concurrency Exposure | 0.0 | 100.0 | 4.9 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 82.5 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 72.9 | 0.9 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 60.1 | 66.7 | 100.0 |
| Instability Exposure | 0.0 | 2.1 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 43.2 | 2.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 23.4 | 17.0 | 11.2 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `test/middleware-mockserver.cjs` (Hits: 10)
- `test/bundler_smoke_tests/run-jsdom-tests.js` (Hits: 7)
- `src/ajax/xhr.js` (Hits: 1)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **AUTHORS.txt** (`AUTHORS.txt`) — 0 inbound connections
2. **LICENSE.txt** (`LICENSE.txt`) — 0 inbound connections
3. **package.json** (`dist-module/package.json`) — 0 inbound connections
4. **package.json** (`package.json`) — 0 inbound connections
5. **.npmrc** (`.npmrc`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **selector.js** (`src/selector.js`) — 23 outbound dependencies
2. **css.js** (`src/css.js`) — 16 outbound dependencies
3. **core.js** (`src/core.js`) — 14 outbound dependencies
4. **manipulation.js** (`src/manipulation.js`) — 14 outbound dependencies
5. **selector-native.js** (`src/selector-native.js`) — 13 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `superMatcher` (@ `src/selector.js`) -> Impact: **135.6** | LOC: 165
- `trigger` (@ `src/event/trigger.js`) -> Impact: **125.5** | LOC: 139
- `remove` (@ `src/event.js`) -> Impact: **107.1** | LOC: 85
- `matcherFromGroupMatchers` (@ `src/selector.js`) -> Impact: **98.5** | LOC: 168
- `setMatcher` (@ `src/selector.js`) -> Impact: **94.9** | LOC: 98
- `ajax` (@ `src/ajax.js`) -> Impact: **87.5** | LOC: 225
- `getResponseHeader` (@ `src/ajax.js`) -> Impact: **81.8** | LOC: 156
- `nonnativeSelectorCache` (@ `src/selector.js`) -> Impact: **81.4** | LOC: 103
- `handlers` (@ `src/event.js`) -> Impact: **79.1** | LOC: 232
- `find` (@ `src/selector-native.js`) -> Impact: **75.8** | LOC: 84

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 11 | 5073.7 | 1.21% | 0.0% |
| `src` | 23 | 3923.32 | 47.16% | 66.82% |
| `src/core` | 15 | 435.96 | 26.26% | 46.24% |
| `src/attributes` | 4 | 374.98 | 63.98% | 74.95% |
| `src/var` | 26 | 344.06 | 5.0% | 0.0% |
| `src/selector` | 11 | 293.32 | 31.48% | 18.18% |
| `src/manipulation` | 6 | 253.74 | 35.91% | 33.16% |
| `src/css` | 8 | 222.44 | 39.33% | 12.5% |
| `test` | 1 | 210.82 | 7.4% | 0.0% |
| `src/event` | 1 | 183.3 | 91.65% | 96.34% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `src/callbacks.js` -> **100.0%** Exposure
- `src/core/access.js` -> **100.0%** Exposure
- `src/core/isAttached.js` -> **100.0%** Exposure
- `src/core/ready-no-deferred.js` -> **100.0%** Exposure
- `src/core/readyException.js` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `src/ajax/var/location.js` -> **100.0%** Exposure
- `src/ajax/var/nonce.js` -> **100.0%** Exposure
- `src/ajax/var/rquery.js` -> **100.0%** Exposure
- `src/attributes/classes.js` -> **100.0%** Exposure
- `src/core/isArrayLike.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `test/middleware-mockserver.cjs` -> **19** Orphaned Functions | **7** Duplicates
- `src/selector.js` -> **8** Orphaned Functions | **16** Duplicates
- `src/callbacks.js` -> **6** Orphaned Functions | **7** Duplicates
- `src/effects.js` -> **5** Orphaned Functions | **4** Duplicates
- `src/event.js` -> **2** Orphaned Functions | **7** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/event.js`** -> AI Confidence: **99.39%**
2. **`src/css.js`** -> AI Confidence: **99.31%**
3. **`src/effects.js`** -> AI Confidence: **99.31%**
4. **`src/manipulation.js`** -> AI Confidence: **99.31%**
5. **`src/manipulation/buildFragment.js`** -> AI Confidence: **99.31%**
6. **`src/manipulation/domManip.js`** -> AI Confidence: **99.31%**
7. **`src/selector-native.js`** -> AI Confidence: **99.31%**
8. **`src/selector.js`** -> AI Confidence: **99.31%**
9. **`src/css/isAutoPx.js`** -> AI Confidence: **99.29%**
10. **`src/wrapper.js`** -> AI Confidence: **99.29%**
11. **`src/core.js`** -> AI Confidence: **99.24%**
12. **`src/traversing.js`** -> AI Confidence: **99.24%**
13. **`src/event/trigger.js`** -> AI Confidence: **99.22%**
14. **`test/bundler_smoke_tests/run-jsdom-tests.js`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `13` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/serialize.js` (JAVASCRIPT) -> Cumulative Risk: **585.44**
- **Archetype:** `file_cluster_17` (Distance: 12.817 IQR)
- **Magnitude:** 154.04 | **LOC:** 141 | **CtrlFlow:** 52.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (85.3522%)
- **Heaviest Functions:** `buildParams` (Impact: 28.7), `param` (Impact: 17.5), `buildParams` (Impact: 15.4)

### 2. `src/event/trigger.js` (JAVASCRIPT) -> Cumulative Risk: **564.66**
- **Archetype:** `file_cluster_8` (Distance: 11.623 IQR)
- **Magnitude:** 183.3 | **LOC:** 193 | **CtrlFlow:** 72.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9794%), Tech Debt (96.3358%), Cognitive Load (91.6475%)
- **Heaviest Functions:** `trigger` (Impact: 125.5), `acceptData` (Impact: 9.7), `triggerHandler` (Impact: 3.8)

### 3. `src/manipulation.js` (JAVASCRIPT) -> Cumulative Risk: **558.64**
- **Archetype:** `file_cluster_13` (Distance: 13.256 IQR)
- **Magnitude:** 347.58 | **LOC:** 336 | **CtrlFlow:** 55.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.4121%), Verification (80.0%)
- **Heaviest Functions:** `setGlobalEval` (Impact: 50.9), `clone` (Impact: 32.4), `html` (Impact: 29.9)

### 4. `src/core.js` (JAVASCRIPT) -> Cumulative Risk: **547.72**
- **Archetype:** `file_cluster_13` (Distance: 12.919 IQR)
- **Magnitude:** 275.72 | **LOC:** 420 | **CtrlFlow:** 46.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9977%), Tech Debt (83.2237%), Verification (80.0%)
- **Heaviest Functions:** `extend` (Impact: 23.7), `text` (Impact: 17.4), `each` (Impact: 16.6)

### 5. `src/queue.js` (JAVASCRIPT) -> Cumulative Risk: **546.64**
- **Archetype:** `file_cluster_8` (Distance: 12.485 IQR)
- **Magnitude:** 118.4 | **LOC:** 142 | **CtrlFlow:** 56.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9998%), Tech Debt (99.9996%), Verification (80.0%)
- **Heaviest Functions:** `queue` (Impact: 16.9), `dequeue` (Impact: 13.8), `promise` (Impact: 13.5)

### 6. `src/traversing.js` (JAVASCRIPT) -> Cumulative Risk: **539.33**
- **Archetype:** `file_cluster_13` (Distance: 12.872 IQR)
- **Magnitude:** 142.3 | **LOC:** 194 | **CtrlFlow:** 39.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Tech Debt (94.5687%), Verification (80.0%)
- **Heaviest Functions:** `index` (Impact: 12.9), `contents` (Impact: 11.0), `closest` (Impact: 7.7)

### 7. `src/callbacks.js` (JAVASCRIPT) -> Cumulative Risk: **532.86**
- **Archetype:** `file_cluster_8` (Distance: 11.4 IQR)
- **Magnitude:** 240.88 | **LOC:** 231 | **CtrlFlow:** 61.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.7744%), Verification (80.0%)
- **Heaviest Functions:** `Callbacks` (Impact: 75.4), `fire` (Impact: 53.2), `add` (Impact: 19.8)

### 8. `src/attributes/val.js` (JAVASCRIPT) -> Cumulative Risk: **530.96**
- **Archetype:** `file_cluster_8` (Distance: 11.928 IQR)
- **Magnitude:** 122.74 | **LOC:** 170 | **CtrlFlow:** 61.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9913%), Tech Debt (99.846%), Verification (80.0%)
- **Heaviest Functions:** `val` (Impact: 45.0), `get` (Impact: 21.5), `set` (Impact: 8.0)

### 9. `src/ajax/xhr.js` (JAVASCRIPT) -> Cumulative Risk: **525.94**
- **Archetype:** `file_cluster_8` (Distance: 9.196 IQR)
- **Magnitude:** 26.52 | **LOC:** 115 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.5648%), Tech Debt (97.334%), State Flux (65.6296%)
- **Heaviest Functions:** `send` (Impact: 12.0), `abort` (Impact: 3.1), `xhr` (Impact: 1.6)

### 10. `src/event.js` (JAVASCRIPT) -> Cumulative Risk: **525.04**
- **Archetype:** `file_cluster_8` (Distance: 12.348 IQR)
- **Magnitude:** 489.58 | **LOC:** 881 | **CtrlFlow:** 70.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.8738%), Tech Debt (96.4904%), Cognitive Load (80.7252%)
- **Heaviest Functions:** `remove` (Impact: 107.1), `handlers` (Impact: 79.1), `add` (Impact: 65.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/selector.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.485 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.192 IQR)
- **Top Global Matches:** file_cluster_13: 12.485, file_cluster_8: 12.513, file_cluster_11: 12.805
- **Magnitude:** 936.66 | **LOC:** 1377 | **CtrlFlow:** 68.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.3727%), Tech Debt (99.8112%)
**Top Internal Functions/Classes:**
  * `superMatcher` (Impact: 135.6)
  * `matcherFromGroupMatchers` (Impact: 98.5)
  * `setMatcher` (Impact: 94.9)
  * `nonnativeSelectorCache` (Impact: 81.4)
  * `select` (Impact: 70.8)
    * *Intent:* // https://www.w3.org/TR/selectors/#empty-pseudo
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 219`, `structural_boundaries: 101`, `args: 35`, `func_start: 46`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 103`, `duplicate_logic: 16`, `orphaned_logic: 8`
* *Architecture:* `api: 1`, `import: 23`
* *Defense:* `safety: 46`, `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core.js, push.js, rdescend.js, document.js, toSelector.js, isIE.js, tokenize.js, createCache.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/event.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.348 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.175 IQR)
- **Top Global Matches:** file_cluster_8: 12.348, file_cluster_13: 12.46, file_cluster_11: 12.659
- **Magnitude:** 489.58 | **LOC:** 881 | **CtrlFlow:** 70.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.7252%), Tech Debt (96.4904%)
**Top Internal Functions/Classes:**
  * `remove` (Impact: 107.1)
  * `handlers` (Impact: 79.1)
  * `add` (Impact: 65.6)
  * `on` (Impact: 45.3)
  * `off` (Impact: 21.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 50`, `args: 23`, `func_start: 24`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 77`, `duplicate_logic: 7`, `orphaned_logic: 2`
* *Architecture:* `api: 1`, `import: 9`
* *Defense:* `safety: 34`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core.js, dataPriv.js, slice.js, rcheckableType.js, rnothtmlwhite.js, acceptData.js, documentElement.js, isIE.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ajax.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.729 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.397 IQR)
- **Top Global Matches:** file_cluster_8: 11.729, file_cluster_13: 12.0, file_cluster_11: 12.229
- **Magnitude:** 372.22 | **LOC:** 889 | **CtrlFlow:** 69.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (39.2239%), Tech Debt (71.7354%)
**Top Internal Functions/Classes:**
  * `ajax` (Impact: 87.5)
  * `getResponseHeader` (Impact: 81.8)
  * `ajaxHandleResponses` (Impact: 53.6)
  * `addToPrefiltersOrTransports` (Impact: 24.0)
    * *Intent:* /* Transports bindings * 1) key is the dataType * 2) the catchall symbol "*" can be used * 3) select...
  * `inspectPrefiltersOrTransports` (Impact: 21.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 41`, `args: 15`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 48`, `duplicate_logic: 4`
* *Architecture:* `api: 4`, `concurrency: 1`, `import: 6`
* *Defense:* `safety: 33`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core.js, createElement.js, nonce.js, rnothtmlwhite.js, rquery.js, location.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/manipulation.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.256 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.282 IQR)
- **Top Global Matches:** file_cluster_13: 13.256, file_cluster_8: 13.376, file_cluster_11: 13.448
- **Magnitude:** 347.58 | **LOC:** 336 | **CtrlFlow:** 55.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.1391%), Tech Debt (99.4121%)
**Top Internal Functions/Classes:**
  * `setGlobalEval` (Impact: 50.9)
  * `clone` (Impact: 32.4)
  * `html` (Impact: 29.9)
  * `cleanData` (Impact: 19.6)
  * `remove` (Impact: 17.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 57`, `args: 28`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 111`, `duplicate_logic: 7`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `import: 14`
* *Defense:* `safety: 25`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` getAll.js, core.js, push.js, dataPriv.js, rtagName.js, isAttached.js, acceptData.js, domManip.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/effects.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.043 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.949 IQR)
- **Top Global Matches:** file_cluster_8: 12.043, file_cluster_13: 12.147, file_cluster_17: 12.331
- **Magnitude:** 288.96 | **LOC:** 688 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.7029%), Tech Debt (91.484%)
**Top Internal Functions/Classes:**
  * `speed` (Impact: 40.1)
  * `Animation` (Impact: 35.0)
  * `finish` (Impact: 26.1)
  * `createTween` (Impact: 15.1)
  * `stop` (Impact: 13.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 54`, `args: 27`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 71`, `duplicate_logic: 4`, `orphaned_logic: 5`
* *Architecture:* `api: 1`, `concurrency: 4`, `import: 10`
* *Defense:* `safety: 24`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core.js, cssCamelCase.js, adjustCSS.js, document.js, dataPriv.js, cssExpand.js, showHide.js, rnothtmlwhite.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/core.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.919 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.185 IQR)
- **Top Global Matches:** file_cluster_13: 12.919, file_cluster_11: 13.024, file_cluster_8: 13.194
- **Magnitude:** 275.72 | **LOC:** 420 | **CtrlFlow:** 46.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.9254%), Tech Debt (83.2237%)
**Top Internal Functions/Classes:**
  * `extend` (Impact: 23.7)
  * `text` (Impact: 17.4)
  * `each` (Impact: 16.6)
  * `map` (Impact: 15.5)
  * `isPlainObject` (Impact: 13.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 73`, `args: 31`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 83`, `dead_code: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 12`, `import: 14`
* *Defense:* `safety: 26`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DOMEval.js, push.js, flat.js, isArrayLike.js, slice.js, getProto.js, indexOf.js, class2type.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/callbacks.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.4 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.855 IQR)
- **Top Global Matches:** file_cluster_8: 11.4, file_cluster_13: 11.632, file_cluster_11: 11.83
- **Magnitude:** 240.88 | **LOC:** 231 | **CtrlFlow:** 61.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.8584%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `Callbacks` (Impact: 75.4)
    * *Intent:* /*
  * `fire` (Impact: 53.2)
  * `add` (Impact: 19.8)
  * `add` (Impact: 18.5)
  * `fireWith` (Impact: 9.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 21`, `args: 18`, `func_start: 19`
* *Risk/State:* `state_mutation: 27`, `duplicate_logic: 7`, `orphaned_logic: 6`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 6`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core.js, toType.js, rnothtmlwhite.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/middleware-mockserver.cjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.118 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 5.185 IQR)
- **Top Global Matches:** file_cluster_8: 10.118, file_cluster_15: 10.64, file_cluster_7: 10.696
- **Magnitude:** 210.82 | **LOC:** 426 | **CtrlFlow:** 77.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (7.4036%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `jsonp` (Impact: 21.2)
  * `MockserverMiddlewareFactory` (Impact: 10.0)
  * `json` (Impact: 9.6)
  * `errorWithScript` (Impact: 9.3)
  * `formData` (Impact: 8.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 18`, `args: 51`, `func_start: 46`
* *Risk/State:* `state_mutation: 8`, `duplicate_logic: 7`, `orphaned_logic: 19`
* *Architecture:* `io: 10`, `api: 1`, `concurrency: 18`, `import: 4`
* *Defense:* `safety: 14`, `doc: 8`, `test: 4`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` multiparty, node:url, raw-body, node:fs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/event/trigger.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.623 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.212 IQR)
- **Top Global Matches:** file_cluster_8: 11.623, file_cluster_13: 11.625, file_cluster_11: 11.981
- **Magnitude:** 183.3 | **LOC:** 193 | **CtrlFlow:** 72.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.6475%), Tech Debt (96.3358%)
**Top Internal Functions/Classes:**
  * `trigger` (Impact: 125.5)
  * `acceptData` (Impact: 9.7)
  * `triggerHandler` (Impact: 3.8)
  * `simulate` (Impact: 2.6)
  * `stopPropagationCallback` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 21`, `args: 6`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 35`, `duplicate_logic: 2`, `orphaned_logic: 2`
* *Architecture:* `import: 6`
* *Defense:* `safety: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` isWindow.js, dataPriv.js, document.js, acceptData.js, core.js, hasOwn.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/serialize.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.817 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 4.935 IQR)
- **Top Global Matches:** file_cluster_17: 12.817, file_cluster_13: 12.996, file_cluster_8: 13.016
- **Magnitude:** 154.04 | **LOC:** 141 | **CtrlFlow:** 52.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (80.08%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `buildParams` (Impact: 28.7)
  * `param` (Impact: 17.5)
    * *Intent:* // Serialize an array of form elements or a set of // key/values into a query string
  * `buildParams` (Impact: 15.4)
  * `serializeArray` (Impact: 14.7)
  * `buildParams` (Impact: 7.8)
    * *Intent:* // Item is non-scalar (array or object), encode its numeric index.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 27`, `args: 11`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 46`, `duplicate_logic: 7`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core.js, toType.js, rcheckableType.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/effects/Tween.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.485 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.753 IQR)
- **Top Global Matches:** file_cluster_13: 13.485, file_cluster_8: 13.517, file_cluster_11: 13.517
- **Magnitude:** 150.96 | **LOC:** 111 | **CtrlFlow:** 61.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.1016%), Tech Debt (33.3417%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 15.2)
  * `set` (Impact: 14.8)
  * `get` (Impact: 12.9)
  * `init` (Impact: 11.0)
  * `cur` (Impact: 4.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 14`, `args: 8`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 84`, `orphaned_logic: 1`
* *Architecture:* `import: 3`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` isAutoPx.js, core.js, finalPropName.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/traversing.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.872 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.649 IQR)
- **Top Global Matches:** file_cluster_13: 12.872, file_cluster_17: 12.903, file_cluster_8: 12.911
- **Magnitude:** 142.3 | **LOC:** 194 | **CtrlFlow:** 39.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.8005%), Tech Debt (94.5687%)
**Top Internal Functions/Classes:**
  * `index` (Impact: 12.9)
  * `contents` (Impact: 11.0)
  * `closest` (Impact: 7.7)
  * `has` (Impact: 6.7)
  * `parent` (Impact: 6.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 45`, `args: 21`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 58`, `orphaned_logic: 7`
* *Architecture:* `api: 1`, `import: 7`
* *Defense:* `safety: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core.js, getProto.js, indexOf.js, rneedsContext.js, dir.js, siblings.js, nodeName.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/attributes/classes.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.004 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.745 IQR)
- **Top Global Matches:** file_cluster_8: 13.004, file_cluster_13: 13.139, file_cluster_11: 13.218
- **Magnitude:** 135.06 | **LOC:** 157 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.8032%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `removeClass` (Impact: 20.1)
  * `addClass` (Impact: 17.8)
  * `toggleClass` (Impact: 15.8)
  * `classesToArray` (Impact: 9.4)
  * `hasClass` (Impact: 8.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 30`, `args: 12`, `func_start: 6`
* *Risk/State:* `state_mutation: 54`
* *Architecture:* `import: 3`
* *Defense:* `safety: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` rnothtmlwhite.js, core.js, stripAndCollapse.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/data/Data.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.286 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.168 IQR)
- **Top Global Matches:** file_cluster_11: 14.286, file_cluster_13: 14.304, file_cluster_17: 14.315
- **Magnitude:** 128.58 | **LOC:** 156 | **CtrlFlow:** 56.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (85.9304%), Tech Debt (47.0273%)
**Top Internal Functions/Classes:**
  * `remove` (Impact: 23.1)
  * `access` (Impact: 13.6)
  * `cache` (Impact: 11.7)
  * `set` (Impact: 8.9)
  * `get` (Impact: 5.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 20`, `args: 7`, `func_start: 7`
* *Risk/State:* `state_mutation: 54`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* `safety: 13`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` rnothtmlwhite.js, camelCase.js, core.js, acceptData.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/attributes/val.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.928 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.081 IQR)
- **Top Global Matches:** file_cluster_8: 11.928, file_cluster_13: 12.019, file_cluster_17: 12.178
- **Magnitude:** 122.74 | **LOC:** 170 | **CtrlFlow:** 61.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.1502%), Tech Debt (99.846%)
**Top Internal Functions/Classes:**
  * `val` (Impact: 45.0)
  * `get` (Impact: 21.5)
  * `set` (Impact: 8.0)
  * `get` (Impact: 4.6)
  * `set` (Impact: 3.7)
    * *Intent:* // Support: IE <=10 - 11+ // option.text throws exceptions (trac-14686, trac-14858) // Strip and col...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 22`, `args: 8`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 34`, `duplicate_logic: 4`
* *Architecture:* `import: 4`
* *Defense:* `safety: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` nodeName.js, core.js, isIE.js, stripAndCollapse.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/queue.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.485 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.709 IQR)
- **Top Global Matches:** file_cluster_8: 12.485, file_cluster_13: 12.637, file_cluster_11: 12.691
- **Magnitude:** 118.4 | **LOC:** 142 | **CtrlFlow:** 56.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (76.8525%), Tech Debt (99.9996%)
**Top Internal Functions/Classes:**
  * `queue` (Impact: 16.9)
  * `dequeue` (Impact: 13.8)
  * `promise` (Impact: 13.5)
    * *Intent:* // Get a promise resolved when queues of a certain type // are emptied (fx is the type by default)
  * `queue` (Impact: 11.7)
  * `clearQueue` (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 20`, `args: 12`, `func_start: 10`
* *Risk/State:* `state_mutation: 43`, `duplicate_logic: 6`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 10`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core.js, dataPriv.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/css.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.612 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.936 IQR)
- **Top Global Matches:** file_cluster_13: 11.612, file_cluster_8: 11.66, file_cluster_11: 12.083
- **Magnitude:** 110.48 | **LOC:** 405 | **CtrlFlow:** 58.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.7031%), Tech Debt (97.9147%)
**Top Internal Functions/Classes:**
  * `boxModelAdjustment` (Impact: 25.6)
  * `set` (Impact: 15.3)
    * *Intent:* // Make sure that we're working with the right name. We don't // want to query the value if it is a ...
  * `expand` (Impact: 10.7)
  * `setPositiveNumber` (Impact: 8.6)
  * `css` (Impact: 8.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 45`, `args: 10`, `func_start: 9`
* *Risk/State:* `state_mutation: 23`, `fragile_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `import: 16`
* *Defense:* `safety: 25`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core.js, rnumnonpx.js, isAutoPx.js, cssCamelCase.js, adjustCSS.js, finalPropName.js, getStyles.js, cssExpand.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/core/init.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 11.968 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.716 IQR)
- **Top Global Matches:** file_cluster_17: 11.968, file_cluster_13: 12.031, file_cluster_8: 12.206
- **Magnitude:** 109.68 | **LOC:** 123 | **CtrlFlow:** 64.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (86.7036%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `init` (Impact: 58.6)
  * `selector` (Impact: 29.8)
    * *Intent:* // Execute immediately if ready is not present
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 17`, `args: 1`, `func_start: 2`
* *Risk/State:* `state_mutation: 20`
* *Architecture:* `import: 4`
* *Defense:* `safety: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core.js, document.js, isObviousHtml.js, rsingleTag.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/selector-native.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.619 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.279 IQR)
- **Top Global Matches:** file_cluster_13: 10.619, file_cluster_8: 10.877, file_cluster_11: 11.165
- **Magnitude:** 109.34 | **LOC:** 152 | **CtrlFlow:** 52.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (50.6859%), Tech Debt (38.9166%)
**Top Internal Functions/Classes:**
  * `find` (Impact: 75.8)
  * `testContext` (Impact: 7.9)
  * `toSelector` (Impact: 2.4)
  * `matches` (Impact: 1.9)
  * `matchesSelector` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 31`, `args: 3`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 16`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 1`, `import: 13`
* *Defense:* `safety: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` matches.js, core.js, preFilter.js, rdescend.js, rsibling.js, document.js, toSelector.js, tokenize.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/manipulation/domManip.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.429 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.204 IQR)
- **Top Global Matches:** file_cluster_13: 10.429, file_cluster_8: 10.495, file_cluster_17: 10.718
- **Magnitude:** 95.76 | **LOC:** 108 | **CtrlFlow:** 57.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (26.8941%), Tech Debt (98.9557%)
**Top Internal Functions/Classes:**
  * `domManip` (Impact: 51.2)
  * `domManip` (Impact: 23.2)
  * `restoreScript` (Impact: 9.4)
  * `disableScript` (Impact: 2.4)
    * *Intent:* // Replace/restore the type attribute of script elements for safe DOM manipulation
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 17`, `args: 4`, `func_start: 5`
* *Risk/State:* `state_mutation: 7`, `duplicate_logic: 2`
* *Architecture:* `api: 1`, `import: 7`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dataPriv.js, flat.js, DOMEval.js, getAll.js, core.js, buildFragment.js, rscriptType.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/manipulation/buildFragment.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.596 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.683 IQR)
- **Top Global Matches:** file_cluster_13: 10.596, file_cluster_8: 10.984, file_cluster_11: 11.46
- **Magnitude:** 92.28 | **LOC:** 98 | **CtrlFlow:** 59.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.8594%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `buildFragment` (Impact: 65.4)
  * `setGlobalEval` (Impact: 5.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 17`, `args: 1`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 18`
* *Architecture:* `api: 2`, `import: 10`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` isArrayLike.js, setGlobalEval.js, getAll.js, rtagName.js, core.js, toType.js, wrapMap.js, isAttached.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/offset.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.988 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.547 IQR)
- **Top Global Matches:** file_cluster_8: 11.988, file_cluster_13: 11.995, file_cluster_17: 12.059
- **Magnitude:** 82.4 | **LOC:** 202 | **CtrlFlow:** 64.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (57.6663%), Tech Debt (24.2989%)
**Top Internal Functions/Classes:**
  * `setOffset` (Impact: 28.4)
  * `position` (Impact: 20.6)
  * `offsetParent` (Impact: 6.2)
    * *Intent:* // Account for the *real* offset parent, which can be the document or its root element
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 20`, `args: 7`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 24`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `safety: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core.js, isWindow.js, documentElement.js, access.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/traversing/findFilter.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.321 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.692 IQR)
- **Top Global Matches:** file_cluster_17: 13.321, file_cluster_13: 13.509, file_cluster_11: 13.535
- **Magnitude:** 78.6 | **LOC:** 92 | **CtrlFlow:** 41.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.7574%), Tech Debt (99.9968%)
**Top Internal Functions/Classes:**
  * `find` (Impact: 13.2)
  * `filter` (Impact: 10.8)
  * `winnow` (Impact: 9.2)
    * *Intent:* // Implement the identical functionality for filter and not
  * `is` (Impact: 8.6)
  * `filter` (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 24`, `args: 11`, `func_start: 6`
* *Risk/State:* `state_mutation: 27`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `import: 3`
* *Defense:* `safety: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` rneedsContext.js, core.js, indexOf.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/core/access.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.779 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 3.925 IQR)
- **Top Global Matches:** file_cluster_8: 9.779, file_cluster_13: 9.983, file_cluster_0: 10.508
- **Magnitude:** 77.8 | **LOC:** 64 | **CtrlFlow:** 63.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (26.0293%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `access` (Impact: 45.3)
    * *Intent:* // Multifunctional method to get and set values of a collection // The value/s can optionally be exe...
  * `access` (Impact: 21.9)
  * `fn` (Impact: 3.6)
  * `fn` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 8`, `args: 2`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`, `duplicate_logic: 4`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core.js, toType.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/data/Data.js` (JAVASCRIPT) | Magnitude: 128.58 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 75, state_mutation: 54, branch: 26, structural_boundaries: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/exports/global.js` (JAVASCRIPT) | Magnitude: 11.92 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 10, branch: 4, safety: 4, globals: 4
- `src/core/ready.js` (JAVASCRIPT) | Magnitude: 25.38 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 24, structural_boundaries: 9, branch: 7, globals: 7
- `src/deprecated.js` (JAVASCRIPT) | Magnitude: 24.9 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 20, structural_boundaries: 10, branch: 6, safety: 4
- `src/selector.js` (JAVASCRIPT) | Magnitude: 936.66 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 479, branch: 219, state_mutation: 103, structural_boundaries: 101
- `src/traversing.js` (JAVASCRIPT) | Magnitude: 142.3 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 121, state_mutation: 58, structural_boundaries: 45, branch: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/core/init.js` (JAVASCRIPT) | Magnitude: 109.68 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 56, branch: 31, state_mutation: 20, structural_boundaries: 17
- `src/core/parseXML.js` (JAVASCRIPT) | Magnitude: 22.62 | Delta: **0.086 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 18, branch: 8, structural_boundaries: 5, safety: 4
- `src/serialize.js` (JAVASCRIPT) | Magnitude: 154.04 | Delta: **0.179 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 78, state_mutation: 46, branch: 30, structural_boundaries: 27
- `src/traversing/findFilter.js` (JAVASCRIPT) | Magnitude: 78.6 | Delta: **0.188 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 60, state_mutation: 27, structural_boundaries: 24, branch: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/queue/delay.js` (JAVASCRIPT) | Magnitude: 21.36 | Delta: **0.407 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 8, state_mutation: 6, concurrency: 6, structural_boundaries: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/ajax/jsonp.js` (JAVASCRIPT) | Magnitude: 25.16 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 44, state_mutation: 21, branch: 20, structural_boundaries: 12
- `src/event/trigger.js` (JAVASCRIPT) | Magnitude: 183.3 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 118, branch: 54, state_mutation: 35, structural_boundaries: 21
- `src/offset.js` (JAVASCRIPT) | Magnitude: 82.4 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 97, branch: 36, state_mutation: 24, structural_boundaries: 20
- `src/css/adjustCSS.js` (JAVASCRIPT) | Magnitude: 61.32 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 41, branch: 21, structural_boundaries: 9, state_mutation: 6
- `src/selector/escapeSelector.js` (JAVASCRIPT) | Magnitude: 11.28 | Delta: **0.067 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 8, structural_boundaries: 6, sec_reflection_metaprogramming: 5, branch: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/wrapper-factory.js` (JAVASCRIPT) | Magnitude: 7.94 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 3, structural_boundaries: 2, args: 2, func_start: 2
- `src/wrapper-factory-esm.js` (JAVASCRIPT) | Magnitude: 7.68 | Delta: **0.081 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 3, args: 2, func_start: 2, dead_code: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `test/middleware-mockserver.cjs` -> **Apoorv Darshan** (100.0% isolated ownership) | Magnitude: 210.82
- `src/serialize.js` -> **Michał Gołębiowski-Owczarek** (100.0% isolated ownership) | Magnitude: 154.04
- `src/selector-native.js` -> **Michał Gołębiowski-Owczarek** (100.0% isolated ownership) | Magnitude: 109.34
- `src/selector/uniqueSort.js` -> **Michał Gołębiowski-Owczarek** (100.0% isolated ownership) | Magnitude: 75.96

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/css/finalPropName.js` -> **Severity: 662.3** (Blast Radius: 6.623 * Doc Risk: 100.0%)
- `src/css/adjustCSS.js` -> **Severity: 593.586** (Blast Radius: 6.623 * Doc Risk: 89.625%)
- `src/manipulation/buildFragment.js` -> **Severity: 511.024** (Blast Radius: 6.623 * Doc Risk: 77.159%)
- `src/manipulation/getAll.js` -> **Severity: 486.232** (Blast Radius: 6.623 * Doc Risk: 73.4156%)
- `src/core/DOMEval.js` -> **Severity: 474.493** (Blast Radius: 6.623 * Doc Risk: 71.6432%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
