# ARCHITECTURAL_BRIEF: tailwindcss
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_web/tailwindcss` |
| **Timestamp** | `2026-08-07T04:27:50.524004+00:00` |
| **Scan Duration** | `6.06s` |
| **Git Branch** | `main` |
| **Git Commit** | `d7fc281a0e678bf92f0e82f4ab1b8edfd7cb1675` |
| **Git Remote** | `https://github.com/tailwindlabs/tailwindcss.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 335 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are a Senior Technical Storyteller and Codebase Architect. GitGalaxy has translated the non-visual architecture of this repository into measurable Structural Signatures (regex-derived counts, not an AST or compiler pass). Your job is to weave those signatures into a coherent, factual narrative about how this system is built -- its architecture, design patterns, and complexity -- not to render a verdict.
> 
> **CORE DIRECTIVES:**
> 1. **Narrate the Architecture, Don't Judge the Author:** Frame every observation as a blameless description of the system's physical reality. High Risk Exposure (e.g., Cognitive Load Exposure) describes where the architecture may be drifting into fragile territory, not developer incompetence -- it is a prompt to investigate, never a verdict.
> 2. **The Physical Reality Rule:** Base your narrative strictly on the provided Structural Signatures and the numbers derived from them. Do not hallucinate meaning, and do not restate a heuristic's raw label (e.g. a 'Logic Bomb' or 'O(2^N)' flag) as a confirmed finding of malice or a guaranteed defect -- explain what the signature actually measures, weave it into the story of the file, and let the reader draw their own conclusion.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`. Tell that balance as part of the narrative, not as an isolated alarm.
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
| Dominant Lang | PLAINTEXT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4953 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
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
> **Architectural Drift Z-Score:** `3.883`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 176 | 40.5% |
| file_cluster_13 | 96 | 22.1% |
| file_cluster_4 | 57 | 13.1% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 34.0 | 13.4 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.5 | 46.4 | 52.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 21.0 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 5.3 | 0.0 | 0.0 |
| API Exposure | 0.0 | 19.4 | 3.3 | 2.8 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 23.5 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 56.1 | 78.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 64.6 | 0.8 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 85.8 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 7.1 | 1.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 98.5 | 8.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 20.1 | 14.9 | 0.0 |
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

- `createUtilities` (@ `packages/tailwindcss/src/utilities.ts`) -> Impact: **392.1** | LOC: 1523
- `replaceAlpha` (@ `packages/tailwindcss/src/utilities.ts`) -> Impact: **359.3** | LOC: 1539
  * *Intent:* // Convert numeric values (like `0.5`) to percentages (like `50%`) so they // work properly with `color-mix`. Assume anything that isn't a number is
