# ARCHITECTURAL_BRIEF: selenium
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/SeleniumHQ/selenium.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |
| **Archetype Brains** | trained against engine v2.9.1 (44ffeb1e, 2026-09-19); last measured at engine 49cba5db on language-crucible@v1.7.0 |
| **Function archetypes** | **VALIDATED**, 98.4% agreement with trained state |
| **File archetypes** | **VALIDATED**, 98.7% agreement with trained state |
| **Composition (file)** | **DEGRADED**, 97.4% agreement with trained state -- engine changes since training relabelled 2.6% of crucible files (agreement 97.4%); composition_file inputs disagree with the function model's labels: never read ['Annotated & Test Methods', 'Stateful Encapsulated Methods'], never emitted ['Annotated Framework Methods', 'Tests & Verification'] -- those units drop out and those input columns are always 0.0 (retrain tracked in #4111) |
| **Composition (repo)** | **INVALID**, labels withheld -- not measurable on one corpus; inherits composition_file's measured state; composition_repo reads the composition_file brain labels by name, but none of its 20 inputs (e.g. 'Static: Literature & Documentation') is a label the composition_file brain emits (e.g. 'Annotated Framework Methods Files') -- every input column is 0.0 (retrain tracked in #4111) |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 3982 analyzed artifact(s), 326384 LOC.
- **Load-bearing artifact:** `java/src/org/openqa/selenium/internal/Require.java` -- 369 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `java/src/org/openqa/selenium/grid/node/local/LocalNode.java` -- pulls in 114 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `.npmrc` at magnitude 5000.0 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 3982 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1060 |
| Total LOC | 326384 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 79.0% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6861 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0928 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.859 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 275 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 1428 | 132413 | 35.9% |
| CSHARP | 669 | 45116 | 16.8% |
| PYTHON | 351 | 28434 | 8.8% |
| HTML | 336 | 24160 | 8.4% |
| RUBY | 319 | 21170 | 8.0% |
| JAVASCRIPT | 256 | 32739 | 6.4% |
| CPP | 249 | 25780 | 6.3% |
| PLAINTEXT | 131 | 3 | 3.3% |
| TYPESCRIPT | 63 | 4697 | 1.6% |
| YAML | 36 | 2935 | 0.9% |
| RUST | 36 | 6791 | 0.9% |
| MARKDOWN | 31 | 0 | 0.8% |
| XML | 29 | 9 | 0.7% |
| SHELL | 20 | 418 | 0.5% |
| JSON | 16 | 662 | 0.4% |
| POWERSHELL | 3 | 251 | 0.1% |
| DOCKERFILE | 3 | 128 | 0.1% |
| CSS | 2 | 27 | 0.1% |
| BATCH | 2 | 56 | 0.1% |
| MAKEFILE | 1 | 9 | 0.0% |
| C | 1 | 586 | 0.0% |

## 4.1 SOURCE ENCODINGS
> 2 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 3970 |
| utf-8 | bom | 6 |
| unknown | unknown | 3 |
| cp1252 | cp1252-fallback | 1 |
| latin-1 | latin-1-fallback | 1 |
| utf-16-le | bom | 1 |

> 1 guessed file(s) read as double-byte text that decodes strictly as gbk: if that is the estate's code page, rescan with `--source-encoding gbk` (or the right one of those). E.g. `common/src/web/cn-test.html`.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 24%, Declarative / Non-Code 19%, State Mutators Files 9%, Large Core Modules (3) 9%, Large Core Modules (2) 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 3811 | 95.7% |
| Unknown | 3 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 159 | 4.0% |
| Static: Minified & Vendor Opaque Mass | 9 | 0.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1060*

