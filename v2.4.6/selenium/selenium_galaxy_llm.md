# ARCHITECTURAL_BRIEF: selenium
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_python/selenium` |
| **Timestamp** | `2026-08-03T19:41:27.505546+00:00` |
| **Scan Duration** | `10.08s` |
| **Git Branch** | `trunk` |
| **Git Commit** | `549261ba1cccb1d3bfa662d35d7b144607abf51c` |
| **Git Remote** | `https://github.com/SeleniumHQ/selenium.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 2205 malicious artifacts.

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
| Total Artifacts | 5042 |
| Analyzed Artifacts (Scanned) | 2635 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2407 |
| Total LOC | 157436 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 52.3% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5859 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1637 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.4316 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 175 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 968 | 64615 | 36.7% |
| CSHARP | 509 | 21565 | 19.3% |
| CPP | 247 | 20577 | 9.4% |
| HTML | 233 | 11286 | 8.8% |
| PYTHON | 198 | 13433 | 7.5% |
| JAVASCRIPT | 138 | 10982 | 5.2% |
| PLAINTEXT | 125 | 3 | 4.7% |
| TYPESCRIPT | 63 | 4675 | 2.4% |
| RUST | 36 | 6825 | 1.4% |
| XML | 27 | 9 | 1.0% |
| MARKDOWN | 26 | 0 | 1.0% |
| SHELL | 18 | 385 | 0.7% |
| RUBY | 17 | 1593 | 0.6% |
| JSON | 14 | 547 | 0.5% |
| YAML | 3 | 215 | 0.1% |
| POWERSHELL | 3 | 179 | 0.1% |
| DOCKERFILE | 3 | 128 | 0.1% |
| CSS | 2 | 27 | 0.1% |
| BATCH | 2 | 65 | 0.1% |
| MAKEFILE | 1 | 9 | 0.0% |
| C | 1 | 317 | 0.0% |
| BINARY_THREAT | 1 | 1 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.666`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 1235 | 46.9% |
| file_cluster_13 | 828 | 31.4% |
| file_cluster_16 | 139 | 5.3% |
| file_cluster_0 | 98 | 3.7% |
| file_cluster_4 | 76 | 2.9% |
| file_cluster_7 | 47 | 1.8% |
| file_cluster_2 | 14 | 0.5% |
| file_cluster_17 | 11 | 0.4% |
| file_cluster_15 | 10 | 0.4% |
| file_cluster_9 | 6 | 0.2% |
| file_cluster_12 | 5 | 0.2% |
| Unknown | 4 | 0.2% |
| file_cluster_11 | 3 | 0.1% |
| file_cluster_1 | 1 | 0.0% |
| file_cluster_6 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 148 | 5.6% |
| Static: Minified & Vendor Opaque Mass | 9 | 0.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2407*

**Composition by Extension & Reason:**
- `.java`: 492x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 354x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rb`: 301x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.bazel`: 213x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Unsupported Extension: '.bazel')
- `.rbs`: 175x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 25x Excluded (Unsupported Extension: '.rbs')
- `.cs`: 194x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 141x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 88 LOC), 1x Excluded (Machine-Generated Source Code Signature: 217 LOC)
- `.html`: 103x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 3 exceeds 500 chars), 1x Excluded (Saturation: Line 10 exceeds 500 chars)
- `.css`: 54x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 35x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable), 2x Unsupported Format (.bazelproject)
- `.yml`: 39x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 31x Excluded (Explicitly Denied Extension: '.png')
- `.xml`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.bzl`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 10 exceeds 500 chars)
- `.json`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 17193 LOC), 1x Excluded (Massive Static Asset Blob: 3476 LOC)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 20.6 | 7.9 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.3 | 28.0 | 12.2 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 36.6 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 19.7 | 2.4 | 80.0 |
| API Exposure | 0.0 | 17.0 | 4.5 | 4.3 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 7.6 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 34.3 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 99.7 | 0.5 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 84.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 1.9 | 0.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 6.6 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 54.2 | 56.1 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 29.9 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 16.5 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 5.5 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `common/src/web/macbeth.html` (Hits: 3036)
- `cpp/linux-specific/x_ignore_nofocus.c` (Hits: 74)
- `py/selenium/webdriver/firefox/firefox_profile.py` (Hits: 40)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Require.java** (`java/src/org/openqa/selenium/internal/Require.java`) — 359 inbound connections
2. **Json.java** (`java/src/org/openqa/selenium/json/Json.java`) — 131 inbound connections
3. **Optional.cs** (`dotnet/src/webdriver/BiDi/Optional.cs`) — 126 inbound connections
4. **Logger.cs** (`dotnet/src/webdriver/Internal/Logging/Logger.cs`) — 120 inbound connections
5. **Capabilities.java** (`java/src/org/openqa/selenium/Capabilities.java`) — 108 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **LocalNode.java** (`java/src/org/openqa/selenium/grid/node/local/LocalNode.java`) — 114 outbound dependencies
2. **KubernetesSessionFactory.java** (`java/src/org/openqa/selenium/grid/node/kubernetes/KubernetesSessionFactory.java`) — 95 outbound dependencies
3. **RemoteWebDriver.java** (`java/src/org/openqa/selenium/remote/RemoteWebDriver.java`) — 87 outbound dependencies
4. **AbstractHttpCommandCodec.java** (`java/src/org/openqa/selenium/remote/codec/AbstractHttpCommandCodec.java`) — 86 outbound dependencies
5. **LocalDistributor.java** (`java/src/org/openqa/selenium/grid/distributor/local/LocalDistributor.java`) — 83 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `Browser::NewWindow3` (@ `cpp/iedriver/Browser.cpp`) -> Impact: **1866.0** | LOC: 627
- `Element::IsFocusable` (@ `cpp/iedriver/Element.cpp`) -> Impact: **1495.6** | LOC: 807
- `NewSessionCommandHandler::ValidateCapabi` (@ `cpp/iedriver/CommandHandlers/NewSessionCommandHandler.cpp`) -> Impact: **1221.4** | LOC: 348
- `WebDriver` (@ `dotnet/src/webdriver/WebDriver.cs`) -> Impact: **1201.8** | LOC: 758
  * *Intent:* /// <summary> /// Initializes a new instance of the <see cref="WebDriver"/> class. /// </summary> /// <param name="executor">The <see cref="ICommandEx...
- `parse` (@ `common/devtools/pdl.py`) -> Impact: **1086.5** | LOC: 129
- `fireMSPointerEvent` (@ `javascript/atoms/device.js`) -> Impact: **684.6** | LOC: 373
  * *Intent:* // On click and mousedown events, captured pointers are ignored and the
- `Alert::Dismiss` (@ `cpp/iedriver/Alert.cpp`) -> Impact: **662.6** | LOC: 383
- `quit` (@ `java/src/org/openqa/selenium/remote/RemoteWebDriver.java`) -> Impact: **624.0** | LOC: 581
- `SendKeysCommandHandler::CreateActionSequ` (@ `cpp/iedriver/CommandHandlers/SendKeysCommandHandler.cpp`) -> Impact: **558.2** | LOC: 494
- `find_elements` (@ `py/selenium/webdriver/remote/webdriver.py`) -> Impact: **558.0** | LOC: 480

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `read_m2_user_pass` (@ `rake_tasks/java.rake`) -> **O(2^N) [Recursive]**
- `__convert_to_local_value` (@ `py/selenium/webdriver/common/bidi/script.py`) -> **O(2^N) [Recursive]**
- `_request` (@ `py/selenium/webdriver/remote/remote_connection.py`) -> **O(2^N) [Recursive]**
  * *Intent:* """Retrieve a command if it exists."""