- `arbitraryUtilities` (@ `packages/tailwindcss/src/canonicalize-candidates.ts`) -> Impact: **266.8** | LOC: 659
- `matchVariant` (@ `packages/tailwindcss/src/compat/plugin-api.ts`) -> Impact: **209.7** | LOC: 194
- `parseCandidate` (@ `packages/tailwindcss/src/candidate.ts`) -> Impact: **187.0** | LOC: 345
  * *Intent:* /** * Static candidates are candidates that don't take any arguments. *
- `optimizeAst` (@ `packages/tailwindcss/src/ast.ts`) -> Impact: **174.0** | LOC: 215
  * *Intent:* // Optimize the AST for printing where all the special nodes that require custom // handling are handled such that the printing is a 1-to-1 transforma...
- `async` (@ `integrations/utils.ts`) -> Impact: **170.4** | LOC: 360
- `findStaticPlugins` (@ `packages/@tailwindcss-upgrade/src/utils/extract-static-plugins.ts`) -> Impact: **147.1** | LOC: 142
- `describe` (@ `packages/tailwindcss/src/compat/config.test.ts`) -> Impact: **146.4** | LOC: 468
- `migrateTheme` (@ `packages/@tailwindcss-upgrade/src/codemods/config/migrate-js-config.ts`) -> Impact: **141.5** | LOC: 191

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `crates/node/npm/wasm32-wasi` | 4 | 5018.16 | 0.0% | 0.0% |
| `packages/tailwindcss/src` | 57 | 3052.59 | 40.5% | 18.92% |
| `crates/ignore/src` | 8 | 1481.8 | 9.34% | 64.2% |
| `crates/oxide/src/extractor` | 15 | 1141.0 | 12.62% | 76.58% |
| `crates/oxide/src/extractor/pre_processors` | 14 | 728.88 | 16.14% | 59.25% |
| `packages/tailwindcss/src/compat` | 24 | 478.32 | 44.56% | 21.68% |
| `scripts` | 6 | 402.74 | 68.33% | 20.35% |
| `crates/oxide/src/scanner` | 5 | 364.4 | 13.07% | 34.78% |
| `crates/oxide/src` | 7 | 346.54 | 15.66% | 56.26% |
| `packages/@tailwindcss-upgrade/src/codemods/css` | 26 | 212.06 | 46.04% | 6.13% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `crates/ignore/src/pathutil.rs` -> **100.0%** Exposure
- `playgrounds/v3/scripts/upgrade.mjs` -> **100.0%** Exposure
- `packages/@tailwindcss-cli/src/commands/help/index.ts` -> **100.0%** Exposure
- `packages/@tailwindcss-node/src/require-cache.cts` -> **100.0%** Exposure
- `packages/@tailwindcss-postcss/src/ast.ts` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `scripts/lock-pre-release-versions.mjs` -> **100.0%** Exposure
- `scripts/pack-packages.mjs` -> **100.0%** Exposure
- `scripts/release-channel.js` -> **100.0%** Exposure
- `scripts/release-notes.mjs` -> **100.0%** Exposure
- `scripts/version-packages.mjs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/tailwindcss/src/utilities.test.ts` -> **0** Orphaned Functions | **321** Duplicates
- `packages/tailwindcss/src/index.test.ts` -> **0** Orphaned Functions | **270** Duplicates
- `packages/tailwindcss/src/utilities.ts` -> **0** Orphaned Functions | **204** Duplicates
- `packages/tailwindcss/src/candidate.test.ts` -> **0** Orphaned Functions | **157** Duplicates
- `packages/tailwindcss/src/css-parser.test.ts` -> **0** Orphaned Functions | **136** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`packages/@tailwindcss-upgrade/src/codemods/config/migrate-postcss.ts`** -> AI Confidence: **99.39%**
2. **`packages/@tailwindcss-postcss/src/index.ts`** -> AI Confidence: **99.35%**
3. **`packages/tailwindcss/src/compat/plugin-functions.ts`** -> AI Confidence: **99.34%**
4. **`packages/tailwindcss/src/css-parser.ts`** -> AI Confidence: **99.32%**
5. **`crates/oxide/src/extractor/pre_processors/ruby.rs`** -> AI Confidence: **99.31%**
6. **`integrations/utils.ts`** -> AI Confidence: **99.31%**
7. **`packages/@tailwindcss-standalone/src/index.ts`** -> AI Confidence: **99.31%**
8. **`packages/@tailwindcss-upgrade/src/codemods/config/migrate-js-config.ts`** -> AI Confidence: **99.31%**
9. **`packages/@tailwindcss-upgrade/src/codemods/css/analyze.ts`** -> AI Confidence: **99.31%**
10. **`packages/@tailwindcss-upgrade/src/codemods/css/migrate-missing-layers.ts`** -> AI Confidence: **99.31%**
11. **`packages/@tailwindcss-upgrade/src/codemods/css/migrate-preflight.ts`** -> AI Confidence: **99.31%**
12. **`packages/@tailwindcss-upgrade/src/codemods/css/migrate-tailwind-directives.ts`** -> AI Confidence: **99.31%**
13. **`packages/@tailwindcss-upgrade/src/codemods/template/migrate-theme-to-var.ts`** -> AI Confidence: **99.31%**
14. **`packages/@tailwindcss-vite/src/index.ts`** -> AI Confidence: **99.31%**
15. **`packages/@tailwindcss-webpack/src/index.ts`** -> AI Confidence: **99.31%**
16. **`packages/tailwindcss/src/apply.ts`** -> AI Confidence: **99.31%**
17. **`packages/tailwindcss/src/ast.ts`** -> AI Confidence: **99.31%**
18. **`packages/tailwindcss/src/candidate.ts`** -> AI Confidence: **99.31%**
19. **`packages/tailwindcss/src/canonicalize-candidates.ts`** -> AI Confidence: **99.31%**
20. **`packages/tailwindcss/src/compat/apply-compat-hooks.ts`** -> AI Confidence: **99.31%**
21. **`packages/tailwindcss/src/compat/config/resolve-config.ts`** -> AI Confidence: **99.31%**
22. **`packages/tailwindcss/src/compat/plugin-api.ts`** -> AI Confidence: **99.31%**
23. **`packages/tailwindcss/src/compile.ts`** -> AI Confidence: **99.31%**
24. **`packages/tailwindcss/src/css-functions.ts`** -> AI Confidence: **99.31%**
25. **`packages/tailwindcss/src/index.ts`** -> AI Confidence: **99.31%**
26. **`packages/tailwindcss/src/intellisense.ts`** -> AI Confidence: **99.31%**
27. **`packages/tailwindcss/src/attribute-selector-parser.ts`** -> AI Confidence: **99.29%**
28. **`packages/tailwindcss/src/utils/brace-expansion.ts`** -> AI Confidence: **99.29%**
29. **`packages/tailwindcss/src/utils/decode-arbitrary-value.ts`** -> AI Confidence: **99.29%**
30. **`packages/tailwindcss/src/utils/escape.ts`** -> AI Confidence: **99.29%**
31. **`packages/tailwindcss/src/utils/is-valid-arbitrary.ts`** -> AI Confidence: **99.29%**
32. **`packages/tailwindcss/src/utils/math-operators.ts`** -> AI Confidence: **99.29%**
33. **`packages/tailwindcss/src/utils/segment.ts`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1003` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `integrations/utils.ts` (TYPESCRIPT) -> Cumulative Risk: **745.02**
- **Archetype:** `file_cluster_4` (Distance: 13.235 IQR)
- **Magnitude:** 96.75 | **LOC:** 697 | **CtrlFlow:** 48.5% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9999%), Cognitive Load (94.7806%)
- **Heaviest Functions:** `async` (Impact: 170.4), `notifyNext` (Impact: 49.2), `dumpFiles` (Impact: 29.6)

### 2. `packages/@tailwindcss-node/src/compile.ts` (TYPESCRIPT) -> Cumulative Risk: **714.48**
- **Archetype:** `file_cluster_4` (Distance: 11.59 IQR)
- **Magnitude:** 36.29 | **LOC:** 279 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Cognitive Load (99.9998%), State Flux (99.8893%)
- **Heaviest Functions:** `onDependency` (Impact: 27.8), `resolveJsId` (Impact: 16.7), `importModule` (Impact: 14.8)

### 3. `packages/@tailwindcss-upgrade/src/codemods/config/migrate-postcss.ts` (TYPESCRIPT) -> Cumulative Risk: **702.64**
- **Archetype:** `file_cluster_4` (Distance: 13.092 IQR)
- **Magnitude:** 39.08 | **LOC:** 350 | **CtrlFlow:** 71.4% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.8879%)
- **Heaviest Functions:** `migratePostCSSConfig` (Impact: 79.7), `isTailwindCSSNestingPlugin` (Impact: 44.8), `isTailwindCSSPlugin` (Impact: 20.4)

### 4. `packages/tailwindcss/src/compat/plugin-functions.ts` (TYPESCRIPT) -> Cumulative Risk: **685.15**
- **Archetype:** `file_cluster_13` (Distance: 13.65 IQR)
- **Magnitude:** 48.03 | **LOC:** 255 | **CtrlFlow:** 69.5% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.3207%)
- **Heaviest Functions:** `resolveValue` (Impact: 93.0), `theme` (Impact: 81.1), `resolvedValue` (Impact: 69.7)

### 5. `packages/@tailwindcss-vite/src/index.ts` (TYPESCRIPT) -> Cumulative Risk: **681.24**
- **Archetype:** `file_cluster_4` (Distance: 13.242 IQR)
- **Magnitude:** 45.0 | **LOC:** 632 | **CtrlFlow:** 59.3% | **Authorship Centralization:** 20.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (97.6139%)
- **Heaviest Functions:** `createRoot` (Impact: 33.7), `handler` (Impact: 25.3), `customJsResolver` (Impact: 21.5)

### 6. `packages/@tailwindcss-upgrade/src/codemods/css/sort-buckets.ts` (TYPESCRIPT) -> Cumulative Risk: **664.3**
- **Archetype:** `file_cluster_4` (Distance: 12.358 IQR)
- **Magnitude:** 32.05 | **LOC:** 162 | **CtrlFlow:** 53.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9979%), Cognitive Load (99.3211%)
- **Heaviest Functions:** `migrate` (Impact: 76.0), `sortBuckets` (Impact: 67.0), `walk` (Impact: 53.1)

### 7. `packages/@tailwindcss-upgrade/src/codemods/config/migrate-js-config.ts` (TYPESCRIPT) -> Cumulative Risk: **648.69**
- **Archetype:** `file_cluster_4` (Distance: 12.596 IQR)
- **Magnitude:** 64.91 | **LOC:** 554 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 60.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.8878%), Safety Score (92.0805%)
- **Heaviest Functions:** `migrateTheme` (Impact: 141.5), `removeUnnecessarySpacingKeys` (Impact: 64.0), `canMigrateConfig` (Impact: 40.1)

### 8. `packages/tailwindcss/src/index.ts` (TYPESCRIPT) -> Cumulative Risk: **643.25**
- **Archetype:** `file_cluster_4` (Distance: 12.526 IQR)
- **Magnitude:** 52.06 | **LOC:** 867 | **CtrlFlow:** 52.2% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9998%), Concurrency (99.0411%), Cognitive Load (98.0757%)
- **Heaviest Functions:** `walk` (Impact: 86.2), `build` (Impact: 50.0), `build` (Impact: 43.1)

### 9. `packages/tailwindcss/src/apply.ts` (TYPESCRIPT) -> Cumulative Risk: **618.7**
- **Archetype:** `file_cluster_11` (Distance: 12.859 IQR)
- **Magnitude:** 50.74 | **LOC:** 325 | **CtrlFlow:** 58.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (96.747%)
- **Heaviest Functions:** `substituteAtApply` (Impact: 126.9), `walk` (Impact: 53.5), `visit` (Impact: 49.6)

### 10. `packages/@tailwindcss-webpack/src/index.ts` (TYPESCRIPT) -> Cumulative Risk: **615.16**
- **Archetype:** `file_cluster_4` (Distance: 13.017 IQR)
- **Magnitude:** 22.56 | **LOC:** 288 | **CtrlFlow:** 62.7% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9995%), Safety Score (93.9219%)
- **Heaviest Functions:** `tailwindLoader` (Impact: 45.2), `onDependency` (Impact: 20.7), `callback` (Impact: 19.3)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `crates/node/npm/wasm32-wasi/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `packages/tailwindcss/src/utilities.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.137 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.346 IQR)
- **Top Global Matches:** file_cluster_8: 12.137, file_cluster_4: 12.365, file_cluster_0: 12.396
- **Magnitude:** 1241.18 | **LOC:** 29983 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (44.422%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 77.8)
  * `test` (Impact: 77.8)
  * `test` (Impact: 57.1)
  * `test` (Impact: 44.6)
  * `test` (Impact: 41.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 184`, `structural_boundaries: 8104`, `args: 911`, `func_start: 984`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 7329`, `fragile_debt: 1`, `duplicate_logic: 321`
* *Architecture:* `io: 6`, `concurrency: 2280`, `import: 4`
* *Defense:* `safety: 97`, `test: 984`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` vitest, run, utilities, 
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/ignore/src/walk.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 15.117 IQR)
- **Top Global Matches:** file_cluster_0: 15.117, file_cluster_4: 15.175, file_cluster_13: 15.202
- **Magnitude:** 596.08 | **LOC:** 2482 | **CtrlFlow:** 37.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (25.6911%), Tech Debt (98.9138%)
**Top Internal Functions/Classes:**
  * `next` (Impact: 33.4)
  * `visit` (Impact: 29.7)
    * *Intent:* /// Yields only entries which satisfy the given predicate and skips /// descending into directories ...
  * `skip_entry` (Impact: 19.1)
  * `build` (Impact: 18.1)
  * `next` (Impact: 15.3)
    * *Intent:* /// Enables reading a global gitignore file, whose path is specified in /// git's `core.excludesFile...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 147`, `structural_boundaries: 248`, `args: 98`, `func_start: 75`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 105`, `dead_code: 10`, `duplicate_logic: 29`
* *Architecture:* `io: 1`, `api: 46`, `concurrency: 68`, `import: 13`
* *Defense:* `safety: 257`, `doc: 478`, `test: 2`, `sync_locks: 1`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` WalkState, self::DirEntryInner::*, std::sync::Arc, AtomicUsize, walkdir::DirEntryExt, std::ffi::OsStr, Ordering, walkdir::WalkDir...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tailwindcss/src/utilities.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.252 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.264 IQR)
- **Top Global Matches:** file_cluster_8: 13.252, file_cluster_13: 13.613, file_cluster_7: 13.621
- **Magnitude:** 302.73 | **LOC:** 6690 | **CtrlFlow:** 38.8% | **Authorship Centralization:** 36.0%
- **Risk Profile:** Cognitive Load (62.1344%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `createUtilities` (Impact: 392.1)
  * `replaceAlpha` (Impact: 359.3)
    * *Intent:* // Convert numeric values (like `0.5`) to percentages (like `50%`) so they // work properly with `co...
  * `staticUtility` (Impact: 75.2)
  * `staticUtility` (Impact: 68.2)
  * `maskStopUtility` (Impact: 46.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 478`, `structural_boundaries: 754`, `args: 838`, `func_start: 882`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 794`, `duplicate_logic: 204`
* *Architecture:* `api: 8`, `import: 14`
* *Defense:* `safety: 34`, `doc: 47`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` infer-data-type, design-system, escape, theme, segment, feature-flags, walk, value-parser...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/ignore/src/dir.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.968 IQR)
- **Top Global Matches:** file_cluster_0: 12.968, file_cluster_16: 13.027, file_cluster_8: 13.068
- **Magnitude:** 285.74 | **LOC:** 1270 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (12.5184%), Tech Debt (99.997%)
**Top Internal Functions/Classes:**
  * `create_gitignore` (Impact: 27.8)
  * `matched` (Impact: 19.0)
  * `build_with_cwd` (Impact: 14.1)
    * *Intent:* // Match against the override patterns. If an override matches // regardless of whether it's whiteli...
  * `add_parents` (Impact: 9.3)
  * `git_info_exclude_in_linked_worktree` (Impact: 5.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 155`, `args: 59`, `func_start: 52`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 72`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 14`, `orphaned_logic: 21`
* *Architecture:* `io: 4`, `api: 21`, `import: 3`
* *Defense:* `safety: 56`, `doc: 191`, `test: 92`, `sync_locks: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::Error, Override, io::self, Weak, BufRead, PartialErrorBuilder, strip_prefix, Match...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tailwindcss/src/index.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.046 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.055 IQR)
- **Top Global Matches:** file_cluster_8: 11.046, file_cluster_0: 11.104, file_cluster_4: 11.157
- **Magnitude:** 268.07 | **LOC:** 6301 | **CtrlFlow:** 4.4% | **Authorship Centralization:** 46.7%
- **Risk Profile:** Cognitive Load (41.1727%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 73.1)
  * `describe` (Impact: 39.5)
  * `describe` (Impact: 37.9)
  * `describe` (Impact: 31.2)
  * `describe` (Impact: 28.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 781`, `args: 457`, `func_start: 445`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 352`, `planned_debt: 1`, `duplicate_logic: 270`
* *Architecture:* `io: 59`, `concurrency: 1029`, `import: 7`
* *Defense:* `safety: 22`, `doc: 5`, `test: 384`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` vitest, three.css, preflight, plugin-api, node:fs, bar.css, , run...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/ignore/src/types.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.542 IQR)
- **Top Global Matches:** file_cluster_13: 12.542, file_cluster_0: 12.546, file_cluster_16: 12.651
- **Magnitude:** 206.9 | **LOC:** 602 | **CtrlFlow:** 31.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (9.1764%), Tech Debt (40.2578%)
**Top Internal Functions/Classes:**
  * `add_def` (Impact: 20.8)
    * *Intent:* /// Add a new file type definition specified in string form. There are two /// valid formats: /// 1....
  * `build` (Impact: 14.2)
  * `add` (Impact: 8.8)
    * *Intent:* /// Add a new file type definition. `name` can be arbitrary and `pat` /// should be a glob recognizi...
  * `add_defaults` (Impact: 8.6)
  * `select` (Impact: 7.5)
    * *Intent:* /// Select the file type given by `name`.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 122`, `args: 32`, `func_start: 22`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 59`, `dead_code: 3`, `duplicate_logic: 4`
* *Architecture:* `api: 24`, `import: 8`
* *Defense:* `safety: 43`, `doc: 85`, `test: 14`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` globset::GlobBuilder, regex_automata::util::pool::Pool, Match, crate::Error, GlobSet, super::TypesBuilder, ignore::types::TypesBuilder, pathutil::file_name...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/oxide/src/extractor/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.759 IQR)
- **Top Global Matches:** file_cluster_8: 10.759, file_cluster_13: 10.847, file_cluster_0: 10.944
- **Magnitude:** 205.14 | **LOC:** 1138 | **CtrlFlow:** 28.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (16.6019%), Tech Debt (39.6059%)
**Top Internal Functions/Classes:**
  * `extract` (Impact: 23.4)
  * `extract_variables_from_css` (Impact: 19.7)
  * `extract_sub_candidates` (Impact: 9.9)
    * *Intent:* // Extract sub-candidates from a given range. // // E.g.: `[ClassPrefix('gap-y-4')]` will not be a v...
  * `drop_covered_spans` (Impact: 9.9)
  * `assert_extract_candidates_contains` (Impact: 7.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 95`, `args: 21`, `func_start: 15`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 2`, `state_mutation: 64`, `planned_debt: 1`, `orphaned_logic: 5`
* *Architecture:* `api: 19`, `import: 10`
* *Defense:* `safety: 12`, `doc: 8`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` css_variable_machine::CssVariableMachine, Extractor, std::fmt, std::hint::black_box, super::Extracted, pretty_assertions::assert_eq, crate::extractor::machine::Span, crate::cursor...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/version-packages.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.311 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.703 IQR)
- **Top Global Matches:** file_cluster_4: 12.311, file_cluster_17: 12.945, file_cluster_13: 12.957
- **Magnitude:** 189.42 | **LOC:** 179 | **CtrlFlow:** 29.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (99.9782%), Tech Debt (22.0917%)
**Top Internal Functions/Classes:**
  * `async` (Impact: 40.9)
  * `spawnSync` (Impact: 1.1)
    * *Intent:* // Edit the file, once the editor is closed, the file will be saved and we // can read the changes
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 53`, `args: 8`, `func_start: 3`
* *Risk/State:* `state_mutation: 68`, `orphaned_logic: 1`
* *Architecture:* `io: 23`, `concurrency: 77`, `import: 7`
* *Defense:* `safety: 7`, `immutability_locks: 5`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:path, node:os, prettier, node:child_process, node:crypto, node:url, promises
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tailwindcss/src/canonicalize-candidates.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.901 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.487 IQR)
- **Top Global Matches:** file_cluster_13: 13.901, file_cluster_11: 13.948, file_cluster_17: 14.02
- **Magnitude:** 176.23 | **LOC:** 2909 | **CtrlFlow:** 60.2% | **Authorship Centralization:** 79.2%
- **Risk Profile:** Cognitive Load (75.228%), Tech Debt (79.35%)
**Top Internal Functions/Classes:**
  * `arbitraryUtilities` (Impact: 266.8)
  * `collapseCandidates` (Impact: 138.5)
  * `collapseGroup` (Impact: 135.3)
  * `canonicalizeAst` (Impact: 77.7)
  * `walk` (Impact: 67.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 275`, `structural_boundaries: 182`, `args: 70`, `func_start: 44`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 479`, `dead_code: 2`, `duplicate_logic: 12`
* *Architecture:* `io: 3`, `api: 14`, `import: 22`
* *Defense:* `safety: 38`, `doc: 5`, `immutability_locks: 9`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.581
  * `Choke Point (Betweenness):` 0.003689 | `Ripple Effect (Closeness):` 0.058751
  * `Imports (Out-Degree: 16):` dimensions, walk, ast, constant-fold-declaration, to-key-path, types, design-system, segment...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `crates/oxide/tests/scanner.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.212 IQR)
- **Top Global Matches:** file_cluster_8: 8.212, file_cluster_16: 8.565, file_cluster_0: 9.059
- **Magnitude:** 171.14 | **LOC:** 1799 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.2099%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `scan_with_globs` (Impact: 13.8)
  * `it_should_not_ignore_folders_that_end_wi` (Impact: 7.2)
    * *Intent:* // https://github.com/tailwindlabs/tailwindcss/issues/17569
  * `skips_ignore_files_outside_of_a_repo` (Impact: 6.8)
  * `test_manually_scanning_files_should_foll` (Impact: 5.9)
  * `create_files_in` (Impact: 5.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 106`, `args: 34`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 20`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 21`, `concurrency: 1`, `import: 8`
* *Defense:* `safety: 1`, `test: 97`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::thread::sleep, std::process::Command, std::path::Path, path, std::time::Duration, tempfile::tempdir, pretty_assertions::assert_eq, tailwindcss_oxide::*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/oxide/src/scanner/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.066 IQR)
- **Top Global Matches:** file_cluster_13: 12.066, file_cluster_0: 12.217, file_cluster_16: 12.44
- **Magnitude:** 168.52 | **LOC:** 896 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (15.7856%), Tech Debt (25.4167%)
**Top Internal Functions/Classes:**
  * `discover_sources` (Impact: 85.2)
  * `get_globs` (Impact: 9.8)
  * `test_positions` (Impact: 5.4)
  * `get_normalized_sources` (Impact: 4.3)
  * `get_candidates_with_positions` (Impact: 2.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 73`, `args: 14`, `func_start: 6`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 36`, `dead_code: 1`, `orphaned_logic: 4`
* *Architecture:* `io: 1`, `api: 17`, `import: 19`
* *Defense:* `safety: 28`, `doc: 23`, `test: 3`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` init_tracing::init_tracing, Extractor, auto_source_detection::BINARY_EXTENSIONS_GLOB, fast_glob::glob_match, BTreeSet, std::sync::Arc, PublicSourceEntry, fxhash::FxHashMap...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/oxide/src/extractor/pre_processors/haml.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.565 IQR)
- **Top Global Matches:** file_cluster_8: 9.565, file_cluster_13: 9.839, file_cluster_0: 10.002
- **Magnitude:** 140.74 | **LOC:** 467 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (27.1337%), Tech Debt (56.9001%)
**Top Internal Functions/Classes:**
  * `skip_indented_block` (Impact: 56.4)
    * *Intent:* // If the dot is surrounded by digits, we want to keep it. E.g.: `px-2.5` // EXCEPT if it's followed...
  * `process` (Impact: 38.2)
  * `test_haml_pre_processor` (Impact: 5.5)
  * `test_strings_only_occur_when_nested` (Impact: 3.0)
  * `test_arbitrary_code_followed_by_classes` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 56`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 23`, `orphaned_logic: 7`
* *Architecture:* `api: 1`, `import: 10`
* *Defense:* `safety: 3`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::extractor::pre_processors::pre_processor::PreProcessor, crate::scanner::pre_process_input, super::Haml, crate::extractor::variant_machine::VariantMachine, pretty_assertions::assert_eq, crate::extractor::bracket_stack::BracketStack, crate::cursor, bstr::ByteVec...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/ignore/src/gitignore.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.779 IQR)
- **Top Global Matches:** file_cluster_0: 12.779, file_cluster_16: 12.795, file_cluster_13: 12.861
- **Magnitude:** 133.28 | **LOC:** 869 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (5.0729%), Tech Debt (8.9159%)
**Top Internal Functions/Classes:**
  * `build_global` (Impact: 11.0)
  * `add` (Impact: 9.8)
    * *Intent:* /// Returns whether the given path (file or directory, and expected to be /// under the root) or any...
  * `parse_excludes_file` (Impact: 9.4)
  * `gitconfig_excludes_path` (Impact: 8.7)
  * `home_dir` (Impact: 7.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 40`, `args: 29`, `func_start: 23`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 13`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 22`, `import: 5`
* *Defense:* `safety: 35`, `doc: 162`, `test: 16`, `sync_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::sync::OnceLock, Read, BufReader, GlobBuilder, util::syntax, super::Gitignore, PartialErrorBuilder, GlobSetBuilder...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/ignore/src/lib.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.069 IQR)
- **Top Global Matches:** file_cluster_16: 13.069, file_cluster_8: 13.142, file_cluster_13: 13.172
- **Magnitude:** 130.04 | **LOC:** 561 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (9.5496%), Tech Debt (55.5702%)
**Top Internal Functions/Classes:**
  * `into_error_option` (Impact: 10.4)
  * `new` (Impact: 9.6)
  * `clone` (Impact: 6.9)
  * `is_io` (Impact: 5.8)
  * `or` (Impact: 5.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 66`, `args: 19`, `func_start: 17`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 20`, `orphaned_logic: 7`
* *Architecture:* `io: 5`, `api: 18`, `concurrency: 9`, `import: 4`
* *Defense:* `safety: 48`, `doc: 97`, `test: 1`, `sync_locks: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` WalkState, PathBuf, std::sync::atomic::AtomicUsize, Walk, WalkParallel, ignore::WalkBuilder, std::path::Path, Ordering...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/oxide/src/extractor/arbitrary_variable_machine.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.315 IQR)
- **Top Global Matches:** file_cluster_0: 11.315, file_cluster_13: 11.48, file_cluster_16: 11.523
- **Magnitude:** 125.44 | **LOC:** 414 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (10.3263%), Tech Debt (99.9996%)
**Top Internal Functions/Classes:**
  * `next` (Impact: 30.7)
  * `next` (Impact: 10.3)
    * *Intent:* // End of an arbitrary variable, must be followed by `)`
  * `next` (Impact: 10.1)
    * *Intent:* #[inline(always)]
  * `test_arbitrary_variable_extraction` (Impact: 8.9)
  * `next` (Impact: 8.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 46`, `args: 12`, `func_start: 12`, `class_start: 5`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 28`, `planned_debt: 1`, `duplicate_logic: 8`, `orphaned_logic: 3`
* *Architecture:* `api: 5`, `import: 10`
* *Defense:* `safety: 10`, `doc: 31`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::extractor::string_machine::StringMachine, classification_macros::ClassifyBytes, super::ArbitraryVariableMachine, crate::extractor::machine::Machine, std::marker::PhantomData, pretty_assertions::assert_eq, crate::extractor::bracket_stack::BracketStack, crate::cursor...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tailwindcss/src/compat/config.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.438 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.15 IQR)
- **Top Global Matches:** file_cluster_4: 11.438, file_cluster_8: 11.61, file_cluster_0: 11.73
- **Magnitude:** 125.26 | **LOC:** 1774 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (68.9321%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 146.4)
  * `test` (Impact: 23.9)
  * `describe` (Impact: 21.0)
  * `test` (Impact: 12.0)
  * `test` (Impact: 12.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 254`, `args: 167`, `func_start: 167`
* *Risk/State:* `state_mutation: 259`, `duplicate_logic: 106`
* *Architecture:* `io: 43`, `concurrency: 448`, `import: 4`
* *Defense:* `safety: 6`, `test: 113`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` plugin, vitest, .., flatten-color-palette
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/oxide/src/glob.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.854 IQR)
- **Top Global Matches:** file_cluster_8: 9.854, file_cluster_13: 10.224, file_cluster_0: 10.263
- **Magnitude:** 122.96 | **LOC:** 602 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.4596%), Tech Debt (76.5493%)
**Top Internal Functions/Classes:**
  * `hoist_static_glob_parts` (Impact: 21.7)
  * `split_pattern` (Impact: 17.6)
    * *Intent:* // // Assumption: we assume that all globs are expanded, which means that the only dynamic parts are...
  * `optimize_patterns` (Impact: 8.2)
    * *Intent:* /// ```sh /// tailwind --pwd ./project --content "{pages,components}/**/*.js" /// ``` /// Then the g...
  * `create_folders` (Impact: 7.2)
  * `test` (Impact: 5.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 82`, `args: 21`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 16`, `planned_debt: 2`, `orphaned_logic: 10`
* *Architecture:* `api: 6`, `import: 10`
* *Defense:* `safety: 22`, `doc: 25`, `test: 32`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` fxhash::FxHashMap, bexpand::Expression, std::path::PathBuf, std::process::Command, super::optimize_patterns, path, crate::GlobEntry, tempfile::tempdir...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/oxide/src/extractor/arbitrary_property_machine.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.918 IQR)
- **Top Global Matches:** file_cluster_0: 10.918, file_cluster_16: 11.094, file_cluster_13: 11.1
- **Magnitude:** 118.26 | **LOC:** 458 | **CtrlFlow:** 32.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (9.3002%), Tech Debt (99.9531%)
**Top Internal Functions/Classes:**
  * `next` (Impact: 20.5)
  * `test_arbitrary_property_machine_extracti` (Impact: 15.5)
  * `next` (Impact: 10.6)
  * `parse_property_variable` (Impact: 6.1)
    * *Intent:* // End of the property name, but there must be at least a single character
  * `next` (Impact: 5.9)
    * *Intent:* #[inline(always)]
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 55`, `args: 12`, `func_start: 12`, `class_start: 5`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 31`, `planned_debt: 1`, `duplicate_logic: 6`, `orphaned_logic: 3`
* *Architecture:* `api: 4`, `import: 10`
* *Defense:* `safety: 8`, `doc: 28`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::extractor::string_machine::StringMachine, classification_macros::ClassifyBytes, super::ArbitraryPropertyMachine, std::marker::PhantomData, crate::extractor::CssVariableMachine, pretty_assertions::assert_eq, crate::extractor::bracket_stack::BracketStack, crate::cursor...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/oxide/src/extractor/pre_processors/vue.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.886 IQR)
- **Top Global Matches:** file_cluster_13: 8.886, file_cluster_8: 9.213, file_cluster_0: 9.361
- **Magnitude:** 113.2 | **LOC:** 46 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (12.5165%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 15`, `args: 4`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 3`
* *Architecture:* `api: 1`, `import: 7`
* *Defense:* `test: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::extractor::pre_processors::pre_processor::PreProcessor, std::sync, crate::scanner::pre_process_input, super::Vue, bstr::ByteSlice, regex::Regex
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/oxide/src/extractor/named_variant_machine.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.439 IQR)
- **Top Global Matches:** file_cluster_0: 11.439, file_cluster_13: 11.617, file_cluster_16: 11.624
- **Magnitude:** 113.0 | **LOC:** 423 | **CtrlFlow:** 31.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (9.8908%), Tech Debt (99.9964%)
**Top Internal Functions/Classes:**
  * `next` (Impact: 23.6)
  * `next` (Impact: 9.1)
    * *Intent:* #[inline(always)]
  * `test_named_variant_extraction` (Impact: 7.1)
  * `next` (Impact: 6.1)
  * `next` (Impact: 5.8)
    * *Intent:* // Modifier must be followed by a `:` //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 50`, `args: 16`, `func_start: 12`, `class_start: 6`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 34`, `planned_debt: 1`, `duplicate_logic: 8`, `orphaned_logic: 2`
