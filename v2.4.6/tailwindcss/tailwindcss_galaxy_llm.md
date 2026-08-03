# ARCHITECTURAL_BRIEF: tailwindcss
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_web/tailwindcss` |
| **Timestamp** | `2026-08-03T20:07:04.804514+00:00` |
| **Scan Duration** | `6.08s` |
| **Git Branch** | `main` |
| **Git Commit** | `d7fc281a0e678bf92f0e82f4ab1b8edfd7cb1675` |
| **Git Remote** | `https://github.com/tailwindlabs/tailwindcss.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 335 malicious artifacts.

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
| Total Artifacts | 538 |
| Analyzed Artifacts (Scanned) | 435 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 103 |
| Total LOC | 83160 |
| Volatility Index | 0.03 |
| % Scanned of codebase = | 80.9% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5009 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1368 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.4921 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 41 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 262 | 71095 | 60.2% |
| RUST | 57 | 10267 | 13.1% |
| PLAINTEXT | 37 | 1 | 8.5% |
| MARKDOWN | 24 | 0 | 5.5% |
| CSS | 18 | 652 | 4.1% |
| JAVASCRIPT | 16 | 325 | 3.7% |
| JSON | 14 | 177 | 3.2% |
| HTML | 3 | 565 | 0.7% |
| YAML | 2 | 77 | 0.5% |
| XML | 2 | 1 | 0.5% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `3.893`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 178 | 40.9% |
| file_cluster_13 | 93 | 21.4% |
| file_cluster_4 | 58 | 13.3% |
| file_cluster_0 | 19 | 4.4% |
| file_cluster_16 | 11 | 2.5% |
| file_cluster_17 | 7 | 1.6% |
| file_cluster_2 | 4 | 0.9% |
| file_cluster_11 | 2 | 0.5% |
| Unknown | 1 | 0.2% |
| file_cluster_9 | 1 | 0.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 60 | 13.8% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 103*

**Composition by Extension & Reason:**
- `.ts`: 46x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.undeterminable), 1x Excluded (Machine-Generated Source Code Signature: 1236 LOC)
- `no_extension`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.toml`: 6x Unsupported Format (.toml), 2x Excluded (Unsupported Extension: '.toml'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 4288 LOC)
- `.haml`: 4x Unsupported Format (.haml)
- `.snap`: 4x Unsupported Format (.snap)
- `.svg`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 2x Excluded (Unsupported Extension: '.lock')
- `.gitignore`: 2x Excluded (Unsupported Extension: '.gitignore')
- `.patch`: 2x Excluded (Unsupported Extension: '.patch')
- `.json`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tsx`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rs`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ico`: 1x Excluded (Explicitly Denied Extension: '.ico')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 34.1 | 13.9 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.5 | 45.2 | 50.6 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 16.1 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 10.7 | 0.0 | 0.0 |
| API Exposure | 0.0 | 19.4 | 3.2 | 2.6 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 24.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 56.2 | 80.4 | 0.0 |
| Commented Logic Exposure | 0.0 | 64.6 | 0.8 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 85.8 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 7.1 | 1.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 98.5 | 8.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 33.1 | 17.9 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 33.1 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 14.1 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 1.3 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `crates/oxide/src/fixtures/example.html` (Hits: 140)
- `packages/tailwindcss/src/index.test.ts` (Hits: 59)
- `packages/tailwindcss/src/compat/config.test.ts` (Hits: 43)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **design-system.ts** (`packages/tailwindcss/src/design-system.ts`) — 53 inbound connections
2. **plugin-api.ts** (`packages/tailwindcss/src/compat/plugin-api.ts`) — 30 inbound connections
3. **default-map.ts** (`packages/tailwindcss/src/utils/default-map.ts`) — 27 inbound connections
4. **segment.ts** (`packages/tailwindcss/src/utils/segment.ts`) — 26 inbound connections
5. **version.ts** (`packages/@tailwindcss-upgrade/src/utils/version.ts`) — 22 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **walk.rs** (`crates/ignore/src/walk.rs`) — 44 outbound dependencies
2. **mod.rs** (`crates/oxide/src/scanner/mod.rs`) — 31 outbound dependencies
3. **dir.rs** (`crates/ignore/src/dir.rs`) — 30 outbound dependencies
4. **gitignore.rs** (`crates/ignore/src/gitignore.rs`) — 23 outbound dependencies
5. **index.ts** (`packages/tailwindcss/src/index.ts`) — 22 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `async` (@ `integrations/utils.ts`) -> Impact: **932.5** | LOC: 360
- `replaceAlpha` (@ `packages/tailwindcss/src/utilities.ts`) -> Impact: **782.8** | LOC: 1539
  * *Intent:* // Convert numeric values (like `0.5`) to percentages (like `50%`) so they // work properly with `color-mix`. Assume anything that isn't a number is
- `arbitraryUtilities` (@ `packages/tailwindcss/src/canonicalize-candidates.ts`) -> Impact: **617.5** | LOC: 659
- `matchVariant` (@ `packages/tailwindcss/src/compat/plugin-api.ts`) -> Impact: **609.7** | LOC: 194
- `findStaticPlugins` (@ `packages/@tailwindcss-upgrade/src/utils/extract-static-plugins.ts`) -> Impact: **497.1** | LOC: 142
- `walk` (@ `packages/tailwindcss/src/index.ts`) -> Impact: **458.2** | LOC: 165
  * *Intent:* // Handle at-rules