- `update_preferences` (@ `py/selenium/webdriver/firefox/firefox_profile.py`) -> **O(2^N) [Recursive]**
- `JavaScriptActionSimulator::SimulateActio` (@ `cpp/iedriver/ActionSimulators/JavaScriptActionSimulator.cpp`) -> **O(2^N) [Recursive]**
- `PersistentEventSimulator` (@ `cpp/iedriver/ActionSimulators/PersistentEventSimulator.cpp`) -> **O(2^N) [Recursive]**
- `SendInputActionSimulator::SimulateAction` (@ `cpp/iedriver/ActionSimulators/SendInputActionSimulator.cpp`) -> **O(2^N) [Recursive]**
- `Alert::Dismiss` (@ `cpp/iedriver/Alert.cpp`) -> **O(2^N) [Recursive]**
- `AsyncScriptExecutor::ThreadProc` (@ `cpp/iedriver/AsyncScriptExecutor.cpp`) -> **O(2^N) [Recursive]**
- `AsyncScriptExecutor::OnCreate` (@ `cpp/iedriver/AsyncScriptExecutor.cpp`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `Element::IsFocusable` (@ `cpp/iedriver/Element.cpp`) -> DB Complexity: **331**
- `Browser::NewWindow3` (@ `cpp/iedriver/Browser.cpp`) -> DB Complexity: **147**
- `Alert::Dismiss` (@ `cpp/iedriver/Alert.cpp`) -> DB Complexity: **133**
- `SendKeysCommandHandler::CreateActionSequ` (@ `cpp/iedriver/CommandHandlers/SendKeysCommandHandler.cpp`) -> DB Complexity: **125**
- `Anonymous_Block_[Truncated]` (@ `scripts/format.sh`) -> DB Complexity: **119**
- `setup_pypirc_[Truncated]` (@ `rake_tasks/python.rake`) -> DB Complexity: **91**
- `NewSessionCommandHandler::ValidateCapabi` (@ `cpp/iedriver/CommandHandlers/NewSessionCommandHandler.cpp`) -> DB Complexity: **91**
- `Read` (@ `dotnet/src/webdriver/BiDi/Json/Converters/Polymorphic/RemoteValueConverter.cs`) -> DB Complexity: **80**
- `IECommandExecutor::OpenNewBrowserWindow` (@ `cpp/iedriver/IECommandExecutor.cpp`) -> DB Complexity: **72**
- `ExecuteAsyncScriptCommandHandler::Execut` (@ `cpp/iedriver/CommandHandlers/ExecuteAsyncScriptCommandHandler.cpp`) -> DB Complexity: **70**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `rust/src` | 19 | 49559.66 | 20.17% | 51.96% |
| `cpp/iedriver` | 72 | 21503.5 | 38.95% | 32.66% |
| `dotnet/src/webdriver` | 128 | 10994.75 | 12.85% | 48.38% |
| `dotnet/src/webdriver/BiDi/BrowsingContext` | 37 | 10850.96 | 33.97% | 16.68% |
| `cpp/iedriver/CommandHandlers` | 116 | 10833.34 | 52.73% | 44.3% |
| `java/src/org/openqa/selenium/remote` | 60 | 6143.43 | 15.32% | 47.0% |
| `__monolith__` | 19 | 5297.24 | 9.73% | 15.78% |
| `javascript/selenium-webdriver/bidi` | 35 | 5157.04 | 25.34% | 38.41% |
| `javascript/grid-ui` | 6 | 5061.5 | 5.58% | 0.0% |
| `common/extensions/webextensions-selenium-example-signed/META-INF` | 1 | 5000.0 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `rake_tasks/dotnet.rake` -> **100.0%** Exposure
- `rake_tasks/rust.rake` -> **100.0%** Exposure
- `rb/Gemfile` -> **100.0%** Exposure
- `rb/Rakefile` -> **100.0%** Exposure
- `dotnet/private/dotnet_utils.bzl` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `common/devtools/pdl.py` -> **100.0%** Exposure
- `javascript/grid-ui/scripts/rmSourcemaps.py` -> **100.0%** Exposure
- `py/selenium/webdriver/chromium/service.py` -> **100.0%** Exposure
- `py/selenium/webdriver/common/bidi/cdp.py` -> **100.0%** Exposure
- `py/selenium/webdriver/common/bidi/emulation.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `java/src/org/openqa/selenium/support/events/WebDriverListener.java` -> **114** Orphaned Functions | **34** Duplicates
- `java/src/org/openqa/selenium/devtools/CdpClientGenerator.java` -> **1** Orphaned Functions | **53** Duplicates
- `java/src/org/openqa/selenium/support/ui/ExpectedConditions.java` -> **16** Orphaned Functions | **33** Duplicates
- `dotnet/src/webdriver/BiDi/BrowsingContext/BrowsingContextModule.cs` -> **13** Orphaned Functions | **28** Duplicates
- `py/selenium/webdriver/common/bidi/browsing_context.py` -> **0** Orphaned Functions | **40** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`javascript/atoms/locators/css.js`** -> AI Confidence: **99.48%**
2. **`cpp/iedriver/ActionSimulators/SendMessageActionSimulator.cpp`** -> AI Confidence: **99.48%**
3. **`cpp/iedriver/InputManager.cpp`** -> AI Confidence: **99.48%**
4. **`cpp/iedriver/ProxyManager.cpp`** -> AI Confidence: **99.48%**
5. **`cpp/imehandler/windows/src/winapihandler.cc`** -> AI Confidence: **99.48%**
6. **`cpp/linux-specific/print_events.h`** -> AI Confidence: **99.48%**
7. **`dotnet/src/webdriver/WebDriver.cs`** -> AI Confidence: **99.48%**
8. **`Rakefile`** -> AI Confidence: **99.39%**
9. **`javascript/atoms/action.js`** -> AI Confidence: **99.39%**
10. **`javascript/atoms/keyboard.js`** -> AI Confidence: **99.39%**
11. **`javascript/atoms/mouse.js`** -> AI Confidence: **99.39%**
12. **`javascript/atoms/touchscreen.js`** -> AI Confidence: **99.39%**
13. **`cpp/iedriver/CommandHandlers/NewSessionCommandHandler.cpp`** -> AI Confidence: **99.39%**
14. **`cpp/iedriver/CookieManager.cpp`** -> AI Confidence: **99.39%**
15. **`cpp/iedriver/Element.cpp`** -> AI Confidence: **99.39%**
16. **`cpp/iedriver/IESession.cpp`** -> AI Confidence: **99.39%**
17. **`cpp/iedriver/Script.cpp`** -> AI Confidence: **99.39%**
18. **`cpp/webdriver-interactions/interactions_common.cpp`** -> AI Confidence: **99.34%**
19. **`javascript/webdriver/stacktrace.js`** -> AI Confidence: **99.32%**
20. **`dotnet/src/webdriver/Proxy.cs`** -> AI Confidence: **99.32%**
21. **`py/selenium/webdriver/common/bidi/browsing_context.py`** -> AI Confidence: **99.31%**
22. **`py/selenium/webdriver/common/selenium_manager.py`** -> AI Confidence: **99.31%**
23. **`py/selenium/webdriver/remote/client_config.py`** -> AI Confidence: **99.31%**
24. **`scripts/pinned_browsers.py`** -> AI Confidence: **99.31%**
25. **`scripts/update_cdp.py`** -> AI Confidence: **99.31%**
26. **`py/selenium/webdriver/firefox/firefox_profile.py`** -> AI Confidence: **99.31%**
27. **`javascript/atoms/device.js`** -> AI Confidence: **99.31%**
28. **`javascript/atoms/dom.js`** -> AI Confidence: **99.31%**
29. **`javascript/atoms/domcore.js`** -> AI Confidence: **99.31%**
30. **`javascript/atoms/events.js`** -> AI Confidence: **99.31%**
31. **`javascript/atoms/inject.js`** -> AI Confidence: **99.31%**
32. **`javascript/atoms/locators/xpath.js`** -> AI Confidence: **99.31%**
33. **`javascript/atoms/window.js`** -> AI Confidence: **99.31%**
34. **`javascript/selenium-webdriver/index.js`** -> AI Confidence: **99.31%**
35. **`javascript/selenium-webdriver/testing/index.js`** -> AI Confidence: **99.31%**
36. **`javascript/webdriver/atoms/element.js`** -> AI Confidence: **99.31%**
37. **`cpp/iedriver/Alert.cpp`** -> AI Confidence: **99.31%**
38. **`cpp/iedriver/AsyncScriptExecutor.cpp`** -> AI Confidence: **99.31%**
39. **`cpp/iedriver/Browser.cpp`** -> AI Confidence: **99.31%**
40. **`cpp/iedriver/BrowserFactory.cpp`** -> AI Confidence: **99.31%**
41. **`cpp/iedriver/CommandHandlers/AddCookieCommandHandler.cpp`** -> AI Confidence: **99.31%**
42. **`cpp/iedriver/CommandHandlers/ClearElementCommandHandler.cpp`** -> AI Confidence: **99.31%**
43. **`cpp/iedriver/CommandHandlers/ClickElementCommandHandler.cpp`** -> AI Confidence: **99.31%**
44. **`cpp/iedriver/CommandHandlers/GetElementRectCommandHandler.cpp`** -> AI Confidence: **99.31%**
45. **`cpp/iedriver/CommandHandlers/SendKeysCommandHandler.cpp`** -> AI Confidence: **99.31%**
46. **`cpp/iedriver/DocumentHost.cpp`** -> AI Confidence: **99.31%**
47. **`cpp/iedriver/ElementFinder.cpp`** -> AI Confidence: **99.31%**
48. **`cpp/iedriver/IECommandExecutor.cpp`** -> AI Confidence: **99.31%**
49. **`cpp/iedriver/IECommandHandler.cpp`** -> AI Confidence: **99.31%**
50. **`cpp/iedriver/VariantUtilities.cpp`** -> AI Confidence: **99.31%**
51. **`cpp/iedriverserver/IEDriverServer.cpp`** -> AI Confidence: **99.31%**
52. **`cpp/imehandler/linux/src/ibushandler.cpp`** -> AI Confidence: **99.31%**
53. **`cpp/webdriver-interactions/interactions.cpp`** -> AI Confidence: **99.31%**
54. **`cpp/webdriver-interactions/interactions_linux_common.cpp`** -> AI Confidence: **99.31%**
55. **`cpp/webdriver-interactions/interactions_linux_mouse.cpp`** -> AI Confidence: **99.31%**
56. **`cpp/webdriver-interactions/logging.h`** -> AI Confidence: **99.31%**
57. **`cpp/webdriver-server/server.cc`** -> AI Confidence: **99.31%**
58. **`dotnet/src/webdriver/Manager/SeleniumManager.cs`** -> AI Confidence: **99.31%**
59. **`dotnet/src/webdriver/Remote/HttpCommandExecutor.cs`** -> AI Confidence: **99.31%**
60. **`cpp/linux-specific/x_ignore_nofocus.c`** -> AI Confidence: **99.31%**
61. **`java/src/org/openqa/selenium/Proxy.java`** -> AI Confidence: **99.31%**
62. **`java/src/org/openqa/selenium/bidi/network/Cookie.java`** -> AI Confidence: **99.31%**
63. **`java/src/org/openqa/selenium/bidi/network/ResponseData.java`** -> AI Confidence: **99.31%**
64. **`java/src/org/openqa/selenium/bidi/script/RemoteValue.java`** -> AI Confidence: **99.31%**
65. **`java/src/org/openqa/selenium/docker/internal/Reference.java`** -> AI Confidence: **99.31%**
66. **`java/src/org/openqa/selenium/grid/commands/CompletionCommand.java`** -> AI Confidence: **99.31%**
67. **`java/src/org/openqa/selenium/grid/commands/InfoCommand.java`** -> AI Confidence: **99.31%**
68. **`java/src/org/openqa/selenium/grid/config/AnnotatedConfig.java`** -> AI Confidence: **99.31%**
69. **`java/src/org/openqa/selenium/grid/config/CompoundConfig.java`** -> AI Confidence: **99.31%**
70. **`java/src/org/openqa/selenium/grid/config/TomlConfig.java`** -> AI Confidence: **99.31%**
71. **`java/src/org/openqa/selenium/grid/data/CapabilityCount.java`** -> AI Confidence: **99.31%**
72. **`java/src/org/openqa/selenium/grid/data/SessionClosedData.java`** -> AI Confidence: **99.31%**
73. **`java/src/org/openqa/selenium/grid/data/SessionEventData.java`** -> AI Confidence: **99.31%**
74. **`java/src/org/openqa/selenium/grid/distributor/local/LocalNodeRegistry.java`** -> AI Confidence: **99.31%**
75. **`java/src/org/openqa/selenium/grid/jmx/MBean.java`** -> AI Confidence: **99.31%**
76. **`java/src/org/openqa/selenium/grid/node/ProxyNodeWebsockets.java`** -> AI Confidence: **99.31%**
77. **`java/src/org/openqa/selenium/grid/node/config/NodeFlags.java`** -> AI Confidence: **99.31%**
78. **`java/src/org/openqa/selenium/grid/node/config/SessionCapabilitiesMutator.java`** -> AI Confidence: **99.31%**
79. **`java/src/org/openqa/selenium/grid/node/kubernetes/KubernetesFlags.java`** -> AI Confidence: **99.31%**
80. **`java/src/org/openqa/selenium/grid/node/kubernetes/KubernetesOptions.java`** -> AI Confidence: **99.31%**
81. **`java/src/org/openqa/selenium/grid/web/ResourceHandler.java`** -> AI Confidence: **99.31%**
82. **`java/src/org/openqa/selenium/json/JsonInput.java`** -> AI Confidence: **99.31%**
83. **`java/src/org/openqa/selenium/json/JsonOutput.java`** -> AI Confidence: **99.31%**
84. **`java/src/org/openqa/selenium/manager/SeleniumManagerOutput.java`** -> AI Confidence: **99.31%**
85. **`java/src/org/openqa/selenium/net/HostIdentifier.java`** -> AI Confidence: **99.31%**
86. **`java/src/org/openqa/selenium/net/NetworkUtils.java`** -> AI Confidence: **99.31%**
87. **`java/src/org/openqa/selenium/net/UrlChecker.java`** -> AI Confidence: **99.31%**
88. **`java/src/org/openqa/selenium/netty/server/MessageInboundConverter.java`** -> AI Confidence: **99.31%**
89. **`java/src/org/openqa/selenium/remote/ErrorHandler.java`** -> AI Confidence: **99.31%**
90. **`java/src/org/openqa/selenium/remote/WebElementToJsonConverter.java`** -> AI Confidence: **99.31%**
91. **`java/src/org/openqa/selenium/remote/http/jdk/JdkHttpMessages.java`** -> AI Confidence: **99.31%**
92. **`java/src/org/openqa/selenium/remote/service/DriverFinder.java`** -> AI Confidence: **99.31%**
93. **`java/src/org/openqa/selenium/support/events/EventFiringDecorator.java`** -> AI Confidence: **99.31%**
94. **`java/src/org/openqa/selenium/support/ui/Select.java`** -> AI Confidence: **99.31%**
95. **`javascript/grid-ui/src/App.tsx`** -> AI Confidence: **99.31%**
96. **`rust/src/edge.rs`** -> AI Confidence: **99.31%**
97. **`rust/src/files.rs`** -> AI Confidence: **99.31%**
98. **`rust/src/firefox.rs`** -> AI Confidence: **99.31%**
99. **`rust/src/lib.rs`** -> AI Confidence: **99.31%**
100. **`rust/src/logger.rs`** -> AI Confidence: **99.31%**
101. **`rake_tasks/appium.rake`** -> AI Confidence: **99.29%**
102. **`rake_tasks/bazel.rake`** -> AI Confidence: **99.29%**
103. **`rake_tasks/dotnet.rake`** -> AI Confidence: **99.29%**
104. **`rake_tasks/java.rake`** -> AI Confidence: **99.29%**
105. **`rake_tasks/node.rake`** -> AI Confidence: **99.29%**
106. **`rake_tasks/python.rake`** -> AI Confidence: **99.29%**
107. **`rake_tasks/ruby.rake`** -> AI Confidence: **99.29%**
108. **`rb/support/rbs_collection_update.rb`** -> AI Confidence: **99.29%**
109. **`common/repositories.bzl`** -> AI Confidence: **99.29%**
110. **`java/private/module.bzl`** -> AI Confidence: **99.29%**
111. **`javascript/private/header.bzl`** -> AI Confidence: **99.29%**
112. **`javascript/bidi-support/bidi-mutation-listener.js`** -> AI Confidence: **99.29%**
113. **`javascript/grid-ui/jest.config.cjs`** -> AI Confidence: **99.29%**
114. **`javascript/selenium-webdriver/common/driverFinder.js`** -> AI Confidence: **99.29%**
115. **`javascript/webdriver/key.js`** -> AI Confidence: **99.29%**
116. **`go`** -> AI Confidence: **99.29%**
117. **`scripts/build-info.sh`** -> AI Confidence: **99.29%**
118. **`scripts/format.sh`** -> AI Confidence: **99.29%**
119. **`scripts/github-actions/collect-test-logs.sh`** -> AI Confidence: **99.29%**
120. **`scripts/gitpod/start-vnc.sh`** -> AI Confidence: **99.29%**
121. **`cpp/iedriver/ActionSimulators/ActionSimulator.cpp`** -> AI Confidence: **99.29%**
122. **`dotnet/src/webdriver/BiDi/Browser/IBrowserModule.cs`** -> AI Confidence: **99.29%**
123. **`dotnet/src/webdriver/BiDi/BrowsingContext/IBrowsingContextModule.cs`** -> AI Confidence: **99.29%**
124. **`dotnet/src/webdriver/BiDi/BrowsingContext/IBrowsingContextNetworkModule.cs`** -> AI Confidence: **99.29%**
125. **`dotnet/src/webdriver/BiDi/BrowsingContext/IBrowsingContextScriptModule.cs`** -> AI Confidence: **99.29%**
126. **`dotnet/src/webdriver/BiDi/Emulation/IEmulationModule.cs`** -> AI Confidence: **99.29%**
127. **`dotnet/src/webdriver/BiDi/Input/IInputModule.cs`** -> AI Confidence: **99.29%**
128. **`dotnet/src/webdriver/BiDi/Network/INetworkModule.cs`** -> AI Confidence: **99.29%**
129. **`dotnet/src/webdriver/BiDi/Script/IScriptModule.cs`** -> AI Confidence: **99.29%**
130. **`dotnet/src/webdriver/BiDi/Session/ISessionModule.cs`** -> AI Confidence: **99.29%**
131. **`dotnet/src/webdriver/Chromium/ChromiumDriverService.cs`** -> AI Confidence: **99.29%**
132. **`dotnet/src/webdriver/Chromium/ChromiumOptions.cs`** -> AI Confidence: **99.29%**
133. **`dotnet/src/webdriver/ErrorResponse.cs`** -> AI Confidence: **99.29%**
134. **`dotnet/src/webdriver/Firefox/FirefoxOptions.cs`** -> AI Confidence: **99.29%**
135. **`dotnet/src/webdriver/Firefox/Internal/IniFileReader.cs`** -> AI Confidence: **99.29%**
136. **`dotnet/src/webdriver/IE/InternetExplorerOptions.cs`** -> AI Confidence: **99.29%**
137. **`dotnet/src/webdriver/Internal/ResponseValueJsonConverter.cs`** -> AI Confidence: **99.29%**
138. **`scripts/build-info.ps1`** -> AI Confidence: **99.29%**
139. **`scripts/dev-environment-setup.ps1`** -> AI Confidence: **99.29%**
140. **`scripts/gitpod/.gitpod.Dockerfile`** -> AI Confidence: **99.29%**
141. **`scripts/remote-image/Dockerfile`** -> AI Confidence: **99.29%**
142. **`javascript/atoms/json.js`** -> AI Confidence: **99.26%**
143. **`java/src/org/openqa/selenium/manager/SeleniumManager.java`** -> AI Confidence: **99.25%**
144. **`py/selenium/webdriver/common/service.py`** -> AI Confidence: **99.24%**
145. **`py/selenium/webdriver/remote/remote_connection.py`** -> AI Confidence: **99.24%**
146. **`javascript/atoms/locators/locators.js`** -> AI Confidence: **99.24%**
147. **`cpp/iedriver/CommandHandlers/ScreenshotElementCommandHandler.cpp`** -> AI Confidence: **99.24%**
148. **`cpp/webdriver-server/logging.h`** -> AI Confidence: **99.24%**
149. **`java/src/dev/selenium/tools/javadoc/JavadocJarMaker.java`** -> AI Confidence: **99.24%**
150. **`java/src/org/openqa/selenium/SharedCapabilitiesMethods.java`** -> AI Confidence: **99.24%**
151. **`java/src/org/openqa/selenium/bidi/Connection.java`** -> AI Confidence: **99.24%**
152. **`java/src/org/openqa/selenium/chromium/ChromiumOptions.java`** -> AI Confidence: **99.24%**
153. **`java/src/org/openqa/selenium/devtools/CdpEndpointFinder.java`** -> AI Confidence: **99.24%**
154. **`java/src/org/openqa/selenium/devtools/SeleniumCdpConnection.java`** -> AI Confidence: **99.24%**
155. **`java/src/org/openqa/selenium/firefox/FileExtension.java`** -> AI Confidence: **99.24%**
156. **`java/src/org/openqa/selenium/firefox/Preferences.java`** -> AI Confidence: **99.24%**
157. **`java/src/org/openqa/selenium/firefox/ProfilesIni.java`** -> AI Confidence: **99.24%**
158. **`java/src/org/openqa/selenium/grid/Bootstrap.java`** -> AI Confidence: **99.24%**
159. **`java/src/org/openqa/selenium/grid/config/ConcatenatingConfig.java`** -> AI Confidence: **99.24%**
160. **`java/src/org/openqa/selenium/grid/config/ConfigFlags.java`** -> AI Confidence: **99.24%**
161. **`java/src/org/openqa/selenium/grid/config/MapConfig.java`** -> AI Confidence: **99.24%**
162. **`java/src/org/openqa/selenium/grid/data/NodeStatus.java`** -> AI Confidence: **99.24%**
163. **`java/src/org/openqa/selenium/grid/data/Session.java`** -> AI Confidence: **99.24%**
164. **`java/src/org/openqa/selenium/grid/distributor/local/LocalGridModel.java`** -> AI Confidence: **99.24%**
165. **`java/src/org/openqa/selenium/grid/node/docker/DockerFlags.java`** -> AI Confidence: **99.24%**
166. **`java/src/org/openqa/selenium/grid/node/docker/DockerSessionFactory.java`** -> AI Confidence: **99.24%**
167. **`java/src/org/openqa/selenium/grid/node/kubernetes/KubernetesSession.java`** -> AI Confidence: **99.24%**
168. **`java/src/org/openqa/selenium/grid/node/kubernetes/KubernetesSessionFactory.java`** -> AI Confidence: **99.24%**
169. **`java/src/org/openqa/selenium/grid/node/relay/RelayFlags.java`** -> AI Confidence: **99.24%**
170. **`java/src/org/openqa/selenium/grid/sessionmap/jdbc/JdbcBackedSessionMap.java`** -> AI Confidence: **99.24%**
171. **`java/src/org/openqa/selenium/io/FileHandler.java`** -> AI Confidence: **99.24%**
172. **`java/src/org/openqa/selenium/json/InstanceCoercer.java`** -> AI Confidence: **99.24%**
173. **`java/src/org/openqa/selenium/json/InstantCoercer.java`** -> AI Confidence: **99.24%**
174. **`java/src/org/openqa/selenium/logging/LogLevelMapping.java`** -> AI Confidence: **99.24%**
175. **`java/src/org/openqa/selenium/net/DefaultNetworkInterfaceProvider.java`** -> AI Confidence: **99.24%**
176. **`java/src/org/openqa/selenium/netty/server/WebSocketFrameProxy.java`** -> AI Confidence: **99.24%**
177. **`java/src/org/openqa/selenium/os/ExecutableFinder.java`** -> AI Confidence: **99.24%**
178. **`java/src/org/openqa/selenium/remote/ElementLocation.java`** -> AI Confidence: **99.24%**
179. **`java/src/org/openqa/selenium/remote/ErrorCodec.java`** -> AI Confidence: **99.24%**
180. **`java/src/org/openqa/selenium/remote/NewSessionPayload.java`** -> AI Confidence: **99.24%**
181. **`java/src/org/openqa/selenium/remote/codec/AbstractHttpResponseCodec.java`** -> AI Confidence: **99.24%**
182. **`java/src/org/openqa/selenium/remote/http/jdk/JdkHttpClient.java`** -> AI Confidence: **99.24%**
183. **`java/src/org/openqa/selenium/remote/service/DriverCommandExecutor.java`** -> AI Confidence: **99.24%**
184. **`java/src/org/openqa/selenium/remote/service/DriverService.java`** -> AI Confidence: **99.24%**
185. **`java/src/org/openqa/selenium/remote/tracing/Tags.java`** -> AI Confidence: **99.24%**
186. **`java/src/org/openqa/selenium/support/events/WebDriverListener.java`** -> AI Confidence: **99.24%**
187. **`javascript/grid-ui/src/screens/Overview/Overview.tsx`** -> AI Confidence: **99.24%**
188. **`javascript/grid-ui/src/screens/Sessions/Sessions.tsx`** -> AI Confidence: **99.24%**
189. **`javascript/grid-ui/src/util/browser-logo.tsx`** -> AI Confidence: **99.24%**
190. **`rust/src/chrome.rs`** -> AI Confidence: **99.24%**
191. **`rust/src/main.rs`** -> AI Confidence: **99.24%**
192. **`py/selenium/webdriver/remote/server.py`** -> AI Confidence: **99.23%**
193. **`scripts/update_docfx.py`** -> AI Confidence: **99.23%**
194. **`javascript/atoms/frame.js`** -> AI Confidence: **99.23%**
195. **`javascript/selenium-webdriver/common/seleniumManager.js`** -> AI Confidence: **99.23%**
196. **`javascript/webdriver/atoms/inputs.js`** -> AI Confidence: **99.23%**
197. **`cpp/iedriver/CommandHandlers/ActionsCommandHandler.cpp`** -> AI Confidence: **99.23%**
198. **`cpp/iedriver/CommandHandlers/GetElementTextCommandHandler.cpp`** -> AI Confidence: **99.23%**
199. **`cpp/iedriver/CommandHandlers/SwitchToFrameCommandHandler.cpp`** -> AI Confidence: **99.23%**
200. **`cpp/iedriver/HookProcessor.cpp`** -> AI Confidence: **99.23%**
201. **`java/src/org/openqa/selenium/Capabilities.java`** -> AI Confidence: **99.23%**
202. **`java/src/org/openqa/selenium/WebDriverException.java`** -> AI Confidence: **99.23%**
203. **`java/src/org/openqa/selenium/grid/config/Config.java`** -> AI Confidence: **99.23%**
204. **`java/src/org/openqa/selenium/grid/data/SessionCreatedData.java`** -> AI Confidence: **99.23%**
205. **`java/src/org/openqa/selenium/grid/server/BaseServerFlags.java`** -> AI Confidence: **99.23%**
206. **`java/src/org/openqa/selenium/remote/http/UrlTemplate.java`** -> AI Confidence: **99.23%**
207. **`javascript/grid-ui/src/components/Node/Node.tsx`** -> AI Confidence: **99.23%**
208. **`rake_tasks/common.rb`** -> AI Confidence: **99.2%**
209. **`py/selenium/webdriver/remote/errorhandler.py`** -> AI Confidence: **99.2%**
210. **`cpp/iedriver/RegistryUtilities.cpp`** -> AI Confidence: **99.2%**
211. **`cpp/webdriver-server/command.cc`** -> AI Confidence: **99.2%**
212. **`dotnet/src/webdriver/Cookie.cs`** -> AI Confidence: **99.2%**
213. **`dotnet/src/webdriver/IE/InternetExplorerDriverService.cs`** -> AI Confidence: **99.2%**
214. **`py/selenium/webdriver/common/action_chains.py`** -> AI Confidence: **99.18%**
215. **`javascript/selenium-webdriver/remote/index.js`** -> AI Confidence: **99.18%**
216. **`java/src/org/openqa/selenium/By.java`** -> AI Confidence: **99.18%**
217. **`java/src/org/openqa/selenium/bidi/module/BrowsingContextInspector.java`** -> AI Confidence: **99.18%**
218. **`java/src/org/openqa/selenium/bidi/module/Network.java`** -> AI Confidence: **99.18%**
219. **`java/src/org/openqa/selenium/chrome/AddHasCasting.java`** -> AI Confidence: **99.18%**
220. **`java/src/org/openqa/selenium/chromium/ChromiumDriver.java`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `java/src/org/openqa/selenium/Platform.java` -> **0.0001%** Exposure
### Exploit Generation Surface
- `rake_tasks/bazel.rake` -> **100.0%** Exposure
- `rake_tasks/common.rb` -> **100.0%** Exposure
- `rake_tasks/dotnet.rake` -> **100.0%** Exposure
- `rake_tasks/java.rake` -> **100.0%** Exposure
- `rake_tasks/node.rake` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `rake_tasks/dotnet.rake` -> **100.0%** Exposure
- `rake_tasks/java.rake` -> **100.0%** Exposure
- `rake_tasks/node.rake` -> **100.0%** Exposure
- `rake_tasks/python.rake` -> **100.0%** Exposure
- `rake_tasks/ruby.rake` -> **100.0%** Exposure
### Raw Memory Manipulation
- `cpp/iedriver/ProxyManager.cpp` -> **9.9998%** Exposure
- `cpp/iedriver/CommandHandlers/SendKeysCommandHandler.cpp` -> **9.9991%** Exposure
- `cpp/iedriver/InputManager.cpp` -> **9.9972%** Exposure
- `cpp/iedriver/Alert.cpp` -> **9.9657%** Exposure
- `cpp/iedriver/BrowserFactory.cpp` -> **9.6522%** Exposure
### Algorithmic DoS Exposure
- `rake_tasks/bazel.rake` -> **100.0%** Exposure
- `rake_tasks/common.rb` -> **100.0%** Exposure
- `rake_tasks/dotnet.rake` -> **100.0%** Exposure
- `rake_tasks/java.rake` -> **100.0%** Exposure
- `rake_tasks/node.rake` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `25` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `11427` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `java/src/org/openqa/selenium/devtools/idealized/Network.java` (JAVA) -> Cumulative Risk: **1046.46**
- **Archetype:** `file_cluster_13` (Distance: 12.711 IQR)
- **Magnitude:** 421.76 | **LOC:** 382 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `prepareToInterceptTraffic` (Impact: 219.7), `disable` (Impact: 6.8), `acceptLanguage` (Impact: 4.6)

### 2. `java/src/org/openqa/selenium/bidi/Connection.java` (JAVA) -> Cumulative Risk: **1032.99**
- **Archetype:** `file_cluster_13` (Distance: 12.081 IQR)
- **Magnitude:** 416.22 | **LOC:** 390 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Logic Bomb (100.0%), Concurrency (99.9963%)
- **Heaviest Functions:** `handleEventResponse` (Impact: 54.6), `handleResponse` (Impact: 53.4), `removeListener` (Impact: 32.2)

### 3. `java/src/org/openqa/selenium/devtools/Connection.java` (JAVA) -> Cumulative Risk: **1012.38**
- **Archetype:** `file_cluster_13` (Distance: 11.951 IQR)
- **Magnitude:** 288.86 | **LOC:** 374 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `send` (Impact: 63.2), `sendAndWait` (Impact: 18.9), `onText` (Impact: 18.5)

### 4. `dotnet/src/webdriver/BiDi/EventDispatcher.cs` (CSHARP) -> Cumulative Risk: **955.28**
- **Archetype:** `file_cluster_4` (Distance: 11.984 IQR)
- **Magnitude:** 242.6 | **LOC:** 163 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `ProcessEventsAwaiterAsync` (Impact: 48.1), `SubscribeAsync` (Impact: 21.3), `InvokeHandlerAsync` (Impact: 18.0)

### 5. `dotnet/src/webdriver/BiDi/BrowsingContext/BrowsingContext.cs` (CSHARP) -> Cumulative Risk: **954.45**
- **Archetype:** `file_cluster_4` (Distance: 13.918 IQR)
- **Magnitude:** 1090.72 | **LOC:** 482 | **CtrlFlow:** 58.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `OnNavigationStartedAsync` (Impact: 24.4), `OnFragmentNavigatedAsync` (Impact: 24.4), `OnHistoryUpdatedAsync` (Impact: 24.4)

### 6. `java/src/org/openqa/selenium/grid/router/GridStatusHandler.java` (JAVA) -> Cumulative Risk: **951.97**
- **Archetype:** `file_cluster_13` (Distance: 11.17 IQR)
- **Magnitude:** 161.6 | **LOC:** 168 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `execute` (Impact: 106.0), `nodeAsMap` (Impact: 2.1), `GridStatusHandler` (Impact: 1.9)

### 7. `java/src/org/openqa/selenium/grid/sessionmap/local/LocalSessionMap.java` (JAVA) -> Cumulative Risk: **948.19**
- **Archetype:** `file_cluster_13` (Distance: 11.327 IQR)
- **Magnitude:** 365.62 | **LOC:** 317 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `get` (Impact: 45.5), `add` (Impact: 36.8), `removeWithReason` (Impact: 36.0)

### 8. `py/selenium/webdriver/common/bidi/cdp.py` (PYTHON) -> Cumulative Risk: **939.56**
- **Archetype:** `file_cluster_4` (Distance: 13.243 IQR)
- **Magnitude:** 667.06 | **LOC:** 516 | **CtrlFlow:** 35.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `import_devtools` (Impact: 280.1), `_reader_task` (Impact: 86.0), `dom_enable` (Impact: 25.8)

### 9. `java/src/org/openqa/selenium/remote/RemoteWebDriver.java` (JAVA) -> Cumulative Risk: **938.55**
- **Archetype:** `file_cluster_13` (Distance: 11.507 IQR)
- **Magnitude:** 1021.18 | **LOC:** 1430 | **CtrlFlow:** 33.6% | **Authorship Centralization:** 63.6%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `quit` (Impact: 624.0), `close` (Impact: 73.5), `getScreenshotAs` (Impact: 44.9)

### 10. `dotnet/src/webdriver/Remote/HttpCommandExecutor.cs` (CSHARP) -> Cumulative Risk: **932.69**
- **Archetype:** `file_cluster_13` (Distance: 13.852 IQR)
- **Magnitude:** 644.16 | **LOC:** 498 | **CtrlFlow:** 57.7% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `SendAsync` (Impact: 180.0), `ExecuteAsync` (Impact: 65.7), `CreateResponse` (Impact: 46.3)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `rust/src/lib.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.854 IQR)
- **Top Global Matches:** file_cluster_8: 12.854, file_cluster_13: 13.097, file_cluster_16: 13.24
- **Magnitude:** 43532.9 | **LOC:** 1758 | **CtrlFlow:** 55.9% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (20.5015%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 327`, `structural_boundaries: 258`, `args: 167`, `func_start: 147`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 151`
* *Architecture:* `io: 1`, `api: 68`, `concurrency: 1`, `import: 32`
* *Defense:* `safety: 196`, `sync_locks: 12`, `immutability_locks: 45`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::firefox::FIREFOX_NAME, find_latest_from_cache, ChromeManager, std::sync::mpsc::Receiver, uncompress, EDGEDRIVER_NAME, send_stats_to_plausible, anyhow::anyhow...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dotnet/src/webdriver/BiDi/BrowsingContext/IBrowsingContextModule.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.579 IQR)
- **Top Global Matches:** file_cluster_16: 10.579, file_cluster_8: 11.107, file_cluster_4: 11.227
- **Magnitude:** 5264.41 | **LOC:** 65 | **CtrlFlow:** 97.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 2`, `args: 40`, `func_start: 40`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `concurrency: 54`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `common/extensions/webextensions-selenium-example-signed/META-INF/cose.sig` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `javascript/grid-ui/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cpp/iedriver/IECommandExecutor.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.945 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.11 IQR)
- **Top Global Matches:** file_cluster_8: 13.945, file_cluster_13: 14.061, file_cluster_11: 14.357
- **Magnitude:** 3420.84 | **LOC:** 1720 | **CtrlFlow:** 66.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 72
- **Risk Profile:** Cognitive Load (90.3331%), Tech Debt (79.4033%)
**Top Internal Functions/Classes:**
  * `IECommandExecutor::OpenNewBrowserWindow` (Impact: 376.6 | O(2^N) | DB: 72)
  * `IECommandExecutor::OnAfterNewWindow` (Impact: 365.6 | O(2^N) | DB: 43)
  * `IECommandExecutor::DispatchCommand` (Impact: 313.1 | O(2^N) | DB: 27)
  * `IECommandExecutor::HandleUnexpectedAlert` (Impact: 284.1 | O(2^N) | DB: 10)
  * `IECommandExecutor::OnNewHtmlDialog` (Impact: 191.0 | O(2^N) | DB: 20)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 178`, `structural_boundaries: 88`, `args: 186`, `func_start: 48`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 722`, `dead_code: 3`, `duplicate_logic: 4`, `orphaned_logic: 35`
