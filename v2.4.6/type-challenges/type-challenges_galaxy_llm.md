# ARCHITECTURAL_BRIEF: type-challenges
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_typescript/type-challenges` |
| **Timestamp** | `2026-08-03T19:59:33.765375+00:00` |
| **Scan Duration** | `1.05s` |
| **Git Branch** | `main` |
| **Git Commit** | `0b0b0b18bcb7ac42dc22ce26ffb438231d4754b1` |
| **Git Remote** | `https://github.com/type-challenges/type-challenges.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 213 malicious artifacts.

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
| Total Artifacts | 1088 |
| Analyzed Artifacts (Scanned) | 863 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 225 |
| Total LOC | 3037 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 79.3% |
| Dominant Lang | PLAINTEXT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.1769 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4833 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.883 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| MARKDOWN | 402 | 187 | 46.6% |
| YAML | 234 | 1302 | 27.1% |
| TYPESCRIPT | 211 | 1353 | 24.4% |
| JSON | 9 | 166 | 1.0% |
| PLAINTEXT | 4 | 1 | 0.5% |
| JAVASCRIPT | 1 | 23 | 0.1% |
| XML | 1 | 0 | 0.1% |
| SHELL | 1 | 5 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `3.269`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 282 | 32.7% |
| file_cluster_16 | 156 | 18.1% |
| file_cluster_2 | 8 | 0.9% |
| file_cluster_13 | 7 | 0.8% |
| file_cluster_4 | 3 | 0.3% |
| Unknown | 1 | 0.1% |
| file_cluster_17 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 403 | 46.7% |
| Static: Minified & Vendor Opaque Mass | 2 | 0.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 225*

