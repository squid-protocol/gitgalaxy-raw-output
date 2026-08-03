# ARCHITECTURAL_BRIEF: typescript-eslint
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_typescript/typescript-eslint` |
| **Timestamp** | `2026-08-03T19:59:52.375826+00:00` |
| **Scan Duration** | `7.14s` |
| **Git Branch** | `main` |
| **Git Commit** | `493341709fe7d1d6433332b7bd2724e3332c7cdf` |
| **Git Remote** | `https://github.com/typescript-eslint/typescript-eslint.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 2290 malicious artifacts.

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
| Total Artifacts | 8445 |
| Analyzed Artifacts (Scanned) | 2491 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 5954 |
| Total LOC | 70300 |
| Volatility Index | 0.009 |
| % Scanned of codebase = | 29.5% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.8113 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2773 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 6.1322 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 70 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 2248 | 66321 | 90.2% |
| JSON | 59 | 1213 | 2.4% |
| MARKDOWN | 49 | 0 | 2.0% |
| JAVASCRIPT | 42 | 939 | 1.7% |
| CSS | 36 | 1671 | 1.4% |
| PLAINTEXT | 31 | 1 | 1.2% |
| XML | 17 | 0 | 0.7% |
| HTML | 7 | 116 | 0.3% |
| YAML | 2 | 39 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.522`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 1556 | 62.5% |
| file_cluster_13 | 529 | 21.2% |
| file_cluster_16 | 170 | 6.8% |
| file_cluster_6 | 55 | 2.2% |
| file_cluster_0 | 36 | 1.4% |
| file_cluster_2 | 33 | 1.3% |
| file_cluster_4 | 10 | 0.4% |
| file_cluster_11 | 8 | 0.3% |
| file_cluster_17 | 8 | 0.3% |
| file_cluster_1 | 4 | 0.2% |
| file_cluster_7 | 2 | 0.1% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 79 | 3.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 5954*

**Composition by Extension & Reason:**
- `.shot`: 4641x Unsupported Format (.shot), 426x Excluded (Unsupported Extension: '.shot'), 130x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 334x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 19x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Machine-Generated Source Code Signature: 1814 LOC)
- `.mdx`: 191x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 43x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 34x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 6140 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 5587 LOC)
- `no_extension`: 29x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.mts`: 22x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.snap`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 11x Excluded (Explicitly Denied Extension: '.png')
- `.yaml`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 19945 LOC)
- `.jpg`: 8x Excluded (Explicitly Denied Extension: '.jpg')
- `.js`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cts`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json5`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 5.1 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 97.5 | 12.5 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 17.6 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 5.8 | 0.5 | 0.2 |
| API Exposure | 0.0 | 19.9 | 3.1 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 2.8 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 7.9 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 92.4 | 0.3 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 45.0 | 33.3 | 6.7 |
| Instability Exposure | 0.0 | 8.9 | 0.7 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 73.4 | 2.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 22.7 | 6.7 | 0.8 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 4.2 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 1.6 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 76.9 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `packages/integration-tests/tools/pack-packages.ts` (Hits: 27)
- `packages/website-eslint/src/mock/path.js` (Hits: 25)
- `packages/types/tools/copy-ast-spec.mts` (Hits: 14)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **ast-node-types.ts** (`packages/ast-spec/src/ast-node-types.ts`) — 170 inbound connections
2. **BaseNode.ts** (`packages/ast-spec/src/base/BaseNode.ts`) — 155 inbound connections
3. **util.js** (`packages/website-eslint/src/mock/util.js`) — 140 inbound connections
4. **base-config.ts** (`packages/scope-manager/src/lib/base-config.ts`) — 87 inbound connections
5. **Expression.ts** (`packages/ast-spec/src/unions/Expression.ts`) — 51 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **Node.ts** (`packages/ast-spec/src/unions/Node.ts`) — 168 outbound dependencies
2. **index.ts** (`packages/eslint-plugin/src/rules/index.ts`) — 135 outbound dependencies
3. **index.ts** (`packages/scope-manager/src/lib/index.ts`) — 120 outbound dependencies
4. **index.ts** (`packages/ast-spec/src/index.ts`) — 49 outbound dependencies
5. **spec.ts** (`packages/ast-spec/src/type/spec.ts`) — 45 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `convertNode` (@ `packages/typescript-estree/src/convert.ts`) -> Impact: **1214.4** | LOC: 1425
- `checkSyntaxError` (@ `packages/typescript-estree/src/check-syntax-errors.ts`) -> Impact: **1075.5** | LOC: 603
- `isJSDocComment` (@ `packages/typescript-estree/src/node-utils.ts`) -> Impact: **808.5** | LOC: 489
  * *Intent:* /** * Returns true if the given ts.Token is a comma */
- `create` (@ `packages/eslint-plugin/src/rules/no-shadow.ts`) -> Impact: **649.3** | LOC: 515
- `create` (@ `packages/eslint-plugin/src/rules/no-unused-vars.ts`) -> Impact: **625.7** | LOC: 736
- `checkNode` (@ `packages/eslint-plugin/src/rules/no-unnecessary-condition.ts`) -> Impact: **595.1** | LOC: 274
  * *Intent:* /**
- `create` (@ `packages/eslint-plugin/src/rules/no-deprecated.ts`) -> Impact: **539.9** | LOC: 406
- `PrivateIdentifier` (@ `packages/eslint-plugin/src/util/class-scope-analyzer/classScopeAnalyzer.ts`) -> Impact: **518.8** | LOC: 175
- `constructor` (@ `packages/rule-tester/src/RuleTester.ts`) -> Impact: **484.9** | LOC: 345
- `createLinter` (@ `packages/website/src/components/linter/createLinter.ts`) -> Impact: **460.6** | LOC: 217

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `generateFixToRemoveArrayElementAccess` (@ `packages/eslint-plugin/src/rules/prefer-find.ts`) -> **O(2^N) [Recursive]**
- `ObjectExpression` (@ `packages/eslint-plugin-internal/src/rules/plugin-test-formatting.ts`) -> **O(2^N) [Recursive]**
- `TSUnionType` (@ `packages/eslint-plugin/src/rules/no-duplicate-type-constituents.ts`) -> **O(2^N) [Recursive]**
- `noEmptyMessage` (@ `packages/eslint-plugin/src/rules/no-empty-object-type.ts`) -> **O(2^N) [Recursive]**
- `node` (@ `packages/eslint-plugin/src/rules/prefer-readonly.ts`) -> **O(2^N) [Recursive]**
- `constructor` (@ `packages/rule-tester/src/RuleTester.ts`) -> **O(2^N) [Recursive]**
- `toText` (@ `packages/eslint-plugin/src/rules/ban-tslint-comment.ts`) -> **O(2^N) [Recursive]**
- `create` (@ `packages/eslint-plugin/src/rules/dot-notation.ts`) -> **O(2^N) [Recursive]**
- `TSVoidKeyword` (@ `packages/eslint-plugin/src/rules/no-invalid-void-type.ts`) -> **O(2^N) [Recursive]**
- `create` (@ `packages/eslint-plugin/src/rules/no-restricted-imports.ts`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `convertNode` (@ `packages/typescript-estree/src/convert.ts`) -> DB Complexity: **328**
- `setup` (@ `packages/integration-tests/tools/pack-packages.ts`) -> DB Complexity: **44**
- `staticCloseRef` (@ `packages/scope-manager/src/scope/ScopeBase.ts`) -> DB Complexity: **34**
  * *Intent:* /** * List of {@link Reference}s that are left to be resolved (i.e. which
- `createFileSystem` (@ `packages/website/src/components/linter/bridge.ts`) -> DB Complexity: **31**
- `normalize` (@ `packages/website-eslint/src/mock/path.js`) -> DB Complexity: **30**
  * *Intent:* // path.normalize(path) // posix version
- `create` (@ `packages/eslint-plugin/src/rules/naming-convention.ts`) -> DB Complexity: **29**
- `useSandboxServices` (@ `packages/website/src/components/editor/useSandboxServices.ts`) -> DB Complexity: **29**
- `create` (@ `packages/eslint-plugin-internal/src/rules/no-relative-paths-to-internal-packages.ts`) -> DB Complexity: **24**
- `resolve` (@ `packages/website-eslint/src/mock/path.js`) -> DB Complexity: **21**
  * *Intent:* // path.resolve([from ...], to) // posix version
- `getWatchProgramsForProjects` (@ `packages/typescript-estree/src/create-program/getWatchProgramsForProjects.ts`) -> DB Complexity: **20**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 14 | 5117.36 | 3.06% | 0.0% |
| `packages/eslint-plugin/src/rules` | 135 | 2103.65 | 9.44% | 4.76% |
| `packages/typescript-estree/src` | 20 | 555.37 | 13.92% | 3.35% |
| `packages/website-eslint/src/mock` | 9 | 374.86 | 18.5% | 12.61% |
| `packages/eslint-plugin/src/util` | 46 | 281.11 | 7.62% | 5.76% |
| `packages/scope-manager/src/referencer` | 10 | 193.21 | 31.72% | 5.19% |
| `packages/scope-manager/src/lib` | 120 | 187.75 | 4.78% | 0.0% |
| `packages/eslint-plugin-internal/src/rules` | 12 | 133.34 | 7.91% | 0.0% |
| `packages/website/static/img` | 11 | 115.72 | 5.0% | 0.0% |
| `packages/website/blog` | 15 | 94.56 | 0.33% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `packages/ast-spec/src/declaration/ClassDeclaration/fixtures/_error_/abstract-constructor/fixture.ts` -> **100.0%** Exposure
- `packages/ast-spec/src/declaration/ClassDeclaration/fixtures/_error_/abstract-getter-with-implementation/fixture.ts` -> **100.0%** Exposure
- `packages/ast-spec/src/declaration/ClassDeclaration/fixtures/_error_/abstract-method-with-implementation/fixture.ts` -> **100.0%** Exposure
- `packages/ast-spec/src/declaration/ClassDeclaration/fixtures/_error_/abstract-setter-with-implementation/fixture.ts` -> **100.0%** Exposure
- `packages/ast-spec/src/declaration/ExportNamedDeclaration/fixtures/_error_/arrow-function/fixture.ts` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `packages/ast-spec/src/declaration/VariableDeclaration/fixtures/_error_/declare-let-destructure-init/fixture.ts` -> **100.0%** Exposure
- `packages/ast-spec/src/declaration/VariableDeclaration/fixtures/_error_/declare-let-destructure-type-init/fixture.ts` -> **100.0%** Exposure
- `packages/ast-spec/src/declaration/VariableDeclaration/fixtures/_error_/declare-let-id-definite-init/fixture.ts` -> **100.0%** Exposure
- `packages/ast-spec/src/declaration/VariableDeclaration/fixtures/_error_/declare-let-id-definite-no-init/fixture.ts` -> **100.0%** Exposure
- `packages/ast-spec/src/declaration/VariableDeclaration/fixtures/_error_/declare-let-id-definite-type-init/fixture.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/website/src/components/editor/LoadedEditor.tsx` -> **0** Orphaned Functions | **20** Duplicates
- `packages/rule-tester/src/TestFramework.ts` -> **0** Orphaned Functions | **12** Duplicates
- `packages/eslint-plugin/src/rules/class-methods-use-this.ts` -> **0** Orphaned Functions | **6** Duplicates
- `packages/ast-spec/src/legacy-fixtures/types/fixtures/this-type-expanded/fixture.ts` -> **5** Orphaned Functions | **0** Duplicates
- `packages/eslint-plugin/src/rules/parameter-properties.ts` -> **0** Orphaned Functions | **4** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`packages/eslint-plugin/src/rules/prefer-optional-chain-utils/analyzeChain.ts`** -> AI Confidence: **99.31%**
2. **`packages/scope-manager/src/referencer/Referencer.ts`** -> AI Confidence: **99.31%**
3. **`packages/typescript-estree/src/convert.ts`** -> AI Confidence: **99.31%**
4. **`packages/typescript-estree/src/create-program/getWatchProgramsForProjects.ts`** -> AI Confidence: **99.31%**
5. **`packages/typescript-estree/src/parseSettings/createParseSettings.ts`** -> AI Confidence: **99.31%**
6. **`packages/typescript-estree/src/useProgramFromProjectService.ts`** -> AI Confidence: **99.31%**
7. **`packages/website/src/components/hooks/useHashState.ts`** -> AI Confidence: **99.31%**
8. **`packages/ast-spec/src/expression/TaggedTemplateExpression/fixtures/_error_/optional-nested-function-tag/fixture.ts`** -> AI Confidence: **99.29%**
9. **`packages/ast-spec/src/expression/TaggedTemplateExpression/fixtures/_error_/optional-nested-tag/fixture.ts`** -> AI Confidence: **99.29%**
10. **`packages/ast-spec/src/expression/TaggedTemplateExpression/fixtures/_error_/optional-tag/fixture.ts`** -> AI Confidence: **99.29%**
11. **`packages/ast-spec/src/expression/UpdateExpression/fixtures/_error_/optional-chain/fixture.ts`** -> AI Confidence: **99.29%**
12. **`packages/ast-spec/src/expression/UpdateExpression/fixtures/_error_/optional-chain2/fixture.ts`** -> AI Confidence: **99.29%**
13. **`packages/ast-spec/src/expression/UpdateExpression/fixtures/_error_/optional-chain3/fixture.ts`** -> AI Confidence: **99.29%**
14. **`packages/ast-spec/src/legacy-fixtures/basics/fixtures/catch-clause-with-annotation/fixture.ts`** -> AI Confidence: **99.29%**
15. **`packages/ast-spec/src/legacy-fixtures/basics/fixtures/catch-clause-with-invalid-annotation/fixture.ts`** -> AI Confidence: **99.29%**
16. **`packages/ast-spec/src/legacy-fixtures/basics/fixtures/class-with-optional-computed-method/fixture.ts`** -> AI Confidence: **99.29%**
17. **`packages/ast-spec/src/legacy-fixtures/basics/fixtures/class-with-optional-properties/fixture.ts`** -> AI Confidence: **99.29%**
18. **`packages/ast-spec/src/legacy-fixtures/basics/fixtures/function-with-object-type-with-optional-properties/fixture.ts`** -> AI Confidence: **99.29%**
19. **`packages/ast-spec/src/legacy-fixtures/basics/fixtures/interface-with-all-property-types/fixture.ts`** -> AI Confidence: **99.29%**
20. **`packages/ast-spec/src/legacy-fixtures/basics/fixtures/interface-with-optional-properties/fixture.ts`** -> AI Confidence: **99.29%**
21. **`packages/ast-spec/src/legacy-fixtures/basics/fixtures/non-null-assertion-operator/fixture.ts`** -> AI Confidence: **99.29%**
22. **`packages/ast-spec/src/legacy-fixtures/basics/fixtures/nullish-coalescing/fixture.ts`** -> AI Confidence: **99.29%**
23. **`packages/ast-spec/src/legacy-fixtures/basics/fixtures/optional-chain-call-with-non-null-assertion/fixture.ts`** -> AI Confidence: **99.29%**
24. **`packages/ast-spec/src/legacy-fixtures/basics/fixtures/optional-chain-call-with-parens/fixture.ts`** -> AI Confidence: **99.29%**
25. **`packages/ast-spec/src/legacy-fixtures/basics/fixtures/optional-chain-call/fixture.ts`** -> AI Confidence: **99.29%**
26. **`packages/ast-spec/src/legacy-fixtures/basics/fixtures/optional-chain-element-access-with-non-null-assertion/fixture.ts`** -> AI Confidence: **99.29%**
27. **`packages/ast-spec/src/legacy-fixtures/basics/fixtures/optional-chain-element-access-with-parens/fixture.ts`** -> AI Confidence: **99.29%**
28. **`packages/ast-spec/src/legacy-fixtures/basics/fixtures/optional-chain-element-access/fixture.ts`** -> AI Confidence: **99.29%**
29. **`packages/ast-spec/src/legacy-fixtures/basics/fixtures/optional-chain-with-non-null-assertion/fixture.ts`** -> AI Confidence: **99.29%**
30. **`packages/ast-spec/src/legacy-fixtures/basics/fixtures/optional-chain-with-parens/fixture.ts`** -> AI Confidence: **99.29%**
31. **`packages/ast-spec/src/legacy-fixtures/basics/fixtures/optional-chain/fixture.ts`** -> AI Confidence: **99.29%**
32. **`packages/ast-spec/src/legacy-fixtures/basics/fixtures/short-circuiting-assignment-and-and/fixture.ts`** -> AI Confidence: **99.29%**
33. **`packages/ast-spec/src/legacy-fixtures/basics/fixtures/short-circuiting-assignment-or-or/fixture.ts`** -> AI Confidence: **99.29%**
34. **`packages/ast-spec/src/legacy-fixtures/basics/fixtures/short-circuiting-assignment-question-question/fixture.ts`** -> AI Confidence: **99.29%**
35. **`packages/ast-spec/src/legacy-fixtures/errorRecovery/fixtures/_error_/object-optional-not-allowed/fixture.ts`** -> AI Confidence: **99.29%**
36. **`packages/ast-spec/src/legacy-fixtures/expressions/fixtures/_error_/instantiation-expression/fixture.ts`** -> AI Confidence: **99.29%**
37. **`packages/ast-spec/src/legacy-fixtures/expressions/fixtures/optional-call-expression-type-arguments/fixture.ts`** -> AI Confidence: **99.29%**
38. **`packages/ast-spec/src/legacy-fixtures/types/fixtures/mapped-readonly-minus/fixture.ts`** -> AI Confidence: **99.29%**
39. **`packages/ast-spec/src/legacy-fixtures/types/fixtures/mapped-readonly-plus/fixture.ts`** -> AI Confidence: **99.29%**
40. **`packages/ast-spec/src/legacy-fixtures/types/fixtures/mapped-readonly/fixture.ts`** -> AI Confidence: **99.29%**
41. **`packages/ast-spec/src/legacy-fixtures/types/fixtures/tuple-named-optional/fixture.ts`** -> AI Confidence: **99.29%**
42. **`packages/ast-spec/src/legacy-fixtures/types/fixtures/tuple-optional/fixture.ts`** -> AI Confidence: **99.29%**
43. **`packages/ast-spec/src/special/CatchClause/fixtures/_error_/with-initializer/fixture.ts`** -> AI Confidence: **99.29%**
44. **`packages/ast-spec/src/statement/ForInStatement/fixtures/expr-init/fixture.ts`** -> AI Confidence: **99.29%**
45. **`packages/ast-spec/src/statement/ForOfStatement/fixtures/_error_/decl-definite/fixture.ts`** -> AI Confidence: **99.29%**
46. **`packages/ast-spec/src/statement/ForOfStatement/fixtures/_error_/decl-init/fixture.ts`** -> AI Confidence: **99.29%**
47. **`packages/ast-spec/src/statement/ForOfStatement/fixtures/_error_/decl-multi/fixture.ts`** -> AI Confidence: **99.29%**
48. **`packages/ast-spec/src/statement/ForOfStatement/fixtures/_error_/decl-type/fixture.ts`** -> AI Confidence: **99.29%**
49. **`packages/ast-spec/src/statement/ForOfStatement/fixtures/_error_/expr-not-assignment-target/fixture.ts`** -> AI Confidence: **99.29%**
50. **`packages/ast-spec/src/statement/ForOfStatement/fixtures/expr-init/fixture.ts`** -> AI Confidence: **99.29%**
51. **`packages/ast-spec/src/statement/SwitchStatement/fixtures/_error_/multiple-default-cases/fixture.ts`** -> AI Confidence: **99.29%**
52. **`packages/eslint-plugin/src/util/walkStatements.ts`** -> AI Confidence: **99.29%**
53. **`packages/parser/tests/fixtures/scope-analysis/function-overload.ts`** -> AI Confidence: **99.29%**
54. **`packages/rule-tester/src/utils/freezeDeeply.ts`** -> AI Confidence: **99.29%**
55. **`packages/scope-manager/tests/fixtures/catch/destructuring-array.ts`** -> AI Confidence: **99.29%**
56. **`packages/scope-manager/tests/fixtures/catch/destructuring-object.ts`** -> AI Confidence: **99.29%**
57. **`packages/scope-manager/tests/fixtures/catch/inherited-scope.ts`** -> AI Confidence: **99.29%**
58. **`packages/scope-manager/tests/fixtures/catch/scope.ts`** -> AI Confidence: **99.29%**
59. **`packages/scope-manager/tests/fixtures/member-expression/member-expression.ts`** -> AI Confidence: **99.29%**
60. **`packages/typescript-estree/src/check-syntax-errors.ts`** -> AI Confidence: **99.29%**
61. **`packages/ast-spec/src/declaration/VariableDeclaration/fixtures/generate-fixtures.mjs`** -> AI Confidence: **99.29%**
62. **`packages/parser/tests/fixtures/basics/do-while-statements.src.js`** -> AI Confidence: **99.29%**
63. **`packages/website/src/prism/language/jsonc.js`** -> AI Confidence: **99.29%**
64. **`packages/eslint-plugin/src/rules/consistent-type-imports.ts`** -> AI Confidence: **99.24%**
65. **`packages/eslint-plugin/src/rules/triple-slash-reference.ts`** -> AI Confidence: **99.24%**
66. **`packages/scope-manager/src/scope/ScopeBase.ts`** -> AI Confidence: **99.24%**
67. **`packages/website/src/components/Playground.tsx`** -> AI Confidence: **99.24%**
68. **`packages/website/src/components/ast/DataRenderer.tsx`** -> AI Confidence: **99.24%**
69. **`packages/website/src/components/linter/createLinter.ts`** -> AI Confidence: **99.24%**
70. **`packages/website/src/theme/CodeBlock/Content/String.tsx`** -> AI Confidence: **99.24%**
71. **`packages/eslint-plugin/src/rules/naming-convention.ts`** -> AI Confidence: **99.23%**
72. **`packages/website/src/components/ast/ASTViewer.tsx`** -> AI Confidence: **99.23%**
73. **`packages/eslint-plugin/src/util/getOperatorPrecedence.ts`** -> AI Confidence: **99.2%**
74. **`packages/integration-tests/tools/pack-packages.ts`** -> AI Confidence: **99.18%**
75. **`packages/rule-schema-to-typescript-types/src/generateType.ts`** -> AI Confidence: **99.18%**
76. **`packages/scope-manager/src/scope/GlobalScope.ts`** -> AI Confidence: **99.18%**
77. **`packages/type-utils/src/TypeOrValueSpecifier.ts`** -> AI Confidence: **99.18%**
78. **`packages/website/docusaurus.config.mts`** -> AI Confidence: **99.18%**
79. **`packages/website/src/components/ErrorsViewer.tsx`** -> AI Confidence: **99.18%**
80. **`packages/website/src/components/editor/LoadedEditor.tsx`** -> AI Confidence: **99.18%**
81. **`packages/website/src/components/inputs/CopyButton.tsx`** -> AI Confidence: **99.18%**
82. **`packages/website/src/components/typeDetails/TypesDetails.tsx`** -> AI Confidence: **99.18%**
83. **`packages/website/src/theme/BlogPostItem/Header/Title/index.tsx`** -> AI Confidence: **99.18%**
84. **`packages/website/src/theme/MDXComponents/RuleAttributes.tsx`** -> AI Confidence: **99.18%**
85. **`knip.ts`** -> AI Confidence: **99.17%**
86. **`packages/ast-spec/src/legacy-fixtures/basics/fixtures/class-with-optional-methods/fixture.ts`** -> AI Confidence: **99.17%**
87. **`packages/ast-spec/src/legacy-fixtures/basics/fixtures/class-with-private-optional-property/fixture.ts`** -> AI Confidence: **99.17%**
88. **`packages/ast-spec/src/legacy-fixtures/types/fixtures/nested-types/fixture.ts`** -> AI Confidence: **99.17%**
89. **`packages/parser/tests/fixtures/scope-analysis/types-nested-types.src.ts`** -> AI Confidence: **99.17%**
90. **`packages/typescript-estree/src/check-modifiers.ts`** -> AI Confidence: **99.17%**
91. **`packages/typescript-estree/src/semantic-or-syntactic-errors.ts`** -> AI Confidence: **99.17%**
92. **`packages/website-eslint/src/mock/assert.js`** -> AI Confidence: **99.17%**
93. **`packages/eslint-plugin/src/rules/prefer-optional-chain.ts`** -> AI Confidence: **99.16%**
94. **`packages/rule-tester/src/RuleTester.ts`** -> AI Confidence: **99.16%**
95. **`packages/typescript-estree/src/ast-converter.ts`** -> AI Confidence: **99.16%**
96. **`packages/website/src/components/RulesTable/index.tsx`** -> AI Confidence: **99.16%**
97. **`packages/eslint-plugin/src/rules/naming-convention-utils/validator.ts`** -> AI Confidence: **99.15%**
98. **`packages/website/src/components/home/Explainers/index.tsx`** -> AI Confidence: **99.15%**
99. **`tools/scripts/generate-configs.mts`** -> AI Confidence: **99.15%**
100. **`packages/eslint-plugin-internal/src/rules/plugin-test-formatting.ts`** -> AI Confidence: **99.13%**
101. **`packages/eslint-plugin/src/rules/naming-convention-utils/parse-options.ts`** -> AI Confidence: **99.13%**
102. **`packages/eslint-plugin/src/rules/no-deprecated.ts`** -> AI Confidence: **99.13%**
103. **`packages/eslint-plugin/src/rules/no-misused-promises.ts`** -> AI Confidence: **99.13%**
104. **`packages/eslint-plugin/src/rules/no-mixed-enums.ts`** -> AI Confidence: **99.13%**
105. **`packages/eslint-plugin/src/rules/no-unnecessary-condition.ts`** -> AI Confidence: **99.13%**
106. **`packages/eslint-plugin/src/rules/no-unnecessary-type-parameters.ts`** -> AI Confidence: **99.13%**
107. **`packages/eslint-plugin/src/rules/no-unused-vars.ts`** -> AI Confidence: **99.13%**
108. **`packages/eslint-plugin/src/rules/prefer-nullish-coalescing.ts`** -> AI Confidence: **99.13%**
109. **`packages/eslint-plugin/src/rules/prefer-optional-chain-utils/gatherLogicalOperands.ts`** -> AI Confidence: **99.13%**
110. **`packages/eslint-plugin/src/rules/prefer-readonly.ts`** -> AI Confidence: **99.13%**
111. **`packages/eslint-plugin/src/util/astUtils.ts`** -> AI Confidence: **99.13%**
112. **`packages/eslint-plugin/src/util/class-scope-analyzer/classScopeAnalyzer.ts`** -> AI Confidence: **99.13%**
113. **`packages/parser/src/parser.ts`** -> AI Confidence: **99.13%**
114. **`packages/typescript-estree/src/create-program/createProjectProgramError.ts`** -> AI Confidence: **99.13%**
115. **`packages/typescript-estree/src/parseSettings/getProjectConfigFiles.ts`** -> AI Confidence: **99.13%**
116. **`packages/typescript-estree/src/parseSettings/resolveProjectList.ts`** -> AI Confidence: **99.13%**
117. **`packages/scope-manager/src/analyze.ts`** -> AI Confidence: **99.11%**
118. **`packages/ast-spec/src/declaration/spec.ts`** -> AI Confidence: **99.09%**
119. **`packages/ast-spec/src/element/spec.ts`** -> AI Confidence: **99.09%**
120. **`packages/ast-spec/src/expression/spec.ts`** -> AI Confidence: **99.09%**
121. **`packages/ast-spec/src/index.ts`** -> AI Confidence: **99.09%**
122. **`packages/ast-spec/src/jsx/spec.ts`** -> AI Confidence: **99.09%**
123. **`packages/ast-spec/src/special/spec.ts`** -> AI Confidence: **99.09%**
124. **`packages/ast-spec/src/statement/spec.ts`** -> AI Confidence: **99.09%**
125. **`packages/ast-spec/src/token/spec.ts`** -> AI Confidence: **99.09%**
126. **`packages/ast-spec/src/type/spec.ts`** -> AI Confidence: **99.09%**
127. **`packages/ast-spec/src/unions/DeclarationStatement.ts`** -> AI Confidence: **99.09%**
128. **`packages/ast-spec/src/unions/ExportDeclaration.ts`** -> AI Confidence: **99.09%**
129. **`packages/ast-spec/src/unions/Expression.ts`** -> AI Confidence: **99.09%**
130. **`packages/ast-spec/src/unions/LeftHandSideExpression.ts`** -> AI Confidence: **99.09%**
131. **`packages/ast-spec/src/unions/Node.ts`** -> AI Confidence: **99.09%**
132. **`packages/ast-spec/src/unions/PrimaryExpression.ts`** -> AI Confidence: **99.09%**
133. **`packages/ast-spec/src/unions/Statement.ts`** -> AI Confidence: **99.09%**
134. **`packages/ast-spec/src/unions/Token.ts`** -> AI Confidence: **99.09%**
135. **`packages/ast-spec/src/unions/TypeNode.ts`** -> AI Confidence: **99.09%**
136. **`packages/eslint-plugin-internal/src/rules/no-multiple-lines-of-errors.ts`** -> AI Confidence: **99.09%**
137. **`packages/eslint-plugin/src/raw-plugin.ts`** -> AI Confidence: **99.09%**
138. **`packages/eslint-plugin/src/rules/index.ts`** -> AI Confidence: **99.09%**
139. **`packages/eslint-plugin/src/rules/no-loop-func.ts`** -> AI Confidence: **99.09%**
140. **`packages/eslint-plugin/src/rules/prefer-string-starts-ends-with.ts`** -> AI Confidence: **99.09%**
141. **`packages/eslint-plugin/src/rules/return-await.ts`** -> AI Confidence: **99.09%**
142. **`packages/eslint-plugin/src/rules/sort-type-constituents.ts`** -> AI Confidence: **99.09%**
143. **`packages/eslint-plugin/src/util/getESLintCoreRule.ts`** -> AI Confidence: **99.09%**
144. **`packages/eslint-plugin/src/util/index.ts`** -> AI Confidence: **99.09%**
145. **`packages/eslint-plugin/typings/eslint-rules.d.ts`** -> AI Confidence: **99.09%**
146. **`packages/rule-tester/src/utils/config-validator.ts`** -> AI Confidence: **99.09%**
147. **`packages/scope-manager/src/definition/Definition.ts`** -> AI Confidence: **99.09%**
148. **`packages/scope-manager/src/definition/index.ts`** -> AI Confidence: **99.09%**
149. **`packages/scope-manager/src/lib/es2015.ts`** -> AI Confidence: **99.09%**
150. **`packages/scope-manager/src/lib/es2020.ts`** -> AI Confidence: **99.09%**
151. **`packages/scope-manager/src/lib/es6.ts`** -> AI Confidence: **99.09%**
152. **`packages/scope-manager/src/lib/esnext.ts`** -> AI Confidence: **99.09%**
153. **`packages/scope-manager/src/lib/index.ts`** -> AI Confidence: **99.09%**
154. **`packages/scope-manager/src/scope/Scope.ts`** -> AI Confidence: **99.09%**
155. **`packages/scope-manager/src/scope/index.ts`** -> AI Confidence: **99.09%**
156. **`packages/scope-manager/src/variable/ImplicitLibVariable.ts`** -> AI Confidence: **99.09%**
157. **`packages/type-utils/src/index.ts`** -> AI Confidence: **99.09%**
158. **`packages/typescript-estree/src/index.ts`** -> AI Confidence: **99.09%**
159. **`packages/utils/src/ts-eslint/index.ts`** -> AI Confidence: **99.09%**
160. **`packages/website/src/components/inputs/Tooltip.tsx`** -> AI Confidence: **99.09%**
161. **`packages/website/src/components/linter/utils.ts`** -> AI Confidence: **99.09%**
162. **`packages/website/src/pages/index.tsx`** -> AI Confidence: **99.09%**
163. **`packages/ast-spec/src/base/ClassBase.ts`** -> AI Confidence: **99.08%**
164. **`packages/ast-spec/src/base/FunctionBase.ts`** -> AI Confidence: **99.08%**
165. **`packages/ast-spec/src/declaration/ExportAllDeclaration/spec.ts`** -> AI Confidence: **99.08%**
166. **`packages/ast-spec/src/declaration/ExportNamedDeclaration/spec.ts`** -> AI Confidence: **99.08%**
167. **`packages/ast-spec/src/declaration/ImportDeclaration/spec.ts`** -> AI Confidence: **99.08%**
168. **`packages/ast-spec/src/declaration/TSImportEqualsDeclaration/spec.ts`** -> AI Confidence: **99.08%**
169. **`packages/ast-spec/src/declaration/TSModuleDeclaration/spec.ts`** -> AI Confidence: **99.08%**
170. **`packages/ast-spec/src/element/Property/spec.ts`** -> AI Confidence: **99.08%**
171. **`packages/ast-spec/src/element/TSMethodSignature/spec.ts`** -> AI Confidence: **99.08%**
172. **`packages/ast-spec/src/expression/ArrowFunctionExpression/spec.ts`** -> AI Confidence: **99.08%**
173. **`packages/ast-spec/src/jsx/JSXAttribute/spec.ts`** -> AI Confidence: **99.08%**
174. **`packages/ast-spec/src/type/TSImportType/spec.ts`** -> AI Confidence: **99.08%**
175. **`packages/ast-spec/src/unions/ClassElement.ts`** -> AI Confidence: **99.08%**
176. **`packages/eslint-plugin-internal/src/rules/index.ts`** -> AI Confidence: **99.08%**
177. **`packages/eslint-plugin/src/rules/consistent-type-exports.ts`** -> AI Confidence: **99.08%**
178. **`packages/scope-manager/src/index.ts`** -> AI Confidence: **99.08%**
179. **`packages/scope-manager/src/lib/es2017.ts`** -> AI Confidence: **99.08%**
180. **`packages/scope-manager/src/lib/es2018.full.ts`** -> AI Confidence: **99.08%**
181. **`packages/scope-manager/src/lib/es2018.ts`** -> AI Confidence: **99.08%**
182. **`packages/scope-manager/src/lib/es2019.full.ts`** -> AI Confidence: **99.08%**
183. **`packages/scope-manager/src/lib/es2019.ts`** -> AI Confidence: **99.08%**
184. **`packages/scope-manager/src/lib/es2020.full.ts`** -> AI Confidence: **99.08%**
185. **`packages/scope-manager/src/lib/es2021.full.ts`** -> AI Confidence: **99.08%**
186. **`packages/scope-manager/src/lib/es2022.full.ts`** -> AI Confidence: **99.08%**
187. **`packages/scope-manager/src/lib/es2022.ts`** -> AI Confidence: **99.08%**
188. **`packages/scope-manager/src/lib/es2023.full.ts`** -> AI Confidence: **99.08%**
189. **`packages/scope-manager/src/lib/es2024.full.ts`** -> AI Confidence: **99.08%**
190. **`packages/scope-manager/src/lib/es2024.ts`** -> AI Confidence: **99.08%**
191. **`packages/scope-manager/src/lib/es2025.full.ts`** -> AI Confidence: **99.08%**
192. **`packages/scope-manager/src/lib/es2025.ts`** -> AI Confidence: **99.08%**
193. **`packages/scope-manager/src/lib/esnext.full.ts`** -> AI Confidence: **99.08%**
194. **`packages/typescript-eslint/src/index.ts`** -> AI Confidence: **99.08%**
195. **`packages/utils/src/ts-eslint/Rule.ts`** -> AI Confidence: **99.08%**
196. **`packages/website/src/components/OptionsSelector.tsx`** -> AI Confidence: **99.08%**
197. **`packages/website/src/components/editor/useSandboxServices.ts`** -> AI Confidence: **99.08%**
198. **`packages/website/src/components/home/FinancialContributors/index.tsx`** -> AI Confidence: **99.08%**
199. **`packages/website/src/components/home/RecentBlogPosts/index.tsx`** -> AI Confidence: **99.08%**
200. **`packages/website/tools/generate-website-dts.mts`** -> AI Confidence: **99.08%**
201. **`packages/scope-manager/src/scope/FunctionScope.ts`** -> AI Confidence: **99.07%**
202. **`packages/typescript-estree/src/parser.ts`** -> AI Confidence: **99.07%**
203. **`packages/website/src/components/typeDetails/SimplifiedTreeView.tsx`** -> AI Confidence: **99.07%**
204. **`packages/website/src/theme/BlogSidebar/Content/index.tsx`** -> AI Confidence: **99.07%**
205. **`packages/website/src/theme/MDXComponents/index.tsx`** -> AI Confidence: **99.07%**
206. **`tools/scripts/generate-lib.mts`** -> AI Confidence: **99.07%**
207. **`packages/integration-tests/fixtures/flat-config-types-@types__eslint-v8/eslint.config.js`** -> AI Confidence: **99.07%**
208. **`packages/integration-tests/fixtures/flat-config-types-@types__eslint-v9/eslint.config.js`** -> AI Confidence: **99.07%**
209. **`packages/website-eslint/src/index.js`** -> AI Confidence: **99.07%**
210. **`packages/ast-spec/src/declaration/ExportDefaultDeclaration/fixtures/_error_/variable-declaration/fixture.ts`** -> AI Confidence: **99.06%**
211. **`packages/ast-spec/src/declaration/ExportDefaultDeclaration/fixtures/anonymous-function/fixture.ts`** -> AI Confidence: **99.06%**
212. **`packages/ast-spec/src/declaration/ExportDefaultDeclaration/fixtures/function/fixture.ts`** -> AI Confidence: **99.06%**
213. **`packages/ast-spec/src/declaration/ExportDefaultDeclaration/fixtures/identifier/fixture.ts`** -> AI Confidence: **99.06%**
214. **`packages/ast-spec/src/declaration/ExportDefaultDeclaration/fixtures/literal/fixture.ts`** -> AI Confidence: **99.06%**
215. **`packages/ast-spec/src/expression/AssignmentExpression/AssignmentOperatorToText.ts`** -> AI Confidence: **99.06%**
216. **`packages/ast-spec/src/expression/TSSatisfiesExpression/fixtures/conditional-no-parentheses/fixture.ts`** -> AI Confidence: **99.06%**
217. **`packages/ast-spec/src/expression/TSSatisfiesExpression/fixtures/conditional-with-parentheses/fixture.ts`** -> AI Confidence: **99.06%**
218. **`packages/ast-spec/src/legacy-fixtures/basics/fixtures/arrow-function-with-optional-parameter/fixture.ts`** -> AI Confidence: **99.06%**
219. **`packages/ast-spec/src/legacy-fixtures/basics/fixtures/class-static-blocks/fixture.ts`** -> AI Confidence: **99.06%**
220. **`packages/ast-spec/src/legacy-fixtures/basics/fixtures/class-with-optional-computed-property/fixture.ts`** -> AI Confidence: **99.06%**
221. **`packages/ast-spec/src/legacy-fixtures/basics/fixtures/class-with-optional-property-undefined/fixture.ts`** -> AI Confidence: **99.06%**
222. **`packages/ast-spec/src/legacy-fixtures/errorRecovery/fixtures/_error_/interface-with-optional-index-signature/fixture.ts`** -> AI Confidence: **99.06%**
223. **`packages/ast-spec/src/legacy-fixtures/types/fixtures/conditional-with-null/fixture.ts`** -> AI Confidence: **99.06%**
224. **`packages/ast-spec/src/legacy-fixtures/types/fixtures/conditional/fixture.ts`** -> AI Confidence: **99.06%**
225. **`packages/ast-spec/src/legacy-fixtures/types/fixtures/constructor/fixture.ts`** -> AI Confidence: **99.06%**
226. **`packages/ast-spec/src/legacy-fixtures/types/fixtures/function/fixture.ts`** -> AI Confidence: **99.06%**
227. **`packages/ast-spec/src/legacy-fixtures/types/fixtures/tuple-named-type/fixture.ts`** -> AI Confidence: **99.06%**
228. **`packages/ast-spec/src/legacy-fixtures/types/fixtures/tuple-type/fixture.ts`** -> AI Confidence: **99.06%**
229. **`packages/ast-spec/src/statement/ForInStatement/fixtures/_error_/using-initializer/fixture.ts`** -> AI Confidence: **99.06%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `packages/eslint-plugin/src/rules/consistent-type-imports.ts` -> **100.0%** Exposure
- `packages/eslint-plugin/src/rules/naming-convention.ts` -> **100.0%** Exposure
- `packages/eslint-plugin/src/rules/sort-type-constituents.ts` -> **100.0%** Exposure
- `packages/eslint-plugin/src/util/class-scope-analyzer/classScopeAnalyzer.ts` -> **100.0%** Exposure
- `packages/eslint-plugin/src/util/collectUnusedVariables.ts` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `packages/eslint-plugin/tools/generate-breaking-changes.mts` -> **100.0%** Exposure
- `packages/website/typings/esquery.d.ts` -> **100.0%** Exposure
- `packages/rule-tester/src/RuleTester.ts` -> **0.0019%** Exposure
### Hardcoded Payload Artifacts
- `packages/website/docusaurus.config.mts` -> **76.8824%** Exposure
### Algorithmic DoS Exposure
- `packages/eslint-plugin-internal/src/rules/no-relative-paths-to-internal-packages.ts` -> **100.0%** Exposure
- `packages/eslint-plugin/src/rules/class-literal-property-style.ts` -> **100.0%** Exposure
- `packages/eslint-plugin/src/rules/consistent-type-definitions.ts` -> **100.0%** Exposure
- `packages/eslint-plugin/src/rules/consistent-type-imports.ts` -> **100.0%** Exposure
- `packages/eslint-plugin/src/rules/explicit-member-accessibility.ts` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1232` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `packages/typescript-estree/src/convert.ts` (TYPESCRIPT) -> Cumulative Risk: **861.42**
- **Archetype:** `file_cluster_2` (Distance: 13.529 IQR)
- **Magnitude:** 237.94 | **LOC:** 3059 | **CtrlFlow:** 46.6% | **Authorship Centralization:** 64.3%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `convertNode` (Impact: 1214.4), `convertJSXTagName` (Impact: 49.4), `fixExports` (Impact: 27.9)