* *Architecture:* `concurrency: 12`, `import: 28`
* *Defense:* `safety: 1`, `sync_locks: 6`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 21):` errorcodes.h, command_types.h, mutex, Alert.h, InputManager.h, ProxyManager.h, WebDriverConstants.h, WindowUtilities.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cpp/iedriver/CommandHandlers/NewSessionCommandHandler.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.537 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.553 IQR)
- **Top Global Matches:** file_cluster_8: 13.537, file_cluster_13: 13.829, file_cluster_7: 13.986
- **Magnitude:** 3035.12 | **LOC:** 1046 | **CtrlFlow:** 71.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 91
- **Risk Profile:** Cognitive Load (70.2996%), Tech Debt (78.0184%)
**Top Internal Functions/Classes:**
  * `NewSessionCommandHandler::ValidateCapabi` (Impact: 1221.4 | O(2^N) | DB: 91)
  * `NewSessionCommandHandler::MatchCapabilit` (Impact: 198.8 | O(2^N) | DB: 24)
  * `NewSessionCommandHandler::ValidateArgume` (Impact: 185.4 | O(2^N) | DB: 13)
  * `NewSessionCommandHandler::ProcessCapabil` (Impact: 115.5 | O(2^N) | DB: 17)
  * `NewSessionCommandHandler::SetProxySettin` (Impact: 100.3 | O(2^N) | DB: 30)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 181`, `structural_boundaries: 71`, `args: 81`, `func_start: 19`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 673`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 2`, `orphaned_logic: 16`