**Composition by Extension & Reason:**
- `.ts`: 191x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 3209 LOC)
- `.yml`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.svg`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 3x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Unsupported Format (.toml)
- `.html`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.css`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 99.2 | 4.2 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 98.5 | 33.8 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 2.3 | 0.5 | 0.2 | 0.2 |
| API Exposure | 0.0 | 16.1 | 0.3 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 2.2 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 0.4 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 28.6 | 33.3 | 6.7 |
| Instability Exposure | 0.0 | 4.6 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 58.3 | 0.2 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 6.5 | 4.0 | 0.8 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 0.8 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `scripts/generate-play.ts` (Hits: 21)
- `scripts/loader.ts` (Hits: 14)
- `scripts/readme.ts` (Hits: 13)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **locales.ts** (`scripts/locales.ts`) — 13 inbound connections
2. **types.ts** (`scripts/types.ts`) — 12 inbound connections
3. **toUrl.ts** (`scripts/toUrl.ts`) — 5 inbound connections
4. **formatToCode.ts** (`scripts/actions/utils/formatToCode.ts`) — 3 inbound connections
5. **readme.ts** (`scripts/readme.ts`) — 2 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **generate-play.ts** (`scripts/generate-play.ts`) — 11 outbound dependencies
2. **issue-pr.ts** (`scripts/actions/issue-pr.ts`) — 9 outbound dependencies
3. **formatToCode.ts** (`scripts/actions/utils/formatToCode.ts`) — 7 outbound dependencies
4. **readme.ts** (`scripts/readme.ts`) — 7 outbound dependencies
5. **translate.ts** (`scripts/translate.ts`) — 7 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `Action` (@ `scripts/actions/issue-pr.ts`) -> Impact: **98.3** | LOC: 166
- `generatePlayground` (@ `scripts/generate-play.ts`) -> Impact: **58.9** | LOC: 86
- `Action` (@ `scripts/actions/labeling.ts`) -> Impact: **42.0** | LOC: 60
- `updateIndexREADME` (@ `scripts/readme.ts`) -> Impact: **29.6** | LOC: 53
- `Action` (@ `scripts/actions/toggle-pr-with-issue.ts`) -> Impact: **27.1** | LOC: 62
- `insertInfoReadme` (@ `scripts/readme.ts`) -> Impact: **26.6** | LOC: 41
- `takeSnapshot` (@ `scripts/generate-play.ts`) -> Impact: **25.1** | LOC: 23
- `loadInfo` (@ `scripts/loader.ts`) -> Impact: **19.1** | LOC: 22
- `resolveInfo` (@ `scripts/loader.ts`) -> Impact: **17.9** | LOC: 11
- `build` (@ `scripts/build.ts`) -> Impact: **17.8** | LOC: 45

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `takeSnapshot` (@ `scripts/generate-play.ts`) -> **O(2^N) [Recursive]**
- `updateComment` (@ `scripts/actions/issue-pr.ts`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `generatePlayground` (@ `scripts/generate-play.ts`) -> DB Complexity: **39**
- `build` (@ `scripts/build.ts`) -> DB Complexity: **26**
- `Action` (@ `scripts/actions/issue-pr.ts`) -> DB Complexity: **16**
- `loadQuiz` (@ `scripts/loader.ts`) -> DB Complexity: **15**
- `updateIndexREADME` (@ `scripts/readme.ts`) -> DB Complexity: **13**
- `takeSnapshot` (@ `scripts/generate-play.ts`) -> DB Complexity: **10**
- `insertInfoReadme` (@ `scripts/readme.ts`) -> DB Complexity: **10**
- `translateQuiz` (@ `scripts/translate.ts`) -> DB Complexity: **10**
- `toRawREADME` (@ `scripts/toUrl.ts`) -> DB Complexity: **9**
- `readPlaygroundCache` (@ `scripts/generate-play.ts`) -> DB Complexity: **8**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 13 | 5071.48 | 3.19% | 0.0% |
| `scripts` | 12 | 84.67 | 36.43% | 8.33% |
| `utils` | 5 | 47.14 | 6.57% | 0.0% |
| `questions/00002-medium-return-type` | 9 | 46.97 | 1.67% | 0.0% |
| `questions/00003-medium-omit` | 8 | 30.73 | 1.25% | 0.0% |
| `questions/00004-easy-pick` | 8 | 30.73 | 1.25% | 0.0% |
| `questions/00007-easy-readonly` | 8 | 30.73 | 1.25% | 0.0% |
| `questions/00008-medium-readonly-2` | 8 | 30.73 | 1.25% | 0.0% |
| `questions/00009-medium-deep-readonly` | 8 | 30.73 | 1.25% | 0.0% |
| `questions/00010-medium-tuple-to-union` | 8 | 30.73 | 1.25% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `questions/00925-extreme-assert-array-index/template.ts` -> **100.0%** Exposure
- `questions/30178-hard-unique-items/template.ts` -> **100.0%** Exposure
- `scripts/netlify.sh` -> **100.0%** Exposure
- `scripts/actions/issue-pr.ts` -> **13.4823%** Exposure
### Highest State Flux (Mutation/Volatility)
- `scripts/build.ts` -> **100.0%** Exposure
- `scripts/translate.ts` -> **61.2336%** Exposure
- `scripts/readme.ts` -> **36.3335%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `questions/00925-extreme-assert-array-index/template.ts` -> **1** Orphaned Functions | **0** Duplicates
- `questions/30178-hard-unique-items/template.ts` -> **1** Orphaned Functions | **0** Duplicates
- `scripts/netlify.sh` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`scripts/actions/issue-pr.ts`** -> AI Confidence: **99.31%**
2. **`scripts/generate-play.ts`** -> AI Confidence: **99.24%**
3. **`scripts/translate.ts`** -> AI Confidence: **99.16%**
4. **`scripts/readme.ts`** -> AI Confidence: **99.15%**
5. **`eslint.config.js`** -> AI Confidence: **99.06%**
6. **`scripts/actions/labeling.ts`** -> AI Confidence: **99.06%**
7. **`scripts/actions/toggle-pr-with-issue.ts`** -> AI Confidence: **99.06%**
8. **`scripts/actions/utils/formatToCode.ts`** -> AI Confidence: **99.06%**
9. **`scripts/actions/utils/toInfoHeader.ts`** -> AI Confidence: **99.0%**
10. **`scripts/build.ts`** -> AI Confidence: **98.96%**
11. **`scripts/toUrl.ts`** -> AI Confidence: **98.96%**
12. **`scripts/loader.ts`** -> AI Confidence: **98.93%**
13. **`scripts/locales.ts`** -> AI Confidence: **98.93%**
14. **`scripts/actions/utils/toCommentBlock.ts`** -> AI Confidence: **98.89%**
15. **`scripts/actions/utils/toFooter.ts`** -> AI Confidence: **98.88%**
16. **`scripts/actions/utils/toLinks.ts`** -> AI Confidence: **98.88%**
17. **`scripts/translate-cli.ts`** -> AI Confidence: **98.88%**
18. **`scripts/types.ts`** -> AI Confidence: **98.88%**
19. **`scripts/actions/loader.ts`** -> AI Confidence: **98.85%**
20. **`scripts/utils/resolve.ts`** -> AI Confidence: **98.85%**
21. **`questions/00002-medium-return-type/template.ts`** -> AI Confidence: **98.84%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Algorithmic DoS Exposure
- `scripts/build.ts` -> **100.0%** Exposure
- `scripts/readme.ts` -> **100.0%** Exposure
- `scripts/generate-play.ts` -> **96.7439%** Exposure
- `scripts/actions/issue-pr.ts` -> **43.0147%** Exposure
- `scripts/loader.ts` -> **1.7878%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `31` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `scripts/build.ts` (TYPESCRIPT) -> Cumulative Risk: **619.69**
- **Archetype:** `file_cluster_4` (Distance: 11.934 IQR)
- **Magnitude:** 5.96 | **LOC:** 55 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `build` (Impact: 17.8)

### 2. `scripts/translate.ts` (TYPESCRIPT) -> Cumulative Risk: **522.54**
- **Archetype:** `file_cluster_4` (Distance: 10.234 IQR)
- **Magnitude:** 7.58 | **LOC:** 74 | **CtrlFlow:** 29.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Cognitive Load (99.1113%), Documentation (89.7326%)
- **Heaviest Functions:** `translateMarkdown` (Impact: 15.4), `translateAllQuizzes` (Impact: 9.3), `translateQuiz` (Impact: 4.7)

### 3. `scripts/readme.ts` (TYPESCRIPT) -> Cumulative Risk: **446.46**
- **Archetype:** `file_cluster_17` (Distance: 10.259 IQR)
- **Magnitude:** 14.32 | **LOC:** 241 | **CtrlFlow:** 38.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Concurrency (99.9999%), Safety Score (61.3943%)
- **Heaviest Functions:** `updateIndexREADME` (Impact: 29.6), `insertInfoReadme` (Impact: 26.6), `quizToBadge` (Impact: 11.6)

### 4. `scripts/generate-play.ts` (TYPESCRIPT) -> Cumulative Risk: **441.05**
- **Archetype:** `file_cluster_13` (Distance: 10.157 IQR)
- **Magnitude:** 14.07 | **LOC:** 181 | **CtrlFlow:** 43.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (96.7439%), Safety Score (62.4593%)
- **Heaviest Functions:** `generatePlayground` (Impact: 58.9), `takeSnapshot` (Impact: 25.1), `readPlaygroundCache` (Impact: 8.8)

### 5. `scripts/loader.ts` (TYPESCRIPT) -> Cumulative Risk: **424.36**
- **Archetype:** `file_cluster_4` (Distance: 9.652 IQR)
- **Magnitude:** 10.48 | **LOC:** 118 | **CtrlFlow:** 35.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.999%), Documentation (95.6492%), Cognitive Load (64.8603%)
- **Heaviest Functions:** `loadInfo` (Impact: 19.1), `resolveInfo` (Impact: 17.9), `T` (Impact: 13.2)

