# ARCHITECTURAL_BRIEF: selenium
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_python/selenium` |
| **Timestamp** | `2026-08-07T04:02:37.809954+00:00` |
| **Scan Duration** | `9.83s` |
| **Git Branch** | `trunk` |
| **Git Commit** | `549261ba1cccb1d3bfa662d35d7b144607abf51c` |
| **Git Remote** | `https://github.com/SeleniumHQ/selenium.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 2205 malicious artifacts.

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
> **Architectural Drift Z-Score:** `4.693`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 1248 | 47.4% |
| file_cluster_13 | 824 | 31.3% |
| file_cluster_16 | 142 | 5.4% |
| file_cluster_0 | 95 | 3.6% |
| file_cluster_4 | 73 | 2.8% |
| file_cluster_7 | 43 | 1.6% |
| file_cluster_2 | 14 | 0.5% |
| file_cluster_17 | 11 | 0.4% |
| file_cluster_15 | 8 | 0.3% |
| file_cluster_9 | 6 | 0.2% |
| file_cluster_12 | 5 | 0.2% |
| Unknown | 4 | 0.2% |
| file_cluster_11 | 2 | 0.1% |
| file_cluster_1 | 2 | 0.1% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 19.8 | 7.5 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.8 | 36.5 | 41.2 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 39.0 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 11.3 | 2.4 | 80.0 |
| API Exposure | 0.0 | 17.0 | 4.5 | 4.3 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 6.9 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 33.8 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 99.7 | 0.5 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 84.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 1.9 | 0.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 6.6 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 39.4 | 21.7 | 11.9 |
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

- `Browser::NewWindow3` (@ `cpp/iedriver/Browser.cpp`) -> Impact: **293.4** | LOC: 627
- `WebDriver` (@ `dotnet/src/webdriver/WebDriver.cs`) -> Impact: **250.9** | LOC: 758
  * *Intent:* /// <summary> /// Initializes a new instance of the <see cref="WebDriver"/> class. /// </summary> /// <param name="executor">The <see cref="ICommandEx...
- `Element::IsFocusable` (@ `cpp/iedriver/Element.cpp`) -> Impact: **248.2** | LOC: 807
- `fireMSPointerEvent` (@ `javascript/atoms/device.js`) -> Impact: **240.7** | LOC: 373
  * *Intent:* // On click and mousedown events, captured pointers are ignored and the
