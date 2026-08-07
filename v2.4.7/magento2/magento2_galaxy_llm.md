# ARCHITECTURAL_BRIEF: magento2
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_php/magento2` |
| **Timestamp** | `2026-08-07T03:54:17.882237+00:00` |
| **Scan Duration** | `49.15s` |
| **Git Branch** | `2.4-develop` |
| **Git Commit** | `8d95ae6ee2a7dc1960f8f853af011fbabec2e0f0` |
| **Git Remote** | `https://github.com/magento/magento2.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 15236 malicious artifacts.

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
> **Architectural Drift Z-Score:** `5.521`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 11008 | 56.6% |
| file_cluster_13 | 6721 | 34.5% |
| file_cluster_2 | 761 | 3.9% |
| file_cluster_7 | 138 | 0.7% |
| file_cluster_0 | 49 | 0.3% |
| file_cluster_15 | 45 | 0.2% |
| file_cluster_1 | 43 | 0.2% |
| file_cluster_17 | 14 | 0.1% |
| file_cluster_4 | 13 | 0.1% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 16.7 | 9.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 43.9 | 59.4 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 29.8 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 5.7 | 2.3 | 0.0 |
| API Exposure | 0.0 | 15.1 | 2.3 | 1.5 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 0.4 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 46.4 | 23.7 | 0.0 |
| Commented Logic Exposure | 0.0 | 64.6 | 0.1 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 78.6 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 24.9 | 0.1 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 12.2 | 11.9 | 11.9 |
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

- `define` (@ `app/code/Magento/Shipping/view/adminhtml/web/order/packaging.js`) -> Impact: **303.5** | LOC: 908
  * *Intent:* /** * Copyright 2014 Adobe
- `initFromOrder` (@ `app/code/Magento/Sales/Model/AdminOrder/Create.php`) -> Impact: **292.8** | LOC: 736
- `require` (@ `app/code/Magento/Downloadable/view/adminhtml/templates/product/edit/downloadable/links.phtml`) -> Impact: **268.7** | LOC: 385
- `define` (@ `app/code/Magento/Ui/view/base/web/js/form/element/ui-select.js`) -> Impact: **256.7** | LOC: 942
  * *Intent:* /** * Copyright 2015 Adobe * All Rights Reserved.
- `define` (@ `app/code/Magento/Swatches/view/base/web/js/swatch-renderer.js`) -> Impact: **241.0** | LOC: 941
  * *Intent:* /** * Copyright 2015 Adobe
- `define` (@ `app/code/Magento/ProductVideo/view/adminhtml/web/js/new-video-dialog.js`) -> Impact: **236.9** | LOC: 1170
  * *Intent:* /**
- `__construct` (@ `app/code/Magento/Customer/Model/AccountManagement.php`) -> Impact: **227.4** | LOC: 89
  * *Intent:* /** * @var ManagerInterface */
