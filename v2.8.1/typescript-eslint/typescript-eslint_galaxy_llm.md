# ARCHITECTURAL_BRIEF: typescript-eslint
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/typescript-eslint/typescript-eslint.git` |
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
| Total Artifacts | 8445 |
| Analyzed Artifacts (Scanned) | 2886 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 5559 |
| Total LOC | 260790 |
| Volatility Index | 0.008 |
| % Scanned of codebase = | 34.2% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7715 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2573 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 8.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.3417 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 228 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 2603 | 256197 | 90.2% |
| JSON | 95 | 1790 | 3.3% |
| MARKDOWN | 51 | 0 | 1.8% |
| JAVASCRIPT | 43 | 980 | 1.5% |
| CSS | 36 | 1668 | 1.2% |
| PLAINTEXT | 31 | 1 | 1.1% |
| XML | 18 | 0 | 0.6% |
| HTML | 7 | 115 | 0.2% |
| YAML | 2 | 39 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Flat Modular Platform` (z -0.87; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 59%, Declarative / Non-Code 21%, Large Core Modules 4%, Compute Cores Files 4%, Interface Declarations Files 3%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 2804 | 97.2% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 81 | 2.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 5559*

**Composition by Extension & Reason:**
- `.shot`: 4641x Unsupported Format (.shot), 556x Excluded (Unsupported Extension: '.shot')
- `.mdx`: 191x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 31x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 6140 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 2227 LOC)
- `no_extension`: 29x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.ts`: 19x Excluded: Neighborhood Micro-Mass Limit Exceeded, 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1814 LOC)
- `.yml`: 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.snap`: 15x Excluded (Unsupported Extension: '.snap')
- `.png`: 11x Excluded (Explicitly Denied Extension: '.png')
- `.yaml`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 19945 LOC)
- `.jpg`: 8x Excluded (Explicitly Denied Extension: '.jpg')
- `.json`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mts`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json5`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mjs`: 1x Excluded (Machine-Generated Source Code Signature: 771 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 2.9 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.0 | 14.1 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 8.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 2.3 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 12.0 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 3.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 5.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.6 | 0.3 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 55.5 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 7.2 | 0.7 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 72.1 | 2.3 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 26.7 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 76.9 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 800 | 219 | 0 | `packages/eslint-plugin/tests/rules/consistent-type-assertions.test.ts` |
| cleanup | 40 | 11 | 0 | `packages/scope-manager/src/referencer/Referencer.ts` |
| guards | 8848 | 726 | 4 | `packages/eslint-plugin/tests/rules/member-ordering.test.ts` |
| danger | 2640 | 401 | 1 | `packages/eslint-plugin/tests/rules/no-explicit-any.test.ts` |
| concurrency | 4576 | 200 | 0 | `packages/eslint-plugin/tests/rules/no-floating-promises.test.ts` |
| connectivity | 5677 | 1327 | 4 | `packages/eslint-plugin/tests/rules/member-ordering.test.ts` |
| io | 945 | 153 | 0 | `packages/eslint-plugin/tests/rules/no-floating-promises.test.ts` |
| crypto | 0 | 0 | 0 | - |
| ipc | 15 | 4 | 0 | `packages/eslint-plugin/tests/rules/naming-convention/naming-convention.test.ts` |
| time | 140 | 21 | 0 | `packages/eslint-plugin/tests/rules/no-implied-eval.test.ts` |
| serialization | 65 | 38 | 0 | `packages/website/src/components/hooks/useHashState.ts` |
| regex | 230 | 76 | 0 | `packages/eslint-plugin/tests/rules/prefer-regexp-exec.test.ts` |
| events | 245 | 81 | 0 | `packages/typescript-estree/tests/lib/parse.test.ts` |
| tests | 4286 | 171 | 0 | `packages/scope-manager/tests/eslint-scope/es6-destructuring-assignments.test.ts` |
| docs | 4050 | 743 | 3 | `packages/eslint-plugin/tests/rules/no-deprecated.test.ts` |
| debt | 1223 | 514 | 1 | `packages/eslint-plugin/tests/rules/no-confusing-void-expression.test.ts` |
| mutation | 21140 | 1506 | 16 | `packages/eslint-plugin/tests/rules/member-ordering.test.ts` |
| dead_code | 621 | 396 | 1 | `packages/eslint-plugin/src/rules/consistent-type-imports.ts` |
| credential | 1 | 1 | 0 | `packages/website/docusaurus.config.mts` |
| threat | 148 | 55 | 0 | `packages/eslint-plugin/tests/rules/unbound-method.test.ts` |
| ml_ai | 312 | 38 | 0 | `packages/eslint-plugin/tests/rules/strict-boolean-expressions.test.ts` |
| ui | 903 | 128 | 0 | `packages/eslint-plugin/tests/rules/consistent-type-assertions.test.ts` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `packages/eslint-plugin/tests/rules/no-floating-promises.test.ts` (Hits: 49)
- `packages/integration-tests/tools/pack-packages.ts` (Hits: 39)
- `packages/typescript-estree/tests/lib/semanticInfo.test.ts` (Hits: 37)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **ast-node-types.ts** (`packages/ast-spec/src/ast-node-types.ts`) — 171 inbound connections
2. **BaseNode.ts** (`packages/ast-spec/src/base/BaseNode.ts`) — 155 inbound connections
3. **util.js** (`packages/website-eslint/src/mock/util.js`) — 147 inbound connections
4. **base-config.ts** (`packages/scope-manager/src/lib/base-config.ts`) — 87 inbound connections
5. **index.js** (`packages/website-eslint/src/index.js`) — 55 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **Node.ts** (`packages/ast-spec/src/unions/Node.ts`) — 168 outbound dependencies
2. **index.ts** (`packages/eslint-plugin/src/rules/index.ts`) — 135 outbound dependencies
3. **index.ts** (`packages/scope-manager/src/lib/index.ts`) — 120 outbound dependencies
4. **index.ts** (`packages/ast-spec/src/index.ts`) — 49 outbound dependencies
5. **spec.ts** (`packages/ast-spec/src/type/spec.ts`) — 45 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `nullishTypeTest` **(Compute Cores)** (@ `packages/eslint-plugin/tests/rules/prefer-nullish-coalescing.test.ts`) -> Impact: **2152.8** | LOC: 6315
- `unnecessaryConditionTest` **(Many-Argument Workhorses)** (@ `packages/eslint-plugin/tests/rules/no-unnecessary-condition.test.ts`) -> Impact: **1174.5** | LOC: 3813
- `convertNode` **(Many-Argument Workhorses)** (@ `packages/typescript-estree/src/convert.ts`) -> Impact: **464.3** | LOC: 1457
  * *Intent:* /** * Converts a TypeScript node into an ESTree node. * The core of the conversion logic: * Identify and convert each relevant TypeScript SyntaxKind *...
- `isValidEscape` **(Compute Cores)** (@ `packages/typescript-estree/src/convert.ts`) -> Impact: **418.9** | LOC: 1590
- `create` **(Many-Argument Workhorses)** (@ `packages/eslint-plugin/src/rules/no-unused-vars.ts`) -> Impact: **364.4** | LOC: 1052
- `checkSyntaxError` **(Many-Argument Workhorses)** (@ `packages/typescript-estree/src/check-syntax-errors.ts`) -> Impact: **358.9** | LOC: 618
- `create` **(Many-Argument Workhorses)** (@ `packages/eslint-plugin/src/rules/no-unnecessary-condition.ts`) -> Impact: **258.4** | LOC: 699
- `create` **(Many-Argument Workhorses)** (@ `packages/eslint-plugin/src/rules/no-misused-promises.ts`) -> Impact: **258.2** | LOC: 523
- `create` **(Many-Argument Workhorses)** (@ `packages/eslint-plugin/src/rules/consistent-type-imports.ts`) -> Impact: **250.6** | LOC: 855
- `create` **(Many-Argument Workhorses)** (@ `packages/eslint-plugin/src/rules/strict-boolean-expressions.ts`) -> Impact: **246.2** | LOC: 872

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `packages/eslint-plugin/tests/rules` | 130 | 599820.8 | 3.89% | 0.0% |
| `packages/eslint-plugin/src/rules` | 135 | 22170.77 | 11.12% | 1.91% |
| `packages/eslint-plugin/tests/rules/member-ordering` | 5 | 10067.07 | 6.12% | 0.0% |
| `packages/scope-manager/tests/eslint-scope` | 32 | 6923.37 | 2.03% | 0.0% |
| `packages/eslint-plugin/tests/rules/naming-convention` | 1 | 5822.93 | 7.25% | 0.0% |
| `__monolith__` | 18 | 5197.26 | 0.79% | 0.0% |
| `packages/type-utils/tests` | 12 | 3453.91 | 3.57% | 0.0% |
| `packages/typescript-estree/src` | 20 | 3048.04 | 9.25% | 7.24% |
| `packages/eslint-plugin/tests/rules/no-shadow` | 2 | 2148.21 | 2.74% | 0.0% |
| `packages/eslint-plugin/src/util` | 46 | 2026.78 | 7.04% | 0.67% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `packages/ast-spec/src/legacy-fixtures/basics/fixtures/class-with-optional-computed-method/fixture.ts` -> **100.0%** Exposure
- `packages/ast-spec/src/legacy-fixtures/types/fixtures/this-type-expanded/fixture.ts` -> **100.0%** Exposure
- `packages/ast-spec/src/legacy-fixtures/basics/fixtures/interface-with-all-property-types/fixture.ts` -> **99.9992%** Exposure
- `packages/eslint-plugin/typings/typescript.d.ts` -> **99.9992%** Exposure
- `packages/type-utils/typings/typescript.d.ts` -> **99.9992%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `packages/ast-spec/tests/util/serializers/Node.ts` -> **100.0%** Exposure
- `packages/eslint-plugin/src/util/baseTypeUtils.ts` -> **100.0%** Exposure
- `packages/eslint-plugin/src/util/class-scope-analyzer/classScopeAnalyzer.ts` -> **100.0%** Exposure
- `packages/eslint-plugin/src/util/collectUnusedVariables.ts` -> **100.0%** Exposure
- `packages/eslint-plugin/src/util/getFunctionHeadLoc.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/eslint-plugin/typings/eslint-rules.d.ts` -> **9** Orphaned Functions | **19** Duplicates
- `packages/scope-manager/tests/types/reference-type.test.ts` -> **2** Orphaned Functions | **11** Duplicates
- `packages/scope-manager/tests/test-utils/custom-matchers/vitest-custom-matchers.d.ts` -> **10** Orphaned Functions | **0** Duplicates
- `packages/type-utils/tests/test-utils/custom-matchers/vitest-custom-matchers.d.ts` -> **9** Orphaned Functions | **0** Duplicates
- `packages/scope-manager/tests/test-utils/custom-matchers/custom-matchers.ts` -> **8** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `packages/website/docusaurus.config.mts` -> **76.8824%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1859` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `packages/website/src/components/editor/createProvideTwoslashInlay.ts` (TYPESCRIPT) -> Cumulative Risk: **660.74**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.29)
- **Magnitude:** 65.7 | **LOC:** 94 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (98.9013%)
- **Heaviest Functions:** `createTwoslashInlayProvider` (Compute Cores, Impact: 16.6), `resolveInlayHint` (Compute Cores, Impact: 8.9), `provideInlayHints` (Generic / Templated Code, Impact: 6.4)

