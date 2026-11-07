# ARCHITECTURAL_BRIEF: magento2
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/magento/magento2.git` |
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
- **Scope:** 40266 analyzed artifact(s), 2177221 LOC.
- **Load-bearing artifact:** `dev/tests/integration/framework/Magento/TestFramework/Indexer/TestCase.php` -- 5866 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `app/code/Magento/Catalog/Test/Unit/Model/ProductTest.php` -- pulls in 79 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `lib/web/prototype/prototype.js` at magnitude 5238.5 (structural weight, not risk).
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
| Total Artifacts | 41590 |
| Analyzed Artifacts (Scanned) | 40266 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1324 |
| Total LOC | 2177221 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 96.8% |
| Dominant Lang | PHP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5102 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0777 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 10.0718 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 1337 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PHP | 26251 | 1914839 | 65.2% |
| XML | 9896 | 13 | 24.6% |
| JAVASCRIPT | 1342 | 150559 | 3.3% |
| PLAINTEXT | 721 | 2 | 1.8% |
| CSS | 479 | 69216 | 1.2% |
| MARKDOWN | 434 | 0 | 1.1% |
| HTML | 403 | 8831 | 1.0% |
| JSON | 397 | 19864 | 1.0% |
| CSV | 337 | 13457 | 0.8% |
| YAML | 5 | 440 | 0.0% |
| SQLITE | 1 | 0 | 0.0% |

## 4.1 SOURCE ENCODINGS
> 1 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 40258 |
| utf-8 | bom | 7 |
| cp1252 | cp1252-fallback | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 36%, Declarative / Non-Code 13%, Large Core Modules 11%, Encapsulated Accessors Files 9%, Parameter Forwarders Files 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 39088 | 97.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1154 | 2.9% |
| Static: Minified & Vendor Opaque Mass | 24 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1324*

**Composition by Extension & Reason:**
- `.png`: 225x Excluded (Explicitly Denied Extension: '.png')
- `.js`: 209x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 8 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 1192 LOC)
- `no_extension`: 126x Unsupported Format (.undeterminable), 62x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Unresolved Ambiguity (No Retainable Structure)
- `.gif`: 114x Excluded (Explicitly Denied Extension: '.gif')
- `.php`: 110x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 83 exceeds 500 chars)
- `.jpg`: 65x Excluded (Explicitly Denied Extension: '.jpg')
- `.css`: 57x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Saturation: Line 1 exceeds 500 chars), 3x Excluded (Saturation: Line 6 exceeds 500 chars)
- `.graphqls`: 48x Excluded (Unsupported Extension: '.graphqls')
- `.less`: 30x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Zero-Density Threshold (LOC: 127, Signals: 0), 1x Zero-Density Threshold (LOC: 60, Signals: 0)
- `.xml`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Saturation: Line 57 exceeds 500 chars), 2x Excluded (Saturation: Line 12 exceeds 500 chars)
- `.html`: 26x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 24 exceeds 500 chars), 1x Excluded (Saturation: Line 16 exceeds 500 chars)
- `.dist`: 23x Excluded (Unsupported Extension: '.dist')
- `.sample`: 14x Excluded (Unsupported Extension: '.sample'), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 1150 LOC), 1x Excluded (Static Asset Blob without Intent: 1278 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 6.7 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 31.8 | 48.1 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 8.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 0.8 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 7.0 | 1.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 27.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 74.3 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 24.9 | 0.4 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.5 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 6.5 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 22428 | 9676 | 2 | `dev/tests/integration/testsuite/Magento/Framework/Jwt/JwtManagerTest.php` |
| cleanup | 1817 | 977 | 0 | `dev/tests/api-functional/testsuite/Magento/Downloadable/Api/ProductRepositoryTest.php` |
| guards | 142605 | 20173 | 10 | `lib/web/prototype/prototype.js` |
| danger | 19999 | 6062 | 1 | `lib/web/knockoutjs/knockout.js` |
| concurrency | 1380 | 441 | 0 | `lib/web/vimeo/player.js` |
| connectivity | 88390 | 21910 | 5 | `app/code/Magento/Sales/Model/Order.php` |
| io | 2586 | 846 | 0 | `lib/internal/Magento/Framework/Archive/Tar.php` |
| crypto | 0 | 0 | 0 | - |
| ipc | 731 | 275 | 0 | `app/code/Magento/Config/Test/Unit/Model/Config/_files/invalidSystemXmlArray.php` |
| time | 2817 | 952 | 0 | `lib/web/jquery/ui-modules/widgets/datepicker.js` |
| serialization | 2781 | 1262 | 0 | `app/code/Magento/Csp/Test/Unit/Model/SubresourceIntegrity/Storage/FileTest.php` |
| regex | 1945 | 748 | 0 | `lib/web/prototype/prototype.js` |
| events | 6030 | 1630 | 0 | `app/code/Magento/Newsletter/Test/Unit/Model/SubscriptionManagerTest.php` |
| tests | 107915 | 8509 | 8 | `dev/tests/js/jasmine/tests/lib/mage/validation.test.js` |
| docs | 224229 | 27928 | 13 | `app/code/Magento/Sales/Model/Order.php` |
| debt | 2267 | 1137 | 0 | `dev/tests/js/jasmine/tests/app/code/Magento/Ui/base/js/form/components/tab_group.test.js` |
| mutation | 323303 | 24019 | 20 | `lib/web/prototype/prototype.js` |
| dead_code | 47296 | 13269 | 4 | `app/code/Magento/Catalog/Test/Unit/Model/ResourceModel/CategoryTest.php` |
| credential | 376 | 184 | 0 | `app/code/Magento/Integration/Test/Unit/Oauth/OauthTest.php` |
| threat | 404 | 210 | 0 | `dev/tests/api-functional/testsuite/Magento/GraphQl/Catalog/CategoryListTest.php` |
| ml_ai | 607 | 268 | 0 | `lib/internal/Magento/Framework/Setup/BackupRollback.php` |
| ui | 10988 | 1829 | 0 | `app/code/Magento/GiftMessage/view/frontend/templates/inline.phtml` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.1946**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `lib/internal/Magento/Framework/Archive/Tar.php` (Hits: 58)
- `lib/web/prototype/windows/themes/lighting.css` (Hits: 52)
- `app/code/Magento/Widget/Test/Unit/Block/Adminhtml/Widget/Instance/Edit/Chooser/ContainerTest.php` (Hits: 30)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **TestCase.php** (`dev/tests/integration/framework/Magento/TestFramework/Indexer/TestCase.php`) — 5866 inbound connections
2. **Bootstrap.php** (`dev/tests/integration/framework/Magento/TestFramework/Helper/Bootstrap.php`) — 3257 inbound connections
3. **ObjectManager.php** (`lib/internal/Magento/Framework/TestFramework/Unit/Helper/ObjectManager.php`) — 2521 inbound connections
4. **LocalizedException.php** (`lib/internal/Magento/Framework/Exception/LocalizedException.php`) — 1700 inbound connections
5. **ObjectManager.php** (`lib/internal/Magento/Framework/App/ObjectManager.php`) — 1507 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ProductTest.php** (`app/code/Magento/Catalog/Test/Unit/Model/ProductTest.php`) — 79 outbound dependencies
2. **AccountManagementTest.php** (`app/code/Magento/Customer/Test/Unit/Model/AccountManagementTest.php`) — 70 outbound dependencies
3. **ProductTest.php** (`app/code/Magento/CatalogImportExport/Test/Unit/Model/Import/ProductTest.php`) — 66 outbound dependencies
4. **InstallerTest.php** (`setup/src/Magento/Setup/Test/Unit/Model/InstallerTest.php`) — 64 outbound dependencies
5. **MultishippingTest.php** (`app/code/Magento/Multishipping/Test/Unit/Model/Checkout/Type/MultishippingTest.php`) — 62 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `Fotorama` **(Many-Argument Workhorses)** (@ `lib/web/fotorama/fotorama.js`) -> Impact: **878.8** | LOC: 2127
- `newContext` **(Many-Argument Workhorses)** (@ `lib/web/requirejs/require.js`) -> Impact: **474.5** | LOC: 1571
- `spectrum` **(Many-Argument Workhorses)** (@ `lib/web/jquery/spectrum/spectrum.js`) -> Impact: **273.9** | LOC: 802
- `Magnify` **(Many-Argument Workhorses)** (@ `lib/web/magnifier/magnifier.js`) -> Impact: **225.1** | LOC: 588
- `__construct` **(Many-Argument Workhorses)** (@ `app/code/Magento/Customer/Model/AccountManagement.php`) -> Impact: **224.8** | LOC: 89
  * *Intent:* * @param SessionCleanerInterface|null $sessionCleaner * @param AuthorizationInterface|null $authorization * @param AuthenticationInterface|null $authe...
- `__construct` **(Many-Argument Workhorses)** (@ `app/code/Magento/CatalogRule/Model/Indexer/IndexBuilder.php`) -> Impact: **207.1** | LOC: 89
  * *Intent:* * @param TableSwapper|null $tableSwapper * @param TimezoneInterface|null $localeDate * @param ProductCollectionFactory|null $productCollectionFactory ...
- `magnifierFullscreen` **(Defensive Guards)** (@ `lib/web/magnifier/magnify.js`) -> Impact: **191.9** | LOC: 388
  * *Intent:* /** * Method which makes draggable picture. Also work on touch devices. */
- `loadImg` **(Many-Argument Workhorses)** (@ `lib/web/fotorama/fotorama.js`) -> Impact: **151.8** | LOC: 173
- `init` **(Many-Argument Workhorses)** (@ `lib/web/knockoutjs/knockout-repeat.js`) -> Impact: **147.8** | LOC: 164
- `_generateHTML` **(Compute Cores)** (@ `lib/web/mage/calendar.js`) -> Impact: **143.9** | LOC: 248
  * *Intent:* /** * Overwrite jQuery UI datepicker function. * Reason: magento date could be set before calendar show * but local date will be styled as current in ...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `lib/web/jquery/ui-modules/widgets` | 20 | 10264.46 | 71.31% | 45.34% |
| `dev/tests/integration/testsuite/Magento/Catalog/_files` | 420 | 9240.32 | 3.79% | 0.0% |
| `lib/web/prototype` | 4 | 7397.1 | 57.42% | 28.72% |
| `app/code/Magento/Catalog/Test/Mftf/ActionGroup` | 578 | 6080.56 | 0.0% | 0.0% |
| `lib/web/knockoutjs` | 4 | 5921.82 | 83.42% | 36.23% |
| `app/code/Magento/Sales/Model/Order` | 46 | 5732.76 | 18.11% | 7.39% |
| `app/code/Magento/Sales/Api/Data` | 51 | 4807.78 | 0.24% | 0.0% |
| `dev/tests/integration/testsuite/Magento/Sales/_files` | 202 | 4753.2 | 6.07% | 0.0% |
| `lib/web/fotorama` | 1 | 4704.34 | 90.0% | 12.45% |
| `app/code/Magento/Catalog/Model` | 50 | 4378.26 | 14.62% | 12.72% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `app/code/Magento/AsynchronousOperations/Model/ItemStatus.php` -> **100.0%** Exposure
- `app/code/Magento/Catalog/Model/Product/Price/SpecialPrice.php` -> **100.0%** Exposure
- `app/code/Magento/Catalog/Model/ProductRender/Image.php` -> **100.0%** Exposure
- `app/code/Magento/Catalog/Model/Template/Filter.php` -> **100.0%** Exposure
- `app/code/Magento/CatalogRule/Model/Data/Condition.php` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `app/code/Magento/AdminAnalytics/Controller/Adminhtml/Config/DisableAdminUsage.php` -> **100.0%** Exposure
- `app/code/Magento/AdminAnalytics/Controller/Adminhtml/Config/EnableAdminUsage.php` -> **100.0%** Exposure
- `app/code/Magento/AdminAnalytics/Test/Unit/Controller/Adminhtml/Config/EnableAdminUsageTest.php` -> **100.0%** Exposure
- `app/code/Magento/AdminAnalytics/view/adminhtml/templates/notification.phtml` -> **100.0%** Exposure
- `app/code/Magento/AdminNotification/Block/Grid/Renderer/Severity.php` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `app/code/Magento/Catalog/Test/Unit/Model/ResourceModel/CategoryTest.php` -> **78** Orphaned Functions | **0** Duplicates
- `app/code/Magento/Catalog/Test/Unit/Model/ProductTest.php` -> **73** Orphaned Functions | **0** Duplicates
- `lib/internal/Magento/Framework/View/Layout/Proxy.php` -> **61** Orphaned Functions | **0** Duplicates
- `app/code/Magento/Customer/Test/Unit/Model/AccountManagementTest.php` -> **53** Orphaned Functions | **0** Duplicates
- `lib/internal/Magento/Framework/Test/Unit/EscaperTest.php` -> **39** Orphaned Functions | **12** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `app/code/Magento/Config/Test/Unit/Model/Config/Parser/CommentTest.php` -> **100.0%** Exposure
- `app/code/Magento/Integration/Test/Unit/Oauth/OauthTest.php` -> **100.0%** Exposure
- `dev/tests/api-functional/framework/Magento/TestFramework/TestCase/Webapi/AdapterInterface.php` -> **100.0%** Exposure
- `dev/tests/api-functional/testsuite/Magento/GraphQl/Customer/ChangeCustomerPasswordTest.php` -> **100.0%** Exposure
- `lib/internal/Magento/Framework/Oauth/OauthInterface.php` -> **100.0%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `43` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `118279` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `lib/web/prototype/prototype.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.564)
- **Top Global Matches:** file_cluster_12: 7.564, file_cluster_15: 9.361, file_cluster_10: 9.665
- **Magnitude:** 5238.5 | **LOC:** 7670 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (78.0%), Guard Balance (formerly Safety Score) (65.4%), Debt Markers (formerly Tech Debt) (18.0%)
- **Documentation Coverage:** 99.661% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `select` **(Many-Argument Workhorses)** (Impact: 65.6)
    * *Intent:* /** * A low-level selection function that works with Sizzle's compiled * selector functions * select...
  * `getPixelValue` **(Many-Argument Workhorses)** (Impact: 64.8)
  * `Str` **(Defensive Guards)** (Impact: 51.0)
  * `clonePosition` **(Many-Argument Workhorses)** (Impact: 45.1)
  * `serializeElements` **(Defensive Guards)** (Impact: 42.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 10 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 707 instances
* *High Risk Execution (weighted view):* 5
* *Concurrency (weighted view):* 18
* *State Mutation (weighted view):* 2500
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1216`, `structural_boundaries: 1452`, `args: 731`, `func_start: 514`
* *Risk/State:* `safety_bypasses: 99`, `high_risk_execution: 15`, `state_mutation: 1086`, `fragile_debt: 1`, `duplicate_logic: 8`, `unreferenced_by_name: 19`
* *Architecture:* `io: 2`, `api: 5`, `concurrency: 3`
* *Defense:* `safety: 433`, `doc: 14`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/web/knockoutjs/knockout.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.912)
- **Top Global Matches:** file_cluster_12: 8.912, file_cluster_4: 9.607, file_cluster_7: 11.377
- **Magnitude:** 5078.86 | **LOC:** 6612 | **CtrlFlow:** 28.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (84.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setDomNodeChildrenFromArrayMapping` **(Many-Argument Workhorses)** (Impact: 126.4)
  * `extenders[                   ]` **(Many-Argument Workhorses)** (Impact: 71.9)
  * `applyBindingsToNodeInternal` **(Many-Argument Workhorses)** (Impact: 71.5)
  * `dependentObservable` **(Many-Argument Workhorses)** (Impact: 65.8)
  * `compareSmallArrayToBigArray` **(Many-Argument Workhorses)** (Impact: 56.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 562 instances
* *High Risk Execution (weighted view):* 2
* *Concurrency (weighted view):* 56
* *State Mutation (weighted view):* 2005
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1441`, `structural_boundaries: 933`, `args: 577`, `func_start: 340`
* *Risk/State:* `safety_bypasses: 144`, `high_risk_execution: 6`, `state_mutation: 881`, `dead_code: 6`, `planned_debt: 3`, `fragile_debt: 10`
* *Architecture:* `io: 1`, `api: 25`, `concurrency: 16`
* *Defense:* `safety: 363`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/web/fotorama/fotorama.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.818)
- **Top Global Matches:** file_cluster_4: 8.818, file_cluster_15: 12.785, file_cluster_12: 13.076
- **Magnitude:** 4704.34 | **LOC:** 4082 | **CtrlFlow:** 27.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (90.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.4%)
- **Documentation Coverage:** 95.9854% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Fotorama` **(Many-Argument Workhorses)** (Impact: 878.8)
  * `loadImg` **(Many-Argument Workhorses)** (Impact: 151.8)
  * `touch` **(Many-Argument Workhorses)** (Impact: 108.7)
  * `moveOnTouch` **(Many-Argument Workhorses)** (Impact: 95.7)
  * `bindGlobalEvents` **(Defensive Guards)** (Impact: 67.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 472 instances
* *Concurrency (weighted view):* 61
* *State Mutation (weighted view):* 1581
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 857`, `structural_boundaries: 342`, `args: 297`, `func_start: 223`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 1`, `state_mutation: 637`, `duplicate_logic: 2`, `unreferenced_by_name: 12`
* *Architecture:* `concurrency: 16`
* *Defense:* `safety: 207`, `doc: 21`, `test: 2`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/code/Magento/Downloadable/view/adminhtml/templates/product/edit/downloadable/links.phtml` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 5.621)
- **Top Global Matches:** file_cluster_12: 5.621, file_cluster_7: 6.68, file_cluster_10: 6.851
- **Magnitude:** 3364.73 | **LOC:** 486 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (58.6%), Complexity Load (formerly Cognitive Load) (25.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 64
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 109`, `args: 22`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 52`
* *Architecture:* `import: 1`
* *Defense:* `safety: 5`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/internal/Magento/Framework/DB/Adapter/Pdo/Mysql.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.064)
- **Top Global Matches:** file_cluster_4: 7.064, file_cluster_12: 9.253, file_cluster_16: 11.264
- **Magnitude:** 3140.94 | **LOC:** 4388 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **114** in-repo importer(s); it depends on **29**; blast radius 0.153; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (77.5%), Connectivity (formerly Api Exposure) (70.1%), Complexity Load (formerly Cognitive Load) (39.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_getColumnDefinition` **(Many-Argument Workhorses)** (Impact: 117.6)
    * *Intent:* /** * Retrieve column definition fragment * * @param array $options * @param string $ddlType Table D...
  * `prepareColumnValue` **(Many-Argument Workhorses)** (Impact: 66.2)
    * *Intent:* /** * Prepare value for save in column * * Return converted to column data type value * * @param arr...
  * `addIndex` **(Many-Argument Workhorses)** (Impact: 55.6)
    * *Intent:* /** * Add new index to table name * * @param string $tableName * @param string $indexName * @param s...
  * `insertOnDuplicate` **(Many-Argument Workhorses)** (Impact: 39.2)
    * *Intent:* /** * Inserts a table row with specified data. * * @param string $table The table to insert data int...
  * `_splitMultiQuery` **(Compute Cores)** (Impact: 38.1)
    * *Intent:* /** * Split multi statement query * * @param string $sql * @return array * @SuppressWarnings(PHPMD.C...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 506 instances
* *Api Near Db Sink:* 12 instances
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 1659
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 560`, `structural_boundaries: 479`, `args: 143`, `func_start: 141`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 59`, `high_risk_execution: 3`, `state_mutation: 647`, `fragile_debt: 2`
* *Architecture:* `io: 8`, `api: 117`, `import: 29`
* *Defense:* `safety: 123`, `doc: 179`, `immutability_locks: 17`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.153
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.002839
  * `Imports (Out-Degree: 27):` Magento\Framework\App\ObjectManager, Magento\Framework\Cache\CacheConstants, Magento\Framework\Cache\FrontendInterface, Magento\Framework\DB\Adapter\AdapterInterface, Magento\Framework\DB\Adapter\ConnectionException, Magento\Framework\DB\Adapter\DeadlockException, Magento\Framework\DB\Adapter\DuplicateException, Magento\Framework\DB\Adapter\LockWaitException...
  * `Imported By (In-Degree: 114):` (Excluded from Brief to save tokens)

### `lib/web/jquery/ui-modules/widgets/datepicker.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.039)
- **Top Global Matches:** file_cluster_6: 7.039, file_cluster_4: 9.887, file_cluster_8: 16.643
- **Magnitude:** 2218.84 | **LOC:** 2238 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (77.8%), Guard Balance (formerly Safety Score) (70.3%), Debt Markers (formerly Tech Debt) (24.0%)
- **Documentation Coverage:** 74.1176% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_generateHTML` **(Defensive Guards)** (Impact: 143.0)
    * *Intent:* /* Generate the HTML for the current state of the date picker. */
  * `parseDate` **(Many-Argument Workhorses)** (Impact: 132.3)
    * *Intent:* /* Parse a string value into a date object. * See formatDate below for the possible formats. * * sho...
  * `formatDate` **(Many-Argument Workhorses)** (Impact: 78.5)
    * *Intent:* * @ - Unix timestamp (ms since 01/01/1970) * ! - Windows ticks (100ns since 01/01/0001) * "..." - li...
  * `_doKeyDown` **(Compute Cores)** (Impact: 75.7)
    * *Intent:* /* Handle keystrokes. */
  * `_determineDate` **(Defensive Guards)** (Impact: 50.7)
    * *Intent:* /* A date may be specified as an exact value or a relative one. */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 314 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 1084
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 500`, `structural_boundaries: 216`, `args: 104`, `func_start: 89`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 456`, `planned_debt: 1`, `duplicate_logic: 3`, `unreferenced_by_name: 8`
* *Architecture:* `concurrency: 1`
* *Defense:* `safety: 159`, `doc: 45`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/code/Magento/Ups/Model/Carrier.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.869)
- **Top Global Matches:** file_cluster_6: 7.869, file_cluster_4: 8.178, file_cluster_12: 14.363
- **Magnitude:** 2205.12 | **LOC:** 3012 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **44**; blast radius 0.02; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (78.6%), Complexity Load (formerly Cognitive Load) (40.5%), Connectivity (formerly Api Exposure) (15.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_formShipmentRequest` **(Many-Argument Workhorses)** (Impact: 56.9)
    * *Intent:* /** * Form XML for shipment request * * @param DataObject $request * @return string * @SuppressWarni...
  * `_formShipmentRestRequest` **(Many-Argument Workhorses)** (Impact: 54.4)
    * *Intent:* /** * Form REST for shipment request * * @param DataObject $request * @return string * @SuppressWarn...
  * `processShippingRestRateForItem` **(Many-Argument Workhorses)** (Impact: 48.4)
    * *Intent:* /** * Processing rate for ship element * * @param array $shipElement * @param array $allowedMethods ...
  * `setRequest` **(Compute Cores)** (Impact: 46.0)
    * *Intent:* /** * Prepare and set request to this instance * * @param RateRequest $request * @return $this * @Su...
  * `processShippingXmlRateForItem` **(Many-Argument Workhorses)** (Impact: 43.6)
    * *Intent:* /** * Processing rate for ship element * * @param \Magento\Framework\Simplexml\Element $shipElement ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 401 instances
* *State Mutation (weighted view):* 1406
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 338`, `structural_boundaries: 250`, `args: 58`, `func_start: 55`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 604`
* *Architecture:* `api: 24`, `import: 44`
* *Defense:* `safety: 76`, `doc: 92`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 9.9e-05
  * `Imports (Out-Degree: 35):` GuzzleHttp\Exception\GuzzleException, Laminas\Http\Client, Magento\CatalogInventory\Api\StockRegistryInterface, Magento\Directory\Helper\Data, Magento\Directory\Model\CountryFactory, Magento\Directory\Model\CurrencyFactory, Magento\Directory\Model\RegionFactory, Magento\Framework\App\Config\ScopeConfigInterface...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `lib/web/requirejs/require.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.437)
