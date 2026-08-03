# ARCHITECTURAL_BRIEF: berry
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_typescript/berry` |
| **Timestamp** | `2026-08-03T19:53:56.358006+00:00` |
| **Scan Duration** | `3.04s` |
| **Git Branch** | `master` |
| **Git Commit** | `4bd2b2111867ca3a9dc46438aa3010145e31910b` |
| **Git Remote** | `https://github.com/yarnpkg/berry.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 534 malicious artifacts.

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
| Total Artifacts | 3799 |
| Analyzed Artifacts (Scanned) | 830 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2969 |
| Total LOC | 40105 |
| Volatility Index | 0.006 |
| % Scanned of codebase = | 21.8% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7298 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2572 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 4.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.0131 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 47 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 344 | 32019 | 41.4% |
| PLAINTEXT | 221 | 0 | 26.6% |
| JAVASCRIPT | 163 | 4576 | 19.6% |
| MARKDOWN | 47 | 0 | 5.7% |
| SHELL | 23 | 698 | 2.8% |
| CSS | 10 | 859 | 1.2% |
| JSON | 9 | 1779 | 1.1% |
| XML | 6 | 0 | 0.7% |
| YAML | 2 | 51 | 0.2% |
| DOCKERFILE | 2 | 16 | 0.2% |
| PERL | 1 | 101 | 0.1% |
| BATCH | 1 | 1 | 0.1% |
| POWERSHELL | 1 | 5 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `3.248`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 264 | 31.8% |
| file_cluster_13 | 158 | 19.0% |
| file_cluster_4 | 107 | 12.9% |
| file_cluster_17 | 13 | 1.6% |
| file_cluster_0 | 8 | 1.0% |
| file_cluster_2 | 4 | 0.5% |
| file_cluster_12 | 3 | 0.4% |
| file_cluster_16 | 2 | 0.2% |
| file_cluster_11 | 2 | 0.2% |
| file_cluster_9 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 268 | 32.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2969*

**Composition by Extension & Reason:**
- `.zip`: 2223x Excluded (Explicitly Denied Extension: '.zip')
- `no_extension`: 85x Unsupported Format (.undeterminable), 84x Excluded (Binary Format Detected), 22x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 159x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Saturation: Line 5 exceeds 500 chars), 2x Excluded (Embedded Array/Matrix Payload: 90519 commas in 941 LOC)
- `.ts`: 145x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Unsupported Format (.undeterminable), 3x Excluded (Saturation: Line 5 exceeds 500 chars)
- `.mdx`: 45x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 33 exceeds 500 chars), 1x Excluded (Saturation: Line 65 exceeds 500 chars)
- `.yml`: 46x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.diff`: 35x Excluded (Unsupported Extension: '.diff')
- `.json`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 180 LOC)
- `.snap`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 13x Excluded (Explicitly Denied Extension: '.png')
- `.sh`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.idx`: 6x Excluded (Unsupported Extension: '.idx')
- `.pack`: 6x Excluded (Unsupported Extension: '.pack')
- `.mjs`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 31.2 | 8.1 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 30.2 | 5.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 14.9 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 14.6 | 2.3 | 80.0 |
| API Exposure | 0.0 | 19.6 | 5.9 | 5.8 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 34.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 29.9 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 64.6 | 0.4 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 73.8 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 7.8 | 0.5 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 96.0 | 2.3 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 46.3 | 40.0 | 40.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 20.5 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 8.7 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 2.1 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `packages/acceptance-tests/pkg-tests-core/sources/utils/tests.ts` (Hits: 41)
- `scripts/bench-run.sh` (Hits: 40)
- `scripts/vscode-zip-test-procedure.sh` (Hits: 34)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **clipanion.ts** (`packages/plugin-essentials/sources/commands/entries/clipanion.ts`) — 78 inbound connections
2. **cli.ts** (`packages/yarnpkg-cli/sources/cli.ts`) — 61 inbound connections
3. **fs.ts** (`packages/acceptance-tests/pkg-tests-core/sources/utils/fs.ts`) — 26 inbound connections
4. **Report.ts** (`packages/yarnpkg-core/sources/Report.ts`) — 18 inbound connections
5. **MessageName.ts** (`packages/yarnpkg-core/sources/MessageName.ts`) — 16 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.ts** (`packages/plugin-essentials/sources/index.ts`) — 41 outbound dependencies
2. **Project.ts** (`packages/yarnpkg-core/sources/Project.ts`) — 38 outbound dependencies
3. **index.ts** (`packages/yarnpkg-core/sources/index.ts`) — 36 outbound dependencies
4. **Configuration.ts** (`packages/yarnpkg-core/sources/Configuration.ts`) — 32 outbound dependencies
5. **tests.ts** (`packages/acceptance-tests/pkg-tests-core/sources/utils/tests.ts`) — 22 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `makeLockfileChecksum` (@ `packages/yarnpkg-core/sources/Project.ts`) -> Impact: **2757.4** | LOC: 1348
- `makePathWrapper` (@ `packages/yarnpkg-core/sources/scriptUtils.ts`) -> Impact: **1760.0** | LOC: 764
- `parseSingleValue` (@ `packages/yarnpkg-core/sources/Configuration.ts`) -> Impact: **1107.9** | LOC: 798
- `executeCommandChainImpl` (@ `packages/yarnpkg-shell/sources/index.ts`) -> Impact: **745.0** | LOC: 339
- `makeApi` (@ `packages/yarnpkg-pnp/sources/loader/makeApi.ts`) -> Impact: **660.1** | LOC: 558
- `getLocatorPath` (@ `packages/yarnpkg-core/sources/Cache.ts`) -> Impact: **372.5** | LOC: 175
- `GenerateBaseWrapper` (@ `packages/yarnpkg-sdks/sources/sdks/base.ts`) -> Impact: **362.0** | LOC: 225
- `interpolateArguments` (@ `packages/yarnpkg-shell/sources/index.ts`) -> Impact: **325.7** | LOC: 114
- `execute` (@ `packages/plugin-interactive-tools/sources/commands/upgrade-interactive.tsx`) -> Impact: **325.1** | LOC: 371
- `applyPatch` (@ `packages/yarnpkg-pnp/sources/loader/applyPatch.ts`) -> Impact: **309.8** | LOC: 307

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `plugin` (@ `packages/docusaurus/config/docusaurus/plugins/webpack-config.ts`) -> **O(2^N) [Recursive]**
- `Home` (@ `packages/docusaurus/src/pages/index.tsx`) -> **O(2^N) [Recursive]**
  * *Intent:* // eslint-disable-next-line arca/no-default-export