### 2. `packages/website-eslint/src/mock/path.js` (JAVASCRIPT) -> Cumulative Risk: **619.66**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z -0.46)
- **Magnitude:** 185.72 | **LOC:** 235 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (88.4794%)
- **Heaviest Functions:** `normalizeArray` (Defensive Guards, Impact: 16.8), `relative` (Defensive Guards, Impact: 16.0), `resolve` (Defensive Guards, Impact: 14.2)

### 3. `packages/website-eslint/src/index.js` (JAVASCRIPT) -> Cumulative Risk: **579.04**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z -0.46)
- **Magnitude:** 33.7 | **LOC:** 51 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Api Exposure (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `createLinter` (Callbacks & Closures, Impact: 1.1)

### 4. `packages/website/src/components/editor/loadSandbox.ts` (TYPESCRIPT) -> Cumulative Risk: **568.67**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z -0.06)
- **Magnitude:** 42.48 | **LOC:** 72 | **CtrlFlow:** 3.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `loadSandbox` (Callbacks & Closures, Impact: 5.1), `onload` (Callbacks & Closures, Impact: 4.2), `sandboxSingleton` (Callbacks & Closures, Impact: 3.1)

### 5. `packages/eslint-plugin/src/rules/naming-convention.ts` (TYPESCRIPT) -> Cumulative Risk: **568.16**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.67)
- **Magnitude:** 529.94 | **LOC:** 790 | **CtrlFlow:** 14.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.3458%), Concurrency (92.3153%)
- **Heaviest Functions:** `create` (Compute Cores, Impact: 136.3), `isExported` (Defensive Guards, Impact: 25.6), `getMemberModifiers` (Compute Cores, Impact: 21.6)

