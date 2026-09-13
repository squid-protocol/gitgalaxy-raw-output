# ARCHITECTURAL_BRIEF: type-fest
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/sindresorhus/type-fest.git` |
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
| Total Artifacts | 453 |
| Analyzed Artifacts (Scanned) | 427 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 26 |
| Total LOC | 18857 |
| Volatility Index | 0.005 |
| % Scanned of codebase = | 94.3% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3553 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4298 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 4.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.5265 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 41 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 403 | 14660 | 94.4% |
| JAVASCRIPT | 15 | 4170 | 3.5% |
| PLAINTEXT | 4 | 1 | 0.9% |
| MARKDOWN | 3 | 0 | 0.7% |
| XML | 1 | 14 | 0.2% |
| JSON | 1 | 12 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 419 | 98.1% |
| Unknown | 1 | 0.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 6 | 1.4% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 26*

**Composition by Extension & Reason:**
- `.yml`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 1x Excluded (Saturation: Line 11 exceeds 500 chars), 1x Excluded (Saturation: Line 12 exceeds 500 chars), 1x Excluded (Saturation: Line 15 exceeds 500 chars)
- `.md`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 2x Excluded (Explicitly Denied Extension: '.png')
- `.sketch`: 1x Excluded (Explicitly Denied Extension: '.sketch')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 55.5 | 4.4 | 3.5 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.4 | 24.2 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 3.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 2.6 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 18.3 | 7.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 97.6 | 1.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 2.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 34.7 | 0.2 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 16.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 5.5 | 1.1 | 0.1 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 73.7 | 12.4 | 7.6 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 11.5 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1331 | 146 | 8 | `test-d/object-merge.ts` |
| cleanup | 0 | 0 | 0 | - |
| guards | 1097 | 148 | 7 | `test-d/set-required.ts` |
| danger | 592 | 138 | 4 | `test-d/all-union-fields.ts` |
| concurrency | 47 | 11 | 0 | `source/tsconfig-json.d.ts` |
| connectivity | 765 | 216 | 3 | `lint-rules/validate-jsdoc-codeblocks.test.js` |
| io | 30 | 8 | 0 | `lint-rules/test-utils.js` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 48 | 17 | 0 | `test-d/jsonify.ts` |
| serialization | 4 | 4 | 0 | `test-d/opaque.ts` |
| regex | 8 | 2 | 0 | `lint-processors/jsdoc-codeblocks.js` |
| events | 116 | 19 | 0 | `test-d/remove-prefix.ts` |
| tests | 23 | 5 | 0 | `test-d/require-at-least-one.ts` |
| docs | 955 | 236 | 3 | `source/tsconfig-json.d.ts` |
| debt | 26 | 21 | 0 | `source/globals/observable-like.d.ts` |
| mutation | 1824 | 247 | 7 | `lint-rules/validate-jsdoc-codeblocks.test.js` |
| dead_code | 34 | 24 | 0 | `source/object-merge.d.ts` |
| credential | 0 | 0 | 0 | - |
| threat | 16 | 6 | 0 | `test-d/set-return-type.ts` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 18 | 6 | 0 | `lint-processors/jsdoc-codeblocks.test.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `lint-rules/test-utils.js` (Hits: 9)
- `lint-processors/jsdoc-codeblocks.test.js` (Hits: 8)
- `lint-rules/require-exported-types.js` (Hits: 8)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **index.d.ts** (`source/internal/index.d.ts`) — 78 inbound connections
2. **unknown-array.d.ts** (`source/unknown-array.d.ts`) — 37 inbound connections
3. **is-never.d.ts** (`source/is-never.d.ts`) — 32 inbound connections
4. **is-any.d.ts** (`source/is-any.d.ts`) — 25 inbound connections
5. **if.d.ts** (`source/if.d.ts`) — 22 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **readme.md** (`readme.md`) — 189 outbound dependencies
2. **import-path.test.js** (`lint-rules/import-path.test.js`) — 17 outbound dependencies
3. **object.d.ts** (`source/internal/object.d.ts`) — 13 outbound dependencies
4. **array-slice.d.ts** (`source/array-slice.d.ts`) — 11 outbound dependencies
5. **merge-deep.d.ts** (`source/merge-deep.d.ts`) — 11 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `incorrectTwoslashFormatErrorAt` (@ `lint-rules/validate-jsdoc-codeblocks.test.js`) -> Impact: **122.8** | LOC: 1778
- `create` (@ `lint-rules/validate-jsdoc-codeblocks.js`) -> Impact: **38.7** | LOC: 95
- `create` (@ `lint-rules/require-exported-types.js`) -> Impact: **38.1** | LOC: 111
- `TSTypeAliasDeclaration` (@ `lint-rules/validate-jsdoc-codeblocks.js`) -> Impact: **36.4** | LOC: 78
- `writeFixture` (@ `lint-rules/test-utils.js`) -> Impact: **34.9** | LOC: 40
- `validateTwoslashTypes` (@ `lint-rules/validate-jsdoc-codeblocks.js`) -> Impact: **31.0** | LOC: 84
- `postprocess` (@ `lint-processors/jsdoc-codeblocks.js`) -> Impact: **27.3** | LOC: 61
  * *Intent:* /** */