### 2. `packages/scope-manager/src/referencer/Referencer.ts` (TYPESCRIPT) -> Cumulative Risk: **772.39**
- **Archetype:** `file_cluster_13` (Distance: 13.765 IQR)
- **Magnitude:** 107.91 | **LOC:** 850 | **CtrlFlow:** 56.5% | **Authorship Centralization:** 28.6%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `AssignmentExpression` (Impact: 72.1), `visitFunctionParameterTypeAnnotation` (Impact: 42.3), `TSEnumDeclaration` (Impact: 37.8)

### 3. `packages/eslint-plugin/src/rules/no-unsafe-argument.ts` (TYPESCRIPT) -> Cumulative Risk: **759.38**
- **Archetype:** `file_cluster_8` (Distance: 10.09 IQR)
- **Magnitude:** 31.86 | **LOC:** 328 | **CtrlFlow:** 41.3% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (99.9996%)
- **Heaviest Functions:** `create` (Impact: 176.8), `create` (Impact: 46.4), `getNextParameterType` (Impact: 36.3)

### 4. `packages/scope-manager/src/scope/GlobalScope.ts` (TYPESCRIPT) -> Cumulative Risk: **729.38**
- **Archetype:** `file_cluster_13` (Distance: 12.231 IQR)
- **Magnitude:** 12.66 | **LOC:** 116 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `close` (Impact: 46.0), `addVariables` (Impact: 13.6), `super` (Impact: 2.7)

