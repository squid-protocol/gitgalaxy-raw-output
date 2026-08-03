# ARCHITECTURAL_BRIEF: type-fest
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_typescript/type-fest` |
| **Timestamp** | `2026-08-03T19:59:36.450756+00:00` |
| **Scan Duration** | `0.49s` |
| **Git Branch** | `main` |
| **Git Commit** | `b390869422d9207e008863a8784914177e55fb4a` |
| **Git Remote** | `https://github.com/sindresorhus/type-fest.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 207 malicious artifacts.

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
| Total Artifacts | 453 |
| Analyzed Artifacts (Scanned) | 216 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 237 |
| Total LOC | 4843 |
| Volatility Index | 0.014 |
| % Scanned of codebase = | 47.7% |
| Dominant Lang | PLAINTEXT |

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
| TYPESCRIPT | 199 | 4185 | 92.1% |
| JAVASCRIPT | 8 | 631 | 3.7% |
| PLAINTEXT | 4 | 1 | 1.9% |
| MARKDOWN | 3 | 0 | 1.4% |
| XML | 1 | 14 | 0.5% |
| JSON | 1 | 12 | 0.5% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.498`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_16 | 115 | 53.2% |
| file_cluster_13 | 57 | 26.4% |
| file_cluster_8 | 21 | 9.7% |
| file_cluster_2 | 14 | 6.5% |
| Unknown | 1 | 0.5% |
| file_cluster_1 | 1 | 0.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 6 | 2.8% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 237*

**Composition by Extension & Reason:**
- `.ts`: 207x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 11 exceeds 500 chars), 1x Excluded (Saturation: Line 12 exceeds 500 chars)
- `.yml`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 2x Excluded (Explicitly Denied Extension: '.png')
- `.sketch`: 1x Excluded (Explicitly Denied Extension: '.sketch')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 23.3 | 5.1 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 80.0 | 7.7 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 3.1 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 1.9 | 1.5 | 2.3 |
| API Exposure | 0.0 | 19.5 | 5.3 | 5.3 | 6.0 |
| Concurrency Exposure | 0.0 | 70.2 | 1.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 0.9 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 11.1 | 0.1 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 66.0 | 66.7 | 100.0 |
| Instability Exposure | 0.0 | 5.5 | 1.9 | 0.6 | 0.0 |
| Volatility Exposure | 0.0 | 91.4 | 19.1 | 10.8 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 18.0 | 14.9 | 17.9 |
| Algorithmic DoS Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `lint-rules/require-exported-types.js` (Hits: 10)
- `lint-rules/import-path.js` (Hits: 4)
- `lint-rules/source-files-extension.js` (Hits: 3)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **CLAUDE.md** (`CLAUDE.md`) — 0 inbound connections
2. **readme.md** (`media/readme.md`) — 0 inbound connections
3. **readme.md** (`readme.md`) — 0 inbound connections
4. **index.d.ts** (`index.d.ts`) — 0 inbound connections
5. **absolute.d.ts** (`source/absolute.d.ts`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.d.ts** (`index.d.ts`) — 190 outbound dependencies
2. **object.d.ts** (`source/internal/object.d.ts`) — 13 outbound dependencies
3. **array-slice.d.ts** (`source/array-slice.d.ts`) — 11 outbound dependencies
4. **merge-deep.d.ts** (`source/merge-deep.d.ts`) — 11 outbound dependencies
5. **jsonify.d.ts** (`source/jsonify.d.ts`) — 10 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `create` (@ `lint-rules/require-exported-types.js`) -> Impact: **39.5** | LOC: 111
- `preprocess` (@ `lint-processors/jsdoc-codeblocks.js`) -> Impact: **36.8** | LOC: 78
- `create` (@ `lint-rules/validate-jsdoc-codeblocks.js`) -> Impact: **28.3** | LOC: 56
- `parseCompilerOptions` (@ `lint-rules/validate-jsdoc-codeblocks.js`) -> Impact: **13.5** | LOC: 28
- `indentsUptoIndex` (@ `lint-processors/jsdoc-codeblocks.js`) -> Impact: **13.1** | LOC: 21
  * *Intent:* /**
- `create` (@ `lint-rules/import-path.js`) -> Impact: **11.9** | LOC: 40
- `create` (@ `lint-rules/require-export.js`) -> Impact: **11.4** | LOC: 31
- `getJSDocNode` (@ `lint-rules/validate-jsdoc-codeblocks.js`) -> Impact: **11.1** | LOC: 14
- `create` (@ `lint-rules/source-files-extension.js`) -> Impact: **6.9** | LOC: 25
- `create` (@ `lint-processors/fixtures/eslint.config.js`) -> Impact: **4.0** | LOC: 23

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Data Gravity (Database Complexity)
- `create` (@ `lint-rules/require-exported-types.js`) -> DB Complexity: **21**
- `preprocess` (@ `lint-processors/jsdoc-codeblocks.js`) -> DB Complexity: **3**
- `create` (@ `lint-rules/import-path.js`) -> DB Complexity: **3**
- `create` (@ `lint-rules/source-files-extension.js`) -> DB Complexity: **3**
- `indentsUptoIndex` (@ `lint-processors/jsdoc-codeblocks.js`) -> DB Complexity: **2**
  * *Intent:* /**
- `create` (@ `lint-rules/validate-jsdoc-codeblocks.js`) -> DB Complexity: **2**
- `parseCompilerOptions` (@ `lint-rules/validate-jsdoc-codeblocks.js`) -> DB Complexity: **2**
- `create` (@ `lint-rules/require-export.js`) -> DB Complexity: **1**
- `getJSDocNode` (@ `lint-rules/validate-jsdoc-codeblocks.js`) -> DB Complexity: **1**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 9 | 5087.28 | 1.49% | 0.0% |
| `source` | 186 | 335.08 | 4.89% | 2.64% |
| `lint-rules` | 5 | 163.7 | 10.34% | 0.0% |
| `lint-processors` | 1 | 64.38 | 23.31% | 0.0% |
| `source/internal` | 10 | 22.6 | 6.72% | 1.65% |
| `source/globals` | 2 | 2.55 | 1.21% | 49.52% |
| `media` | 2 | 2.0 | 0.0% | 0.0% |
| `lint-processors/fixtures` | 1 | 0.01 | 4.35% | 52.15% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `source/keys-of-union.d.ts` -> **100.0%** Exposure
- `source/arrayable.d.ts` -> **99.9955%** Exposure
- `source/globals/observable-like.d.ts` -> **99.0462%** Exposure
- `source/iterable-element.d.ts` -> **99.0462%** Exposure
- `source/sum.d.ts` -> **74.4868%** Exposure
### Highest State Flux (Mutation/Volatility)
- `source/fixed-length-array.d.ts` -> **100.0%** Exposure
- `lint-rules/require-export.js` -> **43.0454%** Exposure
- `source/words.d.ts` -> **26.1852%** Exposure
- `source/omit-deep.d.ts` -> **16.1747%** Exposure
- `lint-processors/jsdoc-codeblocks.js` -> **11.8185%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `lint-processors/fixtures/eslint.config.js` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`source/array-slice.d.ts`** -> AI Confidence: **99.18%**
2. **`source/exact.d.ts`** -> AI Confidence: **99.18%**
3. **`source/get.d.ts`** -> AI Confidence: **99.18%**
4. **`source/greater-than.d.ts`** -> AI Confidence: **99.18%**
5. **`source/internal/object.d.ts`** -> AI Confidence: **99.18%**
6. **`source/merge-deep.d.ts`** -> AI Confidence: **99.18%**
7. **`source/object-merge.d.ts`** -> AI Confidence: **99.18%**
8. **`source/omit-deep.d.ts`** -> AI Confidence: **99.18%**
9. **`source/split-on-rest-element.d.ts`** -> AI Confidence: **99.18%**
10. **`source/tsconfig-json.d.ts`** -> AI Confidence: **99.17%**
11. **`lint-processors/jsdoc-codeblocks.js`** -> AI Confidence: **99.17%**
12. **`source/jsonify.d.ts`** -> AI Confidence: **99.16%**
13. **`source/pick-deep.d.ts`** -> AI Confidence: **99.16%**
14. **`source/paths.d.ts`** -> AI Confidence: **99.15%**
15. **`lint-rules/validate-jsdoc-codeblocks.js`** -> AI Confidence: **99.14%**
16. **`index.d.ts`** -> AI Confidence: **99.09%**
17. **`source/internal/index.d.ts`** -> AI Confidence: **99.08%**
18. **`xo.config.js`** -> AI Confidence: **99.08%**
19. **`source/all-extend.d.ts`** -> AI Confidence: **99.07%**
20. **`source/conditional-pick-deep.d.ts`** -> AI Confidence: **99.07%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `196` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `index.d.ts` (TYPESCRIPT) -> Cumulative Risk: **375.36**
- **Archetype:** `file_cluster_13` (Distance: 9.59 IQR)
- **Magnitude:** 21.42 | **LOC:** 220 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 45.5%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Churn (91.42%), Safety Score (39.953%)

### 2. `lint-rules/validate-jsdoc-codeblocks.js` (JAVASCRIPT) -> Cumulative Risk: **293.23**
- **Archetype:** `file_cluster_8` (Distance: 10.019 IQR)
- **Magnitude:** 67.46 | **LOC:** 421 | **CtrlFlow:** 70.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), Churn (73.74%), Documentation (17.8804%)
- **Heaviest Functions:** `create` (Impact: 28.3), `parseCompilerOptions` (Impact: 13.5), `getJSDocNode` (Impact: 11.1)

### 3. `source/set-readonly.d.ts` (TYPESCRIPT) -> Cumulative Risk: **284.49**
- **Archetype:** `file_cluster_13` (Distance: 11.546 IQR)
- **Magnitude:** 1.83 | **LOC:** 41 | **CtrlFlow:** 10.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Churn (52.53%), Safety Score (20.7236%)

### 4. `lint-rules/require-export.js` (JAVASCRIPT) -> Cumulative Risk: **262.46**
- **Archetype:** `file_cluster_8` (Distance: 8.806 IQR)
- **Magnitude:** 19.2 | **LOC:** 47 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (91.409%), State Flux (43.0454%), Cognitive Load (9.6589%)
- **Heaviest Functions:** `create` (Impact: 11.4)

### 5. `source/required-deep.d.ts` (TYPESCRIPT) -> Cumulative Risk: **259.07**
- **Archetype:** `file_cluster_16` (Distance: 10.542 IQR)
- **Magnitude:** 1.96 | **LOC:** 77 | **CtrlFlow:** 34.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (69.1474%), Safety Score (33.2239%), Cognitive Load (20.374%)

### 6. `source/globals/observable-like.d.ts` (TYPESCRIPT) -> Cumulative Risk: **250.38**
- **Archetype:** `file_cluster_16` (Distance: 13.0 IQR)
- **Magnitude:** 1.25 | **LOC:** 79 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.0462%), Documentation (37.6422%), Api Exposure (8.8813%)
- **Heaviest Functions:** `subscribe` (Impact: 3.7), `unsubscribe` (Impact: 2.4)

### 7. `source/words.d.ts` (TYPESCRIPT) -> Cumulative Risk: **248.44**
- **Archetype:** `file_cluster_2` (Distance: 9.404 IQR)
- **Magnitude:** 2.38 | **LOC:** 149 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Spec Match (100.0%), Churn (52.53%), Safety Score (40.8675%), State Flux (26.1852%)

### 8. `source/fixed-length-array.d.ts` (TYPESCRIPT) -> Cumulative Risk: **243.1**
- **Archetype:** `file_cluster_13` (Distance: 12.453 IQR)
- **Magnitude:** 2.12 | **LOC:** 98 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (53.3333%), Safety Score (49.1965%), Churn (16.23%)

### 9. `source/internal/numeric.d.ts` (TYPESCRIPT) -> Cumulative Risk: **242.57**
- **Archetype:** `file_cluster_16` (Distance: 9.222 IQR)
- **Magnitude:** 2.2 | **LOC:** 142 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Churn (60.99%), Documentation (39.8803%), Safety Score (30.3402%)

### 10. `source/internal/type.d.ts` (TYPESCRIPT) -> Cumulative Risk: **242.38**
- **Archetype:** `file_cluster_16` (Distance: 12.958 IQR)
- **Magnitude:** 2.87 | **LOC:** 166 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (49.2492%), Concurrency (33.4361%), Churn (33.12%)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lint-rules/validate-jsdoc-codeblocks.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.14%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.019 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 4.717 IQR)
- **Top Global Matches:** file_cluster_8: 10.019, file_cluster_13: 10.28, file_cluster_7: 10.521
- **Magnitude:** 67.46 | **LOC:** 421 | **CtrlFlow:** 70.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (13.8199%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `create` (Impact: 28.3 | O(N^1) | DB: 2)
  * `parseCompilerOptions` (Impact: 13.5 | O(N^1) | DB: 2)
  * `getJSDocNode` (Impact: 11.1 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 14`, `args: 4`, `func_start: 4`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `io: 3`, `api: 3`, `import: 3`
