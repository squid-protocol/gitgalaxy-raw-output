# ARCHITECTURAL_BRIEF: selenium
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/SeleniumHQ/selenium.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 3941 analyzed artifact(s), 323317 LOC.
- **Load-bearing artifact:** `java/src/org/openqa/selenium/internal/Require.java` -- 367 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `java/src/org/openqa/selenium/grid/node/local/LocalNode.java` -- pulls in 114 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `rust/src/lib.rs` at magnitude 41412.31 (structural weight, not risk).
- **How to read this brief:** section 11 ranks artifacts by structural magnitude with a blast-radius line each; section 7 has the full dependency graph. The surface vectors in section 6 describe what is present in a file, not the probability of a defect -- Appendix A has the equations and the validation record behind that distinction.

## 1.5 SYSTEM ROLE & PHILOSOPHY
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
> *(Section 2, the structural-surface lexicon and its equations, is now **Appendix A** at the end of this brief -- the findings come first.)*

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 5042 |
| Analyzed Artifacts (Scanned) | 3941 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1101 |
| Total LOC | 323317 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 78.2% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6176 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1523 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.9013 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 170 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 1427 | 132358 | 36.2% |
| CSHARP | 670 | 45160 | 17.0% |
| PYTHON | 350 | 28384 | 8.9% |
| HTML | 336 | 24160 | 8.5% |
| RUBY | 319 | 21165 | 8.1% |
| JAVASCRIPT | 256 | 32739 | 6.5% |
| CPP | 247 | 25720 | 6.3% |
| PLAINTEXT | 129 | 3 | 3.3% |
| TYPESCRIPT | 63 | 4697 | 1.6% |
| RUST | 36 | 6791 | 0.9% |
| MARKDOWN | 29 | 0 | 0.7% |
| XML | 29 | 9 | 0.7% |
| SHELL | 20 | 418 | 0.5% |
| JSON | 15 | 636 | 0.4% |
| POWERSHELL | 3 | 251 | 0.1% |
| DOCKERFILE | 3 | 128 | 0.1% |
| CSS | 2 | 27 | 0.1% |
| BATCH | 2 | 56 | 0.1% |
| YAML | 2 | 19 | 0.1% |
| MAKEFILE | 1 | 9 | 0.0% |
| C | 1 | 586 | 0.0% |
| BINARY_THREAT | 1 | 1 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled Monorepo`
> **Architectural Drift Z-Score:** `4.844`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +4.84; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 23%, Declarative / Non-Code 19%, Large Core Modules (3) 10%, State Mutators Files 9%, Large Core Modules (2) 8%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 3773 | 95.7% |
| Unknown | 4 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 155 | 3.9% |
| Static: Minified & Vendor Opaque Mass | 9 | 0.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1101*

**Composition by Extension & Reason:**
- `.js`: 237x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 58 LOC), 1x Excluded (Machine-Generated Source Code Signature: 35 LOC)
- `.bazel`: 150x Excluded (Unsupported Extension: '.bazel'), 65x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rbs`: 200x Excluded (Unsupported Extension: '.rbs')
- `.css`: 54x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 31x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable), 2x Unsupported Format (.bazelproject)
- `.yml`: 39x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cs`: 33x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.java`: 32x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 87 LOC)
- `.png`: 31x Excluded (Explicitly Denied Extension: '.png')
- `.xml`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jpg`: 11x Excluded (Explicitly Denied Extension: '.jpg')
- `.json`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 17193 LOC), 1x Excluded (Massive Static Asset Blob: 3476 LOC)
- `.h`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Binary Format Detected)
- `.inl`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.hbs`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 15.5 | 5.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 40.4 | 48.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 15.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 4.8 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 13.0 | 5.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 9.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 30.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.7 | 0.5 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.0 | 0.4 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 6.7 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 56.9 | 94.9 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 71.7 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 8620 | 748 | 2 | `cpp/iedriver/IECommandExecutor.cpp` |
| cleanup | 519 | 235 | 0 | `py/test/selenium/webdriver/common/bidi_browsing_context_tests.py` |
| guards | 22475 | 2238 | 15 | `java/src/org/openqa/selenium/support/ui/ExpectedConditions.java` |
| danger | 9516 | 1592 | 7 | `java/test/org/openqa/selenium/grid/node/kubernetes/InheritedPodSpecTest.java` |
| concurrency | 8657 | 562 | 3 | `javascript/selenium-webdriver/test/bidi/script_test.js` |
| connectivity | 20438 | 2798 | 13 | `java/src/org/openqa/selenium/support/ui/ExpectedConditions.java` |
| io | 7615 | 801 | 3 | `common/src/web/macbeth.html` |
| crypto | 6 | 6 | 0 | `py/selenium/webdriver/remote/shadowroot.py` |
| ipc | 107 | 49 | 0 | `py/selenium/webdriver/common/service.py` |
| time | 2214 | 413 | 1 | `java/test/org/openqa/selenium/grid/distributor/local/LocalDistributorTest.java` |
| serialization | 334 | 171 | 0 | `dotnet/src/webdriver/BiDi/Json/Converters/Polymorphic/RemoteValueConverter.cs` |
| regex | 359 | 155 | 0 | `java/test/org/openqa/selenium/grid/data/DefaultSlotMatcherTest.java` |
| events | 1854 | 371 | 0 | `py/test/unit/selenium/webdriver/remote/error_handler_tests.py` |
| tests | 25400 | 934 | 19 | `java/test/org/openqa/selenium/support/ui/ExpectedConditionsTest.java` |
| docs | 18319 | 1373 | 10 | `dotnet/src/support/Events/EventFiringWebDriver.cs` |
| debt | 1123 | 370 | 0 | `cpp/linux-specific/print_events.h` |
| mutation | 77328 | 2903 | 53 | `common/src/web/macbeth.html` |
| dead_code | 10289 | 1508 | 7 | `dotnet/test/webdriver/ElementFindingTests.cs` |
| credential | 83 | 16 | 0 | `rb/spec/integration/selenium/webdriver/virtual_authenticator_spec.rb` |
| threat | 2202 | 590 | 1 | `common/src/web/javascriptPage.html` |
| ml_ai | 240 | 77 | 0 | `rb/spec/tests.bzl` |
| ui | 1863 | 156 | 0 | `common/src/web/macbeth.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.6667**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `common/src/web/macbeth.html` (Hits: 3036)
- `javascript/selenium-webdriver/test/io/io_test.js` (Hits: 120)
- `py/selenium/webdriver/firefox/firefox_profile.py` (Hits: 40)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Require.java** (`java/src/org/openqa/selenium/internal/Require.java`) — 367 inbound connections
2. **Capabilities.java** (`java/src/org/openqa/selenium/Capabilities.java`) — 187 inbound connections
3. **HttpResponse.java** (`java/src/org/openqa/selenium/remote/http/HttpResponse.java`) — 178 inbound connections
4. **Optional.cs** (`dotnet/src/webdriver/BiDi/Optional.cs`) — 169 inbound connections
5. **HttpRequest.java** (`java/src/org/openqa/selenium/remote/http/HttpRequest.java`) — 169 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **LocalNode.java** (`java/src/org/openqa/selenium/grid/node/local/LocalNode.java`) — 114 outbound dependencies
2. **KubernetesSessionFactory.java** (`java/src/org/openqa/selenium/grid/node/kubernetes/KubernetesSessionFactory.java`) — 95 outbound dependencies
3. **RemoteWebDriver.java** (`java/src/org/openqa/selenium/remote/RemoteWebDriver.java`) — 87 outbound dependencies
4. **AbstractHttpCommandCodec.java** (`java/src/org/openqa/selenium/remote/codec/AbstractHttpCommandCodec.java`) — 86 outbound dependencies
5. **common.rb** (`rb/lib/selenium/webdriver/common.rb`) — 84 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `sendKeys` **(Many-Argument Workhorses)** (@ `cpp/webdriver-interactions/interactions.cpp`) -> Impact: **258.9** | LOC: 258
- `InputManager::GetKeyInfo` **(Many-Argument Workhorses)** (@ `cpp/iedriver/InputManager.cpp`) -> Impact: **231.7** | LOC: 304
- `NewSessionCommandHandler::ValidateCapabilities` **(Many-Argument Workhorses)** (@ `cpp/iedriver/CommandHandlers/NewSessionCommandHandler.cpp`) -> Impact: **189.4** | LOC: 348
- `parse` **(Many-Argument Workhorses)** (@ `common/devtools/pdl.py`) -> Impact: **184.2** | LOC: 123
- `appendVisibleTextLinesFromTextNode_` **(Many-Argument Workhorses)** (@ `javascript/atoms/dom.js`) -> Impact: **150.5** | LOC: 281
  * *Intent:* /** */
- `print_event` **(Many-Argument Workhorses)** (@ `cpp/linux-specific/print_events.h`) -> Impact: **147.1** | LOC: 141
- `InputManager::AddKeyboardInput` **(Many-Argument Workhorses)** (@ `cpp/iedriver/InputManager.cpp`) -> Impact: **142.7** | LOC: 261
- `uncompress` **(Many-Argument Workhorses)** (@ `rust/src/files.rs`) -> Impact: **120.3** | LOC: 78
- `CookieWndProc` **(Many-Argument Workhorses)** (@ `cpp/iedriver/CookieManager.cpp`) -> Impact: **100.8** | LOC: 256
- `RunCommandAsync` **(Many-Argument Workhorses)** (@ `dotnet/src/webdriver/Manager/SeleniumManager.cs`) -> Impact: **100.6** | LOC: 252

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `rust/src` | 19 | 43968.57 | 14.4% | 62.61% |
| `cpp/iedriver` | 72 | 9554.88 | 19.03% | 35.72% |
| `javascript/atoms/test` | 53 | 7101.58 | 11.05% | 0.0% |
| `py/test/selenium/webdriver/common` | 71 | 6735.1 | 22.66% | 0.0% |
| `dotnet/test/webdriver` | 64 | 5461.72 | 8.5% | 0.0% |
| `__monolith__` | 19 | 5333.6 | 6.11% | 0.0% |
| `dotnet/src/webdriver/BiDi/BrowsingContext` | 37 | 5289.43 | 20.76% | 16.48% |
| `javascript/grid-ui` | 9 | 5109.36 | 1.14% | 0.0% |
| `common/extensions/webextensions-selenium-example-signed/META-INF` | 1 | 5000.0 | 0.0% | 0.0% |
| `dotnet/src/webdriver` | 128 | 4932.48 | 6.08% | 21.1% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `javascript/selenium-webdriver/lib/error.js` -> **100.0%** Exposure
- `cpp/iedriver/HtmlDialog.cpp` -> **100.0%** Exposure
- `dotnet/src/webdriver/DevTools/JavaScript.cs` -> **100.0%** Exposure
- `dotnet/src/webdriver/DevTools/Network.cs` -> **100.0%** Exposure
- `java/src/org/openqa/selenium/bidi/emulation/Emulation.java` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `rake_tasks/bazel.rake` -> **100.0%** Exposure
- `rake_tasks/bazel.rb` -> **100.0%** Exposure
- `rake_tasks/common.rb` -> **100.0%** Exposure
- `rake_tasks/node.rake` -> **100.0%** Exposure
- `rake_tasks/ruby.rake` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `dotnet/test/webdriver/ElementFindingTests.cs` -> **111** Orphaned Functions | **0** Duplicates
- `py/test/selenium/webdriver/common/driver_element_finding_tests.py` -> **92** Orphaned Functions | **0** Duplicates
- `java/test/org/openqa/selenium/ElementFindingTest.java` -> **92** Orphaned Functions | **0** Duplicates
- `py/test/selenium/webdriver/common/bidi_script_tests.py` -> **74** Orphaned Functions | **6** Duplicates
- `java/test/org/openqa/selenium/support/ui/ExpectedConditionsTest.java` -> **76** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `py/test/unit/selenium/webdriver/remote/remote_connection_tests.py` -> **71.6928%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `15` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `20153` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `rust/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 41412.31 | **LOC:** 1758 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **72**; blast radius 0.155; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (55.0%), Mutation Surface (formerly State Flux) (38.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (22.1%), Complexity Load (formerly Cognitive Load) (16.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 94
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 315`, `structural_boundaries: 258`, `args: 163`, `func_start: 147`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 36`
* *Architecture:* `io: 1`, `api: 68`, `concurrency: 1`, `import: 32`
* *Defense:* `safety: 32`, `sync_locks: 11`, `immutability_locks: 43`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.155
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ARMV7, CHROMEDRIVER_NAME, ChromeManager, EDGEDRIVER_NAME, EdgeManager, ElectronManager, FirefoxManager, GECKODRIVER_NAME...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.155
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `common/extensions/webextensions-selenium-example-signed/META-INF/cose.sig` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.155
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `javascript/grid-ui/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.155
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dotnet/src/webdriver/BiDi/BrowsingContext/IBrowsingContextModule.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 2703.16 | **LOC:** 65 | **CtrlFlow:** 90.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (9.3%), Connectivity (formerly Api Exposure) (3.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 2`, `args: 40`, `func_start: 40`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `concurrency: 54`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.155
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cpp/iedriver/InputManager.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1710.52 | **LOC:** 1399 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 0.155; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.1%), Complexity Load (formerly Cognitive Load) (94.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `InputManager::GetKeyInfo` **(Many-Argument Workhorses)** (Impact: 231.7)
  * `InputManager::AddKeyboardInput` **(Many-Argument Workhorses)** (Impact: 142.7)
  * `InputManager::PointerMoveTo` **(Many-Argument Workhorses)** (Impact: 99.2)
  * `InputManager::PerformInputSequence` **(Many-Argument Workhorses)** (Impact: 39.3)
  * `InputManager::GetTicks` **(Compute Cores)** (Impact: 37.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 278 instances
* *State Mutation (weighted view):* 971
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 333`, `structural_boundaries: 49`, `args: 108`, `func_start: 26`
* *Risk/State:* `state_mutation: 415`, `dead_code: 4`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 26`
* *Architecture:* `import: 19`
* *Defense:* `sync_locks: 5`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.155
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` JavaScriptActionSimulator.h, SendInputActionSimulator.h, SendMessageActionSimulator.h, DocumentHost.h, Element.h, atoms.h, HookProcessor.h, IElementManager.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `javascript/atoms/test/inject_test.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1695.77 | **LOC:** 568 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.155; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (13.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (12.0%), Complexity Load (formerly Cognitive Load) (5.6%), Connectivity (formerly Api Exposure) (4.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Concurrency (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 97`, `args: 70`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 13`, `planned_debt: 4`
* *Architecture:* `io: 6`, `api: 3`, `concurrency: 13`, `import: 12`
* *Defense:* `safety: 21`, `doc: 1`, `test: 150`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.155
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` qunit.css, qunit.js, qunit_test_runner.js, test_bootstrap.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `javascript/selenium-webdriver/test/bidi/script_test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1669.88 | **LOC:** 830 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.155; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (25.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 192 instances
* *Concurrency (weighted view):* 1198
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 276`, `args: 84`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 63`
* *Architecture:* `concurrency: 238`, `import: 11`
* *Defense:* `safety: 6`, `test: 196`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.155
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` test, node:assert, selenium-webdriver, argumentValue, browsingContext, evaluateResult, protocolValue, realmInfo...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `javascript/webdriver/test/atoms/element_test.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1500.1 | **LOC:** 298 | **CtrlFlow:** 9.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.155; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (31.6%), Connectivity (formerly Api Exposure) (11.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (6.7%), Complexity Load (formerly Cognitive Load) (5.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 74`, `args: 40`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 6`
* *Architecture:* `io: 11`, `api: 28`, `import: 7`
* *Defense:* `safety: 4`, `doc: 1`, `test: 41`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.155
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` test_bootstrap.js, qunit.css, qunit.js, qunit_test_runner.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `javascript/selenium-webdriver/lib/webdriver.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 1384.02 | **LOC:** 3402 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **22**; blast radius 0.608; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (98.6%), Connectivity (formerly Api Exposure) (78.7%), Complexity Load (formerly Cognitive Load) (49.4%)
- **Documentation Coverage:** 17.6056% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `wait` **(Defensive Guards)** (Impact: 50.1)
  * `getWsUrl` **(Defensive Guards)** (Impact: 25.4)
    * *Intent:* /** * Retrieves 'webSocketDebuggerUrl' by sending a http request using debugger address */
  * `createCDPConnection` **(Defensive Guards)** (Impact: 24.1)
    * *Intent:* /** * Creates a new WebSocket connection. */
  * `fromWireValue` **(Defensive Guards)** (Impact: 18.3)
    * *Intent:* /** * Converts a value from its JSON representation according to the WebDriver wire * protocol. Any ...
  * `toWireValue` **(Defensive Guards)** (Impact: 16.8)
    * *Intent:* * <li>if the object is a WebElement, the return value will be the element's * server ID * will be re...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 46 instances
* *Amplified Cascading Flux:* 59 instances
* *Concurrency (weighted view):* 372
* *State Mutation (weighted view):* 246
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 194`, `structural_boundaries: 355`, `args: 241`, `func_start: 194`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 128`, `duplicate_logic: 8`
* *Architecture:* `io: 10`, `api: 73`, `concurrency: 142`, `import: 24`
* *Defense:* `safety: 156`, `doc: 216`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.608
  * `Choke Point (Betweenness):` 1.4e-05 | `Ripple Effect (Closeness):` 0.005023
  * `Imports (Out-Degree: 6):` bidi, CDPConnection, index, by, capabilities, command, error, dialog...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `dotnet/src/webdriver/BiDi/Network/INetworkModule.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1294.56 | **LOC:** 49 | **CtrlFlow:** 85.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (29.0%), Connectivity (formerly Api Exposure) (3.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 2`, `args: 24`, `func_start: 24`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `concurrency: 29`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.155
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `javascript/atoms/test/overflow_test.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1258.4 | **LOC:** 563 | **CtrlFlow:** 3.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.155; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (61.1%), Complexity Load (formerly Cognitive Load) (11.6%), Connectivity (formerly Api Exposure) (11.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (6.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 121`, `args: 30`, `func_start: 6`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 5`, `state_mutation: 35`
* *Architecture:* `io: 6`, `api: 32`, `import: 6`
* *Defense:* `doc: 1`, `test: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.155
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` qunit.css, qunit.js, qunit_test_runner.js, test_bootstrap.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cpp/iedriver/Element.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1194.24 | **LOC:** 1880 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.155; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.0%), Debt Markers (formerly Tech Debt) (90.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Element::IsObscured` **(Many-Argument Workhorses)** (Impact: 99.3)
  * `Element::GetLocation` **(Many-Argument Workhorses)** (Impact: 54.3)
  * `Element::AppendFrameDetails` **(Compute Cores)** (Impact: 45.8)
  * `Element::IsImageMap` **(Compute Cores)** (Impact: 38.1)
  * `Element::GetClickableViewPortLocation` **(Many-Argument Workhorses)** (Impact: 33.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 163 instances
* *State Mutation (weighted view):* 560
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 293`, `structural_boundaries: 134`, `args: 158`, `func_start: 40`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 234`, `dead_code: 4`, `planned_debt: 4`, `fragile_debt: 3`, `unreferenced_by_name: 38`
* *Architecture:* `import: 11`
* *Defense:* `safety: 4`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.155
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` Browser.h, Element.h, atoms.h, Script.h, StringUtilities.h, VariantUtilities.h, WebDriverConstants.h, algorithm...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cpp/webdriver-interactions/interactions.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 1088.02 | **LOC:** 887 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.155; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.2%), Complexity Load (formerly Cognitive Load) (94.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sendKeys` **(Many-Argument Workhorses)** (Impact: 258.9)
  * `backgroundKeyDown` **(Many-Argument Workhorses)** (Impact: 30.7)
  * `backgroundKeyUp` **(Many-Argument Workhorses)** (Impact: 21.3)
  * `fillEventData` **(Many-Argument Workhorses)** (Impact: 19.0)
  * `mouseUpAt` **(Many-Argument Workhorses)** (Impact: 17.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 183 instances
* *State Mutation (weighted view):* 553
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 199`, `structural_boundaries: 50`, `args: 60`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `state_mutation: 187`, `dead_code: 2`, `planned_debt: 1`, `unreferenced_by_name: 4`
* *Architecture:* `import: 8`
* *Defense:* `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.155
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` ctime, event_firing_thread.h, interactions.h, interactions_common.h, iostream, logging.h, stdafx.h, string
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `javascript/atoms/dom.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1058.68 | **LOC:** 1448 | **CtrlFlow:** 35.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.155; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (36.2%)
- **Documentation Coverage:** 12.1366% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `appendVisibleTextLinesFromTextNode_` **(Many-Argument Workhorses)** (Impact: 150.5)
    * *Intent:* /** */
  * `getOverflowState` **(Compute Cores)** (Impact: 99.2)
    * *Intent:* /** * Returns the overflow state of the given element. * * If an optional coordinate or rectangle re...
  * `isShown_` **(Many-Argument Workhorses)** (Impact: 77.7)
    * *Intent:* /** * Extracted code from bot.dom.isShown. * * when determining whether it is shown. * to tell if th...
  * `appendVisibleTextLinesFromNodeInComposedDom_` **(Many-Argument Workhorses)** (Impact: 52.3)
    * *Intent:* /** */
  * `appendVisibleTextLinesFromElementCommon_` **(Many-Argument Workhorses)** (Impact: 48.3)
    * *Intent:* /** * Helper function used by bot.dom.appendVisibleTextLinesFromElement_ and * bot.dom.appendVisible...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 79 instances
* *State Mutation (weighted view):* 256
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 280`, `structural_boundaries: 216`, `args: 56`, `func_start: 43`
* *Risk/State:* `safety_bypasses: 81`, `state_mutation: 98`, `dead_code: 4`, `planned_debt: 9`, `unreferenced_by_name: 5`
* *Architecture:* `import: 16`
* *Defense:* `safety: 19`, `doc: 63`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.155
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` bot, bot.color, bot.dom.core, bot.locators.css, bot.userAgent, goog.array, goog.dom, goog.dom.DomHelper...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/selenium/webdriver/remote/webdriver.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 950.12 | **LOC:** 1571 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **54**; blast radius 1.141; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.2%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (68.8%)
- **Documentation Coverage:** 16.1458% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_remote_connection` **(Many-Argument Workhorses)** (Impact: 29.1)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 27.7)
  * `set_window_rect` **(Many-Argument Workhorses)** (Impact: 20.4)
    * *Intent:* """Set the window's position and size. Sets the x, y coordinates and height and width of the current...
  * `start_devtools` **(Stateful Encapsulated Methods)** (Impact: 20.3)
  * `create_matches` **(Compute Cores)** (Impact: 15.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 103 instances
* *Api Near Db Sink:* 17 instances
* *Concurrency (weighted view):* 24
* *State Mutation (weighted view):* 343
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 326`, `args: 101`, `func_start: 100`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 137`
* *Architecture:* `io: 5`, `api: 94`, `concurrency: 4`, `import: 56`
* *Defense:* `safety: 43`, `doc: 86`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.141
  * `Choke Point (Betweenness):` 0.000126 | `Ripple Effect (Closeness):` 0.005944
  * `Imports (Out-Degree: 35):` abc, base64, contextlib, copy, importlib, json, os, pkgutil...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `java/src/org/openqa/selenium/support/ui/ExpectedConditions.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 913.72 | **LOC:** 1855 | **CtrlFlow:** 9.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **21**; blast radius 0.494; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.4%), Guard Balance (formerly Safety Score) (86.6%), Connectivity (formerly Api Exposure) (74.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (35.3%)
- **Documentation Coverage:** 58.7838% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `or` **(Defensive Guards)** (Impact: 20.7)
    * *Intent:* /** * An expectation with the logical or condition of the given list of conditions. * * <p>Each cond...
  * `apply` **(Defensive Guards)** (Impact: 14.0)
  * `and` **(Stateful Encapsulated Methods)** (Impact: 11.4)
    * *Intent:* /** * An expectation with the logical and condition of the given list of conditions. * * <p>Each con...
  * `resultAsString` **(Stateful Encapsulated Methods)** (Impact: 10.2)
  * `elementSelectionStateToBe` **(Stateful Encapsulated Methods)** (Impact: 10.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *Api Near Db Sink:* 2 instances
* *State Mutation (weighted view):* 202
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 305`, `args: 165`, `func_start: 151`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 107`, `state_mutation: 112`, `planned_debt: 2`
* *Architecture:* `api: 165`, `import: 21`
* *Defense:* `safety: 60`, `doc: 56`, `sync_locks: 15`, `immutability_locks: 91`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.494
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.002537
  * `Imports (Out-Degree: 14):` java.lang.System.lineSeparator, java.util.Collection, java.util.List, java.util.Objects.requireNonNullElse, java.util.Optional, java.util.logging.Level, java.util.logging.Logger, java.util.regex.Pattern...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `java/test/org/openqa/selenium/support/ui/ExpectedConditionsTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 913.5 | **LOC:** 2232 | **CtrlFlow:** 32.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **78**; blast radius 0.155; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (33.9%), Complexity Load (formerly Cognitive Load) (16.9%), Guard Balance (formerly Safety Score) (13.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `whenAllThrow` **(Annotated & Test Methods)** (Impact: 13.3)
  * `fails_ifAtLeastOneElementIsVisible` **(Annotated & Test Methods)** (Impact: 11.8)
  * `urlToBe_negative` **(Annotated & Test Methods)** (Impact: 11.6)
  * `urlMatches_negative` **(Annotated & Test Methods)** (Impact: 11.6)
  * `whenAllFailed` **(Annotated & Test Methods)** (Impact: 11.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 621`, `structural_boundaries: 507`, `args: 261`, `func_start: 168`, `class_start: 63`
* *Risk/State:* `safety_bypasses: 14`, `unreferenced_by_name: 76`
* *Architecture:* `api: 1`, `import: 78`
* *Defense:* `test: 638`, `sync_locks: 87`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.155
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` java.lang.System.lineSeparator, java.time.Duration, java.time.Instant.EPOCH, java.util.Collections.emptyList, java.util.Collections.singletonList, java.util.List, java.util.Set, java.util.regex.Pattern...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cpp/iedriver/IECommandExecutor.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 868.02 | **LOC:** 1720 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **28**; blast radius 0.155; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.1%), Debt Markers (formerly Tech Debt) (94.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `IECommandExecutor::OnAfterNewWindow` **(Many-Argument Workhorses)** (Impact: 57.0)
  * `IECommandExecutor::HandleUnexpectedAlert` **(Many-Argument Workhorses)** (Impact: 42.6)
  * `IECommandExecutor::OnScriptWait` **(Many-Argument Workhorses)** (Impact: 39.6)
  * `IECommandExecutor::DispatchCommand` **(I/O & Config Routines)** (Impact: 38.9)
  * `IECommandExecutor::OpenNewBrowserTab` **(Compute Cores)** (Impact: 38.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 66 instances
* *State Mutation (weighted view):* 267
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 216`, `structural_boundaries: 101`, `args: 214`, `func_start: 55`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 135`, `dead_code: 6`, `fragile_debt: 1`, `unreferenced_by_name: 48`
* *Architecture:* `concurrency: 2`, `import: 28`
* *Defense:* `safety: 1`, `sync_locks: 6`, `immutability_locks: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.155
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 21):` Alert.h, Browser.h, BrowserFactory.h, CommandExecutor.h, CommandHandlerRepository.h, CookieManager.h, Element.h, ElementFinder.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cpp/iedriver/BrowserFactory.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 863.58 | **LOC:** 1594 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.155; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (92.9%), Guard Balance (formerly Safety Score) (83.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `BrowserFactory::AttachToBrowserUsingActiveAccessibility` **(Many-Argument Workhorses)** (Impact: 56.7)
  * `BrowserFactory::AttachToBrowserUsingShellWindows` **(Many-Argument Workhorses)** (Impact: 42.4)
  * `BrowserFactory::LaunchBrowserProcess` **(Compute Cores)** (Impact: 34.0)
  * `BrowserFactory::GetZoomLevel` **(Many-Argument Workhorses)** (Impact: 33.6)
  * `BrowserFactory::InvokeClearCacheUtility` **(Compute Cores)** (Impact: 29.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 92 instances
* *State Mutation (weighted view):* 310
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 265`, `structural_boundaries: 114`, `args: 185`, `func_start: 42`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 126`, `dead_code: 6`, `fragile_debt: 2`, `unreferenced_by_name: 38`
* *Architecture:* `import: 14`
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.155
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` BrowserFactory.h, FileUtilities.h, RegistryUtilities.h, StringUtilities.h, WebDriverConstants.h, ctime, exdispid.h, iepmapi.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/selenium/webdriver/common/bidi/browsing_context.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 819.7 | **LOC:** 1061 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **7**; blast radius 0.255; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.9%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (76.7%)
- **Documentation Coverage:** 71.4286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `from_json` **(Defensive Guards)** (Impact: 44.3)
    * *Intent:* """Creates a BrowsingContextInfo instance from a dictionary. Args: json: A dictionary containing the...
  * `from_json` **(Defensive Guards)** (Impact: 29.5)
    * *Intent:* """Creates a UserPromptOpenedParams instance from a dictionary. Args: json: A dictionary containing ...
  * `set_viewport` **(Many-Argument Workhorses)** (Impact: 28.8)
  * `from_json` **(Defensive Guards)** (Impact: 24.1)
    * *Intent:* """Creates a UserPromptClosedParams instance from a dictionary. Args: json: A dictionary containing ...
  * `from_json` **(Defensive Guards)** (Impact: 23.8)
    * *Intent:* """Creates a NavigationInfo instance from a dictionary. Args: json: A dictionary containing the navi...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 86 instances
* *Api Near Db Sink:* 1 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 313
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 168`, `args: 58`, `func_start: 58`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 141`, `duplicate_logic: 9`
* *Architecture:* `api: 74`, `concurrency: 2`, `import: 7`
* *Defense:* `safety: 35`, `doc: 49`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.255
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.00451
  * `Imports (Out-Degree: 2):` collections.abc, dataclasses, selenium.webdriver.common.bidi.common, selenium.webdriver.common.bidi.session, threading, typing, typing_extensions
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `java/src/org/openqa/selenium/grid/node/local/LocalNode.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 813.96 | **LOC:** 1555 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 57.1%
- **Blast Radius:** changing it is visible to **19** in-repo importer(s); it depends on **114**; blast radius 0.261; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Guard Balance (formerly Safety Score) (84.9%), Concurrency Surface (formerly Concurrency) (79.8%), Complexity Load (formerly Cognitive Load) (77.5%)
- **Documentation Coverage:** 94.1667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createExternalSession` **(Many-Argument Workhorses)** (Impact: 42.8)
  * `LocalNode` **(Many-Argument Workhorses)** (Impact: 35.1)
  * `newSession` **(I/O & Config Routines)** (Impact: 30.1)
  * `stopTimedOutSession` **(Many-Argument Workhorses)** (Impact: 22.9)
  * `downloadFile` **(Defensive Guards)** (Impact: 19.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 71 instances
* *Concurrency (weighted view):* 73
* *State Mutation (weighted view):* 288
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 332`, `args: 116`, `func_start: 72`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 146`, `dead_code: 1`
* *Architecture:* `io: 30`, `api: 51`, `concurrency: 23`, `import: 114`
* *Defense:* `safety: 29`, `doc: 5`, `sync_locks: 12`, `immutability_locks: 36`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 6.2e-05 | `Ripple Effect (Closeness):` 0.00482
  * `Imports (Out-Degree: 56):` com.github.benmanes.caffeine.cache.Cache, com.github.benmanes.caffeine.cache.Caffeine, com.github.benmanes.caffeine.cache.RemovalCause, com.github.benmanes.caffeine.cache.Ticker, com.google.common.annotations.VisibleForTesting, com.google.common.net.MediaType, java.io.Closeable, java.io.File...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `javascript/selenium-webdriver/test/select_test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 809.76 | **LOC:** 283 | **CtrlFlow:** 4.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.155; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (46.9%), Guard Balance (formerly Safety Score) (27.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Concurrency (weighted view):* 98
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 105`, `args: 35`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1`
* *Architecture:* `concurrency: 78`, `import: 4`
* *Defense:* `test: 53`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.155
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` test, node:assert, selenium-webdriver, select
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `java/src/org/openqa/selenium/grid/node/kubernetes/KubernetesSessionFactory.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 775.12 | **LOC:** 1438 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **95**; blast radius 0.155; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Guard Balance (formerly Safety Score) (90.8%), Complexity Load (formerly Cognitive Load) (39.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (18.2%)
- **Documentation Coverage:** 98.3051% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `apply` **(Many-Argument Workhorses)** (Impact: 67.2)
  * `evaluatePodStatus` **(Many-Argument Workhorses)** (Impact: 46.8)
  * `buildJobSpec` **(Many-Argument Workhorses)** (Impact: 39.3)
  * `doWaitForPodRunning` **(Defensive Guards)** (Impact: 27.3)
  * `buildJobSpecFromTemplate` **(Many-Argument Workhorses)** (Impact: 23.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 68 instances
* *State Mutation (weighted view):* 277
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 177`, `structural_boundaries: 275`, `args: 68`, `func_start: 51`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 90`, `state_mutation: 141`, `unreferenced_by_name: 5`
* *Architecture:* `io: 12`, `api: 9`, `concurrency: 6`, `import: 95`
* *Defense:* `safety: 35`, `doc: 1`, `sync_locks: 1`, `immutability_locks: 29`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.155
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 35):` io.fabric8.kubernetes.api.model.Container, io.fabric8.kubernetes.api.model.ContainerBuilder, io.fabric8.kubernetes.api.model.ContainerPortBuilder, io.fabric8.kubernetes.api.model.DeletionPropagation, io.fabric8.kubernetes.api.model.EmptyDirVolumeSourceBuilder, io.fabric8.kubernetes.api.model.EnvVar, io.fabric8.kubernetes.api.model.EnvVarBuilder, io.fabric8.kubernetes.api.model.ObjectMetaBuilder...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cpp/iedriver/CommandHandlers/SendKeysCommandHandler.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 733.86 | **LOC:** 1145 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 0.155; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.7%), Debt Markers (formerly Tech Debt) (83.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SendKeysCommandHandler::ExecuteInternal` **(Many-Argument Workhorses)** (Impact: 49.2)
  * `SendKeysCommandHandler::UploadFile` **(Many-Argument Workhorses)** (Impact: 44.2)
  * `SendKeysCommandHandler::GetFileSelectionDialogCandidates` **(Many-Argument Workhorses)** (Impact: 35.0)
  * `SendKeysCommandHandler::CreateActionSequencePayload` **(Many-Argument Workhorses)** (Impact: 33.5)
  * `SendKeysCommandHandler::LegacySendKeysToFileUploadAlert` **(Many-Argument Workhorses)** (Impact: 30.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 87 instances
* *State Mutation (weighted view):* 285
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 192`, `structural_boundaries: 89`, `args: 129`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 111`, `dead_code: 1`, `planned_debt: 2`, `unreferenced_by_name: 24`
* *Architecture:* `io: 2`, `import: 15`
* *Defense:* `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.155
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` Browser.h, BrowserFactory.h, Element.h, IECommandExecutor.h, InputManager.h, StringUtilities.h, VariantUtilities.h, WindowUtilities.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `Rakefile` -> Churn: **76.82%** | Cog Load: 50.2172% | Debt: 0.0%
- `dotnet/src/webdriver/BiDi/BrowsingContext/BrowsingContextNetworkModule.cs` -> Churn: **65.67%** | Cog Load: 68.7081% | Debt: 24.608%
- `dotnet/src/webdriver/BiDi/Input/InputModule.cs` -> Churn: **65.67%** | Cog Load: 95.4372% | Debt: 99.7527%
- `dotnet/src/webdriver/BiDi/Broker.cs` -> Churn: **61.75%** | Cog Load: 93.625% | Debt: 37.5298%
- `dotnet/src/webdriver/BiDi/Input/SourceActions.cs` -> Churn: **54.95%** | Cog Load: 0.0% | Debt: 51.8374%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `dotnet/src/webdriver/BiDi/BrowsingContext/IBrowsingContextModule.cs` -> **Nikolay Borisenko** (100.0% isolated ownership) | Magnitude: 2703.16
- `javascript/atoms/test/inject_test.html` -> **Simon Mavi Stewart** (100.0% isolated ownership) | Magnitude: 1695.77
- `javascript/webdriver/test/atoms/element_test.html` -> **Simon Mavi Stewart** (100.0% isolated ownership) | Magnitude: 1500.1
- `dotnet/src/webdriver/BiDi/Network/INetworkModule.cs` -> **Nikolay Borisenko** (100.0% isolated ownership) | Magnitude: 1294.56
- `javascript/atoms/test/overflow_test.html` -> **Simon Mavi Stewart** (100.0% isolated ownership) | Magnitude: 1258.4

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `java/src/org/openqa/selenium/remote/RemoteWebDriver.java` -> **Severity: 0.053** (Bridge: 0.0007 * Flux: 78.3733%)
- `java/src/org/openqa/selenium/remote/codec/w3c/W3CHttpResponseCodec.java` -> **Severity: 0.016** (Bridge: 0.0002 * Flux: 100.0%)
- `py/selenium/webdriver/remote/webdriver.py` -> **Severity: 0.013** (Bridge: 0.0001 * Flux: 100.0%)
- `rb/lib/selenium/webdriver.rb` -> **Severity: 0.009** (Bridge: 0.0001 * Flux: 99.1837%)
- `py/selenium/webdriver/support/wait.py` -> **Severity: 0.009** (Bridge: 0.0001 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `java/src/org/openqa/selenium/internal/Require.java` -> **Severity: 10.011** (Embedded: 0.1375 * Error Risk: 72.8144%)
- `dotnet/src/webdriver/BiDi/Optional.cs` -> **Severity: 5.289** (Embedded: 0.0873 * Error Risk: 60.5532%)
- `java/src/org/openqa/selenium/Capabilities.java` -> **Severity: 5.222** (Embedded: 0.0653 * Error Risk: 80.0%)
- `dotnet/src/webdriver/Internal/Logging/Logger.cs` -> **Severity: 4.012** (Embedded: 0.0706 * Error Risk: 56.8145%)
- `java/src/org/openqa/selenium/WebDriverException.java` -> **Severity: 3.344** (Embedded: 0.0498 * Error Risk: 67.1679%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `java/src/org/openqa/selenium/internal/Require.java` -> **Severity: 5230.4** (Blast Radius: 52.304 * Doc Risk: 100.0%)
- `dotnet/src/webdriver/BiDi/Optional.cs` -> **Severity: 1757.0** (Blast Radius: 17.57 * Doc Risk: 100.0%)
- `dotnet/src/webdriver/Internal/Logging/Logger.cs` -> **Severity: 909.882** (Blast Radius: 10.312 * Doc Risk: 88.2353%)
- `py/private/pytest.bzl` -> **Severity: 606.4** (Blast Radius: 6.064 * Doc Risk: 100.0%)
- `java/test/org/openqa/selenium/testing/drivers/Browser.java` -> **Severity: 503.0** (Blast Radius: 5.03 * Doc Risk: 100.0%)

## APPENDIX A. STRUCTURAL SURFACE LEXICON (EQUATIONS & CONTEXT)
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

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with high Structural Magnitude combined with a wide Blast Radius, severe Z-Scores (Architectural Drift), or extreme spikes in individual surface vectors (like Mutation Surface or Complexity Load). Do NOT sum the surface vectors together or treat any total of them as a score -- they are independently scaled meters in different units (#3112). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