### 5. `packages/eslint-plugin/src/rules/naming-convention.ts` (TYPESCRIPT) -> Cumulative Risk: **727.33**
- **Archetype:** `file_cluster_8` (Distance: 11.785 IQR)
- **Magnitude:** 46.38 | **LOC:** 790 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `create` (Impact: 261.8), `isExported` (Impact: 41.8), `isGlobal` (Impact: 7.8)

### 6. `packages/website/src/hooks/useDebouncedToggle.ts` (TYPESCRIPT) -> Cumulative Risk: **694.39**
- **Archetype:** `file_cluster_4` (Distance: 12.951 IQR)
- **Magnitude:** 2.67 | **LOC:** 27 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9998%)
- **Heaviest Functions:** `useDebouncedToggle` (Impact: 7.2)

### 7. `packages/website-eslint/src/mock/assert.js` (JAVASCRIPT) -> Cumulative Risk: **692.47**
- **Archetype:** `file_cluster_8` (Distance: 12.273 IQR)
- **Magnitude:** 98.94 | **LOC:** 110 | **CtrlFlow:** 76.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9964%)
- **Heaviest Functions:** `constructor` (Impact: 27.4), `equal` (Impact: 8.3), `notEqual` (Impact: 8.3)

### 8. `packages/eslint-plugin/src/rules/no-non-null-assertion.ts` (TYPESCRIPT) -> Cumulative Risk: **667.34**
- **Archetype:** `file_cluster_8` (Distance: 10.077 IQR)
- **Magnitude:** 8.79 | **LOC:** 120 | **CtrlFlow:** 47.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (97.8168%)
- **Heaviest Functions:** `create` (Impact: 67.9)