**Composition by Extension & Reason:**
- `.js`: 237x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 58 LOC), 1x Excluded (Machine-Generated Source Code Signature: 35 LOC)
- `.bazel`: 150x Excluded (Unsupported Extension: '.bazel'), 65x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rbs`: 200x Excluded (Unsupported Extension: '.rbs')
- `.css`: 54x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 31x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable), 2x Unsupported Format (.bazelproject)
- `.cs`: 33x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Packed Payload Guard (Impossible Density: 3.78 hits/line)
- `.java`: 32x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 31x Excluded (Explicitly Denied Extension: '.png')
- `.xml`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jpg`: 11x Excluded (Explicitly Denied Extension: '.jpg')
- `.json`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 17193 LOC), 1x Excluded (Massive Static Asset Blob: 3476 LOC)
- `.inl`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.h`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.hbs`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.iml`: 5x Excluded (Unsupported Extension: '.iml'), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 13.7 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 95.3 | 36.1 | 48.4 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 14.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 4.4 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 13.4 | 5.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 9.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 29.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.0 | 0.4 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 6.9 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 56.7 | 93.3 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 71.7 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 2671 | 687 | 1 | `cpp/iedriver/IECommandExecutor.cpp` |
| cleanup | 521 | 237 | 0 | `py/test/selenium/webdriver/common/bidi_browsing_context_tests.py` |
| guards | 22498 | 2259 | 15 | `java/src/org/openqa/selenium/support/ui/ExpectedConditions.java` |
| danger | 9541 | 1599 | 6 | `java/test/org/openqa/selenium/grid/node/kubernetes/InheritedPodSpecTest.java` |
| concurrency | 8609 | 566 | 3 | `javascript/selenium-webdriver/test/bidi/script_test.js` |
| connectivity | 20679 | 2833 | 13 | `java/src/org/openqa/selenium/support/ui/ExpectedConditions.java` |
| io | 7643 | 806 | 3 | `common/src/web/macbeth.html` |
| crypto | 6 | 6 | 0 | `py/selenium/webdriver/remote/shadowroot.py` |
| ipc | 105 | 48 | 0 | `py/selenium/webdriver/common/service.py` |
| time | 2214 | 413 | 1 | `java/test/org/openqa/selenium/grid/distributor/local/LocalDistributorTest.java` |
| serialization | 334 | 171 | 0 | `dotnet/src/webdriver/BiDi/Json/Converters/Polymorphic/RemoteValueConverter.cs` |
| regex | 384 | 162 | 0 | `java/test/org/openqa/selenium/grid/data/DefaultSlotMatcherTest.java` |
| events | 1875 | 381 | 0 | `py/test/unit/selenium/webdriver/remote/error_handler_tests.py` |
| tests | 25403 | 936 | 19 | `java/test/org/openqa/selenium/support/ui/ExpectedConditionsTest.java` |
| docs | 18546 | 1405 | 10 | `dotnet/src/support/Events/EventFiringWebDriver.cs` |
| debt | 1206 | 389 | 0 | `cpp/linux-specific/print_events.h` |
| mutation | 77483 | 2922 | 53 | `common/src/web/macbeth.html` |
| dead_code | 10019 | 1454 | 7 | `dotnet/test/webdriver/ElementFindingTests.cs` |
| credential | 84 | 17 | 0 | `rb/spec/integration/selenium/webdriver/virtual_authenticator_spec.rb` |
| threat | 19 | 9 | 0 | `common/src/web/simpleTest.html` |
| ml_ai | 143 | 62 | 0 | `java/src/org/openqa/selenium/grid/node/config/NodeOptions.java` |
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

1. **Require.java** (`java/src/org/openqa/selenium/internal/Require.java`) — 369 inbound connections
2. **Capabilities.java** (`java/src/org/openqa/selenium/Capabilities.java`) — 189 inbound connections
3. **Json.java** (`java/src/org/openqa/selenium/json/Json.java`) — 185 inbound connections
4. **HttpResponse.java** (`java/src/org/openqa/selenium/remote/http/HttpResponse.java`) — 181 inbound connections
5. **HttpRequest.java** (`java/src/org/openqa/selenium/remote/http/HttpRequest.java`) — 166 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **LocalNode.java** (`java/src/org/openqa/selenium/grid/node/local/LocalNode.java`) — 114 outbound dependencies
2. **KubernetesSessionFactory.java** (`java/src/org/openqa/selenium/grid/node/kubernetes/KubernetesSessionFactory.java`) — 95 outbound dependencies
3. **lib.rs** (`rust/src/lib.rs`) — 89 outbound dependencies
4. **RemoteWebDriver.java** (`java/src/org/openqa/selenium/remote/RemoteWebDriver.java`) — 87 outbound dependencies
5. **AbstractHttpCommandCodec.java** (`java/src/org/openqa/selenium/remote/codec/AbstractHttpCommandCodec.java`) — 86 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `sendKeys` **(Many-Argument Workhorses)** (@ `cpp/webdriver-interactions/interactions.cpp`) -> Impact: **256.9** | LOC: 258
- `InputManager::GetKeyInfo` **(Many-Argument Workhorses)** (@ `cpp/iedriver/InputManager.cpp`) -> Impact: **231.7** | LOC: 304
- `NewSessionCommandHandler::ValidateCapabilities` **(Many-Argument Workhorses)** (@ `cpp/iedriver/CommandHandlers/NewSessionCommandHandler.cpp`) -> Impact: **189.4** | LOC: 348
- `parse` **(Many-Argument Workhorses)** (@ `common/devtools/pdl.py`) -> Impact: **184.2** | LOC: 123
- `print_event` **(Many-Argument Workhorses)** (@ `cpp/linux-specific/print_events.h`) -> Impact: **147.1** | LOC: 141
- `InputManager::AddKeyboardInput` **(Many-Argument Workhorses)** (@ `cpp/iedriver/InputManager.cpp`) -> Impact: **138.3** | LOC: 261
- `uncompress` **(Many-Argument Workhorses)** (@ `rust/src/files.rs`) -> Impact: **117.7** | LOC: 78
- `appendVisibleTextLinesFromTextNode_` **(Many-Argument Workhorses)** (@ `javascript/atoms/dom.js`) -> Impact: **108.0** | LOC: 281
  * *Intent:* /** */
- `CookieWndProc` **(Many-Argument Workhorses)** (@ `cpp/iedriver/CookieManager.cpp`) -> Impact: **100.8** | LOC: 256
- `RunCommandAsync` **(Many-Argument Workhorses)** (@ `dotnet/src/webdriver/Manager/SeleniumManager.cs`) -> Impact: **100.6** | LOC: 252

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `cpp/iedriver` | 72 | 9295.98 | 18.66% | 33.98% |
| `py/test/selenium/webdriver/common` | 71 | 6746.5 | 22.65% | 0.0% |
| `javascript/atoms/test` | 53 | 6527.0 | 10.65% | 0.0% |
| `__monolith__` | 19 | 5333.6 | 6.11% | 0.0% |
| `javascript/grid-ui` | 9 | 5109.36 | 0.57% | 0.0% |
| `common/extensions/webextensions-selenium-example-signed/META-INF` | 1 | 5000.0 | 0.0% | 0.0% |
| `dotnet/test/webdriver` | 64 | 4908.82 | 5.37% | 0.0% |
| `dotnet/src/webdriver` | 128 | 4791.78 | 5.79% | 19.46% |
| `rust/src` | 19 | 4382.29 | 13.64% | 0.58% |
| `cpp/iedriver/CommandHandlers` | 117 | 4206.58 | 9.99% | 45.51% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `rb/lib/selenium/webdriver/bidi/browsing_context.rb` -> **100.0%** Exposure
- `javascript/selenium-webdriver/lib/error.js` -> **100.0%** Exposure
- `cpp/iedriver/HtmlDialog.cpp` -> **100.0%** Exposure
- `dotnet/src/webdriver/DevTools/JavaScript.cs` -> **100.0%** Exposure
- `dotnet/src/webdriver/DevTools/Network.cs` -> **100.0%** Exposure
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
- `rb/lib/selenium/webdriver/remote/bridge.rb` -> **76** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `py/test/unit/selenium/webdriver/remote/remote_connection_tests.py` -> **71.6928%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `21` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `20158` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.131
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `common/extensions/webextensions-selenium-example-signed/META-INF/cose.sig` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.131
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `javascript/grid-ui/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.131
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cpp/iedriver/InputManager.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.633)
- **Top Global Matches:** file_cluster_6: 5.633, file_cluster_4: 12.239, file_cluster_8: 12.5
- **Magnitude:** 1682.12 | **LOC:** 1399 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **19**; blast radius 0.135; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.2%), Guard Balance (formerly Safety Score) (82.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `InputManager::GetKeyInfo` **(Many-Argument Workhorses)** (Impact: 231.7)
  * `InputManager::AddKeyboardInput` **(Many-Argument Workhorses)** (Impact: 138.3)
  * `InputManager::PointerMoveTo` **(Many-Argument Workhorses)** (Impact: 95.2)
  * `InputManager::PerformInputSequence` **(Many-Argument Workhorses)** (Impact: 39.3)
  * `InputManager::GetTicks` **(Compute Cores)** (Impact: 37.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 272 instances
* *State Mutation (weighted view):* 959
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 324`, `structural_boundaries: 49`, `args: 108`, `func_start: 26`
* *Risk/State:* `state_mutation: 415`, `dead_code: 6`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 26`
* *Architecture:* `import: 19`
* *Defense:* `sync_locks: 5`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.135
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000251
  * `Imports (Out-Degree: 17):` JavaScriptActionSimulator.h, SendInputActionSimulator.h, SendMessageActionSimulator.h, DocumentHost.h, Element.h, atoms.h, HookProcessor.h, IElementManager.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `javascript/selenium-webdriver/test/bidi/script_test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.748)
- **Top Global Matches:** file_cluster_10: 6.748, file_cluster_12: 8.045, file_cluster_2: 8.949
- **Magnitude:** 1669.88 | **LOC:** 830 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.131; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (40.5%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.131
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` test, node:assert, selenium-webdriver, argumentValue, browsingContext, evaluateResult, protocolValue, realmInfo...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rust/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 5.715)
- **Top Global Matches:** file_cluster_0: 5.715, file_cluster_2: 6.079, file_cluster_17: 6.178
- **Magnitude:** 1656.93 | **LOC:** 1758 | **CtrlFlow:** 0.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **89**; blast radius 4.268; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (49.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (22.1%), Mutation Surface (formerly State Flux) (12.3%), Connectivity (formerly Api Exposure) (11.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 38
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 258`, `args: 163`, `func_start: 147`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 36`
* *Architecture:* `io: 1`, `api: 68`, `concurrency: 1`, `import: 32`
* *Defense:* `safety: 32`, `sync_locks: 11`, `immutability_locks: 43`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.268
  * `Choke Point (Betweenness):` 2.4e-05 | `Ripple Effect (Closeness):` 0.004143
  * `Imports (Out-Degree: 17):` chrome, config, downloads, edge, electron, files, firefox, grid...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `javascript/atoms/test/inject_test.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.322)
- **Top Global Matches:** file_cluster_12: 7.322, file_cluster_7: 7.887, file_cluster_10: 8.022
- **Magnitude:** 1358.72 | **LOC:** 568 | **CtrlFlow:** 2.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.131; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (34.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (12.0%), Complexity Load (formerly Cognitive Load) (5.5%), Connectivity (formerly Api Exposure) (4.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Concurrency (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 97`, `args: 70`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 13`, `planned_debt: 4`
* *Architecture:* `io: 6`, `api: 3`, `concurrency: 13`, `import: 12`
* *Defense:* `safety: 21`, `doc: 1`, `test: 150`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.131
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` qunit.css, qunit.js, qunit_test_runner.js, test_bootstrap.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `javascript/selenium-webdriver/lib/webdriver.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.011)
- **Top Global Matches:** file_cluster_15: 8.011, file_cluster_10: 8.039, file_cluster_12: 8.193
- **Magnitude:** 1358.52 | **LOC:** 3402 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **18** in-repo importer(s); it depends on **22**; blast radius 0.944; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (98.6%), Connectivity (formerly Api Exposure) (78.4%), Complexity Load (formerly Cognitive Load) (49.4%)
- **Documentation Coverage:** 16.6078% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `wait` **(Defensive Guards)** (Impact: 45.6)
  * `getWsUrl` **(Defensive Guards)** (Impact: 25.4)
    * *Intent:* /** * Retrieves 'webSocketDebuggerUrl' by sending a http request using debugger address */
  * `createCDPConnection` **(Defensive Guards)** (Impact: 21.3)
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
* *Structure:* `branch: 181`, `structural_boundaries: 355`, `args: 241`, `func_start: 194`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 128`, `duplicate_logic: 8`
* *Architecture:* `io: 10`, `api: 72`, `concurrency: 142`, `import: 24`
* *Defense:* `safety: 156`, `doc: 216`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.944
  * `Choke Point (Betweenness):` 0.00011 | `Ripple Effect (Closeness):` 0.010985
  * `Imports (Out-Degree: 19):` bidi, CDPConnection, index, by, capabilities, command, error, dialog...
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `dotnet/src/webdriver/BiDi/Network/INetworkModule.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 9.528)
- **Top Global Matches:** file_cluster_0: 9.528, file_cluster_13: 13.95, file_cluster_2: 14.029
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.131
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `javascript/atoms/test/overflow_test.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.436)
- **Top Global Matches:** file_cluster_10: 5.436, file_cluster_13: 6.01, file_cluster_2: 6.786
- **Magnitude:** 1197.72 | **LOC:** 563 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.131; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (53.8%), Complexity Load (formerly Cognitive Load) (11.5%), Connectivity (formerly Api Exposure) (11.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (6.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 121`, `args: 30`, `func_start: 6`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 5`, `state_mutation: 35`
* *Architecture:* `io: 6`, `api: 32`, `import: 6`
* *Defense:* `doc: 1`, `test: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.131
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` qunit.css, qunit.js, qunit_test_runner.js, test_bootstrap.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cpp/iedriver/Element.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.79)
- **Top Global Matches:** file_cluster_4: 6.79, file_cluster_6: 7.018, file_cluster_15: 14.392
- **Magnitude:** 1161.24 | **LOC:** 1880 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **11**; blast radius 0.174; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (89.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (68.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Element::IsObscured` **(Many-Argument Workhorses)** (Impact: 97.3)
  * `Element::GetLocation` **(Many-Argument Workhorses)** (Impact: 52.6)
  * `Element::AppendFrameDetails` **(Compute Cores)** (Impact: 43.0)
  * `Element::IsImageMap` **(Compute Cores)** (Impact: 36.7)
  * `Element::GetClickableViewPortLocation` **(Many-Argument Workhorses)** (Impact: 33.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 160 instances
* *State Mutation (weighted view):* 554
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 275`, `structural_boundaries: 134`, `args: 158`, `func_start: 40`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 234`, `dead_code: 6`, `planned_debt: 4`, `fragile_debt: 3`, `unreferenced_by_name: 38`
* *Architecture:* `import: 11`
* *Defense:* `safety: 4`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.174
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.000564
  * `Imports (Out-Degree: 9):` Browser.h, Element.h, atoms.h, Script.h, StringUtilities.h, VariantUtilities.h, WebDriverConstants.h, algorithm...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `cpp/webdriver-interactions/interactions.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.583)
- **Top Global Matches:** file_cluster_15: 6.583, file_cluster_4: 7.363, file_cluster_16: 8.272
- **Magnitude:** 1086.02 | **LOC:** 887 | **CtrlFlow:** 29.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.131; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.7%), Guard Balance (formerly Safety Score) (83.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sendKeys` **(Many-Argument Workhorses)** (Impact: 256.9)
  * `backgroundKeyDown` **(Many-Argument Workhorses)** (Impact: 30.7)
  * `backgroundKeyUp` **(Many-Argument Workhorses)** (Impact: 21.3)
  * `fillEventData` **(Many-Argument Workhorses)** (Impact: 19.0)
  * `mouseUpAt` **(Many-Argument Workhorses)** (Impact: 17.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 183 instances
* *State Mutation (weighted view):* 553
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 198`, `structural_boundaries: 50`, `args: 60`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `state_mutation: 187`, `planned_debt: 1`, `unreferenced_by_name: 4`
* *Architecture:* `import: 8`
* *Defense:* `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.131
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` ctime, event_firing_thread.h, interactions.h, interactions_common.h, iostream, logging.h, stdafx.h, string
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `javascript/atoms/dom.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 12.157)
- **Top Global Matches:** file_cluster_6: 12.157, file_cluster_4: 15.485, file_cluster_8: 18.146
- **Magnitude:** 998.78 | **LOC:** 1448 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.131; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (33.2%)
- **Documentation Coverage:** 12.1366% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `appendVisibleTextLinesFromTextNode_` **(Many-Argument Workhorses)** (Impact: 108.0)
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
* *Amplified Cascading Flux:* 71 instances
* *State Mutation (weighted view):* 240
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 256`, `structural_boundaries: 216`, `args: 56`, `func_start: 43`
* *Risk/State:* `safety_bypasses: 81`, `state_mutation: 98`, `planned_debt: 9`, `unreferenced_by_name: 5`
* *Architecture:* `import: 16`
* *Defense:* `safety: 19`, `doc: 63`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.131
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` bot, bot.color, bot.dom.core, bot.locators.css, bot.userAgent, goog.array, goog.dom, goog.dom.DomHelper...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `py/selenium/webdriver/remote/webdriver.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.007)
- **Top Global Matches:** file_cluster_5: 6.007, file_cluster_12: 9.168, file_cluster_0: 10.399
- **Magnitude:** 950.12 | **LOC:** 1571 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **53**; blast radius 1.036; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (73.4%), Guard Balance (formerly Safety Score) (70.3%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.036
  * `Choke Point (Betweenness):` 0.000147 | `Ripple Effect (Closeness):` 0.006724
  * `Imports (Out-Degree: 37):` abc, base64, contextlib, copy, importlib, json, os, pkgutil...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `cpp/iedriver/IECommandExecutor.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.225)
- **Top Global Matches:** file_cluster_4: 5.225, file_cluster_15: 9.357, file_cluster_16: 10.629
- **Magnitude:** 853.92 | **LOC:** 1720 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **28**; blast radius 0.131; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.1%), Debt Markers (formerly Tech Debt) (94.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `IECommandExecutor::OnAfterNewWindow` **(Many-Argument Workhorses)** (Impact: 57.0)
  * `IECommandExecutor::HandleUnexpectedAlert` **(Many-Argument Workhorses)** (Impact: 42.6)
  * `IECommandExecutor::OpenNewBrowserTab` **(Compute Cores)** (Impact: 38.6)
  * `IECommandExecutor::OnScriptWait` **(Many-Argument Workhorses)** (Impact: 37.3)
  * `IECommandExecutor::DispatchCommand` **(I/O & Config Routines)** (Impact: 35.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 65 instances
* *State Mutation (weighted view):* 265
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 209`, `structural_boundaries: 101`, `args: 214`, `func_start: 55`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 135`, `dead_code: 1`, `fragile_debt: 1`, `unreferenced_by_name: 48`
* *Architecture:* `concurrency: 2`, `import: 28`
* *Defense:* `safety: 1`, `sync_locks: 6`, `immutability_locks: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.131
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 32):` Alert.h, Browser.h, BrowserFactory.h, CommandExecutor.h, CommandHandlerRepository.h, CookieManager.h, Element.h, ElementFinder.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cpp/iedriver/BrowserFactory.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.52)
- **Top Global Matches:** file_cluster_4: 5.52, file_cluster_15: 10.083, file_cluster_9: 10.791
- **Magnitude:** 821.38 | **LOC:** 1594 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **14**; blast radius 0.135; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Debt Markers (formerly Tech Debt) (92.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `BrowserFactory::AttachToBrowserUsingActiveAccessibility` **(Many-Argument Workhorses)** (Impact: 46.3)
  * `BrowserFactory::AttachToBrowserUsingShellWindows` **(Many-Argument Workhorses)** (Impact: 38.9)
  * `BrowserFactory::LaunchBrowserProcess` **(Compute Cores)** (Impact: 34.0)
  * `BrowserFactory::GetZoomLevel` **(Many-Argument Workhorses)** (Impact: 30.2)
  * `BrowserFactory::InvokeClearCacheUtility` **(Compute Cores)** (Impact: 26.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 91 instances
* *State Mutation (weighted view):* 308
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 235`, `structural_boundaries: 114`, `args: 185`, `func_start: 42`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 126`, `fragile_debt: 2`, `unreferenced_by_name: 38`
* *Architecture:* `import: 14`
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.135
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000251
  * `Imports (Out-Degree: 7):` BrowserFactory.h, FileUtilities.h, RegistryUtilities.h, StringUtilities.h, WebDriverConstants.h, ctime, exdispid.h, iepmapi.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `py/selenium/webdriver/common/bidi/browsing_context.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.291)
- **Top Global Matches:** file_cluster_5: 8.291, file_cluster_12: 8.805, file_cluster_0: 9.779
- **Magnitude:** 819.7 | **LOC:** 1061 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **7**; blast radius 0.219; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (76.7%), Debt Markers (formerly Tech Debt) (75.0%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.219
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.004994
  * `Imports (Out-Degree: 2):` collections.abc, dataclasses, selenium.webdriver.common.bidi.common, selenium.webdriver.common.bidi.session, threading, typing, typing_extensions
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `javascript/selenium-webdriver/test/select_test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.409)
- **Top Global Matches:** file_cluster_10: 6.409, file_cluster_12: 7.838, file_cluster_2: 8.847
- **Magnitude:** 809.76 | **LOC:** 283 | **CtrlFlow:** 4.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.131; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (46.9%), Guard Balance (formerly Safety Score) (40.9%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.131
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` test, node:assert, selenium-webdriver, select
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `java/src/org/openqa/selenium/support/ui/ExpectedConditions.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.631)
- **Top Global Matches:** file_cluster_5: 6.631, file_cluster_7: 9.558, file_cluster_12: 9.997
- **Magnitude:** 787.32 | **LOC:** 1855 | **CtrlFlow:** 4.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **40** in-repo importer(s); it depends on **21**; blast radius 0.952; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (92.5%), Connectivity (formerly Api Exposure) (74.0%), Guard Balance (formerly Safety Score) (73.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (35.3%)
- **Documentation Coverage:** 58.7838% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `or` **(Defensive Guards)** (Impact: 10.8)
    * *Intent:* /** * An expectation with the logical or condition of the given list of conditions. * * <p>Each cond...
  * `apply` **(Defensive Guards)** (Impact: 8.4)
  * `elementToBeClickable` **(Stateful Encapsulated Methods)** (Impact: 7.2)
    * *Intent:* /** * An expectation for checking an element is visible and enabled such that you can click it. * * ...
  * `elementToBeClickable` **(Stateful Encapsulated Methods)** (Impact: 7.1)
    * *Intent:* /** * An expectation for checking an element is visible and enabled such that you can click it. * * ...
  * `apply` **(Generic / Templated Code)** (Impact: 6.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 43 instances
* *Api Near Db Sink:* 2 instances
* *State Mutation (weighted view):* 198
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 305`, `args: 165`, `func_start: 151`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 107`, `state_mutation: 112`, `planned_debt: 2`
* *Architecture:* `api: 165`, `import: 21`
* *Defense:* `safety: 60`, `doc: 56`, `sync_locks: 15`, `immutability_locks: 91`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.952
  * `Choke Point (Betweenness):` 3.5e-05 | `Ripple Effect (Closeness):` 0.010263
  * `Imports (Out-Degree: 13):` java.lang.System.lineSeparator, java.util.Collection, java.util.List, java.util.Objects.requireNonNullElse, java.util.Optional, java.util.logging.Level, java.util.logging.Logger, java.util.regex.Pattern...
  * `Imported By (In-Degree: 40):` (Excluded from Brief to save tokens)

### `java/src/org/openqa/selenium/grid/node/local/LocalNode.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.164)
- **Top Global Matches:** file_cluster_5: 7.164, file_cluster_12: 7.457, file_cluster_7: 9.996
- **Magnitude:** 722.06 | **LOC:** 1555 | **CtrlFlow:** 6.6% | **Authorship Centralization:** 57.1%
- **Blast Radius:** changing it is visible to **25** in-repo importer(s); it depends on **114**; blast radius 0.251; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Concurrency Surface (formerly Concurrency) (79.8%), Complexity Load (formerly Cognitive Load) (70.7%), Guard Balance (formerly Safety Score) (63.5%)
- **Documentation Coverage:** 94.1667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `newSession` **(I/O & Config Routines)** (Impact: 27.1)
  * `LocalNode` **(Many-Argument Workhorses)** (Impact: 26.4)
  * `createExternalSession` **(Many-Argument Workhorses)** (Impact: 23.2)
  * `stopTimedOutSession` **(Many-Argument Workhorses)** (Impact: 18.9)
  * `downloadFile` **(Defensive Guards)** (Impact: 14.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 64 instances
* *Concurrency (weighted view):* 73
* *State Mutation (weighted view):* 274
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 332`, `args: 116`, `func_start: 72`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 146`
* *Architecture:* `io: 30`, `api: 51`, `concurrency: 23`, `import: 114`
* *Defense:* `safety: 29`, `doc: 5`, `sync_locks: 12`, `immutability_locks: 36`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.000208 | `Ripple Effect (Closeness):` 0.005655
  * `Imports (Out-Degree: 62):` com.github.benmanes.caffeine.cache.Cache, com.github.benmanes.caffeine.cache.Caffeine, com.github.benmanes.caffeine.cache.RemovalCause, com.github.benmanes.caffeine.cache.Ticker, com.google.common.annotations.VisibleForTesting, com.google.common.net.MediaType, java.io.Closeable, java.io.File...
  * `Imported By (In-Degree: 25):` (Excluded from Brief to save tokens)

### `cpp/iedriver/CommandHandlers/SendKeysCommandHandler.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.495)
- **Top Global Matches:** file_cluster_6: 5.495, file_cluster_4: 9.142, file_cluster_8: 15.905
- **Magnitude:** 693.76 | **LOC:** 1145 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 0.131; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (82.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SendKeysCommandHandler::ExecuteInternal` **(Many-Argument Workhorses)** (Impact: 49.2)
  * `SendKeysCommandHandler::UploadFile` **(Many-Argument Workhorses)** (Impact: 44.2)
  * `SendKeysCommandHandler::CreateActionSequencePayload` **(Many-Argument Workhorses)** (Impact: 33.5)
  * `SendKeysCommandHandler::GetFileSelectionDialogCandidates` **(Many-Argument Workhorses)** (Impact: 33.0)
  * `SendKeysCommandHandler::LegacySendKeysToFileUploadAlert` **(Many-Argument Workhorses)** (Impact: 30.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 81 instances
* *State Mutation (weighted view):* 273
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 176`, `structural_boundaries: 89`, `args: 129`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 111`, `planned_debt: 2`, `unreferenced_by_name: 24`
* *Architecture:* `io: 2`, `import: 15`
* *Defense:* `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.131
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` Browser.h, BrowserFactory.h, Element.h, IECommandExecutor.h, InputManager.h, StringUtilities.h, VariantUtilities.h, WindowUtilities.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `javascript/atoms/test/html5/storage_test.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.053)
- **Top Global Matches:** file_cluster_10: 4.053, file_cluster_2: 5.584, file_cluster_13: 6.488
- **Magnitude:** 690.09 | **LOC:** 233 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.131; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (41.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (12.0%), Complexity Load (formerly Cognitive Load) (5.5%), Connectivity (formerly Api Exposure) (4.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 35`, `args: 12`, `func_start: 5`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `io: 13`, `api: 2`, `import: 6`
* *Defense:* `safety: 1`, `doc: 1`, `test: 47`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.131
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` test_bootstrap.js, qunit.css, qunit.js, qunit_test_runner.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cpp/iedriver/CommandHandlers/NewSessionCommandHandler.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.63)
- **Top Global Matches:** file_cluster_4: 6.63, file_cluster_6: 8.712, file_cluster_9: 12.391
- **Magnitude:** 676.1 | **LOC:** 1046 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.131; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (69.3%), Guard Balance (formerly Safety Score) (62.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `NewSessionCommandHandler::ValidateCapabilities` **(Many-Argument Workhorses)** (Impact: 189.4)
  * `NewSessionCommandHandler::ValidateArguments` **(Many-Argument Workhorses)** (Impact: 35.6)
  * `NewSessionCommandHandler::MatchCapabilities` **(Many-Argument Workhorses)** (Impact: 28.8)
  * `NewSessionCommandHandler::ProcessCapabilities` **(Many-Argument Workhorses)** (Impact: 19.6)
  * `NewSessionCommandHandler::SetProxySettings` **(Many-Argument Workhorses)** (Impact: 16.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 61 instances
* *State Mutation (weighted view):* 243
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 178`, `structural_boundaries: 71`, `args: 82`, `func_start: 19`
* *Risk/State:* `state_mutation: 121`, `planned_debt: 2`, `unreferenced_by_name: 19`
* *Architecture:* `import: 10`
* *Defense:* `immutability_locks: 33`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.131
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` Alert.h, Browser.h, BrowserFactory.h, IECommandExecutor.h, InputManager.h, ProxyManager.h, WebDriverConstants.h, NewSessionCommandHandler.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `java/src/org/openqa/selenium/grid/node/kubernetes/KubernetesSessionFactory.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.36)
- **Top Global Matches:** file_cluster_5: 6.36, file_cluster_12: 8.668, file_cluster_7: 9.103
- **Magnitude:** 645.12 | **LOC:** 1438 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **95**; blast radius 0.167; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Guard Balance (formerly Safety Score) (67.6%), Complexity Load (formerly Cognitive Load) (32.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (18.2%)
- **Documentation Coverage:** 98.3051% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `buildJobSpec` **(Many-Argument Workhorses)** (Impact: 37.5)
  * `evaluatePodStatus` **(Many-Argument Workhorses)** (Impact: 28.8)
  * `apply` **(Many-Argument Workhorses)** (Impact: 25.6)
  * `buildJobSpecFromTemplate` **(Many-Argument Workhorses)** (Impact: 23.3)
  * `doWaitForPodRunning` **(Defensive Guards)** (Impact: 14.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 60 instances
* *State Mutation (weighted view):* 261
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 275`, `args: 68`, `func_start: 51`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 90`, `state_mutation: 141`, `unreferenced_by_name: 5`
* *Architecture:* `io: 12`, `api: 9`, `concurrency: 6`, `import: 95`
* *Defense:* `safety: 35`, `doc: 1`, `sync_locks: 1`, `immutability_locks: 29`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.167
  * `Choke Point (Betweenness):` 3.1e-05 | `Ripple Effect (Closeness):` 0.000669
  * `Imports (Out-Degree: 36):` io.fabric8.kubernetes.api.model.Container, io.fabric8.kubernetes.api.model.ContainerBuilder, io.fabric8.kubernetes.api.model.ContainerPortBuilder, io.fabric8.kubernetes.api.model.DeletionPropagation, io.fabric8.kubernetes.api.model.EmptyDirVolumeSourceBuilder, io.fabric8.kubernetes.api.model.EnvVar, io.fabric8.kubernetes.api.model.EnvVarBuilder, io.fabric8.kubernetes.api.model.ObjectMetaBuilder...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `py/conftest.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.425)
- **Top Global Matches:** file_cluster_12: 6.425, file_cluster_7: 9.409, file_cluster_15: 9.629
- **Magnitude:** 641.5 | **LOC:** 707 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 62.5%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **19**; blast radius 0.252; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.7%), Guard Balance (formerly Safety Score) (73.2%)
- **Documentation Coverage:** 43.5345% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `driver` **(Many-Argument Workhorses)** (Impact: 41.9)
  * `options` **(Stateful Encapsulated Methods)** (Impact: 23.9)
  * `clean_driver` **(Defensive Guards)** (Impact: 11.2)
  * `pytest_ignore_collect` **(Type Conversions)** (Impact: 10.8)
  * `server` **(Compute Cores)** (Impact: 10.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 88 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 294
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 154`, `args: 53`, `func_start: 53`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 118`
* *Architecture:* `io: 6`, `api: 58`, `concurrency: 2`, `import: 19`
* *Defense:* `safety: 12`, `doc: 7`, `test: 39`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.252
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.000753
  * `Imports (Out-Degree: 7):` dataclasses, http.server, os, pathlib, pytest, python.runfiles, rich.console, rich.traceback...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `java/test/org/openqa/selenium/grid/distributor/selector/DefaultSlotSelectorTest.java` (JAVA) | Magnitude: 63.1 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 212, structural_boundaries: 98, core_var_decl: 65, import: 40
- `java/src/org/openqa/selenium/bidi/webextension/ExtensionArchivePath.java` (JAVA) | Magnitude: 7.04 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 5, api: 3, func_start: 2
- `java/src/org/openqa/selenium/bidi/webextension/ExtensionBase64Encoded.java` (JAVA) | Magnitude: 7.04 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 5, api: 3, func_start: 2
- `java/src/org/openqa/selenium/bidi/webextension/ExtensionPath.java` (JAVA) | Magnitude: 7.04 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 5, api: 3, func_start: 2
- `java/src/org/openqa/selenium/bidi/script/DateLocalValue.java` (JAVA) | Magnitude: 6.04 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 5, func_start: 2, api: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `java/test/org/openqa/selenium/grid/distributor/SessionSchedulingTest.java` (JAVA) | Magnitude: 77.68 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 250, structural_boundaries: 80, core_var_decl: 56, design_snake_case: 41
- `javascript/selenium-webdriver/test/firefox/options_test.js` (JAVASCRIPT) | Magnitude: 159.04 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 120, structural_boundaries: 44, concurrency: 33, core_var_decl: 28
- `java/src/org/openqa/selenium/grid/commands/CompletionCommand.java` (JAVA) | Magnitude: 69.96 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 155, structural_boundaries: 49, args: 20, branch: 19
- `javascript/chrome-driver/test/atoms_test.html` (HTML) | Magnitude: 38.4 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 161, test: 36, core_var_decl: 36, design_snake_case: 36
- `dotnet/test/webdriver/ProxyTests.cs` (CSHARP) | Magnitude: 71.94 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 212, test: 117, state_mutation: 36, args: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `javascript/selenium-webdriver/bidi/external/permissions.js` (JAVASCRIPT) | Magnitude: 0.05 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 7, concurrency: 7, args: 4
- `rb/lib/selenium/webdriver/firefox/driver.rb` (RUBY) | Magnitude: 6.08 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 8, class_start: 4, func_start: 2
- `cpp/iedriver/CommandHandlers/IsElementEnabledCommandHandler.cpp` (CPP) | Magnitude: 23.6 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 27, pointers: 10, structural_boundaries: 8, branch: 7
- `cpp/iedriver/CommandHandlers/IsElementSelectedCommandHandler.cpp` (CPP) | Magnitude: 23.62 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 28, pointers: 10, structural_boundaries: 8, branch: 7
- `rb/lib/selenium/webdriver/remote/http/common.rb` (RUBY) | Magnitude: 111.24 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 105, structural_boundaries: 26, branch: 24, state_mutation: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `common/src/web/javascriptPage.html` (HTML) | Magnitude: 119.56 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 182, core_var_decl: 117, design_snake_case: 114, reflection_metaprogramming: 83
- `java/src/org/openqa/selenium/grid/sessionqueue/httpd/NewSessionQueueServer.java` (JAVA) | Magnitude: 33.28 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 84, structural_boundaries: 48, import: 26, args: 15
- `dotnet/src/webdriver/NetworkManager.cs` (CSHARP) | Magnitude: 160.48 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 158, doc: 46, structural_boundaries: 27, branch: 25
- `java/test/org/openqa/selenium/grid/router/SessionCleanUpTest.java` (JAVA) | Magnitude: 57.82 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 256, structural_boundaries: 151, import: 72, core_var_decl: 44
- `java/test/org/openqa/selenium/net/UrlCheckerTest.java` (JAVA) | Magnitude: 20.38 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 57, structural_boundaries: 32, import: 14, args: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `java/src/org/openqa/selenium/bidi/browsingcontext/ClipRectangle.java` (JAVA) | Magnitude: 14.36 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 7, func_start: 6, args: 5
- `java/src/org/openqa/selenium/json/ObjectCoercer.java` (JAVA) | Magnitude: 39.36 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 21, branch: 8, state_mutation: 6
- `java/src/org/openqa/selenium/support/pagefactory/ElementLocatorFactory.java` (JAVA) | Magnitude: 3.6 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 3, api: 2, doc: 2, args: 1
- `dotnet/src/webdriver/Command.cs` (CSHARP) | Magnitude: 33.08 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 48, decorators: 43, doc: 38, structural_boundaries: 11
- `java/test/org/openqa/selenium/remote/HasMagicNumbers.java` (JAVA) | Magnitude: 2.18 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 2, args: 1, func_start: 1, class_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `py/test/unit/selenium/webdriver/ie/test_ie_options.py` (PYTHON) | Magnitude: 109.8 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 92, structural_boundaries: 86, safety: 47, state_mutation: 34
- `dotnet/src/webdriver/Remote/SendingRemoteHttpRequestEventArgs.cs` (CSHARP) | Magnitude: 31.74 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: doc: 35, indent_spaces: 23, safety: 9, api: 7
- `rb/lib/selenium/webdriver/support/escaper.rb` (RUBY) | Magnitude: 15.3 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 8, branch: 4, class_start: 4
- `py/test/selenium/webdriver/remote/remote_session_event_tests.py` (PYTHON) | Magnitude: 26.2 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 21, safety: 16, state_mutation: 9
- `rb/lib/selenium/webdriver/support/color.rb` (RUBY) | Magnitude: 114.94 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 110, core_var_decl: 26, branch: 22, state_mutation: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `dotnet/src/webdriver/Remote/ReadOnlyDesiredCapabilities.cs` (CSHARP) | Magnitude: 65.34 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 115, doc: 61, structural_boundaries: 24, branch: 22
- `java/src/org/openqa/selenium/grid/commands/Standalone.java` (JAVA) | Magnitude: 67.62 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 169, structural_boundaries: 101, import: 58, core_var_decl: 36
- `javascript/private/fragment.bzl` (PYTHON) | Magnitude: 54.96 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 75, core_var_decl: 27, design_snake_case: 26, state_mutation: 15
- `dotnet/src/webdriver/Platform.cs` (CSHARP) | Magnitude: 64.96 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: doc: 73, indent_spaces: 71, branch: 19, structural_boundaries: 15
- `dotnet/paket.nuget_extension.bzl` (PYTHON) | Magnitude: 2.76 | Delta: **0.053** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 3, core_var_decl: 3, design_snake_case: 3, structural_boundaries: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `java/src/org/openqa/selenium/support/pagefactory/FieldDecorator.java` (JAVA) | Magnitude: 3.9 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, api: 2, doc: 2, reflection_metaprogramming: 2
- `cpp/iedriver/cominterfaces.cpp` (CPP) | Magnitude: 12.08 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: immutability_locks: 3, core_var_decl: 3, import: 1
- `rb/lib/selenium/webdriver/common.rb` (RUBY) | Magnitude: 7.88 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 84, import: 84
- `cpp/iedriver/InputManager.h` (CPP) | Magnitude: 21.38 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 75, structural_boundaries: 41, args: 35, immutability_locks: 19
- `cpp/iedriver/ActionSimulators/PersistentEventSimulator.h` (CPP) | Magnitude: 21.2 | Delta: **0.096** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 21, indent_spaces: 21, args: 12, api: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `rb/lib/selenium/webdriver/remote/bridge/locator_converter.rb` (RUBY) | Magnitude: 213.84 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 46, core_var_decl: 13, state_mutation: 11, design_snake_case: 11
- `py/test/selenium/webdriver/remote/remote_hub_connection_tests.py` (PYTHON) | Magnitude: 4.64 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 13, indent_spaces: 7, safety: 4, import: 4
- `java/src/org/openqa/selenium/grid/web/HandlerNotFoundException.java` (JAVA) | Magnitude: 3.74 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 3, api: 2, args: 1
- `py/test/selenium/webdriver/firefox/ff_takes_full_page_screenshots_tests.py` (PYTHON) | Magnitude: 11.36 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 9, core_var_decl: 6, design_snake_case: 6
- `common/src/web/scrolling_tests/page_with_double_overflow_auto.html` (HTML) | Magnitude: 25.02 | Delta: **0.059** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 5, core_var_decl: 3, design_snake_case: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `java/src/org/openqa/selenium/grid/router/httpd/RouterServer.java` (JAVA) | Magnitude: 57.58 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 132, structural_boundaries: 102, import: 63, core_var_decl: 35
- `java/src/org/openqa/selenium/grid/sessionmap/httpd/SessionMapServer.java` (JAVA) | Magnitude: 33.36 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 82, structural_boundaries: 48, import: 27, args: 15
- `java/src/org/openqa/selenium/grid/web/PathResource.java` (JAVA) | Magnitude: 36.64 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 58, structural_boundaries: 29, io: 14, args: 12
- `java/src/org/openqa/selenium/grid/node/relay/RelaySessionFactory.java` (JAVA) | Magnitude: 69.16 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 169, structural_boundaries: 81, import: 51, core_var_decl: 24
- `java/test/org/openqa/selenium/netty/server/NettyServerTest.java` (JAVA) | Magnitude: 27.08 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 103, structural_boundaries: 64, core_var_decl: 27, design_snake_case: 26

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `go` (SHELL) | Magnitude: 31.76 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: structural_boundaries: 13, indent_spaces: 9, state_mutation: 8, core_var_decl: 7
- `java/test/org/openqa/selenium/grid/sessionmap/jdbc/JdbcBackedSessionMapTest.java` (JAVA) | Magnitude: 29.58 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 83, structural_boundaries: 58, import: 23, core_var_decl: 19
- `java/src/org/openqa/selenium/bidi/browsingcontext/UserPromptOpened.java` (JAVA) | Magnitude: 43.84 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 60, structural_boundaries: 21, core_var_decl: 9, state_mutation: 8
- `java/test/org/openqa/selenium/environment/GlobalTestEnvironment.java` (JAVA) | Magnitude: 24.92 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 10, safety_bypasses: 6, api: 5
- `java/src/org/openqa/selenium/bidi/browsingcontext/UserPromptType.java` (JAVA) | Magnitude: 15.14 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 6, args: 3, func_start: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `javascript/selenium-webdriver/bidi/storage.js` (JAVASCRIPT) | Magnitude: 106.9 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 120, branch: 30, structural_boundaries: 19, reflection_metaprogramming: 18
- `common/repositories.bzl` (PYTHON) | Magnitude: 61.6 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 128, core_var_decl: 83, design_snake_case: 83, state_mutation: 22
- `dotnet/src/webdriver/BiDi/Json/Converters/InputOriginConverter.cs` (CSHARP) | Magnitude: 18.9 | Delta: **0.122** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 23, branch: 5, structural_boundaries: 5, safety: 3

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `Rakefile` -> Churn: **76.82%** | Cog Load: 50.2172% | Debt: 0.0%
- `dotnet/src/webdriver/BiDi/BrowsingContext/BrowsingContextNetworkModule.cs` -> Churn: **65.67%** | Cog Load: 68.7081% | Debt: 21.8743%
- `dotnet/src/webdriver/BiDi/Input/InputModule.cs` -> Churn: **65.67%** | Cog Load: 95.4372% | Debt: 99.593%
- `dotnet/src/webdriver/BiDi/Broker.cs` -> Churn: **61.75%** | Cog Load: 93.4255% | Debt: 35.6825%
- `dotnet/src/webdriver/BiDi/Module.cs` -> Churn: **54.11%** | Cog Load: 0.0% | Debt: 81.7574%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `javascript/atoms/test/inject_test.html` -> **Simon Mavi Stewart** (100.0% isolated ownership) | Magnitude: 1358.72
- `dotnet/src/webdriver/BiDi/Network/INetworkModule.cs` -> **Nikolay Borisenko** (100.0% isolated ownership) | Magnitude: 1294.56
- `javascript/atoms/test/overflow_test.html` -> **Simon Mavi Stewart** (100.0% isolated ownership) | Magnitude: 1197.72
- `javascript/atoms/dom.js` -> **Simon Mavi Stewart** (100.0% isolated ownership) | Magnitude: 998.78
- `py/selenium/webdriver/common/bidi/browsing_context.py` -> **Corey Goldberg** (100.0% isolated ownership) | Magnitude: 819.7

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `java/src/org/openqa/selenium/remote/RemoteWebDriver.java` -> **Severity: 0.239** (Bridge: 0.0031 * Flux: 78.3733%)
- `java/src/org/openqa/selenium/json/JsonTypeCoercer.java` -> **Severity: 0.077** (Bridge: 0.0008 * Flux: 99.9451%)
- `java/src/org/openqa/selenium/remote/codec/w3c/W3CHttpResponseCodec.java` -> **Severity: 0.056** (Bridge: 0.0006 * Flux: 100.0%)
- `java/src/org/openqa/selenium/grid/node/CustomLocatorHandler.java` -> **Severity: 0.05** (Bridge: 0.0005 * Flux: 99.9999%)
- `java/src/org/openqa/selenium/remote/JsonToWebElementConverter.java` -> **Severity: 0.048** (Bridge: 0.0005 * Flux: 98.7342%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `java/src/org/openqa/selenium/internal/Require.java` -> **Severity: 8.681** (Embedded: 0.1493 * Error Risk: 58.1372%)
- `java/src/org/openqa/selenium/Capabilities.java` -> **Severity: 6.466** (Embedded: 0.0808 * Error Risk: 80.0%)
- `java/src/org/openqa/selenium/net/HostIdentifier.java` -> **Severity: 5.164** (Embedded: 0.0645 * Error Risk: 80.0%)
- `java/src/org/openqa/selenium/WebDriverException.java` -> **Severity: 4.814** (Embedded: 0.0874 * Error Risk: 55.0702%)
- `java/src/org/openqa/selenium/MutableCapabilities.java` -> **Severity: 4.147** (Embedded: 0.0564 * Error Risk: 73.4783%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `java/src/org/openqa/selenium/internal/Require.java` -> **Severity: 4395.1** (Blast Radius: 43.951 * Doc Risk: 100.0%)
- `java/src/org/openqa/selenium/WebDriverException.java` -> **Severity: 1375.082** (Blast Radius: 16.876 * Doc Risk: 81.4815%)
- `java/src/org/openqa/selenium/UsernameAndPassword.java` -> **Severity: 793.6** (Blast Radius: 7.936 * Doc Risk: 100.0%)
- `java/src/org/openqa/selenium/json/JsonException.java` -> **Severity: 544.6** (Blast Radius: 5.446 * Doc Risk: 100.0%)
- `java/src/org/openqa/selenium/net/HostIdentifier.java` -> **Severity: 527.4** (Blast Radius: 5.274 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 574 literal sites + 31 sites through wrappers = 605
- **`panics_and_aborts`:** 2907 literal sites + 44 sites through wrappers = 2951

- `get_stdout` (function, debug_prints, primitive): 10 call sites in 6 files -- `rust/tests/common.rs`
- `JsonConfig` (function, panics_and_aborts, primitive): 6 call sites in 2 files -- `java/src/org/openqa/selenium/grid/config/JsonConfig.java`
- `info` (function, debug_prints, primitive): 6 call sites in 1 files -- `javascript/selenium-webdriver/testing/index.js`
- `files` (function, panics_and_aborts, primitive): 5 call sites in 1 files -- `java/test/org/openqa/selenium/bidi/browser/BrowserCommandsTest.java`
- `fromUri` (function, panics_and_aborts, primitive): 4 call sites in 3 files -- `java/src/org/openqa/selenium/net/Urls.java`
- `verifyNoCommands` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `java/test/org/openqa/selenium/remote/RemoteWebDriverInitializationTest.java`
- `createUri` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `java/test/org/openqa/selenium/grid/distributor/selector/DefaultSlotSelectorTest.java`
- `ResetGlobalLog` (function, debug_prints, primitive): 2 call sites in 1 files -- `dotnet/test/webdriver/Firefox/FirefoxDriverServiceTests.cs`
- `ResetGlobalLog` (function, debug_prints, primitive): 2 call sites in 1 files -- `dotnet/test/webdriver/Internal/Logging/LogTests.cs`
- `createUri` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `java/test/org/openqa/selenium/grid/distributor/DistributorTestBase.java`
- `createUri` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `java/test/org/openqa/selenium/grid/distributor/selector/GreedySlotSelectorTest.java`
- `fail` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `javascript/selenium-webdriver/test/lib/until_test.js`
*(+22 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 97409 call pairs -- scoped 29.4%, unique 0.9%, ambiguous 28.1%, external 41.7%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| java | 57598 | 32.0% | 0.9% | 31.0% | 36.2% |
| csharp | 13837 | 30.0% | 2.3% | 24.5% | 43.2% |
| python | 9359 | 27.1% | 0.0% | 36.6% | 36.4% |
| cpp | 5171 | 20.4% | 0.7% | 20.8% | 58.2% |
| javascript | 4749 | 27.7% | 0.0% | 18.6% | 53.7% |
| ruby | 3431 | 18.0% | 0.0% | 19.6% | 62.5% |
| rust | 1713 | 16.2% | 0.0% | 0.2% | 83.7% |
| html | 1072 | 17.4% | 0.1% | 0.1% | 82.5% |
| typescript | 267 | 11.6% | 0.0% | 2.6% | 85.8% |
| shell | 99 | 16.2% | 0.0% | 0.0% | 83.8% |

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