- `parseCandidate` (@ `packages/tailwindcss/src/candidate.ts`) -> Impact: **441.6** | LOC: 345
  * *Intent:* /** * Static candidates are candidates that don't take any arguments. *
- `optimizeAst` (@ `packages/tailwindcss/src/ast.ts`) -> Impact: **418.8** | LOC: 215
  * *Intent:* // Optimize the AST for printing where all the special nodes that require custom // handling are handled such that the printing is a 1-to-1 transforma...
- `resolveValue` (@ `packages/tailwindcss/src/compat/plugin-functions.ts`) -> Impact: **357.0** | LOC: 100
- `describe` (@ `packages/tailwindcss/src/walk.test.ts`) -> Impact: **356.4** | LOC: 887

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `build` (@ `crates/ignore/src/types.rs`) -> **O(2^N) [Recursive]**
- `next` (@ `crates/ignore/src/walk.rs`) -> **O(2^N) [Recursive]**
- `visit` (@ `crates/ignore/src/walk.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// Yields only entries which satisfy the given predicate and skips /// descending into directories that do not satisfy the given predicate. /// /// T...
- `build` (@ `crates/ignore/src/walk.rs`) -> **O(2^N) [Recursive]**
- `next` (@ `crates/oxide/src/extractor/candidate_machine.rs`) -> **O(2^N) [Recursive]**
- `next` (@ `crates/oxide/src/extractor/css_variable_machine.rs`) -> **O(2^N) [Recursive]**
- `next` (@ `crates/oxide/src/extractor/modifier_machine.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// /// E.g.: /// /// ```text /// bg-red-500/20 /// ^^^ /// /// bg-red-500/[20%] /// ^^^^^^ /// /// bg-red-500/(--my-opacity) /// ^^^^^^^^^^^^^^^ /// ...
- `next` (@ `crates/oxide/src/extractor/named_utility_machine.rs`) -> **O(2^N) [Recursive]**
- `next` (@ `crates/oxide/src/extractor/named_variant_machine.rs`) -> **O(2^N) [Recursive]**
- `strip` (@ `crates/ignore/src/gitignore.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// Creates a new gitignore matcher from the gitignore file path given. ///

### Highest Data Gravity (Database Complexity)
- `test` (@ `packages/tailwindcss/src/utilities.test.ts`) -> DB Complexity: **212**
- `test` (@ `packages/tailwindcss/src/utilities.test.ts`) -> DB Complexity: **212**
- `test` (@ `packages/tailwindcss/src/utilities.test.ts`) -> DB Complexity: **212**
- `test` (@ `packages/tailwindcss/src/utilities.test.ts`) -> DB Complexity: **212**
- `test` (@ `packages/tailwindcss/src/utilities.test.ts`) -> DB Complexity: **211**
- `test` (@ `packages/tailwindcss/src/utilities.test.ts`) -> DB Complexity: **171**
- `test` (@ `packages/tailwindcss/src/utilities.test.ts`) -> DB Complexity: **171**
- `test` (@ `packages/tailwindcss/src/utilities.test.ts`) -> DB Complexity: **169**
- `test` (@ `packages/tailwindcss/src/utilities.test.ts`) -> DB Complexity: **169**
- `test` (@ `packages/tailwindcss/src/utilities.test.ts`) -> DB Complexity: **169**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `crates/node/npm/wasm32-wasi` | 4 | 5018.16 | 0.0% | 0.0% |
| `packages/tailwindcss/src` | 57 | 3043.88 | 40.99% | 11.82% |
| `crates/ignore/src` | 8 | 2992.3 | 9.39% | 63.19% |
| `crates/oxide/src/extractor` | 15 | 2923.3 | 13.63% | 76.58% |
| `crates/oxide/src/extractor/pre_processors` | 14 | 1356.38 | 14.81% | 55.88% |
| `crates/oxide/src/scanner` | 5 | 822.3 | 13.38% | 33.55% |
| `crates/oxide/src` | 7 | 615.54 | 15.79% | 56.26% |
| `packages/tailwindcss/src/compat` | 24 | 593.58 | 45.31% | 8.57% |
| `scripts` | 6 | 498.54 | 68.33% | 20.35% |
| `crates/oxide/tests` | 1 | 259.44 | 3.21% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `playgrounds/v3/scripts/upgrade.mjs` -> **100.0%** Exposure
- `packages/@tailwindcss-node/src/require-cache.cts` -> **100.0%** Exposure
- `packages/@tailwindcss-postcss/src/index.cts` -> **100.0%** Exposure
- `packages/@tailwindcss-upgrade/src/utils/renderer.ts` -> **100.0%** Exposure
- `packages/tailwindcss/src/css-parser.bench.ts` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `scripts/lock-pre-release-versions.mjs` -> **100.0%** Exposure
- `scripts/pack-packages.mjs` -> **100.0%** Exposure
- `scripts/release-channel.js` -> **100.0%** Exposure
- `scripts/release-notes.mjs` -> **100.0%** Exposure
- `scripts/version-packages.mjs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/tailwindcss/src/utilities.test.ts` -> **0** Orphaned Functions | **249** Duplicates
- `packages/tailwindcss/src/candidate.test.ts` -> **0** Orphaned Functions | **73** Duplicates
- `packages/tailwindcss/src/variants.test.ts` -> **0** Orphaned Functions | **72** Duplicates
- `packages/tailwindcss/src/utilities.ts` -> **0** Orphaned Functions | **63** Duplicates
- `packages/tailwindcss/src/compat/config.test.ts` -> **0** Orphaned Functions | **27** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`packages/@tailwindcss-upgrade/src/codemods/config/migrate-postcss.ts`** -> AI Confidence: **99.39%**
2. **`packages/@tailwindcss-postcss/src/index.ts`** -> AI Confidence: **99.35%**
3. **`packages/tailwindcss/src/compat/plugin-functions.ts`** -> AI Confidence: **99.34%**
4. **`packages/tailwindcss/src/css-parser.ts`** -> AI Confidence: **99.32%**
5. **`crates/ignore/src/pathutil.rs`** -> AI Confidence: **99.31%**
6. **`crates/oxide/src/extractor/pre_processors/ruby.rs`** -> AI Confidence: **99.31%**
7. **`integrations/utils.ts`** -> AI Confidence: **99.31%**
8. **`packages/@tailwindcss-standalone/src/index.ts`** -> AI Confidence: **99.31%**
9. **`packages/@tailwindcss-upgrade/src/codemods/config/migrate-js-config.ts`** -> AI Confidence: **99.31%**
10. **`packages/@tailwindcss-upgrade/src/codemods/css/analyze.ts`** -> AI Confidence: **99.31%**
11. **`packages/@tailwindcss-upgrade/src/codemods/css/migrate-missing-layers.ts`** -> AI Confidence: **99.31%**
12. **`packages/@tailwindcss-upgrade/src/codemods/css/migrate-preflight.ts`** -> AI Confidence: **99.31%**
13. **`packages/@tailwindcss-upgrade/src/codemods/css/migrate-tailwind-directives.ts`** -> AI Confidence: **99.31%**
14. **`packages/@tailwindcss-upgrade/src/codemods/template/migrate-theme-to-var.ts`** -> AI Confidence: **99.31%**
15. **`packages/@tailwindcss-vite/src/index.ts`** -> AI Confidence: **99.31%**
16. **`packages/@tailwindcss-webpack/src/index.ts`** -> AI Confidence: **99.31%**
17. **`packages/tailwindcss/src/apply.ts`** -> AI Confidence: **99.31%**
18. **`packages/tailwindcss/src/ast.ts`** -> AI Confidence: **99.31%**
19. **`packages/tailwindcss/src/candidate.ts`** -> AI Confidence: **99.31%**
20. **`packages/tailwindcss/src/canonicalize-candidates.ts`** -> AI Confidence: **99.31%**
21. **`packages/tailwindcss/src/compat/apply-compat-hooks.ts`** -> AI Confidence: **99.31%**
22. **`packages/tailwindcss/src/compat/config/resolve-config.ts`** -> AI Confidence: **99.31%**
23. **`packages/tailwindcss/src/compat/plugin-api.ts`** -> AI Confidence: **99.31%**
24. **`packages/tailwindcss/src/compile.ts`** -> AI Confidence: **99.31%**
25. **`packages/tailwindcss/src/css-functions.ts`** -> AI Confidence: **99.31%**
26. **`packages/tailwindcss/src/index.ts`** -> AI Confidence: **99.31%**
27. **`packages/tailwindcss/src/intellisense.ts`** -> AI Confidence: **99.31%**
28. **`packages/tailwindcss/src/attribute-selector-parser.ts`** -> AI Confidence: **99.29%**
29. **`packages/tailwindcss/src/utils/brace-expansion.ts`** -> AI Confidence: **99.29%**
30. **`packages/tailwindcss/src/utils/decode-arbitrary-value.ts`** -> AI Confidence: **99.29%**
31. **`packages/tailwindcss/src/utils/escape.ts`** -> AI Confidence: **99.29%**
32. **`packages/tailwindcss/src/utils/is-valid-arbitrary.ts`** -> AI Confidence: **99.29%**
33. **`packages/tailwindcss/src/utils/math-operators.ts`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `crates/ignore/tests/gitignore_matched_path_or_any_parents_tests.rs` -> **0.0001%** Exposure
### Exploit Generation Surface
- `scripts/version-packages.mjs` -> **100.0%** Exposure
- `integrations/utils.ts` -> **100.0%** Exposure
- `packages/@tailwindcss-postcss/src/index.ts` -> **100.0%** Exposure
- `packages/@tailwindcss-upgrade/src/codemods/css/analyze.ts` -> **100.0%** Exposure
- `packages/@tailwindcss-upgrade/src/codemods/css/migrate-preflight.ts` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `scripts/lock-pre-release-versions.mjs` -> **100.0%** Exposure
- `scripts/version-packages.mjs` -> **100.0%** Exposure
- `integrations/utils.ts` -> **100.0%** Exposure
- `packages/tailwindcss/src/compat/apply-config-to-theme.test.ts` -> **100.0%** Exposure
- `packages/@tailwindcss-upgrade/src/utils/extract-static-plugins.ts` -> **84.9493%** Exposure
### Algorithmic DoS Exposure
- `crates/classification-macros/src/lib.rs` -> **100.0%** Exposure
- `crates/ignore/examples/walk.rs` -> **100.0%** Exposure
- `crates/ignore/src/dir.rs` -> **100.0%** Exposure
- `crates/ignore/src/gitignore.rs` -> **100.0%** Exposure
- `crates/ignore/src/lib.rs` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1003` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `integrations/utils.ts` (TYPESCRIPT) -> Cumulative Risk: **989.52**
- **Archetype:** `file_cluster_4` (Distance: 13.277 IQR)
- **Magnitude:** 159.03 | **LOC:** 697 | **CtrlFlow:** 48.5% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `async` (Impact: 932.5), `overwriteVersionsInPackageJson` (Impact: 31.8), `candidate` (Impact: 5.7)

### 2. `packages/@tailwindcss-upgrade/src/codemods/css/analyze.ts` (TYPESCRIPT) -> Cumulative Risk: **817.46**
- **Archetype:** `file_cluster_4` (Distance: 12.588 IQR)
- **Magnitude:** 37.33 | **LOC:** 301 | **CtrlFlow:** 59.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `import` (Impact: 201.6), `pathToString` (Impact: 18.9), `analyze` (Impact: 7.2)

### 3. `packages/@tailwindcss-upgrade/src/codemods/css/sort-buckets.ts` (TYPESCRIPT) -> Cumulative Risk: **815.92**
- **Archetype:** `file_cluster_4` (Distance: 12.397 IQR)
- **Magnitude:** 20.85 | **LOC:** 162 | **CtrlFlow:** 53.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Concurrency (99.9993%)
- **Heaviest Functions:** `sortBuckets` (Impact: 127.6), `distance` (Impact: 19.6)

### 4. `scripts/version-packages.mjs` (JAVASCRIPT) -> Cumulative Risk: **799.81**
- **Archetype:** `file_cluster_4` (Distance: 12.339 IQR)
- **Magnitude:** 222.92 | **LOC:** 179 | **CtrlFlow:** 29.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `async` (Impact: 75.5)

### 5. `packages/@tailwindcss-vite/src/index.ts` (TYPESCRIPT) -> Cumulative Risk: **797.37**
- **Archetype:** `file_cluster_4` (Distance: 13.254 IQR)
- **Magnitude:** 44.88 | **LOC:** 632 | **CtrlFlow:** 59.3% | **Authorship Centralization:** 20.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `createRoot` (Impact: 63.1), `handler` (Impact: 49.6), `configResolved` (Impact: 11.1)

### 6. `packages/@tailwindcss-upgrade/src/codemods/config/migrate-postcss.ts` (TYPESCRIPT) -> Cumulative Risk: **794.18**
- **Archetype:** `file_cluster_4` (Distance: 13.114 IQR)
- **Magnitude:** 50.31 | **LOC:** 350 | **CtrlFlow:** 71.4% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `isTailwindCSSNestingPlugin` (Impact: 128.8), `migratePostCSSConfig` (Impact: 116.7), `isTailwindCSSPlugin` (Impact: 20.4)

### 7. `packages/@tailwindcss-upgrade/src/codemods/css/migrate-import.ts` (TYPESCRIPT) -> Cumulative Risk: **782.97**
- **Archetype:** `file_cluster_4` (Distance: 13.218 IQR)
- **Magnitude:** 8.72 | **LOC:** 53 | **CtrlFlow:** 34.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `migrateImport` (Impact: 40.4)

### 8. `packages/tailwindcss/src/theme.ts` (TYPESCRIPT) -> Cumulative Risk: **772.43**
- **Archetype:** `file_cluster_13` (Distance: 13.086 IQR)
- **Magnitude:** 49.69 | **LOC:** 305 | **CtrlFlow:** 51.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `add` (Impact: 41.6), `clearNamespace` (Impact: 39.0), `namespace` (Impact: 37.3)

### 9. `scripts/lock-pre-release-versions.mjs` (JAVASCRIPT) -> Cumulative Risk: **757.57**
- **Archetype:** `file_cluster_4` (Distance: 13.39 IQR)
- **Magnitude:** 116.32 | **LOC:** 61 | **CtrlFlow:** 48.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `exec` (Impact: 79.8)

### 10. `packages/tailwindcss/src/compat/plugin-api.ts` (TYPESCRIPT) -> Cumulative Risk: **755.48**
- **Archetype:** `file_cluster_13` (Distance: 13.229 IQR)
- **Magnitude:** 108.54 | **LOC:** 637 | **CtrlFlow:** 63.8% | **Authorship Centralization:** 55.6%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9992%)
- **Heaviest Functions:** `matchVariant` (Impact: 609.7), `objectToAst` (Impact: 134.4), `addVariant` (Impact: 119.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `crates/node/npm/wasm32-wasi/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/ignore/src/walk.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 15.137 IQR)
- **Top Global Matches:** file_cluster_0: 15.137, file_cluster_4: 15.195, file_cluster_13: 15.222
- **Magnitude:** 1447.98 | **LOC:** 2482 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (26.0719%), Tech Debt (96.4522%)
**Top Internal Functions/Classes:**
  * `next` (Impact: 213.3 | O(2^N) | DB: 2)
  * `visit` (Impact: 185.6 | O(2^N) | DB: 9)
    * *Intent:* /// Yields only entries which satisfy the given predicate and skips /// descending into directories ...
  * `build` (Impact: 111.6 | O(2^N) | DB: 1)
  * `next` (Impact: 71.3 | O(2^N) | DB: 1)
    * *Intent:* /// Enables reading a global gitignore file, whose path is specified in /// git's `core.excludesFile...
  * `skip_entry` (Impact: 45.1 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 149`, `structural_boundaries: 248`, `args: 100`, `func_start: 75`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 107`, `dead_code: 10`, `duplicate_logic: 24`
* *Architecture:* `io: 1`, `api: 46`, `concurrency: 68`, `import: 13`
* *Defense:* `safety: 257`, `doc: 478`, `test: 2`, `sync_locks: 1`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` io, WalkBuilder, std::os::unix::fs::symlink, PathBuf, walkdir::DirEntryExt, std::ffi::OsStr, Mutex, std::
    cmp::Ordering...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tailwindcss/src/utilities.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.147 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.349 IQR)
- **Top Global Matches:** file_cluster_8: 12.147, file_cluster_4: 12.358, file_cluster_0: 12.408
- **Magnitude:** 1221.4 | **LOC:** 29983 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 212
- **Risk Profile:** Cognitive Load (44.9717%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 77.8 | O(N^1))
  * `test` (Impact: 77.8 | O(N^1))
  * `test` (Impact: 61.4 | O(N^2))
  * `test` (Impact: 58.0 | O(N^2) | DB: 147)
  * `test` (Impact: 41.8 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 184`, `structural_boundaries: 8104`, `args: 911`, `func_start: 984`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 7329`, `fragile_debt: 1`, `duplicate_logic: 249`
* *Architecture:* `io: 6`, `concurrency: 2440`, `import: 4`
* *Defense:* `safety: 97`, `test: 984`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` , vitest, utilities, run
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/ignore/src/dir.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.94 IQR)
- **Top Global Matches:** file_cluster_0: 12.94, file_cluster_16: 12.985, file_cluster_8: 13.027
- **Magnitude:** 463.94 | **LOC:** 1270 | **CtrlFlow:** 32.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (12.346%), Tech Debt (96.2117%)
**Top Internal Functions/Classes:**
  * `matched` (Impact: 136.2 | O(2^N) | DB: 2)
  * `create_gitignore` (Impact: 47.4 | O(N^3) | DB: 15)
  * `build_with_cwd` (Impact: 32.3 | O(N^4) | DB: 1)
    * *Intent:* // Match against the override patterns. If an override matches // regardless of whether it's whiteli...
  * `add_parents` (Impact: 22.3 | O(N^4))
  * `next` (Impact: 10.4 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 155`, `args: 63`, `func_start: 52`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 72`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 8`, `orphaned_logic: 4`
* *Architecture:* `io: 4`, `api: 21`, `import: 3`
* *Defense:* `safety: 56`, `doc: 191`, `test: 92`, `sync_locks: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::
    collections::HashMap, Match, types::self, Error, crate::Error, PathBuf, tests::TempDir, io::self...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/ignore/src/types.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.564 IQR)
- **Top Global Matches:** file_cluster_13: 12.564, file_cluster_0: 12.567, file_cluster_16: 12.672
- **Magnitude:** 443.2 | **LOC:** 602 | **CtrlFlow:** 31.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (9.1764%), Tech Debt (40.2578%)
**Top Internal Functions/Classes:**
  * `build` (Impact: 87.0 | O(2^N) | DB: 3)
  * `add_def` (Impact: 68.4 | O(N^6) | DB: 1)
    * *Intent:* /// Add a new file type definition specified in string form. There are two /// valid formats: /// 1....
  * `add_defaults` (Impact: 24.6 | O(N^5) | DB: 2)
  * `select` (Impact: 21.4 | O(N^5) | DB: 2)
    * *Intent:* /// Select the file type given by `name`.
  * `negate` (Impact: 21.4 | O(N^5) | DB: 2)
    * *Intent:* /// Ignore the file type given by `name`.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 122`, `args: 37`, `func_start: 22`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 59`, `dead_code: 3`, `duplicate_logic: 4`
* *Architecture:* `api: 24`, `import: 8`
* *Defense:* `safety: 43`, `doc: 85`, `test: 14`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` default_types::DEFAULT_TYPES, globset::GlobBuilder, crate::Error, Match, super::TypesBuilder, sync::Arc, ignore::types::TypesBuilder, GlobSetBuilder...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/oxide/src/extractor/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.774 IQR)
- **Top Global Matches:** file_cluster_8: 10.774, file_cluster_13: 10.861, file_cluster_0: 10.958
- **Magnitude:** 398.94 | **LOC:** 1138 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (18.1065%), Tech Debt (39.6059%)
**Top Internal Functions/Classes:**
  * `extract` (Impact: 73.4 | O(N^6) | DB: 7)
  * `extract_variables_from_css` (Impact: 55.7 | O(N^5) | DB: 3)
  * `extract_sub_candidates` (Impact: 34.7 | O(N^5) | DB: 4)
    * *Intent:* // Extract sub-candidates from a given range. // // E.g.: `[ClassPrefix('gap-y-4')]` will not be a v...
  * `fmt` (Impact: 21.5 | O(2^N) | DB: 1)
  * `drop_covered_spans` (Impact: 18.8 | O(N^3) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 95`, `args: 21`, `func_start: 15`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 2`, `state_mutation: 64`, `planned_debt: 1`, `orphaned_logic: 5`
* *Architecture:* `api: 19`, `import: 10`
* *Defense:* `safety: 12`, `doc: 8`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` css_variable_machine::CssVariableMachine, super::Extracted, machine::Machine, crate::extractor::machine::Span, crate::throughput::Throughput, std::hint::black_box, MachineState, candidate_machine::CandidateMachine...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/oxide/src/scanner/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.061 IQR)
- **Top Global Matches:** file_cluster_13: 12.061, file_cluster_0: 12.212, file_cluster_16: 12.434
- **Magnitude:** 373.22 | **LOC:** 896 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (15.6272%), Tech Debt (19.2727%)
**Top Internal Functions/Classes:**
  * `discover_sources` (Impact: 270.1 | O(N^6) | DB: 12)
  * `get_globs` (Impact: 25.8 | O(N^5) | DB: 2)
  * `get_normalized_sources` (Impact: 9.5 | O(N^4))
  * `get_candidates_with_positions` (Impact: 5.7 | O(N^4) | DB: 1)
  * `get_files` (Impact: 3.5 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 73`, `args: 14`, `func_start: 6`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 36`, `dead_code: 1`, `orphaned_logic: 3`
* *Architecture:* `io: 1`, `api: 17`, `import: 19`
* *Defense:* `safety: 28`, `doc: 23`, `test: 3`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` WalkBuilder, init_tracing::init_tracing, FxHashSet, PathBuf, Mutex, Extractor, fast_glob::glob_match, std::sync::Arc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/oxide/src/extractor/candidate_machine.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.14 IQR)
- **Top Global Matches:** file_cluster_0: 11.14, file_cluster_13: 11.182, file_cluster_8: 11.455
- **Magnitude:** 350.0 | **LOC:** 362 | **CtrlFlow:** 39.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (28.9156%), Tech Debt (44.3425%)
**Top Internal Functions/Classes:**
  * `next` (Impact: 310.2 | O(2^N) | DB: 6)
  * `test_candidate_extraction` (Impact: 8.9 | O(N^3))
  * `test_candidate_machine_performance` (Impact: 2.4 | O(N^1))
  * `reset` (Impact: 2.2 | O(N^1) | DB: 1)
  * `done_span` (Impact: 2.0 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 40`, `args: 10`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 20`, `dead_code: 1`, `planned_debt: 1`, `orphaned_logic: 2`
* *Architecture:* `api: 1`, `import: 9`
* *Defense:* `safety: 14`, `doc: 3`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::CandidateMachine, crate::extractor::boundary::has_valid_boundaries, is_valid_before_boundary, MachineState, crate::extractor::machine::Machine, crate::extractor::Span, pretty_assertions::assert_eq, crate::cursor...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/oxide/src/extractor/pre_processors/haml.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.606 IQR)
- **Top Global Matches:** file_cluster_8: 9.606, file_cluster_13: 9.878, file_cluster_0: 10.041
- **Magnitude:** 348.84 | **LOC:** 467 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (27.1337%), Tech Debt (56.9001%)
**Top Internal Functions/Classes:**
  * `skip_indented_block` (Impact: 185.0 | O(N^6) | DB: 2)
    * *Intent:* // If the dot is surrounded by digits, we want to keep it. E.g.: `px-2.5` // EXCEPT if it's followed...
  * `process` (Impact: 111.8 | O(N^6) | DB: 11)
  * `test_haml_pre_processor` (Impact: 8.9 | O(N^3))
  * `test_strings_only_occur_when_nested` (Impact: 4.7 | O(N^3))
  * `test_arbitrary_code_followed_by_classes` (Impact: 3.0 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 56`, `args: 11`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 23`, `orphaned_logic: 7`
* *Architecture:* `api: 1`, `import: 10`
* *Defense:* `safety: 3`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::scanner::pre_process_input, super::Haml, MachineState, crate::extractor::variant_machine::VariantMachine, crate::extractor::machine::Machine, bstr::ByteVec, pretty_assertions::assert_eq, crate::cursor...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/oxide/src/extractor/arbitrary_variable_machine.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.304 IQR)
- **Top Global Matches:** file_cluster_0: 11.304, file_cluster_13: 11.461, file_cluster_16: 11.501
- **Magnitude:** 336.24 | **LOC:** 414 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (11.0349%), Tech Debt (99.9972%)
**Top Internal Functions/Classes:**
  * `next` (Impact: 143.3 | O(2^N) | DB: 2)
  * `next` (Impact: 53.6 | O(2^N) | DB: 2)
    * *Intent:* // End of an arbitrary variable, must be followed by `)`
  * `next` (Impact: 44.8 | O(2^N) | DB: 2)
    * *Intent:* #[inline(always)]
  * `next` (Impact: 43.2 | O(2^N) | DB: 2)
  * `reset` (Impact: 4.2 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 46`, `args: 12`, `func_start: 12`, `class_start: 5`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 28`, `planned_debt: 1`, `duplicate_logic: 8`
* *Architecture:* `api: 5`, `import: 10`
* *Defense:* `safety: 10`, `doc: 31`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::marker::PhantomData, classification_macros::ClassifyBytes, super::ArbitraryVariableMachine, machine::Machine, MachineState, crate::extractor::css_variable_machine::CssVariableMachine, crate::extractor::string_machine::StringMachine, crate::extractor::machine::Machine...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/oxide/src/extractor/named_utility_machine.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.871 IQR)
- **Top Global Matches:** file_cluster_0: 9.871, file_cluster_8: 9.871, file_cluster_13: 10.071
- **Magnitude:** 328.6 | **LOC:** 536 | **CtrlFlow:** 31.7% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (10.4211%), Tech Debt (96.641%)
**Top Internal Functions/Classes:**
  * `next` (Impact: 204.6 | O(2^N) | DB: 2)
  * `next` (Impact: 63.4 | O(2^N) | DB: 2)
  * `test_named_utility_extraction` (Impact: 23.7 | O(N^4) | DB: 2)
    * *Intent:* #[test] #[ignore]
  * `transition` (Impact: 3.0 | O(N^2))
  * `reset` (Impact: 2.2 | O(N^1) | DB: 1)
    * *Intent:* // Everything else, is not a valid start of the utility.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 56`, `args: 21`, `func_start: 7`, `class_start: 4`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 18`, `planned_debt: 1`, `duplicate_logic: 4`, `orphaned_logic: 2`
* *Architecture:* `api: 3`, `import: 10`
* *Defense:* `safety: 8`, `doc: 12`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::marker::PhantomData, super::IdleState, classification_macros::ClassifyBytes, crate::extractor::arbitrary_value_machine::ArbitraryValueMachine, NamedUtilityMachine, MachineState, crate::extractor::machine::Machine, crate::extractor::arbitrary_variable_machine::ArbitraryVariableMachine...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tailwindcss/src/utilities.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.267 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.152 IQR)
- **Top Global Matches:** file_cluster_8: 13.267, file_cluster_7: 13.637, file_cluster_13: 13.637
- **Magnitude:** 301.39 | **LOC:** 6690 | **CtrlFlow:** 38.8% | **Authorship Centralization:** 36.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 169
- **Risk Profile:** Cognitive Load (62.1764%), Tech Debt (94.5406%)
**Top Internal Functions/Classes:**
  * `replaceAlpha` (Impact: 782.8 | O(N^4) | DB: 169)
    * *Intent:* // Convert numeric values (like `0.5`) to percentages (like `50%`) so they // work properly with `co...
  * `staticUtility` (Impact: 134.1 | O(N^4) | DB: 11)
  * `staticUtility` (Impact: 122.6 | O(N^4) | DB: 11)
  * `staticUtility` (Impact: 114.6 | O(N^3) | DB: 9)
  * `inferDataType` (Impact: 114.5 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 478`, `structural_boundaries: 754`, `args: 839`, `func_start: 882`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 798`, `duplicate_logic: 63`
* *Architecture:* `api: 7`, `import: 14`
* *Defense:* `safety: 34`, `doc: 47`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` segment, replace-shadow-colors, walk, default-map, value-parser, theme, feature-flags, compare-breakpoints...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/oxide/src/extractor/arbitrary_property_machine.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.938 IQR)
- **Top Global Matches:** file_cluster_0: 10.938, file_cluster_16: 11.114, file_cluster_13: 11.12
- **Magnitude:** 292.76 | **LOC:** 458 | **CtrlFlow:** 32.9% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (9.8676%), Tech Debt (99.9531%)
**Top Internal Functions/Classes:**
  * `next` (Impact: 107.1 | O(2^N) | DB: 2)
  * `next` (Impact: 45.3 | O(2^N) | DB: 2)
  * `test_arbitrary_property_machine_extracti` (Impact: 31.1 | O(N^4))
  * `next` (Impact: 21.5 | O(2^N) | DB: 2)
    * *Intent:* #[inline(always)]
  * `parse_property_variable` (Impact: 16.5 | O(N^5) | DB: 2)
    * *Intent:* // End of the property name, but there must be at least a single character
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 55`, `args: 14`, `func_start: 12`, `class_start: 5`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 31`, `planned_debt: 1`, `duplicate_logic: 6`, `orphaned_logic: 3`
* *Architecture:* `api: 4`, `import: 10`
* *Defense:* `safety: 8`, `doc: 28`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::marker::PhantomData, classification_macros::ClassifyBytes, crate::extractor::CssVariableMachine, MachineState, crate::extractor::string_machine::StringMachine, IdleState, crate::extractor::machine::Machine, pretty_assertions::assert_eq...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/oxide/src/extractor/named_variant_machine.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.457 IQR)
- **Top Global Matches:** file_cluster_0: 11.457, file_cluster_13: 11.635, file_cluster_16: 11.641
- **Magnitude:** 277.5 | **LOC:** 423 | **CtrlFlow:** 31.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (10.5033%), Tech Debt (99.9964%)
**Top Internal Functions/Classes:**
  * `next` (Impact: 127.5 | O(2^N) | DB: 2)
  * `next` (Impact: 36.8 | O(2^N) | DB: 2)
    * *Intent:* #[inline(always)]
  * `next` (Impact: 26.9 | O(2^N) | DB: 2)
  * `test_named_variant_extraction` (Impact: 12.3 | O(N^3))
  * `next` (Impact: 8.4 | O(N^2) | DB: 2)
    * *Intent:* // Modifier must be followed by a `:` //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 50`, `args: 18`, `func_start: 12`, `class_start: 6`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 34`, `planned_debt: 1`, `duplicate_logic: 8`, `orphaned_logic: 2`
* *Architecture:* `api: 5`, `import: 10`
* *Defense:* `safety: 12`, `doc: 33`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::marker::PhantomData, super::IdleState, classification_macros::ClassifyBytes, crate::extractor::modifier_machine::ModifierMachine, crate::extractor::arbitrary_value_machine::ArbitraryValueMachine, NamedVariantMachine, MachineState, crate::extractor::machine::Machine...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/ignore/src/lib.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.037 IQR)
- **Top Global Matches:** file_cluster_16: 13.037, file_cluster_8: 13.111, file_cluster_13: 13.141
- **Magnitude:** 266.54 | **LOC:** 561 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (9.5496%), Tech Debt (55.5702%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 52.9 | O(2^N) | DB: 3)
  * `clone` (Impact: 27.7 | O(2^N) | DB: 6)
  * `is_io` (Impact: 21.4 | O(2^N))
  * `into_error_option` (Impact: 20.4 | O(N^3) | DB: 1)
  * `is_partial` (Impact: 14.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 66`, `args: 15`, `func_start: 17`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 20`, `orphaned_logic: 7`
* *Architecture:* `io: 5`, `api: 18`, `concurrency: 9`, `import: 4`
* *Defense:* `safety: 48`, `doc: 97`, `test: 1`, `sync_locks: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Walk, ignore::Walk, WalkBuilder, std::path::Path, fs, ignore::WalkBuilder, PathBuf, std::sync::atomic::AtomicUsize...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/oxide/tests/scanner.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.218 IQR)
- **Top Global Matches:** file_cluster_8: 8.218, file_cluster_16: 8.571, file_cluster_0: 9.064
- **Magnitude:** 259.44 | **LOC:** 1799 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (3.2099%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `scan_with_globs` (Impact: 37.3 | O(N^5) | DB: 4)
  * `create_files_in` (Impact: 15.7 | O(N^4))
  * `it_should_not_ignore_folders_that_end_wi` (Impact: 9.8 | O(N^4) | DB: 1)
    * *Intent:* // https://github.com/tailwindlabs/tailwindcss/issues/17569
  * `public_source_entry_from_pattern` (Impact: 9.6 | O(N^4) | DB: 1)
  * `skips_ignore_files_outside_of_a_repo` (Impact: 9.4 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 106`, `args: 34`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 20`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 21`, `concurrency: 1`, `import: 8`
* *Defense:* `safety: 1`, `test: 97`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::time::Duration, path, tempfile::tempdir, std::fs, std::path::Path, PathBuf, tailwindcss_oxide::*, pretty_assertions::assert_eq...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/oxide/src/glob.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.876 IQR)
- **Top Global Matches:** file_cluster_8: 9.876, file_cluster_13: 10.242, file_cluster_0: 10.281
- **Magnitude:** 231.96 | **LOC:** 602 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (4.5163%), Tech Debt (76.5493%)
**Top Internal Functions/Classes:**
  * `hoist_static_glob_parts` (Impact: 65.0 | O(N^5) | DB: 1)
  * `split_pattern` (Impact: 33.5 | O(N^3) | DB: 1)
    * *Intent:* // // Assumption: we assume that all globs are expanded, which means that the only dynamic parts are...
  * `optimize_patterns` (Impact: 23.1 | O(N^6) | DB: 4)
    * *Intent:* /// ```sh /// tailwind --pwd ./project --content "{pages,components}/**/*.js" /// ``` /// Then the g...
  * `create_folders` (Impact: 16.1 | O(N^4))
  * `test` (Impact: 14.5 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 82`, `args: 22`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 16`, `planned_debt: 2`, `orphaned_logic: 10`
* *Architecture:* `api: 6`, `import: 10`
* *Defense:* `safety: 22`, `doc: 25`, `test: 32`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::optimize_patterns, bexpand::Expression, path, tempfile::tempdir, std::fs, tracing::event, FxHashSet, fxhash::FxHashMap...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/ignore/src/gitignore.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.88 IQR)
- **Top Global Matches:** file_cluster_0: 12.88, file_cluster_16: 12.901, file_cluster_13: 12.955
- **Magnitude:** 228.88 | **LOC:** 869 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (4.458%), Tech Debt (8.9159%)
**Top Internal Functions/Classes:**
  * `strip` (Impact: 49.0 | O(2^N) | DB: 1)
    * *Intent:* /// Creates a new gitignore matcher from the gitignore file path given. ///
  * `build_global` (Impact: 36.0 | O(N^6) | DB: 2)
  * `add` (Impact: 27.1 | O(N^5) | DB: 5)
    * *Intent:* /// Returns whether the given path (file or directory, and expected to be /// under the root) or any...
  * `build` (Impact: 21.7 | O(2^N))
    * *Intent:* /// Returns the directory containing this gitignore matcher. ///
  * `gitconfig_excludes_path` (Impact: 18.1 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 40`, `args: 30`, `func_start: 23`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 15`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 15`, `import: 5`
* *Defense:* `safety: 35`, `doc: 162`, `test: 16`, `sync_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BufReader, Match, PathBuf, io::BufRead, GlobBuilder, sync::Arc, PartialErrorBuilder, path::Path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/version-packages.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.339 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.703 IQR)
- **Top Global Matches:** file_cluster_4: 12.339, file_cluster_17: 12.971, file_cluster_13: 12.982
- **Magnitude:** 222.92 | **LOC:** 179 | **CtrlFlow:** 29.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 78
- **Risk Profile:** Cognitive Load (99.9782%), Tech Debt (22.0917%)
**Top Internal Functions/Classes:**
  * `async` (Impact: 75.5 | O(N^3) | DB: 78)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 53`, `args: 8`, `func_start: 3`
* *Risk/State:* `state_mutation: 68`, `orphaned_logic: 1`
* *Architecture:* `io: 23`, `concurrency: 77`, `import: 7`
* *Defense:* `safety: 7`, `immutability_locks: 5`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:child_process, prettier, node:os, node:url, node:crypto, promises, node:path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/oxide/src/scanner/sources.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.463 IQR)
- **Top Global Matches:** file_cluster_16: 11.463, file_cluster_8: 11.543, file_cluster_13: 11.593
- **Magnitude:** 218.38 | **LOC:** 310 | **CtrlFlow:** 41.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (5.4498%), Tech Debt (99.8327%)
**Top Internal Functions/Classes:**
  * `optimize` (Impact: 108.5 | O(N^6) | DB: 1)
  * `from` (Impact: 41.6 | O(2^N))
  * `public_source_entries_to_private_source_` (Impact: 12.1 | O(N^5) | DB: 1)
  * `from` (Impact: 10.8 | O(N^4))
  * `from` (Impact: 10.8 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 34`, `args: 14`, `func_start: 8`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 4`, `planned_debt: 1`, `duplicate_logic: 4`, `orphaned_logic: 1`
* *Architecture:* `api: 10`, `import: 6`
* *Defense:* `safety: 19`, `doc: 78`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` bexpand::Expression, super::auto_source_detection::IGNORED_CONTENT_DIRS, tracing::event, Level, crate::glob::split_pattern, crate::GlobEntry, std::path::PathBuf
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tailwindcss/src/index.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.131 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.997 IQR)
- **Top Global Matches:** file_cluster_8: 11.131, file_cluster_0: 11.204, file_cluster_4: 11.222
- **Magnitude:** 216.98 | **LOC:** 6301 | **CtrlFlow:** 4.4% | **Authorship Centralization:** 46.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 108
- **Risk Profile:** Cognitive Load (43.1642%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 132.0 | O(N^5) | DB: 108)
  * `describe` (Impact: 53.3 | O(2^N) | DB: 34)
  * `describe` (Impact: 52.6 | O(N^5) | DB: 35)
  * `describe` (Impact: 50.9 | O(N^4) | DB: 38)
  * `describe` (Impact: 37.6 | O(N^4) | DB: 53)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 781`, `args: 457`, `func_start: 445`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 376`, `planned_debt: 1`, `duplicate_logic: 19`