### 9. `packages/eslint-plugin/src/util/class-scope-analyzer/classScopeAnalyzer.ts` (TYPESCRIPT) -> Cumulative Risk: **651.78**
- **Archetype:** `file_cluster_8` (Distance: 12.165 IQR)
- **Magnitude:** 68.21 | **LOC:** 782 | **CtrlFlow:** 63.0% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `PrivateIdentifier` (Impact: 518.8), `MemberExpression` (Impact: 43.6), `findClassScopeWithName` (Impact: 12.7)

### 10. `packages/eslint-plugin/src/util/collectUnusedVariables.ts` (TYPESCRIPT) -> Cumulative Risk: **635.21**
- **Archetype:** `file_cluster_0` (Distance: 12.396 IQR)
- **Magnitude:** 73.74 | **LOC:** 827 | **CtrlFlow:** 57.0% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `isUsedVariable` (Impact: 381.5), `TSParameterProperty` (Impact: 36.7), `isMergeableExported` (Impact: 28.1)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/typescript-estree/src/convert.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_2` (Drift: 13.529 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.428 IQR)
- **Top Global Matches:** file_cluster_2: 13.529, file_cluster_17: 13.578, file_cluster_8: 13.588
- **Magnitude:** 237.94 | **LOC:** 3059 | **CtrlFlow:** 46.6% | **Authorship Centralization:** 64.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 328
- **Risk Profile:** Cognitive Load (78.7709%), Tech Debt (8.3063%)
**Top Internal Functions/Classes:**
  * `convertNode` (Impact: 1214.4 | O(N^5) | DB: 328)
  * `convertJSXTagName` (Impact: 49.4 | O(2^N) | DB: 6)
  * `fixExports` (Impact: 27.9 | O(N^3) | DB: 11)
  * `convertMethodSignature` (Impact: 22.3 | O(N^3) | DB: 5)
  * `registerTSNodeInNodeMap` (Impact: 8.6 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 260`, `structural_boundaries: 298`, `args: 19`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 973`, `dead_code: 1`, `planned_debt: 3`
* *Architecture:* `api: 2`, `concurrency: 36`
* *Defense:* `safety: 27`, `doc: 23`, `immutability_locks: 91`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.762
  * `Choke Point (Betweenness):` 1.2e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` parser-options, ts-estree, semantic-or-syntactic-errors, typescript, check-syntax-errors, node-utils, getModifiers
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/website-eslint/src/mock/path.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.907 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.483 IQR)
- **Top Global Matches:** file_cluster_17: 12.907, file_cluster_11: 12.944, file_cluster_0: 13.021
- **Magnitude:** 204.52 | **LOC:** 235 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (66.6699%), Tech Debt (13.4823%)
**Top Internal Functions/Classes:**
  * `resolve` (Impact: 36.1 | O(2^N) | DB: 21)
    * *Intent:* // path.resolve([from ...], to) // posix version
  * `relative` (Impact: 30.7 | O(N^2) | DB: 4)
    * *Intent:* // path.relative(from, to) // posix version
  * `normalizeArray` (Impact: 16.8 | O(N^1) | DB: 6)
    * *Intent:* // in all copies or substantial portions of the Software. // // THE SOFTWARE IS PROVIDED "AS IS", WI...
  * `filter` (Impact: 14.5 | O(2^N) | DB: 2)
  * `normalize` (Impact: 11.3 | O(N^1) | DB: 30)
    * *Intent:* // path.normalize(path) // posix version
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 42`, `args: 15`, `func_start: 15`
* *Risk/State:* `state_mutation: 51`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `io: 25`, `api: 11`, `import: 1`
* *Defense:* `safety: 12`, `doc: 1`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.417
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/typescript-estree/src/check-syntax-errors.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.418 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.829 IQR)
- **Top Global Matches:** file_cluster_8: 9.418, file_cluster_7: 10.009, file_cluster_1: 10.171
- **Magnitude:** 110.61 | **LOC:** 691 | **CtrlFlow:** 80.5% | **Authorship Centralization:** 90.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (19.8705%), Tech Debt (11.6355%)
**Top Internal Functions/Classes:**
  * `checkSyntaxError` (Impact: 1075.5 | O(N^4) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 186`, `structural_boundaries: 45`, `args: 5`, `func_start: 4`