- `preprocess` (@ `lint-processors/jsdoc-codeblocks.js`) -> Impact: **21.8** | LOC: 54
  * *Intent:* /** */
- `extractTypeFromQuickInfo` (@ `lint-rules/validate-jsdoc-codeblocks.js`) -> Impact: **21.4** | LOC: 32
- `normalizeType` (@ `lint-rules/validate-jsdoc-codeblocks.js`) -> Impact: **20.4** | LOC: 62

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `__monolith__` | 8 | 5065.86 | 0.3% | 0.0% |
| `test-d` | 183 | 2679.17 | 5.18% | 5.34% |
| `lint-rules` | 11 | 786.32 | 6.48% | 0.0% |
| `lint-processors` | 2 | 509.23 | 20.1% | 0.0% |
| `test-d/internal` | 22 | 334.0 | 3.3% | 2.44% |
| `source` | 186 | 153.96 | 3.41% | 1.3% |
| `source/internal` | 10 | 11.55 | 5.24% | 2.34% |
| `media` | 2 | 2.0 | 0.0% | 0.0% |
| `source/globals` | 2 | 1.28 | 1.09% | 36.55% |
| `lint-processors/fixtures` | 1 | 0.01 | 3.54% | 62.65% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `test-d/observable-like.ts` -> **99.9955%** Exposure
- `test-d/abstract-class.ts` -> **99.949%** Exposure
- `test-d/set-parameter-type.ts` -> **99.6827%** Exposure
- `test-d/require-all-or-none.ts` -> **88.2248%** Exposure
- `test-d/require-exactly-one.ts` -> **84.8229%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `lint-processors/jsdoc-codeblocks.js` -> **99.9997%** Exposure
- `test-d/multidimensional-readonly-array.ts` -> **99.8341%** Exposure
- `test-d/multidimensional-array.ts` -> **99.6316%** Exposure
- `lint-rules/validate-jsdoc-codeblocks.js` -> **97.5815%** Exposure
- `test-d/empty-object.ts` -> **91.6827%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `test-d/abstract-class.ts` -> **1** Orphaned Functions | **2** Duplicates
- `test-d/observable-like.ts` -> **1** Orphaned Functions | **2** Duplicates
- `test-d/require-all-or-none.ts` -> **3** Orphaned Functions | **0** Duplicates
- `test-d/require-exactly-one.ts` -> **3** Orphaned Functions | **0** Duplicates
- `test-d/require-one-or-none.ts` -> **3** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `604` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `lint-rules/validate-jsdoc-codeblocks.js` (JAVASCRIPT) -> Cumulative Risk: **470.55**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 265.66 | **LOC:** 421 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (97.5815%), Documentation (88.2353%), Churn (73.74%)
- **Heaviest Functions:** `create` (Impact: 38.7), `TSTypeAliasDeclaration` (Impact: 36.4), `validateTwoslashTypes` (Impact: 31.0)

### 2. `test-d/multidimensional-readonly-array.ts` (TYPESCRIPT) -> Cumulative Risk: **408.35**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 18.88 | **LOC:** 33 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.8341%), Safety Score (72.5402%)
- **Heaviest Functions:** `createArray` (Impact: 6.4)

### 3. `test-d/multidimensional-array.ts` (TYPESCRIPT) -> Cumulative Risk: **396.7**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 13.82 | **LOC:** 30 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.6316%), Safety Score (73.6639%)
- **Heaviest Functions:** `createArray` (Impact: 3.4)

### 4. `test-d/require-all-or-none.ts` (TYPESCRIPT) -> Cumulative Risk: **392.69**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 12.24 | **LOC:** 105 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Safety Score (89.5872%), Tech Debt (88.2248%)
- **Heaviest Functions:** `narrowingTest3` (Impact: 3.7), `narrowingTest2` (Impact: 3.6), `narrowingTest` (Impact: 3.5)