- `StringPrototypeSlice` (@ `packages/yarnpkg-pnp/sources/node/resolve.js`) -> **O(2^N) [Recursive]**
- `getName` (@ `packages/acceptance-tests/pkg-tests-core/sources/utils/tests.ts`) -> **O(2^N) [Recursive]**
- `getLocatorPath` (@ `packages/yarnpkg-core/sources/Cache.ts`) -> **O(2^N) [Recursive]**
- `makeLockfileChecksum` (@ `packages/yarnpkg-core/sources/Project.ts`) -> **O(2^N) [Recursive]**
- `makePathWrapper` (@ `packages/yarnpkg-core/sources/scriptUtils.ts`) -> **O(2^N) [Recursive]**
- `interpolateArguments` (@ `packages/yarnpkg-shell/sources/index.ts`) -> **O(2^N) [Recursive]**
- `reportError` (@ `packages/plugin-constraints/sources/index.ts`) -> **O(2^N) [Recursive]**
- `makeTreeNode` (@ `packages/plugin-essentials/sources/commands/explain/peerRequirements.ts`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `makeLockfileChecksum` (@ `packages/yarnpkg-core/sources/Project.ts`) -> DB Complexity: **209**
- `parseSingleValue` (@ `packages/yarnpkg-core/sources/Configuration.ts`) -> DB Complexity: **115**
- `Anonymous_Block_[Truncated]` (@ `scripts/vscode-zip-test-procedure.sh`) -> DB Complexity: **111**
- `applyPatch` (@ `packages/yarnpkg-pnp/sources/loader/applyPatch.ts`) -> DB Complexity: **82**
- `GenerateBaseWrapper` (@ `packages/yarnpkg-sdks/sources/sdks/base.ts`) -> DB Complexity: **63**
- `makeApi` (@ `packages/yarnpkg-pnp/sources/loader/makeApi.ts`) -> DB Complexity: **61**
- `execute` (@ `packages/plugin-essentials/sources/commands/set/version.ts`) -> DB Complexity: **46**
- `interpretParsedPatchFile` (@ `packages/plugin-patch/sources/tools/parse.ts`) -> DB Complexity: **42**
- `getBufferAndClose` (@ `packages/yarnpkg-libzip/sources/libzipImpl.ts`) -> DB Complexity: **42**
- `watch` (@ `packages/plugin-compat/extra/fsevents/fsevents-1.2.11.js`) -> DB Complexity: **37**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `packages/yarnpkg-libzip/sources` | 15 | 2407.71 | 40.45% | 23.58% |
| `packages/yarnpkg-core/sources` | 44 | 1266.02 | 50.99% | 14.72% |
| `packages/yarnpkg-pnp/sources/node` | 7 | 711.48 | 24.82% | 24.01% |
| `packages/acceptance-tests/pkg-tests-fixtures/repositories/no-lockfile-project.git/hooks` | 13 | 473.18 | 54.65% | 92.23% |
| `scripts` | 28 | 328.92 | 31.73% | 24.46% |
| `packages/plugin-compat/extra/fsevents` | 4 | 306.12 | 67.13% | 25.0% |
| `packages/plugin-essentials/sources/commands` | 15 | 232.16 | 92.54% | 11.24% |
| `packages/yarnpkg-shell/sources` | 5 | 222.23 | 43.14% | 54.78% |
| `packages/yarnpkg-pnpify/sources` | 7 | 215.37 | 44.97% | 14.29% |
| `packages/yarnpkg-pnp/sources/loader` | 10 | 157.8 | 22.76% | 19.85% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `scripts/plugin-base.js` -> **100.0%** Exposure
- `packages/docusaurus/src/pages/configuration.tsx` -> **100.0%** Exposure
- `packages/yarnpkg-core/sources/execUtils.ts` -> **100.0%** Exposure
- `packages/yarnpkg-pnpify/sources/NodeModulesFS.ts` -> **100.0%** Exposure
- `packages/acceptance-tests/pkg-tests-fixtures/repositories/has-prepack.git/hooks/post-update` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `packages/acceptance-tests/pkg-tests-fixtures/packages/has-bin-entries-1.0.0/bin.js` -> **100.0%** Exposure
- `packages/acceptance-tests/pkg-tests-fixtures/packages/has-bin-entries-2.0.0/bin.js` -> **100.0%** Exposure
- `packages/acceptance-tests/pkg-tests-fixtures/packages/path-parse-1.0.6/index.js` -> **100.0%** Exposure
- `packages/plugin-compat/extra/fsevents/vfs.js` -> **100.0%** Exposure
- `packages/yarnpkg-libzip/sources/libzipSync.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/yarnpkg-pnpify/sources/NodeModulesFS.ts` -> **0** Orphaned Functions | **42** Duplicates
- `packages/yarnpkg-libzip/sources/ZipFS.ts` -> **0** Orphaned Functions | **38** Duplicates
- `packages/yarnpkg-core/tests/TestPlugin.ts` -> **3** Orphaned Functions | **16** Duplicates
- `packages/yarnpkg-shell/sources/index.ts` -> **0** Orphaned Functions | **14** Duplicates
- `packages/yarnpkg-core/sources/execUtils.ts` -> **0** Orphaned Functions | **11** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`packages/yarnpkg-core/sources/Manifest.ts`** -> AI Confidence: **99.48%**
2. **`packages/docusaurus/src/pages/index.tsx`** -> AI Confidence: **99.31%**
3. **`packages/docusaurus/src/pages/search.tsx`** -> AI Confidence: **99.31%**
4. **`packages/plugin-git/sources/gitUtils.ts`** -> AI Confidence: **99.31%**
5. **`packages/plugin-npm-cli/sources/commands/npm/info.ts`** -> AI Confidence: **99.31%**
6. **`packages/plugin-pack/sources/packUtils.ts`** -> AI Confidence: **99.31%**
7. **`packages/plugin-version/sources/versionUtils.ts`** -> AI Confidence: **99.31%**
8. **`packages/yarnpkg-core/sources/Cache.ts`** -> AI Confidence: **99.31%**
9. **`packages/yarnpkg-core/sources/Configuration.ts`** -> AI Confidence: **99.31%**
10. **`packages/yarnpkg-core/sources/LegacyMigrationResolver.ts`** -> AI Confidence: **99.31%**
11. **`packages/yarnpkg-core/sources/Project.ts`** -> AI Confidence: **99.31%**
12. **`packages/yarnpkg-core/sources/StreamReport.ts`** -> AI Confidence: **99.31%**
13. **`packages/yarnpkg-core/sources/TelemetryManager.ts`** -> AI Confidence: **99.31%**
14. **`packages/yarnpkg-core/sources/Workspace.ts`** -> AI Confidence: **99.31%**
15. **`packages/yarnpkg-core/sources/execUtils.ts`** -> AI Confidence: **99.31%**
16. **`packages/yarnpkg-core/sources/tgzUtils.ts`** -> AI Confidence: **99.31%**
17. **`packages/yarnpkg-pnp/sources/loader/applyPatch.ts`** -> AI Confidence: **99.31%**
18. **`packages/yarnpkg-pnp/sources/loader/makeApi.ts`** -> AI Confidence: **99.31%**
19. **`packages/yarnpkg-pnpify/sources/NodeModulesFS.ts`** -> AI Confidence: **99.31%**
20. **`packages/yarnpkg-shell/sources/index.ts`** -> AI Confidence: **99.31%**
21. **`jest.config.js`** -> AI Confidence: **99.29%**
22. **`packages/acceptance-tests/pkg-tests-fixtures/default-index.js`** -> AI Confidence: **99.29%**
23. **`packages/acceptance-tests/pkg-tests-fixtures/packages/@babel__traverse-7.99.0/index.js`** -> AI Confidence: **99.29%**
24. **`packages/acceptance-tests/pkg-tests-fixtures/packages/@private__has-bin-entry-1.0.0/index.js`** -> AI Confidence: **99.29%**
25. **`packages/acceptance-tests/pkg-tests-fixtures/packages/@private__package-1.0.0/index.js`** -> AI Confidence: **99.29%**
26. **`packages/acceptance-tests/pkg-tests-fixtures/packages/@private__unconventional-tarball-1.0.0/index.js`** -> AI Confidence: **99.29%**
27. **`packages/acceptance-tests/pkg-tests-fixtures/packages/@scoped__release-date-1.0.0/index.js`** -> AI Confidence: **99.29%**
28. **`packages/acceptance-tests/pkg-tests-fixtures/packages/@scoped__release-date-1.1.0/index.js`** -> AI Confidence: **99.29%**
29. **`packages/acceptance-tests/pkg-tests-fixtures/packages/@scoped__release-date-1.1.1/index.js`** -> AI Confidence: **99.29%**
30. **`packages/acceptance-tests/pkg-tests-fixtures/packages/@scoped__release-date-1.1.2/index.js`** -> AI Confidence: **99.29%**
31. **`packages/acceptance-tests/pkg-tests-fixtures/packages/@types__babel_traverse-7.99.0/index.js`** -> AI Confidence: **99.29%**
32. **`packages/acceptance-tests/pkg-tests-fixtures/packages/@types__is-number-1.0.0/index.js`** -> AI Confidence: **99.29%**
33. **`packages/acceptance-tests/pkg-tests-fixtures/packages/@types__is-number-2.0.0/index.js`** -> AI Confidence: **99.29%**
34. **`packages/acceptance-tests/pkg-tests-fixtures/packages/has-bin-entries-1.0.0/index.js`** -> AI Confidence: **99.29%**
35. **`packages/acceptance-tests/pkg-tests-fixtures/packages/has-bin-entries-2.0.0/index.js`** -> AI Confidence: **99.29%**
36. **`packages/acceptance-tests/pkg-tests-fixtures/packages/has-symlinks-1.0.0/index.js`** -> AI Confidence: **99.29%**
37. **`packages/acceptance-tests/pkg-tests-fixtures/packages/has-symlinks-1.0.0/symlink.js`** -> AI Confidence: **99.29%**
38. **`packages/acceptance-tests/pkg-tests-fixtures/packages/has-types-1.0.0/index.js`** -> AI Confidence: **99.29%**
39. **`packages/acceptance-tests/pkg-tests-fixtures/packages/hoisting-peer-check-child-1.0.0/index.js`** -> AI Confidence: **99.29%**
40. **`packages/acceptance-tests/pkg-tests-fixtures/packages/hoisting-peer-check-parent-1.0.0/index.js`** -> AI Confidence: **99.29%**
41. **`packages/acceptance-tests/pkg-tests-fixtures/packages/inject-node-gyp-1.0.0/index.js`** -> AI Confidence: **99.29%**
42. **`packages/acceptance-tests/pkg-tests-fixtures/packages/invalid-main-1.0.0/index.js`** -> AI Confidence: **99.29%**
43. **`packages/acceptance-tests/pkg-tests-fixtures/packages/is-number-1.0.0/index.js`** -> AI Confidence: **99.29%**
44. **`packages/acceptance-tests/pkg-tests-fixtures/packages/is-number-2.0.0/index.js`** -> AI Confidence: **99.29%**
45. **`packages/acceptance-tests/pkg-tests-fixtures/packages/left-pad-1.0.0/index.js`** -> AI Confidence: **99.29%**
46. **`packages/acceptance-tests/pkg-tests-fixtures/packages/native-1.0.0/index.js`** -> AI Confidence: **99.29%**
47. **`packages/acceptance-tests/pkg-tests-fixtures/packages/native-bar-x64-1.0.0/index.js`** -> AI Confidence: **99.29%**
48. **`packages/acceptance-tests/pkg-tests-fixtures/packages/native-foo-x64-1.0.0/index.js`** -> AI Confidence: **99.29%**
49. **`packages/acceptance-tests/pkg-tests-fixtures/packages/native-foo-x86-1.0.0/index.js`** -> AI Confidence: **99.29%**
50. **`packages/acceptance-tests/pkg-tests-fixtures/packages/native-libc-glibc-1.0.0/index.js`** -> AI Confidence: **99.29%**
51. **`packages/acceptance-tests/pkg-tests-fixtures/packages/native-libc-musl-1.0.0/index.js`** -> AI Confidence: **99.29%**
52. **`packages/acceptance-tests/pkg-tests-fixtures/packages/node-gyp-1.0.0/index.js`** -> AI Confidence: **99.29%**
53. **`packages/acceptance-tests/pkg-tests-fixtures/packages/optional-native-1.0.0/index.js`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `packages/plugin-compat/extra/debugPatch.js` -> **100.0%** Exposure
- `packages/yarnpkg-libzip/sources/libzipAsync.js` -> **100.0%** Exposure
- `packages/yarnpkg-libzip/sources/libzipSync.js` -> **100.0%** Exposure
- `packages/yarnpkg-pnp/sources/node/resolve.js` -> **100.0%** Exposure
- `packages/acceptance-tests/pkg-tests-core/sources/utils/tests.ts` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `packages/plugin-compat/extra/debugPatch.js` -> **100.0%** Exposure
- `scripts/setup-local-plugins.js` -> **100.0%** Exposure
- `packages/plugin-constraints/sources/Constraints.ts` -> **100.0%** Exposure
- `packages/plugin-essentials/sources/commands/entries/clipanion.ts` -> **100.0%** Exposure
- `packages/plugin-essentials/sources/commands/entries/run.ts` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `packages/plugin-compat/extra/fsevents/fsevents-1.2.11.js` -> **100.0%** Exposure
- `packages/yarnpkg-libzip/sources/libzipAsync.js` -> **100.0%** Exposure
- `packages/yarnpkg-libzip/sources/libzipSync.js` -> **100.0%** Exposure
- `packages/acceptance-tests/pkg-tests-core/sources/utils/tests.ts` -> **100.0%** Exposure
- `packages/docusaurus/config/docusaurus/plugins/webpack-config.ts` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `12` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `951` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `packages/yarnpkg-shell/sources/index.ts` (TYPESCRIPT) -> Cumulative Risk: **924.62**
- **Archetype:** `file_cluster_4` (Distance: 11.814 IQR)
- **Magnitude:** 171.94 | **LOC:** 1090 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `executeCommandChainImpl` (Impact: 745.0), `interpolateArguments` (Impact: 325.7), `getFileDescriptorStream` (Impact: 49.9)

### 2. `packages/yarnpkg-shell/sources/pipe.ts` (TYPESCRIPT) -> Cumulative Risk: **921.17**
- **Archetype:** `file_cluster_4` (Distance: 12.138 IQR)
- **Magnitude:** 36.68 | **LOC:** 348 | **CtrlFlow:** 48.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Algorithmic Dos (99.9998%)
- **Heaviest Functions:** `makeProcess` (Impact: 89.0), `createStreamReporter` (Impact: 32.4), `exec` (Impact: 28.2)

### 3. `packages/yarnpkg-libzip/sources/ZipFS.ts` (TYPESCRIPT) -> Cumulative Risk: **917.55**
- **Archetype:** `file_cluster_4` (Distance: 13.781 IQR)
- **Magnitude:** 130.69 | **LOC:** 1527 | **CtrlFlow:** 62.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `resolveFilename` (Impact: 150.2), `existsSync` (Impact: 28.8), `toUnixTimestamp` (Impact: 23.5)

### 4. `packages/yarnpkg-core/sources/miscUtils.ts` (TYPESCRIPT) -> Cumulative Risk: **913.67**
- **Archetype:** `file_cluster_4` (Distance: 13.665 IQR)
- **Magnitude:** 40.1 | **LOC:** 668 | **CtrlFlow:** 31.4% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9981%)
- **Heaviest Functions:** `convertMapsToIndexableObjects` (Impact: 30.8), `set` (Impact: 21.8), `releaseAfterUseAsync` (Impact: 10.5)

