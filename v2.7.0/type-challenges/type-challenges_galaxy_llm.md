# ARCHITECTURAL_BRIEF: type-challenges
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/type-challenges/type-challenges.git` |
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
| Total Artifacts | 1088 |
| Analyzed Artifacts (Scanned) | 1054 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 34 |
| Total LOC | 6809 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 96.9% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.302 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3881 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.0362 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 4 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| MARKDOWN | 404 | 187 | 38.3% |
| TYPESCRIPT | 398 | 5113 | 37.8% |
| YAML | 236 | 1314 | 22.4% |
| JSON | 9 | 166 | 0.9% |
| PLAINTEXT | 4 | 1 | 0.4% |
| JAVASCRIPT | 1 | 23 | 0.1% |
| XML | 1 | 0 | 0.1% |
| SHELL | 1 | 5 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 646 | 61.3% |
| Unknown | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 405 | 38.4% |
| Static: Minified & Vendor Opaque Mass | 2 | 0.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 34*

**Composition by Extension & Reason:**
- `.md`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 3209 LOC)
- `.ts`: 2x Excluded (Saturation: Line 8 exceeds 500 chars), 1x Excluded (Saturation: Line 29 exceeds 500 chars), 1x Packed Payload Guard (Impossible Density: 3.95 hits/line)
- `.svg`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 3x Excluded (Explicitly Denied Extension: '.png')
- `.yml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Unsupported Format (.toml)
- `.html`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.css`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 98.8 | 1.4 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 97.7 | 21.2 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.1 | 1.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 2.4 | 2.2 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 84.3 | 0.9 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 1.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 8.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 4.6 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 4.1 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 19 | 6 | 0 | `questions/00925-extreme-assert-array-index/test-cases.ts` |
| cleanup | 0 | 0 | 0 | - |
| guards | 137 | 37 | 0 | `questions/00472-hard-tuple-to-enum-object/test-cases.ts` |
| danger | 298 | 210 | 1 | `questions/21220-medium-permutations-of-tuple/test-cases.ts` |
| concurrency | 113 | 14 | 0 | `scripts/loader.ts` |
| connectivity | 76 | 21 | 0 | `scripts/toUrl.ts` |
| io | 80 | 8 | 0 | `scripts/generate-play.ts` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 2 | 1 | 0 | `scripts/actions/issue-pr.ts` |
| serialization | 10 | 3 | 0 | `scripts/actions/issue-pr.ts` |
| regex | 30 | 6 | 0 | `scripts/readme.ts` |
| events | 23 | 5 | 0 | `eslint.config.js` |
| tests | 17 | 5 | 0 | `questions/33345-extreme-dynamic-route/test-cases.ts` |
| docs | 402 | 392 | 1 | `questions/00697-extreme-tag/test-cases.ts` |
| debt | 34 | 9 | 0 | `questions/33345-extreme-dynamic-route/test-cases.ts` |
| mutation | 871 | 225 | 1 | `scripts/readme.ts` |
| dead_code | 19 | 15 | 0 | `questions/00006-hard-simple-vue/test-cases.ts` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 7 | 4 | 0 | `questions/00006-hard-simple-vue/test-cases.ts` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `scripts/generate-play.ts` (Hits: 21)
- `scripts/readme.ts` (Hits: 15)
- `scripts/loader.ts` (Hits: 14)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **locales.ts** (`scripts/locales.ts`) — 13 inbound connections
2. **types.ts** (`scripts/types.ts`) — 12 inbound connections
3. **TODOs.md** (`TODOs.md`) — 5 inbound connections
4. **toUrl.ts** (`scripts/toUrl.ts`) — 5 inbound connections
5. **formatToCode.ts** (`scripts/actions/utils/formatToCode.ts`) — 3 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **generate-play.ts** (`scripts/generate-play.ts`) — 11 outbound dependencies
2. **issue-pr.ts** (`scripts/actions/issue-pr.ts`) — 9 outbound dependencies
3. **formatToCode.ts** (`scripts/actions/utils/formatToCode.ts`) — 7 outbound dependencies
4. **readme.ts** (`scripts/readme.ts`) — 7 outbound dependencies
5. **translate.ts** (`scripts/translate.ts`) — 7 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `action` (@ `scripts/actions/issue-pr.ts`) -> Impact: **52.1** | LOC: 122
- `action` (@ `scripts/actions/toggle-pr-with-issue.ts`) -> Impact: **29.2** | LOC: 64
- `action` (@ `scripts/actions/labeling.ts`) -> Impact: **27.1** | LOC: 62
- `insertInfoReadme` (@ `scripts/readme.ts`) -> Impact: **26.6** | LOC: 41
- `generatePlayground` (@ `scripts/generate-play.ts`) -> Impact: **24.3** | LOC: 86
- `resolveInfo` (@ `scripts/loader.ts`) -> Impact: **17.9** | LOC: 11
- `updateIndexREADME` (@ `scripts/readme.ts`) -> Impact: **15.4** | LOC: 53
- `translateMarkdown` (@ `scripts/translate.ts`) -> Impact: **15.4** | LOC: 29
- `toInfoHeader` (@ `scripts/actions/utils/toInfoHeader.ts`) -> Impact: **14.4** | LOC: 10
- `toQuizREADME` (@ `scripts/toUrl.ts`) -> Impact: **12.3** | LOC: 6

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `__monolith__` | 13 | 5074.48 | 0.62% | 0.0% |
| `scripts` | 12 | 783.18 | 43.97% | 0.0% |
| `scripts/actions` | 4 | 279.14 | 34.95% | 27.54% |
| `questions/00925-extreme-assert-array-index` | 4 | 69.98 | 15.73% | 12.5% |
| `questions/00697-extreme-tag` | 4 | 66.68 | 0.0% | 0.0% |
| `questions/00002-medium-return-type` | 10 | 65.18 | 0.69% | 0.0% |
| `questions/00009-medium-deep-readonly` | 9 | 56.22 | 0.0% | 0.0% |
| `questions/00012-medium-chainable-options` | 8 | 55.9 | 0.0% | 0.0% |
| `questions/00003-medium-omit` | 9 | 55.72 | 0.0% | 8.12% |
| `questions/00008-medium-readonly-2` | 9 | 55.66 | 0.53% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `questions/33345-extreme-dynamic-route/test-cases.ts` -> **99.0913%** Exposure
- `questions/00006-hard-simple-vue/test-cases.ts` -> **98.2014%** Exposure
- `questions/00213-hard-vue-basic-props/test-cases.ts` -> **97.4221%** Exposure
- `questions/00004-easy-pick/test-cases.ts` -> **88.0797%** Exposure
- `questions/00003-medium-omit/test-cases.ts` -> **73.1059%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `questions/00925-extreme-assert-array-index/test-cases.ts` -> **100.0%** Exposure
- `scripts/build.ts` -> **100.0%** Exposure
- `scripts/readme.ts` -> **100.0%** Exposure
- `scripts/loader.ts` -> **99.9958%** Exposure
- `questions/00697-extreme-tag/test-cases.ts` -> **99.4438%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `questions/00006-hard-simple-vue/test-cases.ts` -> **3** Orphaned Functions | **0** Duplicates
- `questions/00213-hard-vue-basic-props/test-cases.ts` -> **3** Orphaned Functions | **0** Duplicates
- `questions/00006-hard-simple-vue/template.ts` -> **1** Orphaned Functions | **0** Duplicates
- `questions/00017-hard-currying-1/template.ts` -> **1** Orphaned Functions | **0** Duplicates
- `questions/00020-medium-promise-all/template.ts` -> **1** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `216` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `scripts/loader.ts` (TYPESCRIPT) -> Cumulative Risk: **652.01**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 113.06 | **LOC:** 118 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9958%)
- **Heaviest Functions:** `resolveInfo` (Impact: 17.9), `loadInfo` (Impact: 9.6), `loadQuiz` (Impact: 4.8)

### 2. `scripts/readme.ts` (TYPESCRIPT) -> Cumulative Risk: **626.79**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 290.22 | **LOC:** 241 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `insertInfoReadme` (Impact: 26.6), `updateIndexREADME` (Impact: 15.4), `quizToBadge` (Impact: 11.6)

### 3. `scripts/translate.ts` (TYPESCRIPT) -> Cumulative Risk: **608.4**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 67.12 | **LOC:** 74 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (98.2512%)
- **Heaviest Functions:** `translateMarkdown` (Impact: 15.4), `translateAllQuizzes` (Impact: 7.6), `translateQuiz` (Impact: 4.7)

### 4. `scripts/actions/issue-pr.ts` (TYPESCRIPT) -> Cumulative Risk: **601.48**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 203.28 | **LOC:** 273 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9987%), State Flux (94.8784%)
- **Heaviest Functions:** `action` (Impact: 52.1), `createMessageBody` (Impact: 10.7), `getCodeBlock` (Impact: 10.4)

### 5. `scripts/build.ts` (TYPESCRIPT) -> Cumulative Risk: **592.65**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 50.02 | **LOC:** 55 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9999%)
- **Heaviest Functions:** `build` (Impact: 8.2)

### 6. `scripts/generate-play.ts` (TYPESCRIPT) -> Cumulative Risk: **573.26**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 128.0 | **LOC:** 181 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.3621%)
- **Heaviest Functions:** `generatePlayground` (Impact: 24.3), `takeSnapshot` (Impact: 6.8), `isQuizWritable` (Impact: 6.3)

### 7. `scripts/actions/toggle-pr-with-issue.ts` (TYPESCRIPT) -> Cumulative Risk: **427.04**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 35.12 | **LOC:** 67 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (90.6079%), Safety Score (57.793%)
- **Heaviest Functions:** `action` (Impact: 29.2)

### 8. `scripts/actions/labeling.ts` (TYPESCRIPT) -> Cumulative Risk: **424.41**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 34.18 | **LOC:** 65 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (95.5353%), Safety Score (54.7154%)
- **Heaviest Functions:** `action` (Impact: 27.1)

### 9. `questions/01290-hard-pinia/test-cases.ts` (TYPESCRIPT) -> Cumulative Risk: **337.55**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 15.44 | **LOC:** 67 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (80.9406%), Safety Score (63.7994%), Tech Debt (47.598%)
- **Heaviest Functions:** `increment` (Impact: 1.6), `setNum` (Impact: 1.6), `reset` (Impact: 1.4)

### 10. `questions/02828-hard-classpublickeys/test-cases.ts` (TYPESCRIPT) -> Cumulative Risk: **336.81**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 6.64 | **LOC:** 21 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (73.18%), Safety Score (60.143%), Tech Debt (50.0%)
- **Heaviest Functions:** `constructor` (Impact: 1.2), `getNum` (Impact: 1.1)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.925
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/readme.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 290.22 | **LOC:** 241 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (98.2371%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `insertInfoReadme` (Impact: 26.6)
  * `updateIndexREADME` (Impact: 15.4)
  * `quizToBadge` (Impact: 11.6)
  * `updateREADMEs` (Impact: 9.3)
  * `getAllTags` (Impact: 9.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 35 instances
* *Concurrency (weighted view):* 54
* *State Mutation (weighted view):* 133
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 54`, `args: 31`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 63`
* *Architecture:* `io: 15`, `api: 3`, `concurrency: 14`, `import: 9`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.345
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002135
  * `Imports (Out-Degree: 3):` loader, locales, toUrl, types, fs-extra, node:path, node:process
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `scripts/actions/issue-pr.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 203.28 | **LOC:** 273 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.9508%), Tech Debt (14.7778%)
**Top Internal Functions/Classes:**
  * `action` (Impact: 52.1)
  * `createMessageBody` (Impact: 10.7)
  * `getCodeBlock` (Impact: 10.4)
  * `updateComment` (Impact: 9.4)
  * `getCommentRange` (Impact: 7.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 17 instances
* *Concurrency (weighted view):* 43
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 41`, `args: 11`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 19`, `fragile_debt: 1`
* *Architecture:* `io: 2`, `api: 4`, `concurrency: 13`, `import: 9`
* *Defense:* `safety: 5`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.121
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000949
  * `Imports (Out-Degree: 6):` locales, readme, toUrl, types, resolve, formatToCode, octokit-create-pull-request, js-yaml...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `scripts/generate-play.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 128.0 | **LOC:** 181 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.4072%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `generatePlayground` (Impact: 24.3)
  * `takeSnapshot` (Impact: 6.8)
  * `isQuizWritable` (Impact: 6.3)
  * `calculateOverridableFiles` (Impact: 5.7)
  * `readPlaygroundCache` (Impact: 3.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 9 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 49
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 40`, `args: 12`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 9`
* *Architecture:* `io: 21`, `concurrency: 14`, `import: 11`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.925
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` issue-pr, formatToCode, loader, locales, types, ansis, fs-extra, node:crypto...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/loader.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 113.06 | **LOC:** 118 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (98.7846%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `resolveInfo` (Impact: 17.9)
  * `loadInfo` (Impact: 9.6)
  * `loadQuiz` (Impact: 4.8)
  * `loadQuizByNo` (Impact: 3.4)
  * `loadFile` (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 7 instances
* *Concurrency (weighted view):* 30
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 43`, `args: 11`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 15`
* *Architecture:* `io: 14`, `api: 9`, `concurrency: 20`, `import: 6`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.925
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` locales, types, fast-glob, fs-extra, js-yaml, node:path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/toUrl.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 91.06 | **LOC:** 86 | **CtrlFlow:** 44.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.5256%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `toQuizREADME` (Impact: 12.3)
  * `toRawREADME` (Impact: 9.0)
  * `toShareAnswerFull` (Impact: 9.0)
  * `toNearborREADME` (Impact: 8.9)
  * `toQuestionsRawREADME` (Impact: 5.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 44`, `args: 13`, `func_start: 12`
* *Risk/State:* None
* *Architecture:* `io: 11`, `api: 15`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.358
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00552
  * `Imports (Out-Degree: 2):` loader, locales, types, lz-string
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `scripts/translate.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 67.12 | **LOC:** 74 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (97.2653%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `translateMarkdown` (Impact: 15.4)
  * `translateAllQuizzes` (Impact: 7.6)
  * `translateQuiz` (Impact: 4.7)
  * `translateQuizByNo` (Impact: 4.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 21
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 30`, `args: 7`, `func_start: 4`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `io: 7`, `api: 4`, `concurrency: 11`, `import: 12`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.187
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000949
  * `Imports (Out-Degree: 3):` loader, locales, types, resolve, google-translate-api, fs-extra, node:path
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `questions/00925-extreme-assert-array-index/test-cases.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 52.06 | **LOC:** 101 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (62.9087%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`
* *Risk/State:* `state_mutation: 12`
* *Architecture:* None
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.925
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/build.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 50.02 | **LOC:** 55 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (98.2014%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `build` (Impact: 8.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 7 instances
* *Concurrency (weighted view):* 15
* *State Mutation (weighted view):* 25
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 15`, `args: 5`, `func_start: 1`
* *Risk/State:* `state_mutation: 11`
* *Architecture:* `io: 9`, `api: 1`, `concurrency: 5`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.925
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` formatToCode, loader, locales, toUrl, fs-extra, node:path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `questions/00697-extreme-tag/test-cases.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 39.32 | **LOC:** 162 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 22`
* *Architecture:* `import: 1`
* *Defense:* `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.925
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/actions/toggle-pr-with-issue.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 35.12 | **LOC:** 67 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (25.3506%), Tech Debt (50.0%)
**Top Internal Functions/Classes:**
  * `action` (Impact: 29.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 12`, `args: 3`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `concurrency: 4`, `import: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.925
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/actions/labeling.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 34.18 | **LOC:** 65 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (25.4629%), Tech Debt (45.3836%)
**Top Internal Functions/Classes:**
  * `action` (Impact: 27.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 12`, `args: 2`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `concurrency: 5`, `import: 1`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.925
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `questions/00020-medium-promise-all/test-cases.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 25.26 | **LOC:** 16 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`
* *Risk/State:* None
* *Architecture:* `concurrency: 10`, `import: 1`
* *Defense:* `doc: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.925
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `questions/00189-easy-awaited/test-cases.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 22.26 | **LOC:** 16 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 11`, `args: 1`
* *Risk/State:* `safety_bypasses: 2`
* *Architecture:* `concurrency: 7`, `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.925
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/locales.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 19.62 | **LOC:** 27 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.9138%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `t` (Impact: 9.0)
  * `f` (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 10`, `args: 2`, `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 6`, `import: 5`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.417
  * `Choke Point (Betweenness):` 4.7e-05 | `Ripple Effect (Closeness):` 0.012334
  * `Imports (Out-Degree: 5):` en.json, ja.json, ko.json, pt-BR.json, zh-CN.json
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `eslint.config.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 19.46 | **LOC:** 25 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.0173%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.925
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` eslint-config
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `questions/03326-medium-bem-style-string/test-cases.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 18.12 | **LOC:** 8 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.925
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `questions/26401-medium-json-schema-to-typescript/test-cases.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 17.68 | **LOC:** 161 | **CtrlFlow:** 4.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.2011%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 78`
* *Risk/State:* None
* *Architecture:* `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.925
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `questions/14080-hard-fizzbuzz/test-cases.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 17.58 | **LOC:** 131 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`
* *Risk/State:* None
* *Architecture:* `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.925
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `questions/00553-hard-deep-object-to-unique/test-cases.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 17.44 | **LOC:** 29 | **CtrlFlow:** 4.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.5311%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 12`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.925
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `questions/31997-extreme-parameter-intersection/test-cases.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 17.24 | **LOC:** 127 | **CtrlFlow:** 10.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.4661%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 31`
* *Risk/State:* None
* *Architecture:* `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.925
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `questions/31797-hard-sudoku/test-cases.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 16.98 | **LOC:** 109 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 12`
* *Risk/State:* None
* *Architecture:* `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.925
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `questions/00869-extreme-distributeunions/test-cases.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 16.54 | **LOC:** 83 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 18`
* *Risk/State:* None
* *Architecture:* `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.925
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `questions/33345-extreme-dynamic-route/test-cases.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 16.46 | **LOC:** 75 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.8761%), Tech Debt (99.0913%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 7`
* *Risk/State:* `planned_debt: 10`
* *Architecture:* `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.925
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `questions/09160-hard-assign/test-cases.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 16.42 | **LOC:** 93 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 19`
* *Risk/State:* None
* *Architecture:* `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.925
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `questions/00003-medium-omit/test-cases.ts` -> Churn: **100.0%** | Cog Load: 0.0% | Debt: 73.1059%

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `scripts/types.ts` -> **Severity: 0.704** (Embedded: 0.0116 * Error Risk: 60.5532%)
- `scripts/readme.ts` -> **Severity: 0.209** (Embedded: 0.0021 * Error Risk: 97.7435%)
- `scripts/actions/issue-pr.ts` -> **Severity: 0.074** (Embedded: 0.0009 * Error Risk: 78.2234%)
- `scripts/translate.ts` -> **Severity: 0.067** (Embedded: 0.0009 * Error Risk: 70.4417%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `scripts/locales.ts` -> **Severity: 641.7** (Blast Radius: 6.417 * Doc Risk: 100.0%)
- `scripts/toUrl.ts` -> **Severity: 235.8** (Blast Radius: 2.358 * Doc Risk: 100.0%)
- `scripts/actions/utils/formatToCode.ts` -> **Severity: 154.2** (Blast Radius: 1.542 * Doc Risk: 100.0%)
- `scripts/utils/resolve.ts` -> **Severity: 142.0** (Blast Radius: 1.42 * Doc Risk: 100.0%)
- `scripts/readme.ts` -> **Severity: 134.5** (Blast Radius: 1.345 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
