# ARCHITECTURAL_BRIEF: puppeteer
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_web/puppeteer` |
| **Timestamp** | `2026-08-07T04:27:16.583064+00:00` |
| **Scan Duration** | `2.08s` |
| **Git Branch** | `main` |
| **Git Commit** | `bf1e9722eef723c80250119d81fd9d9e0596c074` |
| **Git Remote** | `https://github.com/puppeteer/puppeteer.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 413 malicious artifacts.

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
> **Architectural Drift Z-Score:** `4.531`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 235 | 46.8% |
| file_cluster_4 | 113 | 22.5% |
| file_cluster_13 | 98 | 19.5% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 25.3 | 14.2 | 5.0 |
| Error & Exception Exposure | 0.0 | 94.4 | 28.8 | 31.2 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 15.7 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 5.1 | 0.0 | 0.0 |
| API Exposure | 0.0 | 19.1 | 2.8 | 0.7 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 54.6 | 86.5 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 20.7 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 23.1 | 0.2 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 91.7 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 6.1 | 1.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 89.9 | 5.9 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 17.9 | 11.9 | 0.0 |
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

- `describe` (@ `test/src/requestinterception-experimental.spec.ts`) -> Impact: **274.4** | LOC: 1019
- `describe` (@ `test/src/launcher.spec.ts`) -> Impact: **268.9** | LOC: 979
- `describe` (@ `test/src/launcher.spec.ts`) -> Impact: **257.8** | LOC: 895
- `describe` (@ `test/src/requestinterception.spec.ts`) -> Impact: **246.0** | LOC: 1110
- `getBidiKeyValue` (@ `packages/puppeteer-core/src/bidi/Input.ts`) -> Impact: **237.1** | LOC: 222
- `describe` (@ `test/src/requestinterception-experimental.spec.ts`) -> Impact: **219.0** | LOC: 709
- `describe` (@ `test/src/launcher.spec.ts`) -> Impact: **179.6** | LOC: 509
- `describe` (@ `test/src/requestinterception.spec.ts`) -> Impact: **176.4** | LOC: 722
- `describe` (@ `test/src/page.spec.ts`) -> Impact: **174.4** | LOC: 1652
- `frame` (@ `packages/puppeteer-core/src/cdp/NetworkManager.ts`) -> Impact: **154.5** | LOC: 422
  * *Intent:* /** * Download speed (bytes/s) */

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `packages/testserver` | 7 | 10033.52 | 1.43% | 0.0% |
| `__monolith__` | 12 | 5309.34 | 8.61% | 9.65% |
| `test/src` | 56 | 2094.1 | 35.49% | 0.0% |
| `tools/docgen/src` | 2 | 1853.8 | 24.82% | 53.45% |
| `packages/puppeteer-core/src/cdp` | 43 | 784.17 | 38.88% | 16.73% |
| `packages/puppeteer-core/src/bidi` | 25 | 361.66 | 45.28% | 37.67% |
| `packages/puppeteer-core/src/api` | 22 | 268.85 | 30.24% | 18.27% |
| `packages/puppeteer-core/src/common` | 42 | 198.29 | 18.1% | 17.79% |
| `examples` | 11 | 196.36 | 21.8% | 0.0% |
| `packages/puppeteer-core` | 7 | 180.8 | 23.56% | 37.44% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `packages/puppeteer-core/function-fixture.mjs` -> **100.0%** Exposure
- `docker/pack.sh` -> **100.0%** Exposure
- `packages/browsers/src/DefaultProvider.spec.ts` -> **100.0%** Exposure
- `packages/puppeteer-core/src/api/locators/locators.ts` -> **100.0%** Exposure
- `packages/puppeteer-core/src/bidi/Target.ts` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `docker/Dockerfile` -> **100.0%** Exposure
- `packages/ng-schematics/src/schematics/ng-add/files/common/e2e/tests/utils.ts.template` -> **100.0%** Exposure
- `packages/puppeteer-core/src/bidi/core/Realm.ts` -> **100.0%** Exposure
- `packages/puppeteer-core/src/cdp/FrameTree.ts` -> **100.0%** Exposure
- `packages/puppeteer-core/src/common/BrowserWebSocketTransport.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `test/src/page.spec.ts` -> **0** Orphaned Functions | **203** Duplicates
- `test/src/launcher.spec.ts` -> **3** Orphaned Functions | **107** Duplicates
- `test/src/emulation.spec.ts` -> **0** Orphaned Functions | **96** Duplicates
- `test/src/navigation.spec.ts` -> **0** Orphaned Functions | **76** Duplicates
- `test/src/ariaqueryhandler.spec.ts` -> **0** Orphaned Functions | **75** Duplicates

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

### Hardcoded Payload Artifacts
- `website/docusaurus.config.js` -> **35.1292%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `810` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `packages/puppeteer-core/src/bidi/core/Realm.ts` (TYPESCRIPT) -> Cumulative Risk: **667.3**
- **Archetype:** `file_cluster_4` (Distance: 12.761 IQR)
- **Magnitude:** 28.74 | **LOC:** 362 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9999%), Tech Debt (99.9985%)
- **Heaviest Functions:** `initialize` (Impact: 12.3), `initialize` (Impact: 8.8), `initialize` (Impact: 8.8)

### 2. `packages/puppeteer-core/src/bidi/Frame.ts` (TYPESCRIPT) -> Cumulative Risk: **625.2**
- **Archetype:** `file_cluster_4` (Distance: 12.441 IQR)
- **Magnitude:** 51.61 | **LOC:** 611 | **CtrlFlow:** 32.2% | **Authorship Centralization:** 20.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9685%), Cognitive Load (97.881%)
- **Heaviest Functions:** `initialize` (Impact: 29.4), `getConsoleMessage` (Impact: 21.3), `switchMap` (Impact: 10.1)

### 3. `packages/ng-schematics/src/builders/puppeteer/index.ts` (TYPESCRIPT) -> Cumulative Risk: **605.7**
- **Archetype:** `file_cluster_4` (Distance: 10.477 IQR)
- **Magnitude:** 16.21 | **LOC:** 235 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9993%), Tech Debt (97.7023%), Verification (80.0%)
- **Heaviest Functions:** `message` (Impact: 18.9), `executeE2ETest` (Impact: 13.6), `getCommandForRunner` (Impact: 13.0)

### 4. `packages/ng-schematics/src/schematics/utils/packages.ts` (TYPESCRIPT) -> Cumulative Risk: **598.18**
- **Archetype:** `file_cluster_13` (Distance: 10.598 IQR)
- **Magnitude:** 9.76 | **LOC:** 190 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9783%), Concurrency (96.0425%), Verification (80.0%)
- **Heaviest Functions:** `getDependenciesFromOptions` (Impact: 18.4), `getPackageLatestNpmVersion` (Impact: 17.5), `addPackageJsonDependencies` (Impact: 6.4)

### 5. `packages/puppeteer-core/src/cdp/Target.ts` (TYPESCRIPT) -> Cumulative Risk: **594.01**
- **Archetype:** `file_cluster_4` (Distance: 12.669 IQR)
- **Magnitude:** 32.41 | **LOC:** 310 | **CtrlFlow:** 31.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9905%), Tech Debt (82.4709%)
- **Heaviest Functions:** `_initialize` (Impact: 15.1), `page` (Impact: 14.7), `pagePromise` (Impact: 13.0)

### 6. `packages/puppeteer-core/src/util/decorators.ts` (TYPESCRIPT) -> Cumulative Risk: **593.66**
- **Archetype:** `file_cluster_13` (Distance: 11.991 IQR)
- **Magnitude:** 14.74 | **LOC:** 211 | **CtrlFlow:** 27.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (93.1593%), Concurrency (90.7129%)
- **Heaviest Functions:** `bubble` (Impact: 16.6), `target` (Impact: 13.7), `bubbleInitializer` (Impact: 13.3)

### 7. `packages/puppeteer-core/src/api/locators/locators.ts` (TYPESCRIPT) -> Cumulative Risk: **591.21**
- **Archetype:** `file_cluster_2` (Distance: 12.528 IQR)
- **Magnitude:** 80.44 | **LOC:** 1150 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Concurrency (99.9983%), State Flux (85.1491%)
- **Heaviest Functions:** `mergeMap` (Impact: 96.0), `fill` (Impact: 79.2), `mergeMap` (Impact: 60.9)

### 8. `packages/testserver/src/index.ts` (TYPESCRIPT) -> Cumulative Risk: **590.06**
- **Archetype:** `file_cluster_4` (Distance: 11.587 IQR)
- **Magnitude:** 25.58 | **LOC:** 338 | **CtrlFlow:** 34.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Cognitive Load (94.1452%), Verification (80.0%)
- **Heaviest Functions:** `serveFile` (Impact: 34.3), `RequestListener` (Impact: 24.7), `readFile` (Impact: 13.7)

### 9. `packages/puppeteer-core/src/node/ChromeLauncher.ts` (TYPESCRIPT) -> Cumulative Risk: **588.32**
- **Archetype:** `file_cluster_13` (Distance: 11.805 IQR)
- **Magnitude:** 17.48 | **LOC:** 346 | **CtrlFlow:** 49.5% | **Authorship Centralization:** 85.7%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9688%), Tech Debt (95.0478%), Concurrency (92.6446%)
- **Heaviest Functions:** `assert` (Impact: 12.8), `assert` (Impact: 12.7), `executablePath` (Impact: 8.7)

### 10. `packages/puppeteer-core/src/bidi/Page.ts` (TYPESCRIPT) -> Cumulative Risk: **584.57**
- **Archetype:** `file_cluster_13` (Distance: 12.296 IQR)
- **Magnitude:** 47.0 | **LOC:** 1213 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Cognitive Load (93.0996%), State Flux (86.7572%)
- **Heaviest Functions:** `setViewport` (Impact: 69.9), `_screenshot` (Impact: 24.1), `setGeolocation` (Impact: 14.7)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/testserver/cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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
- **Global Archetype:** `file_cluster_8` (Drift: 11.775 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.797 IQR)
- **Top Global Matches:** file_cluster_8: 11.775, file_cluster_7: 12.296, file_cluster_0: 12.431
- **Magnitude:** 1852.91 | **LOC:** 1629 | **CtrlFlow:** 84.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (45.655%), Tech Debt (7.8468%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 265`, `structural_boundaries: 50`, `args: 42`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 374`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 3`
* *Defense:* `safety: 25`, `doc: 10`, `immutability_locks: 107`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DocTableCell, DocTable, Utilities, MarkdownDocumenterFeature, DocHeading, DocumenterConfig, DocEmphasisSpan, api-extractor-model...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/src/page.spec.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.377 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.446 IQR)
- **Top Global Matches:** file_cluster_4: 11.377, file_cluster_8: 11.818, file_cluster_13: 12.219
- **Magnitude:** 227.37 | **LOC:** 2567 | **CtrlFlow:** 7.4% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (49.7169%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 174.4)
  * `describe` (Impact: 34.2)
  * `describe` (Impact: 27.7)
  * `describe` (Impact: 25.0)
  * `describe` (Impact: 22.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 957`, `args: 477`, `func_start: 352`
* *Risk/State:* `safety_bypasses: 49`, `high_risk_execution: 5`, `state_mutation: 73`, `duplicate_logic: 203`
* *Architecture:* `io: 63`, `api: 1`, `concurrency: 1152`, `import: 15`
* *Defense:* `safety: 88`, `doc: 1`, `test: 327`, `immutability_locks: 239`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Page.js, es6module.js, HTTPRequest.js, node:assert, node:http, mocha-utils.js, puppeteer, sinon...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/src/launcher.spec.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.103 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.443 IQR)
- **Top Global Matches:** file_cluster_4: 12.103, file_cluster_8: 12.536, file_cluster_17: 12.622
- **Magnitude:** 177.02 | **LOC:** 1004 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (49.3349%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 268.9)
  * `describe` (Impact: 257.8)
  * `describe` (Impact: 179.6)
  * `describe` (Impact: 47.1)
  * `describe` (Impact: 16.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 349`, `args: 183`, `func_start: 152`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 42`, `planned_debt: 1`, `duplicate_logic: 107`, `orphaned_logic: 3`
* *Architecture:* `io: 40`, `concurrency: 411`, `import: 13`
* *Defense:* `safety: 94`, `doc: 1`, `test: 134`, `immutability_locks: 131`, `cleanup: 88`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` node:tls, Page.js, node:assert, mocha-utils.js, puppeteer, sinon, expect, utils.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `website/src/theme/SearchPage/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.774 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.094 IQR)
- **Top Global Matches:** file_cluster_8: 8.774, file_cluster_2: 9.055, file_cluster_13: 9.232
- **Magnitude:** 159.92 | **LOC:** 520 | **CtrlFlow:** 34.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (8.5515%), Tech Debt (85.3454%)
**Top Internal Functions/Classes:**
  * `SearchPageContent` (Impact: 91.8)
  * `getTitle` (Impact: 9.6)
  * `useEffect` (Impact: 5.9)
  * `useEffect` (Impact: 5.5)
  * `useDocumentsFoundPlural` (Impact: 4.3)
    * *Intent:* // eslint-disable-next-line @puppeteer/extensions
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 82`, `args: 35`, `func_start: 21`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 3`, `duplicate_logic: 8`
* *Architecture:* `io: 5`, `api: 2`, `concurrency: 1`, `import: 14`
* *Defense:* `safety: 5`, `doc: 1`, `immutability_locks: 30`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` react, Layout, styles.module.css, SearchMetadata, theme-common, client, Link, clsx...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/src/requestinterception.spec.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.951 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 6.675 IQR)
- **Top Global Matches:** file_cluster_4: 11.951, file_cluster_8: 12.395, file_cluster_13: 12.726
- **Magnitude:** 151.29 | **LOC:** 1156 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (49.4755%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 246.0)
  * `describe` (Impact: 176.4)
  * `describe` (Impact: 34.2)
  * `describe` (Impact: 28.3)
  * `it` (Impact: 16.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 417`, `args: 255`, `func_start: 171`
* *Risk/State:* `safety_bypasses: 40`, `high_risk_execution: 1`, `state_mutation: 80`, `fragile_debt: 1`, `duplicate_logic: 72`
* *Architecture:* `io: 23`, `concurrency: 540`, `import: 7`
* *Defense:* `safety: 70`, `doc: 1`, `test: 162`, `immutability_locks: 124`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HTTPRequest.js, mocha-utils.js, expect, utils.js, ConsoleMessage.js, node:path, node:fs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/src/requestinterception-experimental.spec.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.199 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 6.692 IQR)
- **Top Global Matches:** file_cluster_4: 12.199, file_cluster_8: 12.626, file_cluster_13: 12.912
- **Magnitude:** 150.13 | **LOC:** 1069 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (49.4028%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 274.4)
  * `describe` (Impact: 219.0)
  * `it` (Impact: 41.3)
  * `describe` (Impact: 27.9)
  * `describe` (Impact: 20.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 370`, `args: 236`, `func_start: 156`
* *Risk/State:* `safety_bypasses: 52`, `high_risk_execution: 1`, `state_mutation: 84`, `duplicate_logic: 69`
* *Architecture:* `io: 22`, `concurrency: 439`, `import: 7`
* *Defense:* `safety: 75`, `doc: 1`, `test: 147`, `immutability_locks: 109`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HTTPRequest.js, mocha-utils.js, expect, utils.js, ConsoleMessage.js, node:path, node:fs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/src/navigation.spec.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.673 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 6.443 IQR)
- **Top Global Matches:** file_cluster_4: 11.673, file_cluster_8: 12.175, file_cluster_13: 12.537
- **Magnitude:** 119.83 | **LOC:** 1033 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (49.4272%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 97.3)
  * `describe` (Impact: 74.9)
  * `describe` (Impact: 16.0)
  * `it` (Impact: 13.6)
  * `describe` (Impact: 12.3)
    * *Intent:* // Make sure subresources do not inherit referer.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 368`, `args: 263`, `func_start: 198`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 96`, `planned_debt: 1`, `duplicate_logic: 76`