- `quit` (@ `java/src/org/openqa/selenium/remote/RemoteWebDriver.java`) -> Impact: **219.2** | LOC: 582
- `execute` (@ `java/src/org/openqa/selenium/remote/RemoteWebDriver.java`) -> Impact: **218.6** | LOC: 571
- `find_elements` (@ `py/selenium/webdriver/remote/webdriver.py`) -> Impact: **202.0** | LOC: 480
- `NewSessionCommandHandler::ValidateCapabi` (@ `cpp/iedriver/CommandHandlers/NewSessionCommandHandler.cpp`) -> Impact: **189.4** | LOC: 348
- `parse` (@ `common/devtools/pdl.py`) -> Impact: **186.4** | LOC: 129
- `SendKeysCommandHandler::CreateActionSequ` (@ `cpp/iedriver/CommandHandlers/SendKeysCommandHandler.cpp`) -> Impact: **177.1** | LOC: 494

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `rust/src` | 19 | 45837.77 | 19.99% | 51.96% |
| `cpp/iedriver` | 72 | 11106.0 | 38.85% | 34.82% |
| `cpp/iedriver/CommandHandlers` | 116 | 6681.34 | 52.55% | 44.92% |
| `dotnet/src/webdriver` | 128 | 5747.79 | 10.84% | 49.69% |
| `dotnet/src/webdriver/BiDi/BrowsingContext` | 37 | 5715.0 | 29.65% | 25.79% |
| `__monolith__` | 19 | 5293.64 | 9.38% | 15.78% |
| `javascript/grid-ui` | 6 | 5061.5 | 5.58% | 0.0% |
| `common/extensions/webextensions-selenium-example-signed/META-INF` | 1 | 5000.0 | 0.0% | 0.0% |
| `java/src/org/openqa/selenium/remote` | 60 | 4442.23 | 15.32% | 51.53% |
| `javascript/selenium-webdriver/bidi` | 35 | 4166.74 | 25.32% | 41.25% |

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
- `java/src/org/openqa/selenium/support/ui/ExpectedConditions.java` -> **16** Orphaned Functions | **90** Duplicates
- `java/src/org/openqa/selenium/devtools/CdpClientGenerator.java` -> **3** Orphaned Functions | **68** Duplicates
- `py/selenium/webdriver/support/expected_conditions.py` -> **29** Orphaned Functions | **27** Duplicates
- `cpp/iedriver/IECommandExecutor.cpp` -> **44** Orphaned Functions | **4** Duplicates

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
20. **`py/selenium/webdriver/common/bidi/browsing_context.py`** -> AI Confidence: **99.31%**
21. **`py/selenium/webdriver/common/selenium_manager.py`** -> AI Confidence: **99.31%**
22. **`py/selenium/webdriver/remote/client_config.py`** -> AI Confidence: **99.31%**
23. **`scripts/pinned_browsers.py`** -> AI Confidence: **99.31%**
24. **`scripts/update_cdp.py`** -> AI Confidence: **99.31%**
25. **`py/selenium/webdriver/firefox/firefox_profile.py`** -> AI Confidence: **99.31%**
26. **`javascript/atoms/device.js`** -> AI Confidence: **99.31%**
27. **`javascript/atoms/dom.js`** -> AI Confidence: **99.31%**
28. **`javascript/atoms/domcore.js`** -> AI Confidence: **99.31%**
29. **`javascript/atoms/events.js`** -> AI Confidence: **99.31%**
30. **`javascript/atoms/inject.js`** -> AI Confidence: **99.31%**
31. **`javascript/atoms/locators/xpath.js`** -> AI Confidence: **99.31%**
32. **`javascript/atoms/window.js`** -> AI Confidence: **99.31%**
33. **`javascript/selenium-webdriver/index.js`** -> AI Confidence: **99.31%**
34. **`javascript/selenium-webdriver/testing/index.js`** -> AI Confidence: **99.31%**
35. **`javascript/webdriver/atoms/element.js`** -> AI Confidence: **99.31%**
36. **`cpp/iedriver/Alert.cpp`** -> AI Confidence: **99.31%**
37. **`cpp/iedriver/AsyncScriptExecutor.cpp`** -> AI Confidence: **99.31%**
38. **`cpp/iedriver/Browser.cpp`** -> AI Confidence: **99.31%**
39. **`cpp/iedriver/BrowserFactory.cpp`** -> AI Confidence: **99.31%**
40. **`cpp/iedriver/CommandHandlers/AddCookieCommandHandler.cpp`** -> AI Confidence: **99.31%**
41. **`cpp/iedriver/CommandHandlers/ClearElementCommandHandler.cpp`** -> AI Confidence: **99.31%**
42. **`cpp/iedriver/CommandHandlers/ClickElementCommandHandler.cpp`** -> AI Confidence: **99.31%**
43. **`cpp/iedriver/CommandHandlers/GetElementRectCommandHandler.cpp`** -> AI Confidence: **99.31%**
44. **`cpp/iedriver/CommandHandlers/SendKeysCommandHandler.cpp`** -> AI Confidence: **99.31%**
45. **`cpp/iedriver/DocumentHost.cpp`** -> AI Confidence: **99.31%**
46. **`cpp/iedriver/ElementFinder.cpp`** -> AI Confidence: **99.31%**
47. **`cpp/iedriver/IECommandExecutor.cpp`** -> AI Confidence: **99.31%**
48. **`cpp/iedriver/IECommandHandler.cpp`** -> AI Confidence: **99.31%**
49. **`cpp/iedriver/VariantUtilities.cpp`** -> AI Confidence: **99.31%**
50. **`cpp/iedriverserver/IEDriverServer.cpp`** -> AI Confidence: **99.31%**
51. **`cpp/imehandler/linux/src/ibushandler.cpp`** -> AI Confidence: **99.31%**
52. **`cpp/webdriver-interactions/interactions.cpp`** -> AI Confidence: **99.31%**
53. **`cpp/webdriver-interactions/interactions_linux_common.cpp`** -> AI Confidence: **99.31%**
54. **`cpp/webdriver-interactions/interactions_linux_mouse.cpp`** -> AI Confidence: **99.31%**
55. **`cpp/webdriver-interactions/logging.h`** -> AI Confidence: **99.31%**
56. **`cpp/webdriver-server/server.cc`** -> AI Confidence: **99.31%**
57. **`dotnet/src/webdriver/Manager/SeleniumManager.cs`** -> AI Confidence: **99.31%**
58. **`dotnet/src/webdriver/Remote/HttpCommandExecutor.cs`** -> AI Confidence: **99.31%**
59. **`cpp/linux-specific/x_ignore_nofocus.c`** -> AI Confidence: **99.31%**
60. **`java/src/org/openqa/selenium/Proxy.java`** -> AI Confidence: **99.31%**
61. **`java/src/org/openqa/selenium/bidi/network/Cookie.java`** -> AI Confidence: **99.31%**
62. **`java/src/org/openqa/selenium/bidi/network/ResponseData.java`** -> AI Confidence: **99.31%**
63. **`java/src/org/openqa/selenium/bidi/script/RemoteValue.java`** -> AI Confidence: **99.31%**
64. **`java/src/org/openqa/selenium/docker/internal/Reference.java`** -> AI Confidence: **99.31%**
65. **`java/src/org/openqa/selenium/grid/commands/CompletionCommand.java`** -> AI Confidence: **99.31%**
66. **`java/src/org/openqa/selenium/grid/commands/InfoCommand.java`** -> AI Confidence: **99.31%**
67. **`java/src/org/openqa/selenium/grid/config/AnnotatedConfig.java`** -> AI Confidence: **99.31%**
68. **`java/src/org/openqa/selenium/grid/config/CompoundConfig.java`** -> AI Confidence: **99.31%**
69. **`java/src/org/openqa/selenium/grid/config/TomlConfig.java`** -> AI Confidence: **99.31%**
70. **`java/src/org/openqa/selenium/grid/data/CapabilityCount.java`** -> AI Confidence: **99.31%**
71. **`java/src/org/openqa/selenium/grid/data/SessionClosedData.java`** -> AI Confidence: **99.31%**
72. **`java/src/org/openqa/selenium/grid/data/SessionEventData.java`** -> AI Confidence: **99.31%**
73. **`java/src/org/openqa/selenium/grid/distributor/local/LocalNodeRegistry.java`** -> AI Confidence: **99.31%**
74. **`java/src/org/openqa/selenium/grid/jmx/MBean.java`** -> AI Confidence: **99.31%**
75. **`java/src/org/openqa/selenium/grid/node/ProxyNodeWebsockets.java`** -> AI Confidence: **99.31%**
76. **`java/src/org/openqa/selenium/grid/node/config/NodeFlags.java`** -> AI Confidence: **99.31%**
77. **`java/src/org/openqa/selenium/grid/node/config/SessionCapabilitiesMutator.java`** -> AI Confidence: **99.31%**
78. **`java/src/org/openqa/selenium/grid/node/kubernetes/KubernetesFlags.java`** -> AI Confidence: **99.31%**
79. **`java/src/org/openqa/selenium/grid/node/kubernetes/KubernetesOptions.java`** -> AI Confidence: **99.31%**
80. **`java/src/org/openqa/selenium/grid/web/ResourceHandler.java`** -> AI Confidence: **99.31%**
81. **`java/src/org/openqa/selenium/json/JsonInput.java`** -> AI Confidence: **99.31%**
82. **`java/src/org/openqa/selenium/json/JsonOutput.java`** -> AI Confidence: **99.31%**
83. **`java/src/org/openqa/selenium/manager/SeleniumManagerOutput.java`** -> AI Confidence: **99.31%**
84. **`java/src/org/openqa/selenium/net/HostIdentifier.java`** -> AI Confidence: **99.31%**
85. **`java/src/org/openqa/selenium/net/NetworkUtils.java`** -> AI Confidence: **99.31%**
86. **`java/src/org/openqa/selenium/net/UrlChecker.java`** -> AI Confidence: **99.31%**
87. **`java/src/org/openqa/selenium/netty/server/MessageInboundConverter.java`** -> AI Confidence: **99.31%**
88. **`java/src/org/openqa/selenium/remote/ErrorHandler.java`** -> AI Confidence: **99.31%**
89. **`java/src/org/openqa/selenium/remote/WebElementToJsonConverter.java`** -> AI Confidence: **99.31%**
90. **`java/src/org/openqa/selenium/remote/http/jdk/JdkHttpMessages.java`** -> AI Confidence: **99.31%**
91. **`java/src/org/openqa/selenium/remote/service/DriverFinder.java`** -> AI Confidence: **99.31%**
92. **`java/src/org/openqa/selenium/support/events/EventFiringDecorator.java`** -> AI Confidence: **99.31%**
93. **`java/src/org/openqa/selenium/support/ui/Select.java`** -> AI Confidence: **99.31%**
94. **`javascript/grid-ui/src/App.tsx`** -> AI Confidence: **99.31%**
95. **`rust/src/edge.rs`** -> AI Confidence: **99.31%**
96. **`rust/src/files.rs`** -> AI Confidence: **99.31%**
97. **`rust/src/firefox.rs`** -> AI Confidence: **99.31%**
98. **`rust/src/lib.rs`** -> AI Confidence: **99.31%**
99. **`rust/src/logger.rs`** -> AI Confidence: **99.31%**
100. **`rake_tasks/appium.rake`** -> AI Confidence: **99.29%**
101. **`rake_tasks/bazel.rake`** -> AI Confidence: **99.29%**
102. **`rake_tasks/dotnet.rake`** -> AI Confidence: **99.29%**
103. **`rake_tasks/java.rake`** -> AI Confidence: **99.29%**
104. **`rake_tasks/node.rake`** -> AI Confidence: **99.29%**
105. **`rake_tasks/python.rake`** -> AI Confidence: **99.29%**
106. **`rake_tasks/ruby.rake`** -> AI Confidence: **99.29%**
107. **`rb/support/rbs_collection_update.rb`** -> AI Confidence: **99.29%**
108. **`common/repositories.bzl`** -> AI Confidence: **99.29%**
109. **`java/private/module.bzl`** -> AI Confidence: **99.29%**
110. **`javascript/private/header.bzl`** -> AI Confidence: **99.29%**
111. **`javascript/bidi-support/bidi-mutation-listener.js`** -> AI Confidence: **99.29%**
112. **`javascript/grid-ui/jest.config.cjs`** -> AI Confidence: **99.29%**
113. **`javascript/selenium-webdriver/common/driverFinder.js`** -> AI Confidence: **99.29%**
114. **`javascript/webdriver/key.js`** -> AI Confidence: **99.29%**
115. **`go`** -> AI Confidence: **99.29%**
116. **`scripts/build-info.sh`** -> AI Confidence: **99.29%**
117. **`scripts/credential-helper.sh`** -> AI Confidence: **99.29%**
118. **`scripts/format.sh`** -> AI Confidence: **99.29%**
119. **`scripts/github-actions/check-format.sh`** -> AI Confidence: **99.29%**
120. **`scripts/github-actions/collect-test-logs.sh`** -> AI Confidence: **99.29%**
121. **`scripts/gitpod/start-vnc.sh`** -> AI Confidence: **99.29%**
122. **`cpp/iedriver/ActionSimulators/ActionSimulator.cpp`** -> AI Confidence: **99.29%**
123. **`dotnet/src/webdriver/BiDi/Browser/IBrowserModule.cs`** -> AI Confidence: **99.29%**
124. **`dotnet/src/webdriver/BiDi/BrowsingContext/IBrowsingContextModule.cs`** -> AI Confidence: **99.29%**
125. **`dotnet/src/webdriver/BiDi/BrowsingContext/IBrowsingContextNetworkModule.cs`** -> AI Confidence: **99.29%**
126. **`dotnet/src/webdriver/BiDi/Emulation/IEmulationModule.cs`** -> AI Confidence: **99.29%**
127. **`dotnet/src/webdriver/BiDi/Network/INetworkModule.cs`** -> AI Confidence: **99.29%**
128. **`dotnet/src/webdriver/BiDi/Script/IScriptModule.cs`** -> AI Confidence: **99.29%**
129. **`dotnet/src/webdriver/Chromium/ChromiumOptions.cs`** -> AI Confidence: **99.29%**
130. **`dotnet/src/webdriver/ErrorResponse.cs`** -> AI Confidence: **99.29%**
131. **`dotnet/src/webdriver/Firefox/FirefoxOptions.cs`** -> AI Confidence: **99.29%**
132. **`dotnet/src/webdriver/Firefox/Internal/IniFileReader.cs`** -> AI Confidence: **99.29%**
133. **`dotnet/src/webdriver/Internal/ResponseValueJsonConverter.cs`** -> AI Confidence: **99.29%**
134. **`scripts/build-info.ps1`** -> AI Confidence: **99.29%**
135. **`scripts/dev-environment-setup.ps1`** -> AI Confidence: **99.29%**
136. **`scripts/gitpod/.gitpod.Dockerfile`** -> AI Confidence: **99.29%**
137. **`scripts/remote-image/Dockerfile`** -> AI Confidence: **99.29%**
138. **`javascript/atoms/json.js`** -> AI Confidence: **99.26%**
139. **`java/src/org/openqa/selenium/manager/SeleniumManager.java`** -> AI Confidence: **99.25%**
140. **`py/selenium/webdriver/common/service.py`** -> AI Confidence: **99.24%**
141. **`py/selenium/webdriver/remote/remote_connection.py`** -> AI Confidence: **99.24%**
142. **`javascript/atoms/locators/locators.js`** -> AI Confidence: **99.24%**
143. **`cpp/iedriver/CommandHandlers/ScreenshotElementCommandHandler.cpp`** -> AI Confidence: **99.24%**
144. **`cpp/webdriver-server/logging.h`** -> AI Confidence: **99.24%**
145. **`java/src/dev/selenium/tools/javadoc/JavadocJarMaker.java`** -> AI Confidence: **99.24%**
146. **`java/src/org/openqa/selenium/SharedCapabilitiesMethods.java`** -> AI Confidence: **99.24%**
147. **`java/src/org/openqa/selenium/bidi/Connection.java`** -> AI Confidence: **99.24%**
148. **`java/src/org/openqa/selenium/chromium/ChromiumOptions.java`** -> AI Confidence: **99.24%**
149. **`java/src/org/openqa/selenium/devtools/CdpEndpointFinder.java`** -> AI Confidence: **99.24%**
150. **`java/src/org/openqa/selenium/devtools/SeleniumCdpConnection.java`** -> AI Confidence: **99.24%**
151. **`java/src/org/openqa/selenium/firefox/FileExtension.java`** -> AI Confidence: **99.24%**
152. **`java/src/org/openqa/selenium/firefox/Preferences.java`** -> AI Confidence: **99.24%**
153. **`java/src/org/openqa/selenium/firefox/ProfilesIni.java`** -> AI Confidence: **99.24%**
154. **`java/src/org/openqa/selenium/grid/Bootstrap.java`** -> AI Confidence: **99.24%**
155. **`java/src/org/openqa/selenium/grid/config/ConcatenatingConfig.java`** -> AI Confidence: **99.24%**
156. **`java/src/org/openqa/selenium/grid/config/ConfigFlags.java`** -> AI Confidence: **99.24%**
157. **`java/src/org/openqa/selenium/grid/config/MapConfig.java`** -> AI Confidence: **99.24%**
158. **`java/src/org/openqa/selenium/grid/data/NodeStatus.java`** -> AI Confidence: **99.24%**
159. **`java/src/org/openqa/selenium/grid/data/Session.java`** -> AI Confidence: **99.24%**
160. **`java/src/org/openqa/selenium/grid/distributor/local/LocalGridModel.java`** -> AI Confidence: **99.24%**
161. **`java/src/org/openqa/selenium/grid/node/docker/DockerFlags.java`** -> AI Confidence: **99.24%**
162. **`java/src/org/openqa/selenium/grid/node/docker/DockerSessionFactory.java`** -> AI Confidence: **99.24%**
163. **`java/src/org/openqa/selenium/grid/node/kubernetes/KubernetesSession.java`** -> AI Confidence: **99.24%**
164. **`java/src/org/openqa/selenium/grid/node/kubernetes/KubernetesSessionFactory.java`** -> AI Confidence: **99.24%**
165. **`java/src/org/openqa/selenium/grid/node/relay/RelayFlags.java`** -> AI Confidence: **99.24%**
166. **`java/src/org/openqa/selenium/grid/sessionmap/jdbc/JdbcBackedSessionMap.java`** -> AI Confidence: **99.24%**
167. **`java/src/org/openqa/selenium/io/FileHandler.java`** -> AI Confidence: **99.24%**
168. **`java/src/org/openqa/selenium/json/InstanceCoercer.java`** -> AI Confidence: **99.24%**
169. **`java/src/org/openqa/selenium/json/InstantCoercer.java`** -> AI Confidence: **99.24%**
170. **`java/src/org/openqa/selenium/logging/LogLevelMapping.java`** -> AI Confidence: **99.24%**
171. **`java/src/org/openqa/selenium/net/DefaultNetworkInterfaceProvider.java`** -> AI Confidence: **99.24%**
172. **`java/src/org/openqa/selenium/netty/server/WebSocketFrameProxy.java`** -> AI Confidence: **99.24%**
173. **`java/src/org/openqa/selenium/os/ExecutableFinder.java`** -> AI Confidence: **99.24%**
174. **`java/src/org/openqa/selenium/remote/ElementLocation.java`** -> AI Confidence: **99.24%**
175. **`java/src/org/openqa/selenium/remote/ErrorCodec.java`** -> AI Confidence: **99.24%**
176. **`java/src/org/openqa/selenium/remote/NewSessionPayload.java`** -> AI Confidence: **99.24%**
177. **`java/src/org/openqa/selenium/remote/codec/AbstractHttpResponseCodec.java`** -> AI Confidence: **99.24%**
178. **`java/src/org/openqa/selenium/remote/http/jdk/JdkHttpClient.java`** -> AI Confidence: **99.24%**
179. **`java/src/org/openqa/selenium/remote/service/DriverCommandExecutor.java`** -> AI Confidence: **99.24%**
180. **`java/src/org/openqa/selenium/remote/service/DriverService.java`** -> AI Confidence: **99.24%**
181. **`java/src/org/openqa/selenium/remote/tracing/Tags.java`** -> AI Confidence: **99.24%**
182. **`java/src/org/openqa/selenium/support/events/WebDriverListener.java`** -> AI Confidence: **99.24%**
183. **`javascript/grid-ui/src/screens/Overview/Overview.tsx`** -> AI Confidence: **99.24%**
184. **`javascript/grid-ui/src/screens/Sessions/Sessions.tsx`** -> AI Confidence: **99.24%**
185. **`javascript/grid-ui/src/util/browser-logo.tsx`** -> AI Confidence: **99.24%**
186. **`rust/src/chrome.rs`** -> AI Confidence: **99.24%**
187. **`rust/src/main.rs`** -> AI Confidence: **99.24%**
188. **`py/selenium/webdriver/remote/server.py`** -> AI Confidence: **99.23%**
189. **`scripts/update_docfx.py`** -> AI Confidence: **99.23%**
190. **`javascript/atoms/frame.js`** -> AI Confidence: **99.23%**
191. **`javascript/selenium-webdriver/common/seleniumManager.js`** -> AI Confidence: **99.23%**
192. **`javascript/webdriver/atoms/inputs.js`** -> AI Confidence: **99.23%**
193. **`cpp/iedriver/CommandHandlers/ActionsCommandHandler.cpp`** -> AI Confidence: **99.23%**
194. **`cpp/iedriver/CommandHandlers/GetElementTextCommandHandler.cpp`** -> AI Confidence: **99.23%**
195. **`cpp/iedriver/CommandHandlers/SwitchToFrameCommandHandler.cpp`** -> AI Confidence: **99.23%**
196. **`cpp/iedriver/HookProcessor.cpp`** -> AI Confidence: **99.23%**
197. **`java/src/org/openqa/selenium/Capabilities.java`** -> AI Confidence: **99.23%**
198. **`java/src/org/openqa/selenium/WebDriverException.java`** -> AI Confidence: **99.23%**
199. **`java/src/org/openqa/selenium/grid/config/Config.java`** -> AI Confidence: **99.23%**
200. **`java/src/org/openqa/selenium/grid/data/SessionCreatedData.java`** -> AI Confidence: **99.23%**
201. **`java/src/org/openqa/selenium/grid/server/BaseServerFlags.java`** -> AI Confidence: **99.23%**
202. **`java/src/org/openqa/selenium/remote/http/UrlTemplate.java`** -> AI Confidence: **99.23%**
203. **`javascript/grid-ui/src/components/Node/Node.tsx`** -> AI Confidence: **99.23%**
204. **`rake_tasks/common.rb`** -> AI Confidence: **99.2%**
205. **`py/selenium/webdriver/remote/errorhandler.py`** -> AI Confidence: **99.2%**
206. **`cpp/iedriver/RegistryUtilities.cpp`** -> AI Confidence: **99.2%**
207. **`cpp/webdriver-server/command.cc`** -> AI Confidence: **99.2%**
208. **`py/selenium/webdriver/common/action_chains.py`** -> AI Confidence: **99.18%**
209. **`javascript/selenium-webdriver/remote/index.js`** -> AI Confidence: **99.18%**
210. **`java/src/org/openqa/selenium/By.java`** -> AI Confidence: **99.18%**
211. **`java/src/org/openqa/selenium/bidi/module/BrowsingContextInspector.java`** -> AI Confidence: **99.18%**
212. **`java/src/org/openqa/selenium/bidi/module/Network.java`** -> AI Confidence: **99.18%**
213. **`java/src/org/openqa/selenium/chrome/AddHasCasting.java`** -> AI Confidence: **99.18%**
214. **`java/src/org/openqa/selenium/chromium/ChromiumDriver.java`** -> AI Confidence: **99.18%**
215. **`java/src/org/openqa/selenium/chromium/ChromiumDriverCommandExecutor.java`** -> AI Confidence: **99.18%**
216. **`java/src/org/openqa/selenium/devtools/Connection.java`** -> AI Confidence: **99.18%**
217. **`java/src/org/openqa/selenium/devtools/DevToolsProvider.java`** -> AI Confidence: **99.18%**
218. **`java/src/org/openqa/selenium/devtools/v143/v143Domains.java`** -> AI Confidence: **99.18%**
219. **`java/src/org/openqa/selenium/devtools/v144/v144Domains.java`** -> AI Confidence: **99.18%**
220. **`java/src/org/openqa/selenium/devtools/v145/v145Domains.java`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `25` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `11427` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `dotnet/src/webdriver/BiDi/EventDispatcher.cs` (CSHARP) -> Cumulative Risk: **788.95**
- **Archetype:** `file_cluster_4` (Distance: 12.016 IQR)
- **Magnitude:** 181.2 | **LOC:** 163 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9541%)
- **Heaviest Functions:** `ProcessEventsAwaiterAsync` (Impact: 14.6), `reader.WaitToReadAsync` (Impact: 9.4), `InvokeHandlerAsync` (Impact: 7.6)

