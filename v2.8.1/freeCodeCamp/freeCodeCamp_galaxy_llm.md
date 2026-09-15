# ARCHITECTURAL_BRIEF: freeCodeCamp
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/freeCodeCamp/freeCodeCamp.git` |
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
| Total Artifacts | 18528 |
| Analyzed Artifacts (Scanned) | 18306 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 222 |
| Total LOC | 207220 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 98.8% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5231 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1963 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.9939 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 162 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| MARKDOWN | 15918 | 0 | 87.0% |
| JSON | 1149 | 80157 | 6.3% |
| TYPESCRIPT | 899 | 90758 | 4.9% |
| JAVASCRIPT | 183 | 26671 | 1.0% |
| CSS | 86 | 7655 | 0.5% |
| YAML | 37 | 838 | 0.2% |
| PLAINTEXT | 18 | 1 | 0.1% |
| XML | 10 | 1006 | 0.1% |
| HTML | 2 | 21 | 0.0% |
| DOCKERFILE | 2 | 98 | 0.0% |
| SHELL | 2 | 15 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Flat Modular Platform` (z +0.52; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 94%, Declarative / Non-Code 2%, Callbacks & Closures Files 1%, I/O & Config Routines Files 1%, Large Core Modules 0%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 2360 | 12.9% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 15935 | 87.0% |
| Static: Minified & Vendor Opaque Mass | 10 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 222*

**Composition by Extension & Reason:**
- `.tsx`: 8x Excluded (Saturation: Line 13 exceeds 500 chars), 7x Excluded (Saturation: Line 18 exceeds 500 chars), 3x Excluded (Saturation: Line 16 exceeds 500 chars)
- `.md`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Machine-Generated Source Code Signature: 53 LOC), 2x Excluded (Machine-Generated Source Code Signature: 82 LOC)
- `.yml`: 28x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 11x Excluded (Static Asset Blob without Intent: 1531 LOC), 5x Excluded (Massive Static Asset Blob: 10022 LOC), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.woff`: 23x Excluded (Explicitly Denied Extension: '.woff')
- `.snap`: 17x Unsupported Format (.snap), 1x Excluded (Saturation: Line 6 exceeds 500 chars), 1x Excluded (Saturation: Line 59 exceeds 500 chars)
- `no_extension`: 19x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 14x Excluded (Explicitly Denied Extension: '.png')
- `.mjs`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.woff2`: 5x Excluded (Explicitly Denied Extension: '.woff2')
- `.yaml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 31800 LOC exceeds safe regex boundaries)
- `.prisma`: 3x Excluded (Unsupported Extension: '.prisma')
- `.js`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.css`: 1x Excluded (Saturation: Line 74 exceeds 500 chars), 1x Excluded (Saturation: Line 28 exceeds 500 chars)
- `.env`: 1x Excluded (Unsupported Extension: '.env'), 1x Unsupported Format (.env)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 8.2 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.9 | 14.1 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 2.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 2.2 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 7.7 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 13.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 11.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 80.2 | 0.2 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 37.6 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.9 | 0.5 | 0.4 | 0.4 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 87.1 | 10.0 | 12.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 26.3 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 293 | 125 | 0 | `client/src/templates/Introduction/components/block.test.tsx` |
| cleanup | 109 | 56 | 0 | `client/src/templates/Challenges/classic/show.tsx` |
| guards | 2232 | 428 | 0 | `api/src/routes/protected/settings.ts` |
| danger | 1019 | 251 | 0 | `api/__mocks__/exam-environment-exam.ts` |
| concurrency | 6789 | 389 | 0 | `api/src/routes/protected/challenge.test.ts` |
| connectivity | 2133 | 725 | 0 | `client/src/components/layouts/variables.css` |
| io | 1458 | 332 | 0 | `client/src/assets/icons/top-contributor-badge-emblem.tsx` |
| crypto | 1 | 1 | 0 | `tools/client-plugins/gatsby-source-challenges/create-challenge-nodes.js` |
| ipc | 101 | 46 | 0 | `packages/challenge-builder/src/worker-executor.test.js` |
| time | 286 | 83 | 0 | `api/src/exam-environment/routes/exam-environment.test.ts` |
| serialization | 115 | 51 | 0 | `api/src/exam-environment/routes/exam-environment.ts` |
| regex | 180 | 90 | 0 | `e2e/donate-page-default.spec.ts` |
| events | 659 | 156 | 0 | `api/src/routes/protected/challenge.ts` |
| tests | 7237 | 317 | 0 | `api/src/routes/protected/challenge.test.ts` |
| docs | 424 | 154 | 0 | `api/src/exam-environment/routes/exam-environment.test.ts` |
| debt | 511 | 204 | 0 | `curriculum/src/test/test-challenges.js` |
| mutation | 18297 | 1005 | 0 | `client/src/assets/icons/top-contributor-badge-emblem.tsx` |
| dead_code | 198 | 122 | 0 | `client/src/templates/Introduction/super-block-intro.test.tsx` |
| credential | 20 | 12 | 0 | `api/src/routes/protected/settings.test.ts` |
| threat | 68 | 32 | 0 | `client/i18n/schema-validation.ts` |
| ml_ai | 88 | 44 | 0 | `api/src/exam-environment/routes/exam-environment.ts` |
| ui | 4399 | 363 | 0 | `client/src/client-only-routes/show-certification.tsx` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `client/src/assets/icons/top-contributor-badge-emblem.tsx` (Hits: 80)
- `client/src/components/formHelpers/form-validators.test.ts` (Hits: 48)
- `api/src/routes/protected/settings.test.ts` (Hits: 47)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **react.json** (`curriculum/structure/blocks/react.json`) — 344 inbound connections
2. **react-i18next.js** (`client/__mocks__/react-i18next.js`) — 186 inbound connections
3. **prop-types.ts** (`client/src/redux/prop-types.ts`) — 92 inbound connections
4. **redux.json** (`curriculum/structure/blocks/redux.json`) — 59 inbound connections
5. **gatsby.ts** (`client/__mocks__/gatsby.ts`) — 40 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **schemas.ts** (`api/src/schemas.ts`) — 47 outbound dependencies
2. **show.tsx** (`client/src/templates/Challenges/classic/show.tsx`) — 46 outbound dependencies
3. **default.tsx** (`client/src/components/layouts/default.tsx`) — 39 outbound dependencies
4. **show.tsx** (`client/src/templates/Challenges/codeally/show.tsx`) — 36 outbound dependencies
5. **show.tsx** (`client/src/templates/Challenges/generic/show.tsx`) — 35 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `togglePane` **(Compute Cores)** (@ `client/src/templates/Challenges/classic/desktop-layout.tsx`) -> Impact: **98.7** | LOC: 221
- `Scene` **(Compute Cores)** (@ `client/src/templates/Challenges/components/scene/scene.tsx`) -> Impact: **84.3** | LOC: 413
- `generateExam` **(Compute Cores)** (@ `api/src/exam-environment/utils/exam-environment.ts`) -> Impact: **76.5** | LOC: 314
  * *Intent:* /** * Generates an exam for the user, based on the exam configuration. */