### 6. `scripts/actions/issue-pr.ts` (TYPESCRIPT) -> Cumulative Risk: **356.76**
- **Archetype:** `file_cluster_8` (Distance: 8.42 IQR)
- **Magnitude:** 16.31 | **LOC:** 273 | **CtrlFlow:** 50.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Safety Score (49.2914%), Algorithmic Dos (43.0147%)
- **Heaviest Functions:** `Action` (Impact: 98.3), `updateComment` (Impact: 17.4), `getCodeBlock` (Impact: 10.4)

### 7. `scripts/types.ts` (TYPESCRIPT) -> Cumulative Risk: **309.68**
- **Archetype:** `file_cluster_13` (Distance: 8.237 IQR)
- **Magnitude:** 2.27 | **LOC:** 39 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.3687%), Safety Score (52.7749%), Concurrency (34.4328%)

### 8. `scripts/actions/labeling.ts` (TYPESCRIPT) -> Cumulative Risk: **303.21**
- **Archetype:** `file_cluster_8` (Distance: 7.81 IQR)
- **Magnitude:** 4.91 | **LOC:** 65 | **CtrlFlow:** 52.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9705%), Safety Score (47.9741%), Cognitive Load (28.3752%)
- **Heaviest Functions:** `Action` (Impact: 42.0)