### 5. `packages/yarnpkg-core/sources/Workspace.ts` (TYPESCRIPT) -> Cumulative Risk: **903.36**
- **Archetype:** `file_cluster_4` (Distance: 13.515 IQR)
- **Magnitude:** 35.7 | **LOC:** 231 | **CtrlFlow:** 48.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `visitWorkspace` (Impact: 48.8), `visitWorkspace` (Impact: 40.8), `accepts` (Impact: 27.6)

### 6. `scripts/extract-hooks.ts` (TYPESCRIPT) -> Cumulative Risk: **896.32**
- **Archetype:** `file_cluster_4` (Distance: 10.183 IQR)
- **Magnitude:** 18.58 | **LOC:** 133 | **CtrlFlow:** 55.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Injection Surface (100.0%), Algorithmic Dos (99.9998%)
- **Heaviest Functions:** `processFile` (Impact: 70.7), `execute` (Impact: 54.0), `execute` (Impact: 5.4)

### 7. `packages/plugin-npm-cli/sources/commands/npm/publish.ts` (TYPESCRIPT) -> Cumulative Risk: **883.83**
- **Archetype:** `file_cluster_4` (Distance: 11.682 IQR)
- **Magnitude:** 23.96 | **LOC:** 198 | **CtrlFlow:** 56.7% | **Authorship Centralization:** 25.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `execute` (Impact: 107.4)