- `createLanguageBlock` **(Many-Argument Workhorses)** (@ `tools/challenge-helper-scripts/create-language-block.ts`) -> Impact: **68.5** | LOC: 73
- `render` **(I/O & Config Routines)** (@ `client/src/templates/Introduction/components/block.tsx`) -> Impact: **68.1** | LOC: 462
- `postExamGeneratedExamHandler` **(Many-Argument Workhorses)** (@ `api/src/exam-environment/routes/exam-environment.ts`) -> Impact: **66.8** | LOC: 336
  * *Intent:* /** * Generates an exam for the user. * * Requires token to be validated and TODO: live longer than the exam attempt. */
- `handleSubmit` **(Many-Argument Workhorses)** (@ `client/src/components/profile/components/experience.tsx`) -> Impact: **63.7** | LOC: 201
- `courseCompletionStatus` **(I/O & Config Routines)** (@ `client/src/templates/Introduction/components/block.tsx`) -> Impact: **61.5** | LOC: 411
- `sourceChallengesSourceNodes` **(Defensive Guards)** (@ `tools/client-plugins/gatsby-source-challenges/gatsby-node.js`) -> Impact: **61.1** | LOC: 217
- `transformer` **(Defensive Guards)** (@ `tools/challenge-parser/parser/plugins/add-video-question.js`) -> Impact: **58.6** | LOC: 132

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `e2e` | 123 | 21137.16 | 52.37% | 1.5% |
| `curriculum/structure/blocks` | 970 | 15887.02 | 0.0% | 0.0% |
| `api/src/routes/protected` | 11 | 11815.97 | 16.74% | 8.36% |
| `api/src/routes/public` | 21 | 5717.79 | 8.24% | 3.05% |
| `api/src/exam-environment/routes` | 2 | 5176.06 | 25.3% | 5.47% |
| `__monolith__` | 10 | 5094.12 | 0.0% | 0.0% |
| `client/src/templates/Challenges/components` | 65 | 3151.04 | 10.96% | 0.63% |
| `api/src/plugins` | 28 | 1912.48 | 22.79% | 5.96% |
| `client/src/components/profile/components` | 30 | 1830.4 | 6.71% | 0.0% |
| `api/src/exam-environment/utils` | 3 | 1789.22 | 6.67% | 3.72% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `api/src/utils/error-formatting.ts` -> **99.9756%** Exposure
- `api/src/utils/create-user.ts` -> **99.9712%** Exposure
- `client/gatsby-browser.tsx` -> **99.7527%** Exposure
- `client/gatsby-ssr.tsx` -> **99.2058%** Exposure
- `api/src/routes/helpers/user-utils.ts` -> **98.5936%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `curriculum/src/test/utils/challenge-titles.js` -> **100.0%** Exposure
- `curriculum/src/test/utils/mongo-ids.js` -> **100.0%** Exposure
- `curriculum/src/test/utils/pseudo-worker.js` -> **100.0%** Exposure
- `packages/challenge-builder/src/worker-executor.js` -> **100.0%** Exposure
- `tools/challenge-parser/parser/plugins/add-fill-in-the-blank.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `client/src/templates/Introduction/super-block-intro.test.tsx` -> **14** Orphaned Functions | **0** Duplicates
- `api/src/routes/protected/challenge.ts` -> **0** Orphaned Functions | **5** Duplicates
- `api/src/utils/exam-schemas.ts` -> **5** Orphaned Functions | **0** Duplicates
- `api/src/utils/logger.ts` -> **5** Orphaned Functions | **0** Duplicates
- `client/src/components/growth-book/growth-book-wrapper.test.tsx` -> **5** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `62` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2635` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `client/src/templates/Challenges/components/scene/scene.tsx` (TYPESCRIPT) -> Cumulative Risk: **663.66**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z -0.19)
- **Magnitude:** 261.3 | **LOC:** 449 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `Scene` (Compute Cores, Impact: 84.3), `resetScene` (Callbacks & Closures, Impact: 34.7), `updateCurrentTime` (Callbacks & Closures, Impact: 15.1)