### 9. `scripts/toUrl.ts` (TYPESCRIPT) -> Cumulative Risk: **298.75**
- **Archetype:** `file_cluster_8` (Distance: 8.955 IQR)
- **Magnitude:** 10.86 | **LOC:** 86 | **CtrlFlow:** 40.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.9999%), Safety Score (55.0959%), Cognitive Load (29.269%)
- **Heaviest Functions:** `toQuizREADME` (Impact: 12.3), `toRawREADME` (Impact: 9.0), `toShareAnswerFull` (Impact: 9.0)

### 10. `scripts/actions/toggle-pr-with-issue.ts` (TYPESCRIPT) -> Cumulative Risk: **292.37**
- **Archetype:** `file_cluster_8` (Distance: 7.615 IQR)
- **Magnitude:** 3.3 | **LOC:** 67 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (92.4634%), Safety Score (52.2712%), Cognitive Load (28.6377%)
- **Heaviest Functions:** `Action` (Impact: 27.1)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `utils/index.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.063 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 6.268 IQR)
- **Top Global Matches:** file_cluster_16: 11.063, file_cluster_2: 11.853, file_cluster_8: 11.934
- **Magnitude:** 32.04 | **LOC:** 30 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (22.86%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 53`, `args: 5`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 4`
* *Architecture:* `api: 15`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `eslint.config.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.827 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 5.612 IQR)
- **Top Global Matches:** file_cluster_8: 6.827, file_cluster_1: 6.857, file_cluster_13: 7.629
- **Magnitude:** 16.46 | **LOC:** 25 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (16.677%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` eslint-config
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/actions/issue-pr.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.42 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.686 IQR)
- **Top Global Matches:** file_cluster_8: 8.42, file_cluster_13: 8.818, file_cluster_7: 9.18
- **Magnitude:** 16.31 | **LOC:** 273 | **CtrlFlow:** 50.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (17.2807%), Tech Debt (13.4823%)
**Top Internal Functions/Classes:**
  * `Action` (Impact: 98.3 | O(N^2) | DB: 16)
  * `updateComment` (Impact: 17.4 | O(2^N))
  * `getCodeBlock` (Impact: 10.4 | O(N^1))
  * `getCommentRange` (Impact: 7.3 | O(N^1))
  * `getTimestampBadge` (Impact: 3.7 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 41`, `args: 13`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 3`, `fragile_debt: 1`
* *Architecture:* `io: 2`, `api: 3`, `concurrency: 13`, `import: 9`
* *Defense:* `safety: 5`, `doc: 1`, `immutability_locks: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.379
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00116
  * `Imports (Out-Degree: 6):` types, octokit-create-pull-request, js-yaml, resolve, formatToCode, readme, locales, limax...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `scripts/tsconfig.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 15.32 | **LOC:** 17 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (14.8047%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tsconfig.base.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 15.32 | **LOC:** 17 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (14.8047%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `questions/00002-medium-return-type/info.pt-BR.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.736 IQR)