- `getShippingOptions` (@ `app/code/Magento/Usps/Model/ShipmentService.php`) -> Impact: **209.9** | LOC: 478
- `__construct` (@ `app/code/Magento/CatalogRule/Model/Indexer/IndexBuilder.php`) -> Impact: **207.1** | LOC: 89
- `_init` (@ `app/code/Magento/Swatches/view/base/web/js/swatch-renderer.js`) -> Impact: **193.4** | LOC: 682

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `dev/tests/integration/testsuite/Magento/Catalog/_files` | 419 | 9971.68 | 19.77% | 0.0% |
| `app/code/Magento/Sales/Model/Order` | 46 | 7140.46 | 21.61% | 32.51% |
| `app/code/Magento/Sales/Api/Data` | 51 | 6693.77 | 4.56% | 0.0% |
| `app/code/Magento/Customer/Model` | 43 | 4865.96 | 24.7% | 13.69% |
| `dev/tests/integration/testsuite/Magento/Sales/_files` | 202 | 4844.2 | 15.93% | 0.0% |
| `app/code/Magento/Paypal/Model` | 25 | 4466.5 | 26.94% | 41.52% |
| `app/code/Magento/Catalog/Model` | 50 | 4223.0 | 21.03% | 36.33% |
| `app/code/Magento/Ui/view/base/web/js/form/element` | 23 | 3898.42 | 32.59% | 76.88% |
| `app/code/Magento/Sales/Model` | 29 | 3871.34 | 22.16% | 34.83% |
| `app/code/Magento/Quote/Model` | 38 | 3504.9 | 21.17% | 46.69% |

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
- `app/code/Magento/Paypal/view/adminhtml/web/js/rules.js` -> **31** Orphaned Functions | **10** Duplicates
- `app/code/Magento/Sales/Model/Order/ShippingTotal.php` -> **38** Orphaned Functions | **0** Duplicates
- `app/code/Magento/Tax/Model/TaxDetails/ItemDetails.php` -> **28** Orphaned Functions | **0** Duplicates

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
47. **`dev/tests/integration/testsuite/Magento/Widget/Model/Config/_files/expectedGlobalArray.php`** -> AI Confidence: **99.48%**
48. **`dev/tests/integration/testsuite/Magento/Widget/Model/Config/_files/expectedGlobalDesignArray.php`** -> AI Confidence: **99.48%**
49. **`app/code/Magento/Bundle/view/adminhtml/templates/product/edit/bundle/option.phtml`** -> AI Confidence: **99.39%**
50. **`app/code/Magento/Bundle/view/adminhtml/templates/product/edit/bundle/option/selection.phtml`** -> AI Confidence: **99.39%**
51. **`app/code/Magento/Customer/view/frontend/templates/form/edit.phtml`** -> AI Confidence: **99.39%**
52. **`app/code/Magento/Sales/view/adminhtml/templates/order/creditmemo/create/items.phtml`** -> AI Confidence: **99.39%**
53. **`app/code/Magento/Shipping/view/adminhtml/templates/order/packaging/popup_content.phtml`** -> AI Confidence: **99.39%**
54. **`app/code/Magento/Shipping/view/adminhtml/templates/order/tracking/view.phtml`** -> AI Confidence: **99.39%**
55. **`dev/tests/integration/testsuite/Magento/Bundle/_files/bundle_product_two_dropdown_options.php`** -> AI Confidence: **99.39%**
56. **`dev/tests/integration/testsuite/Magento/Bundle/_files/product.php`** -> AI Confidence: **99.39%**
57. **`dev/tests/integration/testsuite/Magento/Bundle/_files/product_1.php`** -> AI Confidence: **99.39%**
58. **`dev/tests/integration/testsuite/Magento/Bundle/_files/product_with_multiple_options.php`** -> AI Confidence: **99.39%**
59. **`dev/tests/integration/testsuite/Magento/Bundle/_files/product_with_multiple_options_and_custom_quantity.php`** -> AI Confidence: **99.39%**
60. **`dev/tests/integration/testsuite/Magento/Bundle/_files/issaleable_product.php`** -> AI Confidence: **99.35%**
61. **`dev/tests/integration/testsuite/Magento/Bundle/_files/product_with_multiple_options_1.php`** -> AI Confidence: **99.35%**
62. **`app/code/Magento/Backend/view/adminhtml/templates/widget/form/container.phtml`** -> AI Confidence: **99.34%**
63. **`app/code/Magento/Backend/view/adminhtml/templates/widget/grid.phtml`** -> AI Confidence: **99.34%**
64. **`app/code/Magento/Backend/view/adminhtml/templates/widget/tabs.phtml`** -> AI Confidence: **99.34%**
65. **`app/code/Magento/Captcha/view/adminhtml/templates/default.phtml`** -> AI Confidence: **99.34%**
66. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/category/tree.phtml`** -> AI Confidence: **99.34%**
67. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/edit/options/option.phtml`** -> AI Confidence: **99.34%**
68. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/js.phtml`** -> AI Confidence: **99.34%**
69. **`app/code/Magento/CatalogWidget/view/adminhtml/templates/product/widget/conditions.phtml`** -> AI Confidence: **99.34%**
70. **`app/code/Magento/CatalogWidget/view/frontend/templates/product/widget/content/grid.phtml`** -> AI Confidence: **99.34%**
71. **`app/code/Magento/ConfigurableProduct/view/adminhtml/templates/catalog/product/attribute/set/js.phtml`** -> AI Confidence: **99.34%**
72. **`app/code/Magento/ConfigurableProduct/view/adminhtml/templates/catalog/product/composite/fieldset/configurable.phtml`** -> AI Confidence: **99.34%**
73. **`app/code/Magento/Customer/view/adminhtml/templates/tab/cart.phtml`** -> AI Confidence: **99.34%**
74. **`app/code/Magento/Customer/view/frontend/templates/widget/dob.phtml`** -> AI Confidence: **99.34%**
75. **`app/code/Magento/Customer/view/frontend/templates/widget/name.phtml`** -> AI Confidence: **99.34%**
76. **`app/code/Magento/Directory/view/adminhtml/templates/js/optional_zip_countries.phtml`** -> AI Confidence: **99.34%**
77. **`app/code/Magento/Downloadable/view/adminhtml/templates/product/composite/fieldset/downloadable.phtml`** -> AI Confidence: **99.34%**
78. **`app/code/Magento/Newsletter/view/adminhtml/templates/queue/edit.phtml`** -> AI Confidence: **99.34%**
79. **`app/code/Magento/Reports/view/adminhtml/templates/report/grid/container.phtml`** -> AI Confidence: **99.34%**
80. **`app/code/Magento/Review/view/adminhtml/templates/add.phtml`** -> AI Confidence: **99.34%**
81. **`app/code/Magento/Sales/view/adminhtml/templates/order/create/items/grid.phtml`** -> AI Confidence: **99.34%**
82. **`app/code/Magento/Sales/view/adminhtml/templates/order/create/js.phtml`** -> AI Confidence: **99.34%**
83. **`app/code/Magento/Sales/view/adminhtml/templates/order/creditmemo/create/totals/adjustments.phtml`** -> AI Confidence: **99.34%**
84. **`app/code/Magento/Shipping/view/adminhtml/templates/order/packaging/popup.phtml`** -> AI Confidence: **99.34%**
85. **`app/code/Magento/Swatches/view/frontend/templates/product/layered/renderer.phtml`** -> AI Confidence: **99.34%**
86. **`lib/web/mage/utils/main.js`** -> AI Confidence: **99.34%**
87. **`app/bootstrap.php`** -> AI Confidence: **99.32%**
88. **`app/code/Magento/Backend/view/adminhtml/templates/system/cache/edit.phtml`** -> AI Confidence: **99.32%**
89. **`app/code/Magento/Backend/view/adminhtml/templates/system/design/edit.phtml`** -> AI Confidence: **99.32%**
90. **`app/code/Magento/Backend/view/adminhtml/templates/widget/accordion.phtml`** -> AI Confidence: **99.32%**
91. **`app/code/Magento/Backend/view/adminhtml/templates/widget/grid/extended.phtml`** -> AI Confidence: **99.32%**
92. **`app/code/Magento/Backend/view/adminhtml/templates/widget/grid/massaction_extended.phtml`** -> AI Confidence: **99.32%**
93. **`app/code/Magento/Bundle/view/adminhtml/templates/catalog/product/edit/tab/attributes/extend.phtml`** -> AI Confidence: **99.32%**
94. **`app/code/Magento/Bundle/view/adminhtml/templates/product/edit/bundle.phtml`** -> AI Confidence: **99.32%**
95. **`app/code/Magento/Bundle/view/adminhtml/templates/product/stock/disabler.phtml`** -> AI Confidence: **99.32%**
96. **`app/code/Magento/Bundle/view/adminhtml/templates/sales/creditmemo/create/items/renderer.phtml`** -> AI Confidence: **99.32%**
97. **`app/code/Magento/Bundle/view/adminhtml/templates/sales/creditmemo/view/items/renderer.phtml`** -> AI Confidence: **99.32%**
98. **`app/code/Magento/Bundle/view/adminhtml/templates/sales/invoice/create/items/renderer.phtml`** -> AI Confidence: **99.32%**
99. **`app/code/Magento/Bundle/view/adminhtml/templates/sales/invoice/view/items/renderer.phtml`** -> AI Confidence: **99.32%**
100. **`app/code/Magento/Bundle/view/adminhtml/templates/sales/order/view/items/renderer.phtml`** -> AI Confidence: **99.32%**
101. **`app/code/Magento/Bundle/view/adminhtml/templates/sales/shipment/create/items/renderer.phtml`** -> AI Confidence: **99.32%**
102. **`app/code/Magento/Bundle/view/adminhtml/templates/sales/shipment/view/items/renderer.phtml`** -> AI Confidence: **99.32%**
103. **`app/code/Magento/Bundle/view/frontend/templates/catalog/product/view/type/bundle/option/radio.phtml`** -> AI Confidence: **99.32%**
104. **`app/code/Magento/Captcha/view/frontend/templates/default.phtml`** -> AI Confidence: **99.32%**
105. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/attribute/set/toolbar/add.phtml`** -> AI Confidence: **99.32%**
106. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/helper/gallery.phtml`** -> AI Confidence: **99.32%**
107. **`app/code/Magento/Config/view/adminhtml/templates/system/config/form/field/array.phtml`** -> AI Confidence: **99.32%**
108. **`app/code/Magento/ConfigurableProduct/view/adminhtml/templates/product/configurable/stock/disabler.phtml`** -> AI Confidence: **99.32%**
109. **`app/code/Magento/CurrencySymbol/view/adminhtml/templates/system/currency/rate/matrix.phtml`** -> AI Confidence: **99.32%**
110. **`app/code/Magento/Downloadable/view/adminhtml/templates/sales/items/column/downloadable/creditmemo/name.phtml`** -> AI Confidence: **99.32%**
111. **`app/code/Magento/Downloadable/view/adminhtml/templates/sales/items/column/downloadable/invoice/name.phtml`** -> AI Confidence: **99.32%**
112. **`app/code/Magento/GiftMessage/view/adminhtml/templates/sales/order/create/giftoptions.phtml`** -> AI Confidence: **99.32%**
113. **`app/code/Magento/GiftMessage/view/adminhtml/templates/sales/order/view/giftoptions.phtml`** -> AI Confidence: **99.32%**
114. **`app/code/Magento/GiftMessage/view/frontend/templates/inline.phtml`** -> AI Confidence: **99.32%**
115. **`app/code/Magento/GroupedProduct/view/adminhtml/templates/product/stock/disabler.phtml`** -> AI Confidence: **99.32%**
116. **`app/code/Magento/ImportExport/view/adminhtml/templates/export/form/before.phtml`** -> AI Confidence: **99.32%**
117. **`app/code/Magento/ImportExport/view/adminhtml/templates/export/form/filter/after.phtml`** -> AI Confidence: **99.32%**
118. **`app/code/Magento/Newsletter/view/adminhtml/templates/problem/list.phtml`** -> AI Confidence: **99.32%**
119. **`app/code/Magento/Newsletter/view/adminhtml/templates/subscriber/list.phtml`** -> AI Confidence: **99.32%**
120. **`app/code/Magento/PageCache/view/adminhtml/templates/page_cache_validation.phtml`** -> AI Confidence: **99.32%**
121. **`app/code/Magento/Payment/view/adminhtml/templates/transparent/iframe.phtml`** -> AI Confidence: **99.32%**
122. **`app/code/Magento/Paypal/view/adminhtml/templates/system/config/rules.phtml`** -> AI Confidence: **99.32%**
123. **`app/code/Magento/Paypal/view/adminhtml/templates/transparent/iframe.phtml`** -> AI Confidence: **99.32%**
124. **`app/code/Magento/ProductVideo/view/adminhtml/templates/helper/gallery.phtml`** -> AI Confidence: **99.32%**
125. **`app/code/Magento/Sales/view/adminhtml/templates/order/create/totals/subtotal.phtml`** -> AI Confidence: **99.32%**
126. **`app/code/Magento/Shipping/view/frontend/templates/tracking/popup.phtml`** -> AI Confidence: **99.32%**
127. **`app/code/Magento/Swatches/view/frontend/templates/product/listing/renderer.phtml`** -> AI Confidence: **99.32%**
128. **`app/code/Magento/Tax/view/adminhtml/templates/toolbar/class/save.phtml`** -> AI Confidence: **99.32%**
129. **`app/code/Magento/Tax/view/adminhtml/templates/toolbar/rate/save.phtml`** -> AI Confidence: **99.32%**
130. **`app/code/Magento/Tax/view/adminhtml/templates/toolbar/rule/save.phtml`** -> AI Confidence: **99.32%**
131. **`app/code/Magento/User/view/adminhtml/templates/role/info.phtml`** -> AI Confidence: **99.32%**
132. **`app/code/Magento/User/view/adminhtml/templates/user/roles_grid_js.phtml`** -> AI Confidence: **99.32%**
133. **`app/code/Magento/Vault/view/frontend/templates/customer_account/credit_card.phtml`** -> AI Confidence: **99.32%**
134. **`phpserver/router.php`** -> AI Confidence: **99.32%**
135. **`app/code/Magento/AdvancedPricingImportExport/Model/Import/AdvancedPricing/Validator/TierPrice.php`** -> AI Confidence: **99.31%**
136. **`app/code/Magento/Authorization/Model/Acl/Loader/Rule.php`** -> AI Confidence: **99.31%**
137. **`app/code/Magento/Backend/App/Area/FrontNameResolver.php`** -> AI Confidence: **99.31%**
138. **`app/code/Magento/Backend/Controller/Adminhtml/System/Account/Save.php`** -> AI Confidence: **99.31%**
139. **`app/code/Magento/Backend/Controller/Adminhtml/System/Store/Save.php`** -> AI Confidence: **99.31%**
140. **`app/code/Magento/Backend/view/adminhtml/templates/page/js/calendar.phtml`** -> AI Confidence: **99.31%**
141. **`app/code/Magento/Bundle/Block/Catalog/Product/View/Type/Bundle/Option.php`** -> AI Confidence: **99.31%**
142. **`app/code/Magento/Bundle/Controller/Adminhtml/Product/Initialization/Helper/Plugin/Bundle.php`** -> AI Confidence: **99.31%**
143. **`app/code/Magento/Bundle/Model/LinkManagement.php`** -> AI Confidence: **99.31%**
144. **`app/code/Magento/Bundle/Model/Product/Price.php`** -> AI Confidence: **99.31%**
145. **`app/code/Magento/Bundle/Model/Product/Type.php`** -> AI Confidence: **99.31%**
146. **`app/code/Magento/Bundle/Model/ResourceModel/Selection.php`** -> AI Confidence: **99.31%**
147. **`app/code/Magento/Bundle/Model/Sales/Order/Pdf/Items/AbstractItems.php`** -> AI Confidence: **99.31%**
148. **`app/code/Magento/Bundle/Model/Sales/Order/Pdf/Items/Creditmemo.php`** -> AI Confidence: **99.31%**
149. **`app/code/Magento/Bundle/Model/Sales/Order/Pdf/Items/Shipment.php`** -> AI Confidence: **99.31%**
150. **`app/code/Magento/BundleImportExport/Model/Import/Product/Type/Bundle.php`** -> AI Confidence: **99.31%**
151. **`app/code/Magento/Catalog/Block/Product/View/Options/Type/Date.php`** -> AI Confidence: **99.31%**
152. **`app/code/Magento/Catalog/Controller/Adminhtml/Category/Save.php`** -> AI Confidence: **99.31%**
153. **`app/code/Magento/Catalog/Controller/Adminhtml/Product/Action/Attribute/Save.php`** -> AI Confidence: **99.31%**
154. **`app/code/Magento/Catalog/Controller/Adminhtml/Product/Attribute/Save.php`** -> AI Confidence: **99.31%**
155. **`app/code/Magento/Catalog/Controller/Adminhtml/Product/Attribute/Validate.php`** -> AI Confidence: **99.31%**
156. **`app/code/Magento/Catalog/Controller/Adminhtml/Product/Save.php`** -> AI Confidence: **99.31%**
157. **`app/code/Magento/Catalog/Model/Category/Authorization.php`** -> AI Confidence: **99.31%**
158. **`app/code/Magento/Catalog/Model/Category/DataProvider.php`** -> AI Confidence: **99.31%**
159. **`app/code/Magento/Catalog/Model/CustomOptions/CustomOptionProcessor.php`** -> AI Confidence: **99.31%**
160. **`app/code/Magento/Catalog/Model/Design.php`** -> AI Confidence: **99.31%**
161. **`app/code/Magento/Catalog/Model/Indexer/Category/Flat/AbstractAction.php`** -> AI Confidence: **99.31%**
162. **`app/code/Magento/Catalog/Model/Indexer/Product/Flat/FlatTableBuilder.php`** -> AI Confidence: **99.31%**
163. **`app/code/Magento/Catalog/Model/Product/Authorization.php`** -> AI Confidence: **99.31%**
164. **`app/code/Magento/Catalog/Model/Product/Gallery/CreateHandler.php`** -> AI Confidence: **99.31%**
165. **`app/code/Magento/Catalog/Model/Product/Gallery/GalleryManagement.php`** -> AI Confidence: **99.31%**
166. **`app/code/Magento/Catalog/Model/Product/Image/ParamsBuilder.php`** -> AI Confidence: **99.31%**
167. **`app/code/Magento/Catalog/Model/Product/Option/Type/File.php`** -> AI Confidence: **99.31%**
168. **`app/code/Magento/Catalog/Model/Product/Option/Type/File/Validator.php`** -> AI Confidence: **99.31%**
169. **`app/code/Magento/Catalog/Model/Product/Option/Type/File/ValidatorFile.php`** -> AI Confidence: **99.31%**
170. **`app/code/Magento/Catalog/Model/Product/Price/Validation/TierPriceValidator.php`** -> AI Confidence: **99.31%**
171. **`app/code/Magento/Catalog/Model/Product/TierPriceManagement.php`** -> AI Confidence: **99.31%**
172. **`app/code/Magento/Catalog/Model/Product/Type/AbstractType.php`** -> AI Confidence: **99.31%**
173. **`app/code/Magento/Catalog/Model/Product/Type/Price.php`** -> AI Confidence: **99.31%**
174. **`app/code/Magento/Catalog/Model/ProductRepository/MediaGalleryProcessor.php`** -> AI Confidence: **99.31%**
175. **`app/code/Magento/Catalog/Model/ResourceModel/Category/Tree.php`** -> AI Confidence: **99.31%**
176. **`app/code/Magento/Catalog/Model/ResourceModel/Product/Option/Value.php`** -> AI Confidence: **99.31%**
177. **`app/code/Magento/Catalog/Ui/DataProvider/Product/Form/Modifier/Websites.php`** -> AI Confidence: **99.31%**
178. **`app/code/Magento/CatalogGraphQl/DataProvider/Product/SearchCriteriaBuilder.php`** -> AI Confidence: **99.31%**
179. **`app/code/Magento/CatalogGraphQl/Model/Resolver/Products.php`** -> AI Confidence: **99.31%**
180. **`app/code/Magento/CatalogImportExport/Model/Export/Product.php`** -> AI Confidence: **99.31%**
181. **`app/code/Magento/CatalogImportExport/Model/Import/Product.php`** -> AI Confidence: **99.31%**
182. **`app/code/Magento/CatalogImportExport/Model/Import/Product/MediaGalleryProcessor.php`** -> AI Confidence: **99.31%**
183. **`app/code/Magento/CatalogImportExport/Model/Import/Product/Option.php`** -> AI Confidence: **99.31%**
184. **`app/code/Magento/CatalogImportExport/Model/Import/Product/Validator.php`** -> AI Confidence: **99.31%**
185. **`app/code/Magento/CatalogInventory/Model/Quote/Item/QuantityValidator.php`** -> AI Confidence: **99.31%**
186. **`app/code/Magento/CatalogInventory/Model/Quote/Item/QuantityValidator/Initializer/StockItem.php`** -> AI Confidence: **99.31%**
187. **`app/code/Magento/CatalogInventory/Model/ResourceModel/Stock/Status.php`** -> AI Confidence: **99.31%**
188. **`app/code/Magento/CatalogInventory/Model/StockStateProvider.php`** -> AI Confidence: **99.31%**
189. **`app/code/Magento/CatalogSearch/Model/Advanced.php`** -> AI Confidence: **99.31%**
190. **`app/code/Magento/CatalogSearch/Model/Indexer/Fulltext/Action/DataProvider.php`** -> AI Confidence: **99.31%**
191. **`app/code/Magento/CatalogSearch/Model/Search/RequestGenerator.php`** -> AI Confidence: **99.31%**
192. **`app/code/Magento/CatalogUrlRewrite/Model/Storage/DynamicStorage.php`** -> AI Confidence: **99.31%**
193. **`app/code/Magento/CatalogUrlRewrite/Observer/CategoryUrlPathAutogeneratorObserver.php`** -> AI Confidence: **99.31%**
194. **`app/code/Magento/Cms/Controller/Adminhtml/Block/Save.php`** -> AI Confidence: **99.31%**
195. **`app/code/Magento/Cms/Helper/Page.php`** -> AI Confidence: **99.31%**
196. **`app/code/Magento/Cms/Model/Wysiwyg/Images/Storage.php`** -> AI Confidence: **99.31%**
197. **`app/code/Magento/Config/Console/Command/ConfigShowCommand.php`** -> AI Confidence: **99.31%**
198. **`app/code/Magento/Config/Model/Config.php`** -> AI Confidence: **99.31%**
199. **`app/code/Magento/ConfigurableProduct/Controller/Adminhtml/Product/Builder/Plugin.php`** -> AI Confidence: **99.31%**
200. **`app/code/Magento/ConfigurableProduct/Model/Product/Type/Configurable.php`** -> AI Confidence: **99.31%**
201. **`app/code/Magento/ConfigurableProduct/view/adminhtml/templates/catalog/product/edit/super/matrix.phtml`** -> AI Confidence: **99.31%**
202. **`app/code/Magento/Cron/Observer/ProcessCronQueueObserver.php`** -> AI Confidence: **99.31%**
203. **`app/code/Magento/Csp/Helper/InlineUtil.php`** -> AI Confidence: **99.31%**
204. **`app/code/Magento/Csp/Model/SubresourceIntegrity/Storage/File.php`** -> AI Confidence: **99.31%**
205. **`app/code/Magento/Csp/Plugin/AddDefaultPropertiesToGroupPlugin.php`** -> AI Confidence: **99.31%**
206. **`app/code/Magento/Csp/Plugin/GenerateBundleAssetIntegrity.php`** -> AI Confidence: **99.31%**
207. **`app/code/Magento/Csp/Plugin/RemoveAllAssetIntegrityHashes.php`** -> AI Confidence: **99.31%**
208. **`app/code/Magento/Customer/Block/Adminhtml/Group/Edit/Form.php`** -> AI Confidence: **99.31%**
209. **`app/code/Magento/Customer/Controller/Adminhtml/Address/Save.php`** -> AI Confidence: **99.31%**
210. **`app/code/Magento/Customer/Model/Address/AbstractAddress.php`** -> AI Confidence: **99.31%**
211. **`app/code/Magento/Customer/Model/Address/Validator/General.php`** -> AI Confidence: **99.31%**
212. **`app/code/Magento/Customer/Model/FileUploaderDataResolver.php`** -> AI Confidence: **99.31%**
213. **`app/code/Magento/Customer/Model/Metadata/Form/File.php`** -> AI Confidence: **99.31%**
214. **`app/code/Magento/Customer/Model/Vat.php`** -> AI Confidence: **99.31%**
215. **`app/code/Magento/Customer/Plugin/ValidateDobOnSave.php`** -> AI Confidence: **99.31%**
216. **`app/code/Magento/Customer/Ui/Component/DataProvider/Document.php`** -> AI Confidence: **99.31%**
217. **`app/code/Magento/Customer/Ui/Component/Listing/Columns.php`** -> AI Confidence: **99.31%**
218. **`app/code/Magento/CustomerImportExport/Model/Import/Customer.php`** -> AI Confidence: **99.31%**
219. **`app/code/Magento/Deploy/Console/ConsoleLogger.php`** -> AI Confidence: **99.31%**
220. **`app/code/Magento/Deploy/Package/Processor/PreProcessor/Less.php`** -> AI Confidence: **99.31%**
221. **`app/code/Magento/Deploy/Service/Bundle.php`** -> AI Confidence: **99.31%**
222. **`app/code/Magento/Deploy/Service/DeployPackage.php`** -> AI Confidence: **99.31%**
223. **`app/code/Magento/Deploy/Strategy/QuickDeploy.php`** -> AI Confidence: **99.31%**
224. **`app/code/Magento/Developer/Model/Setup/Declaration/Schema/WhitelistGenerator.php`** -> AI Confidence: **99.31%**
225. **`app/code/Magento/Dhl/Model/Carrier.php`** -> AI Confidence: **99.31%**
226. **`app/code/Magento/Directory/Model/Observer.php`** -> AI Confidence: **99.31%**
227. **`app/code/Magento/Downloadable/Controller/Adminhtml/Product/Initialization/Helper/Plugin/Downloadable.php`** -> AI Confidence: **99.31%**
228. **`app/code/Magento/Downloadable/Model/Link/ContentValidator.php`** -> AI Confidence: **99.31%**
229. **`app/code/Magento/Downloadable/Model/LinkRepository.php`** -> AI Confidence: **99.31%**
230. **`app/code/Magento/Downloadable/view/adminhtml/templates/product/edit/downloadable/links.phtml`** -> AI Confidence: **99.31%**
231. **`app/code/Magento/Downloadable/view/adminhtml/templates/product/edit/downloadable/samples.phtml`** -> AI Confidence: **99.31%**
232. **`app/code/Magento/Eav/Model/Config.php`** -> AI Confidence: **99.31%**
233. **`app/code/Magento/Eav/Model/Entity/Attribute.php`** -> AI Confidence: **99.31%**
234. **`app/code/Magento/Eav/Model/Entity/Attribute/Frontend/AbstractFrontend.php`** -> AI Confidence: **99.31%**
235. **`app/code/Magento/Eav/Model/ResourceModel/Entity/Attribute.php`** -> AI Confidence: **99.31%**
236. **`app/code/Magento/Elasticsearch/Model/Adapter/Elasticsearch.php`** -> AI Confidence: **99.31%**
237. **`app/code/Magento/Elasticsearch/Model/ResourceModel/Index.php`** -> AI Confidence: **99.31%**
238. **`app/code/Magento/Email/Model/AbstractTemplate.php`** -> AI Confidence: **99.31%**
239. **`app/code/Magento/Fedex/Model/Carrier.php`** -> AI Confidence: **99.31%**
240. **`app/code/Magento/ImportExport/Controller/Adminhtml/Import/Validate.php`** -> AI Confidence: **99.31%**
241. **`app/code/Magento/Indexer/Model/Processor.php`** -> AI Confidence: **99.31%**
242. **`app/code/Magento/MessageQueue/Model/Cron/ConsumersRunner.php`** -> AI Confidence: **99.31%**
243. **`app/code/Magento/NewRelicReporting/Console/Command/DeployMarker.php`** -> AI Confidence: **99.31%**
244. **`app/code/Magento/NewRelicReporting/Model/Apm/Deployments.php`** -> AI Confidence: **99.31%**
245. **`app/code/Magento/Newsletter/Block/Adminhtml/Queue/Edit/Form.php`** -> AI Confidence: **99.31%**
246. **`app/code/Magento/Newsletter/Model/SubscriptionManager.php`** -> AI Confidence: **99.31%**
247. **`app/code/Magento/PageCache/Model/Config.php`** -> AI Confidence: **99.31%**
248. **`app/code/Magento/Paypal/Model/AbstractIpn.php`** -> AI Confidence: **99.31%**
249. **`app/code/Magento/Paypal/Model/Config.php`** -> AI Confidence: **99.31%**
250. **`app/code/Magento/Paypal/Model/Info.php`** -> AI Confidence: **99.31%**
251. **`app/code/Magento/Paypal/Model/Ipn.php`** -> AI Confidence: **99.31%**
252. **`app/code/Magento/Paypal/Model/Report/Settlement.php`** -> AI Confidence: **99.31%**
253. **`app/code/Magento/Paypal/Setup/Patch/Data/UpdateBmltoPayLater.php`** -> AI Confidence: **99.31%**
254. **`app/code/Magento/Persistent/Model/QuoteManager.php`** -> AI Confidence: **99.31%**
255. **`app/code/Magento/ProductAlert/Model/Observer.php`** -> AI Confidence: **99.31%**
256. **`app/code/Magento/Quote/Model/Address/Validator/AddressAttributeValidator.php`** -> AI Confidence: **99.31%**
257. **`app/code/Magento/Quote/Model/CustomerManagement.php`** -> AI Confidence: **99.31%**
258. **`app/code/Magento/Quote/Model/Quote/Address/BillingAddressPersister.php`** -> AI Confidence: **99.31%**
259. **`app/code/Magento/Quote/Model/Quote/Item/CartItemPersister.php`** -> AI Confidence: **99.31%**
260. **`app/code/Magento/Quote/Model/Quote/Item/Processor.php`** -> AI Confidence: **99.31%**
261. **`app/code/Magento/Quote/Model/QuoteManagement.php`** -> AI Confidence: **99.31%**
262. **`app/code/Magento/Quote/Model/ResourceModel/Quote/Item/Collection.php`** -> AI Confidence: **99.31%**
263. **`app/code/Magento/Quote/Model/ShippingAddressManagement.php`** -> AI Confidence: **99.31%**
264. **`app/code/Magento/QuoteGraphQl/Model/Cart/SetBillingAddressOnCart.php`** -> AI Confidence: **99.31%**
265. **`app/code/Magento/QuoteGraphQl/Model/CartItem/DataProvider/UpdateCartItems.php`** -> AI Confidence: **99.31%**
266. **`app/code/Magento/Review/Block/Adminhtml/Edit/Form.php`** -> AI Confidence: **99.31%**
267. **`app/code/Magento/Review/Block/Adminhtml/Rating/Edit/Tab/Form.php`** -> AI Confidence: **99.31%**
268. **`app/code/Magento/Rule/Model/Condition/Sql/Builder.php`** -> AI Confidence: **99.31%**
269. **`app/code/Magento/Sales/Controller/Adminhtml/Order/Create/LoadBlock.php`** -> AI Confidence: **99.31%**
270. **`app/code/Magento/Sales/Controller/Adminhtml/Order/Creditmemo/Save.php`** -> AI Confidence: **99.31%**
271. **`app/code/Magento/Sales/Controller/Adminhtml/Order/Invoice/Save.php`** -> AI Confidence: **99.31%**
272. **`app/code/Magento/Sales/Model/AdminOrder/Create.php`** -> AI Confidence: **99.31%**
273. **`app/code/Magento/Sales/Model/EmailSenderHandler.php`** -> AI Confidence: **99.31%**
274. **`app/code/Magento/Sales/Model/Order/Address/Validator.php`** -> AI Confidence: **99.31%**
275. **`app/code/Magento/Sales/Model/Order/Creditmemo/Total/Tax.php`** -> AI Confidence: **99.31%**
276. **`app/code/Magento/Sales/Model/Order/CreditmemoFactory.php`** -> AI Confidence: **99.31%**
277. **`app/code/Magento/Sales/Model/Service/InvoiceService.php`** -> AI Confidence: **99.31%**
278. **`app/code/Magento/Sales/Plugin/Webapi/OrderResponseNullKeysPlugin.php`** -> AI Confidence: **99.31%**
279. **`app/code/Magento/SalesGraphQl/Model/Resolver/CustomerOrders.php`** -> AI Confidence: **99.31%**
280. **`app/code/Magento/SalesRule/Controller/Adminhtml/Promo/Quote/Generate.php`** -> AI Confidence: **99.31%**
281. **`app/code/Magento/SalesRule/Model/Converter/ToDataModel.php`** -> AI Confidence: **99.31%**
282. **`app/code/Magento/SalesRule/Model/Coupon/Usage/Processor.php`** -> AI Confidence: **99.31%**
283. **`app/code/Magento/SalesRule/Model/Quote/Discount.php`** -> AI Confidence: **99.31%**
284. **`app/code/Magento/SalesRule/Model/Rule/Action/Discount/CartFixed.php`** -> AI Confidence: **99.31%**
285. **`app/code/Magento/SalesRule/Model/RulesApplier.php`** -> AI Confidence: **99.31%**
286. **`app/code/Magento/SalesRule/Model/Utility.php`** -> AI Confidence: **99.31%**
287. **`app/code/Magento/SalesRule/Model/Validator.php`** -> AI Confidence: **99.31%**
288. **`app/code/Magento/SendFriend/view/frontend/templates/send.phtml`** -> AI Confidence: **99.31%**
289. **`app/code/Magento/Shipping/Model/Shipping.php`** -> AI Confidence: **99.31%**
290. **`app/code/Magento/Sitemap/Model/ResourceModel/Catalog/Product.php`** -> AI Confidence: **99.31%**
291. **`app/code/Magento/Store/Model/Config/Importer/Processor/Delete.php`** -> AI Confidence: **99.31%**
292. **`app/code/Magento/Store/Model/Config/Importer/Processor/Update.php`** -> AI Confidence: **99.31%**
293. **`app/code/Magento/Swatches/Model/Plugin/EavAttribute.php`** -> AI Confidence: **99.31%**
294. **`app/code/Magento/Tax/Block/Adminhtml/Rate/Form.php`** -> AI Confidence: **99.31%**
295. **`app/code/Magento/Tax/Model/Calculation.php`** -> AI Confidence: **99.31%**
296. **`app/code/Magento/Tax/Model/Calculation/RateRepository.php`** -> AI Confidence: **99.31%**
297. **`app/code/Magento/Tax/Model/Calculation/Rule/Validator.php`** -> AI Confidence: **99.31%**
298. **`app/code/Magento/Tax/Model/ResourceModel/Sales/Order/Relation.php`** -> AI Confidence: **99.31%**
299. **`app/code/Magento/Tax/Model/Sales/Total/Quote/CommonTaxCollector.php`** -> AI Confidence: **99.31%**
300. **`app/code/Magento/Tax/Model/Sales/Total/Quote/Tax.php`** -> AI Confidence: **99.31%**
301. **`app/code/Magento/Tax/Observer/GetPriceConfigurationObserver.php`** -> AI Confidence: **99.31%**
302. **`app/code/Magento/TaxImportExport/Model/Rate/CsvImportHandler.php`** -> AI Confidence: **99.31%**
303. **`app/code/Magento/Theme/view/adminhtml/templates/browser/content/uploader.phtml`** -> AI Confidence: **99.31%**
304. **`app/code/Magento/Translation/Model/Inline/Parser.php`** -> AI Confidence: **99.31%**
305. **`app/code/Magento/Translation/Model/ResourceModel/StringUtils.php`** -> AI Confidence: **99.31%**
306. **`app/code/Magento/Ui/Component/Form/AttributeMapper.php`** -> AI Confidence: **99.31%**
307. **`app/code/Magento/Ui/Component/Listing/Columns/Date.php`** -> AI Confidence: **99.31%**
308. **`app/code/Magento/Ui/Component/MassAction/Filter.php`** -> AI Confidence: **99.31%**
309. **`app/code/Magento/Ui/Config/Reader/DefinitionMap/Converter.php`** -> AI Confidence: **99.31%**
310. **`app/code/Magento/Ui/Controller/Adminhtml/Bookmark/Save.php`** -> AI Confidence: **99.31%**
311. **`app/code/Magento/Ups/Model/Carrier.php`** -> AI Confidence: **99.31%**
312. **`app/code/Magento/Ups/view/adminhtml/templates/system/shipping/carrier_config.phtml`** -> AI Confidence: **99.31%**
313. **`app/code/Magento/UrlRewrite/Model/Storage/DbStorage.php`** -> AI Confidence: **99.31%**
314. **`app/code/Magento/UrlRewrite/Model/UrlRewrite.php`** -> AI Confidence: **99.31%**
315. **`app/code/Magento/UrlRewriteGraphQl/Model/Resolver/AbstractEntityUrl.php`** -> AI Confidence: **99.31%**
316. **`app/code/Magento/Usps/Model/Carrier.php`** -> AI Confidence: **99.31%**
317. **`app/code/Magento/Usps/Model/ShipmentService.php`** -> AI Confidence: **99.31%**
318. **`app/code/Magento/Usps/Model/TrackingService.php`** -> AI Confidence: **99.31%**
319. **`app/code/Magento/Webapi/Model/Rest/Swagger/Generator.php`** -> AI Confidence: **99.31%**
320. **`app/code/Magento/Webapi/Model/ServiceMetadata.php`** -> AI Confidence: **99.31%**
321. **`app/code/Magento/Webapi/Model/Soap/Wsdl/ComplexTypeStrategy.php`** -> AI Confidence: **99.31%**
322. **`app/code/Magento/Weee/Model/Total/Invoice/Weee.php`** -> AI Confidence: **99.31%**
323. **`app/code/Magento/Wishlist/Model/ItemCarrier.php`** -> AI Confidence: **99.31%**
324. **`app/etc/registration_globlist.php`** -> AI Confidence: **99.31%**
325. **`dev/tests/api-functional/framework/Magento/TestFramework/Annotation/ApiConfigFixture.php`** -> AI Confidence: **99.31%**
326. **`dev/tests/integration/framework/Magento/TestFramework/Annotation/ConfigFixture.php`** -> AI Confidence: **99.31%**
327. **`dev/tests/integration/framework/Magento/TestFramework/Annotation/DataFixtureSetup.php`** -> AI Confidence: **99.31%**
328. **`dev/tests/integration/framework/Magento/TestFramework/Annotation/TestsIsolation.php`** -> AI Confidence: **99.31%**
329. **`dev/tests/integration/testsuite/Magento/Bundle/_files/bundle_product_with_not_visible_children.php`** -> AI Confidence: **99.31%**
330. **`dev/tests/integration/testsuite/Magento/Bundle/_files/dynamic_bundle_product_with_multiple_options.php`** -> AI Confidence: **99.31%**
331. **`dev/tests/integration/testsuite/Magento/Bundle/_files/product_with_multiple_options_radio_select.php`** -> AI Confidence: **99.31%**
332. **`dev/tests/integration/testsuite/Magento/Bundle/_files/product_with_tier_pricing.php`** -> AI Confidence: **99.31%**
333. **`dev/tests/integration/testsuite/Magento/Catalog/Ui/DataProvider/Product/Form/Modifier/_files/eav_expected_meta_output.php`** -> AI Confidence: **99.31%**
334. **`dev/tests/integration/testsuite/Magento/Catalog/Ui/DataProvider/Product/Form/Modifier/_files/eav_expected_meta_output_w_default.php`** -> AI Confidence: **99.31%**
335. **`dev/tests/integration/testsuite/Magento/Catalog/Ui/DataProvider/Product/Form/Modifier/_files/input_meta_for_categories.php`** -> AI Confidence: **99.31%**
336. **`dev/tests/integration/testsuite/Magento/Catalog/_files/category_with_different_price_products_rollback.php`** -> AI Confidence: **99.31%**
337. **`dev/tests/integration/testsuite/Magento/Catalog/_files/product_simple_with_all_fields.php`** -> AI Confidence: **99.31%**
338. **`dev/tests/integration/testsuite/Magento/Catalog/_files/products_with_layered_navigation_attribute_rollback.php`** -> AI Confidence: **99.31%**
339. **`dev/tests/integration/testsuite/Magento/Catalog/_files/products_with_layered_navigation_attributes_rollback.php`** -> AI Confidence: **99.31%**
340. **`dev/tests/integration/testsuite/Magento/ConfigurableProduct/_files/configurable_attribute_with_source_model.php`** -> AI Confidence: **99.31%**
341. **`dev/tests/integration/testsuite/Magento/Elasticsearch/_files/case_sensitive.php`** -> AI Confidence: **99.31%**
342. **`dev/tests/integration/testsuite/Magento/Elasticsearch/_files/indexer.php`** -> AI Confidence: **99.31%**
343. **`dev/tests/integration/testsuite/Magento/Framework/GraphQl/_files/query_array_output.php`** -> AI Confidence: **99.31%**
344. **`dev/tests/integration/testsuite/Magento/Sales/_files/order_with_different_types_of_product_rollback.php`** -> AI Confidence: **99.31%**
345. **`dev/tests/integration/testsuite/Magento/Sales/_files/quote_with_bundle.php`** -> AI Confidence: **99.31%**
346. **`dev/tests/integration/testsuite/Magento/Widget/Model/Config/_files/expectedMergedArray.php`** -> AI Confidence: **99.31%**
347. **`dev/tests/static/framework/Magento/CodeMessDetector/Rule/Design/CookieAndSessionMisuse.php`** -> AI Confidence: **99.31%**
348. **`dev/tests/static/framework/Magento/TestFramework/Dependency/PhpRule.php`** -> AI Confidence: **99.31%**
349. **`dev/tests/static/framework/Magento/TestFramework/Dependency/Route/RouteMapper.php`** -> AI Confidence: **99.31%**
350. **`dev/tests/utils/phpunitGroupConfig.php`** -> AI Confidence: **99.31%**
351. **`setup/src/Magento/Setup/Module/Di/Code/Reader/FileScanner.php`** -> AI Confidence: **99.31%**
352. **`app/code/Magento/AdminAnalytics/view/adminhtml/templates/notification.phtml`** -> AI Confidence: **99.29%**
353. **`app/code/Magento/AdminAnalytics/view/adminhtml/templates/tracking.phtml`** -> AI Confidence: **99.29%**
354. **`app/code/Magento/AdminNotification/view/adminhtml/templates/notification/window.phtml`** -> AI Confidence: **99.29%**
355. **`app/code/Magento/AdminNotification/view/adminhtml/templates/system/messages.phtml`** -> AI Confidence: **99.29%**
356. **`app/code/Magento/AdminNotification/view/adminhtml/templates/system/messages/popup.phtml`** -> AI Confidence: **99.29%**
357. **`app/code/Magento/AdminNotification/view/adminhtml/templates/toolbar_entry.phtml`** -> AI Confidence: **99.29%**
358. **`app/code/Magento/AdvancedSearch/view/adminhtml/templates/system/config/testconnection.phtml`** -> AI Confidence: **99.29%**
359. **`app/code/Magento/AdvancedSearch/view/frontend/templates/search_data.phtml`** -> AI Confidence: **99.29%**
360. **`app/code/Magento/Analytics/registration.php`** -> AI Confidence: **99.29%**
361. **`app/code/Magento/Backend/cli_commands.php`** -> AI Confidence: **99.29%**
362. **`app/code/Magento/Backend/view/adminhtml/templates/admin/access_denied.phtml`** -> AI Confidence: **99.29%**
363. **`app/code/Magento/Backend/view/adminhtml/templates/admin/formkey.phtml`** -> AI Confidence: **99.29%**
364. **`app/code/Magento/Backend/view/adminhtml/templates/admin/overlay_popup.phtml`** -> AI Confidence: **99.29%**
365. **`app/code/Magento/Backend/view/adminhtml/templates/admin/page.phtml`** -> AI Confidence: **99.29%**
366. **`app/code/Magento/Backend/view/adminhtml/templates/admin/save_confirm.phtml`** -> AI Confidence: **99.29%**
367. **`app/code/Magento/Backend/view/adminhtml/templates/dashboard/graph.phtml`** -> AI Confidence: **99.29%**
368. **`app/code/Magento/Backend/view/adminhtml/templates/dashboard/graph/disabled.phtml`** -> AI Confidence: **99.29%**
369. **`app/code/Magento/Backend/view/adminhtml/templates/dashboard/grid.phtml`** -> AI Confidence: **99.29%**
370. **`app/code/Magento/Backend/view/adminhtml/templates/dashboard/searches.phtml`** -> AI Confidence: **99.29%**
371. **`app/code/Magento/Backend/view/adminhtml/templates/dashboard/store/switcher.phtml`** -> AI Confidence: **99.29%**
372. **`app/code/Magento/Backend/view/adminhtml/templates/menu.phtml`** -> AI Confidence: **99.29%**
373. **`app/code/Magento/Backend/view/adminhtml/templates/page/container.phtml`** -> AI Confidence: **99.29%**
374. **`app/code/Magento/Backend/view/adminhtml/templates/page/copyright.phtml`** -> AI Confidence: **99.29%**
375. **`app/code/Magento/Backend/view/adminhtml/templates/page/footer.phtml`** -> AI Confidence: **99.29%**
376. **`app/code/Magento/Backend/view/adminhtml/templates/page/header.phtml`** -> AI Confidence: **99.29%**
377. **`app/code/Magento/Backend/view/adminhtml/templates/page/js/components.phtml`** -> AI Confidence: **99.29%**
378. **`app/code/Magento/Backend/view/adminhtml/templates/page/js/require_js.phtml`** -> AI Confidence: **99.29%**
379. **`app/code/Magento/Backend/view/adminhtml/templates/page/notices.phtml`** -> AI Confidence: **99.29%**
380. **`app/code/Magento/Backend/view/adminhtml/templates/page/privacyPolicy.phtml`** -> AI Confidence: **99.29%**
381. **`app/code/Magento/Backend/view/adminhtml/templates/page/report.phtml`** -> AI Confidence: **99.29%**
382. **`app/code/Magento/Backend/view/adminhtml/templates/pageactions.phtml`** -> AI Confidence: **99.29%**
383. **`app/code/Magento/Backend/view/adminhtml/templates/store/switcher.phtml`** -> AI Confidence: **99.29%**
384. **`app/code/Magento/Backend/view/adminhtml/templates/store/switcher/form/renderer/fieldset.phtml`** -> AI Confidence: **99.29%**
385. **`app/code/Magento/Backend/view/adminhtml/templates/store/switcher/form/renderer/fieldset/element.phtml`** -> AI Confidence: **99.29%**
386. **`app/code/Magento/Backend/view/adminhtml/templates/system/cache/additional.phtml`** -> AI Confidence: **99.29%**
387. **`app/code/Magento/Backend/view/adminhtml/templates/system/design/index.phtml`** -> AI Confidence: **99.29%**
388. **`app/code/Magento/Backend/view/adminhtml/templates/system/shipping/applicable_country.phtml`** -> AI Confidence: **99.29%**
389. **`app/code/Magento/Backend/view/adminhtml/templates/widget/breadcrumbs.phtml`** -> AI Confidence: **99.29%**
390. **`app/code/Magento/Backend/view/adminhtml/templates/widget/button.phtml`** -> AI Confidence: **99.29%**
391. **`app/code/Magento/Backend/view/adminhtml/templates/widget/button/split.phtml`** -> AI Confidence: **99.29%**
392. **`app/code/Magento/Backend/view/adminhtml/templates/widget/form.phtml`** -> AI Confidence: **99.29%**
393. **`app/code/Magento/Backend/view/adminhtml/templates/widget/form/element/gallery.phtml`** -> AI Confidence: **99.29%**
394. **`app/code/Magento/Backend/view/adminhtml/templates/widget/form/renderer/element.phtml`** -> AI Confidence: **99.29%**
395. **`app/code/Magento/Backend/view/adminhtml/templates/widget/form/renderer/fieldset.phtml`** -> AI Confidence: **99.29%**
396. **`app/code/Magento/Backend/view/adminhtml/templates/widget/form/renderer/fieldset/element.phtml`** -> AI Confidence: **99.29%**
397. **`app/code/Magento/Backend/view/adminhtml/templates/widget/grid/column_set.phtml`** -> AI Confidence: **99.29%**
398. **`app/code/Magento/Backend/view/adminhtml/templates/widget/grid/container.phtml`** -> AI Confidence: **99.29%**
399. **`app/code/Magento/Backend/view/adminhtml/templates/widget/grid/container/empty.phtml`** -> AI Confidence: **99.29%**
400. **`app/code/Magento/Backend/view/adminhtml/templates/widget/grid/export.phtml`** -> AI Confidence: **99.29%**
401. **`app/code/Magento/Backend/view/adminhtml/templates/widget/grid/massaction.phtml`** -> AI Confidence: **99.29%**
402. **`app/code/Magento/Backend/view/adminhtml/templates/widget/tabsleft.phtml`** -> AI Confidence: **99.29%**
403. **`app/code/Magento/Backend/view/adminhtml/templates/widget/view/container.phtml`** -> AI Confidence: **99.29%**
404. **`app/code/Magento/Backup/view/adminhtml/templates/backup/left.phtml`** -> AI Confidence: **99.29%**
405. **`app/code/Magento/Backup/view/adminhtml/templates/backup/list.phtml`** -> AI Confidence: **99.29%**
406. **`app/code/Magento/Bundle/view/adminhtml/templates/product/composite/fieldset/options/bundle.phtml`** -> AI Confidence: **99.29%**
407. **`app/code/Magento/Bundle/view/adminhtml/templates/product/composite/fieldset/options/type/checkbox.phtml`** -> AI Confidence: **99.29%**
408. **`app/code/Magento/Bundle/view/adminhtml/templates/product/composite/fieldset/options/type/multi.phtml`** -> AI Confidence: **99.29%**
409. **`app/code/Magento/Bundle/view/adminhtml/templates/product/composite/fieldset/options/type/radio.phtml`** -> AI Confidence: **99.29%**
410. **`app/code/Magento/Bundle/view/adminhtml/templates/product/composite/fieldset/options/type/select.phtml`** -> AI Confidence: **99.29%**
411. **`app/code/Magento/Bundle/view/adminhtml/templates/product/edit/bundle/option/search.phtml`** -> AI Confidence: **99.29%**
412. **`app/code/Magento/Bundle/view/base/templates/product/price/final_price.phtml`** -> AI Confidence: **99.29%**
413. **`app/code/Magento/Bundle/view/base/templates/product/price/selection/amount.phtml`** -> AI Confidence: **99.29%**
414. **`app/code/Magento/Bundle/view/base/templates/product/price/tier_prices.phtml`** -> AI Confidence: **99.29%**
415. **`app/code/Magento/Bundle/view/frontend/templates/catalog/product/view/backbutton.phtml`** -> AI Confidence: **99.29%**
416. **`app/code/Magento/Bundle/view/frontend/templates/catalog/product/view/customize.phtml`** -> AI Confidence: **99.29%**
417. **`app/code/Magento/Bundle/view/frontend/templates/catalog/product/view/options/notice.phtml`** -> AI Confidence: **99.29%**
418. **`app/code/Magento/Bundle/view/frontend/templates/catalog/product/view/type/bundle.phtml`** -> AI Confidence: **99.29%**
419. **`app/code/Magento/Bundle/view/frontend/templates/catalog/product/view/type/bundle/option/checkbox.phtml`** -> AI Confidence: **99.29%**
420. **`app/code/Magento/Bundle/view/frontend/templates/catalog/product/view/type/bundle/option/multi.phtml`** -> AI Confidence: **99.29%**
421. **`app/code/Magento/Bundle/view/frontend/templates/catalog/product/view/type/bundle/option/select.phtml`** -> AI Confidence: **99.29%**
422. **`app/code/Magento/Bundle/view/frontend/templates/catalog/product/view/type/bundle/options.phtml`** -> AI Confidence: **99.29%**
423. **`app/code/Magento/Bundle/view/frontend/templates/email/order/items/creditmemo/default.phtml`** -> AI Confidence: **99.29%**
424. **`app/code/Magento/Bundle/view/frontend/templates/email/order/items/invoice/default.phtml`** -> AI Confidence: **99.29%**
425. **`app/code/Magento/Bundle/view/frontend/templates/email/order/items/order/default.phtml`** -> AI Confidence: **99.29%**
426. **`app/code/Magento/Bundle/view/frontend/templates/email/order/items/shipment/default.phtml`** -> AI Confidence: **99.29%**
427. **`app/code/Magento/Bundle/view/frontend/templates/js/components.phtml`** -> AI Confidence: **99.29%**
428. **`app/code/Magento/Bundle/view/frontend/templates/sales/order/creditmemo/items/renderer.phtml`** -> AI Confidence: **99.29%**
429. **`app/code/Magento/Bundle/view/frontend/templates/sales/order/invoice/items/renderer.phtml`** -> AI Confidence: **99.29%**
430. **`app/code/Magento/Bundle/view/frontend/templates/sales/order/items/renderer.phtml`** -> AI Confidence: **99.29%**
431. **`app/code/Magento/Bundle/view/frontend/templates/sales/order/shipment/items/renderer.phtml`** -> AI Confidence: **99.29%**
432. **`app/code/Magento/Captcha/view/frontend/templates/js/components.phtml`** -> AI Confidence: **99.29%**
433. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/category/checkboxes/tree.phtml`** -> AI Confidence: **99.29%**
434. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/category/edit.phtml`** -> AI Confidence: **99.29%**
435. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/category/edit/assign_products.phtml`** -> AI Confidence: **99.29%**
436. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/category/widget/tree.phtml`** -> AI Confidence: **99.29%**
437. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/form/renderer/fieldset/element.phtml`** -> AI Confidence: **99.29%**
438. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product.phtml`** -> AI Confidence: **99.29%**
439. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/attribute/form.phtml`** -> AI Confidence: **99.29%**
440. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/attribute/set/main/tree/attribute.phtml`** -> AI Confidence: **99.29%**
441. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/attribute/set/main/tree/group.phtml`** -> AI Confidence: **99.29%**
442. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/attribute/set/toolbar/main.phtml`** -> AI Confidence: **99.29%**
443. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/composite/fieldset/options.phtml`** -> AI Confidence: **99.29%**
444. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/composite/fieldset/options/js.phtml`** -> AI Confidence: **99.29%**
445. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/composite/fieldset/options/type/default.phtml`** -> AI Confidence: **99.29%**
446. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/composite/fieldset/options/type/file.phtml`** -> AI Confidence: **99.29%**
447. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/composite/fieldset/options/type/select.phtml`** -> AI Confidence: **99.29%**
448. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/composite/fieldset/options/type/text.phtml`** -> AI Confidence: **99.29%**
449. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/edit/action/attribute.phtml`** -> AI Confidence: **99.29%**
450. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/edit/attribute_set.phtml`** -> AI Confidence: **99.29%**
451. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/edit/category/new/form.phtml`** -> AI Confidence: **99.29%**
452. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/edit/options/type/date.phtml`** -> AI Confidence: **99.29%**
453. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/edit/serializer.phtml`** -> AI Confidence: **99.29%**
454. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/edit/websites.phtml`** -> AI Confidence: **99.29%**
455. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/tab/alert.phtml`** -> AI Confidence: **99.29%**
456. **`app/code/Magento/Catalog/view/adminhtml/templates/product/edit/tabs.phtml`** -> AI Confidence: **99.29%**
457. **`app/code/Magento/Catalog/view/adminhtml/templates/product/edit/tabs/child_tab.phtml`** -> AI Confidence: **99.29%**
458. **`app/code/Magento/Catalog/view/adminhtml/templates/product/grid/massaction_extended.phtml`** -> AI Confidence: **99.29%**
459. **`app/code/Magento/Catalog/view/adminhtml/templates/product/grid/url_filter_applier.phtml`** -> AI Confidence: **99.29%**
460. **`app/code/Magento/Catalog/view/adminhtml/templates/rss/grid/link.phtml`** -> AI Confidence: **99.29%**
461. **`app/code/Magento/Catalog/view/base/templates/js/components.phtml`** -> AI Confidence: **99.29%**
462. **`app/code/Magento/Catalog/view/base/templates/product/composite/fieldset/options/view/checkable.phtml`** -> AI Confidence: **99.29%**
463. **`app/code/Magento/Catalog/view/base/templates/product/price/amount/default.phtml`** -> AI Confidence: **99.29%**
464. **`app/code/Magento/Catalog/view/base/templates/product/price/configured_price.phtml`** -> AI Confidence: **99.29%**
465. **`app/code/Magento/Catalog/view/base/templates/product/price/default.phtml`** -> AI Confidence: **99.29%**
466. **`app/code/Magento/Catalog/view/base/templates/product/price/final_price.phtml`** -> AI Confidence: **99.29%**
467. **`app/code/Magento/Catalog/view/frontend/templates/category/cms.phtml`** -> AI Confidence: **99.29%**
468. **`app/code/Magento/Catalog/view/frontend/templates/category/description.phtml`** -> AI Confidence: **99.29%**
469. **`app/code/Magento/Catalog/view/frontend/templates/category/products.phtml`** -> AI Confidence: **99.29%**
470. **`app/code/Magento/Catalog/view/frontend/templates/category/rss.phtml`** -> AI Confidence: **99.29%**
471. **`app/code/Magento/Catalog/view/frontend/templates/category/widget/link/link_block.phtml`** -> AI Confidence: **99.29%**
472. **`app/code/Magento/Catalog/view/frontend/templates/category/widget/link/link_href.phtml`** -> AI Confidence: **99.29%**
473. **`app/code/Magento/Catalog/view/frontend/templates/category/widget/link/link_inline.phtml`** -> AI Confidence: **99.29%**
474. **`app/code/Magento/Catalog/view/frontend/templates/frontend_storage_manager.phtml`** -> AI Confidence: **99.29%**
475. **`app/code/Magento/Catalog/view/frontend/templates/messages/addCompareSuccessMessage.phtml`** -> AI Confidence: **99.29%**
476. **`app/code/Magento/Catalog/view/frontend/templates/navigation/left.phtml`** -> AI Confidence: **99.29%**
477. **`app/code/Magento/Catalog/view/frontend/templates/product/breadcrumbs.phtml`** -> AI Confidence: **99.29%**
478. **`app/code/Magento/Catalog/view/frontend/templates/product/compare/list.phtml`** -> AI Confidence: **99.29%**
479. **`app/code/Magento/Catalog/view/frontend/templates/product/gallery.phtml`** -> AI Confidence: **99.29%**
480. **`app/code/Magento/Catalog/view/frontend/templates/product/image.phtml`** -> AI Confidence: **99.29%**
481. **`app/code/Magento/Catalog/view/frontend/templates/product/image_with_borders.phtml`** -> AI Confidence: **99.29%**
482. **`app/code/Magento/Catalog/view/frontend/templates/product/list.phtml`** -> AI Confidence: **99.29%**
483. **`app/code/Magento/Catalog/view/frontend/templates/product/list/addto/compare.phtml`** -> AI Confidence: **99.29%**
484. **`app/code/Magento/Catalog/view/frontend/templates/product/list/items.phtml`** -> AI Confidence: **99.29%**
485. **`app/code/Magento/Catalog/view/frontend/templates/product/list/toolbar.phtml`** -> AI Confidence: **99.29%**
486. **`app/code/Magento/Catalog/view/frontend/templates/product/list/toolbar/limiter.phtml`** -> AI Confidence: **99.29%**
487. **`app/code/Magento/Catalog/view/frontend/templates/product/list/toolbar/sorter.phtml`** -> AI Confidence: **99.29%**
488. **`app/code/Magento/Catalog/view/frontend/templates/product/list/toolbar/viewmode.phtml`** -> AI Confidence: **99.29%**
489. **`app/code/Magento/Catalog/view/frontend/templates/product/view/additional.phtml`** -> AI Confidence: **99.29%**
490. **`app/code/Magento/Catalog/view/frontend/templates/product/view/addto.phtml`** -> AI Confidence: **99.29%**
491. **`app/code/Magento/Catalog/view/frontend/templates/product/view/addto/compare.phtml`** -> AI Confidence: **99.29%**
492. **`app/code/Magento/Catalog/view/frontend/templates/product/view/addtocart.phtml`** -> AI Confidence: **99.29%**
493. **`app/code/Magento/Catalog/view/frontend/templates/product/view/attribute.phtml`** -> AI Confidence: **99.29%**
494. **`app/code/Magento/Catalog/view/frontend/templates/product/view/attributes.phtml`** -> AI Confidence: **99.29%**
495. **`app/code/Magento/Catalog/view/frontend/templates/product/view/counter.phtml`** -> AI Confidence: **99.29%**
496. **`app/code/Magento/Catalog/view/frontend/templates/product/view/description.phtml`** -> AI Confidence: **99.29%**
497. **`app/code/Magento/Catalog/view/frontend/templates/product/view/details.phtml`** -> AI Confidence: **99.29%**
498. **`app/code/Magento/Catalog/view/frontend/templates/product/view/form.phtml`** -> AI Confidence: **99.29%**
499. **`app/code/Magento/Catalog/view/frontend/templates/product/view/gallery.phtml`** -> AI Confidence: **99.29%**
500. **`app/code/Magento/Catalog/view/frontend/templates/product/view/mailto.phtml`** -> AI Confidence: **99.29%**
501. **`app/code/Magento/Catalog/view/frontend/templates/product/view/opengraph/currency.phtml`** -> AI Confidence: **99.29%**
502. **`app/code/Magento/Catalog/view/frontend/templates/product/view/opengraph/general.phtml`** -> AI Confidence: **99.29%**
503. **`app/code/Magento/Catalog/view/frontend/templates/product/view/options.phtml`** -> AI Confidence: **99.29%**
504. **`app/code/Magento/Catalog/view/frontend/templates/product/view/options/type/date.phtml`** -> AI Confidence: **99.29%**
505. **`app/code/Magento/Catalog/view/frontend/templates/product/view/options/type/file.phtml`** -> AI Confidence: **99.29%**
506. **`app/code/Magento/Catalog/view/frontend/templates/product/view/options/type/select.phtml`** -> AI Confidence: **99.29%**
507. **`app/code/Magento/Catalog/view/frontend/templates/product/view/options/type/text.phtml`** -> AI Confidence: **99.29%**
508. **`app/code/Magento/Catalog/view/frontend/templates/product/view/options/wrapper.phtml`** -> AI Confidence: **99.29%**
509. **`app/code/Magento/Catalog/view/frontend/templates/product/view/options/wrapper/bottom.phtml`** -> AI Confidence: **99.29%**
510. **`app/code/Magento/Catalog/view/frontend/templates/product/view/price_clone.phtml`** -> AI Confidence: **99.29%**
511. **`app/code/Magento/Catalog/view/frontend/templates/product/view/review.phtml`** -> AI Confidence: **99.29%**
512. **`app/code/Magento/Catalog/view/frontend/templates/product/view/type/default.phtml`** -> AI Confidence: **99.29%**
513. **`app/code/Magento/Catalog/view/frontend/templates/product/widget/compared/grid.phtml`** -> AI Confidence: **99.29%**
514. **`app/code/Magento/Catalog/view/frontend/templates/product/widget/compared/list.phtml`** -> AI Confidence: **99.29%**
515. **`app/code/Magento/Catalog/view/frontend/templates/product/widget/compared/sidebar.phtml`** -> AI Confidence: **99.29%**
516. **`app/code/Magento/Catalog/view/frontend/templates/product/widget/link/link_block.phtml`** -> AI Confidence: **99.29%**
517. **`app/code/Magento/Catalog/view/frontend/templates/product/widget/link/link_inline.phtml`** -> AI Confidence: **99.29%**
518. **`app/code/Magento/Catalog/view/frontend/templates/product/widget/new/column/new_default_list.phtml`** -> AI Confidence: **99.29%**
519. **`app/code/Magento/Catalog/view/frontend/templates/product/widget/new/content/new_grid.phtml`** -> AI Confidence: **99.29%**
520. **`app/code/Magento/Catalog/view/frontend/templates/product/widget/new/content/new_list.phtml`** -> AI Confidence: **99.29%**
521. **`app/code/Magento/Catalog/view/frontend/templates/product/widget/viewed/grid.phtml`** -> AI Confidence: **99.29%**
522. **`app/code/Magento/Catalog/view/frontend/templates/product/widget/viewed/list.phtml`** -> AI Confidence: **99.29%**
523. **`app/code/Magento/Catalog/view/frontend/templates/product/widget/viewed/sidebar.phtml`** -> AI Confidence: **99.29%**
524. **`app/code/Magento/CatalogAnalytics/registration.php`** -> AI Confidence: **99.29%**
525. **`app/code/Magento/CatalogInventory/view/frontend/templates/qtyincrements.phtml`** -> AI Confidence: **99.29%**
526. **`app/code/Magento/CatalogInventory/view/frontend/templates/stockqty/composite.phtml`** -> AI Confidence: **99.29%**
527. **`app/code/Magento/CatalogInventory/view/frontend/templates/stockqty/default.phtml`** -> AI Confidence: **99.29%**
528. **`app/code/Magento/CatalogRule/view/adminhtml/templates/promo/form.phtml`** -> AI Confidence: **99.29%**
529. **`app/code/Magento/CatalogSearch/view/adminhtml/templates/search_engine_comment.phtml`** -> AI Confidence: **99.29%**
530. **`app/code/Magento/CatalogSearch/view/frontend/templates/advanced/result.phtml`** -> AI Confidence: **99.29%**
531. **`app/code/Magento/CatalogSearch/view/frontend/templates/result.phtml`** -> AI Confidence: **99.29%**
532. **`app/code/Magento/CatalogSearch/view/frontend/templates/search_terms_log.phtml`** -> AI Confidence: **99.29%**
533. **`app/code/Magento/CheckoutAgreements/view/frontend/templates/agreements.phtml`** -> AI Confidence: **99.29%**
534. **`app/code/Magento/CheckoutAgreements/view/frontend/templates/multishipping_agreements.phtml`** -> AI Confidence: **99.29%**
535. **`app/code/Magento/Cms/view/adminhtml/templates/browser/content/files.phtml`** -> AI Confidence: **99.29%**
536. **`app/code/Magento/Cms/view/adminhtml/templates/page/edit/form/renderer/content.phtml`** -> AI Confidence: **99.29%**
537. **`app/code/Magento/Cms/view/adminhtml/templates/url_filter_applier.phtml`** -> AI Confidence: **99.29%**
538. **`app/code/Magento/Cms/view/frontend/templates/content.phtml`** -> AI Confidence: **99.29%**
539. **`app/code/Magento/Cms/view/frontend/templates/default/home.phtml`** -> AI Confidence: **99.29%**
540. **`app/code/Magento/Cms/view/frontend/templates/default/no-route.phtml`** -> AI Confidence: **99.29%**
541. **`app/code/Magento/Cms/view/frontend/templates/meta.phtml`** -> AI Confidence: **99.29%**
542. **`app/code/Magento/Cms/view/frontend/templates/widget/link/link_block.phtml`** -> AI Confidence: **99.29%**
543. **`app/code/Magento/Cms/view/frontend/templates/widget/link/link_inline.phtml`** -> AI Confidence: **99.29%**
544. **`app/code/Magento/Cms/view/frontend/templates/widget/static_block/default.phtml`** -> AI Confidence: **99.29%**
545. **`app/code/Magento/Config/view/adminhtml/templates/page/system/config/robots/reset.phtml`** -> AI Confidence: **99.29%**
546. **`app/code/Magento/Config/view/adminhtml/templates/system/config/js.phtml`** -> AI Confidence: **99.29%**
547. **`app/code/Magento/Config/view/adminhtml/templates/system/config/switcher.phtml`** -> AI Confidence: **99.29%**
548. **`app/code/Magento/Config/view/adminhtml/templates/system/config/tabs.phtml`** -> AI Confidence: **99.29%**
549. **`app/code/Magento/ConfigurableProduct/view/adminhtml/templates/catalog/product/attribute/new/created.phtml`** -> AI Confidence: **99.29%**
550. **`app/code/Magento/ConfigurableProduct/view/adminhtml/templates/catalog/product/edit/attribute/steps/select_attributes.phtml`** -> AI Confidence: **99.29%**
551. **`app/code/Magento/ConfigurableProduct/view/adminhtml/templates/catalog/product/edit/attribute/steps/summary.phtml`** -> AI Confidence: **99.29%**
552. **`app/code/Magento/ConfigurableProduct/view/adminhtml/templates/catalog/product/edit/super/wizard.phtml`** -> AI Confidence: **99.29%**
553. **`app/code/Magento/ConfigurableProduct/view/adminhtml/templates/product/configurable/affected-attribute-set-selector/form.phtml`** -> AI Confidence: **99.29%**
554. **`app/code/Magento/ConfigurableProduct/view/adminhtml/templates/product/configurable/attribute-selector/js.phtml`** -> AI Confidence: **99.29%**
555. **`app/code/Magento/ConfigurableProduct/view/base/templates/product/price/final_price.phtml`** -> AI Confidence: **99.29%**
556. **`app/code/Magento/ConfigurableProduct/view/frontend/templates/js/components.phtml`** -> AI Confidence: **99.29%**
557. **`app/code/Magento/ConfigurableProduct/view/frontend/templates/product/view/type/options/configurable.phtml`** -> AI Confidence: **99.29%**
558. **`app/code/Magento/Cookie/view/base/templates/html/cookie.phtml`** -> AI Confidence: **99.29%**
559. **`app/code/Magento/Cookie/view/frontend/templates/html/notices.phtml`** -> AI Confidence: **99.29%**
560. **`app/code/Magento/Cookie/view/frontend/templates/require_cookie.phtml`** -> AI Confidence: **99.29%**
561. **`app/code/Magento/Csp/view/base/templates/nonce/nonce.phtml`** -> AI Confidence: **99.29%**
562. **`app/code/Magento/Csp/view/base/templates/sri/hashes.phtml`** -> AI Confidence: **99.29%**
563. **`app/code/Magento/CurrencySymbol/view/adminhtml/templates/grid.phtml`** -> AI Confidence: **99.29%**
564. **`app/code/Magento/CurrencySymbol/view/adminhtml/templates/system/currency/rates.phtml`** -> AI Confidence: **99.29%**
565. **`app/code/Magento/Customer/view/adminhtml/templates/edit/js.phtml`** -> AI Confidence: **99.29%**
566. **`app/code/Magento/Customer/view/adminhtml/templates/sales/order/create/address/form/renderer/vat.phtml`** -> AI Confidence: **99.29%**
567. **`app/code/Magento/Customer/view/adminhtml/templates/system/config/validatevat.phtml`** -> AI Confidence: **99.29%**
568. **`app/code/Magento/Customer/view/adminhtml/templates/tab/cart_website_filter_form.phtml`** -> AI Confidence: **99.29%**
569. **`app/code/Magento/Customer/view/adminhtml/templates/tab/newsletter.phtml`** -> AI Confidence: **99.29%**
570. **`app/code/Magento/Customer/view/adminhtml/templates/tab/view.phtml`** -> AI Confidence: **99.29%**
571. **`app/code/Magento/Customer/view/adminhtml/templates/tab/view/personal_info.phtml`** -> AI Confidence: **99.29%**
572. **`app/code/Magento/Customer/view/adminhtml/templates/tab/view/sales.phtml`** -> AI Confidence: **99.29%**
573. **`app/code/Magento/Customer/view/frontend/templates/account/authentication-popup.phtml`** -> AI Confidence: **99.29%**
574. **`app/code/Magento/Customer/view/frontend/templates/account/customer.phtml`** -> AI Confidence: **99.29%**
575. **`app/code/Magento/Customer/view/frontend/templates/account/link/authorization.phtml`** -> AI Confidence: **99.29%**
576. **`app/code/Magento/Customer/view/frontend/templates/account/link/my-account.phtml`** -> AI Confidence: **99.29%**
577. **`app/code/Magento/Customer/view/frontend/templates/additionalinfocustomer.phtml`** -> AI Confidence: **99.29%**
578. **`app/code/Magento/Customer/view/frontend/templates/js/components.phtml`** -> AI Confidence: **99.29%**
579. **`app/code/Magento/Customer/view/frontend/templates/js/customer-data.phtml`** -> AI Confidence: **99.29%**
580. **`app/code/Magento/Customer/view/frontend/templates/js/customer-data/invalidation-rules.phtml`** -> AI Confidence: **99.29%**
581. **`app/code/Magento/Customer/view/frontend/templates/messages/confirmAccountErrorMessage.phtml`** -> AI Confidence: **99.29%**
582. **`app/code/Magento/Customer/view/frontend/templates/messages/confirmAccountSuccessMessage.phtml`** -> AI Confidence: **99.29%**
583. **`app/code/Magento/Customer/view/frontend/templates/messages/customerAlreadyExistsErrorMessage.phtml`** -> AI Confidence: **99.29%**
584. **`app/code/Magento/Customer/view/frontend/templates/messages/customerVatBillingAddressSuccessMessage.phtml`** -> AI Confidence: **99.29%**
585. **`app/code/Magento/Customer/view/frontend/templates/messages/customerVatShippingAddressSuccessMessage.phtml`** -> AI Confidence: **99.29%**
586. **`app/code/Magento/Customer/view/frontend/templates/widget/company.phtml`** -> AI Confidence: **99.29%**
587. **`app/code/Magento/Customer/view/frontend/templates/widget/fax.phtml`** -> AI Confidence: **99.29%**
588. **`app/code/Magento/Customer/view/frontend/templates/widget/gender.phtml`** -> AI Confidence: **99.29%**
589. **`app/code/Magento/CustomerAnalytics/registration.php`** -> AI Confidence: **99.29%**
590. **`app/code/Magento/Deploy/cli_commands.php`** -> AI Confidence: **99.29%**
591. **`app/code/Magento/Dhl/view/adminhtml/templates/unitofmeasure.phtml`** -> AI Confidence: **99.29%**
592. **`app/code/Magento/Directory/view/frontend/templates/currency.phtml`** -> AI Confidence: **99.29%**
593. **`app/code/Magento/Directory/view/frontend/templates/currency/switch.phtml`** -> AI Confidence: **99.29%**
594. **`app/code/Magento/Downloadable/view/adminhtml/templates/sales/items/column/downloadable/name.phtml`** -> AI Confidence: **99.29%**
595. **`app/code/Magento/Downloadable/view/frontend/templates/catalog/product/links.phtml`** -> AI Confidence: **99.29%**
596. **`app/code/Magento/Downloadable/view/frontend/templates/catalog/product/samples.phtml`** -> AI Confidence: **99.29%**
597. **`app/code/Magento/Downloadable/view/frontend/templates/catalog/product/type.phtml`** -> AI Confidence: **99.29%**
598. **`app/code/Magento/Downloadable/view/frontend/templates/customer/products/list.phtml`** -> AI Confidence: **99.29%**
599. **`app/code/Magento/Downloadable/view/frontend/templates/email/order/items/creditmemo/downloadable.phtml`** -> AI Confidence: **99.29%**
600. **`app/code/Magento/Downloadable/view/frontend/templates/email/order/items/invoice/downloadable.phtml`** -> AI Confidence: **99.29%**
601. **`app/code/Magento/Downloadable/view/frontend/templates/email/order/items/order/downloadable.phtml`** -> AI Confidence: **99.29%**
602. **`app/code/Magento/Downloadable/view/frontend/templates/js/components.phtml`** -> AI Confidence: **99.29%**
603. **`app/code/Magento/Downloadable/view/frontend/templates/sales/order/creditmemo/items/renderer/downloadable.phtml`** -> AI Confidence: **99.29%**
604. **`app/code/Magento/Downloadable/view/frontend/templates/sales/order/invoice/items/renderer/downloadable.phtml`** -> AI Confidence: **99.29%**
605. **`app/code/Magento/Downloadable/view/frontend/templates/sales/order/items/renderer/downloadable.phtml`** -> AI Confidence: **99.29%**
606. **`app/code/Magento/Eav/view/adminhtml/templates/attribute/edit/js.phtml`** -> AI Confidence: **99.29%**
607. **`app/code/Magento/Elasticsearch/registration.php`** -> AI Confidence: **99.29%**
608. **`app/code/Magento/Email/view/adminhtml/templates/preview/iframeswitcher.phtml`** -> AI Confidence: **99.29%**
609. **`app/code/Magento/Email/view/adminhtml/templates/template/list.phtml`** -> AI Confidence: **99.29%**
610. **`app/code/Magento/Email/view/adminhtml/templates/template/preview.phtml`** -> AI Confidence: **99.29%**
611. **`app/code/Magento/GiftMessage/view/adminhtml/templates/sales/order/create/items.phtml`** -> AI Confidence: **99.29%**
612. **`app/code/Magento/GiftMessage/view/adminhtml/templates/sales/order/view/items.phtml`** -> AI Confidence: **99.29%**
613. **`app/code/Magento/GiftMessage/view/frontend/templates/cart/gift_options.phtml`** -> AI Confidence: **99.29%**
614. **`app/code/Magento/GiftMessage/view/frontend/templates/cart/item/renderer/actions/gift_options.phtml`** -> AI Confidence: **99.29%**
615. **`app/code/Magento/GoogleAnalytics/view/frontend/templates/ga.phtml`** -> AI Confidence: **99.29%**
616. **`app/code/Magento/GoogleGtag/view/frontend/templates/code.phtml`** -> AI Confidence: **99.29%**
617. **`app/code/Magento/GoogleGtag/view/frontend/templates/ga.phtml`** -> AI Confidence: **99.29%**
618. **`app/code/Magento/GoogleGtag/view/frontend/templates/head.phtml`** -> AI Confidence: **99.29%**
619. **`app/code/Magento/GroupedProduct/view/adminhtml/templates/catalog/product/composite/fieldset/grouped.phtml`** -> AI Confidence: **99.29%**
620. **`app/code/Magento/GroupedProduct/view/base/templates/product/price/final_price.phtml`** -> AI Confidence: **99.29%**
621. **`app/code/Magento/GroupedProduct/view/frontend/templates/product/view/type/default.phtml`** -> AI Confidence: **99.29%**
622. **`app/code/Magento/GroupedProduct/view/frontend/templates/product/view/type/grouped.phtml`** -> AI Confidence: **99.29%**
623. **`app/code/Magento/ImportExport/view/adminhtml/templates/export/form/after.phtml`** -> AI Confidence: **99.29%**
624. **`app/code/Magento/ImportExport/view/adminhtml/templates/import/frame/result.phtml`** -> AI Confidence: **99.29%**
625. **`app/code/Magento/InstantPurchase/view/frontend/templates/button.phtml`** -> AI Confidence: **99.29%**
626. **`app/code/Magento/Integration/view/adminhtml/templates/integration/activate/permissions.phtml`** -> AI Confidence: **99.29%**
627. **`app/code/Magento/Integration/view/adminhtml/templates/integration/activate/permissions/tab/webapi.phtml`** -> AI Confidence: **99.29%**
628. **`app/code/Magento/Integration/view/adminhtml/templates/integration/tokens_exchange.phtml`** -> AI Confidence: **99.29%**
629. **`app/code/Magento/LayeredNavigation/view/frontend/templates/layer/filter.phtml`** -> AI Confidence: **99.29%**
630. **`app/code/Magento/LayeredNavigation/view/frontend/templates/layer/state.phtml`** -> AI Confidence: **99.29%**
631. **`app/code/Magento/LayeredNavigation/view/frontend/templates/layer/view.phtml`** -> AI Confidence: **99.29%**
632. **`app/code/Magento/LoginAsCustomer/registration.php`** -> AI Confidence: **99.29%**
633. **`app/code/Magento/LoginAsCustomerAdminUi/view/adminhtml/templates/confirmation-popup.phtml`** -> AI Confidence: **99.29%**
634. **`app/code/Magento/LoginAsCustomerAssistance/view/adminhtml/templates/not-allowed-popup.phtml`** -> AI Confidence: **99.29%**
635. **`app/code/Magento/LoginAsCustomerFrontendUi/view/frontend/templates/login.phtml`** -> AI Confidence: **99.29%**
636. **`app/code/Magento/Marketplace/view/adminhtml/templates/partners.phtml`** -> AI Confidence: **99.29%**
637. **`app/code/Magento/MediaGalleryCatalogUi/view/adminhtml/templates/url_filter_applier.phtml`** -> AI Confidence: **99.29%**
638. **`app/code/Magento/MediaGalleryUi/view/adminhtml/templates/container.phtml`** -> AI Confidence: **99.29%**
639. **`app/code/Magento/MediaGalleryUi/view/adminhtml/templates/image_details_standalone.phtml`** -> AI Confidence: **99.29%**
640. **`app/code/Magento/MediaGalleryUi/view/adminhtml/templates/image_edit_details.phtml`** -> AI Confidence: **99.29%**
641. **`app/code/Magento/MediaGalleryUi/view/adminhtml/templates/image_edit_details_standalone.phtml`** -> AI Confidence: **99.29%**
642. **`app/code/Magento/Msrp/view/base/templates/product/price/msrp.phtml`** -> AI Confidence: **99.29%**
643. **`app/code/Magento/Msrp/view/frontend/templates/render/item/price_msrp_item.phtml`** -> AI Confidence: **99.29%**
644. **`app/code/Magento/Msrp/view/frontend/templates/render/item/price_msrp_rss.phtml`** -> AI Confidence: **99.29%**
645. **`app/code/Magento/Multishipping/view/frontend/templates/js/components.phtml`** -> AI Confidence: **99.29%**
646. **`app/code/Magento/Multishipping/view/frontend/templates/multishipping/item/default.phtml`** -> AI Confidence: **99.29%**
647. **`app/code/Magento/NewRelicReporting/view/base/templates/html/inline_js.phtml`** -> AI Confidence: **99.29%**
648. **`app/code/Magento/Newsletter/view/adminhtml/templates/preview/store.phtml`** -> AI Confidence: **99.29%**
649. **`app/code/Magento/Newsletter/view/adminhtml/templates/queue/list.phtml`** -> AI Confidence: **99.29%**
650. **`app/code/Magento/Newsletter/view/adminhtml/templates/queue/preview.phtml`** -> AI Confidence: **99.29%**
651. **`app/code/Magento/Newsletter/view/adminhtml/templates/template/list.phtml`** -> AI Confidence: **99.29%**
652. **`app/code/Magento/Newsletter/view/adminhtml/templates/template/preview.phtml`** -> AI Confidence: **99.29%**
653. **`app/code/Magento/Newsletter/view/frontend/templates/form/register/newsletter.phtml`** -> AI Confidence: **99.29%**
654. **`app/code/Magento/Newsletter/view/frontend/templates/js/components.phtml`** -> AI Confidence: **99.29%**
655. **`app/code/Magento/Newsletter/view/frontend/templates/messages/localizedSubscriptionErrorMessage.phtml`** -> AI Confidence: **99.29%**
656. **`app/code/Magento/OfflinePayments/view/adminhtml/templates/form/banktransfer.phtml`** -> AI Confidence: **99.29%**
657. **`app/code/Magento/OfflinePayments/view/adminhtml/templates/form/cashondelivery.phtml`** -> AI Confidence: **99.29%**
658. **`app/code/Magento/OfflinePayments/view/adminhtml/templates/form/checkmo.phtml`** -> AI Confidence: **99.29%**
659. **`app/code/Magento/OfflinePayments/view/adminhtml/templates/info/checkmo.phtml`** -> AI Confidence: **99.29%**
660. **`app/code/Magento/OfflinePayments/view/adminhtml/templates/info/pdf/checkmo.phtml`** -> AI Confidence: **99.29%**
661. **`app/code/Magento/OfflinePayments/view/adminhtml/templates/info/pdf/purchaseorder.phtml`** -> AI Confidence: **99.29%**
662. **`app/code/Magento/OfflinePayments/view/adminhtml/templates/info/purchaseorder.phtml`** -> AI Confidence: **99.29%**
663. **`app/code/Magento/OfflinePayments/view/base/templates/info/pdf/checkmo.phtml`** -> AI Confidence: **99.29%**
664. **`app/code/Magento/OfflinePayments/view/base/templates/info/pdf/purchaseorder.phtml`** -> AI Confidence: **99.29%**
665. **`app/code/Magento/OfflinePayments/view/frontend/templates/form/banktransfer.phtml`** -> AI Confidence: **99.29%**
666. **`app/code/Magento/OfflinePayments/view/frontend/templates/form/cashondelivery.phtml`** -> AI Confidence: **99.29%**
667. **`app/code/Magento/OfflinePayments/view/frontend/templates/form/checkmo.phtml`** -> AI Confidence: **99.29%**
668. **`app/code/Magento/OfflinePayments/view/frontend/templates/info/checkmo.phtml`** -> AI Confidence: **99.29%**
669. **`app/code/Magento/OfflinePayments/view/frontend/templates/multishipping/checkmo_form.phtml`** -> AI Confidence: **99.29%**
670. **`app/code/Magento/OrderCancellationUi/view/frontend/templates/cancel-order-modal.phtml`** -> AI Confidence: **99.29%**
671. **`app/code/Magento/OrderCancellationUi/view/frontend/templates/order/history.phtml`** -> AI Confidence: **99.29%**
672. **`app/code/Magento/OrderCancellationUi/view/frontend/templates/order/info/buttons.phtml`** -> AI Confidence: **99.29%**
673. **`app/code/Magento/OrderCancellationUi/view/frontend/templates/order/recent.phtml`** -> AI Confidence: **99.29%**
674. **`app/code/Magento/PageCache/view/frontend/templates/form_key_provider.phtml`** -> AI Confidence: **99.29%**
675. **`app/code/Magento/PageCache/view/frontend/templates/javascript.phtml`** -> AI Confidence: **99.29%**
676. **`app/code/Magento/PageCache/view/frontend/templates/js/components.phtml`** -> AI Confidence: **99.29%**
677. **`app/code/Magento/Payment/view/adminhtml/templates/form/cc.phtml`** -> AI Confidence: **99.29%**
678. **`app/code/Magento/Payment/view/adminhtml/templates/info/default.phtml`** -> AI Confidence: **99.29%**
679. **`app/code/Magento/Payment/view/adminhtml/templates/info/instructions.phtml`** -> AI Confidence: **99.29%**
680. **`app/code/Magento/Payment/view/adminhtml/templates/info/pdf/default.phtml`** -> AI Confidence: **99.29%**
681. **`app/code/Magento/Payment/view/adminhtml/templates/info/substitution.phtml`** -> AI Confidence: **99.29%**
682. **`app/code/Magento/Payment/view/adminhtml/templates/transparent/info.phtml`** -> AI Confidence: **99.29%**
683. **`app/code/Magento/Payment/view/adminhtml/templates/transparent/redirect.phtml`** -> AI Confidence: **99.29%**
684. **`app/code/Magento/Payment/view/base/templates/info/pdf/default.phtml`** -> AI Confidence: **99.29%**
685. **`app/code/Magento/Payment/view/frontend/templates/info/default.phtml`** -> AI Confidence: **99.29%**
686. **`app/code/Magento/Payment/view/frontend/templates/info/instructions.phtml`** -> AI Confidence: **99.29%**
687. **`app/code/Magento/Payment/view/frontend/templates/info/pdf/default.phtml`** -> AI Confidence: **99.29%**
688. **`app/code/Magento/Payment/view/frontend/templates/transparent/info.phtml`** -> AI Confidence: **99.29%**
689. **`app/code/Magento/Payment/view/frontend/templates/transparent/redirect.phtml`** -> AI Confidence: **99.29%**
690. **`app/code/Magento/Paypal/view/adminhtml/templates/billing/agreement/form.phtml`** -> AI Confidence: **99.29%**
691. **`app/code/Magento/Paypal/view/adminhtml/templates/billing/agreement/view/tab/info.phtml`** -> AI Confidence: **99.29%**
692. **`app/code/Magento/Paypal/view/adminhtml/templates/payflowpro/vault.phtml`** -> AI Confidence: **99.29%**
693. **`app/code/Magento/Paypal/view/adminhtml/templates/payment/form/billing/agreement.phtml`** -> AI Confidence: **99.29%**
694. **`app/code/Magento/Paypal/view/adminhtml/templates/system/config/api_wizard.phtml`** -> AI Confidence: **99.29%**
695. **`app/code/Magento/Paypal/view/adminhtml/templates/system/config/bml_api_wizard.phtml`** -> AI Confidence: **99.29%**
696. **`app/code/Magento/Paypal/view/adminhtml/templates/system/config/fieldset/hint.phtml`** -> AI Confidence: **99.29%**
697. **`app/code/Magento/Paypal/view/frontend/templates/bml.phtml`** -> AI Confidence: **99.29%**
698. **`app/code/Magento/Paypal/view/frontend/templates/express/in-context/shortcut/button.phtml`** -> AI Confidence: **99.29%**
699. **`app/code/Magento/Paypal/view/frontend/templates/express/review.phtml`** -> AI Confidence: **99.29%**
700. **`app/code/Magento/Paypal/view/frontend/templates/express/review/shipping/method.phtml`** -> AI Confidence: **99.29%**
701. **`app/code/Magento/Paypal/view/frontend/templates/express/shortcut.phtml`** -> AI Confidence: **99.29%**
702. **`app/code/Magento/Paypal/view/frontend/templates/express/shortcut/container.phtml`** -> AI Confidence: **99.29%**
703. **`app/code/Magento/Paypal/view/frontend/templates/express/shortcut_button.phtml`** -> AI Confidence: **99.29%**
704. **`app/code/Magento/Paypal/view/frontend/templates/hss/form.phtml`** -> AI Confidence: **99.29%**
705. **`app/code/Magento/Paypal/view/frontend/templates/hss/info.phtml`** -> AI Confidence: **99.29%**
706. **`app/code/Magento/Paypal/view/frontend/templates/hss/review/button.phtml`** -> AI Confidence: **99.29%**
707. **`app/code/Magento/Paypal/view/frontend/templates/js/components.phtml`** -> AI Confidence: **99.29%**
708. **`app/code/Magento/Paypal/view/frontend/templates/partner/logo.phtml`** -> AI Confidence: **99.29%**
709. **`app/code/Magento/Paypal/view/frontend/templates/payflowadvanced/form.phtml`** -> AI Confidence: **99.29%**
710. **`app/code/Magento/Paypal/view/frontend/templates/payflowadvanced/info.phtml`** -> AI Confidence: **99.29%**
711. **`app/code/Magento/Paypal/view/frontend/templates/payflowlink/form.phtml`** -> AI Confidence: **99.29%**
712. **`app/code/Magento/Paypal/view/frontend/templates/payflowlink/info.phtml`** -> AI Confidence: **99.29%**
713. **`app/code/Magento/Paypal/view/frontend/templates/paylater/banner.phtml`** -> AI Confidence: **99.29%**
714. **`app/code/Magento/Paypal/view/frontend/templates/payment/form/billing/agreement.phtml`** -> AI Confidence: **99.29%**
715. **`app/code/Magento/Paypal/view/frontend/templates/payment/mark.phtml`** -> AI Confidence: **99.29%**
716. **`app/code/Magento/Paypal/view/frontend/templates/payment/redirect.phtml`** -> AI Confidence: **99.29%**
717. **`app/code/Magento/Persistent/view/frontend/templates/additional.phtml`** -> AI Confidence: **99.29%**
718. **`app/code/Magento/Persistent/view/frontend/templates/remember_me.phtml`** -> AI Confidence: **99.29%**
719. **`app/code/Magento/ProductAlert/view/frontend/templates/email/email.phtml`** -> AI Confidence: **99.29%**
720. **`app/code/Magento/ProductAlert/view/frontend/templates/email/price.phtml`** -> AI Confidence: **99.29%**
721. **`app/code/Magento/ProductAlert/view/frontend/templates/email/stock.phtml`** -> AI Confidence: **99.29%**
722. **`app/code/Magento/ProductAlert/view/frontend/templates/product/view.phtml`** -> AI Confidence: **99.29%**
723. **`app/code/Magento/ProductVideo/view/frontend/templates/product/view/gallery.phtml`** -> AI Confidence: **99.29%**
724. **`app/code/Magento/QuoteAnalytics/registration.php`** -> AI Confidence: **99.29%**
725. **`app/code/Magento/ReleaseNotification/registration.php`** -> AI Confidence: **99.29%**
726. **`app/code/Magento/RemoteStorage/registration.php`** -> AI Confidence: **99.29%**
727. **`app/code/Magento/Reports/view/adminhtml/templates/report/refresh/statistics.phtml`** -> AI Confidence: **99.29%**
728. **`app/code/Magento/Reports/view/adminhtml/templates/report/wishlist.phtml`** -> AI Confidence: **99.29%**
729. **`app/code/Magento/Reports/view/adminhtml/templates/store/switcher.phtml`** -> AI Confidence: **99.29%**
730. **`app/code/Magento/Reports/view/adminhtml/templates/store/switcher/enhanced.phtml`** -> AI Confidence: **99.29%**
731. **`app/code/Magento/Reports/view/frontend/templates/js/components.phtml`** -> AI Confidence: **99.29%**
732. **`app/code/Magento/Reports/view/frontend/templates/product/report_viewed_product.phtml`** -> AI Confidence: **99.29%**
733. **`app/code/Magento/Reports/view/frontend/templates/product/widget/viewed/item.phtml`** -> AI Confidence: **99.29%**
734. **`app/code/Magento/Reports/view/frontend/templates/widget/compared/column/compared_default_list.phtml`** -> AI Confidence: **99.29%**
735. **`app/code/Magento/Reports/view/frontend/templates/widget/compared/column/compared_images_list.phtml`** -> AI Confidence: **99.29%**
736. **`app/code/Magento/Reports/view/frontend/templates/widget/compared/content/compared_grid.phtml`** -> AI Confidence: **99.29%**
737. **`app/code/Magento/Reports/view/frontend/templates/widget/compared/content/compared_list.phtml`** -> AI Confidence: **99.29%**
738. **`app/code/Magento/Reports/view/frontend/templates/widget/viewed/column/viewed_default_list.phtml`** -> AI Confidence: **99.29%**
739. **`app/code/Magento/Reports/view/frontend/templates/widget/viewed/column/viewed_images_list.phtml`** -> AI Confidence: **99.29%**
740. **`app/code/Magento/Reports/view/frontend/templates/widget/viewed/content/viewed_grid.phtml`** -> AI Confidence: **99.29%**
741. **`app/code/Magento/Reports/view/frontend/templates/widget/viewed/content/viewed_list.phtml`** -> AI Confidence: **99.29%**
742. **`app/code/Magento/Review/view/adminhtml/templates/rating/detailed.phtml`** -> AI Confidence: **99.29%**
743. **`app/code/Magento/Review/view/adminhtml/templates/rating/options.phtml`** -> AI Confidence: **99.29%**
744. **`app/code/Magento/Review/view/adminhtml/templates/rating/stars/detailed.phtml`** -> AI Confidence: **99.29%**
745. **`app/code/Magento/Review/view/adminhtml/templates/rating/stars/summary.phtml`** -> AI Confidence: **99.29%**
746. **`app/code/Magento/Review/view/adminhtml/templates/rss/grid/link.phtml`** -> AI Confidence: **99.29%**
747. **`app/code/Magento/Review/view/frontend/templates/empty.phtml`** -> AI Confidence: **99.29%**
748. **`app/code/Magento/Review/view/frontend/templates/helper/summary.phtml`** -> AI Confidence: **99.29%**
749. **`app/code/Magento/Review/view/frontend/templates/helper/summary_short.phtml`** -> AI Confidence: **99.29%**
750. **`app/code/Magento/Review/view/frontend/templates/product/view/count.phtml`** -> AI Confidence: **99.29%**
751. **`app/code/Magento/Review/view/frontend/templates/product/view/other.phtml`** -> AI Confidence: **99.29%**
752. **`app/code/Magento/Review/view/frontend/templates/redirect.phtml`** -> AI Confidence: **99.29%**
753. **`app/code/Magento/Review/view/frontend/templates/review.phtml`** -> AI Confidence: **99.29%**
754. **`app/code/Magento/Review/view/frontend/templates/view.phtml`** -> AI Confidence: **99.29%**
755. **`app/code/Magento/ReviewAnalytics/registration.php`** -> AI Confidence: **99.29%**
756. **`app/code/Magento/Robots/view/frontend/templates/robots.phtml`** -> AI Confidence: **99.29%**
757. **`app/code/Magento/Rss/view/frontend/templates/feeds.phtml`** -> AI Confidence: **99.29%**
758. **`app/code/Magento/Sales/view/adminhtml/templates/items/column/name.phtml`** -> AI Confidence: **99.29%**
759. **`app/code/Magento/Sales/view/adminhtml/templates/items/column/qty.phtml`** -> AI Confidence: **99.29%**
760. **`app/code/Magento/Sales/view/adminhtml/templates/items/price/row.phtml`** -> AI Confidence: **99.29%**
761. **`app/code/Magento/Sales/view/adminhtml/templates/items/price/total.phtml`** -> AI Confidence: **99.29%**
762. **`app/code/Magento/Sales/view/adminhtml/templates/items/price/unit.phtml`** -> AI Confidence: **99.29%**
763. **`app/code/Magento/Sales/view/adminhtml/templates/items/renderer/default.phtml`** -> AI Confidence: **99.29%**
764. **`app/code/Magento/Sales/view/adminhtml/templates/order/create/abstract.phtml`** -> AI Confidence: **99.29%**
765. **`app/code/Magento/Sales/view/adminhtml/templates/order/create/form.phtml`** -> AI Confidence: **99.29%**
766. **`app/code/Magento/Sales/view/adminhtml/templates/order/create/form/address.phtml`** -> AI Confidence: **99.29%**
767. **`app/code/Magento/Sales/view/adminhtml/templates/order/create/giftmessage.phtml`** -> AI Confidence: **99.29%**
768. **`app/code/Magento/Sales/view/adminhtml/templates/order/create/items/price/row.phtml`** -> AI Confidence: **99.29%**
769. **`app/code/Magento/Sales/view/adminhtml/templates/order/create/items/price/total.phtml`** -> AI Confidence: **99.29%**
770. **`app/code/Magento/Sales/view/adminhtml/templates/order/create/items/price/unit.phtml`** -> AI Confidence: **99.29%**
771. **`app/code/Magento/Sales/view/adminhtml/templates/order/create/newsletter/form.phtml`** -> AI Confidence: **99.29%**
772. **`app/code/Magento/Sales/view/adminhtml/templates/order/create/sidebar/items.phtml`** -> AI Confidence: **99.29%**
773. **`app/code/Magento/Sales/view/adminhtml/templates/order/create/totals/default.phtml`** -> AI Confidence: **99.29%**
774. **`app/code/Magento/Sales/view/adminhtml/templates/order/create/totals/shipping.phtml`** -> AI Confidence: **99.29%**
775. **`app/code/Magento/Sales/view/adminhtml/templates/order/create/totals/tax.phtml`** -> AI Confidence: **99.29%**
776. **`app/code/Magento/Sales/view/adminhtml/templates/order/creditmemo/create/form.phtml`** -> AI Confidence: **99.29%**
777. **`app/code/Magento/Sales/view/adminhtml/templates/order/creditmemo/create/items/renderer/default.phtml`** -> AI Confidence: **99.29%**
778. **`app/code/Magento/Sales/view/adminhtml/templates/order/details.phtml`** -> AI Confidence: **99.29%**
779. **`app/code/Magento/Sales/view/adminhtml/templates/order/giftoptions.phtml`** -> AI Confidence: **99.29%**
780. **`app/code/Magento/Sales/view/adminhtml/templates/order/invoice/create/form.phtml`** -> AI Confidence: **99.29%**
781. **`app/code/Magento/Sales/view/adminhtml/templates/order/invoice/create/items/renderer/default.phtml`** -> AI Confidence: **99.29%**
782. **`app/code/Magento/Sales/view/adminhtml/templates/order/totalbar.phtml`** -> AI Confidence: **99.29%**
783. **`app/code/Magento/Sales/view/adminhtml/templates/order/totals.phtml`** -> AI Confidence: **99.29%**
784. **`app/code/Magento/Sales/view/adminhtml/templates/order/totals/discount.phtml`** -> AI Confidence: **99.29%**
785. **`app/code/Magento/Sales/view/adminhtml/templates/order/totals/due.phtml`** -> AI Confidence: **99.29%**
786. **`app/code/Magento/Sales/view/adminhtml/templates/order/totals/footer.phtml`** -> AI Confidence: **99.29%**
787. **`app/code/Magento/Sales/view/adminhtml/templates/order/totals/grand.phtml`** -> AI Confidence: **99.29%**
788. **`app/code/Magento/Sales/view/adminhtml/templates/order/totals/item.phtml`** -> AI Confidence: **99.29%**
789. **`app/code/Magento/Sales/view/adminhtml/templates/order/totals/main.phtml`** -> AI Confidence: **99.29%**
790. **`app/code/Magento/Sales/view/adminhtml/templates/order/totals/paid.phtml`** -> AI Confidence: **99.29%**
791. **`app/code/Magento/Sales/view/adminhtml/templates/order/totals/refunded.phtml`** -> AI Confidence: **99.29%**
792. **`app/code/Magento/Sales/view/adminhtml/templates/order/totals/shipping.phtml`** -> AI Confidence: **99.29%**
793. **`app/code/Magento/Sales/view/adminhtml/templates/order/totals/tax.phtml`** -> AI Confidence: **99.29%**
794. **`app/code/Magento/Sales/view/adminhtml/templates/order/view/giftmessage.phtml`** -> AI Confidence: **99.29%**
795. **`app/code/Magento/Sales/view/adminhtml/templates/order/view/info.phtml`** -> AI Confidence: **99.29%**
796. **`app/code/Magento/Sales/view/adminhtml/templates/order/view/items.phtml`** -> AI Confidence: **99.29%**
797. **`app/code/Magento/Sales/view/adminhtml/templates/order/view/items/renderer/default.phtml`** -> AI Confidence: **99.29%**
798. **`app/code/Magento/Sales/view/adminhtml/templates/page/js/components.phtml`** -> AI Confidence: **99.29%**
799. **`app/code/Magento/Sales/view/adminhtml/templates/rss/order/grid/link.phtml`** -> AI Confidence: **99.29%**
800. **`app/code/Magento/Sales/view/adminhtml/templates/transactions/detail.phtml`** -> AI Confidence: **99.29%**
801. **`app/code/Magento/Sales/view/frontend/templates/email/creditmemo/items.phtml`** -> AI Confidence: **99.29%**
802. **`app/code/Magento/Sales/view/frontend/templates/email/invoice/items.phtml`** -> AI Confidence: **99.29%**
803. **`app/code/Magento/Sales/view/frontend/templates/email/items.phtml`** -> AI Confidence: **99.29%**
804. **`app/code/Magento/Sales/view/frontend/templates/email/items/creditmemo/default.phtml`** -> AI Confidence: **99.29%**
805. **`app/code/Magento/Sales/view/frontend/templates/email/items/invoice/default.phtml`** -> AI Confidence: **99.29%**
806. **`app/code/Magento/Sales/view/frontend/templates/email/items/order/default.phtml`** -> AI Confidence: **99.29%**
807. **`app/code/Magento/Sales/view/frontend/templates/email/items/price/row.phtml`** -> AI Confidence: **99.29%**
808. **`app/code/Magento/Sales/view/frontend/templates/email/items/shipment/default.phtml`** -> AI Confidence: **99.29%**
809. **`app/code/Magento/Sales/view/frontend/templates/email/shipment/items.phtml`** -> AI Confidence: **99.29%**
810. **`app/code/Magento/Sales/view/frontend/templates/email/shipment/track.phtml`** -> AI Confidence: **99.29%**
811. **`app/code/Magento/Sales/view/frontend/templates/items/price/total_after_discount.phtml`** -> AI Confidence: **99.29%**
812. **`app/code/Magento/Sales/view/frontend/templates/js/components.phtml`** -> AI Confidence: **99.29%**
813. **`app/code/Magento/Sales/view/frontend/templates/order/creditmemo/items.phtml`** -> AI Confidence: **99.29%**
814. **`app/code/Magento/Sales/view/frontend/templates/order/creditmemo/items/renderer/default.phtml`** -> AI Confidence: **99.29%**
815. **`app/code/Magento/Sales/view/frontend/templates/order/history.phtml`** -> AI Confidence: **99.29%**
816. **`app/code/Magento/Sales/view/frontend/templates/order/info/buttons.phtml`** -> AI Confidence: **99.29%**
817. **`app/code/Magento/Sales/view/frontend/templates/order/info/buttons/rss.phtml`** -> AI Confidence: **99.29%**
818. **`app/code/Magento/Sales/view/frontend/templates/order/invoice/items.phtml`** -> AI Confidence: **99.29%**
819. **`app/code/Magento/Sales/view/frontend/templates/order/invoice/items/renderer/default.phtml`** -> AI Confidence: **99.29%**
820. **`app/code/Magento/Sales/view/frontend/templates/order/items.phtml`** -> AI Confidence: **99.29%**
821. **`app/code/Magento/Sales/view/frontend/templates/order/items/renderer/default.phtml`** -> AI Confidence: **99.29%**
822. **`app/code/Magento/Sales/view/frontend/templates/order/order_status.phtml`** -> AI Confidence: **99.29%**
823. **`app/code/Magento/Sales/view/frontend/templates/order/recent.phtml`** -> AI Confidence: **99.29%**
824. **`app/code/Magento/Sales/view/frontend/templates/order/shipment/items/renderer/default.phtml`** -> AI Confidence: **99.29%**
825. **`app/code/Magento/Sales/view/frontend/templates/order/totals.phtml`** -> AI Confidence: **99.29%**
826. **`app/code/Magento/SalesAnalytics/registration.php`** -> AI Confidence: **99.29%**
827. **`app/code/Magento/SalesRule/view/adminhtml/templates/tab/coupons.phtml`** -> AI Confidence: **99.29%**
828. **`app/code/Magento/SampleData/cli_commands.php`** -> AI Confidence: **99.29%**
829. **`app/code/Magento/Search/view/frontend/templates/form.mini.phtml`** -> AI Confidence: **99.29%**
830. **`app/code/Magento/Search/view/frontend/templates/term.phtml`** -> AI Confidence: **99.29%**
831. **`app/code/Magento/Security/view/adminhtml/templates/page/activity_link.phtml`** -> AI Confidence: **99.29%**
832. **`app/code/Magento/Security/view/adminhtml/templates/session/activity.phtml`** -> AI Confidence: **99.29%**
833. **`app/code/Magento/Security/view/adminhtml/templates/system/config/session_size_admin/modal_content_body.phtml`** -> AI Confidence: **99.29%**
834. **`app/code/Magento/Security/view/adminhtml/templates/system/config/session_size_storefront/modal_content_body.phtml`** -> AI Confidence: **99.29%**
835. **`app/code/Magento/Shipping/view/adminhtml/templates/create/form.phtml`** -> AI Confidence: **99.29%**
836. **`app/code/Magento/Shipping/view/adminhtml/templates/create/items/renderer/default.phtml`** -> AI Confidence: **99.29%**
837. **`app/code/Magento/Shipping/view/adminhtml/templates/order/packaging/grid.phtml`** -> AI Confidence: **99.29%**
838. **`app/code/Magento/Shipping/view/adminhtml/templates/order/packaging/packed.phtml`** -> AI Confidence: **99.29%**
839. **`app/code/Magento/Shipping/view/adminhtml/templates/order/view/info.phtml`** -> AI Confidence: **99.29%**
840. **`app/code/Magento/Shipping/view/adminhtml/templates/view/items.phtml`** -> AI Confidence: **99.29%**
841. **`app/code/Magento/Shipping/view/frontend/templates/items.phtml`** -> AI Confidence: **99.29%**
842. **`app/code/Magento/Shipping/view/frontend/templates/tracking/details.phtml`** -> AI Confidence: **99.29%**
843. **`app/code/Magento/Shipping/view/frontend/templates/tracking/link.phtml`** -> AI Confidence: **99.29%**
844. **`app/code/Magento/Shipping/view/frontend/templates/tracking/progress.phtml`** -> AI Confidence: **99.29%**
845. **`app/code/Magento/Sitemap/view/adminhtml/templates/js.phtml`** -> AI Confidence: **99.29%**
846. **`app/code/Magento/Store/view/frontend/templates/switch/flags.phtml`** -> AI Confidence: **99.29%**
847. **`app/code/Magento/Store/view/frontend/templates/switch/languages.phtml`** -> AI Confidence: **99.29%**
848. **`app/code/Magento/Store/view/frontend/templates/switch/stores.phtml`** -> AI Confidence: **99.29%**
849. **`app/code/Magento/Swagger/view/frontend/templates/swagger-ui/index.phtml`** -> AI Confidence: **99.29%**
850. **`app/code/Magento/Swatches/view/adminhtml/templates/catalog/product/attribute/js.phtml`** -> AI Confidence: **99.29%**
851. **`app/code/Magento/Swatches/view/frontend/templates/product/view/renderer.phtml`** -> AI Confidence: **99.29%**
852. **`app/code/Magento/Tax/view/adminhtml/templates/items/price/row.phtml`** -> AI Confidence: **99.29%**
853. **`app/code/Magento/Tax/view/adminhtml/templates/items/price/total.phtml`** -> AI Confidence: **99.29%**
854. **`app/code/Magento/Tax/view/adminhtml/templates/items/price/unit.phtml`** -> AI Confidence: **99.29%**
855. **`app/code/Magento/Tax/view/adminhtml/templates/order/create/items/price/row.phtml`** -> AI Confidence: **99.29%**
856. **`app/code/Magento/Tax/view/adminhtml/templates/order/create/items/price/total.phtml`** -> AI Confidence: **99.29%**
857. **`app/code/Magento/Tax/view/adminhtml/templates/order/create/items/price/unit.phtml`** -> AI Confidence: **99.29%**
858. **`app/code/Magento/Tax/view/adminhtml/templates/rate/form.phtml`** -> AI Confidence: **99.29%**
859. **`app/code/Magento/Tax/view/adminhtml/templates/toolbar/class/add.phtml`** -> AI Confidence: **99.29%**
860. **`app/code/Magento/Tax/view/adminhtml/templates/toolbar/rate/add.phtml`** -> AI Confidence: **99.29%**
861. **`app/code/Magento/Tax/view/adminhtml/templates/toolbar/rule/add.phtml`** -> AI Confidence: **99.29%**
862. **`app/code/Magento/Tax/view/base/templates/pricing/adjustment.phtml`** -> AI Confidence: **99.29%**
863. **`app/code/Magento/Tax/view/base/templates/pricing/adjustment/bundle.phtml`** -> AI Confidence: **99.29%**
864. **`app/code/Magento/Tax/view/frontend/templates/email/items/price/row.phtml`** -> AI Confidence: **99.29%**
865. **`app/code/Magento/Tax/view/frontend/templates/item/price/row.phtml`** -> AI Confidence: **99.29%**
866. **`app/code/Magento/Tax/view/frontend/templates/item/price/total_after_discount.phtml`** -> AI Confidence: **99.29%**
867. **`app/code/Magento/Tax/view/frontend/templates/item/price/unit.phtml`** -> AI Confidence: **99.29%**
868. **`app/code/Magento/Tax/view/frontend/templates/order/tax.phtml`** -> AI Confidence: **99.29%**
869. **`app/code/Magento/TaxImportExport/view/adminhtml/templates/importExportHeader.phtml`** -> AI Confidence: **99.29%**
870. **`app/code/Magento/Theme/view/adminhtml/templates/browser/content.phtml`** -> AI Confidence: **99.29%**
871. **`app/code/Magento/Theme/view/adminhtml/templates/browser/content/files.phtml`** -> AI Confidence: **99.29%**
872. **`app/code/Magento/Theme/view/adminhtml/templates/title.phtml`** -> AI Confidence: **99.29%**
873. **`app/code/Magento/Theme/view/base/templates/root.phtml`** -> AI Confidence: **99.29%**
874. **`app/code/Magento/Theme/view/frontend/templates/callouts/left_col.phtml`** -> AI Confidence: **99.29%**
875. **`app/code/Magento/Theme/view/frontend/templates/callouts/right_col.phtml`** -> AI Confidence: **99.29%**
876. **`app/code/Magento/Theme/view/frontend/templates/html/absolute_footer.phtml`** -> AI Confidence: **99.29%**
877. **`app/code/Magento/Theme/view/frontend/templates/html/block.phtml`** -> AI Confidence: **99.29%**
878. **`app/code/Magento/Theme/view/frontend/templates/html/breadcrumbs.phtml`** -> AI Confidence: **99.29%**
879. **`app/code/Magento/Theme/view/frontend/templates/html/bugreport.phtml`** -> AI Confidence: **99.29%**
880. **`app/code/Magento/Theme/view/frontend/templates/html/collapsible.phtml`** -> AI Confidence: **99.29%**
881. **`app/code/Magento/Theme/view/frontend/templates/html/container.phtml`** -> AI Confidence: **99.29%**
882. **`app/code/Magento/Theme/view/frontend/templates/html/copyright.phtml`** -> AI Confidence: **99.29%**
883. **`app/code/Magento/Theme/view/frontend/templates/html/header.phtml`** -> AI Confidence: **99.29%**
884. **`app/code/Magento/Theme/view/frontend/templates/html/header/criticalCss.phtml`** -> AI Confidence: **99.29%**
885. **`app/code/Magento/Theme/view/frontend/templates/html/header/logo.phtml`** -> AI Confidence: **99.29%**
886. **`app/code/Magento/Theme/view/frontend/templates/html/main_css_preloader.phtml`** -> AI Confidence: **99.29%**
887. **`app/code/Magento/Theme/view/frontend/templates/html/messages.phtml`** -> AI Confidence: **99.29%**
888. **`app/code/Magento/Theme/view/frontend/templates/html/notices.phtml`** -> AI Confidence: **99.29%**
889. **`app/code/Magento/Theme/view/frontend/templates/html/pager.phtml`** -> AI Confidence: **99.29%**
890. **`app/code/Magento/Theme/view/frontend/templates/html/print.phtml`** -> AI Confidence: **99.29%**
891. **`app/code/Magento/Theme/view/frontend/templates/html/sections.phtml`** -> AI Confidence: **99.29%**
892. **`app/code/Magento/Theme/view/frontend/templates/html/skip.phtml`** -> AI Confidence: **99.29%**
893. **`app/code/Magento/Theme/view/frontend/templates/html/skiptarget.phtml`** -> AI Confidence: **99.29%**
894. **`app/code/Magento/Theme/view/frontend/templates/html/title.phtml`** -> AI Confidence: **99.29%**
895. **`app/code/Magento/Theme/view/frontend/templates/html/topmenu.phtml`** -> AI Confidence: **99.29%**
896. **`app/code/Magento/Theme/view/frontend/templates/js/components.phtml`** -> AI Confidence: **99.29%**
897. **`app/code/Magento/Theme/view/frontend/templates/js/cookie.phtml`** -> AI Confidence: **99.29%**
898. **`app/code/Magento/Theme/view/frontend/templates/js/cookie_status.phtml`** -> AI Confidence: **99.29%**
899. **`app/code/Magento/Theme/view/frontend/templates/js/css_rel_preload.phtml`** -> AI Confidence: **99.29%**
900. **`app/code/Magento/Theme/view/frontend/templates/link.phtml`** -> AI Confidence: **99.29%**
901. **`app/code/Magento/Theme/view/frontend/templates/template.phtml`** -> AI Confidence: **99.29%**
902. **`app/code/Magento/Translation/view/base/templates/translate.phtml`** -> AI Confidence: **99.29%**
903. **`app/code/Magento/Ui/view/base/templates/container/content/default.phtml`** -> AI Confidence: **99.29%**
904. **`app/code/Magento/Ui/view/base/templates/context/default.phtml`** -> AI Confidence: **99.29%**
905. **`app/code/Magento/Ui/view/base/templates/control/button/default.phtml`** -> AI Confidence: **99.29%**
906. **`app/code/Magento/Ui/view/base/templates/control/button/split.phtml`** -> AI Confidence: **99.29%**
907. **`app/code/Magento/Ui/view/base/templates/label/default.phtml`** -> AI Confidence: **99.29%**
908. **`app/code/Magento/Ui/view/base/templates/logger.phtml`** -> AI Confidence: **99.29%**
909. **`app/code/Magento/Ui/view/base/templates/wysiwyg/active_editor.phtml`** -> AI Confidence: **99.29%**
910. **`app/code/Magento/UrlRewrite/view/adminhtml/templates/categories.phtml`** -> AI Confidence: **99.29%**
911. **`app/code/Magento/UrlRewrite/view/adminhtml/templates/edit.phtml`** -> AI Confidence: **99.29%**
912. **`app/code/Magento/UrlRewrite/view/adminhtml/templates/messages/url_duplicate_message.phtml`** -> AI Confidence: **99.29%**
913. **`app/code/Magento/Variable/view/adminhtml/templates/system/variable/js.phtml`** -> AI Confidence: **99.29%**
914. **`app/code/Magento/Vault/view/adminhtml/templates/form/vault.phtml`** -> AI Confidence: **99.29%**
915. **`app/code/Magento/Weee/view/adminhtml/templates/items/price/row.phtml`** -> AI Confidence: **99.29%**
916. **`app/code/Magento/Weee/view/adminhtml/templates/items/price/total.phtml`** -> AI Confidence: **99.29%**
917. **`app/code/Magento/Weee/view/adminhtml/templates/items/price/unit.phtml`** -> AI Confidence: **99.29%**
918. **`app/code/Magento/Weee/view/adminhtml/templates/order/create/items/price/row.phtml`** -> AI Confidence: **99.29%**
919. **`app/code/Magento/Weee/view/adminhtml/templates/order/create/items/price/total.phtml`** -> AI Confidence: **99.29%**
920. **`app/code/Magento/Weee/view/adminhtml/templates/order/create/items/price/unit.phtml`** -> AI Confidence: **99.29%**
921. **`app/code/Magento/Weee/view/adminhtml/templates/renderer/tax.phtml`** -> AI Confidence: **99.29%**
922. **`app/code/Magento/Weee/view/base/templates/pricing/adjustment.phtml`** -> AI Confidence: **99.29%**
923. **`app/code/Magento/Weee/view/frontend/templates/email/items/price/row.phtml`** -> AI Confidence: **99.29%**
924. **`app/code/Magento/Weee/view/frontend/templates/item/price/row.phtml`** -> AI Confidence: **99.29%**
925. **`app/code/Magento/Weee/view/frontend/templates/item/price/total_after_discount.phtml`** -> AI Confidence: **99.29%**
926. **`app/code/Magento/Weee/view/frontend/templates/item/price/unit.phtml`** -> AI Confidence: **99.29%**
927. **`app/code/Magento/Wishlist/view/adminhtml/templates/customer/edit/tab/wishlist.phtml`** -> AI Confidence: **99.29%**
928. **`app/code/Magento/Wishlist/view/base/templates/product/price/bundle/configured_price.phtml`** -> AI Confidence: **99.29%**
929. **`app/code/Magento/Wishlist/view/base/templates/product/price/configurable/configured_price.phtml`** -> AI Confidence: **99.29%**
930. **`app/code/Magento/Wishlist/view/frontend/templates/addto.phtml`** -> AI Confidence: **99.29%**
931. **`app/code/Magento/Wishlist/view/frontend/templates/button/share.phtml`** -> AI Confidence: **99.29%**
932. **`app/code/Magento/Wishlist/view/frontend/templates/button/tocart.phtml`** -> AI Confidence: **99.29%**
933. **`app/code/Magento/Wishlist/view/frontend/templates/button/update.phtml`** -> AI Confidence: **99.29%**
934. **`app/code/Magento/Wishlist/view/frontend/templates/cart/item/renderer/actions/move_to_wishlist.phtml`** -> AI Confidence: **99.29%**
935. **`app/code/Magento/Wishlist/view/frontend/templates/catalog/product/list/addto/wishlist.phtml`** -> AI Confidence: **99.29%**
936. **`app/code/Magento/Wishlist/view/frontend/templates/catalog/product/view/addto/wishlist.phtml`** -> AI Confidence: **99.29%**
937. **`app/code/Magento/Wishlist/view/frontend/templates/email/items.phtml`** -> AI Confidence: **99.29%**
938. **`app/code/Magento/Wishlist/view/frontend/templates/item/column/actions.phtml`** -> AI Confidence: **99.29%**
939. **`app/code/Magento/Wishlist/view/frontend/templates/item/column/cart.phtml`** -> AI Confidence: **99.29%**
940. **`app/code/Magento/Wishlist/view/frontend/templates/item/column/edit.phtml`** -> AI Confidence: **99.29%**
941. **`app/code/Magento/Wishlist/view/frontend/templates/item/column/image.phtml`** -> AI Confidence: **99.29%**
942. **`app/code/Magento/Wishlist/view/frontend/templates/item/column/name.phtml`** -> AI Confidence: **99.29%**
943. **`app/code/Magento/Wishlist/view/frontend/templates/item/column/price.phtml`** -> AI Confidence: **99.29%**
944. **`app/code/Magento/Wishlist/view/frontend/templates/item/column/remove.phtml`** -> AI Confidence: **99.29%**
945. **`app/code/Magento/Wishlist/view/frontend/templates/item/column/review.phtml`** -> AI Confidence: **99.29%**
946. **`app/code/Magento/Wishlist/view/frontend/templates/item/configure/addto.phtml`** -> AI Confidence: **99.29%**
947. **`app/code/Magento/Wishlist/view/frontend/templates/item/configure/addto/wishlist.phtml`** -> AI Confidence: **99.29%**
948. **`app/code/Magento/Wishlist/view/frontend/templates/item/list.phtml`** -> AI Confidence: **99.29%**
949. **`app/code/Magento/Wishlist/view/frontend/templates/js/components.phtml`** -> AI Confidence: **99.29%**
950. **`app/code/Magento/Wishlist/view/frontend/templates/messages/addProductSuccessMessage.phtml`** -> AI Confidence: **99.29%**
951. **`app/code/Magento/Wishlist/view/frontend/templates/messages/removeWishlistItemSuccessMessage.phtml`** -> AI Confidence: **99.29%**
952. **`app/code/Magento/Wishlist/view/frontend/templates/options_list.phtml`** -> AI Confidence: **99.29%**
953. **`app/code/Magento/Wishlist/view/frontend/templates/rss/email.phtml`** -> AI Confidence: **99.29%**
954. **`app/code/Magento/Wishlist/view/frontend/templates/rss/wishlist.phtml`** -> AI Confidence: **99.29%**
955. **`app/code/Magento/Wishlist/view/frontend/templates/shared.phtml`** -> AI Confidence: **99.29%**
956. **`app/code/Magento/Wishlist/view/frontend/templates/view.phtml`** -> AI Confidence: **99.29%**
957. **`app/code/Magento/WishlistAnalytics/registration.php`** -> AI Confidence: **99.29%**
958. **`app/design/frontend/Magento/luma/Magento_LayeredNavigation/templates/layer/state.phtml`** -> AI Confidence: **99.29%**
959. **`app/design/frontend/Magento/luma/Magento_LayeredNavigation/templates/layer/view.phtml`** -> AI Confidence: **99.29%**
960. **`dev/tests/integration/_files/Magento/TestModuleCspUtil/view/frontend/templates/helper.phtml`** -> AI Confidence: **99.29%**
961. **`dev/tests/integration/_files/Magento/TestModuleCspUtil/view/frontend/templates/secure.phtml`** -> AI Confidence: **99.29%**
962. **`dev/tests/integration/_files/Magento/TestModuleSecureHtmlRenderer/view/frontend/templates/helper.phtml`** -> AI Confidence: **99.29%**
963. **`dev/tests/integration/testsuite/Magento/Analytics/_files/create_link.php`** -> AI Confidence: **99.29%**
964. **`dev/tests/integration/testsuite/Magento/Backend/Block/_files/form_key_disabled.php`** -> AI Confidence: **99.29%**
965. **`dev/tests/integration/testsuite/Magento/Backend/Block/_files/form_key_disabled_rollback.php`** -> AI Confidence: **99.29%**
966. **`dev/tests/integration/testsuite/Magento/Backend/controllers/_files/cache/all_types_invalidated.php`** -> AI Confidence: **99.29%**
967. **`dev/tests/integration/testsuite/Magento/Backend/controllers/_files/cache/application_cache.php`** -> AI Confidence: **99.29%**
968. **`dev/tests/integration/testsuite/Magento/Backend/controllers/_files/cache/empty_storage.php`** -> AI Confidence: **99.29%**
969. **`dev/tests/integration/testsuite/Magento/Bundle/_files/multiple_products_rollback.php`** -> AI Confidence: **99.29%**
970. **`dev/tests/integration/testsuite/Magento/Captcha/_files/dummy_user.php`** -> AI Confidence: **99.29%**
971. **`dev/tests/integration/testsuite/Magento/Catalog/Model/Category/_files/category_without_image.php`** -> AI Confidence: **99.29%**
972. **`dev/tests/integration/testsuite/Magento/Catalog/Model/Category/_files/service_category_create.php`** -> AI Confidence: **99.29%**
973. **`dev/tests/integration/testsuite/Magento/Catalog/Model/Layer/Filter/Price/_files/_algorithm_base_data.php`** -> AI Confidence: **99.29%**
974. **`dev/tests/integration/testsuite/Magento/Catalog/Model/Layer/Filter/Price/_files/products_advanced_rollback.php`** -> AI Confidence: **99.29%**
975. **`dev/tests/integration/testsuite/Magento/Catalog/Model/Layer/Filter/_files/attribute_weight_filterable.php`** -> AI Confidence: **99.29%**
976. **`dev/tests/integration/testsuite/Magento/Catalog/Model/Layer/Filter/_files/attribute_with_option_rollback.php`** -> AI Confidence: **99.29%**
977. **`dev/tests/integration/testsuite/Magento/Catalog/Model/Product/Attribute/_files/create_attribute_service.php`** -> AI Confidence: **99.29%**
978. **`dev/tests/integration/testsuite/Magento/Catalog/Model/Product/Attribute/_files/select_attribute.php`** -> AI Confidence: **99.29%**
979. **`dev/tests/integration/testsuite/Magento/Catalog/Model/Product/Attribute/_files/select_attribute_rollback.php`** -> AI Confidence: **99.29%**
980. **`dev/tests/integration/testsuite/Magento/Catalog/Model/Product/_files/service_product_create.php`** -> AI Confidence: **99.29%**
981. **`dev/tests/integration/testsuite/Magento/Catalog/_files/attribute_set_based_on_default.php`** -> AI Confidence: **99.29%**
982. **`dev/tests/integration/testsuite/Magento/Catalog/_files/attribute_set_based_on_default_rollback.php`** -> AI Confidence: **99.29%**
983. **`dev/tests/integration/testsuite/Magento/Catalog/_files/attribute_set_based_on_default_set.php`** -> AI Confidence: **99.29%**
984. **`dev/tests/integration/testsuite/Magento/Catalog/_files/attribute_set_with_image_attribute.php`** -> AI Confidence: **99.29%**
985. **`dev/tests/integration/testsuite/Magento/Catalog/_files/attribute_set_with_image_attribute_rollback.php`** -> AI Confidence: **99.29%**
986. **`dev/tests/integration/testsuite/Magento/Catalog/_files/catalog_category_with_apostrophe.php`** -> AI Confidence: **99.29%**
987. **`dev/tests/integration/testsuite/Magento/Catalog/_files/catalog_category_with_apostrophe_rollback.php`** -> AI Confidence: **99.29%**
988. **`dev/tests/integration/testsuite/Magento/Catalog/_files/catalog_category_with_image_rollback.php`** -> AI Confidence: **99.29%**
989. **`dev/tests/integration/testsuite/Magento/Catalog/_files/catalog_category_with_long_image_name_rollback.php`** -> AI Confidence: **99.29%**
990. **`dev/tests/integration/testsuite/Magento/Catalog/_files/catalog_category_with_slash.php`** -> AI Confidence: **99.29%**
991. **`dev/tests/integration/testsuite/Magento/Catalog/_files/categories_no_products.php`** -> AI Confidence: **99.29%**
992. **`dev/tests/integration/testsuite/Magento/Catalog/_files/categories_no_products_rollback.php`** -> AI Confidence: **99.29%**
993. **`dev/tests/integration/testsuite/Magento/Catalog/_files/category.php`** -> AI Confidence: **99.29%**
994. **`dev/tests/integration/testsuite/Magento/Catalog/_files/category_backend_rollback.php`** -> AI Confidence: **99.29%**
995. **`dev/tests/integration/testsuite/Magento/Catalog/_files/category_duplicates.php`** -> AI Confidence: **99.29%**
996. **`dev/tests/integration/testsuite/Magento/Catalog/_files/category_product.php`** -> AI Confidence: **99.29%**
997. **`dev/tests/integration/testsuite/Magento/Catalog/_files/category_product_rollback.php`** -> AI Confidence: **99.29%**
998. **`dev/tests/integration/testsuite/Magento/Catalog/_files/category_rollback.php`** -> AI Confidence: **99.29%**
999. **`dev/tests/integration/testsuite/Magento/Catalog/_files/category_tree_rollback.php`** -> AI Confidence: **99.29%**
1000. **`dev/tests/integration/testsuite/Magento/Catalog/_files/category_with_position.php`** -> AI Confidence: **99.29%**
1001. **`dev/tests/integration/testsuite/Magento/Catalog/_files/category_with_position_rollback.php`** -> AI Confidence: **99.29%**
1002. **`dev/tests/integration/testsuite/Magento/Catalog/_files/category_with_two_stores_rollback.php`** -> AI Confidence: **99.29%**
1003. **`dev/tests/integration/testsuite/Magento/Catalog/_files/configurable_attribute_rollback.php`** -> AI Confidence: **99.29%**
1004. **`dev/tests/integration/testsuite/Magento/Catalog/_files/dropdown_attribute.php`** -> AI Confidence: **99.29%**
1005. **`dev/tests/integration/testsuite/Magento/Catalog/_files/dropdown_attribute_rollback.php`** -> AI Confidence: **99.29%**
1006. **`dev/tests/integration/testsuite/Magento/Catalog/_files/empty_attribute_group.php`** -> AI Confidence: **99.29%**
1007. **`dev/tests/integration/testsuite/Magento/Catalog/_files/empty_attribute_group_rollback.php`** -> AI Confidence: **99.29%**
1008. **`dev/tests/integration/testsuite/Magento/Catalog/_files/enable_reindex_schedule.php`** -> AI Confidence: **99.29%**
1009. **`dev/tests/integration/testsuite/Magento/Catalog/_files/enable_reindex_schedule_rollback.php`** -> AI Confidence: **99.29%**
1010. **`dev/tests/integration/testsuite/Magento/Catalog/_files/filterable_attributes.php`** -> AI Confidence: **99.29%**
1011. **`dev/tests/integration/testsuite/Magento/Catalog/_files/indexer_catalog_category.php`** -> AI Confidence: **99.29%**
1012. **`dev/tests/integration/testsuite/Magento/Catalog/_files/indexer_catalog_category_rollback.php`** -> AI Confidence: **99.29%**
1013. **`dev/tests/integration/testsuite/Magento/Catalog/_files/indexer_catalog_products.php`** -> AI Confidence: **99.29%**
1014. **`dev/tests/integration/testsuite/Magento/Catalog/_files/indexer_catalog_products_rollback.php`** -> AI Confidence: **99.29%**
1015. **`dev/tests/integration/testsuite/Magento/Catalog/_files/multiple_products.php`** -> AI Confidence: **99.29%**
1016. **`dev/tests/integration/testsuite/Magento/Catalog/_files/multiple_products_rollback.php`** -> AI Confidence: **99.29%**
1017. **`dev/tests/integration/testsuite/Magento/Catalog/_files/multiple_products_staged.php`** -> AI Confidence: **99.29%**
1018. **`dev/tests/integration/testsuite/Magento/Catalog/_files/multiple_products_staged_rollback.php`** -> AI Confidence: **99.29%**
1019. **`dev/tests/integration/testsuite/Magento/Catalog/_files/multiple_products_with_different_sku_and_name.php`** -> AI Confidence: **99.29%**
1020. **`dev/tests/integration/testsuite/Magento/Catalog/_files/multiple_products_with_different_sku_and_name_rollback.php`** -> AI Confidence: **99.29%**
1021. **`dev/tests/integration/testsuite/Magento/Catalog/_files/multiselect_attribute.php`** -> AI Confidence: **99.29%**
1022. **`dev/tests/integration/testsuite/Magento/Catalog/_files/multiselect_attribute_rollback.php`** -> AI Confidence: **99.29%**
1023. **`dev/tests/integration/testsuite/Magento/Catalog/_files/multiselect_attribute_with_incorrect_values.php`** -> AI Confidence: **99.29%**
1024. **`dev/tests/integration/testsuite/Magento/Catalog/_files/multiselect_attribute_with_source_model.php`** -> AI Confidence: **99.29%**
1025. **`dev/tests/integration/testsuite/Magento/Catalog/_files/multiselect_attribute_with_source_model_rollback.php`** -> AI Confidence: **99.29%**
1026. **`dev/tests/integration/testsuite/Magento/Catalog/_files/price_row_fixture.php`** -> AI Confidence: **99.29%**
1027. **`dev/tests/integration/testsuite/Magento/Catalog/_files/product_associated.php`** -> AI Confidence: **99.29%**
1028. **`dev/tests/integration/testsuite/Magento/Catalog/_files/product_attribute.php`** -> AI Confidence: **99.29%**
1029. **`dev/tests/integration/testsuite/Magento/Catalog/_files/product_attribute_rollback.php`** -> AI Confidence: **99.29%**
1030. **`dev/tests/integration/testsuite/Magento/Catalog/_files/product_attribute_with_invalid_apply_to.php`** -> AI Confidence: **99.29%**
1031. **`dev/tests/integration/testsuite/Magento/Catalog/_files/product_group_prices_rollback.php`** -> AI Confidence: **99.29%**
1032. **`dev/tests/integration/testsuite/Magento/Catalog/_files/product_has_tier_price_show_as_low_as_rollback.php`** -> AI Confidence: **99.29%**
1033. **`dev/tests/integration/testsuite/Magento/Catalog/_files/product_in_multiple_categories_rollback.php`** -> AI Confidence: **99.29%**
1034. **`dev/tests/integration/testsuite/Magento/Catalog/_files/product_price_attribute_rollback.php`** -> AI Confidence: **99.29%**
1035. **`dev/tests/integration/testsuite/Magento/Catalog/_files/product_simple_duplicated.php`** -> AI Confidence: **99.29%**
1036. **`dev/tests/integration/testsuite/Magento/Catalog/_files/product_simple_duplicated_rollback.php`** -> AI Confidence: **99.29%**
1037. **`dev/tests/integration/testsuite/Magento/Catalog/_files/product_simple_with_spaces_in_url_key.php`** -> AI Confidence: **99.29%**
1038. **`dev/tests/integration/testsuite/Magento/Catalog/_files/product_simple_with_url_key.php`** -> AI Confidence: **99.29%**
1039. **`dev/tests/integration/testsuite/Magento/Catalog/_files/product_simple_xss.php`** -> AI Confidence: **99.29%**
1040. **`dev/tests/integration/testsuite/Magento/Catalog/_files/product_simple_xss_rollback.php`** -> AI Confidence: **99.29%**
1041. **`dev/tests/integration/testsuite/Magento/Catalog/_files/product_special_price.php`** -> AI Confidence: **99.29%**
1042. **`dev/tests/integration/testsuite/Magento/Catalog/_files/product_special_price_rollback.php`** -> AI Confidence: **99.29%**
1043. **`dev/tests/integration/testsuite/Magento/Catalog/_files/product_text_attribute.php`** -> AI Confidence: **99.29%**
1044. **`dev/tests/integration/testsuite/Magento/Catalog/_files/product_text_attribute_rollback.php`** -> AI Confidence: **99.29%**
1045. **`dev/tests/integration/testsuite/Magento/Catalog/_files/product_virtual_in_stock.php`** -> AI Confidence: **99.29%**
1046. **`dev/tests/integration/testsuite/Magento/Catalog/_files/product_virtual_in_stock_rollback.php`** -> AI Confidence: **99.29%**
1047. **`dev/tests/integration/testsuite/Magento/Catalog/_files/product_virtual_out_of_stock.php`** -> AI Confidence: **99.29%**
1048. **`dev/tests/integration/testsuite/Magento/Catalog/_files/product_virtual_out_of_stock_rollback.php`** -> AI Confidence: **99.29%**
1049. **`dev/tests/integration/testsuite/Magento/Catalog/_files/product_with_options_rollback.php`** -> AI Confidence: **99.29%**
1050. **`dev/tests/integration/testsuite/Magento/Catalog/_files/product_with_two_websites_rollback.php`** -> AI Confidence: **99.29%**
1051. **`dev/tests/integration/testsuite/Magento/Catalog/_files/product_without_options.php`** -> AI Confidence: **99.29%**
1052. **`dev/tests/integration/testsuite/Magento/Catalog/_files/product_without_options_rollback.php`** -> AI Confidence: **99.29%**
1053. **`dev/tests/integration/testsuite/Magento/Catalog/_files/products.php`** -> AI Confidence: **99.29%**
1054. **`dev/tests/integration/testsuite/Magento/Catalog/_files/products_crosssell.php`** -> AI Confidence: **99.29%**
1055. **`dev/tests/integration/testsuite/Magento/Catalog/_files/products_crosssell_rollback.php`** -> AI Confidence: **99.29%**
1056. **`dev/tests/integration/testsuite/Magento/Catalog/_files/products_in_category.php`** -> AI Confidence: **99.29%**
1057. **`dev/tests/integration/testsuite/Magento/Catalog/_files/products_in_category_rollback.php`** -> AI Confidence: **99.29%**
1058. **`dev/tests/integration/testsuite/Magento/Catalog/_files/products_related.php`** -> AI Confidence: **99.29%**
1059. **`dev/tests/integration/testsuite/Magento/Catalog/_files/products_related_disabled.php`** -> AI Confidence: **99.29%**
1060. **`dev/tests/integration/testsuite/Magento/Catalog/_files/products_related_disabled_in_store_rollback.php`** -> AI Confidence: **99.29%**
1061. **`dev/tests/integration/testsuite/Magento/Catalog/_files/products_related_disabled_rollback.php`** -> AI Confidence: **99.29%**
1062. **`dev/tests/integration/testsuite/Magento/Catalog/_files/products_related_multiple.php`** -> AI Confidence: **99.29%**
1063. **`dev/tests/integration/testsuite/Magento/Catalog/_files/products_related_multiple_rollback.php`** -> AI Confidence: **99.29%**
1064. **`dev/tests/integration/testsuite/Magento/Catalog/_files/products_related_rollback.php`** -> AI Confidence: **99.29%**
1065. **`dev/tests/integration/testsuite/Magento/Catalog/_files/products_rollback.php`** -> AI Confidence: **99.29%**
1066. **`dev/tests/integration/testsuite/Magento/Catalog/_files/row_fixture.php`** -> AI Confidence: **99.29%**
1067. **`dev/tests/integration/testsuite/Magento/Catalog/_files/row_fixture_rollback.php`** -> AI Confidence: **99.29%**
1068. **`dev/tests/integration/testsuite/Magento/Catalog/_files/second_product_simple.php`** -> AI Confidence: **99.29%**
1069. **`dev/tests/integration/testsuite/Magento/Catalog/_files/second_website.php`** -> AI Confidence: **99.29%**
1070. **`dev/tests/integration/testsuite/Magento/Catalog/_files/second_website_rollback.php`** -> AI Confidence: **99.29%**
1071. **`dev/tests/integration/testsuite/Magento/Catalog/_files/unique_input_attribute.php`** -> AI Confidence: **99.29%**
1072. **`dev/tests/integration/testsuite/Magento/Catalog/_files/url_rewrites.php`** -> AI Confidence: **99.29%**
1073. **`dev/tests/integration/testsuite/Magento/Catalog/_files/url_rewrites_rollback.php`** -> AI Confidence: **99.29%**
1074. **`dev/tests/integration/testsuite/Magento/Catalog/_files/validate_image.php`** -> AI Confidence: **99.29%**
1075. **`dev/tests/integration/testsuite/Magento/Catalog/_files/validate_image_info.php`** -> AI Confidence: **99.29%**
1076. **`dev/tests/integration/testsuite/Magento/Catalog/_files/validate_image_info_rollback.php`** -> AI Confidence: **99.29%**
1077. **`dev/tests/integration/testsuite/Magento/Catalog/_files/validate_image_rollback.php`** -> AI Confidence: **99.29%**
1078. **`dev/tests/integration/testsuite/Magento/Catalog/controllers/_files/attribute_system.php`** -> AI Confidence: **99.29%**
1079. **`dev/tests/integration/testsuite/Magento/Catalog/controllers/_files/attribute_system_popup.php`** -> AI Confidence: **99.29%**
1080. **`dev/tests/integration/testsuite/Magento/Catalog/controllers/_files/attribute_system_with_applyto_data.php`** -> AI Confidence: **99.29%**
1081. **`dev/tests/integration/testsuite/Magento/Catalog/controllers/_files/attribute_user_defined.php`** -> AI Confidence: **99.29%**
1082. **`dev/tests/integration/testsuite/Magento/Catalog/controllers/_files/products_rollback.php`** -> AI Confidence: **99.29%**
1083. **`dev/tests/integration/testsuite/Magento/CatalogImportExport/Model/Import/_files/custom_category_store_media_disabled_rollback.php`** -> AI Confidence: **99.29%**
1084. **`dev/tests/integration/testsuite/Magento/CatalogImportExport/Model/Import/_files/import_with_filesystem_images_rollback.php`** -> AI Confidence: **99.29%**
1085. **`dev/tests/integration/testsuite/Magento/CatalogImportExport/Model/Import/_files/media_import_image.php`** -> AI Confidence: **99.29%**
1086. **`dev/tests/integration/testsuite/Magento/CatalogImportExport/Model/Import/_files/media_import_image_rollback.php`** -> AI Confidence: **99.29%**
1087. **`dev/tests/integration/testsuite/Magento/CatalogRule/_files/attribute.php`** -> AI Confidence: **99.29%**
1088. **`dev/tests/integration/testsuite/Magento/CatalogRule/_files/attribute_rollback.php`** -> AI Confidence: **99.29%**
1089. **`dev/tests/integration/testsuite/Magento/CatalogRule/_files/catalog_rule_10_off_not_logged.php`** -> AI Confidence: **99.29%**
1090. **`dev/tests/integration/testsuite/Magento/CatalogRule/_files/catalog_rule_10_off_not_logged_rollback.php`** -> AI Confidence: **99.29%**
1091. **`dev/tests/integration/testsuite/Magento/CatalogRule/_files/conditions_to_collection/attribute_sets_rollback.php`** -> AI Confidence: **99.29%**
1092. **`dev/tests/integration/testsuite/Magento/CatalogRule/_files/rule_by_attribute_rollback.php`** -> AI Confidence: **99.29%**
1093. **`dev/tests/integration/testsuite/Magento/CatalogRule/_files/rule_by_category_ids_rollback.php`** -> AI Confidence: **99.29%**
1094. **`dev/tests/integration/testsuite/Magento/CatalogRule/_files/two_rules_rollback.php`** -> AI Confidence: **99.29%**
1095. **`dev/tests/integration/testsuite/Magento/CatalogSearch/_files/full_reindex.php`** -> AI Confidence: **99.29%**
1096. **`dev/tests/integration/testsuite/Magento/CatalogSearch/_files/indexer_fulltext.php`** -> AI Confidence: **99.29%**
1097. **`dev/tests/integration/testsuite/Magento/CatalogSearch/_files/indexer_fulltext_rollback.php`** -> AI Confidence: **99.29%**
1098. **`dev/tests/integration/testsuite/Magento/CatalogSearch/_files/popular_query.php`** -> AI Confidence: **99.29%**
1099. **`dev/tests/integration/testsuite/Magento/CatalogSearch/_files/query.php`** -> AI Confidence: **99.29%**
1100. **`dev/tests/integration/testsuite/Magento/CatalogSearch/_files/search_attributes_rollback.php`** -> AI Confidence: **99.29%**
1101. **`dev/tests/integration/testsuite/Magento/CatalogUrlRewrite/_files/categories.php`** -> AI Confidence: **99.29%**
1102. **`dev/tests/integration/testsuite/Magento/CatalogUrlRewrite/_files/categories_rollback.php`** -> AI Confidence: **99.29%**
1103. **`dev/tests/integration/testsuite/Magento/CatalogUrlRewrite/_files/category_with_products.php`** -> AI Confidence: **99.29%**
1104. **`dev/tests/integration/testsuite/Magento/CatalogUrlRewrite/_files/category_with_products_rollback.php`** -> AI Confidence: **99.29%**
1105. **`dev/tests/integration/testsuite/Magento/Config/_files/config.php`** -> AI Confidence: **99.29%**
1106. **`dev/tests/integration/testsuite/Magento/Config/_files/env.php`** -> AI Confidence: **99.29%**
1107. **`dev/tests/integration/testsuite/Magento/ConfigurableProduct/_files/associated_products.php`** -> AI Confidence: **99.29%**
1108. **`dev/tests/integration/testsuite/Magento/ConfigurableProduct/_files/configurable_attribute_2_rollback.php`** -> AI Confidence: **99.29%**
1109. **`dev/tests/integration/testsuite/Magento/ConfigurableProduct/_files/configurable_attribute_first_rollback.php`** -> AI Confidence: **99.29%**
1110. **`dev/tests/integration/testsuite/Magento/ConfigurableProduct/_files/configurable_attribute_rollback.php`** -> AI Confidence: **99.29%**
1111. **`dev/tests/integration/testsuite/Magento/ConfigurableProduct/_files/configurable_attribute_second_rollback.php`** -> AI Confidence: **99.29%**
1112. **`dev/tests/integration/testsuite/Magento/ConfigurableProduct/_files/delete_association.php`** -> AI Confidence: **99.29%**
1113. **`dev/tests/integration/testsuite/Magento/ConfigurableProduct/_files/quote_with_configurable_product_last_variation_rollback.php`** -> AI Confidence: **99.29%**
1114. **`dev/tests/integration/testsuite/Magento/ConfigurableProduct/_files/tax_rule.php`** -> AI Confidence: **99.29%**
1115. **`dev/tests/integration/testsuite/Magento/Customer/_files/attribute_user_defined_address.php`** -> AI Confidence: **99.29%**
1116. **`dev/tests/integration/testsuite/Magento/Customer/_files/attribute_user_defined_address_custom_attribute_rollback.php`** -> AI Confidence: **99.29%**
1117. **`dev/tests/integration/testsuite/Magento/Customer/_files/attribute_user_defined_address_rollback.php`** -> AI Confidence: **99.29%**
1118. **`dev/tests/integration/testsuite/Magento/Customer/_files/attribute_user_defined_custom_attribute.php`** -> AI Confidence: **99.29%**
1119. **`dev/tests/integration/testsuite/Magento/Customer/_files/attribute_user_defined_custom_attribute_rollback.php`** -> AI Confidence: **99.29%**
1120. **`dev/tests/integration/testsuite/Magento/Customer/_files/attribute_user_defined_customer.php`** -> AI Confidence: **99.29%**
1121. **`dev/tests/integration/testsuite/Magento/Customer/_files/attribute_user_defined_customer_rollback.php`** -> AI Confidence: **99.29%**
1122. **`dev/tests/integration/testsuite/Magento/Customer/_files/attribute_user_fullname.php`** -> AI Confidence: **99.29%**
1123. **`dev/tests/integration/testsuite/Magento/Customer/_files/customer_address.php`** -> AI Confidence: **99.29%**
1124. **`dev/tests/integration/testsuite/Magento/Customer/_files/customer_address_attribute_update.php`** -> AI Confidence: **99.29%**
1125. **`dev/tests/integration/testsuite/Magento/Customer/_files/customer_address_attribute_update_rollback.php`** -> AI Confidence: **99.29%**
1126. **`dev/tests/integration/testsuite/Magento/Customer/_files/customer_address_rollback.php`** -> AI Confidence: **99.29%**
1127. **`dev/tests/integration/testsuite/Magento/Customer/_files/customer_from_repository.php`** -> AI Confidence: **99.29%**
1128. **`dev/tests/integration/testsuite/Magento/Customer/_files/customer_grid_indexer_enabled_update_on_schedule.php`** -> AI Confidence: **99.29%**
1129. **`dev/tests/integration/testsuite/Magento/Customer/_files/customer_grid_indexer_enabled_update_on_schedule_rollback.php`** -> AI Confidence: **99.29%**
1130. **`dev/tests/integration/testsuite/Magento/Customer/_files/customer_group.php`** -> AI Confidence: **99.29%**
1131. **`dev/tests/integration/testsuite/Magento/Customer/_files/customer_no_address.php`** -> AI Confidence: **99.29%**
1132. **`dev/tests/integration/testsuite/Magento/Customer/_files/customer_rp_token.php`** -> AI Confidence: **99.29%**
1133. **`dev/tests/integration/testsuite/Magento/Customer/_files/customer_shipping_address_36104.php`** -> AI Confidence: **99.29%**
1134. **`dev/tests/integration/testsuite/Magento/Customer/_files/customer_shipping_address_36104_rollback.php`** -> AI Confidence: **99.29%**
1135. **`dev/tests/integration/testsuite/Magento/Customer/_files/customer_with_website.php`** -> AI Confidence: **99.29%**
1136. **`dev/tests/integration/testsuite/Magento/Customer/_files/inactive_customer.php`** -> AI Confidence: **99.29%**
1137. **`dev/tests/integration/testsuite/Magento/Customer/_files/quote.php`** -> AI Confidence: **99.29%**
1138. **`dev/tests/integration/testsuite/Magento/Deploy/_files/_config.local.php`** -> AI Confidence: **99.29%**
1139. **`dev/tests/integration/testsuite/Magento/Deploy/_files/config.php`** -> AI Confidence: **99.29%**
1140. **`dev/tests/integration/testsuite/Magento/Deploy/_files/map.php`** -> AI Confidence: **99.29%**
1141. **`dev/tests/integration/testsuite/Magento/Deploy/_files/scopes/config_with_changed_stores.php`** -> AI Confidence: **99.29%**
1142. **`dev/tests/integration/testsuite/Magento/Deploy/_files/theme_rollback.php`** -> AI Confidence: **99.29%**
1143. **`dev/tests/integration/testsuite/Magento/Downloadable/_files/order_with_downloadable_product_with_additional_options.php`** -> AI Confidence: **99.29%**
1144. **`dev/tests/integration/testsuite/Magento/Downloadable/_files/product_downloadable_with_files.php`** -> AI Confidence: **99.29%**
1145. **`dev/tests/integration/testsuite/Magento/Eav/_files/empty_attribute_set.php`** -> AI Confidence: **99.29%**
1146. **`dev/tests/integration/testsuite/Magento/Eav/_files/empty_attribute_set_rollback.php`** -> AI Confidence: **99.29%**
1147. **`dev/tests/integration/testsuite/Magento/Elasticsearch/_files/multiselect_attribute_rollback.php`** -> AI Confidence: **99.29%**
1148. **`dev/tests/integration/testsuite/Magento/Elasticsearch/_files/select_attribute_rollback.php`** -> AI Confidence: **99.29%**
1149. **`dev/tests/integration/testsuite/Magento/Email/Model/_files/design/adminhtml/Magento/default/Magento_Email/templates/sample_email_content.phtml`** -> AI Confidence: **99.29%**
1150. **`dev/tests/integration/testsuite/Magento/Email/Model/_files/design/frontend/Magento/default/Magento_Email/templates/sample_email_content.phtml`** -> AI Confidence: **99.29%**
1151. **`dev/tests/integration/testsuite/Magento/Email/Model/_files/design/frontend/Magento/default/Magento_Email/templates/sample_email_content_custom.phtml`** -> AI Confidence: **99.29%**
1152. **`dev/tests/integration/testsuite/Magento/Email/Model/_files/email_template.php`** -> AI Confidence: **99.29%**
1153. **`dev/tests/integration/testsuite/Magento/Email/Model/_files/email_template_new_user_notification.php`** -> AI Confidence: **99.29%**
1154. **`dev/tests/integration/testsuite/Magento/Email/Model/_files/email_template_reset_password_user_notification.php`** -> AI Confidence: **99.29%**
1155. **`dev/tests/integration/testsuite/Magento/EncryptionKey/_files/payment_info.php`** -> AI Confidence: **99.29%**
1156. **`dev/tests/integration/testsuite/Magento/Framework/Code/_files/ClassToFind.php`** -> AI Confidence: **99.29%**
1157. **`dev/tests/integration/testsuite/Magento/Framework/Filesystem/_files/ClassToFind.php`** -> AI Confidence: **99.29%**
1158. **`dev/tests/integration/testsuite/Magento/Framework/Search/_files/configurable_attribute_rollback.php`** -> AI Confidence: **99.29%**
1159. **`dev/tests/integration/testsuite/Magento/Framework/Search/_files/date_attribute.php`** -> AI Confidence: **99.29%**
1160. **`dev/tests/integration/testsuite/Magento/Framework/Search/_files/date_attribute_rollback.php`** -> AI Confidence: **99.29%**
1161. **`dev/tests/integration/testsuite/Magento/Framework/Search/_files/filterable_attribute_rollback.php`** -> AI Confidence: **99.29%**
1162. **`dev/tests/integration/testsuite/Magento/Framework/Search/_files/products.php`** -> AI Confidence: **99.29%**
1163. **`dev/tests/integration/testsuite/Magento/Framework/Search/_files/products_multi_option.php`** -> AI Confidence: **99.29%**
1164. **`dev/tests/integration/testsuite/Magento/Framework/Search/_files/products_multi_option_rollback.php`** -> AI Confidence: **99.29%**
1165. **`dev/tests/integration/testsuite/Magento/Framework/Search/_files/products_with_the_same_search_score_rollback.php`** -> AI Confidence: **99.29%**
1166. **`dev/tests/integration/testsuite/Magento/Framework/Search/_files/search_weight_products_rollback.php`** -> AI Confidence: **99.29%**
1167. **`dev/tests/integration/testsuite/Magento/Framework/Translate/_files/_translation_data.php`** -> AI Confidence: **99.29%**
1168. **`dev/tests/integration/testsuite/Magento/Framework/View/_files/test_template.phtml`** -> AI Confidence: **99.29%**
1169. **`dev/tests/integration/testsuite/Magento/GiftMessage/_files/quote_with_customer_and_message_rollback.php`** -> AI Confidence: **99.29%**
1170. **`dev/tests/integration/testsuite/Magento/GiftMessage/_files/quote_with_message.php`** -> AI Confidence: **99.29%**
1171. **`dev/tests/integration/testsuite/Magento/GiftMessage/_files/quote_with_message_rollback.php`** -> AI Confidence: **99.29%**
1172. **`dev/tests/integration/testsuite/Magento/GroupedProduct/_files/product_grouped_in_multiple_websites_rollback.php`** -> AI Confidence: **99.29%**
1173. **`dev/tests/integration/testsuite/Magento/GroupedProduct/_files/product_grouped_items_in_multiple_websites_rollback.php`** -> AI Confidence: **99.29%**
1174. **`dev/tests/integration/testsuite/Magento/GroupedProduct/_files/product_grouped_rollback.php`** -> AI Confidence: **99.29%**
1175. **`dev/tests/integration/testsuite/Magento/GroupedProduct/_files/product_grouped_with_simple_out_of_stock_rollback.php`** -> AI Confidence: **99.29%**
1176. **`dev/tests/integration/testsuite/Magento/GroupedProduct/_files/product_grouped_with_simple_rollback.php`** -> AI Confidence: **99.29%**
1177. **`dev/tests/integration/testsuite/Magento/ImportExport/_files/product.php`** -> AI Confidence: **99.29%**
1178. **`dev/tests/integration/testsuite/Magento/Integration/_files/integration_all_permissions.php`** -> AI Confidence: **99.29%**
1179. **`dev/tests/integration/testsuite/Magento/Integration/_files/integration_all_permissions_rollback.php`** -> AI Confidence: **99.29%**
1180. **`dev/tests/integration/testsuite/Magento/MediaContentCatalog/_files/category_with_asset_rollback.php`** -> AI Confidence: **99.29%**
1181. **`dev/tests/integration/testsuite/Magento/MediaContentCms/_files/page_with_asset.php`** -> AI Confidence: **99.29%**
1182. **`dev/tests/integration/testsuite/Magento/Newsletter/_files/template.php`** -> AI Confidence: **99.29%**
1183. **`dev/tests/integration/testsuite/Magento/OfflineShipping/_files/tablerates.php`** -> AI Confidence: **99.29%**
1184. **`dev/tests/integration/testsuite/Magento/OfflineShipping/_files/tablerates_rollback.php`** -> AI Confidence: **99.29%**
1185. **`dev/tests/integration/testsuite/Magento/Payment/_files/order_status.php`** -> AI Confidence: **99.29%**
1186. **`dev/tests/integration/testsuite/Magento/Paypal/_files/billing_agreement.php`** -> AI Confidence: **99.29%**
1187. **`dev/tests/integration/testsuite/Magento/Paypal/_files/quote_payment.php`** -> AI Confidence: **99.29%**
1188. **`dev/tests/integration/testsuite/Magento/Quote/_files/empty_quote.php`** -> AI Confidence: **99.29%**
1189. **`dev/tests/integration/testsuite/Magento/Quote/_files/empty_quote_rollback.php`** -> AI Confidence: **99.29%**
1190. **`dev/tests/integration/testsuite/Magento/Quote/_files/is_not_salable_product.php`** -> AI Confidence: **99.29%**
1191. **`dev/tests/integration/testsuite/Magento/Quote/_files/is_salable_product.php`** -> AI Confidence: **99.29%**
1192. **`dev/tests/integration/testsuite/Magento/Sales/_files/address.php`** -> AI Confidence: **99.29%**
1193. **`dev/tests/integration/testsuite/Magento/Sales/_files/guest_quote_with_addresses_rollback.php`** -> AI Confidence: **99.29%**
1194. **`dev/tests/integration/testsuite/Magento/Sales/_files/order_from_past.php`** -> AI Confidence: **99.29%**
1195. **`dev/tests/integration/testsuite/Magento/Sales/_files/quote_rollback.php`** -> AI Confidence: **99.29%**
1196. **`dev/tests/integration/testsuite/Magento/Sales/_files/quote_with_backorder_rollback.php`** -> AI Confidence: **99.29%**
1197. **`dev/tests/integration/testsuite/Magento/Sales/_files/quote_with_bundle_rollback.php`** -> AI Confidence: **99.29%**
1198. **`dev/tests/integration/testsuite/Magento/Sales/_files/report_bestsellers.php`** -> AI Confidence: **99.29%**
1199. **`dev/tests/integration/testsuite/Magento/Sales/_files/report_invoiced.php`** -> AI Confidence: **99.29%**
1200. **`dev/tests/integration/testsuite/Magento/Sales/_files/report_refunded.php`** -> AI Confidence: **99.29%**
1201. **`dev/tests/integration/testsuite/Magento/Sales/_files/report_shipping.php`** -> AI Confidence: **99.29%**
1202. **`dev/tests/integration/testsuite/Magento/Sales/_files/transactions.php`** -> AI Confidence: **99.29%**
1203. **`dev/tests/integration/testsuite/Magento/Sales/_files/transactions_detailed.php`** -> AI Confidence: **99.29%**
1204. **`dev/tests/integration/testsuite/Magento/SalesRule/_files/cart_rule_40_percent_off.php`** -> AI Confidence: **99.29%**
1205. **`dev/tests/integration/testsuite/Magento/SalesRule/_files/cart_rule_50_percent_off.php`** -> AI Confidence: **99.29%**
1206. **`dev/tests/integration/testsuite/Magento/SalesRule/_files/cart_rule_free_shipping.php`** -> AI Confidence: **99.29%**
1207. **`dev/tests/integration/testsuite/Magento/SalesRule/_files/cart_rule_free_shipping_rollback.php`** -> AI Confidence: **99.29%**
1208. **`dev/tests/integration/testsuite/Magento/SalesRule/_files/cart_rule_product_in_category.php`** -> AI Confidence: **99.29%**
1209. **`dev/tests/integration/testsuite/Magento/SalesRule/_files/coupons.php`** -> AI Confidence: **99.29%**
1210. **`dev/tests/integration/testsuite/Magento/SalesRule/_files/report_coupons.php`** -> AI Confidence: **99.29%**
1211. **`dev/tests/integration/testsuite/Magento/SalesRule/_files/rule_custom_product_attribute.php`** -> AI Confidence: **99.29%**
1212. **`dev/tests/integration/testsuite/Magento/SalesRule/_files/rules.php`** -> AI Confidence: **99.29%**
1213. **`dev/tests/integration/testsuite/Magento/SalesRule/_files/rules_autogeneration.php`** -> AI Confidence: **99.29%**
1214. **`dev/tests/integration/testsuite/Magento/SalesRule/_files/rules_autogeneration_rollback.php`** -> AI Confidence: **99.29%**
1215. **`dev/tests/integration/testsuite/Magento/SalesRule/_files/rules_categories.php`** -> AI Confidence: **99.29%**
1216. **`dev/tests/integration/testsuite/Magento/SalesRule/_files/rules_category.php`** -> AI Confidence: **99.29%**
1217. **`dev/tests/integration/testsuite/Magento/SalesRule/_files/rules_category_rollback.php`** -> AI Confidence: **99.29%**
1218. **`dev/tests/integration/testsuite/Magento/SalesRule/_files/rules_group_all_categories.php`** -> AI Confidence: **99.29%**
1219. **`dev/tests/integration/testsuite/Magento/SalesRule/_files/rules_group_all_categories_price_attr_set.php`** -> AI Confidence: **99.29%**
1220. **`dev/tests/integration/testsuite/Magento/SalesRule/_files/rules_group_any_categories.php`** -> AI Confidence: **99.29%**
1221. **`dev/tests/integration/testsuite/Magento/SalesRule/_files/rules_group_any_categories_price_attr_set.php`** -> AI Confidence: **99.29%**
1222. **`dev/tests/integration/testsuite/Magento/SalesRule/_files/rules_group_any_categories_price_attr_set_any.php`** -> AI Confidence: **99.29%**
1223. **`dev/tests/integration/testsuite/Magento/SalesRule/_files/rules_group_categories_price_sku_attr_set_any.php`** -> AI Confidence: **99.29%**
1224. **`dev/tests/integration/testsuite/Magento/SalesRule/_files/rules_group_not_categories_sku_attr.php`** -> AI Confidence: **99.29%**
1225. **`dev/tests/integration/testsuite/Magento/Search/_files/synonym_reader.php`** -> AI Confidence: **99.29%**
1226. **`dev/tests/integration/testsuite/Magento/Search/_files/synonym_reader_rollback.php`** -> AI Confidence: **99.29%**
1227. **`dev/tests/integration/testsuite/Magento/Security/_files/adminsession.php`** -> AI Confidence: **99.29%**
1228. **`dev/tests/integration/testsuite/Magento/Setup/Console/Command/_files/config/dump_config.php`** -> AI Confidence: **99.29%**
1229. **`dev/tests/integration/testsuite/Magento/Setup/Module/I18n/Dictionary/_files/source/app/code/Magento/FirstModule/view/frontend/template.phtml`** -> AI Confidence: **99.29%**
1230. **`dev/tests/integration/testsuite/Magento/Setup/Module/I18n/Dictionary/_files/source/app/design/adminhtml/default/backend/template.phtml`** -> AI Confidence: **99.29%**
1231. **`dev/tests/integration/testsuite/Magento/Setup/Module/I18n/Dictionary/_files/source/not_magento_dir/template.phtml`** -> AI Confidence: **99.29%**
1232. **`dev/tests/integration/testsuite/Magento/Store/_files/core_fixturestore_rollback.php`** -> AI Confidence: **99.29%**
1233. **`dev/tests/integration/testsuite/Magento/Store/_files/core_second_third_fixturestore.php`** -> AI Confidence: **99.29%**
1234. **`dev/tests/integration/testsuite/Magento/Store/_files/dump_config.php`** -> AI Confidence: **99.29%**
1235. **`dev/tests/integration/testsuite/Magento/Store/_files/fixture_store_with_catalogsearch_index_rollback.php`** -> AI Confidence: **99.29%**
1236. **`dev/tests/integration/testsuite/Magento/Store/_files/multiple_websites_with_store_groups_stores_rollback.php`** -> AI Confidence: **99.29%**
1237. **`dev/tests/integration/testsuite/Magento/Store/_files/second_store.php`** -> AI Confidence: **99.29%**
1238. **`dev/tests/integration/testsuite/Magento/Store/_files/second_website_with_two_stores.php`** -> AI Confidence: **99.29%**
1239. **`dev/tests/integration/testsuite/Magento/Store/_files/second_website_with_two_stores_rollback.php`** -> AI Confidence: **99.29%**
1240. **`dev/tests/integration/testsuite/Magento/Store/_files/store.php`** -> AI Confidence: **99.29%**
1241. **`dev/tests/integration/testsuite/Magento/Store/_files/store_with_long_name.php`** -> AI Confidence: **99.29%**
1242. **`dev/tests/integration/testsuite/Magento/Store/_files/website.php`** -> AI Confidence: **99.29%**
1243. **`dev/tests/integration/testsuite/Magento/Store/_files/website_rollback.php`** -> AI Confidence: **99.29%**
1244. **`dev/tests/integration/testsuite/Magento/Swatches/_files/swatch_attribute_rollback.php`** -> AI Confidence: **99.29%**
1245. **`dev/tests/integration/testsuite/Magento/Swatches/_files/text_swatch_attribute_rollback.php`** -> AI Confidence: **99.29%**
1246. **`dev/tests/integration/testsuite/Magento/Tax/_files/report_tax.php`** -> AI Confidence: **99.29%**
1247. **`dev/tests/integration/testsuite/Magento/Tax/_files/tax_class_customer_group_rollback.php`** -> AI Confidence: **99.29%**
1248. **`dev/tests/integration/testsuite/Magento/Tax/_files/tax_classes.php`** -> AI Confidence: **99.29%**
1249. **`dev/tests/integration/testsuite/Magento/Tax/_files/tax_rule_postal_36104.php`** -> AI Confidence: **99.29%**
1250. **`dev/tests/integration/testsuite/Magento/Tax/_files/tax_rule_region_1_al.php`** -> AI Confidence: **99.29%**
1251. **`dev/tests/integration/testsuite/Magento/Theme/Model/_files/design/frontend/access_violation.php`** -> AI Confidence: **99.29%**
1252. **`dev/tests/integration/testsuite/Magento/Theme/_files/config_data_rollback.php`** -> AI Confidence: **99.29%**
1253. **`dev/tests/integration/testsuite/Magento/Theme/_files/design_change.php`** -> AI Confidence: **99.29%**
1254. **`dev/tests/integration/testsuite/Magento/Theme/_files/design_change_rollback.php`** -> AI Confidence: **99.29%**
1255. **`dev/tests/integration/testsuite/Magento/Theme/_files/design_change_timezone.php`** -> AI Confidence: **99.29%**
1256. **`dev/tests/integration/testsuite/Magento/Translation/_files/db_translate.php`** -> AI Confidence: **99.29%**
1257. **`dev/tests/integration/testsuite/Magento/Translation/_files/db_translate_admin_store.php`** -> AI Confidence: **99.29%**
1258. **`dev/tests/integration/testsuite/Magento/UrlRewrite/_files/url_rewrites_rollback.php`** -> AI Confidence: **99.29%**
1259. **`dev/tests/integration/testsuite/Magento/User/_files/dummy_user.php`** -> AI Confidence: **99.29%**
1260. **`dev/tests/integration/testsuite/Magento/User/_files/locked_users.php`** -> AI Confidence: **99.29%**
1261. **`dev/tests/integration/testsuite/Magento/User/_files/user_with_role.php`** -> AI Confidence: **99.29%**
1262. **`dev/tests/integration/testsuite/Magento/Variable/_files/variable.php`** -> AI Confidence: **99.29%**
1263. **`dev/tests/integration/testsuite/Magento/Webapi/_files/webapi_user.php`** -> AI Confidence: **99.29%**
1264. **`dev/tests/integration/testsuite/Magento/Weee/_files/product_with_fpt_rollback.php`** -> AI Confidence: **99.29%**
1265. **`dev/tests/integration/testsuite/Magento/Widget/_files/layout_cache.php`** -> AI Confidence: **99.29%**
1266. **`dev/tests/integration/testsuite/Magento/Widget/_files/layout_update.php`** -> AI Confidence: **99.29%**
1267. **`dev/tests/integration/testsuite/Magento/Widget/_files/new_widget.php`** -> AI Confidence: **99.29%**
1268. **`dev/tests/setup-integration/_files/Magento/TestSetupDeclarationModule1/fixture/foreign_key_interpreter_result.php`** -> AI Confidence: **99.29%**
1269. **`dev/tests/setup-integration/_files/Magento/TestSetupDeclarationModule1/fixture/valid_xml_revision_1.php`** -> AI Confidence: **99.29%**
1270. **`dev/tests/static/framework/tests/unit/testsuite/Magento/TestFramework/Inspection/_files/words_finder/buffy.php`** -> AI Confidence: **99.29%**
1271. **`dev/tests/static/framework/tests/unit/testsuite/Magento/TestFramework/Inspection/_files/words_finder/interview_with_the_vampire.php`** -> AI Confidence: **99.29%**
1272. **`dev/tests/static/framework/tests/unit/testsuite/Magento/TestFramework/Inspection/_files/words_finder/twilight/eclipse.php`** -> AI Confidence: **99.29%**
1273. **`dev/tests/static/framework/tests/unit/testsuite/Magento/TestFramework/Inspection/_files/words_finder/twilight/newmoon.php`** -> AI Confidence: **99.29%**
1274. **`pub/errors/default/404.phtml`** -> AI Confidence: **99.29%**
1275. **`pub/errors/default/503.phtml`** -> AI Confidence: **99.29%**
1276. **`pub/errors/default/nocache.phtml`** -> AI Confidence: **99.29%**
1277. **`pub/errors/default/page.phtml`** -> AI Confidence: **99.29%**
1278. **`app/code/Magento/Backend/view/adminhtml/web/js/save-with-confirm.js`** -> AI Confidence: **99.29%**
1279. **`app/code/Magento/Bundle/view/frontend/web/js/slide.js`** -> AI Confidence: **99.29%**
1280. **`app/code/Magento/Catalog/view/adminhtml/web/js/utils/percentage-price-calculator.js`** -> AI Confidence: **99.29%**
1281. **`app/code/Magento/Catalog/view/base/web/js/price-option-file.js`** -> AI Confidence: **99.29%**
1282. **`app/code/Magento/Csp/view/base/web/js/sri.js`** -> AI Confidence: **99.29%**
1283. **`app/code/Magento/Customer/view/frontend/web/js/change-email-password.js`** -> AI Confidence: **99.29%**
1284. **`app/code/Magento/Directory/view/frontend/web/js/region-updater.js`** -> AI Confidence: **99.29%**
1285. **`app/code/Magento/Downloadable/view/adminhtml/web/downloadable-type-handler.js`** -> AI Confidence: **99.29%**
1286. **`app/code/Magento/Downloadable/view/adminhtml/web/js/components/is-downloadable-handler.js`** -> AI Confidence: **99.29%**
1287. **`app/code/Magento/Eav/view/adminhtml/web/js/input-types.js`** -> AI Confidence: **99.29%**
1288. **`app/code/Magento/GoogleAnalytics/view/frontend/web/js/google-analytics.js`** -> AI Confidence: **99.29%**
1289. **`app/code/Magento/Paypal/view/adminhtml/web/js/rules.js`** -> AI Confidence: **99.29%**
1290. **`app/code/Magento/Paypal/view/frontend/web/js/model/iframe-redirect.js`** -> AI Confidence: **99.29%**
1291. **`app/code/Magento/Search/view/frontend/web/js/form-mini.js`** -> AI Confidence: **99.29%**
1292. **`app/code/Magento/Swatches/view/adminhtml/web/js/product-attributes.js`** -> AI Confidence: **99.29%**
1293. **`app/code/Magento/Theme/view/frontend/requirejs-config.js`** -> AI Confidence: **99.29%**
1294. **`app/code/Magento/Ui/view/base/web/js/form/element/date.js`** -> AI Confidence: **99.29%**
1295. **`app/code/Magento/Ui/view/base/web/js/form/element/single-checkbox.js`** -> AI Confidence: **99.29%**
1296. **`app/code/Magento/Wishlist/view/frontend/web/js/search.js`** -> AI Confidence: **99.29%**
1297. **`setup/pub/scripts/main.js`** -> AI Confidence: **99.29%**
1298. **`app/code/Magento/AsynchronousOperations/Model/MassConsumerEnvelopeCallback.php`** -> AI Confidence: **99.24%**
1299. **`app/code/Magento/AsynchronousOperations/Model/OperationProcessor.php`** -> AI Confidence: **99.24%**
1300. **`app/code/Magento/Backend/Controller/Adminhtml/Auth/Login.php`** -> AI Confidence: **99.24%**
1301. **`app/code/Magento/Bundle/Model/Option/SaveAction.php`** -> AI Confidence: **99.24%**
1302. **`app/code/Magento/Bundle/Model/Product/SaveHandler.php`** -> AI Confidence: **99.24%**
1303. **`app/code/Magento/Bundle/Model/Sales/Order/Pdf/Items/Invoice.php`** -> AI Confidence: **99.24%**
1304. **`app/code/Magento/Bundle/Pricing/Adjustment/DefaultSelectionPriceListProvider.php`** -> AI Confidence: **99.24%**
1305. **`app/code/Magento/Bundle/Ui/DataProvider/Product/Form/Modifier/Composite.php`** -> AI Confidence: **99.24%**
1306. **`app/code/Magento/BundleGraphQl/Model/Resolver/Order/Item/BundleOptions.php`** -> AI Confidence: **99.24%**
1307. **`app/code/Magento/Catalog/Block/Product/View/Options/Type/Select.php`** -> AI Confidence: **99.24%**
1308. **`app/code/Magento/Catalog/Controller/Adminhtml/Product/AddAttributeToTemplate.php`** -> AI Confidence: **99.24%**
1309. **`app/code/Magento/Catalog/Controller/Adminhtml/Product/Validate.php`** -> AI Confidence: **99.24%**
1310. **`app/code/Magento/Catalog/Helper/Data.php`** -> AI Confidence: **99.24%**
1311. **`app/code/Magento/Catalog/Helper/Output.php`** -> AI Confidence: **99.24%**
1312. **`app/code/Magento/Catalog/Model/Attribute/ScopeOverriddenValue.php`** -> AI Confidence: **99.24%**
1313. **`app/code/Magento/Catalog/Model/CategoryRepository.php`** -> AI Confidence: **99.24%**
1314. **`app/code/Magento/Catalog/Model/Indexer/Category/Product/Action/Rows.php`** -> AI Confidence: **99.24%**
1315. **`app/code/Magento/Catalog/Model/Indexer/Product/Category/Action/Rows.php`** -> AI Confidence: **99.24%**
1316. **`app/code/Magento/Catalog/Model/Indexer/Product/Eav/Action/Full.php`** -> AI Confidence: **99.24%**
1317. **`app/code/Magento/Catalog/Model/Indexer/Product/Price/AbstractAction.php`** -> AI Confidence: **99.24%**
1318. **`app/code/Magento/Catalog/Model/Indexer/Product/Price/Action/Rows.php`** -> AI Confidence: **99.24%**
1319. **`app/code/Magento/Catalog/Model/Product/Gallery/CopyHandler.php`** -> AI Confidence: **99.24%**
1320. **`app/code/Magento/Catalog/Model/Product/Gallery/UpdateHandler.php`** -> AI Confidence: **99.24%**
1321. **`app/code/Magento/Catalog/Model/Product/Option/Repository.php`** -> AI Confidence: **99.24%**
1322. **`app/code/Magento/Catalog/Model/Product/Price/BasePriceStorage.php`** -> AI Confidence: **99.24%**
1323. **`app/code/Magento/Catalog/Model/Product/Price/SpecialPriceStorage.php`** -> AI Confidence: **99.24%**
1324. **`app/code/Magento/Catalog/Model/ProductLink/Management.php`** -> AI Confidence: **99.24%**
1325. **`app/code/Magento/Catalog/Model/ProductLink/ProductLinkQuery.php`** -> AI Confidence: **99.24%**
1326. **`app/code/Magento/Catalog/Model/ProductLink/Repository.php`** -> AI Confidence: **99.24%**
1327. **`app/code/Magento/Catalog/Model/ProductRepository.php`** -> AI Confidence: **99.24%**
1328. **`app/code/Magento/Catalog/Model/ResourceModel/Category/Collection.php`** -> AI Confidence: **99.24%**
1329. **`app/code/Magento/Catalog/Model/ResourceModel/Layer/Filter/Price.php`** -> AI Confidence: **99.24%**
1330. **`app/code/Magento/Catalog/Model/ResourceModel/Product/Action.php`** -> AI Confidence: **99.24%**
1331. **`app/code/Magento/Catalog/Model/ResourceModel/Product/Collection.php`** -> AI Confidence: **99.24%**
1332. **`app/code/Magento/Catalog/Model/ResourceModel/Product/Indexer/Eav/Source.php`** -> AI Confidence: **99.24%**
1333. **`app/code/Magento/Catalog/Model/ResourceModel/Product/Indexer/LinkedProductSelectBuilderByIndexPrice.php`** -> AI Confidence: **99.24%**
1334. **`app/code/Magento/Catalog/Model/ResourceModel/Product/Link.php`** -> AI Confidence: **99.24%**
1335. **`app/code/Magento/Catalog/Model/ResourceModel/Product/Option/Collection.php`** -> AI Confidence: **99.24%**
1336. **`app/code/Magento/Catalog/Model/ResourceModel/Product/Price/SpecialPrice.php`** -> AI Confidence: **99.24%**
1337. **`app/code/Magento/Catalog/Model/System/Config/Backend/Catalog/Url/Rewrite/Suffix.php`** -> AI Confidence: **99.24%**
1338. **`app/code/Magento/Catalog/Pricing/Price/TierPrice.php`** -> AI Confidence: **99.24%**
1339. **`app/code/Magento/Catalog/Ui/DataProvider/Product/Form/Modifier/Eav.php`** -> AI Confidence: **99.24%**
1340. **`app/code/Magento/Catalog/Ui/DataProvider/Product/Form/Modifier/General.php`** -> AI Confidence: **99.24%**
1341. **`app/code/Magento/CatalogGraphQl/DataProvider/Product/LayeredNavigation/Builder/Aggregations/Category/IncludeDirectChildrenOnly.php`** -> AI Confidence: **99.24%**
1342. **`app/code/Magento/CatalogGraphQl/Model/Resolver/Aggregations.php`** -> AI Confidence: **99.24%**
1343. **`app/code/Magento/CatalogGraphQl/Model/Resolver/Product/Options.php`** -> AI Confidence: **99.24%**
1344. **`app/code/Magento/CatalogGraphQl/Plugin/ProductAttributeSortInput.php`** -> AI Confidence: **99.24%**
1345. **`app/code/Magento/CatalogImportExport/Model/Import/Product/Type/AbstractType.php`** -> AI Confidence: **99.24%**
1346. **`app/code/Magento/CatalogInventory/Block/Adminhtml/Form/Field/Stock.php`** -> AI Confidence: **99.24%**
1347. **`app/code/Magento/CatalogInventory/Model/Indexer/Stock/Action/Full.php`** -> AI Confidence: **99.24%**
1348. **`app/code/Magento/CatalogInventory/Model/Indexer/Stock/CacheCleaner.php`** -> AI Confidence: **99.24%**
1349. **`app/code/Magento/CatalogInventory/Model/ResourceModel/Stock.php`** -> AI Confidence: **99.24%**
1350. **`app/code/Magento/CatalogInventory/Model/Stock/StockItemRepository.php`** -> AI Confidence: **99.24%**
1351. **`app/code/Magento/CatalogInventory/Model/StockIndex.php`** -> AI Confidence: **99.24%**
1352. **`app/code/Magento/CatalogInventory/Model/StockManagement.php`** -> AI Confidence: **99.24%**
1353. **`app/code/Magento/CatalogRule/Model/Indexer/IndexBuilder.php`** -> AI Confidence: **99.24%**
1354. **`app/code/Magento/CatalogSearch/Controller/Result/Index.php`** -> AI Confidence: **99.24%**
1355. **`app/code/Magento/CatalogSearch/Model/Indexer/Fulltext.php`** -> AI Confidence: **99.24%**
1356. **`app/code/Magento/CatalogSearch/Model/ResourceModel/Fulltext/Collection.php`** -> AI Confidence: **99.24%**
1357. **`app/code/Magento/CatalogUrlRewrite/Model/Product/CurrentUrlRewritesRegenerator.php`** -> AI Confidence: **99.24%**
1358. **`app/code/Magento/CatalogUrlRewrite/Model/ProductScopeRewriteGenerator.php`** -> AI Confidence: **99.24%**
1359. **`app/code/Magento/CatalogUrlRewrite/Observer/AfterImportDataObserver.php`** -> AI Confidence: **99.24%**
1360. **`app/code/Magento/CatalogUrlRewrite/Observer/ProductProcessUrlRewriteSavingObserver.php`** -> AI Confidence: **99.24%**
1361. **`app/code/Magento/CheckoutAgreements/Controller/Adminhtml/Agreement/Save.php`** -> AI Confidence: **99.24%**
1362. **`app/code/Magento/Cms/Controller/Adminhtml/Page/PostDataProcessor.php`** -> AI Confidence: **99.24%**
1363. **`app/code/Magento/Cms/Controller/Adminhtml/Page/Save.php`** -> AI Confidence: **99.24%**
1364. **`app/code/Magento/Cms/Model/Page/DataProvider.php`** -> AI Confidence: **99.24%**
1365. **`app/code/Magento/CompareListGraphQl/Model/Resolver/RemoveProductsFromCompareList.php`** -> AI Confidence: **99.24%**
1366. **`app/code/Magento/Config/App/Config/Source/DumpConfigSourceAggregated.php`** -> AI Confidence: **99.24%**
1367. **`app/code/Magento/Config/Block/System/Config/Form.php`** -> AI Confidence: **99.24%**
1368. **`app/code/Magento/ConfigurableProduct/Helper/Data.php`** -> AI Confidence: **99.24%**
1369. **`app/code/Magento/ConfigurableProduct/Model/LinkManagement.php`** -> AI Confidence: **99.24%**
1370. **`app/code/Magento/ConfigurableProduct/Model/Product/SaveHandler.php`** -> AI Confidence: **99.24%**
1371. **`app/code/Magento/ConfigurableProduct/Plugin/Model/ResourceModel/Product.php`** -> AI Confidence: **99.24%**
1372. **`app/code/Magento/ConfigurableProductGraphQl/Model/Options/Metadata.php`** -> AI Confidence: **99.24%**
1373. **`app/code/Magento/Csp/Model/Deploy/Package/Processor/PostProcessor/Integrity.php`** -> AI Confidence: **99.24%**
1374. **`app/code/Magento/Csp/Model/Mode/ConfigManager.php`** -> AI Confidence: **99.24%**
1375. **`app/code/Magento/Csp/Plugin/GenerateAssetIntegrity.php`** -> AI Confidence: **99.24%**
1376. **`app/code/Magento/Csp/Plugin/GenerateMergedAssetIntegrity.php`** -> AI Confidence: **99.24%**
1377. **`app/code/Magento/Customer/Block/Widget/Name.php`** -> AI Confidence: **99.24%**
1378. **`app/code/Magento/Customer/Controller/Account/CreatePost.php`** -> AI Confidence: **99.24%**
1379. **`app/code/Magento/Customer/Controller/Account/EditPost.php`** -> AI Confidence: **99.24%**
1380. **`app/code/Magento/Customer/Controller/Account/ResetPasswordPost.php`** -> AI Confidence: **99.24%**
1381. **`app/code/Magento/Customer/Controller/Address/FormPost.php`** -> AI Confidence: **99.24%**
1382. **`app/code/Magento/Customer/Controller/Adminhtml/Index/Save.php`** -> AI Confidence: **99.24%**
1383. **`app/code/Magento/Customer/Controller/Adminhtml/Index/Viewfile.php`** -> AI Confidence: **99.24%**
1384. **`app/code/Magento/Customer/Controller/Ajax/Login.php`** -> AI Confidence: **99.24%**
1385. **`app/code/Magento/Customer/Model/Account/Redirect.php`** -> AI Confidence: **99.24%**
1386. **`app/code/Magento/Customer/Model/AccountManagement.php`** -> AI Confidence: **99.24%**
1387. **`app/code/Magento/Customer/Model/Address/DataProvider.php`** -> AI Confidence: **99.24%**
1388. **`app/code/Magento/Customer/Model/AttributeMetadataResolver.php`** -> AI Confidence: **99.24%**
1389. **`app/code/Magento/Customer/Model/Customer/DataProvider.php`** -> AI Confidence: **99.24%**
1390. **`app/code/Magento/Customer/Model/ResourceModel/GroupRepository.php`** -> AI Confidence: **99.24%**
1391. **`app/code/Magento/Customer/Observer/AfterAddressSaveObserver.php`** -> AI Confidence: **99.24%**
1392. **`app/code/Magento/Deploy/Console/Command/App/ConfigImport/Processor.php`** -> AI Confidence: **99.24%**
1393. **`app/code/Magento/Deploy/Console/Command/SetModeCommand.php`** -> AI Confidence: **99.24%**
1394. **`app/code/Magento/Deploy/Package/PackagePool.php`** -> AI Confidence: **99.24%**
1395. **`app/code/Magento/Deploy/Package/Processor/PreProcessor/Css.php`** -> AI Confidence: **99.24%**
1396. **`app/code/Magento/Deploy/Strategy/StandardDeploy.php`** -> AI Confidence: **99.24%**
1397. **`app/code/Magento/Directory/Model/Currency/Import/CurrencyConverterApi.php`** -> AI Confidence: **99.24%**
1398. **`app/code/Magento/Downloadable/Controller/Download/Sample.php`** -> AI Confidence: **99.24%**
1399. **`app/code/Magento/Downloadable/Model/SampleRepository.php`** -> AI Confidence: **99.24%**
1400. **`app/code/Magento/Eav/Model/Attribute/Data/AbstractData.php`** -> AI Confidence: **99.24%**
1401. **`app/code/Magento/Eav/Model/Entity/Attribute/OptionManagement.php`** -> AI Confidence: **99.24%**
1402. **`app/code/Magento/Eav/Model/ResourceModel/ReadHandler.php`** -> AI Confidence: **99.24%**
1403. **`app/code/Magento/Eav/Setup/EavSetup.php`** -> AI Confidence: **99.24%**
1404. **`app/code/Magento/EavGraphQl/Model/Resolver/CustomAttributeMetadata.php`** -> AI Confidence: **99.24%**
1405. **`app/code/Magento/Email/Controller/Adminhtml/Email/Template/Save.php`** -> AI Confidence: **99.24%**
1406. **`app/code/Magento/GiftMessageGraphQl/Model/Resolver/Order/GiftMessage.php`** -> AI Confidence: **99.24%**
1407. **`app/code/Magento/GraphQl/Controller/GraphQl.php`** -> AI Confidence: **99.24%**
1408. **`app/code/Magento/GraphQl/Helper/Query/Logger/LogData.php`** -> AI Confidence: **99.24%**
1409. **`app/code/Magento/ImportExport/Model/Import/Entity/AbstractEntity.php`** -> AI Confidence: **99.24%**
1410. **`app/code/Magento/ImportExport/Ui/DataProvider/ExportFileDataProvider.php`** -> AI Confidence: **99.24%**
1411. **`app/code/Magento/Integration/Model/OauthService.php`** -> AI Confidence: **99.24%**
1412. **`app/code/Magento/JwtFrameworkAdapter/Model/JweManager.php`** -> AI Confidence: **99.24%**
1413. **`app/code/Magento/JwtFrameworkAdapter/Model/JwtManager.php`** -> AI Confidence: **99.24%**
1414. **`app/code/Magento/LoginAsCustomerAdminUi/Ui/Customer/Component/ConfirmationPopup/Options.php`** -> AI Confidence: **99.24%**
1415. **`app/code/Magento/MediaGalleryMetadata/Model/AddIptcMetadata.php`** -> AI Confidence: **99.24%**
1416. **`app/code/Magento/MediaGalleryMetadata/Model/File/ExtractMetadata.php`** -> AI Confidence: **99.24%**
1417. **`app/code/Magento/MediaGalleryUi/Model/Directories/GetDirectoryTree.php`** -> AI Confidence: **99.24%**
1418. **`app/code/Magento/MediaStorage/Service/ImageResize.php`** -> AI Confidence: **99.24%**
1419. **`app/code/Magento/Msrp/Helper/Data.php`** -> AI Confidence: **99.24%**
1420. **`app/code/Magento/Multishipping/Model/Cart/MultishippingClearItemAddress.php`** -> AI Confidence: **99.24%**
1421. **`app/code/Magento/Newsletter/Block/Adminhtml/Template/Preview.php`** -> AI Confidence: **99.24%**
1422. **`app/code/Magento/OfflineShipping/Model/ResourceModel/Carrier/Tablerate.php`** -> AI Confidence: **99.24%**
1423. **`app/code/Magento/OrderCancellationGraphQl/Model/Validator/ValidateGuestRequest.php`** -> AI Confidence: **99.24%**
1424. **`app/code/Magento/Payment/Gateway/Http/Client/Zend.php`** -> AI Confidence: **99.24%**
1425. **`app/code/Magento/Paypal/Model/Config/StructurePlugin.php`** -> AI Confidence: **99.24%**
1426. **`app/code/Magento/Paypal/Model/Report/Settlement/Row.php`** -> AI Confidence: **99.24%**
1427. **`app/code/Magento/PaypalGraphQl/Model/Resolver/PaypalExpressToken.php`** -> AI Confidence: **99.24%**
1428. **`app/code/Magento/Persistent/Observer/SetCheckoutSessionPersistentDataObserver.php`** -> AI Confidence: **99.24%**
1429. **`app/code/Magento/ProductAlert/Model/Mailing/AlertProcessor.php`** -> AI Confidence: **99.24%**
1430. **`app/code/Magento/Quote/Model/Cart/AddProductsToCart.php`** -> AI Confidence: **99.24%**
1431. **`app/code/Magento/Quote/Model/Quote.php`** -> AI Confidence: **99.24%**
1432. **`app/code/Magento/Quote/Model/QuoteRepository.php`** -> AI Confidence: **99.24%**
1433. **`app/code/Magento/Quote/Model/QuoteRepository/SaveHandler.php`** -> AI Confidence: **99.24%**
1434. **`app/code/Magento/Quote/Model/ShippingMethodManagement.php`** -> AI Confidence: **99.24%**
1435. **`app/code/Magento/Quote/Observer/Frontend/Quote/Address/CollectTotalsObserver.php`** -> AI Confidence: **99.24%**
1436. **`app/code/Magento/Quote/Plugin/UpdateCartId.php`** -> AI Confidence: **99.24%**
1437. **`app/code/Magento/QuoteGraphQl/Model/Cart/MergeCarts/CartQuantityValidator.php`** -> AI Confidence: **99.24%**
1438. **`app/code/Magento/QuoteGraphQl/Model/Resolver/ShippingAddress/SelectedShippingMethod.php`** -> AI Confidence: **99.24%**
1439. **`app/code/Magento/RequireJs/Block/Html/Head/Config.php`** -> AI Confidence: **99.24%**
1440. **`app/code/Magento/Review/Block/Adminhtml/Edit.php`** -> AI Confidence: **99.24%**
1441. **`app/code/Magento/Sales/Model/Order/Creditmemo/Validation/QuantityValidator.php`** -> AI Confidence: **99.24%**
1442. **`app/code/Magento/Sales/Model/Order/CustomerManagement.php`** -> AI Confidence: **99.24%**
1443. **`app/code/Magento/Sales/Model/OrderRepository.php`** -> AI Confidence: **99.24%**
1444. **`app/code/Magento/SalesRule/Model/ResourceModel/Report/Rule/Createdat.php`** -> AI Confidence: **99.24%**
1445. **`app/code/Magento/Shipping/Controller/Adminhtml/Order/Shipment/AddTrack.php`** -> AI Confidence: **99.24%**
1446. **`app/code/Magento/Shipping/Controller/Adminhtml/Order/ShipmentLoader.php`** -> AI Confidence: **99.24%**
1447. **`app/code/Magento/Sitemap/Model/Batch/Sitemap.php`** -> AI Confidence: **99.24%**
1448. **`app/code/Magento/Sitemap/Model/ResourceModel/Catalog/Batch/Product.php`** -> AI Confidence: **99.24%**
1449. **`app/code/Magento/Store/App/Action/Plugin/Context.php`** -> AI Confidence: **99.24%**
1450. **`app/code/Magento/Store/App/Response/Redirect.php`** -> AI Confidence: **99.24%**
1451. **`app/code/Magento/Store/Model/Config/Processor/Fallback.php`** -> AI Confidence: **99.24%**
1452. **`app/code/Magento/StoreGraphQl/Controller/HttpHeaderProcessor/StoreProcessor.php`** -> AI Confidence: **99.24%**
1453. **`app/code/Magento/Tax/Block/Adminhtml/Rule/Edit/Form.php`** -> AI Confidence: **99.24%**
1454. **`app/code/Magento/Theme/Block/Html/Topmenu.php`** -> AI Confidence: **99.24%**
1455. **`app/code/Magento/Theme/Controller/Result/AsyncCssPlugin.php`** -> AI Confidence: **99.24%**
1456. **`app/code/Magento/Theme/Model/Design/Backend/File.php`** -> AI Confidence: **99.24%**
1457. **`app/code/Magento/Theme/Ui/Component/Design/Config/DataProvider.php`** -> AI Confidence: **99.24%**
1458. **`app/code/Magento/Ui/Controller/Index/Render.php`** -> AI Confidence: **99.24%**
1459. **`app/code/Magento/Ui/Model/Export/MetadataProvider.php`** -> AI Confidence: **99.24%**
1460. **`app/code/Magento/User/Controller/Adminhtml/Auth/Forgotpassword.php`** -> AI Confidence: **99.24%**
1461. **`app/code/Magento/User/Observer/Backend/AuthObserver.php`** -> AI Confidence: **99.24%**
1462. **`app/code/Magento/Webapi/Model/Authorization/TokenUserContext.php`** -> AI Confidence: **99.24%**
1463. **`app/code/Magento/Weee/Block/Item/Price/Renderer.php`** -> AI Confidence: **99.24%**
1464. **`app/code/Magento/Weee/Helper/Data.php`** -> AI Confidence: **99.24%**
1465. **`app/code/Magento/Weee/Model/App/Action/ContextPlugin.php`** -> AI Confidence: **99.24%**
1466. **`app/code/Magento/Weee/Model/Total/Quote/WeeeTax.php`** -> AI Confidence: **99.24%**
1467. **`app/code/Magento/Widget/Model/Widget/Instance.php`** -> AI Confidence: **99.24%**
1468. **`app/code/Magento/Wishlist/Controller/Index/Add.php`** -> AI Confidence: **99.24%**
1469. **`app/code/Magento/Wishlist/Controller/Index/Cart.php`** -> AI Confidence: **99.24%**
1470. **`app/code/Magento/Wishlist/Controller/Index/Remove.php`** -> AI Confidence: **99.24%**
1471. **`app/code/Magento/Wishlist/Controller/Index/Send.php`** -> AI Confidence: **99.24%**
1472. **`app/code/Magento/Wishlist/Helper/Data.php`** -> AI Confidence: **99.24%**
1473. **`app/code/Magento/Wishlist/Model/ResourceModel/Item/Collection.php`** -> AI Confidence: **99.24%**
1474. **`dev/tests/integration/framework/Magento/TestFramework/TestCase/AbstractController.php`** -> AI Confidence: **99.24%**
1475. **`dev/tests/integration/framework/Magento/TestFramework/Workaround/Cleanup/StaticProperties.php`** -> AI Confidence: **99.24%**
1476. **`dev/tests/integration/framework/Magento/TestFramework/Workaround/Override/Config.php`** -> AI Confidence: **99.24%**
1477. **`dev/tests/integration/testsuite/Magento/Bundle/_files/bundle_product_single_dropdown_option.php`** -> AI Confidence: **99.24%**
1478. **`dev/tests/integration/testsuite/Magento/Bundle/_files/bundle_product_with_disabled_product_options.php`** -> AI Confidence: **99.24%**
1479. **`dev/tests/integration/testsuite/Magento/Bundle/_files/dynamic_bundle_product_with_catalog_rule_rollback.php`** -> AI Confidence: **99.24%**
1480. **`dev/tests/integration/testsuite/Magento/CatalogImportExport/Model/AbstractProductExportImportTestCase.php`** -> AI Confidence: **99.24%**
1481. **`dev/tests/integration/testsuite/Magento/Sales/_files/order_with_different_types_of_product.php`** -> AI Confidence: **99.24%**
1482. **`dev/tests/integration/testsuite/Magento/SalesRule/_files/cart_rule_free_shipping_by_cart.php`** -> AI Confidence: **99.24%**
1483. **`setup/src/Magento/Setup/Model/ConfigGenerator.php`** -> AI Confidence: **99.24%**
1484. **`setup/src/Magento/Setup/Model/ConfigOptionsList/Lock.php`** -> AI Confidence: **99.24%**
1485. **`setup/src/Magento/Setup/Model/ConfigOptionsList/PageCache.php`** -> AI Confidence: **99.24%**
1486. **`setup/src/Magento/Setup/Model/Installer.php`** -> AI Confidence: **99.24%**
1487. **`setup/src/Magento/Setup/Model/PhpReadinessCheck.php`** -> AI Confidence: **99.24%**
1488. **`setup/src/Magento/Setup/Module/Di/Compiler/Config/Reader.php`** -> AI Confidence: **99.24%**
1489. **`app/code/Magento/Authorization/Model/Acl/AclRetriever.php`** -> AI Confidence: **99.23%**
1490. **`app/code/Magento/Backend/Block/Dashboard/Totals.php`** -> AI Confidence: **99.23%**
1491. **`app/code/Magento/Catalog/Controller/Adminhtml/Product/MassStatus.php`** -> AI Confidence: **99.23%**
1492. **`app/code/Magento/Catalog/Model/Product/Option/Type/File/ValidatorInfo.php`** -> AI Confidence: **99.23%**
1493. **`app/code/Magento/Catalog/Model/ProductLink/CollectionProvider/LinkedMapProvider.php`** -> AI Confidence: **99.23%**
1494. **`app/code/Magento/Catalog/Model/ResourceModel/Category.php`** -> AI Confidence: **99.23%**
1495. **`app/code/Magento/Catalog/Model/ResourceModel/Product/Indexer/Price/TierPrice.php`** -> AI Confidence: **99.23%**
1496. **`app/code/Magento/Catalog/Ui/Component/ColumnFactory.php`** -> AI Confidence: **99.23%**
1497. **`app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/attribute/set/main.phtml`** -> AI Confidence: **99.23%**
1498. **`app/code/Magento/CatalogGraphQl/DataProvider/Product/LayeredNavigation/Builder/Attribute.php`** -> AI Confidence: **99.23%**
1499. **`app/code/Magento/CatalogImportExport/Model/Import/Product/LinkProcessor.php`** -> AI Confidence: **99.23%**
1500. **`app/code/Magento/CatalogImportExport/Model/Import/Uploader.php`** -> AI Confidence: **99.23%**
1501. **`app/code/Magento/CatalogInventory/Model/Indexer/ProductPriceIndexFilter.php`** -> AI Confidence: **99.23%**
1502. **`app/code/Magento/CatalogRule/Controller/Adminhtml/Promo/Catalog/Save.php`** -> AI Confidence: **99.23%**
1503. **`app/code/Magento/CatalogRule/Model/Indexer/ReindexRuleProduct.php`** -> AI Confidence: **99.23%**
1504. **`app/code/Magento/CatalogRule/Model/Indexer/ReindexRuleProductsPriceProcessor.php`** -> AI Confidence: **99.23%**
1505. **`app/code/Magento/CatalogUrlRewrite/Model/Product/Validator.php`** -> AI Confidence: **99.23%**
1506. **`app/code/Magento/Cms/Ui/Component/Listing/Column/PageActions.php`** -> AI Confidence: **99.23%**
1507. **`app/code/Magento/Config/App/Config/Source/RuntimeConfigSource.php`** -> AI Confidence: **99.23%**
1508. **`app/code/Magento/ConfigurableProduct/Controller/Adminhtml/Product/Initialization/Helper/Plugin/Configurable.php`** -> AI Confidence: **99.23%**
1509. **`app/code/Magento/Csp/Block/Sri/Hashes.php`** -> AI Confidence: **99.23%**
1510. **`app/code/Magento/Csp/Model/SubresourceIntegrity/HashResolver/HashResolver.php`** -> AI Confidence: **99.23%**
1511. **`app/code/Magento/Customer/Model/Metadata/Form/AbstractData.php`** -> AI Confidence: **99.23%**
1512. **`app/code/Magento/Customer/Model/ResourceModel/Address/Relation.php`** -> AI Confidence: **99.23%**
1513. **`app/code/Magento/Customer/view/frontend/templates/form/login.phtml`** -> AI Confidence: **99.23%**
1514. **`app/code/Magento/CustomerGraphQl/Model/Customer/Address/UpdateCustomerAddress.php`** -> AI Confidence: **99.23%**
1515. **`app/code/Magento/CustomerGraphQl/Model/Customer/Address/ValidateAddress.php`** -> AI Confidence: **99.23%**
1516. **`app/code/Magento/Deploy/Console/InputValidator.php`** -> AI Confidence: **99.23%**
1517. **`app/code/Magento/Deploy/Package/Processor/PostProcessor/CssUrls.php`** -> AI Confidence: **99.23%**
1518. **`app/code/Magento/Deploy/Service/DeployStaticContent.php`** -> AI Confidence: **99.23%**
1519. **`app/code/Magento/Downloadable/Helper/Download.php`** -> AI Confidence: **99.23%**
1520. **`app/code/Magento/Eav/Model/AttributeManagement.php`** -> AI Confidence: **99.23%**
1521. **`app/code/Magento/Elasticsearch/Model/Adapter/BatchDataMapper/ProductDataMapper.php`** -> AI Confidence: **99.23%**
1522. **`app/code/Magento/Elasticsearch/SearchAdapter/Query/Builder/MatchQuery.php`** -> AI Confidence: **99.23%**
1523. **`app/code/Magento/Elasticsearch8/Model/Client/Elasticsearch.php`** -> AI Confidence: **99.23%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `46` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `52115` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `app/code/Magento/MediaGalleryUi/view/adminhtml/web/js/directory/directories.js` (JAVASCRIPT) -> Cumulative Risk: **654.73**
- **Archetype:** `file_cluster_8` (Distance: 11.675 IQR)
- **Magnitude:** 128.68 | **LOC:** 209 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9955%)
- **Heaviest Functions:** `define` (Impact: 19.0), `getNewFolderPath` (Impact: 5.5), `deleteFolder` (Impact: 4.8)