* *Defense:* `safety: 9`, `doc: 5`, `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` typescript, node:path, vfs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lint-processors/jsdoc-codeblocks.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.914 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 5.304 IQR)
- **Top Global Matches:** file_cluster_8: 11.914, file_cluster_17: 12.02, file_cluster_13: 12.061
- **Magnitude:** 64.38 | **LOC:** 173 | **CtrlFlow:** 76.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (23.3134%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `preprocess` (Impact: 36.8 | O(N^1) | DB: 3)
  * `indentsUptoIndex` (Impact: 13.1 | O(N^1) | DB: 2)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 9`, `args: 5`, `func_start: 2`
* *Risk/State:* `state_mutation: 11`
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `safety: 7`, `doc: 18`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` parser, eslint
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lint-rules/require-exported-types.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.77 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.653 IQR)
- **Top Global Matches:** file_cluster_8: 9.77, file_cluster_13: 9.928, file_cluster_17: 10.224
- **Magnitude:** 52.54 | **LOC:** 143 | **CtrlFlow:** 64.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (18.2072%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `create` (Impact: 39.5 | O(N^1) | DB: 21)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 13`, `args: 3`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 9`
* *Architecture:* `io: 10`, `api: 2`, `import: 3`
* *Defense:* `safety: 7`, `doc: 2`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:path, node:fs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `source/set-parameter-type.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.021 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.89 IQR)
- **Top Global Matches:** file_cluster_16: 11.021, file_cluster_13: 11.077, file_cluster_2: 11.099
- **Magnitude:** 29.67 | **LOC:** 126 | **CtrlFlow:** 7.8% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (3.9406%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 71`, `args: 13`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 5`
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* `safety: 14`, `doc: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.d.ts, is-unknown.d.ts, unknown-array.d.ts, type-fest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xo.config.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_1` (Drift: 8.395 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 5.629 IQR)
- **Top Global Matches:** file_cluster_1: 8.395, file_cluster_8: 8.632, file_cluster_0: 8.915
- **Magnitude:** 21.88 | **LOC:** 155 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (2.5668%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 17`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `io: 3`, `api: 4`, `import: 7`
* *Defense:* `doc: 29`, `test: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` validate-jsdoc-codeblocks.js, source-files-extension.js, import-path.js, jsdoc-codeblocks.js, require-exported-types.js, xo, require-export.js, typescript-eslint
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `readme.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 21.5 | **LOC:** 1075 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `index.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.59 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.527 IQR)
- **Top Global Matches:** file_cluster_13: 9.59, file_cluster_8: 10.514, file_cluster_0: 11.06
- **Magnitude:** 21.42 | **LOC:** 220 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 45.5%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.8872%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 389`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 3`
* *Architecture:* `api: 191`, `concurrency: 1`, `import: 190`
* *Defense:* `safety: 8`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` split-on-rest-element.d.ts, extends-strict.d.ts, camel-cased-properties-deep.d.ts, set-required-deep.d.ts, conditional-pick-deep.d.ts, union-to-intersection.d.ts, set-readonly.d.ts, xor.d.ts...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lint-rules/require-export.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.806 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.211 IQR)
- **Top Global Matches:** file_cluster_8: 8.806, file_cluster_7: 9.338, file_cluster_1: 9.662
- **Magnitude:** 19.2 | **LOC:** 47 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (9.6589%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `create` (Impact: 11.4 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 7`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 4`
* *Defense:* `safety: 1`, `doc: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tsconfig.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 15.24 | **LOC:** 13 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lint-rules/import-path.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.61 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.211 IQR)
- **Top Global Matches:** file_cluster_8: 7.61, file_cluster_7: 8.321, file_cluster_13: 8.419
- **Magnitude:** 14.84 | **LOC:** 58 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (5.7159%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `create` (Impact: 11.9 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 8`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 2`
* *Architecture:* `io: 4`, `api: 2`, `import: 1`
* *Defense:* `safety: 2`, `doc: 2`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lint-rules/source-files-extension.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.926 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 4.42 IQR)
- **Top Global Matches:** file_cluster_8: 7.926, file_cluster_7: 8.588, file_cluster_13: 8.641
- **Magnitude:** 9.66 | **LOC:** 43 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (4.2953%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `create` (Impact: 6.9 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 4`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 2`
* *Architecture:* `io: 3`, `api: 2`, `import: 1`
* *Defense:* `safety: 2`, `doc: 2`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `source/tsconfig-json.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.456 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 2.748 IQR)
- **Top Global Matches:** file_cluster_8: 8.456, file_cluster_7: 8.723, file_cluster_1: 8.983
- **Magnitude:** 3.16 | **LOC:** 1325 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0193%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 22`
* *Risk/State:* None
* *Architecture:* `api: 3`, `concurrency: 6`
* *Defense:* `doc: 74`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `source/internal/type.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.958 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 6.11 IQR)
- **Top Global Matches:** file_cluster_16: 12.958, file_cluster_13: 12.999, file_cluster_2: 13.402
- **Magnitude:** 2.87 | **LOC:** 166 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (9.6707%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 50`, `args: 2`
* *Risk/State:* `safety_bypasses: 4`
* *Architecture:* `api: 12`, `concurrency: 1`, `import: 6`
* *Defense:* `safety: 14`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` is-any.d.ts, unknown-array.d.ts, type-fest, primitive.d.ts, union-to-intersection.d.ts, is-never.d.ts, if.d.ts
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `source/internal/object.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.73 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.517 IQR)
- **Top Global Matches:** file_cluster_16: 11.73, file_cluster_13: 11.839, file_cluster_2: 12.047
- **Magnitude:** 2.64 | **LOC:** 293 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.3889%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 72`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `api: 10`, `import: 12`
* *Defense:* `safety: 13`, `doc: 9`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` type.d.ts, is-any.d.ts, simplify.d.ts, string.d.ts, optional-keys-of.d.ts, type-fest, keys-of-union.d.ts, required-keys-of.d.ts...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `source/numeric.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.312 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.483 IQR)
- **Top Global Matches:** file_cluster_16: 13.312, file_cluster_13: 13.622, file_cluster_2: 14.015
- **Magnitude:** 2.64 | **LOC:** 227 | **CtrlFlow:** 17.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (8.4072%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 39`
* *Risk/State:* None
* *Architecture:* `api: 11`, `import: 2`
* *Defense:* `safety: 9`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` is-float.d.ts, type-fest, is-integer.d.ts
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `source/internal/index.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_13` (Drift: 7.507 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.052 IQR)
- **Top Global Matches:** file_cluster_13: 7.507, file_cluster_8: 8.183, file_cluster_7: 9.032
- **Magnitude:** 2.52 | **LOC:** 12 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 20`
* *Risk/State:* None
* *Architecture:* `api: 10`, `import: 9`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` object.d.ts, array.d.ts, numeric.d.ts, type.d.ts, tuple.d.ts, characters.d.ts, string.d.ts, enforce-optional.d.ts...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `source/internal/string.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.933 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.958 IQR)
- **Top Global Matches:** file_cluster_16: 10.933, file_cluster_13: 11.468, file_cluster_8: 11.733
- **Magnitude:** 2.52 | **LOC:** 203 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (7.9666%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 68`
* *Risk/State:* None
* *Architecture:* `api: 9`, `import: 4`
* *Defense:* `safety: 12`, `doc: 10`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` characters.d.ts, numeric.d.ts, trim.d.ts, tuple-of.d.ts
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `license-cc0` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 2.44 | **LOC:** 122 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `source/internal/array.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.226 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.102 IQR)
- **Top Global Matches:** file_cluster_16: 11.226, file_cluster_13: 11.472, file_cluster_2: 11.736
- **Magnitude:** 2.41 | **LOC:** 145 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.9925%), Tech Debt (16.4818%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 53`
* *Risk/State:* `planned_debt: 1`
* *Architecture:* `api: 8`, `import: 5`
* *Defense:* `safety: 13`, `doc: 7`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` type.d.ts, optional-keys-of.d.ts, unknown-array.d.ts, is-never.d.ts, if.d.ts
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `source/words.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_2` (Drift: 9.404 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.782 IQR)
- **Top Global Matches:** file_cluster_2: 9.404, file_cluster_16: 9.456, file_cluster_13: 9.718
- **Magnitude:** 2.38 | **LOC:** 149 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.7518%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 59`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* `safety: 3`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.d.ts, is-uppercase.d.ts, is-lowercase.d.ts, type-fest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CLAUDE.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 2.32 | **LOC:** 116 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `source/is-literal.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_16` (Drift: 9.782 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.162 IQR)
- **Top Global Matches:** file_cluster_16: 9.782, file_cluster_13: 10.187, file_cluster_8: 10.555
- **Magnitude:** 2.29 | **LOC:** 316 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (4.3093%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 36`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `api: 7`, `import: 5`
* *Defense:* `safety: 3`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` numeric.d.ts, tagged.d.ts, primitive.d.ts, index.d.ts, is-never.d.ts, type-fest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `source/merge-deep.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_2` (Drift: 10.106 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.194 IQR)
- **Top Global Matches:** file_cluster_2: 10.106, file_cluster_16: 10.168, file_cluster_13: 10.612
- **Magnitude:** 2.24 | **LOC:** 496 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (4.1287%), Tech Debt (9.3584%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 145`
* *Risk/State:* `planned_debt: 1`
* *Architecture:* `api: 3`, `import: 10`
* *Defense:* `safety: 13`, `doc: 26`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` non-empty-tuple.d.ts, simplify-deep.d.ts, merge.d.ts, pick-index-signature.d.ts, index.d.ts, unknown-record.d.ts, array-tail.d.ts, unknown-array.d.ts...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `source/internal/numeric.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_16` (Drift: 9.222 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.086 IQR)
- **Top Global Matches:** file_cluster_16: 9.222, file_cluster_8: 9.564, file_cluster_13: 9.677
- **Magnitude:** 2.2 | **LOC:** 142 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (3.757%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 69`
* *Risk/State:* `safety_bypasses: 2`
* *Architecture:* `api: 5`, `import: 4`
* *Defense:* `safety: 8`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.63
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` numeric.d.ts, unknown-array.d.ts, is-never.d.ts, type.d.ts
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `xo.config.js` (JAVASCRIPT) | Magnitude: 21.88 | Delta: **0.237 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 134, events: 31, doc: 29, decorators: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `source/pascal-cased-properties.d.ts` (TYPESCRIPT) | Magnitude: 1.67 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 12, generics: 6, branch: 4, indent_tabs: 4
- `source/extends-strict.d.ts` (TYPESCRIPT) | Magnitude: 1.72 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 10, generics: 7, indent_tabs: 7, ui_framework: 4
- `source/conditional-pick-deep.d.ts` (TYPESCRIPT) | Magnitude: 1.88 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 32, indent_tabs: 20, generics: 16, ui_framework: 9
- `source/distributed-omit.d.ts` (TYPESCRIPT) | Magnitude: 1.51 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 7, generics: 4, ui_framework: 3, indent_tabs: 3
- `source/string-slice.d.ts` (TYPESCRIPT) | Magnitude: 1.73 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 15, generics: 7, indent_tabs: 7, safety: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `source/array-tail.d.ts` (TYPESCRIPT) | Magnitude: 1.74 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 17, generics: 12, indent_tabs: 11, branch: 7
- `source/remove-prefix.d.ts` (TYPESCRIPT) | Magnitude: 1.86 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 25, indent_tabs: 18, generics: 9, ui_framework: 5
- `source/async-return-type.d.ts` (TYPESCRIPT) | Magnitude: 1.36 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 6, ui_framework: 3, generics: 3, api: 2
- `source/globals/observable-like.d.ts` (TYPESCRIPT) | Magnitude: 1.25 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 15, indent_tabs: 9, doc: 7, ui_framework: 7
- `source/set-optional.d.ts` (TYPESCRIPT) | Magnitude: 1.73 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 16, generics: 12, indent_tabs: 10, ui_framework: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `source/value-of.d.ts` (TYPESCRIPT) | Magnitude: 1.3 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 4, api: 2, doc: 1, ui_framework: 1
- `source/invariant-of.d.ts` (TYPESCRIPT) | Magnitude: 1.36 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 5, api: 2, args: 1, doc: 1
- `source/require-exactly-one.d.ts` (TYPESCRIPT) | Magnitude: 1.73 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 14, ui_framework: 14, generics: 11, indent_tabs: 9
- `source/optional.d.ts` (TYPESCRIPT) | Magnitude: 1.3 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 3, api: 2, ui_framework: 2, generics: 2
- `source/multidimensional-array.d.ts` (TYPESCRIPT) | Magnitude: 1.67 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 11, generics: 8, ui_framework: 7, indent_tabs: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `source/json-value.d.ts` (TYPESCRIPT) | Magnitude: 1.76 | Delta: **0.081 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 9, api: 5, doc: 4, immutability_locks: 1
- `source/characters.d.ts` (TYPESCRIPT) | Magnitude: 1.76 | Delta: **0.093 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 9, api: 5, doc: 4
- `lint-processors/jsdoc-codeblocks.js` (JAVASCRIPT) | Magnitude: 64.38 | Delta: **0.106 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 67, branch: 29, immutability_locks: 21, doc: 18
- `lint-rules/require-exported-types.js` (JAVASCRIPT) | Magnitude: 52.54 | Delta: **0.158 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 98, branch: 24, immutability_locks: 18, structural_boundaries: 13
- `source/global-this.d.ts` (TYPESCRIPT) | Magnitude: 1.3 | Delta: **0.178 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 3, api: 2, doc: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `lint-rules/validate-jsdoc-codeblocks.js` -> **Som Shekhar Mukherjee** (100.0% isolated ownership) | Magnitude: 67.46
- `lint-processors/jsdoc-codeblocks.js` -> **Som Shekhar Mukherjee** (100.0% isolated ownership) | Magnitude: 64.38

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `index.d.ts` -> **Severity: 463.0** (Blast Radius: 4.63 * Doc Risk: 100.0%)
- `source/set-readonly.d.ts` -> **Severity: 463.0** (Blast Radius: 4.63 * Doc Risk: 100.0%)
- `lint-rules/require-export.js` -> **Severity: 423.224** (Blast Radius: 4.63 * Doc Risk: 91.409%)
- `source/typed-array.d.ts` -> **Severity: 366.939** (Blast Radius: 4.63 * Doc Risk: 79.2524%)
- `source/screaming-snake-case.d.ts` -> **Severity: 312.647** (Blast Radius: 4.63 * Doc Risk: 67.5264%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