* *Architecture:* `import: 10`
* *Defense:* `immutability_locks: 33`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` errorcodes.h, ProxyManager.h, IECommandExecutor.h, BrowserFactory.h, WebDriverConstants.h, InputManager.h, logging.h, Browser.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cpp/iedriver/Element.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.585 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.069 IQR)
- **Top Global Matches:** file_cluster_8: 14.585, file_cluster_13: 14.81, file_cluster_7: 14.994
- **Magnitude:** 2686.28 | **LOC:** 1880 | **CtrlFlow:** 71.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 331
- **Risk Profile:** Cognitive Load (92.0438%), Tech Debt (66.9324%)
**Top Internal Functions/Classes:**
  * `Element::IsFocusable` (Impact: 1495.6 | O(2^N) | DB: 331)
  * `Element::IsXmlDocument` (Impact: 70.7 | O(2^N) | DB: 17)
  * `Element::CalculateClickPoint` (Impact: 25.6 | O(2^N) | DB: 11)
  * `Element::IsEnabled` (Impact: 12.9 | O(2^N) | DB: 6)
  * `Element::Element` (Impact: 11.8 | O(2^N) | DB: 11)
    * *Intent:* #include "Element.h" #include <algorithm> #include "errorcodes.h" #include "logging.h" #include "jso...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 166`, `structural_boundaries: 66`, `args: 109`, `func_start: 25`