### 2. `app/code/Magento/CatalogInventory/view/adminhtml/web/js/components/use-config-min-sale-qty.js` (JAVASCRIPT) -> Cumulative Risk: **638.88**
- **Archetype:** `file_cluster_4` (Distance: 14.815 IQR)
- **Magnitude:** 143.14 | **LOC:** 85 | **CtrlFlow:** 77.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (98.5667%)
- **Heaviest Functions:** `define` (Impact: 34.5), `onCheckedChanged` (Impact: 23.4), `changeVisibleDisabled` (Impact: 14.2)

### 3. `app/code/Magento/MediaGalleryUi/view/adminhtml/web/js/directory/directoryTree.js` (JAVASCRIPT) -> Cumulative Risk: **636.62**
- **Archetype:** `file_cluster_4` (Distance: 13.733 IQR)
- **Magnitude:** 667.64 | **LOC:** 674 | **CtrlFlow:** 51.4% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (91.3654%)
- **Heaviest Functions:** `define` (Impact: 126.1), `updateSelectedDirectory` (Impact: 31.9), `ensurePathLoaded` (Impact: 14.7)

### 4. `app/code/Magento/Paypal/view/frontend/web/js/view/paylater.js` (JAVASCRIPT) -> Cumulative Risk: **635.8**
- **Archetype:** `file_cluster_8` (Distance: 13.324 IQR)
- **Magnitude:** 122.78 | **LOC:** 135 | **CtrlFlow:** 61.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (89.8824%)
- **Heaviest Functions:** `define` (Impact: 26.1), `initialize` (Impact: 19.4), `getAttribute` (Impact: 3.7)