- **Top Global Matches:** file_cluster_8: 5.736, file_cluster_7: 6.711, file_cluster_1: 6.8
- **Magnitude:** 15.2 | **LOC:** 16 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `questions/00002-medium-return-type/info.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.736 IQR)
- **Top Global Matches:** file_cluster_8: 5.736, file_cluster_7: 6.711, file_cluster_1: 6.8
- **Magnitude:** 15.2 | **LOC:** 16 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `questions/00189-easy-awaited/info.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.552 IQR)
- **Top Global Matches:** file_cluster_8: 6.552, file_cluster_7: 7.269, file_cluster_1: 7.36
- **Magnitude:** 14.68 | **LOC:** 10 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `questions/00191-medium-append-argument/info.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.552 IQR)
- **Top Global Matches:** file_cluster_8: 6.552, file_cluster_7: 7.269, file_cluster_1: 7.36
- **Magnitude:** 14.68 | **LOC:** 10 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/readme.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_17` (Drift: 10.259 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.559 IQR)
- **Top Global Matches:** file_cluster_17: 10.259, file_cluster_4: 10.33, file_cluster_13: 10.36
- **Magnitude:** 14.32 | **LOC:** 241 | **CtrlFlow:** 38.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (45.7003%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `updateIndexREADME` (Impact: 29.6 | O(N^2) | DB: 13)
  * `insertInfoReadme` (Impact: 26.6 | O(N^1) | DB: 10)
  * `quizToBadge` (Impact: 11.6 | O(N^1))
  * `getAllTags` (Impact: 9.1 | O(N^1) | DB: 2)
  * `escapeHtml` (Impact: 5.4 | O(N^1) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 46`, `args: 30`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 17`
* *Architecture:* `io: 13`, `api: 3`, `concurrency: 20`, `import: 9`
* *Defense:* `safety: 4`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.655
  * `Choke Point (Betweenness):` 1.7e-05 | `Ripple Effect (Closeness):` 0.00261
  * `Imports (Out-Degree: 3):` node:process, locales, fs-extra, types, loader, toUrl, node:path
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `questions/00003-medium-omit/info.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.947 IQR)
- **Top Global Matches:** file_cluster_8: 5.947, file_cluster_7: 6.848, file_cluster_1: 6.938
- **Magnitude:** 14.16 | **LOC:** 13 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `questions/00004-easy-pick/info.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.947 IQR)
- **Top Global Matches:** file_cluster_8: 5.947, file_cluster_7: 6.848, file_cluster_1: 6.938
- **Magnitude:** 14.16 | **LOC:** 13 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `questions/00007-easy-readonly/info.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.947 IQR)
- **Top Global Matches:** file_cluster_8: 5.947, file_cluster_7: 6.848, file_cluster_1: 6.938
- **Magnitude:** 14.16 | **LOC:** 13 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `questions/00008-medium-readonly-2/info.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.947 IQR)
- **Top Global Matches:** file_cluster_8: 5.947, file_cluster_7: 6.848, file_cluster_1: 6.938
- **Magnitude:** 14.16 | **LOC:** 13 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `questions/00009-medium-deep-readonly/info.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.947 IQR)
- **Top Global Matches:** file_cluster_8: 5.947, file_cluster_7: 6.848, file_cluster_1: 6.938
- **Magnitude:** 14.16 | **LOC:** 13 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `questions/00010-medium-tuple-to-union/info.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.947 IQR)
- **Top Global Matches:** file_cluster_8: 5.947, file_cluster_7: 6.848, file_cluster_1: 6.938
- **Magnitude:** 14.16 | **LOC:** 13 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `questions/00011-easy-tuple-to-object/info.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.947 IQR)
- **Top Global Matches:** file_cluster_8: 5.947, file_cluster_7: 6.848, file_cluster_1: 6.938
- **Magnitude:** 14.16 | **LOC:** 13 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `questions/00014-easy-first/info.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.947 IQR)
- **Top Global Matches:** file_cluster_8: 5.947, file_cluster_7: 6.848, file_cluster_1: 6.938
- **Magnitude:** 14.16 | **LOC:** 13 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `questions/00015-medium-last/info.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.947 IQR)
- **Top Global Matches:** file_cluster_8: 5.947, file_cluster_7: 6.848, file_cluster_1: 6.938
- **Magnitude:** 14.16 | **LOC:** 13 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `questions/00016-medium-pop/info.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.947 IQR)
- **Top Global Matches:** file_cluster_8: 5.947, file_cluster_7: 6.848, file_cluster_1: 6.938
- **Magnitude:** 14.16 | **LOC:** 13 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `questions/00017-hard-currying-1/info.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.947 IQR)
- **Top Global Matches:** file_cluster_8: 5.947, file_cluster_7: 6.848, file_cluster_1: 6.938
- **Magnitude:** 14.16 | **LOC:** 13 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `questions/00925-extreme-assert-array-index/info.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.947 IQR)
- **Top Global Matches:** file_cluster_8: 5.947, file_cluster_7: 6.848, file_cluster_1: 6.938
- **Magnitude:** 14.16 | **LOC:** 9 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `questions/06228-extreme-json-parser/info.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.947 IQR)
- **Top Global Matches:** file_cluster_8: 5.947, file_cluster_7: 6.848, file_cluster_1: 6.938
- **Magnitude:** 14.16 | **LOC:** 9 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/generate-play.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.157 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.243 IQR)
- **Top Global Matches:** file_cluster_13: 10.157, file_cluster_4: 10.229, file_cluster_8: 10.282
- **Magnitude:** 14.07 | **LOC:** 181 | **CtrlFlow:** 43.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 39
- **Risk Profile:** Cognitive Load (50.1724%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `generatePlayground` (Impact: 58.9 | O(N^2) | DB: 39)
  * `takeSnapshot` (Impact: 25.1 | O(2^N) | DB: 10)
  * `readPlaygroundCache` (Impact: 8.8 | O(N^1) | DB: 8)
  * `isQuizWritable` (Impact: 6.3 | O(N^1))
  * `calculateOverridableFiles` (Impact: 5.7 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 39`, `args: 14`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 11`
* *Architecture:* `io: 21`, `concurrency: 19`, `import: 11`
* *Defense:* `safety: 3`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.137
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` node:process, locales, formatToCode, fs-extra, types, loader, issue-pr, ansis...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `scripts/generate-play.ts` (TYPESCRIPT) | Magnitude: 14.07 | Delta: **0.072 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 120, structural_boundaries: 39, branch: 30, immutability_locks: 22
- `scripts/actions/utils/toFooter.ts` (TYPESCRIPT) | Magnitude: 0.42 | Delta: **0.146 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 8, import: 4, indent_spaces: 4, api: 2
- `scripts/types.ts` (TYPESCRIPT) | Magnitude: 2.27 | Delta: **0.186 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 21, branch: 6, api: 6
- `scripts/actions/loader.ts` (TYPESCRIPT) | Magnitude: 0.85 | Delta: **0.209 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 8, import: 5, structural_boundaries: 4, immutability_locks: 4
- `scripts/locales.ts` (TYPESCRIPT) | Magnitude: 1.96 | Delta: **0.21 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 10, api: 6, branch: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `questions/31997-extreme-parameter-intersection/template.ts` (TYPESCRIPT) | Magnitude: 1.21 | Delta: **0.114 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, safety: 2, generics: 2, immutability_locks: 2
- `questions/32532-hard-binary-addition/template.ts` (TYPESCRIPT) | Magnitude: 1.1 | Delta: **0.191 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, safety_bypasses: 1, generics: 1
- `questions/09160-hard-assign/template.ts` (TYPESCRIPT) | Magnitude: 1.05 | Delta: **0.409 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, safety: 1, safety_bypasses: 1, generics: 1
- `questions/21220-medium-permutations-of-tuple/template.ts` (TYPESCRIPT) | Magnitude: 1.05 | Delta: **0.409 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, safety: 1, safety_bypasses: 1, generics: 1
- `questions/27958-medium-checkrepeatedtuple/template.ts` (TYPESCRIPT) | Magnitude: 1.05 | Delta: **0.409 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, safety: 1, safety_bypasses: 1, generics: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `scripts/readme.ts` (TYPESCRIPT) | Magnitude: 14.32 | Delta: **0.071 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 127, structural_boundaries: 46, args: 30, branch: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `questions/00925-extreme-assert-array-index/template.ts` (TYPESCRIPT) | Magnitude: 0.18 | Delta: **0.187 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 1, args: 1, func_start: 1, safety: 1
- `utils/index.d.test.ts` (TYPESCRIPT) | Magnitude: 1.54 | Delta: **0.24 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 18, ui_framework: 14, generics: 14, bitwise_ops: 14
- `questions/00734-extreme-inclusive-range/template.ts` (TYPESCRIPT) | Magnitude: 1.05 | Delta: **0.382 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 3, safety_bypasses: 1, ui_framework: 1, generics: 1
- `questions/30575-hard-bitwisexor/template.ts` (TYPESCRIPT) | Magnitude: 1.05 | Delta: **0.382 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 3, safety_bypasses: 1, ui_framework: 1, generics: 1
- `questions/00191-medium-append-argument/template.ts` (TYPESCRIPT) | Magnitude: 1.05 | Delta: **0.387 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 1, safety_bypasses: 1, ui_framework: 1, generics: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `scripts/loader.ts` (TYPESCRIPT) | Magnitude: 10.48 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 69, structural_boundaries: 43, branch: 24, concurrency: 20
- `scripts/translate.ts` (TYPESCRIPT) | Magnitude: 7.58 | Delta: **0.179 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 40, structural_boundaries: 29, concurrency: 26, branch: 12
- `scripts/build.ts` (TYPESCRIPT) | Magnitude: 5.96 | Delta: **0.316 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 32, state_mutation: 25, structural_boundaries: 15, concurrency: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `scripts/actions/utils/formatToCode.ts` (TYPESCRIPT) | Magnitude: 1.03 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 12, import: 8, args: 4
- `eslint.config.js` (JAVASCRIPT) | Magnitude: 16.46 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_1`
  * Top Architectural Signatures: indent_spaces: 20, events: 13, immutability_locks: 2, branch: 1
- `scripts/toUrl.ts` (TYPESCRIPT) | Magnitude: 10.86 | Delta: **0.086 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 44, indent_spaces: 36, branch: 30, api: 27
- `scripts/translate-cli.ts` (TYPESCRIPT) | Magnitude: 0.72 | Delta: **0.261 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 7, concurrency: 5, indent_spaces: 4, import: 3
- `scripts/utils/resolve.ts` (TYPESCRIPT) | Magnitude: 0.91 | Delta: **0.303 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 4, branch: 2, api: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `scripts/readme.ts` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 36.3335%)
- `scripts/translate.ts` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 61.2336%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `scripts/types.ts` -> **Severity: 0.75** (Embedded: 0.0142 * Error Risk: 52.7749%)
- `scripts/toUrl.ts` -> **Severity: 0.372** (Embedded: 0.0067 * Error Risk: 55.0959%)
- `scripts/readme.ts` -> **Severity: 0.16** (Embedded: 0.0026 * Error Risk: 61.3943%)
- `scripts/translate.ts` -> **Severity: 0.078** (Embedded: 0.0012 * Error Risk: 67.0517%)
- `scripts/actions/issue-pr.ts` -> **Severity: 0.057** (Embedded: 0.0012 * Error Risk: 49.2914%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `scripts/locales.ts` -> **Severity: 788.737** (Blast Radius: 7.888 * Doc Risk: 99.992%)
- `scripts/types.ts` -> **Severity: 764.344** (Blast Radius: 7.692 * Doc Risk: 99.3687%)
- `scripts/toUrl.ts` -> **Severity: 289.9** (Blast Radius: 2.899 * Doc Risk: 99.9999%)
- `scripts/actions/utils/formatToCode.ts` -> **Severity: 145.712** (Blast Radius: 1.896 * Doc Risk: 76.8525%)
- `scripts/translate.ts` -> **Severity: 130.92** (Blast Radius: 1.459 * Doc Risk: 89.7326%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