### 5. `test-d/require-exactly-one.ts` (TYPESCRIPT) -> Cumulative Risk: **391.74**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 14.14 | **LOC:** 111 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Safety Score (89.1203%), Tech Debt (84.8229%)
- **Heaviest Functions:** `narrowingTest2` (Impact: 5.4), `narrowingTest3` (Impact: 3.7), `narrowingTest` (Impact: 3.5)

### 6. `lint-processors/jsdoc-codeblocks.js` (JAVASCRIPT) -> Cumulative Risk: **387.58**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 102.24 | **LOC:** 173 | **CtrlFlow:** 31.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9997%), Safety Score (74.1247%), Churn (41.63%)
- **Heaviest Functions:** `postprocess` (Impact: 27.3), `preprocess` (Impact: 21.8), `indentsUptoIndex` (Impact: 9.1)

### 7. `lint-rules/require-export.js` (JAVASCRIPT) -> Cumulative Risk: **383.74**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 28.8 | **LOC:** 47 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Safety Score (64.1725%), Api Exposure (60.3656%)
- **Heaviest Functions:** `create` (Impact: 11.4), `ExportNamedDeclaration` (Impact: 6.0), `fix` (Impact: 1.6)

### 8. `lint-rules/require-exported-types.js` (JAVASCRIPT) -> Cumulative Risk: **382.21**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 62.94 | **LOC:** 143 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (75.573%), Safety Score (54.6586%)
- **Heaviest Functions:** `create` (Impact: 38.1), `checkExportedType` (Impact: 10.8)

### 9. `test-d/require-one-or-none.ts` (TYPESCRIPT) -> Cumulative Risk: **375.14**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 19.86 | **LOC:** 133 | **CtrlFlow:** 33.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Safety Score (87.3493%), Tech Debt (69.3456%)
- **Heaviest Functions:** `narrowingTest2` (Impact: 7.2), `narrowingTest3` (Impact: 5.5), `narrowingTest` (Impact: 5.2)