### 5. `app/code/Magento/MediaGalleryUi/view/adminhtml/web/js/image/image-details.js` (JAVASCRIPT) -> Cumulative Risk: **630.76**
- **Archetype:** `file_cluster_8` (Distance: 13.753 IQR)
- **Magnitude:** 129.54 | **LOC:** 185 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9955%)
- **Heaviest Functions:** `define` (Impact: 23.7), `showImageDetailsById` (Impact: 8.0), `openImageDetailsModal` (Impact: 5.7)

### 6. `app/code/Magento/Ui/view/base/web/js/grid/toolbar.js` (JAVASCRIPT) -> Cumulative Risk: **627.68**
- **Archetype:** `file_cluster_8` (Distance: 13.489 IQR)
- **Magnitude:** 277.0 | **LOC:** 610 | **CtrlFlow:** 38.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (94.9539%)
- **Heaviest Functions:** `define` (Impact: 47.9), `refresh` (Impact: 11.4), `updateStickyTableOffset` (Impact: 6.3)

### 7. `app/code/Magento/Ui/view/base/web/js/grid/columns/actions.js` (JAVASCRIPT) -> Cumulative Risk: **622.68**
- **Archetype:** `file_cluster_8` (Distance: 12.87 IQR)
- **Magnitude:** 107.04 | **LOC:** 341 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (98.9114%), Concurrency (98.6362%)
- **Heaviest Functions:** `define` (Impact: 19.4), `getAction` (Impact: 5.5), `isHandlerRequired` (Impact: 5.4)