* *Risk/State:* `state_mutation: 1017`, `planned_debt: 2`, `fragile_debt: 2`, `duplicate_logic: 2`, `orphaned_logic: 8`
* *Architecture:* `import: 11`
* *Defense:* `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` errorcodes.h, Script.h, VariantUtilities.h, WebDriverConstants.h, algorithm, Browser.h, atoms.h, json.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dotnet/src/webdriver/BiDi/Network/INetworkModule.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.402 IQR)
- **Top Global Matches:** file_cluster_16: 10.402, file_cluster_8: 10.904, file_cluster_4: 11.03
- **Magnitude:** 2494.56 | **LOC:** 49 | **CtrlFlow:** 96.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 2`, `args: 24`, `func_start: 24`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `concurrency: 29`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cpp/iedriver/Browser.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.649 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.914 IQR)
- **Top Global Matches:** file_cluster_8: 13.649, file_cluster_13: 13.823, file_cluster_7: 14.087
- **Magnitude:** 2361.06 | **LOC:** 913 | **CtrlFlow:** 63.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 147
- **Risk Profile:** Cognitive Load (91.0597%), Tech Debt (42.6996%)
**Top Internal Functions/Classes:**
  * `Browser::NewWindow3` (Impact: 1866.0 | O(2^N) | DB: 147)
  * `Browser::OnQuit` (Impact: 35.9 | O(2^N) | DB: 7)
  * `Browser::BeforeNavigate2` (Impact: 20.4 | O(2^N))
  * `Browser::NewProcess` (Impact: 14.3 | O(2^N))
  * `Browser::Browser` (Impact: 4.9 | O(2^N) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 109`, `structural_boundaries: 62`, `args: 123`, `func_start: 30`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 405`, `fragile_debt: 2`, `orphaned_logic: 5`
* *Architecture:* `import: 14`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` errorcodes.h, Script.h, ShlGuid.h, BrowserFactory.h, WindowUtilities.h, comutil.h, CustomTypes.h, WebDriverConstants.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `java/src/org/openqa/selenium/grid/node/kubernetes/KubernetesSessionFactory.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.028 IQR)
- **Top Global Matches:** file_cluster_13: 12.028, file_cluster_8: 12.229, file_cluster_0: 12.39
- **Magnitude:** 1860.52 | **LOC:** 1438 | **CtrlFlow:** 43.9% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (28.1395%), Tech Debt (19.7288%)
**Top Internal Functions/Classes:**
  * `apply` (Impact: 555.5 | O(2^N) | DB: 25)
  * `doWaitForPodRunning` (Impact: 175.4 | O(N^6))
  * `evaluatePodStatus` (Impact: 156.8 | O(N^6))
  * `buildJobSpec` (Impact: 121.5 | O(N^6) | DB: 8)
  * `buildJobSpecFromTemplate` (Impact: 42.4 | O(N^3) | DB: 12)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 214`, `structural_boundaries: 274`, `args: 108`, `func_start: 91`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 90`, `state_mutation: 183`, `duplicate_logic: 5`, `orphaned_logic: 1`
* *Architecture:* `io: 12`, `api: 9`, `concurrency: 6`, `import: 95`
* *Defense:* `safety: 44`, `doc: 1`, `sync_locks: 1`, `immutability_locks: 29`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 35):` io.fabric8.kubernetes.api.model.ObjectMetaBuilder, io.fabric8.kubernetes.client.WatcherException, java.net.URL, java.util.Optional.ofNullable, io.fabric8.kubernetes.api.model.ResourceRequirementsBuilder, java.io.UncheckedIOException, org.openqa.selenium.remote.http.HttpMethod.GET, io.fabric8.kubernetes.client.LocalPortForward...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `java/src/org/openqa/selenium/devtools/CdpClientGenerator.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.084 IQR)
- **Top Global Matches:** file_cluster_0: 12.084, file_cluster_13: 12.124, file_cluster_17: 12.181
- **Magnitude:** 1829.62 | **LOC:** 1438 | **CtrlFlow:** 35.4% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 44
- **Risk Profile:** Cognitive Load (42.7023%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `toTypeDeclaration` (Impact: 327.6 | O(2^N) | DB: 20)
  * `parse` (Impact: 122.3 | O(2^N) | DB: 1)
  * `toMethodDeclaration` (Impact: 101.7 | O(N^6) | DB: 7)
  * `toTypeDeclaration` (Impact: 94.0 | O(N^4) | DB: 35)
  * `toTypeDeclaration` (Impact: 64.9 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 192`, `structural_boundaries: 350`, `args: 175`, `func_start: 125`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 60`, `state_mutation: 180`, `planned_debt: 2`, `duplicate_logic: 53`, `orphaned_logic: 1`
* *Architecture:* `io: 37`, `api: 95`, `import: 38`
* *Defense:* `safety: 35`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` java.io.InputStream, java.util.List, java.nio.file.Path, com.github.javaparser.ast.body.TypeDeclaration, java.util.Objects, java.util.jar.JarEntry, java.util.jar.JarOutputStream, com.github.javaparser.ast.body.BodyDeclaration...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cpp/iedriver/BrowserFactory.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.896 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.326 IQR)
- **Top Global Matches:** file_cluster_8: 13.896, file_cluster_13: 14.018, file_cluster_11: 14.16
- **Magnitude:** 1798.34 | **LOC:** 1594 | **CtrlFlow:** 66.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 41
- **Risk Profile:** Cognitive Load (86.7423%), Tech Debt (95.3304%)
**Top Internal Functions/Classes:**
  * `BrowserFactory::AttachToBrowserUsingShel` (Impact: 271.0 | O(2^N) | DB: 18)
  * `BrowserFactory::AttachToBrowserUsingActi` (Impact: 233.1 | O(2^N) | DB: 14)
  * `BrowserFactory::InvokeClearCacheUtility` (Impact: 211.2 | O(2^N) | DB: 41)
  * `BrowserFactory::CreateLowIntegrityLevelT` (Impact: 114.7 | O(2^N) | DB: 10)
  * `BrowserFactory::LaunchEdgeInIEMode` (Impact: 87.0 | O(2^N) | DB: 11)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 76`, `args: 113`, `func_start: 27`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 2`, `state_mutation: 485`, `dead_code: 3`, `fragile_debt: 1`, `orphaned_logic: 24`