### 2. `.github/scripts/pr-guidelines/fix-pr-title.js` (JAVASCRIPT) -> Cumulative Risk: **649.77**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z +1.08)
- **Magnitude:** 60.9 | **LOC:** 77 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Concurrency (98.9932%)
- **Heaviest Functions:** `exports` (Compute Cores, Impact: 15.5), `levenshtein` (Defensive Guards, Impact: 11.2)

### 3. `client/src/utils/ajax.ts` (TYPESCRIPT) -> Cumulative Risk: **640.36**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z -0.43)
- **Magnitude:** 211.3 | **LOC:** 520 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.6502%), Api Exposure (98.3393%), Documentation (95.4023%)
- **Heaviest Functions:** `parseApiResponseToClientUser` (Defensive Guards, Impact: 10.6), `getUserProfile` (Defensive Guards, Impact: 7.9), `getCSRFToken` (Defensive Guards, Impact: 4.2)

### 4. `client/src/templates/Challenges/utils/python-worker-handler.ts` (TYPESCRIPT) -> Cumulative Risk: **637.8**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +0.50)
- **Magnitude:** 82.0 | **LOC:** 114 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (86.2158%)
- **Heaviest Functions:** `registerTerminal` (Callbacks & Closures, Impact: 14.3), `listener` (Compute Cores, Impact: 10.0), `interruptCodeExecution` (Interface Declarations, Impact: 4.0)