### 6. `packages/typescript-estree/src/create-program/getWatchProgramsForProjects.ts` (TYPESCRIPT) -> Cumulative Risk: **565.75**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.37)
- **Magnitude:** 221.22 | **LOC:** 494 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9674%), Safety Score (82.2268%), Verification (80.0%)
- **Heaviest Functions:** `maybeInvalidateProgram` (Many-Argument Workhorses, Impact: 36.5), `getWatchProgramsForProjects` (Compute Cores, Impact: 31.1), `createWatchProgram` (Compute Cores, Impact: 17.3)

### 7. `packages/website/src/hooks/useDebouncedToggle.ts` (TYPESCRIPT) -> Cumulative Risk: **565.22**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z -0.69)
- **Magnitude:** 22.16 | **LOC:** 27 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.6316%), Concurrency (98.7872%)
- **Heaviest Functions:** `useDebouncedToggle` (Callbacks & Closures, Impact: 4.7)

### 8. `packages/integration-tests/tools/integration-test-base.ts` (TYPESCRIPT) -> Cumulative Risk: **556.7**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.87)
- **Magnitude:** 0.08 | **LOC:** 129 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (91.4561%)
- **Heaviest Functions:** `eslintIntegrationTest` (Defensive Guards, Impact: 15.3), `typescriptIntegrationTest` (Many-Argument Workhorses, Impact: 10.7), `integrationTest` (Callbacks & Closures, Impact: 2.9)

