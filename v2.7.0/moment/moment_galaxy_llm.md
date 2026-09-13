# ARCHITECTURAL_BRIEF: moment
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/moment/moment.git` |
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
| Total Artifacts | 795 |
| Analyzed Artifacts (Scanned) | 637 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 158 |
| Total LOC | 157333 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 80.1% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5471 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.573 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.3227 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 15 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 620 | 155001 | 97.3% |
| JSON | 6 | 239 | 0.9% |
| MARKDOWN | 5 | 0 | 0.8% |
| TYPESCRIPT | 4 | 2056 | 0.6% |
| PLAINTEXT | 1 | 0 | 0.2% |
| SHELL | 1 | 37 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 631 | 99.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 6 | 0.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 158*

**Composition by Extension & Reason:**
- `.js`: 141x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 149293 LOC exceeds safe regex boundaries)
- `no_extension`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.map`: 3x Excluded (Unsupported Extension: '.map')
- `.json`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 12060 LOC)
- `.md`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.nuspec`: 1x Excluded (Unsupported Extension: '.nuspec')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 92.8 | 15.3 | 10.8 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 38.9 | 42.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 26.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 10.1 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 91.1 | 6.7 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 98.8 | 2.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 24.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 40.2 | 0.5 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 85.4 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 84.4 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1 | 1 | 0 | `src/test/moment/is_number.js` |
| cleanup | 2 | 1 | 0 | `scripts/npm_prepublish.sh` |
| guards | 3989 | 341 | 12 | `min/moment-with-locales.js` |
| danger | 852 | 83 | 1 | `src/test/moment/create.js` |
| concurrency | 54 | 18 | 0 | `tasks/transpile.js` |
| connectivity | 594 | 284 | 1 | `moment.d.ts` |
| io | 22 | 3 | 0 | `tasks/transpile.js` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 1146 | 182 | 1 | `src/test/moment/is_between.js` |
| serialization | 10 | 4 | 0 | `src/test/moment/format.js` |
| regex | 3957 | 440 | 7 | `min/moment-with-locales.js` |
| events | 238 | 24 | 0 | `src/test/moment/is_between.js` |
| tests | 19929 | 193 | 109 | `src/test/moment/duration.js` |
| docs | 74 | 11 | 0 | `moment.d.ts` |
| debt | 217 | 35 | 0 | `min/moment-with-locales.js` |
| mutation | 23850 | 546 | 92 | `min/moment-with-locales.js` |
| dead_code | 786 | 266 | 4 | `moment.d.ts` |
| credential | 0 | 0 | 0 | - |
| threat | 377 | 66 | 1 | `min/moment-with-locales.js` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tasks/transpile.js` (Hits: 11)
- `scripts/locales.js` (Hits: 9)
- `scripts/npm_prepublish.sh` (Hits: 2)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **qunit.js** (`src/test/qunit.js`) — 192 inbound connections
2. **qunit-locale.js** (`src/test/qunit-locale.js`) — 138 inbound connections
3. **format.js** (`src/lib/format/format.js`) — 19 inbound connections
4. **hooks.js** (`src/lib/utils/hooks.js`) — 18 inbound connections
5. **to-int.js** (`src/lib/utils/to-int.js`) — 17 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **prototype.js** (`src/lib/moment/prototype.js`) — 32 outbound dependencies
2. **from-anything.js** (`src/lib/create/from-anything.js`) — 17 outbound dependencies
3. **month.js** (`src/lib/units/month.js`) — 15 outbound dependencies
4. **offset.js** (`src/lib/units/offset.js`) — 15 outbound dependencies
5. **prototype.js** (`src/lib/locale/prototype.js`) — 13 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `processRelativeTime` (@ `locale/sl.js`) -> Impact: **225.5** | LOC: 83
  * *Intent:* //! moment.js locale configuration
- `processRelativeTime` (@ `src/locale/sl.js`) -> Impact: **225.5** | LOC: 83
- `translate` (@ `locale/is.js`) -> Impact: **115.6** | LOC: 75
- `translate` (@ `src/locale/is.js`) -> Impact: **115.6** | LOC: 75
- `translate` (@ `locale/cs.js`) -> Impact: **114.5** | LOC: 53
- `translate` (@ `locale/sk.js`) -> Impact: **114.5** | LOC: 53
- `translate` (@ `src/locale/cs.js`) -> Impact: **114.5** | LOC: 53
- `translate` (@ `src/locale/sk.js`) -> Impact: **114.5** | LOC: 53
- `processRelativeTime$9` (@ `min/locales.js`) -> Impact: **103.2** | LOC: 83
  * *Intent:* //! moment.js locale configuration
