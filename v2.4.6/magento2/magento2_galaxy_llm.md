# ARCHITECTURAL_BRIEF: magento2
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_php/magento2` |
| **Timestamp** | `2026-08-03T19:32:34.664625+00:00` |
| **Scan Duration** | `62.76s` |
| **Git Branch** | `2.4-develop` |
| **Git Commit** | `8d95ae6ee2a7dc1960f8f853af011fbabec2e0f0` |
| **Git Remote** | `https://github.com/magento/magento2.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 15236 malicious artifacts.

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
| Total Artifacts | 41590 |
| Analyzed Artifacts (Scanned) | 19454 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 22136 |
| Total LOC | 901782 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 46.8% |
| Dominant Lang | PHP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0378 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 1239 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PHP | 14550 | 766583 | 74.8% |
| XML | 2215 | 10 | 11.4% |
| JAVASCRIPT | 685 | 46224 | 3.5% |
| PLAINTEXT | 407 | 2 | 2.1% |
| JSON | 381 | 17757 | 2.0% |
| CSS | 344 | 50789 | 1.8% |
| CSV | 324 | 13105 | 1.7% |
| HTML | 320 | 7312 | 1.6% |
| MARKDOWN | 227 | 0 | 1.2% |
| SQLITE | 1 | 0 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.519`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 10991 | 56.5% |
| file_cluster_13 | 6740 | 34.6% |
| file_cluster_2 | 762 | 3.9% |
| file_cluster_7 | 138 | 0.7% |
| file_cluster_0 | 49 | 0.3% |
| file_cluster_1 | 43 | 0.2% |
| file_cluster_15 | 43 | 0.2% |
| file_cluster_17 | 14 | 0.1% |
| file_cluster_4 | 12 | 0.1% |
| file_cluster_6 | 4 | 0.0% |
| file_cluster_5 | 1 | 0.0% |
| file_cluster_9 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 633 | 3.3% |
| Static: Minified & Vendor Opaque Mass | 23 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 22136*

**Composition by Extension & Reason:**
- `.php`: 11740x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 50 LOC), 1x Excluded (Machine-Generated Source Code Signature: 39 LOC)
- `.xml`: 7627x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 85 exceeds 500 chars), 1x Excluded (Static Asset Blob without Intent: 1880 LOC)
- `.js`: 867x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1039 LOC), 1x Excluded (Saturation: Line 8 exceeds 500 chars)
- `.txt`: 325x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 225x Excluded (Explicitly Denied Extension: '.png')
- `.md`: 208x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 7978 LOC), 1x Excluded (Machine-Generated Source Code Signature: 57 LOC)
- `no_extension`: 192x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Unsupported Format (.undeterminable)
- `.less`: 152x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gif`: 114x Excluded (Explicitly Denied Extension: '.gif')
- `.html`: 111x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.css`: 87x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 6 exceeds 500 chars), 1x Excluded (Saturation: Line 2 exceeds 500 chars)
- `.xsd`: 79x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.phtml`: 71x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 46 exceeds 500 chars), 1x Excluded (Saturation: Line 12 exceeds 500 chars)
- `.jpg`: 65x Excluded (Explicitly Denied Extension: '.jpg')
- `.graphqls`: 48x Excluded (Unsupported Extension: '.graphqls')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 93.1 | 16.8 | 9.1 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 13.4 | 8.6 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 29.1 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 13.8 | 2.3 | 0.0 |
| API Exposure | 0.0 | 15.1 | 2.3 | 1.5 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 0.6 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 46.4 | 23.7 | 0.0 |
| Commented Logic Exposure | 0.0 | 64.6 | 0.1 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 78.6 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 24.9 | 0.1 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 29.3 | 11.9 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 46.9 | 15.8 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 28.6 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.6 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `app/code/Magento/MediaGalleryUi/view/adminhtml/web/js/directory/directoryTree.js` (Hits: 32)
- `dev/tools/grunt/configs/clean.js` (Hits: 31)
- `lib/web/mage/utils/objects.js` (Hits: 24)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **ObjectManager.php** (`dev/tests/integration/framework/Magento/TestFramework/ObjectManager.php`) — 1084 inbound connections
2. **Bootstrap.php** (`dev/tests/integration/framework/Magento/TestFramework/Helper/Bootstrap.php`) — 1022 inbound connections
3. **Resolver.php** (`dev/tests/integration/framework/Magento/TestFramework/Workaround/Override/Fixture/Resolver.php`) — 829 inbound connections
4. **ProductRepositoryInterface.php** (`app/code/Magento/Catalog/Api/ProductRepositoryInterface.php`) — 512 inbound connections
5. **StoreManagerInterface.php** (`app/code/Magento/Store/Model/StoreManagerInterface.php`) — 467 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **schema_response_sdl_description.php** (`dev/tests/integration/testsuite/Magento/Framework/GraphQl/_files/schema_response_sdl_description.php`) — 344 outbound dependencies
2. **schema_with_description_sdl.php** (`dev/tests/integration/testsuite/Magento/Framework/GraphQl/_files/schema_with_description_sdl.php`) — 344 outbound dependencies
3. **CategorySetup.php** (`app/code/Magento/Catalog/Setup/CategorySetup.php`) — 286 outbound dependencies
4. **InstallerTest.php** (`setup/src/Magento/Setup/Test/Unit/Model/InstallerTest.php`) — 157 outbound dependencies
5. **CustomerSetup.php** (`app/code/Magento/Customer/Setup/CustomerSetup.php`) — 155 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `require` (@ `app/code/Magento/Downloadable/view/adminhtml/templates/product/edit/downloadable/links.phtml`) -> Impact: **1690.8** | LOC: 385
- `define` (@ `app/code/Magento/Ui/view/base/web/js/form/element/ui-select.js`) -> Impact: **1631.7** | LOC: 942
  * *Intent:* /** * Copyright 2015 Adobe * All Rights Reserved.
- `define` (@ `app/code/Magento/Swatches/view/base/web/js/swatch-renderer.js`) -> Impact: **1615.0** | LOC: 941
  * *Intent:* /** * Copyright 2015 Adobe
- `define` (@ `app/code/Magento/ProductVideo/view/adminhtml/web/js/new-video-dialog.js`) -> Impact: **1254.1** | LOC: 1170
  * *Intent:* /**
- `define` (@ `app/code/Magento/ConfigurableProduct/view/frontend/web/js/configurable.js`) -> Impact: **1207.7** | LOC: 567
  * *Intent:* /** * Copyright 2012 Adobe
- `createExportRow` (@ `app/code/Magento/AdvancedPricingImportExport/Model/Export/AdvancedPricing.php`) -> Impact: **964.9** | LOC: 258
- `define` (@ `app/code/Magento/Shipping/view/adminhtml/web/order/packaging.js`) -> Impact: **948.7** | LOC: 908
  * *Intent:* /** * Copyright 2014 Adobe
- `initFromOrder` (@ `app/code/Magento/Sales/Model/AdminOrder/Create.php`) -> Impact: **932.8** | LOC: 736
- `define` (@ `app/code/Magento/Swatches/view/adminhtml/web/js/product-attributes.js`) -> Impact: **929.4** | LOC: 437
  * *Intent:* /** * Copyright 2015 Adobe * All Rights Reserved.
- `define` (@ `app/code/Magento/Catalog/view/adminhtml/web/catalog/product/composite/configure.js`) -> Impact: **875.5** | LOC: 482
  * *Intent:* /** * Copyright 2014 Adobe * All Rights Reserved.

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `_afterLoad` (@ `app/code/Magento/AdminNotification/Model/ResourceModel/System/Message/Collection/Synchronized.php`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * @api * @since 100.0.2 */
- `createExportRow` (@ `app/code/Magento/AdvancedPricingImportExport/Model/Export/AdvancedPricing.php`) -> **O(2^N) [Recursive]**
- `addFieldToFilter` (@ `app/code/Magento/AsynchronousOperations/Ui/Component/DataProvider/SearchResult.php`) -> **O(2^N) [Recursive]**
- `prepareDataSource` (@ `app/code/Magento/AsynchronousOperations/Ui/Component/Listing/Column/NotificationActions.php`) -> **O(2^N) [Recursive]**
  * *Intent:* /**
- `prepareDataSource` (@ `app/code/Magento/AsynchronousOperations/Ui/Component/Listing/Column/NotificationDismissActions.php`) -> **O(2^N) [Recursive]**
  * *Intent:* /**
- `_construct` (@ `app/code/Magento/Backend/Block/Cache.php`) -> **O(2^N) [Recursive]**
  * *Intent:* /**
- `getValue` (@ `app/code/Magento/Backend/Block/Widget/Grid/Column/Filter/Datetime.php`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * Date grid column filter * * @todo date format
- `_prepareLayout` (@ `app/code/Magento/Backend/Block/Widget/Grid/Container.php`) -> **O(2^N) [Recursive]**
- `_construct` (@ `app/code/Magento/Backend/Block/Widget/Grid/Export.php`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * Template file name * * @var string
- `login` (@ `app/code/Magento/Backend/Model/Auth.php`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * Set auth storage if it is instance of \Magento\Backend\Model\Auth\StorageInterface * * @param \Magento\Backend\Model\Auth\StorageInterface $stor...

### Highest Data Gravity (Database Complexity)
- `define` (@ `app/code/Magento/ProductVideo/view/adminhtml/web/js/new-video-dialog.js`) -> DB Complexity: **311**
  * *Intent:* /**
- `define` (@ `app/code/Magento/Ui/view/base/web/js/form/element/ui-select.js`) -> DB Complexity: **293**
  * *Intent:* /** * Copyright 2015 Adobe * All Rights Reserved.
- `define` (@ `app/code/Magento/Shipping/view/adminhtml/web/order/packaging.js`) -> DB Complexity: **287**
  * *Intent:* /** * Copyright 2014 Adobe
- `define` (@ `app/code/Magento/MediaGalleryUi/view/adminhtml/web/js/directory/directoryTree.js`) -> DB Complexity: **218**
  * *Intent:* /** * Copyright 2020 Adobe * All Rights Reserved.
- `define` (@ `app/code/Magento/Ui/view/base/web/js/modal/modal.js`) -> DB Complexity: **182**
  * *Intent:* /** * Copyright 2015 Adobe * All Rights Reserved.
- `define` (@ `app/code/Magento/Swatches/view/base/web/js/swatch-renderer.js`) -> DB Complexity: **168**
  * *Intent:* /** * Copyright 2015 Adobe
- `define` (@ `app/code/Magento/Catalog/view/adminhtml/web/js/product-gallery.js`) -> DB Complexity: **166**
  * *Intent:* /** * Copyright 2014 Adobe * All Rights Reserved.
- `define` (@ `app/code/Magento/ConfigurableProduct/view/adminhtml/web/js/components/dynamic-rows-configurable.js`) -> DB Complexity: **156**
  * *Intent:* /** * Copyright 2016 Adobe
- `define` (@ `app/code/Magento/ProductVideo/view/adminhtml/web/js/get-video-information.js`) -> DB Complexity: **152**
  * *Intent:* /**
- `define` (@ `app/code/Magento/ProductVideo/view/frontend/web/js/fotorama-add-video-events.js`) -> DB Complexity: **151**
  * *Intent:* /** * Copyright 2015 Adobe

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `app/code/Magento/Sales/Model/Order` | 46 | 11580.36 | 21.61% | 32.51% |
| `dev/tests/integration/testsuite/Magento/Catalog/_files` | 419 | 9978.58 | 19.8% | 0.0% |
| `app/code/Magento/Paypal/Model` | 25 | 8029.9 | 26.94% | 41.52% |
| `app/code/Magento/Customer/Model` | 43 | 7616.96 | 24.72% | 13.69% |
| `app/code/Magento/Catalog/Model` | 50 | 7213.8 | 21.1% | 36.33% |
| `app/code/Magento/Sales/Api/Data` | 51 | 6693.77 | 4.56% | 0.0% |
| `app/code/Magento/Ui/view/base/web/js/form/element` | 23 | 6158.52 | 30.6% | 43.16% |
| `app/code/Magento/Catalog/Model/ResourceModel/Product` | 20 | 5895.1 | 30.25% | 38.86% |
| `app/code/Magento/CatalogImportExport/Model/Import/Product` | 15 | 5730.84 | 30.48% | 14.32% |
| `app/code/Magento/Quote/Model` | 38 | 5704.6 | 21.17% | 46.69% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `app/code/Magento/AdminNotification/Model/System/Message.php` -> **100.0%** Exposure
- `app/code/Magento/Analytics/Model/Connector/Http/JsonConverter.php` -> **100.0%** Exposure
- `app/code/Magento/Analytics/Model/EncodedContext.php` -> **100.0%** Exposure
- `app/code/Magento/Analytics/Model/FileInfo.php` -> **100.0%** Exposure
- `app/code/Magento/ApplicationPerformanceMonitor/Profiler/Metrics.php` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `app/autoload.php` -> **100.0%** Exposure
- `app/code/Magento/AdminAnalytics/Controller/Adminhtml/Config/DisableAdminUsage.php` -> **100.0%** Exposure
- `app/code/Magento/AdminAnalytics/Controller/Adminhtml/Config/EnableAdminUsage.php` -> **100.0%** Exposure
- `app/code/Magento/AdminAnalytics/view/adminhtml/templates/notification.phtml` -> **100.0%** Exposure
- `app/code/Magento/AdminAnalytics/view/adminhtml/templates/tracking.phtml` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `app/code/Magento/Quote/Model/Cart/Totals/Item.php` -> **44** Orphaned Functions | **0** Duplicates
- `app/code/Magento/Vault/Model/Method/NullPaymentProvider.php` -> **42** Orphaned Functions | **0** Duplicates
- `app/code/Magento/Sales/Model/Order/ShippingTotal.php` -> **38** Orphaned Functions | **0** Duplicates
- `app/code/Magento/Tax/Model/TaxDetails/ItemDetails.php` -> **28** Orphaned Functions | **0** Duplicates
- `app/code/Magento/Sales/Model/Data/Order/Tax/Item.php` -> **25** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`app/code/Magento/Backend/view/adminhtml/templates/widget/form/element.phtml`** -> AI Confidence: **99.48%**
2. **`app/code/Magento/Backend/view/adminhtml/templates/widget/grid/serializer.phtml`** -> AI Confidence: **99.48%**
3. **`app/code/Magento/Backend/view/adminhtml/templates/widget/tabshoriz.phtml`** -> AI Confidence: **99.48%**
4. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/attribute/js.phtml`** -> AI Confidence: **99.48%**
5. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/composite/fieldset/options/type/date.phtml`** -> AI Confidence: **99.48%**
6. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/edit.phtml`** -> AI Confidence: **99.48%**
7. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/edit/price/tier.phtml`** -> AI Confidence: **99.48%**
8. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/tab/inventory.phtml`** -> AI Confidence: **99.48%**
9. **`app/code/Magento/Catalog/view/base/templates/product/price/tier_prices.phtml`** -> AI Confidence: **99.48%**
10. **`app/code/Magento/CatalogSearch/view/frontend/templates/advanced/form.phtml`** -> AI Confidence: **99.48%**
11. **`app/code/Magento/CatalogUrlRewrite/view/adminhtml/templates/confirm.phtml`** -> AI Confidence: **99.48%**
12. **`app/code/Magento/Config/view/adminhtml/templates/system/config/edit.phtml`** -> AI Confidence: **99.48%**
13. **`app/code/Magento/ConfigurableProduct/view/adminhtml/templates/catalog/product/edit/super/wizard-ajax.phtml`** -> AI Confidence: **99.48%**
14. **`app/code/Magento/ConfigurableProduct/view/adminhtml/templates/product/configurable/affected-attribute-set-selector/js.phtml`** -> AI Confidence: **99.48%**
15. **`app/code/Magento/Customer/view/frontend/templates/address/edit.phtml`** -> AI Confidence: **99.48%**
16. **`app/code/Magento/Customer/view/frontend/templates/form/register.phtml`** -> AI Confidence: **99.48%**
17. **`app/code/Magento/Downloadable/view/adminhtml/templates/product/edit/downloadable.phtml`** -> AI Confidence: **99.48%**
18. **`app/code/Magento/Email/view/adminhtml/templates/template/edit.phtml`** -> AI Confidence: **99.48%**
19. **`app/code/Magento/ImportExport/view/adminhtml/templates/import/form/before.phtml`** -> AI Confidence: **99.48%**
20. **`app/code/Magento/Integration/view/adminhtml/templates/integration/popup_container.phtml`** -> AI Confidence: **99.48%**
21. **`app/code/Magento/MediaStorage/Model/File/Validator/AvailablePath.php`** -> AI Confidence: **99.48%**
22. **`app/code/Magento/MediaStorage/view/adminhtml/templates/system/config/system/storage/media/synchronize.phtml`** -> AI Confidence: **99.48%**
23. **`app/code/Magento/Newsletter/view/adminhtml/templates/template/edit.phtml`** -> AI Confidence: **99.48%**
24. **`app/code/Magento/Payment/view/adminhtml/templates/transparent/form.phtml`** -> AI Confidence: **99.48%**
25. **`app/code/Magento/Payment/view/frontend/templates/form/cc.phtml`** -> AI Confidence: **99.48%**
26. **`app/code/Magento/Payment/view/frontend/templates/transparent/form.phtml`** -> AI Confidence: **99.48%**
27. **`app/code/Magento/Payment/view/frontend/templates/transparent/iframe.phtml`** -> AI Confidence: **99.48%**
28. **`app/code/Magento/Paypal/view/adminhtml/templates/transparent/form.phtml`** -> AI Confidence: **99.48%**
29. **`app/code/Magento/Paypal/view/frontend/templates/payflowlink/redirect.phtml`** -> AI Confidence: **99.48%**
30. **`app/code/Magento/Reports/view/adminhtml/templates/grid.phtml`** -> AI Confidence: **99.48%**
31. **`app/code/Magento/Sales/view/adminhtml/templates/order/create/billing/method/form.phtml`** -> AI Confidence: **99.48%**
32. **`app/code/Magento/Sales/view/adminhtml/templates/order/create/coupons/form.phtml`** -> AI Confidence: **99.48%**
33. **`app/code/Magento/Sales/view/adminhtml/templates/order/create/shipping/method/form.phtml`** -> AI Confidence: **99.48%**
34. **`app/code/Magento/Sales/view/adminhtml/templates/order/create/sidebar.phtml`** -> AI Confidence: **99.48%**
35. **`app/code/Magento/Sales/view/adminhtml/templates/order/create/totals/grandtotal.phtml`** -> AI Confidence: **99.48%**
36. **`app/code/Magento/SalesRule/view/adminhtml/templates/promo/salesrulejs.phtml`** -> AI Confidence: **99.48%**
37. **`app/code/Magento/Tax/view/adminhtml/templates/rate/js.phtml`** -> AI Confidence: **99.48%**
38. **`app/code/Magento/Tax/view/adminhtml/templates/rule/edit.phtml`** -> AI Confidence: **99.48%**
39. **`app/code/Magento/TaxImportExport/view/adminhtml/templates/importExport.phtml`** -> AI Confidence: **99.48%**
40. **`app/code/Magento/Theme/view/adminhtml/templates/tabs/css.phtml`** -> AI Confidence: **99.48%**
41. **`app/code/Magento/Theme/view/adminhtml/templates/tabs/js.phtml`** -> AI Confidence: **99.48%**
42. **`app/code/Magento/Theme/view/frontend/templates/js/calendar.phtml`** -> AI Confidence: **99.48%**
43. **`app/code/Magento/User/view/adminhtml/templates/role/users_grid_js.phtml`** -> AI Confidence: **99.48%**
44. **`app/code/Magento/Widget/view/adminhtml/templates/instance/js.phtml`** -> AI Confidence: **99.48%**
45. **`dev/tests/integration/testsuite/Magento/Framework/GraphQl/_files/schema_response_sdl_description.php`** -> AI Confidence: **99.48%**
46. **`dev/tests/integration/testsuite/Magento/Framework/GraphQl/_files/schema_with_description_sdl.php`** -> AI Confidence: **99.48%**
47. **`app/code/Magento/Bundle/view/adminhtml/templates/product/edit/bundle/option.phtml`** -> AI Confidence: **99.39%**
48. **`app/code/Magento/Bundle/view/adminhtml/templates/product/edit/bundle/option/selection.phtml`** -> AI Confidence: **99.39%**
49. **`app/code/Magento/Customer/view/frontend/templates/form/edit.phtml`** -> AI Confidence: **99.39%**
50. **`app/code/Magento/Sales/view/adminhtml/templates/order/creditmemo/create/items.phtml`** -> AI Confidence: **99.39%**
51. **`app/code/Magento/Shipping/view/adminhtml/templates/order/packaging/popup_content.phtml`** -> AI Confidence: **99.39%**
52. **`app/code/Magento/Shipping/view/adminhtml/templates/order/tracking/view.phtml`** -> AI Confidence: **99.39%**
53. **`app/code/Magento/Webapi/Model/Soap/Wsdl/ComplexTypeStrategy.php`** -> AI Confidence: **99.39%**
54. **`app/code/Magento/Backend/view/adminhtml/templates/widget/form/container.phtml`** -> AI Confidence: **99.34%**
55. **`app/code/Magento/Backend/view/adminhtml/templates/widget/grid.phtml`** -> AI Confidence: **99.34%**
56. **`app/code/Magento/Backend/view/adminhtml/templates/widget/tabs.phtml`** -> AI Confidence: **99.34%**
57. **`app/code/Magento/Captcha/view/adminhtml/templates/default.phtml`** -> AI Confidence: **99.34%**
58. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/category/tree.phtml`** -> AI Confidence: **99.34%**
59. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/edit/options/option.phtml`** -> AI Confidence: **99.34%**
60. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/js.phtml`** -> AI Confidence: **99.34%**
61. **`app/code/Magento/CatalogWidget/view/adminhtml/templates/product/widget/conditions.phtml`** -> AI Confidence: **99.34%**
62. **`app/code/Magento/CatalogWidget/view/frontend/templates/product/widget/content/grid.phtml`** -> AI Confidence: **99.34%**
63. **`app/code/Magento/ConfigurableProduct/view/adminhtml/templates/catalog/product/attribute/set/js.phtml`** -> AI Confidence: **99.34%**
64. **`app/code/Magento/ConfigurableProduct/view/adminhtml/templates/catalog/product/composite/fieldset/configurable.phtml`** -> AI Confidence: **99.34%**
65. **`app/code/Magento/Customer/view/adminhtml/templates/tab/cart.phtml`** -> AI Confidence: **99.34%**
66. **`app/code/Magento/Customer/view/frontend/templates/widget/dob.phtml`** -> AI Confidence: **99.34%**
67. **`app/code/Magento/Customer/view/frontend/templates/widget/name.phtml`** -> AI Confidence: **99.34%**
68. **`app/code/Magento/Directory/view/adminhtml/templates/js/optional_zip_countries.phtml`** -> AI Confidence: **99.34%**
69. **`app/code/Magento/Downloadable/view/adminhtml/templates/product/composite/fieldset/downloadable.phtml`** -> AI Confidence: **99.34%**
70. **`app/code/Magento/Newsletter/view/adminhtml/templates/queue/edit.phtml`** -> AI Confidence: **99.34%**
71. **`app/code/Magento/Reports/view/adminhtml/templates/report/grid/container.phtml`** -> AI Confidence: **99.34%**
72. **`app/code/Magento/Review/view/adminhtml/templates/add.phtml`** -> AI Confidence: **99.34%**
73. **`app/code/Magento/Sales/view/adminhtml/templates/order/create/items/grid.phtml`** -> AI Confidence: **99.34%**
74. **`app/code/Magento/Sales/view/adminhtml/templates/order/create/js.phtml`** -> AI Confidence: **99.34%**
75. **`app/code/Magento/Sales/view/adminhtml/templates/order/creditmemo/create/totals/adjustments.phtml`** -> AI Confidence: **99.34%**
76. **`app/code/Magento/Shipping/view/adminhtml/templates/order/packaging/popup.phtml`** -> AI Confidence: **99.34%**
77. **`app/code/Magento/Swatches/view/frontend/templates/product/layered/renderer.phtml`** -> AI Confidence: **99.34%**
78. **`lib/web/mage/utils/main.js`** -> AI Confidence: **99.34%**
79. **`app/bootstrap.php`** -> AI Confidence: **99.32%**
80. **`app/code/Magento/Backend/view/adminhtml/templates/system/cache/edit.phtml`** -> AI Confidence: **99.32%**
81. **`app/code/Magento/Backend/view/adminhtml/templates/system/design/edit.phtml`** -> AI Confidence: **99.32%**
82. **`app/code/Magento/Backend/view/adminhtml/templates/widget/accordion.phtml`** -> AI Confidence: **99.32%**
83. **`app/code/Magento/Backend/view/adminhtml/templates/widget/grid/extended.phtml`** -> AI Confidence: **99.32%**
84. **`app/code/Magento/Backend/view/adminhtml/templates/widget/grid/massaction_extended.phtml`** -> AI Confidence: **99.32%**
85. **`app/code/Magento/Bundle/view/adminhtml/templates/catalog/product/edit/tab/attributes/extend.phtml`** -> AI Confidence: **99.32%**
86. **`app/code/Magento/Bundle/view/adminhtml/templates/product/edit/bundle.phtml`** -> AI Confidence: **99.32%**
87. **`app/code/Magento/Bundle/view/adminhtml/templates/product/stock/disabler.phtml`** -> AI Confidence: **99.32%**
88. **`app/code/Magento/Bundle/view/adminhtml/templates/sales/creditmemo/create/items/renderer.phtml`** -> AI Confidence: **99.32%**
89. **`app/code/Magento/Bundle/view/adminhtml/templates/sales/creditmemo/view/items/renderer.phtml`** -> AI Confidence: **99.32%**
90. **`app/code/Magento/Bundle/view/adminhtml/templates/sales/invoice/create/items/renderer.phtml`** -> AI Confidence: **99.32%**
91. **`app/code/Magento/Bundle/view/adminhtml/templates/sales/invoice/view/items/renderer.phtml`** -> AI Confidence: **99.32%**
92. **`app/code/Magento/Bundle/view/adminhtml/templates/sales/order/view/items/renderer.phtml`** -> AI Confidence: **99.32%**
93. **`app/code/Magento/Bundle/view/adminhtml/templates/sales/shipment/create/items/renderer.phtml`** -> AI Confidence: **99.32%**
94. **`app/code/Magento/Bundle/view/adminhtml/templates/sales/shipment/view/items/renderer.phtml`** -> AI Confidence: **99.32%**
95. **`app/code/Magento/Bundle/view/frontend/templates/catalog/product/view/type/bundle/option/radio.phtml`** -> AI Confidence: **99.32%**
96. **`app/code/Magento/Captcha/view/frontend/templates/default.phtml`** -> AI Confidence: **99.32%**
97. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/attribute/set/toolbar/add.phtml`** -> AI Confidence: **99.32%**
98. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/helper/gallery.phtml`** -> AI Confidence: **99.32%**
99. **`app/code/Magento/Config/view/adminhtml/templates/system/config/form/field/array.phtml`** -> AI Confidence: **99.32%**
100. **`app/code/Magento/ConfigurableProduct/view/adminhtml/templates/product/configurable/stock/disabler.phtml`** -> AI Confidence: **99.32%**
101. **`app/code/Magento/CurrencySymbol/view/adminhtml/templates/system/currency/rate/matrix.phtml`** -> AI Confidence: **99.32%**
102. **`app/code/Magento/Downloadable/view/adminhtml/templates/sales/items/column/downloadable/creditmemo/name.phtml`** -> AI Confidence: **99.32%**
103. **`app/code/Magento/Downloadable/view/adminhtml/templates/sales/items/column/downloadable/invoice/name.phtml`** -> AI Confidence: **99.32%**
104. **`app/code/Magento/GiftMessage/view/adminhtml/templates/sales/order/create/giftoptions.phtml`** -> AI Confidence: **99.32%**
105. **`app/code/Magento/GiftMessage/view/adminhtml/templates/sales/order/view/giftoptions.phtml`** -> AI Confidence: **99.32%**
106. **`app/code/Magento/GiftMessage/view/frontend/templates/inline.phtml`** -> AI Confidence: **99.32%**
107. **`app/code/Magento/GroupedProduct/view/adminhtml/templates/product/stock/disabler.phtml`** -> AI Confidence: **99.32%**
108. **`app/code/Magento/ImportExport/view/adminhtml/templates/export/form/before.phtml`** -> AI Confidence: **99.32%**
109. **`app/code/Magento/ImportExport/view/adminhtml/templates/export/form/filter/after.phtml`** -> AI Confidence: **99.32%**
110. **`app/code/Magento/Newsletter/view/adminhtml/templates/problem/list.phtml`** -> AI Confidence: **99.32%**
111. **`app/code/Magento/Newsletter/view/adminhtml/templates/subscriber/list.phtml`** -> AI Confidence: **99.32%**
112. **`app/code/Magento/PageCache/view/adminhtml/templates/page_cache_validation.phtml`** -> AI Confidence: **99.32%**
113. **`app/code/Magento/Payment/view/adminhtml/templates/transparent/iframe.phtml`** -> AI Confidence: **99.32%**
114. **`app/code/Magento/Paypal/view/adminhtml/templates/system/config/rules.phtml`** -> AI Confidence: **99.32%**
115. **`app/code/Magento/Paypal/view/adminhtml/templates/transparent/iframe.phtml`** -> AI Confidence: **99.32%**
116. **`app/code/Magento/ProductVideo/view/adminhtml/templates/helper/gallery.phtml`** -> AI Confidence: **99.32%**
117. **`app/code/Magento/Sales/view/adminhtml/templates/order/create/totals/subtotal.phtml`** -> AI Confidence: **99.32%**
118. **`app/code/Magento/Shipping/view/frontend/templates/tracking/popup.phtml`** -> AI Confidence: **99.32%**
119. **`app/code/Magento/Swatches/view/frontend/templates/product/listing/renderer.phtml`** -> AI Confidence: **99.32%**
120. **`app/code/Magento/Tax/view/adminhtml/templates/toolbar/class/save.phtml`** -> AI Confidence: **99.32%**
121. **`app/code/Magento/Tax/view/adminhtml/templates/toolbar/rate/save.phtml`** -> AI Confidence: **99.32%**
122. **`app/code/Magento/Tax/view/adminhtml/templates/toolbar/rule/save.phtml`** -> AI Confidence: **99.32%**
123. **`app/code/Magento/User/view/adminhtml/templates/role/info.phtml`** -> AI Confidence: **99.32%**
124. **`app/code/Magento/User/view/adminhtml/templates/user/roles_grid_js.phtml`** -> AI Confidence: **99.32%**
125. **`app/code/Magento/Vault/view/frontend/templates/customer_account/credit_card.phtml`** -> AI Confidence: **99.32%**
126. **`phpserver/router.php`** -> AI Confidence: **99.32%**
127. **`app/code/Magento/AdvancedPricingImportExport/Model/Import/AdvancedPricing/Validator/TierPrice.php`** -> AI Confidence: **99.31%**
128. **`app/code/Magento/Authorization/Model/Acl/Loader/Rule.php`** -> AI Confidence: **99.31%**
129. **`app/code/Magento/Backend/view/adminhtml/templates/page/js/calendar.phtml`** -> AI Confidence: **99.31%**
130. **`app/code/Magento/Bundle/Block/Catalog/Product/View/Type/Bundle/Option.php`** -> AI Confidence: **99.31%**
131. **`app/code/Magento/Bundle/Controller/Adminhtml/Product/Initialization/Helper/Plugin/Bundle.php`** -> AI Confidence: **99.31%**
132. **`app/code/Magento/Bundle/Model/Product/Price.php`** -> AI Confidence: **99.31%**
133. **`app/code/Magento/Bundle/Model/Product/Type.php`** -> AI Confidence: **99.31%**
134. **`app/code/Magento/Bundle/Model/Sales/Order/Pdf/Items/AbstractItems.php`** -> AI Confidence: **99.31%**
135. **`app/code/Magento/Bundle/Model/Sales/Order/Pdf/Items/Creditmemo.php`** -> AI Confidence: **99.31%**
136. **`app/code/Magento/Bundle/Model/Sales/Order/Pdf/Items/Shipment.php`** -> AI Confidence: **99.31%**
137. **`app/code/Magento/BundleImportExport/Model/Import/Product/Type/Bundle.php`** -> AI Confidence: **99.31%**
138. **`app/code/Magento/Catalog/Block/Product/View/Options/Type/Date.php`** -> AI Confidence: **99.31%**
139. **`app/code/Magento/Catalog/Controller/Adminhtml/Category/Save.php`** -> AI Confidence: **99.31%**
140. **`app/code/Magento/Catalog/Controller/Adminhtml/Product/Action/Attribute/Save.php`** -> AI Confidence: **99.31%**
141. **`app/code/Magento/Catalog/Controller/Adminhtml/Product/Attribute/Save.php`** -> AI Confidence: **99.31%**
142. **`app/code/Magento/Catalog/Controller/Adminhtml/Product/Attribute/Validate.php`** -> AI Confidence: **99.31%**
143. **`app/code/Magento/Catalog/Controller/Adminhtml/Product/Save.php`** -> AI Confidence: **99.31%**
144. **`app/code/Magento/Catalog/Model/Category/Authorization.php`** -> AI Confidence: **99.31%**
145. **`app/code/Magento/Catalog/Model/Category/DataProvider.php`** -> AI Confidence: **99.31%**
146. **`app/code/Magento/Catalog/Model/CustomOptions/CustomOptionProcessor.php`** -> AI Confidence: **99.31%**
147. **`app/code/Magento/Catalog/Model/Design.php`** -> AI Confidence: **99.31%**
148. **`app/code/Magento/Catalog/Model/Indexer/Category/Flat/AbstractAction.php`** -> AI Confidence: **99.31%**
149. **`app/code/Magento/Catalog/Model/Indexer/Product/Flat/FlatTableBuilder.php`** -> AI Confidence: **99.31%**
150. **`app/code/Magento/Catalog/Model/Product/Authorization.php`** -> AI Confidence: **99.31%**
151. **`app/code/Magento/Catalog/Model/Product/Gallery/CreateHandler.php`** -> AI Confidence: **99.31%**
152. **`app/code/Magento/Catalog/Model/Product/Gallery/GalleryManagement.php`** -> AI Confidence: **99.31%**
153. **`app/code/Magento/Catalog/Model/Product/Image/ParamsBuilder.php`** -> AI Confidence: **99.31%**
154. **`app/code/Magento/Catalog/Model/Product/Option/Type/File.php`** -> AI Confidence: **99.31%**
155. **`app/code/Magento/Catalog/Model/Product/Option/Type/File/Validator.php`** -> AI Confidence: **99.31%**
156. **`app/code/Magento/Catalog/Model/Product/Option/Type/File/ValidatorFile.php`** -> AI Confidence: **99.31%**
157. **`app/code/Magento/Catalog/Model/Product/Price/Validation/TierPriceValidator.php`** -> AI Confidence: **99.31%**
158. **`app/code/Magento/Catalog/Model/Product/TierPriceManagement.php`** -> AI Confidence: **99.31%**
159. **`app/code/Magento/Catalog/Model/Product/Type/AbstractType.php`** -> AI Confidence: **99.31%**
160. **`app/code/Magento/Catalog/Model/Product/Type/Price.php`** -> AI Confidence: **99.31%**
161. **`app/code/Magento/Catalog/Model/ProductRepository/MediaGalleryProcessor.php`** -> AI Confidence: **99.31%**
162. **`app/code/Magento/Catalog/Model/ResourceModel/Category/Tree.php`** -> AI Confidence: **99.31%**
163. **`app/code/Magento/Catalog/Model/ResourceModel/Product/Option/Value.php`** -> AI Confidence: **99.31%**
164. **`app/code/Magento/Catalog/Ui/DataProvider/Product/Form/Modifier/Websites.php`** -> AI Confidence: **99.31%**
165. **`app/code/Magento/CatalogGraphQl/DataProvider/Product/SearchCriteriaBuilder.php`** -> AI Confidence: **99.31%**
166. **`app/code/Magento/CatalogImportExport/Model/Export/Product.php`** -> AI Confidence: **99.31%**
167. **`app/code/Magento/CatalogImportExport/Model/Import/Product/MediaGalleryProcessor.php`** -> AI Confidence: **99.31%**
168. **`app/code/Magento/CatalogImportExport/Model/Import/Product/Option.php`** -> AI Confidence: **99.31%**
169. **`app/code/Magento/CatalogImportExport/Model/Import/Product/Validator.php`** -> AI Confidence: **99.31%**
170. **`app/code/Magento/CatalogInventory/Model/Quote/Item/QuantityValidator.php`** -> AI Confidence: **99.31%**
171. **`app/code/Magento/CatalogInventory/Model/Quote/Item/QuantityValidator/Initializer/StockItem.php`** -> AI Confidence: **99.31%**
172. **`app/code/Magento/CatalogInventory/Model/ResourceModel/Stock/Status.php`** -> AI Confidence: **99.31%**
173. **`app/code/Magento/CatalogInventory/Model/StockStateProvider.php`** -> AI Confidence: **99.31%**
174. **`app/code/Magento/CatalogSearch/Model/Advanced.php`** -> AI Confidence: **99.31%**
175. **`app/code/Magento/CatalogSearch/Model/Indexer/Fulltext/Action/DataProvider.php`** -> AI Confidence: **99.31%**
176. **`app/code/Magento/CatalogSearch/Model/Search/RequestGenerator.php`** -> AI Confidence: **99.31%**
177. **`app/code/Magento/CatalogUrlRewrite/Model/Storage/DynamicStorage.php`** -> AI Confidence: **99.31%**
178. **`app/code/Magento/Cms/Controller/Adminhtml/Block/Save.php`** -> AI Confidence: **99.31%**
179. **`app/code/Magento/Cms/Helper/Page.php`** -> AI Confidence: **99.31%**
180. **`app/code/Magento/Cms/Model/Wysiwyg/Images/Storage.php`** -> AI Confidence: **99.31%**
181. **`app/code/Magento/Config/Model/Config.php`** -> AI Confidence: **99.31%**
182. **`app/code/Magento/ConfigurableProduct/Controller/Adminhtml/Product/Builder/Plugin.php`** -> AI Confidence: **99.31%**
183. **`app/code/Magento/ConfigurableProduct/Model/Product/Type/Configurable.php`** -> AI Confidence: **99.31%**
184. **`app/code/Magento/ConfigurableProduct/view/adminhtml/templates/catalog/product/edit/super/matrix.phtml`** -> AI Confidence: **99.31%**
185. **`app/code/Magento/Cron/Observer/ProcessCronQueueObserver.php`** -> AI Confidence: **99.31%**
186. **`app/code/Magento/Csp/Model/SubresourceIntegrity/Storage/File.php`** -> AI Confidence: **99.31%**
187. **`app/code/Magento/Csp/Plugin/RemoveAllAssetIntegrityHashes.php`** -> AI Confidence: **99.31%**
188. **`app/code/Magento/Customer/Model/Address/AbstractAddress.php`** -> AI Confidence: **99.31%**
189. **`app/code/Magento/Customer/Model/FileUploaderDataResolver.php`** -> AI Confidence: **99.31%**
190. **`app/code/Magento/Customer/Model/Metadata/Form/File.php`** -> AI Confidence: **99.31%**
191. **`app/code/Magento/Customer/Model/Vat.php`** -> AI Confidence: **99.31%**
192. **`app/code/Magento/Customer/Plugin/ValidateDobOnSave.php`** -> AI Confidence: **99.31%**
193. **`app/code/Magento/Customer/Ui/Component/DataProvider/Document.php`** -> AI Confidence: **99.31%**
194. **`app/code/Magento/Customer/Ui/Component/Listing/Columns.php`** -> AI Confidence: **99.31%**
195. **`app/code/Magento/CustomerImportExport/Model/Import/Customer.php`** -> AI Confidence: **99.31%**
196. **`app/code/Magento/Deploy/Console/ConsoleLogger.php`** -> AI Confidence: **99.31%**
197. **`app/code/Magento/Deploy/Package/Processor/PreProcessor/Less.php`** -> AI Confidence: **99.31%**
198. **`app/code/Magento/Deploy/Service/Bundle.php`** -> AI Confidence: **99.31%**
199. **`app/code/Magento/Deploy/Service/DeployPackage.php`** -> AI Confidence: **99.31%**
200. **`app/code/Magento/Deploy/Strategy/QuickDeploy.php`** -> AI Confidence: **99.31%**
201. **`app/code/Magento/Developer/Model/Setup/Declaration/Schema/WhitelistGenerator.php`** -> AI Confidence: **99.31%**
202. **`app/code/Magento/Dhl/Model/Carrier.php`** -> AI Confidence: **99.31%**
203. **`app/code/Magento/Directory/Model/Observer.php`** -> AI Confidence: **99.31%**
204. **`app/code/Magento/Downloadable/Controller/Adminhtml/Product/Initialization/Helper/Plugin/Downloadable.php`** -> AI Confidence: **99.31%**
205. **`app/code/Magento/Downloadable/view/adminhtml/templates/product/edit/downloadable/links.phtml`** -> AI Confidence: **99.31%**
206. **`app/code/Magento/Downloadable/view/adminhtml/templates/product/edit/downloadable/samples.phtml`** -> AI Confidence: **99.31%**
207. **`app/code/Magento/Eav/Model/Config.php`** -> AI Confidence: **99.31%**
208. **`app/code/Magento/Eav/Model/Entity/Attribute.php`** -> AI Confidence: **99.31%**
209. **`app/code/Magento/Eav/Model/ResourceModel/Entity/Attribute.php`** -> AI Confidence: **99.31%**
210. **`app/code/Magento/Elasticsearch/Model/ResourceModel/Index.php`** -> AI Confidence: **99.31%**
211. **`app/code/Magento/Elasticsearch/SearchAdapter/Query/Builder/MatchQuery.php`** -> AI Confidence: **99.31%**
212. **`app/code/Magento/Email/Model/AbstractTemplate.php`** -> AI Confidence: **99.31%**
213. **`app/code/Magento/Fedex/Model/Carrier.php`** -> AI Confidence: **99.31%**
214. **`app/code/Magento/ImportExport/Controller/Adminhtml/Import/Validate.php`** -> AI Confidence: **99.31%**
215. **`app/code/Magento/MessageQueue/Model/Cron/ConsumersRunner.php`** -> AI Confidence: **99.31%**
216. **`app/code/Magento/NewRelicReporting/Console/Command/DeployMarker.php`** -> AI Confidence: **99.31%**
217. **`app/code/Magento/NewRelicReporting/Model/Apm/Deployments.php`** -> AI Confidence: **99.31%**
218. **`app/code/Magento/Newsletter/Block/Adminhtml/Queue/Edit/Form.php`** -> AI Confidence: **99.31%**
219. **`app/code/Magento/Newsletter/Model/SubscriptionManager.php`** -> AI Confidence: **99.31%**
220. **`app/code/Magento/PageCache/Model/Config.php`** -> AI Confidence: **99.31%**
221. **`app/code/Magento/Paypal/Model/AbstractIpn.php`** -> AI Confidence: **99.31%**
222. **`app/code/Magento/Paypal/Model/Config.php`** -> AI Confidence: **99.31%**
223. **`app/code/Magento/Paypal/Model/Info.php`** -> AI Confidence: **99.31%**
224. **`app/code/Magento/Paypal/Model/Ipn.php`** -> AI Confidence: **99.31%**
225. **`app/code/Magento/Paypal/Model/Report/Settlement.php`** -> AI Confidence: **99.31%**
226. **`app/code/Magento/Paypal/Setup/Patch/Data/UpdateBmltoPayLater.php`** -> AI Confidence: **99.31%**
227. **`app/code/Magento/ProductAlert/Model/Observer.php`** -> AI Confidence: **99.31%**
228. **`app/code/Magento/Quote/Model/Address/Validator/AddressAttributeValidator.php`** -> AI Confidence: **99.31%**
229. **`app/code/Magento/Quote/Model/CustomerManagement.php`** -> AI Confidence: **99.31%**
230. **`app/code/Magento/Quote/Model/Quote/Address/BillingAddressPersister.php`** -> AI Confidence: **99.31%**
231. **`app/code/Magento/Quote/Model/Quote/Item/CartItemPersister.php`** -> AI Confidence: **99.31%**
232. **`app/code/Magento/Quote/Model/Quote/Item/Processor.php`** -> AI Confidence: **99.31%**
233. **`app/code/Magento/Quote/Model/QuoteManagement.php`** -> AI Confidence: **99.31%**
234. **`app/code/Magento/Quote/Model/ResourceModel/Quote/Item/Collection.php`** -> AI Confidence: **99.31%**
235. **`app/code/Magento/Quote/Model/ShippingAddressManagement.php`** -> AI Confidence: **99.31%**
236. **`app/code/Magento/QuoteGraphQl/Model/Cart/SetBillingAddressOnCart.php`** -> AI Confidence: **99.31%**
237. **`app/code/Magento/QuoteGraphQl/Model/CartItem/DataProvider/UpdateCartItems.php`** -> AI Confidence: **99.31%**
238. **`app/code/Magento/Review/Block/Adminhtml/Rating/Edit/Tab/Form.php`** -> AI Confidence: **99.31%**
239. **`app/code/Magento/Rule/Model/Condition/Sql/Builder.php`** -> AI Confidence: **99.31%**
240. **`app/code/Magento/Sales/Controller/Adminhtml/Order/Creditmemo/Save.php`** -> AI Confidence: **99.31%**
241. **`app/code/Magento/Sales/Controller/Adminhtml/Order/Invoice/Save.php`** -> AI Confidence: **99.31%**
242. **`app/code/Magento/Sales/Model/AdminOrder/Create.php`** -> AI Confidence: **99.31%**
243. **`app/code/Magento/Sales/Model/Order/Address/Validator.php`** -> AI Confidence: **99.31%**
244. **`app/code/Magento/Sales/Model/Order/Creditmemo/Total/Tax.php`** -> AI Confidence: **99.31%**
245. **`app/code/Magento/Sales/Model/Order/CreditmemoFactory.php`** -> AI Confidence: **99.31%**
246. **`app/code/Magento/Sales/Model/Service/InvoiceService.php`** -> AI Confidence: **99.31%**
247. **`app/code/Magento/Sales/Plugin/Webapi/OrderResponseNullKeysPlugin.php`** -> AI Confidence: **99.31%**
248. **`app/code/Magento/SalesGraphQl/Model/Resolver/CustomerOrders.php`** -> AI Confidence: **99.31%**
249. **`app/code/Magento/SalesRule/Controller/Adminhtml/Promo/Quote/Generate.php`** -> AI Confidence: **99.31%**
250. **`app/code/Magento/SalesRule/Model/Converter/ToDataModel.php`** -> AI Confidence: **99.31%**
251. **`app/code/Magento/SalesRule/Model/Coupon/Usage/Processor.php`** -> AI Confidence: **99.31%**
252. **`app/code/Magento/SalesRule/Model/Quote/Discount.php`** -> AI Confidence: **99.31%**
253. **`app/code/Magento/SalesRule/Model/Rule/Action/Discount/CartFixed.php`** -> AI Confidence: **99.31%**
254. **`app/code/Magento/SalesRule/Model/Utility.php`** -> AI Confidence: **99.31%**
255. **`app/code/Magento/SalesRule/Model/Validator.php`** -> AI Confidence: **99.31%**
256. **`app/code/Magento/SendFriend/view/frontend/templates/send.phtml`** -> AI Confidence: **99.31%**
257. **`app/code/Magento/Shipping/Model/Shipping.php`** -> AI Confidence: **99.31%**
258. **`app/code/Magento/Sitemap/Model/ResourceModel/Catalog/Product.php`** -> AI Confidence: **99.31%**
259. **`app/code/Magento/Store/Model/Config/Importer/Processor/Delete.php`** -> AI Confidence: **99.31%**
260. **`app/code/Magento/Store/Model/Config/Importer/Processor/Update.php`** -> AI Confidence: **99.31%**
261. **`app/code/Magento/Swatches/Model/Plugin/EavAttribute.php`** -> AI Confidence: **99.31%**
262. **`app/code/Magento/Tax/Block/Adminhtml/Rate/Form.php`** -> AI Confidence: **99.31%**
263. **`app/code/Magento/Tax/Model/Calculation.php`** -> AI Confidence: **99.31%**
264. **`app/code/Magento/Tax/Model/Calculation/Rule/Validator.php`** -> AI Confidence: **99.31%**
265. **`app/code/Magento/Tax/Model/ResourceModel/Sales/Order/Relation.php`** -> AI Confidence: **99.31%**
266. **`app/code/Magento/Tax/Model/Sales/Total/Quote/CommonTaxCollector.php`** -> AI Confidence: **99.31%**
267. **`app/code/Magento/Tax/Model/Sales/Total/Quote/Tax.php`** -> AI Confidence: **99.31%**
268. **`app/code/Magento/Tax/Observer/GetPriceConfigurationObserver.php`** -> AI Confidence: **99.31%**
269. **`app/code/Magento/TaxImportExport/Model/Rate/CsvImportHandler.php`** -> AI Confidence: **99.31%**
270. **`app/code/Magento/Theme/view/adminhtml/templates/browser/content/uploader.phtml`** -> AI Confidence: **99.31%**
271. **`app/code/Magento/Translation/Model/Inline/Parser.php`** -> AI Confidence: **99.31%**
272. **`app/code/Magento/Translation/Model/ResourceModel/StringUtils.php`** -> AI Confidence: **99.31%**
273. **`app/code/Magento/Ui/Component/Form/AttributeMapper.php`** -> AI Confidence: **99.31%**
274. **`app/code/Magento/Ui/Config/Reader/DefinitionMap/Converter.php`** -> AI Confidence: **99.31%**
275. **`app/code/Magento/Ups/Model/Carrier.php`** -> AI Confidence: **99.31%**
276. **`app/code/Magento/Ups/view/adminhtml/templates/system/shipping/carrier_config.phtml`** -> AI Confidence: **99.31%**
277. **`app/code/Magento/UrlRewrite/Model/Storage/DbStorage.php`** -> AI Confidence: **99.31%**
278. **`app/code/Magento/UrlRewriteGraphQl/Model/Resolver/AbstractEntityUrl.php`** -> AI Confidence: **99.31%**
279. **`app/code/Magento/Usps/Model/Carrier.php`** -> AI Confidence: **99.31%**
280. **`app/code/Magento/Usps/Model/ShipmentService.php`** -> AI Confidence: **99.31%**
281. **`app/code/Magento/Usps/Model/TrackingService.php`** -> AI Confidence: **99.31%**
282. **`app/code/Magento/Webapi/Model/Rest/Swagger/Generator.php`** -> AI Confidence: **99.31%**
283. **`app/code/Magento/Webapi/Model/ServiceMetadata.php`** -> AI Confidence: **99.31%**
284. **`app/code/Magento/Weee/Model/Total/Invoice/Weee.php`** -> AI Confidence: **99.31%**
285. **`app/code/Magento/Wishlist/Model/ItemCarrier.php`** -> AI Confidence: **99.31%**
286. **`app/etc/registration_globlist.php`** -> AI Confidence: **99.31%**
287. **`dev/tests/api-functional/framework/Magento/TestFramework/Annotation/ApiConfigFixture.php`** -> AI Confidence: **99.31%**
288. **`dev/tests/integration/framework/Magento/TestFramework/Annotation/ConfigFixture.php`** -> AI Confidence: **99.31%**
289. **`dev/tests/integration/framework/Magento/TestFramework/Annotation/DataFixtureSetup.php`** -> AI Confidence: **99.31%**
290. **`dev/tests/integration/framework/Magento/TestFramework/Annotation/TestsIsolation.php`** -> AI Confidence: **99.31%**
291. **`dev/tests/integration/testsuite/Magento/Bundle/_files/bundle_product_two_dropdown_options.php`** -> AI Confidence: **99.31%**
292. **`dev/tests/integration/testsuite/Magento/Bundle/_files/bundle_product_with_not_visible_children.php`** -> AI Confidence: **99.31%**
293. **`dev/tests/integration/testsuite/Magento/Bundle/_files/issaleable_product.php`** -> AI Confidence: **99.31%**
294. **`dev/tests/integration/testsuite/Magento/Bundle/_files/product.php`** -> AI Confidence: **99.31%**
295. **`dev/tests/integration/testsuite/Magento/Bundle/_files/product_1.php`** -> AI Confidence: **99.31%**
296. **`dev/tests/integration/testsuite/Magento/Bundle/_files/product_with_multiple_options.php`** -> AI Confidence: **99.31%**
297. **`dev/tests/integration/testsuite/Magento/Bundle/_files/product_with_multiple_options_1.php`** -> AI Confidence: **99.31%**
298. **`dev/tests/integration/testsuite/Magento/Bundle/_files/product_with_multiple_options_and_custom_quantity.php`** -> AI Confidence: **99.31%**
299. **`dev/tests/integration/testsuite/Magento/Catalog/Ui/DataProvider/Product/Form/Modifier/_files/eav_expected_meta_output.php`** -> AI Confidence: **99.31%**
300. **`dev/tests/integration/testsuite/Magento/Catalog/Ui/DataProvider/Product/Form/Modifier/_files/eav_expected_meta_output_w_default.php`** -> AI Confidence: **99.31%**
301. **`dev/tests/integration/testsuite/Magento/Catalog/Ui/DataProvider/Product/Form/Modifier/_files/input_meta_for_categories.php`** -> AI Confidence: **99.31%**
302. **`dev/tests/integration/testsuite/Magento/Sales/_files/order_with_different_types_of_product_rollback.php`** -> AI Confidence: **99.31%**
303. **`dev/tests/integration/testsuite/Magento/Widget/Model/Config/_files/expectedGlobalArray.php`** -> AI Confidence: **99.31%**
304. **`dev/tests/integration/testsuite/Magento/Widget/Model/Config/_files/expectedGlobalDesignArray.php`** -> AI Confidence: **99.31%**
305. **`dev/tests/static/framework/Magento/TestFramework/Dependency/PhpRule.php`** -> AI Confidence: **99.31%**
306. **`dev/tests/static/framework/Magento/TestFramework/Dependency/Route/RouteMapper.php`** -> AI Confidence: **99.31%**
307. **`dev/tests/utils/phpunitGroupConfig.php`** -> AI Confidence: **99.31%**
308. **`setup/src/Magento/Setup/Module/Di/Code/Reader/FileScanner.php`** -> AI Confidence: **99.31%**
309. **`app/code/Magento/AdminAnalytics/view/adminhtml/templates/notification.phtml`** -> AI Confidence: **99.29%**
310. **`app/code/Magento/AdminAnalytics/view/adminhtml/templates/tracking.phtml`** -> AI Confidence: **99.29%**
311. **`app/code/Magento/AdminNotification/view/adminhtml/templates/notification/window.phtml`** -> AI Confidence: **99.29%**
312. **`app/code/Magento/AdminNotification/view/adminhtml/templates/system/messages.phtml`** -> AI Confidence: **99.29%**
313. **`app/code/Magento/AdminNotification/view/adminhtml/templates/system/messages/popup.phtml`** -> AI Confidence: **99.29%**
314. **`app/code/Magento/AdminNotification/view/adminhtml/templates/toolbar_entry.phtml`** -> AI Confidence: **99.29%**
315. **`app/code/Magento/AdvancedSearch/view/adminhtml/templates/system/config/testconnection.phtml`** -> AI Confidence: **99.29%**
316. **`app/code/Magento/AdvancedSearch/view/frontend/templates/search_data.phtml`** -> AI Confidence: **99.29%**
317. **`app/code/Magento/Analytics/registration.php`** -> AI Confidence: **99.29%**
318. **`app/code/Magento/Backend/view/adminhtml/templates/admin/access_denied.phtml`** -> AI Confidence: **99.29%**
319. **`app/code/Magento/Backend/view/adminhtml/templates/admin/formkey.phtml`** -> AI Confidence: **99.29%**
320. **`app/code/Magento/Backend/view/adminhtml/templates/admin/overlay_popup.phtml`** -> AI Confidence: **99.29%**
321. **`app/code/Magento/Backend/view/adminhtml/templates/admin/page.phtml`** -> AI Confidence: **99.29%**
322. **`app/code/Magento/Backend/view/adminhtml/templates/admin/save_confirm.phtml`** -> AI Confidence: **99.29%**
323. **`app/code/Magento/Backend/view/adminhtml/templates/dashboard/graph.phtml`** -> AI Confidence: **99.29%**
324. **`app/code/Magento/Backend/view/adminhtml/templates/dashboard/graph/disabled.phtml`** -> AI Confidence: **99.29%**
325. **`app/code/Magento/Backend/view/adminhtml/templates/dashboard/grid.phtml`** -> AI Confidence: **99.29%**
326. **`app/code/Magento/Backend/view/adminhtml/templates/dashboard/searches.phtml`** -> AI Confidence: **99.29%**
327. **`app/code/Magento/Backend/view/adminhtml/templates/dashboard/store/switcher.phtml`** -> AI Confidence: **99.29%**
328. **`app/code/Magento/Backend/view/adminhtml/templates/menu.phtml`** -> AI Confidence: **99.29%**
329. **`app/code/Magento/Backend/view/adminhtml/templates/page/container.phtml`** -> AI Confidence: **99.29%**
330. **`app/code/Magento/Backend/view/adminhtml/templates/page/copyright.phtml`** -> AI Confidence: **99.29%**
331. **`app/code/Magento/Backend/view/adminhtml/templates/page/footer.phtml`** -> AI Confidence: **99.29%**
332. **`app/code/Magento/Backend/view/adminhtml/templates/page/header.phtml`** -> AI Confidence: **99.29%**
333. **`app/code/Magento/Backend/view/adminhtml/templates/page/js/components.phtml`** -> AI Confidence: **99.29%**
334. **`app/code/Magento/Backend/view/adminhtml/templates/page/js/require_js.phtml`** -> AI Confidence: **99.29%**
335. **`app/code/Magento/Backend/view/adminhtml/templates/page/notices.phtml`** -> AI Confidence: **99.29%**
336. **`app/code/Magento/Backend/view/adminhtml/templates/page/privacyPolicy.phtml`** -> AI Confidence: **99.29%**
337. **`app/code/Magento/Backend/view/adminhtml/templates/page/report.phtml`** -> AI Confidence: **99.29%**
338. **`app/code/Magento/Backend/view/adminhtml/templates/pageactions.phtml`** -> AI Confidence: **99.29%**
339. **`app/code/Magento/Backend/view/adminhtml/templates/store/switcher.phtml`** -> AI Confidence: **99.29%**
340. **`app/code/Magento/Backend/view/adminhtml/templates/store/switcher/form/renderer/fieldset.phtml`** -> AI Confidence: **99.29%**
341. **`app/code/Magento/Backend/view/adminhtml/templates/store/switcher/form/renderer/fieldset/element.phtml`** -> AI Confidence: **99.29%**
342. **`app/code/Magento/Backend/view/adminhtml/templates/system/cache/additional.phtml`** -> AI Confidence: **99.29%**
343. **`app/code/Magento/Backend/view/adminhtml/templates/system/design/index.phtml`** -> AI Confidence: **99.29%**
344. **`app/code/Magento/Backend/view/adminhtml/templates/system/shipping/applicable_country.phtml`** -> AI Confidence: **99.29%**
345. **`app/code/Magento/Backend/view/adminhtml/templates/widget/breadcrumbs.phtml`** -> AI Confidence: **99.29%**
346. **`app/code/Magento/Backend/view/adminhtml/templates/widget/button.phtml`** -> AI Confidence: **99.29%**
347. **`app/code/Magento/Backend/view/adminhtml/templates/widget/button/split.phtml`** -> AI Confidence: **99.29%**
348. **`app/code/Magento/Backend/view/adminhtml/templates/widget/form.phtml`** -> AI Confidence: **99.29%**
349. **`app/code/Magento/Backend/view/adminhtml/templates/widget/form/element/gallery.phtml`** -> AI Confidence: **99.29%**
350. **`app/code/Magento/Backend/view/adminhtml/templates/widget/form/renderer/element.phtml`** -> AI Confidence: **99.29%**
351. **`app/code/Magento/Backend/view/adminhtml/templates/widget/form/renderer/fieldset.phtml`** -> AI Confidence: **99.29%**
352. **`app/code/Magento/Backend/view/adminhtml/templates/widget/form/renderer/fieldset/element.phtml`** -> AI Confidence: **99.29%**
353. **`app/code/Magento/Backend/view/adminhtml/templates/widget/grid/column_set.phtml`** -> AI Confidence: **99.29%**
354. **`app/code/Magento/Backend/view/adminhtml/templates/widget/grid/container.phtml`** -> AI Confidence: **99.29%**
355. **`app/code/Magento/Backend/view/adminhtml/templates/widget/grid/container/empty.phtml`** -> AI Confidence: **99.29%**
356. **`app/code/Magento/Backend/view/adminhtml/templates/widget/grid/export.phtml`** -> AI Confidence: **99.29%**
357. **`app/code/Magento/Backend/view/adminhtml/templates/widget/grid/massaction.phtml`** -> AI Confidence: **99.29%**
358. **`app/code/Magento/Backend/view/adminhtml/templates/widget/tabsleft.phtml`** -> AI Confidence: **99.29%**
359. **`app/code/Magento/Backend/view/adminhtml/templates/widget/view/container.phtml`** -> AI Confidence: **99.29%**
360. **`app/code/Magento/Backup/view/adminhtml/templates/backup/left.phtml`** -> AI Confidence: **99.29%**
361. **`app/code/Magento/Backup/view/adminhtml/templates/backup/list.phtml`** -> AI Confidence: **99.29%**
362. **`app/code/Magento/Bundle/view/adminhtml/templates/product/composite/fieldset/options/bundle.phtml`** -> AI Confidence: **99.29%**
363. **`app/code/Magento/Bundle/view/adminhtml/templates/product/composite/fieldset/options/type/checkbox.phtml`** -> AI Confidence: **99.29%**
364. **`app/code/Magento/Bundle/view/adminhtml/templates/product/composite/fieldset/options/type/multi.phtml`** -> AI Confidence: **99.29%**
365. **`app/code/Magento/Bundle/view/adminhtml/templates/product/composite/fieldset/options/type/radio.phtml`** -> AI Confidence: **99.29%**
366. **`app/code/Magento/Bundle/view/adminhtml/templates/product/composite/fieldset/options/type/select.phtml`** -> AI Confidence: **99.29%**
367. **`app/code/Magento/Bundle/view/adminhtml/templates/product/edit/bundle/option/search.phtml`** -> AI Confidence: **99.29%**
368. **`app/code/Magento/Bundle/view/base/templates/product/price/final_price.phtml`** -> AI Confidence: **99.29%**
369. **`app/code/Magento/Bundle/view/base/templates/product/price/selection/amount.phtml`** -> AI Confidence: **99.29%**
370. **`app/code/Magento/Bundle/view/base/templates/product/price/tier_prices.phtml`** -> AI Confidence: **99.29%**
371. **`app/code/Magento/Bundle/view/frontend/templates/catalog/product/view/backbutton.phtml`** -> AI Confidence: **99.29%**
372. **`app/code/Magento/Bundle/view/frontend/templates/catalog/product/view/customize.phtml`** -> AI Confidence: **99.29%**
373. **`app/code/Magento/Bundle/view/frontend/templates/catalog/product/view/options/notice.phtml`** -> AI Confidence: **99.29%**
374. **`app/code/Magento/Bundle/view/frontend/templates/catalog/product/view/type/bundle.phtml`** -> AI Confidence: **99.29%**
375. **`app/code/Magento/Bundle/view/frontend/templates/catalog/product/view/type/bundle/option/checkbox.phtml`** -> AI Confidence: **99.29%**
376. **`app/code/Magento/Bundle/view/frontend/templates/catalog/product/view/type/bundle/option/multi.phtml`** -> AI Confidence: **99.29%**
377. **`app/code/Magento/Bundle/view/frontend/templates/catalog/product/view/type/bundle/option/select.phtml`** -> AI Confidence: **99.29%**
378. **`app/code/Magento/Bundle/view/frontend/templates/catalog/product/view/type/bundle/options.phtml`** -> AI Confidence: **99.29%**
379. **`app/code/Magento/Bundle/view/frontend/templates/email/order/items/creditmemo/default.phtml`** -> AI Confidence: **99.29%**
380. **`app/code/Magento/Bundle/view/frontend/templates/email/order/items/invoice/default.phtml`** -> AI Confidence: **99.29%**
381. **`app/code/Magento/Bundle/view/frontend/templates/email/order/items/order/default.phtml`** -> AI Confidence: **99.29%**
382. **`app/code/Magento/Bundle/view/frontend/templates/email/order/items/shipment/default.phtml`** -> AI Confidence: **99.29%**
383. **`app/code/Magento/Bundle/view/frontend/templates/js/components.phtml`** -> AI Confidence: **99.29%**
384. **`app/code/Magento/Bundle/view/frontend/templates/sales/order/creditmemo/items/renderer.phtml`** -> AI Confidence: **99.29%**
385. **`app/code/Magento/Bundle/view/frontend/templates/sales/order/invoice/items/renderer.phtml`** -> AI Confidence: **99.29%**
386. **`app/code/Magento/Bundle/view/frontend/templates/sales/order/items/renderer.phtml`** -> AI Confidence: **99.29%**
387. **`app/code/Magento/Bundle/view/frontend/templates/sales/order/shipment/items/renderer.phtml`** -> AI Confidence: **99.29%**
388. **`app/code/Magento/Captcha/view/frontend/templates/js/components.phtml`** -> AI Confidence: **99.29%**
389. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/category/checkboxes/tree.phtml`** -> AI Confidence: **99.29%**
390. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/category/edit.phtml`** -> AI Confidence: **99.29%**
391. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/category/edit/assign_products.phtml`** -> AI Confidence: **99.29%**
392. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/category/widget/tree.phtml`** -> AI Confidence: **99.29%**
393. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/form/renderer/fieldset/element.phtml`** -> AI Confidence: **99.29%**
394. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product.phtml`** -> AI Confidence: **99.29%**
395. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/attribute/form.phtml`** -> AI Confidence: **99.29%**
396. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/attribute/set/main/tree/attribute.phtml`** -> AI Confidence: **99.29%**
397. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/attribute/set/main/tree/group.phtml`** -> AI Confidence: **99.29%**
398. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/attribute/set/toolbar/main.phtml`** -> AI Confidence: **99.29%**
399. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/composite/fieldset/options.phtml`** -> AI Confidence: **99.29%**
400. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/composite/fieldset/options/js.phtml`** -> AI Confidence: **99.29%**
401. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/composite/fieldset/options/type/default.phtml`** -> AI Confidence: **99.29%**
402. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/composite/fieldset/options/type/file.phtml`** -> AI Confidence: **99.29%**
403. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/composite/fieldset/options/type/select.phtml`** -> AI Confidence: **99.29%**
404. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/composite/fieldset/options/type/text.phtml`** -> AI Confidence: **99.29%**
405. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/edit/action/attribute.phtml`** -> AI Confidence: **99.29%**
406. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/edit/attribute_set.phtml`** -> AI Confidence: **99.29%**
407. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/edit/category/new/form.phtml`** -> AI Confidence: **99.29%**
408. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/edit/options/type/date.phtml`** -> AI Confidence: **99.29%**
409. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/edit/serializer.phtml`** -> AI Confidence: **99.29%**
410. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/edit/websites.phtml`** -> AI Confidence: **99.29%**
411. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/tab/alert.phtml`** -> AI Confidence: **99.29%**
412. **`app/code/Magento/Catalog/view/adminhtml/templates/product/edit/tabs.phtml`** -> AI Confidence: **99.29%**
413. **`app/code/Magento/Catalog/view/adminhtml/templates/product/edit/tabs/child_tab.phtml`** -> AI Confidence: **99.29%**
414. **`app/code/Magento/Catalog/view/adminhtml/templates/product/grid/massaction_extended.phtml`** -> AI Confidence: **99.29%**
415. **`app/code/Magento/Catalog/view/adminhtml/templates/product/grid/url_filter_applier.phtml`** -> AI Confidence: **99.29%**
416. **`app/code/Magento/Catalog/view/adminhtml/templates/rss/grid/link.phtml`** -> AI Confidence: **99.29%**
417. **`app/code/Magento/Catalog/view/base/templates/js/components.phtml`** -> AI Confidence: **99.29%**
418. **`app/code/Magento/Catalog/view/base/templates/product/composite/fieldset/options/view/checkable.phtml`** -> AI Confidence: **99.29%**
419. **`app/code/Magento/Catalog/view/base/templates/product/price/amount/default.phtml`** -> AI Confidence: **99.29%**
420. **`app/code/Magento/Catalog/view/base/templates/product/price/configured_price.phtml`** -> AI Confidence: **99.29%**
421. **`app/code/Magento/Catalog/view/base/templates/product/price/default.phtml`** -> AI Confidence: **99.29%**
422. **`app/code/Magento/Catalog/view/base/templates/product/price/final_price.phtml`** -> AI Confidence: **99.29%**
423. **`app/code/Magento/Catalog/view/frontend/templates/category/cms.phtml`** -> AI Confidence: **99.29%**
424. **`app/code/Magento/Catalog/view/frontend/templates/category/description.phtml`** -> AI Confidence: **99.29%**
425. **`app/code/Magento/Catalog/view/frontend/templates/category/products.phtml`** -> AI Confidence: **99.29%**
426. **`app/code/Magento/Catalog/view/frontend/templates/category/rss.phtml`** -> AI Confidence: **99.29%**
427. **`app/code/Magento/Catalog/view/frontend/templates/category/widget/link/link_block.phtml`** -> AI Confidence: **99.29%**
428. **`app/code/Magento/Catalog/view/frontend/templates/category/widget/link/link_href.phtml`** -> AI Confidence: **99.29%**
429. **`app/code/Magento/Catalog/view/frontend/templates/category/widget/link/link_inline.phtml`** -> AI Confidence: **99.29%**
430. **`app/code/Magento/Catalog/view/frontend/templates/frontend_storage_manager.phtml`** -> AI Confidence: **99.29%**
431. **`app/code/Magento/Catalog/view/frontend/templates/messages/addCompareSuccessMessage.phtml`** -> AI Confidence: **99.29%**
432. **`app/code/Magento/Catalog/view/frontend/templates/navigation/left.phtml`** -> AI Confidence: **99.29%**
433. **`app/code/Magento/Catalog/view/frontend/templates/product/compare/list.phtml`** -> AI Confidence: **99.29%**
434. **`app/code/Magento/Catalog/view/frontend/templates/product/gallery.phtml`** -> AI Confidence: **99.29%**
435. **`app/code/Magento/Catalog/view/frontend/templates/product/image.phtml`** -> AI Confidence: **99.29%**
436. **`app/code/Magento/Catalog/view/frontend/templates/product/image_with_borders.phtml`** -> AI Confidence: **99.29%**
437. **`app/code/Magento/Catalog/view/frontend/templates/product/list.phtml`** -> AI Confidence: **99.29%**
438. **`app/code/Magento/Catalog/view/frontend/templates/product/list/addto/compare.phtml`** -> AI Confidence: **99.29%**
439. **`app/code/Magento/Catalog/view/frontend/templates/product/list/items.phtml`** -> AI Confidence: **99.29%**
440. **`app/code/Magento/Catalog/view/frontend/templates/product/list/toolbar.phtml`** -> AI Confidence: **99.29%**
441. **`app/code/Magento/Catalog/view/frontend/templates/product/list/toolbar/limiter.phtml`** -> AI Confidence: **99.29%**
442. **`app/code/Magento/Catalog/view/frontend/templates/product/list/toolbar/sorter.phtml`** -> AI Confidence: **99.29%**
443. **`app/code/Magento/Catalog/view/frontend/templates/product/list/toolbar/viewmode.phtml`** -> AI Confidence: **99.29%**
444. **`app/code/Magento/Catalog/view/frontend/templates/product/view/additional.phtml`** -> AI Confidence: **99.29%**
445. **`app/code/Magento/Catalog/view/frontend/templates/product/view/addto.phtml`** -> AI Confidence: **99.29%**
446. **`app/code/Magento/Catalog/view/frontend/templates/product/view/addto/compare.phtml`** -> AI Confidence: **99.29%**
447. **`app/code/Magento/Catalog/view/frontend/templates/product/view/addtocart.phtml`** -> AI Confidence: **99.29%**
448. **`app/code/Magento/Catalog/view/frontend/templates/product/view/attribute.phtml`** -> AI Confidence: **99.29%**
449. **`app/code/Magento/Catalog/view/frontend/templates/product/view/counter.phtml`** -> AI Confidence: **99.29%**
450. **`app/code/Magento/Catalog/view/frontend/templates/product/view/description.phtml`** -> AI Confidence: **99.29%**
451. **`app/code/Magento/Catalog/view/frontend/templates/product/view/details.phtml`** -> AI Confidence: **99.29%**
452. **`app/code/Magento/Catalog/view/frontend/templates/product/view/form.phtml`** -> AI Confidence: **99.29%**
453. **`app/code/Magento/Catalog/view/frontend/templates/product/view/gallery.phtml`** -> AI Confidence: **99.29%**
454. **`app/code/Magento/Catalog/view/frontend/templates/product/view/mailto.phtml`** -> AI Confidence: **99.29%**
455. **`app/code/Magento/Catalog/view/frontend/templates/product/view/opengraph/currency.phtml`** -> AI Confidence: **99.29%**
456. **`app/code/Magento/Catalog/view/frontend/templates/product/view/opengraph/general.phtml`** -> AI Confidence: **99.29%**
457. **`app/code/Magento/Catalog/view/frontend/templates/product/view/options.phtml`** -> AI Confidence: **99.29%**
458. **`app/code/Magento/Catalog/view/frontend/templates/product/view/options/type/date.phtml`** -> AI Confidence: **99.29%**
459. **`app/code/Magento/Catalog/view/frontend/templates/product/view/options/type/file.phtml`** -> AI Confidence: **99.29%**
460. **`app/code/Magento/Catalog/view/frontend/templates/product/view/options/type/select.phtml`** -> AI Confidence: **99.29%**
461. **`app/code/Magento/Catalog/view/frontend/templates/product/view/options/type/text.phtml`** -> AI Confidence: **99.29%**
462. **`app/code/Magento/Catalog/view/frontend/templates/product/view/options/wrapper.phtml`** -> AI Confidence: **99.29%**
463. **`app/code/Magento/Catalog/view/frontend/templates/product/view/options/wrapper/bottom.phtml`** -> AI Confidence: **99.29%**
464. **`app/code/Magento/Catalog/view/frontend/templates/product/view/price_clone.phtml`** -> AI Confidence: **99.29%**
465. **`app/code/Magento/Catalog/view/frontend/templates/product/view/review.phtml`** -> AI Confidence: **99.29%**
466. **`app/code/Magento/Catalog/view/frontend/templates/product/view/type/default.phtml`** -> AI Confidence: **99.29%**
467. **`app/code/Magento/Catalog/view/frontend/templates/product/widget/compared/grid.phtml`** -> AI Confidence: **99.29%**
468. **`app/code/Magento/Catalog/view/frontend/templates/product/widget/compared/list.phtml`** -> AI Confidence: **99.29%**
469. **`app/code/Magento/Catalog/view/frontend/templates/product/widget/compared/sidebar.phtml`** -> AI Confidence: **99.29%**
470. **`app/code/Magento/Catalog/view/frontend/templates/product/widget/link/link_block.phtml`** -> AI Confidence: **99.29%**
471. **`app/code/Magento/Catalog/view/frontend/templates/product/widget/link/link_inline.phtml`** -> AI Confidence: **99.29%**
472. **`app/code/Magento/Catalog/view/frontend/templates/product/widget/new/column/new_default_list.phtml`** -> AI Confidence: **99.29%**
473. **`app/code/Magento/Catalog/view/frontend/templates/product/widget/new/content/new_grid.phtml`** -> AI Confidence: **99.29%**
474. **`app/code/Magento/Catalog/view/frontend/templates/product/widget/new/content/new_list.phtml`** -> AI Confidence: **99.29%**
475. **`app/code/Magento/Catalog/view/frontend/templates/product/widget/viewed/grid.phtml`** -> AI Confidence: **99.29%**
476. **`app/code/Magento/Catalog/view/frontend/templates/product/widget/viewed/list.phtml`** -> AI Confidence: **99.29%**
477. **`app/code/Magento/Catalog/view/frontend/templates/product/widget/viewed/sidebar.phtml`** -> AI Confidence: **99.29%**
478. **`app/code/Magento/CatalogAnalytics/registration.php`** -> AI Confidence: **99.29%**
479. **`app/code/Magento/CatalogInventory/view/frontend/templates/qtyincrements.phtml`** -> AI Confidence: **99.29%**
480. **`app/code/Magento/CatalogInventory/view/frontend/templates/stockqty/composite.phtml`** -> AI Confidence: **99.29%**
481. **`app/code/Magento/CatalogInventory/view/frontend/templates/stockqty/default.phtml`** -> AI Confidence: **99.29%**
482. **`app/code/Magento/CatalogRule/view/adminhtml/templates/promo/form.phtml`** -> AI Confidence: **99.29%**
483. **`app/code/Magento/CatalogSearch/view/adminhtml/templates/search_engine_comment.phtml`** -> AI Confidence: **99.29%**
484. **`app/code/Magento/CatalogSearch/view/frontend/templates/advanced/result.phtml`** -> AI Confidence: **99.29%**
485. **`app/code/Magento/CatalogSearch/view/frontend/templates/result.phtml`** -> AI Confidence: **99.29%**
486. **`app/code/Magento/CatalogSearch/view/frontend/templates/search_terms_log.phtml`** -> AI Confidence: **99.29%**
487. **`app/code/Magento/CheckoutAgreements/view/frontend/templates/agreements.phtml`** -> AI Confidence: **99.29%**
488. **`app/code/Magento/CheckoutAgreements/view/frontend/templates/multishipping_agreements.phtml`** -> AI Confidence: **99.29%**
489. **`app/code/Magento/Cms/view/adminhtml/templates/browser/content/files.phtml`** -> AI Confidence: **99.29%**
490. **`app/code/Magento/Cms/view/adminhtml/templates/page/edit/form/renderer/content.phtml`** -> AI Confidence: **99.29%**
491. **`app/code/Magento/Cms/view/adminhtml/templates/url_filter_applier.phtml`** -> AI Confidence: **99.29%**
492. **`app/code/Magento/Cms/view/frontend/templates/content.phtml`** -> AI Confidence: **99.29%**
493. **`app/code/Magento/Cms/view/frontend/templates/default/home.phtml`** -> AI Confidence: **99.29%**
494. **`app/code/Magento/Cms/view/frontend/templates/default/no-route.phtml`** -> AI Confidence: **99.29%**
495. **`app/code/Magento/Cms/view/frontend/templates/meta.phtml`** -> AI Confidence: **99.29%**
496. **`app/code/Magento/Cms/view/frontend/templates/widget/link/link_block.phtml`** -> AI Confidence: **99.29%**
497. **`app/code/Magento/Cms/view/frontend/templates/widget/link/link_inline.phtml`** -> AI Confidence: **99.29%**
498. **`app/code/Magento/Cms/view/frontend/templates/widget/static_block/default.phtml`** -> AI Confidence: **99.29%**
499. **`app/code/Magento/Config/view/adminhtml/templates/page/system/config/robots/reset.phtml`** -> AI Confidence: **99.29%**
500. **`app/code/Magento/Config/view/adminhtml/templates/system/config/js.phtml`** -> AI Confidence: **99.29%**
501. **`app/code/Magento/Config/view/adminhtml/templates/system/config/switcher.phtml`** -> AI Confidence: **99.29%**
502. **`app/code/Magento/Config/view/adminhtml/templates/system/config/tabs.phtml`** -> AI Confidence: **99.29%**
503. **`app/code/Magento/ConfigurableProduct/view/adminhtml/templates/catalog/product/attribute/new/created.phtml`** -> AI Confidence: **99.29%**
504. **`app/code/Magento/ConfigurableProduct/view/adminhtml/templates/catalog/product/edit/attribute/steps/select_attributes.phtml`** -> AI Confidence: **99.29%**
505. **`app/code/Magento/ConfigurableProduct/view/adminhtml/templates/catalog/product/edit/attribute/steps/summary.phtml`** -> AI Confidence: **99.29%**
506. **`app/code/Magento/ConfigurableProduct/view/adminhtml/templates/catalog/product/edit/super/wizard.phtml`** -> AI Confidence: **99.29%**
507. **`app/code/Magento/ConfigurableProduct/view/adminhtml/templates/product/configurable/affected-attribute-set-selector/form.phtml`** -> AI Confidence: **99.29%**
508. **`app/code/Magento/ConfigurableProduct/view/adminhtml/templates/product/configurable/attribute-selector/js.phtml`** -> AI Confidence: **99.29%**
509. **`app/code/Magento/ConfigurableProduct/view/base/templates/product/price/final_price.phtml`** -> AI Confidence: **99.29%**
510. **`app/code/Magento/ConfigurableProduct/view/frontend/templates/js/components.phtml`** -> AI Confidence: **99.29%**
511. **`app/code/Magento/ConfigurableProduct/view/frontend/templates/product/view/type/options/configurable.phtml`** -> AI Confidence: **99.29%**
512. **`app/code/Magento/Cookie/view/base/templates/html/cookie.phtml`** -> AI Confidence: **99.29%**
513. **`app/code/Magento/Cookie/view/frontend/templates/html/notices.phtml`** -> AI Confidence: **99.29%**
514. **`app/code/Magento/Cookie/view/frontend/templates/require_cookie.phtml`** -> AI Confidence: **99.29%**
515. **`app/code/Magento/Csp/view/base/templates/nonce/nonce.phtml`** -> AI Confidence: **99.29%**
516. **`app/code/Magento/Csp/view/base/templates/sri/hashes.phtml`** -> AI Confidence: **99.29%**
517. **`app/code/Magento/CurrencySymbol/view/adminhtml/templates/grid.phtml`** -> AI Confidence: **99.29%**
518. **`app/code/Magento/CurrencySymbol/view/adminhtml/templates/system/currency/rates.phtml`** -> AI Confidence: **99.29%**
519. **`app/code/Magento/Customer/view/adminhtml/templates/edit/js.phtml`** -> AI Confidence: **99.29%**
520. **`app/code/Magento/Customer/view/adminhtml/templates/sales/order/create/address/form/renderer/vat.phtml`** -> AI Confidence: **99.29%**
521. **`app/code/Magento/Customer/view/adminhtml/templates/system/config/validatevat.phtml`** -> AI Confidence: **99.29%**
522. **`app/code/Magento/Customer/view/adminhtml/templates/tab/cart_website_filter_form.phtml`** -> AI Confidence: **99.29%**
523. **`app/code/Magento/Customer/view/adminhtml/templates/tab/newsletter.phtml`** -> AI Confidence: **99.29%**
524. **`app/code/Magento/Customer/view/adminhtml/templates/tab/view.phtml`** -> AI Confidence: **99.29%**
525. **`app/code/Magento/Customer/view/adminhtml/templates/tab/view/personal_info.phtml`** -> AI Confidence: **99.29%**
526. **`app/code/Magento/Customer/view/adminhtml/templates/tab/view/sales.phtml`** -> AI Confidence: **99.29%**
527. **`app/code/Magento/Customer/view/frontend/templates/account/authentication-popup.phtml`** -> AI Confidence: **99.29%**
528. **`app/code/Magento/Customer/view/frontend/templates/account/customer.phtml`** -> AI Confidence: **99.29%**
529. **`app/code/Magento/Customer/view/frontend/templates/account/link/authorization.phtml`** -> AI Confidence: **99.29%**
530. **`app/code/Magento/Customer/view/frontend/templates/account/link/my-account.phtml`** -> AI Confidence: **99.29%**
531. **`app/code/Magento/Customer/view/frontend/templates/additionalinfocustomer.phtml`** -> AI Confidence: **99.29%**
532. **`app/code/Magento/Customer/view/frontend/templates/js/components.phtml`** -> AI Confidence: **99.29%**
533. **`app/code/Magento/Customer/view/frontend/templates/js/customer-data.phtml`** -> AI Confidence: **99.29%**
534. **`app/code/Magento/Customer/view/frontend/templates/js/customer-data/invalidation-rules.phtml`** -> AI Confidence: **99.29%**
535. **`app/code/Magento/Customer/view/frontend/templates/messages/confirmAccountErrorMessage.phtml`** -> AI Confidence: **99.29%**
536. **`app/code/Magento/Customer/view/frontend/templates/messages/confirmAccountSuccessMessage.phtml`** -> AI Confidence: **99.29%**
537. **`app/code/Magento/Customer/view/frontend/templates/messages/customerAlreadyExistsErrorMessage.phtml`** -> AI Confidence: **99.29%**
538. **`app/code/Magento/Customer/view/frontend/templates/messages/customerVatBillingAddressSuccessMessage.phtml`** -> AI Confidence: **99.29%**
539. **`app/code/Magento/Customer/view/frontend/templates/messages/customerVatShippingAddressSuccessMessage.phtml`** -> AI Confidence: **99.29%**
540. **`app/code/Magento/Customer/view/frontend/templates/widget/gender.phtml`** -> AI Confidence: **99.29%**
541. **`app/code/Magento/CustomerAnalytics/registration.php`** -> AI Confidence: **99.29%**
542. **`app/code/Magento/Dhl/view/adminhtml/templates/unitofmeasure.phtml`** -> AI Confidence: **99.29%**
543. **`app/code/Magento/Directory/view/frontend/templates/currency.phtml`** -> AI Confidence: **99.29%**
544. **`app/code/Magento/Directory/view/frontend/templates/currency/switch.phtml`** -> AI Confidence: **99.29%**
545. **`app/code/Magento/Downloadable/view/adminhtml/templates/sales/items/column/downloadable/name.phtml`** -> AI Confidence: **99.29%**
546. **`app/code/Magento/Downloadable/view/frontend/templates/catalog/product/links.phtml`** -> AI Confidence: **99.29%**
547. **`app/code/Magento/Downloadable/view/frontend/templates/catalog/product/samples.phtml`** -> AI Confidence: **99.29%**
548. **`app/code/Magento/Downloadable/view/frontend/templates/catalog/product/type.phtml`** -> AI Confidence: **99.29%**
549. **`app/code/Magento/Downloadable/view/frontend/templates/customer/products/list.phtml`** -> AI Confidence: **99.29%**
550. **`app/code/Magento/Downloadable/view/frontend/templates/email/order/items/creditmemo/downloadable.phtml`** -> AI Confidence: **99.29%**
551. **`app/code/Magento/Downloadable/view/frontend/templates/email/order/items/invoice/downloadable.phtml`** -> AI Confidence: **99.29%**
552. **`app/code/Magento/Downloadable/view/frontend/templates/email/order/items/order/downloadable.phtml`** -> AI Confidence: **99.29%**
553. **`app/code/Magento/Downloadable/view/frontend/templates/js/components.phtml`** -> AI Confidence: **99.29%**
554. **`app/code/Magento/Downloadable/view/frontend/templates/sales/order/creditmemo/items/renderer/downloadable.phtml`** -> AI Confidence: **99.29%**
555. **`app/code/Magento/Downloadable/view/frontend/templates/sales/order/invoice/items/renderer/downloadable.phtml`** -> AI Confidence: **99.29%**
556. **`app/code/Magento/Downloadable/view/frontend/templates/sales/order/items/renderer/downloadable.phtml`** -> AI Confidence: **99.29%**
557. **`app/code/Magento/Eav/view/adminhtml/templates/attribute/edit/js.phtml`** -> AI Confidence: **99.29%**
558. **`app/code/Magento/Elasticsearch/registration.php`** -> AI Confidence: **99.29%**
559. **`app/code/Magento/Email/view/adminhtml/templates/preview/iframeswitcher.phtml`** -> AI Confidence: **99.29%**
560. **`app/code/Magento/Email/view/adminhtml/templates/template/list.phtml`** -> AI Confidence: **99.29%**
561. **`app/code/Magento/Email/view/adminhtml/templates/template/preview.phtml`** -> AI Confidence: **99.29%**
562. **`app/code/Magento/GiftMessage/view/adminhtml/templates/sales/order/create/items.phtml`** -> AI Confidence: **99.29%**
563. **`app/code/Magento/GiftMessage/view/adminhtml/templates/sales/order/view/items.phtml`** -> AI Confidence: **99.29%**
564. **`app/code/Magento/GiftMessage/view/frontend/templates/cart/gift_options.phtml`** -> AI Confidence: **99.29%**
565. **`app/code/Magento/GiftMessage/view/frontend/templates/cart/item/renderer/actions/gift_options.phtml`** -> AI Confidence: **99.29%**
566. **`app/code/Magento/GoogleAnalytics/view/frontend/templates/ga.phtml`** -> AI Confidence: **99.29%**
567. **`app/code/Magento/GoogleGtag/view/frontend/templates/code.phtml`** -> AI Confidence: **99.29%**
568. **`app/code/Magento/GoogleGtag/view/frontend/templates/ga.phtml`** -> AI Confidence: **99.29%**
569. **`app/code/Magento/GoogleGtag/view/frontend/templates/head.phtml`** -> AI Confidence: **99.29%**
570. **`app/code/Magento/GroupedProduct/view/adminhtml/templates/catalog/product/composite/fieldset/grouped.phtml`** -> AI Confidence: **99.29%**
571. **`app/code/Magento/GroupedProduct/view/base/templates/product/price/final_price.phtml`** -> AI Confidence: **99.29%**
572. **`app/code/Magento/GroupedProduct/view/frontend/templates/product/view/type/default.phtml`** -> AI Confidence: **99.29%**
573. **`app/code/Magento/GroupedProduct/view/frontend/templates/product/view/type/grouped.phtml`** -> AI Confidence: **99.29%**
574. **`app/code/Magento/ImportExport/view/adminhtml/templates/export/form/after.phtml`** -> AI Confidence: **99.29%**
575. **`app/code/Magento/ImportExport/view/adminhtml/templates/import/frame/result.phtml`** -> AI Confidence: **99.29%**
576. **`app/code/Magento/InstantPurchase/view/frontend/templates/button.phtml`** -> AI Confidence: **99.29%**
577. **`app/code/Magento/Integration/view/adminhtml/templates/integration/activate/permissions.phtml`** -> AI Confidence: **99.29%**
578. **`app/code/Magento/Integration/view/adminhtml/templates/integration/activate/permissions/tab/webapi.phtml`** -> AI Confidence: **99.29%**
579. **`app/code/Magento/Integration/view/adminhtml/templates/integration/tokens_exchange.phtml`** -> AI Confidence: **99.29%**
580. **`app/code/Magento/LayeredNavigation/view/frontend/templates/layer/filter.phtml`** -> AI Confidence: **99.29%**
581. **`app/code/Magento/LayeredNavigation/view/frontend/templates/layer/state.phtml`** -> AI Confidence: **99.29%**
582. **`app/code/Magento/LayeredNavigation/view/frontend/templates/layer/view.phtml`** -> AI Confidence: **99.29%**
583. **`app/code/Magento/LoginAsCustomer/registration.php`** -> AI Confidence: **99.29%**
584. **`app/code/Magento/LoginAsCustomerAdminUi/view/adminhtml/templates/confirmation-popup.phtml`** -> AI Confidence: **99.29%**
585. **`app/code/Magento/LoginAsCustomerAssistance/view/adminhtml/templates/not-allowed-popup.phtml`** -> AI Confidence: **99.29%**
586. **`app/code/Magento/LoginAsCustomerFrontendUi/view/frontend/templates/login.phtml`** -> AI Confidence: **99.29%**
587. **`app/code/Magento/Marketplace/view/adminhtml/templates/partners.phtml`** -> AI Confidence: **99.29%**
588. **`app/code/Magento/MediaGalleryCatalogUi/view/adminhtml/templates/url_filter_applier.phtml`** -> AI Confidence: **99.29%**
589. **`app/code/Magento/MediaGalleryUi/view/adminhtml/templates/container.phtml`** -> AI Confidence: **99.29%**
590. **`app/code/Magento/MediaGalleryUi/view/adminhtml/templates/image_details_standalone.phtml`** -> AI Confidence: **99.29%**
591. **`app/code/Magento/MediaGalleryUi/view/adminhtml/templates/image_edit_details.phtml`** -> AI Confidence: **99.29%**
592. **`app/code/Magento/MediaGalleryUi/view/adminhtml/templates/image_edit_details_standalone.phtml`** -> AI Confidence: **99.29%**
593. **`app/code/Magento/Msrp/view/base/templates/product/price/msrp.phtml`** -> AI Confidence: **99.29%**
594. **`app/code/Magento/Msrp/view/frontend/templates/render/item/price_msrp_item.phtml`** -> AI Confidence: **99.29%**
595. **`app/code/Magento/Msrp/view/frontend/templates/render/item/price_msrp_rss.phtml`** -> AI Confidence: **99.29%**
596. **`app/code/Magento/Multishipping/view/frontend/templates/js/components.phtml`** -> AI Confidence: **99.29%**
597. **`app/code/Magento/Multishipping/view/frontend/templates/multishipping/item/default.phtml`** -> AI Confidence: **99.29%**
598. **`app/code/Magento/NewRelicReporting/view/base/templates/html/inline_js.phtml`** -> AI Confidence: **99.29%**
599. **`app/code/Magento/Newsletter/view/adminhtml/templates/preview/store.phtml`** -> AI Confidence: **99.29%**
600. **`app/code/Magento/Newsletter/view/adminhtml/templates/queue/list.phtml`** -> AI Confidence: **99.29%**
601. **`app/code/Magento/Newsletter/view/adminhtml/templates/queue/preview.phtml`** -> AI Confidence: **99.29%**
602. **`app/code/Magento/Newsletter/view/adminhtml/templates/template/list.phtml`** -> AI Confidence: **99.29%**
603. **`app/code/Magento/Newsletter/view/adminhtml/templates/template/preview.phtml`** -> AI Confidence: **99.29%**
604. **`app/code/Magento/Newsletter/view/frontend/templates/form/register/newsletter.phtml`** -> AI Confidence: **99.29%**
605. **`app/code/Magento/Newsletter/view/frontend/templates/js/components.phtml`** -> AI Confidence: **99.29%**
606. **`app/code/Magento/Newsletter/view/frontend/templates/messages/localizedSubscriptionErrorMessage.phtml`** -> AI Confidence: **99.29%**
607. **`app/code/Magento/OfflinePayments/view/adminhtml/templates/form/banktransfer.phtml`** -> AI Confidence: **99.29%**
608. **`app/code/Magento/OfflinePayments/view/adminhtml/templates/form/cashondelivery.phtml`** -> AI Confidence: **99.29%**
609. **`app/code/Magento/OfflinePayments/view/adminhtml/templates/form/checkmo.phtml`** -> AI Confidence: **99.29%**
610. **`app/code/Magento/OfflinePayments/view/adminhtml/templates/info/checkmo.phtml`** -> AI Confidence: **99.29%**
611. **`app/code/Magento/OfflinePayments/view/adminhtml/templates/info/pdf/checkmo.phtml`** -> AI Confidence: **99.29%**
612. **`app/code/Magento/OfflinePayments/view/adminhtml/templates/info/pdf/purchaseorder.phtml`** -> AI Confidence: **99.29%**
613. **`app/code/Magento/OfflinePayments/view/adminhtml/templates/info/purchaseorder.phtml`** -> AI Confidence: **99.29%**
614. **`app/code/Magento/OfflinePayments/view/base/templates/info/pdf/checkmo.phtml`** -> AI Confidence: **99.29%**
615. **`app/code/Magento/OfflinePayments/view/base/templates/info/pdf/purchaseorder.phtml`** -> AI Confidence: **99.29%**
616. **`app/code/Magento/OfflinePayments/view/frontend/templates/form/banktransfer.phtml`** -> AI Confidence: **99.29%**
617. **`app/code/Magento/OfflinePayments/view/frontend/templates/form/cashondelivery.phtml`** -> AI Confidence: **99.29%**
618. **`app/code/Magento/OfflinePayments/view/frontend/templates/form/checkmo.phtml`** -> AI Confidence: **99.29%**
619. **`app/code/Magento/OfflinePayments/view/frontend/templates/info/checkmo.phtml`** -> AI Confidence: **99.29%**
620. **`app/code/Magento/OfflinePayments/view/frontend/templates/multishipping/checkmo_form.phtml`** -> AI Confidence: **99.29%**
621. **`app/code/Magento/OrderCancellationUi/view/frontend/templates/cancel-order-modal.phtml`** -> AI Confidence: **99.29%**
622. **`app/code/Magento/OrderCancellationUi/view/frontend/templates/order/history.phtml`** -> AI Confidence: **99.29%**
623. **`app/code/Magento/OrderCancellationUi/view/frontend/templates/order/info/buttons.phtml`** -> AI Confidence: **99.29%**
624. **`app/code/Magento/OrderCancellationUi/view/frontend/templates/order/recent.phtml`** -> AI Confidence: **99.29%**
625. **`app/code/Magento/PageCache/view/frontend/templates/form_key_provider.phtml`** -> AI Confidence: **99.29%**
626. **`app/code/Magento/PageCache/view/frontend/templates/javascript.phtml`** -> AI Confidence: **99.29%**
627. **`app/code/Magento/PageCache/view/frontend/templates/js/components.phtml`** -> AI Confidence: **99.29%**
628. **`app/code/Magento/Payment/view/adminhtml/templates/form/cc.phtml`** -> AI Confidence: **99.29%**
629. **`app/code/Magento/Payment/view/adminhtml/templates/info/default.phtml`** -> AI Confidence: **99.29%**
630. **`app/code/Magento/Payment/view/adminhtml/templates/info/instructions.phtml`** -> AI Confidence: **99.29%**
631. **`app/code/Magento/Payment/view/adminhtml/templates/info/pdf/default.phtml`** -> AI Confidence: **99.29%**
632. **`app/code/Magento/Payment/view/adminhtml/templates/info/substitution.phtml`** -> AI Confidence: **99.29%**
633. **`app/code/Magento/Payment/view/adminhtml/templates/transparent/info.phtml`** -> AI Confidence: **99.29%**
634. **`app/code/Magento/Payment/view/adminhtml/templates/transparent/redirect.phtml`** -> AI Confidence: **99.29%**
635. **`app/code/Magento/Payment/view/base/templates/info/pdf/default.phtml`** -> AI Confidence: **99.29%**
636. **`app/code/Magento/Payment/view/frontend/templates/info/default.phtml`** -> AI Confidence: **99.29%**
637. **`app/code/Magento/Payment/view/frontend/templates/info/instructions.phtml`** -> AI Confidence: **99.29%**
638. **`app/code/Magento/Payment/view/frontend/templates/info/pdf/default.phtml`** -> AI Confidence: **99.29%**
639. **`app/code/Magento/Payment/view/frontend/templates/transparent/info.phtml`** -> AI Confidence: **99.29%**
640. **`app/code/Magento/Payment/view/frontend/templates/transparent/redirect.phtml`** -> AI Confidence: **99.29%**
641. **`app/code/Magento/Paypal/view/adminhtml/templates/billing/agreement/form.phtml`** -> AI Confidence: **99.29%**
642. **`app/code/Magento/Paypal/view/adminhtml/templates/billing/agreement/view/tab/info.phtml`** -> AI Confidence: **99.29%**
643. **`app/code/Magento/Paypal/view/adminhtml/templates/payflowpro/vault.phtml`** -> AI Confidence: **99.29%**
644. **`app/code/Magento/Paypal/view/adminhtml/templates/payment/form/billing/agreement.phtml`** -> AI Confidence: **99.29%**
645. **`app/code/Magento/Paypal/view/adminhtml/templates/system/config/api_wizard.phtml`** -> AI Confidence: **99.29%**
646. **`app/code/Magento/Paypal/view/adminhtml/templates/system/config/bml_api_wizard.phtml`** -> AI Confidence: **99.29%**
647. **`app/code/Magento/Paypal/view/adminhtml/templates/system/config/fieldset/hint.phtml`** -> AI Confidence: **99.29%**
648. **`app/code/Magento/Paypal/view/frontend/templates/bml.phtml`** -> AI Confidence: **99.29%**
649. **`app/code/Magento/Paypal/view/frontend/templates/express/review.phtml`** -> AI Confidence: **99.29%**
650. **`app/code/Magento/Paypal/view/frontend/templates/express/review/shipping/method.phtml`** -> AI Confidence: **99.29%**
651. **`app/code/Magento/Paypal/view/frontend/templates/express/shortcut.phtml`** -> AI Confidence: **99.29%**
652. **`app/code/Magento/Paypal/view/frontend/templates/express/shortcut/container.phtml`** -> AI Confidence: **99.29%**
653. **`app/code/Magento/Paypal/view/frontend/templates/hss/form.phtml`** -> AI Confidence: **99.29%**
654. **`app/code/Magento/Paypal/view/frontend/templates/hss/info.phtml`** -> AI Confidence: **99.29%**
655. **`app/code/Magento/Paypal/view/frontend/templates/hss/review/button.phtml`** -> AI Confidence: **99.29%**
656. **`app/code/Magento/Paypal/view/frontend/templates/js/components.phtml`** -> AI Confidence: **99.29%**
657. **`app/code/Magento/Paypal/view/frontend/templates/partner/logo.phtml`** -> AI Confidence: **99.29%**
658. **`app/code/Magento/Paypal/view/frontend/templates/payflowadvanced/form.phtml`** -> AI Confidence: **99.29%**
659. **`app/code/Magento/Paypal/view/frontend/templates/payflowadvanced/info.phtml`** -> AI Confidence: **99.29%**
660. **`app/code/Magento/Paypal/view/frontend/templates/payflowlink/form.phtml`** -> AI Confidence: **99.29%**
661. **`app/code/Magento/Paypal/view/frontend/templates/payflowlink/info.phtml`** -> AI Confidence: **99.29%**
662. **`app/code/Magento/Paypal/view/frontend/templates/paylater/banner.phtml`** -> AI Confidence: **99.29%**
663. **`app/code/Magento/Paypal/view/frontend/templates/payment/form/billing/agreement.phtml`** -> AI Confidence: **99.29%**
664. **`app/code/Magento/Paypal/view/frontend/templates/payment/mark.phtml`** -> AI Confidence: **99.29%**
665. **`app/code/Magento/Paypal/view/frontend/templates/payment/redirect.phtml`** -> AI Confidence: **99.29%**
666. **`app/code/Magento/Persistent/view/frontend/templates/additional.phtml`** -> AI Confidence: **99.29%**
667. **`app/code/Magento/Persistent/view/frontend/templates/remember_me.phtml`** -> AI Confidence: **99.29%**
668. **`app/code/Magento/ProductAlert/view/frontend/templates/email/email.phtml`** -> AI Confidence: **99.29%**
669. **`app/code/Magento/ProductAlert/view/frontend/templates/email/price.phtml`** -> AI Confidence: **99.29%**
670. **`app/code/Magento/ProductAlert/view/frontend/templates/email/stock.phtml`** -> AI Confidence: **99.29%**
671. **`app/code/Magento/ProductAlert/view/frontend/templates/product/view.phtml`** -> AI Confidence: **99.29%**
672. **`app/code/Magento/ProductVideo/view/frontend/templates/product/view/gallery.phtml`** -> AI Confidence: **99.29%**
673. **`app/code/Magento/QuoteAnalytics/registration.php`** -> AI Confidence: **99.29%**
674. **`app/code/Magento/ReleaseNotification/registration.php`** -> AI Confidence: **99.29%**
675. **`app/code/Magento/RemoteStorage/registration.php`** -> AI Confidence: **99.29%**
676. **`app/code/Magento/Reports/view/adminhtml/templates/report/refresh/statistics.phtml`** -> AI Confidence: **99.29%**
677. **`app/code/Magento/Reports/view/adminhtml/templates/report/wishlist.phtml`** -> AI Confidence: **99.29%**
678. **`app/code/Magento/Reports/view/adminhtml/templates/store/switcher.phtml`** -> AI Confidence: **99.29%**
679. **`app/code/Magento/Reports/view/adminhtml/templates/store/switcher/enhanced.phtml`** -> AI Confidence: **99.29%**
680. **`app/code/Magento/Reports/view/frontend/templates/js/components.phtml`** -> AI Confidence: **99.29%**
681. **`app/code/Magento/Reports/view/frontend/templates/product/report_viewed_product.phtml`** -> AI Confidence: **99.29%**
682. **`app/code/Magento/Reports/view/frontend/templates/product/widget/viewed/item.phtml`** -> AI Confidence: **99.29%**
683. **`app/code/Magento/Reports/view/frontend/templates/widget/compared/column/compared_default_list.phtml`** -> AI Confidence: **99.29%**
684. **`app/code/Magento/Reports/view/frontend/templates/widget/compared/column/compared_images_list.phtml`** -> AI Confidence: **99.29%**
685. **`app/code/Magento/Reports/view/frontend/templates/widget/compared/content/compared_grid.phtml`** -> AI Confidence: **99.29%**
686. **`app/code/Magento/Reports/view/frontend/templates/widget/compared/content/compared_list.phtml`** -> AI Confidence: **99.29%**
687. **`app/code/Magento/Reports/view/frontend/templates/widget/viewed/column/viewed_default_list.phtml`** -> AI Confidence: **99.29%**
688. **`app/code/Magento/Reports/view/frontend/templates/widget/viewed/column/viewed_images_list.phtml`** -> AI Confidence: **99.29%**
689. **`app/code/Magento/Reports/view/frontend/templates/widget/viewed/content/viewed_grid.phtml`** -> AI Confidence: **99.29%**
690. **`app/code/Magento/Reports/view/frontend/templates/widget/viewed/content/viewed_list.phtml`** -> AI Confidence: **99.29%**
691. **`app/code/Magento/Review/view/adminhtml/templates/rating/detailed.phtml`** -> AI Confidence: **99.29%**
692. **`app/code/Magento/Review/view/adminhtml/templates/rating/options.phtml`** -> AI Confidence: **99.29%**
693. **`app/code/Magento/Review/view/adminhtml/templates/rating/stars/detailed.phtml`** -> AI Confidence: **99.29%**
694. **`app/code/Magento/Review/view/adminhtml/templates/rating/stars/summary.phtml`** -> AI Confidence: **99.29%**
695. **`app/code/Magento/Review/view/adminhtml/templates/rss/grid/link.phtml`** -> AI Confidence: **99.29%**
696. **`app/code/Magento/Review/view/frontend/templates/empty.phtml`** -> AI Confidence: **99.29%**
697. **`app/code/Magento/Review/view/frontend/templates/helper/summary.phtml`** -> AI Confidence: **99.29%**
698. **`app/code/Magento/Review/view/frontend/templates/helper/summary_short.phtml`** -> AI Confidence: **99.29%**
699. **`app/code/Magento/Review/view/frontend/templates/product/view/count.phtml`** -> AI Confidence: **99.29%**
700. **`app/code/Magento/Review/view/frontend/templates/product/view/other.phtml`** -> AI Confidence: **99.29%**
701. **`app/code/Magento/Review/view/frontend/templates/redirect.phtml`** -> AI Confidence: **99.29%**
702. **`app/code/Magento/Review/view/frontend/templates/review.phtml`** -> AI Confidence: **99.29%**
703. **`app/code/Magento/Review/view/frontend/templates/view.phtml`** -> AI Confidence: **99.29%**
704. **`app/code/Magento/ReviewAnalytics/registration.php`** -> AI Confidence: **99.29%**
705. **`app/code/Magento/Robots/view/frontend/templates/robots.phtml`** -> AI Confidence: **99.29%**
706. **`app/code/Magento/Rss/view/frontend/templates/feeds.phtml`** -> AI Confidence: **99.29%**
707. **`app/code/Magento/Sales/view/adminhtml/templates/items/column/name.phtml`** -> AI Confidence: **99.29%**
708. **`app/code/Magento/Sales/view/adminhtml/templates/items/column/qty.phtml`** -> AI Confidence: **99.29%**
709. **`app/code/Magento/Sales/view/adminhtml/templates/items/price/row.phtml`** -> AI Confidence: **99.29%**
710. **`app/code/Magento/Sales/view/adminhtml/templates/items/price/total.phtml`** -> AI Confidence: **99.29%**
711. **`app/code/Magento/Sales/view/adminhtml/templates/items/price/unit.phtml`** -> AI Confidence: **99.29%**
712. **`app/code/Magento/Sales/view/adminhtml/templates/items/renderer/default.phtml`** -> AI Confidence: **99.29%**
713. **`app/code/Magento/Sales/view/adminhtml/templates/order/create/abstract.phtml`** -> AI Confidence: **99.29%**
714. **`app/code/Magento/Sales/view/adminhtml/templates/order/create/form.phtml`** -> AI Confidence: **99.29%**
715. **`app/code/Magento/Sales/view/adminhtml/templates/order/create/form/address.phtml`** -> AI Confidence: **99.29%**
716. **`app/code/Magento/Sales/view/adminhtml/templates/order/create/giftmessage.phtml`** -> AI Confidence: **99.29%**
717. **`app/code/Magento/Sales/view/adminhtml/templates/order/create/items/price/row.phtml`** -> AI Confidence: **99.29%**
718. **`app/code/Magento/Sales/view/adminhtml/templates/order/create/items/price/total.phtml`** -> AI Confidence: **99.29%**
719. **`app/code/Magento/Sales/view/adminhtml/templates/order/create/items/price/unit.phtml`** -> AI Confidence: **99.29%**
720. **`app/code/Magento/Sales/view/adminhtml/templates/order/create/newsletter/form.phtml`** -> AI Confidence: **99.29%**
721. **`app/code/Magento/Sales/view/adminhtml/templates/order/create/sidebar/items.phtml`** -> AI Confidence: **99.29%**
722. **`app/code/Magento/Sales/view/adminhtml/templates/order/create/totals/default.phtml`** -> AI Confidence: **99.29%**
723. **`app/code/Magento/Sales/view/adminhtml/templates/order/create/totals/shipping.phtml`** -> AI Confidence: **99.29%**
724. **`app/code/Magento/Sales/view/adminhtml/templates/order/create/totals/tax.phtml`** -> AI Confidence: **99.29%**
725. **`app/code/Magento/Sales/view/adminhtml/templates/order/creditmemo/create/form.phtml`** -> AI Confidence: **99.29%**
726. **`app/code/Magento/Sales/view/adminhtml/templates/order/creditmemo/create/items/renderer/default.phtml`** -> AI Confidence: **99.29%**
727. **`app/code/Magento/Sales/view/adminhtml/templates/order/details.phtml`** -> AI Confidence: **99.29%**
728. **`app/code/Magento/Sales/view/adminhtml/templates/order/giftoptions.phtml`** -> AI Confidence: **99.29%**
729. **`app/code/Magento/Sales/view/adminhtml/templates/order/invoice/create/form.phtml`** -> AI Confidence: **99.29%**
730. **`app/code/Magento/Sales/view/adminhtml/templates/order/invoice/create/items/renderer/default.phtml`** -> AI Confidence: **99.29%**
731. **`app/code/Magento/Sales/view/adminhtml/templates/order/totalbar.phtml`** -> AI Confidence: **99.29%**
732. **`app/code/Magento/Sales/view/adminhtml/templates/order/totals.phtml`** -> AI Confidence: **99.29%**
733. **`app/code/Magento/Sales/view/adminhtml/templates/order/totals/discount.phtml`** -> AI Confidence: **99.29%**
734. **`app/code/Magento/Sales/view/adminhtml/templates/order/totals/due.phtml`** -> AI Confidence: **99.29%**
735. **`app/code/Magento/Sales/view/adminhtml/templates/order/totals/footer.phtml`** -> AI Confidence: **99.29%**
736. **`app/code/Magento/Sales/view/adminhtml/templates/order/totals/grand.phtml`** -> AI Confidence: **99.29%**
737. **`app/code/Magento/Sales/view/adminhtml/templates/order/totals/item.phtml`** -> AI Confidence: **99.29%**
738. **`app/code/Magento/Sales/view/adminhtml/templates/order/totals/main.phtml`** -> AI Confidence: **99.29%**
739. **`app/code/Magento/Sales/view/adminhtml/templates/order/totals/paid.phtml`** -> AI Confidence: **99.29%**
740. **`app/code/Magento/Sales/view/adminhtml/templates/order/totals/refunded.phtml`** -> AI Confidence: **99.29%**
741. **`app/code/Magento/Sales/view/adminhtml/templates/order/totals/shipping.phtml`** -> AI Confidence: **99.29%**
742. **`app/code/Magento/Sales/view/adminhtml/templates/order/totals/tax.phtml`** -> AI Confidence: **99.29%**
743. **`app/code/Magento/Sales/view/adminhtml/templates/order/view/giftmessage.phtml`** -> AI Confidence: **99.29%**
744. **`app/code/Magento/Sales/view/adminhtml/templates/order/view/info.phtml`** -> AI Confidence: **99.29%**
745. **`app/code/Magento/Sales/view/adminhtml/templates/order/view/items.phtml`** -> AI Confidence: **99.29%**
746. **`app/code/Magento/Sales/view/adminhtml/templates/order/view/items/renderer/default.phtml`** -> AI Confidence: **99.29%**
747. **`app/code/Magento/Sales/view/adminhtml/templates/page/js/components.phtml`** -> AI Confidence: **99.29%**
748. **`app/code/Magento/Sales/view/adminhtml/templates/rss/order/grid/link.phtml`** -> AI Confidence: **99.29%**
749. **`app/code/Magento/Sales/view/adminhtml/templates/transactions/detail.phtml`** -> AI Confidence: **99.29%**
750. **`app/code/Magento/Sales/view/frontend/templates/email/creditmemo/items.phtml`** -> AI Confidence: **99.29%**
751. **`app/code/Magento/Sales/view/frontend/templates/email/invoice/items.phtml`** -> AI Confidence: **99.29%**
752. **`app/code/Magento/Sales/view/frontend/templates/email/items.phtml`** -> AI Confidence: **99.29%**
753. **`app/code/Magento/Sales/view/frontend/templates/email/items/creditmemo/default.phtml`** -> AI Confidence: **99.29%**
754. **`app/code/Magento/Sales/view/frontend/templates/email/items/invoice/default.phtml`** -> AI Confidence: **99.29%**
755. **`app/code/Magento/Sales/view/frontend/templates/email/items/order/default.phtml`** -> AI Confidence: **99.29%**
756. **`app/code/Magento/Sales/view/frontend/templates/email/items/price/row.phtml`** -> AI Confidence: **99.29%**
757. **`app/code/Magento/Sales/view/frontend/templates/email/items/shipment/default.phtml`** -> AI Confidence: **99.29%**
758. **`app/code/Magento/Sales/view/frontend/templates/email/shipment/items.phtml`** -> AI Confidence: **99.29%**
759. **`app/code/Magento/Sales/view/frontend/templates/email/shipment/track.phtml`** -> AI Confidence: **99.29%**
760. **`app/code/Magento/Sales/view/frontend/templates/items/price/total_after_discount.phtml`** -> AI Confidence: **99.29%**
761. **`app/code/Magento/Sales/view/frontend/templates/js/components.phtml`** -> AI Confidence: **99.29%**
762. **`app/code/Magento/Sales/view/frontend/templates/order/creditmemo/items.phtml`** -> AI Confidence: **99.29%**
763. **`app/code/Magento/Sales/view/frontend/templates/order/creditmemo/items/renderer/default.phtml`** -> AI Confidence: **99.29%**
764. **`app/code/Magento/Sales/view/frontend/templates/order/history.phtml`** -> AI Confidence: **99.29%**
765. **`app/code/Magento/Sales/view/frontend/templates/order/info/buttons.phtml`** -> AI Confidence: **99.29%**
766. **`app/code/Magento/Sales/view/frontend/templates/order/info/buttons/rss.phtml`** -> AI Confidence: **99.29%**
767. **`app/code/Magento/Sales/view/frontend/templates/order/invoice/items.phtml`** -> AI Confidence: **99.29%**
768. **`app/code/Magento/Sales/view/frontend/templates/order/invoice/items/renderer/default.phtml`** -> AI Confidence: **99.29%**
769. **`app/code/Magento/Sales/view/frontend/templates/order/items/renderer/default.phtml`** -> AI Confidence: **99.29%**
770. **`app/code/Magento/Sales/view/frontend/templates/order/order_status.phtml`** -> AI Confidence: **99.29%**
771. **`app/code/Magento/Sales/view/frontend/templates/order/shipment/items/renderer/default.phtml`** -> AI Confidence: **99.29%**
772. **`app/code/Magento/Sales/view/frontend/templates/order/totals.phtml`** -> AI Confidence: **99.29%**
773. **`app/code/Magento/SalesAnalytics/registration.php`** -> AI Confidence: **99.29%**
774. **`app/code/Magento/SalesRule/view/adminhtml/templates/tab/coupons.phtml`** -> AI Confidence: **99.29%**
775. **`app/code/Magento/Search/view/frontend/templates/form.mini.phtml`** -> AI Confidence: **99.29%**
776. **`app/code/Magento/Search/view/frontend/templates/term.phtml`** -> AI Confidence: **99.29%**
777. **`app/code/Magento/Security/view/adminhtml/templates/page/activity_link.phtml`** -> AI Confidence: **99.29%**
778. **`app/code/Magento/Security/view/adminhtml/templates/session/activity.phtml`** -> AI Confidence: **99.29%**
779. **`app/code/Magento/Security/view/adminhtml/templates/system/config/session_size_admin/modal_content_body.phtml`** -> AI Confidence: **99.29%**
780. **`app/code/Magento/Security/view/adminhtml/templates/system/config/session_size_storefront/modal_content_body.phtml`** -> AI Confidence: **99.29%**
781. **`app/code/Magento/Shipping/view/adminhtml/templates/create/form.phtml`** -> AI Confidence: **99.29%**
782. **`app/code/Magento/Shipping/view/adminhtml/templates/create/items/renderer/default.phtml`** -> AI Confidence: **99.29%**
783. **`app/code/Magento/Shipping/view/adminhtml/templates/order/packaging/grid.phtml`** -> AI Confidence: **99.29%**
784. **`app/code/Magento/Shipping/view/adminhtml/templates/order/packaging/packed.phtml`** -> AI Confidence: **99.29%**
785. **`app/code/Magento/Shipping/view/adminhtml/templates/order/view/info.phtml`** -> AI Confidence: **99.29%**
786. **`app/code/Magento/Shipping/view/adminhtml/templates/view/items.phtml`** -> AI Confidence: **99.29%**
787. **`app/code/Magento/Shipping/view/frontend/templates/items.phtml`** -> AI Confidence: **99.29%**
788. **`app/code/Magento/Shipping/view/frontend/templates/tracking/details.phtml`** -> AI Confidence: **99.29%**
789. **`app/code/Magento/Shipping/view/frontend/templates/tracking/link.phtml`** -> AI Confidence: **99.29%**
790. **`app/code/Magento/Shipping/view/frontend/templates/tracking/progress.phtml`** -> AI Confidence: **99.29%**
791. **`app/code/Magento/Sitemap/view/adminhtml/templates/js.phtml`** -> AI Confidence: **99.29%**
792. **`app/code/Magento/Store/view/frontend/templates/switch/flags.phtml`** -> AI Confidence: **99.29%**
793. **`app/code/Magento/Store/view/frontend/templates/switch/languages.phtml`** -> AI Confidence: **99.29%**
794. **`app/code/Magento/Store/view/frontend/templates/switch/stores.phtml`** -> AI Confidence: **99.29%**
795. **`app/code/Magento/Swagger/view/frontend/templates/swagger-ui/index.phtml`** -> AI Confidence: **99.29%**
796. **`app/code/Magento/Swatches/view/adminhtml/templates/catalog/product/attribute/js.phtml`** -> AI Confidence: **99.29%**
797. **`app/code/Magento/Swatches/view/frontend/templates/product/view/renderer.phtml`** -> AI Confidence: **99.29%**
798. **`app/code/Magento/Tax/view/adminhtml/templates/items/price/row.phtml`** -> AI Confidence: **99.29%**
799. **`app/code/Magento/Tax/view/adminhtml/templates/items/price/total.phtml`** -> AI Confidence: **99.29%**
800. **`app/code/Magento/Tax/view/adminhtml/templates/order/create/items/price/row.phtml`** -> AI Confidence: **99.29%**
801. **`app/code/Magento/Tax/view/adminhtml/templates/order/create/items/price/total.phtml`** -> AI Confidence: **99.29%**
802. **`app/code/Magento/Tax/view/adminhtml/templates/order/create/items/price/unit.phtml`** -> AI Confidence: **99.29%**
803. **`app/code/Magento/Tax/view/adminhtml/templates/rate/form.phtml`** -> AI Confidence: **99.29%**
804. **`app/code/Magento/Tax/view/adminhtml/templates/toolbar/class/add.phtml`** -> AI Confidence: **99.29%**
805. **`app/code/Magento/Tax/view/adminhtml/templates/toolbar/rate/add.phtml`** -> AI Confidence: **99.29%**
806. **`app/code/Magento/Tax/view/adminhtml/templates/toolbar/rule/add.phtml`** -> AI Confidence: **99.29%**
807. **`app/code/Magento/Tax/view/base/templates/pricing/adjustment.phtml`** -> AI Confidence: **99.29%**
808. **`app/code/Magento/Tax/view/base/templates/pricing/adjustment/bundle.phtml`** -> AI Confidence: **99.29%**
809. **`app/code/Magento/Tax/view/frontend/templates/email/items/price/row.phtml`** -> AI Confidence: **99.29%**
810. **`app/code/Magento/Tax/view/frontend/templates/item/price/row.phtml`** -> AI Confidence: **99.29%**
811. **`app/code/Magento/Tax/view/frontend/templates/item/price/total_after_discount.phtml`** -> AI Confidence: **99.29%**
812. **`app/code/Magento/Tax/view/frontend/templates/item/price/unit.phtml`** -> AI Confidence: **99.29%**
813. **`app/code/Magento/Tax/view/frontend/templates/order/tax.phtml`** -> AI Confidence: **99.29%**
814. **`app/code/Magento/TaxImportExport/view/adminhtml/templates/importExportHeader.phtml`** -> AI Confidence: **99.29%**
815. **`app/code/Magento/Theme/view/adminhtml/templates/browser/content.phtml`** -> AI Confidence: **99.29%**
816. **`app/code/Magento/Theme/view/adminhtml/templates/browser/content/files.phtml`** -> AI Confidence: **99.29%**
817. **`app/code/Magento/Theme/view/adminhtml/templates/title.phtml`** -> AI Confidence: **99.29%**
818. **`app/code/Magento/Theme/view/base/templates/root.phtml`** -> AI Confidence: **99.29%**
819. **`app/code/Magento/Theme/view/frontend/templates/callouts/left_col.phtml`** -> AI Confidence: **99.29%**
820. **`app/code/Magento/Theme/view/frontend/templates/callouts/right_col.phtml`** -> AI Confidence: **99.29%**
821. **`app/code/Magento/Theme/view/frontend/templates/html/absolute_footer.phtml`** -> AI Confidence: **99.29%**
822. **`app/code/Magento/Theme/view/frontend/templates/html/block.phtml`** -> AI Confidence: **99.29%**
823. **`app/code/Magento/Theme/view/frontend/templates/html/breadcrumbs.phtml`** -> AI Confidence: **99.29%**
824. **`app/code/Magento/Theme/view/frontend/templates/html/bugreport.phtml`** -> AI Confidence: **99.29%**
825. **`app/code/Magento/Theme/view/frontend/templates/html/collapsible.phtml`** -> AI Confidence: **99.29%**
826. **`app/code/Magento/Theme/view/frontend/templates/html/container.phtml`** -> AI Confidence: **99.29%**
827. **`app/code/Magento/Theme/view/frontend/templates/html/copyright.phtml`** -> AI Confidence: **99.29%**
828. **`app/code/Magento/Theme/view/frontend/templates/html/header.phtml`** -> AI Confidence: **99.29%**
829. **`app/code/Magento/Theme/view/frontend/templates/html/header/criticalCss.phtml`** -> AI Confidence: **99.29%**
830. **`app/code/Magento/Theme/view/frontend/templates/html/header/logo.phtml`** -> AI Confidence: **99.29%**
831. **`app/code/Magento/Theme/view/frontend/templates/html/main_css_preloader.phtml`** -> AI Confidence: **99.29%**
832. **`app/code/Magento/Theme/view/frontend/templates/html/messages.phtml`** -> AI Confidence: **99.29%**
833. **`app/code/Magento/Theme/view/frontend/templates/html/notices.phtml`** -> AI Confidence: **99.29%**
834. **`app/code/Magento/Theme/view/frontend/templates/html/pager.phtml`** -> AI Confidence: **99.29%**
835. **`app/code/Magento/Theme/view/frontend/templates/html/print.phtml`** -> AI Confidence: **99.29%**
836. **`app/code/Magento/Theme/view/frontend/templates/html/sections.phtml`** -> AI Confidence: **99.29%**
837. **`app/code/Magento/Theme/view/frontend/templates/html/skip.phtml`** -> AI Confidence: **99.29%**
838. **`app/code/Magento/Theme/view/frontend/templates/html/skiptarget.phtml`** -> AI Confidence: **99.29%**
839. **`app/code/Magento/Theme/view/frontend/templates/html/title.phtml`** -> AI Confidence: **99.29%**
840. **`app/code/Magento/Theme/view/frontend/templates/html/topmenu.phtml`** -> AI Confidence: **99.29%**
841. **`app/code/Magento/Theme/view/frontend/templates/js/components.phtml`** -> AI Confidence: **99.29%**
842. **`app/code/Magento/Theme/view/frontend/templates/js/cookie.phtml`** -> AI Confidence: **99.29%**
843. **`app/code/Magento/Theme/view/frontend/templates/js/cookie_status.phtml`** -> AI Confidence: **99.29%**
844. **`app/code/Magento/Theme/view/frontend/templates/js/css_rel_preload.phtml`** -> AI Confidence: **99.29%**
845. **`app/code/Magento/Theme/view/frontend/templates/link.phtml`** -> AI Confidence: **99.29%**
846. **`app/code/Magento/Theme/view/frontend/templates/template.phtml`** -> AI Confidence: **99.29%**
847. **`app/code/Magento/Translation/view/base/templates/translate.phtml`** -> AI Confidence: **99.29%**
848. **`app/code/Magento/Ui/view/base/templates/container/content/default.phtml`** -> AI Confidence: **99.29%**
849. **`app/code/Magento/Ui/view/base/templates/context/default.phtml`** -> AI Confidence: **99.29%**
850. **`app/code/Magento/Ui/view/base/templates/control/button/default.phtml`** -> AI Confidence: **99.29%**
851. **`app/code/Magento/Ui/view/base/templates/control/button/split.phtml`** -> AI Confidence: **99.29%**
852. **`app/code/Magento/Ui/view/base/templates/label/default.phtml`** -> AI Confidence: **99.29%**
853. **`app/code/Magento/Ui/view/base/templates/logger.phtml`** -> AI Confidence: **99.29%**
854. **`app/code/Magento/Ui/view/base/templates/wysiwyg/active_editor.phtml`** -> AI Confidence: **99.29%**
855. **`app/code/Magento/UrlRewrite/view/adminhtml/templates/categories.phtml`** -> AI Confidence: **99.29%**
856. **`app/code/Magento/UrlRewrite/view/adminhtml/templates/edit.phtml`** -> AI Confidence: **99.29%**
857. **`app/code/Magento/UrlRewrite/view/adminhtml/templates/messages/url_duplicate_message.phtml`** -> AI Confidence: **99.29%**
858. **`app/code/Magento/Variable/view/adminhtml/templates/system/variable/js.phtml`** -> AI Confidence: **99.29%**
859. **`app/code/Magento/Vault/view/adminhtml/templates/form/vault.phtml`** -> AI Confidence: **99.29%**
860. **`app/code/Magento/Weee/view/adminhtml/templates/items/price/row.phtml`** -> AI Confidence: **99.29%**
861. **`app/code/Magento/Weee/view/adminhtml/templates/items/price/total.phtml`** -> AI Confidence: **99.29%**
862. **`app/code/Magento/Weee/view/adminhtml/templates/items/price/unit.phtml`** -> AI Confidence: **99.29%**
863. **`app/code/Magento/Weee/view/adminhtml/templates/order/create/items/price/row.phtml`** -> AI Confidence: **99.29%**
864. **`app/code/Magento/Weee/view/adminhtml/templates/order/create/items/price/total.phtml`** -> AI Confidence: **99.29%**
865. **`app/code/Magento/Weee/view/adminhtml/templates/order/create/items/price/unit.phtml`** -> AI Confidence: **99.29%**
866. **`app/code/Magento/Weee/view/adminhtml/templates/renderer/tax.phtml`** -> AI Confidence: **99.29%**
867. **`app/code/Magento/Weee/view/base/templates/pricing/adjustment.phtml`** -> AI Confidence: **99.29%**
868. **`app/code/Magento/Weee/view/frontend/templates/email/items/price/row.phtml`** -> AI Confidence: **99.29%**
869. **`app/code/Magento/Weee/view/frontend/templates/item/price/row.phtml`** -> AI Confidence: **99.29%**
870. **`app/code/Magento/Weee/view/frontend/templates/item/price/total_after_discount.phtml`** -> AI Confidence: **99.29%**
871. **`app/code/Magento/Weee/view/frontend/templates/item/price/unit.phtml`** -> AI Confidence: **99.29%**
872. **`app/code/Magento/Wishlist/view/adminhtml/templates/customer/edit/tab/wishlist.phtml`** -> AI Confidence: **99.29%**
873. **`app/code/Magento/Wishlist/view/base/templates/product/price/bundle/configured_price.phtml`** -> AI Confidence: **99.29%**
874. **`app/code/Magento/Wishlist/view/base/templates/product/price/configurable/configured_price.phtml`** -> AI Confidence: **99.29%**
875. **`app/code/Magento/Wishlist/view/frontend/templates/addto.phtml`** -> AI Confidence: **99.29%**
876. **`app/code/Magento/Wishlist/view/frontend/templates/button/share.phtml`** -> AI Confidence: **99.29%**
877. **`app/code/Magento/Wishlist/view/frontend/templates/button/tocart.phtml`** -> AI Confidence: **99.29%**
878. **`app/code/Magento/Wishlist/view/frontend/templates/button/update.phtml`** -> AI Confidence: **99.29%**
879. **`app/code/Magento/Wishlist/view/frontend/templates/cart/item/renderer/actions/move_to_wishlist.phtml`** -> AI Confidence: **99.29%**
880. **`app/code/Magento/Wishlist/view/frontend/templates/catalog/product/list/addto/wishlist.phtml`** -> AI Confidence: **99.29%**
881. **`app/code/Magento/Wishlist/view/frontend/templates/catalog/product/view/addto/wishlist.phtml`** -> AI Confidence: **99.29%**
882. **`app/code/Magento/Wishlist/view/frontend/templates/email/items.phtml`** -> AI Confidence: **99.29%**
883. **`app/code/Magento/Wishlist/view/frontend/templates/item/column/actions.phtml`** -> AI Confidence: **99.29%**
884. **`app/code/Magento/Wishlist/view/frontend/templates/item/column/cart.phtml`** -> AI Confidence: **99.29%**
885. **`app/code/Magento/Wishlist/view/frontend/templates/item/column/edit.phtml`** -> AI Confidence: **99.29%**
886. **`app/code/Magento/Wishlist/view/frontend/templates/item/column/image.phtml`** -> AI Confidence: **99.29%**
887. **`app/code/Magento/Wishlist/view/frontend/templates/item/column/name.phtml`** -> AI Confidence: **99.29%**
888. **`app/code/Magento/Wishlist/view/frontend/templates/item/column/price.phtml`** -> AI Confidence: **99.29%**
889. **`app/code/Magento/Wishlist/view/frontend/templates/item/column/remove.phtml`** -> AI Confidence: **99.29%**
890. **`app/code/Magento/Wishlist/view/frontend/templates/item/column/review.phtml`** -> AI Confidence: **99.29%**
891. **`app/code/Magento/Wishlist/view/frontend/templates/item/configure/addto.phtml`** -> AI Confidence: **99.29%**
892. **`app/code/Magento/Wishlist/view/frontend/templates/item/configure/addto/wishlist.phtml`** -> AI Confidence: **99.29%**
893. **`app/code/Magento/Wishlist/view/frontend/templates/item/list.phtml`** -> AI Confidence: **99.29%**
894. **`app/code/Magento/Wishlist/view/frontend/templates/js/components.phtml`** -> AI Confidence: **99.29%**
895. **`app/code/Magento/Wishlist/view/frontend/templates/messages/addProductSuccessMessage.phtml`** -> AI Confidence: **99.29%**
896. **`app/code/Magento/Wishlist/view/frontend/templates/messages/removeWishlistItemSuccessMessage.phtml`** -> AI Confidence: **99.29%**
897. **`app/code/Magento/Wishlist/view/frontend/templates/options_list.phtml`** -> AI Confidence: **99.29%**
898. **`app/code/Magento/Wishlist/view/frontend/templates/rss/email.phtml`** -> AI Confidence: **99.29%**
899. **`app/code/Magento/Wishlist/view/frontend/templates/rss/wishlist.phtml`** -> AI Confidence: **99.29%**
900. **`app/code/Magento/Wishlist/view/frontend/templates/shared.phtml`** -> AI Confidence: **99.29%**
901. **`app/code/Magento/Wishlist/view/frontend/templates/view.phtml`** -> AI Confidence: **99.29%**
902. **`app/code/Magento/WishlistAnalytics/registration.php`** -> AI Confidence: **99.29%**
903. **`app/design/frontend/Magento/luma/Magento_LayeredNavigation/templates/layer/state.phtml`** -> AI Confidence: **99.29%**
904. **`app/design/frontend/Magento/luma/Magento_LayeredNavigation/templates/layer/view.phtml`** -> AI Confidence: **99.29%**
905. **`dev/tests/integration/_files/Magento/TestModuleCspUtil/view/frontend/templates/helper.phtml`** -> AI Confidence: **99.29%**
906. **`dev/tests/integration/_files/Magento/TestModuleCspUtil/view/frontend/templates/secure.phtml`** -> AI Confidence: **99.29%**
907. **`dev/tests/integration/_files/Magento/TestModuleSecureHtmlRenderer/view/frontend/templates/helper.phtml`** -> AI Confidence: **99.29%**
908. **`dev/tests/integration/testsuite/Magento/Catalog/Model/Category/_files/service_category_create.php`** -> AI Confidence: **99.29%**
909. **`dev/tests/integration/testsuite/Magento/Catalog/Model/Layer/Filter/Price/_files/_algorithm_base_data.php`** -> AI Confidence: **99.29%**
910. **`dev/tests/integration/testsuite/Magento/Catalog/Model/Product/Attribute/_files/create_attribute_service.php`** -> AI Confidence: **99.29%**
911. **`dev/tests/integration/testsuite/Magento/Catalog/Model/Product/_files/service_product_create.php`** -> AI Confidence: **99.29%**
912. **`dev/tests/integration/testsuite/Magento/Catalog/_files/dropdown_attribute_rollback.php`** -> AI Confidence: **99.29%**
913. **`dev/tests/integration/testsuite/Magento/Catalog/_files/multiselect_attribute_rollback.php`** -> AI Confidence: **99.29%**
914. **`dev/tests/integration/testsuite/Magento/Catalog/_files/multiselect_attribute_with_source_model_rollback.php`** -> AI Confidence: **99.29%**
915. **`dev/tests/integration/testsuite/Magento/Config/_files/config.php`** -> AI Confidence: **99.29%**
916. **`dev/tests/integration/testsuite/Magento/Config/_files/env.php`** -> AI Confidence: **99.29%**
917. **`dev/tests/integration/testsuite/Magento/Deploy/_files/_config.local.php`** -> AI Confidence: **99.29%**
918. **`dev/tests/integration/testsuite/Magento/Deploy/_files/config.php`** -> AI Confidence: **99.29%**
919. **`dev/tests/integration/testsuite/Magento/Deploy/_files/map.php`** -> AI Confidence: **99.29%**
920. **`dev/tests/integration/testsuite/Magento/Deploy/_files/scopes/config_with_changed_stores.php`** -> AI Confidence: **99.29%**
921. **`dev/tests/integration/testsuite/Magento/Email/Model/_files/design/adminhtml/Magento/default/Magento_Email/templates/sample_email_content.phtml`** -> AI Confidence: **99.29%**
922. **`dev/tests/integration/testsuite/Magento/Email/Model/_files/design/frontend/Magento/default/Magento_Email/templates/sample_email_content.phtml`** -> AI Confidence: **99.29%**
923. **`dev/tests/integration/testsuite/Magento/Email/Model/_files/design/frontend/Magento/default/Magento_Email/templates/sample_email_content_custom.phtml`** -> AI Confidence: **99.29%**
924. **`dev/tests/integration/testsuite/Magento/Framework/Code/_files/ClassToFind.php`** -> AI Confidence: **99.29%**
925. **`dev/tests/integration/testsuite/Magento/Framework/Filesystem/_files/ClassToFind.php`** -> AI Confidence: **99.29%**
926. **`dev/tests/integration/testsuite/Magento/Framework/Translate/_files/_translation_data.php`** -> AI Confidence: **99.29%**
927. **`dev/tests/integration/testsuite/Magento/Framework/View/_files/test_template.phtml`** -> AI Confidence: **99.29%**
928. **`dev/tests/integration/testsuite/Magento/MediaContentCms/_files/page_with_asset.php`** -> AI Confidence: **99.29%**
929. **`dev/tests/integration/testsuite/Magento/Setup/Console/Command/_files/config/dump_config.php`** -> AI Confidence: **99.29%**
930. **`dev/tests/integration/testsuite/Magento/Setup/Module/I18n/Dictionary/_files/source/app/code/Magento/FirstModule/view/frontend/template.phtml`** -> AI Confidence: **99.29%**
931. **`dev/tests/integration/testsuite/Magento/Setup/Module/I18n/Dictionary/_files/source/app/design/adminhtml/default/backend/template.phtml`** -> AI Confidence: **99.29%**
932. **`dev/tests/integration/testsuite/Magento/Setup/Module/I18n/Dictionary/_files/source/not_magento_dir/template.phtml`** -> AI Confidence: **99.29%**
933. **`dev/tests/integration/testsuite/Magento/Store/_files/dump_config.php`** -> AI Confidence: **99.29%**
934. **`dev/tests/integration/testsuite/Magento/Theme/Model/_files/design/frontend/access_violation.php`** -> AI Confidence: **99.29%**
935. **`dev/tests/setup-integration/_files/Magento/TestSetupDeclarationModule1/fixture/foreign_key_interpreter_result.php`** -> AI Confidence: **99.29%**
936. **`dev/tests/setup-integration/_files/Magento/TestSetupDeclarationModule1/fixture/valid_xml_revision_1.php`** -> AI Confidence: **99.29%**
937. **`dev/tests/static/framework/tests/unit/testsuite/Magento/TestFramework/Inspection/_files/words_finder/buffy.php`** -> AI Confidence: **99.29%**
938. **`dev/tests/static/framework/tests/unit/testsuite/Magento/TestFramework/Inspection/_files/words_finder/interview_with_the_vampire.php`** -> AI Confidence: **99.29%**
939. **`dev/tests/static/framework/tests/unit/testsuite/Magento/TestFramework/Inspection/_files/words_finder/twilight/eclipse.php`** -> AI Confidence: **99.29%**
940. **`dev/tests/static/framework/tests/unit/testsuite/Magento/TestFramework/Inspection/_files/words_finder/twilight/newmoon.php`** -> AI Confidence: **99.29%**
941. **`pub/errors/default/404.phtml`** -> AI Confidence: **99.29%**
942. **`pub/errors/default/503.phtml`** -> AI Confidence: **99.29%**
943. **`pub/errors/default/nocache.phtml`** -> AI Confidence: **99.29%**
944. **`pub/errors/default/page.phtml`** -> AI Confidence: **99.29%**
945. **`app/code/Magento/Backend/view/adminhtml/web/js/save-with-confirm.js`** -> AI Confidence: **99.29%**
946. **`app/code/Magento/Bundle/view/frontend/web/js/slide.js`** -> AI Confidence: **99.29%**
947. **`app/code/Magento/Catalog/view/adminhtml/web/js/utils/percentage-price-calculator.js`** -> AI Confidence: **99.29%**
948. **`app/code/Magento/Catalog/view/base/web/js/price-option-file.js`** -> AI Confidence: **99.29%**
949. **`app/code/Magento/Csp/view/base/web/js/sri.js`** -> AI Confidence: **99.29%**
950. **`app/code/Magento/Customer/view/frontend/web/js/change-email-password.js`** -> AI Confidence: **99.29%**
951. **`app/code/Magento/Directory/view/frontend/web/js/region-updater.js`** -> AI Confidence: **99.29%**
952. **`app/code/Magento/Downloadable/view/adminhtml/web/downloadable-type-handler.js`** -> AI Confidence: **99.29%**
953. **`app/code/Magento/Downloadable/view/adminhtml/web/js/components/is-downloadable-handler.js`** -> AI Confidence: **99.29%**
954. **`app/code/Magento/Eav/view/adminhtml/web/js/input-types.js`** -> AI Confidence: **99.29%**
955. **`app/code/Magento/GoogleAnalytics/view/frontend/web/js/google-analytics.js`** -> AI Confidence: **99.29%**
956. **`app/code/Magento/Paypal/view/adminhtml/web/js/rules.js`** -> AI Confidence: **99.29%**
957. **`app/code/Magento/Paypal/view/frontend/web/js/model/iframe-redirect.js`** -> AI Confidence: **99.29%**
958. **`app/code/Magento/Search/view/frontend/web/js/form-mini.js`** -> AI Confidence: **99.29%**
959. **`app/code/Magento/Swatches/view/adminhtml/web/js/product-attributes.js`** -> AI Confidence: **99.29%**
960. **`app/code/Magento/Theme/view/frontend/requirejs-config.js`** -> AI Confidence: **99.29%**
961. **`app/code/Magento/Ui/view/base/web/js/form/element/date.js`** -> AI Confidence: **99.29%**
962. **`app/code/Magento/Ui/view/base/web/js/form/element/single-checkbox.js`** -> AI Confidence: **99.29%**
963. **`app/code/Magento/Wishlist/view/frontend/web/js/search.js`** -> AI Confidence: **99.29%**
964. **`setup/pub/scripts/main.js`** -> AI Confidence: **99.29%**
965. **`app/code/Magento/AsynchronousOperations/Model/MassConsumerEnvelopeCallback.php`** -> AI Confidence: **99.24%**
966. **`app/code/Magento/AsynchronousOperations/Model/OperationProcessor.php`** -> AI Confidence: **99.24%**
967. **`app/code/Magento/Authorization/Model/Acl/AclRetriever.php`** -> AI Confidence: **99.24%**
968. **`app/code/Magento/Backend/App/Area/FrontNameResolver.php`** -> AI Confidence: **99.24%**
969. **`app/code/Magento/Backend/Controller/Adminhtml/System/Store/Save.php`** -> AI Confidence: **99.24%**
970. **`app/code/Magento/Bundle/Model/LinkManagement.php`** -> AI Confidence: **99.24%**
971. **`app/code/Magento/Bundle/Model/Option/SaveAction.php`** -> AI Confidence: **99.24%**
972. **`app/code/Magento/Bundle/Model/ResourceModel/Selection.php`** -> AI Confidence: **99.24%**
973. **`app/code/Magento/Bundle/Model/Sales/Order/Pdf/Items/Invoice.php`** -> AI Confidence: **99.24%**
974. **`app/code/Magento/Bundle/Pricing/Adjustment/DefaultSelectionPriceListProvider.php`** -> AI Confidence: **99.24%**
975. **`app/code/Magento/Bundle/Ui/DataProvider/Product/Form/Modifier/Composite.php`** -> AI Confidence: **99.24%**
976. **`app/code/Magento/BundleGraphQl/Model/Resolver/Order/Item/BundleOptions.php`** -> AI Confidence: **99.24%**
977. **`app/code/Magento/Catalog/Helper/Data.php`** -> AI Confidence: **99.24%**
978. **`app/code/Magento/Catalog/Helper/Output.php`** -> AI Confidence: **99.24%**
979. **`app/code/Magento/Catalog/Model/Attribute/ScopeOverriddenValue.php`** -> AI Confidence: **99.24%**
980. **`app/code/Magento/Catalog/Model/CategoryRepository.php`** -> AI Confidence: **99.24%**
981. **`app/code/Magento/Catalog/Model/Indexer/Category/Product/Action/Rows.php`** -> AI Confidence: **99.24%**
982. **`app/code/Magento/Catalog/Model/Indexer/Product/Category/Action/Rows.php`** -> AI Confidence: **99.24%**
983. **`app/code/Magento/Catalog/Model/Indexer/Product/Price/Action/Rows.php`** -> AI Confidence: **99.24%**
984. **`app/code/Magento/Catalog/Model/Product/Price/BasePriceStorage.php`** -> AI Confidence: **99.24%**
985. **`app/code/Magento/Catalog/Model/Product/Price/SpecialPriceStorage.php`** -> AI Confidence: **99.24%**
986. **`app/code/Magento/Catalog/Model/ProductLink/Management.php`** -> AI Confidence: **99.24%**
987. **`app/code/Magento/Catalog/Model/ProductLink/ProductLinkQuery.php`** -> AI Confidence: **99.24%**
988. **`app/code/Magento/Catalog/Model/ProductRepository.php`** -> AI Confidence: **99.24%**
989. **`app/code/Magento/Catalog/Model/ResourceModel/Category/Collection.php`** -> AI Confidence: **99.24%**
990. **`app/code/Magento/Catalog/Model/ResourceModel/Product/Action.php`** -> AI Confidence: **99.24%**
991. **`app/code/Magento/Catalog/Model/ResourceModel/Product/Collection.php`** -> AI Confidence: **99.24%**
992. **`app/code/Magento/Catalog/Model/ResourceModel/Product/Link.php`** -> AI Confidence: **99.24%**
993. **`app/code/Magento/Catalog/Pricing/Price/TierPrice.php`** -> AI Confidence: **99.24%**
994. **`app/code/Magento/Catalog/Ui/DataProvider/Product/Form/Modifier/Eav.php`** -> AI Confidence: **99.24%**
995. **`app/code/Magento/Catalog/Ui/DataProvider/Product/Form/Modifier/General.php`** -> AI Confidence: **99.24%**
996. **`app/code/Magento/CatalogGraphQl/DataProvider/Product/LayeredNavigation/Builder/Aggregations/Category/IncludeDirectChildrenOnly.php`** -> AI Confidence: **99.24%**
997. **`app/code/Magento/CatalogGraphQl/Model/Resolver/Aggregations.php`** -> AI Confidence: **99.24%**
998. **`app/code/Magento/CatalogGraphQl/Model/Resolver/Product/Options.php`** -> AI Confidence: **99.24%**
999. **`app/code/Magento/CatalogGraphQl/Model/Resolver/Products.php`** -> AI Confidence: **99.24%**
1000. **`app/code/Magento/CatalogGraphQl/Plugin/ProductAttributeSortInput.php`** -> AI Confidence: **99.24%**
1001. **`app/code/Magento/CatalogImportExport/Model/Import/Product.php`** -> AI Confidence: **99.24%**
1002. **`app/code/Magento/CatalogImportExport/Model/Import/Product/Type/AbstractType.php`** -> AI Confidence: **99.24%**
1003. **`app/code/Magento/CatalogInventory/Block/Adminhtml/Form/Field/Stock.php`** -> AI Confidence: **99.24%**
1004. **`app/code/Magento/CatalogInventory/Model/ResourceModel/Stock.php`** -> AI Confidence: **99.24%**
1005. **`app/code/Magento/CatalogInventory/Model/Stock/StockItemRepository.php`** -> AI Confidence: **99.24%**
1006. **`app/code/Magento/CatalogInventory/Model/StockIndex.php`** -> AI Confidence: **99.24%**
1007. **`app/code/Magento/CatalogInventory/Model/StockManagement.php`** -> AI Confidence: **99.24%**
1008. **`app/code/Magento/CatalogRule/Model/Indexer/IndexBuilder.php`** -> AI Confidence: **99.24%**
1009. **`app/code/Magento/CatalogSearch/Controller/Result/Index.php`** -> AI Confidence: **99.24%**
1010. **`app/code/Magento/CatalogSearch/Model/ResourceModel/Fulltext/Collection.php`** -> AI Confidence: **99.24%**
1011. **`app/code/Magento/CatalogUrlRewrite/Model/ProductScopeRewriteGenerator.php`** -> AI Confidence: **99.24%**
1012. **`app/code/Magento/CatalogUrlRewrite/Observer/AfterImportDataObserver.php`** -> AI Confidence: **99.24%**
1013. **`app/code/Magento/CatalogUrlRewrite/Observer/CategoryUrlPathAutogeneratorObserver.php`** -> AI Confidence: **99.24%**
1014. **`app/code/Magento/CatalogUrlRewrite/Observer/ProductProcessUrlRewriteSavingObserver.php`** -> AI Confidence: **99.24%**
1015. **`app/code/Magento/Cms/Controller/Adminhtml/Page/PostDataProcessor.php`** -> AI Confidence: **99.24%**
1016. **`app/code/Magento/Cms/Controller/Adminhtml/Page/Save.php`** -> AI Confidence: **99.24%**
1017. **`app/code/Magento/Cms/Model/Page/DataProvider.php`** -> AI Confidence: **99.24%**
1018. **`app/code/Magento/Config/App/Config/Source/DumpConfigSourceAggregated.php`** -> AI Confidence: **99.24%**
1019. **`app/code/Magento/Config/App/Config/Source/RuntimeConfigSource.php`** -> AI Confidence: **99.24%**
1020. **`app/code/Magento/Config/Block/System/Config/Form.php`** -> AI Confidence: **99.24%**
1021. **`app/code/Magento/Config/Console/Command/ConfigShowCommand.php`** -> AI Confidence: **99.24%**
1022. **`app/code/Magento/ConfigurableProductGraphQl/Model/Options/Metadata.php`** -> AI Confidence: **99.24%**
1023. **`app/code/Magento/Csp/Block/Sri/Hashes.php`** -> AI Confidence: **99.24%**
1024. **`app/code/Magento/Csp/Helper/InlineUtil.php`** -> AI Confidence: **99.24%**
1025. **`app/code/Magento/Csp/Plugin/AddDefaultPropertiesToGroupPlugin.php`** -> AI Confidence: **99.24%**
1026. **`app/code/Magento/Csp/Plugin/GenerateBundleAssetIntegrity.php`** -> AI Confidence: **99.24%**
1027. **`app/code/Magento/Customer/Block/Adminhtml/Group/Edit/Form.php`** -> AI Confidence: **99.24%**
1028. **`app/code/Magento/Customer/Controller/Account/CreatePost.php`** -> AI Confidence: **99.24%**
1029. **`app/code/Magento/Customer/Controller/Account/ResetPasswordPost.php`** -> AI Confidence: **99.24%**
1030. **`app/code/Magento/Customer/Controller/Adminhtml/Address/Save.php`** -> AI Confidence: **99.24%**
1031. **`app/code/Magento/Customer/Controller/Adminhtml/Index/Save.php`** -> AI Confidence: **99.24%**
1032. **`app/code/Magento/Customer/Controller/Adminhtml/Index/Viewfile.php`** -> AI Confidence: **99.24%**
1033. **`app/code/Magento/Customer/Model/Account/Redirect.php`** -> AI Confidence: **99.24%**
1034. **`app/code/Magento/Customer/Model/AccountManagement.php`** -> AI Confidence: **99.24%**
1035. **`app/code/Magento/Customer/Model/Address/DataProvider.php`** -> AI Confidence: **99.24%**
1036. **`app/code/Magento/Customer/Model/Address/Validator/General.php`** -> AI Confidence: **99.24%**
1037. **`app/code/Magento/Customer/Model/AttributeMetadataResolver.php`** -> AI Confidence: **99.24%**
1038. **`app/code/Magento/Customer/Model/Customer/DataProvider.php`** -> AI Confidence: **99.24%**
1039. **`app/code/Magento/Customer/Observer/AfterAddressSaveObserver.php`** -> AI Confidence: **99.24%**
1040. **`app/code/Magento/CustomerGraphQl/Model/Customer/Address/UpdateCustomerAddress.php`** -> AI Confidence: **99.24%**
1041. **`app/code/Magento/Deploy/Console/Command/App/ConfigImport/Processor.php`** -> AI Confidence: **99.24%**
1042. **`app/code/Magento/Deploy/Console/Command/SetModeCommand.php`** -> AI Confidence: **99.24%**
1043. **`app/code/Magento/Deploy/Console/InputValidator.php`** -> AI Confidence: **99.24%**
1044. **`app/code/Magento/Deploy/Package/PackagePool.php`** -> AI Confidence: **99.24%**
1045. **`app/code/Magento/Deploy/Package/Processor/PreProcessor/Css.php`** -> AI Confidence: **99.24%**
1046. **`app/code/Magento/Deploy/Strategy/StandardDeploy.php`** -> AI Confidence: **99.24%**
1047. **`app/code/Magento/Directory/Model/Currency/Import/CurrencyConverterApi.php`** -> AI Confidence: **99.24%**
1048. **`app/code/Magento/Downloadable/Model/LinkRepository.php`** -> AI Confidence: **99.24%**
1049. **`app/code/Magento/Downloadable/Model/SampleRepository.php`** -> AI Confidence: **99.24%**
1050. **`app/code/Magento/Eav/Model/Attribute/Data/AbstractData.php`** -> AI Confidence: **99.24%**
1051. **`app/code/Magento/Eav/Model/Entity/Attribute/OptionManagement.php`** -> AI Confidence: **99.24%**
1052. **`app/code/Magento/Eav/Model/ResourceModel/ReadHandler.php`** -> AI Confidence: **99.24%**
1053. **`app/code/Magento/Eav/Setup/EavSetup.php`** -> AI Confidence: **99.24%**
1054. **`app/code/Magento/EavGraphQl/Model/Resolver/CustomAttributeMetadata.php`** -> AI Confidence: **99.24%**
1055. **`app/code/Magento/Elasticsearch/Model/Adapter/Elasticsearch.php`** -> AI Confidence: **99.24%**
1056. **`app/code/Magento/GiftMessageGraphQl/Model/Resolver/Order/GiftMessage.php`** -> AI Confidence: **99.24%**
1057. **`app/code/Magento/GraphQl/Controller/GraphQl.php`** -> AI Confidence: **99.24%**
1058. **`app/code/Magento/GraphQl/Helper/Query/Logger/LogData.php`** -> AI Confidence: **99.24%**
1059. **`app/code/Magento/ImportExport/Model/Import/Entity/AbstractEntity.php`** -> AI Confidence: **99.24%**
1060. **`app/code/Magento/Integration/Model/OauthService.php`** -> AI Confidence: **99.24%**
1061. **`app/code/Magento/JwtFrameworkAdapter/Model/JweManager.php`** -> AI Confidence: **99.24%**
1062. **`app/code/Magento/JwtFrameworkAdapter/Model/JwtManager.php`** -> AI Confidence: **99.24%**
1063. **`app/code/Magento/LoginAsCustomerAssistance/Plugin/CustomerPlugin.php`** -> AI Confidence: **99.24%**
1064. **`app/code/Magento/MediaGalleryMetadata/Model/AddIptcMetadata.php`** -> AI Confidence: **99.24%**
1065. **`app/code/Magento/MediaGalleryUi/Model/Directories/GetDirectoryTree.php`** -> AI Confidence: **99.24%**
1066. **`app/code/Magento/Msrp/Helper/Data.php`** -> AI Confidence: **99.24%**
1067. **`app/code/Magento/Multishipping/Model/Cart/MultishippingClearItemAddress.php`** -> AI Confidence: **99.24%**
1068. **`app/code/Magento/Newsletter/Block/Adminhtml/Template/Preview.php`** -> AI Confidence: **99.24%**
1069. **`app/code/Magento/OfflineShipping/Model/ResourceModel/Carrier/Tablerate.php`** -> AI Confidence: **99.24%**
1070. **`app/code/Magento/OrderCancellationGraphQl/Model/Validator/ValidateGuestRequest.php`** -> AI Confidence: **99.24%**
1071. **`app/code/Magento/Payment/Gateway/Http/Client/Zend.php`** -> AI Confidence: **99.24%**
1072. **`app/code/Magento/Paypal/Model/Config/StructurePlugin.php`** -> AI Confidence: **99.24%**
1073. **`app/code/Magento/Paypal/Model/Report/Settlement/Row.php`** -> AI Confidence: **99.24%**
1074. **`app/code/Magento/PaypalGraphQl/Model/Resolver/PaypalExpressToken.php`** -> AI Confidence: **99.24%**
1075. **`app/code/Magento/Persistent/Model/QuoteManager.php`** -> AI Confidence: **99.24%**
1076. **`app/code/Magento/Persistent/Observer/SetCheckoutSessionPersistentDataObserver.php`** -> AI Confidence: **99.24%**
1077. **`app/code/Magento/ProductAlert/Model/Mailing/AlertProcessor.php`** -> AI Confidence: **99.24%**
1078. **`app/code/Magento/Quote/Model/Cart/AddProductsToCart.php`** -> AI Confidence: **99.24%**
1079. **`app/code/Magento/Quote/Model/Quote.php`** -> AI Confidence: **99.24%**
1080. **`app/code/Magento/Quote/Model/QuoteRepository.php`** -> AI Confidence: **99.24%**
1081. **`app/code/Magento/Quote/Model/QuoteRepository/SaveHandler.php`** -> AI Confidence: **99.24%**
1082. **`app/code/Magento/Quote/Model/QuoteValidator.php`** -> AI Confidence: **99.24%**
1083. **`app/code/Magento/Quote/Observer/Frontend/Quote/Address/CollectTotalsObserver.php`** -> AI Confidence: **99.24%**
1084. **`app/code/Magento/Quote/Plugin/UpdateCartId.php`** -> AI Confidence: **99.24%**
1085. **`app/code/Magento/QuoteGraphQl/Model/Cart/MergeCarts/CartQuantityValidator.php`** -> AI Confidence: **99.24%**
1086. **`app/code/Magento/QuoteGraphQl/Model/Resolver/ShippingAddress/SelectedShippingMethod.php`** -> AI Confidence: **99.24%**
1087. **`app/code/Magento/RemoteStorage/Model/File/Uploader.php`** -> AI Confidence: **99.24%**
1088. **`app/code/Magento/RequireJs/Block/Html/Head/Config.php`** -> AI Confidence: **99.24%**
1089. **`app/code/Magento/Review/Block/Adminhtml/Edit.php`** -> AI Confidence: **99.24%**
1090. **`app/code/Magento/Review/Block/Adminhtml/Edit/Form.php`** -> AI Confidence: **99.24%**
1091. **`app/code/Magento/Sales/Controller/Adminhtml/Order/Create/LoadBlock.php`** -> AI Confidence: **99.24%**
1092. **`app/code/Magento/Sales/Model/Order/Creditmemo/Validation/QuantityValidator.php`** -> AI Confidence: **99.24%**
1093. **`app/code/Magento/Sales/Model/Order/Invoice/Comment/Validator.php`** -> AI Confidence: **99.24%**
1094. **`app/code/Magento/Sales/Model/OrderRepository.php`** -> AI Confidence: **99.24%**
1095. **`app/code/Magento/Sales/Ui/Component/Listing/Column/Price.php`** -> AI Confidence: **99.24%**
1096. **`app/code/Magento/SalesRule/Model/ResourceModel/Report/Rule/Createdat.php`** -> AI Confidence: **99.24%**
1097. **`app/code/Magento/SalesRule/Model/ResourceModel/Rule.php`** -> AI Confidence: **99.24%**
1098. **`app/code/Magento/SalesRule/Model/RulesApplier.php`** -> AI Confidence: **99.24%**
1099. **`app/code/Magento/Shipping/Controller/Adminhtml/Order/Shipment/AddTrack.php`** -> AI Confidence: **99.24%**
1100. **`app/code/Magento/Shipping/Controller/Adminhtml/Order/ShipmentLoader.php`** -> AI Confidence: **99.24%**
1101. **`app/code/Magento/Sitemap/Model/Batch/Sitemap.php`** -> AI Confidence: **99.24%**
1102. **`app/code/Magento/Sitemap/Model/ResourceModel/Catalog/Batch/Product.php`** -> AI Confidence: **99.24%**
1103. **`app/code/Magento/Store/App/Action/Plugin/Context.php`** -> AI Confidence: **99.24%**
1104. **`app/code/Magento/Store/App/Response/Redirect.php`** -> AI Confidence: **99.24%**
1105. **`app/code/Magento/Store/Model/Config/Processor/Fallback.php`** -> AI Confidence: **99.24%**
1106. **`app/code/Magento/Tax/Block/Adminhtml/Rule/Edit/Form.php`** -> AI Confidence: **99.24%**
1107. **`app/code/Magento/Tax/Model/Calculation/RateRepository.php`** -> AI Confidence: **99.24%**
1108. **`app/code/Magento/Theme/Block/Html/Topmenu.php`** -> AI Confidence: **99.24%**
1109. **`app/code/Magento/Theme/Controller/Result/AsyncCssPlugin.php`** -> AI Confidence: **99.24%**
1110. **`app/code/Magento/Theme/Ui/Component/Design/Config/DataProvider.php`** -> AI Confidence: **99.24%**
1111. **`app/code/Magento/Ui/Controller/Adminhtml/Bookmark/Save.php`** -> AI Confidence: **99.24%**
1112. **`app/code/Magento/Ui/Model/Export/MetadataProvider.php`** -> AI Confidence: **99.24%**
1113. **`app/code/Magento/UrlRewrite/Model/UrlRewrite.php`** -> AI Confidence: **99.24%**
1114. **`app/code/Magento/User/Controller/Adminhtml/Auth/Forgotpassword.php`** -> AI Confidence: **99.24%**
1115. **`app/code/Magento/User/Controller/Adminhtml/Auth/ResetPasswordPost.php`** -> AI Confidence: **99.24%**
1116. **`app/code/Magento/User/Observer/Backend/AuthObserver.php`** -> AI Confidence: **99.24%**
1117. **`app/code/Magento/Webapi/Model/Authorization/TokenUserContext.php`** -> AI Confidence: **99.24%**
1118. **`app/code/Magento/Weee/Block/Item/Price/Renderer.php`** -> AI Confidence: **99.24%**
1119. **`app/code/Magento/Weee/Helper/Data.php`** -> AI Confidence: **99.24%**
1120. **`app/code/Magento/Weee/Model/App/Action/ContextPlugin.php`** -> AI Confidence: **99.24%**
1121. **`app/code/Magento/Weee/Model/Total/Quote/WeeeTax.php`** -> AI Confidence: **99.24%**
1122. **`app/code/Magento/Wishlist/Controller/Index/Add.php`** -> AI Confidence: **99.24%**
1123. **`app/code/Magento/Wishlist/Controller/Index/Cart.php`** -> AI Confidence: **99.24%**
1124. **`app/code/Magento/Wishlist/Controller/Index/Send.php`** -> AI Confidence: **99.24%**
1125. **`app/code/Magento/Wishlist/Helper/Data.php`** -> AI Confidence: **99.24%**
1126. **`dev/tests/api-functional/framework/Magento/TestFramework/Authentication/OauthHelper.php`** -> AI Confidence: **99.24%**
1127. **`dev/tests/integration/testsuite/Magento/Bundle/_files/dynamic_bundle_product_with_multiple_options.php`** -> AI Confidence: **99.24%**
1128. **`dev/tests/integration/testsuite/Magento/Bundle/_files/product_with_multiple_options_radio_select.php`** -> AI Confidence: **99.24%**
1129. **`dev/tests/integration/testsuite/Magento/Catalog/_files/products_with_layered_navigation_attributes_rollback.php`** -> AI Confidence: **99.24%**
1130. **`dev/tests/integration/testsuite/Magento/CatalogImportExport/Model/AbstractProductExportImportTestCase.php`** -> AI Confidence: **99.24%**
1131. **`dev/tests/integration/testsuite/Magento/Widget/Model/Config/_files/expectedMergedArray.php`** -> AI Confidence: **99.24%**
1132. **`setup/src/Magento/Setup/Console/Style/MagentoStyle.php`** -> AI Confidence: **99.24%**
1133. **`setup/src/Magento/Setup/Model/ConfigOptionsList/Lock.php`** -> AI Confidence: **99.24%**
1134. **`setup/src/Magento/Setup/Model/ConfigOptionsList/PageCache.php`** -> AI Confidence: **99.24%**
1135. **`setup/src/Magento/Setup/Model/PhpReadinessCheck.php`** -> AI Confidence: **99.24%**
1136. **`setup/src/Magento/Setup/Module/Di/Code/Reader/ClassesScanner.php`** -> AI Confidence: **99.24%**
1137. **`setup/src/Magento/Setup/Module/Di/Compiler/Config/Reader.php`** -> AI Confidence: **99.24%**
1138. **`app/code/Magento/Backend/Block/Dashboard/Totals.php`** -> AI Confidence: **99.23%**
1139. **`app/code/Magento/Backend/Controller/Adminhtml/System/Account/Save.php`** -> AI Confidence: **99.23%**
1140. **`app/code/Magento/Catalog/Controller/Adminhtml/Product/MassStatus.php`** -> AI Confidence: **99.23%**
1141. **`app/code/Magento/Catalog/Model/Product/Option/Type/File/ValidatorInfo.php`** -> AI Confidence: **99.23%**
1142. **`app/code/Magento/Catalog/Model/ProductLink/CollectionProvider/LinkedMapProvider.php`** -> AI Confidence: **99.23%**
1143. **`app/code/Magento/Catalog/Model/ResourceModel/Category.php`** -> AI Confidence: **99.23%**
1144. **`app/code/Magento/Catalog/Model/ResourceModel/Product/Indexer/Price/TierPrice.php`** -> AI Confidence: **99.23%**
1145. **`app/code/Magento/Catalog/Ui/Component/ColumnFactory.php`** -> AI Confidence: **99.23%**
1146. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/attribute/set/main.phtml`** -> AI Confidence: **99.23%**
1147. **`app/code/Magento/CatalogGraphQl/DataProvider/Product/LayeredNavigation/Builder/Attribute.php`** -> AI Confidence: **99.23%**
1148. **`app/code/Magento/CatalogImportExport/Model/Import/Product/LinkProcessor.php`** -> AI Confidence: **99.23%**
1149. **`app/code/Magento/CatalogImportExport/Model/Import/Uploader.php`** -> AI Confidence: **99.23%**
1150. **`app/code/Magento/CatalogInventory/Model/Indexer/ProductPriceIndexFilter.php`** -> AI Confidence: **99.23%**
1151. **`app/code/Magento/CatalogRule/Model/Indexer/ReindexRuleProduct.php`** -> AI Confidence: **99.23%**
1152. **`app/code/Magento/CatalogRule/Model/Indexer/ReindexRuleProductsPriceProcessor.php`** -> AI Confidence: **99.23%**
1153. **`app/code/Magento/CatalogUrlRewrite/Model/Product/Validator.php`** -> AI Confidence: **99.23%**
1154. **`app/code/Magento/Cms/Ui/Component/Listing/Column/PageActions.php`** -> AI Confidence: **99.23%**
1155. **`app/code/Magento/ConfigurableProduct/Controller/Adminhtml/Product/Initialization/Helper/Plugin/Configurable.php`** -> AI Confidence: **99.23%**
1156. **`app/code/Magento/Csp/Model/SubresourceIntegrity/HashResolver/HashResolver.php`** -> AI Confidence: **99.23%**
1157. **`app/code/Magento/Customer/Model/Metadata/Form/AbstractData.php`** -> AI Confidence: **99.23%**
1158. **`app/code/Magento/Customer/Model/ResourceModel/Address/Relation.php`** -> AI Confidence: **99.23%**
1159. **`app/code/Magento/Customer/view/frontend/templates/form/login.phtml`** -> AI Confidence: **99.23%**
1160. **`app/code/Magento/CustomerGraphQl/Model/Customer/Address/ValidateAddress.php`** -> AI Confidence: **99.23%**
1161. **`app/code/Magento/Deploy/Package/Processor/PostProcessor/CssUrls.php`** -> AI Confidence: **99.23%**
1162. **`app/code/Magento/Downloadable/Helper/Download.php`** -> AI Confidence: **99.23%**
1163. **`app/code/Magento/Downloadable/Model/Link/ContentValidator.php`** -> AI Confidence: **99.23%**
1164. **`app/code/Magento/Eav/Model/AttributeManagement.php`** -> AI Confidence: **99.23%**
1165. **`app/code/Magento/Eav/Model/Entity/Attribute/Frontend/AbstractFrontend.php`** -> AI Confidence: **99.23%**
1166. **`app/code/Magento/Elasticsearch/Model/Adapter/BatchDataMapper/ProductDataMapper.php`** -> AI Confidence: **99.23%**
1167. **`app/code/Magento/Elasticsearch8/Model/Client/Elasticsearch.php`** -> AI Confidence: **99.23%**
1168. **`app/code/Magento/GiftMessage/view/adminhtml/templates/popup.phtml`** -> AI Confidence: **99.23%**
1169. **`app/code/Magento/GiftMessageGraphQl/Model/Resolver/Cart/Item/GiftMessage.php`** -> AI Confidence: **99.23%**
1170. **`app/code/Magento/GiftMessageGraphQl/Model/Resolver/Order/Item/GiftMessage.php`** -> AI Confidence: **99.23%**
1171. **`app/code/Magento/GroupedProduct/Model/Product/Type/Grouped.php`** -> AI Confidence: **99.23%**
1172. **`app/code/Magento/Indexer/Console/Command/IndexerStatusCommand.php`** -> AI Confidence: **99.23%**
1173. **`app/code/Magento/Indexer/Model/Processor.php`** -> AI Confidence: **99.23%**
1174. **`app/code/Magento/Integration/Controller/Adminhtml/Integration/Save.php`** -> AI Confidence: **99.23%**
1175. **`app/code/Magento/MediaGallery/Model/Directory/IsExcluded.php`** -> AI Confidence: **99.23%**
1176. **`app/code/Magento/MessageQueue/Console/StartConsumerCommand.php`** -> AI Confidence: **99.23%**
1177. **`app/code/Magento/Newsletter/view/adminhtml/templates/preview/iframeswitcher.phtml`** -> AI Confidence: **99.23%**
1178. **`app/code/Magento/Paypal/Model/Payflow/Service/Gateway.php`** -> AI Confidence: **99.23%**
1179. **`app/code/Magento/Quote/Model/Cart/CustomerCartResolver.php`** -> AI Confidence: **99.23%**
1180. **`app/code/Magento/Quote/Setup/QuoteSetup.php`** -> AI Confidence: **99.23%**
1181. **`app/code/Magento/Sales/Block/Adminhtml/Order/Status/NewStatus/Form.php`** -> AI Confidence: **99.23%**
1182. **`app/code/Magento/Sales/Model/EmailSenderHandler.php`** -> AI Confidence: **99.23%**
1183. **`app/code/Magento/Sales/Model/Order/Creditmemo/Comment/Validator.php`** -> AI Confidence: **99.23%**
1184. **`app/code/Magento/Sales/Model/Order/Creditmemo/Total/Shipping.php`** -> AI Confidence: **99.23%**
1185. **`app/code/Magento/Sales/Model/Order/Shipment/Comment/Validator.php`** -> AI Confidence: **99.23%**
1186. **`app/code/Magento/Sales/Model/Order/Shipment/Track/Validator.php`** -> AI Confidence: **99.23%**
1187. **`app/code/Magento/SalesGraphQl/Model/Resolver/CreditMemo/CreditMemoTotal.php`** -> AI Confidence: **99.23%**
1188. **`app/code/Magento/SalesGraphQl/Model/Resolver/Invoice/InvoiceTotal.php`** -> AI Confidence: **99.23%**
1189. **`app/code/Magento/SalesGraphQl/Model/Resolver/OrderTotal.php`** -> AI Confidence: **99.23%**
1190. **`app/code/Magento/SalesRule/Helper/CartFixedDiscount.php`** -> AI Confidence: **99.23%**
1191. **`app/code/Magento/SalesRule/Model/Converter/ToModel.php`** -> AI Confidence: **99.23%**
1192. **`app/code/Magento/SalesRule/Model/Queue/Consumer/RuleQuoteRecollectTotals.php`** -> AI Confidence: **99.23%**
1193. **`app/code/Magento/Shipping/Model/Shipping/Labels.php`** -> AI Confidence: **99.23%**
1194. **`app/code/Magento/Store/Model/Config/Importer/Processor/Create.php`** -> AI Confidence: **99.23%**
1195. **`app/code/Magento/Swatches/Model/Plugin/ProductImage.php`** -> AI Confidence: **99.23%**
1196. **`app/code/Magento/Ui/Component/Listing/Columns/Date.php`** -> AI Confidence: **99.23%**
1197. **`app/code/Magento/Ui/Component/MassAction/Filter.php`** -> AI Confidence: **99.23%**
1198. **`app/code/Magento/Widget/Model/Widget.php`** -> AI Confidence: **99.23%**
1199. **`dev/tests/integration/testsuite/Magento/Elasticsearch/_files/case_sensitive.php`** -> AI Confidence: **99.23%**
1200. **`dev/tests/static/get_github_changes.php`** -> AI Confidence: **99.23%**
1201. **`setup/src/Magento/Setup/Console/Command/ConfigSetCommand.php`** -> AI Confidence: **99.23%**
1202. **`setup/src/Magento/Setup/Model/ConfigOptionsList/Cache.php`** -> AI Confidence: **99.23%**
1203. **`setup/src/Magento/Setup/Module/I18n/Parser/Adapter/Php/Tokenizer/PhraseCollector.php`** -> AI Confidence: **99.23%**
1204. **`app/code/Magento/Review/view/frontend/templates/form.phtml`** -> AI Confidence: **99.22%**
1205. **`app/code/Magento/Backend/view/adminhtml/templates/dashboard/chart/period.phtml`** -> AI Confidence: **99.2%**
1206. **`app/code/Magento/CatalogRule/view/adminhtml/templates/promo/fieldset.phtml`** -> AI Confidence: **99.2%**
1207. **`app/code/Magento/Sales/view/adminhtml/templates/order/create/form/account.phtml`** -> AI Confidence: **99.2%**
1208. **`app/code/Magento/Sales/view/adminhtml/templates/order/view/history.phtml`** -> AI Confidence: **99.2%**
1209. **`app/code/Magento/Shipping/view/adminhtml/templates/view/form.phtml`** -> AI Confidence: **99.2%**
1210. **`dev/tools/grunt/tasks/static.js`** -> AI Confidence: **99.2%**
1211. **`app/code/Magento/AdminNotification/Block/Grid/Renderer/Actions.php`** -> AI Confidence: **99.18%**
1212. **`app/code/Magento/AdvancedPricingImportExport/Controller/Adminhtml/Export/GetFilter.php`** -> AI Confidence: **99.18%**
1213. **`app/code/Magento/AdvancedSearch/Controller/Adminhtml/Search/System/Config/TestConnection.php`** -> AI Confidence: **99.18%**
1214. **`app/code/Magento/Analytics/Controller/Adminhtml/Reports/Show.php`** -> AI Confidence: **99.18%**
1215. **`app/code/Magento/AsyncConfig/Setup/ConfigOptionsList.php`** -> AI Confidence: **99.18%**
1216. **`app/code/Magento/AsynchronousOperations/Model/BulkStatus.php`** -> AI Confidence: **99.18%**
1217. **`app/code/Magento/AsynchronousOperations/Model/MessageControllerDecorator.php`** -> AI Confidence: **99.18%**
1218. **`app/code/Magento/Backend/Block/Widget/Grid/Massaction/AbstractMassaction.php`** -> AI Confidence: **99.18%**
1219. **`app/code/Magento/Backend/Console/Command/MaintenanceAllowIpsCommand.php`** -> AI Confidence: **99.18%**
1220. **`app/code/Magento/Backend/Controller/Adminhtml/Dashboard/Tunnel.php`** -> AI Confidence: **99.18%**
1221. **`app/code/Magento/Bundle/Model/Option/Validator.php`** -> AI Confidence: **99.18%**
1222. **`app/code/Magento/Bundle/Plugin/Catalog/Model/Product/Type/AbstractType.php`** -> AI Confidence: **99.18%**
1223. **`app/code/Magento/Bundle/Pricing/Price/FinalPrice.php`** -> AI Confidence: **99.18%**
1224. **`app/code/Magento/Bundle/Setup/Patch/Data/ApplyAttributesUpdate.php`** -> AI Confidence: **99.18%**
1225. **`app/code/Magento/BundleGraphQl/Model/Resolver/BundleItemLinks.php`** -> AI Confidence: **99.18%**
1226. **`app/code/Magento/BundleGraphQl/Model/Resolver/BundleItems.php`** -> AI Confidence: **99.18%**
1227. **`app/code/Magento/BundleGraphQl/Model/Resolver/Options/Label.php`** -> AI Confidence: **99.18%**
1228. **`app/code/Magento/Captcha/Controller/Refresh/Index.php`** -> AI Confidence: **99.18%**
1229. **`app/code/Magento/Captcha/CustomerData/Captcha.php`** -> AI Confidence: **99.18%**
1230. **`app/code/Magento/Captcha/Observer/CheckUserForgotPasswordBackendObserver.php`** -> AI Confidence: **99.18%**
1231. **`app/code/Magento/Catalog/Block/Adminhtml/Category/Tree.php`** -> AI Confidence: **99.18%**
1232. **`app/code/Magento/Catalog/Block/Adminhtml/Product/Edit/NewCategory.php`** -> AI Confidence: **99.18%**
1233. **`app/code/Magento/Catalog/Block/Adminhtml/Product/Helper/Form/Category.php`** -> AI Confidence: **99.18%**
1234. **`app/code/Magento/Catalog/Block/Category/Plugin/PriceBoxTags.php`** -> AI Confidence: **99.18%**
1235. **`app/code/Magento/Catalog/Block/Product/ProductList/Related.php`** -> AI Confidence: **99.18%**
1236. **`app/code/Magento/Catalog/Controller/Adminhtml/Category/Add.php`** -> AI Confidence: **99.18%**
1237. **`app/code/Magento/Catalog/Controller/Adminhtml/Product/Initialization/Helper.php`** -> AI Confidence: **99.18%**
1238. **`app/code/Magento/Catalog/Controller/Adminhtml/Product/Set/Edit.php`** -> AI Confidence: **99.18%**
1239. **`app/code/Magento/Catalog/Helper/Product/Composite.php`** -> AI Confidence: **99.18%**
1240. **`app/code/Magento/Catalog/Model/Category/Attribute/LayoutUpdateManager.php`** -> AI Confidence: **99.18%**
1241. **`app/code/Magento/Catalog/Model/Category/Tree.php`** -> AI Confidence: **99.18%**
1242. **`app/code/Magento/Catalog/Model/CategoryList.php`** -> AI Confidence: **99.18%**
1243. **`app/code/Magento/Catalog/Model/Indexer/Product/Eav/Plugin/AttributeSet.php`** -> AI Confidence: **99.18%**
1244. **`app/code/Magento/Catalog/Model/Indexer/Product/Price/Plugin/CustomerGroup.php`** -> AI Confidence: **99.18%**
1245. **`app/code/Magento/Catalog/Model/Indexer/Product/Price/Plugin/TableResolver.php`** -> AI Confidence: **99.18%**
1246. **`app/code/Magento/Catalog/Model/Indexer/Product/Price/Plugin/Website.php`** -> AI Confidence: **99.18%**
1247. **`app/code/Magento/Catalog/Model/Layer/Filter/Dynamic/Auto.php`** -> AI Confidence: **99.18%**
1248. **`app/code/Magento/Catalog/Model/Layer/Filter/Dynamic/Manual.php`** -> AI Confidence: **99.18%**
1249. **`app/code/Magento/Catalog/Model/Product.php`** -> AI Confidence: **99.18%**
1250. **`app/code/Magento/Catalog/Model/Product/Attribute/LayoutUpdateManager.php`** -> AI Confidence: **99.18%**
1251. **`app/code/Magento/Catalog/Model/Product/Gallery/DeleteHandler.php`** -> AI Confidence: **99.18%**
1252. **`app/code/Magento/Catalog/Model/Product/Image/RemoveDeletedImagesFromCache.php`** -> AI Confidence: **99.18%**
1253. **`app/code/Magento/Catalog/Model/Product/Option/Type/DefaultType.php`** -> AI Confidence: **99.18%**
1254. **`app/code/Magento/Catalog/Model/Product/Option/Type/File/RequestAwareValidatorFile.php`** -> AI Confidence: **99.18%**
1255. **`app/code/Magento/Catalog/Model/Product/Price/TierPriceStorage.php`** -> AI Confidence: **99.18%**
1256. **`app/code/Magento/Catalog/Model/Product/ProductFrontendAction/Synchronizer.php`** -> AI Confidence: **99.18%**
1257. **`app/code/Magento/Catalog/Model/ResourceModel/AttributePersistor.php`** -> AI Confidence: **99.18%**
1258. **`app/code/Magento/Catalog/Model/ResourceModel/Product/Link/DeleteHandler.php`** -> AI Confidence: **99.18%**
1259. **`app/code/Magento/Catalog/Model/ResourceModel/Product/Link/SaveHandler.php`** -> AI Confidence: **99.18%**
1260. **`app/code/Magento/Catalog/Model/View/Asset/Image.php`** -> AI Confidence: **99.18%**
1261. **`app/code/Magento/Catalog/Model/View/Asset/Placeholder.php`** -> AI Confidence: **99.18%**
1262. **`app/code/Magento/Catalog/Pricing/Price/SpecialPrice.php`** -> AI Confidence: **99.18%**
1263. **`app/code/Magento/Catalog/Setup/Patch/Data/UpgradeWebsiteAttributes.php`** -> AI Confidence: **99.18%**
1264. **`app/code/Magento/Catalog/Ui/DataProvider/Product/Form/Modifier/AdvancedPricing.php`** -> AI Confidence: **99.18%**
1265. **`app/code/Magento/Catalog/Ui/DataProvider/Product/Form/Modifier/Categories.php`** -> AI Confidence: **99.18%**
1266. **`app/code/Magento/Catalog/Ui/DataProvider/Product/Form/Modifier/TierPrice.php`** -> AI Confidence: **99.18%**
1267. **`app/code/Magento/Catalog/Ui/DataProvider/Product/Related/AbstractDataProvider.php`** -> AI Confidence: **99.18%**
1268. **`app/code/Magento/CatalogCmsGraphQl/Model/Resolver/Category/Block.php`** -> AI Confidence: **99.18%**
1269. **`app/code/Magento/CatalogCustomerGraphQl/Model/Resolver/Product/Price/Tiers.php`** -> AI Confidence: **99.18%**
1270. **`app/code/Magento/CatalogCustomerGraphQl/Model/Resolver/TierPrices.php`** -> AI Confidence: **99.18%**
1271. **`app/code/Magento/CatalogGraphQl/Model/Category/CategoryFilter.php`** -> AI Confidence: **99.18%**
1272. **`app/code/Magento/CatalogGraphQl/Model/Config/AttributeReader.php`** -> AI Confidence: **99.18%**
1273. **`app/code/Magento/CatalogGraphQl/Model/Config/FilterAttributeReader.php`** -> AI Confidence: **99.18%**
1274. **`app/code/Magento/CatalogGraphQl/Model/Config/SortAttributeReader.php`** -> AI Confidence: **99.18%**
1275. **`app/code/Magento/CatalogGraphQl/Model/Resolver/Category/CanonicalUrl.php`** -> AI Confidence: **99.18%**
1276. **`app/code/Magento/CatalogGraphQl/Model/Resolver/Category/Image.php`** -> AI Confidence: **99.18%**
1277. **`app/code/Magento/CatalogGraphQl/Model/Resolver/CategoryList.php`** -> AI Confidence: **99.18%**
1278. **`app/code/Magento/CatalogGraphQl/Model/Resolver/CategoryTree.php`** -> AI Confidence: **99.18%**
1279. **`app/code/Magento/CatalogGraphQl/Model/Resolver/Product/CanonicalUrl.php`** -> AI Confidence: **99.18%**
1280. **`app/code/Magento/CatalogGraphQl/Model/Resolver/Product/Price.php`** -> AI Confidence: **99.18%**
1281. **`app/code/Magento/CatalogGraphQl/Model/Resolver/Products/DataProvider/CategoryTree.php`** -> AI Confidence: **99.18%**
1282. **`app/code/Magento/CatalogGraphQl/Model/Resolver/Products/DataProvider/Product.php`** -> AI Confidence: **99.18%**
1283. **`app/code/Magento/CatalogGraphQl/Observer/AfterImportDataObserver.php`** -> AI Confidence: **99.18%**
1284. **`app/code/Magento/CatalogGraphQl/Plugin/Search/Request/ConfigReader.php`** -> AI Confidence: **99.18%**
1285. **`app/code/Magento/CatalogInventory/Helper/Stock.php`** -> AI Confidence: **99.18%**
1286. **`app/code/Magento/CatalogInventory/Model/ResourceModel/Indexer/Stock/DefaultStock.php`** -> AI Confidence: **99.18%**
1287. **`app/code/Magento/CatalogInventory/Model/Stock/StockRepository.php`** -> AI Confidence: **99.18%**
1288. **`app/code/Magento/CatalogInventory/Model/Stock/StockStatusRepository.php`** -> AI Confidence: **99.18%**
1289. **`app/code/Magento/CatalogRule/Model/Rule/Condition/ConditionsToSearchCriteriaMapper.php`** -> AI Confidence: **99.18%**
1290. **`app/code/Magento/CatalogSearch/Model/Adapter/Aggregation/AggregationResolver.php`** -> AI Confidence: **99.18%**
1291. **`app/code/Magento/CatalogUrlRewrite/Model/Category/Plugin/Category/UpdateUrlPath.php`** -> AI Confidence: **99.18%**
1292. **`app/code/Magento/CatalogUrlRewrite/Model/Product/AnchorUrlRewriteGenerator.php`** -> AI Confidence: **99.18%**
1293. **`app/code/Magento/CatalogUrlRewrite/Model/ProductUrlRewriteGenerator.php`** -> AI Confidence: **99.18%**
1294. **`app/code/Magento/CatalogUrlRewrite/Model/ResourceModel/Product/GetUrlRewriteData.php`** -> AI Confidence: **99.18%**
1295. **`app/code/Magento/CatalogUrlRewrite/Model/TableCleaner.php`** -> AI Confidence: **99.18%**
1296. **`app/code/Magento/CatalogUrlRewrite/Observer/CategoryProcessUrlRewriteSavingObserver.php`** -> AI Confidence: **99.18%**
1297. **`app/code/Magento/CatalogUrlRewrite/Plugin/Catalog/Model/Product/UpdateProductWebsiteUrlRewrites.php`** -> AI Confidence: **99.18%**
1298. **`app/code/Magento/CatalogUrlRewrite/Ui/DataProvider/Product/Form/Modifier/ProductUrlRewrite.php`** -> AI Confidence: **99.18%**
1299. **`app/code/Magento/CheckoutAgreements/Block/Adminhtml/Agreement/Edit/Form.php`** -> AI Confidence: **99.18%**
1300. **`app/code/Magento/CheckoutAgreementsGraphQl/Model/Resolver/CheckoutAgreements.php`** -> AI Confidence: **99.18%**
1301. **`app/code/Magento/Cms/Block/BlockByIdentifier.php`** -> AI Confidence: **99.18%**
1302. **`app/code/Magento/Cms/Controller/Adminhtml/Wysiwyg/Images/OnInsert.php`** -> AI Confidence: **99.18%**
1303. **`app/code/Magento/Cms/Helper/Wysiwyg/Images.php`** -> AI Confidence: **99.18%**
1304. **`app/code/Magento/Cms/Model/ResourceModel/Page.php`** -> AI Confidence: **99.18%**
1305. **`app/code/Magento/CmsUrlRewrite/Model/Page/TargetUrlBuilder.php`** -> AI Confidence: **99.18%**
1306. **`app/code/Magento/CompareListGraphQl/Model/Resolver/CompareList.php`** -> AI Confidence: **99.18%**
1307. **`app/code/Magento/CompareListGraphQl/Model/Resolver/CustomerCompareList.php`** -> AI Confidence: **99.18%**
1308. **`app/code/Magento/CompareListGraphQl/Model/Service/Customer/SetCustomerToCompareList.php`** -> AI Confidence: **99.18%**
1309. **`app/code/Magento/Config/Console/Command/ConfigSet/DefaultProcessor.php`** -> AI Confidence: **99.18%**
1310. **`app/code/Magento/Config/Console/Command/ConfigSet/LockProcessor.php`** -> AI Confidence: **99.18%**
1311. **`app/code/Magento/Config/Console/Command/ConfigSetCommand.php`** -> AI Confidence: **99.18%**
1312. **`app/code/Magento/Config/Console/Command/ConfigShow/ValueProcessor.php`** -> AI Confidence: **99.18%**
1313. **`app/code/Magento/Config/Model/Config/Compiler/IncludeElement.php`** -> AI Confidence: **99.18%**
1314. **`app/code/Magento/Config/Model/Config/Importer.php`** -> AI Confidence: **99.18%**
1315. **`app/code/Magento/Config/Model/Config/Parser/Comment.php`** -> AI Confidence: **99.18%**
1316. **`app/code/Magento/Config/Setup/ConfigOptionsList.php`** -> AI Confidence: **99.18%**
1317. **`app/code/Magento/ConfigurableImportExport/Model/Export/RowCustomizer.php`** -> AI Confidence: **99.18%**
1318. **`app/code/Magento/ConfigurableProduct/Block/Adminhtml/Product/Composite/Fieldset/Configurable.php`** -> AI Confidence: **99.18%**
1319. **`app/code/Magento/ConfigurableProduct/Model/Plugin/ProductIdentitiesExtender.php`** -> AI Confidence: **99.18%**
1320. **`app/code/Magento/ConfigurableProduct/Model/Product/Configuration/Item/ItemProductResolver.php`** -> AI Confidence: **99.18%**
1321. **`app/code/Magento/ConfigurableProduct/Model/ResourceModel/Product/Indexer/Price/Configurable.php`** -> AI Confidence: **99.18%**
1322. **`app/code/Magento/ConfigurableProduct/Model/ResourceModel/Product/Type/Configurable/Attribute/Collection.php`** -> AI Confidence: **99.18%**
1323. **`app/code/Magento/ConfigurableProduct/Pricing/Render/FinalPriceBox.php`** -> AI Confidence: **99.18%**
1324. **`app/code/Magento/ConfigurableProduct/Ui/DataProvider/Product/Form/Modifier/Data/AssociatedProducts.php`** -> AI Confidence: **99.18%**
1325. **`app/code/Magento/ConfigurableProductGraphQl/Model/Options/Collection.php`** -> AI Confidence: **99.18%**
1326. **`app/code/Magento/ConfigurableProductGraphQl/Model/Resolver/ConfigurableCartItemOptions.php`** -> AI Confidence: **99.18%**
1327. **`app/code/Magento/ConfigurableProductGraphQl/Model/Resolver/OptionsSelectionMetadata.php`** -> AI Confidence: **99.18%**
1328. **`app/code/Magento/ConfigurableProductGraphQl/Model/Wishlist/ConfigurableOptions.php`** -> AI Confidence: **99.18%**
1329. **`app/code/Magento/ConfigurableProductSales/Model/Order/Reorder/OrderedProductAvailabilityChecker.php`** -> AI Confidence: **99.18%**
1330. **`app/code/Magento/Cron/Cron/CleanOldJobs.php`** -> AI Confidence: **99.18%**
1331. **`app/code/Magento/Csp/Model/Deploy/Package/Processor/PostProcessor/Map.php`** -> AI Confidence: **99.18%**
1332. **`app/code/Magento/Csp/Plugin/RepositionSriBeforeRequireJsConfig.php`** -> AI Confidence: **99.18%**
1333. **`app/code/Magento/CurrencySymbol/Controller/Adminhtml/System/Currencysymbol/Save.php`** -> AI Confidence: **99.18%**
1334. **`app/code/Magento/Customer/Block/Account/Dashboard.php`** -> AI Confidence: **99.18%**
1335. **`app/code/Magento/Customer/Block/Adminhtml/Edit/Tab/Cart.php`** -> AI Confidence: **99.18%**
1336. **`app/code/Magento/Customer/Block/Adminhtml/Edit/Tab/Newsletter/Grid.php`** -> AI Confidence: **99.18%**
1337. **`app/code/Magento/Customer/Controller/Account/Confirmation.php`** -> AI Confidence: **99.18%**
1338. **`app/code/Magento/Customer/Controller/Account/ForgotPasswordPost.php`** -> AI Confidence: **99.18%**
1339. **`app/code/Magento/Customer/Controller/Adminhtml/Address/DefaultBillingAddress.php`** -> AI Confidence: **99.18%**
1340. **`app/code/Magento/Customer/Controller/Adminhtml/Address/DefaultShippingAddress.php`** -> AI Confidence: **99.18%**
1341. **`app/code/Magento/Customer/Controller/Adminhtml/Cart/Product/Composite/Cart.php`** -> AI Confidence: **99.18%**
1342. **`app/code/Magento/Customer/Controller/Adminhtml/Customer/InvalidateToken.php`** -> AI Confidence: **99.18%**
1343. **`app/code/Magento/Customer/Controller/Adminhtml/Index.php`** -> AI Confidence: **99.18%**
1344. **`app/code/Magento/Customer/Controller/Adminhtml/Index/MassUnsubscribe.php`** -> AI Confidence: **99.18%**
1345. **`app/code/Magento/Customer/Helper/Session/CurrentCustomer.php`** -> AI Confidence: **99.18%**
1346. **`app/code/Magento/Customer/Model/AccountConfirmation.php`** -> AI Confidence: **99.18%**
1347. **`app/code/Magento/Customer/Model/Address.php`** -> AI Confidence: **99.18%**
1348. **`app/code/Magento/Customer/Model/Delegation/Storage.php`** -> AI Confidence: **99.18%**
1349. **`app/code/Magento/Customer/Model/Metadata/AttributeMetadataHydrator.php`** -> AI Confidence: **99.18%**
1350. **`app/code/Magento/Customer/Model/ResourceModel/Grid/Collection.php`** -> AI Confidence: **99.18%**
1351. **`app/code/Magento/Customer/Model/ResourceModel/Online/Grid/Collection.php`** -> AI Confidence: **99.18%**
1352. **`app/code/Magento/Customer/Model/Session.php`** -> AI Confidence: **99.18%**
1353. **`app/code/Magento/Customer/Model/Session/SessionCleaner.php`** -> AI Confidence: **99.18%**
1354. **`app/code/Magento/Customer/Observer/CustomerEmailChangedObserver.php`** -> AI Confidence: **99.18%**
1355. **`app/code/Magento/Customer/Setup/CustomerSetup.php`** -> AI Confidence: **99.18%**
1356. **`app/code/Magento/Customer/Ui/Component/Listing/AttributeRepository.php`** -> AI Confidence: **99.18%**
1357. **`app/code/Magento/CustomerGraphQl/Controller/HttpRequestValidator/AuthorizationRequestValidator.php`** -> AI Confidence: **99.18%**
1358. **`app/code/Magento/CustomerGraphQl/Model/Customer/Address/GetCustomerAddress.php`** -> AI Confidence: **99.18%**
1359. **`app/code/Magento/CustomerGraphQl/Model/Customer/Address/GetCustomerAddressV2.php`** -> AI Confidence: **99.18%**
1360. **`app/code/Magento/CustomerGraphQl/Model/Customer/Address/PopulateCustomerAddressFromInput.php`** -> AI Confidence: **99.18%**
1361. **`app/code/Magento/CustomerGraphQl/Model/Customer/CreateCustomerAccount.php`** -> AI Confidence: **99.18%**
1362. **`app/code/Magento/CustomerGraphQl/Model/Customer/ExtractCustomerData.php`** -> AI Confidence: **99.18%**
1363. **`app/code/Magento/CustomerGraphQl/Model/Customer/GetAllowedCustomerAttributes.php`** -> AI Confidence: **99.18%**
1364. **`app/code/Magento/CustomerGraphQl/Model/Customer/SaveCustomer.php`** -> AI Confidence: **99.18%**
1365. **`app/code/Magento/CustomerGraphQl/Model/Resolver/ConfirmEmail.php`** -> AI Confidence: **99.18%**
1366. **`app/code/Magento/CustomerGraphQl/Model/Resolver/CreateCustomerAddress.php`** -> AI Confidence: **99.18%**
1367. **`app/code/Magento/CustomerGraphQl/Model/Resolver/Customer.php`** -> AI Confidence: **99.18%**
1368. **`app/code/Magento/CustomerGraphQl/Model/Resolver/CustomerAddressesV2.php`** -> AI Confidence: **99.18%**
1369. **`app/code/Magento/CustomerGraphQl/Model/Resolver/DeleteCustomerAddressV2.php`** -> AI Confidence: **99.18%**
1370. **`app/code/Magento/CustomerGraphQl/Model/Resolver/GenerateCustomerToken.php`** -> AI Confidence: **99.18%**
1371. **`app/code/Magento/CustomerGraphQl/Model/Resolver/IsEmailAvailable.php`** -> AI Confidence: **99.18%**
1372. **`app/code/Magento/CustomerGraphQl/Model/Resolver/ResendConfirmationEmail.php`** -> AI Confidence: **99.18%**
1373. **`app/code/Magento/CustomerGraphQl/Model/Resolver/UpdateCustomer.php`** -> AI Confidence: **99.18%**
1374. **`app/code/Magento/CustomerGraphQl/Model/Resolver/UpdateCustomerAddress.php`** -> AI Confidence: **99.18%**
1375. **`app/code/Magento/CustomerGraphQl/Model/Resolver/UpdateCustomerAddressV2.php`** -> AI Confidence: **99.18%**
1376. **`app/code/Magento/CustomerGraphQl/Model/Resolver/UpdateCustomerEmail.php`** -> AI Confidence: **99.18%**
1377. **`app/code/Magento/CustomerGraphQl/Model/Resolver/Visitor.php`** -> AI Confidence: **99.18%**
1378. **`app/code/Magento/CustomerGraphQl/Plugin/ClearCustomerSessionAfterRequest.php`** -> AI Confidence: **99.18%**
1379. **`app/code/Magento/CustomerImportExport/Model/Export/Address.php`** -> AI Confidence: **99.18%**
1380. **`app/code/Magento/Deploy/Console/Command/App/SensitiveConfigSet/SensitiveConfigSetFacade.php`** -> AI Confidence: **99.18%**
1381. **`app/code/Magento/Deploy/Model/ConfigWriter.php`** -> AI Confidence: **99.18%**
1382. **`app/code/Magento/Deploy/Model/Mode.php`** -> AI Confidence: **99.18%**
1383. **`app/code/Magento/Deploy/Package/Processor/PostProcessor/Map.php`** -> AI Confidence: **99.18%**
1384. **`app/code/Magento/Deploy/Service/DeployStaticFile.php`** -> AI Confidence: **99.18%**
1385. **`app/code/Magento/Developer/Console/Command/GeneratePatchCommand.php`** -> AI Confidence: **99.18%**
1386. **`app/code/Magento/Developer/Console/Command/ProfilerEnableCommand.php`** -> AI Confidence: **99.18%**
1387. **`app/code/Magento/Developer/Console/Command/SourceThemeDeployCommand.php`** -> AI Confidence: **99.18%**
1388. **`app/code/Magento/Developer/Console/Command/XmlCatalogGenerateCommand.php`** -> AI Confidence: **99.18%**
1389. **`app/code/Magento/Developer/Console/Command/XmlConverterCommand.php`** -> AI Confidence: **99.18%**
1390. **`app/code/Magento/Developer/Model/Css/PreProcessor/FileGenerator/PublicationDecorator.php`** -> AI Confidence: **99.18%**
1391. **`app/code/Magento/Developer/Model/Logger/Handler/Debug.php`** -> AI Confidence: **99.18%**
1392. **`app/code/Magento/Developer/Model/View/Asset/PreProcessor/FrontendCompilation.php`** -> AI Confidence: **99.18%**
1393. **`app/code/Magento/Directory/Model/PriceCurrency.php`** -> AI Confidence: **99.18%**
1394. **`app/code/Magento/DirectoryGraphQl/Model/Resolver/Country.php`** -> AI Confidence: **99.18%**
1395. **`app/code/Magento/Downloadable/Console/Command/DomainsAddCommand.php`** -> AI Confidence: **99.18%**
1396. **`app/code/Magento/Downloadable/Console/Command/DomainsRemoveCommand.php`** -> AI Confidence: **99.18%**
1397. **`app/code/Magento/Downloadable/Model/Sample/Builder.php`** -> AI Confidence: **99.18%**
1398. **`app/code/Magento/Downloadable/Setup/Patch/Data/InstallDownloadableAttributes.php`** -> AI Confidence: **99.18%**
1399. **`app/code/Magento/DownloadableGraphQl/Resolver/DownloadableCartItem/Links.php`** -> AI Confidence: **99.18%**
1400. **`app/code/Magento/DownloadableGraphQl/Resolver/DownloadableCartItem/Samples.php`** -> AI Confidence: **99.18%**
1401. **`app/code/Magento/DownloadableGraphQl/Resolver/Order/Item/Links.php`** -> AI Confidence: **99.18%**
1402. **`app/code/Magento/DownloadableGraphQl/Resolver/Product/Links.php`** -> AI Confidence: **99.18%**
1403. **`app/code/Magento/DownloadableGraphQl/Resolver/Product/Samples.php`** -> AI Confidence: **99.18%**
1404. **`app/code/Magento/Eav/Model/Entity/Setup/PropertyMapper.php`** -> AI Confidence: **99.18%**
1405. **`app/code/Magento/Eav/Model/ResourceModel/Form/Fieldset/Collection.php`** -> AI Confidence: **99.18%**
1406. **`app/code/Magento/EavGraphQl/Model/Resolver/AttributesForm.php`** -> AI Confidence: **99.18%**
1407. **`app/code/Magento/Elasticsearch/ElasticAdapter/SearchAdapter/Adapter.php`** -> AI Confidence: **99.18%**
1408. **`app/code/Magento/Elasticsearch/Model/Adapter/FieldMapper/Product/FieldProvider/DynamicField.php`** -> AI Confidence: **99.18%**
1409. **`app/code/Magento/Elasticsearch/Model/Indexer/Fulltext/Plugin/Category/Product/Attribute.php`** -> AI Confidence: **99.18%**
1410. **`app/code/Magento/Elasticsearch/SearchAdapter/Query/Preprocessor/Stopwords.php`** -> AI Confidence: **99.18%**
1411. **`app/code/Magento/Elasticsearch8/SearchAdapter/Adapter.php`** -> AI Confidence: **99.18%**
1412. **`app/code/Magento/EncryptionKey/Console/Command/UpdateEncryptionKeyCommand.php`** -> AI Confidence: **99.18%**
1413. **`app/code/Magento/EncryptionKey/Model/ResourceModel/Key/Change.php`** -> AI Confidence: **99.18%**
1414. **`app/code/Magento/GiftMessage/Model/GiftMessageConfigProvider.php`** -> AI Confidence: **99.18%**
1415. **`app/code/Magento/GiftMessageGraphQl/Model/Resolver/Product/GiftMessage.php`** -> AI Confidence: **99.18%**
1416. **`app/code/Magento/GoogleGtag/Block/Ga.php`** -> AI Confidence: **99.18%**
1417. **`app/code/Magento/GraphQl/Controller/HttpRequestValidator/HttpVerbValidator.php`** -> AI Confidence: **99.18%**
1418. **`app/code/Magento/GraphQl/Helper/Error/AggregateExceptionMessageFormatter.php`** -> AI Confidence: **99.18%**
1419. **`app/code/Magento/GraphQl/Helper/Error/MessageFormatters/GraphQlExceptionMessageFormatter.php`** -> AI Confidence: **99.18%**
1420. **`app/code/Magento/GraphQl/Helper/Error/MessageFormatters/ValidationExceptionMessageFormatter.php`** -> AI Confidence: **99.18%**
1421. **`app/code/Magento/GraphQlCache/Controller/Plugin/GraphQl.php`** -> AI Confidence: **99.18%**
1422. **`app/code/Magento/GraphQlCache/Model/CacheId/CacheIdCalculator.php`** -> AI Confidence: **99.18%**
1423. **`app/code/Magento/GraphQlResolverCache/Model/Plugin/Resolver/Cache.php`** -> AI Confidence: **99.18%**
1424. **`app/code/Magento/ImportExport/Block/Adminhtml/Import/Edit/Form.php`** -> AI Confidence: **99.18%**
1425. **`app/code/Magento/ImportExport/Controller/Adminhtml/Export/File/Delete.php`** -> AI Confidence: **99.18%**
1426. **`app/code/Magento/ImportExport/Controller/Adminhtml/ImportResult.php`** -> AI Confidence: **99.18%**
1427. **`app/code/Magento/ImportExport/Model/Import/RenderErrorMessages.php`** -> AI Confidence: **99.18%**
1428. **`app/code/Magento/Indexer/Console/Command/IndexerSetStatusCommand.php`** -> AI Confidence: **99.18%**
1429. **`app/code/Magento/InstantPurchase/Controller/Button/PlaceOrder.php`** -> AI Confidence: **99.18%**
1430. **`app/code/Magento/Integration/Model/AdminTokenService.php`** -> AI Confidence: **99.18%**
1431. **`app/code/Magento/Integration/Model/CustomerTokenService.php`** -> AI Confidence: **99.18%**
1432. **`app/code/Magento/Integration/Model/OpaqueToken/Issuer.php`** -> AI Confidence: **99.18%**
1433. **`app/code/Magento/Integration/Setup/Patch/Data/UpgradeConsumerSecret.php`** -> AI Confidence: **99.18%**
1434. **`app/code/Magento/JwtUserToken/Model/Issuer.php`** -> AI Confidence: **99.18%**
1435. **`app/code/Magento/LoginAsCustomer/Model/ResourceModel/SaveAuthenticationData.php`** -> AI Confidence: **99.18%**
1436. **`app/code/Magento/LoginAsCustomerAdminUi/Ui/Customer/Component/Control/LoginAsCustomerButton.php`** -> AI Confidence: **99.18%**
1437. **`app/code/Magento/LoginAsCustomerFrontendUi/Controller/Login/Index.php`** -> AI Confidence: **99.18%**
1438. **`app/code/Magento/MediaContent/Model/UpdateContentAssetLinks.php`** -> AI Confidence: **99.18%**
1439. **`app/code/Magento/MediaContentCatalog/Model/ResourceModel/GetAssetIdsByCategoryStore.php`** -> AI Confidence: **99.18%**
1440. **`app/code/Magento/MediaContentCatalog/Observer/Category.php`** -> AI Confidence: **99.18%**
1441. **`app/code/Magento/MediaContentCatalog/Observer/CategoryDelete.php`** -> AI Confidence: **99.18%**
1442. **`app/code/Magento/MediaContentCatalog/Observer/Product.php`** -> AI Confidence: **99.18%**
1443. **`app/code/Magento/MediaContentCatalog/Observer/ProductDelete.php`** -> AI Confidence: **99.18%**
1444. **`app/code/Magento/MediaContentCms/Observer/BlockDelete.php`** -> AI Confidence: **99.18%**
1445. **`app/code/Magento/MediaContentCms/Observer/PageDelete.php`** -> AI Confidence: **99.18%**
1446. **`app/code/Magento/MediaContentSynchronization/Model/ResourceModel/GetOutdatedRelations.php`** -> AI Confidence: **99.18%**
1447. **`app/code/Magento/MediaGallery/Model/Asset/Command/GetByPath.php`** -> AI Confidence: **99.18%**
1448. **`app/code/Magento/MediaGallery/Model/Keyword/Command/SaveAssetKeywords.php`** -> AI Confidence: **99.18%**
1449. **`app/code/Magento/MediaGallery/Model/ResourceModel/Keyword/GetAssetsKeywords.php`** -> AI Confidence: **99.18%**
1450. **`app/code/Magento/MediaGalleryMetadata/Model/File/AddMetadata.php`** -> AI Confidence: **99.18%**
1451. **`app/code/Magento/MediaGalleryMetadata/Model/Jpeg/WriteFile.php`** -> AI Confidence: **99.18%**
1452. **`app/code/Magento/MediaGallerySynchronization/Model/SynchronizeFiles.php`** -> AI Confidence: **99.18%**
1453. **`app/code/Magento/MediaGallerySynchronizationMetadata/Model/ImportKeywords.php`** -> AI Confidence: **99.18%**
1454. **`app/code/Magento/MediaGalleryUi/Controller/Adminhtml/Asset/Search.php`** -> AI Confidence: **99.18%**
1455. **`app/code/Magento/MediaGalleryUi/Controller/Adminhtml/Directories/Create.php`** -> AI Confidence: **99.18%**
1456. **`app/code/Magento/MediaGalleryUi/Controller/Adminhtml/Directories/Delete.php`** -> AI Confidence: **99.18%**
1457. **`app/code/Magento/MediaGalleryUi/Controller/Adminhtml/Image/Details.php`** -> AI Confidence: **99.18%**
1458. **`app/code/Magento/MediaGalleryUi/Controller/Adminhtml/Image/Upload.php`** -> AI Confidence: **99.18%**
1459. **`app/code/Magento/MediaGalleryUi/Model/InsertImageData/GetInsertImageData.php`** -> AI Confidence: **99.18%**
1460. **`app/code/Magento/MediaGalleryUi/Model/UpdateAsset.php`** -> AI Confidence: **99.18%**
1461. **`app/code/Magento/MediaGalleryUi/Ui/Component/Listing/Filters/Asset.php`** -> AI Confidence: **99.18%**
1462. **`app/code/Magento/NewRelicReporting/Model/Observer/CheckConfig.php`** -> AI Confidence: **99.18%**
1463. **`app/code/Magento/Newsletter/Console/Command/TemplateCheckCommand.php`** -> AI Confidence: **99.18%**
1464. **`app/code/Magento/Newsletter/Controller/Ajax/Status.php`** -> AI Confidence: **99.18%**
1465. **`app/code/Magento/Newsletter/Model/Queue/TransportBuilder.php`** -> AI Confidence: **99.18%**
1466. **`app/code/Magento/Newsletter/Model/Subscriber.php`** -> AI Confidence: **99.18%**
1467. **`app/code/Magento/Newsletter/Observer/PredispatchNewsletterObserver.php`** -> AI Confidence: **99.18%**
1468. **`app/code/Magento/OrderCancellation/Model/CancelOrder.php`** -> AI Confidence: **99.18%**
1469. **`app/code/Magento/OrderCancellationGraphQl/Model/Resolver/CancelOrder.php`** -> AI Confidence: **99.18%**
1470. **`app/code/Magento/OrderCancellationGraphQl/Model/Resolver/RequestGuestOrderCancel.php`** -> AI Confidence: **99.18%**
1471. **`app/code/Magento/PageCache/Console/Command/GenerateVclCommand.php`** -> AI Confidence: **99.18%**
1472. **`app/code/Magento/PageCache/Model/App/FrontController/VarnishPlugin.php`** -> AI Confidence: **99.18%**
1473. **`app/code/Magento/PageCache/Model/Controller/Result/BuiltinPlugin.php`** -> AI Confidence: **99.18%**
1474. **`app/code/Magento/PageCache/Observer/FlushCacheByTags.php`** -> AI Confidence: **99.18%**
1475. **`app/code/Magento/Payment/Model/IframeConfigProvider.php`** -> AI Confidence: **99.18%**
1476. **`app/code/Magento/Paypal/Block/Express/InContext/Minicart/SmartButton.php`** -> AI Confidence: **99.18%**
1477. **`app/code/Magento/Paypal/Controller/Adminhtml/Express/Authorization.php`** -> AI Confidence: **99.18%**
1478. **`app/code/Magento/Paypal/Controller/Express/GetTokenData.php`** -> AI Confidence: **99.18%**
1479. **`app/code/Magento/Paypal/Controller/Transparent/Response.php`** -> AI Confidence: **99.18%**
1480. **`app/code/Magento/Paypal/Model/Payflow/Transparent.php`** -> AI Confidence: **99.18%**
1481. **`app/code/Magento/ProductAlert/Model/Email.php`** -> AI Confidence: **99.18%**
1482. **`app/code/Magento/Quote/Model/Backpressure/Config/PeriodValue.php`** -> AI Confidence: **99.18%**
1483. **`app/code/Magento/Quote/Model/BillingAddressManagement.php`** -> AI Confidence: **99.18%**
1484. **`app/code/Magento/Quote/Model/Quote/Address/Validator.php`** -> AI Confidence: **99.18%**
1485. **`app/code/Magento/QuoteCommerceGraphQl/Model/Resolver/ClearCart.php`** -> AI Confidence: **99.18%**
1486. **`app/code/Magento/QuoteGraphQl/Model/Cart/AssignBillingAddressToCart.php`** -> AI Confidence: **99.18%**
1487. **`app/code/Magento/QuoteGraphQl/Model/CartItem/DataProvider/CustomizableOptionValue/Multiple.php`** -> AI Confidence: **99.18%**
1488. **`app/code/Magento/QuoteGraphQl/Model/Resolver/AddSimpleProductsToCart.php`** -> AI Confidence: **99.18%**
1489. **`app/code/Magento/QuoteGraphQl/Model/Resolver/BillingAddress.php`** -> AI Confidence: **99.18%**
1490. **`app/code/Magento/QuoteGraphQl/Model/Resolver/MaskedCartId.php`** -> AI Confidence: **99.18%**
1491. **`app/code/Magento/QuoteGraphQl/Model/Resolver/SetBillingAddressOnCart.php`** -> AI Confidence: **99.18%**
1492. **`app/code/Magento/QuoteGraphQl/Model/Resolver/SetPaymentMethodOnCart.php`** -> AI Confidence: **99.18%**
1493. **`app/code/Magento/QuoteGraphQl/Model/Resolver/SetShippingAddressesOnCart.php`** -> AI Confidence: **99.18%**
1494. **`app/code/Magento/QuoteGraphQl/Model/Resolver/SetShippingMethodsOnCart.php`** -> AI Confidence: **99.18%**
1495. **`app/code/Magento/QuoteGraphQl/Model/Resolver/ShippingAddress/AvailableShippingMethods.php`** -> AI Confidence: **99.18%**
1496. **`app/code/Magento/RelatedProductGraphQl/Model/Resolver/Batch/AbstractLikedProducts.php`** -> AI Confidence: **99.18%**
1497. **`app/code/Magento/RelatedProductGraphQl/Model/Resolver/CrossSellProducts.php`** -> AI Confidence: **99.18%**
1498. **`app/code/Magento/RelatedProductGraphQl/Model/Resolver/RelatedProducts.php`** -> AI Confidence: **99.18%**
1499. **`app/code/Magento/RelatedProductGraphQl/Model/Resolver/UpSellProducts.php`** -> AI Confidence: **99.18%**
1500. **`app/code/Magento/ReleaseNotification/Controller/Adminhtml/Notification/MarkUserNotified.php`** -> AI Confidence: **99.18%**
1501. **`app/code/Magento/RemoteStorage/Model/File/Storage/Synchronization.php`** -> AI Confidence: **99.18%**
1502. **`app/code/Magento/RemoteStorage/Model/Synchronizer.php`** -> AI Confidence: **99.18%**
1503. **`app/code/Magento/Review/Block/Product/ReviewRenderer.php`** -> AI Confidence: **99.18%**
1504. **`app/code/Magento/Review/Model/Review.php`** -> AI Confidence: **99.18%**
1505. **`app/code/Magento/ReviewGraphQl/Model/Resolver/CreateProductReview.php`** -> AI Confidence: **99.18%**
1506. **`app/code/Magento/ReviewGraphQl/Model/Resolver/Customer/Reviews.php`** -> AI Confidence: **99.18%**
1507. **`app/code/Magento/ReviewGraphQl/Model/Resolver/Product/RatingSummary.php`** -> AI Confidence: **99.18%**
1508. **`app/code/Magento/ReviewGraphQl/Model/Resolver/Product/Review/AverageRating.php`** -> AI Confidence: **99.18%**
1509. **`app/code/Magento/ReviewGraphQl/Model/Resolver/Product/ReviewCount.php`** -> AI Confidence: **99.18%**
1510. **`app/code/Magento/ReviewGraphQl/Model/Resolver/Product/Reviews.php`** -> AI Confidence: **99.18%**
1511. **`app/code/Magento/ReviewGraphQl/Model/Review/AddReviewToProduct.php`** -> AI Confidence: **99.18%**
1512. **`app/code/Magento/Robots/Model/Config/Value.php`** -> AI Confidence: **99.18%**
1513. **`app/code/Magento/Sales/Controller/Adminhtml/Order/Create/Reorder.php`** -> AI Confidence: **99.18%**
1514. **`app/code/Magento/Sales/Controller/Guest/Form.php`** -> AI Confidence: **99.18%**
1515. **`app/code/Magento/Sales/Model/AdminOrder/EmailSender.php`** -> AI Confidence: **99.18%**
1516. **`app/code/Magento/Sales/Model/Order/Address/Renderer.php`** -> AI Confidence: **99.18%**
1517. **`app/code/Magento/Sales/Model/Order/Creditmemo/Item/Validation/CreationQuantityValidator.php`** -> AI Confidence: **99.18%**
1518. **`app/code/Magento/Sales/Model/Order/Email/Sender/CreditmemoSender.php`** -> AI Confidence: **99.18%**
1519. **`app/code/Magento/Sales/Model/Order/Email/Sender/InvoiceSender.php`** -> AI Confidence: **99.18%**
1520. **`app/code/Magento/Sales/Model/Order/Email/Sender/ShipmentSender.php`** -> AI Confidence: **99.18%**
1521. **`app/code/Magento/Sales/Model/Order/Payment.php`** -> AI Confidence: **99.18%**
1522. **`app/code/Magento/Sales/Model/Order/Payment/Transaction/Repository.php`** -> AI Confidence: **99.18%**
1523. **`app/code/Magento/Sales/Model/Order/Pdf/Items/AbstractItems.php`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `app/code/Magento/AdminAnalytics/Model/Condition/CanViewNotification.php` -> **100.0%** Exposure
- `app/code/Magento/AdminNotification/Block/Grid/Renderer/Actions.php` -> **100.0%** Exposure
- `app/code/Magento/AdminNotification/Block/Grid/Renderer/Severity.php` -> **100.0%** Exposure
- `app/code/Magento/AdminNotification/Block/ToolbarEntry.php` -> **100.0%** Exposure
- `app/code/Magento/AdminNotification/Block/Window.php` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `app/code/Magento/AdminNotification/Controller/Adminhtml/Notification/Index.php` -> **100.0%** Exposure
- `app/code/Magento/Backend/Controller/Adminhtml/System/Design/Edit.php` -> **100.0%** Exposure
- `app/code/Magento/Backend/Controller/Adminhtml/System/Design/Index.php` -> **100.0%** Exposure
- `app/code/Magento/Backend/Controller/Adminhtml/System/Design/NewAction.php` -> **100.0%** Exposure
- `app/code/Magento/Backend/Controller/Adminhtml/System/SetStore.php` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `app/code/Magento/AdminAnalytics/Controller/Adminhtml/Config/DisableAdminUsage.php` -> **100.0%** Exposure
- `app/code/Magento/AdminAnalytics/Controller/Adminhtml/Config/EnableAdminUsage.php` -> **100.0%** Exposure
- `app/code/Magento/AdminAnalytics/Model/Condition/CanViewNotification.php` -> **100.0%** Exposure
- `app/code/Magento/AdminAnalytics/Model/ResourceModel/Viewer/Logger.php` -> **100.0%** Exposure
- `app/code/Magento/AdminAnalytics/ViewModel/Metadata.php` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `46` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `52115` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `app/code/Magento/Downloadable/view/adminhtml/templates/product/edit/downloadable.phtml` (PHP) -> Cumulative Risk: **850.78**
- **Archetype:** `file_cluster_8` (Distance: 13.192 IQR)
- **Magnitude:** 452.7 | **LOC:** 268 | **CtrlFlow:** 78.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `require` (Impact: 311.2), `require` (Impact: 17.8), `require` (Impact: 6.0)

### 2. `app/code/Magento/Backup/Model/ResourceModel/Helper.php` (PHP) -> Cumulative Risk: **834.47**
- **Archetype:** `file_cluster_13` (Distance: 14.514 IQR)
- **Magnitude:** 529.74 | **LOC:** 379 | **CtrlFlow:** 52.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `getTableCreateSql` (Impact: 100.7), `getTableTriggersSql` (Impact: 36.4), `_quoteRow` (Impact: 31.3)

### 3. `app/code/Magento/Catalog/Model/Indexer/Product/Flat/Action/Eraser.php` (PHP) -> Cumulative Risk: **814.05**
- **Archetype:** `file_cluster_13` (Distance: 12.634 IQR)
- **Magnitude:** 139.14 | **LOC:** 170 | **CtrlFlow:** 45.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `deleteProductsFromStore` (Impact: 37.3), `removeDisabledProducts` (Impact: 15.8), `__construct` (Impact: 14.0)

### 4. `app/code/Magento/Sales/Model/ResourceModel/Grid.php` (PHP) -> Cumulative Risk: **812.31**
- **Archetype:** `file_cluster_13` (Distance: 13.466 IQR)
- **Magnitude:** 255.08 | **LOC:** 221 | **CtrlFlow:** 38.3% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `__construct` (Impact: 64.5), `refreshBySchedule` (Impact: 37.7), `getGridOriginSelect` (Impact: 27.4)

### 5. `app/code/Magento/Catalog/Model/Layer/Filter/DataProvider/Price.php` (PHP) -> Cumulative Risk: **797.15**
- **Archetype:** `file_cluster_13` (Distance: 13.281 IQR)
- **Magnitude:** 420.7 | **LOC:** 412 | **CtrlFlow:** 41.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `getPriceRange` (Impact: 62.3), `getRangeItemCounts` (Impact: 42.8), `validateFilter` (Impact: 39.7)

### 6. `app/code/Magento/Ui/view/base/web/js/form/components/insert.js` (JAVASCRIPT) -> Cumulative Risk: **792.75**
- **Archetype:** `file_cluster_8` (Distance: 13.494 IQR)
- **Magnitude:** 421.3 | **LOC:** 321 | **CtrlFlow:** 45.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `define` (Impact: 284.3)

### 7. `app/code/Magento/DownloadableImportExport/Helper/Data.php` (PHP) -> Cumulative Risk: **791.41**
- **Archetype:** `file_cluster_13` (Distance: 12.908 IQR)
- **Magnitude:** 124.6 | **LOC:** 111 | **CtrlFlow:** 48.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (99.9984%)
- **Heaviest Functions:** `fillExistOptions` (Impact: 61.0), `getTypeByValue` (Impact: 10.8), `isRowDownloadableEmptyOptions` (Impact: 8.2)

### 8. `app/code/Magento/Customer/Model/Metadata/Form/Multiline.php` (PHP) -> Cumulative Risk: **789.39**
- **Archetype:** `file_cluster_13` (Distance: 13.169 IQR)
- **Magnitude:** 327.7 | **LOC:** 128 | **CtrlFlow:** 61.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9814%)
- **Heaviest Functions:** `validateValue` (Impact: 147.6), `outputValue` (Impact: 62.6), `compactValue` (Impact: 14.4)

### 9. `app/code/Magento/Customer/Model/Plugin/UpdateCustomer.php` (PHP) -> Cumulative Risk: **788.61**
- **Archetype:** `file_cluster_13` (Distance: 13.717 IQR)
- **Magnitude:** 140.94 | **LOC:** 102 | **CtrlFlow:** 45.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `beforeSave` (Impact: 49.2), `getUpdatedCustomer` (Impact: 22.6), `__construct` (Impact: 8.0)

### 10. `app/code/Magento/Catalog/Model/Indexer/Category/Product/Plugin/MviewState.php` (PHP) -> Cumulative Risk: **788.25**
- **Archetype:** `file_cluster_8` (Distance: 13.178 IQR)
- **Magnitude:** 64.38 | **LOC:** 82 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.7273%)
- **Heaviest Functions:** `afterSetStatus` (Impact: 49.6), `__construct` (Impact: 2.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `app/code/Magento/Ups/Model/Carrier.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.441 IQR)
- **Top Global Matches:** file_cluster_13: 14.441, file_cluster_8: 14.466, file_cluster_7: 14.619
- **Magnitude:** 4171.72 | **LOC:** 3012 | **CtrlFlow:** 59.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 56
- **Risk Profile:** Cognitive Load (36.92%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_formShipmentRequest` (Impact: 255.2 | O(N^6) | DB: 43)
  * `_formShipmentRestRequest` (Impact: 227.6 | O(N^6) | DB: 56)
  * `setRequest` (Impact: 169.8 | O(N^5) | DB: 19)
    * *Intent:* * @param LoggerInterface $logger * @param Security $xmlSecurity * @param ElementFactory $xmlElFactor...
  * `processShippingRestRateForItem` (Impact: 160.8 | O(N^6) | DB: 20)
  * `getContainerTypes` (Impact: 148.1 | O(N^6) | DB: 21)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 373`, `structural_boundaries: 252`, `args: 58`, `func_start: 55`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 1315`
* *Architecture:* `api: 33`, `import: 44`
* *Defense:* `safety: 76`, `doc: 268`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.044
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 21):` Magento\Framework\DataObject, Magento\Shipping\Model\Tracking\Result\StatusFactory, Magento\Shipping\Model\Tracking\ResultFactory, Magento\Framework\Measure\Length, Magento\Shipping\Model\Tracking\Result\ErrorFactory, Magento\Shipping\Model\Shipment\Request, Magento\Framework\App\ObjectManager, Magento\Directory\Helper\Data...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/code/Magento/CatalogImportExport/Model/Import/Product/Option.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.657 IQR)
- **Top Global Matches:** file_cluster_8: 14.657, file_cluster_13: 14.661, file_cluster_7: 14.778
- **Magnitude:** 2966.14 | **LOC:** 2252 | **CtrlFlow:** 58.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 42
- **Risk Profile:** Cognitive Load (39.2344%), Tech Debt (16.3599%)
**Top Internal Functions/Classes:**
  * `_importData` (Impact: 132.9 | O(N^6) | DB: 42)
    * *Intent:* /** * Save option data in array for non-existing new product * * @param array $rowData
  * `__construct` (Impact: 115.2 | O(N^3) | DB: 24)
  * `_parseCustomOptions` (Impact: 99.8 | O(N^6) | DB: 21)
  * `_getSpecificTypeData` (Impact: 85.4 | O(N^5) | DB: 6)
  * `_collectOptionTypeData` (Impact: 74.9 | O(N^6) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 313`, `structural_boundaries: 224`, `args: 63`, `func_start: 61`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 749`, `dead_code: 1`, `planned_debt: 1`, `orphaned_logic: 7`
* *Architecture:* `api: 28`, `import: 20`
* *Defense:* `safety: 111`, `doc: 332`, `immutability_locks: 23`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` Magento\ImportExport\Model\ResourceModel\CollectionByPagesIteratorFactory, Magento\ImportExport\Model\ResourceModel\Helper, Magento\Framework\App\ObjectManager, $rowNumber, Magento\CatalogImportExport\Model\Import\Product, Magento\ImportExport\Model\Import\ErrorProcessing\ProcessingErrorAggregatorInterface, Magento\Store\Model\StoreManagerInterface, Magento\Framework\Model\ResourceModel\Db\TransactionManagerInterface...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/code/Magento/Sales/Model/Order.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.094 IQR)
- **Top Global Matches:** file_cluster_8: 13.094, file_cluster_7: 13.152, file_cluster_13: 13.17
- **Magnitude:** 2866.66 | **LOC:** 4738 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (23.627%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_canReorder` (Impact: 68.9 | O(N^5) | DB: 5)
  * `registerCancellation` (Impact: 68.9 | O(N^6) | DB: 5)
  * `canEdit` (Impact: 63.8 | O(2^N) | DB: 3)
  * `checkItemShipping` (Impact: 58.2 | O(N^5) | DB: 3)
  * `canCancel` (Impact: 58.0 | O(N^4) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 232`, `structural_boundaries: 898`, `args: 375`, `func_start: 375`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 433`
* *Architecture:* `api: 526`, `import: 44`
* *Defense:* `safety: 17`, `doc: 824`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.58
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 30):` Magento\Framework\Api\SearchCriteriaBuilder, Magento\Sales\Model\ResourceModel\Order\Creditmemo\Collection, Magento\Catalog\Api\ProductRepositoryInterface, Magento\Framework\Data\Collection\AbstractDb, Magento\Framework\App\ObjectManager, Magento\Store\Model\StoreManagerInterface, Magento\Sales\Api\Data\OrderInterface, Magento\Framework\Locale\ResolverInterface...
  * `Imported By (In-Degree: 161):` (Excluded from Brief to save tokens)

### `app/code/Magento/Dhl/Model/Carrier.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.24 IQR)
- **Top Global Matches:** file_cluster_13: 14.24, file_cluster_8: 14.408, file_cluster_7: 14.579
- **Magnitude:** 2744.36 | **LOC:** 2939 | **CtrlFlow:** 56.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 47
- **Risk Profile:** Cognitive Load (37.3832%), Tech Debt (12.7316%)
**Top Internal Functions/Classes:**
  * `_doShipmentRequestRest` (Impact: 198.1 | O(N^6) | DB: 47)
  * `_doRequest` (Impact: 185.7 | O(N^6) | DB: 40)
  * `_addRate` (Impact: 178.3 | O(N^6) | DB: 15)
  * `_parseXmlTrackingResponse` (Impact: 173.9 | O(N^6) | DB: 21)
  * `_addRestRate` (Impact: 155.1 | O(N^6) | DB: 17)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 276`, `structural_boundaries: 215`, `args: 46`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 758`, `dead_code: 1`, `orphaned_logic: 8`
* *Architecture:* `api: 19`, `import: 55`
* *Defense:* `safety: 100`, `doc: 192`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` Magento\Framework\DataObject, Magento\Shipping\Model\Tracking\Result\StatusFactory, Magento\Shipping\Model\Tracking\ResultFactory, Magento\Framework\Measure\Length, Magento\Framework\Stdlib\StringUtils, Magento\Shipping\Model\Tracking\Result\ErrorFactory, Magento\Shipping\Model\Shipment\Request, Magento\Framework\App\ObjectManager...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/code/Magento/Catalog/Model/ResourceModel/Product/Collection.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.835 IQR)
- **Top Global Matches:** file_cluster_13: 13.835, file_cluster_8: 13.843, file_cluster_7: 13.927
- **Magnitude:** 2728.28 | **LOC:** 2584 | **CtrlFlow:** 44.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (36.5377%), Tech Debt (8.1641%)
**Top Internal Functions/Classes:**
  * `__construct` (Impact: 441.8 | O(2^N) | DB: 30)
    * *Intent:* /**
  * `addAttributeToSort` (Impact: 179.5 | O(2^N) | DB: 8)
    * *Intent:* /** * Retrieve all ids for collection
  * `addAttributeToFilter` (Impact: 146.0 | O(2^N) | DB: 8)
  * `addAttributeToSelect` (Impact: 110.5 | O(2^N) | DB: 6)
  * `_productLimitationPrice` (Impact: 88.4 | O(N^6) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 212`, `structural_boundaries: 264`, `args: 81`, `func_start: 79`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 597`, `planned_debt: 1`
* *Architecture:* `api: 94`, `import: 19`
* *Defense:* `safety: 39`, `doc: 330`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.381
  * `Choke Point (Betweenness):` 0.000222 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` 'left', Magento\Catalog\Model\Product\Attribute\Source\Status, Magento\Catalog\Model\ResourceModel\Product\Collection\ProductLimitationFactory, Magento\Framework\App\ObjectManager, 
    public function addTaxPercents()
    
        $this->_addTaxPercents = true, Magento\Customer\Model\Indexer\CustomerGroupDimensionProvider, Magento\Framework\Indexer\DimensionFactory, 
    public function addFilterByRequiredOptions()
    
        $this->addAttributeToFilter('required_options'...
  * `Imported By (In-Degree: 72):` (Excluded from Brief to save tokens)

### `app/code/Magento/Usps/Model/Carrier.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.024 IQR)
- **Top Global Matches:** file_cluster_8: 13.024, file_cluster_7: 13.211, file_cluster_13: 13.232
- **Magnitude:** 2317.12 | **LOC:** 2538 | **CtrlFlow:** 65.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 60
- **Risk Profile:** Cognitive Load (35.0969%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_formIntlShipmentRequest` (Impact: 288.2 | O(N^5) | DB: 60)
  * `_parseXmlResponse` (Impact: 197.9 | O(N^6) | DB: 15)
  * `setRequest` (Impact: 174.2 | O(N^5) | DB: 21)
    * *Intent:* * @param \Psr\Log\LoggerInterface $logger * @param Security $xmlSecurity * @param \Magento\Shipping\...
  * `_doShipmentRequest` (Impact: 158.6 | O(N^6) | DB: 30)
  * `__construct` (Impact: 148.5 | O(2^N) | DB: 14)
    * *Intent:* /** * Container types that could be customized for USPS carrier
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 230`, `structural_boundaries: 123`, `args: 33`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 619`
* *Architecture:* `api: 45`, `import: 19`
* *Defense:* `safety: 30`, `doc: 183`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` Magento\Framework\DataObject, Magento\Shipping\Helper\Carrier, Magento\Framework\Measure\Length, Magento\Framework\App\ObjectManager, Magento\Framework\HTTP\AsyncClientInterface, Magento\Framework\Async\CallbackDeferred, Magento\Shipping\Model\Rate\Result, Magento\Framework\Measure\Weight...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/code/Magento/Ui/view/base/web/js/form/element/ui-select.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_15` (Drift: 14.757 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 3.755 IQR)
- **Top Global Matches:** file_cluster_15: 14.757, file_cluster_8: 14.84, file_cluster_7: 14.962
- **Magnitude:** 2298.82 | **LOC:** 1315 | **CtrlFlow:** 56.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 293
- **Risk Profile:** Cognitive Load (40.2999%), Tech Debt (9.2161%)
**Top Internal Functions/Classes:**
  * `define` (Impact: 1631.7 | O(N^6) | DB: 293)
    * *Intent:* /** * Copyright 2015 Adobe * All Rights Reserved.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 92`, `args: 77`, `func_start: 69`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 641`, `orphaned_logic: 1`
* *Architecture:* `io: 8`, `concurrency: 12`
* *Defense:* `safety: 20`, `doc: 165`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/code/Magento/Sales/Model/Order/Payment.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.137 IQR)
- **Top Global Matches:** file_cluster_8: 13.137, file_cluster_7: 13.192, file_cluster_13: 13.29
- **Magnitude:** 2256.94 | **LOC:** 2618 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 80.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (36.4127%), Tech Debt (9.3378%)
**Top Internal Functions/Classes:**
  * `refund` (Impact: 186.7 | O(2^N) | DB: 15)
    * *Intent:* /** * Perform actions based on passed action name * * @param string $action
  * `__construct` (Impact: 124.1 | O(2^N) | DB: 14)
    * *Intent:* /**
  * `updateOrder` (Impact: 88.4 | O(N^5) | DB: 4)
  * `update` (Impact: 80.0 | O(2^N) | DB: 7)
    * *Intent:* // update transactions and order state
  * `deny` (Impact: 79.9 | O(2^N) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 379`, `args: 177`, `func_start: 177`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 350`, `dead_code: 1`, `planned_debt: 5`
* *Architecture:* `api: 267`, `import: 11`
* *Defense:* `safety: 11`, `doc: 429`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.397
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` $skipFraudDetection = false)
    
        return $this->orderPaymentProcessor->registerCaptureNotification($this, Magento\Sales\Api\Data\OrderPaymentInterface, 
    public function refund($creditmemo)
    
        $baseAmountToRefund = $this->formatAmount($creditmemo->getBaseGrandTotal(), Magento\Sales\Model\Order, Magento\Framework\App\ObjectManager, d
     * Updates payment totals, d)
                return $invoice, Magento\Sales\Api\OrderRepositoryInterface...
  * `Imported By (In-Degree: 41):` (Excluded from Brief to save tokens)

### `app/code/Magento/Quote/Model/Quote.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.509 IQR)
- **Top Global Matches:** file_cluster_8: 13.509, file_cluster_13: 13.536, file_cluster_7: 13.544
- **Magnitude:** 2059.72 | **LOC:** 2736 | **CtrlFlow:** 41.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (45.6722%), Tech Debt (9.2964%)
**Top Internal Functions/Classes:**
  * `getShippingAddressesItems` (Impact: 99.0 | O(N^6) | DB: 9)
  * `updateItem` (Impact: 93.7 | O(N^6) | DB: 10)
  * `assignCustomerWithAddressChange` (Impact: 86.2 | O(N^5) | DB: 7)
  * `getItemVirtualQty` (Impact: 68.0 | O(N^6) | DB: 5)
  * `beforeSave` (Impact: 64.6 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 208`, `structural_boundaries: 294`, `args: 105`, `func_start: 105`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 373`, `dead_code: 1`, `planned_debt: 4`
* *Architecture:* `api: 163`, `import: 15`
* *Defense:* `safety: 22`, `doc: 451`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.658
  * `Choke Point (Betweenness):` 2.5e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` Magento\Framework\DataObject, Magento\Catalog\Model\Product\Attribute\Source\Status, Magento\Directory\Model\AllowedCountries, Magento\Framework\App\ObjectManager, Magento\Quote\Api\Data\PaymentInterface, Magento\Customer\Api\Data\GroupInterface, \Magento\Store\Model\ScopeInterface::SCOPE_STORE, Discount ?
                        $item->getBaseRowTotal() - $item->getBaseDiscountAmount() + $taxes :
                        $item->getBaseRowTotal() + $taxes...
  * `Imported By (In-Degree: 132):` (Excluded from Brief to save tokens)

### `app/code/Magento/Fedex/Model/Carrier.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.719 IQR)
- **Top Global Matches:** file_cluster_8: 13.719, file_cluster_13: 13.839, file_cluster_7: 13.883
- **Magnitude:** 2046.22 | **LOC:** 1884 | **CtrlFlow:** 56.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (35.8098%), Tech Debt (8.7603%)
**Top Internal Functions/Classes:**
  * `processTrackingDetails` (Impact: 149.6 | O(N^6) | DB: 12)
  * `getContainerTypes` (Impact: 139.1 | O(N^6) | DB: 19)
  * `_formShipmentRequest` (Impact: 121.0 | O(N^6) | DB: 24)
  * `setRequest` (Impact: 94.2 | O(N^5) | DB: 10)
  * `_prepareRateResponse` (Impact: 75.4 | O(N^6) | DB: 13)
    * *Intent:* /** * Forming request for rate estimation depending to the purpose * * @param string $purpose * @ret...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 197`, `structural_boundaries: 152`, `args: 45`, `func_start: 45`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 572`, `fragile_debt: 1`
* *Architecture:* `api: 35`, `import: 15`
* *Defense:* `safety: 57`, `doc: 207`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.054
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` Magento\Framework\DataObject, Magento\Framework\Measure\Length, 'USE_SCHEDULED_PICKUP' => __('Use Scheduled Pickup'), 'KG' => __('Kilograms'), 'TAG' => __('Tag'), Magento\Sales\Model\Order, Magento\Framework\App\ObjectManager, Magento\Framework\App\CacheInterface...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `app/code/Magento/Paypal/Model/Config.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.439 IQR)
- **Top Global Matches:** file_cluster_8: 12.439, file_cluster_7: 12.555, file_cluster_13: 12.828
- **Magnitude:** 2029.72 | **LOC:** 1872 | **CtrlFlow:** 59.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (15.8789%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `isMethodAvailable` (Impact: 297.4 | O(2^N) | DB: 8)
  * `_getSpecificConfigPath` (Impact: 137.3 | O(N^5) | DB: 12)
    * *Intent:* /** * Return supported types for PayPal logo
  * `_mapWpukFieldset` (Impact: 83.8 | O(N^4) | DB: 9)
    * *Intent:* /**
  * `_mapExpressFieldset` (Impact: 83.5 | O(N^4))
    * *Intent:* /** * Express Checkout button "flavors" source getter * * @return array
  * `__construct` (Impact: 72.0 | O(2^N) | DB: 11)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 230`, `structural_boundaries: 159`, `args: 61`, `func_start: 61`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 310`
* *Architecture:* `api: 130`, `import: 4`
* *Defense:* `safety: 1`, `doc: 230`, `immutability_locks: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.49
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` _BILLING_ADDRESS_ALL = 1, customer to do after placing the order.
     *
     * For instance, Formatter, Magento\Csp\Helper\CspNonceProvider, 
    public const REQUIRE_BILLING_ADDRESS_NO = 0, $fieldName", Magento\Framework\App\ObjectManager, _BILLING_ADDRESS_VIRTUAL = 2...
  * `Imported By (In-Degree: 41):` (Excluded from Brief to save tokens)

### `app/code/Magento/ConfigurableProduct/Model/Product/Type/Configurable.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.063 IQR)
- **Top Global Matches:** file_cluster_13: 14.063, file_cluster_8: 14.157, file_cluster_7: 14.223
- **Magnitude:** 2009.22 | **LOC:** 1688 | **CtrlFlow:** 48.2% | **Authorship Centralization:** 80.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (37.5924%), Tech Debt (8.6647%)
**Top Internal Functions/Classes:**
  * `_prepareProduct` (Impact: 382.2 | O(2^N) | DB: 16)
  * `__construct` (Impact: 268.1 | O(2^N) | DB: 22)
    * *Intent:* /** * Product is configurable *
  * `save` (Impact: 209.7 | O(2^N) | DB: 8)
  * `beforeSave` (Impact: 147.8 | O(2^N) | DB: 5)
  * `checkProductBuyState` (Impact: 73.7 | O(2^N) | DB: 6)
    * *Intent:* /** * Save configurable product attributes * * @param ProductInterface $product
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 141`, `args: 41`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 354`, `planned_debt: 1`
* *Architecture:* `api: 50`, `import: 15`
* *Defense:* `safety: 23`, `doc: 236`, `immutability_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.768
  * `Choke Point (Betweenness):` 3.9e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` Magento\Framework\Api\SearchCriteriaBuilder, Magento\Catalog\Api\ProductRepositoryInterface, $required, dAttributeIds) 
            $this->searchCriteriaBuilder->addFilter('attribute_id', dAttributes = [
            'name', Magento\Catalog\Api\ProductAttributeRepositoryInterface, Magento\Framework\App\ObjectManager, Magento\Framework\File\UploaderFactory...
  * `Imported By (In-Degree: 93):` (Excluded from Brief to save tokens)

### `app/code/Magento/Swatches/view/base/web/js/swatch-renderer.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.706 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.578 IQR)
- **Top Global Matches:** file_cluster_17: 13.706, file_cluster_8: 13.713, file_cluster_15: 13.755
- **Magnitude:** 1981.96 | **LOC:** 1508 | **CtrlFlow:** 57.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 168
- **Risk Profile:** Cognitive Load (37.5688%), Tech Debt (9.2364%)
**Top Internal Functions/Classes:**
  * `define` (Impact: 1615.0 | O(N^6) | DB: 168)
    * *Intent:* /** * Copyright 2015 Adobe
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 81`, `args: 70`, `func_start: 44`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 346`, `orphaned_logic: 1`
* *Architecture:* `concurrency: 7`
* *Defense:* `safety: 23`, `doc: 84`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/code/Magento/Eav/Model/Entity/Collection/AbstractCollection.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.316 IQR)
- **Top Global Matches:** file_cluster_13: 14.316, file_cluster_8: 14.342, file_cluster_7: 14.42
- **Magnitude:** 1881.86 | **LOC:** 1789 | **CtrlFlow:** 55.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (40.3583%), Tech Debt (9.7841%)
**Top Internal Functions/Classes:**
  * `joinAttribute` (Impact: 149.2 | O(N^4) | DB: 15)
  * `addAttributeToSelect` (Impact: 147.2 | O(2^N) | DB: 6)
    * *Intent:* /** * Initialize collection *
  * `_loadAttributes` (Impact: 131.0 | O(N^6) | DB: 20)
    * *Intent:* * Developer is encouraged to use existing instances of attributes and entities * After first use of ...
  * `joinField` (Impact: 129.5 | O(N^5) | DB: 13)
  * `joinTable` (Impact: 127.8 | O(N^5) | DB: 15)
    * *Intent:* /** * Add attribute to sort order
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 180`, `structural_boundaries: 145`, `args: 41`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 416`, `dead_code: 1`, `planned_debt: 3`
* *Architecture:* `io: 4`, `api: 56`, `import: 4`
* *Defense:* `safety: 61`, `doc: 170`, `test: 1`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.298
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Magento\Framework\DB\Select, Magento\Framework\App\ResourceConnection\SourceProviderInterface, Magento\Framework\Data\Collection\AbstractDb, Magento\Framework\Exception\LocalizedException
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `app/code/Magento/ProductVideo/view/adminhtml/web/js/new-video-dialog.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.856 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.999 IQR)
- **Top Global Matches:** file_cluster_17: 13.856, file_cluster_8: 13.988, file_cluster_15: 14.045
- **Magnitude:** 1862.08 | **LOC:** 1352 | **CtrlFlow:** 57.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 311
- **Risk Profile:** Cognitive Load (34.6149%), Tech Debt (8.8415%)
**Top Internal Functions/Classes:**
  * `define` (Impact: 1254.1 | O(N^6) | DB: 311)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 75`, `args: 76`, `func_start: 57`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 590`, `orphaned_logic: 1`
* *Architecture:* `io: 1`
* *Defense:* `safety: 22`, `doc: 98`, `immutability_locks: 6`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/code/Magento/Customer/Model/AccountManagement.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.885 IQR)
- **Top Global Matches:** file_cluster_13: 13.885, file_cluster_8: 14.158, file_cluster_7: 14.203
- **Magnitude:** 1796.36 | **LOC:** 1702 | **CtrlFlow:** 39.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 57
- **Risk Profile:** Cognitive Load (35.6164%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__construct` (Impact: 450.4 | O(N^3) | DB: 57)
    * *Intent:* /** * @var ManagerInterface */
  * `createAccountWithPasswordHash` (Impact: 124.8 | O(N^5) | DB: 19)
  * `initiatePasswordReset` (Impact: 67.7 | O(N^5) | DB: 5)
    * *Intent:* /**
  * `validateResetPasswordToken` (Impact: 48.0 | O(N^5) | DB: 4)
  * `checkPasswordStrength` (Impact: 43.5 | O(N^5) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 244`, `args: 49`, `func_start: 48`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 103`, `state_mutation: 435`
* *Architecture:* `api: 66`, `import: 52`
* *Defense:* `safety: 56`, `doc: 332`, `test: 1`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.141
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 26):` Magento\Framework\Api\SearchCriteriaBuilder, Magento\Framework\Exception\State\InvalidTransitionException, Magento\Framework\Exception\InputException, Magento\Customer\Api\AccountManagementInterface, Magento\Framework\Exception\State\InputMismatchException, Magento\Framework\Stdlib\StringUtils, Magento\Directory\Model\AllowedCountries, Magento\Framework\Event\ManagerInterface...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `app/code/Magento/CatalogImportExport/Model/Export/Product.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.482 IQR)
- **Top Global Matches:** file_cluster_8: 13.482, file_cluster_7: 13.641, file_cluster_13: 13.669
- **Magnitude:** 1780.16 | **LOC:** 2366 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (35.6247%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `filterAttributeCollection` (Impact: 141.4 | O(2^N) | DB: 5)
  * `__construct` (Impact: 117.0 | O(2^N) | DB: 21)
    * *Intent:* /** * Provider of product link types * * @var \Magento\Catalog\Model\Product\LinkTypeProvider */
  * `getCustomOptionsData` (Impact: 88.1 | O(N^6) | DB: 13)
  * `export` (Impact: 87.5 | O(2^N) | DB: 25)
  * `_prepareEntityCollection` (Impact: 61.0 | O(2^N) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 153`, `structural_boundaries: 153`, `args: 45`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 524`
* *Architecture:* `api: 13`, `import: 12`
* *Defense:* `safety: 27`, `doc: 227`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.04
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` Magento\CatalogImportExport\Model\Import\Product\CategoryProcessor, $optionData, Magento\Eav\Model\Entity\Attribute\ScopedAttributeInterface, Magento\Catalog\Model\Product, Magento\ImportExport\Model\Export\Adapter\AbstractAdapter, Magento\ImportExport\Model\Import, Magento\Framework\App\ObjectManager, Magento\Eav\Model\Entity\Collection\AbstractCollection...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/code/Magento/Catalog/Model/Product.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.13 IQR)
- **Top Global Matches:** file_cluster_8: 13.13, file_cluster_7: 13.141, file_cluster_13: 13.202
- **Magnitude:** 1769.54 | **LOC:** 2859 | **CtrlFlow:** 28.2% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 38
- **Risk Profile:** Cognitive Load (38.6121%), Tech Debt (9.1008%)
**Top Internal Functions/Classes:**
  * `processBuyRequest` (Impact: 591.5 | O(2^N) | DB: 38)
    * *Intent:* /** * Check if data was changed * * @return bool
  * `getMediaGalleryImages` (Impact: 53.3 | O(N^5) | DB: 3)
    * *Intent:* /** * Get product attribute set id
  * `toArray` (Impact: 39.8 | O(2^N) | DB: 3)
  * `getFinalPrice` (Impact: 36.2 | O(2^N) | DB: 1)
    * *Intent:* * @param Product\Attribute\Source\Status $catalogProductStatus * @param Product\Media\Config $catalo...
  * `getPrice` (Impact: 28.1 | O(2^N))
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 288`, `args: 120`, `func_start: 118`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 286`, `planned_debt: 3`
* *Architecture:* `api: 161`, `import: 13`
* *Defense:* `safety: 13`, `doc: 447`, `immutability_locks: 4`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.002
  * `Choke Point (Betweenness):` 3.1e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` Magento\Catalog\Api\ProductLinkRepositoryInterface, Magento\Catalog\Api\Data\ProductInterface, Magento\Framework\Api\AttributeValueFactory, Magento\Catalog\Model\Product\Attribute\Source\Status, Magento\Framework\DataObject\IdentityInterface, d_options') === "1" && $this->isProductHasOptions(, d_options') === null) 
            $this->setRequiredOptions(false, Magento\Framework\App\ObjectManager...
  * `Imported By (In-Degree: 404):` (Excluded from Brief to save tokens)

### `app/code/Magento/Downloadable/view/adminhtml/templates/product/edit/downloadable/links.phtml` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.018 IQR)
- **Top Global Matches:** file_cluster_8: 11.018, file_cluster_2: 11.265, file_cluster_17: 11.483
- **Magnitude:** 1767.7 | **LOC:** 486 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 31
- **Risk Profile:** Cognitive Load (59.2235%), Tech Debt (10.313%)
**Top Internal Functions/Classes:**
  * `require` (Impact: 1690.8 | O(N^6) | DB: 31)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 218`, `structural_boundaries: 109`, `args: 22`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 68`, `orphaned_logic: 1`
* *Architecture:* `import: 1`
* *Defense:* `safety: 5`, `doc: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` [
    'jquery', template', translate'
], function(jQuery, tr>', div>' +
                <?php endif, 'prototype', "<?=  $block->escapeJs($block->escapeUrl($block->getUploadUrl('link_samples'))) ?>"...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/code/Magento/Quote/Model/Quote/Address.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.213 IQR)
- **Top Global Matches:** file_cluster_13: 13.213, file_cluster_8: 13.381, file_cluster_7: 13.415
- **Magnitude:** 1695.72 | **LOC:** 1826 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (42.3713%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__construct` (Impact: 253.8 | O(2^N) | DB: 27)
  * `requestShippingRates` (Impact: 166.9 | O(N^6) | DB: 16)
  * `addItem` (Impact: 98.7 | O(2^N) | DB: 4)
  * `getAllItems` (Impact: 93.3 | O(N^6) | DB: 9)
  * `getItemQty` (Impact: 34.5 | O(N^4) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 271`, `args: 97`, `func_start: 97`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 281`
* *Architecture:* `api: 152`, `import: 41`
* *Defense:* `safety: 8`, `doc: 371`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.008
  * `Choke Point (Betweenness):` 3e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 25):` Magento\Customer\Model\Address\CompositeValidator, Magento\Store\Api\Data\StoreInterface, Magento\Framework\Data\Collection\AbstractDb, Magento\Framework\App\ObjectManager, include_discount_amount', Magento\Directory\Helper\Data, Magento\Quote\Api\Data\AddressExtensionInterface, ScopeInterface::SCOPE_STORE...
  * `Imported By (In-Degree: 48):` (Excluded from Brief to save tokens)

### `app/code/Magento/Bundle/Model/Product/Type.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.496 IQR)
- **Top Global Matches:** file_cluster_13: 13.496, file_cluster_8: 13.512, file_cluster_7: 13.616
- **Magnitude:** 1679.46 | **LOC:** 1415 | **CtrlFlow:** 51.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 40
- **Risk Profile:** Cognitive Load (36.3956%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_prepareProduct` (Impact: 316.1 | O(2^N) | DB: 40)
  * `__construct` (Impact: 236.1 | O(2^N) | DB: 22)
    * *Intent:* /** * Catalog data helper *
  * `beforeSave` (Impact: 159.3 | O(2^N) | DB: 2)
  * `getOrderOptions` (Impact: 99.8 | O(2^N) | DB: 15)
  * `getSku` (Impact: 98.3 | O(2^N) | DB: 8)
    * *Intent:* /** * @param \Magento\Catalog\Model\Product\Option $catalogProductOption * @param \Magento\Eav\Model...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 96`, `args: 25`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 298`
* *Architecture:* `api: 26`, `import: 12`
* *Defense:* `safety: 15`, `doc: 171`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.378
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` Magento\Catalog\Api\ProductRepositoryInterface, $required = true)
    
        return $this->_bundleSelection->getChildrenIds($parentId, Magento\Framework\Stdlib\ArrayUtils, $required, Magento\Framework\App\ObjectManager, $options)
    
        if (!$product->getSkipCheckRequiredOption() && $isStrictProcessMode) 
            foreach ($optionsCollection->getItems(), Magento\Framework\File\UploaderFactory, 
    public function getParentIdsByChild($childId)
    
        return $this->_bundleSelection->getParentIdsByChild($childId...
  * `Imported By (In-Degree: 30):` (Excluded from Brief to save tokens)

### `app/code/Magento/Sales/Model/Order/Item.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.113 IQR)
- **Top Global Matches:** file_cluster_8: 12.113, file_cluster_7: 12.18, file_cluster_13: 12.474
- **Magnitude:** 1661.7 | **LOC:** 2421 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (18.3418%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `isDummy` (Impact: 108.1 | O(N^4) | DB: 1)
    * *Intent:* /** * Retrieve order item statuses array *
  * `getStatusId` (Impact: 74.9 | O(N^3) | DB: 13)
  * `__construct` (Impact: 70.7 | O(2^N) | DB: 8)
    * *Intent:* /**
  * `getForceApplyDiscountToParentItem` (Impact: 21.3 | O(2^N) | DB: 2)
  * `isChildrenCalculated` (Impact: 18.2 | O(N^3) | DB: 3)
    * *Intent:* /** * Retrieve status *
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 479`, `args: 222`, `func_start: 222`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 182`
* *Architecture:* `api: 412`, `import: 3`
* *Defense:* `safety: 8`, `doc: 392`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.46
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Magento\Sales\Api\Data\OrderItemInterface, Magento\Framework\Api\AttributeValueFactory, Magento\Sales\Model\AbstractModel
  * `Imported By (In-Degree: 49):` (Excluded from Brief to save tokens)

### `app/code/Magento/Eav/Setup/EavSetup.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.039 IQR)
- **Top Global Matches:** file_cluster_8: 13.039, file_cluster_7: 13.152, file_cluster_13: 13.183
- **Magnitude:** 1660.3 | **LOC:** 1532 | **CtrlFlow:** 44.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (17.85%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `installEntities` (Impact: 143.2 | O(N^6) | DB: 8)
  * `_updateAttributeAdditionalData` (Impact: 80.9 | O(N^6) | DB: 9)
  * `addAttribute` (Impact: 79.8 | O(N^6) | DB: 7)
    * *Intent:* /** * Get number of all attributes in group * * @param int|string $entityTypeId * @param int|string ...
  * `_updateAttribute` (Impact: 79.6 | O(N^6) | DB: 7)
  * `__construct` (Impact: 70.7 | O(N^3) | DB: 14)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 155`, `structural_boundaries: 192`, `args: 49`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 179`, `state_mutation: 425`
* *Architecture:* `api: 54`, `import: 13`
* *Defense:* `safety: 39`, `doc: 262`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.485
  * `Choke Point (Betweenness):` 1.4e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` Magento\Eav\Model\Entity\Setup\PropertyMapperInterface, Magento\Eav\Model\Config, Magento\Eav\Model\ReservedAttributeCheckerInterface, Magento\Eav\Model\AttributeFactory, Magento\Framework\App\CacheInterface, Magento\Framework\App\ObjectManager, Magento\Eav\Model\Entity\Attribute, Magento\Framework\Setup\ModuleDataSetupInterface...
  * `Imported By (In-Degree: 32):` (Excluded from Brief to save tokens)

### `app/code/Magento/CatalogImportExport/Model/Import/Product.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.072 IQR)
- **Top Global Matches:** file_cluster_13: 14.072, file_cluster_8: 14.229, file_cluster_7: 14.283
- **Magnitude:** 1655.6 | **LOC:** 3680 | **CtrlFlow:** 45.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (36.2661%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `formatStockDataForRow` (Impact: 93.5 | O(N^6) | DB: 7)
  * `validateRow` (Impact: 68.3 | O(N^6) | DB: 7)
  * `_saveStockItem` (Impact: 62.8 | O(N^6) | DB: 12)
  * `saveProductEntityPhase` (Impact: 58.0 | O(N^6) | DB: 7)
    * *Intent:* /**
  * `_deleteProducts` (Impact: 57.0 | O(N^6) | DB: 5)
    * *Intent:* /** * @var Product\SkuProcessor */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 178`, `structural_boundaries: 212`, `args: 60`, `func_start: 60`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 515`, `dead_code: 1`
* *Architecture:* `api: 67`, `import: 33`
* *Defense:* `safety: 48`, `doc: 370`, `test: 1`, `immutability_locks: 30`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.213
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` Magento\Catalog\Api\ProductRepositoryInterface, ValidatorInterface::ERROR_MEDIA_URL_NOT_ACCESSIBLE => 'Imported resource (image: %s) at row %s could not be downloaded from external resource due to timeout or access permissions', 'invalidNewToDateValue' => 'Make sure new_to_date is later than or the same, Magento\Framework\Model\ResourceModel\Db\ObjectRelationProcessor, Magento\CatalogImportExport\Model\Import\Product\RowValidatorInterface, Magento\Framework\App\ObjectManager, d', Magento\CatalogImportExport\Model\Import\Product\MediaGalleryProcessor...
  * `Imported By (In-Degree: 23):` (Excluded from Brief to save tokens)

### `app/code/Magento/Eav/Model/Entity/Attribute/AbstractAttribute.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.987 IQR)
- **Top Global Matches:** file_cluster_8: 12.987, file_cluster_7: 13.066, file_cluster_13: 13.18
- **Magnitude:** 1648.84 | **LOC:** 1464 | **CtrlFlow:** 42.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (45.2361%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getFlatIndexes` (Impact: 233.6 | O(2^N) | DB: 8)
  * `_getFlatColumnsDdlDefinition` (Impact: 138.9 | O(N^5) | DB: 5)
  * `_getFlatColumnsOldDefinition` (Impact: 138.5 | O(N^5) | DB: 3)
  * `__construct` (Impact: 120.8 | O(2^N) | DB: 15)
  * `getFlatUpdateSelect` (Impact: 56.9 | O(2^N) | DB: 2)
    * *Intent:* /** * Check if attribute in specified set * * @param int|int[] $setId * @return bool */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 141`, `structural_boundaries: 195`, `args: 78`, `func_start: 78`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 242`
* *Architecture:* `api: 118`, `import: 4`
* *Defense:* `safety: 24`, `doc: 234`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.27
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Magento\Framework\Serialize\Serializer\Json, Magento\Framework\Api\AttributeValueFactory, Magento\Framework\ObjectManager\ResetAfterRequestInterface, Magento\Framework\Exception\LocalizedException
  * `Imported By (In-Degree: 57):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/edit/options/option.phtml` (PHP) | Magnitude: 32.48 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 104, branch: 79, structural_boundaries: 21, decorators: 20
- `app/code/Magento/Ui/view/adminhtml/web/templates/modal/modal-prompt-content.html` (HTML) | Magnitude: 17.28 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 12, ssr_boundaries: 7, args: 5, decorators: 5
- `app/code/Magento/Ui/view/base/web/templates/modal/modal-prompt-content.html` (HTML) | Magnitude: 17.28 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 12, ssr_boundaries: 7, args: 5, decorators: 5
- `app/code/Magento/Security/view/base/web/js/escaper.js` (JAVASCRIPT) | Magnitude: 162.72 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 144, state_mutation: 36, branch: 19, doc: 18
- `app/code/Magento/Widget/Model/NamespaceResolver.php` (PHP) | Magnitude: 110.18 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 44, state_mutation: 35, structural_boundaries: 17, doc: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `app/code/Magento/PageCache/Model/Cache/Type.php` (PHP) | Magnitude: 18.32 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, doc: 13, structural_boundaries: 7, api: 4
- `app/code/Magento/Quote/Model/ResourceModel/Quote/Address/Collection.php` (PHP) | Magnitude: 19.3 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 20, doc: 13, structural_boundaries: 10, encapsulation: 4
- `app/code/Magento/Reports/Model/ResourceModel/Event/Collection.php` (PHP) | Magnitude: 79.44 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 37, doc: 17, branch: 10, structural_boundaries: 10
- `app/code/Magento/Translation/Model/Inline/CacheManager.php` (PHP) | Magnitude: 14.44 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 22, doc: 17, structural_boundaries: 5, state_mutation: 5
- `app/code/Magento/Catalog/view/adminhtml/web/catalog/type-events.js` (JAVASCRIPT) | Magnitude: 24.4 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 27, state_mutation: 13, doc: 8, args: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `app/code/Magento/Catalog/Model/Product/Option/Value.php` (PHP) | Magnitude: 296.76 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 191, doc: 102, structural_boundaries: 73, api: 58
- `app/code/Magento/CatalogImportExport/Model/Export/RowCustomizer/Composite.php` (PHP) | Magnitude: 81.22 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 39, doc: 24, structural_boundaries: 17, state_mutation: 12
- `app/code/Magento/Tax/Model/Api/SearchCriteria/JoinProcessor/CalculationData.php` (PHP) | Magnitude: 11.1 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 8, doc: 6, branch: 2
- `app/code/Magento/User/ViewModel/JsonSerializer.php` (PHP) | Magnitude: 12.72 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 8, doc: 8, args: 2
- `app/code/Magento/Wishlist/Block/AbstractBlock.php` (PHP) | Magnitude: 245.0 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 146, doc: 85, structural_boundaries: 59, state_mutation: 43

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `app/code/Magento/Ui/view/base/web/js/grid/controls/bookmarks/bookmarks.js` (JAVASCRIPT) | Magnitude: 273.42 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 128, state_mutation: 78, doc: 39, structural_boundaries: 17
- `app/code/Magento/Ui/view/base/web/js/form/element/single-checkbox.js` (JAVASCRIPT) | Magnitude: 809.92 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 281, indent_spaces: 153, branch: 64, safety: 23
- `app/code/Magento/Ui/view/base/web/js/modal/modal.js` (JAVASCRIPT) | Magnitude: 1083.04 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 420, indent_spaces: 289, branch: 42, doc: 42
- `app/code/Magento/LoginAsCustomerAssistance/view/frontend/web/js/opt-in.js` (JAVASCRIPT) | Magnitude: 17.24 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 9, state_mutation: 6, args: 3, closures: 3
- `app/code/Magento/Ui/view/base/web/js/form/element/checkbox-set.js` (JAVASCRIPT) | Magnitude: 192.78 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 106, indent_spaces: 76, structural_boundaries: 21, doc: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `app/code/Magento/Swatches/view/base/web/js/swatch-renderer.js` (JAVASCRIPT) | Magnitude: 1981.96 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 695, state_mutation: 346, branch: 111, doc: 84
- `app/code/Magento/GroupedProduct/view/adminhtml/web/js/grouped-product-grid.js` (JAVASCRIPT) | Magnitude: 357.12 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 118, state_mutation: 115, doc: 31, bitwise_ops: 30
- `app/code/Magento/MediaStorage/Model/File/Validator/AvailablePath.php` (PHP) | Magnitude: 257.44 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 60, indent_spaces: 55, branch: 32, safety: 7
- `app/code/Magento/Catalog/view/adminhtml/web/js/product-gallery.js` (JAVASCRIPT) | Magnitude: 1054.2 | Delta: **0.077 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 547, state_mutation: 330, doc: 60, branch: 57
- `app/code/Magento/Customer/view/adminhtml/web/js/form/element/region.js` (JAVASCRIPT) | Magnitude: 54.16 | Delta: **0.095 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 21, indent_spaces: 20, branch: 5, args: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `app/code/Magento/Newsletter/Block/Adminhtml/Problem/Grid/Renderer/Checkbox.php` (PHP) | Magnitude: 4.38 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 6, doc: 5, indent_spaces: 4, branch: 1
- `dev/tests/integration/testsuite/Magento/Cms/_files/blocks_for_different_stores.php` (PHP) | Magnitude: 47.12 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 36, state_mutation: 31, doc: 13, structural_boundaries: 9
- `app/code/Magento/ConfigurableProduct/view/adminhtml/templates/catalog/product/attribute/set/js.phtml` (PHP) | Magnitude: 24.3 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 9, branch: 7, doc: 5, indent_spaces: 5
- `app/code/Magento/Ui/view/base/web/templates/grid/toolbar.html` (HTML) | Magnitude: 15.36 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 9, decorators: 8, ui_framework: 5
- `app/code/Magento/Review/view/adminhtml/templates/rating/stars/summary.phtml` (PHP) | Magnitude: 15.28 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 14, indent_spaces: 9, doc: 4, structural_boundaries: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `app/code/Magento/Ui/view/base/web/js/grid/editing/editor-view.js` (JAVASCRIPT) | Magnitude: 160.64 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 104, state_mutation: 28, doc: 23, concurrency: 19
- `app/code/Magento/Ui/view/base/web/js/grid/url-filter-applier.js` (JAVASCRIPT) | Magnitude: 129.76 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 65, state_mutation: 38, concurrency: 12, structural_boundaries: 8
- `app/code/Magento/Catalog/view/adminhtml/web/component/static-type-input.js` (JAVASCRIPT) | Magnitude: 47.26 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 25, state_mutation: 22, doc: 7, concurrency: 6
- `app/code/Magento/MediaGalleryRenditions/Model/Queue/FetchRenditionPathsBatches.php` (PHP) | Magnitude: 113.2 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 52, state_mutation: 24, doc: 24, structural_boundaries: 13
- `dev/tools/grunt/tasks/mage-minify.js` (JAVASCRIPT) | Magnitude: 0.04 | Delta: **0.072 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 27, state_mutation: 9, doc: 6, concurrency: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `app/code/Magento/Store/Model/StoreSwitcher/RedirectDataSerializerInterface.php` (PHP) | Magnitude: 40.8 | Delta: **0.128 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 8, structural_boundaries: 5, args: 2, func_start: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `app/code/Magento/Paypal/Controller/Express/AbstractExpress/Cancel.php` (PHP) | Magnitude: 57.22 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 30, branch: 9, state_mutation: 7, doc: 7
- `dev/tests/static/testsuite/Magento/Framework/Validator/RegexFactory.php` (PHP) | Magnitude: 7.08 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 5, doc: 4, indent_spaces: 4, api: 2
- `app/code/Magento/Config/view/adminhtml/templates/system/config/js.phtml` (PHP) | Magnitude: 31.2 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: state_mutation: 16, branch: 6, doc: 4, planned_debt: 3
- `app/code/Magento/Backend/view/adminhtml/templates/system/shipping/applicable_country.phtml` (PHP) | Magnitude: 15.6 | Delta: **0.264 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: branch: 6, state_mutation: 3, doc: 3, dead_code: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `app/code/Magento/Catalog/Api/Data/ProductRenderInterface.php` (PHP) | Magnitude: 141.68 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 62, structural_boundaries: 30, indent_spaces: 26, args: 24
- `app/code/Magento/Sales/Api/Data/InvoiceInterface.php` (PHP) | Magnitude: 364.34 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 238, indent_spaces: 140, structural_boundaries: 97, args: 94
- `setup/src/Magento/Setup/Module/Dependency/Report/Dependency/Data/Dependency.php` (PHP) | Magnitude: 40.3 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 25, doc: 18, state_mutation: 14, structural_boundaries: 11
- `app/code/Magento/Sales/Api/Data/CreditmemoInterface.php` (PHP) | Magnitude: 386.62 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 258, indent_spaces: 152, structural_boundaries: 105, args: 102
- `app/code/Magento/Cms/Api/BlockRepositoryInterface.php` (PHP) | Magnitude: 59.19 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 23, structural_boundaries: 7, args: 5, func_start: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `app/code/Magento/Cms/Setup/Patch/Data/UpdatePrivacyPolicyPage.php` (PHP) | Magnitude: 37.3 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 17, doc: 12, args: 6
- `app/code/Magento/Customer/Controller/Adminhtml/Index/NewAction.php` (PHP) | Magnitude: 5.14 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 6, doc: 3, branch: 1
- `app/code/Magento/Customer/Model/ResourceModel/Group/Resolver.php` (PHP) | Magnitude: 46.62 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 24, state_mutation: 17, doc: 9, structural_boundaries: 7
- `app/code/Magento/Sales/Controller/Adminhtml/Order/Index.php` (PHP) | Magnitude: 5.14 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 6, doc: 3, branch: 1
- `app/code/Magento/Search/Block/Adminhtml/Synonyms/Edit/GenericButton.php` (PHP) | Magnitude: 24.18 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 18, doc: 14, structural_boundaries: 8, state_mutation: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `dev/tests/integration/testsuite/Magento/Tax/_files/tax_rule_region_1_al.php` (PHP) | Magnitude: 25.5 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 12, state_mutation: 10, doc: 5, structural_boundaries: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `app/code/Magento/Ups/Model/Carrier.php` -> **Rajesh Kumar** (100.0% isolated ownership) | Magnitude: 4171.72
- `app/code/Magento/CatalogImportExport/Model/Import/Product/Option.php` -> **Rajesh Kumar** (100.0% isolated ownership) | Magnitude: 2966.14
- `app/code/Magento/Sales/Model/Order.php` -> **Rajesh Kumar** (100.0% isolated ownership) | Magnitude: 2866.66
- `app/code/Magento/Catalog/Model/ResourceModel/Product/Collection.php` -> **Rajesh Kumar** (100.0% isolated ownership) | Magnitude: 2728.28
- `app/code/Magento/Usps/Model/Carrier.php` -> **Bhavin Parmar** (100.0% isolated ownership) | Magnitude: 2317.12

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `app/code/Magento/Catalog/Model/ResourceModel/Product/Collection.php` -> **Severity: 0.022** (Bridge: 0.0002 * Flux: 100.0%)
- `app/code/Magento/Catalog/Model/ResourceModel/Category.php` -> **Severity: 0.013** (Bridge: 0.0001 * Flux: 99.9999%)
- `app/code/Magento/CatalogGraphQl/DataProvider/Product/SearchCriteriaBuilder.php` -> **Severity: 0.008** (Bridge: 0.0001 * Flux: 99.9999%)
- `app/code/Magento/Store/Model/Store.php` -> **Severity: 0.008** (Bridge: 0.0001 * Flux: 85.0%)
- `app/code/Magento/CatalogRule/Model/Rule.php` -> **Severity: 0.006** (Bridge: 0.0001 * Flux: 99.9999%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `app/code/Magento/Catalog/Api/Data/ProductInterface.php` -> **Severity: 495.427** (Blast Radius: 4.957 * Doc Risk: 99.9449%)
- `app/code/Magento/GraphQl/Model/Query/Logger/LoggerInterface.php` -> **Severity: 325.5** (Blast Radius: 3.255 * Doc Risk: 100.0%)
- `app/code/Magento/Store/Model/Store.php` -> **Severity: 253.038** (Blast Radius: 3.742 * Doc Risk: 67.621%)
- `setup/src/Magento/Setup/Module/I18n/Dictionary/Phrase.php` -> **Severity: 192.213** (Blast Radius: 2.063 * Doc Risk: 93.1718%)
- `app/code/Magento/Catalog/Model/Product/Attribute/Source/Status.php` -> **Severity: 175.5** (Blast Radius: 1.755 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