### 5. `packages/challenge-builder/src/transformers.js` (JAVASCRIPT) -> Cumulative Risk: **634.69**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.95)
- **Magnitude:** 318.32 | **LOC:** 418 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (97.6397%)
- **Heaviest Functions:** `embedFilesInHtml` (Defensive Guards, Impact: 47.9), `embedStylesAndScript` (Defensive Guards, Impact: 47.7), `transformScript` (Compute Cores, Impact: 15.7)

### 6. `packages/challenge-builder/src/worker-executor.js` (JAVASCRIPT) -> Cumulative Risk: **634.54**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +1.31)
- **Magnitude:** 186.46 | **LOC:** 150 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `execute` (Callbacks & Closures, Impact: 9.2), `_execute` (Callbacks & Closures, Impact: 7.3), `_handleTaskEnd` (Callbacks & Closures, Impact: 6.5)

### 7. `tools/challenge-helper-scripts/create-language-block.ts` (TYPESCRIPT) -> Cumulative Risk: **633.02**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Compute Cores Files` (z +1.02)
- **Magnitude:** 0.54 | **LOC:** 636 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9997%), State Flux (99.9976%)
- **Heaviest Functions:** `createLanguageBlock` (Many-Argument Workhorses, Impact: 68.5), `validate` (Compute Cores, Impact: 28.9), `updateIntroJson` (Compute Cores, Impact: 24.3)

### 8. `client/src/templates/Challenges/classic/xterm.tsx` (TYPESCRIPT) -> Cumulative Risk: **626.2**
- **Archetype:** `file_cluster_8` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +1.01)
- **Magnitude:** 121.72 | **LOC:** 149 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9716%), Concurrency (99.9578%)
- **Heaviest Functions:** `createTerminal` (Defensive Guards, Impact: 27.4), `keyListener` (Defensive Guards, Impact: 15.1), `print` (Defensive Guards, Impact: 10.4)

### 9. `api/src/db/prisma.ts` (TYPESCRIPT) -> Cumulative Risk: **618.47**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z -0.98)
- **Magnitude:** 36.32 | **LOC:** 63 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (94.4799%)
- **Heaviest Functions:** `extendClient` (Interface Declarations, Impact: 2.6), `update` (Interface Declarations, Impact: 1.6), `updateMany` (Interface Declarations, Impact: 1.6)