- `processRelativeTime$9` (@ `min/moment-with-locales.js`) -> Impact: **103.2** | LOC: 83
  * *Intent:* //! moment.js locale configuration

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `min` | 2 | 10256.06 | 22.62% | 15.63% |
| `__monolith__` | 14 | 4184.8 | 7.14% | 16.37% |
| `meteor` | 5 | 4059.64 | 15.98% | 1.7% |
| `src/test/moment` | 52 | 2200.54 | 4.31% | 0.0% |
| `src/lib/units` | 21 | 1506.78 | 26.39% | 3.0% |
| `src/lib/moment` | 19 | 1003.64 | 41.46% | 9.05% |
| `src/lib/create` | 12 | 875.82 | 55.19% | 33.86% |
| `src/lib/parse` | 2 | 709.34 | 52.17% | 0.0% |
| `src/lib/duration` | 13 | 664.14 | 39.27% | 0.0% |
| `src/lib/utils` | 27 | 348.18 | 20.22% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `benchmarks/query.js` -> **100.0%** Exposure
- `moment.d.ts` -> **100.0%** Exposure
- `ts3.1-typings/moment.d.ts` -> **100.0%** Exposure
- `benchmarks/isObjectEmpty.js` -> **99.9975%** Exposure
- `src/locale/gl.js` -> **99.921%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `meteor/moment.js` -> **100.0%** Exposure
- `moment.js` -> **100.0%** Exposure
- `src/lib/create/from-anything.js` -> **100.0%** Exposure
- `src/lib/create/from-array.js` -> **100.0%** Exposure
- `src/lib/create/from-string-and-array.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `moment.d.ts` -> **67** Orphaned Functions | **26** Duplicates
- `ts3.1-typings/moment.d.ts` -> **65** Orphaned Functions | **26** Duplicates
- `min/moment-with-locales.js` -> **2** Orphaned Functions | **29** Duplicates
- `min/locales.js` -> **0** Orphaned Functions | **29** Duplicates
- `benchmarks/query.js` -> **0** Orphaned Functions | **6** Duplicates

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
- **Unknown Dependencies:** `25` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/lib/moment/get-set.js` (JAVASCRIPT) -> Cumulative Risk: **639.04**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 139.5 | **LOC:** 118 | **CtrlFlow:** 45.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9994%), Safety Score (93.9913%)
- **Heaviest Functions:** `set` (Impact: 42.0), `get` (Impact: 36.1), `stringSet` (Impact: 9.5)

### 2. `tasks/qtest.js` (JAVASCRIPT) -> Cumulative Risk: **635.65**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 46.56 | **LOC:** 57 | **CtrlFlow:** 15.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (89.4446%)
- **Heaviest Functions:** `exports` (Impact: 15.5)

### 3. `tasks/transpile.js` (JAVASCRIPT) -> Cumulative Risk: **635.31**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 232.66 | **LOC:** 363 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (96.5501%), Concurrency (84.9999%)
- **Heaviest Functions:** `exports` (Impact: 54.9), `transpile` (Impact: 12.6), `generateLocales` (Impact: 11.6)

### 4. `src/lib/units/month.js` (JAVASCRIPT) -> Cumulative Risk: **633.34**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 294.74 | **LOC:** 341 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (89.7806%)
- **Heaviest Functions:** `localeMonthsParse` (Impact: 38.6), `handleStrictParse` (Impact: 32.3), `setMonth` (Impact: 15.2)

### 5. `src/lib/create/from-array.js` (JAVASCRIPT) -> Cumulative Risk: **617.51**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 178.8 | **LOC:** 188 | **CtrlFlow:** 30.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.1207%)
- **Heaviest Functions:** `configFromArray` (Impact: 38.3), `dayOfYearFromWeekInfo` (Impact: 31.3), `currentDateArray` (Impact: 3.4)