* *Architecture:* `import: 14`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` FileUtilities.h, BrowserFactory.h, vector, psapi.h, shlobj.h, RegistryUtilities.h, WebDriverConstants.h, exdispid.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cpp/webdriver-server/server.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.981 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.857 IQR)
- **Top Global Matches:** file_cluster_8: 12.981, file_cluster_13: 13.304, file_cluster_7: 13.491
- **Magnitude:** 1520.94 | **LOC:** 812 | **CtrlFlow:** 61.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 28
- **Risk Profile:** Cognitive Load (67.9535%), Tech Debt (95.1379%)
**Top Internal Functions/Classes:**
  * `Server::DispatchCommand` (Impact: 298.9 | O(2^N) | DB: 28)
  * `Server::SendResponseToClient` (Impact: 254.8 | O(2^N) | DB: 16)
  * `Server::ReadRequestBody` (Impact: 98.7 | O(2^N) | DB: 10)
  * `Server::LookupCommand` (Impact: 95.3 | O(2^N) | DB: 10)
  * `Server::ProcessRequest` (Impact: 74.7 | O(2^N) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 51`, `args: 59`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `state_mutation: 340`, `duplicate_logic: 4`, `orphaned_logic: 23`
* *Architecture:* `import: 10`
* *Defense:* `safety: 1`, `immutability_locks: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` cstdio, errorcodes.h, cstring, algorithm, server.h, sstream, uri_info.h, logging.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dotnet/src/webdriver/BiDi/Emulation/IEmulationModule.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.093 IQR)
- **Top Global Matches:** file_cluster_16: 10.093, file_cluster_8: 10.418, file_cluster_4: 10.583
- **Magnitude:** 1407.25 | **LOC:** 38 | **CtrlFlow:** 94.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 2`, `args: 13`, `func_start: 13`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `concurrency: 13`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `java/src/org/openqa/selenium/grid/node/local/LocalNode.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.034 IQR)
- **Top Global Matches:** file_cluster_13: 12.034, file_cluster_4: 12.226, file_cluster_8: 12.395
- **Magnitude:** 1384.34 | **LOC:** 1555 | **CtrlFlow:** 33.8% | **Authorship Centralization:** 57.1%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (72.9272%), Tech Debt (65.528%)
**Top Internal Functions/Classes:**
  * `LocalNode` (Impact: 253.0 | O(N^6) | DB: 8)
  * `createExternalSession` (Impact: 113.9 | O(N^4) | DB: 8)
  * `stopTimedOutSession` (Impact: 67.9 | O(N^4) | DB: 11)
  * `getStatus` (Impact: 65.8 | O(N^6))
  * `getDownloadedFile` (Impact: 44.1 | O(N^6) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 294`, `args: 119`, `func_start: 82`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 118`, `dead_code: 1`, `duplicate_logic: 6`, `orphaned_logic: 19`
* *Architecture:* `io: 30`, `api: 38`, `concurrency: 128`, `import: 114`
* *Defense:* `safety: 36`, `doc: 6`, `sync_locks: 8`, `immutability_locks: 36`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 56):` org.openqa.selenium.grid.data.SessionCreatedEvent, java.io.UncheckedIOException, org.openqa.selenium.grid.data.SessionEventData, org.openqa.selenium.grid.data.Availability, org.openqa.selenium.HasDownloads.DownloadedFile, org.openqa.selenium.json.Json, org.openqa.selenium.remote.http.Contents.asJson, org.openqa.selenium.remote.tracing.Tracer...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dotnet/src/webdriver/WebDriver.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.364 IQR)
- **Top Global Matches:** file_cluster_13: 14.364, file_cluster_8: 14.44, file_cluster_7: 14.515
- **Magnitude:** 1380.96 | **LOC:** 1186 | **CtrlFlow:** 85.0% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N^6) | **DB Complexity:** 50
- **Risk Profile:** Cognitive Load (35.845%), Tech Debt (9.0862%)
**Top Internal Functions/Classes:**
  * `WebDriver` (Impact: 1201.8 | O(N^6) | DB: 50)
    * *Intent:* /// <summary> /// Initializes a new instance of the <see cref="WebDriver"/> class. /// </summary> //...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 192`, `structural_boundaries: 34`, `args: 34`, `func_start: 79`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 143`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `api: 19`, `concurrency: 7`, `import: 7`
* *Defense:* `safety: 71`, `doc: 142`, `immutability_locks: 2`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Diagnostics.CodeAnalysis, System.Globalization, System.Collections, OpenQA.Selenium.Interactions, System.Collections.ObjectModel, OpenQA.Selenium.Internal, OpenQA.Selenium.VirtualAuth
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/selenium/webdriver/remote/webdriver.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.266 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.283 IQR)
- **Top Global Matches:** file_cluster_13: 13.266, file_cluster_16: 13.409, file_cluster_0: 13.499
- **Magnitude:** 1358.82 | **LOC:** 1571 | **CtrlFlow:** 34.1% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 33
- **Risk Profile:** Cognitive Load (39.2574%), Tech Debt (15.0352%)
**Top Internal Functions/Classes:**
  * `find_elements` (Impact: 558.0 | O(N^5) | DB: 33)
  * `create_matches` (Impact: 71.6 | O(N^6) | DB: 2)
  * `_wrap_value` (Impact: 61.3 | O(2^N))
  * `_unwrap_value` (Impact: 61.2 | O(2^N))
  * `execute` (Impact: 56.9 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 162`, `structural_boundaries: 313`, `args: 101`, `func_start: 100`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 106`, `duplicate_logic: 2`
* *Architecture:* `io: 5`, `api: 120`, `concurrency: 9`, `import: 56`
* *Defense:* `safety: 44`, `doc: 172`, `test: 5`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.957
  * `Choke Point (Betweenness):` 0.000171 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 38):` selenium.webdriver.remote.errorhandler, warnings, selenium.webdriver.common.bidi.script, selenium.webdriver.common.bidi.storage, selenium.webdriver.safari.remote_connection, urllib3, selenium.webdriver.common.by, selenium.webdriver.remote.client_config...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `rust/src/files.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.73 IQR)
- **Top Global Matches:** file_cluster_13: 12.73, file_cluster_0: 12.857, file_cluster_8: 12.883
- **Magnitude:** 1344.34 | **LOC:** 686 | **CtrlFlow:** 48.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (37.8919%), Tech Debt (30.4712%)
**Top Internal Functions/Classes:**
  * `uncompress` (Impact: 377.3 | O(N^5) | DB: 9)
  * `copy_folder_content` (Impact: 272.1 | O(2^N))
  * `unzip` (Impact: 188.1 | O(N^5) | DB: 12)
  * `uncompress_pkg` (Impact: 85.5 | O(N^5) | DB: 7)
  * `parse_version` (Impact: 46.0 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 165`, `args: 32`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 110`, `duplicate_logic: 2`, `orphaned_logic: 5`
* *Architecture:* `io: 12`, `api: 29`, `import: 27`
* *Defense:* `safety: 79`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` std::io, crate::
    CP_VOLUME_COMMAND, std::os::windows::ffi::OsStrExt, anyhow::anyhow, directories::BaseDirs, format_three_args, Command, walkdir::DirEntry...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cpp/iedriver/CommandHandlers/SendKeysCommandHandler.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.863 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.048 IQR)
