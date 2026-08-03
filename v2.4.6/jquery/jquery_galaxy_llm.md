# ARCHITECTURAL_BRIEF: jquery
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_web/jquery` |
| **Timestamp** | `2026-08-03T20:05:36.095242+00:00` |
| **Scan Duration** | `0.43s` |
| **Git Branch** | `main` |
| **Git Commit** | `b43c8046f5196186fcba0860dae1680f42797f93` |
| **Git Remote** | `https://github.com/jquery/jquery.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 140 malicious artifacts.

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
| Cognitive Load Exposure | 3.9 | 93.1 | 25.4 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 91.3 | 18.8 | 16.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 23.0 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 15.8 | 1.6 | 80.0 |
| API Exposure | 0.0 | 9.2 | 4.3 | 5.8 | 5.8 |
| Concurrency Exposure | 0.0 | 100.0 | 5.5 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 82.5 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 72.9 | 0.9 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 60.1 | 66.7 | 100.0 |
| Instability Exposure | 0.0 | 3.3 | 0.1 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 43.2 | 2.2 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 31.5 | 20.0 | 13.3 |
| Algorithmic DoS Exposure | 0.0 | 99.8 | 0.9 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.8 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
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

- `trigger` (@ `src/event/trigger.js`) -> Impact: **244.0** | LOC: 139
- `remove` (@ `src/event.js`) -> Impact: **210.0** | LOC: 85
- `setMatcher` (@ `src/selector.js`) -> Impact: **184.8** | LOC: 98
- `ajax` (@ `src/ajax.js`) -> Impact: **163.7** | LOC: 225
- `find` (@ `src/selector-native.js`) -> Impact: **147.3** | LOC: 84
- `handlers` (@ `src/event.js`) -> Impact: **146.7** | LOC: 232
- `domManip` (@ `src/manipulation/domManip.js`) -> Impact: **145.1** | LOC: 84
- `Callbacks` (@ `src/callbacks.js`) -> Impact: **108.4** | LOC: 188
  * *Intent:* /*
- `matcherFromGroupMatchers` (@ `src/selector.js`) -> Impact: **98.5** | LOC: 168
- `matcherFromTokens` (@ `src/selector.js`) -> Impact: **92.8** | LOC: 67

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `domManip` (@ `src/manipulation/domManip.js`) -> **O(2^N) [Recursive]**
- `matcher` (@ `src/selector.js`) -> **O(2^N) [Recursive]**
- `ajax` (@ `src/ajax.js`) -> **O(2^N) [Recursive]**
- `canUseScriptTag` (@ `src/ajax/script.js`) -> **O(2^N) [Recursive]**
- `removeAttr` (@ `src/attributes/attr.js`) -> **O(2^N) [Recursive]**
- `attr` (@ `src/attributes/attr.js`) -> **O(2^N) [Recursive]**
- `removeClass` (@ `src/attributes/classes.js`) -> **O(2^N) [Recursive]**
- `addClass` (@ `src/attributes/classes.js`) -> **O(2^N) [Recursive]**
- `toggleClass` (@ `src/attributes/classes.js`) -> **O(2^N) [Recursive]**
- `prop` (@ `src/attributes/prop.js`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `run` (@ `src/effects/Tween.js`) -> DB Complexity: **16**
- `MockserverMiddlewareFactory` (@ `test/middleware-mockserver.cjs`) -> DB Complexity: **16**
- `handlers` (@ `src/event.js`) -> DB Complexity: **15**
- `init` (@ `src/effects/Tween.js`) -> DB Complexity: **9**
- `readFileSync` (@ `test/middleware-mockserver.cjs`) -> DB Complexity: **9**
  * *Intent:* /**
- `matcherFromGroupMatchers` (@ `src/selector.js`) -> DB Complexity: **8**
- `serializeArray` (@ `src/serialize.js`) -> DB Complexity: **8**
- `val` (@ `src/attributes/val.js`) -> DB Complexity: **7**
- `Callbacks` (@ `src/callbacks.js`) -> DB Complexity: **7**
  * *Intent:* /*
- `removeClass` (@ `src/attributes/classes.js`) -> DB Complexity: **6**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 11 | 5073.7 | 1.21% | 0.0% |
| `src` | 23 | 3899.02 | 44.17% | 41.12% |
| `src/attributes` | 4 | 466.68 | 63.98% | 74.95% |
| `src/core` | 15 | 432.26 | 27.71% | 39.57% |
| `src/var` | 26 | 344.06 | 5.0% | 0.0% |
| `src/manipulation` | 6 | 316.74 | 36.89% | 16.62% |
| `src/event` | 1 | 293.8 | 91.78% | 96.34% |
| `src/selector` | 11 | 282.92 | 31.48% | 18.18% |
| `test` | 1 | 228.02 | 7.4% | 0.0% |
| `src/css` | 8 | 215.94 | 39.33% | 12.5% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `src/core/isAttached.js` -> **100.0%** Exposure
- `src/core/readyException.js` -> **100.0%** Exposure
- `src/css/hiddenVisibleSelectors.js` -> **100.0%** Exposure
- `src/effects/animatedSelector.js` -> **100.0%** Exposure
- `src/wrapper-factory-esm.js` -> **99.9999%** Exposure
### Highest State Flux (Mutation/Volatility)
- `src/ajax/var/location.js` -> **100.0%** Exposure
- `src/ajax/var/nonce.js` -> **100.0%** Exposure
- `src/ajax/var/rquery.js` -> **100.0%** Exposure
- `src/attributes/classes.js` -> **100.0%** Exposure
- `src/core/isArrayLike.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `test/middleware-mockserver.cjs` -> **18** Orphaned Functions | **0** Duplicates
- `src/selector.js` -> **7** Orphaned Functions | **2** Duplicates
- `src/traversing.js` -> **7** Orphaned Functions | **0** Duplicates
- `src/deprecated/event.js` -> **5** Orphaned Functions | **0** Duplicates
- `src/manipulation.js` -> **1** Orphaned Functions | **4** Duplicates

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

### Exploit Generation Surface
- `src/selector.js` -> **100.0%** Exposure
- `src/ajax.js` -> **0.019%** Exposure
- `test/middleware-mockserver.cjs` -> **0.0002%** Exposure
### Weaponizable Injection Vectors
- `test/middleware-mockserver.cjs` -> **0.7516%** Exposure
### Algorithmic DoS Exposure
- `src/callbacks.js` -> **99.7861%** Exposure
- `src/manipulation/domManip.js` -> **8.3575%** Exposure
- `src/ajax.js` -> **3.9764%** Exposure
- `src/deferred.js` -> **2.9207%** Exposure
- `src/core/init.js` -> **2.1603%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `13` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/serialize.js` (JAVASCRIPT) -> Cumulative Risk: **528.15**
- **Archetype:** `file_cluster_17` (Distance: 12.88 IQR)
- **Magnitude:** 138.14 | **LOC:** 141 | **CtrlFlow:** 52.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (80.08%), Verification (80.0%)
- **Heaviest Functions:** `buildParams` (Impact: 55.5), `param` (Impact: 17.5), `serializeArray` (Impact: 14.7)

### 2. `src/attributes/val.js` (JAVASCRIPT) -> Cumulative Risk: **524.98**
- **Archetype:** `file_cluster_8` (Distance: 11.936 IQR)
- **Magnitude:** 161.14 | **LOC:** 170 | **CtrlFlow:** 61.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9913%), Tech Debt (99.846%), Verification (80.0%)
- **Heaviest Functions:** `val` (Impact: 87.0), `get` (Impact: 21.5), `set` (Impact: 8.0)

### 3. `src/effects/Tween.js` (JAVASCRIPT) -> Cumulative Risk: **510.89**
- **Archetype:** `file_cluster_13` (Distance: 13.485 IQR)
- **Magnitude:** 153.36 | **LOC:** 111 | **CtrlFlow:** 61.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (93.1016%), Safety Score (91.3204%)
- **Heaviest Functions:** `run` (Impact: 15.2), `set` (Impact: 14.8), `get` (Impact: 12.9)

### 4. `src/event/trigger.js` (JAVASCRIPT) -> Cumulative Risk: **508.07**
- **Archetype:** `file_cluster_8` (Distance: 11.637 IQR)
- **Magnitude:** 293.8 | **LOC:** 193 | **CtrlFlow:** 72.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9794%), Tech Debt (96.3358%), Cognitive Load (91.7818%)
- **Heaviest Functions:** `trigger` (Impact: 244.0), `triggerHandler` (Impact: 3.8), `trigger` (Impact: 3.7)

### 5. `src/core.js` (JAVASCRIPT) -> Cumulative Risk: **497.41**
- **Archetype:** `file_cluster_13` (Distance: 12.921 IQR)
- **Magnitude:** 297.12 | **LOC:** 420 | **CtrlFlow:** 46.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9977%), Tech Debt (83.2237%), Verification (80.0%)
- **Heaviest Functions:** `text` (Impact: 33.5), `extend` (Impact: 23.7), `each` (Impact: 16.6)

### 6. `src/manipulation.js` (JAVASCRIPT) -> Cumulative Risk: **496.92**
- **Archetype:** `file_cluster_13` (Distance: 13.259 IQR)
- **Magnitude:** 344.08 | **LOC:** 336 | **CtrlFlow:** 55.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (89.2686%), Verification (80.0%)
- **Heaviest Functions:** `clone` (Impact: 62.4), `html` (Impact: 29.9), `cleanData` (Impact: 28.6)

### 7. `src/queue.js` (JAVASCRIPT) -> Cumulative Risk: **494.4**
- **Archetype:** `file_cluster_8` (Distance: 12.498 IQR)
- **Magnitude:** 165.0 | **LOC:** 142 | **CtrlFlow:** 56.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9998%), Tech Debt (99.9649%), Verification (80.0%)
- **Heaviest Functions:** `queue` (Impact: 32.9), `dequeue` (Impact: 25.9), `promise` (Impact: 25.6)

### 8. `src/selector.js` (JAVASCRIPT) -> Cumulative Risk: **486.61**
- **Archetype:** `file_cluster_13` (Distance: 12.525 IQR)
- **Magnitude:** 712.46 | **LOC:** 1377 | **CtrlFlow:** 68.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), State Flux (99.4349%), Verification (80.0%)
- **Heaviest Functions:** `setMatcher` (Impact: 184.8), `matcherFromGroupMatchers` (Impact: 98.5), `matcherFromTokens` (Impact: 92.8)

### 9. `src/traversing.js` (JAVASCRIPT) -> Cumulative Risk: **486.57**
- **Archetype:** `file_cluster_13` (Distance: 12.875 IQR)
- **Magnitude:** 151.1 | **LOC:** 194 | **CtrlFlow:** 39.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Tech Debt (94.5687%), Verification (80.0%)
- **Heaviest Functions:** `index` (Impact: 12.9), `parent` (Impact: 12.2), `contents` (Impact: 11.0)

### 10. `src/selector/uniqueSort.js` (JAVASCRIPT) -> Cumulative Risk: **484.83**
- **Archetype:** `file_cluster_13` (Distance: 11.988 IQR)
- **Magnitude:** 77.36 | **LOC:** 99 | **CtrlFlow:** 45.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9621%), Safety Score (82.0135%)
- **Heaviest Functions:** `sortOrder` (Impact: 27.1), `uniqueSort` (Impact: 11.2), `uniqueSort` (Impact: 3.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
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
- **Global Archetype:** `file_cluster_13` (Drift: 12.525 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.841 IQR)
- **Top Global Matches:** file_cluster_13: 12.525, file_cluster_8: 12.542, file_cluster_11: 12.838
- **Magnitude:** 712.46 | **LOC:** 1377 | **CtrlFlow:** 68.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (39.3727%), Tech Debt (44.0384%)
**Top Internal Functions/Classes:**
  * `setMatcher` (Impact: 184.8 | O(2^N) | DB: 4)
  * `matcherFromGroupMatchers` (Impact: 98.5 | O(N^1) | DB: 8)
  * `matcherFromTokens` (Impact: 92.8 | O(2^N) | DB: 3)
  * `find` (Impact: 52.4 | O(N^1) | DB: 2)
  * `createDisabledPseudo` (Impact: 27.0 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 219`, `structural_boundaries: 101`, `args: 35`, `func_start: 46`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 103`, `duplicate_logic: 2`, `orphaned_logic: 7`
* *Architecture:* `api: 1`, `import: 23`
* *Defense:* `safety: 46`, `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` identifier.js, filterMatchExpr.js, selectorError.js, rsibling.js, rleadingCombinator.js, unescapeSelector.js, push.js, nodeName.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/event.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.373 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.969 IQR)
- **Top Global Matches:** file_cluster_8: 12.373, file_cluster_13: 12.497, file_cluster_11: 12.69
- **Magnitude:** 556.28 | **LOC:** 881 | **CtrlFlow:** 70.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (55.7879%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `remove` (Impact: 210.0 | O(2^N) | DB: 3)
  * `handlers` (Impact: 146.7 | O(2^N) | DB: 15)
  * `add` (Impact: 65.6 | O(N^1) | DB: 4)
  * `on` (Impact: 45.3 | O(N^1) | DB: 1)
  * `returnTrue` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 50`, `args: 23`, `func_start: 24`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 77`
* *Architecture:* `api: 1`, `import: 9`
* *Defense:* `safety: 34`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` rnothtmlwhite.js, slice.js, isIE.js, documentElement.js, rcheckableType.js, nodeName.js, acceptData.js, core.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ajax.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.735 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.297 IQR)
- **Top Global Matches:** file_cluster_8: 11.735, file_cluster_13: 12.034, file_cluster_11: 12.26
- **Magnitude:** 361.62 | **LOC:** 889 | **CtrlFlow:** 69.9% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (39.2239%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ajax` (Impact: 163.7 | O(2^N) | DB: 3)
  * `ajaxHandleResponses` (Impact: 78.6 | O(N^2) | DB: 3)
  * `addToPrefiltersOrTransports` (Impact: 24.0 | O(N^1) | DB: 3)
    * *Intent:* /* Transports bindings * 1) key is the dataType * 2) the catchall symbol "*" can be used * 3) select...
  * `inspectPrefiltersOrTransports` (Impact: 21.4 | O(N^1) | DB: 4)
  * `ajaxExtend` (Impact: 12.9 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 41`, `args: 15`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 48`
* *Architecture:* `api: 2`, `concurrency: 1`, `import: 6`
* *Defense:* `safety: 33`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` rnothtmlwhite.js, createElement.js, core.js, location.js, rquery.js, nonce.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/effects.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.038 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.815 IQR)
- **Top Global Matches:** file_cluster_8: 12.038, file_cluster_13: 12.151, file_cluster_17: 12.341
- **Magnitude:** 360.66 | **LOC:** 688 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (46.7029%), Tech Debt (19.7916%)
**Top Internal Functions/Classes:**
  * `speed` (Impact: 78.2 | O(2^N) | DB: 1)
  * `Animation` (Impact: 65.0 | O(2^N) | DB: 4)
  * `finish` (Impact: 50.0 | O(2^N) | DB: 3)
  * `schedule` (Impact: 17.9 | O(2^N))
  * `createTween` (Impact: 15.1 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 54`, `args: 27`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 71`, `orphaned_logic: 3`
* *Architecture:* `api: 1`, `concurrency: 4`, `import: 10`
* *Defense:* `safety: 24`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` rnothtmlwhite.js, adjustCSS.js, cssCamelCase.js, showHide.js, isHiddenWithinTree.js, rcssNum.js, core.js, dataPriv.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/manipulation.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.259 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.106 IQR)
- **Top Global Matches:** file_cluster_13: 13.259, file_cluster_8: 13.367, file_cluster_11: 13.448
- **Magnitude:** 344.08 | **LOC:** 336 | **CtrlFlow:** 55.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (79.1391%), Tech Debt (89.2686%)
**Top Internal Functions/Classes:**
  * `clone` (Impact: 62.4 | O(2^N) | DB: 1)
  * `html` (Impact: 29.9 | O(N^1) | DB: 3)
  * `cleanData` (Impact: 28.6 | O(N^2) | DB: 1)
  * `text` (Impact: 20.6 | O(2^N) | DB: 5)
  * `remove` (Impact: 17.0 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 57`, `args: 28`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 111`, `duplicate_logic: 4`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `import: 14`
* *Defense:* `safety: 25`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` access.js, isIE.js, dataUser.js, push.js, isAttached.js, rtagName.js, wrapMap.js, acceptData.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/core.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.921 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.185 IQR)
- **Top Global Matches:** file_cluster_13: 12.921, file_cluster_11: 13.026, file_cluster_8: 13.196
- **Magnitude:** 297.12 | **LOC:** 420 | **CtrlFlow:** 46.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (69.9254%), Tech Debt (83.2237%)
**Top Internal Functions/Classes:**
  * `text` (Impact: 33.5 | O(2^N) | DB: 1)
  * `extend` (Impact: 23.7 | O(N^1) | DB: 1)
  * `each` (Impact: 16.6 | O(N^1) | DB: 1)
  * `map` (Impact: 15.5 | O(N^1) | DB: 3)
  * `isPlainObject` (Impact: 13.0 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 73`, `args: 31`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 83`, `dead_code: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 12`, `import: 14`
* *Defense:* `safety: 26`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` slice.js, isArrayLike.js, class2type.js, fnToString.js, ObjectFunctionString.js, toString.js, flat.js, support.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/event/trigger.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.637 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.212 IQR)
- **Top Global Matches:** file_cluster_8: 11.637, file_cluster_13: 11.639, file_cluster_11: 11.994
- **Magnitude:** 293.8 | **LOC:** 193 | **CtrlFlow:** 72.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (91.7818%), Tech Debt (96.3358%)
**Top Internal Functions/Classes:**
  * `trigger` (Impact: 244.0 | O(2^N) | DB: 6)
  * `triggerHandler` (Impact: 3.8 | O(N^1) | DB: 1)
  * `trigger` (Impact: 3.7 | O(2^N) | DB: 1)
  * `simulate` (Impact: 2.6 | O(N^1) | DB: 1)
  * `stopPropagationCallback` (Impact: 2.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 21`, `args: 6`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 35`, `duplicate_logic: 2`, `orphaned_logic: 2`
* *Architecture:* `import: 6`
* *Defense:* `safety: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` document.js, hasOwn.js, dataPriv.js, core.js, acceptData.js, isWindow.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/middleware-mockserver.cjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.121 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 5.035 IQR)
- **Top Global Matches:** file_cluster_8: 10.121, file_cluster_15: 10.642, file_cluster_7: 10.701
- **Magnitude:** 228.02 | **LOC:** 426 | **CtrlFlow:** 77.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (7.4036%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `jsonp` (Impact: 21.2 | O(N^1) | DB: 5)
  * `json` (Impact: 18.3 | O(2^N) | DB: 4)
  * `readFileSync` (Impact: 13.8 | O(2^N) | DB: 9)
    * *Intent:* /**
  * `etag` (Impact: 11.0 | O(2^N))
  * `wait` (Impact: 10.8 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 18`, `args: 51`, `func_start: 46`
* *Risk/State:* `state_mutation: 8`, `orphaned_logic: 18`
* *Architecture:* `io: 10`, `api: 1`, `concurrency: 18`, `import: 4`
* *Defense:* `safety: 14`, `doc: 8`, `test: 4`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` raw-body, node:fs, multiparty, node:url
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/attributes/classes.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.004 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.745 IQR)
- **Top Global Matches:** file_cluster_8: 13.004, file_cluster_13: 13.139, file_cluster_11: 13.218
- **Magnitude:** 182.96 | **LOC:** 157 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (77.8032%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `removeClass` (Impact: 38.1 | O(2^N) | DB: 6)
  * `addClass` (Impact: 33.8 | O(2^N) | DB: 5)
  * `toggleClass` (Impact: 29.7 | O(2^N) | DB: 5)
  * `classesToArray` (Impact: 9.4 | O(N^1))
  * `hasClass` (Impact: 8.7 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 30`, `args: 12`, `func_start: 6`
* *Risk/State:* `state_mutation: 54`
* *Architecture:* `import: 3`
* *Defense:* `safety: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stripAndCollapse.js, rnothtmlwhite.js, core.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/selector-native.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.653 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.279 IQR)
- **Top Global Matches:** file_cluster_13: 10.653, file_cluster_8: 10.912, file_cluster_11: 11.196
- **Magnitude:** 170.54 | **LOC:** 152 | **CtrlFlow:** 52.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (31.6373%), Tech Debt (38.9166%)
**Top Internal Functions/Classes:**
  * `find` (Impact: 147.3 | O(2^N) | DB: 2)
  * `matches` (Impact: 1.9 | O(N^1))
  * `matchesSelector` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 31`, `args: 3`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 16`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 1`, `import: 13`
* *Defense:* `safety: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` rdescend.js, isIE.js, rsibling.js, preFilter.js, toSelector.js, rleadingCombinator.js, whitespace.js, tokenize.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/manipulation/domManip.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.482 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.896 IQR)
- **Top Global Matches:** file_cluster_13: 10.482, file_cluster_8: 10.531, file_cluster_17: 10.78
- **Magnitude:** 166.46 | **LOC:** 108 | **CtrlFlow:** 57.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (26.8941%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `domManip` (Impact: 145.1 | O(2^N) | DB: 2)
  * `restoreScript` (Impact: 9.4 | O(N^1))
  * `disableScript` (Impact: 2.4 | O(N^1))
    * *Intent:* // Replace/restore the type attribute of script elements for safe DOM manipulation
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 17`, `args: 4`, `func_start: 5`
* *Risk/State:* `state_mutation: 7`
* *Architecture:* `api: 1`, `import: 7`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dataPriv.js, getAll.js, core.js, flat.js, rscriptType.js, buildFragment.js, DOMEval.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/queue.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.498 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.487 IQR)
- **Top Global Matches:** file_cluster_8: 12.498, file_cluster_13: 12.652, file_cluster_11: 12.704
- **Magnitude:** 165.0 | **LOC:** 142 | **CtrlFlow:** 56.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (76.8525%), Tech Debt (99.9649%)
**Top Internal Functions/Classes:**
  * `queue` (Impact: 32.9 | O(2^N) | DB: 2)
  * `dequeue` (Impact: 25.9 | O(2^N) | DB: 4)
  * `promise` (Impact: 25.6 | O(2^N) | DB: 2)
    * *Intent:* // Get a promise resolved when queues of a certain type // are emptied (fx is the type by default)
  * `queue` (Impact: 22.1 | O(2^N) | DB: 3)
  * `dequeue` (Impact: 4.2 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 20`, `args: 12`, `func_start: 10`
* *Risk/State:* `state_mutation: 43`, `duplicate_logic: 4`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 10`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core.js, dataPriv.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/attributes/val.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.936 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.081 IQR)
- **Top Global Matches:** file_cluster_8: 11.936, file_cluster_13: 12.027, file_cluster_17: 12.185
- **Magnitude:** 161.14 | **LOC:** 170 | **CtrlFlow:** 61.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (68.1502%), Tech Debt (99.846%)
**Top Internal Functions/Classes:**
  * `val` (Impact: 87.0 | O(2^N) | DB: 7)
  * `get` (Impact: 21.5 | O(N^1) | DB: 2)
  * `set` (Impact: 8.0 | O(N^1) | DB: 1)
  * `get` (Impact: 4.6 | O(N^1) | DB: 1)
  * `set` (Impact: 3.7 | O(N^1))
    * *Intent:* // Support: IE <=10 - 11+ // option.text throws exceptions (trac-14686, trac-14858) // Strip and col...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 22`, `args: 8`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 34`, `duplicate_logic: 4`
* *Architecture:* `import: 4`
* *Defense:* `safety: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stripAndCollapse.js, isIE.js, nodeName.js, core.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/effects/Tween.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.485 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.753 IQR)
- **Top Global Matches:** file_cluster_13: 13.485, file_cluster_8: 13.517, file_cluster_11: 13.517
- **Magnitude:** 153.36 | **LOC:** 111 | **CtrlFlow:** 61.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (93.1016%), Tech Debt (33.3417%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 15.2 | O(N^1) | DB: 16)
  * `set` (Impact: 14.8 | O(N^1))
  * `get` (Impact: 12.9 | O(N^1) | DB: 1)
  * `init` (Impact: 11.0 | O(N^1) | DB: 9)
  * `Tween` (Impact: 5.0 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 14`, `args: 8`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 84`, `orphaned_logic: 1`
* *Architecture:* `import: 3`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` isAutoPx.js, finalPropName.js, core.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/traversing.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.875 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.649 IQR)
- **Top Global Matches:** file_cluster_13: 12.875, file_cluster_17: 12.907, file_cluster_8: 12.915
- **Magnitude:** 151.1 | **LOC:** 194 | **CtrlFlow:** 39.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (70.8005%), Tech Debt (94.5687%)
**Top Internal Functions/Classes:**
  * `index` (Impact: 12.9 | O(N^1) | DB: 1)
  * `parent` (Impact: 12.2 | O(2^N) | DB: 1)
  * `contents` (Impact: 11.0 | O(N^1))
  * `siblings` (Impact: 8.2 | O(2^N))
  * `closest` (Impact: 7.7 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 45`, `args: 21`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 58`, `orphaned_logic: 7`
* *Architecture:* `api: 1`, `import: 7`
* *Defense:* `safety: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dir.js, getProto.js, rneedsContext.js, nodeName.js, siblings.js, core.js, indexOf.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/callbacks.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.35 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.835 IQR)
- **Top Global Matches:** file_cluster_8: 11.35, file_cluster_13: 11.606, file_cluster_15: 11.782
- **Magnitude:** 143.78 | **LOC:** 231 | **CtrlFlow:** 61.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (44.021%), Tech Debt (20.7969%)
**Top Internal Functions/Classes:**
  * `Callbacks` (Impact: 108.4 | O(N^2) | DB: 7)
    * *Intent:* /*
  * `createOptions` (Impact: 4.8 | O(N^1) | DB: 1)
    * *Intent:* // Convert String-formatted options into Object-formatted ones
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 21`, `args: 18`, `func_start: 19`
* *Risk/State:* `state_mutation: 27`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 6`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` rnothtmlwhite.js, core.js, toType.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/serialize.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.88 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.298 IQR)
- **Top Global Matches:** file_cluster_17: 12.88, file_cluster_8: 13.041, file_cluster_13: 13.043
- **Magnitude:** 138.14 | **LOC:** 141 | **CtrlFlow:** 52.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (80.08%), Tech Debt (29.5345%)
**Top Internal Functions/Classes:**
  * `buildParams` (Impact: 55.5 | O(2^N) | DB: 1)
  * `param` (Impact: 17.5 | O(N^1) | DB: 4)
    * *Intent:* // Serialize an array of form elements or a set of // key/values into a query string
  * `serializeArray` (Impact: 14.7 | O(N^1) | DB: 8)
  * `serialize` (Impact: 1.6 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 27`, `args: 11`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 46`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core.js, rcheckableType.js, toType.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/data/Data.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.286 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.168 IQR)
- **Top Global Matches:** file_cluster_11: 14.286, file_cluster_13: 14.304, file_cluster_17: 14.315
- **Magnitude:** 130.28 | **LOC:** 156 | **CtrlFlow:** 56.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (85.9304%), Tech Debt (47.0273%)
**Top Internal Functions/Classes:**
  * `remove` (Impact: 23.1 | O(N^1) | DB: 4)
  * `access` (Impact: 13.6 | O(N^1) | DB: 2)
  * `cache` (Impact: 11.7 | O(N^1) | DB: 4)
  * `set` (Impact: 8.9 | O(N^1) | DB: 2)
  * `get` (Impact: 5.5 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 20`, `args: 7`, `func_start: 7`
* *Risk/State:* `state_mutation: 54`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* `safety: 13`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` acceptData.js, camelCase.js, rnothtmlwhite.js, core.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/css.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.638 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.88 IQR)
- **Top Global Matches:** file_cluster_13: 11.638, file_cluster_8: 11.677, file_cluster_11: 12.104
- **Magnitude:** 109.58 | **LOC:** 405 | **CtrlFlow:** 58.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (36.7031%), Tech Debt (47.0273%)
**Top Internal Functions/Classes:**
  * `boxModelAdjustment` (Impact: 25.6 | O(N^1) | DB: 1)
  * `set` (Impact: 15.3 | O(N^1) | DB: 1)
    * *Intent:* // Make sure that we're working with the right name. We don't // want to query the value if it is a ...
  * `css` (Impact: 15.0 | O(2^N) | DB: 1)
  * `expand` (Impact: 10.7 | O(N^1) | DB: 1)
  * `setPositiveNumber` (Impact: 8.6 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 45`, `args: 10`, `func_start: 9`
* *Risk/State:* `state_mutation: 23`, `fragile_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `import: 16`
* *Defense:* `safety: 25`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` adjustCSS.js, access.js, isIE.js, cssCamelCase.js, rnumnonpx.js, isAutoPx.js, support.js, curCSS.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/core/init.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 11.996 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.716 IQR)
- **Top Global Matches:** file_cluster_17: 11.996, file_cluster_13: 12.058, file_cluster_8: 12.235
- **Magnitude:** 106.78 | **LOC:** 123 | **CtrlFlow:** 64.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (86.7036%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `init` (Impact: 85.5 | O(N^2) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 17`, `args: 1`, `func_start: 2`
* *Risk/State:* `state_mutation: 20`
* *Architecture:* `import: 4`
* *Defense:* `safety: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` isObviousHtml.js, document.js, rsingleTag.js, core.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/offset.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.988 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.547 IQR)
- **Top Global Matches:** file_cluster_8: 11.988, file_cluster_13: 11.995, file_cluster_17: 12.059
- **Magnitude:** 106.5 | **LOC:** 202 | **CtrlFlow:** 64.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (57.6663%), Tech Debt (24.2989%)
**Top Internal Functions/Classes:**
  * `position` (Impact: 39.0 | O(2^N) | DB: 2)
  * `setOffset` (Impact: 28.4 | O(N^1) | DB: 1)
  * `offsetParent` (Impact: 11.9 | O(2^N) | DB: 3)
    * *Intent:* // Account for the *real* offset parent, which can be the document or its root element
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 20`, `args: 7`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 24`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `safety: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` access.js, core.js, documentElement.js, isWindow.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/core/access.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.886 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.382 IQR)
- **Top Global Matches:** file_cluster_8: 9.886, file_cluster_13: 10.117, file_cluster_0: 10.64
- **Magnitude:** 92.7 | **LOC:** 64 | **CtrlFlow:** 63.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (26.0293%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `access` (Impact: 87.8 | O(2^N) | DB: 1)
    * *Intent:* // Multifunctional method to get and set values of a collection // The value/s can optionally be exe...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 8`, `args: 2`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` toType.js, core.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/traversing/findFilter.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.321 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.692 IQR)
- **Top Global Matches:** file_cluster_17: 13.321, file_cluster_13: 13.509, file_cluster_11: 13.535
- **Magnitude:** 90.5 | **LOC:** 92 | **CtrlFlow:** 41.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (74.7574%), Tech Debt (99.9968%)
**Top Internal Functions/Classes:**
  * `find` (Impact: 25.1 | O(2^N) | DB: 4)
  * `filter` (Impact: 10.8 | O(N^1) | DB: 1)
  * `winnow` (Impact: 9.2 | O(N^1))
    * *Intent:* // Implement the identical functionality for filter and not
  * `is` (Impact: 8.6 | O(N^1))
  * `filter` (Impact: 4.2 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 24`, `args: 11`, `func_start: 6`
* *Risk/State:* `state_mutation: 27`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `import: 3`
* *Defense:* `safety: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` rneedsContext.js, indexOf.js, core.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/manipulation/buildFragment.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.669 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.683 IQR)
- **Top Global Matches:** file_cluster_13: 10.669, file_cluster_8: 11.058, file_cluster_11: 11.526
- **Magnitude:** 86.68 | **LOC:** 98 | **CtrlFlow:** 59.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (77.73%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `buildFragment` (Impact: 65.4 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 17`, `args: 1`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 18`
* *Architecture:* `api: 2`, `import: 10`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` toType.js, getAll.js, core.js, wrapMap.js, isAttached.js, isArrayLike.js, arr.js, setGlobalEval.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/data/Data.js` (JAVASCRIPT) | Magnitude: 130.28 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 75, state_mutation: 54, branch: 26, structural_boundaries: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/deprecated.js` (JAVASCRIPT) | Magnitude: 30.5 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 20, structural_boundaries: 10, branch: 6, safety: 4
- `src/exports/global.js` (JAVASCRIPT) | Magnitude: 11.92 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 10, branch: 4, safety: 4, globals: 4
- `src/selector.js` (JAVASCRIPT) | Magnitude: 712.46 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 479, branch: 219, state_mutation: 103, structural_boundaries: 101
- `src/core/ready.js` (JAVASCRIPT) | Magnitude: 27.08 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 24, structural_boundaries: 9, branch: 7, globals: 7
- `src/effects/Tween.js` (JAVASCRIPT) | Magnitude: 153.36 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 84, indent_tabs: 67, branch: 22, structural_boundaries: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/core/init.js` (JAVASCRIPT) | Magnitude: 106.78 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 56, branch: 31, state_mutation: 20, structural_boundaries: 17
- `src/core/parseXML.js` (JAVASCRIPT) | Magnitude: 22.62 | Delta: **0.086 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 18, branch: 8, structural_boundaries: 5, safety: 4
- `src/serialize.js` (JAVASCRIPT) | Magnitude: 138.14 | Delta: **0.161 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 78, state_mutation: 46, branch: 30, structural_boundaries: 27
- `src/traversing/findFilter.js` (JAVASCRIPT) | Magnitude: 90.5 | Delta: **0.188 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 60, state_mutation: 27, structural_boundaries: 24, branch: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/queue/delay.js` (JAVASCRIPT) | Magnitude: 19.76 | Delta: **0.412 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 8, state_mutation: 6, concurrency: 6, structural_boundaries: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/event/trigger.js` (JAVASCRIPT) | Magnitude: 293.8 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 118, branch: 54, state_mutation: 35, structural_boundaries: 21
- `src/ajax/jsonp.js` (JAVASCRIPT) | Magnitude: 25.16 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 44, state_mutation: 21, branch: 20, structural_boundaries: 12
- `src/offset.js` (JAVASCRIPT) | Magnitude: 106.5 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 97, branch: 36, state_mutation: 24, structural_boundaries: 20
- `src/css/adjustCSS.js` (JAVASCRIPT) | Magnitude: 61.32 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 41, branch: 21, structural_boundaries: 9, state_mutation: 6
- `src/selector/escapeSelector.js` (JAVASCRIPT) | Magnitude: 11.28 | Delta: **0.067 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 8, structural_boundaries: 6, sec_reflection_metaprogramming: 5, branch: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/wrapper-factory.js` (JAVASCRIPT) | Magnitude: 7.94 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 3, structural_boundaries: 2, args: 2, func_start: 2
- `src/wrapper-factory-esm.js` (JAVASCRIPT) | Magnitude: 7.68 | Delta: **0.081 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 3, args: 2, func_start: 2, dead_code: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `test/middleware-mockserver.cjs` -> **Apoorv Darshan** (100.0% isolated ownership) | Magnitude: 228.02
- `src/selector-native.js` -> **Michał Gołębiowski-Owczarek** (100.0% isolated ownership) | Magnitude: 170.54
- `src/serialize.js` -> **Michał Gołębiowski-Owczarek** (100.0% isolated ownership) | Magnitude: 138.14
- `src/selector/uniqueSort.js` -> **Michał Gołębiowski-Owczarek** (100.0% isolated ownership) | Magnitude: 77.36

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/css/finalPropName.js` -> **Severity: 662.3** (Blast Radius: 6.623 * Doc Risk: 100.0%)
- `src/selector/unescapeSelector.js` -> **Severity: 656.277** (Blast Radius: 6.623 * Doc Risk: 99.0906%)
- `src/manipulation/getAll.js` -> **Severity: 655.468** (Blast Radius: 6.623 * Doc Risk: 98.9685%)
- `src/core/DOMEval.js` -> **Severity: 646.542** (Blast Radius: 6.623 * Doc Risk: 97.6207%)
- `src/selector/filterMatchExpr.js` -> **Severity: 639.487** (Blast Radius: 6.623 * Doc Risk: 96.5555%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