### 6. `src/lib/units/day-of-week.js` (JAVASCRIPT) -> Cumulative Risk: **616.64**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 386.58 | **LOC:** 433 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Cognitive Load (87.7387%)
- **Heaviest Functions:** `handleStrictParse` (Impact: 53.6), `localeWeekdaysParse` (Impact: 51.3), `weekdaysRegex` (Impact: 13.7)

### 7. `src/lib/create/from-string-and-format.js` (JAVASCRIPT) -> Cumulative Risk: **614.86**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 118.9 | **LOC:** 136 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (95.4616%)
- **Heaviest Functions:** `configFromStringAndFormat` (Impact: 31.3), `meridiemFixWrap` (Impact: 21.2), `ISO_8601` (Impact: 1.1)

### 8. `src/lib/units/offset.js` (JAVASCRIPT) -> Cumulative Risk: **604.96**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 203.3 | **LOC:** 250 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9998%), Safety Score (88.6667%)
- **Heaviest Functions:** `getSetOffset` (Impact: 42.1), `offsetFromString` (Impact: 12.9), `cloneWithOffset` (Impact: 9.5)

### 9. `meteor/moment.js` (JAVASCRIPT) -> Cumulative Risk: **601.16**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 4014.54 | **LOC:** 5689 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (96.4894%), Safety Score (93.7076%)
- **Heaviest Functions:** `createDuration` (Impact: 43.4), `getSetOffset` (Impact: 42.1), `checkOverflow` (Impact: 38.9)