- **Top Global Matches:** file_cluster_6: 8.437, file_cluster_4: 8.701, file_cluster_15: 15.821
- **Magnitude:** 2128.96 | **LOC:** 2180 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.1%), Guard Balance (formerly Safety Score) (73.0%)
- **Documentation Coverage:** 67.0886% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `newContext` **(Many-Argument Workhorses)** (Impact: 474.5)
  * `normalize` **(Many-Argument Workhorses)** (Impact: 52.4)
    * *Intent:* /** * Given a relative module name, like ./something, normalize it to * a real name that can be mapp...
  * `makeRequire` **(Many-Argument Workhorses)** (Impact: 45.4)
  * `makeModuleMap` **(Many-Argument Workhorses)** (Impact: 42.1)
    * *Intent:* * Creates a module mapping that includes plugin prefix, module * name, and path. If parentModuleMap ...
  * `configure` **(Defensive Guards)** (Impact: 39.4)
    * *Intent:* /** * Set a configuration for the context. */
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 258 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 33
* *State Mutation (weighted view):* 819
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 365`, `structural_boundaries: 145`, `args: 118`, `func_start: 68`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 303`, `dead_code: 1`, `fragile_debt: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `concurrency: 8`, `import: 3`
* *Defense:* `safety: 80`, `doc: 29`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/web/jquery/timepicker.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.709)
- **Top Global Matches:** file_cluster_4: 7.709, file_cluster_6: 8.547, file_cluster_15: 14.526
- **Magnitude:** 2100.1 | **LOC:** 2292 | **CtrlFlow:** 28.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.2%), Guard Balance (formerly Safety Score) (64.2%), Debt Markers (formerly Tech Debt) (30.6%)
- **Documentation Coverage:** 83.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_limitMinMaxDateTime` **(Many-Argument Workhorses)** (Impact: 130.6)
    * *Intent:* /* * This function tries to limit the ability to go outside the * min/max date range */
  * `_optionDatepicker` **(Many-Argument Workhorses)** (Impact: 94.6)
  * `_newInst` **(Defensive Guards)** (Impact: 90.3)
    * *Intent:* /* * Create a new Timepicker instance */
  * `_injectTimePicker` **(Defensive Guards)** (Impact: 70.4)
    * *Intent:* /* * generate and inject html for timepicker into ui datepicker */
  * `_onTimeChange` **(Defensive Guards)** (Impact: 51.0)
    * *Intent:* /* * when a slider moves, set the internal time... * on time change is also called when the time is ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 311 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 1006
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 504`, `structural_boundaries: 259`, `args: 93`, `func_start: 72`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 384`, `dead_code: 5`, `planned_debt: 2`, `fragile_debt: 6`, `unreferenced_by_name: 10`
* *Architecture:* `concurrency: 1`
* *Defense:* `safety: 242`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/code/Magento/CatalogImportExport/Model/Import/Product.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.354)
- **Top Global Matches:** file_cluster_12: 7.354, file_cluster_4: 7.505, file_cluster_16: 8.214
- **Magnitude:** 2034.9 | **LOC:** 3680 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **54** in-repo importer(s); it depends on **33**; blast radius 0.253; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (70.6%), Complexity Load (formerly Cognitive Load) (36.5%), Connectivity (formerly Api Exposure) (23.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `saveProductMediaGalleryPhase` **(Many-Argument Workhorses)** (Impact: 114.1)
    * *Intent:* * @param int $rowNum * @param array $rowData * @param int $storeId * @param array $existingImages * ...
  * `saveProductAttributesPhase` **(Many-Argument Workhorses)** (Impact: 85.7)
    * *Intent:* /** * In _saveProducts loop, save product's attributes * * @param array $rowData * @param int $rowSc...
  * `validateRow` **(Many-Argument Workhorses)** (Impact: 66.3)
    * *Intent:* /** * Validate data row. * * @param array $rowData * @param int $rowNum * @return boolean * @Suppres...
  * `_saveProducts` **(I/O & Config Routines)** (Impact: 21.5)
    * *Intent:* /** * Gather and save information about product entities. * * FIXME: Reduce nesting level * * @retur...
  * `formatStockDataForRow` **(Stateful Encapsulated Methods)** (Impact: 21.1)
    * *Intent:* /** * Format row data to DB compatible values. * * @param array $rowData * @return array */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 335 instances