### 2. `java/src/org/openqa/selenium/grid/sessionmap/local/LocalSessionMap.java` (JAVA) -> Cumulative Risk: **735.05**
- **Archetype:** `file_cluster_13` (Distance: 11.263 IQR)
- **Magnitude:** 243.92 | **LOC:** 317 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9694%), State Flux (99.7891%), Documentation (96.6606%)
- **Heaviest Functions:** `removeWithReason` (Impact: 18.7), `batchRemove` (Impact: 14.3), `batchRemoveByUri` (Impact: 13.6)

### 3. `dotnet/src/webdriver/BiDi/Broker.cs` (CSHARP) -> Cumulative Risk: **725.66**
- **Archetype:** `file_cluster_4` (Distance: 12.899 IQR)
- **Magnitude:** 380.18 | **LOC:** 405 | **CtrlFlow:** 59.7% | **Authorship Centralization:** 93.8%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9395%), Concurrency (99.8304%), Cognitive Load (96.7202%)
- **Heaviest Functions:** `ProcessReceivedMessage` (Impact: 128.1), `ReceiveMessagesLoopAsync` (Impact: 41.8), `ExecuteCommandAsync` (Impact: 18.2)

### 4. `dotnet/src/webdriver/BiDi/Input/InputModule.cs` (CSHARP) -> Cumulative Risk: **711.2**
- **Archetype:** `file_cluster_4` (Distance: 10.621 IQR)
- **Magnitude:** 52.72 | **LOC:** 80 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 90.9%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `SetFilesAsync` (Impact: 5.2), `PerformActionsAsync` (Impact: 4.8), `ReleaseActionsAsync` (Impact: 4.3)