### 10. `src/lib/locale/locales.js` (JAVASCRIPT) -> Cumulative Risk: **600.64**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 0.23 | **LOC:** 250 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (97.1014%)
- **Heaviest Functions:** `defineLocale` (Impact: 26.9), `updateLocale` (Impact: 24.7), `getSetGlobalLocale` (Impact: 16.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `min/moment-with-locales.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 7130.22 | **LOC:** 18473 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.1981%), Tech Debt (14.4099%)
**Top Internal Functions/Classes:**
  * `processRelativeTime$9` (Impact: 103.2)
    * *Intent:* //! moment.js locale configuration
  * `relativeTimeMr` (Impact: 69.0)
  * `translate$5` (Impact: 53.8)
  * `translate$9` (Impact: 52.6)
  * `translate$3` (Impact: 47.0)
    * *Intent:* //! moment.js locale configuration
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 849 instances
* *State Mutation (weighted view):* 2914
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3339`, `structural_boundaries: 1815`, `args: 736`, `func_start: 664`
* *Risk/State:* `safety_bypasses: 96`, `state_mutation: 1216`, `dead_code: 12`, `planned_debt: 12`, `duplicate_logic: 29`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`
* *Defense:* `safety: 667`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.843
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `meteor/moment.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4014.54 | **LOC:** 5689 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.8892%), Tech Debt (8.5001%)
**Top Internal Functions/Classes:**
  * `createDuration` (Impact: 43.4)
  * `getSetOffset` (Impact: 42.1)
    * *Intent:* // MOMENTS // keepLocalTime = true means only change the timezone, without // affecting the local ho...
  * `checkOverflow` (Impact: 38.9)
  * `configFromArray` (Impact: 38.3)
    * *Intent:* // convert an array to a date. // the array should mirror the parameters below // note: all values p...
  * `isValid` (Impact: 31.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 656 instances
* *State Mutation (weighted view):* 2281
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1230`, `structural_boundaries: 713`, `args: 346`, `func_start: 283`
* *Risk/State:* `safety_bypasses: 86`, `state_mutation: 969`, `dead_code: 8`, `planned_debt: 10`
* *Architecture:* `api: 4`
* *Defense:* `safety: 222`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.843
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `moment.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4014.54 | **LOC:** 5689 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.8892%), Tech Debt (8.5001%)
**Top Internal Functions/Classes:**
  * `createDuration` (Impact: 43.4)
  * `getSetOffset` (Impact: 42.1)
    * *Intent:* // MOMENTS // keepLocalTime = true means only change the timezone, without // affecting the local ho...
  * `checkOverflow` (Impact: 38.9)
  * `configFromArray` (Impact: 38.3)
    * *Intent:* // convert an array to a date. // the array should mirror the parameters below // note: all values p...
  * `isValid` (Impact: 31.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 656 instances
* *State Mutation (weighted view):* 2281
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1230`, `structural_boundaries: 713`, `args: 346`, `func_start: 283`
* *Risk/State:* `safety_bypasses: 86`, `state_mutation: 969`, `dead_code: 8`, `planned_debt: 10`
* *Architecture:* `api: 4`
* *Defense:* `safety: 222`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.843
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `min/locales.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3125.84 | **LOC:** 12801 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.0451%), Tech Debt (16.8472%)
**Top Internal Functions/Classes:**
  * `processRelativeTime$9` (Impact: 103.2)
    * *Intent:* //! moment.js locale configuration
  * `relativeTimeMr` (Impact: 69.0)
  * `translate$5` (Impact: 53.8)
  * `translate$9` (Impact: 52.6)
  * `translate$3` (Impact: 47.0)
    * *Intent:* //! moment.js locale configuration
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 193 instances
* *State Mutation (weighted view):* 633
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2114`, `structural_boundaries: 1103`, `args: 394`, `func_start: 381`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 247`, `dead_code: 4`, `planned_debt: 2`, `duplicate_logic: 29`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 453`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.843
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` moment
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/lib/parse/regex.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 672.0 | **LOC:** 85 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (61.2886%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 13`, `args: 6`, `func_start: 4`
* *Risk/State:* `state_mutation: 7`
* *Architecture:* `api: 4`, `import: 2`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.036
  * `Choke Point (Betweenness):` 4.8e-05 | `Ripple Effect (Closeness):` 0.033166
  * `Imports (Out-Degree: 2):` has-own-prop, is-function
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `src/lib/units/day-of-week.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 386.58 | **LOC:** 433 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (87.7387%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handleStrictParse` (Impact: 53.6)
  * `localeWeekdaysParse` (Impact: 51.3)
  * `weekdaysRegex` (Impact: 13.7)
  * `weekdaysShortRegex` (Impact: 13.7)
  * `weekdaysMinRegex` (Impact: 13.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 44 instances
* *State Mutation (weighted view):* 153
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 81`, `args: 24`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 65`, `dead_code: 1`
* *Architecture:* `api: 11`, `import: 10`
* *Defense:* `safety: 29`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.247
  * `Choke Point (Betweenness):` 0.000182 | `Ripple Effect (Closeness):` 0.014391
  * `Imports (Out-Degree: 10):` parsing-flags, utc, format, get-set, regex, token, has-own-prop, index-of...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/lib/units/month.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 294.74 | **LOC:** 341 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.6188%), Tech Debt (13.0031%)
**Top Internal Functions/Classes:**
  * `localeMonthsParse` (Impact: 38.6)
  * `handleStrictParse` (Impact: 32.3)
  * `setMonth` (Impact: 15.2)
    * *Intent:* // MOMENTS
  * `monthsShortRegex` (Impact: 13.7)
  * `monthsRegex` (Impact: 13.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 124
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 66`, `args: 19`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 50`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `api: 10`, `import: 15`
* *Defense:* `safety: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.967
  * `Choke Point (Betweenness):` 0.001044 | `Ripple Effect (Closeness):` 0.017171
  * `Imports (Out-Degree: 15):` parsing-flags, utc, format, get-set, regex, token, has-own-prop, hooks...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/lib/units/era.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 235.06 | **LOC:** 294 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (76.1567%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `localeErasParse` (Impact: 30.1)
  * `localeEras` (Impact: 15.2)
  * `getEraYear` (Impact: 8.2)
  * `localeErasConvertYear` (Impact: 7.3)
  * `getEraName` (Impact: 7.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 34 instances
* *State Mutation (weighted view):* 112
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 59`, `args: 17`, `func_start: 15`
* *Risk/State:* `state_mutation: 44`
* *Architecture:* `api: 10`, `import: 8`
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.955
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003145
  * `Imports (Out-Degree: 8):` parsing-flags, format, locales, regex, token, has-own-prop, hooks, constants
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tasks/transpile.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 232.66 | **LOC:** 363 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.6236%), Tech Debt (12.2769%)
**Top Internal Functions/Classes:**
  * `exports` (Impact: 54.9)
  * `transpile` (Impact: 12.6)
  * `generateLocales` (Impact: 11.6)
  * `rollupBundle` (Impact: 7.5)
  * `transpileCode` (Impact: 5.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 12 instances
* *Concurrency (weighted view):* 69
* *State Mutation (weighted view):* 47
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 44`, `args: 42`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 23`, `dead_code: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 11`, `api: 2`, `concurrency: 29`, `import: 6`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.843
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` moment-with-locales.custom.js, , moment, es6-promise, esperanto, path, rollup, rollup-plugin-babel
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/lib/units/offset.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 203.3 | **LOC:** 250 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.9273%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getSetOffset` (Impact: 42.1)
    * *Intent:* // MOMENTS // keepLocalTime = true means only change the timezone, without // affecting the local ho...
  * `offsetFromString` (Impact: 12.9)
  * `cloneWithOffset` (Impact: 9.5)
    * *Intent:* // Return a moment from input, that is local/utc/zone equivalent to model.
  * `getSetZone` (Impact: 7.6)
  * `isDaylightSavingTimeShifted` (Impact: 7.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 74
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 57`, `args: 18`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 26`
* *Architecture:* `api: 12`, `import: 15`
* *Defense:* `safety: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.437
  * `Choke Point (Betweenness):` 0.000732 | `Ripple Effect (Closeness):` 0.008386
  * `Imports (Out-Degree: 15):` from-anything, local, utc, create, format, add-subtract, constructor, regex...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/lib/create/from-string.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 186.74 | **LOC:** 259 | **CtrlFlow:** 34.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.4599%), Tech Debt (26.6351%)
**Top Internal Functions/Classes:**
  * `configFromISO` (Impact: 29.7)
    * *Intent:* // date from iso format
  * `configFromString` (Impact: 12.7)
    * *Intent:* // date from 1) ASP.NET, 2) ISO, 3) RFC 2822 formats, or 4) optional fallback if parsing isn't stric...
  * `calculateOffset` (Impact: 10.7)
  * `configFromRFC2822` (Impact: 7.0)
    * *Intent:* // date and time from ref 2822 format
  * `checkWeekday` (Impact: 6.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 98
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 40`, `args: 9`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 34`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `import: 7`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.236
  * `Choke Point (Betweenness):` 0.000106 | `Ripple Effect (Closeness):` 0.014529
  * `Imports (Out-Degree: 7):` day-of-week, month, deprecate, hooks, date-from-array, from-string-and-format, parsing-flags
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/test/moment/create.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 180.42 | **LOC:** 2920 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.4612%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `offStr` (Impact: 4.7)
  * `extend` (Impact: 3.8)
  * `getVerifier` (Impact: 3.4)
  * `pad` (Impact: 3.1)
  * `parseTwoDigitYear` (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 108
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 52`, `args: 92`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 103`, `state_mutation: 56`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `import: 4`
* *Defense:* `safety: 25`, `test: 490`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.843
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` moment, each-own-prop, has-own-prop, qunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/lib/create/from-array.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 178.8 | **LOC:** 188 | **CtrlFlow:** 30.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.3568%), Tech Debt (47.7693%)
**Top Internal Functions/Classes:**
  * `configFromArray` (Impact: 38.3)
    * *Intent:* // convert an array to a date. // the array should mirror the parameters below // note: all values p...
  * `dayOfYearFromWeekInfo` (Impact: 31.3)
  * `currentDateArray` (Impact: 3.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 34 instances
* *State Mutation (weighted view):* 102
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 15`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 34`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 8`
* *Defense:* `safety: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.546
  * `Choke Point (Betweenness):` 0.000196 | `Ripple Effect (Closeness):` 0.01511
  * `Imports (Out-Degree: 8):` constants, week-calendar-utils, year, defaults, hooks, date-from-array, local, parsing-flags
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/lib/duration/humanize.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 165.16 | **LOC:** 115 | **CtrlFlow:** 40.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.5016%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `relativeTime` (Impact: 64.4)
  * `humanize` (Impact: 15.5)
  * `getSetRelativeTimeThreshold` (Impact: 7.6)
    * *Intent:* // This function allows you to set a threshold for relative time strings
  * `substituteTimeAgo` (Impact: 5.0)
    * *Intent:* // helper function for moment.fn.from, moment.fn.fromNow, and moment.duration.fn.humanize
  * `getSetRelativeTimeRounding` (Impact: 4.7)
    * *Intent:* // This function allows you to set the rounding function for relative time strings
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 63
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 17`, `args: 5`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 25`
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* `safety: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.766
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003538
  * `Imports (Out-Degree: 0):` create
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/lib/moment/start-end-of.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 163.14 | **LOC:** 165 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.7693%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `endOf` (Impact: 27.4)
  * `startOf` (Impact: 27.1)
  * `localStartOfDate` (Impact: 8.4)
  * `utcStartOfDate` (Impact: 8.4)
  * `mod` (Impact: 1.9)
    * *Intent:* // actual modulo - handles negative numbers (for dates before 1970):
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 28 instances
* *State Mutation (weighted view):* 85
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 34`, `args: 5`, `func_start: 5`
* *Risk/State:* `state_mutation: 29`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.876
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001572
  * `Imports (Out-Degree: 2):` aliases, hooks
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/test/moment/add_subtract.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 160.94 | **LOC:** 546 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.1674%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 136
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 18`, `args: 17`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 132`, `fragile_debt: 1`
* *Architecture:* `import: 2`
* *Defense:* `safety: 1`, `test: 175`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.843
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` moment, qunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/lib/duration/create.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 152.72 | **LOC:** 134 | **CtrlFlow:** 55.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.9228%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createDuration` (Impact: 43.4)
  * `momentsDifference` (Impact: 9.5)
  * `parseIso` (Impact: 5.6)
  * `positiveMomentsDifference` (Impact: 4.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 87
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 20`, `args: 4`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 29`
* *Architecture:* `api: 1`, `import: 9`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.552
  * `Choke Point (Betweenness):` 0.000328 | `Ripple Effect (Closeness):` 0.007741
  * `Imports (Out-Degree: 7):` local, constants, offset, abs-round, has-own-prop, is-number, to-int, constructor...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `ts3.1-typing-tests/moment-tests.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 142.78 | **LOC:** 550 | **CtrlFlow:** 9.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.5954%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `meridiem` (Impact: 42.6)
  * `meridiem` (Impact: 22.6)
  * `ordinal` (Impact: 7.5)
  * `ordinal` (Impact: 7.4)
  * `months` (Impact: 5.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 77`, `args: 10`, `func_start: 11`
* *Risk/State:* `state_mutation: 28`, `dead_code: 1`
* *Architecture:* `import: 1`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.843
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` moment
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typing-tests/moment-tests.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 140.82 | **LOC:** 558 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.2186%), Tech Debt (10.563%)
**Top Internal Functions/Classes:**
  * `meridiem` (Impact: 42.6)
  * `meridiem` (Impact: 22.6)
  * `ordinal` (Impact: 7.5)
  * `ordinal` (Impact: 7.4)
  * `months` (Impact: 5.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 32
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 77`, `args: 10`, `func_start: 11`
* *Risk/State:* `state_mutation: 28`, `dead_code: 1`, `planned_debt: 3`
* *Architecture:* `import: 1`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.843
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` moment
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/test/helpers/common-locale.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 139.94 | **LOC:** 266 | **CtrlFlow:** 7.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.818%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `defineCommonLocaleTests` (Impact: 44.2)
  * `tester` (Impact: 6.2)
  * `tester` (Impact: 5.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 78
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 22`, `args: 14`, `func_start: 3`
* *Risk/State:* `state_mutation: 32`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 10`, `test: 42`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.104
  * `Choke Point (Betweenness):` 0.000472 | `Ripple Effect (Closeness):` 0.109671
  * `Imports (Out-Degree: 2):` moment, qunit, each-own-prop
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/lib/moment/get-set.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 139.5 | **LOC:** 118 | **CtrlFlow:** 45.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (84.2905%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `set` (Impact: 42.0)
  * `get` (Impact: 36.1)
  * `stringSet` (Impact: 9.5)
  * `makeGetSet` (Impact: 5.7)
  * `stringGet` (Impact: 3.2)
    * *Intent:* // MOMENTS
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 38`, `args: 6`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 12`, `dead_code: 2`
* *Architecture:* `api: 5`, `import: 5`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.07
  * `Choke Point (Betweenness):` 0.000224 | `Ripple Effect (Closeness):` 0.022983
  * `Imports (Out-Degree: 5):` aliases, priorities, year, hooks, is-function
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/lib/create/from-anything.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 133.04 | **LOC:** 118 | **CtrlFlow:** 36.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.8965%), Tech Debt (33.2727%)
**Top Internal Functions/Classes:**
  * `createLocalOrUTC` (Impact: 23.5)
  * `prepareConfig` (Impact: 22.8)
  * `configFromInput` (Impact: 19.5)
  * `createFromConfig` (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 30`, `args: 5`, `func_start: 4`
* *Risk/State:* `state_mutation: 22`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 18`
* *Defense:* `safety: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.761
  * `Choke Point (Betweenness):` 0.001402 | `Ripple Effect (Closeness):` 0.018427
  * `Imports (Out-Degree: 16):` locales, constructor, hooks, is-array, is-date, is-number, is-object, is-object-empty...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/lib/create/from-string-and-format.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 118.9 | **LOC:** 136 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.7469%), Tech Debt (63.8344%)
**Top Internal Functions/Classes:**
  * `configFromStringAndFormat` (Impact: 31.3)
    * *Intent:* // date from string and format string
  * `meridiemFixWrap` (Impact: 21.2)
  * `ISO_8601` (Impact: 1.1)
    * *Intent:* // constant that refers to the ISO standard
  * `RFC_2822` (Impact: 1.1)
    * *Intent:* // constant that refers to the RFC 2822 form
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 61
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 18`, `args: 4`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 21`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 9`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.479
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.01467
  * `Imports (Out-Degree: 9):` format, regex, token, constants, hooks, check-overflow, from-array, from-string...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/lib/moment/prototype.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 107.4 | **LOC:** 198 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (56.6274%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `proto[Symbol.for` (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 100
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 35`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 82`
* *Architecture:* `api: 2`, `import: 32`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.843
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 22):` day-of-month, day-of-week, day-of-year, era, hour, millisecond, minute, month...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/lib/moment/diff.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 102.62 | **LOC:** 80 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.3014%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `diff` (Impact: 30.4)
  * `monthDiff` (Impact: 10.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 19`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 20`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.843
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` aliases, offset, abs-floor
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

- `src/lib/create/from-anything.js` -> **Severity: 0.14** (Bridge: 0.0014 * Flux: 100.0%)
- `src/lib/locale/locales.js` -> **Severity: 0.107** (Bridge: 0.0011 * Flux: 100.0%)
- `src/lib/units/month.js` -> **Severity: 0.104** (Bridge: 0.001 * Flux: 100.0%)
- `src/lib/units/offset.js` -> **Severity: 0.073** (Bridge: 0.0007 * Flux: 99.9998%)
- `src/test/helpers/common-locale.js` -> **Severity: 0.047** (Bridge: 0.0005 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/test/qunit.js` -> **Severity: 18.892** (Embedded: 0.3019 * Error Risk: 62.5811%)
- `src/test/helpers/deprecation-handler.js` -> **Severity: 13.434** (Embedded: 0.1525 * Error Risk: 88.0797%)
- `src/test/qunit-locale.js` -> **Severity: 13.139** (Embedded: 0.217 * Error Risk: 60.5532%)
- `src/test/helpers/each.js` -> **Severity: 7.198** (Embedded: 0.1053 * Error Risk: 68.383%)
- `src/test/helpers/common-locale.js` -> **Severity: 6.836** (Embedded: 0.1097 * Error Risk: 62.3356%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/test/qunit.js` -> **Severity: 10417.5** (Blast Radius: 104.175 * Doc Risk: 100.0%)
- `src/test/helpers/deprecation-handler.js` -> **Severity: 10373.2** (Blast Radius: 103.732 * Doc Risk: 100.0%)
- `src/test/helpers/each.js` -> **Severity: 9349.9** (Blast Radius: 93.499 * Doc Risk: 100.0%)
- `src/test/qunit-locale.js` -> **Severity: 5028.5** (Blast Radius: 50.285 * Doc Risk: 100.0%)
- `src/test/helpers/common-locale.js` -> **Severity: 1510.4** (Blast Radius: 15.104 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