### 8. `packages/plugin-essentials/sources/commands/plugin/import.ts` (TYPESCRIPT) -> Cumulative Risk: **881.81**
- **Archetype:** `file_cluster_4` (Distance: 12.25 IQR)
- **Magnitude:** 18.97 | **LOC:** 152 | **CtrlFlow:** 43.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `execute` (Impact: 72.6), `runInNewContext` (Impact: 1.6), `savePlugin` (Impact: 1.1)

### 9. `packages/acceptance-tests/pkg-tests-core/sources/utils/tests.ts` (TYPESCRIPT) -> Cumulative Risk: **878.65**
- **Archetype:** `file_cluster_4` (Distance: 11.654 IQR)
- **Magnitude:** 86.98 | **LOC:** 1159 | **CtrlFlow:** 40.1% | **Authorship Centralization:** 80.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `getName` (Impact: 206.1), `staticServer` (Impact: 64.8), `void` (Impact: 45.8)

### 10. `packages/plugin-essentials/sources/commands/entries/clipanion.ts` (TYPESCRIPT) -> Cumulative Risk: **877.63**
- **Archetype:** `file_cluster_4` (Distance: 10.856 IQR)
- **Magnitude:** 4.49 | **LOC:** 54 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `execute` (Impact: 19.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `packages/yarnpkg-libzip/sources/libzipAsync.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.011 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.649 IQR)
- **Top Global Matches:** file_cluster_8: 13.011, file_cluster_4: 13.199, file_cluster_11: 13.309
- **Magnitude:** 1111.66 | **LOC:** 987 | **CtrlFlow:** 38.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (77.4869%), Tech Debt (13.7198%)
**Top Internal Functions/Classes:**
  * `getValue` (Impact: 79.2 | O(2^N))
  * `stringToUTF8Array` (Impact: 65.4 | O(N^2) | DB: 5)
  * `ccall` (Impact: 60.8 | O(N^3) | DB: 10)
  * `createWasm` (Impact: 46.3 | O(N^4) | DB: 11)
  * `run` (Impact: 32.7 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 179`, `structural_boundaries: 290`, `args: 126`, `func_start: 134`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 363`, `duplicate_logic: 2`, `orphaned_logic: 1`
* *Architecture:* `io: 10`, `api: 1`, `concurrency: 38`, `import: 3`
* *Defense:* `safety: 59`, `test: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.768
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` fs, path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/yarnpkg-libzip/sources/libzipSync.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.27 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.436 IQR)
- **Top Global Matches:** file_cluster_8: 13.27, file_cluster_11: 13.572, file_cluster_17: 13.577
- **Magnitude:** 1047.76 | **LOC:** 772 | **CtrlFlow:** 42.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (75.7794%), Tech Debt (14.3828%)
**Top Internal Functions/Classes:**
  * `getValue` (Impact: 79.2 | O(2^N))
  * `stringToUTF8Array` (Impact: 65.4 | O(N^2) | DB: 5)
  * `ccall` (Impact: 60.8 | O(N^3) | DB: 10)
  * `run` (Impact: 32.7 | O(N^3))
  * `callRuntimeCallbacks` (Impact: 32.1 | O(N^3) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 173`, `structural_boundaries: 234`, `args: 67`, `func_start: 128`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 375`, `duplicate_logic: 2`
* *Architecture:* `io: 6`, `api: 2`, `concurrency: 8`, `import: 3`
* *Defense:* `safety: 53`, `test: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.923
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001608
  * `Imports (Out-Degree: 1):` fs, path
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/yarnpkg-pnp/sources/node/resolve.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.267 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.454 IQR)
- **Top Global Matches:** file_cluster_8: 11.267, file_cluster_13: 11.67, file_cluster_0: 11.813
- **Magnitude:** 565.98 | **LOC:** 518 | **CtrlFlow:** 67.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (24.0796%), Tech Debt (71.3838%)
**Top Internal Functions/Classes:**
  * `resolvePackageTarget` (Impact: 266.1 | O(2^N) | DB: 5)
  * `resolvePackageTargetString` (Impact: 84.4 | O(N^2) | DB: 1)
  * `isConditionalExportsMainSugar` (Impact: 31.2 | O(N^2) | DB: 3)
  * `StringPrototypeSlice` (Impact: 25.9 | O(2^N))
  * `StringPrototypeSlice` (Impact: 19.5 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 109`, `structural_boundaries: 52`, `args: 15`, `func_start: 45`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 51`, `dead_code: 1`, `duplicate_logic: 6`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `safety: 47`, `doc: 1`, `immutability_locks: 42`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.768
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` errors.js, primordials.js, package_config.js, url
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/yarnpkg-core/sources/Project.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.689 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.713 IQR)
- **Top Global Matches:** file_cluster_4: 13.689, file_cluster_13: 13.871, file_cluster_11: 14.004
- **Magnitude:** 397.19 | **LOC:** 2771 | **CtrlFlow:** 61.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 209
- **Risk Profile:** Cognitive Load (89.4151%), Tech Debt (14.6266%)
**Top Internal Functions/Classes:**
  * `makeLockfileChecksum` (Impact: 2757.4 | O(2^N) | DB: 209)
  * `emitPeerDependencyWarnings` (Impact: 90.8 | O(N^3) | DB: 3)
  * `fn` (Impact: 39.7 | O(N^3) | DB: 9)
  * `resolveWorkspaceRange` (Impact: 20.6 | O(N^3))
  * `allPeerRequestsWithRoot` (Impact: 11.5 | O(N^2) | DB: 3)
    * *Intent:* // If we operate with a frozen lockfile, we take a snapshot of it to later make sure it didn't chang...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 362`, `structural_boundaries: 228`, `args: 90`, `func_start: 56`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 604`, `planned_debt: 4`, `duplicate_logic: 2`
* *Architecture:* `io: 3`, `api: 34`, `concurrency: 381`, `import: 41`
* *Defense:* `safety: 59`, `doc: 15`, `sync_locks: 2`, `immutability_locks: 303`, `cleanup: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.113
  * `Choke Point (Betweenness):` 0.000773 | `Ripple Effect (Closeness):` 0.019367
  * `Imports (Out-Degree: 26):` fslib, types, LockfileResolver, p-limit, LegacyMigrationResolver, Manifest, zlib, Resolver...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `packages/yarnpkg-core/sources/scriptUtils.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.651 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.037 IQR)
- **Top Global Matches:** file_cluster_4: 10.651, file_cluster_13: 10.877, file_cluster_8: 10.963
- **Magnitude:** 195.37 | **LOC:** 810 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (51.7793%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `makePathWrapper` (Impact: 1760.0 | O(2^N) | DB: 19)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 193`, `args: 47`, `func_start: 26`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 22`, `dead_code: 1`
* *Architecture:* `io: 3`, `api: 16`, `concurrency: 143`, `import: 21`
* *Defense:* `safety: 25`, `doc: 18`, `sync_locks: 6`, `immutability_locks: 107`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.955
  * `Choke Point (Betweenness):` 6.8e-05 | `Ripple Effect (Closeness):` 0.013408
  * `Imports (Out-Degree: 13):` fslib, types, p-limit, Manifest, libzip, stream, Configuration, Project...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/yarnpkg-pnpify/sources/NodeModulesFS.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.239 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.479 IQR)
- **Top Global Matches:** file_cluster_4: 14.239, file_cluster_17: 14.82, file_cluster_13: 14.836
- **Magnitude:** 181.54 | **LOC:** 649 | **CtrlFlow:** 48.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (99.9997%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `readdirPromise` (Impact: 68.8 | O(2^N) | DB: 10)
  * `readdirSync` (Impact: 68.8 | O(2^N) | DB: 10)
  * `watch` (Impact: 48.8 | O(2^N) | DB: 4)
  * `opendirPromise` (Impact: 42.3 | O(2^N) | DB: 6)
  * `opendirSync` (Impact: 42.3 | O(2^N) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 158`, `structural_boundaries: 170`, `args: 158`, `func_start: 157`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 450`, `duplicate_logic: 42`
* *Architecture:* `io: 16`, `api: 7`, `concurrency: 514`, `import: 14`
* *Defense:* `safety: 20`, `immutability_locks: 35`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.312
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002413
  * `Imports (Out-Degree: 3):` fslib, nm, dynamicRequire, fs, WatchManager, resolveNodeModulesPath, pnp
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/yarnpkg-shell/sources/index.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.814 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.919 IQR)
- **Top Global Matches:** file_cluster_4: 11.814, file_cluster_8: 12.026, file_cluster_13: 12.039
- **Magnitude:** 171.94 | **LOC:** 1090 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (93.8768%), Tech Debt (97.9407%)
**Top Internal Functions/Classes:**
  * `executeCommandChainImpl` (Impact: 745.0 | O(2^N) | DB: 12)
  * `interpolateArguments` (Impact: 325.7 | O(2^N) | DB: 25)
  * `getFileDescriptorStream` (Impact: 49.9 | O(N^2))
  * `evaluateArithmetic` (Impact: 37.3 | O(2^N) | DB: 1)
  * `pushOutput` (Impact: 32.8 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 245`, `structural_boundaries: 219`, `args: 114`, `func_start: 76`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 157`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 14`
* *Architecture:* `io: 1`, `api: 12`, `concurrency: 124`, `import: 12`
* *Defense:* `safety: 12`, `doc: 2`, `immutability_locks: 92`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.768
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` fslib, chalk, globUtils, pipe, entry, os, stream, parsers...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/acceptance-tests/pkg-tests-fixtures/repositories/no-lockfile-project.git/hooks/fsmonitor-watchman.sample` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 16.024 IQR)
- **Top Global Matches:** file_cluster_0: 16.024, file_cluster_13: 16.284, file_cluster_11: 16.327
- **Magnitude:** 157.42 | **LOC:** 175 | **CtrlFlow:** 57.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `watchman_query` (Impact: 67.5 | O(N^1) | DB: 23)
  * `output_result` (Impact: 4.2 | O(N^1))
  * `watchman_clock` (Impact: 3.4 | O(N^1) | DB: 1)
  * `launch_watchman` (Impact: 2.3 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 31`, `args: 2`, `func_start: 6`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 78`, `dead_code: 4`
* *Architecture:* `io: 1`, `import: 7`
* *Defense:* `safety: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.768
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` output, JSON::XS, JSON::PP, warnings, the, strict, IPC::Open2, Cwd
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/yarnpkg-core/sources/Configuration.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.515 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.526 IQR)
- **Top Global Matches:** file_cluster_4: 12.515, file_cluster_13: 12.631, file_cluster_0: 12.824
- **Magnitude:** 139.38 | **LOC:** 2084 | **CtrlFlow:** 56.4% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 115
- **Risk Profile:** Cognitive Load (77.4876%), Tech Debt (9.2442%)
**Top Internal Functions/Classes:**
  * `parseSingleValue` (Impact: 1107.9 | O(N^3) | DB: 115)
  * `parseValue` (Impact: 34.0 | O(N^2) | DB: 15)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 234`, `structural_boundaries: 181`, `args: 52`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 126`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `io: 29`, `api: 18`, `concurrency: 94`, `import: 32`