* *Architecture:* `io: 12`, `concurrency: 596`, `import: 8`
* *Defense:* `safety: 37`, `doc: 1`, `test: 183`, `immutability_locks: 125`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` HTTPRequest.js, Deferred.js, node:http, mocha-utils.js, puppeteer, expect, utils.js, HTTPResponse.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CHANGELOG.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 118.06 | **LOC:** 5903 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `test/src/locator.spec.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.038 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.433 IQR)
- **Top Global Matches:** file_cluster_4: 11.038, file_cluster_8: 11.385, file_cluster_17: 11.697
- **Magnitude:** 107.09 | **LOC:** 867 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (48.976%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 150.7)
  * `describe` (Impact: 65.2)
  * `describe` (Impact: 44.9)
  * `describe` (Impact: 14.8)
  * `it` (Impact: 13.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 332`, `args: 122`, `func_start: 84`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 28`, `duplicate_logic: 63`
* *Architecture:* `concurrency: 442`, `import: 6`
* *Defense:* `safety: 49`, `doc: 1`, `test: 94`, `immutability_locks: 73`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` puppeteer-core, locators.js, mocha-utils.js, sinon, expect, utils.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/src/waittask.spec.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.945 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.945 IQR)
- **Top Global Matches:** file_cluster_4: 10.945, file_cluster_8: 11.38, file_cluster_13: 11.923
- **Magnitude:** 103.32 | **LOC:** 957 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (49.4206%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 77.0)
  * `describe` (Impact: 48.3)
  * `describe` (Impact: 30.2)
  * `it` (Impact: 10.0)
  * `it` (Impact: 9.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 495`, `args: 204`, `func_start: 125`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 42`, `duplicate_logic: 58`, `orphaned_logic: 2`
* *Architecture:* `concurrency: 597`, `import: 5`
* *Defense:* `safety: 44`, `doc: 1`, `test: 142`, `immutability_locks: 116`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` mocha-utils.js, puppeteer, expect, utils.js, ErrorLike.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Herebyfile.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_4` (Drift: 9.564 IQR)
- **Local Micro-Species:** `Cluster 5: I/O, UI & Routing Configuration` (Drift: 4.832 IQR)
- **Top Global Matches:** file_cluster_4: 9.564, file_cluster_13: 10.028, file_cluster_8: 10.118
- **Magnitude:** 95.62 | **LOC:** 128 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.386%), Tech Debt (99.8151%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 22.9)
  * `getApiUrl` (Impact: 9.1)
    * *Intent:* ---
  * `run` (Impact: 5.0)
  * `spliceIntoSection` (Impact: 4.8)
  * `addNoTocHeader` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 31`, `args: 5`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 10`, `duplicate_logic: 3`
* *Architecture:* `io: 7`, `api: 3`, `concurrency: 35`, `import: 6`
* *Defense:* `safety: 1`, `doc: 2`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` execa, docgen, versions.json, promises, hereby, semver
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/puppeteer-core/Herebyfile.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 9.184 IQR)
- **Local Micro-Species:** `Cluster 5: I/O, UI & Routing Configuration` (Drift: 4.938 IQR)
- **Top Global Matches:** file_cluster_4: 9.184, file_cluster_8: 9.259, file_cluster_13: 9.426
- **Magnitude:** 83.26 | **LOC:** 166 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 81.0%
- **Risk Profile:** Cognitive Load (76.003%), Tech Debt (99.8629%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 24.4)
  * `run` (Impact: 4.5)
  * `run` (Impact: 2.7)
  * `run` (Impact: 1.9)
  * `run` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 42`, `args: 7`, `func_start: 5`
* *Risk/State:* `state_mutation: 6`, `duplicate_logic: 5`
* *Architecture:* `io: 11`, `api: 6`, `concurrency: 33`, `import: 7`
* *Defense:* `doc: 2`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` esbuild, node:module, posix, execa, promises, hereby, node:path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/src/ariaqueryhandler.spec.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.075 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.843 IQR)
- **Top Global Matches:** file_cluster_4: 10.075, file_cluster_8: 10.27, file_cluster_13: 10.892
- **Magnitude:** 81.1 | **LOC:** 859 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.2296%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 85.0)
  * `describe` (Impact: 65.2)
  * `describe` (Impact: 10.0)
  * `describe` (Impact: 7.4)
  * `it` (Impact: 7.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 378`, `args: 163`, `func_start: 119`
* *Risk/State:* `safety_bypasses: 25`, `high_risk_execution: 3`, `state_mutation: 29`, `duplicate_logic: 75`
* *Architecture:* `concurrency: 375`, `import: 6`
* *Defense:* `safety: 15`, `doc: 1`, `test: 113`, `immutability_locks: 98`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ElementHandle.js, node:assert, mocha-utils.js, puppeteer, expect, utils.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/puppeteer-core/src/api/locators/locators.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_2` (Drift: 12.528 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.076 IQR)
- **Top Global Matches:** file_cluster_2: 12.528, file_cluster_16: 12.544, file_cluster_13: 12.79
- **Magnitude:** 80.44 | **LOC:** 1150 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (47.8532%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `mergeMap` (Impact: 96.0)
  * `fill` (Impact: 79.2)
    * *Intent:* /** * Creates a new locator instance by cloning the current locator and * specifying whether to wait...
  * `mergeMap` (Impact: 60.9)
    * *Intent:* /** * If the element has a "disabled" property, wait for the element to be
  * `scroll` (Impact: 18.1)
  * `waitForVisibilityIfNeeded` (Impact: 12.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 255`, `args: 114`, `func_start: 93`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 93`, `duplicate_logic: 60`, `orphaned_logic: 4`
* *Architecture:* `api: 21`, `concurrency: 124`, `import: 9`
* *Defense:* `safety: 46`, `doc: 50`, `immutability_locks: 33`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Page.js, ElementHandle.js, rxjs.js, types.js, EventEmitter.js, util.js, Frame.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/puppeteer/CHANGELOG.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 79.98 | **LOC:** 3999 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `test/src/cookies.spec.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_4` (Drift: 9.49 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.443 IQR)
- **Top Global Matches:** file_cluster_4: 9.49, file_cluster_8: 9.593, file_cluster_7: 10.309
- **Magnitude:** 78.08 | **LOC:** 883 | **CtrlFlow:** 9.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (49.0743%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 91.9)
  * `describe` (Impact: 48.5)
  * `describe` (Impact: 23.9)
  * `describe` (Impact: 22.7)
  * `it` (Impact: 7.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 266`, `args: 111`, `func_start: 95`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 16`, `duplicate_logic: 58`
* *Architecture:* `io: 55`, `concurrency: 367`, `import: 2`
* *Defense:* `safety: 17`, `doc: 1`, `test: 94`, `immutability_locks: 78`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` expect, mocha-utils.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `website/docusaurus.config.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.253 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 3.8 IQR)
- **Top Global Matches:** file_cluster_8: 9.253, file_cluster_7: 9.828, file_cluster_13: 9.867
- **Magnitude:** 69.18 | **LOC:** 399 | **CtrlFlow:** 45.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (8.6047%), Tech Debt (70.8381%)
**Top Internal Functions/Classes:**
  * `getApiUrl` (Impact: 9.1)
  * `addNamespace` (Impact: 8.4)
  * `jsLoader` (Impact: 4.6)
  * `addNamespace` (Impact: 4.5)
  * `assert` (Impact: 3.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 26`, `args: 12`, `func_start: 8`
* *Risk/State:* `state_mutation: 23`, `duplicate_logic: 4`, `orphaned_logic: 2`
* *Architecture:* `io: 13`, `api: 1`, `concurrency: 4`, `import: 5`
* *Defense:* `safety: 7`, `doc: 12`, `test: 3`, `immutability_locks: 24`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` prism-react-renderer, node:assert, versionsArchived.json, types, plugin-client-redirects, preset-classic, remark-plugin-npm2yarn, semver
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/ng-schematics/src/schematics/ng-add/files/common/e2e/tests/utils.ts.template` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.706 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.427 IQR)
- **Top Global Matches:** file_cluster_4: 11.706, file_cluster_13: 12.145, file_cluster_8: 12.164
- **Magnitude:** 68.8 | **LOC:** 57 | **CtrlFlow:** 45.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setupBrowserHooks` (Impact: 28.3)
  * `afterEach` (Impact: 3.6)
  * `afterAll` (Impact: 3.6)
  * `after` (Impact: 3.6)
  * `getBrowserState` (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 18`, `args: 8`, `func_start: 8`
* *Risk/State:* `state_mutation: 6`, `orphaned_logic: 3`
* *Architecture:* `io: 2`, `api: 2`, `concurrency: 13`, `import: 2`
* *Defense:* `safety: 6`, `test: 2`, `immutability_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` node:test, puppeteer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/puppeteer-core/src/cdp/Page.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.894 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.288 IQR)
- **Top Global Matches:** file_cluster_4: 11.894, file_cluster_13: 12.008, file_cluster_8: 12.277
- **Magnitude:** 67.05 | **LOC:** 1370 | **CtrlFlow:** 27.7% | **Authorship Centralization:** 41.2%
- **Risk Profile:** Cognitive Load (90.0224%), Tech Debt (31.9909%)
**Top Internal Functions/Classes:**
  * `onConsoleAPI` (Impact: 21.8)
  * `_screenshot` (Impact: 21.7)
  * `_create` (Impact: 16.7)
  * `onBindingCalled` (Impact: 13.2)
  * `setCookie` (Impact: 12.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 214`, `args: 68`, `func_start: 59`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 56`, `duplicate_logic: 5`
* *Architecture:* `io: 5`, `api: 20`, `concurrency: 328`, `import: 51`
* *Defense:* `safety: 52`, `doc: 7`, `test: 7`, `immutability_locks: 50`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HTTPResponse.js, disposable.js, Connection.js, Frame.js, Coverage.js, Dialog.js, CdpSession.js, FileChooser.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/src/emulation.spec.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_4` (Drift: 9.772 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.96 IQR)
- **Top Global Matches:** file_cluster_4: 9.772, file_cluster_8: 9.86, file_cluster_7: 10.536
- **Magnitude:** 66.54 | **LOC:** 670 | **CtrlFlow:** 4.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (48.9192%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 60.5)
  * `describe` (Impact: 13.7)
  * `describe` (Impact: 11.7)
  * `describe` (Impact: 11.2)
  * `describe` (Impact: 10.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 325`, `args: 127`, `func_start: 115`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 16`, `duplicate_logic: 96`
* *Architecture:* `concurrency: 265`, `import: 3`
* *Defense:* `safety: 8`, `doc: 1`, `test: 110`, `immutability_locks: 43`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` expect, mocha-utils.js, puppeteer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/puppeteer-core/src/cdp/Input.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.911 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.582 IQR)
- **Top Global Matches:** file_cluster_4: 11.911, file_cluster_8: 12.42, file_cluster_13: 12.446
- **Magnitude:** 60.48 | **LOC:** 654 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.1048%), Tech Debt (99.8985%)
**Top Internal Functions/Classes:**
  * `keyDescriptionForString` (Impact: 26.9)
  * `getButtonFromPressedButtons` (Impact: 18.1)
  * `getFlag` (Impact: 16.4)
  * `reset` (Impact: 10.9)
  * `modifierBit` (Impact: 9.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 133`, `args: 63`, `func_start: 54`, `class_start: 5`
* *Risk/State:* `state_mutation: 101`, `dead_code: 1`, `duplicate_logic: 21`
* *Architecture:* `api: 8`, `concurrency: 314`, `import: 7`
* *Defense:* `safety: 34`, `doc: 10`, `test: 1`, `immutability_locks: 39`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ElementHandle.js, Input.js, devtools-protocol, USKeyboardLayout.js, Errors.js, CDPSession.js, assert.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `docker/Dockerfile` (DOCKERFILE | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_17` (Drift: 16.311 IQR)
- **Top Global Matches:** file_cluster_17: 16.311, file_cluster_13: 16.346, file_cluster_11: 16.516
- **Magnitude:** 58.36 | **LOC:** 40 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 93.3%
- **Risk Profile:** Cognitive Load (85.5422%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 4`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 9`, `dead_code: 1`
* *Architecture:* `io: 3`, `import: 1`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:24-bookworm
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `packages/puppeteer-core/src/api/BluetoothEmulation.ts` (TYPESCRIPT) | Magnitude: 4.92 | Delta: **0.195 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: doc: 9, indent_spaces: 5, structural_boundaries: 4, args: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/puppeteer-core/src/bidi/Page.ts` (TYPESCRIPT) | Magnitude: 47.0 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 427, concurrency: 154, structural_boundaries: 140, branch: 80
- `packages/ng-schematics/src/schematics/utils/files.ts` (TYPESCRIPT) | Magnitude: 5.91 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 94, structural_boundaries: 31, branch: 20, args: 14
- `packages/puppeteer-core/src/bidi/WebWorker.ts` (TYPESCRIPT) | Magnitude: 1.49 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 15, import: 7, encapsulation: 7
- `packages/puppeteer-core/src/bidi/CDPSession.ts` (TYPESCRIPT) | Magnitude: 11.54 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 88, structural_boundaries: 29, state_mutation: 29, concurrency: 24
- `test/src/proxy.spec.ts` (TYPESCRIPT) | Magnitude: 2.98 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 18, immutability_locks: 12, concurrency: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `tools/mocha-runner/src/reporter.cts` (TYPESCRIPT) | Magnitude: 0.49 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 4, args: 2, func_start: 2
- `packages/puppeteer-core/src/api/CDPSession.ts` (TYPESCRIPT) | Magnitude: 1.32 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 23, indent_spaces: 19, doc: 17, api: 11
- `packages/puppeteer-core/src/common/TaskQueue.ts` (TYPESCRIPT) | Magnitude: 1.13 | Delta: **0.129 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 8, args: 4, concurrency: 4
- `packages/puppeteer-core/src/common/LazyArg.ts` (TYPESCRIPT) | Magnitude: 1.72 | Delta: **0.205 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 15, indent_spaces: 13, concurrency: 7, generics: 7
- `packages/puppeteer-core/src/common/types.ts` (TYPESCRIPT) | Magnitude: 2.2 | Delta: **0.392 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 57, generics: 39, doc: 20, api: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `docker/Dockerfile` (DOCKERFILE) | Magnitude: 58.36 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 9, func_start: 5, structural_boundaries: 4, indent_spaces: 4
- `packages/puppeteer-core/src/cdp/FrameTree.ts` (TYPESCRIPT) | Magnitude: 9.23 | Delta: **0.124 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 68, state_mutation: 33, encapsulation: 26, structural_boundaries: 20
- `packages/puppeteer-core/src/bidi/Deserializer.ts` (TYPESCRIPT) | Magnitude: 13.48 | Delta: **0.14 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 72, structural_boundaries: 37, branch: 26, state_mutation: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `packages/puppeteer-core/src/injected/XPathQuerySelector.ts` (TYPESCRIPT) | Magnitude: 2.0 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 23, state_mutation: 9, branch: 6, immutability_locks: 4
- `packages/puppeteer-core/src/injected/util.ts` (TYPESCRIPT) | Magnitude: 4.05 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 40, branch: 15, structural_boundaries: 10, immutability_locks: 9
- `packages/puppeteer-core/src/api/Realm.ts` (TYPESCRIPT) | Magnitude: 4.66 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 78, structural_boundaries: 27, ui_framework: 26, concurrency: 19
- `packages/puppeteer-core/src/api/locators/locators.ts` (TYPESCRIPT) | Magnitude: 80.44 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 687, structural_boundaries: 255, generics: 190, ui_framework: 127
- `packages/puppeteer-core/src/injected/CSSSelector.ts` (TYPESCRIPT) | Magnitude: 0.9 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 5, api: 4, doc: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/ng-schematics/test/src/ng-add.test.ts` (TYPESCRIPT) | Magnitude: 13.91 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 227, args: 97, test: 87, func_start: 73
- `packages/browsers/test/src/chrome-headless-shell/install.spec.ts` (TYPESCRIPT) | Magnitude: 4.46 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 64, concurrency: 17, structural_boundaries: 16, io: 13
- `packages/browsers/test/src/chromedriver/install.spec.ts` (TYPESCRIPT) | Magnitude: 4.46 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 64, concurrency: 17, structural_boundaries: 16, io: 13
- `packages/puppeteer-core/src/util/Deferred.ts` (TYPESCRIPT) | Magnitude: 9.43 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 86, encapsulation: 36, concurrency: 27, structural_boundaries: 25
- `packages/puppeteer-core/src/bidi/core/Realm.ts` (TYPESCRIPT) | Magnitude: 28.74 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 254, state_mutation: 131, structural_boundaries: 84, concurrency: 62

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
- `packages/puppeteer-core/function-fixture.mjs` (JAVASCRIPT) | Magnitude: 29.1 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 24, args: 20, concurrency: 12, structural_boundaries: 11
- `packages/puppeteer-core/src/util/incremental-id-generator.ts` (TYPESCRIPT) | Magnitude: 1.01 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 7, args: 3, api: 3
- `packages/puppeteer/src/node/install.ts` (TYPESCRIPT) | Magnitude: 13.4 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 118, branch: 34, safety: 16, immutability_locks: 16
- `tools/sort-test-expectations.mjs` (JAVASCRIPT) | Magnitude: 0.06 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 108, state_mutation: 37, branch: 31, structural_boundaries: 24
- `packages/puppeteer-core/src/common/ConnectOptions.ts` (TYPESCRIPT) | Magnitude: 2.08 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 21, doc: 20, branch: 19

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/puppeteer-core/src/cdp/Page.ts` -> Churn: **65.77%** | Cog Load: 90.0224% | Debt: 31.9909%
- `docker/Dockerfile` -> Churn: **63.09%** | Cog Load: 85.5422% | Debt: 0.0%
- `packages/puppeteer-core/Herebyfile.mjs` -> Churn: **63.02%** | Cog Load: 76.003% | Debt: 99.8629%
- `packages/puppeteer-core/src/bidi/Page.ts` -> Churn: **56.62%** | Cog Load: 93.0996% | Debt: 83.6355%
- `packages/puppeteer-core/src/api/Page.ts` -> Churn: **50.7%** | Cog Load: 49.9912% | Debt: 95.0943%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `tools/docgen/src/custom_markdown_documenter.ts` -> **Nikolay Vitkov** (100.0% isolated ownership) | Magnitude: 1852.91
- `test/src/launcher.spec.ts` -> **Nikolay Vitkov** (100.0% isolated ownership) | Magnitude: 177.02
- `test/src/requestinterception-experimental.spec.ts` -> **Nikolay Vitkov** (100.0% isolated ownership) | Magnitude: 150.13
- `test/src/navigation.spec.ts` -> **Julian Descottes** (100.0% isolated ownership) | Magnitude: 119.83
- `test/src/locator.spec.ts` -> **Alex Rudenko** (100.0% isolated ownership) | Magnitude: 107.09

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/ng-schematics/src/schematics/utils/json.ts` -> **Severity: 0.459** (Embedded: 0.012 * Error Risk: 38.3322%)
- `tools/docgen/src/docgen.ts` -> **Severity: 0.092** (Embedded: 0.002 * Error Risk: 46.257%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/puppeteer-core/src/puppeteer-core.ts` -> **Severity: 680.363** (Blast Radius: 57.076 * Doc Risk: 11.9203%)
- `packages/puppeteer/src/puppeteer.ts` -> **Severity: 631.967** (Blast Radius: 53.016 * Doc Risk: 11.9203%)
- `packages/ng-schematics/src/schematics/utils/json.ts` -> **Severity: 582.75** (Blast Radius: 9.296 * Doc Risk: 62.6883%)
- `packages/browsers/src/main.ts` -> **Severity: 172.4** (Blast Radius: 1.724 * Doc Risk: 100.0%)
- `packages/puppeteer-core/src/api/api.ts` -> **Severity: 172.4** (Blast Radius: 1.724 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