### 5. `java/src/org/openqa/selenium/bidi/Connection.java` (JAVA) -> Cumulative Risk: **707.99**
- **Archetype:** `file_cluster_4` (Distance: 12.023 IQR)
- **Magnitude:** 317.32 | **LOC:** 390 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9892%), Concurrency (98.3693%), Cognitive Load (94.3625%)
- **Heaviest Functions:** `handleResponse` (Impact: 23.9), `handleEventResponse` (Impact: 16.8), `removeListener` (Impact: 16.6)

### 6. `dotnet/src/webdriver/BiDi/Subscription.cs` (CSHARP) -> Cumulative Risk: **704.33**
- **Archetype:** `file_cluster_4` (Distance: 12.1 IQR)
- **Magnitude:** 48.14 | **LOC:** 68 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9956%), Concurrency (99.6802%)
- **Heaviest Functions:** `UnsubscribeAsync` (Impact: 5.9), `WithContext` (Impact: 3.7), `DisposeAsync` (Impact: 2.5)

### 7. `dotnet/src/webdriver/BiDi/BrowsingContext/BrowsingContextScriptModule.cs` (CSHARP) -> Cumulative Risk: **695.89**
- **Archetype:** `file_cluster_4` (Distance: 11.31 IQR)
- **Magnitude:** 67.2 | **LOC:** 71 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 83.3%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9967%)
- **Heaviest Functions:** `BrowsingContextScriptModule` (Impact: 17.9), `EvaluateAsync` (Impact: 6.5), `CallFunctionAsync` (Impact: 6.5)

### 8. `dotnet/src/webdriver/BiDi/BrowsingContext/BrowsingContextNetworkModule.cs` (CSHARP) -> Cumulative Risk: **692.69**
- **Archetype:** `file_cluster_4` (Distance: 13.413 IQR)
- **Magnitude:** 258.96 | **LOC:** 216 | **CtrlFlow:** 51.6% | **Authorship Centralization:** 90.9%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9999%), Concurrency (99.9999%)
- **Heaviest Functions:** `BrowsingContextNetworkModule` (Impact: 66.8), `OnBeforeRequestSentAsync` (Impact: 6.5), `OnBeforeRequestSentAsync` (Impact: 6.5)

### 9. `java/src/org/openqa/selenium/devtools/Connection.java` (JAVA) -> Cumulative Risk: **679.58**
- **Archetype:** `file_cluster_13` (Distance: 11.928 IQR)
- **Magnitude:** 228.56 | **LOC:** 374 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (97.1125%), Cognitive Load (96.0953%)
- **Heaviest Functions:** `send` (Impact: 19.9), `sendAndWait` (Impact: 12.8), `onText` (Impact: 10.4)

### 10. `dotnet/src/webdriver/BiDi/BrowsingContext/BrowsingContext.cs` (CSHARP) -> Cumulative Risk: **676.98**
- **Archetype:** `file_cluster_4` (Distance: 13.843 IQR)
- **Magnitude:** 461.02 | **LOC:** 482 | **CtrlFlow:** 47.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `GetHashCode` (Impact: 6.9), `Equals` (Impact: 4.7), `NavigateAsync` (Impact: 4.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `rust/src/lib.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.848 IQR)
- **Top Global Matches:** file_cluster_8: 12.848, file_cluster_13: 13.091, file_cluster_16: 13.234
- **Magnitude:** 42767.61 | **LOC:** 1758 | **CtrlFlow:** 55.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (20.4168%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 325`, `structural_boundaries: 258`, `args: 163`, `func_start: 147`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 151`
* *Architecture:* `io: 1`, `api: 68`, `concurrency: 1`, `import: 32`
* *Defense:* `safety: 196`, `sync_locks: 12`, `immutability_locks: 45`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::lock::Lock, SAFARIDRIVER_NAME, crate::config::OS::MACOS, X64, crate::metadata::
    create_browser_metadata, crate::grid::GRID_NAME, collect_files_from_cache, IEDRIVER_NAME...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `common/extensions/webextensions-selenium-example-signed/META-INF/cose.sig` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `dotnet/src/webdriver/BiDi/BrowsingContext/IBrowsingContextModule.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.547 IQR)
- **Top Global Matches:** file_cluster_16: 10.547, file_cluster_8: 11.083, file_cluster_4: 11.232
- **Magnitude:** 2703.16 | **LOC:** 65 | **CtrlFlow:** 95.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 2`, `args: 40`, `func_start: 40`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `concurrency: 54`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cpp/iedriver/Element.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.576 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.047 IQR)
- **Top Global Matches:** file_cluster_8: 14.576, file_cluster_13: 14.8, file_cluster_7: 14.984
- **Magnitude:** 1586.48 | **LOC:** 1880 | **CtrlFlow:** 71.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (90.7835%), Tech Debt (96.3358%)
**Top Internal Functions/Classes:**
  * `Element::IsFocusable` (Impact: 248.2)
  * `Element::GetLocation` (Impact: 68.7)
  * `Element::IsImageMap` (Impact: 45.4)
  * `Element::GetLocationOnceScrolledIntoView` (Impact: 26.6)
  * `Element::GetCssPropertyValue` (Impact: 25.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 166`, `structural_boundaries: 66`, `args: 79`, `func_start: 25`