### 10. `test-d/abstract-class.ts` (TYPESCRIPT) -> Cumulative Risk: **372.62**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 24.54 | **LOC:** 92 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.949%), Documentation (88.8889%), Safety Score (56.5475%)
- **Heaviest Functions:** `constructor` (Impact: 2.0), `withBar` (Impact: 1.8), `constructor` (Impact: 1.6)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lint-processors/jsdoc-codeblocks.test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 406.99 | **LOC:** 1482 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (1.297%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 120`, `args: 19`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 4`
* *Architecture:* `io: 8`, `api: 75`, `concurrency: 7`, `import: 11`
* *Defense:* `safety: 3`, `doc: 125`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` test-utils.js, eslint, promises, node:path, node:test, type-fest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lint-rules/validate-jsdoc-codeblocks.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 265.66 | **LOC:** 421 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (26.9034%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `create` (Impact: 38.7)
  * `TSTypeAliasDeclaration` (Impact: 36.4)
  * `validateTwoslashTypes` (Impact: 31.0)
  * `extractTypeFromQuickInfo` (Impact: 21.4)
  * `normalizeType` (Impact: 20.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 50
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 60`, `args: 28`, `func_start: 14`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `io: 1`, `api: 4`, `import: 3`
* *Defense:* `safety: 26`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.783
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004684
  * `Imports (Out-Degree: 0):` vfs, node:path, typescript
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `lint-rules/validate-jsdoc-codeblocks.test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 239.34 | **LOC:** 1793 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (1.2867%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `incorrectTwoslashFormatErrorAt` (Impact: 122.8)
  * `invalidCodeblockErrorAt` (Impact: 1.5)
  * `incorrectTwoslashTypeErrorAt` (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 266`, `args: 8`, `func_start: 8`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 4`, `unreferenced_by_name: 1`
* *Architecture:* `api: 79`, `import: 27`
* *Defense:* `doc: 76`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` test-utils.js, validate-jsdoc-codeblocks.js, type-fest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lint-processors/jsdoc-codeblocks.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 102.24 | **LOC:** 173 | **CtrlFlow:** 31.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (38.9074%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `postprocess` (Impact: 27.3)
    * *Intent:* /** */
  * `preprocess` (Impact: 21.8)
    * *Intent:* /** */
  * `indentsUptoIndex` (Impact: 9.1)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 16`, `args: 6`, `func_start: 3`
* *Risk/State:* `state_mutation: 17`
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* `safety: 11`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004684
  * `Imports (Out-Degree: 0):` parser, eslint
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `lint-rules/test-utils.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 84.8 | **LOC:** 314 | **CtrlFlow:** 14.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (5.17%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `writeFixture` (Impact: 34.9)
  * `errorAt` (Impact: 8.8)
    * *Intent:* */
  * `createRuleTester` (Impact: 3.6)
  * `exportOption` (Impact: 3.4)
    * *Intent:* */
  * `fixturePath` (Impact: 3.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 37`, `args: 13`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 1`, `dead_code: 1`
* *Architecture:* `io: 9`, `api: 14`, `import: 8`
* *Defense:* `safety: 9`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.523
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.014052
  * `Imports (Out-Degree: 0):` parser, dedent, eslint, node:fs, node:os, node:path, type-fest
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `test-d/exact.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 81.98 | **LOC:** 556 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (5.2878%), Tech Debt (9.9601%)
**Top Internal Functions/Classes:**
  * `function_` (Impact: 8.1)
  * `function_` (Impact: 5.2)
  * `function_` (Impact: 4.5)
  * `function_` (Impact: 4.5)
  * `function_` (Impact: 4.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 69`, `args: 20`, `func_start: 20`
* *Risk/State:* `unreferenced_by_name: 1`
* *Architecture:* `import: 1`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.d.ts
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lint-rules/require-exported-types.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 62.94 | **LOC:** 143 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.9548%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `create` (Impact: 38.1)
  * `checkExportedType` (Impact: 10.8)
    * *Intent:* // Helper function to check exported type/interface
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 14`, `args: 3`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`
* *Architecture:* `io: 8`, `api: 3`, `import: 3`
* *Defense:* `safety: 7`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.783
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004684
  * `Imports (Out-Degree: 0):` node:fs, node:path
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `lint-rules/import-path.test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 37.38 | **LOC:** 133 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `invalidImport` (Impact: 8.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 47`, `args: 1`, `func_start: 1`
* *Risk/State:* `unreferenced_by_name: 1`
* *Architecture:* `api: 27`, `import: 41`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` all.js, path.tsx, bar, bar.d.ts, bar.ts, foo, foo.d.d.ts, foo.d.ts...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lint-rules/require-export.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 28.8 | **LOC:** 47 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.2053%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `create` (Impact: 11.4)
  * `ExportNamedDeclaration` (Impact: 6.0)
  * `fix` (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 7`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 6`
* *Defense:* `safety: 1`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.783
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004684
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `test-d/partial-deep.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 28.28 | **LOC:** 138 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.8533%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 24`, `args: 3`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 5`
* *Architecture:* `import: 2`
* *Defense:* `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.d.ts, tsd
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test-d/abstract-class.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 24.54 | **LOC:** 92 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (99.949%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 2.0)
    * *Intent:* // This should be alright since `barMethod` is implemented.
  * `withBar` (Impact: 1.8)
  * `constructor` (Impact: 1.6)
  * `functionReceivingAbsClass` (Impact: 1.6)
  * `constructor` (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 34`, `args: 11`, `func_start: 16`, `class_start: 9`
* *Risk/State:* `state_mutation: 2`, `duplicate_logic: 2`, `unreferenced_by_name: 1`
* *Architecture:* `import: 2`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.d.ts, tsd
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test-d/paths.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 22.84 | **LOC:** 583 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (7.8953%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 239`, `args: 1`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`
* *Architecture:* `import: 3`
* *Defense:* `doc: 1`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` index.d.ts, type.d.ts, tsd
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test-d/required-deep.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 22.18 | **LOC:** 86 | **CtrlFlow:** 142.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (55.4863%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 16`
* *Risk/State:* None
* *Architecture:* `concurrency: 6`, `import: 3`
* *Defense:* `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` index.d.ts, type.d.ts, tsd
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test-d/words.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 22.12 | **LOC:** 113 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` words.d.ts, tsd
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test-d/fixed-length-array.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 21.98 | **LOC:** 87 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 18`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `import: 2`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.d.ts, tsd
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xo.config.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 21.88 | **LOC:** 155 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (2.4348%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 17`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `api: 4`, `import: 7`
* *Defense:* `doc: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` jsdoc-codeblocks.js, import-path.js, require-export.js, require-exported-types.js, source-files-extension.js, validate-jsdoc-codeblocks.js, typescript-eslint, xo
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `readme.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 21.5 | **LOC:** 1075 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 183):` contributing.md, license-cc0, license-mit, absolute.d.ts, all-extend.d.ts, all-union-fields.d.ts, and-all.d.ts, and.d.ts...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test-d/empty-object.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 21.42 | **LOC:** 37 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 8`, `args: 1`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.d.ts, tsd
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test-d/array-reverse.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 20.34 | **LOC:** 300 | **CtrlFlow:** 9.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (6.658%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 17`
* *Risk/State:* `safety_bypasses: 6`
* *Architecture:* `import: 4`
* *Defense:* `immutability_locks: 36`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` array-reverse.d.ts, int-range.d.ts, tuple-of.d.ts, tsd
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test-d/require-one-or-none.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 19.86 | **LOC:** 133 | **CtrlFlow:** 33.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.0696%), Tech Debt (69.3456%)
**Top Internal Functions/Classes:**
  * `narrowingTest2` (Impact: 7.2)
  * `narrowingTest3` (Impact: 5.5)
  * `narrowingTest` (Impact: 5.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 52`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 12`, `unreferenced_by_name: 3`
* *Architecture:* `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.d.ts, tsd
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test-d/conditional-pick-deep.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 19.66 | **LOC:** 161 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (5.828%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 66`, `args: 3`, `class_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 1`, `concurrency: 1`, `import: 2`
* *Defense:* `doc: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.d.ts, tsd
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test-d/jsonify.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 19.52 | **LOC:** 396 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (5.5543%), Tech Debt (11.4346%)
**Top Internal Functions/Classes:**
  * `toJSON` (Impact: 1.4)
  * `toJSON` (Impact: 1.2)
  * `toJSON` (Impact: 1.2)
  * `toJSON` (Impact: 1.2)
    * *Intent:* // This is intentionally invalid `.toJSON()`. // It is invalid because the result is not assignable ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 118`, `args: 14`, `func_start: 4`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 16`, `planned_debt: 2`
* *Architecture:* `api: 9`, `import: 2`
* *Defense:* `doc: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.d.ts, tsd
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test-d/object-merge.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 19.42 | **LOC:** 293 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (11.6848%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 33`, `args: 2`
* *Risk/State:* `safety_bypasses: 6`
* *Architecture:* `import: 2`
* *Defense:* `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` object-merge.d.ts, tsd
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test-d/require-at-least-one.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 18.98 | **LOC:** 69 | **CtrlFlow:** 51.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.2852%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 27`, `args: 4`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 1`
* *Architecture:* `import: 2`
* *Defense:* `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.d.ts, tsd
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `lint-processors/jsdoc-codeblocks.test.js` -> **Som Shekhar Mukherjee** (100.0% isolated ownership) | Magnitude: 406.99
- `lint-rules/validate-jsdoc-codeblocks.js` -> **Som Shekhar Mukherjee** (100.0% isolated ownership) | Magnitude: 265.66
- `lint-rules/validate-jsdoc-codeblocks.test.js` -> **Som Shekhar Mukherjee** (100.0% isolated ownership) | Magnitude: 239.34
- `lint-processors/jsdoc-codeblocks.js` -> **Som Shekhar Mukherjee** (100.0% isolated ownership) | Magnitude: 102.24
- `lint-rules/test-utils.js` -> **Som Shekhar Mukherjee** (100.0% isolated ownership) | Magnitude: 84.8

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `source/array-splice.d.ts` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 27.98%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `source/internal/type.d.ts` -> **Severity: 8.326** (Embedded: 0.1779 * Error Risk: 46.7901%)
- `source/internal/object.d.ts` -> **Severity: 6.653** (Embedded: 0.1408 * Error Risk: 47.2683%)
- `source/internal/keys.d.ts` -> **Severity: 6.419** (Embedded: 0.1309 * Error Risk: 49.0358%)
- `source/is-literal.d.ts` -> **Severity: 4.727** (Embedded: 0.1003 * Error Risk: 47.1104%)
- `source/is-optional-key-of.d.ts` -> **Severity: 4.526** (Embedded: 0.0903 * Error Risk: 50.1071%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `lint-rules/import-path.js` -> **Severity: 178.3** (Blast Radius: 1.783 * Doc Risk: 100.0%)
- `lint-rules/require-export.js` -> **Severity: 178.3** (Blast Radius: 1.783 * Doc Risk: 100.0%)
- `lint-rules/require-exported-types.js` -> **Severity: 178.3** (Blast Radius: 1.783 * Doc Risk: 100.0%)
- `lint-rules/source-files-extension.js` -> **Severity: 178.3** (Blast Radius: 1.783 * Doc Risk: 100.0%)
- `lint-rules/validate-jsdoc-codeblocks.js` -> **Severity: 157.324** (Blast Radius: 1.783 * Doc Risk: 88.2353%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