* *Architecture:* `api: 5`, `import: 10`
* *Defense:* `safety: 12`, `doc: 33`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` NamedVariantMachine, classification_macros::ClassifyBytes, crate::extractor::arbitrary_variable_machine::ArbitraryVariableMachine, crate::extractor::modifier_machine::ModifierMachine, super::IdleState, std::marker::PhantomData, pretty_assertions::assert_eq, crate::cursor...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/oxide/src/extractor/named_utility_machine.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.786 IQR)
- **Top Global Matches:** file_cluster_8: 9.786, file_cluster_0: 9.787, file_cluster_13: 9.988
- **Magnitude:** 102.6 | **LOC:** 536 | **CtrlFlow:** 31.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (9.7052%), Tech Debt (96.641%)
**Top Internal Functions/Classes:**
  * `next` (Impact: 38.3)
  * `next` (Impact: 14.9)
  * `test_named_utility_extraction` (Impact: 13.3)
    * *Intent:* #[test] #[ignore]
  * `transition` (Impact: 2.2)
  * `reset` (Impact: 2.2)
    * *Intent:* // Everything else, is not a valid start of the utility.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 56`, `args: 12`, `func_start: 7`, `class_start: 4`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 18`, `planned_debt: 1`, `duplicate_logic: 4`, `orphaned_logic: 2`
* *Architecture:* `api: 3`, `import: 10`
* *Defense:* `safety: 8`, `doc: 12`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::extractor::boundary::is_valid_after_boundary, classification_macros::ClassifyBytes, crate::extractor::arbitrary_variable_machine::ArbitraryVariableMachine, super::IdleState, NamedUtilityMachine, std::marker::PhantomData, pretty_assertions::assert_eq, crate::cursor...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integrations/utils.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.235 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.228 IQR)
- **Top Global Matches:** file_cluster_4: 13.235, file_cluster_13: 13.885, file_cluster_11: 13.887
- **Magnitude:** 96.75 | **LOC:** 697 | **CtrlFlow:** 48.5% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (94.7806%), Tech Debt (84.2097%)
**Top Internal Functions/Classes:**
  * `async` (Impact: 170.4)
  * `notifyNext` (Impact: 49.2)
  * `dumpFiles` (Impact: 29.6)
  * `overwriteVersionsInPackageJson` (Impact: 21.8)
  * `write` (Impact: 10.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 137`, `args: 73`, `func_start: 58`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 238`, `dead_code: 1`, `duplicate_logic: 8`, `orphaned_logic: 4`
* *Architecture:* `io: 40`, `api: 16`, `concurrency: 282`, `import: 12`
* *Defense:* `safety: 45`, `doc: 3`, `test: 7`, `immutability_locks: 6`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` vitest, node:path, fast-glob, node:os, source-map-js, node:child_process, node:util, dedent...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tailwindcss/src/compat/plugin-api.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.091 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.851 IQR)
- **Top Global Matches:** file_cluster_8: 10.091, file_cluster_4: 10.197, file_cluster_0: 10.546
- **Magnitude:** 89.16 | **LOC:** 4640 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (45.1361%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 72.0)
  * `describe` (Impact: 23.3)
  * `test` (Impact: 15.1)
  * `test` (Impact: 9.0)
  * `test` (Impact: 8.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 219`, `args: 202`, `func_start: 193`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 99`, `duplicate_logic: 95`
* *Architecture:* `io: 29`, `concurrency: 346`, `import: 6`
* *Defense:* `safety: 5`, `test: 62`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` plugin, vitest, inside.css, run, .., plugin-api, …, default-theme
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/oxide/src/extractor/candidate_machine.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.074 IQR)
- **Top Global Matches:** file_cluster_0: 11.074, file_cluster_13: 11.116, file_cluster_8: 11.391
- **Magnitude:** 86.8 | **LOC:** 362 | **CtrlFlow:** 39.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (25.8442%), Tech Debt (44.3425%)
**Top Internal Functions/Classes:**
  * `next` (Impact: 50.4)
  * `test_candidate_extraction` (Impact: 5.5)
  * `test_candidate_machine_performance` (Impact: 2.4)
  * `reset` (Impact: 2.2)
  * `done_span` (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 40`, `args: 6`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 20`, `dead_code: 1`, `planned_debt: 1`, `orphaned_logic: 2`
* *Architecture:* `api: 1`, `import: 9`
* *Defense:* `safety: 14`, `doc: 3`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::CandidateMachine, is_valid_before_boundary, crate::extractor::variant_machine::VariantMachine, crate::extractor::utility_machine::UtilityMachine, pretty_assertions::assert_eq, crate::cursor, crate::extractor::Span, crate::extractor::machine::Machine...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `crates/oxide/src/extractor/machine.rs` (RUST) | Magnitude: 83.38 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 113, structural_boundaries: 49, state_mutation: 40, args: 12
- `crates/ignore/src/overrides.rs` (RUST) | Magnitude: 29.2 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 96, doc: 77, test: 50, sec_high_risk_execution: 41
- `crates/oxide/src/extractor/pre_processors/markdown.rs` (RUST) | Magnitude: 31.46 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 64, structural_boundaries: 16, state_mutation: 10, branch: 7
- `crates/ignore/src/gitignore.rs` (RUST) | Magnitude: 133.28 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 260, doc: 162, structural_boundaries: 40, safety: 35
- `playgrounds/v3/scripts/upgrade.mjs` (JAVASCRIPT) | Magnitude: 15.78 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: structural_boundaries: 16, io: 16, concurrency: 7, decorators: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `packages/tailwindcss/src/apply.ts` (TYPESCRIPT) | Magnitude: 50.74 | Delta: **0.111 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 184, state_mutation: 132, branch: 65, structural_boundaries: 47
- `packages/tailwindcss/src/utils/topological-sort.ts` (TYPESCRIPT) | Magnitude: 5.64 | Delta: **0.259 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 33, indent_spaces: 23, branch: 8, io: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `crates/ignore/src/types.rs` (RUST) | Magnitude: 206.9 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 363, structural_boundaries: 122, doc: 85, state_mutation: 59
- `packages/tailwindcss/src/theme.ts` (TYPESCRIPT) | Magnitude: 41.72 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 224, state_mutation: 218, branch: 71, structural_boundaries: 67
- `packages/@tailwindcss-upgrade/src/codemods/template/migrate-camelcase-in-named-value.ts` (TYPESCRIPT) | Magnitude: 5.18 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 34, branch: 15, structural_boundaries: 11, state_mutation: 9
- `packages/@tailwindcss-upgrade/src/utils/extract-static-plugins.test.ts` (TYPESCRIPT) | Magnitude: 20.48 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 301, structural_boundaries: 103, func_start: 65, api: 41
- `packages/@tailwindcss-upgrade/src/codemods/template/migrate-variant-order.ts` (TYPESCRIPT) | Magnitude: 15.12 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 90, state_mutation: 50, branch: 32, structural_boundaries: 30

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `crates/ignore/tests/gitignore_skip_bom.rs` (RUST) | Magnitude: 3.42 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, indent_spaces: 5, doc: 4, test: 3
- `crates/ignore/src/lib.rs` (RUST) | Magnitude: 130.04 | Delta: **0.073 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 227, doc: 97, structural_boundaries: 66, safety: 48
- `crates/oxide/src/cursor.rs` (RUST) | Magnitude: 76.42 | Delta: **0.075 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 95, branch: 17, structural_boundaries: 17, test: 16
- `crates/oxide/src/scanner/sources.rs` (RUST) | Magnitude: 77.98 | Delta: **0.078 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 164, doc: 78, structural_boundaries: 34, branch: 22
- `packages/tailwindcss/src/compat/config/deep-merge.ts` (TYPESCRIPT) | Magnitude: 4.75 | Delta: **0.114 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 29, state_mutation: 15, branch: 12, structural_boundaries: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/tailwindcss/src/utils/replace-shadow-colors.ts` (TYPESCRIPT) | Magnitude: 3.9 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, state_mutation: 16, branch: 12, structural_boundaries: 5
- `packages/tailwindcss/src/candidate.bench.ts` (TYPESCRIPT) | Magnitude: 8.55 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 22, branch: 21, args: 13
- `packages/tailwindcss/src/compat/screens-config.ts` (TYPESCRIPT) | Magnitude: 11.31 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 75, state_mutation: 39, branch: 28, structural_boundaries: 22
- `packages/tailwindcss/src/sort.ts` (TYPESCRIPT) | Magnitude: 3.52 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 16, indent_spaces: 12, branch: 8, structural_boundaries: 7
- `crates/oxide/fuzz/fuzz_targets/parsing.rs` (RUST) | Magnitude: 15.46 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 7, import: 5, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `playgrounds/vite/src/index.html` (HTML) | Magnitude: 17.24 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 4, decorators: 3, api: 2
- `playgrounds/vite/src/app.tsx` (TYPESCRIPT) | Magnitude: 0.32 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 5, structural_boundaries: 2, ui_framework: 2, args: 1
- `playgrounds/v3/app/page.tsx` (TYPESCRIPT) | Magnitude: 0.3 | Delta: **0.178 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, branch: 1, args: 1, func_start: 1
- `packages/@tailwindcss-postcss/src/fixtures/example-project/index.html` (HTML) | Magnitude: 0.01 | Delta: **0.639 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 1, ui_framework: 1, decorators: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/tailwindcss/src/prefix.test.ts` (TYPESCRIPT) | Magnitude: 20.64 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 286, concurrency: 118, structural_boundaries: 42, decorators: 38
- `packages/@tailwindcss-upgrade/src/codemods/css/sort-buckets.ts` (TYPESCRIPT) | Magnitude: 32.05 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 104, state_mutation: 51, branch: 45, structural_boundaries: 39
- `packages/@tailwindcss-upgrade/src/codemods/template/migrate-legacy-classes.ts` (TYPESCRIPT) | Magnitude: 10.02 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 79, state_mutation: 34, structural_boundaries: 21, branch: 18
- `packages/@tailwindcss-upgrade/src/codemods/template/migrate-modernize-arbitrary-values.test.ts` (TYPESCRIPT) | Magnitude: 2.97 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 18, concurrency: 12, import: 9
- `packages/tailwindcss/src/source-maps/source-map.test.ts` (TYPESCRIPT) | Magnitude: 18.58 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 380, concurrency: 65, structural_boundaries: 58, state_mutation: 50

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `crates/oxide/src/extractor/named_utility_machine.rs` (RUST) | Magnitude: 102.6 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 294, structural_boundaries: 56, decorators: 31, branch: 26
- `packages/@tailwindcss-upgrade/src/utils/args.ts` (TYPESCRIPT) | Magnitude: 9.28 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 79, branch: 39, structural_boundaries: 39, state_mutation: 18
- `packages/@tailwindcss-upgrade/src/codemods/template/migrate-variant-order.test.ts` (TYPESCRIPT) | Magnitude: 3.38 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 54, concurrency: 24, decorators: 14, structural_boundaries: 12
- `packages/@tailwindcss-node/src/optimize.ts` (TYPESCRIPT) | Magnitude: 1.95 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 49, structural_boundaries: 16, sec_reflection_metaprogramming: 8, args: 6
- `crates/oxide/src/extractor/utility_machine.rs` (RUST) | Magnitude: 73.38 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 126, state_mutation: 31, structural_boundaries: 24, branch: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `packages/@tailwindcss-postcss/src/postcss-fix-relative-paths/fixtures/example-project/src/index.css` (CSS) | Magnitude: 0.01 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 2, doc: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/tailwindcss/src/utilities.ts` -> Churn: **96.28%** | Cog Load: 62.1344% | Debt: 100.0%
- `packages/tailwindcss/src/canonicalize-candidates.ts` -> Churn: **95.12%** | Cog Load: 75.228% | Debt: 79.35%
- `packages/@tailwindcss-vite/src/index.ts` -> Churn: **70.86%** | Cog Load: 92.5986% | Debt: 94.0183%
- `packages/tailwindcss/src/constant-fold-declaration.ts` -> Churn: **52.95%** | Cog Load: 66.5138% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `crates/ignore/src/walk.rs` -> **Jordan Pittman** (100.0% isolated ownership) | Magnitude: 596.08
- `crates/ignore/src/dir.rs` -> **Jordan Pittman** (100.0% isolated ownership) | Magnitude: 285.74
- `crates/ignore/src/types.rs` -> **Jordan Pittman** (100.0% isolated ownership) | Magnitude: 206.9
- `crates/oxide/src/extractor/mod.rs` -> **Robin Malfait** (100.0% isolated ownership) | Magnitude: 205.14
- `crates/oxide/src/extractor/pre_processors/haml.rs` -> **Robin Malfait** (100.0% isolated ownership) | Magnitude: 140.74

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/tailwindcss/src/design-system.ts` -> **Severity: 0.652** (Bridge: 0.0065 * Flux: 99.8656%)
- `packages/tailwindcss/src/intellisense.ts` -> **Severity: 0.405** (Bridge: 0.004 * Flux: 100.0%)
- `packages/tailwindcss/src/compat/plugin-api.ts` -> **Severity: 0.382** (Bridge: 0.0038 * Flux: 99.9993%)
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

- `packages/tailwindcss/src/utils/default-map.ts` -> **Severity: 1318.895** (Blast Radius: 35.329 * Doc Risk: 37.3318%)
- `packages/@tailwindcss-upgrade/src/utils/version.ts` -> **Severity: 1215.7** (Blast Radius: 12.157 * Doc Risk: 100.0%)
- `packages/tailwindcss/src/test-utils/run.ts` -> **Severity: 822.886** (Blast Radius: 8.502 * Doc Risk: 96.7873%)
- `packages/tailwindcss/src/design-system.ts` -> **Severity: 688.861** (Blast Radius: 44.453 * Doc Risk: 15.4964%)
- `packages/tailwindcss/src/utils/variables.ts` -> **Severity: 579.695** (Blast Radius: 7.05 * Doc Risk: 82.2263%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