### 8. `app/code/Magento/Payment/view/frontend/web/js/view/payment/iframe.js` (JAVASCRIPT) -> Cumulative Risk: **617.85**
- **Archetype:** `file_cluster_8` (Distance: 12.502 IQR)
- **Magnitude:** 108.9 | **LOC:** 229 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.623%), Concurrency (89.5241%)
- **Heaviest Functions:** `define` (Impact: 16.0), `placeOrder` (Impact: 8.2), `timeoutHandler` (Impact: 2.5)

### 9. `app/code/Magento/MediaGalleryUi/view/adminhtml/web/js/image/image-edit.js` (JAVASCRIPT) -> Cumulative Risk: **614.85**
- **Archetype:** `file_cluster_8` (Distance: 13.241 IQR)
- **Magnitude:** 173.12 | **LOC:** 238 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (97.1484%), Safety Score (90.6578%)
- **Heaviest Functions:** `define` (Impact: 28.4), `showEditDetailsPanel` (Impact: 8.0), `addKeyword` (Impact: 6.1)

### 10. `app/code/Magento/ProductVideo/view/frontend/web/js/load-player.js` (JAVASCRIPT) -> Cumulative Risk: **611.37**
- **Archetype:** `file_cluster_15` (Distance: 13.987 IQR)
- **Magnitude:** 379.06 | **LOC:** 393 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (94.3541%)
- **Heaviest Functions:** `define` (Impact: 69.4), `_create` (Impact: 24.3), `onStateChange` (Impact: 14.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `app/code/Magento/Ups/Model/Carrier.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.443 IQR)
- **Top Global Matches:** file_cluster_13: 14.443, file_cluster_8: 14.467, file_cluster_7: 14.621
- **Magnitude:** 2362.12 | **LOC:** 3012 | **CtrlFlow:** 59.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (36.92%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_formShipmentRequest` (Impact: 80.2)
  * `_formShipmentRestRequest` (Impact: 72.5)
  * `setRequest` (Impact: 61.8)
    * *Intent:* * @param LoggerInterface $logger * @param Security $xmlSecurity * @param ElementFactory $xmlElFactor...
  * `processShippingRestRateForItem` (Impact: 48.4)
  * `getContainerTypes` (Impact: 44.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 373`, `structural_boundaries: 250`, `args: 58`, `func_start: 55`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 1315`
* *Architecture:* `api: 33`, `import: 44`
* *Defense:* `safety: 76`, `doc: 268`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.044
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 21):` Throwable, Magento\Store\Model\ScopeInterface, Magento\Directory\Model\RegionFactory, Magento\Shipping\Model\Rate\Result\ProxyDeferredFactory, 2 => __('Adult Signature Required')], Magento\Shipping\Model\Carrier\AbstractCarrierOnline, Laminas\Http\Client, Magento\Framework\Measure\Length...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/code/Magento/Sales/Model/Order.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.123 IQR)
- **Top Global Matches:** file_cluster_8: 13.123, file_cluster_7: 13.176, file_cluster_13: 13.191
- **Magnitude:** 2255.16 | **LOC:** 4738 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (24.2967%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `canCancel` (Impact: 24.3)
  * `_canReorder` (Impact: 24.2)
  * `registerCancellation` (Impact: 21.3)
  * `getCustomerName` (Impact: 20.3)
  * `checkItemShipping` (Impact: 20.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 232`, `structural_boundaries: 888`, `args: 375`, `func_start: 375`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 433`
* *Architecture:* `api: 636`, `import: 44`
* *Defense:* `safety: 17`, `doc: 824`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.58
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 30):` Magento\Framework\Api\ExtensionAttributesFactory, Magento\Sales\Model\ResourceModel\Order\Item\CollectionFactory, Magento\Sales\Model\ResourceModel\Order\Shipment\Collection, Magento\Sales\Model\Order\Status\HistoryFactory, Magento\Sales\Model\Order\StatusLabel, Magento\Store\Model\ScopeInterface, Magento\Directory\Model\RegionFactory, Magento\Framework\Api\SearchCriteriaBuilder...
  * `Imported By (In-Degree: 161):` (Excluded from Brief to save tokens)

### `app/code/Magento/CatalogImportExport/Model/Import/Product/Option.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.659 IQR)
- **Top Global Matches:** file_cluster_8: 14.659, file_cluster_13: 14.663, file_cluster_7: 14.779
- **Magnitude:** 1615.34 | **LOC:** 2252 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (39.2344%), Tech Debt (16.3599%)
**Top Internal Functions/Classes:**
  * `__construct` (Impact: 59.2)
  * `_importData` (Impact: 41.9)
    * *Intent:* /** * Save option data in array for non-existing new product * * @param array $rowData
  * `_parseCustomOptions` (Impact: 30.6)
  * `_getSpecificTypeData` (Impact: 29.4)
  * `_initSourceEntities` (Impact: 27.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 313`, `structural_boundaries: 220`, `args: 63`, `func_start: 61`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 749`, `dead_code: 1`, `planned_debt: 1`, `orphaned_logic: 7`
* *Architecture:* `api: 28`, `import: 20`
* *Defense:* `safety: 111`, `doc: 332`, `immutability_locks: 23`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` 
    protected function _parseRequiredData(array $rowData)
    
        if ($this->_rowProductId === null) 
            return false, Magento\ImportExport\Model\Import, $rowNumber, Magento\Catalog\Model\ResourceModel\Product\Option\Value\CollectionFactory, d_options' => 0, Magento\ImportExport\Model\Import\ErrorProcessing\ProcessingErrorAggregatorInterface, Magento\CatalogImportExport\Model\Import\Product, Magento\Store\Model\Store...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/code/Magento/Dhl/Model/Carrier.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.241 IQR)
- **Top Global Matches:** file_cluster_13: 14.241, file_cluster_8: 14.409, file_cluster_7: 14.579
- **Magnitude:** 1458.96 | **LOC:** 2939 | **CtrlFlow:** 56.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.3832%), Tech Debt (12.7316%)
**Top Internal Functions/Classes:**
  * `_doShipmentRequestRest` (Impact: 63.8)
  * `_doRequest` (Impact: 60.1)
  * `_addRate` (Impact: 53.4)
  * `_parseXmlTrackingResponse` (Impact: 52.7)
  * `_addRestRate` (Impact: 46.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 276`, `structural_boundaries: 214`, `args: 46`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 758`, `dead_code: 1`, `orphaned_logic: 8`
* *Architecture:* `api: 19`, `import: 55`
* *Defense:* `safety: 100`, `doc: 192`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` Throwable, Magento\Store\Model\ScopeInterface, Magento\Directory\Model\RegionFactory, Magento\Sales\Exception\DocumentValidationException, Magento\Shipping\Model\Rate\Result\ProxyDeferredFactory, Magento\Framework\App\ProductMetadataInterface, Magento\Catalog\Model\Product\Type, Laminas\Http\Request...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/code/Magento/Catalog/Model/ResourceModel/Product/Collection.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.848 IQR)
- **Top Global Matches:** file_cluster_13: 13.848, file_cluster_8: 13.855, file_cluster_7: 13.938
- **Magnitude:** 1377.68 | **LOC:** 2584 | **CtrlFlow:** 46.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (36.5377%), Tech Debt (8.1641%)
**Top Internal Functions/Classes:**
  * `__construct` (Impact: 113.2)
    * *Intent:* /**
  * `addAttributeToSort` (Impact: 32.2)
    * *Intent:* /** * Retrieve all ids for collection
  * `_productLimitationPrice` (Impact: 26.9)
  * `addAttributeToFilter` (Impact: 26.0)
  * `_productLimitationJoinWebsite` (Impact: 24.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 212`, `structural_boundaries: 249`, `args: 81`, `func_start: 79`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 597`, `planned_debt: 1`
* *Architecture:* `api: 94`, `import: 19`
* *Defense:* `safety: 39`, `doc: 330`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.381
  * `Choke Point (Betweenness):` 0.000222 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` Magento\Customer\Model\Indexer\CustomerGroupDimensionProvider, 'left', Magento\Framework\DB\Select, 
    public function addFilterByRequiredOptions()
    
        $this->addAttributeToFilter('required_options', 
    public function requireTaxPercent()
    
        return $this->_addTaxPercents, Magento\Framework\EntityManager\MetadataPool, Zend_Db_Expr, 
    public function addStoreFilter($store = null)
    
        if ($store === null) 
            $store = $this->getStoreId(...
  * `Imported By (In-Degree: 72):` (Excluded from Brief to save tokens)

### `app/code/Magento/Sales/Api/Data/OrderInterface.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_7` (Drift: 11.939 IQR)
- **Top Global Matches:** file_cluster_7: 11.939, file_cluster_8: 11.975, file_cluster_1: 12.202
- **Magnitude:** 1327.96 | **LOC:** 2630 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.2472%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 277`, `args: 274`, `func_start: 274`, `class_start: 1`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 274`
* *Defense:* `doc: 688`, `immutability_locks: 136`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 105):` (Excluded from Brief to save tokens)

### `app/code/Magento/Shipping/view/adminhtml/web/order/packaging.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.555 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.525 IQR)
- **Top Global Matches:** file_cluster_8: 13.555, file_cluster_15: 13.755, file_cluster_11: 13.76
- **Magnitude:** 1324.96 | **LOC:** 920 | **CtrlFlow:** 53.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.1735%), Tech Debt (87.032%)
**Top Internal Functions/Classes:**
  * `define` (Impact: 303.5)
    * *Intent:* /** * Copyright 2014 Adobe
  * `sendCreateLabelRequest` (Impact: 64.2)
  * `packItems` (Impact: 36.8)
  * `processPackagePrepare` (Impact: 32.6)
  * `checkSizeAndGirthParameter` (Impact: 27.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 148`, `structural_boundaries: 130`, `args: 70`, `func_start: 43`
* *Risk/State:* `safety_bypasses: 35`, `high_risk_execution: 1`, `state_mutation: 619`, `duplicate_logic: 4`, `orphaned_logic: 22`
* *Architecture:* None
* *Defense:* `safety: 15`, `doc: 9`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/code/Magento/Sales/Model/Order/Payment.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.14 IQR)
- **Top Global Matches:** file_cluster_8: 13.14, file_cluster_7: 13.194, file_cluster_13: 13.293
- **Magnitude:** 1289.74 | **LOC:** 2618 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 80.0%
- **Risk Profile:** Cognitive Load (36.4127%), Tech Debt (9.3378%)
**Top Internal Functions/Classes:**
  * `__construct` (Impact: 32.6)
    * *Intent:* /**
  * `refund` (Impact: 30.8)
    * *Intent:* /** * Perform actions based on passed action name * * @param string $action
  * `updateOrder` (Impact: 30.3)
  * `place` (Impact: 25.2)
    * *Intent:* /** * Retrieve order model object * * @codeCoverageIgnore
  * `_void` (Impact: 22.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 375`, `args: 177`, `func_start: 177`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 350`, `dead_code: 1`, `planned_debt: 5`
* *Architecture:* `api: 267`, `import: 11`
* *Defense:* `safety: 11`, `doc: 429`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.397
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` Magento\Sales\Model\Order, $isOnline, 
    public function refund($creditmemo)
    
        $baseAmountToRefund = $this->formatAmount($creditmemo->getBaseGrandTotal(), 
    public function authorize($isOnline, Magento\Sales\Api\CreditmemoManagementInterface, 
    public function registerCaptureNotification($amount, $skipFraudDetection = false)
    
        return $this->orderPaymentProcessor->registerCaptureNotification($this, Magento\Sales\Model\Order\Payment\Info...
  * `Imported By (In-Degree: 41):` (Excluded from Brief to save tokens)

### `app/code/Magento/Ui/view/base/web/js/form/element/ui-select.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_15` (Drift: 14.598 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.039 IQR)
- **Top Global Matches:** file_cluster_15: 14.598, file_cluster_8: 14.674, file_cluster_7: 14.801
- **Magnitude:** 1271.12 | **LOC:** 1315 | **CtrlFlow:** 56.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (51.0802%), Tech Debt (77.7912%)
**Top Internal Functions/Classes:**
  * `define` (Impact: 256.7)
    * *Intent:* /** * Copyright 2015 Adobe * All Rights Reserved.
  * `setProperty` (Impact: 17.1)
  * `openChildLevel` (Impact: 16.5)
    * *Intent:* /** * Return formatted items placeholder.
  * `filterOptionsList` (Impact: 15.8)
  * `toggleOptionSelected` (Impact: 15.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 92`, `args: 77`, `func_start: 69`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 621`, `orphaned_logic: 26`
* *Architecture:* `io: 8`, `concurrency: 12`
* *Defense:* `safety: 20`, `doc: 165`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/code/Magento/Usps/Model/Carrier.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.027 IQR)
- **Top Global Matches:** file_cluster_8: 13.027, file_cluster_7: 13.214, file_cluster_13: 13.236
- **Magnitude:** 1269.72 | **LOC:** 2538 | **CtrlFlow:** 65.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (35.0969%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_formIntlShipmentRequest` (Impact: 104.2)
  * `setRequest` (Impact: 62.2)
    * *Intent:* * @param \Psr\Log\LoggerInterface $logger * @param Security $xmlSecurity * @param \Magento\Shipping\...
  * `_parseXmlResponse` (Impact: 59.3)
  * `_doShipmentRequest` (Impact: 48.5)
  * `_formUsSignatureConfirmationShipmentRequ` (Impact: 47.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 230`, `structural_boundaries: 120`, `args: 33`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 619`
* *Architecture:* `api: 45`, `import: 19`
* *Defense:* `safety: 30`, `doc: 183`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` 'False' => __('Required')]
        ], Magento\Shipping\Model\Rate\Result\ProxyDeferredFactory, Magento\Shipping\Helper\Carrier, Magento\Shipping\Model\Carrier\AbstractCarrierOnline, Magento\Shipping\Model\Carrier\AbstractCarrier, Magento\Framework\Measure\Length, Magento\Framework\HTTP\LaminasClientFactory, Magento\Framework\Async\CallbackDeferred...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/code/Magento/Sales/Model/Order/Item.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.115 IQR)
- **Top Global Matches:** file_cluster_8: 12.115, file_cluster_7: 12.182, file_cluster_13: 12.476
- **Magnitude:** 1207.2 | **LOC:** 2421 | **CtrlFlow:** 14.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (18.3418%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `isDummy` (Impact: 44.3)
    * *Intent:* /** * Retrieve order item statuses array *
  * `getStatusId` (Impact: 38.5)
  * `__construct` (Impact: 18.7)
    * *Intent:* /**
  * `isChildrenCalculated` (Impact: 9.5)
    * *Intent:* /** * Retrieve status *
  * `isShipSeparately` (Impact: 9.5)
    * *Intent:* /** * Cancel order item * * @return $this */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 477`, `args: 222`, `func_start: 222`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 182`
* *Architecture:* `api: 412`, `import: 3`
* *Defense:* `safety: 8`, `doc: 392`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.46
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Magento\Sales\Model\AbstractModel, Magento\Framework\Api\AttributeValueFactory, Magento\Sales\Api\Data\OrderItemInterface
  * `Imported By (In-Degree: 49):` (Excluded from Brief to save tokens)

### `app/code/Magento/ProductVideo/view/adminhtml/web/js/new-video-dialog.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.675 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.932 IQR)
- **Top Global Matches:** file_cluster_17: 13.675, file_cluster_8: 13.817, file_cluster_15: 13.879
- **Magnitude:** 1169.38 | **LOC:** 1352 | **CtrlFlow:** 57.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.3471%), Tech Debt (61.0097%)
**Top Internal Functions/Classes:**
  * `define` (Impact: 236.9)
    * *Intent:* /**
  * `_onUpdate` (Impact: 33.7)
  * `_onImageLoaded` (Impact: 19.5)
  * `_onCreate` (Impact: 19.1)
  * `update` (Impact: 18.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 75`, `args: 76`, `func_start: 57`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 584`, `duplicate_logic: 8`, `orphaned_logic: 6`
* *Architecture:* `io: 1`
* *Defense:* `safety: 22`, `doc: 98`, `immutability_locks: 6`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/code/Magento/Quote/Model/Quote.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.513 IQR)
- **Top Global Matches:** file_cluster_8: 13.513, file_cluster_13: 13.541, file_cluster_7: 13.548
- **Magnitude:** 1165.32 | **LOC:** 2736 | **CtrlFlow:** 41.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (45.6722%), Tech Debt (9.2964%)
**Top Internal Functions/Classes:**
  * `assignCustomerWithAddressChange` (Impact: 30.2)
  * `getShippingAddressesItems` (Impact: 29.8)
  * `updateItem` (Impact: 28.6)
  * `getItemVirtualQty` (Impact: 20.4)
  * `setShippingAddress` (Impact: 17.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 208`, `structural_boundaries: 289`, `args: 105`, `func_start: 105`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 373`, `dead_code: 1`, `planned_debt: 4`
* *Architecture:* `api: 163`, `import: 15`
* *Defense:* `safety: 22`, `doc: 451`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.658
  * `Choke Point (Betweenness):` 2.5e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` Magento\Store\Model\ScopeInterface, Magento\Quote\Model\Quote\Address\Total,  collect totals and save me, include_discount_amount', Magento\Quote\Api\Data\PaymentInterface, \Magento\Store\Model\ScopeInterface::SCOPE_STORE, Magento\Framework\Api\AttributeValueFactory, Discount ?
                    $address->getBaseSubtotalWithDiscount() + $taxes :
                    $address->getBaseSubtotal() + $taxes...
  * `Imported By (In-Degree: 132):` (Excluded from Brief to save tokens)

### `app/code/Magento/Fedex/Model/Carrier.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.72 IQR)
- **Top Global Matches:** file_cluster_8: 13.72, file_cluster_13: 13.84, file_cluster_7: 13.884
- **Magnitude:** 1155.82 | **LOC:** 1884 | **CtrlFlow:** 56.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (35.8098%), Tech Debt (8.7603%)
**Top Internal Functions/Classes:**
  * `processTrackingDetails` (Impact: 45.7)
  * `getContainerTypes` (Impact: 41.1)
  * `_formShipmentRequest` (Impact: 41.0)
  * `setRequest` (Impact: 34.2)
  * `_prepareRateResponse` (Impact: 23.4)
    * *Intent:* /** * Forming request for rate estimation depending to the purpose * * @param string $purpose * @ret...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 197`, `structural_boundaries: 151`, `args: 45`, `func_start: 45`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 572`, `fragile_debt: 1`
* *Architecture:* `api: 35`, `import: 15`
* *Defense:* `safety: 57`, `doc: 207`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.054
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` Magento\Sales\Model\Order, 'USE_SCHEDULED_PICKUP' => __('Use Scheduled Pickup'), 'KG' => __('Kilograms'), ]
        ], Magento\Shipping\Model\Carrier\AbstractCarrierOnline, 'ON_CALL' => __('On Call'), Magento\Framework\App\CacheInterface, Magento\Shipping\Model\Carrier\AbstractCarrier...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `app/code/Magento/Swatches/view/base/web/js/swatch-renderer.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.493 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.577 IQR)
- **Top Global Matches:** file_cluster_17: 13.493, file_cluster_8: 13.507, file_cluster_15: 13.557
- **Magnitude:** 1118.06 | **LOC:** 1508 | **CtrlFlow:** 57.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (49.7942%), Tech Debt (80.8428%)
**Top Internal Functions/Classes:**
  * `define` (Impact: 241.0)
    * *Intent:* /** * Copyright 2015 Adobe
  * `_init` (Impact: 193.4)
  * `_init` (Impact: 31.2)
  * `_UpdatePrice` (Impact: 23.5)
    * *Intent:* /** * Render swatch options by part of config * * @param {Object} config * @param {String} controlId
  * `_ProductMediaCallback` (Impact: 19.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 81`, `args: 70`, `func_start: 44`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 346`, `duplicate_logic: 6`, `orphaned_logic: 12`
* *Architecture:* `concurrency: 7`
* *Defense:* `safety: 23`, `doc: 84`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/code/Magento/Customer/Model/AccountManagement.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.904 IQR)
- **Top Global Matches:** file_cluster_13: 13.904, file_cluster_8: 14.175, file_cluster_7: 14.219
- **Magnitude:** 1098.56 | **LOC:** 1702 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (35.6164%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__construct` (Impact: 227.4)
    * *Intent:* /** * @var ManagerInterface */
  * `createAccountWithPasswordHash` (Impact: 44.8)
  * `initiatePasswordReset` (Impact: 23.6)
    * *Intent:* /**
  * `validateResetPasswordToken` (Impact: 16.8)
  * `checkPasswordStrength` (Impact: 15.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 224`, `args: 49`, `func_start: 48`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 103`, `state_mutation: 435`
* *Architecture:* `api: 66`, `import: 52`
* *Defense:* `safety: 56`, `doc: 332`, `test: 1`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.141
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 26):` Magento\Customer\Api\AccountManagementInterface, Magento\Framework\Exception\InvalidEmailOrPasswordException, Magento\Customer\Api\CustomerMetadataInterface, Magento\Framework\AuthorizationInterface, 
    public const NEW_ACCOUNT_EMAIL_REGISTERED_NO_PASSWORD = 'registered_no_password', Magento\Store\Model\ScopeInterface, $customer->getId(), Magento\Framework\Api\SearchCriteriaBuilder...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `app/code/Magento/Paypal/Model/Config.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.44 IQR)
- **Top Global Matches:** file_cluster_8: 12.44, file_cluster_7: 12.556, file_cluster_13: 12.83
- **Magnitude:** 1050.12 | **LOC:** 1872 | **CtrlFlow:** 59.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.8789%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `isMethodAvailable` (Impact: 51.4)
  * `_getSpecificConfigPath` (Impact: 47.3)
    * *Intent:* /** * Return supported types for PayPal logo
  * `_mapWpukFieldset` (Impact: 34.5)
    * *Intent:* /**
  * `_mapExpressFieldset` (Impact: 34.1)
    * *Intent:* /** * Express Checkout button "flavors" source getter * * @return array
  * `_mapWppFieldset` (Impact: 27.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 230`, `structural_boundaries: 158`, `args: 61`, `func_start: 61`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 310`
* *Architecture:* `api: 130`, `import: 4`
* *Defense:* `safety: 1`, `doc: 230`, `immutability_locks: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.49
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Magento\Framework\App\ObjectManager, 
    public function getExpressCheckoutSolutionTypes()
    
        return [self::EC_SOLUTION_TYPE_SOLE => __('Yes'), Formatter, self::EC_SOLUTION_TYPE_MARK => __('No')], customer to do after placing the order.
     *
     * For instance, 
    public function getExpressCheckoutCompleteUrl($token)
    
        return $this->getPaypalUrl(['cmd' => '_complete-express-checkout', 
    public function getRequireBillingAddressOptions()
    
        return [
            self::REQUIRE_BILLING_ADDRESS_ALL => __('Yes'), _BILLING_ADDRESS_ALL = 1...
  * `Imported By (In-Degree: 41):` (Excluded from Brief to save tokens)

### `app/code/Magento/Catalog/Model/Product.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.149 IQR)
- **Top Global Matches:** file_cluster_8: 13.149, file_cluster_7: 13.156, file_cluster_13: 13.215
- **Magnitude:** 1034.64 | **LOC:** 2859 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (38.4821%), Tech Debt (9.1008%)
**Top Internal Functions/Classes:**
  * `processBuyRequest` (Impact: 99.5)
    * *Intent:* /** * Check if data was changed * * @return bool
  * `getIdentities` (Impact: 22.5)
  * `getMediaGalleryImages` (Impact: 18.7)
    * *Intent:* /** * Get product attribute set id
  * `__toArray` (Impact: 14.9)
    * *Intent:* /**
  * `setMediaGalleryEntries` (Impact: 10.5)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 282`, `args: 120`, `func_start: 118`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 286`, `planned_debt: 3`
* *Architecture:* `api: 182`, `import: 13`
* *Defense:* `safety: 13`, `doc: 447`, `immutability_locks: 4`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.002
  * `Choke Point (Betweenness):` 3.1e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` Magento\Framework\Api\AttributeValueFactory, Magento\Framework\App\ObjectManager, Magento\Catalog\Model\Product\Attribute\Backend\Media\EntryConverterPool, Magento\Framework\DataObject\IdentityInterface, Magento\Catalog\Api\Data\ProductAttributeMediaGalleryEntryInterface, d_options') === null) 
            $this->setRequiredOptions(false, Magento\Framework\Pricing\SaleableInterface, Magento\Framework\ObjectManager\ResetAfterRequestInterface...
  * `Imported By (In-Degree: 404):` (Excluded from Brief to save tokens)

### `app/code/Magento/Sales/Model/AdminOrder/Create.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.965 IQR)
- **Top Global Matches:** file_cluster_13: 13.965, file_cluster_8: 14.049, file_cluster_7: 14.104
- **Magnitude:** 1013.82 | **LOC:** 2434 | **CtrlFlow:** 54.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (49.6076%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `initFromOrder` (Impact: 292.8)
  * `_validate` (Impact: 35.7)
  * `_prepareCustomerAddress` (Impact: 28.4)
  * `formattedOptions` (Impact: 23.5)
  * `importPostData` (Impact: 21.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 149`, `structural_boundaries: 127`, `args: 44`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 354`
* *Architecture:* `api: 36`, `import: 18`
* *Defense:* `safety: 51`, `doc: 261`, `immutability_locks: 2`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.068
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` Magento\Sales\Model\Order, 
    private function isEmailRequired(): bool
    
        return (bool)$this->_scopeConfig->getValue(
            self::XML_PATH_EMAIL_REQUIRED_CREATE_ORDER, Magento\Payment\Model\MethodInterface, Magento\Quote\Model\Quote\Address\CustomAttributeListInterface, Magento\Quote\Model\Quote\Item, \Magento\Store\Model\ScopeInterface::SCOPE_STORE, Magento\Customer\Model\Metadata\Form, Magento\Framework\App\Request\Http...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `app/code/Magento/CatalogImportExport/Model/Import/Product.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.088 IQR)
- **Top Global Matches:** file_cluster_13: 14.088, file_cluster_8: 14.244, file_cluster_7: 14.297
- **Magnitude:** 1005.4 | **LOC:** 3680 | **CtrlFlow:** 47.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (36.2661%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `formatStockDataForRow` (Impact: 28.6)
  * `validateRow` (Impact: 20.7)
  * `_saveStockItem` (Impact: 19.5)
  * `saveProductToWebsitePhase` (Impact: 19.4)
    * *Intent:* * @param \Magento\Catalog\Helper\Data $catalogData * @param \Magento\ImportExport\Model\Import\Confi...
  * `findImageByColumnImageUsingHash` (Impact: 19.2)
    * *Intent:* /** * Set valid attribute set and product type to rows. * * Set valid attribute set and product type...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 178`, `structural_boundaries: 196`, `args: 60`, `func_start: 60`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 515`, `dead_code: 1`
* *Architecture:* `api: 67`, `import: 33`
* *Defense:* `safety: 48`, `doc: 370`, `test: 1`, `immutability_locks: 30`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.213
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` path used for attribute %s', Magento\Framework\Filesystem, \'text\'', Magento\ImportExport\Model\Import\Entity\AbstractEntity, ValidatorInterface::ERROR_DUPLICATE_MULTISELECT_VALUES => 'Value for multiselect attribute %s contains duplicated values', Magento\ImportExport\Model\Import, 'invalidNewToDateValue' => 'Make sure new_to_date is later than or the same, \'radio\'...
  * `Imported By (In-Degree: 23):` (Excluded from Brief to save tokens)

### `app/code/Magento/CatalogImportExport/Model/Export/Product.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.487 IQR)
- **Top Global Matches:** file_cluster_8: 13.487, file_cluster_7: 13.646, file_cluster_13: 13.675
- **Magnitude:** 967.16 | **LOC:** 2366 | **CtrlFlow:** 50.7% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (35.6247%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getCustomOptionsData` (Impact: 27.4)
  * `__construct` (Impact: 25.4)
    * *Intent:* /** * Provider of product link types * * @var \Magento\Catalog\Model\Product\LinkTypeProvider */
  * `filterAttributeCollection` (Impact: 21.4)
  * `getMemoryLimitForPagination` (Impact: 19.0)
  * `processExportData` (Impact: 17.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 153`, `structural_boundaries: 149`, `args: 45`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 524`
* *Architecture:* `api: 13`, `import: 12`
* *Defense:* `safety: 27`, `doc: 227`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.04
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` Magento\Store\Model\Store, d'] = $this->getOptionValue('is_require', Magento\Framework\App\ObjectManager, Magento\Catalog\Model\Product, Magento\Catalog\Model\ResourceModel\Product\Option\Collection, Magento\Eav\Model\Entity\Collection\AbstractCollection, Magento\ImportExport\Model\Export\Adapter\AbstractAdapter, Magento\ImportExport\Model\Import...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/code/Magento/Eav/Model/Entity/Collection/AbstractCollection.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.316 IQR)
- **Top Global Matches:** file_cluster_13: 14.316, file_cluster_8: 14.342, file_cluster_7: 14.42
- **Magnitude:** 965.96 | **LOC:** 1789 | **CtrlFlow:** 55.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.3583%), Tech Debt (9.7841%)
**Top Internal Functions/Classes:**
  * `joinAttribute` (Impact: 61.9)
  * `joinField` (Impact: 44.8)
  * `joinTable` (Impact: 44.5)
    * *Intent:* /** * Add attribute to sort order
  * `_loadAttributes` (Impact: 40.1)
    * *Intent:* * Developer is encouraged to use existing instances of attributes and entities * After first use of ...
  * `addAttributeToFilter` (Impact: 28.1)
    * *Intent:* /** * Attributes to be filtered order sorted by * * @var array
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 180`, `structural_boundaries: 145`, `args: 41`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 416`, `dead_code: 1`, `planned_debt: 3`
* *Architecture:* `io: 4`, `api: 56`, `import: 4`
* *Defense:* `safety: 61`, `doc: 170`, `test: 1`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.298
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Magento\Framework\DB\Select, Magento\Framework\Data\Collection\AbstractDb, Magento\Framework\App\ResourceConnection\SourceProviderInterface, Magento\Framework\Exception\LocalizedException
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `app/code/Magento/Eav/Setup/EavSetup.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.041 IQR)
- **Top Global Matches:** file_cluster_8: 13.041, file_cluster_7: 13.153, file_cluster_13: 13.186
- **Magnitude:** 964.5 | **LOC:** 1532 | **CtrlFlow:** 45.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.7707%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `installEntities` (Impact: 42.6)
  * `__construct` (Impact: 35.9)
  * `_updateAttributeAdditionalData` (Impact: 25.0)
  * `addAttribute` (Impact: 24.8)
    * *Intent:* /** * Get number of all attributes in group * * @param int|string $entityTypeId * @param int|string ...
  * `_updateAttribute` (Impact: 24.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 186`, `args: 49`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 179`, `state_mutation: 425`
* *Architecture:* `api: 54`, `import: 13`
* *Defense:* `safety: 39`, `doc: 262`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.485
  * `Choke Point (Betweenness):` 1.4e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` Magento\Eav\Model\AttributeFactory, Magento\Framework\Exception\LocalizedException, Magento\Framework\App\ObjectManager, Magento\Framework\Setup\ModuleDataSetupInterface, Magento\Eav\Model\Config, Magento\Eav\Model\Entity\Setup\Context, Magento\Eav\Model\Entity\Attribute, Magento\Eav\Model\Entity\Setup\PropertyMapperInterface...
  * `Imported By (In-Degree: 32):` (Excluded from Brief to save tokens)

### `app/code/Magento/Quote/Model/Quote/Address.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.218 IQR)
- **Top Global Matches:** file_cluster_13: 13.218, file_cluster_8: 13.385, file_cluster_7: 13.419
- **Magnitude:** 940.02 | **LOC:** 1826 | **CtrlFlow:** 31.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.3713%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__construct` (Impact: 66.4)
  * `requestShippingRates` (Impact: 50.6)
  * `getAllItems` (Impact: 28.3)
  * `addItem` (Impact: 15.6)
  * `getItemQty` (Impact: 14.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 266`, `args: 97`, `func_start: 97`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 281`
* *Architecture:* `api: 152`, `import: 41`
* *Defense:* `safety: 8`, `doc: 371`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.008
  * `Choke Point (Betweenness):` 3e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 25):` Magento\Framework\Api\ExtensionAttributesFactory, Magento\Framework\DataObject\Copy, Magento\Shipping\Model\CarrierFactoryInterface, Magento\Quote\Model\Quote\Address\Total\Collector, Magento\Directory\Model\RegionFactory, Magento\Customer\Model\Address\AbstractAddress, Magento\Customer\Api\Data\AddressInterfaceFactory, Magento\Store\Model\ScopeInterface...
  * `Imported By (In-Degree: 48):` (Excluded from Brief to save tokens)

### `app/code/Magento/Catalog/view/adminhtml/web/catalog/product/composite/configure.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.83 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.232 IQR)
- **Top Global Matches:** file_cluster_8: 13.83, file_cluster_15: 13.895, file_cluster_11: 14.006
- **Magnitude:** 932.22 | **LOC:** 857 | **CtrlFlow:** 59.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (51.8181%), Tech Debt (98.3797%)
**Top Internal Functions/Classes:**
  * `define` (Impact: 173.1)
    * *Intent:* /** * Copyright 2014 Adobe * All Rights Reserved.
  * `submit` (Impact: 123.1)
  * `rename` (Impact: 76.0)
  * `_renameFields` (Impact: 28.9)
  * `getConfirmedValues` (Impact: 16.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 58`, `args: 28`, `func_start: 33`
* *Risk/State:* `safety_bypasses: 17`, `high_risk_execution: 2`, `state_mutation: 357`, `duplicate_logic: 6`, `orphaned_logic: 10`
* *Architecture:* `concurrency: 7`
* *Defense:* `safety: 8`, `doc: 38`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `app/code/Magento/Catalog/view/adminhtml/templates/catalog/product/edit/options/option.phtml` (PHP) | Magnitude: 32.48 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 104, branch: 79, structural_boundaries: 21, decorators: 20
- `app/code/Magento/Ui/view/adminhtml/web/templates/modal/modal-prompt-content.html` (HTML) | Magnitude: 17.28 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 12, ssr_boundaries: 7, args: 5, decorators: 5
- `app/code/Magento/Ui/view/base/web/templates/modal/modal-prompt-content.html` (HTML) | Magnitude: 17.28 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 12, ssr_boundaries: 7, args: 5, decorators: 5
- `dev/tests/api-functional/framework/Magento/TestFramework/TestCase/HttpClient/CurlClient.php` (PHP) | Magnitude: 141.26 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 103, state_mutation: 78, doc: 43, structural_boundaries: 24
- `app/code/Magento/Catalog/view/frontend/web/template/product/image.html` (HTML) | Magnitude: 11.52 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: args: 1, io: 1, concurrency: 1, decorators: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `app/code/Magento/Quote/Model/ResourceModel/Quote/Address/Collection.php` (PHP) | Magnitude: 12.4 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 20, doc: 13, structural_boundaries: 8, encapsulation: 4
- `app/code/Magento/PageCache/Model/Cache/Type.php` (PHP) | Magnitude: 11.52 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, doc: 13, structural_boundaries: 7, api: 4
- `app/code/Magento/Reports/Model/ResourceModel/Event/Collection.php` (PHP) | Magnitude: 40.74 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 37, doc: 17, branch: 10, structural_boundaries: 8
- `app/code/Magento/Translation/Model/Inline/CacheManager.php` (PHP) | Magnitude: 12.44 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 22, doc: 17, structural_boundaries: 5, state_mutation: 5
- `app/code/Magento/Reports/Observer/CatalogProductViewObserver.php` (PHP) | Magnitude: 26.28 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 37, doc: 25, state_mutation: 9, structural_boundaries: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `app/code/Magento/CatalogImportExport/Model/Export/RowCustomizer/Composite.php` (PHP) | Magnitude: 35.42 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 39, doc: 24, structural_boundaries: 17, state_mutation: 12
- `app/code/Magento/ConfigurableProduct/Model/ResourceModel/Product/Indexer/Price/OptionsSelectBuilder.php` (PHP) | Magnitude: 30.94 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 52, state_mutation: 16, doc: 16, structural_boundaries: 11
- `app/code/Magento/Tax/Model/Api/SearchCriteria/JoinProcessor/CalculationData.php` (PHP) | Magnitude: 7.1 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 8, doc: 6, branch: 2
- `app/code/Magento/User/ViewModel/JsonSerializer.php` (PHP) | Magnitude: 7.72 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 8, doc: 8, args: 2
- `dev/tests/integration/framework/Magento/TestFramework/Eav/Model/ResourceModel/GetEntityIdByAttributeId.php` (PHP) | Magnitude: 32.16 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 21, doc: 11, state_mutation: 10, branch: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `app/code/Magento/Ui/view/base/web/js/grid/masonry.js` (JAVASCRIPT) | Magnitude: 183.8 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 147, state_mutation: 80, doc: 48, args: 21
- `app/code/Magento/Msrp/view/base/web/js/msrp.js` (JAVASCRIPT) | Magnitude: 386.8 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 252, state_mutation: 215, doc: 33, branch: 30
- `app/code/Magento/Catalog/view/frontend/web/js/product/provider.js` (JAVASCRIPT) | Magnitude: 174.08 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 136, state_mutation: 73, doc: 29, branch: 17
- `app/code/Magento/Ui/view/base/web/js/form/element/single-checkbox.js` (JAVASCRIPT) | Magnitude: 540.62 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 281, indent_spaces: 153, branch: 64, safety: 23
- `app/code/Magento/Ui/view/base/web/js/modal/modal.js` (JAVASCRIPT) | Magnitude: 632.24 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 410, indent_spaces: 289, branch: 42, doc: 42

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `app/code/Magento/Swatches/view/base/web/js/swatch-renderer.js` (JAVASCRIPT) | Magnitude: 1118.06 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 695, state_mutation: 346, branch: 111, doc: 84
- `app/code/Magento/GroupedProduct/view/adminhtml/web/js/grouped-product-grid.js` (JAVASCRIPT) | Magnitude: 234.12 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 118, state_mutation: 113, doc: 31, bitwise_ops: 30
- `app/code/Magento/MediaStorage/Model/File/Validator/AvailablePath.php` (PHP) | Magnitude: 129.44 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 60, indent_spaces: 55, branch: 32, safety: 7
- `app/code/Magento/Catalog/view/adminhtml/web/js/product-gallery.js` (JAVASCRIPT) | Magnitude: 646.9 | Delta: **0.082 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 547, state_mutation: 326, doc: 60, branch: 57
- `app/code/Magento/Customer/view/adminhtml/web/js/form/element/region.js` (JAVASCRIPT) | Magnitude: 44.56 | Delta: **0.097 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 21, indent_spaces: 20, branch: 5, args: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `app/code/Magento/Newsletter/Block/Adminhtml/Problem/Grid/Renderer/Checkbox.php` (PHP) | Magnitude: 3.38 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 6, doc: 5, indent_spaces: 4, branch: 1
- `app/code/Magento/ConfigurableProduct/view/adminhtml/templates/catalog/product/attribute/set/js.phtml` (PHP) | Magnitude: 24.3 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 9, branch: 7, doc: 5, indent_spaces: 5
- `app/code/Magento/Ui/view/base/web/templates/grid/toolbar.html` (HTML) | Magnitude: 15.36 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 9, decorators: 8, ui_framework: 5
- `app/code/Magento/Review/view/adminhtml/templates/rating/stars/summary.phtml` (PHP) | Magnitude: 15.28 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 14, indent_spaces: 9, doc: 4, structural_boundaries: 2
- `app/code/Magento/User/view/adminhtml/templates/admin/resetforgottenpassword.phtml` (PHP) | Magnitude: 16.18 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 55, branch: 24, structural_boundaries: 17, ui_framework: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `app/code/Magento/GoogleGtag/view/frontend/web/js/google-analytics.js` (JAVASCRIPT) | Magnitude: 58.92 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 48, state_mutation: 13, branch: 11, func_start: 7
- `app/code/Magento/Ui/view/base/web/js/grid/editing/editor-view.js` (JAVASCRIPT) | Magnitude: 93.34 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 104, state_mutation: 28, doc: 23, concurrency: 19
- `app/code/Magento/Catalog/view/adminhtml/web/component/static-type-input.js` (JAVASCRIPT) | Magnitude: 45.36 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 25, state_mutation: 22, doc: 7, concurrency: 6
- `app/code/Magento/Ui/view/base/web/js/grid/url-filter-applier.js` (JAVASCRIPT) | Magnitude: 89.56 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 65, state_mutation: 34, concurrency: 12, structural_boundaries: 8
- `app/code/Magento/MediaGalleryRenditions/Model/Queue/FetchRenditionPathsBatches.php` (PHP) | Magnitude: 62.4 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 52, state_mutation: 24, doc: 24, structural_boundaries: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `app/code/Magento/Store/Model/StoreSwitcher/RedirectDataSerializerInterface.php` (PHP) | Magnitude: 40.8 | Delta: **0.128 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 8, structural_boundaries: 5, args: 2, func_start: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `app/code/Magento/Paypal/Controller/Express/AbstractExpress/Cancel.php` (PHP) | Magnitude: 26.02 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 30, branch: 9, state_mutation: 7, doc: 7
- `dev/tests/static/testsuite/Magento/Framework/Validator/RegexFactory.php` (PHP) | Magnitude: 5.78 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_8`
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
- `setup/src/Magento/Setup/Module/Dependency/Report/Dependency/Data/Dependency.php` (PHP) | Magnitude: 35.0 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 25, doc: 18, state_mutation: 14, structural_boundaries: 11
- `app/code/Magento/Sales/Api/Data/CreditmemoInterface.php` (PHP) | Magnitude: 386.62 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 258, indent_spaces: 152, structural_boundaries: 105, args: 102
- `app/code/Magento/Cms/Api/BlockRepositoryInterface.php` (PHP) | Magnitude: 59.19 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 23, structural_boundaries: 7, args: 5, func_start: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `app/code/Magento/Catalog/Model/Product/Image.php` (PHP) | Magnitude: 405.86 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 384, doc: 213, state_mutation: 145, structural_boundaries: 105
- `app/code/Magento/Catalog/Model/Product/Option/Value.php` (PHP) | Magnitude: 185.46 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 191, doc: 102, structural_boundaries: 71, api: 58
- `app/code/Magento/Customer/Controller/Adminhtml/Index/NewAction.php` (PHP) | Magnitude: 4.24 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 6, doc: 3, branch: 1
- `app/code/Magento/Customer/Model/ResourceModel/Group/Resolver.php` (PHP) | Magnitude: 33.42 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 24, state_mutation: 17, doc: 9, structural_boundaries: 7
- `app/code/Magento/Sales/Controller/Adminhtml/Order/Index.php` (PHP) | Magnitude: 4.24 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 6, doc: 3, branch: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `dev/tests/integration/testsuite/Magento/Tax/_files/tax_rule_region_1_al.php` (PHP) | Magnitude: 25.5 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 12, state_mutation: 10, doc: 5, dead_code: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `app/code/Magento/Ups/Model/Carrier.php` -> **Rajesh Kumar** (100.0% isolated ownership) | Magnitude: 2362.12
- `app/code/Magento/Sales/Model/Order.php` -> **Rajesh Kumar** (100.0% isolated ownership) | Magnitude: 2255.16
- `app/code/Magento/CatalogImportExport/Model/Import/Product/Option.php` -> **Rajesh Kumar** (100.0% isolated ownership) | Magnitude: 1615.34
- `app/code/Magento/Catalog/Model/ResourceModel/Product/Collection.php` -> **Rajesh Kumar** (100.0% isolated ownership) | Magnitude: 1377.68
- `app/code/Magento/Usps/Model/Carrier.php` -> **Bhavin Parmar** (100.0% isolated ownership) | Magnitude: 1269.72

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

- `app/code/Magento/Catalog/Api/Data/ProductInterface.php` -> **Severity: 493.015** (Blast Radius: 4.957 * Doc Risk: 99.4583%)
- `app/code/Magento/GraphQl/Model/Query/Logger/LoggerInterface.php` -> **Severity: 325.488** (Blast Radius: 3.255 * Doc Risk: 99.9963%)
- `app/code/Magento/Sales/Model/Order.php` -> **Severity: 158.0** (Blast Radius: 1.58 * Doc Risk: 100.0%)
- `app/code/Magento/Catalog/Model/Product/Attribute/Source/Status.php` -> **Severity: 148.925** (Blast Radius: 1.755 * Doc Risk: 84.8576%)
- `app/code/Magento/Authorization/Model/UserContextInterface.php` -> **Severity: 108.685** (Blast Radius: 1.585 * Doc Risk: 68.5708%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