* *Risk/State:* `state_mutation: 15`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `api: 2`, `concurrency: 3`, `import: 4`
* *Defense:* `safety: 11`, `doc: 8`, `immutability_locks: 33`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.454
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ts-estree, check-modifiers, node-utils, typescript
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/scope-manager/src/referencer/Referencer.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.765 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.651 IQR)
- **Top Global Matches:** file_cluster_13: 13.765, file_cluster_8: 13.809, file_cluster_0: 14.006
- **Magnitude:** 107.91 | **LOC:** 850 | **CtrlFlow:** 56.5% | **Authorship Centralization:** 28.6%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (80.1979%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `AssignmentExpression` (Impact: 72.1 | O(2^N) | DB: 8)
  * `visitFunctionParameterTypeAnnotation` (Impact: 42.3 | O(2^N) | DB: 3)
  * `TSEnumDeclaration` (Impact: 37.8 | O(2^N) | DB: 6)
  * `visitFunction` (Impact: 34.4 | O(N^3) | DB: 13)
  * `VariableDeclaration` (Impact: 33.8 | O(2^N) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 67`, `args: 82`, `func_start: 73`, `class_start: 2`
* *Risk/State:* `state_mutation: 356`, `dead_code: 1`
* *Architecture:* `api: 15`, `import: 17`
* *Defense:* `safety: 66`, `doc: 4`, `test: 2`, `immutability_locks: 25`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.182
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` ImportVisitor, Reference, types, assert, PatternVisitor, ScopeManager, ClassVisitor, scope...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `packages/website-eslint/src/mock/assert.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.273 IQR)
- **Local Micro-Species:** `Cluster 1: Async Testing & I/O Mocks` (Drift: 4.791 IQR)
- **Top Global Matches:** file_cluster_8: 12.273, file_cluster_0: 12.734, file_cluster_17: 12.773
- **Magnitude:** 98.94 | **LOC:** 110 | **CtrlFlow:** 76.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (64.8194%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 27.4 | O(N^3) | DB: 9)
  * `equal` (Impact: 8.3 | O(2^N))
  * `notEqual` (Impact: 8.3 | O(2^N))
  * `strictEqual` (Impact: 8.2 | O(2^N))
  * `notStrictEqual` (Impact: 8.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 4`, `args: 7`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 25`
* *Architecture:* `api: 2`
* *Defense:* `safety: 6`, `test: 13`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/typescript-estree/src/node-utils.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.465 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.331 IQR)
- **Top Global Matches:** file_cluster_8: 10.465, file_cluster_13: 10.669, file_cluster_16: 10.736
- **Magnitude:** 91.89 | **LOC:** 849 | **CtrlFlow:** 43.7% | **Authorship Centralization:** 83.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (10.3708%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `isJSDocComment` (Impact: 808.5 | O(2^N) | DB: 10)
    * *Intent:* /** * Returns true if the given ts.Token is a comma */
  * `getLastModifier` (Impact: 8.3 | O(N^1))
    * *Intent:* /** * Checks if a ts.Node has a modifier
  * `hasModifier` (Impact: 4.3 | O(N^1))
  * `isComment` (Impact: 4.3 | O(N^1))
  * `getTextForTokenKind` (Impact: 3.8 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 134`, `args: 58`, `func_start: 50`, `class_start: 2`
* *Risk/State:* `state_mutation: 24`, `dead_code: 1`
* *Architecture:* `api: 45`, `import: 6`
* *Defense:* `safety: 16`, `doc: 35`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` version-check, ts-estree, typescript, ;
  [SyntaxKind.KeyOfKeyword]:, xhtml-entities, getModifiers
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `packages/eslint-plugin/src/rules/no-misused-promises.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.324 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 2.95 IQR)
- **Top Global Matches:** file_cluster_8: 10.324, file_cluster_13: 10.797, file_cluster_7: 10.831
- **Magnitude:** 81.21 | **LOC:** 1018 | **CtrlFlow:** 59.5% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (14.0254%), Tech Debt (13.9467%)
**Top Internal Functions/Classes:**
  * `isPossiblyFunctionType` (Impact: 194.9 | O(N^3))
    * *Intent:* /**
  * `checkProperty` (Impact: 118.7 | O(N^4))
  * `isAlwaysThenable` (Impact: 106.8 | O(N^4) | DB: 5)
  * `checkConditional` (Impact: 55.5 | O(2^N) | DB: 1)
  * `parseChecksVoidReturn` (Impact: 48.2 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 184`, `structural_boundaries: 125`, `args: 49`, `func_start: 44`, `class_start: 1`
* *Risk/State:* `state_mutation: 24`, `dead_code: 2`, `duplicate_logic: 2`
* *Architecture:* `api: 6`, `concurrency: 12`, `import: 7`
* *Defense:* `safety: 40`, `doc: 20`, `immutability_locks: 56`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.294
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ts-api-utils, util, utils, promiseUtils, typescript
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/eslint-plugin/src/util/collectUnusedVariables.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.396 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.455 IQR)
- **Top Global Matches:** file_cluster_0: 12.396, file_cluster_17: 12.53, file_cluster_13: 12.543
- **Magnitude:** 73.74 | **LOC:** 827 | **CtrlFlow:** 57.0% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (31.2742%), Tech Debt (28.6964%)
**Top Internal Functions/Classes:**
  * `isUsedVariable` (Impact: 381.5 | O(N^4) | DB: 10)
    * *Intent:* /**
  * `TSParameterProperty` (Impact: 36.7 | O(2^N) | DB: 2)
  * `isMergeableExported` (Impact: 28.1 | O(N^2))
  * `markVariableAsUsed` (Impact: 25.9 | O(N^2) | DB: 4)
  * `visitForInForOf` (Impact: 22.5 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 142`, `structural_boundaries: 107`, `args: 53`, `func_start: 43`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 122`, `dead_code: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 4`, `import: 6`
* *Defense:* `safety: 50`, `doc: 55`, `immutability_locks: 52`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.301
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` utils, isTypeImport, scope-manager, referenceContainsTypeQuery
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/eslint-plugin/src/rules/no-unused-vars.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.912 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.164 IQR)
- **Top Global Matches:** file_cluster_8: 9.912, file_cluster_7: 10.431, file_cluster_13: 10.467
- **Magnitude:** 72.86 | **LOC:** 1470 | **CtrlFlow:** 47.2% | **Authorship Centralization:** 20.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (13.496%), Tech Debt (36.4649%)
**Top Internal Functions/Classes:**
  * `create` (Impact: 625.7 | O(N^4) | DB: 10)
  * `hasOverridingExportStatement` (Impact: 21.9 | O(N^2))
  * `predicate` (Impact: 13.9 | O(2^N))
  * `predicate` (Impact: 8.4 | O(2^N))
  * `getStatementsOfNode` (Impact: 3.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 175`, `structural_boundaries: 196`, `args: 53`, `func_start: 45`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 30`, `dead_code: 1`, `planned_debt: 13`, `duplicate_logic: 2`
* *Architecture:* `api: 4`, `concurrency: 2`, `import: 7`
* *Defense:* `safety: 29`, `doc: 24`, `immutability_locks: 58`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.294
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` module, util, scope-manager, utils, referenceContainsTypeQuery
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/eslint-plugin-internal/src/rules/plugin-test-formatting.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.013 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.473 IQR)
- **Top Global Matches:** file_cluster_8: 10.013, file_cluster_13: 10.478, file_cluster_0: 10.5
- **Magnitude:** 71.27 | **LOC:** 652 | **CtrlFlow:** 60.5% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (11.9881%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ObjectExpression` (Impact: 292.1 | O(2^N) | DB: 1)
  * `checkTemplateLiteral` (Impact: 148.5 | O(N^4) | DB: 3)
  * `checkLiteral` (Impact: 57.6 | O(N^4))
  * `checkExpression` (Impact: 34.1 | O(N^2))
  * `checkValidTest` (Impact: 32.7 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 79`, `args: 40`, `func_start: 40`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 20`
* *Architecture:* `io: 3`, `api: 2`, `import: 7`
* *Defense:* `safety: 26`, `doc: 8`, `immutability_locks: 43`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sync, index.js, utils, type-utils, node:url, node:path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/eslint-plugin/src/rules/no-shadow.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.174 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.096 IQR)
- **Top Global Matches:** file_cluster_8: 10.174, file_cluster_7: 10.541, file_cluster_0: 10.548
- **Magnitude:** 68.3 | **LOC:** 711 | **CtrlFlow:** 51.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (7.2855%), Tech Debt (9.7956%)
**Top Internal Functions/Classes:**
  * `create` (Impact: 649.3 | O(N^5) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 121`, `args: 42`, `func_start: 35`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 19`, `fragile_debt: 1`
* *Architecture:* `api: 4`, `import: 6`
* *Defense:* `safety: 19`, `doc: 48`, `immutability_locks: 38`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.294
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` utils, isTypeImport, util, scope-manager
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/eslint-plugin/src/util/class-scope-analyzer/classScopeAnalyzer.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.165 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.05 IQR)
- **Top Global Matches:** file_cluster_8: 12.165, file_cluster_13: 12.381, file_cluster_0: 12.405
- **Magnitude:** 68.21 | **LOC:** 782 | **CtrlFlow:** 63.0% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (49.9962%), Tech Debt (9.4425%)
**Top Internal Functions/Classes:**
  * `PrivateIdentifier` (Impact: 518.8 | O(2^N) | DB: 10)
  * `MemberExpression` (Impact: 43.6 | O(2^N) | DB: 2)
  * `findClassScopeWithName` (Impact: 12.7 | O(N^2) | DB: 1)
    * *Intent:* /* eslint-disable @typescript-eslint/no-this-alias -- we do a bunch of "start iterating from here" c...
  * `AssignmentExpression` (Impact: 12.5 | O(2^N) | DB: 2)
  * `AssignmentPattern` (Impact: 12.5 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 37`, `args: 21`, `func_start: 21`, `class_start: 2`
* *Risk/State:* `state_mutation: 55`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 6`
* *Defense:* `safety: 12`, `doc: 9`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.417
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` scope-manager, utils, extractComputedName, .., types
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/eslint-plugin/src/util/getOperatorPrecedence.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.805 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 2.133 IQR)
- **Top Global Matches:** file_cluster_8: 7.805, file_cluster_7: 8.589, file_cluster_13: 8.718
- **Magnitude:** 65.56 | **LOC:** 499 | **CtrlFlow:** 76.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (25.3455%), Tech Debt (14.7929%)
**Top Internal Functions/Classes:**
  * `getOperatorPrecedenceForNode` (Impact: 327.0 | O(2^N))
    * *Intent:* /** * Note that this does not take into account parenthesization. You should check * for parenthesiz...
  * `getOperatorPrecedence` (Impact: 233.4 | O(N^2))
  * `getBinaryOperatorPrecedence` (Impact: 84.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 176`, `structural_boundaries: 54`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `planned_debt: 4`
* *Architecture:* `api: 5`, `import: 4`
* *Defense:* `safety: 2`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils, types, typescript
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/eslint-plugin/src/rules/no-unnecessary-type-parameters.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.747 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.601 IQR)
- **Top Global Matches:** file_cluster_8: 10.747, file_cluster_13: 10.962, file_cluster_17: 11.16
- **Magnitude:** 63.76 | **LOC:** 566 | **CtrlFlow:** 51.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (17.1558%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `collectTypeParameterUsageCounts` (Impact: 349.5 | O(N^3) | DB: 7)
  * `create` (Impact: 161.4 | O(N^6) | DB: 1)
  * `isTypeParameterRepeatedInAST` (Impact: 46.0 | O(N^2) | DB: 1)
  * `skipConstituentsUpward` (Impact: 20.4 | O(2^N))
  * `countTypeParameterUsage` (Impact: 10.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 118`, `structural_boundaries: 110`, `args: 54`, `func_start: 48`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 27`
* *Architecture:* `api: 2`, `import: 7`
* *Defense:* `safety: 31`, `doc: 6`, `immutability_locks: 42`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.294
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ts-api-utils, util, scope-manager, utils, typescript
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/eslint-plugin/src/rules/no-unnecessary-condition.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.684 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.469 IQR)
- **Top Global Matches:** file_cluster_8: 8.684, file_cluster_7: 9.415, file_cluster_13: 9.464
- **Magnitude:** 60.54 | **LOC:** 950 | **CtrlFlow:** 46.8% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (8.5853%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `checkNode` (Impact: 595.1 | O(2^N) | DB: 6)
    * *Intent:* /**
  * `isNullishType` (Impact: 2.1 | O(N^1))
  * `isAlwaysNullish` (Impact: 2.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 58`, `args: 25`, `func_start: 20`
* *Risk/State:* None
* *Architecture:* `io: 2`, `api: 1`, `import: 6`
* *Defense:* `safety: 8`, `doc: 5`, `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.294
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ts-api-utils, assertionFunctionUtils, util, utils, typescript
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/eslint-plugin/src/rules/no-deprecated.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.826 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.14 IQR)
- **Top Global Matches:** file_cluster_8: 9.826, file_cluster_13: 10.249, file_cluster_7: 10.396
- **Magnitude:** 55.84 | **LOC:** 507 | **CtrlFlow:** 60.2% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (14.7057%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `create` (Impact: 539.9 | O(N^4) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 80`, `args: 24`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 9`, `dead_code: 1`
* *Architecture:* `api: 2`, `import: 6`
* *Defense:* `safety: 22`, `doc: 7`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.294
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ts-api-utils, util, utils, typescript, ...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/rule-tester/src/RuleTester.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.094 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.347 IQR)
- **Top Global Matches:** file_cluster_13: 11.094, file_cluster_17: 11.356, file_cluster_0: 11.534
- **Magnitude:** 52.31 | **LOC:** 1399 | **CtrlFlow:** 34.8% | **Authorship Centralization:** 28.6%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (7.8968%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 484.9 | O(2^N) | DB: 8)
  * `throwForbiddenMethodError` (Impact: 4.5 | O(N^1) | DB: 1)
  * `getMessagePlaceholders` (Impact: 2.2 | O(N^1))
  * `getUnsubstitutedMessagePlaceholders` (Impact: 1.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 88`, `args: 32`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 19`, `dead_code: 2`
* *Architecture:* `io: 3`, `api: 3`, `import: 27`
* *Defense:* `safety: 30`, `doc: 32`, `test: 4`, `immutability_locks: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.292
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` eslint-utils, omitCustomConfigProperties, types, freezeDeeply, SourceCodeFixer, node:assert, cloneDeeplyExcludesParent, node:util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/website/src/components/linter/createLinter.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.358 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.815 IQR)
- **Top Global Matches:** file_cluster_13: 11.358, file_cluster_8: 11.473, file_cluster_17: 11.533
- **Magnitude:** 48.9 | **LOC:** 264 | **CtrlFlow:** 45.0% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (11.079%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createLinter` (Impact: 460.6 | O(2^N) | DB: 6)
  * `onParse` (Impact: 5.6 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 44`, `args: 29`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 16`
* *Architecture:* `api: 2`, `import: 11`
* *Defense:* `safety: 25`, `doc: 6`, `immutability_locks: 29`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.535
  * `Choke Point (Betweenness):` 8e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` config, utils, createEventsBinder, ts-eslint, typescript, types, types, typescript-vfs...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/eslint-plugin/src/rules/consistent-type-imports.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.497 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.787 IQR)
- **Top Global Matches:** file_cluster_17: 12.497, file_cluster_0: 12.698, file_cluster_13: 12.736
- **Magnitude:** 47.22 | **LOC:** 958 | **CtrlFlow:** 42.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (15.4787%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `create` (Impact: 434.2 | O(N^6) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 100`, `args: 16`, `func_start: 11`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 27`, `dead_code: 9`
* *Architecture:* `api: 4`, `import: 6`
* *Defense:* `safety: 14`, `doc: 4`, `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.294
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` isClosingBraceToken, util, NullThrowsReasons.MissingToken(, isTypeKeyword, target.source, utils, node.type), );
      yield fixer.insertTextAfter(importToken...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/typescript-estree/src/check-modifiers.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.824 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.811 IQR)
- **Top Global Matches:** file_cluster_8: 8.824, file_cluster_1: 9.462, file_cluster_7: 9.581
- **Magnitude:** 46.53 | **LOC:** 423 | **CtrlFlow:** 75.5% | **Authorship Centralization:** 87.5%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (28.5242%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `checkModifiers` (Impact: 356.6 | O(N^3))
  * `nodeCanBeDecorated` (Impact: 68.8 | O(N^2))
    * *Intent:* // Rewrite version of `ts.nodeCanBeDecorated` // Returns `true` for both `useLegacyDecorators: true`...
  * `nodeIsMissing` (Impact: 10.3 | O(N^1))
    * *Intent:* // `ts.nodeIsMissing`
  * `getThisParameter` (Impact: 7.5 | O(N^1))
    * *Intent:* // `ts.getThisParameter`
  * `nodeIsPresent` (Impact: 2.6 | O(N^1))
    * *Intent:* // `ts.nodeIsPresent`
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 37`, `args: 18`, `func_start: 17`
* *Risk/State:* None
* *Architecture:* `api: 3`, `concurrency: 2`, `import: 4`
* *Defense:* `safety: 8`, `doc: 1`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.486
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ts-estree, node-utils, getModifiers, typescript
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/eslint-plugin/src/rules/no-duplicate-type-constituents.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.761 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.519 IQR)
- **Top Global Matches:** file_cluster_8: 9.761, file_cluster_13: 10.083, file_cluster_17: 10.089
- **Magnitude:** 46.43 | **LOC:** 300 | **CtrlFlow:** 41.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (11.8953%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `checkDuplicateRecursively` (Impact: 138.0 | O(2^N) | DB: 2)
  * `TSUnionType` (Impact: 97.3 | O(2^N))
  * `report` (Impact: 91.4 | O(2^N) | DB: 3)
  * `isSameAstNode` (Impact: 85.6 | O(2^N))
  * `checkDuplicate` (Impact: 14.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 66`, `args: 25`, `func_start: 19`
* *Risk/State:* `state_mutation: 15`
* *Architecture:* `api: 4`, `import: 6`
* *Defense:* `safety: 14`, `doc: 2`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.294
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` utils, ts-api-utils, util, typescript
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/eslint-plugin/src/rules/naming-convention.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.785 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.236 IQR)
- **Top Global Matches:** file_cluster_8: 11.785, file_cluster_4: 11.908, file_cluster_13: 11.909
- **Magnitude:** 46.38 | **LOC:** 790 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(N^4) | **DB Complexity:** 29
- **Risk Profile:** Cognitive Load (41.0173%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `create` (Impact: 261.8 | O(N^4) | DB: 29)
  * `isExported` (Impact: 41.8 | O(N^2))
    * *Intent:* // #endregion enumMember // #region class
  * `isGlobal` (Impact: 7.8 | O(N^1))
  * `requiresQuoting` (Impact: 6.5 | O(N^1))
  * `getIdentifiersFromPattern` (Impact: 2.1 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 98`, `args: 54`, `func_start: 45`
* *Risk/State:* `state_mutation: 88`
* *Architecture:* `api: 9`, `concurrency: 36`, `import: 7`
* *Defense:* `safety: 25`, `doc: 3`, `immutability_locks: 46`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` format: [, FunctionDeclaration, util, scope-manager, utils, TSDeclareFunction, typescript, FunctionExpression...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/eslint-plugin/src/rules/explicit-module-boundary-types.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.433 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.148 IQR)
- **Top Global Matches:** file_cluster_8: 9.433, file_cluster_13: 9.889, file_cluster_7: 10.026
- **Magnitude:** 44.93 | **LOC:** 532 | **CtrlFlow:** 49.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (13.0065%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `create` (Impact: 420.8 | O(N^4) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 102`, `args: 36`, `func_start: 35`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 15`
* *Architecture:* `api: 5`, `import: 6`
* *Defense:* `safety: 15`, `doc: 4`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.294
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` utils, explicitReturnTypeUtils, util, scope-manager
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/eslint-plugin/src/rules/unified-signatures.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.651 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.21 IQR)
- **Top Global Matches:** file_cluster_8: 10.651, file_cluster_13: 11.103, file_cluster_7: 11.182
- **Magnitude:** 44.43 | **LOC:** 732 | **CtrlFlow:** 50.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (12.8822%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `signaturesDifferByOptionalOrRestParamete` (Impact: 51.1 | O(N^2) | DB: 2)
  * `signatureUsesTypeParameter` (Impact: 37.6 | O(N^3))
  * `addOverload` (Impact: 37.6 | O(N^2) | DB: 2)
  * `getOverloadInfo` (Impact: 22.1 | O(N^2))
  * `getStaticParameterName` (Impact: 20.5 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 102`, `args: 57`, `func_start: 50`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 32`
* *Architecture:* `api: 12`, `import: 4`
* *Defense:* `safety: 32`, `doc: 11`, `immutability_locks: 30`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.294
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` utils, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### 🚨 Severe Anti-Patterns (Language Convention Violations)
- `packages/ast-spec/src/expression/ObjectExpression/fixtures/_error_/getter-modifier-private/fixture.ts` (TYPESCRIPT) | **Drift Ratio: 1.6x**
  * **Global Archetype:** `file_cluster_8` (Drift: 3.632 IQR)
  * **Local Reality:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.822 IQR)
- `packages/ast-spec/src/expression/ObjectExpression/fixtures/_error_/getter-modifier-protected/fixture.ts` (TYPESCRIPT) | **Drift Ratio: 1.6x**
  * **Global Archetype:** `file_cluster_8` (Drift: 3.632 IQR)
  * **Local Reality:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.822 IQR)
- `packages/ast-spec/src/expression/ObjectExpression/fixtures/_error_/method-modifier-private/fixture.ts` (TYPESCRIPT) | **Drift Ratio: 1.6x**
  * **Global Archetype:** `file_cluster_8` (Drift: 3.632 IQR)
  * **Local Reality:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.822 IQR)
- `packages/ast-spec/src/expression/ObjectExpression/fixtures/_error_/method-modifier-protected/fixture.ts` (TYPESCRIPT) | **Drift Ratio: 1.6x**
  * **Global Archetype:** `file_cluster_8` (Drift: 3.632 IQR)
  * **Local Reality:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.822 IQR)
- `packages/ast-spec/src/expression/ObjectExpression/fixtures/_error_/property-modifier-private/fixture.ts` (TYPESCRIPT) | **Drift Ratio: 1.6x**
  * **Global Archetype:** `file_cluster_8` (Drift: 3.632 IQR)
  * **Local Reality:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.822 IQR)

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `packages/eslint-plugin/src/configs/flat/eslint-recommended.ts` (TYPESCRIPT) | Magnitude: 1.63 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, indent_spaces: 4, decorators: 3, doc: 2
- `packages/parser/tests/fixtures/scope-analysis/decorator-parameter-property-parameter.ts` (TYPESCRIPT) | Magnitude: 0.36 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, branch: 1, args: 1, func_start: 1
- `packages/eslint-plugin/src/configs/flat/stylistic.ts` (TYPESCRIPT) | Magnitude: 0.61 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 23, doc: 15, decorators: 14, structural_boundaries: 11
- `packages/eslint-plugin/src/configs/eslintrc/disable-type-checked.ts` (TYPESCRIPT) | Magnitude: 3.23 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_1`
  * Top Architectural Signatures: indent_spaces: 64, doc: 62, decorators: 62, events: 61
- `packages/eslint-plugin/src/configs/flat/stylistic-type-checked.ts` (TYPESCRIPT) | Magnitude: 0.67 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_1`
  * Top Architectural Signatures: indent_spaces: 32, doc: 23, decorators: 22, structural_boundaries: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `packages/eslint-plugin/src/configs/flat/disable-type-checked.ts` (TYPESCRIPT) | Magnitude: 3.25 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 69, doc: 63, decorators: 62, events: 61
- `packages/eslint-plugin/src/configs/flat/recommended.ts` (TYPESCRIPT) | Magnitude: 0.5 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 32, doc: 22, decorators: 21, structural_boundaries: 12
- `packages/rule-tester/src/utils/severity.ts` (TYPESCRIPT) | Magnitude: 1.98 | Delta: **0.068 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 10, doc: 7, branch: 6
- `packages/eslint-plugin/src/configs/eslint-recommended-raw.ts` (TYPESCRIPT) | Magnitude: 2.57 | Delta: **0.173 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 31, events: 19, state_mutation: 9, structural_boundaries: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `packages/ast-spec/src/legacy-fixtures/types/fixtures/constructor/fixture.ts` (TYPESCRIPT) | Magnitude: 1.35 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: state_mutation: 3, branch: 1, structural_boundaries: 1, args: 1
- `packages/ast-spec/src/legacy-fixtures/types/fixtures/function/fixture.ts` (TYPESCRIPT) | Magnitude: 1.35 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: state_mutation: 3, branch: 1, structural_boundaries: 1, args: 1
- `packages/ast-spec/src/legacy-fixtures/types/fixtures/constructor-in-generic/fixture.ts` (TYPESCRIPT) | Magnitude: 1.15 | Delta: **0.078 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: structural_boundaries: 1, args: 1, state_mutation: 1, closures: 1
- `packages/ast-spec/src/legacy-fixtures/types/fixtures/function-in-generic/fixture.ts` (TYPESCRIPT) | Magnitude: 1.15 | Delta: **0.101 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: structural_boundaries: 1, args: 1, safety: 1, state_mutation: 1
- `packages/ast-spec/src/legacy-fixtures/types/fixtures/constructor-abstract/fixture.ts` (TYPESCRIPT) | Magnitude: 1.15 | Delta: **0.128 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: structural_boundaries: 2, args: 1, safety: 1, state_mutation: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/website/src/components/typeDetails/TypesDetails.tsx` (TYPESCRIPT) | Magnitude: 1.44 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 17, ui_framework: 15, import: 9
- `packages/scope-manager/src/referencer/ImportVisitor.ts` (TYPESCRIPT) | Magnitude: 2.78 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 44, encapsulation: 10, structural_boundaries: 9, args: 7
- `packages/ast-spec/src/special/ExportSpecifier/spec.ts` (TYPESCRIPT) | Magnitude: 1.84 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 21, indent_spaces: 8, import: 5, class_start: 3
- `packages/website/plugins/utils/nodes.ts` (TYPESCRIPT) | Magnitude: 2.08 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 20, api: 10, indent_spaces: 6, args: 5
- `packages/ast-spec/src/base/SourceLocation.ts` (TYPESCRIPT) | Magnitude: 1.36 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, doc: 2, indent_spaces: 2, class_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `packages/type-utils/typings/typescript.d.ts` (TYPESCRIPT) | Magnitude: 1.47 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 6, class_start: 2, generics: 2
- `packages/utils/src/ts-eslint/RuleTester.ts` (TYPESCRIPT) | Magnitude: 1.31 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 43, doc: 40, structural_boundaries: 37, immutability_locks: 23
- `packages/ast-spec/src/expression/literal/NumberLiteral/spec.ts` (TYPESCRIPT) | Magnitude: 1.31 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, class_start: 1, api: 1, generics: 1
- `packages/ast-spec/src/expression/literal/StringLiteral/spec.ts` (TYPESCRIPT) | Magnitude: 1.31 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, class_start: 1, api: 1, generics: 1
- `packages/ast-spec/src/legacy-fixtures/expressions/fixtures/call-expression-type-arguments/fixture.ts` (TYPESCRIPT) | Magnitude: 1.1 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: func_start: 2, generics: 1, planned_debt: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/website-eslint/src/mock/path.js` (JAVASCRIPT) | Magnitude: 204.52 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 129, state_mutation: 51, branch: 47, structural_boundaries: 42
- `packages/eslint-plugin/src/rules/no-redeclare.ts` (TYPESCRIPT) | Magnitude: 9.82 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 170, structural_boundaries: 40, branch: 26, args: 13
- `packages/scope-manager/src/referencer/ClassVisitor.ts` (TYPESCRIPT) | Magnitude: 21.29 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 186, encapsulation: 45, state_mutation: 36, args: 30
- `packages/website/src/components/inputs/Dropdown.tsx` (TYPESCRIPT) | Magnitude: 1.33 | Delta: **0.076 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 16, immutability_locks: 11, args: 7
- `packages/website/src/components/ast/HiddenItem.tsx` (TYPESCRIPT) | Magnitude: 0.83 | Delta: **0.091 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 13, branch: 9, args: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `packages/website/src/components/home/RecentBlogPosts/index.tsx` (TYPESCRIPT) | Magnitude: 1.0 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 37, ui_framework: 12, structural_boundaries: 11, import: 7
- `packages/rule-tester/src/TestFramework.ts` (TYPESCRIPT) | Magnitude: 26.48 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 147, branch: 40, structural_boundaries: 38, doc: 15
- `packages/utils/src/ast-utils/eslint-utils/predicates.ts` (TYPESCRIPT) | Magnitude: 3.82 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 39, indent_spaces: 27, api: 22, explicit_casts: 22
- `packages/scope-manager/tests/fixtures/jsx/namespaced-attribute.tsx` (TYPESCRIPT) | Magnitude: 0.23 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, ui_framework: 2, generics: 2, immutability_locks: 2
- `packages/website/src/components/hooks/useResizeObserver.ts` (TYPESCRIPT) | Magnitude: 1.79 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 10, args: 8, closures: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/website/tools/generate-website-dts.mts` (TYPESCRIPT) | Magnitude: 4.66 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 54, structural_boundaries: 32, concurrency: 26, io: 14
- `tools/scripts/postinstall.mts` (TYPESCRIPT) | Magnitude: 2.37 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 8, concurrency: 5, branch: 4
- `packages/website/src/hooks/useDebouncedToggle.ts` (TYPESCRIPT) | Magnitude: 2.67 | Delta: **0.061 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 19, state_mutation: 11, args: 7, ui_framework: 7
- `packages/eslint-plugin/src/rules/return-await.ts` (TYPESCRIPT) | Magnitude: 23.45 | Delta: **0.079 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 226, branch: 57, structural_boundaries: 53, safety: 35
- `packages/website/src/components/editor/loadSandbox.ts` (TYPESCRIPT) | Magnitude: 3.51 | Delta: **0.118 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 41, structural_boundaries: 22, concurrency: 12, args: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `packages/ast-spec/src/legacy-fixtures/errorRecovery/fixtures/_error_/interface-method-public/fixture.ts` (TYPESCRIPT) | Magnitude: 1.67 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 1, args: 1, func_start: 1, class_start: 1
- `packages/ast-spec/src/legacy-fixtures/basics/fixtures/null-and-undefined-type-annotations/fixture.ts` (TYPESCRIPT) | Magnitude: 1.3 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 2, planned_debt: 1
- `packages/ast-spec/src/legacy-fixtures/basics/fixtures/angle-bracket-type-assertion-arrow-function/fixture.ts` (TYPESCRIPT) | Magnitude: 1.26 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, args: 1, safety_bypasses: 1, state_mutation: 1
- `packages/ast-spec/src/legacy-fixtures/basics/fixtures/catch-clause-with-invalid-annotation/fixture.ts` (TYPESCRIPT) | Magnitude: 1.1 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 2, safety: 2, planned_debt: 1
- `packages/ast-spec/src/legacy-fixtures/errorRecovery/fixtures/_error_/interface-method-export/fixture.ts` (TYPESCRIPT) | Magnitude: 1.26 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, class_start: 1, safety: 1, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `packages/eslint-plugin/typings/eslint-rules.d.ts` (TYPESCRIPT) | Magnitude: 1.41 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 26, indent_spaces: 5, structural_boundaries: 1, safety: 1
- `packages/eslint-plugin/src/util/walkStatements.ts` (TYPESCRIPT) | Magnitude: 7.95 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 46, branch: 24, lazy_evaluation: 11, structural_boundaries: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `packages/website/src/hooks/useRulesMeta.ts` (TYPESCRIPT) | Magnitude: 0.51 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 5, decorators: 2, import: 2
- `packages/typescript-estree/src/parser-options.ts` (TYPESCRIPT) | Magnitude: 1.7 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 55, structural_boundaries: 37, doc: 23, branch: 22
- `packages/ast-spec/src/declaration/ExportNamedDeclaration/spec.ts` (TYPESCRIPT) | Magnitude: 2.09 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 30, indent_spaces: 26, doc: 17, import: 7
- `packages/scope-manager/tests/fixtures/functions/arrow/default-params/writable-ref.ts` (TYPESCRIPT) | Magnitude: 0.28 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 1, args: 1, func_start: 1, state_mutation: 1
- `packages/scope-manager/src/lib/es2018.promise.ts` (TYPESCRIPT) | Magnitude: 1.51 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, import: 2, indent_spaces: 2, api: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/typescript-estree/src/convert.ts` -> Churn: **73.37%** | Cog Load: 78.7709% | Debt: 8.3063%
- `packages/scope-manager/src/referencer/Referencer.ts` -> Churn: **52.79%** | Cog Load: 80.1979% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/typescript-estree/src/check-syntax-errors.ts` -> **fisker Cheung** (90.0% isolated ownership) | Magnitude: 110.61
- `packages/typescript-estree/src/node-utils.ts` -> **fisker Cheung** (83.3% isolated ownership) | Magnitude: 91.89
- `packages/eslint-plugin/src/util/getOperatorPrecedence.ts` -> **Kirk Waiblinger** (100.0% isolated ownership) | Magnitude: 65.56

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/typescript-estree/src/convert.ts` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)
- `packages/website/src/components/linter/createLinter.ts` -> **Severity: 0.001** (Bridge: 0.0001 * Flux: 11.4872%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/scope-manager/src/lib/base-config.ts` -> **Severity: 2427.293** (Blast Radius: 24.418 * Doc Risk: 99.4059%)
- `packages/website-eslint/src/mock/util.js` -> **Severity: 1027.199** (Blast Radius: 30.816 * Doc Risk: 33.3333%)
- `packages/ast-spec/src/unions/Literal.ts` -> **Severity: 652.985** (Blast Radius: 10.101 * Doc Risk: 64.6456%)
- `packages/website/src/components/lib/json.ts` -> **Severity: 507.494** (Blast Radius: 5.093 * Doc Risk: 99.6453%)
- `packages/scope-manager/src/ScopeManager.ts` -> **Severity: 357.3** (Blast Radius: 3.573 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