* *Architecture:* `io: 59`, `concurrency: 1174`, `import: 7`
* *Defense:* `safety: 22`, `doc: 5`, `test: 384`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` bar.css, , baz.css, plugin-api, utilities, two.css, three.css, vitest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/oxide/src/scanner/detect_sources.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.305 IQR)
- **Top Global Matches:** file_cluster_13: 11.305, file_cluster_17: 11.379, file_cluster_8: 11.475
- **Magnitude:** 177.78 | **LOC:** 160 | **CtrlFlow:** 41.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (24.2256%), Tech Debt (16.4818%)
**Top Internal Functions/Classes:**
  * `resolve_globs` (Impact: 154.0 | O(N^5) | DB: 7)
  * `sort_by_dir_and_name` (Impact: 5.5 | O(N^2))
    * *Intent:* // Sorting to make sure that we always see the directories before the files. Also sorting // alphabe...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 33`, `args: 9`, `func_start: 2`
* *Risk/State:* `state_mutation: 15`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `import: 9`
* *Defense:* `safety: 12`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::scanner::auto_source_detection::IGNORED_CONTENT_DIRS, fxhash::FxHashSet, globwalk::DirEntry, std::cmp::Ordering, walkdir::WalkDir, crate::GlobEntry, std::path::PathBuf, std::sync
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/oxide/src/extractor/modifier_machine.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.586 IQR)
- **Top Global Matches:** file_cluster_0: 10.586, file_cluster_13: 10.619, file_cluster_8: 10.733
- **Magnitude:** 170.2 | **LOC:** 168 | **CtrlFlow:** 38.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (8.7143%), Tech Debt (86.7036%)
**Top Internal Functions/Classes:**
  * `next` (Impact: 148.8 | O(2^N) | DB: 2)
    * *Intent:* /// /// E.g.: /// /// ```text /// bg-red-500/20 /// ^^^ /// /// bg-red-500/[20%] /// ^^^^^^ /// /// ...
  * `test_modifier_extraction` (Impact: 6.7 | O(N^2))
    * *Intent:* #[test] #[ignore]
  * `test_modifier_machine_performance` (Impact: 2.2 | O(N^1))
    * *Intent:* #[fallback]
  * `reset` (Impact: 2.1 | O(N^1) | DB: 1)
    * *Intent:* /// Extract modifiers from an input including the `/`. /// /// E.g.: /// /// ```text /// bg-red-500/...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 21`, `args: 5`, `func_start: 4`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 7`, `planned_debt: 1`, `orphaned_logic: 3`