- **Top Global Matches:** file_cluster_8: 13.863, file_cluster_13: 14.017, file_cluster_7: 14.308
- **Magnitude:** 1222.0 | **LOC:** 1145 | **CtrlFlow:** 63.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 125
- **Risk Profile:** Cognitive Load (90.3899%), Tech Debt (23.8538%)
**Top Internal Functions/Classes:**
  * `SendKeysCommandHandler::CreateActionSequ` (Impact: 558.2 | O(N^6) | DB: 125)
  * `SendKeysCommandHandler::ExecuteInternal` (Impact: 159.2 | O(N^6) | DB: 43)
  * `SendKeysCommandHandler::IsElementInterac` (Impact: 25.0 | O(N^6) | DB: 4)
  * `SendKeysCommandHandler` (Impact: 2.9 | O(2^N))
  * `SendKeysCommandHandler::SendKeysCommandH` (Impact: 1.5 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 64`, `args: 125`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `state_mutation: 464`, `planned_debt: 1`, `orphaned_logic: 4`
* *Architecture:* `import: 15`
* *Defense:* `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` SendKeysCommandHandler.h, errorcodes.h, WindowUtilities.h, VariantUtilities.h, IECommandExecutor.h, Element.h, BrowserFactory.h, InputManager.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cpp/iedriver/Alert.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.005 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.999 IQR)
- **Top Global Matches:** file_cluster_8: 14.005, file_cluster_13: 14.18, file_cluster_11: 14.404
- **Magnitude:** 1200.12 | **LOC:** 666 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 133
- **Risk Profile:** Cognitive Load (70.5232%), Tech Debt (42.4128%)
**Top Internal Functions/Classes:**
  * `Alert::Dismiss` (Impact: 662.6 | O(2^N) | DB: 133)
  * `Alert::Alert` (Impact: 85.0 | O(2^N) | DB: 19)
  * `Alert::Accept` (Impact: 15.1 | O(2^N) | DB: 3)
  * `Alert` (Impact: 2.9 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 47`, `args: 54`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 427`, `planned_debt: 1`, `fragile_debt: 1`, `orphaned_logic: 3`
* *Architecture:* `import: 7`
* *Defense:* `safety: 1`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` errorcodes.h, WebDriverConstants.h, DocumentHost.h, UIAutomation.h, Alert.h, logging.h, StringUtilities.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `common/devtools/pdl.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.125 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.802 IQR)
- **Top Global Matches:** file_cluster_8: 10.125, file_cluster_13: 10.324, file_cluster_16: 10.723
- **Magnitude:** 1166.38 | **LOC:** 188 | **CtrlFlow:** 69.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (60.2831%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 1086.5 | O(2^N) | DB: 10)
  * `assignType` (Impact: 47.7 | O(2^N))
  * `createItem` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 44`, `args: 4`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 24`
* *Architecture:* `io: 1`, `api: 4`, `import: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.357
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` typing, collections, re, sys, json
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `dotnet/src/webdriver/BiDi/Script/IScriptModule.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.215 IQR)
- **Top Global Matches:** file_cluster_16: 10.215, file_cluster_4: 10.762, file_cluster_8: 10.774
- **Magnitude:** 1145.6 | **LOC:** 41 | **CtrlFlow:** 90.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 3`, `args: 12`, `func_start: 14`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `concurrency: 17`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Diagnostics.CodeAnalysis
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dotnet/src/webdriver/BiDi/BrowsingContext/BrowsingContext.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.918 IQR)
- **Top Global Matches:** file_cluster_4: 13.918, file_cluster_16: 14.162, file_cluster_0: 14.236
- **Magnitude:** 1090.72 | **LOC:** 482 | **CtrlFlow:** 58.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (99.9996%)
**Top Internal Functions/Classes:**
  * `OnNavigationStartedAsync` (Impact: 24.4 | O(2^N) | DB: 1)
  * `OnFragmentNavigatedAsync` (Impact: 24.4 | O(2^N) | DB: 1)
  * `OnHistoryUpdatedAsync` (Impact: 24.4 | O(2^N) | DB: 1)
  * `OnDomContentLoadedAsync` (Impact: 24.4 | O(2^N) | DB: 1)
  * `OnLoadAsync` (Impact: 24.4 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 75`, `args: 93`, `func_start: 129`, `class_start: 1`
* *Risk/State:* `state_mutation: 82`, `duplicate_logic: 22`, `orphaned_logic: 1`
* *Architecture:* `api: 44`, `concurrency: 111`, `import: 2`
* *Defense:* `safety: 77`, `sync_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Text.Json.Serialization, System.Text
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/selenium/webdriver/common/bidi/browsing_context.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.083 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.582 IQR)
- **Top Global Matches:** file_cluster_16: 12.083, file_cluster_0: 12.089, file_cluster_8: 12.219
- **Magnitude:** 1082.7 | **LOC:** 1061 | **CtrlFlow:** 46.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (33.3292%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `from_json` (Impact: 251.8 | O(2^N) | DB: 1)
  * `from_json` (Impact: 56.9 | O(N^3))
  * `from_json` (Impact: 49.4 | O(2^N))
  * `from_json` (Impact: 46.3 | O(N^3))
  * `from_json` (Impact: 46.0 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 142`, `structural_boundaries: 163`, `args: 58`, `func_start: 58`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 55`, `duplicate_logic: 40`
* *Architecture:* `api: 81`, `concurrency: 7`, `import: 7`
* *Defense:* `safety: 37`, `doc: 98`, `sync_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.272
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` typing, dataclasses, threading, selenium.webdriver.common.bidi.common, collections.abc, typing_extensions, selenium.webdriver.common.bidi.session
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### 🚨 Severe Anti-Patterns (Language Convention Violations)
- `common/defs.bzl` (PYTHON) | **Drift Ratio: 1.6x**
  * **Global Archetype:** `file_cluster_8` (Drift: 3.628 IQR)
  * **Local Reality:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.821 IQR)
- `javascript/defs.bzl` (PYTHON) | **Drift Ratio: 1.6x**
  * **Global Archetype:** `file_cluster_8` (Drift: 3.634 IQR)
  * **Local Reality:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.821 IQR)
- `py/selenium/__init__.py` (PYTHON) | **Drift Ratio: 1.55x**
  * **Global Archetype:** `file_cluster_8` (Drift: 3.753 IQR)
  * **Local Reality:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.821 IQR)
- `rust/defs.bzl` (PYTHON) | **Drift Ratio: 1.55x**
  * **Global Archetype:** `file_cluster_8` (Drift: 3.635 IQR)
  * **Local Reality:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.619 IQR)

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `java/src/org/openqa/selenium/firefox/GeckoDriverInfo.java` (JAVA) | Magnitude: 45.1 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 32, import: 11, args: 10
- `common/src/web/downloads/download.html` (HTML) | Magnitude: 19.78 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 13, decorators: 13, io: 7
- `dotnet/src/webdriver/BiDi/BrowsingContext/PrintCommand.cs` (CSHARP) | Magnitude: 122.3 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 48, branch: 35, structural_boundaries: 28, api: 24
- `dotnet/src/webdriver/BiDi/Session/ProxyConfiguration.cs` (CSHARP) | Magnitude: 140.66 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 16, api: 14, branch: 7, class_start: 7
- `java/src/org/openqa/selenium/remote/tracing/opentelemetry/OpenTelemetrySpan.java` (JAVA) | Magnitude: 131.28 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 110, structural_boundaries: 29, state_mutation: 20, func_start: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `dotnet/src/webdriver/DevTools/JavaScript.cs` (CSHARP) | Magnitude: 43.02 | Delta: **0.175 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 63, indent_spaces: 23, args: 12, func_start: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `dotnet/src/webdriver/ErrorResponse.cs` (CSHARP) | Magnitude: 182.5 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 46, state_mutation: 31, branch: 25, doc: 23
- `dotnet/src/support/Extensions/WebDriverExtensions.cs` (CSHARP) | Magnitude: 206.52 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 70, branch: 35, doc: 30, safety: 14
- `scripts/github-actions/rerun-failures.sh` (SHELL) | Magnitude: 4.13 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 18, branch: 14, safety_bypasses: 13, io: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `scripts/gitpod/start-xvfb.sh` (SHELL) | Magnitude: 0.28 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: reflection_metaprogramming: 7, sec_dead_code: 4, safety: 3, indent_spaces: 3
- `scripts/github-actions/ci-build.sh` (SHELL) | Magnitude: 1.44 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 9, indent_spaces: 4, reflection_metaprogramming: 3, branch: 2
- `java/src/org/openqa/selenium/support/pagefactory/FieldDecorator.java` (JAVA) | Magnitude: 17.74 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 5, structural_boundaries: 3, reflection_metaprogramming: 2, args: 1
- `common/src/web/iframeWithAlert.html` (HTML) | Magnitude: 11.52 | Delta: **0.15 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: io: 2, api: 1, reflection_metaprogramming: 1, debug_prints: 1
- `common/src/web/click_tests/issue5237_frame.html` (HTML) | Magnitude: 11.52 | Delta: **0.174 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: io: 2, api: 1, reflection_metaprogramming: 1, listeners: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `java/src/org/openqa/selenium/devtools/v144/v144Javascript.java` (JAVA) | Magnitude: 3.52 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 23, ui_framework: 10, decorators: 10
- `dotnet/src/webdriver/Remote/LocalFileDetector.cs` (CSHARP) | Magnitude: 8.38 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 10, structural_boundaries: 4, indent_spaces: 4, func_start: 2
- `java/src/org/openqa/selenium/devtools/v145/v145Javascript.java` (JAVA) | Magnitude: 3.52 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 23, ui_framework: 10, decorators: 10
- `javascript/atoms/html5/html5_browser.js` (JAVASCRIPT) | Magnitude: 56.58 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 54, branch: 24, structural_boundaries: 13, doc: 10
- `py/selenium/webdriver/common/actions/key_input.py` (PYTHON) | Magnitude: 48.06 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 23, indent_spaces: 18, api: 10, args: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `scripts/build-info.ps1` (POWERSHELL) | Magnitude: 27.16 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 12, branch: 2, closures: 2, indent_spaces: 2
- `dotnet/src/webdriver/PrintOptions.cs` (CSHARP) | Magnitude: 251.24 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 229, doc: 111, state_mutation: 96, branch: 46
- `dotnet/src/webdriver/NetworkResponseReceivedEventArgs.cs` (CSHARP) | Magnitude: 27.08 | Delta: **0.071 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 31, indent_spaces: 20, api: 9, state_mutation: 9
- `dotnet/src/webdriver/Timeouts.cs` (CSHARP) | Magnitude: 105.68 | Delta: **0.074 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 59, doc: 48, state_mutation: 30, branch: 13
- `dotnet/src/webdriver/Platform.cs` (CSHARP) | Magnitude: 222.36 | Delta: **0.107 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 73, indent_spaces: 71, state_mutation: 29, branch: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `java/src/org/openqa/selenium/grid/server/Server.java` (JAVA) | Magnitude: 21.96 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, args: 2, func_start: 2, generics: 2
- `dotnet/src/webdriver/DevTools/Target.cs` (CSHARP) | Magnitude: 28.42 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_1`
  * Top Architectural Signatures: doc: 45, indent_spaces: 16, api: 9, args: 8