### 10. `client/src/templates/Challenges/utils/frame.ts` (TYPESCRIPT) -> Cumulative Risk: **617.11**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.09)
- **Magnitude:** 231.86 | **LOC:** 483 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Verification (80.0%)
- **Heaviest Functions:** `createFramer` (Defensive Guards, Impact: 11.2), `prepTestRunner` (Defensive Guards, Impact: 8.4), `updateProxyConsole` (Defensive Guards, Impact: 8.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `api/src/routes/protected/settings.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 9230.47 | **LOC:** 1598 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (24.4652%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Concurrency (weighted view):* 241
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 284`, `args: 109`, `func_start: 73`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 5`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `io: 47`, `concurrency: 201`, `import: 7`
* *Defense:* `safety: 63`, `doc: 3`, `test: 284`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vitest.utils.js, redirect-with-message.js, create-user.js, env.js, auth-helpers.js, settings.js, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `api/src/exam-environment/routes/exam-environment.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 4833.42 | **LOC:** 1470 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (36.6956%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 70 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 532
* *State Mutation (weighted view):* 66
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 249`, `args: 77`, `func_start: 44`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 56`, `planned_debt: 1`
* *Architecture:* `io: 1`, `concurrency: 182`, `import: 12`
* *Defense:* `safety: 7`, `doc: 27`, `test: 170`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` exam-environment-exam.js, vitest.utils.js, env.js, exam-environment-exam-attempt.js, index.js, exam-environment.js, type-provider-typebox, client...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `api/src/routes/public/user.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3274.49 | **LOC:** 648 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (7.6745%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 45
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 69`, `args: 36`, `func_start: 12`
* *Risk/State:* `state_mutation: 2`, `planned_debt: 8`
* *Architecture:* `io: 11`, `concurrency: 35`, `import: 7`
* *Defense:* `safety: 21`, `test: 70`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vitest.utils.js, create-user.js, user.js, client, lodash-es, mongodb, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `api/src/exam-environment/utils/exam-environment.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1491.76 | **LOC:** 544 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (8.4038%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 99`, `args: 66`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 2`
* *Architecture:* `concurrency: 16`, `import: 8`
* *Defense:* `safety: 5`, `test: 59`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` exam-environment-exam.js, vitest.utils.js, index.js, exam-environment.js, type-provider-typebox, client, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `api/src/routes/public/email-subscription.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1036.92 | **LOC:** 283 | **CtrlFlow:** 8.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.7331%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 41`, `args: 15`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 2`, `planned_debt: 2`
* *Architecture:* `concurrency: 29`, `import: 5`
* *Defense:* `doc: 1`, `test: 39`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vitest.utils.js, create-user.js, env.js, client, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `api/src/routes/protected/certificate.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 909.8 | **LOC:** 477 | **CtrlFlow:** 3.1% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (8.4599%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 44
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 63`, `args: 22`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 4`, `dead_code: 1`, `planned_debt: 4`
* *Architecture:* `concurrency: 34`, `import: 5`
* *Defense:* `safety: 3`, `doc: 3`, `test: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` vitest.utils.js, get-challenges.js, certificate.js, certification-settings, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `api/src/routes/public/certificate.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 883.22 | **LOC:** 360 | **CtrlFlow:** 3.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.3172%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 67`, `args: 22`, `func_start: 11`
* *Risk/State:* `planned_debt: 1`
* *Architecture:* `concurrency: 35`, `import: 3`
* *Defense:* `safety: 7`, `test: 46`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vitest.utils.js, certificate-utils.js, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/src/components/profile/components/profile-completeness.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 876.02 | **LOC:** 221 | **CtrlFlow:** 7.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (8.4305%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 45`, `args: 26`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `io: 14`, `concurrency: 3`, `import: 5`
* *Defense:* `safety: 3`, `test: 52`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` profile-completeness, react, user-event, react, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `e2e/help-modal.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 860.12 | **LOC:** 250 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (99.2748%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 11 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 120
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 69`, `args: 10`, `func_start: 8`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `io: 2`, `concurrency: 65`, `import: 2`
* *Defense:* `test: 38`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` translations.json, test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `e2e/header.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 828.97 | **LOC:** 305 | **CtrlFlow:** 4.6% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (82.2642%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 1 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 91
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 86`, `args: 20`, `func_start: 14`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 2`
* *Architecture:* `io: 3`, `concurrency: 76`, `import: 5`
* *Defense:* `safety: 3`, `test: 58`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` links.json, translations.json, i18n, test, child_process
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `e2e/lower-jaw.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 698.23 | **LOC:** 251 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (99.9587%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 22 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 181
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 76`, `args: 10`, `func_start: 10`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `concurrency: 71`, `import: 3`
* *Defense:* `safety: 1`, `test: 33`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` editor, logout, test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `e2e/completion-modal.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 654.52 | **LOC:** 196 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (94.3102%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 1 instances
* *Amplified Race Conditions:* 4 instances
* *Concurrency (weighted view):* 81
* *Sec Tainted Injection (weighted view):* 1
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 71`, `args: 18`, `func_start: 14`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 2`
* *Architecture:* `io: 2`, `concurrency: 61`, `import: 5`
* *Defense:* `test: 48`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` translations.json, request, url, test, node:child_process
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `e2e/quiz-challenge.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 646.76 | **LOC:** 335 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (99.4337%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 152
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 101`, `args: 15`, `func_start: 8`, `class_start: 3`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `io: 11`, `concurrency: 92`, `import: 4`
* *Defense:* `test: 50`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` url, test, fs, path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/src/templates/Challenges/classic/editor.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 513.68 | **LOC:** 1462 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 37.5%
- **Risk Profile:** Cognitive Load (26.0009%), Tech Debt (13.1807%)
**Top Internal Functions/Classes:**
  * `setTabTrapped` **(Many-Argument Workhorses)** (Impact: 23.7)
  * `Editor` **(Compute Cores)** (Impact: 21.0)
  * `handleSubmitAndGoButtonBoolean` **(Defensive Guards)** (Impact: 17.1)
  * `createDescription` **(Compute Cores)** (Impact: 15.7)
  * `onChange` **(Defensive Guards)** (Impact: 14.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 43 instances
* *Concurrency (weighted view):* 18
* *State Mutation (weighted view):* 157
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 184`, `structural_boundaries: 180`, `args: 106`, `func_start: 62`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 5`, `state_mutation: 71`, `dead_code: 1`, `planned_debt: 8`, `fragile_debt: 2`
* *Architecture:* `io: 2`, `api: 7`, `concurrency: 3`, `import: 35`
* *Defense:* `safety: 42`, `doc: 4`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` env.json, green-pass, helpers, actions, prop-types, selectors, types, curriculum-layout...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/src/templates/Challenges/components/pinyin-to-hanzi-input.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 513.19 | **LOC:** 365 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (22.9263%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Concurrency (weighted view):* 38
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 55`, `args: 21`, `func_start: 8`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `concurrency: 23`, `import: 5`
* *Defense:* `test: 62`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` pinyin-to-hanzi-input, react, user-event, react, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `e2e/profile.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 501.41 | **LOC:** 209 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (29.269%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 37`, `args: 13`, `func_start: 6`
* *Risk/State:* None
* *Architecture:* `io: 1`, `concurrency: 30`, `import: 2`
* *Defense:* `test: 33`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` translations.json, test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `e2e/settings.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 497.24 | **LOC:** 357 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (59.9403%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 1 instances
* *Amplified Race Conditions:* 11 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 114
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 70`, `args: 13`, `func_start: 4`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 7`
* *Architecture:* `io: 2`, `concurrency: 59`, `import: 5`
* *Defense:* `test: 56`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` translations.json, alerts, certification-settings, test, child_process
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `e2e/daily-coding-challenge.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 478.78 | **LOC:** 301 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (73.4701%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 77`, `args: 17`, `func_start: 10`
* *Risk/State:* `dead_code: 1`
* *Architecture:* `io: 2`, `concurrency: 70`, `import: 2`
* *Defense:* `test: 45`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` helpers, test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `e2e/mobile-app-modal.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 456.87 | **LOC:** 160 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (67.4657%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 51`, `args: 18`, `func_start: 9`
* *Risk/State:* None
* *Architecture:* `io: 7`, `concurrency: 39`, `import: 2`
* *Defense:* `safety: 1`, `test: 26`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` translations.json, test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `e2e/help-button.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 426.49 | **LOC:** 172 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (75.3552%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 50`, `args: 11`, `func_start: 7`
* *Risk/State:* None
* *Architecture:* `concurrency: 44`, `import: 2`
* *Defense:* `safety: 5`, `test: 34`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` translations.json, test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `e2e/experience.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 421.54 | **LOC:** 133 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 3 instances
* *Amplified Race Conditions:* 49 instances
* *Concurrency (weighted view):* 304
* *Sec Tainted Injection (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 67`, `args: 13`, `func_start: 7`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 25`
* *Architecture:* `io: 1`, `concurrency: 59`, `import: 2`
* *Defense:* `safety: 14`, `test: 28`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` test, child_process
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/src/templates/Challenges/components/completion-modal.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 417.34 | **LOC:** 242 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (7.045%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 39`, `args: 17`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1`
* *Architecture:* `concurrency: 6`, `import: 16`
* *Defense:* `safety: 4`, `doc: 3`, `test: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` test-utils, create-store, prop-types, selectors, curriculum-data, fire-confetti, get-completion-percentage, execute-challenge-saga...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `api/src/routes/protected/user.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 404.42 | **LOC:** 1704 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (38.4721%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `json` **(Tests & Verification)** (Impact: 3.6)
  * `json` **(Tests & Verification)** (Impact: 2.5)
  * `json` **(Tests & Verification)** (Impact: 2.3)
  * `json` **(Tests & Verification)** (Impact: 1.9)
  * `json` **(Callbacks & Closures)** (Impact: 1.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 10 instances
* *Concurrency (weighted view):* 320
* *State Mutation (weighted view):* 43
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 307`, `args: 126`, `func_start: 65`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 23`, `planned_debt: 7`, `unreferenced_by_name: 1`
* *Architecture:* `io: 36`, `concurrency: 240`, `import: 11`
* *Defense:* `safety: 15`, `doc: 3`, `test: 226`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` exam-environment-exam.js, vitest.utils.js, create-user.js, env.js, user.js, client, jsonwebtoken, lodash-es...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `api/src/routes/protected/challenge.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 402.52 | **LOC:** 2556 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (13.6226%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `submitExam` **(Callbacks & Closures)** (Impact: 2.0)
  * `createMSUsernameRecord` **(Interface Declarations)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 338
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 378`, `args: 155`, `func_start: 82`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 12`, `dead_code: 1`, `planned_debt: 4`
* *Architecture:* `io: 33`, `concurrency: 268`, `import: 13`
* *Defense:* `safety: 34`, `doc: 6`, `test: 383`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` exam.js, vitest.utils.js, get-session-user.js, exam-types.js, challenge-helpers.js, type-provider-typebox, challenge-types, client...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `tools/challenge-helper-scripts/create-language-block.ts` -> Churn: **51.69%** | Cog Load: 94.3124% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `api/src/exam-environment/routes/exam-environment.test.ts` -> **Shaun Hamilton** (100.0% isolated ownership) | Magnitude: 4833.42
- `client/src/components/profile/components/profile-completeness.test.tsx` -> **Mrugesh Mohapatra** (100.0% isolated ownership) | Magnitude: 876.02
- `e2e/help-modal.spec.ts` -> **Ahmad Abdolsaheb** (100.0% isolated ownership) | Magnitude: 860.12
- `e2e/lower-jaw.spec.ts` -> **Ahmad Abdolsaheb** (100.0% isolated ownership) | Magnitude: 698.23
- `e2e/completion-modal.spec.ts` -> **Oliver Eyton-Williams** (100.0% isolated ownership) | Magnitude: 654.52

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `client/__mocks__/react-i18next.js` -> **Severity: 0.428** (Embedded: 0.0103 * Error Risk: 41.5116%)
- `packages/shared/src/config/chapters.ts` -> **Severity: 0.28** (Embedded: 0.0041 * Error Risk: 68.383%)
- `packages/shared/src/config/blocks.ts` -> **Severity: 0.245** (Embedded: 0.0043 * Error Risk: 56.3934%)
- `packages/shared/src/config/certification-settings.ts` -> **Severity: 0.232** (Embedded: 0.0046 * Error Risk: 50.5225%)
- `packages/shared/src/config/donation-settings.ts` -> **Severity: 0.118** (Embedded: 0.0021 * Error Risk: 55.7075%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `client/__mocks__/react-i18next.js` -> **Severity: 278.6** (Blast Radius: 2.786 * Doc Risk: 100.0%)
- `packages/shared/src/config/certification-settings.ts` -> **Severity: 110.5** (Blast Radius: 1.105 * Doc Risk: 100.0%)
- `packages/shared/src/config/challenge-types.ts` -> **Severity: 100.4** (Blast Radius: 1.004 * Doc Risk: 100.0%)
- `e2e/utils/editor.ts` -> **Severity: 61.6** (Blast Radius: 0.616 * Doc Risk: 100.0%)
- `packages/shared/src/utils/polyvinyl.ts` -> **Severity: 53.6** (Blast Radius: 0.536 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