* *Defense:* `safety: 51`, `doc: 3`, `immutability_locks: 110`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.537
  * `Choke Point (Betweenness):` 0.000991 | `Ripple Effect (Closeness):` 0.02286
  * `Imports (Out-Degree: 21):` fslib, TelemetryManager, types, p-limit, Manifest, tty, stream, WorkspaceResolver...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `packages/yarnpkg-libzip/sources/ZipFS.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.781 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.812 IQR)
- **Top Global Matches:** file_cluster_4: 13.781, file_cluster_13: 14.069, file_cluster_11: 14.151
- **Magnitude:** 130.69 | **LOC:** 1527 | **CtrlFlow:** 62.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (95.6834%), Tech Debt (99.998%)
**Top Internal Functions/Classes:**
  * `resolveFilename` (Impact: 150.2 | O(2^N) | DB: 14)
  * `existsSync` (Impact: 28.8 | O(2^N) | DB: 8)
  * `toUnixTimestamp` (Impact: 23.5 | O(N^1))
  * `setFileSource` (Impact: 21.7 | O(2^N) | DB: 7)
  * `destroy` (Impact: 21.5 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 211`, `structural_boundaries: 127`, `args: 139`, `func_start: 129`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 539`, `duplicate_logic: 38`
* *Architecture:* `io: 14`, `api: 31`, `concurrency: 174`, `import: 15`
* *Defense:* `safety: 22`, `doc: 3`, `immutability_locks: 112`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.004
  * `Choke Point (Betweenness):` 6e-05 | `Ripple Effect (Closeness):` 0.006433
  * `Imports (Out-Degree: 3):` fslib, fs, zlib, libzipImpl, stream, util
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `packages/acceptance-tests/pkg-tests-core/sources/utils/tests.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.654 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.917 IQR)
- **Top Global Matches:** file_cluster_4: 11.654, file_cluster_13: 11.793, file_cluster_11: 11.894
- **Magnitude:** 86.98 | **LOC:** 1159 | **CtrlFlow:** 40.1% | **Authorship Centralization:** 80.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 35
- **Risk Profile:** Cognitive Load (75.8907%), Tech Debt (81.792%)
**Top Internal Functions/Classes:**
  * `getName` (Impact: 206.1 | O(2^N) | DB: 35)
  * `staticServer` (Impact: 64.8 | O(N^3) | DB: 6)
  * `void` (Impact: 45.8 | O(N^3) | DB: 1)
  * `processError` (Impact: 37.4 | O(2^N) | DB: 6)
  * `needsAuth` (Impact: 34.5 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 193`, `structural_boundaries: 288`, `args: 86`, `func_start: 58`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 101`, `planned_debt: 1`, `duplicate_logic: 9`
* *Architecture:* `io: 41`, `api: 34`, `concurrency: 146`, `import: 27`
* *Defense:* `safety: 34`, `test: 1`, `immutability_locks: 120`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.426
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003619
  * `Imports (Out-Degree: 2):` fslib, zlib, https, stream, uuid, serve-static, net, http...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/plugin-compat/extra/fsevents/fsevents-2.2.0.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.206 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.117 IQR)