* *Risk/State:* `state_mutation: 1015`, `planned_debt: 2`, `fragile_debt: 2`, `duplicate_logic: 2`, `orphaned_logic: 22`
* *Architecture:* `import: 11`
* *Defense:* `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` logging.h, StringUtilities.h, json.h, Script.h, errorcodes.h, VariantUtilities.h, Browser.h, atoms.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dotnet/src/webdriver/BiDi/Network/INetworkModule.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.366 IQR)
- **Top Global Matches:** file_cluster_16: 10.366, file_cluster_8: 10.875, file_cluster_4: 11.031
- **Magnitude:** 1294.56 | **LOC:** 49 | **CtrlFlow:** 92.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 2`, `args: 24`, `func_start: 24`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `concurrency: 29`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cpp/iedriver/IECommandExecutor.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.955 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.108 IQR)
- **Top Global Matches:** file_cluster_8: 13.955, file_cluster_13: 14.071, file_cluster_11: 14.366
- **Magnitude:** 1271.04 | **LOC:** 1720 | **CtrlFlow:** 66.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (90.6557%), Tech Debt (89.1951%)
**Top Internal Functions/Classes:**
  * `IECommandExecutor::OpenNewBrowserWindow` (Impact: 64.5)
  * `IECommandExecutor::OnAfterNewWindow` (Impact: 57.0)
  * `IECommandExecutor::DispatchCommand` (Impact: 50.1)
  * `IECommandExecutor::HandleUnexpectedAlert` (Impact: 42.6)
  * `IECommandExecutor::OnNewHtmlDialog` (Impact: 30.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 178`, `structural_boundaries: 88`, `args: 182`, `func_start: 48`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 722`, `dead_code: 3`, `duplicate_logic: 4`, `orphaned_logic: 44`
* *Architecture:* `concurrency: 12`, `import: 28`
* *Defense:* `safety: 1`, `sync_locks: 6`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 21):` ElementFinder.h, ElementRepository.h, errorcodes.h, vector, InputManager.h, command_types.h, WebDriverConstants.h, algorithm...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cpp/iedriver/CommandHandlers/NewSessionCommandHandler.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.537 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.553 IQR)
- **Top Global Matches:** file_cluster_8: 13.537, file_cluster_13: 13.829, file_cluster_7: 13.986
- **Magnitude:** 1135.42 | **LOC:** 1046 | **CtrlFlow:** 71.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.3592%), Tech Debt (78.0184%)
**Top Internal Functions/Classes:**
  * `NewSessionCommandHandler::ValidateCapabi` (Impact: 189.4)
  * `NewSessionCommandHandler::MatchCapabilit` (Impact: 30.8)
  * `NewSessionCommandHandler::ValidateArgume` (Impact: 29.5)
  * `NewSessionCommandHandler::GetJsonTypeDes` (Impact: 21.0)
  * `NewSessionCommandHandler::GetUnexpectedA` (Impact: 21.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 181`, `structural_boundaries: 71`, `args: 81`, `func_start: 19`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 673`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 2`, `orphaned_logic: 16`
* *Architecture:* `import: 10`
* *Defense:* `immutability_locks: 33`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` WebDriverConstants.h, logging.h, Alert.h, InputManager.h, Browser.h, errorcodes.h, IECommandExecutor.h, BrowserFactory.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `java/src/org/openqa/selenium/remote/RemoteWebDriver.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.469 IQR)
- **Top Global Matches:** file_cluster_13: 11.469, file_cluster_0: 11.564, file_cluster_8: 11.89
- **Magnitude:** 1134.88 | **LOC:** 1430 | **CtrlFlow:** 33.6% | **Authorship Centralization:** 63.6%
- **Risk Profile:** Cognitive Load (17.2541%), Tech Debt (99.8563%)
**Top Internal Functions/Classes:**
  * `quit` (Impact: 219.2)
  * `execute` (Impact: 218.6)
  * `log` (Impact: 62.7)
  * `execute` (Impact: 39.2)
  * `checkChromeW3CFalse` (Impact: 27.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 225`, `args: 97`, `func_start: 99`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 56`, `state_mutation: 30`, `duplicate_logic: 28`
* *Architecture:* `io: 3`, `api: 137`, `concurrency: 12`, `import: 87`
* *Defense:* `safety: 29`, `doc: 15`, `immutability_locks: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.428
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 57):` org.openqa.selenium.logging.LocalLogs, org.openqa.selenium.logging.LoggingHandler, org.openqa.selenium.remote.http.HttpClient, org.openqa.selenium.OutputType, java.util.ArrayList, org.openqa.selenium.JavascriptExecutor, org.openqa.selenium.remote.service.DriverCommandExecutor, java.io.IOException...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `java/src/org/openqa/selenium/devtools/CdpClientGenerator.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.05 IQR)
- **Top Global Matches:** file_cluster_0: 12.05, file_cluster_13: 12.092, file_cluster_17: 12.147
- **Magnitude:** 978.92 | **LOC:** 1438 | **CtrlFlow:** 35.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (42.6443%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `toTypeDeclaration` (Impact: 51.5)
  * `getJavaType` (Impact: 43.5)
  * `getJavaDefaultValue` (Impact: 43.4)
  * `getMapper` (Impact: 41.3)
  * `toTypeDeclaration` (Impact: 40.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 192`, `structural_boundaries: 350`, `args: 161`, `func_start: 114`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 60`, `state_mutation: 180`, `planned_debt: 2`, `duplicate_logic: 68`, `orphaned_logic: 3`
* *Architecture:* `io: 37`, `api: 95`, `import: 38`
* *Defense:* `safety: 35`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` java.io.OutputStream, java.nio.file.SimpleFileVisitor, com.github.javaparser.ast.stmt.BlockStmt, java.util.List, java.nio.file.FileVisitResult.CONTINUE, java.util.stream.Collectors, java.io.InputStream, java.util.jar.JarEntry...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cpp/iedriver/Browser.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.632 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.852 IQR)
- **Top Global Matches:** file_cluster_8: 13.632, file_cluster_13: 13.805, file_cluster_7: 14.071
- **Magnitude:** 958.46 | **LOC:** 913 | **CtrlFlow:** 63.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.339%), Tech Debt (99.8786%)
**Top Internal Functions/Classes:**
  * `Browser::NewWindow3` (Impact: 293.4)
  * `Browser::Wait` (Impact: 58.3)
  * `Browser::IsDocumentNavigating` (Impact: 54.7)
  * `Browser::GetDocumentFromWindow` (Impact: 21.4)
  * `Browser::GetDocument` (Impact: 17.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 109`, `structural_boundaries: 62`, `args: 98`, `func_start: 30`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 401`, `fragile_debt: 2`, `duplicate_logic: 2`, `orphaned_logic: 27`
* *Architecture:* `import: 14`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` Alert.h, logging.h, StringUtilities.h, Script.h, CustomTypes.h, messages.h, errorcodes.h, HookProcessor.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cpp/linux-specific/print_events.h` (CPP | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.527 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.616 IQR)
- **Top Global Matches:** file_cluster_8: 13.527, file_cluster_13: 13.77, file_cluster_11: 13.919
- **Magnitude:** 915.64 | **LOC:** 734 | **CtrlFlow:** 86.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.1669%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `print_event` (Impact: 147.1)
  * `do_EnterNotify` (Impact: 58.8)
    * *Intent:* do_KeyPress (out_f, eventp); /* since it has the same info */
  * `do_FocusIn` (Impact: 55.1)
  * `do_ConfigureRequest` (Impact: 25.3)
  * `do_PropertyNotify` (Impact: 23.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 244`, `structural_boundaries: 39`, `args: 40`, `func_start: 36`
* *Risk/State:* `state_mutation: 355`
* *Architecture:* `api: 2`, `import: 8`
* *Defense:* `safety: 4`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.464
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Xlib.h, Xproto.h, stdio.h, ctype.h, Xutil.h, Xos.h, Xlocale.h, stdlib.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cpp/iedriver/CommandHandlers/SendKeysCommandHandler.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.853 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.979 IQR)
- **Top Global Matches:** file_cluster_8: 13.853, file_cluster_13: 14.002, file_cluster_7: 14.297
- **Magnitude:** 914.8 | **LOC:** 1145 | **CtrlFlow:** 63.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.6526%), Tech Debt (96.7481%)
**Top Internal Functions/Classes:**
  * `SendKeysCommandHandler::CreateActionSequ` (Impact: 177.1)
  * `SendKeysCommandHandler::ExecuteInternal` (Impact: 49.2)
  * `SendKeysCommandHandler::GetFileSelection` (Impact: 35.0)
  * `SendKeysCommandHandler::SetInsertionPoin` (Impact: 24.7)
  * `SendKeysCommandHandler::FillFileName` (Impact: 22.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 64`, `args: 90`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `state_mutation: 464`, `planned_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 16`
* *Architecture:* `import: 15`
* *Defense:* `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` logging.h, UIAutomation.h, VariantUtilities.h, InputManager.h, errorcodes.h, Browser.h, iomanip, IECommandExecutor.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `java/src/org/openqa/selenium/support/ui/ExpectedConditions.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.213 IQR)
- **Top Global Matches:** file_cluster_0: 11.213, file_cluster_8: 11.283, file_cluster_16: 11.392
- **Magnitude:** 912.64 | **LOC:** 1855 | **CtrlFlow:** 35.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (4.3561%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `or` (Impact: 42.0)
    * *Intent:* /** * An expectation for checking number of WebElements with given locator * * @param locator used t...
  * `and` (Impact: 20.1)
  * `resultAsString` (Impact: 17.5)
  * `apply` (Impact: 15.5)
  * `numberOfWindowsToBe` (Impact: 14.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 271`, `args: 126`, `func_start: 114`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 95`, `planned_debt: 2`, `duplicate_logic: 90`, `orphaned_logic: 16`
* *Architecture:* `api: 146`, `import: 21`
* *Defense:* `safety: 57`, `doc: 170`, `sync_locks: 11`, `immutability_locks: 83`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` java.util.Objects.requireNonNullElse, java.util.List, java.util.Optional, java.util.logging.Level, org.openqa.selenium.WebElement, org.openqa.selenium.WebDriverException, org.openqa.selenium.WebDriver, org.openqa.selenium.JavascriptExecutor...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `java/src/org/openqa/selenium/grid/node/kubernetes/KubernetesSessionFactory.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.904 IQR)
- **Top Global Matches:** file_cluster_13: 11.904, file_cluster_8: 12.115, file_cluster_0: 12.266
- **Magnitude:** 898.22 | **LOC:** 1438 | **CtrlFlow:** 43.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (28.1395%), Tech Debt (94.3794%)
**Top Internal Functions/Classes:**
  * `apply` (Impact: 87.9)
  * `doWaitForPodRunning` (Impact: 52.4)
  * `evaluatePodStatus` (Impact: 46.8)
  * `buildJobSpec` (Impact: 39.3)
  * `buildJobSpecFromTemplate` (Impact: 23.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 214`, `structural_boundaries: 274`, `args: 68`, `func_start: 77`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 90`, `state_mutation: 183`, `duplicate_logic: 25`, `orphaned_logic: 3`
* *Architecture:* `io: 12`, `api: 9`, `concurrency: 6`, `import: 95`
* *Defense:* `safety: 44`, `doc: 1`, `sync_locks: 1`, `immutability_locks: 29`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 35):` org.openqa.selenium.remote.http.HttpClient, java.util.Optional.ofNullable, java.util.ArrayList, org.openqa.selenium.TimeoutException, org.openqa.selenium.remote.Dialect, io.fabric8.kubernetes.api.model.ObjectMetaBuilder, org.openqa.selenium.remote.Command, org.openqa.selenium.remote.http.HttpResponse...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cpp/iedriver/BrowserFactory.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.88 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.317 IQR)
- **Top Global Matches:** file_cluster_8: 13.88, file_cluster_13: 14.002, file_cluster_11: 14.144
- **Magnitude:** 856.14 | **LOC:** 1594 | **CtrlFlow:** 66.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (86.078%), Tech Debt (96.8949%)
**Top Internal Functions/Classes:**
  * `BrowserFactory::FindChildWindowForProces` (Impact: 46.6)
  * `BrowserFactory::AttachToBrowserUsingShel` (Impact: 42.4)
  * `BrowserFactory::FindDialogWindowForProce` (Impact: 36.3)
  * `BrowserFactory::AttachToBrowserUsingActi` (Impact: 35.6)
  * `BrowserFactory::InvokeClearCacheUtility` (Impact: 34.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 76`, `args: 101`, `func_start: 27`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 2`, `state_mutation: 485`, `dead_code: 3`, `fragile_debt: 1`, `orphaned_logic: 26`
* *Architecture:* `import: 14`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` exdispid.h, iepmapi.h, logging.h, StringUtilities.h, vector, shlobj.h, ctime, shlguid.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `java/src/org/openqa/selenium/grid/node/local/LocalNode.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.977 IQR)
- **Top Global Matches:** file_cluster_13: 11.977, file_cluster_4: 12.168, file_cluster_0: 12.342
- **Magnitude:** 841.04 | **LOC:** 1555 | **CtrlFlow:** 33.8% | **Authorship Centralization:** 57.1%
- **Risk Profile:** Cognitive Load (72.6805%), Tech Debt (82.729%)
**Top Internal Functions/Classes:**
  * `LocalNode` (Impact: 78.7)
  * `createExternalSession` (Impact: 47.7)
  * `stopTimedOutSession` (Impact: 28.9)
  * `downloadFile` (Impact: 22.9)
  * `getStatus` (Impact: 22.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 294`, `args: 100`, `func_start: 70`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 118`, `dead_code: 1`, `duplicate_logic: 10`, `orphaned_logic: 19`
* *Architecture:* `io: 30`, `api: 38`, `concurrency: 128`, `import: 114`
* *Defense:* `safety: 36`, `doc: 6`, `sync_locks: 8`, `immutability_locks: 36`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 56):` org.openqa.selenium.grid.data.Session, java.time.format.DateTimeFormatter.RFC_1123_DATE_TIME, java.time.ZoneOffset.UTC, java.util.ArrayList, java.net.URISyntaxException, java.util.Objects.requireNonNullElseGet, org.openqa.selenium.grid.data.CreateSessionResponse, org.openqa.selenium.remote.http.HttpResponse...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `javascript/atoms/device.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.241 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.449 IQR)
- **Top Global Matches:** file_cluster_13: 14.241, file_cluster_11: 14.271, file_cluster_15: 14.282
- **Magnitude:** 767.32 | **LOC:** 987 | **CtrlFlow:** 61.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (49.5509%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `fireMSPointerEvent` (Impact: 240.7)
    * *Intent:* // On click and mousedown events, captured pointers are ignored and the
  * `focusOnElement` (Impact: 59.7)
  * `fireMouseEvent` (Impact: 50.0)
    * *Intent:* /** * Sets the element with which the device is interacting. *
  * `clickElement` (Impact: 45.5)
    * *Intent:* * Fires a MSPointer event given the state of the device and the given * arguments. * * @param {!bot....
  * `getTargetOfOptionMouseEvent_` (Impact: 31.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 59`, `args: 34`, `func_start: 34`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 221`, `planned_debt: 3`, `duplicate_logic: 12`, `orphaned_logic: 8`
* *Architecture:* `import: 12`
* *Defense:* `safety: 8`, `doc: 126`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` bot.dom, bot.Error, goog.array, goog.dom.TagName, goog.userAgent, bot.events, bot.userAgent, goog.userAgent.product...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `dotnet/src/webdriver/WebDriver.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.183 IQR)
- **Top Global Matches:** file_cluster_13: 14.183, file_cluster_8: 14.236, file_cluster_7: 14.321
- **Magnitude:** 741.26 | **LOC:** 1186 | **CtrlFlow:** 78.2% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (39.0255%), Tech Debt (79.2257%)
**Top Internal Functions/Classes:**
  * `WebDriver` (Impact: 250.9)
    * *Intent:* /// <summary> /// Initializes a new instance of the <see cref="WebDriver"/> class. /// </summary> //...
  * `UnpackAndThrowOnError` (Impact: 73.4)
  * `ParseJavaScriptReturnValue` (Impact: 39.0)
  * `ConvertObjectToJavaScriptObject` (Impact: 31.9)
  * `StartSession` (Impact: 25.9)
    * *Intent:* /// <summary> /// Dispose the WebDriver Instance /// </summary>
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 34`, `args: 29`, `func_start: 79`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 123`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 2`, `orphaned_logic: 7`
* *Architecture:* `api: 19`, `concurrency: 7`, `import: 7`
* *Defense:* `safety: 71`, `doc: 142`, `immutability_locks: 2`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` OpenQA.Selenium.Interactions, System.Collections.ObjectModel, OpenQA.Selenium.Internal, System.Globalization, System.Collections, OpenQA.Selenium.VirtualAuth, System.Diagnostics.CodeAnalysis
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cpp/iedriver/Alert.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.096 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.984 IQR)
- **Top Global Matches:** file_cluster_8: 14.096, file_cluster_13: 14.267, file_cluster_11: 14.487
- **Magnitude:** 712.52 | **LOC:** 666 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.5232%), Tech Debt (99.8463%)
**Top Internal Functions/Classes:**
  * `Alert::Dismiss` (Impact: 111.1)
  * `Alert::GetDialogButton` (Impact: 24.6)
  * `Alert::ClickAlertButtonUsingAccessibilit` (Impact: 16.8)
    * *Intent:* // ASSUMPTION: This means the alert is from onbeforeunload, and // the second "static text" accessib...
  * `Alert::Alert` (Impact: 15.8)
  * `Alert::SendKeysInternal` (Impact: 13.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 47`, `args: 48`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 425`, `planned_debt: 1`, `fragile_debt: 1`, `orphaned_logic: 20`
* *Architecture:* `import: 7`
* *Defense:* `safety: 1`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` Alert.h, logging.h, UIAutomation.h, StringUtilities.h, errorcodes.h, DocumentHost.h, WebDriverConstants.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/selenium/webdriver/remote/webdriver.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.265 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.283 IQR)
- **Top Global Matches:** file_cluster_13: 13.265, file_cluster_16: 13.408, file_cluster_0: 13.498
- **Magnitude:** 676.32 | **LOC:** 1571 | **CtrlFlow:** 34.1% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (39.1684%), Tech Debt (15.0352%)
**Top Internal Functions/Classes:**
  * `find_elements` (Impact: 202.0)
  * `create_matches` (Impact: 21.6)
  * `_wrap_value` (Impact: 12.8)
  * `_unwrap_value` (Impact: 12.7)
  * `fedcm_dialog` (Impact: 12.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 162`, `structural_boundaries: 313`, `args: 101`, `func_start: 100`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 106`, `duplicate_logic: 2`
* *Architecture:* `io: 5`, `api: 120`, `concurrency: 9`, `import: 56`
* *Defense:* `safety: 44`, `doc: 172`, `test: 5`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.957
  * `Choke Point (Betweenness):` 0.000171 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 38):` selenium.webdriver.common.bidi.storage, urllib3, selenium.webdriver.common.credential, selenium.webdriver.remote.websocket_connection, tempfile, contextlib, types, selenium.webdriver.remote.client_config...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `javascript/atoms/dom.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.879 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.264 IQR)
- **Top Global Matches:** file_cluster_13: 12.879, file_cluster_11: 12.971, file_cluster_0: 12.976
- **Magnitude:** 621.52 | **LOC:** 1448 | **CtrlFlow:** 55.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (32.0848%), Tech Debt (61.4822%)
**Top Internal Functions/Classes:**
  * `getOverflowState` (Impact: 95.9)
  * `getOverflowStyles` (Impact: 76.3)
  * `appendVisibleTextLinesFromNodeInComposed` (Impact: 41.7)
  * `appendVisibleTextLinesFromTextNode_` (Impact: 34.0)
    * *Intent:* /** * Determines whether an element is what a user would call "shown". This means * that the element...
  * `positiveSize` (Impact: 28.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 156`, `structural_boundaries: 124`, `args: 41`, `func_start: 29`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 170`, `dead_code: 3`, `planned_debt: 5`, `orphaned_logic: 8`
* *Architecture:* `import: 16`
* *Defense:* `safety: 6`, `doc: 108`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` goog.dom.DomHelper, goog.math.Coordinate, goog.math.Rect, goog.array, bot.dom.core, goog.string, goog.style, goog.dom.TagName...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `java/src/org/openqa/selenium/support/events/WebDriverListener.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.955 IQR)
- **Top Global Matches:** file_cluster_13: 13.955, file_cluster_8: 14.207, file_cluster_16: 14.212
- **Magnitude:** 603.42 | **LOC:** 1314 | **CtrlFlow:** 46.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.2597%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `afterAnyWebDriverCall` (Impact: 4.6)
    * *Intent:* // Global /** * This method is called before the execution of any method on the 'target' object. It ...
  * `afterExecuteAsyncScript` (Impact: 4.6)
    * *Intent:* /**
  * `afterAnyWebElementCall` (Impact: 4.6)
    * *Intent:* /** * This method will be called before {@link WebDriver#findElement(By)} is called. * * @param driv...
  * `afterAnyNavigationCall` (Impact: 4.6)
    * *Intent:* /** * This method will be called before {@link JavascriptExecutor#executeScript(ScriptKey, * Object....
  * `afterAnyOptionsCall` (Impact: 4.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 148`, `structural_boundaries: 173`, `args: 148`, `func_start: 148`, `class_start: 1`
* *Risk/State:* `state_mutation: 6`, `planned_debt: 1`, `duplicate_logic: 34`, `orphaned_logic: 114`
* *Architecture:* `api: 1`, `import: 23`
* *Defense:* `doc: 439`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` org.openqa.selenium.Dimension, org.openqa.selenium.remote.RemoteWebDriver, java.util.List, org.openqa.selenium.WebElement, org.openqa.selenium.interactions.Sequence, org.openqa.selenium.OutputType, org.openqa.selenium.WebDriver, org.openqa.selenium.interactions.Actions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cpp/webdriver-server/server.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.976 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.856 IQR)
- **Top Global Matches:** file_cluster_8: 12.976, file_cluster_13: 13.298, file_cluster_7: 13.485
- **Magnitude:** 598.84 | **LOC:** 812 | **CtrlFlow:** 61.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.9535%), Tech Debt (95.1379%)
**Top Internal Functions/Classes:**
  * `Server::DispatchCommand` (Impact: 46.9)
  * `Server::SendResponseToClient` (Impact: 38.8)
  * `Server::ReadRequestBody` (Impact: 15.6)
  * `Server::LookupCommand` (Impact: 14.8)
  * `Server::GetListeningPorts` (Impact: 13.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 51`, `args: 57`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `state_mutation: 340`, `duplicate_logic: 4`, `orphaned_logic: 23`
* *Architecture:* `import: 10`
* *Defense:* `safety: 1`, `immutability_locks: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` sstream, logging.h, errorcodes.h, session.h, cstdio, uri_info.h, server.h, algorithm...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

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
- `common/src/web/downloads/download.html` (HTML) | Magnitude: 19.78 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 13, decorators: 13, io: 7
- `java/src/org/openqa/selenium/firefox/GeckoDriverInfo.java` (JAVA) | Magnitude: 39.8 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 32, import: 11, args: 10
- `java/src/org/openqa/selenium/remote/tracing/opentelemetry/OpenTelemetrySpan.java` (JAVA) | Magnitude: 83.18 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 110, structural_boundaries: 29, state_mutation: 20, func_start: 13
- `dotnet/src/webdriver/Properties/NullableAttributes.cs` (CSHARP) | Magnitude: 47.64 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 57, api: 26, indent_spaces: 23, structural_boundaries: 18
- `dotnet/src/webdriver/StackTraceElement.cs` (CSHARP) | Magnitude: 70.86 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 72, state_mutation: 31, doc: 26, branch: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `dotnet/src/webdriver/DevTools/Target.cs` (CSHARP) | Magnitude: 23.62 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 45, indent_spaces: 16, api: 9, args: 8
- `dotnet/src/webdriver/DevTools/JavaScript.cs` (CSHARP) | Magnitude: 35.82 | Delta: **0.183 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 63, indent_spaces: 23, args: 12, func_start: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `dotnet/src/support/Extensions/WebDriverExtensions.cs` (CSHARP) | Magnitude: 67.12 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 70, doc: 30, branch: 23, safety: 14
- `scripts/github-actions/rerun-failures.sh` (SHELL) | Magnitude: 4.54 | Delta: **0.072 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: branch: 18, state_mutation: 18, safety_bypasses: 13, io: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `scripts/gitpod/start-xvfb.sh` (SHELL) | Magnitude: 0.28 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: reflection_metaprogramming: 7, sec_dead_code: 4, safety: 3, indent_spaces: 3
- `java/src/org/openqa/selenium/support/pagefactory/FieldDecorator.java` (JAVA) | Magnitude: 17.74 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 5, structural_boundaries: 3, reflection_metaprogramming: 2, args: 1
- `scripts/github-actions/ci-build.sh` (SHELL) | Magnitude: 1.55 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 9, indent_spaces: 4, branch: 3, reflection_metaprogramming: 3
- `common/src/web/iframeWithAlert.html` (HTML) | Magnitude: 11.52 | Delta: **0.15 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: io: 2, api: 1, reflection_metaprogramming: 1, debug_prints: 1
- `common/src/web/click_tests/issue5237_frame.html` (HTML) | Magnitude: 11.52 | Delta: **0.174 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: io: 2, api: 1, reflection_metaprogramming: 1, listeners: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `java/src/org/openqa/selenium/devtools/v144/v144Domains.java` (JAVA) | Magnitude: 15.08 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 21, import: 8, api: 7
- `java/src/org/openqa/selenium/devtools/v144/v144Javascript.java` (JAVA) | Magnitude: 3.52 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 23, ui_framework: 10, decorators: 10
- `java/src/org/openqa/selenium/devtools/v145/v145Javascript.java` (JAVA) | Magnitude: 3.52 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 23, ui_framework: 10, decorators: 10
- `java/src/org/openqa/selenium/remote/HandshakeResponse.java` (JAVA) | Magnitude: 3.92 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 5, func_start: 3, generics: 3
- `javascript/atoms/html5/html5_browser.js` (JAVASCRIPT) | Magnitude: 40.18 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 54, branch: 24, structural_boundaries: 13, doc: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `scripts/build-info.ps1` (POWERSHELL) | Magnitude: 27.16 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 12, branch: 2, closures: 2, indent_spaces: 2
- `dotnet/src/webdriver/Timeouts.cs` (CSHARP) | Magnitude: 57.38 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 59, doc: 48, state_mutation: 28, time_date_logic: 13
- `dotnet/src/webdriver/Platform.cs` (CSHARP) | Magnitude: 92.36 | Delta: **0.102 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 73, indent_spaces: 71, state_mutation: 29, branch: 19
- `dotnet/src/webdriver/OptionsManager.cs` (CSHARP) | Magnitude: 16.74 | Delta: **0.132 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 22, indent_spaces: 13, structural_boundaries: 7, api: 7
- `dotnet/src/webdriver/Support/SystemClock.cs` (CSHARP) | Magnitude: 10.76 | Delta: **0.151 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 19, structural_boundaries: 5, api: 5, indent_spaces: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `java/src/org/openqa/selenium/grid/server/Server.java` (JAVA) | Magnitude: 21.96 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, args: 2, func_start: 2, generics: 2
- `java/src/org/openqa/selenium/events/EventListener.java` (JAVA) | Magnitude: 12.32 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 8, api: 5, generics: 4
- `py/selenium/webdriver/common/bidi/browsing_context.py` (PYTHON) | Magnitude: 467.0 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 588, structural_boundaries: 163, branch: 142, doc: 98
- `java/src/org/openqa/selenium/remote/tracing/empty/NullPropagator.java` (JAVA) | Magnitude: 7.56 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 7, generics: 4, api: 3
- `dotnet/src/webdriver/IJavaScriptEngine.cs` (CSHARP) | Magnitude: 60.57 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 76, args: 14, func_start: 14, indent_spaces: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `java/src/org/openqa/selenium/grid/config/EnvConfig.java` (JAVA) | Magnitude: 31.8 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 13, comprehensions: 11, args: 10
- `common/src/web/sessionCookieDest.html` (HTML) | Magnitude: 18.04 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 6, state_mutation: 6, globals: 6
- `javascript/grid-ui/src/screens/Overview/Overview.tsx` (TYPESCRIPT) | Magnitude: 16.51 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 184, structural_boundaries: 55, branch: 36, args: 29
- `javascript/selenium-webdriver/bidi/addInterceptParameters.js` (JAVASCRIPT) | Magnitude: 37.96 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 49, doc: 15, state_mutation: 12, encapsulation: 11
- `java/src/org/openqa/selenium/grid/config/MapConfig.java` (JAVA) | Magnitude: 51.32 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 63, structural_boundaries: 21, args: 17, comprehensions: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `javascript/grid-ui/src/components/RunningSessions/RunningSessions.tsx` (TYPESCRIPT) | Magnitude: 37.26 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 625, structural_boundaries: 109, ui_framework: 99, args: 93
- `common/src/web/key_tests/remove_on_keypress.html` (HTML) | Magnitude: 27.24 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 26, func_start: 10, args: 7, globals: 6
- `common/src/web/html5/geolocation.js` (JAVASCRIPT) | Magnitude: 11.72 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 9, high_risk_execution: 5, branch: 4, state_mutation: 4
- `javascript/grid-ui/src/components/LiveView/LiveView.tsx` (TYPESCRIPT) | Magnitude: 6.87 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 138, structural_boundaries: 33, args: 32, func_start: 32
- `common/src/web/mouse_interaction.html` (HTML) | Magnitude: 32.86 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 83, structural_boundaries: 20, args: 18, ui_framework: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `java/src/org/openqa/selenium/bidi/Connection.java` (JAVA) | Magnitude: 317.32 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 277, structural_boundaries: 88, concurrency: 77, branch: 66
- `dotnet/src/webdriver/BiDi/Script/MessageEventArgs.cs` (CSHARP) | Magnitude: 18.18 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, concurrency: 2, args: 1, func_start: 1
- `dotnet/src/webdriver/BiDi/Browser/BrowserModule.cs` (CSHARP) | Magnitude: 80.96 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 43, structural_boundaries: 27, concurrency: 24, func_start: 18
- `dotnet/src/webdriver/BiDi/WebExtension/WebExtensionModule.cs` (CSHARP) | Magnitude: 23.16 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 12, func_start: 6, concurrency: 6
- `dotnet/src/webdriver/Remote/DriverServiceCommandExecutor.cs` (CSHARP) | Magnitude: 60.4 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 52, indent_spaces: 50, func_start: 15, state_mutation: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `dotnet/src/webdriver/IWebDriver.cs` (CSHARP) | Magnitude: 34.29 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 79, indent_spaces: 10, args: 5, func_start: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `dotnet/src/support/Events/WebElementValueEventArgs.cs` (CSHARP) | Magnitude: 6.4 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 13, indent_spaces: 6, api: 3, structural_boundaries: 2
- `dotnet/src/webdriver/Interactions/InputDevice.cs` (CSHARP) | Magnitude: 29.44 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 38, indent_spaces: 27, func_start: 9, api: 8
- `dotnet/src/webdriver/JavaScriptExceptionThrownEventArgs.cs` (CSHARP) | Magnitude: 7.38 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 10, indent_spaces: 5, api: 3, structural_boundaries: 2
- `dotnet/src/webdriver/CapabilityType.cs` (CSHARP) | Magnitude: 36.54 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 89, indent_spaces: 52, api: 28, immutability_locks: 27
- `java/src/org/openqa/selenium/logging/LogType.java` (JAVA) | Magnitude: 22.24 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 10, indent_spaces: 9, api: 7, globals: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `java/src/org/openqa/selenium/devtools/v143/v143Javascript.java` (JAVA) | Magnitude: 3.52 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 23, ui_framework: 10, decorators: 10
- `java/src/org/openqa/selenium/devtools/v145/v145Domains.java` (JAVA) | Magnitude: 15.08 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 21, import: 8, api: 7
- `dotnet/src/webdriver/BiDi/BrowsingContext/PrintCommand.cs` (CSHARP) | Magnitude: 94.8 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 28, api: 24, immutability_locks: 14
- `java/src/org/openqa/selenium/devtools/v143/v143Domains.java` (JAVA) | Magnitude: 15.08 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 21, import: 8, api: 7
- `java/src/org/openqa/selenium/grid/data/SlotMatcher.java` (JAVA) | Magnitude: 18.26 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, args: 1, func_start: 1, class_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `dotnet/src/webdriver/DevTools/DevToolsExtensionMethods.cs` (CSHARP) | Magnitude: 13.08 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 19, dead_code: 8, structural_boundaries: 2, class_start: 1
- `dotnet/src/support/UI/ILoadableComponent.cs` (CSHARP) | Magnitude: 17.74 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 21, dead_code: 4, structural_boundaries: 2, args: 1
- `dotnet/src/webdriver/ICapabilities.cs` (CSHARP) | Magnitude: 21.96 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_6`
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
- `dotnet/src/webdriver/BiDi/BrowsingContext/BrowsingContextNetworkModule.cs` -> Churn: **65.67%** | Cog Load: 94.8508% | Debt: 99.9999%
- `dotnet/src/webdriver/BiDi/Input/InputModule.cs` -> Churn: **65.67%** | Cog Load: 100.0% | Debt: 100.0%
- `dotnet/src/webdriver/BiDi/Broker.cs` -> Churn: **61.75%** | Cog Load: 96.7202% | Debt: 59.0551%
- `dotnet/src/webdriver/BiDi/Module.cs` -> Churn: **54.11%** | Cog Load: 22.7546% | Debt: 99.9999%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `dotnet/src/webdriver/BiDi/BrowsingContext/IBrowsingContextModule.cs` -> **Nikolay Borisenko** (100.0% isolated ownership) | Magnitude: 2703.16
- `dotnet/src/webdriver/BiDi/Network/INetworkModule.cs` -> **Nikolay Borisenko** (100.0% isolated ownership) | Magnitude: 1294.56
- `java/src/org/openqa/selenium/support/ui/ExpectedConditions.java` -> **Andrei Solntsev** (100.0% isolated ownership) | Magnitude: 912.64
- `javascript/atoms/device.js` -> **Simon Mavi Stewart** (100.0% isolated ownership) | Magnitude: 767.32
- `javascript/atoms/dom.js` -> **Simon Mavi Stewart** (100.0% isolated ownership) | Magnitude: 621.52

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
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