- `py/selenium/webdriver/common/bidi/browsing_context.py` (PYTHON) | Magnitude: 1082.7 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 588, structural_boundaries: 163, branch: 142, doc: 98
- `java/src/org/openqa/selenium/events/EventListener.java` (JAVA) | Magnitude: 14.32 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 8, api: 5, generics: 4
- `java/src/org/openqa/selenium/remote/tracing/empty/NullPropagator.java` (JAVA) | Magnitude: 7.86 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 7, generics: 4, api: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `java/src/org/openqa/selenium/grid/config/EnvConfig.java` (JAVA) | Magnitude: 42.9 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 13, comprehensions: 11, args: 10
- `common/src/web/sessionCookieDest.html` (HTML) | Magnitude: 31.84 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 6, state_mutation: 6, globals: 6
- `javascript/grid-ui/src/screens/Overview/Overview.tsx` (TYPESCRIPT) | Magnitude: 27.59 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 184, structural_boundaries: 55, branch: 36, args: 33
- `javascript/selenium-webdriver/bidi/addInterceptParameters.js` (JAVASCRIPT) | Magnitude: 44.96 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 49, doc: 15, state_mutation: 12, encapsulation: 11
- `java/src/org/openqa/selenium/grid/config/MapConfig.java` (JAVA) | Magnitude: 100.92 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 63, structural_boundaries: 21, args: 18, comprehensions: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `javascript/grid-ui/src/components/LiveView/LiveView.tsx` (TYPESCRIPT) | Magnitude: 7.56 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 138, structural_boundaries: 33, args: 33, func_start: 32
- `common/src/web/key_tests/remove_on_keypress.html` (HTML) | Magnitude: 28.94 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 26, func_start: 10, args: 7, globals: 6
- `javascript/grid-ui/src/components/RunningSessions/RunningSessions.tsx` (TYPESCRIPT) | Magnitude: 47.22 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 625, structural_boundaries: 109, ui_framework: 99, args: 96
- `common/src/web/html5/geolocation.js` (JAVASCRIPT) | Magnitude: 11.72 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 9, high_risk_execution: 5, branch: 4, state_mutation: 4
- `common/src/web/mouse_interaction.html` (HTML) | Magnitude: 36.86 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 83, structural_boundaries: 20, args: 18, ui_framework: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `dotnet/src/webdriver/DriverService.cs` (CSHARP) | Magnitude: 587.38 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 311, doc: 126, branch: 70, structural_boundaries: 51
- `dotnet/src/webdriver/BiDi/Script/MessageEventArgs.cs` (CSHARP) | Magnitude: 18.18 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, concurrency: 2, args: 1, func_start: 1
- `dotnet/src/webdriver/BiDi/Browser/BrowserModule.cs` (CSHARP) | Magnitude: 123.06 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 43, structural_boundaries: 27, concurrency: 24, branch: 22
- `dotnet/src/webdriver/BiDi/WebExtension/WebExtensionModule.cs` (CSHARP) | Magnitude: 34.06 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 12, func_start: 6, concurrency: 6
- `dotnet/src/webdriver/BiDi/BrowsingContext/BrowsingContextInputModule.cs` (CSHARP) | Magnitude: 77.54 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 42, func_start: 17, branch: 14, structural_boundaries: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `dotnet/src/webdriver/IWebDriver.cs` (CSHARP) | Magnitude: 34.29 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 79, indent_spaces: 10, args: 5, func_start: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `dotnet/src/webdriver/DevTools/DevToolsEventData.cs` (CSHARP) | Magnitude: 20.82 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 15, indent_spaces: 7, safety: 6, state_mutation: 6
- `dotnet/src/webdriver/Interactions/InputDevice.cs` (CSHARP) | Magnitude: 48.34 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 38, indent_spaces: 27, func_start: 9, api: 8
- `dotnet/src/webdriver/JavaScriptExceptionThrownEventArgs.cs` (CSHARP) | Magnitude: 8.38 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 10, indent_spaces: 5, api: 3, structural_boundaries: 2
- `dotnet/src/webdriver/WebDriverException.cs` (CSHARP) | Magnitude: 21.38 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 25, indent_spaces: 14, api: 4, branch: 3
- `dotnet/src/support/Events/WebDriverNavigationEventArgs.cs` (CSHARP) | Magnitude: 22.5 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 20, indent_spaces: 11, state_mutation: 6, api: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `java/src/org/openqa/selenium/devtools/v143/v143Javascript.java` (JAVA) | Magnitude: 3.52 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 23, ui_framework: 10, decorators: 10
- `java/src/org/openqa/selenium/devtools/v144/v144Domains.java` (JAVA) | Magnitude: 18.68 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 21, import: 8, api: 7
- `java/src/org/openqa/selenium/devtools/v145/v145Domains.java` (JAVA) | Magnitude: 18.68 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 21, import: 8, api: 7
- `dotnet/src/webdriver/BiDi/Browser/SetDownloadBehaviorCommand.cs` (CSHARP) | Magnitude: 96.32 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 10, api: 8, class_start: 7, encapsulation: 5
- `java/src/org/openqa/selenium/devtools/v143/v143Domains.java` (JAVA) | Magnitude: 18.68 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 21, import: 8, api: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `dotnet/src/webdriver/DevTools/DevToolsExtensionMethods.cs` (CSHARP) | Magnitude: 13.08 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 19, dead_code: 8, structural_boundaries: 2, class_start: 1
- `dotnet/src/support/UI/ILoadableComponent.cs` (CSHARP) | Magnitude: 17.74 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 21, dead_code: 4, structural_boundaries: 2, args: 1
- `dotnet/src/webdriver/ICapabilities.cs` (CSHARP) | Magnitude: 39.28 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 22, indent_spaces: 3, structural_boundaries: 2, args: 2
- `dotnet/src/webdriver/BiDi/Input/Key.cs` (CSHARP) | Magnitude: 10.52 | Delta: **0.074 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 2, sec_reflection_metaprogramming: 2, sec_dead_code: 1
- `cpp/imehandler/linux/src/ibushandler.h` (CPP) | Magnitude: 18.54 | Delta: **0.093 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 12, immutability_locks: 7, args: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `Rakefile` -> Churn: **76.82%** | Cog Load: 12.7936% | Debt: 99.9115%
- `dotnet/src/webdriver/BiDi/BrowsingContext/BrowsingContextNetworkModule.cs` -> Churn: **65.67%** | Cog Load: 98.3042% | Debt: 13.1644%
- `dotnet/src/webdriver/BiDi/Input/InputModule.cs` -> Churn: **65.67%** | Cog Load: 100.0% | Debt: 100.0%
- `dotnet/src/webdriver/BiDi/Broker.cs` -> Churn: **61.75%** | Cog Load: 97.1351% | Debt: 22.6862%
- `dotnet/src/webdriver/BiDi/Module.cs` -> Churn: **54.11%** | Cog Load: 39.0682% | Debt: 99.9999%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `dotnet/src/webdriver/BiDi/BrowsingContext/IBrowsingContextModule.cs` -> **Nikolay Borisenko** (100.0% isolated ownership) | Magnitude: 5264.41
- `dotnet/src/webdriver/BiDi/Network/INetworkModule.cs` -> **Nikolay Borisenko** (100.0% isolated ownership) | Magnitude: 2494.56
- `dotnet/src/webdriver/BiDi/Emulation/IEmulationModule.cs` -> **Nikolay Borisenko** (100.0% isolated ownership) | Magnitude: 1407.25
- `common/devtools/pdl.py` -> **Titus Fortner** (100.0% isolated ownership) | Magnitude: 1166.38
- `dotnet/src/webdriver/BiDi/Script/IScriptModule.cs` -> **Nikolay Borisenko** (100.0% isolated ownership) | Magnitude: 1145.6

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `py/selenium/webdriver/remote/webdriver.py` -> **Severity: 0.017** (Bridge: 0.0002 * Flux: 97.4464%)
- `py/selenium/webdriver/common/webdriver.py` -> **Severity: 0.007** (Bridge: 0.0002 * Flux: 42.3183%)
- `py/selenium/webdriver/common/driver_finder.py` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 100.0%)
- `py/selenium/webdriver/support/wait.py` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 99.9995%)
- `py/selenium/webdriver/webkitgtk/options.py` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 91.878%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `java/src/org/openqa/selenium/internal/Require.java` -> **Severity: 6612.8** (Blast Radius: 66.128 * Doc Risk: 100.0%)
- `dotnet/src/webdriver/BiDi/Optional.cs` -> **Severity: 1866.0** (Blast Radius: 18.66 * Doc Risk: 100.0%)
- `dotnet/src/webdriver/Internal/Logging/Logger.cs` -> **Severity: 1251.8** (Blast Radius: 12.518 * Doc Risk: 100.0%)
- `java/src/org/openqa/selenium/WebDriverException.java` -> **Severity: 628.7** (Blast Radius: 6.287 * Doc Risk: 100.0%)
- `java/src/org/openqa/selenium/remote/http/HttpRequest.java` -> **Severity: 348.8** (Blast Radius: 3.488 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