* *State Mutation (weighted view):* 1112
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 372`, `structural_boundaries: 330`, `args: 103`, `func_start: 102`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 442`, `fragile_debt: 1`
* *Architecture:* `api: 56`, `import: 33`
* *Defense:* `safety: 109`, `doc: 208`, `immutability_locks: 30`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.253
  * `Choke Point (Betweenness):` 0.000547 | `Ripple Effect (Closeness):` 0.030089
  * `Imports (Out-Degree: 35):` Magento\AwsS3\Driver\AwsS3, Magento\CatalogImportExport\Model\Import\Product\ImageTypeProcessor, Magento\CatalogImportExport\Model\Import\Product\LinkProcessor, Magento\CatalogImportExport\Model\Import\Product\MediaGalleryProcessor, Magento\CatalogImportExport\Model\Import\Product\RowValidatorInterface, Magento\CatalogImportExport\Model\Import\Product\Skip, Magento\CatalogImportExport\Model\Import\Product\SkuStorage, Magento\CatalogImportExport\Model\Import\Product\StatusProcessor...
  * `Imported By (In-Degree: 54):` (Excluded from Brief to save tokens)

### `app/code/Magento/Dhl/Model/Carrier.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.886)
- **Top Global Matches:** file_cluster_6: 6.886, file_cluster_4: 8.171, file_cluster_12: 15.156
- **Magnitude:** 1926.1 | **LOC:** 2939 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **55**; blast radius 0.013; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (72.4%), Complexity Load (formerly Cognitive Load) (36.5%), Connectivity (formerly Api Exposure) (14.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__construct` **(Many-Argument Workhorses)** (Impact: 58.1)
    * *Intent:* * @param Reader $configReader * @param StoreManagerInterface $storeManager * @param StringUtils $str...
  * `_parseXmlTrackingResponse` **(Defensive Guards)** (Impact: 52.7)
    * *Intent:* /** * Parse xml tracking response * * @param string[] $trackings * @param string $response * @return...
  * `_parseRestTrackingResponse` **(Defensive Guards)** (Impact: 43.7)
    * *Intent:* /** * @param string[] $trackings * @param string $response * @return void * @SuppressWarnings(PHPMD....
  * `_addRestRate` **(Defensive Guards)** (Impact: 43.4)
    * *Intent:* /** * DHL Quote Data calculating rates * * @param array $product * @param array $exchangeRates * @re...
  * `_doShipmentRequestRest` **(I/O & Config Routines)** (Impact: 37.1)
    * *Intent:* /** * DHL Shipment label API * * @return DataObject * @throws LocalizedException * @throws Throwable...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 323 instances
* *State Mutation (weighted view):* 1147
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 345`, `structural_boundaries: 262`, `args: 63`, `func_start: 58`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 501`, `dead_code: 1`
* *Architecture:* `api: 30`, `import: 55`
* *Defense:* `safety: 114`, `doc: 122`, `immutability_locks: 18`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 2.5e-05
  * `Imports (Out-Degree: 45):` DATE_RFC3339, Exception, Laminas\Http\Request, Magento\CatalogInventory\Api\StockRegistryInterface, Magento\Catalog\Model\Product\Type, Magento\Dhl\Model\Validator\XmlValidator, Magento\Directory\Helper\Data, Magento\Directory\Model\CountryFactory...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/web/jquery/spectrum/spectrum.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.486)
- **Top Global Matches:** file_cluster_4: 8.486, file_cluster_12: 9.58, file_cluster_15: 11.088
- **Magnitude:** 1786.18 | **LOC:** 2338 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.013; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (90.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.3%)
- **Documentation Coverage:** 88.7417% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `spectrum` **(Many-Argument Workhorses)** (Impact: 273.9)
  * `draggable` **(Many-Argument Workhorses)** (Impact: 53.5)
    * *Intent:* /** * Lightweight drag helper. Handles containment within the element, so that * when dragging, the ...
  * `initialize` **(I/O & Config Routines)** (Impact: 50.1)
  * `toString` **(Defensive Guards)** (Impact: 31.8)
  * `inputToRGB` **(Defensive Guards)** (Impact: 26.4)
    * *Intent:* // Possible string inputs: // // "red" // "#f00" or "f00" // "#ff0000" or "ff0000" // "#ff000000" or...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 200 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 677
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 343`, `structural_boundaries: 360`, `args: 158`, `func_start: 132`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 277`, `unreferenced_by_name: 7`
* *Architecture:* `io: 6`, `api: 1`, `concurrency: 3`, `import: 1`
* *Defense:* `safety: 72`, `doc: 6`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` jquery
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/web/prototype/window.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 9.486)
- **Top Global Matches:** file_cluster_12: 9.486, file_cluster_7: 10.46, file_cluster_4: 10.867
- **Magnitude:** 1724.0 | **LOC:** 1851 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.015; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.4%), Complexity Load (formerly Cognitive Load) (81.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `initialize` **(I/O & Config Routines)** (Impact: 41.0)
    * *Intent:* // Constructor // Available parameters : className, blurClassName, title, minWidth, minHeight, maxWi...
  * `setSize` **(Many-Argument Workhorses)** (Impact: 37.8)
    * *Intent:* // Sets window size
  * `_openDialog` **(Compute Cores)** (Impact: 35.0)
  * `getPageSize` **(Compute Cores)** (Impact: 29.5)
    * *Intent:* // // getPageSize() // Returns array with page width, height and window width, height // Core code f...
  * `_initDrag` **(Compute Cores)** (Impact: 22.7)
    * *Intent:* // initDrag event
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 266 instances
* *High Risk Execution (weighted view):* 5
* *Concurrency (weighted view):* 19
* *State Mutation (weighted view):* 848
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 421`, `structural_boundaries: 212`, `args: 130`, `func_start: 110`
* *Risk/State:* `safety_bypasses: 71`, `high_risk_execution: 6`, `state_mutation: 316`, `dead_code: 1`, `fragile_debt: 3`, `unreferenced_by_name: 23`
* *Architecture:* `io: 3`, `concurrency: 4`
* *Defense:* `safety: 18`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 2.5e-05
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/code/Magento/Sales/Model/Order.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.217)
- **Top Global Matches:** file_cluster_15: 6.217, file_cluster_11: 6.497, file_cluster_12: 6.521
- **Magnitude:** 1652.06 | **LOC:** 4738 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **413** in-repo importer(s); it depends on **44**; blast radius 0.767; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (99.0%), Guard Balance (formerly Safety Score) (57.3%), Complexity Load (formerly Cognitive Load) (22.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `registerCancellation` **(Many-Argument Workhorses)** (Impact: 21.3)
    * *Intent:* /** * Prepare order totals to cancellation * * @param string $comment * @param bool $graceful * @ret...
  * `_canReorder` **(Stateful Encapsulated Methods)** (Impact: 15.9)
    * *Intent:* /** * Retrieve order reorder availability * * @param bool $ignoreSalable * @return bool * @SuppressW...
  * `canCancel` **(Compute Cores)** (Impact: 14.8)
    * *Intent:* /** * Retrieve order cancel availability * * @return bool * @SuppressWarnings(PHPMD.CyclomaticComple...
  * `canCreditmemoForZeroTotal` **(Stateful Encapsulated Methods)** (Impact: 13.8)
    * *Intent:* /** * Retrieve credit memo for zero total availability. * * @param float $totalRefundable * @return ...
  * `getCustomerName` **(Compute Cores)** (Impact: 12.2)
    * *Intent:* /** * Get customer name * * @return string * @SuppressWarnings(PHPMD.CyclomaticComplexity) */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 117 instances
* *State Mutation (weighted view):* 411
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 231`, `structural_boundaries: 888`, `args: 375`, `func_start: 375`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 177`
* *Architecture:* `api: 384`, `import: 44`
* *Defense:* `safety: 17`, `doc: 428`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.767
  * `Choke Point (Betweenness):` 0.000207 | `Ripple Effect (Closeness):` 0.009837
  * `Imports (Out-Degree: 43):` Magento\Catalog\Api\ProductRepositoryInterface, Magento\Catalog\Model\Product\Type, Magento\Catalog\Model\Product\Visibility, Magento\Config\Model\Config\Source\Nooptreq, Magento\Directory\Model\Currency, Magento\Directory\Model\CurrencyFactory, Magento\Directory\Model\RegionFactory, Magento\Directory\Model\ResourceModel\Region...
  * `Imported By (In-Degree: 413):` (Excluded from Brief to save tokens)

### `app/code/Magento/CatalogImportExport/Model/Import/Product/Option.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 7.667)
- **Top Global Matches:** file_cluster_16: 7.667, file_cluster_12: 8.195, file_cluster_9: 8.222
- **Magnitude:** 1483.74 | **LOC:** 2252 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **20**; blast radius 0.013; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (68.8%), Complexity Load (formerly Cognitive Load) (38.6%), Connectivity (formerly Api Exposure) (12.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__construct` **(Many-Argument Workhorses)** (Impact: 59.3)
    * *Intent:* * @param ProductFactory $productFactory * @param CollectionFactory $optionColFactory * @param Collec...
  * `_getSpecificTypeData` **(Stateful Encapsulated Methods)** (Impact: 29.4)
    * *Intent:* /** * Retrieve specific type data * * @param array $rowData * @param int $optionTypeId * @param bool...
  * `_importData` **(I/O & Config Routines)** (Impact: 26.6)
    * *Intent:* /** * Import data rows. * * Additional store view data (option titles) will be sought in store view ...
  * `_parseCustomOptions` **(Defensive Guards)** (Impact: 22.6)
    * *Intent:* /** * Parse custom options string to inner format. * * @param array $rowData * @return array * @Supp...
  * `_collectOptionTypeData` **(Many-Argument Workhorses)** (Impact: 22.4)
    * *Intent:* * Collect custom option type data to import * * @param array $rowData * @param int &$prevOptionId * ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 233 instances
* *State Mutation (weighted view):* 752
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 295`, `structural_boundaries: 220`, `args: 63`, `func_start: 61`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 286`, `planned_debt: 1`
* *Architecture:* `api: 30`, `import: 20`
* *Defense:* `safety: 111`, `doc: 112`, `immutability_locks: 23`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 5e-05
  * `Imports (Out-Degree: 17):` Magento\CatalogImportExport\Model\Import\Product, Magento\Catalog\Api\Data\ProductInterface, Magento\Catalog\Model\ProductFactory, Magento\Catalog\Model\ResourceModel\Product\Option\CollectionFactory, Magento\Catalog\Model\ResourceModel\Product\Option\Value\Collection, Magento\Catalog\Model\ResourceModel\Product\Option\Value\CollectionFactory, Magento\Framework\App\Config\ScopeConfigInterface, Magento\Framework\App\ObjectManager...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `app/code/Magento/Catalog/Model/ResourceModel/Product/Collection.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.639)
