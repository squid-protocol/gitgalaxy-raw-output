# ARCHITECTURAL_BRIEF: puppeteer
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_web/puppeteer` |
| **Timestamp** | `2026-08-03T20:06:30.660648+00:00` |
| **Scan Duration** | `2.1s` |
| **Git Branch** | `main` |
| **Git Commit** | `bf1e9722eef723c80250119d81fd9d9e0596c074` |
| **Git Remote** | `https://github.com/puppeteer/puppeteer.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 413 malicious artifacts.

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
| Total Artifacts | 2125 |
| Analyzed Artifacts (Scanned) | 502 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1623 |
| Total LOC | 64314 |
| Volatility Index | 0.006 |
| % Scanned of codebase = | 23.6% |
| Dominant Lang | PLAINTEXT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6304 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3036 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.2135 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 8 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 361 | 58650 | 71.9% |
| JAVASCRIPT | 50 | 3064 | 10.0% |
| JSON | 48 | 2439 | 9.6% |
| PLAINTEXT | 18 | 3 | 3.6% |
| MARKDOWN | 17 | 0 | 3.4% |
| HTML | 3 | 14 | 0.6% |
| CSS | 3 | 116 | 0.6% |
| DOCKERFILE | 1 | 18 | 0.2% |
| SHELL | 1 | 10 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.576`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 241 | 48.0% |
| file_cluster_4 | 109 | 21.7% |
| file_cluster_13 | 96 | 19.1% |
| file_cluster_2 | 7 | 1.4% |
| file_cluster_16 | 6 | 1.2% |
| file_cluster_7 | 4 | 0.8% |
| file_cluster_17 | 3 | 0.6% |
| Unknown | 3 | 0.6% |
| file_cluster_1 | 1 | 0.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 32 | 6.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1623*

**Composition by Extension & Reason:**
- `.md`: 1317x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 3774 LOC)
- `.html`: 92x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 67x Excluded (Explicitly Denied Extension: '.png')
- `.js`: 32x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 45039 LOC exceeds safe regex boundaries), 1x Excluded (Static Asset Blob without Intent: 1119 LOC)
- `.yml`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Unsupported Format (.undeterminable)
- `no_extension`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.cjs`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.css`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 42 exceeds 500 chars)
- `.txt`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mjs`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.svg`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ico`: 2x Excluded (Explicitly Denied Extension: '.ico')
- `.jpg`: 2x Excluded (Explicitly Denied Extension: '.jpg')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 97.9 | 25.2 | 14.1 | 5.0 |
| Error & Exception Exposure | 0.0 | 94.4 | 27.0 | 27.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 11.5 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 7.1 | 0.0 | 0.0 |
| API Exposure | 0.0 | 19.1 | 2.7 | 0.7 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 56.1 | 98.8 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 20.9 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 23.1 | 0.2 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 91.7 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 6.1 | 1.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 89.9 | 5.9 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 24.6 | 11.9 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 23.2 | 1.1 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 16.2 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 1.3 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 35.1 | 0.1 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `packages/puppeteer-core/src/cdp/NetworkManager.test.ts` (Hits: 68)
- `test/src/page.spec.ts` (Hits: 63)
- `test/src/cookies.spec.ts` (Hits: 55)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **puppeteer.ts** (`packages/puppeteer/src/puppeteer.ts`) — 35 inbound connections
2. **puppeteer-core.ts** (`packages/puppeteer-core/src/puppeteer-core.ts`) — 8 inbound connections
3. **core.ts** (`packages/puppeteer-core/src/bidi/core/core.ts`) — 7 inbound connections
4. **json.ts** (`packages/ng-schematics/src/schematics/utils/json.ts`) — 6 inbound connections
5. **debug.ts** (`packages/browsers/src/debug.ts`) — 5 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **Page.ts** (`packages/puppeteer-core/src/cdp/Page.ts`) — 50 outbound dependencies
2. **Page.ts** (`packages/puppeteer-core/src/api/Page.ts`) — 40 outbound dependencies
3. **Page.ts** (`packages/puppeteer-core/src/bidi/Page.ts`) — 38 outbound dependencies
4. **cdp.ts** (`packages/puppeteer-core/src/cdp/cdp.ts`) — 37 outbound dependencies
5. **common.ts** (`packages/puppeteer-core/src/common/common.ts`) — 37 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `describe` (@ `test/src/launcher.spec.ts`) -> Impact: **1148.8** | LOC: 979
- `describe` (@ `test/src/requestinterception-experimental.spec.ts`) -> Impact: **944.7** | LOC: 1019
- `describe` (@ `test/src/requestinterception.spec.ts`) -> Impact: **817.6** | LOC: 1110
- `fill` (@ `packages/puppeteer-core/src/api/locators/locators.ts`) -> Impact: **641.2** | LOC: 153
  * *Intent:* /** * Creates a new locator instance by cloning the current locator and * specifying whether to wait for input elements to become enabled before the *...
- `describe` (@ `test/src/page.spec.ts`) -> Impact: **541.6** | LOC: 1652
- `SearchPageContent` (@ `website/src/theme/SearchPage/index.js`) -> Impact: **528.3** | LOC: 382
- `build` (@ `packages/browsers/src/CLI.ts`) -> Impact: **496.1** | LOC: 306
- `describe` (@ `test/src/locator.spec.ts`) -> Impact: **488.5** | LOC: 763
- `setViewport` (@ `packages/puppeteer-core/src/bidi/Page.ts`) -> Impact: **334.5** | LOC: 75
- `describe` (@ `test/src/navigation.spec.ts`) -> Impact: **299.9** | LOC: 595

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `SearchPageContent` (@ `website/src/theme/SearchPage/index.js`) -> **O(2^N) [Recursive]**
- `fill` (@ `packages/puppeteer-core/src/api/locators/locators.ts`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * Creates a new locator instance by cloning the current locator and * specifying whether to wait for input elements to become enabled before the *...
- `switchMap` (@ `packages/puppeteer-core/src/bidi/Frame.ts`) -> **O(2^N) [Recursive]**
- `addNamespace` (@ `website/docusaurus.config.js`) -> **O(2^N) [Recursive]**
- `build` (@ `packages/browsers/src/CLI.ts`) -> **O(2^N) [Recursive]**
- `describe` (@ `packages/browsers/test/src/chrome/cli.spec.ts`) -> **O(2^N) [Recursive]**
- `describe` (@ `packages/browsers/test/src/chrome/install.spec.ts`) -> **O(2^N) [Recursive]**
- `reject` (@ `packages/puppeteer-core/src/bidi/ExposedFunction.ts`) -> **O(2^N) [Recursive]**
- `setViewport` (@ `packages/puppeteer-core/src/bidi/Page.ts`) -> **O(2^N) [Recursive]**
- `evaluate` (@ `packages/puppeteer-core/src/bidi/Realm.ts`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `describe` (@ `packages/puppeteer-core/src/cdp/NetworkManager.test.ts`) -> DB Complexity: **207**
- `describe` (@ `test/src/cookies.spec.ts`) -> DB Complexity: **175**
- `describe` (@ `test/src/page.spec.ts`) -> DB Complexity: **139**
- `describe` (@ `test/src/launcher.spec.ts`) -> DB Complexity: **119**
- `describe` (@ `packages/browsers/test/src/firefox/firefox-data.spec.ts`) -> DB Complexity: **109**
- `describe` (@ `packages/browsers/test/src/chrome/install.spec.ts`) -> DB Complexity: **101**
- `describe` (@ `test/src/requestinterception.spec.ts`) -> DB Complexity: **80**
- `describe` (@ `test/src/requestinterception-experimental.spec.ts`) -> DB Complexity: **77**
- `describe` (@ `test/src/navigation.spec.ts`) -> DB Complexity: **67**
- `describe` (@ `packages/browsers/test/src/fileUtil.spec.ts`) -> DB Complexity: **64**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `packages/testserver` | 7 | 10033.52 | 1.43% | 0.0% |
| `__monolith__` | 12 | 5316.84 | 8.61% | 9.65% |
| `tools/docgen/src` | 2 | 1971.52 | 24.82% | 53.45% |
| `test/src` | 56 | 1822.29 | 34.03% | 0.0% |
| `packages/puppeteer-core/src/cdp` | 43 | 863.2 | 38.88% | 11.61% |
| `website/src/theme/SearchPage` | 2 | 556.38 | 7.75% | 49.28% |
| `packages/puppeteer-core/src/bidi` | 25 | 453.95 | 45.52% | 29.73% |
| `packages/puppeteer-core/src/api` | 22 | 292.11 | 30.61% | 8.56% |
| `packages/puppeteer-core/src/common` | 42 | 215.09 | 18.08% | 15.18% |
| `packages/puppeteer-core` | 7 | 210.9 | 23.56% | 37.44% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `packages/puppeteer-core/function-fixture.mjs` -> **100.0%** Exposure
- `docker/pack.sh` -> **100.0%** Exposure
- `packages/puppeteer-core/src/bidi/Target.ts` -> **100.0%** Exposure
- `packages/puppeteer-core/src/common/CallbackRegistry.ts` -> **100.0%** Exposure
- `packages/puppeteer-core/src/common/Errors.ts` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `docker/Dockerfile` -> **100.0%** Exposure
- `packages/ng-schematics/src/schematics/ng-add/files/common/e2e/tests/utils.ts.template` -> **100.0%** Exposure
- `packages/puppeteer-core/src/bidi/core/Realm.ts` -> **100.0%** Exposure
- `packages/puppeteer-core/src/cdp/FrameTree.ts` -> **100.0%** Exposure
- `packages/puppeteer-core/src/common/BrowserWebSocketTransport.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/puppeteer-core/src/api/locators/locators.ts` -> **4** Orphaned Functions | **32** Duplicates
- `packages/puppeteer-core/src/bidi/Target.ts` -> **0** Orphaned Functions | **31** Duplicates
- `packages/puppeteer-core/src/cdp/Input.ts` -> **0** Orphaned Functions | **19** Duplicates
- `packages/puppeteer-core/src/common/util.ts` -> **15** Orphaned Functions | **2** Duplicates
- `packages/puppeteer-core/src/bidi/core/Realm.ts` -> **0** Orphaned Functions | **15** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`tools/docgen/src/custom_markdown_documenter.ts`** -> AI Confidence: **99.48%**
2. **`packages/browsers/src/CLI.ts`** -> AI Confidence: **99.31%**
3. **`packages/browsers/src/install.ts`** -> AI Confidence: **99.31%**
4. **`packages/browsers/test/src/installWithProviders.spec.ts`** -> AI Confidence: **99.31%**
5. **`packages/puppeteer-core/src/cdp/NetworkManager.ts`** -> AI Confidence: **99.31%**
6. **`packages/puppeteer-core/src/node/BrowserLauncher.ts`** -> AI Confidence: **99.31%**
7. **`packages/puppeteer-core/src/node/ChromeLauncher.ts`** -> AI Confidence: **99.31%**
8. **`packages/puppeteer-core/src/node/FirefoxLauncher.ts`** -> AI Confidence: **99.31%**
9. **`packages/puppeteer-core/src/node/PuppeteerNode.ts`** -> AI Confidence: **99.31%**
10. **`packages/puppeteer-core/src/node/ScreenRecorder.ts`** -> AI Confidence: **99.31%**
11. **`website/archive.js`** -> AI Confidence: **99.29%**
12. **`website/static/fix-location.js`** -> AI Confidence: **99.29%**
13. **`packages/puppeteer-core/src/injected/XPathQuerySelector.ts`** -> AI Confidence: **99.29%**
14. **`tools/compare-trials.ts`** -> AI Confidence: **99.29%**
15. **`tools/merge-changelogs.ts`** -> AI Confidence: **99.29%**
16. **`packages/browsers/src/fileUtil.ts`** -> AI Confidence: **99.24%**
17. **`packages/puppeteer-core/src/bidi/CDPSession.ts`** -> AI Confidence: **99.24%**
18. **`packages/puppeteer-core/src/cdp/CdpSession.ts`** -> AI Confidence: **99.24%**
19. **`test/src/mocha-utils.ts`** -> AI Confidence: **99.24%**
20. **`website/docusaurus.config.js`** -> AI Confidence: **99.23%**
21. **`packages/puppeteer-core/src/api/HTTPRequest.ts`** -> AI Confidence: **99.23%**
22. **`packages/puppeteer-core/src/bidi/util.ts`** -> AI Confidence: **99.23%**
23. **`packages/puppeteer-core/src/cdp/Accessibility.ts`** -> AI Confidence: **99.23%**
24. **`packages/puppeteer-core/src/cdp/HTTPRequest.ts`** -> AI Confidence: **99.23%**
25. **`packages/puppeteer-core/src/injected/PQuerySelector.ts`** -> AI Confidence: **99.23%**
26. **`packages/puppeteer-core/Herebyfile.mjs`** -> AI Confidence: **99.18%**
27. **`tools/update_browser_revision.mjs`** -> AI Confidence: **99.18%**
28. **`website/src/theme/SearchBar/index.js`** -> AI Confidence: **99.18%**
29. **`packages/browsers/test/src/list.spec.ts`** -> AI Confidence: **99.18%**
30. **`packages/puppeteer-core/src/api/Browser.ts`** -> AI Confidence: **99.18%**
31. **`packages/puppeteer-core/src/api/Frame.ts`** -> AI Confidence: **99.18%**
32. **`packages/puppeteer-core/src/api/locators/locators.ts`** -> AI Confidence: **99.18%**
33. **`packages/puppeteer-core/src/bidi/BrowserConnector.ts`** -> AI Confidence: **99.18%**
34. **`packages/puppeteer-core/src/bidi/ElementHandle.ts`** -> AI Confidence: **99.18%**
35. **`packages/puppeteer-core/src/bidi/ExposedFunction.ts`** -> AI Confidence: **99.18%**
36. **`packages/puppeteer-core/src/bidi/HTTPResponse.ts`** -> AI Confidence: **99.18%**
37. **`packages/puppeteer-core/src/bidi/Realm.ts`** -> AI Confidence: **99.18%**
38. **`packages/puppeteer-core/src/bidi/core/Browser.ts`** -> AI Confidence: **99.18%**
39. **`packages/puppeteer-core/src/bidi/core/Realm.ts`** -> AI Confidence: **99.18%**
40. **`packages/puppeteer-core/src/cdp/JSHandle.ts`** -> AI Confidence: **99.18%**
41. **`packages/puppeteer-core/src/cdp/Page.ts`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `tools/clean.mjs` -> **100.0%** Exposure
- `tools/sort-test-expectations.mjs` -> **100.0%** Exposure
- `website/docusaurus.config.js` -> **100.0%** Exposure
- `packages/browsers/src/CLI.ts` -> **100.0%** Exposure
- `packages/browsers/src/Cache.ts` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `tools/clean.mjs` -> **100.0%** Exposure
- `tools/sort-test-expectations.mjs` -> **100.0%** Exposure
- `packages/browsers/test/src/chrome/launch.spec.ts` -> **100.0%** Exposure
- `packages/browsers/test/src/chromium/launch.spec.ts` -> **100.0%** Exposure
- `packages/puppeteer-core/tools/ensure-correct-devtools-protocol-package.mts` -> **100.0%** Exposure
### Hardcoded Payload Artifacts
- `website/docusaurus.config.js` -> **35.1292%** Exposure
### Algorithmic DoS Exposure
- `packages/ng-schematics/tools/projects.mjs` -> **100.0%** Exposure
- `packages/puppeteer-core/Herebyfile.mjs` -> **100.0%** Exposure
- `website/src/theme/SearchPage/index.js` -> **100.0%** Exposure
- `packages/browsers/src/CLI.ts` -> **100.0%** Exposure
- `packages/browsers/src/Cache.ts` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `810` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `packages/puppeteer-core/src/bidi/Frame.ts` (TYPESCRIPT) -> Cumulative Risk: **876.01**
- **Archetype:** `file_cluster_4` (Distance: 12.43 IQR)
- **Magnitude:** 61.15 | **LOC:** 611 | **CtrlFlow:** 32.2% | **Authorship Centralization:** 20.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `initialize` (Impact: 64.3), `switchMap` (Impact: 61.0), `realm` (Impact: 16.0)

### 2. `packages/puppeteer-core/src/util/decorators.ts` (TYPESCRIPT) -> Cumulative Risk: **826.6**
- **Archetype:** `file_cluster_13` (Distance: 11.988 IQR)
- **Magnitude:** 19.05 | **LOC:** 211 | **CtrlFlow:** 27.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Logic Bomb (99.988%)
- **Heaviest Functions:** `target` (Impact: 37.9), `bubbleInitializer` (Impact: 25.4), `bubble` (Impact: 23.9)

### 3. `packages/puppeteer-core/src/bidi/Realm.ts` (TYPESCRIPT) -> Cumulative Risk: **818.01**
- **Archetype:** `file_cluster_13` (Distance: 12.731 IQR)
- **Magnitude:** 35.23 | **LOC:** 439 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `evaluate` (Impact: 109.9), `serialize` (Impact: 56.7), `destroyHandles` (Impact: 13.1)

### 4. `packages/puppeteer-core/src/common/CallbackRegistry.ts` (TYPESCRIPT) -> Cumulative Risk: **800.06**
- **Archetype:** `file_cluster_13` (Distance: 12.174 IQR)
- **Magnitude:** 16.05 | **LOC:** 175 | **CtrlFlow:** 45.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `request` (Impact: 37.0), `constructor` (Impact: 20.7), `_reject` (Impact: 14.6)

### 5. `packages/puppeteer-core/src/api/locators/locators.ts` (TYPESCRIPT) -> Cumulative Risk: **792.45**
- **Archetype:** `file_cluster_2` (Distance: 12.485 IQR)
- **Magnitude:** 133.22 | **LOC:** 1150 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `fill` (Impact: 641.2), `scroll` (Impact: 86.7), `click` (Impact: 35.4)

### 6. `packages/puppeteer-core/src/node/ChromeLauncher.ts` (TYPESCRIPT) -> Cumulative Risk: **776.63**
- **Archetype:** `file_cluster_13` (Distance: 11.803 IQR)
- **Magnitude:** 19.68 | **LOC:** 346 | **CtrlFlow:** 49.5% | **Authorship Centralization:** 85.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), State Flux (99.9688%), Concurrency (92.6446%)
- **Heaviest Functions:** `assert` (Impact: 37.0), `executablePath` (Impact: 12.7), `assert` (Impact: 9.4)

### 7. `packages/puppeteer-core/src/node/FirefoxLauncher.ts` (TYPESCRIPT) -> Cumulative Risk: **768.3**
- **Archetype:** `file_cluster_4` (Distance: 12.248 IQR)
- **Magnitude:** 16.33 | **LOC:** 218 | **CtrlFlow:** 49.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), State Flux (99.9987%)
- **Heaviest Functions:** `debugError` (Impact: 40.9), `assert` (Impact: 9.4), `assert` (Impact: 6.8)

### 8. `packages/puppeteer-core/src/cdp/FrameManager.ts` (TYPESCRIPT) -> Cumulative Risk: **758.94**
- **Archetype:** `file_cluster_4` (Distance: 12.698 IQR)
- **Magnitude:** 56.88 | **LOC:** 583 | **CtrlFlow:** 34.7% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), State Flux (99.8348%)
- **Heaviest Functions:** `initialize` (Impact: 35.7), `removeScriptToEvaluateOnNewDocument` (Impact: 33.2), `setupEventListeners` (Impact: 29.1)

### 9. `packages/puppeteer-core/Herebyfile.mjs` (JAVASCRIPT) -> Cumulative Risk: **758.75**
- **Archetype:** `file_cluster_4` (Distance: 9.184 IQR)
- **Magnitude:** 114.46 | **LOC:** 166 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 81.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (99.9994%)
- **Heaviest Functions:** `run` (Impact: 55.6), `run` (Impact: 4.5), `run` (Impact: 2.7)

### 10. `packages/puppeteer-core/src/node/BrowserLauncher.ts` (TYPESCRIPT) -> Cumulative Risk: **758.03**
- **Archetype:** `file_cluster_4` (Distance: 11.521 IQR)
- **Magnitude:** 36.75 | **LOC:** 552 | **CtrlFlow:** 46.6% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `resolveExecutablePath` (Impact: 95.4), `closeBrowser` (Impact: 49.4), `waitForPageTarget` (Impact: 9.8)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/testserver/cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/testserver/key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tools/docgen/src/custom_markdown_documenter.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.788 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.798 IQR)
- **Top Global Matches:** file_cluster_8: 11.788, file_cluster_7: 12.308, file_cluster_0: 12.443
- **Magnitude:** 1970.63 | **LOC:** 1629 | **CtrlFlow:** 84.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (45.655%), Tech Debt (7.8468%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 265`, `structural_boundaries: 50`, `args: 48`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 374`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 3`
* *Defense:* `safety: 25`, `doc: 10`, `immutability_locks: 107`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DocHeading, Utilities, node-core-library, DocEmphasisSpan, api-extractor-model, CustomMarkdownEmitter, MarkdownDocumenterAccessor, DocTable...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `website/src/theme/SearchPage/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.793 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.908 IQR)
- **Top Global Matches:** file_cluster_8: 8.793, file_cluster_2: 9.081, file_cluster_13: 9.277
- **Magnitude:** 555.82 | **LOC:** 520 | **CtrlFlow:** 34.4% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (9.187%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `SearchPageContent` (Impact: 528.3 | O(2^N) | DB: 13)
  * `useDocumentsFoundPlural` (Impact: 7.8 | O(N^3) | DB: 3)
    * *Intent:* // eslint-disable-next-line @puppeteer/extensions
  * `useDocsSearchVersionsHelpers` (Impact: 4.0 | O(N^2))
  * `SearchVersionSelectList` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 82`, `args: 35`, `func_start: 21`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 3`
* *Architecture:* `io: 5`, `api: 1`, `concurrency: 1`, `import: 14`
* *Defense:* `safety: 5`, `doc: 1`, `immutability_locks: 30`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` client, lite, theme-common, Translate, algoliasearch-helper, clsx, useDocusaurusContext, styles.module.css...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/src/page.spec.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.434 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.34 IQR)
- **Top Global Matches:** file_cluster_4: 11.434, file_cluster_8: 11.831, file_cluster_13: 12.259
- **Magnitude:** 192.39 | **LOC:** 2567 | **CtrlFlow:** 7.4% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 139
- **Risk Profile:** Cognitive Load (49.7131%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 541.6 | O(2^N) | DB: 139)
  * `describe` (Impact: 37.2 | O(N^2) | DB: 37)
  * `describe` (Impact: 34.5 | O(N^2) | DB: 28)
  * `task` (Impact: 21.0 | O(2^N))
  * `describe` (Impact: 3.0 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 957`, `args: 524`, `func_start: 353`
* *Risk/State:* `safety_bypasses: 49`, `high_risk_execution: 5`, `state_mutation: 73`, `duplicate_logic: 7`
* *Architecture:* `io: 63`, `api: 1`, `concurrency: 1172`, `import: 15`
* *Defense:* `safety: 88`, `doc: 1`, `test: 327`, `immutability_locks: 239`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Page.js, CDPSession.js, es6module.js, node:http, Page.js, utils.js, expect, sinon...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/src/launcher.spec.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.164 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.332 IQR)
- **Top Global Matches:** file_cluster_4: 12.164, file_cluster_8: 12.552, file_cluster_17: 12.684
- **Magnitude:** 163.01 | **LOC:** 1004 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 119
- **Risk Profile:** Cognitive Load (48.0821%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 1148.8 | O(2^N) | DB: 119)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 349`, `args: 190`, `func_start: 152`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 42`, `planned_debt: 1`
* *Architecture:* `io: 40`, `concurrency: 421`, `import: 13`
* *Defense:* `safety: 94`, `doc: 1`, `test: 134`, `immutability_locks: 131`, `cleanup: 88`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Page.js, utils.js, fs.js, promises, node:tls, expect, sinon, node:fs...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/src/requestinterception-experimental.spec.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.268 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 6.78 IQR)
- **Top Global Matches:** file_cluster_4: 12.268, file_cluster_8: 12.657, file_cluster_13: 12.966
- **Magnitude:** 150.11 | **LOC:** 1069 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 77
- **Risk Profile:** Cognitive Load (48.5893%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 944.7 | O(2^N) | DB: 77)
  * `pathToFileURL` (Impact: 4.4 | O(N^1) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 370`, `args: 242`, `func_start: 158`
* *Risk/State:* `safety_bypasses: 52`, `high_risk_execution: 1`, `state_mutation: 84`
* *Architecture:* `io: 22`, `concurrency: 449`, `import: 7`
* *Defense:* `safety: 75`, `doc: 1`, `test: 147`, `immutability_locks: 109`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ConsoleMessage.js, expect, node:fs, node:path, HTTPRequest.js, mocha-utils.js, utils.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/src/requestinterception.spec.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.02 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.717 IQR)
- **Top Global Matches:** file_cluster_4: 12.02, file_cluster_8: 12.42, file_cluster_13: 12.772
- **Magnitude:** 146.24 | **LOC:** 1156 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 80
- **Risk Profile:** Cognitive Load (48.9675%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 817.6 | O(2^N) | DB: 80)
  * `pathToFileURL` (Impact: 4.4 | O(N^1) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 417`, `args: 261`, `func_start: 173`
* *Risk/State:* `safety_bypasses: 40`, `high_risk_execution: 1`, `state_mutation: 80`, `fragile_debt: 1`
* *Architecture:* `io: 23`, `concurrency: 540`, `import: 7`
* *Defense:* `safety: 70`, `doc: 1`, `test: 162`, `immutability_locks: 124`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ConsoleMessage.js, expect, node:fs, node:path, HTTPRequest.js, mocha-utils.js, utils.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/puppeteer-core/src/api/locators/locators.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_2` (Drift: 12.485 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.055 IQR)
- **Top Global Matches:** file_cluster_2: 12.485, file_cluster_16: 12.499, file_cluster_13: 12.752
- **Magnitude:** 133.22 | **LOC:** 1150 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (49.1084%), Tech Debt (99.9861%)
**Top Internal Functions/Classes:**
  * `fill` (Impact: 641.2 | O(2^N) | DB: 4)
    * *Intent:* /** * Creates a new locator instance by cloning the current locator and * specifying whether to wait...
  * `scroll` (Impact: 86.7 | O(2^N) | DB: 4)
  * `click` (Impact: 35.4 | O(2^N) | DB: 4)
    * *Intent:* /** * Creates a new locator instance by cloning the current locator and setting * the total timeout ...
  * `hover` (Impact: 33.1 | O(2^N) | DB: 4)
  * `_wait` (Impact: 26.1 | O(2^N) | DB: 2)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 255`, `args: 92`, `func_start: 94`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 93`, `duplicate_logic: 32`, `orphaned_logic: 4`
* *Architecture:* `api: 21`, `concurrency: 134`, `import: 9`
* *Defense:* `safety: 46`, `doc: 50`, `immutability_locks: 33`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ElementHandle.js, EventEmitter.js, util.js, Page.js, rxjs.js, Frame.js, types.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CHANGELOG.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 118.06 | **LOC:** 5903 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/puppeteer-core/Herebyfile.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 9.184 IQR)
- **Local Micro-Species:** `Cluster 5: I/O, UI & Routing Configuration` (Drift: 4.938 IQR)
- **Top Global Matches:** file_cluster_4: 9.184, file_cluster_8: 9.259, file_cluster_13: 9.426
- **Magnitude:** 114.46 | **LOC:** 166 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 81.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (76.003%), Tech Debt (99.8629%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 55.6 | O(N^4) | DB: 23)
  * `run` (Impact: 4.5 | O(N^1))
  * `run` (Impact: 2.7 | O(N^1) | DB: 2)
  * `run` (Impact: 1.9 | O(N^1) | DB: 2)
  * `run` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 42`, `args: 7`, `func_start: 5`
* *Risk/State:* `state_mutation: 6`, `duplicate_logic: 5`
* *Architecture:* `io: 11`, `api: 6`, `concurrency: 33`, `import: 7`
* *Defense:* `doc: 2`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:module, hereby, promises, esbuild, node:path, posix, execa
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/src/navigation.spec.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.764 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 6.486 IQR)
- **Top Global Matches:** file_cluster_4: 11.764, file_cluster_8: 12.233, file_cluster_13: 12.608
- **Magnitude:** 110.63 | **LOC:** 1033 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 67
- **Risk Profile:** Cognitive Load (49.4273%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 299.9 | O(2^N) | DB: 67)
  * `describe` (Impact: 22.1 | O(N^2) | DB: 3)
  * `describe` (Impact: 16.6 | O(N^2) | DB: 3)
    * *Intent:* // Make sure subresources do not inherit referer.
  * `describe` (Impact: 15.4 | O(N^2) | DB: 3)
  * `describe` (Impact: 7.4 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 368`, `args: 291`, `func_start: 198`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 100`, `planned_debt: 1`, `duplicate_logic: 7`
* *Architecture:* `io: 12`, `concurrency: 596`, `import: 8`
* *Defense:* `safety: 37`, `doc: 1`, `test: 183`, `immutability_locks: 125`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` HTTPResponse.js, node:http, utils.js, expect, Deferred.js, HTTPRequest.js, mocha-utils.js, puppeteer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `website/docusaurus.config.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.257 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 3.764 IQR)
- **Top Global Matches:** file_cluster_8: 9.257, file_cluster_7: 9.832, file_cluster_13: 9.872
- **Magnitude:** 104.38 | **LOC:** 399 | **CtrlFlow:** 45.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (8.6047%), Tech Debt (55.2315%)
**Top Internal Functions/Classes:**
  * `addNamespace` (Impact: 22.2 | O(N^5) | DB: 4)
  * `addNamespace` (Impact: 16.5 | O(2^N))
  * `jsLoader` (Impact: 9.8 | O(N^4))
  * `getApiUrl` (Impact: 9.1 | O(N^1) | DB: 9)
  * `assert` (Impact: 7.8 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 26`, `args: 12`, `func_start: 8`
* *Risk/State:* `state_mutation: 23`, `duplicate_logic: 3`, `orphaned_logic: 2`
* *Architecture:* `io: 13`, `api: 1`, `concurrency: 4`, `import: 5`
* *Defense:* `safety: 7`, `doc: 12`, `test: 3`, `immutability_locks: 24`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` preset-classic, versionsArchived.json, remark-plugin-npm2yarn, semver, prism-react-renderer, node:assert, plugin-client-redirects, types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Herebyfile.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_4` (Drift: 9.57 IQR)
- **Local Micro-Species:** `Cluster 5: I/O, UI & Routing Configuration` (Drift: 4.832 IQR)
- **Top Global Matches:** file_cluster_4: 9.57, file_cluster_13: 10.033, file_cluster_8: 10.124
- **Magnitude:** 101.22 | **LOC:** 128 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (78.386%), Tech Debt (99.8151%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 33.3 | O(N^2) | DB: 9)
  * `getApiUrl` (Impact: 9.1 | O(N^1) | DB: 9)
    * *Intent:* ---
  * `run` (Impact: 5.0 | O(N^1) | DB: 4)
  * `addNoTocHeader` (Impact: 2.1 | O(N^1))
  * `run` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 31`, `args: 5`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 10`, `duplicate_logic: 3`
* *Architecture:* `io: 7`, `api: 3`, `concurrency: 35`, `import: 6`
* *Defense:* `safety: 1`, `doc: 2`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` hereby, promises, semver, versions.json, docgen, execa
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/src/locator.spec.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.089 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.341 IQR)
- **Top Global Matches:** file_cluster_4: 11.089, file_cluster_8: 11.383, file_cluster_17: 11.74
- **Magnitude:** 97.69 | **LOC:** 867 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (48.976%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 488.5 | O(2^N) | DB: 24)
  * `setTimeout` (Impact: 3.7 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 332`, `args: 126`, `func_start: 84`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 28`
* *Architecture:* `concurrency: 442`, `import: 6`
* *Defense:* `safety: 49`, `doc: 1`, `test: 94`, `immutability_locks: 73`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` puppeteer-core, expect, sinon, mocha-utils.js, utils.js, locators.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/src/waittask.spec.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.015 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.981 IQR)
- **Top Global Matches:** file_cluster_4: 11.015, file_cluster_8: 11.424, file_cluster_13: 11.981
- **Magnitude:** 96.73 | **LOC:** 957 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (49.3104%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 227.7 | O(2^N) | DB: 12)
  * `it` (Impact: 14.8 | O(N^3) | DB: 1)
  * `describe` (Impact: 11.6 | O(N^3) | DB: 1)
  * `it` (Impact: 11.4 | O(N^3) | DB: 1)
  * `it` (Impact: 7.7 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 495`, `args: 244`, `func_start: 126`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 42`, `duplicate_logic: 10`
* *Architecture:* `concurrency: 607`, `import: 5`
* *Defense:* `safety: 44`, `doc: 1`, `test: 142`, `immutability_locks: 116`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ErrorLike.js, utils.js, expect, mocha-utils.js, puppeteer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/puppeteer/CHANGELOG.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 79.98 | **LOC:** 3999 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/puppeteer-core/src/bidi/Page.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.291 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.507 IQR)
- **Top Global Matches:** file_cluster_13: 12.291, file_cluster_4: 12.295, file_cluster_8: 12.724
- **Magnitude:** 78.59 | **LOC:** 1213 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (93.1026%), Tech Debt (51.0592%)
**Top Internal Functions/Classes:**
  * `setViewport` (Impact: 334.5 | O(2^N) | DB: 4)
  * `_screenshot` (Impact: 35.4 | O(N^2) | DB: 1)
  * `setGeolocation` (Impact: 21.4 | O(N^2))
  * `focusedFrame` (Impact: 18.5 | O(N^3) | DB: 3)
  * `emulateMediaType` (Impact: 9.1 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 140`, `args: 51`, `func_start: 48`, `class_start: 1`
* *Risk/State:* `state_mutation: 65`, `planned_debt: 1`, `duplicate_logic: 3`
* *Architecture:* `io: 2`, `api: 14`, `concurrency: 154`, `import: 40`
* *Defense:* `safety: 35`, `doc: 3`, `test: 4`, `immutability_locks: 29`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` NetworkManager.js, PDFOptions.js, Page.js, util.js, EventEmitter.js, HTTPResponse.js, util.js, Browser.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/puppeteer-core/src/cdp/Page.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.876 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.287 IQR)
- **Top Global Matches:** file_cluster_4: 11.876, file_cluster_13: 11.984, file_cluster_8: 12.25
- **Magnitude:** 74.81 | **LOC:** 1370 | **CtrlFlow:** 27.7% | **Authorship Centralization:** 41.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (89.9991%), Tech Debt (14.1647%)
**Top Internal Functions/Classes:**
  * `_screenshot` (Impact: 40.7 | O(N^3) | DB: 2)
  * `reload` (Impact: 34.2 | O(2^N) | DB: 1)
  * `_create` (Impact: 24.5 | O(N^2))
  * `setCookie` (Impact: 24.0 | O(N^3) | DB: 5)
  * `onConsoleAPI` (Impact: 17.3 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 214`, `args: 61`, `func_start: 59`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 56`, `duplicate_logic: 2`
* *Architecture:* `io: 5`, `api: 20`, `concurrency: 323`, `import: 51`
* *Defense:* `safety: 52`, `doc: 7`, `test: 7`, `immutability_locks: 50`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` disposable.js, PDFOptions.js, ConsoleMessage.js, Page.js, FrameManagerEvents.js, EventEmitter.js, BrowserContext.js, IsolatedWorld.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/puppeteer-core/src/cdp/Accessibility.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.748 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.754 IQR)
- **Top Global Matches:** file_cluster_4: 11.748, file_cluster_8: 11.77, file_cluster_13: 11.876
- **Magnitude:** 70.7 | **LOC:** 785 | **CtrlFlow:** 70.4% | **Authorship Centralization:** 77.8%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (59.253%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `populateIframes` (Impact: 81.8 | O(2^N))
  * `isControl` (Impact: 66.4 | O(N^2))
  * `isLeafNode` (Impact: 51.5 | O(N^2) | DB: 1)
  * `serializeTree` (Impact: 49.2 | O(2^N) | DB: 3)
    * *Intent:* /** * CDP-specific documentId.
  * `constructor` (Impact: 41.0 | O(N^2) | DB: 9)
    * *Intent:* #realm: Realm; #frameId: string; /** * @internal */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 176`, `structural_boundaries: 74`, `args: 19`, `func_start: 19`, `class_start: 2`
* *Risk/State:* `state_mutation: 123`, `dead_code: 1`
* *Architecture:* `api: 13`, `concurrency: 50`, `import: 5`
* *Defense:* `safety: 9`, `doc: 15`, `immutability_locks: 36`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` devtools-protocol, Realm.js, Frame.js, ElementHandle.js, util.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/src/ariaqueryhandler.spec.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.144 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.784 IQR)
- **Top Global Matches:** file_cluster_4: 10.144, file_cluster_8: 10.294, file_cluster_13: 10.938
- **Magnitude:** 66.27 | **LOC:** 859 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (49.2342%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 225.3 | O(2^N) | DB: 11)
  * `getIds` (Impact: 4.5 | O(N^3))
  * `it` (Impact: 3.0 | O(N^2))
  * `it` (Impact: 2.0 | O(N^1))
  * `it` (Impact: 2.0 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 378`, `args: 179`, `func_start: 119`
* *Risk/State:* `safety_bypasses: 25`, `high_risk_execution: 3`, `state_mutation: 29`, `duplicate_logic: 6`
* *Architecture:* `concurrency: 375`, `import: 6`
* *Defense:* `safety: 15`, `doc: 1`, `test: 113`, `immutability_locks: 98`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` utils.js, expect, ElementHandle.js, mocha-utils.js, puppeteer, node:assert
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/browsers/src/CLI.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.388 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.809 IQR)
- **Top Global Matches:** file_cluster_8: 9.388, file_cluster_0: 9.789, file_cluster_13: 9.945
- **Magnitude:** 64.25 | **LOC:** 571 | **CtrlFlow:** 58.0% | **Authorship Centralization:** 80.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (24.0697%), Tech Debt (44.8794%)
**Top Internal Functions/Classes:**
  * `build` (Impact: 496.1 | O(2^N) | DB: 24)
  * `install` (Impact: 29.1 | O(2^N) | DB: 9)
  * `constructor` (Impact: 20.9 | O(N^4))
  * `run` (Impact: 13.2 | O(N^2) | DB: 1)
  * `definePlatformParameter` (Impact: 8.7 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 68`, `args: 19`, `func_start: 18`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 4`, `planned_debt: 1`, `duplicate_logic: 3`
* *Architecture:* `io: 15`, `api: 2`, `concurrency: 27`, `import: 10`
* *Defense:* `safety: 22`, `doc: 2`, `immutability_locks: 27`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` yargs, launch.js, detectPlatform.js, Cache.js, helpers, browser-data.js, install.js, node:process...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/src/cookies.spec.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_4` (Drift: 9.579 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.374 IQR)
- **Top Global Matches:** file_cluster_4: 9.579, file_cluster_8: 9.644, file_cluster_7: 10.357
- **Magnitude:** 63.86 | **LOC:** 883 | **CtrlFlow:** 9.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 175
- **Risk Profile:** Cognitive Load (46.3719%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 237.4 | O(2^N) | DB: 175)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 266`, `args: 113`, `func_start: 95`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 18`
* *Architecture:* `io: 55`, `concurrency: 367`, `import: 2`
* *Defense:* `safety: 17`, `doc: 1`, `test: 94`, `immutability_locks: 78`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` expect, mocha-utils.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/puppeteer-core/src/cdp/Input.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.9 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.575 IQR)
- **Top Global Matches:** file_cluster_4: 11.9, file_cluster_8: 12.407, file_cluster_13: 12.434
- **Magnitude:** 61.73 | **LOC:** 654 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (82.105%), Tech Debt (99.7521%)
**Top Internal Functions/Classes:**
  * `keyDescriptionForString` (Impact: 26.9 | O(N^1) | DB: 6)
  * `getButtonFromPressedButtons` (Impact: 18.1 | O(N^1))
  * `getFlag` (Impact: 16.4 | O(N^1))
  * `reset` (Impact: 15.9 | O(N^2) | DB: 4)
  * `update` (Impact: 12.6 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 133`, `args: 59`, `func_start: 54`, `class_start: 5`
* *Risk/State:* `state_mutation: 101`, `dead_code: 1`, `duplicate_logic: 19`
* *Architecture:* `api: 8`, `concurrency: 314`, `import: 7`
* *Defense:* `safety: 34`, `doc: 10`, `test: 1`, `immutability_locks: 39`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CDPSession.js, devtools-protocol, assert.js, USKeyboardLayout.js, ElementHandle.js, Input.js, Errors.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `packages/puppeteer-core/src/api/BluetoothEmulation.ts` (TYPESCRIPT) | Magnitude: 4.92 | Delta: **0.195 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: doc: 9, indent_spaces: 5, structural_boundaries: 4, args: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/puppeteer-core/src/bidi/Page.ts` (TYPESCRIPT) | Magnitude: 78.59 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 427, concurrency: 154, structural_boundaries: 140, branch: 80
- `packages/puppeteer-core/src/bidi/ExposedFunction.ts` (TYPESCRIPT) | Magnitude: 36.59 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 199, concurrency: 66, structural_boundaries: 65, encapsulation: 33
- `packages/ng-schematics/src/schematics/utils/files.ts` (TYPESCRIPT) | Magnitude: 6.22 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 94, structural_boundaries: 31, branch: 20, args: 14
- `packages/puppeteer-core/src/bidi/WebWorker.ts` (TYPESCRIPT) | Magnitude: 1.66 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 15, import: 7, encapsulation: 7
- `packages/puppeteer-core/src/bidi/CDPSession.ts` (TYPESCRIPT) | Magnitude: 13.69 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 88, structural_boundaries: 29, state_mutation: 29, concurrency: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `tools/mocha-runner/src/reporter.cts` (TYPESCRIPT) | Magnitude: 0.49 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 4, args: 2, func_start: 2
- `packages/puppeteer-core/src/api/CDPSession.ts` (TYPESCRIPT) | Magnitude: 1.32 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 23, indent_spaces: 19, doc: 17, api: 11
- `packages/puppeteer-core/src/common/TaskQueue.ts` (TYPESCRIPT) | Magnitude: 1.26 | Delta: **0.13 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 8, args: 4, concurrency: 4
- `packages/puppeteer-core/src/common/LazyArg.ts` (TYPESCRIPT) | Magnitude: 2.13 | Delta: **0.205 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 15, indent_spaces: 13, concurrency: 7, generics: 7
- `packages/puppeteer-core/src/common/types.ts` (TYPESCRIPT) | Magnitude: 1.97 | Delta: **0.396 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 57, generics: 39, doc: 20, api: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `docker/Dockerfile` (DOCKERFILE) | Magnitude: 58.36 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 9, func_start: 5, structural_boundaries: 4, indent_spaces: 4
- `packages/puppeteer-core/src/cdp/FrameTree.ts` (TYPESCRIPT) | Magnitude: 10.15 | Delta: **0.124 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 68, state_mutation: 33, encapsulation: 26, structural_boundaries: 20
- `packages/puppeteer-core/src/bidi/Deserializer.ts` (TYPESCRIPT) | Magnitude: 15.54 | Delta: **0.142 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 72, structural_boundaries: 37, branch: 26, state_mutation: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `packages/puppeteer-core/src/injected/XPathQuerySelector.ts` (TYPESCRIPT) | Magnitude: 2.0 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 23, state_mutation: 9, branch: 6, immutability_locks: 4
- `packages/puppeteer-core/src/injected/util.ts` (TYPESCRIPT) | Magnitude: 4.3 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 40, branch: 15, structural_boundaries: 10, immutability_locks: 9
- `packages/puppeteer-core/src/api/locators/locators.ts` (TYPESCRIPT) | Magnitude: 133.22 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 687, structural_boundaries: 255, generics: 190, concurrency: 134
- `packages/puppeteer-core/src/api/Realm.ts` (TYPESCRIPT) | Magnitude: 4.3 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 78, structural_boundaries: 27, ui_framework: 26, concurrency: 19
- `packages/puppeteer-core/src/injected/CSSSelector.ts` (TYPESCRIPT) | Magnitude: 0.9 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 5, api: 4, doc: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/puppeteer-core/src/util/Deferred.ts` (TYPESCRIPT) | Magnitude: 12.56 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 86, encapsulation: 36, concurrency: 27, structural_boundaries: 25
- `packages/puppeteer-core/src/bidi/core/Realm.ts` (TYPESCRIPT) | Magnitude: 29.72 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 254, state_mutation: 131, structural_boundaries: 84, concurrency: 62
- `packages/puppeteer-core/src/injected/PQuerySelector.ts` (TYPESCRIPT) | Magnitude: 30.33 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 191, structural_boundaries: 57, state_mutation: 55, branch: 46
- `test/src/download.spec.ts` (TYPESCRIPT) | Magnitude: 4.76 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 42, concurrency: 38, structural_boundaries: 28, args: 8
- `test/src/emulation.spec.ts` (TYPESCRIPT) | Magnitude: 44.13 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 578, structural_boundaries: 325, concurrency: 270, args: 141

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `packages/puppeteer-core/src/cdp/IsolatedWorlds.ts` (TYPESCRIPT) | Magnitude: 1.3 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 3, structural_boundaries: 2, api: 2, immutability_locks: 2
- `packages/ng-schematics/src/schematics/config/files/.puppeteerrc.mjs` (JAVASCRIPT) | Magnitude: 11.52 | Delta: **0.041 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 2, structural_boundaries: 1, api: 1
- `packages/puppeteer-core/src/common/SupportedBrowser.ts` (TYPESCRIPT) | Magnitude: 1.15 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, doc: 2, api: 1
- `packages/puppeteer-core/src/api/ElementHandleSymbol.ts` (TYPESCRIPT) | Magnitude: 1.15 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 2, structural_boundaries: 1, api: 1, immutability_locks: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `test/src/console.spec.ts` (TYPESCRIPT) | Magnitude: 14.5 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 276, structural_boundaries: 127, concurrency: 115, args: 90
- `test/src/evaluation.spec.ts` (TYPESCRIPT) | Magnitude: 26.26 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 313, concurrency: 200, structural_boundaries: 185, args: 114
- `packages/puppeteer-core/function-fixture.mjs` (JAVASCRIPT) | Magnitude: 27.5 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 24, args: 14, concurrency: 12, structural_boundaries: 11
- `packages/puppeteer-core/src/util/incremental-id-generator.ts` (TYPESCRIPT) | Magnitude: 1.01 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 7, args: 4, api: 3
- `packages/ng-schematics/test/src/ng-add.test.ts` (TYPESCRIPT) | Magnitude: 11.82 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 227, args: 97, test: 87, func_start: 73

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/puppeteer-core/src/cdp/Page.ts` -> Churn: **65.77%** | Cog Load: 89.9991% | Debt: 14.1647%
- `docker/Dockerfile` -> Churn: **63.09%** | Cog Load: 85.5422% | Debt: 0.0%
- `packages/puppeteer-core/Herebyfile.mjs` -> Churn: **63.02%** | Cog Load: 76.003% | Debt: 99.8629%
- `packages/puppeteer-core/src/bidi/Page.ts` -> Churn: **56.62%** | Cog Load: 93.1026% | Debt: 51.0592%
- `packages/puppeteer-core/src/api/Page.ts` -> Churn: **50.7%** | Cog Load: 49.9902% | Debt: 88.6324%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `tools/docgen/src/custom_markdown_documenter.ts` -> **Nikolay Vitkov** (100.0% isolated ownership) | Magnitude: 1970.63
- `test/src/launcher.spec.ts` -> **Nikolay Vitkov** (100.0% isolated ownership) | Magnitude: 163.01
- `test/src/requestinterception-experimental.spec.ts` -> **Nikolay Vitkov** (100.0% isolated ownership) | Magnitude: 150.11
- `packages/puppeteer-core/src/api/locators/locators.ts` -> **Alex Rudenko** (100.0% isolated ownership) | Magnitude: 133.22
- `packages/puppeteer-core/Herebyfile.mjs` -> **browser-automation-bot** (81.0% isolated ownership) | Magnitude: 114.46

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/ng-schematics/src/schematics/utils/json.ts` -> **Severity: 0.459** (Embedded: 0.012 * Error Risk: 38.3322%)
- `tools/docgen/src/docgen.ts` -> **Severity: 0.092** (Embedded: 0.002 * Error Risk: 46.257%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/ng-schematics/src/schematics/utils/json.ts` -> **Severity: 823.15** (Blast Radius: 9.296 * Doc Risk: 88.5488%)
- `packages/puppeteer-core/src/puppeteer-core.ts` -> **Severity: 680.363** (Blast Radius: 57.076 * Doc Risk: 11.9203%)
- `packages/puppeteer/src/puppeteer.ts` -> **Severity: 631.967** (Blast Radius: 53.016 * Doc Risk: 11.9203%)
- `packages/ng-schematics/tools/projects.mjs` -> **Severity: 172.4** (Blast Radius: 1.724 * Doc Risk: 100.0%)
- `packages/browsers/src/DefaultProvider.ts` -> **Severity: 172.4** (Blast Radius: 1.724 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