- **Top Global Matches:** file_cluster_4: 12.206, file_cluster_13: 12.248, file_cluster_8: 12.304
- **Magnitude:** 84.02 | **LOC:** 85 | **CtrlFlow:** 47.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (52.4628%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `watch` (Impact: 33.2 | O(2^N) | DB: 18)
  * `getEventType` (Impact: 14.4 | O(N^1))
  * `getFileType` (Impact: 7.2 | O(N^1))
  * `anyIsTrue` (Impact: 5.5 | O(N^1) | DB: 1)
  * `getInfo` (Impact: 2.2 | O(N^1) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 22`, `args: 7`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 12`
* *Architecture:* `io: 7`, `api: 3`, `concurrency: 3`, `import: 2`
* *Defense:* `safety: 14`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.768
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` fsevents.node, vfs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/plugin-compat/extra/fsevents/fsevents-1.2.11.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.96 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.281 IQR)
- **Top Global Matches:** file_cluster_13: 11.96, file_cluster_4: 12.042, file_cluster_11: 12.187
- **Magnitude:** 83.42 | **LOC:** 109 | **CtrlFlow:** 41.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 37
- **Risk Profile:** Cognitive Load (90.1082%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `watch` (Impact: 16.8 | O(N^2) | DB: 37)
  * `getEventType` (Impact: 10.8 | O(N^1))
  * `FSEvents` (Impact: 7.4 | O(2^N) | DB: 6)
  * `getFileType` (Impact: 7.2 | O(N^1))
  * `proxies` (Impact: 2.2 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 23`, `args: 13`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 23`
* *Architecture:* `io: 18`, `api: 4`, `concurrency: 6`, `import: 5`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.768
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` events, fs, bindings, util, vfs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/acceptance-tests/pkg-tests-fixtures/repositories/no-lockfile-project.git/hooks/pre-rebase.sample` (SHELL | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.472 IQR)
- **Top Global Matches:** file_cluster_8: 10.472, file_cluster_12: 11.111, file_cluster_7: 11.114
- **Magnitude:** 81.72 | **LOC:** 170 | **CtrlFlow:** 71.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (80.4164%), Tech Debt (99.0166%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` (Impact: 18.7 | O(N^1) | DB: 17)
  * `Anonymous_Block` (Impact: 18.6 | O(N^1) | DB: 21)
  * `Anonymous_Block_[Truncated]` (Impact: 11.7 | O(N^2))
  * `__global_context__` (Impact: 3.4 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 11`, `args: 5`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 27`, `duplicate_logic: 2`, `orphaned_logic: 2`
* *Architecture:* `io: 15`
* *Defense:* `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.768
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/acceptance-tests/pkg-tests-fixtures/repositories/no-lockfile-project.git/hooks/update.sample` (SHELL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.45 IQR)
- **Top Global Matches:** file_cluster_11: 13.45, file_cluster_17: 13.525, file_cluster_0: 13.55
- **Magnitude:** 78.24 | **LOC:** 129 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 37
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block_[Truncated]` (Impact: 20.9 | O(N^1) | DB: 37)
  * `Anonymous_Block` (Impact: 5.3 | O(N^1) | DB: 27)
    * *Intent:* # --- Safety check
  * `Anonymous_Block` (Impact: 4.2 | O(N^1) | DB: 5)
  * `Anonymous_Block` (Impact: 3.3 | O(N^1) | DB: 6)
  * `Anonymous_Block` (Impact: 3.2 | O(N^1) | DB: 21)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 14`, `args: 3`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 37`, `dead_code: 1`, `duplicate_logic: 4`, `orphaned_logic: 2`
* *Architecture:* `io: 33`
* *Defense:* `test: 1`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.768
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/yarnpkg-pnp/sources/loader/makeApi.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.692 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.406 IQR)
- **Top Global Matches:** file_cluster_13: 11.692, file_cluster_8: 11.782, file_cluster_11: 11.918
- **Magnitude:** 72.83 | **LOC:** 1028 | **CtrlFlow:** 65.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 61
- **Risk Profile:** Cognitive Load (30.4375%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `makeApi` (Impact: 660.1 | O(N^4) | DB: 61)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 147`, `structural_boundaries: 78`, `args: 35`, `func_start: 29`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 57`
* *Architecture:* `io: 12`, `api: 3`, `import: 10`
* *Defense:* `safety: 25`, `doc: 10`, `immutability_locks: 64`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.814
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004308
  * `Imports (Out-Degree: 3):` fslib, types, node-options.js, module, resolve.js, internalTools, nodeUtils, util...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/plugin-pnp/sources/PnpLinker.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.2 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.685 IQR)
- **Top Global Matches:** file_cluster_4: 12.2, file_cluster_13: 12.749, file_cluster_8: 12.862
- **Magnitude:** 71.33 | **LOC:** 518 | **CtrlFlow:** 46.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (97.2496%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `locateNodeModules` (Impact: 53.0 | O(N^2) | DB: 4)
  * `installPackage` (Impact: 52.4 | O(N^2) | DB: 21)
  * `finalizeInstallWithPnp` (Impact: 35.8 | O(N^2) | DB: 10)
  * `finalizeInstall` (Impact: 23.8 | O(N^2) | DB: 21)
  * `shouldBeUnplugged` (Impact: 16.9 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 95`, `args: 29`, `func_start: 23`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 215`
* *Architecture:* `io: 3`, `api: 12`, `concurrency: 181`, `import: 9`
* *Defense:* `safety: 4`, `doc: 1`, `immutability_locks: 72`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001206
  * `Imports (Out-Degree: 3):` jsInstallUtils, fslib, clipanion, pnpUtils, core, index, pnp
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/yarnpkg-libzip/sources/libzipImpl.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.326 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.023 IQR)
- **Top Global Matches:** file_cluster_13: 15.326, file_cluster_0: 15.381, file_cluster_11: 15.443
- **Magnitude:** 70.74 | **LOC:** 312 | **CtrlFlow:** 67.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 42
- **Risk Profile:** Cognitive Load (71.3776%), Tech Debt (41.4637%)
**Top Internal Functions/Classes:**
  * `getBufferAndClose` (Impact: 40.9 | O(N^2) | DB: 42)
  * `getFileSource` (Impact: 33.0 | O(N^2) | DB: 21)
  * `constructor` (Impact: 28.2 | O(N^2) | DB: 31)
  * `setFileSource` (Impact: 19.0 | O(N^2) | DB: 14)
  * `allocateBuffer` (Impact: 10.2 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 26`, `args: 20`, `func_start: 20`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 492`, `duplicate_logic: 2`
* *Architecture:* `io: 3`, `api: 11`, `import: 4`
* *Defense:* `safety: 17`, `immutability_locks: 48`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.058
  * `Choke Point (Betweenness):` 2.4e-05 | `Ripple Effect (Closeness):` 0.005147
  * `Imports (Out-Degree: 2):` fslib, ZipFS, libzip, instance
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/acceptance-tests/pkg-tests-fixtures/packages/path-parse-1.0.6/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.01 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.331 IQR)
- **Top Global Matches:** file_cluster_8: 13.01, file_cluster_0: 13.261, file_cluster_11: 13.269
- **Magnitude:** 70.06 | **LOC:** 94 | **CtrlFlow:** 65.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (92.2342%), Tech Debt (99.6272%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 15.9 | O(N^2) | DB: 4)
  * `parse` (Impact: 9.4 | O(N^2) | DB: 4)
  * `win32SplitPath` (Impact: 7.5 | O(N^1) | DB: 2)
    * *Intent:* // Function to split a filename into [root, dir, basename, ext]
  * `posixSplitPath` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 14`, `args: 4`, `func_start: 4`
* *Risk/State:* `state_mutation: 30`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 4`
* *Defense:* `safety: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.768
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/plugin-compat/extra/fsevents/vfs.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.769 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.643 IQR)
- **Top Global Matches:** file_cluster_17: 12.769, file_cluster_13: 12.908, file_cluster_8: 13.058
- **Magnitude:** 69.66 | **LOC:** 77 | **CtrlFlow:** 43.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (72.1594%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `getVirtualLookupFn` (Impact: 11.9 | O(N^1) | DB: 3)
  * `transpose` (Impact: 6.7 | O(N^2) | DB: 3)
  * `wrap` (Impact: 4.6 | O(N^2) | DB: 7)
  * `constructor` (Impact: 3.0 | O(N^1) | DB: 7)
  * `constructor` (Impact: 1.6 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 17`, `args: 11`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 37`, `duplicate_logic: 4`
* *Architecture:* `io: 5`, `api: 2`, `import: 2`
* *Defense:* `safety: 6`, `test: 1`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.639
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003619
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/plugin-compat/extra/fsevents/fsevents-2.1.2.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.514 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.168 IQR)
- **Top Global Matches:** file_cluster_4: 11.514, file_cluster_13: 11.558, file_cluster_8: 11.614
- **Magnitude:** 69.02 | **LOC:** 80 | **CtrlFlow:** 43.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (53.7806%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `watch` (Impact: 18.3 | O(2^N) | DB: 18)
  * `getEventType` (Impact: 14.4 | O(N^1))
  * `getFileType` (Impact: 7.2 | O(N^1))
  * `anyIsTrue` (Impact: 5.5 | O(N^1) | DB: 1)
  * `getInfo` (Impact: 2.2 | O(N^1) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 22`, `args: 7`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 12`
* *Architecture:* `io: 7`, `api: 3`, `concurrency: 3`, `import: 2`
* *Defense:* `safety: 7`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.768
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` fsevents.node, vfs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/actions/sherlock-prepare.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.322 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 7.565 IQR)
- **Top Global Matches:** file_cluster_4: 13.322, file_cluster_13: 13.73, file_cluster_11: 14.141
- **Magnitude:** 64.78 | **LOC:** 82 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (50.0%), Tech Debt (87.1217%)
**Top Internal Functions/Classes:**
  * `yarn` (Impact: 14.8 | O(2^N) | DB: 3)
  * `packageJson` (Impact: 1.1 | O(N^1))
    * *Intent:* /**
  * `packageJsonAndInstall` (Impact: 1.1 | O(N^1))
    * *Intent:* /** * Creates a package.json file in the current folder, and an `index.js` that * returns the conten...
  * `node` (Impact: 1.1 | O(N^1))
    * *Intent:* /** * Calls the right Yarn binary (which has been built from master). *
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 19`, `args: 7`, `func_start: 4`
* *Risk/State:* `state_mutation: 9`, `orphaned_logic: 1`
* *Architecture:* `io: 3`, `api: 1`, `concurrency: 36`, `import: 5`
* *Defense:* `safety: 5`, `doc: 4`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.768
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` package.json
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/yarnpkg-core/sources/Cache.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.976 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.798 IQR)
- **Top Global Matches:** file_cluster_4: 12.976, file_cluster_13: 13.345, file_cluster_11: 13.601
- **Magnitude:** 64.57 | **LOC:** 525 | **CtrlFlow:** 51.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 37
- **Risk Profile:** Cognitive Load (81.3053%), Tech Debt (14.1965%)
**Top Internal Functions/Classes:**
  * `getLocatorPath` (Impact: 372.5 | O(2^N) | DB: 37)
  * `splitChecksumComponents` (Impact: 16.8 | O(N^1))
  * `getChecksumFilename` (Impact: 15.6 | O(N^1) | DB: 2)
  * `mirrorCwd` (Impact: 10.7 | O(2^N) | DB: 3)
  * `getCacheKey` (Impact: 4.8 | O(N^1))
    * *Intent:* /** * The cache version, on the other hand, is meant to be bumped every time we * change the archive...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 68`, `args: 22`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 118`, `fragile_debt: 1`
* *Architecture:* `io: 5`, `api: 4`, `concurrency: 94`, `import: 14`
* *Defense:* `safety: 13`, `doc: 4`, `sync_locks: 6`, `immutability_locks: 42`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.145
  * `Choke Point (Betweenness):` 9.8e-05 | `Ripple Effect (Closeness):` 0.014229
  * `Imports (Out-Degree: 8):` fslib, types, crypto, fs, structUtils, miscUtils, libzip, Report...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/yarnpkg-pnp/sources/node/package_config.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.166 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.437 IQR)
- **Top Global Matches:** file_cluster_8: 11.166, file_cluster_13: 11.185, file_cluster_0: 11.599
- **Magnitude:** 62.62 | **LOC:** 121 | **CtrlFlow:** 56.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 28
- **Risk Profile:** Cognitive Load (26.0829%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getPackageConfig` (Impact: 34.6 | O(N^1) | DB: 28)
  * `getPackageScopeConfig` (Impact: 10.1 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 13`, `args: 2`, `func_start: 3`
* *Risk/State:* `state_mutation: 14`
* *Architecture:* `io: 8`, `api: 2`, `import: 4`
* *Defense:* `safety: 13`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.768
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` errors.js, primordials.js, util.js, url
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/yarnpkg-nm/sources/buildNodeModulesTree.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.229 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.007 IQR)
- **Top Global Matches:** file_cluster_13: 12.229, file_cluster_2: 12.258, file_cluster_8: 12.331
- **Magnitude:** 57.8 | **LOC:** 736 | **CtrlFlow:** 62.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (33.283%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `addPackageToTree` (Impact: 200.3 | O(N^3) | DB: 10)
  * `buildWorkspaceMap` (Impact: 111.7 | O(N^3) | DB: 8)
  * `dumpDepTree` (Impact: 40.6 | O(N^2) | DB: 2)
  * `buildLocatorMap` (Impact: 35.1 | O(N^2) | DB: 4)
    * *Intent:* /** * The workspace name suffix used internally by this implementation and appeneded to the name of ...
  * `dumpNodeModulesTree` (Impact: 33.1 | O(N^2) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 62`, `args: 28`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 102`
* *Architecture:* `api: 15`, `import: 5`
* *Defense:* `doc: 33`, `immutability_locks: 98`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.421
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001206
  * `Imports (Out-Degree: 0):` fslib, pnp, hoist, core
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `packages/yarnpkg-builder/sources/tools/findPlugins.ts` (TYPESCRIPT) | Magnitude: 0.24 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 6, branch: 4, decorators: 4
- `packages/plugin-npm/tests/_makeConfiguration.js` (JAVASCRIPT) | Magnitude: 3.48 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 10, decorators: 8, import: 4, structural_boundaries: 3
- `packages/eslint-config/rules/errors.js` (JAVASCRIPT) | Magnitude: 19.88 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 40, structural_boundaries: 12, branch: 6, decorators: 5
- `packages/vscode-zipfs/filelinks.js` (JAVASCRIPT) | Magnitude: 15.32 | Delta: **0.082 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: decorators: 12, indent_spaces: 12, io: 3, immutability_locks: 3
- `packages/yarnpkg-pnpify/sources/dynamicRequire.ts` (TYPESCRIPT) | Magnitude: 1.86 | Delta: **0.124 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, state_mutation: 6, immutability_locks: 6, structural_boundaries: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `packages/acceptance-tests/pkg-tests-fixtures/repositories/no-lockfile-project.git/hooks/update.sample` (SHELL) | Magnitude: 78.24 | Delta: **0.075 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 48, state_mutation: 37, io: 33, branch: 28
- `packages/acceptance-tests/pkg-tests-fixtures/repositories/no-lockfile-project.git/hooks/pre-push.sample` (SHELL) | Magnitude: 37.5 | Delta: **0.154 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: state_mutation: 18, indent_tabs: 17, branch: 14, structural_boundaries: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `scripts/dist-scripts/yarn` (SHELL) | Magnitude: 40.86 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 16, state_mutation: 15, branch: 14, io: 10
- `scripts/e2e-setup-ci.sh` (SHELL) | Magnitude: 3.92 | Delta: **0.103 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 15, structural_boundaries: 12, branch: 10, reflection_metaprogramming: 8
- `packages/yarnpkg-pnp/sources/node/primordials.js` (JAVASCRIPT) | Magnitude: 55.97 | Delta: **0.388 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 25, reflection_metaprogramming: 19, api: 15, immutability_locks: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/plugin-typescript/sources/typescriptUtils.ts` (TYPESCRIPT) | Magnitude: 3.0 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 15, immutability_locks: 10, branch: 8
- `packages/yarnpkg-core/sources/VirtualResolver.ts` (TYPESCRIPT) | Magnitude: 4.56 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 12, safety: 12, args: 10
- `packages/yarnpkg-builder/sources/boot-cli-dev.js` (JAVASCRIPT) | Magnitude: 11.56 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: func_start: 2, import: 2, decorators: 1
- `packages/plugin-git/sources/GitResolver.ts` (TYPESCRIPT) | Magnitude: 5.84 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 57, structural_boundaries: 27, args: 10, api: 9
- `packages/plugin-file/sources/TarballFileFetcher.ts` (TYPESCRIPT) | Magnitude: 2.48 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 20, args: 7, func_start: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `packages/yarnpkg-shell/sources/errors.ts` (TYPESCRIPT) | Magnitude: 0.51 | Delta: **0.244 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 4, structural_boundaries: 3, args: 2, func_start: 2
- `packages/yarnpkg-core/sources/ThrowReport.ts` (TYPESCRIPT) | Magnitude: 6.56 | Delta: **0.326 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 26, args: 22, func_start: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/docusaurus/src/lib/queryUtils.ts` (TYPESCRIPT) | Magnitude: 1.45 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 25, indent_spaces: 19, generics: 14, safety_bypasses: 6
- `scripts/actions/sherlock-docker.sh` (SHELL) | Magnitude: 0.55 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 3, safety: 3, state_mutation: 3, io: 2
- `packages/plugin-interactive-tools/sources/commands/upgrade-interactive.tsx` (TYPESCRIPT) | Magnitude: 49.0 | Delta: **0.066 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 319, structural_boundaries: 106, concurrency: 81, state_mutation: 68
- `packages/yarnpkg-pnp/sources/generateSerializedState.ts` (TYPESCRIPT) | Magnitude: 14.03 | Delta: **0.07 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 85, branch: 32, state_mutation: 30, structural_boundaries: 28
- `packages/docusaurus/src/components/CommandLineHighlight.tsx` (TYPESCRIPT) | Magnitude: 2.97 | Delta: **0.076 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 56, structural_boundaries: 35, branch: 17, ui_framework: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `packages/yarnpkg-libui/sources/components/Gem.tsx` (TYPESCRIPT) | Magnitude: 1.72 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 9, ui_framework: 5, indent_spaces: 4, args: 3
- `packages/docusaurus/src/pages/search.tsx` (TYPESCRIPT) | Magnitude: 7.24 | Delta: **0.08 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 167, ui_framework: 50, structural_boundaries: 45, branch: 40
- `packages/plugin-interactive-tools/sources/commands/search.tsx` (TYPESCRIPT) | Magnitude: 19.46 | Delta: **0.088 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 230, ui_framework: 71, concurrency: 68, structural_boundaries: 65
- `packages/yarnpkg-core/sources/RefCountedCache.ts` (TYPESCRIPT) | Magnitude: 7.96 | Delta: **0.089 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 41, state_mutation: 27, structural_boundaries: 11, branch: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/docusaurus/src/lib/npmTools.ts` (TYPESCRIPT) | Magnitude: 9.04 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 160, structural_boundaries: 80, branch: 54, immutability_locks: 31
- `packages/plugin-patch/sources/PatchResolver.ts` (TYPESCRIPT) | Magnitude: 5.44 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 23, concurrency: 12, args: 10
- `packages/plugin-essentials/sources/commands/info.ts` (TYPESCRIPT) | Magnitude: 45.13 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 294, branch: 94, state_mutation: 84, immutability_locks: 63
- `packages/yarnpkg-core/sources/tgzUtils.ts` (TYPESCRIPT) | Magnitude: 11.58 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 129, structural_boundaries: 56, branch: 52, concurrency: 27
- `packages/plugin-compat/extra/fsevents/fsevents-2.2.0.js` (JAVASCRIPT) | Magnitude: 84.02 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 22, branch: 20, safety: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `packages/plugin-pnp/sources/index.ts` (TYPESCRIPT) | Magnitude: 4.82 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 117, structural_boundaries: 37, branch: 23, import: 10
- `packages/plugin-npm/sources/NpmHttpFetcher.ts` (TYPESCRIPT) | Magnitude: 3.25 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 43, structural_boundaries: 22, branch: 7, args: 7
- `packages/plugin-compat/jest.config.js` (JAVASCRIPT) | Magnitude: 12.56 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: api: 1, test: 1, decorators: 1, reflection_metaprogramming: 1
- `packages/plugin-essentials/sources/dedupeUtils.ts` (TYPESCRIPT) | Magnitude: 5.29 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 171, structural_boundaries: 49, concurrency: 33, immutability_locks: 32
- `packages/plugin-exec/sources/index.ts` (TYPESCRIPT) | Magnitude: 2.03 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 6, api: 5, import: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `packages/acceptance-tests/pkg-tests-fixtures/repositories/no-lockfile-project.git/hooks/prepare-commit-msg.sample` (SHELL) | Magnitude: 5.5 | Delta: **0.068 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: args: 3, safety_bypasses: 3, state_mutation: 3, dead_code: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/yarnpkg-core/sources/Configuration.ts` -> Churn: **70.3%** | Cog Load: 77.4876% | Debt: 9.2442%
- `packages/plugin-essentials/sources/commands/install.ts` -> Churn: **60.55%** | Cog Load: 65.6011% | Debt: 99.7634%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/yarnpkg-core/sources/Project.ts` -> **Maël Nison** (100.0% isolated ownership) | Magnitude: 397.19
- `packages/yarnpkg-pnpify/sources/NodeModulesFS.ts` -> **Maël Nison** (100.0% isolated ownership) | Magnitude: 181.54
- `packages/yarnpkg-libzip/sources/ZipFS.ts` -> **Maël Nison** (100.0% isolated ownership) | Magnitude: 130.69
- `packages/yarnpkg-pnp/sources/loader/makeApi.ts` -> **Clement Yan** (100.0% isolated ownership) | Magnitude: 72.83
- `packages/plugin-pnp/sources/PnpLinker.ts` -> **Maël Nison** (100.0% isolated ownership) | Magnitude: 71.33

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/yarnpkg-core/sources/Configuration.ts` -> **Severity: 0.084** (Bridge: 0.001 * Flux: 84.3741%)
- `packages/yarnpkg-core/sources/Project.ts` -> **Severity: 0.077** (Bridge: 0.0008 * Flux: 99.9966%)
- `packages/plugin-essentials/sources/commands/entries/clipanion.ts` -> **Severity: 0.028** (Bridge: 0.0003 * Flux: 91.3876%)
- `packages/yarnpkg-cli/sources/tools/getPluginConfiguration.ts` -> **Severity: 0.024** (Bridge: 0.0002 * Flux: 99.9982%)
- `packages/yarnpkg-core/sources/Cache.ts` -> **Severity: 0.008** (Bridge: 0.0001 * Flux: 85.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/plugin-essentials/sources/commands/entries/clipanion.ts` -> **Severity: 8.421** (Embedded: 0.1059 * Error Risk: 79.492%)
- `packages/yarnpkg-cli/sources/tools/getPluginConfiguration.ts` -> **Severity: 4.377** (Embedded: 0.058 * Error Risk: 75.4915%)
- `packages/yarnpkg-cli/sources/tools/getDynamicLibs.ts` -> **Severity: 2.645** (Embedded: 0.0433 * Error Risk: 61.0639%)
- `packages/yarnpkg-parsers/sources/shell.ts` -> **Severity: 2.025** (Embedded: 0.0398 * Error Risk: 50.8333%)
- `packages/yarnpkg-core/sources/Report.ts` -> **Severity: 1.913** (Embedded: 0.0256 * Error Risk: 74.6295%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/plugin-essentials/sources/commands/entries/clipanion.ts` -> **Severity: 4093.69** (Blast Radius: 41.465 * Doc Risk: 98.7264%)
- `packages/yarnpkg-cli/sources/tools/getPluginConfiguration.ts` -> **Severity: 2237.519** (Blast Radius: 28.232 * Doc Risk: 79.2547%)
- `packages/acceptance-tests/pkg-tests-core/sources/utils/fs.ts` -> **Severity: 1345.536** (Blast Radius: 13.648 * Doc Risk: 98.5885%)
- `packages/yarnpkg-cli/sources/tools/getDynamicLibs.ts` -> **Severity: 1140.546** (Blast Radius: 24.857 * Doc Risk: 45.8843%)
- `packages/yarnpkg-parsers/sources/shell.ts` -> **Severity: 795.682** (Blast Radius: 8.264 * Doc Risk: 96.2829%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