- **Top Global Matches:** file_cluster_12: 6.639, file_cluster_16: 7.263, file_cluster_15: 7.678
- **Magnitude:** 1470.46 | **LOC:** 2584 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **317** in-repo importer(s); it depends on **19**; blast radius 1.93; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (70.1%), Connectivity (formerly Api Exposure) (50.1%), Complexity Load (formerly Cognitive Load) (36.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__construct` **(Many-Argument Workhorses)** (Impact: 113.2)
    * *Intent:* * @param ProductLimitationFactory|null $productLimitationFactory * @param MetadataPool|null $metadat...
  * `addAttributeToSort` **(Defensive Guards)** (Impact: 32.2)
    * *Intent:* /** * Add attribute to sort order * * @param string $attribute * @param string $dir * @return $this ...
  * `addAttributeToFilter` **(Many-Argument Workhorses)** (Impact: 26.0)
    * *Intent:* /** * Add attribute to filter * * @param \Magento\Eav\Model\Entity\Attribute\AbstractAttribute|strin...
  * `_productLimitationPrice` **(Many-Argument Workhorses)** (Impact: 20.9)
    * *Intent:* /** * Join Product Price Table with left-join possibility * * @param bool $joinLeft * @return $this ...
  * `addIdFilter` **(Compute Cores)** (Impact: 18.6)
    * *Intent:* /** * Add collection filters by identifiers * * @param mixed $productId * @param boolean $exclude * ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 211 instances
* *State Mutation (weighted view):* 761
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 249`, `structural_boundaries: 295`, `args: 94`, `func_start: 92`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 339`, `planned_debt: 1`
* *Architecture:* `api: 66`, `import: 19`
* *Defense:* `safety: 54`, `doc: 146`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.93
  * `Choke Point (Betweenness):` 0.002268 | `Ripple Effect (Closeness):` 0.036964
  * `Imports (Out-Degree: 26):` Magento\CatalogUrlRewrite\Model\ProductUrlRewriteGenerator, Magento\CatalogUrlRewrite\Model\Storage\DbStorage, Magento\Catalog\Api\Data\CategoryInterface, Magento\Catalog\Api\Data\ProductInterface, Magento\Catalog\Model\Indexer\Category\Product\TableMaintainer, Magento\Catalog\Model\Indexer\Product\Price\PriceTableResolver, Magento\Catalog\Model\Product\Attribute\Source\Status, Magento\Catalog\Model\Product\Gallery\ReadHandler...
  * `Imported By (In-Degree: 317):` (Excluded from Brief to save tokens)

### `app/code/Magento/Sales/view/adminhtml/web/order/create/scripts.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.011)
- **Top Global Matches:** file_cluster_4: 9.011, file_cluster_12: 9.726, file_cluster_7: 11.498
- **Magnitude:** 1425.76 | **LOC:** 1670 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (91.1%), Guard Balance (formerly Safety Score) (69.9%), Debt Markers (formerly Tech Debt) (60.4%)
- **Documentation Coverage:** 78.9474% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `productGridRowClick` **(Defensive Guards)** (Impact: 60.8)
  * `fillAddressFields` **(Compute Cores)** (Impact: 42.4)
  * `getPriceFields` **(Compute Cores)** (Impact: 35.9)
  * `changeAddressField` **(Defensive Guards)** (Impact: 31.7)
    * *Intent:* /** * Triggers on each form's element changes. * */
  * `productGridCheckboxCheck` **(Compute Cores)** (Impact: 29.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 172 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 19
* *State Mutation (weighted view):* 574
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 331`, `structural_boundaries: 175`, `args: 139`, `func_start: 108`
* *Risk/State:* `safety_bypasses: 41`, `high_risk_execution: 2`, `state_mutation: 230`, `dead_code: 2`, `unreferenced_by_name: 40`
* *Architecture:* `concurrency: 4`
* *Defense:* `safety: 59`, `doc: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/code/Magento/CatalogImportExport/Model/Export/Product.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.761)
- **Top Global Matches:** file_cluster_16: 6.761, file_cluster_4: 7.03, file_cluster_12: 7.96
- **Magnitude:** 1419.44 | **LOC:** 2366 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **12**; blast radius 0.155; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (74.3%), Complexity Load (formerly Cognitive Load) (35.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (31.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `appendMultirowData` **(Many-Argument Workhorses)** (Impact: 56.8)
    * *Intent:* /** * Append multi row data * * @param array $dataRow * @param array $multiRawData * @return array *...
  * `collectRawData` **(I/O & Config Routines)** (Impact: 30.9)
    * *Intent:* /** * Collect export data for all products * * @return array * @SuppressWarnings(PHPMD.CyclomaticCom...
  * `__construct` **(Many-Argument Workhorses)** (Impact: 25.4)
    * *Intent:* * @param \Magento\Eav\Model\ResourceModel\Entity\Attribute\Set\CollectionFactory $attrSetColFactory ...
  * `getCustomOptionsData` **(Compute Cores)** (Impact: 23.0)
    * *Intent:* /** * Collect custom options data for products that will be exported. * * Option name and type will ...
  * `capItemsPerPageByAttributeCount` **(Stateful Encapsulated Methods)** (Impact: 17.6)
    * *Intent:* /** * Cap page size for large attribute sets to keep EAV load queries controllable * * @param int $i...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 256 instances
* *State Mutation (weighted view):* 893
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 232`, `structural_boundaries: 206`, `args: 63`, `func_start: 58`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 381`
* *Architecture:* `api: 20`, `import: 12`
* *Defense:* `safety: 58`, `doc: 121`, `immutability_locks: 11`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.155
  * `Choke Point (Betweenness):` 0.000366 | `Ripple Effect (Closeness):` 0.030045
  * `Imports (Out-Degree: 14):` Magento\CatalogImportExport\Model\Import\Product, Magento\CatalogImportExport\Model\Import\Product\CategoryProcessor, Magento\CatalogInventory\Api\StockConfigurationInterface, Magento\Catalog\Model\Product, Magento\Catalog\Model\ResourceModel\Product\Option\Collection, Magento\Eav\Model\Entity\Attribute\ScopedAttributeInterface, Magento\Eav\Model\Entity\Collection\AbstractCollection, Magento\Framework\App\ObjectManager...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `app/code/Magento/Usps/Model/Carrier.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.468)
- **Top Global Matches:** file_cluster_6: 6.468, file_cluster_4: 9.792, file_cluster_8: 16.254
- **Magnitude:** 1346.38 | **LOC:** 2538 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **19**; blast radius 0.026; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (69.1%), Complexity Load (formerly Cognitive Load) (41.4%), Connectivity (formerly Api Exposure) (33.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_formIntlShipmentRequest` **(Many-Argument Workhorses)** (Impact: 74.5)
    * *Intent:* /** * Form XML for international shipment request * As integration guide it is important to follow a...
  * `setRequest` **(Compute Cores)** (Impact: 45.8)
    * *Intent:* /** * Prepare and set request to this instance * * @param \Magento\Quote\Model\Quote\Address\RateReq...
  * `_formUsSignatureConfirmationShipmentRequest` **(Many-Argument Workhorses)** (Impact: 42.0)
    * *Intent:* /** * Form XML for US Signature Confirmation request * As integration guide it is important to follo...
  * `_parseXmlResponse` **(Defensive Guards)** (Impact: 39.5)
    * *Intent:* /** * Parse calculated rates * * @param string $response * @return Result * @link http://www.usps.co...
  * `__construct` **(Many-Argument Workhorses)** (Impact: 39.4)
    * *Intent:* * @param \Magento\Shipping\Helper\Carrier $carrierHelper * @param \Magento\Catalog\Model\ResourceMod...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 229 instances
* *State Mutation (weighted view):* 750
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 250`, `structural_boundaries: 164`, `args: 47`, `func_start: 44`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 292`
* *Architecture:* `api: 40`, `import: 19`
* *Defense:* `safety: 42`, `doc: 76`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000299
  * `Imports (Out-Degree: 18):` Magento\Framework\App\ObjectManager, Magento\Framework\Async\CallbackDeferred, Magento\Framework\DataObject, Magento\Framework\Exception\LocalizedException, Magento\Framework\HTTP\AsyncClientInterface, Magento\Framework\HTTP\AsyncClient\HttpException, Magento\Framework\HTTP\AsyncClient\Request, Magento\Framework\HTTP\LaminasClient...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `lib/web/vimeo/player.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.051)
- **Top Global Matches:** file_cluster_12: 8.051, file_cluster_4: 10.181, file_cluster_7: 10.775
- **Magnitude:** 1333.96 | **LOC:** 2520 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Concurrency Surface (formerly Concurrency) (99.6%), Guard Balance (formerly Safety Score) (53.1%), Complexity Load (formerly Cognitive Load) (48.4%)
- **Documentation Coverage:** 58.3732% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Player` **(I/O & Config Routines)** (Impact: 138.7)
  * `DEF` **(Defensive Guards)** (Impact: 68.0)
  * `Player` **(Defensive Guards)** (Impact: 53.2)
    * *Intent:* /** * Create a Player. * * player iframe, and id, or a jQuery object. */
  * `WeakMap` **(Defensive Guards)** (Impact: 22.0)
  * `destroy` **(Defensive Guards)** (Impact: 21.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 91 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 120
* *State Mutation (weighted view):* 304
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 248`, `structural_boundaries: 268`, `args: 170`, `func_start: 220`
* *Risk/State:* `safety_bypasses: 34`, `high_risk_execution: 1`, `state_mutation: 122`, `planned_debt: 1`, `unreferenced_by_name: 17`
* *Architecture:* `io: 1`, `api: 5`, `concurrency: 50`
* *Defense:* `safety: 151`, `doc: 130`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/internal/Magento/Framework/App/Utility/Files.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 5.77)
- **Top Global Matches:** file_cluster_12: 5.77, file_cluster_16: 8.637, file_cluster_7: 9.096
- **Magnitude:** 1333.06 | **LOC:** 1723 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **75** in-repo importer(s); it depends on **9**; blast radius 0.287; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Connectivity (formerly Api Exposure) (51.5%), Complexity Load (formerly Cognitive Load) (37.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `accumulateThemeStaticFiles` **(Many-Argument Workhorses)** (Impact: 24.6)
    * *Intent:* /** * Accumulate files from themes * * @param string $area * @param string $locale * @param string $...
  * `classFileExists` **(Compute Cores)** (Impact: 21.9)
    * *Intent:* /** * Check if specified class exists * * @param string $class * @param string &$path * @return bool...
  * `collectModuleLayoutFiles` **(Stateful Encapsulated Methods)** (Impact: 20.8)
    * *Intent:* /** * Collect layout files from modules * * @param array $params * @param string $location * @return...
  * `collectThemeLayoutFiles` **(Stateful Encapsulated Methods)** (Impact: 18.9)
    * *Intent:* /** * Collect layout files from themes * * @param array $params * @param string $location * @return ...
  * `readLists` **(Defensive Guards)** (Impact: 18.0)
    * *Intent:* /** * Read all text files by specified glob pattern and combine them into an array of valid files/di...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 231 instances
* *State Mutation (weighted view):* 758
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 204`, `structural_boundaries: 230`, `args: 63`, `func_start: 59`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 296`
* *Architecture:* `io: 1`, `api: 43`, `import: 9`
* *Defense:* `safety: 27`, `doc: 72`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.287
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.001936
  * `Imports (Out-Degree: 11):` Magento\Framework\App\ObjectManager, Magento\Framework\Component\ComponentFile, Magento\Framework\Component\ComponentRegistrar, Magento\Framework\Component\DirSearch, Magento\Framework\Exception\LocalizedException, Magento\Framework\Filesystem\Glob, Magento\Framework\Serialize\Serializer\Json, Magento\Framework\View\Design\Theme\ThemePackage...
  * `Imported By (In-Degree: 75):` (Excluded from Brief to save tokens)

### `app/code/Magento/Sales/Model/AdminOrder/Create.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.25)
- **Top Global Matches:** file_cluster_4: 6.25, file_cluster_16: 8.252, file_cluster_12: 8.511
- **Magnitude:** 1321.7 | **LOC:** 2434 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **18**; blast radius 0.027; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (66.3%), Complexity Load (formerly Cognitive Load) (37.0%), Connectivity (formerly Api Exposure) (28.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `moveQuoteItem` **(Many-Argument Workhorses)** (Impact: 71.0)
    * *Intent:* /** * Move quote item to another items list * * @param int|\Magento\Quote\Model\Quote\Item $item * @...
  * `initFromOrder` **(Compute Cores)** (Impact: 28.5)
    * *Intent:* /** * Initialize creation data from existing order * * @param \Magento\Sales\Model\Order $order * @r...
  * `applySidebarData` **(Defensive Guards)** (Impact: 28.4)
    * *Intent:* /** * Handle data sent from sidebar * * @param array $data * @return $this * @throws \Magento\Framew...
  * `_prepareCustomerAddress` **(Stateful Encapsulated Methods)** (Impact: 25.0)
    * *Intent:* /** * Create customer address and save it in the quote so that it can be used to persist later. * * ...
  * `_setQuoteAddress` **(Many-Argument Workhorses)** (Impact: 23.3)
    * *Intent:* /** * Set and validate Quote address * * All errors added to _errors * * @param \Magento\Quote\Model...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 213 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 705
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 267`, `structural_boundaries: 213`, `args: 68`, `func_start: 66`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 279`
* *Architecture:* `api: 43`, `import: 18`
* *Defense:* `safety: 100`, `doc: 127`, `immutability_locks: 2`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.000372
  * `Imports (Out-Degree: 18):` Magento\Customer\Api\AddressMetadataInterface, Magento\Customer\Api\Data\AttributeMetadataInterface, Magento\Customer\Model\Metadata\Form, Magento\Framework\Api\ExtensibleDataObjectConverter, Magento\Framework\App\ObjectManager, Magento\Framework\App\Request\Http, Magento\Framework\Exception\LocalizedException, Magento\Payment\Model\Checks\SpecificationFactory...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `app/code/Magento/Quote/Model/Quote.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.501)
- **Top Global Matches:** file_cluster_12: 6.501, file_cluster_15: 7.488, file_cluster_4: 7.899
- **Magnitude:** 1302.92 | **LOC:** 2736 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **392** in-repo importer(s); it depends on **15**; blast radius 0.854; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (79.3%), Guard Balance (formerly Safety Score) (66.6%), Complexity Load (formerly Cognitive Load) (37.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addProduct` **(Many-Argument Workhorses)** (Impact: 46.6)
    * *Intent:* /** * Add product. Returns error message if product type instance can't prepare product. * * @param ...
  * `updateItem` **(Many-Argument Workhorses)** (Impact: 28.8)
    * *Intent:* * - 'files_prefix': string[a-z0-9_] - prefix that was added at frontend to names of file options (fi...
  * `validateMinimumAmount` **(Compute Cores)** (Impact: 26.4)
    * *Intent:* /** * Validate minimum amount. * * @param bool $multishipping * @return bool * @SuppressWarnings(PHP...
  * `removeErrorInfosByParams` **(Compute Cores)** (Impact: 22.5)
    * *Intent:* /** * Removes error infos, that have parameters equal to passed in $params. * $params can have follo...
  * `assignCustomerWithAddressChange` **(Defensive Guards)** (Impact: 22.2)
    * *Intent:* /** * Assign customer model to quote with billing and shipping address change * * @param \Magento\Cu...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 169 instances
* *State Mutation (weighted view):* 562
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 280`, `structural_boundaries: 344`, `args: 119`, `func_start: 119`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 224`, `dead_code: 1`, `planned_debt: 4`
* *Architecture:* `api: 111`, `import: 15`
* *Defense:* `safety: 33`, `doc: 187`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.854
  * `Choke Point (Betweenness):` 0.000152 | `Ripple Effect (Closeness):` 0.013309
  * `Imports (Out-Degree: 15):` Magento\Catalog\Model\Product\Attribute\Source\Status, Magento\Customer\Api\Data\CustomerInterface, Magento\Customer\Api\Data\GroupInterface, Magento\Directory\Model\AllowedCountries, Magento\Framework\Api\AttributeValueFactory, Magento\Framework\Api\ExtensionAttribute\JoinProcessorInterface, Magento\Framework\App\ObjectManager, Magento\Framework\DataObject...
  * `Imported By (In-Degree: 392):` (Excluded from Brief to save tokens)

### `lib/web/jquery/ui-modules/widgets/sortable.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.412)
- **Top Global Matches:** file_cluster_6: 7.412, file_cluster_8: 12.732, file_cluster_4: 13.695
- **Magnitude:** 1250.82 | **LOC:** 1609 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_clear` **(Many-Argument Workhorses)** (Impact: 54.6)
  * `_contactContainers` **(Compute Cores)** (Impact: 48.5)
  * `_mouseStart` **(Many-Argument Workhorses)** (Impact: 48.1)
  * `_generatePosition` **(Defensive Guards)** (Impact: 42.1)
  * `_mouseDrag` **(Defensive Guards)** (Impact: 37.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 171 instances
* *State Mutation (weighted view):* 548
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 357`, `structural_boundaries: 93`, `args: 65`, `func_start: 46`
* *Risk/State:* `state_mutation: 206`, `dead_code: 2`, `planned_debt: 2`, `unreferenced_by_name: 8`
* *Architecture:* None
* *Defense:* `safety: 111`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.013
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/code/Magento/Sales/Api/Data/OrderInterface.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 6.238)
- **Top Global Matches:** file_cluster_17: 6.238, file_cluster_15: 6.977, file_cluster_2: 6.98
- **Magnitude:** 1162.12 | **LOC:** 2630 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **218** in-repo importer(s); blast radius 0.51; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (44.5%), Complexity Load (formerly Cognitive Load) (3.2%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 277`, `args: 274`, `func_start: 274`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 274`
* *Defense:* `doc: 277`, `immutability_locks: 136`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.51
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.009718
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 218):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `app/code/Magento/Payment/Test/Unit/Model/PaymentMethodListTest.php` (PHP) | Magnitude: 65.74 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 162, structural_boundaries: 33, state_mutation: 18, test: 16
- `dev/tests/integration/testsuite/Magento/Swatches/_files/swatch_attribute.php` (PHP) | Magnitude: 34.24 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 41, state_mutation: 14, structural_boundaries: 11, args: 3
- `lib/web/mage/utils/template.js` (JAVASCRIPT) | Magnitude: 150.52 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 108, branch: 29, safety: 27, structural_boundaries: 24
- `app/design/adminhtml/Magento/backend/web/css/source/_actions.less` (CSS) | Magnitude: 22.82 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 333, closures: 47, class_start: 44, ui_framework: 7
- `app/code/Magento/Catalog/Test/Unit/Model/Product/Attribute/Backend/TierpriceTest.php` (PHP) | Magnitude: 53.18 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 172, structural_boundaries: 44, state_mutation: 24, test: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `app/code/Magento/Catalog/Block/Product/View/Options.php` (PHP) | Magnitude: 97.18 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 147, structural_boundaries: 29, state_mutation: 27, doc: 21
- `app/code/Magento/ConfigurableProduct/Test/Unit/Model/Plugin/PriceBackendTest.php` (PHP) | Magnitude: 14.4 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 20, import: 9, doc: 7
- `app/code/Magento/Customer/Test/Unit/Ui/Component/Listing/Column/ConfirmationTest.php` (PHP) | Magnitude: 22.78 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 73, structural_boundaries: 19, state_mutation: 11, import: 10
- `app/code/Magento/Wishlist/Block/AbstractBlock.php` (PHP) | Magnitude: 117.8 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 146, structural_boundaries: 57, doc: 32, args: 24
- `dev/tests/static/framework/tests/unit/testsuite/Magento/TestFramework/Dependency/VirtualType/VirtualTypeMapperTest.php` (PHP) | Magnitude: 44.34 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 125, structural_boundaries: 23, doc: 10, args: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `app/code/Magento/Store/Test/Unit/Model/Config/Processor/PlaceholderTest.php` (PHP) | Magnitude: 13.78 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 13, test: 6, state_mutation: 4
- `app/code/Magento/Bundle/view/adminhtml/templates/sales/creditmemo/view/items/renderer.phtml` (PHP) | Magnitude: 51.56 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 110, branch: 29, structural_boundaries: 22, ui_framework: 19
- `app/code/Magento/Customer/Block/Adminhtml/Grid/Renderer/Multiaction.php` (PHP) | Magnitude: 83.56 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 55, structural_boundaries: 16, branch: 15, state_mutation: 15
- `dev/tests/integration/testsuite/Magento/Customer/Block/Adminhtml/Edit/Tab/View/PersonalInfoTest.php` (PHP) | Magnitude: 87.36 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 186, state_mutation: 37, doc: 27, structural_boundaries: 24
- `app/code/Magento/Swatches/Block/Product/Renderer/Configurable.php` (PHP) | Magnitude: 229.78 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 247, structural_boundaries: 74, state_mutation: 47, doc: 39

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `app/code/Magento/Payment/Test/Unit/Model/Checks/CanUseForCurrencyTest.php` (PHP) | Magnitude: 11.44 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 15, test: 8, import: 6
- `app/code/Magento/Directory/Test/Unit/Model/Currency/Import/ConfigTest.php` (PHP) | Magnitude: 23.14 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 68, structural_boundaries: 29, args: 8, func_start: 8
- `dev/tests/integration/testsuite/Magento/CatalogSearch/Controller/Result/IndexTest.php` (PHP) | Magnitude: 6.82 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 9, doc: 4, args: 2
- `lib/internal/Magento/Framework/Data/Test/Unit/Form/FormKey/ValidatorTest.php` (PHP) | Magnitude: 11.08 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 15, test: 8, doc: 6
- `app/code/Magento/Directory/Test/Unit/Block/CurrencyTest.php` (PHP) | Magnitude: 16.4 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 40, structural_boundaries: 18, state_mutation: 10, test: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `setup/src/Magento/Setup/Test/Unit/Module/Di/Code/Scanner/XmlScannerTest.php` (PHP) | Magnitude: 29.48 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 47, structural_boundaries: 24, branch: 11, safety_bypasses: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `app/code/Magento/Sales/Model/ResourceModel/Order/Creditmemo/Comment/Collection.php` (PHP) | Magnitude: 6.42 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 9, doc: 6, encapsulation: 3
- `app/code/Magento/Sales/Model/ResourceModel/Order/Invoice/Comment/Collection.php` (PHP) | Magnitude: 6.42 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 9, doc: 6, encapsulation: 3
- `app/code/Magento/Catalog/Model/Category/Attribute/Backend/LayoutUpdate.php` (PHP) | Magnitude: 6.58 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 11, indent_spaces: 9, doc: 5, import: 4
- `app/code/Magento/Catalog/Model/Product/Attribute/Backend/LayoutUpdate.php` (PHP) | Magnitude: 6.58 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 11, indent_spaces: 9, doc: 5, import: 4
- `app/code/Magento/QuoteGraphQl/Plugin/ShippingMethodValidationRulePlugin.php` (PHP) | Magnitude: 44.76 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 12, branch: 9, state_mutation: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `app/code/Magento/Catalog/Test/Unit/Model/Product/Option/Type/FactoryTest.php` (PHP) | Magnitude: 21.34 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 55, structural_boundaries: 16, state_mutation: 10, test: 9
- `app/code/Magento/Shipping/Model/Shipping/LabelGenerator.php` (PHP) | Magnitude: 104.38 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 116, state_mutation: 29, structural_boundaries: 23, branch: 15
- `app/code/Magento/GiftMessage/Test/Unit/Model/GuestCartRepositoryTest.php` (PHP) | Magnitude: 22.34 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 68, structural_boundaries: 17, test: 14, state_mutation: 13
- `app/code/Magento/NewRelicReporting/Test/Unit/Model/Observer/ReportProductDeletedToNewRelicTest.php` (PHP) | Magnitude: 13.26 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 41, structural_boundaries: 14, doc: 9, test: 7
- `app/code/Magento/Sales/Test/Unit/Controller/Adminhtml/Order/Create/LoadBlockTest.php` (PHP) | Magnitude: 113.64 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 468, test: 82, structural_boundaries: 65, state_mutation: 53

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `app/code/Magento/Customer/Model/AuthenticationInterface.php` (PHP) | Magnitude: 32.08 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 8, doc: 6, args: 4, func_start: 4
- `dev/tests/integration/testsuite/Magento/GraphQl/Tax/_files/tax_rule_for_region_1_rollback.php` (PHP) | Magnitude: 24.5 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 13, import: 11, state_mutation: 9, doc: 7
- `dev/tests/integration/testsuite/Magento/GraphQl/Tax/_files/tax_rule_for_region_al_rollback.php` (PHP) | Magnitude: 24.5 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 13, import: 11, state_mutation: 9, doc: 7
- `dev/tests/integration/testsuite/Magento/GraphQl/Tax/_files/tax_rule_for_region_with_translated_titles_rollback.php` (PHP) | Magnitude: 24.5 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 13, import: 11, state_mutation: 9, doc: 7
- `dev/tests/integration/testsuite/Magento/CatalogRule/_files/rule_adjust_final_price_to_discount_value_not_logged_user.php` (PHP) | Magnitude: 22.66 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 8, state_mutation: 7, import: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `app/code/Magento/Bundle/Plugin/Framework/Data/Form/Element/FieldsetPlugin.php` (PHP) | Magnitude: 17.34 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 9, state_mutation: 4, doc: 4
- `app/code/Magento/Ui/view/base/web/templates/grid/cells/multiselect.html` (HTML) | Magnitude: 15.22 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 9, args: 4, core_var_decl: 3, design_snake_case: 3
- `app/code/Magento/AdvancedSearch/Test/Unit/Controller/Adminhtml/Search/System/Config/TestConnectionTest.php` (PHP) | Magnitude: 27.02 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 91, structural_boundaries: 25, test: 20, state_mutation: 13
- `app/code/Magento/UrlRewriteGraphQl/Test/Unit/Model/Resolver/AbstractEntityUrlTest.php` (PHP) | Magnitude: 199.28 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 533, state_mutation: 91, structural_boundaries: 66, doc: 30
- `app/code/Magento/Catalog/Test/Unit/Model/Layer/Filter/AttributeTest.php` (PHP) | Magnitude: 42.14 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 133, structural_boundaries: 34, state_mutation: 26, test: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `lib/web/jquery/ui-modules/effect.js` (JAVASCRIPT) | Magnitude: 636.74 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 704, branch: 157, state_mutation: 107, core_var_decl: 107
- `app/code/Magento/Ui/view/base/web/js/core/renderer/layout.js` (JAVASCRIPT) | Magnitude: 344.64 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 354, branch: 72, state_mutation: 57, core_var_decl: 55
- `app/code/Magento/Catalog/Model/Category/DataProvider.php` (PHP) | Magnitude: 516.32 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 372, state_mutation: 114, branch: 82, structural_boundaries: 82
- `app/code/Magento/Catalog/Model/ResourceModel/Category/Collection.php` (PHP) | Magnitude: 384.78 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 422, structural_boundaries: 81, state_mutation: 74, branch: 54
- `app/code/Magento/Shipping/view/adminhtml/web/order/packaging.js` (JAVASCRIPT) | Magnitude: 600.86 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 736, branch: 147, structural_boundaries: 131, core_var_decl: 131

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `app/code/Magento/Webapi/Model/ServiceMetadata.php` (PHP) | Magnitude: 245.6 | Delta: **0.154** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 191, state_mutation: 55, branch: 39, structural_boundaries: 38

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `app/code/Magento/AdminNotification/view/adminhtml/templates/toolbar_entry.phtml` (PHP) | Magnitude: 24.52 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 72, core_var_decl: 23, design_snake_case: 23, structural_boundaries: 18
- `app/code/Magento/Bundle/Model/Product/Attribute/Source/Shipment/Type.php` (PHP) | Magnitude: 12.68 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 9, doc: 4, branch: 3
- `app/code/Magento/Store/Model/Config/Validator.php` (PHP) | Magnitude: 11.36 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 9, branch: 4, doc: 3
- `app/code/Magento/Backend/Block/Widget/Button/Toolbar.php` (PHP) | Magnitude: 52.3 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 12, branch: 10, state_mutation: 9
- `dev/tests/integration/testsuite/Magento/Customer/Controller/Adminhtml/Index/InlineEditTest.php` (PHP) | Magnitude: 47.04 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 117, structural_boundaries: 32, state_mutation: 21, doc: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `app/code/Magento/GiftMessageGraphQl/Model/Resolver/Cart/Item/GiftMessage.php` (PHP) | Magnitude: 45.28 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 17, branch: 10, safety: 10
- `lib/internal/Magento/Framework/View/Element/Text/TextList/Link.php` (PHP) | Magnitude: 22.84 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 10, branch: 8, doc: 4
- `app/code/Magento/CatalogInventory/view/adminhtml/web/js/components/use-config-min-sale-qty.js` (JAVASCRIPT) | Magnitude: 38.04 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 49, branch: 17, args: 6, closures: 6
- `lib/internal/Magento/Framework/Filesystem/Directory/PathValidator.php` (PHP) | Magnitude: 37.82 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 11, branch: 6, state_mutation: 6
- `lib/internal/Magento/Framework/GraphQl/Config/Element/ArgumentFactory.php` (PHP) | Magnitude: 19.04 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 25, safety: 9, branch: 8, structural_boundaries: 7

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `app/code/Magento/Ups/Model/Carrier.php` -> **Rajesh Kumar** (100.0% isolated ownership) | Magnitude: 2205.12
- `app/code/Magento/CatalogImportExport/Model/Import/Product.php` -> **Rajesh Kumar** (100.0% isolated ownership) | Magnitude: 2034.9
- `app/code/Magento/Sales/Model/Order.php` -> **Rajesh Kumar** (100.0% isolated ownership) | Magnitude: 1652.06
- `app/code/Magento/CatalogImportExport/Model/Import/Product/Option.php` -> **Rajesh Kumar** (100.0% isolated ownership) | Magnitude: 1483.74
- `app/code/Magento/Catalog/Model/ResourceModel/Product/Collection.php` -> **Rajesh Kumar** (100.0% isolated ownership) | Magnitude: 1470.46

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `app/code/Magento/Catalog/Model/ResourceModel/Product/Collection.php` -> **Severity: 0.227** (Bridge: 0.0023 * Flux: 100.0%)
- `lib/internal/Magento/Framework/Session/SessionManager.php` -> **Severity: 0.204** (Bridge: 0.002 * Flux: 99.9998%)
- `app/code/Magento/Eav/Model/Config.php` -> **Severity: 0.192** (Bridge: 0.0019 * Flux: 100.0%)
- `app/code/Magento/Catalog/Model/Category.php` -> **Severity: 0.185** (Bridge: 0.0019 * Flux: 99.9998%)
- `app/code/Magento/CatalogUrlRewrite/Model/CategoryUrlRewriteGenerator.php` -> **Severity: 0.181** (Bridge: 0.0018 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `lib/internal/Magento/Framework/Exception/LocalizedException.php` -> **Severity: 8.866** (Embedded: 0.1604 * Error Risk: 55.2661%)
- `lib/internal/Magento/Framework/App/ObjectManager.php` -> **Severity: 7.183** (Embedded: 0.1441 * Error Risk: 49.8571%)
- `lib/internal/Magento/Framework/Phrase/Renderer/Placeholder.php` -> **Severity: 6.765** (Embedded: 0.1194 * Error Risk: 56.6742%)
- `lib/internal/Magento/Framework/Phrase.php` -> **Severity: 6.393** (Embedded: 0.1308 * Error Risk: 48.8734%)
- `lib/internal/Magento/Framework/Profiler.php` -> **Severity: 6.158** (Embedded: 0.0826 * Error Risk: 74.5466%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `dev/tests/integration/testsuite/Magento/Framework/Session/SessionManagerTest.php` -> **Severity: 815.303** (Blast Radius: 11.356 * Doc Risk: 71.7949%)
- `lib/internal/Magento/Framework/Code/Test/Unit/Generator/DefinedClassesTest.php` -> **Severity: 52.867** (Blast Radius: 0.793 * Doc Risk: 66.6667%)
- `app/code/Magento/Captcha/Test/Unit/Cron/DeleteExpiredImagesTest.php` -> **Severity: 32.314** (Blast Radius: 0.754 * Doc Risk: 42.8571%)
- `lib/internal/Magento/Framework/Session/Test/Unit/SessionManagerTest.php` -> **Severity: 9.2** (Blast Radius: 0.184 * Doc Risk: 50.0%)
- `app/code/Magento/Integration/Api/Data/UserToken.php` -> **Severity: 4.133** (Blast Radius: 0.062 * Doc Risk: 66.6667%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 761 literal sites + 2 sites through wrappers = 763

- `setLocalStorageItem` (function, debug_prints, primitive): 1 call sites in 1 files -- `app/code/Magento/Catalog/view/frontend/web/js/product/storage/data-storage.js`
- `setLocalStorageItem` (function, debug_prints, primitive): 1 call sites in 1 files -- `app/code/Magento/Catalog/view/frontend/web/js/product/storage/ids-storage.js`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 438768 call pairs -- scoped 25.5%, unique 0.5%, ambiguous 32.6%, external 41.5%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| php | 411584 | 26.8% | 0.5% | 34.7% | 38.0% |
| javascript | 27184 | 5.5% | 0.0% | 1.0% | 93.5% |

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