### 9. `packages/scope-manager/src/scope/ScopeBase.ts` (TYPESCRIPT) -> Cumulative Risk: **552.84**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -1.56)
- **Magnitude:** 283.42 | **LOC:** 436 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9976%), Safety Score (86.3007%), Verification (80.0%)
- **Heaviest Functions:** `isStrictScope` (Many-Argument Workhorses, Impact: 61.8), `defineVariable` (Many-Argument Workhorses, Impact: 16.1), `constructor` (Many-Argument Workhorses, Impact: 11.4)

### 10. `packages/eslint-plugin/src/rules/prefer-optional-chain-utils/gatherLogicalOperands.ts` (TYPESCRIPT) -> Cumulative Risk: **550.92**
- **Archetype:** `file_cluster_4` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.15)
- **Magnitude:** 331.12 | **LOC:** 493 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.3235%), Verification (80.0%)
- **Heaviest Functions:** `gatherLogicalOperands` (Many-Argument Workhorses, Impact: 162.6), `isValidFalseBooleanCheckType` (Many-Argument Workhorses, Impact: 38.8), `getComparisonValueType` (Compute Cores, Impact: 12.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `packages/eslint-plugin/tests/rules/no-floating-promises.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 193447.7 | **LOC:** 5619 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (28.7933%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 1274
* *State Mutation (weighted view):* 5
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 650`, `structural_boundaries: 1755`, `args: 845`, `func_start: 249`, `class_start: 56`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 3`, `planned_debt: 1`
* *Architecture:* `io: 49`, `api: 2`, `concurrency: 1239`, `import: 4`
* *Defense:* `safety: 649`, `doc: 1`, `test: 139`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.218
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` no-floating-promises, RuleTester, node:path, node:test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/eslint-plugin/tests/rules/strict-boolean-expressions.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 127041.21 | **LOC:** 4769 | **CtrlFlow:** 15.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (4.295%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 700`, `structural_boundaries: 643`, `args: 315`, `func_start: 133`, `class_start: 36`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 5`, `dead_code: 1`, `planned_debt: 4`, `fragile_debt: 1`
* *Architecture:* `io: 4`, `concurrency: 3`, `import: 4`
* *Defense:* `safety: 119`, `doc: 1`, `test: 135`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.218
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` strict-boolean-expressions, RuleTester, rule-tester, node:path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/eslint-plugin/tests/rules/member-ordering.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 34961.2 | **LOC:** 5352 | **CtrlFlow:** 2.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (2.7343%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 257`, `args: 574`, `func_start: 569`, `class_start: 133`
* *Risk/State:* `safety_bypasses: 88`, `state_mutation: 14`, `dead_code: 2`
* *Architecture:* `api: 279`, `import: 4`
* *Defense:* `doc: 2`, `immutability_locks: 165`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.218
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` member-ordering, rule-tester
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/eslint-plugin/tests/rules/switch-exhaustiveness-check.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 33218.22 | **LOC:** 2986 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (5.3815%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 559`, `structural_boundaries: 407`, `args: 31`, `func_start: 31`, `class_start: 22`
* *Risk/State:* `state_mutation: 13`
* *Architecture:* `api: 10`, `import: 5`
* *Defense:* `doc: 1`, `test: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.218
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` switch-exhaustiveness-check, RuleTester, switch-exhaustiveness-check, rule-tester
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/eslint-plugin/tests/rules/no-misused-promises.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 21810.68 | **LOC:** 2664 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (17.8759%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 28 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 461
* *State Mutation (weighted view):* 25
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 973`, `args: 399`, `func_start: 225`, `class_start: 141`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 13`
* *Architecture:* `api: 7`, `concurrency: 321`, `import: 2`
* *Defense:* `safety: 13`, `doc: 2`, `test: 17`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.218
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` no-misused-promises, RuleTester
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/eslint-plugin/tests/rules/strict-void-return.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 15583.73 | **LOC:** 2795 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (4.47%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 12 instances
* *Concurrency (weighted view):* 88
* *State Mutation (weighted view):* 75
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 1188`, `args: 507`, `func_start: 255`, `class_start: 96`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 51`, `fragile_debt: 3`
* *Architecture:* `concurrency: 68`, `import: 3`
* *Defense:* `safety: 20`, `doc: 1`, `test: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.218
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` strict-void-return, RuleTester, rule-tester
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/eslint-plugin/tests/rules/explicit-module-boundary-types.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 11148.75 | **LOC:** 2199 | **CtrlFlow:** 2.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (2.9533%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 574`, `args: 306`, `func_start: 203`, `class_start: 37`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 18`
* *Architecture:* `api: 178`, `import: 2`
* *Defense:* `safety: 7`, `doc: 1`, `test: 29`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.218
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` explicit-module-boundary-types, rule-tester
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/eslint-plugin/tests/rules/no-confusing-void-expression.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 9412.24 | **LOC:** 1205 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (2.8853%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 299`, `args: 182`, `func_start: 102`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 21`
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* `safety: 4`, `doc: 1`, `test: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.218
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` no-confusing-void-expression, RuleTester, rule-tester
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/eslint-plugin/tests/rules/return-await.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 8043.38 | **LOC:** 1676 | **CtrlFlow:** 2.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (24.1373%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 371`, `args: 217`, `func_start: 205`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 15`
* *Architecture:* `io: 2`, `concurrency: 392`, `import: 4`
* *Defense:* `safety: 180`, `doc: 2`, `test: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.218
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` return-await, RuleTester, rule-tester
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/eslint-plugin/tests/rules/await-thenable.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 7071.87 | **LOC:** 1445 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (24.2761%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Concurrency (weighted view):* 318
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 306`, `args: 71`, `func_start: 67`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 2`
* *Architecture:* `io: 10`, `api: 4`, `concurrency: 298`, `import: 3`
* *Defense:* `safety: 25`, `doc: 1`, `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.218
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` await-thenable, RuleTester, rule-tester
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/eslint-plugin/tests/rules/no-loop-func.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 7033.45 | **LOC:** 844 | **CtrlFlow:** 9.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (12.2207%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 53 instances
* *State Mutation (weighted view):* 159
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 60`, `args: 75`, `func_start: 11`
* *Risk/State:* `state_mutation: 53`
* *Architecture:* `import: 2`
* *Defense:* `doc: 3`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.218
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` no-loop-func, rule-tester
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/eslint-plugin/tests/rules/unified-signatures.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 6850.55 | **LOC:** 1261 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.2621%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 274`, `args: 197`, `func_start: 198`, `class_start: 41`
* *Risk/State:* `safety_bypasses: 7`
* *Architecture:* `api: 19`, `concurrency: 11`, `import: 2`
* *Defense:* `doc: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.218
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` unified-signatures, rule-tester
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/eslint-plugin/tests/rules/prefer-readonly.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 6479.18 | **LOC:** 3493 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (3.188%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 109
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 401`, `args: 220`, `func_start: 200`, `class_start: 255`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 93`
* *Architecture:* `api: 132`, `concurrency: 2`, `import: 2`
* *Defense:* `safety: 24`, `test: 60`, `immutability_locks: 97`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.218
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` prefer-readonly, RuleTester
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/eslint-plugin/tests/rules/member-ordering/member-ordering-alphabetically-order.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 6473.52 | **LOC:** 2735 | **CtrlFlow:** 2.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.6051%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 272`, `args: 114`, `func_start: 114`, `class_start: 69`
* *Risk/State:* None
* *Architecture:* `api: 132`, `import: 4`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.218
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` member-ordering, rule-tester
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/eslint-plugin/tests/rules/no-useless-default-assignment.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 5969.26 | **LOC:** 836 | **CtrlFlow:** 7.8% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (9.034%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 30 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 101
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 114`, `args: 71`, `func_start: 59`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 41`
* *Architecture:* `io: 5`, `api: 5`, `concurrency: 2`, `import: 3`
* *Defense:* `safety: 1`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.218
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` no-useless-default-assignment, RuleTester, node:path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/eslint-plugin/tests/rules/naming-convention/naming-convention.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 5822.93 | **LOC:** 2401 | **CtrlFlow:** 2.1% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (7.2486%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 35
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 309`, `args: 96`, `func_start: 100`, `class_start: 76`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 19`
* *Architecture:* `io: 9`, `api: 54`, `concurrency: 32`, `import: 15`
* *Defense:* `safety: 6`, `doc: 3`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.218
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` naming-convention, RuleTester, rule-tester, ], child_process, code:, foo_bar, format: [...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/eslint-plugin/tests/rules/no-unnecessary-type-parameters.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 5525.55 | **LOC:** 1907 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (2.6742%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 638`, `args: 281`, `func_start: 203`, `class_start: 38`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 4`
* *Architecture:* `api: 1`, `concurrency: 12`, `import: 7`
* *Defense:* `safety: 10`, `doc: 4`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.218
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` no-unnecessary-type-parameters, RuleTester, rule-tester, types, typescript
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.218
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/eslint-plugin/tests/rules/no-unnecessary-boolean-literal-compare.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 4790.05 | **LOC:** 623 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (3.9082%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 114`, `args: 26`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 3`
* *Architecture:* `io: 4`, `import: 4`
* *Defense:* `safety: 11`, `doc: 1`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.218
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` no-unnecessary-boolean-literal-compare, RuleTester, rule-tester, node:path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/eslint-plugin/tests/rules/promise-function-async.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 4787.13 | **LOC:** 1015 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (18.5014%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 251`, `args: 142`, `func_start: 143`, `class_start: 38`
* *Risk/State:* `safety_bypasses: 6`
* *Architecture:* `api: 30`, `concurrency: 189`, `import: 3`
* *Defense:* `safety: 5`, `doc: 1`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.218
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` promise-function-async, RuleTester, rule-tester
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/eslint-plugin/tests/rules/explicit-member-accessibility.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 4538.38 | **LOC:** 2520 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (2.9482%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 370`, `args: 185`, `func_start: 192`, `class_start: 163`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 62`
* *Architecture:* `api: 108`, `import: 2`
* *Defense:* `doc: 1`, `immutability_locks: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.218
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` explicit-member-accessibility, rule-tester
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/eslint-plugin/tests/rules/no-invalid-void-type.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 4468.05 | **LOC:** 833 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.2138%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 246`, `args: 78`, `func_start: 70`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `api: 13`, `concurrency: 30`, `import: 2`
* *Defense:* `doc: 3`, `test: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.218
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` no-invalid-void-type, rule-tester
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/eslint-plugin/tests/rules/prefer-find.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 4286.61 | **LOC:** 724 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (2.9055%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 156`, `args: 82`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 2`
* *Architecture:* `import: 3`
* *Defense:* `safety: 23`, `doc: 3`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.218
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` prefer-find, RuleTester, rule-tester
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/eslint-plugin/tests/rules/use-unknown-in-catch-callback-variable.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 3902.81 | **LOC:** 854 | **CtrlFlow:** 3.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (7.9988%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 220`, `args: 112`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 19`
* *Architecture:* `concurrency: 81`, `import: 3`
* *Defense:* `safety: 78`, `doc: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.218
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` use-unknown-in-catch-callback-variable, RuleTester, rule-tester
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/eslint-plugin/tests/rules/no-deprecated.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3849.51 | **LOC:** 4053 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (1.2789%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Concurrency (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 423`, `args: 83`, `func_start: 69`, `class_start: 86`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 8`
* *Architecture:* `io: 6`, `api: 55`, `concurrency: 4`, `import: 63`
* *Defense:* `safety: 11`, `doc: 195`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.218
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` no-deprecated, RuleTester, deprecated, deprecated.js, deprecations, fs, node:assert, react...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/eslint-plugin/tests/rules/strict-boolean-expressions.test.ts` -> **Maria Solano** (100.0% isolated ownership) | Magnitude: 127041.21
- `packages/eslint-plugin/tests/rules/member-ordering.test.ts` -> **fisker Cheung** (100.0% isolated ownership) | Magnitude: 34961.2
- `packages/eslint-plugin/tests/rules/switch-exhaustiveness-check.test.ts` -> **Maria Solano** (100.0% isolated ownership) | Magnitude: 33218.22
- `packages/eslint-plugin/tests/rules/explicit-module-boundary-types.test.ts` -> **Dima Barabash** (100.0% isolated ownership) | Magnitude: 11148.75
- `packages/eslint-plugin/tests/rules/no-confusing-void-expression.test.ts` -> **Maria Solano** (100.0% isolated ownership) | Magnitude: 9412.24

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/website-eslint/src/index.js` -> **Severity: 0.03** (Bridge: 0.0003 * Flux: 100.0%)
- `packages/typescript-estree/src/ast-converter.ts` -> **Severity: 0.013** (Bridge: 0.0001 * Flux: 91.6827%)
- `packages/typescript-estree/src/convert.ts` -> **Severity: 0.004** (Bridge: 0.0001 * Flux: 70.2092%)
- `packages/eslint-plugin/src/raw-plugin.ts` -> **Severity: 0.002** (Bridge: 0.0002 * Flux: 11.9628%)
- `packages/rule-tester/src/RuleTester.ts` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 64.9481%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/website-eslint/src/mock/util.js` -> **Severity: 4.64** (Embedded: 0.0698 * Error Risk: 66.5013%)
- `packages/website-eslint/src/index.js` -> **Severity: 1.74** (Embedded: 0.0191 * Error Risk: 91.2821%)
- `packages/typescript-estree/src/version-check.ts` -> **Severity: 1.024** (Embedded: 0.0177 * Error Risk: 57.793%)
- `packages/typescript-estree/src/ast-converter.ts` -> **Severity: 1.004** (Embedded: 0.0157 * Error Risk: 63.7774%)
- `packages/typescript-estree/src/create-program/shared.ts` -> **Severity: 0.868** (Embedded: 0.0174 * Error Risk: 49.7343%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/website-eslint/src/mock/util.js` -> **Severity: 4567.5** (Blast Radius: 45.675 * Doc Risk: 100.0%)
- `packages/website-eslint/src/index.js` -> **Severity: 933.0** (Blast Radius: 9.33 * Doc Risk: 100.0%)
- `packages/typescript-estree/src/version-check.ts` -> **Severity: 475.3** (Blast Radius: 4.753 * Doc Risk: 100.0%)
- `packages/ast-spec/tests/util/parsers/typescript-estree.ts` -> **Severity: 462.8** (Blast Radius: 4.628 * Doc Risk: 100.0%)
- `packages/website/plugins/utils/nodes.ts` -> **Severity: 420.5** (Blast Radius: 4.205 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