* *Architecture:* `api: 1`, `import: 8`
* *Defense:* `safety: 5`, `doc: 14`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` classification_macros::ClassifyBytes, crate::extractor::arbitrary_value_machine::ArbitraryValueMachine, MachineState, crate::extractor::machine::Machine, crate::extractor::arbitrary_variable_machine::ArbitraryVariableMachine, pretty_assertions::assert_eq, crate::cursor, super::ModifierMachine
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/oxide/src/cursor.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_16` (Drift: 9.733 IQR)
- **Top Global Matches:** file_cluster_16: 9.733, file_cluster_8: 9.81, file_cluster_0: 9.848
- **Magnitude:** 164.32 | **LOC:** 135 | **CtrlFlow:** 51.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (13.7512%), Tech Debt (58.1805%)
**Top Internal Functions/Classes:**
  * `fmt` (Impact: 105.4 | O(2^N) | DB: 1)
  * `curr` (Impact: 8.2 | O(N^2))
    * *Intent:* /// The current byte at `pos`, or 0x00 if past the end.
  * `next` (Impact: 8.2 | O(N^2))
    * *Intent:* /// The next byte at `pos + 1`, or 0x00 if past the end.
  * `prev` (Impact: 8.2 | O(N^2))
    * *Intent:* /// The previous byte at `pos - 1`, or 0x00 if at the start.
  * `test_cursor` (Impact: 3.0 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 17`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 6`, `orphaned_logic: 3`
* *Architecture:* `api: 11`, `import: 3`
* *Defense:* `safety: 1`, `doc: 3`, `test: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::ascii::escape_default, super::*, fmt::Display, pretty_assertions::assert_eq
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/oxide/src/extractor/arbitrary_value_machine.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_0` (Drift: 9.642 IQR)
- **Top Global Matches:** file_cluster_0: 9.642, file_cluster_13: 9.749, file_cluster_8: 9.765
- **Magnitude:** 163.76 | **LOC:** 214 | **CtrlFlow:** 35.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (8.0256%), Tech Debt (57.9214%)
**Top Internal Functions/Classes:**
  * `next` (Impact: 139.0 | O(2^N) | DB: 2)
  * `test_arbitrary_value_machine_extraction` (Impact: 7.7 | O(N^3))
  * `reset` (Impact: 4.2 | O(2^N) | DB: 1)
    * *Intent:* /// Track brackets to ensure they are balanced
  * `test_arbitrary_value_machine_performance` (Impact: 2.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 26`, `args: 6`, `func_start: 4`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 7`, `planned_debt: 1`, `orphaned_logic: 2`
* *Architecture:* `api: 1`, `import: 8`
* *Defense:* `safety: 3`, `doc: 12`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` classification_macros::ClassifyBytes, MachineState, crate::extractor::string_machine::StringMachine, crate::extractor::machine::Machine, super::ArbitraryValueMachine, pretty_assertions::assert_eq, crate::cursor, crate::extractor::bracket_stack::BracketStack
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `crates/oxide/src/extractor/named_utility_machine.rs` (RUST) | Magnitude: 328.6 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 294, structural_boundaries: 56, decorators: 31, branch: 26
- `crates/oxide/src/extractor/machine.rs` (RUST) | Magnitude: 128.88 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 113, structural_boundaries: 49, state_mutation: 40, args: 12
- `crates/ignore/src/overrides.rs` (RUST) | Magnitude: 37.6 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 96, doc: 77, test: 50, sec_high_risk_execution: 41
- `crates/oxide/src/extractor/pre_processors/markdown.rs` (RUST) | Magnitude: 55.56 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 64, structural_boundaries: 16, state_mutation: 10, branch: 7
- `crates/ignore/src/gitignore.rs` (RUST) | Magnitude: 228.88 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 260, doc: 162, structural_boundaries: 40, safety: 35

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `packages/tailwindcss/src/apply.ts` (TYPESCRIPT) | Magnitude: 49.0 | Delta: **0.127 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 184, state_mutation: 132, branch: 65, structural_boundaries: 47
- `packages/tailwindcss/src/utils/topological-sort.ts` (TYPESCRIPT) | Magnitude: 6.66 | Delta: **0.282 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 33, indent_spaces: 23, branch: 8, io: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `crates/ignore/src/types.rs` (RUST) | Magnitude: 443.2 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 363, structural_boundaries: 122, doc: 85, state_mutation: 59
- `packages/tailwindcss/src/theme.ts` (TYPESCRIPT) | Magnitude: 49.69 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 224, state_mutation: 218, branch: 71, structural_boundaries: 67
- `packages/@tailwindcss-upgrade/src/codemods/template/migrate-camelcase-in-named-value.ts` (TYPESCRIPT) | Magnitude: 5.18 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 34, branch: 15, structural_boundaries: 11, state_mutation: 9
- `packages/@tailwindcss-browser/src/assets.ts` (TYPESCRIPT) | Magnitude: 1.62 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 5, import: 4, indent_spaces: 4, api: 1
- `packages/@tailwindcss-upgrade/src/codemods/template/migrate-automatic-var-injection.ts` (TYPESCRIPT) | Magnitude: 6.82 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 70, structural_boundaries: 20, state_mutation: 18, branch: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `crates/ignore/tests/gitignore_skip_bom.rs` (RUST) | Magnitude: 3.42 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, indent_spaces: 5, doc: 4, test: 3
- `crates/ignore/src/lib.rs` (RUST) | Magnitude: 266.54 | Delta: **0.074 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 227, doc: 97, structural_boundaries: 66, safety: 48
- `crates/oxide/src/cursor.rs` (RUST) | Magnitude: 164.32 | Delta: **0.077 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 95, branch: 18, structural_boundaries: 17, test: 16
- `crates/oxide/src/scanner/sources.rs` (RUST) | Magnitude: 218.38 | Delta: **0.08 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 164, doc: 78, structural_boundaries: 34, branch: 24
- `packages/tailwindcss/src/compat/config/deep-merge.ts` (TYPESCRIPT) | Magnitude: 9.15 | Delta: **0.114 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 29, state_mutation: 15, branch: 12, structural_boundaries: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/tailwindcss/src/utils/replace-shadow-colors.ts` (TYPESCRIPT) | Magnitude: 4.85 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, state_mutation: 16, branch: 12, structural_boundaries: 5
- `packages/tailwindcss/src/candidate.bench.ts` (TYPESCRIPT) | Magnitude: 11.56 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 22, branch: 21, args: 13
- `packages/tailwindcss/src/compat/screens-config.ts` (TYPESCRIPT) | Magnitude: 13.2 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 75, state_mutation: 39, branch: 28, structural_boundaries: 22
- `packages/tailwindcss/src/sort.ts` (TYPESCRIPT) | Magnitude: 3.52 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 16, indent_spaces: 12, branch: 8, structural_boundaries: 7
- `crates/oxide/fuzz/fuzz_targets/parsing.rs` (RUST) | Magnitude: 15.46 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 7, import: 5, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `playgrounds/vite/src/index.html` (HTML) | Magnitude: 17.24 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 4, decorators: 3, api: 2
- `playgrounds/vite/src/app.tsx` (TYPESCRIPT) | Magnitude: 0.32 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 5, structural_boundaries: 2, args: 2, ui_framework: 2
- `playgrounds/v3/app/page.tsx` (TYPESCRIPT) | Magnitude: 0.3 | Delta: **0.178 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, branch: 1, args: 1, func_start: 1
- `packages/@tailwindcss-postcss/src/fixtures/example-project/index.html` (HTML) | Magnitude: 0.01 | Delta: **0.639 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 1, ui_framework: 1, decorators: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/@tailwindcss-upgrade/src/codemods/css/sort-buckets.ts` (TYPESCRIPT) | Magnitude: 20.85 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 104, state_mutation: 51, branch: 45, structural_boundaries: 39
- `packages/tailwindcss/src/prefix.test.ts` (TYPESCRIPT) | Magnitude: 21.04 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 286, concurrency: 128, structural_boundaries: 42, decorators: 38
- `packages/@tailwindcss-upgrade/src/codemods/template/migrate-legacy-classes.ts` (TYPESCRIPT) | Magnitude: 11.18 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 79, state_mutation: 34, structural_boundaries: 21, branch: 18
- `packages/@tailwindcss-postcss/src/index.ts` (TYPESCRIPT) | Magnitude: 44.96 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 204, state_mutation: 88, branch: 86, structural_boundaries: 37
- `packages/@tailwindcss-upgrade/src/codemods/template/migrate-modernize-arbitrary-values.test.ts` (TYPESCRIPT) | Magnitude: 2.97 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 18, concurrency: 12, import: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `packages/@tailwindcss-upgrade/src/utils/args.ts` (TYPESCRIPT) | Magnitude: 9.88 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 79, branch: 39, structural_boundaries: 39, state_mutation: 18
- `packages/@tailwindcss-upgrade/src/codemods/template/migrate-variant-order.ts` (TYPESCRIPT) | Magnitude: 15.94 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 90, state_mutation: 50, branch: 32, structural_boundaries: 30
- `packages/@tailwindcss-node/src/optimize.ts` (TYPESCRIPT) | Magnitude: 2.04 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 49, structural_boundaries: 16, sec_reflection_metaprogramming: 8, args: 6
- `packages/@tailwindcss-upgrade/src/utils/extract-static-plugins.test.ts` (TYPESCRIPT) | Magnitude: 15.1 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 301, structural_boundaries: 103, func_start: 65, api: 41
- `crates/oxide/src/extractor/utility_machine.rs` (RUST) | Magnitude: 158.28 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 126, state_mutation: 31, structural_boundaries: 24, branch: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `packages/@tailwindcss-postcss/src/postcss-fix-relative-paths/fixtures/example-project/src/index.css` (CSS) | Magnitude: 0.01 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 2, doc: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/tailwindcss/src/utilities.ts` -> Churn: **96.28%** | Cog Load: 62.1764% | Debt: 94.5406%
- `packages/tailwindcss/src/canonicalize-candidates.ts` -> Churn: **95.12%** | Cog Load: 89.4032% | Debt: 0.0%
- `packages/@tailwindcss-vite/src/index.ts` -> Churn: **70.86%** | Cog Load: 92.5986% | Debt: 10.1422%
- `packages/tailwindcss/src/constant-fold-declaration.ts` -> Churn: **52.95%** | Cog Load: 66.5138% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `crates/ignore/src/walk.rs` -> **Jordan Pittman** (100.0% isolated ownership) | Magnitude: 1447.98
- `crates/ignore/src/dir.rs` -> **Jordan Pittman** (100.0% isolated ownership) | Magnitude: 463.94
- `crates/ignore/src/types.rs` -> **Jordan Pittman** (100.0% isolated ownership) | Magnitude: 443.2
- `crates/oxide/src/extractor/mod.rs` -> **Robin Malfait** (100.0% isolated ownership) | Magnitude: 398.94
- `crates/oxide/src/extractor/candidate_machine.rs` -> **Robin Malfait** (100.0% isolated ownership) | Magnitude: 350.0

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/tailwindcss/src/design-system.ts` -> **Severity: 0.652** (Bridge: 0.0065 * Flux: 99.8656%)
- `packages/tailwindcss/src/intellisense.ts` -> **Severity: 0.405** (Bridge: 0.004 * Flux: 100.0%)
- `packages/tailwindcss/src/compat/plugin-api.ts` -> **Severity: 0.382** (Bridge: 0.0038 * Flux: 99.9992%)
- `packages/tailwindcss/src/canonicalize-candidates.ts` -> **Severity: 0.369** (Bridge: 0.0037 * Flux: 100.0%)
- `packages/tailwindcss/src/candidate.ts` -> **Severity: 0.155** (Bridge: 0.0016 * Flux: 99.9302%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/tailwindcss/src/utils/default-map.ts` -> **Severity: 12.582** (Embedded: 0.1405 * Error Risk: 89.5243%)
- `packages/tailwindcss/src/utils/segment.ts` -> **Severity: 9.693** (Embedded: 0.117 * Error Risk: 82.8704%)
- `packages/tailwindcss/src/design-system.ts` -> **Severity: 9.217** (Embedded: 0.1378 * Error Risk: 66.8787%)
- `packages/tailwindcss/src/intellisense.ts` -> **Severity: 7.934** (Embedded: 0.0801 * Error Risk: 99.003%)
- `packages/tailwindcss/src/value-parser.ts` -> **Severity: 7.92** (Embedded: 0.0898 * Error Risk: 88.2289%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/tailwindcss/src/utils/default-map.ts` -> **Severity: 2799.908** (Blast Radius: 35.329 * Doc Risk: 79.2524%)
- `packages/@tailwindcss-upgrade/src/utils/version.ts` -> **Severity: 1215.7** (Blast Radius: 12.157 * Doc Risk: 100.0%)
- `packages/tailwindcss/src/compat/plugin-api.ts` -> **Severity: 1103.062** (Blast Radius: 16.839 * Doc Risk: 65.5064%)
- `packages/tailwindcss/src/value-parser.ts` -> **Severity: 1012.681** (Blast Radius: 21.113 * Doc Risk: 47.9648%)
- `packages/tailwindcss/src/test-utils/run.ts` -> **Severity: 850.152** (Blast Radius: 8.502 * Doc Risk: 99.9943%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
