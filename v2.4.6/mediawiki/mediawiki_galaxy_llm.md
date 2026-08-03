# ARCHITECTURAL_BRIEF: mediawiki
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/mediawiki` |
| **Timestamp** | `2026-08-03T21:05:46.642426+00:00` |
| **Scan Duration** | `22.41s` |
| **Git Branch** | `master` |
| **Git Commit** | `8863834e673e4f297bfbc40cd4d54ee9027ad876` |
| **Git Remote** | `https://github.com/wikimedia/mediawiki.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 4471 malicious artifacts.

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
| Total Artifacts | 12231 |
| Analyzed Artifacts (Scanned) | 7829 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 4402 |
| Total LOC | 752227 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 64.0% |
| Dominant Lang | PHP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.16 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 10.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 288 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PHP | 3984 | 344483 | 50.9% |
| JSON | 2878 | 359746 | 36.8% |
| JAVASCRIPT | 439 | 30205 | 5.6% |
| CSS | 233 | 8468 | 3.0% |
| XML | 120 | 0 | 1.5% |
| PLAINTEXT | 52 | 4 | 0.7% |
| SQLITE | 42 | 5004 | 0.5% |
| HTML | 37 | 3848 | 0.5% |
| MARKDOWN | 36 | 0 | 0.5% |
| SHELL | 4 | 61 | 0.1% |
| YAML | 2 | 48 | 0.0% |
| MAKEFILE | 2 | 360 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.761`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 4786 | 61.1% |
| file_cluster_13 | 2460 | 31.4% |
| file_cluster_9 | 82 | 1.0% |
| file_cluster_6 | 78 | 1.0% |
| file_cluster_4 | 54 | 0.7% |
| file_cluster_15 | 36 | 0.5% |
| file_cluster_0 | 23 | 0.3% |
| file_cluster_7 | 23 | 0.3% |
| file_cluster_17 | 21 | 0.3% |
| file_cluster_11 | 8 | 0.1% |
| file_cluster_12 | 7 | 0.1% |
| file_cluster_2 | 7 | 0.1% |
| Unknown | 4 | 0.1% |
| file_cluster_1 | 4 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Minified & Vendor Opaque Mass | 152 | 1.9% |
| Static: Literature & Documentation | 84 | 1.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 4402*

**Composition by Extension & Reason:**
- `.php`: 1464x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Machine-Generated Source Code Signature: 45 LOC), 2x Excluded (Machine-Generated Source Code Signature: 42 LOC)
- `.svg`: 1122x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 302x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Static Asset Blob without Intent: 1121 LOC), 2x Excluded (Static Asset Blob without Intent: 1973 LOC)
- `.js`: 400x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 7x Excluded (Saturation: Line 1 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 437 LOC)
- `.css`: 147x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.sql`: 20x Excluded (Machine-Generated Source Code Signature: 7 LOC), 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 7x Excluded (Machine-Generated Source Code Signature: 9 LOC)
- `.png`: 80x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 57x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.undeterminable), 2x Excluded (Unsupported Extension: '.data-parsoid')
- `.cjs`: 54x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 48x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 45 LOC), 1x Excluded (Machine-Generated Source Code Signature: 56 LOC)
- `.jpg`: 32x Excluded (Explicitly Denied Extension: '.jpg')
- `.txt`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Binary Format Detected), 1x Excluded (Lexical Monotony: High structural repetition detected in 4348 LOC)
- `.mustache`: 21x Excluded (Unsupported Extension: '.mustache'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.less`: 19x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.manual`: 16x Excluded (Unsupported Extension: '.manual')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 13.7 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.6 | 14.4 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 31.6 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 10.8 | 2.3 | 2.3 |
| API Exposure | 0.0 | 14.5 | 2.0 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 2.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 41.2 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 91.7 | 0.3 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 83.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 3.8 | 0.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 6.3 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 28.6 | 17.9 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 0.9 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 99.9 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 0.6 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 1.8 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/uidesign/confirmable.html` (Hits: 73)
- `resources/src/mediawiki.special.block/components/BlockLog.vue` (Hits: 27)
- `tests/api-testing/REST/Transform.js` (Hits: 25)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **MediaWikiServices.php** (`includes/MediaWikiServices.php`) — 436 inbound connections
2. **Html.php** (`includes/Html/Html.php`) — 226 inbound connections
3. **UserIdentity.php** (`includes/User/UserIdentity.php`) — 225 inbound connections
4. **Status.php** (`includes/Status/Status.php`) — 204 inbound connections
5. **IConnectionProvider.php** (`includes/libs/Rdbms/LBFactory/IConnectionProvider.php`) — 160 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **MessagesSr_ec.php** (`languages/messages/MessagesSr_ec.php`) — 1213 outbound dependencies
2. **MessagesSr_el.php** (`languages/messages/MessagesSr_el.php`) — 1175 outbound dependencies
3. **MessagesFr.php** (`languages/messages/MessagesFr.php`) — 927 outbound dependencies
4. **MessagesUk.php** (`languages/messages/MessagesUk.php`) — 897 outbound dependencies
5. **MessagesArz.php** (`languages/messages/MessagesArz.php`) — 891 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `getPermissionStatus` (@ `includes/Permissions/PermissionManager.php`) -> Impact: **1835.0** | LOC: 1428
- `__construct` (@ `includes/EditPage/EditPage.php`) -> Impact: **1161.0** | LOC: 1688
- `loadSlotContent` (@ `includes/Revision/RevisionStore.php`) -> Impact: **1111.7** | LOC: 777
  * *Intent:* /** * @param IDatabase $dbw * @param RevisionRecord $rev * @param int $parentId * * @return array a revision table row * * @throws MWException * @thro...
- `getMulti` (@ `includes/libs/ObjectCache/WANObjectCache.php`) -> Impact: **884.6** | LOC: 1056
- `setPageTitle` (@ `includes/Output/OutputPage.php`) -> Impact: **782.7** | LOC: 1366
  * *Intent:* /**
- `getFieldForTag` (@ `resources/src/mediawiki.widgets.datetime/DiscordianDateTimeFormatter.js`) -> Impact: **747.8** | LOC: 511
- `convertDateFormatToJs` (@ `includes/Language/Language.php`) -> Impact: **724.3** | LOC: 1561
- `__construct` (@ `includes/Api/ApiMain.php`) -> Impact: **711.5** | LOC: 549
- `runFirstQuery` (@ `includes/Api/ApiQueryBacklinks.php`) -> Impact: **604.7** | LOC: 346
- `getUndeleteLink` (@ `includes/Skin/Skin.php`) -> Impact: **519.7** | LOC: 833

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `describe` (@ `tests/api-testing/action/Parse.js`) -> **O(2^N) [Recursive]**
- `describe` (@ `tests/api-testing/action/Links.js`) -> **O(2^N) [Recursive]**
- `Uri` (@ `resources/src/mediawiki.Uri/Uri.js`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * Function that's useful when constructing the URI string -- we frequently encounter the pattern * of having to add something to the URI as we go,...
- `login` (@ `resources/src/mediawiki.api/login.js`) -> **O(2^N) [Recursive]**
  * *Intent:* /**
- `xhr` (@ `resources/src/mediawiki.special.apisandbox/ApiSandbox.js`) -> **O(2^N) [Recursive]**
- `getFieldForTag` (@ `resources/src/mediawiki.widgets.datetime/DiscordianDateTimeFormatter.js`) -> **O(2^N) [Recursive]**
- `describe` (@ `tests/api-testing/REST/Transform.js`) -> **O(2^N) [Recursive]**
- `show` (@ `includes/Actions/McrUndoAction.php`) -> **O(2^N) [Recursive]**
- `__construct` (@ `includes/Api/ApiMain.php`) -> **O(2^N) [Recursive]**
- `execute` (@ `includes/Api/ApiPurge.php`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `__construct` (@ `includes/EditPage/EditPage.php`) -> DB Complexity: **333**
- `newFromLinkTarget` (@ `includes/Title/Title.php`) -> DB Complexity: **316**
  * *Intent:* /** * Text form including namespace/interwiki, initialised on demand
- `setPageTitle` (@ `includes/Output/OutputPage.php`) -> DB Complexity: **303**
  * *Intent:* /**
- `urlencode` (@ `includes/Parser/CoreParserFunctions.php`) -> DB Complexity: **283**
- `convertDateFormatToJs` (@ `includes/Language/Language.php`) -> DB Complexity: **218**
- `getContentModel` (@ `includes/Page/WikiPage.php`) -> DB Complexity: **209**
- `getMulti` (@ `includes/libs/ObjectCache/WANObjectCache.php`) -> DB Complexity: **209**
- `getPermissionStatus` (@ `includes/Permissions/PermissionManager.php`) -> DB Complexity: **165**
- `getUndeleteLink` (@ `includes/Skin/Skin.php`) -> DB Complexity: **152**
- `getOldIDFromRequest` (@ `includes/Page/Article.php`) -> DB Complexity: **139**
  * *Intent:* /** @var string|false URL to redirect to or false if none */

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `includes/Api` | 144 | 23792.74 | 38.38% | 65.05% |
| `tests/phpunit/integration/includes/Json` | 4 | 20000.0 | 0.0% | 0.0% |
| `maintenance` | 194 | 18176.9 | 37.3% | 43.26% |
| `includes/Specials` | 130 | 17240.28 | 24.38% | 65.28% |
| `languages/messages` | 517 | 12467.08 | 13.41% | 0.29% |
| `includes/Parser` | 44 | 10493.56 | 27.52% | 63.47% |
| `languages/i18n/datetime` | 578 | 9541.42 | 0.52% | 0.0% |
| `includes/Language` | 32 | 8211.51 | 27.13% | 65.33% |
| `includes/Page` | 49 | 7836.44 | 23.05% | 47.64% |
| `languages/i18n/preferences` | 366 | 6637.88 | 0.4% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `resources/src/mediawiki.DateFormatter/DateFormatter.js` -> **100.0%** Exposure
- `resources/src/mediawiki.Upload.js` -> **100.0%** Exposure
- `resources/src/mediawiki.checkboxtoggle.js` -> **100.0%** Exposure
- `resources/src/mediawiki.confirmCloseWindow.js` -> **100.0%** Exposure
- `resources/src/mediawiki.libs.jpegmeta/export.js` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `maintenance/mediawiki.Title/generateJsToUpperCaseList.js` -> **100.0%** Exposure
- `resources/src/mediawiki.ForeignApi/mediawiki.ForeignApi.core.js` -> **100.0%** Exposure
- `resources/src/mediawiki.ForeignApi/mediawiki.ForeignRest.core.js` -> **100.0%** Exposure
- `resources/src/mediawiki.ForeignStructuredUpload.BookletLayout/BookletLayout.js` -> **100.0%** Exposure
- `resources/src/mediawiki.ForeignStructuredUpload.BookletLayout/ForeignStructuredUpload.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/phpunit/data/db/sqlite/tables-1.45.sql` -> **0** Orphaned Functions | **193** Duplicates
- `tests/phpunit/data/db/sqlite/tables-1.40.sql` -> **0** Orphaned Functions | **191** Duplicates
- `tests/phpunit/data/db/sqlite/tables-1.44.sql` -> **0** Orphaned Functions | **191** Duplicates
- `tests/phpunit/data/db/sqlite/tables-1.39.sql` -> **0** Orphaned Functions | **190** Duplicates
- `tests/phpunit/data/db/sqlite/tables-1.42.sql` -> **0** Orphaned Functions | **188** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`resources/src/mediawiki.rcfilters/mw.rcfilters.js`** -> AI Confidence: **99.48%**
2. **`includes/Media/FormatMetadata.php`** -> AI Confidence: **99.48%**
3. **`includes/Parser/Preprocessor_Hash.php`** -> AI Confidence: **99.48%**
4. **`includes/libs/Diff/DiffEngine.php`** -> AI Confidence: **99.48%**
5. **`languages/messages/MessagesAb.php`** -> AI Confidence: **99.48%**
6. **`languages/messages/MessagesAce.php`** -> AI Confidence: **99.48%**
7. **`languages/messages/MessagesAln.php`** -> AI Confidence: **99.48%**
8. **`languages/messages/MessagesAs.php`** -> AI Confidence: **99.48%**
9. **`languages/messages/MessagesAv.php`** -> AI Confidence: **99.48%**
10. **`languages/messages/MessagesAvk.php`** -> AI Confidence: **99.48%**
11. **`languages/messages/MessagesAz.php`** -> AI Confidence: **99.48%**
12. **`languages/messages/MessagesAzb.php`** -> AI Confidence: **99.48%**
13. **`languages/messages/MessagesBa.php`** -> AI Confidence: **99.48%**
14. **`languages/messages/MessagesBcc.php`** -> AI Confidence: **99.48%**
15. **`languages/messages/MessagesBe.php`** -> AI Confidence: **99.48%**
16. **`languages/messages/MessagesBgn.php`** -> AI Confidence: **99.48%**
17. **`languages/messages/MessagesBho.php`** -> AI Confidence: **99.48%**
18. **`languages/messages/MessagesBjn.php`** -> AI Confidence: **99.48%**
19. **`languages/messages/MessagesBr.php`** -> AI Confidence: **99.48%**
20. **`languages/messages/MessagesBxr.php`** -> AI Confidence: **99.48%**
21. **`languages/messages/MessagesCa.php`** -> AI Confidence: **99.48%**
22. **`languages/messages/MessagesCdo_hant.php`** -> AI Confidence: **99.48%**
23. **`languages/messages/MessagesCeb.php`** -> AI Confidence: **99.48%**
24. **`languages/messages/MessagesCkb.php`** -> AI Confidence: **99.48%**
25. **`languages/messages/MessagesCu.php`** -> AI Confidence: **99.48%**
26. **`languages/messages/MessagesDa.php`** -> AI Confidence: **99.48%**
27. **`languages/messages/MessagesDsb.php`** -> AI Confidence: **99.48%**
28. **`languages/messages/MessagesDv.php`** -> AI Confidence: **99.48%**
29. **`languages/messages/MessagesEt.php`** -> AI Confidence: **99.48%**
30. **`languages/messages/MessagesEu.php`** -> AI Confidence: **99.48%**
31. **`languages/messages/MessagesFi.php`** -> AI Confidence: **99.48%**
32. **`languages/messages/MessagesFo.php`** -> AI Confidence: **99.48%**
33. **`languages/messages/MessagesFrp.php`** -> AI Confidence: **99.48%**
34. **`languages/messages/MessagesFur.php`** -> AI Confidence: **99.48%**
35. **`languages/messages/MessagesFy.php`** -> AI Confidence: **99.48%**
36. **`languages/messages/MessagesGag.php`** -> AI Confidence: **99.48%**
37. **`languages/messages/MessagesGan_hant.php`** -> AI Confidence: **99.48%**
38. **`languages/messages/MessagesGor.php`** -> AI Confidence: **99.48%**
39. **`languages/messages/MessagesGsw.php`** -> AI Confidence: **99.48%**
40. **`languages/messages/MessagesGu.php`** -> AI Confidence: **99.48%**
41. **`languages/messages/MessagesHsb.php`** -> AI Confidence: **99.48%**
42. **`languages/messages/MessagesHt.php`** -> AI Confidence: **99.48%**
43. **`languages/messages/MessagesIa.php`** -> AI Confidence: **99.48%**
44. **`languages/messages/MessagesId.php`** -> AI Confidence: **99.48%**
45. **`languages/messages/MessagesIe.php`** -> AI Confidence: **99.48%**
46. **`languages/messages/MessagesIg.php`** -> AI Confidence: **99.48%**
47. **`languages/messages/MessagesInh.php`** -> AI Confidence: **99.48%**
48. **`languages/messages/MessagesIo.php`** -> AI Confidence: **99.48%**
49. **`languages/messages/MessagesIt.php`** -> AI Confidence: **99.48%**
50. **`languages/messages/MessagesJv.php`** -> AI Confidence: **99.48%**
51. **`languages/messages/MessagesKaa.php`** -> AI Confidence: **99.48%**
52. **`languages/messages/MessagesKrc.php`** -> AI Confidence: **99.48%**
53. **`languages/messages/MessagesKsh.php`** -> AI Confidence: **99.48%**
54. **`languages/messages/MessagesKu_latn.php`** -> AI Confidence: **99.48%**
55. **`languages/messages/MessagesKw.php`** -> AI Confidence: **99.48%**
56. **`languages/messages/MessagesLa.php`** -> AI Confidence: **99.48%**
57. **`languages/messages/MessagesLad.php`** -> AI Confidence: **99.48%**
58. **`languages/messages/MessagesLi.php`** -> AI Confidence: **99.48%**
59. **`languages/messages/MessagesLij.php`** -> AI Confidence: **99.48%**
60. **`languages/messages/MessagesLmo.php`** -> AI Confidence: **99.48%**
61. **`languages/messages/MessagesLo.php`** -> AI Confidence: **99.48%**
62. **`languages/messages/MessagesLrc.php`** -> AI Confidence: **99.48%**
63. **`languages/messages/MessagesLt.php`** -> AI Confidence: **99.48%**
64. **`languages/messages/MessagesMdf.php`** -> AI Confidence: **99.48%**
65. **`languages/messages/MessagesMhr.php`** -> AI Confidence: **99.48%**
66. **`languages/messages/MessagesMin.php`** -> AI Confidence: **99.48%**
67. **`languages/messages/MessagesMnw.php`** -> AI Confidence: **99.48%**
68. **`languages/messages/MessagesMwl.php`** -> AI Confidence: **99.48%**
69. **`languages/messages/MessagesMy.php`** -> AI Confidence: **99.48%**
70. **`languages/messages/MessagesNah.php`** -> AI Confidence: **99.48%**
71. **`languages/messages/MessagesNb.php`** -> AI Confidence: **99.48%**
72. **`languages/messages/MessagesNn.php`** -> AI Confidence: **99.48%**
73. **`languages/messages/MessagesNso.php`** -> AI Confidence: **99.48%**
74. **`languages/messages/MessagesOs.php`** -> AI Confidence: **99.48%**
75. **`languages/messages/MessagesPa.php`** -> AI Confidence: **99.48%**
76. **`languages/messages/MessagesPdc.php`** -> AI Confidence: **99.48%**
77. **`languages/messages/MessagesRm.php`** -> AI Confidence: **99.48%**
78. **`languages/messages/MessagesRoa_tara.php`** -> AI Confidence: **99.48%**
79. **`languages/messages/MessagesRu.php`** -> AI Confidence: **99.48%**
80. **`languages/messages/MessagesRue.php`** -> AI Confidence: **99.48%**
81. **`languages/messages/MessagesSah.php`** -> AI Confidence: **99.48%**
82. **`languages/messages/MessagesScn.php`** -> AI Confidence: **99.48%**
83. **`languages/messages/MessagesSdc.php`** -> AI Confidence: **99.48%**
84. **`languages/messages/MessagesSe.php`** -> AI Confidence: **99.48%**
85. **`languages/messages/MessagesShn.php`** -> AI Confidence: **99.48%**
86. **`languages/messages/MessagesSk.php`** -> AI Confidence: **99.48%**
87. **`languages/messages/MessagesSl.php`** -> AI Confidence: **99.48%**
88. **`languages/messages/MessagesSu.php`** -> AI Confidence: **99.48%**
89. **`languages/messages/MessagesSw.php`** -> AI Confidence: **99.48%**
90. **`languages/messages/MessagesTa.php`** -> AI Confidence: **99.48%**
91. **`languages/messages/MessagesTe.php`** -> AI Confidence: **99.48%**
92. **`languages/messages/MessagesTet.php`** -> AI Confidence: **99.48%**
93. **`languages/messages/MessagesTg_cyrl.php`** -> AI Confidence: **99.48%**
94. **`languages/messages/MessagesTh.php`** -> AI Confidence: **99.48%**
95. **`languages/messages/MessagesTl.php`** -> AI Confidence: **99.48%**
96. **`languages/messages/MessagesTok.php`** -> AI Confidence: **99.48%**
97. **`languages/messages/MessagesTpi.php`** -> AI Confidence: **99.48%**
98. **`languages/messages/MessagesUk.php`** -> AI Confidence: **99.48%**
99. **`languages/messages/MessagesVec.php`** -> AI Confidence: **99.48%**
100. **`languages/messages/MessagesVep.php`** -> AI Confidence: **99.48%**
101. **`languages/messages/MessagesVmf.php`** -> AI Confidence: **99.48%**
102. **`languages/messages/MessagesVo.php`** -> AI Confidence: **99.48%**
103. **`languages/messages/MessagesWa.php`** -> AI Confidence: **99.48%**
104. **`languages/messages/MessagesWar.php`** -> AI Confidence: **99.48%**
105. **`languages/messages/MessagesWo.php`** -> AI Confidence: **99.48%**
106. **`languages/messages/MessagesYo.php`** -> AI Confidence: **99.48%**
107. **`languages/messages/MessagesYue.php`** -> AI Confidence: **99.48%**
108. **`languages/messages/MessagesZh_hk.php`** -> AI Confidence: **99.48%**
109. **`tests/Common/TestsAutoLoader.php`** -> AI Confidence: **99.48%**
110. **`resources/src/mediawiki.special.apisandbox/Util.js`** -> AI Confidence: **99.39%**
111. **`includes/Languages/Data/Names.php`** -> AI Confidence: **99.39%**
112. **`includes/libs/Mime/XmlTypeCheck.php`** -> AI Confidence: **99.39%**
113. **`languages/messages/MessagesAf.php`** -> AI Confidence: **99.39%**
114. **`languages/messages/MessagesBe_tarask.php`** -> AI Confidence: **99.39%**
115. **`languages/messages/MessagesBg.php`** -> AI Confidence: **99.39%**
116. **`languages/messages/MessagesCy.php`** -> AI Confidence: **99.39%**
117. **`languages/messages/MessagesEl.php`** -> AI Confidence: **99.39%**
118. **`languages/messages/MessagesEn.php`** -> AI Confidence: **99.39%**
119. **`languages/messages/MessagesHe.php`** -> AI Confidence: **99.39%**
120. **`languages/messages/MessagesHy.php`** -> AI Confidence: **99.39%**
121. **`languages/messages/MessagesIs.php`** -> AI Confidence: **99.39%**
122. **`languages/messages/MessagesKk_arab.php`** -> AI Confidence: **99.39%**
123. **`languages/messages/MessagesKk_cyrl.php`** -> AI Confidence: **99.39%**
124. **`languages/messages/MessagesKk_latn.php`** -> AI Confidence: **99.39%**
125. **`languages/messages/MessagesKo.php`** -> AI Confidence: **99.39%**
126. **`languages/messages/MessagesLzh.php`** -> AI Confidence: **99.39%**
127. **`languages/messages/MessagesSr_ec.php`** -> AI Confidence: **99.39%**
128. **`languages/messages/MessagesSr_el.php`** -> AI Confidence: **99.39%**
129. **`languages/messages/MessagesZh_hans.php`** -> AI Confidence: **99.39%**
130. **`languages/messages/MessagesEn_gb.php`** -> AI Confidence: **99.34%**
131. **`languages/messages/MessagesHyw.php`** -> AI Confidence: **99.34%**
132. **`languages/messages/MessagesNan_latn_pehoeji.php`** -> AI Confidence: **99.34%**
133. **`languages/messages/MessagesVro.php`** -> AI Confidence: **99.34%**
134. **`includes/Languages/LanguageKk_cyrl.php`** -> AI Confidence: **99.32%**
135. **`includes/Languages/LanguageOs.php`** -> AI Confidence: **99.32%**
136. **`includes/Languages/LanguageTyv.php`** -> AI Confidence: **99.32%**
137. **`includes/Parser/BlockLevelPass.php`** -> AI Confidence: **99.32%**
138. **`includes/Parser/DateFormatter.php`** -> AI Confidence: **99.32%**
139. **`languages/messages/MessagesGot.php`** -> AI Confidence: **99.32%**
140. **`languages/messages/MessagesLfn.php`** -> AI Confidence: **99.32%**
141. **`resources/src/mediawiki.page.ready/ready.js`** -> AI Confidence: **99.31%**
142. **`includes/Actions/ActionEntryPoint.php`** -> AI Confidence: **99.31%**
143. **`includes/Actions/RawAction.php`** -> AI Confidence: **99.31%**
144. **`includes/Api/ApiComparePages.php`** -> AI Confidence: **99.31%**
145. **`includes/Api/ApiEditPage.php`** -> AI Confidence: **99.31%**
146. **`includes/Api/ApiErrorFormatter.php`** -> AI Confidence: **99.31%**
147. **`includes/Api/ApiExpandTemplates.php`** -> AI Confidence: **99.31%**
148. **`includes/Api/ApiLogin.php`** -> AI Confidence: **99.31%**
149. **`includes/Api/ApiMergeHistory.php`** -> AI Confidence: **99.31%**
150. **`includes/Api/ApiPageSet.php`** -> AI Confidence: **99.31%**
151. **`includes/Api/ApiParamInfo.php`** -> AI Confidence: **99.31%**
152. **`includes/Api/ApiQueryAllDeletedRevisions.php`** -> AI Confidence: **99.31%**
153. **`includes/Api/ApiQueryAllImages.php`** -> AI Confidence: **99.31%**
154. **`includes/Api/ApiQueryAllLinks.php`** -> AI Confidence: **99.31%**
155. **`includes/Api/ApiQueryAllMessages.php`** -> AI Confidence: **99.31%**
156. **`includes/Api/ApiQueryAllPages.php`** -> AI Confidence: **99.31%**
157. **`includes/Api/ApiQueryAllUsers.php`** -> AI Confidence: **99.31%**
158. **`includes/Api/ApiQueryBacklinks.php`** -> AI Confidence: **99.31%**
159. **`includes/Api/ApiQueryBacklinksprop.php`** -> AI Confidence: **99.31%**
160. **`includes/Api/ApiQueryBlocks.php`** -> AI Confidence: **99.31%**
161. **`includes/Api/ApiQueryCategoryMembers.php`** -> AI Confidence: **99.31%**
162. **`includes/Api/ApiQueryDeletedRevisions.php`** -> AI Confidence: **99.31%**
163. **`includes/Api/ApiQueryDeletedrevs.php`** -> AI Confidence: **99.31%**
164. **`includes/Api/ApiQueryFilearchive.php`** -> AI Confidence: **99.31%**
165. **`includes/Api/ApiQueryIWLinks.php`** -> AI Confidence: **99.31%**
166. **`includes/Api/ApiQueryImageInfo.php`** -> AI Confidence: **99.31%**
167. **`includes/Api/ApiQueryInfo.php`** -> AI Confidence: **99.31%**
168. **`includes/Api/ApiQueryLangLinks.php`** -> AI Confidence: **99.31%**
169. **`includes/Api/ApiQueryLanguageinfo.php`** -> AI Confidence: **99.31%**
170. **`includes/Api/ApiQueryLinks.php`** -> AI Confidence: **99.31%**
171. **`includes/Api/ApiQueryLogEvents.php`** -> AI Confidence: **99.31%**
172. **`includes/Api/ApiQueryRandom.php`** -> AI Confidence: **99.31%**
173. **`includes/Api/ApiQueryRecentChanges.php`** -> AI Confidence: **99.31%**
174. **`includes/Api/ApiQueryRevisions.php`** -> AI Confidence: **99.31%**
175. **`includes/Api/ApiQueryRevisionsBase.php`** -> AI Confidence: **99.31%**
176. **`includes/Api/ApiQuerySearch.php`** -> AI Confidence: **99.31%**
177. **`includes/Api/ApiQueryUserContribs.php`** -> AI Confidence: **99.31%**
178. **`includes/Api/ApiQueryUserInfo.php`** -> AI Confidence: **99.31%**
179. **`includes/Api/ApiQueryUsers.php`** -> AI Confidence: **99.31%**
180. **`includes/Api/ApiRevisionDelete.php`** -> AI Confidence: **99.31%**
181. **`includes/Api/ApiTag.php`** -> AI Confidence: **99.31%**
182. **`includes/Auth/AuthManager.php`** -> AI Confidence: **99.31%**
183. **`includes/Auth/AuthenticationRequest.php`** -> AI Confidence: **99.31%**
184. **`includes/Auth/Hook/AuthenticationAttemptThrottledHook.php`** -> AI Confidence: **99.31%**
185. **`includes/Auth/Throttler.php`** -> AI Confidence: **99.31%**
186. **`includes/Block/BlockUser.php`** -> AI Confidence: **99.31%**
187. **`includes/Cache/HTMLCacheUpdater.php`** -> AI Confidence: **99.31%**
188. **`includes/Category/CategoryViewer.php`** -> AI Confidence: **99.31%**
189. **`includes/Category/TrackingCategories.php`** -> AI Confidence: **99.31%**
190. **`includes/ChangeTags/ChangeTagsStore.php`** -> AI Confidence: **99.31%**
191. **`includes/CommentStore/CommentStore.php`** -> AI Confidence: **99.31%**
192. **`includes/Config/EtcdConfig.php`** -> AI Confidence: **99.31%**
193. **`includes/Content/Renderer/ContentRenderer.php`** -> AI Confidence: **99.31%**
194. **`includes/EditPage/EditPage.php`** -> AI Confidence: **99.31%**
195. **`includes/EditPage/IntroMessageBuilder.php`** -> AI Confidence: **99.31%**
196. **`includes/Exception/MWExceptionHandler.php`** -> AI Confidence: **99.31%**
197. **`includes/Export/WikiExporter.php`** -> AI Confidence: **99.31%**
198. **`includes/Export/XmlDumpWriter.php`** -> AI Confidence: **99.31%**
199. **`includes/FileRepo/AuthenticatedFileEntryPoint.php`** -> AI Confidence: **99.31%**
200. **`includes/FileRepo/File/LocalFile.php`** -> AI Confidence: **99.31%**
201. **`includes/FileRepo/File/LocalFileDeleteBatch.php`** -> AI Confidence: **99.31%**
202. **`includes/FileRepo/File/LocalFileRestoreBatch.php`** -> AI Confidence: **99.31%**
203. **`includes/FileRepo/File/MediaFileTrait.php`** -> AI Confidence: **99.31%**
204. **`includes/FileRepo/ThumbnailEntryPoint.php`** -> AI Confidence: **99.31%**
205. **`includes/GlobalFunctions.php`** -> AI Confidence: **99.31%**
206. **`includes/HTMLForm/Field/HTMLAutoCompleteSelectField.php`** -> AI Confidence: **99.31%**
207. **`includes/HTMLForm/Field/HTMLDateTimeField.php`** -> AI Confidence: **99.31%**
208. **`includes/HTMLForm/Field/HTMLFormFieldCloner.php`** -> AI Confidence: **99.31%**
209. **`includes/HTMLForm/Field/HTMLMultiSelectField.php`** -> AI Confidence: **99.31%**
210. **`includes/HTMLForm/Field/HTMLSelectAndOtherField.php`** -> AI Confidence: **99.31%**
211. **`includes/HTMLForm/Field/HTMLSelectLanguageField.php`** -> AI Confidence: **99.31%**
212. **`includes/HookContainer/DeprecatedHooks.php`** -> AI Confidence: **99.31%**
213. **`includes/Html/Html.php`** -> AI Confidence: **99.31%**
214. **`includes/Http/GuzzleHttpRequest.php`** -> AI Confidence: **99.31%**
215. **`includes/Http/HttpRequestFactory.php`** -> AI Confidence: **99.31%**
216. **`includes/Import/WikiImporter.php`** -> AI Confidence: **99.31%**
217. **`includes/Installer/CliInstaller.php`** -> AI Confidence: **99.31%**
218. **`includes/Installer/LocalSettingsGenerator.php`** -> AI Confidence: **99.31%**
219. **`includes/Installer/PostgresUpdater.php`** -> AI Confidence: **99.31%**
220. **`includes/Installer/WebInstallerName.php`** -> AI Confidence: **99.31%**
221. **`includes/Installer/WebInstallerOptions.php`** -> AI Confidence: **99.31%**
222. **`includes/Interwiki/ClassicInterwikiLookup.php`** -> AI Confidence: **99.31%**
223. **`includes/JobQueue/JobQueueGroup.php`** -> AI Confidence: **99.31%**
224. **`includes/JobQueue/JobRunner.php`** -> AI Confidence: **99.31%**
225. **`includes/Language/ConverterRule.php`** -> AI Confidence: **99.31%**
226. **`includes/Language/LCStoreStaticArray.php`** -> AI Confidence: **99.31%**
227. **`includes/Language/Language.php`** -> AI Confidence: **99.31%**
228. **`includes/Language/LanguageCode.php`** -> AI Confidence: **99.31%**
229. **`includes/Language/LanguageConverter.php`** -> AI Confidence: **99.31%**
230. **`includes/Language/LocalisationCache.php`** -> AI Confidence: **99.31%**
231. **`includes/Linker/Linker.php`** -> AI Confidence: **99.31%**
232. **`includes/Logging/BlockLogFormatter.php`** -> AI Confidence: **99.31%**
233. **`includes/Logging/LogEventsList.php`** -> AI Confidence: **99.31%**
234. **`includes/Logging/LogFormatter.php`** -> AI Confidence: **99.31%**
235. **`includes/Logging/Pager/LogPager.php`** -> AI Confidence: **99.31%**
236. **`includes/MainConfigSchema.php`** -> AI Confidence: **99.31%**
237. **`includes/Media/BitmapHandler.php`** -> AI Confidence: **99.31%**
238. **`includes/OutputTransform/Stages/HandleTOCMarkersDOM.php`** -> AI Confidence: **99.31%**
239. **`includes/Page/Article.php`** -> AI Confidence: **99.31%**
240. **`includes/Page/Event/PageRecordChangedEvent.php`** -> AI Confidence: **99.31%**
241. **`includes/Page/File/BadFileLookup.php`** -> AI Confidence: **99.31%**
242. **`includes/Page/File/FileDeleteForm.php`** -> AI Confidence: **99.31%**
243. **`includes/Page/ImageHistoryList.php`** -> AI Confidence: **99.31%**
244. **`includes/Page/ImageHistoryPseudoPager.php`** -> AI Confidence: **99.31%**
245. **`includes/Page/ImagePage.php`** -> AI Confidence: **99.31%**
246. **`includes/Page/ParserOutputAccess.php`** -> AI Confidence: **99.31%**
247. **`includes/Page/ProtectionForm.php`** -> AI Confidence: **99.31%**
248. **`includes/Pager/IndexPager.php`** -> AI Confidence: **99.31%**
249. **`includes/ParamValidator/TypeDef/UserDef.php`** -> AI Confidence: **99.31%**
250. **`includes/Parser/CoreParserFunctions.php`** -> AI Confidence: **99.31%**
251. **`includes/Parser/Parsoid/Config/DataAccess.php`** -> AI Confidence: **99.31%**
252. **`includes/Parser/Sanitizer.php`** -> AI Confidence: **99.31%**
253. **`includes/Password/UserPasswordPolicy.php`** -> AI Confidence: **99.31%**
254. **`includes/Permissions/PermissionManager.php`** -> AI Confidence: **99.31%**
255. **`includes/Permissions/RateLimiter.php`** -> AI Confidence: **99.31%**
256. **`includes/Preferences/DefaultPreferencesFactory.php`** -> AI Confidence: **99.31%**
257. **`includes/Profiler/ProfilerXhprof.php`** -> AI Confidence: **99.31%**
258. **`includes/RecentChanges/ChangesListBooleanFilter.php`** -> AI Confidence: **99.31%**
259. **`includes/RecentChanges/ChangesListQuery/WatchedCondition.php`** -> AI Confidence: **99.31%**
260. **`includes/RecentChanges/EnhancedChangesList.php`** -> AI Confidence: **99.31%**
261. **`includes/RecentChanges/RecentChangeMailComposer.php`** -> AI Confidence: **99.31%**
262. **`includes/RecentChanges/RecentChangeNotifier.php`** -> AI Confidence: **99.31%**
263. **`includes/Registration/ExtensionProcessor.php`** -> AI Confidence: **99.31%**
264. **`includes/RenameUser/Job/RenameUserTableJob.php`** -> AI Confidence: **99.31%**
265. **`includes/Request/ContentSecurityPolicy.php`** -> AI Confidence: **99.31%**
266. **`includes/Request/PathRouter.php`** -> AI Confidence: **99.31%**
267. **`includes/Request/WebRequest.php`** -> AI Confidence: **99.31%**
268. **`includes/ResourceLoader/FileModule.php`** -> AI Confidence: **99.31%**
269. **`includes/ResourceLoader/ForeignResourceManager.php`** -> AI Confidence: **99.31%**
270. **`includes/ResourceLoader/StartUpModule.php`** -> AI Confidence: **99.31%**
271. **`includes/Rest/ConditionalHeaderUtil.php`** -> AI Confidence: **99.31%**
272. **`includes/Revision/MainSlotRoleHandler.php`** -> AI Confidence: **99.31%**
273. **`includes/Search/PrefixSearch.php`** -> AI Confidence: **99.31%**
274. **`includes/Search/TitleMatcher.php`** -> AI Confidence: **99.31%**
275. **`includes/Session/SessionManager.php`** -> AI Confidence: **99.31%**
276. **`includes/SetupDynamicConfig.php`** -> AI Confidence: **99.31%**
277. **`includes/Skin/Components/SkinComponentLink.php`** -> AI Confidence: **99.31%**
278. **`includes/Skin/Skin.php`** -> AI Confidence: **99.31%**
279. **`includes/Skin/SkinTemplate.php`** -> AI Confidence: **99.31%**
280. **`includes/SpecialPage/ContributionsSpecialPage.php`** -> AI Confidence: **99.31%**
281. **`includes/SpecialPage/LoginSignupSpecialPage.php`** -> AI Confidence: **99.31%**
282. **`includes/Specials/Forms/UploadForm.php`** -> AI Confidence: **99.31%**
283. **`includes/Specials/Pager/BlockListPager.php`** -> AI Confidence: **99.31%**
284. **`includes/Specials/Pager/ProtectedPagesPager.php`** -> AI Confidence: **99.31%**
285. **`includes/Specials/Pager/UsersPager.php`** -> AI Confidence: **99.31%**
286. **`includes/Specials/SpecialAllPages.php`** -> AI Confidence: **99.31%**
287. **`includes/Specials/SpecialBlock.php`** -> AI Confidence: **99.31%**
288. **`includes/Specials/SpecialEditWatchlist.php`** -> AI Confidence: **99.31%**
289. **`includes/Specials/SpecialExport.php`** -> AI Confidence: **99.31%**
290. **`includes/Specials/SpecialImport.php`** -> AI Confidence: **99.31%**
291. **`includes/Specials/SpecialInterwiki.php`** -> AI Confidence: **99.31%**
292. **`includes/Specials/SpecialListGroupRights.php`** -> AI Confidence: **99.31%**
293. **`includes/Specials/SpecialMovePage.php`** -> AI Confidence: **99.31%**
294. **`includes/Specials/SpecialRecentChanges.php`** -> AI Confidence: **99.31%**
295. **`includes/Specials/SpecialRevisionDelete.php`** -> AI Confidence: **99.31%**
296. **`includes/Specials/SpecialTags.php`** -> AI Confidence: **99.31%**
297. **`includes/Specials/SpecialUnblock.php`** -> AI Confidence: **99.31%**
298. **`includes/Specials/SpecialUndelete.php`** -> AI Confidence: **99.31%**
299. **`includes/Specials/SpecialUpload.php`** -> AI Confidence: **99.31%**
300. **`includes/Specials/SpecialVersion.php`** -> AI Confidence: **99.31%**
301. **`includes/Tidy/RemexCompatFormatter.php`** -> AI Confidence: **99.31%**
302. **`includes/Title/TitleParser.php`** -> AI Confidence: **99.31%**
303. **`includes/Upload/UploadVerification.php`** -> AI Confidence: **99.31%**
304. **`includes/User/Options/UserOptionsManager.php`** -> AI Confidence: **99.31%**
305. **`includes/User/UserGroupAssignmentService.php`** -> AI Confidence: **99.31%**
306. **`includes/User/UserTimeCorrection.php`** -> AI Confidence: **99.31%**
307. **`includes/Utils/GitInfo.php`** -> AI Confidence: **99.31%**
308. **`includes/Utils/UrlUtils.php`** -> AI Confidence: **99.31%**
309. **`includes/Watchlist/WatchedItemQueryService.php`** -> AI Confidence: **99.31%**
310. **`includes/WebStart.php`** -> AI Confidence: **99.31%**
311. **`includes/libs/FileBackend/FSFileBackend.php`** -> AI Confidence: **99.31%**
312. **`includes/libs/FileBackend/FileBackendStore.php`** -> AI Confidence: **99.31%**
313. **`includes/libs/FileBackend/SwiftFileBackend.php`** -> AI Confidence: **99.31%**
314. **`includes/libs/Http/MultiHttpClient.php`** -> AI Confidence: **99.31%**
315. **`includes/libs/Leximorph/Provider/TextDirection.php`** -> AI Confidence: **99.31%**
316. **`includes/libs/ObjectCache/RESTBagOStuff.php`** -> AI Confidence: **99.31%**
317. **`includes/libs/ObjectCache/RedisBagOStuff.php`** -> AI Confidence: **99.31%**
318. **`includes/libs/ObjectCache/WANObjectCache.php`** -> AI Confidence: **99.31%**
319. **`includes/libs/Rdbms/ChronologyProtector.php`** -> AI Confidence: **99.31%**
320. **`includes/libs/Rdbms/LBFactory/LBFactoryMulti.php`** -> AI Confidence: **99.31%**
321. **`includes/libs/Rdbms/LoadBalancer/LoadBalancer.php`** -> AI Confidence: **99.31%**
322. **`includes/libs/Rdbms/LoadMonitor/LoadMonitor.php`** -> AI Confidence: **99.31%**
323. **`includes/libs/Rdbms/Platform/SQLPlatform.php`** -> AI Confidence: **99.31%**
324. **`includes/libs/Rdbms/TransactionProfiler.php`** -> AI Confidence: **99.31%**
325. **`includes/libs/StringUtils/StringUtils.php`** -> AI Confidence: **99.31%**
326. **`includes/libs/XhprofData.php`** -> AI Confidence: **99.31%**
327. **`languages/messages/MessagesAn.php`** -> AI Confidence: **99.31%**
328. **`languages/messages/MessagesArc.php`** -> AI Confidence: **99.31%**
329. **`languages/messages/MessagesAst.php`** -> AI Confidence: **99.31%**
330. **`languages/messages/MessagesBcl.php`** -> AI Confidence: **99.31%**
331. **`languages/messages/MessagesBlk.php`** -> AI Confidence: **99.31%**
332. **`languages/messages/MessagesBs.php`** -> AI Confidence: **99.31%**
333. **`languages/messages/MessagesCe.php`** -> AI Confidence: **99.31%**
334. **`languages/messages/MessagesCs.php`** -> AI Confidence: **99.31%**
335. **`languages/messages/MessagesDe.php`** -> AI Confidence: **99.31%**
336. **`languages/messages/MessagesEo.php`** -> AI Confidence: **99.31%**
337. **`languages/messages/MessagesEs.php`** -> AI Confidence: **99.31%**
338. **`languages/messages/MessagesFa.php`** -> AI Confidence: **99.31%**
339. **`languages/messages/MessagesFr.php`** -> AI Confidence: **99.31%**
340. **`languages/messages/MessagesGa.php`** -> AI Confidence: **99.31%**
341. **`languages/messages/MessagesHaw.php`** -> AI Confidence: **99.31%**
342. **`languages/messages/MessagesHr.php`** -> AI Confidence: **99.31%**
343. **`languages/messages/MessagesHu.php`** -> AI Confidence: **99.31%**
344. **`languages/messages/MessagesJa.php`** -> AI Confidence: **99.31%**
345. **`languages/messages/MessagesKa.php`** -> AI Confidence: **99.31%**
346. **`languages/messages/MessagesKm.php`** -> AI Confidence: **99.31%**
347. **`languages/messages/MessagesLb.php`** -> AI Confidence: **99.31%**
348. **`languages/messages/MessagesMg.php`** -> AI Confidence: **99.31%**
349. **`languages/messages/MessagesMk.php`** -> AI Confidence: **99.31%**
350. **`languages/messages/MessagesMr.php`** -> AI Confidence: **99.31%**
351. **`languages/messages/MessagesMs.php`** -> AI Confidence: **99.31%**
352. **`languages/messages/MessagesMt.php`** -> AI Confidence: **99.31%**
353. **`languages/messages/MessagesMyv.php`** -> AI Confidence: **99.31%**
354. **`languages/messages/MessagesMzn.php`** -> AI Confidence: **99.31%**
355. **`languages/messages/MessagesNds.php`** -> AI Confidence: **99.31%**
356. **`languages/messages/MessagesNds_nl.php`** -> AI Confidence: **99.31%**
357. **`languages/messages/MessagesNl.php`** -> AI Confidence: **99.31%**
358. **`languages/messages/MessagesOc.php`** -> AI Confidence: **99.31%**
359. **`languages/messages/MessagesOr.php`** -> AI Confidence: **99.31%**
360. **`languages/messages/MessagesPl.php`** -> AI Confidence: **99.31%**
361. **`languages/messages/MessagesPs.php`** -> AI Confidence: **99.31%**
362. **`languages/messages/MessagesPt.php`** -> AI Confidence: **99.31%**
363. **`languages/messages/MessagesPt_br.php`** -> AI Confidence: **99.31%**
364. **`languages/messages/MessagesQu.php`** -> AI Confidence: **99.31%**
365. **`languages/messages/MessagesRo.php`** -> AI Confidence: **99.31%**
366. **`languages/messages/MessagesSa.php`** -> AI Confidence: **99.31%**
367. **`languages/messages/MessagesSd.php`** -> AI Confidence: **99.31%**
368. **`languages/messages/MessagesSh_latn.php`** -> AI Confidence: **99.31%**
369. **`languages/messages/MessagesSi.php`** -> AI Confidence: **99.31%**
370. **`languages/messages/MessagesSq.php`** -> AI Confidence: **99.31%**
371. **`languages/messages/MessagesSrn.php`** -> AI Confidence: **99.31%**
372. **`languages/messages/MessagesSv.php`** -> AI Confidence: **99.31%**
373. **`languages/messages/MessagesTly.php`** -> AI Confidence: **99.31%**
374. **`languages/messages/MessagesTt_cyrl.php`** -> AI Confidence: **99.31%**
375. **`languages/messages/MessagesTt_latn.php`** -> AI Confidence: **99.31%**
376. **`languages/messages/MessagesUr.php`** -> AI Confidence: **99.31%**
377. **`languages/messages/MessagesUz.php`** -> AI Confidence: **99.31%**
378. **`languages/messages/MessagesVi.php`** -> AI Confidence: **99.31%**
379. **`languages/messages/MessagesYi.php`** -> AI Confidence: **99.31%**
380. **`languages/messages/MessagesZh.php`** -> AI Confidence: **99.31%**
381. **`languages/messages/MessagesZh_hant.php`** -> AI Confidence: **99.31%**
382. **`maintenance/Maintenance.php`** -> AI Confidence: **99.31%**
383. **`maintenance/cleanupImages.php`** -> AI Confidence: **99.31%**
384. **`maintenance/cleanupInvalidDbKeys.php`** -> AI Confidence: **99.31%**
385. **`maintenance/cleanupUploadStash.php`** -> AI Confidence: **99.31%**
386. **`maintenance/createAndPromote.php`** -> AI Confidence: **99.31%**
387. **`maintenance/deleteEqualMessages.php`** -> AI Confidence: **99.31%**
388. **`maintenance/dumpBackup.php`** -> AI Confidence: **99.31%**
389. **`maintenance/dumpUploads.php`** -> AI Confidence: **99.31%**
390. **`maintenance/eval.php`** -> AI Confidence: **99.31%**
391. **`maintenance/findBadBlobs.php`** -> AI Confidence: **99.31%**
392. **`maintenance/findMissingActors.php`** -> AI Confidence: **99.31%**
393. **`maintenance/findMissingFiles.php`** -> AI Confidence: **99.31%**
394. **`maintenance/generateConfigSchema.php`** -> AI Confidence: **99.31%**
395. **`maintenance/generateJsonI18n.php`** -> AI Confidence: **99.31%**
396. **`maintenance/generateJwt.php`** -> AI Confidence: **99.31%**
397. **`maintenance/getConfiguration.php`** -> AI Confidence: **99.31%**
398. **`maintenance/grep.php`** -> AI Confidence: **99.31%**
399. **`maintenance/importTextFiles.php`** -> AI Confidence: **99.31%**
400. **`maintenance/includes/MaintenanceParameters.php`** -> AI Confidence: **99.31%**
401. **`maintenance/includes/TextPassDumper.php`** -> AI Confidence: **99.31%**
402. **`maintenance/install.php`** -> AI Confidence: **99.31%**
403. **`maintenance/language/generateNormalizerDataAr.php`** -> AI Confidence: **99.31%**
404. **`maintenance/mwdoc-filter.php`** -> AI Confidence: **99.31%**
405. **`maintenance/mysql.php`** -> AI Confidence: **99.31%**
406. **`maintenance/purgeParserCache.php`** -> AI Confidence: **99.31%**
407. **`maintenance/rebuildLocalisationCache.php`** -> AI Confidence: **99.31%**
408. **`maintenance/rebuildrecentchanges.php`** -> AI Confidence: **99.31%**
409. **`maintenance/recountCategories.php`** -> AI Confidence: **99.31%**
410. **`maintenance/refreshImageMetadata.php`** -> AI Confidence: **99.31%**
411. **`maintenance/removeUnusedAccounts.php`** -> AI Confidence: **99.31%**
412. **`maintenance/renameUsersMatchingPattern.php`** -> AI Confidence: **99.31%**
413. **`maintenance/resetAuthenticationThrottle.php`** -> AI Confidence: **99.31%**
414. **`maintenance/storage/compressOld.php`** -> AI Confidence: **99.31%**
415. **`maintenance/storage/moveToExternal.php`** -> AI Confidence: **99.31%**
416. **`maintenance/storage/recompressTracked.php`** -> AI Confidence: **99.31%**
417. **`maintenance/storage/trackBlobs.php`** -> AI Confidence: **99.31%**
418. **`maintenance/update.php`** -> AI Confidence: **99.31%**
419. **`maintenance/updateCollation.php`** -> AI Confidence: **99.31%**
420. **`maintenance/updateExtensionJsonSchema.php`** -> AI Confidence: **99.31%**
421. **`maintenance/userOptions.php`** -> AI Confidence: **99.31%**
422. **`maintenance/wrapOldPasswords.php`** -> AI Confidence: **99.31%**
423. **`tests/parser/parserTests.php`** -> AI Confidence: **99.31%**
424. **`tests/phpunit/bootstrap.php`** -> AI Confidence: **99.31%**
425. **`tests/phpunit/suites/ParserTestTopLevelSuite.php`** -> AI Confidence: **99.31%**
426. **`Gruntfile.js`** -> AI Confidence: **99.29%**
427. **`resources/lib/jquery.i18n/src/languages/bs.js`** -> AI Confidence: **99.29%**
428. **`resources/lib/jquery.i18n/src/languages/dsb.js`** -> AI Confidence: **99.29%**
429. **`resources/lib/jquery.i18n/src/languages/fi.js`** -> AI Confidence: **99.29%**
430. **`resources/lib/jquery.i18n/src/languages/ga.js`** -> AI Confidence: **99.29%**
431. **`resources/lib/jquery.i18n/src/languages/he.js`** -> AI Confidence: **99.29%**
432. **`resources/lib/jquery.i18n/src/languages/hsb.js`** -> AI Confidence: **99.29%**
433. **`resources/lib/jquery.i18n/src/languages/hu.js`** -> AI Confidence: **99.29%**
434. **`resources/lib/jquery.i18n/src/languages/hy.js`** -> AI Confidence: **99.29%**
435. **`resources/lib/jquery.i18n/src/languages/la.js`** -> AI Confidence: **99.29%**
436. **`resources/lib/jquery.i18n/src/languages/ml.js`** -> AI Confidence: **99.29%**
437. **`resources/lib/jquery.i18n/src/languages/os.js`** -> AI Confidence: **99.29%**
438. **`resources/lib/jquery.i18n/src/languages/ru.js`** -> AI Confidence: **99.29%**
439. **`resources/lib/jquery.i18n/src/languages/sl.js`** -> AI Confidence: **99.29%**
440. **`resources/lib/jquery.i18n/src/languages/uk.js`** -> AI Confidence: **99.29%**
441. **`resources/src/mediawiki.authenticationPopup/success.js`** -> AI Confidence: **99.29%**
442. **`resources/src/mediawiki.diff/undoButtonToggle.js`** -> AI Confidence: **99.29%**
443. **`resources/src/mediawiki.feedback/feedback.js`** -> AI Confidence: **99.29%**
444. **`resources/src/mediawiki.filewarning/filewarning.js`** -> AI Confidence: **99.29%**
445. **`resources/src/mediawiki.language/languages/bs.js`** -> AI Confidence: **99.29%**
446. **`resources/src/mediawiki.language/languages/dsb.js`** -> AI Confidence: **99.29%**
447. **`resources/src/mediawiki.language/languages/fi.js`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `includes/libs/Mime/MimeAnalyzer.php` -> **99.943%** Exposure
- `includes/Parser/Parser.php` -> **0.0062%** Exposure
- `tests/api-testing/REST/content/v1/Page.js` -> **0.0006%** Exposure
### Exploit Generation Surface
- `resources/src/mediawiki.api/index.js` -> **100.0%** Exposure
- `resources/src/startup/mediawiki.loader.js` -> **100.0%** Exposure
- `tests/api-testing/REST/Transform.js` -> **100.0%** Exposure
- `includes/Actions/ActionEntryPoint.php` -> **100.0%** Exposure
- `includes/Api/ApiMain.php` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `includes/Api/ApiClearHasMsg.php` -> **100.0%** Exposure
- `includes/Api/ApiComparePages.php` -> **100.0%** Exposure
- `includes/Api/ApiFormatBase.php` -> **100.0%** Exposure
- `includes/Api/ApiFormatJson.php` -> **100.0%** Exposure
- `includes/Api/ApiFormatRaw.php` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `resources/src/mediawiki.rcfilters/dm/FiltersViewModel.js` -> **100.0%** Exposure
- `resources/src/mediawiki.rcfilters/ui/FilterMenuHeaderWidget.js` -> **100.0%** Exposure
- `resources/src/mediawiki.rcfilters/ui/SavedLinksListItemWidget.js` -> **100.0%** Exposure
- `tests/api-testing/REST/Transform.js` -> **100.0%** Exposure
- `includes/Actions/ActionEntryPoint.php` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `24` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `82895` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `includes/GlobalFunctions.php` (PHP) -> Cumulative Risk: **773.56**
- **Archetype:** `file_cluster_13` (Distance: 15.045 IQR)
- **Magnitude:** 1122.82 | **LOC:** 1966 | **CtrlFlow:** 55.4% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `wfStripIllegalFilenameChars` (Impact: 100.3), `wfArrayToCgi` (Impact: 57.8), `wfMerge` (Impact: 57.7)

### 2. `maintenance/storage/checkStorage.php` (PHP) -> Cumulative Risk: **763.56**
- **Archetype:** `file_cluster_8` (Distance: 12.746 IQR)
- **Magnitude:** 545.22 | **LOC:** 597 | **CtrlFlow:** 67.2% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `check` (Impact: 169.7), `checkExternalConcatBlobs` (Impact: 21.6), `addError` (Impact: 17.1)

### 3. `includes/Api/ApiFormatBase.php` (PHP) -> Cumulative Risk: **695.54**
- **Archetype:** `file_cluster_13` (Distance: 11.947 IQR)
- **Magnitude:** 316.28 | **LOC:** 402 | **CtrlFlow:** 46.0% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Injection Surface (100.0%), State Flux (99.9985%)
- **Heaviest Functions:** `closePrinter` (Impact: 67.1), `initPrinter` (Impact: 39.7), `getParameterFromSettings` (Impact: 16.6)

### 4. `includes/Title/TitleParser.php` (PHP) -> Cumulative Risk: **688.91**
- **Archetype:** `file_cluster_13` (Distance: 12.751 IQR)
- **Magnitude:** 382.66 | **LOC:** 430 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Spec Match (85.7143%)
- **Heaviest Functions:** `splitTitleString` (Impact: 176.7), `makeTitleValueSafe` (Impact: 16.8), `overrideCreateMalformedTitleExceptionCal` (Impact: 5.3)

### 5. `includes/libs/Rdbms/Database/Database.php` (PHP) -> Cumulative Risk: **687.09**
- **Archetype:** `file_cluster_13` (Distance: 14.352 IQR)
- **Magnitude:** 1578.34 | **LOC:** 3606 | **CtrlFlow:** 36.1% | **Authorship Centralization:** 20.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%), State Flux (85.0%)
- **Heaviest Functions:** `cancelAtomic` (Impact: 210.9), `__construct` (Impact: 61.8), `insertSelect` (Impact: 45.9)

### 6. `maintenance/includes/Maintenance.php` (PHP) -> Cumulative Risk: **677.44**
- **Archetype:** `file_cluster_13` (Distance: 14.035 IQR)
- **Magnitude:** 737.18 | **LOC:** 1682 | **CtrlFlow:** 43.0% | **Authorship Centralization:** 25.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `setBatchSize` (Impact: 302.3), `getOption` (Impact: 10.5), `getArg` (Impact: 10.5)

### 7. `includes/libs/Http/MultiHttpClient.php` (PHP) -> Cumulative Risk: **672.59**
- **Archetype:** `file_cluster_13` (Distance: 13.715 IQR)
- **Magnitude:** 333.32 | **LOC:** 874 | **CtrlFlow:** 65.3% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `isCurlEnabled` (Impact: 114.1), `runMulti` (Impact: 43.8), `__construct` (Impact: 15.6)

### 8. `includes/Output/OutputPage.php` (PHP) -> Cumulative Risk: **669.81**
- **Archetype:** `file_cluster_13` (Distance: 13.453 IQR)
- **Magnitude:** 1659.96 | **LOC:** 5226 | **CtrlFlow:** 44.0% | **Authorship Centralization:** 7.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.9762%), Safety Score (80.0%)
- **Heaviest Functions:** `setPageTitle` (Impact: 782.7), `setIndexPolicy` (Impact: 14.0), `getRobotsContent` (Impact: 7.6)

### 9. `includes/Actions/ActionEntryPoint.php` (PHP) -> Cumulative Risk: **660.89**
- **Archetype:** `file_cluster_13` (Distance: 13.063 IQR)
- **Magnitude:** 501.6 | **LOC:** 751 | **CtrlFlow:** 55.9% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (95.0%)
- **Heaviest Functions:** `performRequest` (Impact: 98.8), `initializeArticle` (Impact: 44.4), `tryNormaliseRedirect` (Impact: 42.0)

### 10. `includes/Media/PNGMetadataExtractor.php` (PHP) -> Cumulative Risk: **660.63**
- **Archetype:** `file_cluster_13` (Distance: 13.248 IQR)
- **Magnitude:** 410.12 | **LOC:** 415 | **CtrlFlow:** 76.7% | **Authorship Centralization:** 16.7%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (99.9312%)
- **Heaviest Functions:** `getMetadata` (Impact: 224.9), `read` (Impact: 14.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `tests/phpunit/integration/includes/Json/key1.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/phpunit/integration/includes/Json/key1.pem.pub` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/phpunit/integration/includes/Json/key2.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/phpunit/integration/includes/Json/key2.pem.pub` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `includes/Language/Language.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.734 IQR)
- **Top Global Matches:** file_cluster_13: 14.734, file_cluster_8: 14.955, file_cluster_7: 15.005
- **Magnitude:** 4009.64 | **LOC:** 5079 | **CtrlFlow:** 49.5% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 218
- **Risk Profile:** Cognitive Load (46.2121%), Tech Debt (38.8232%)
**Top Internal Functions/Classes:**
  * `convertDateFormatToJs` (Impact: 724.3 | O(N^1) | DB: 218)
  * `truncateInternal` (Impact: 202.4 | O(N^1) | DB: 70)
  * `formatTimePeriod` (Impact: 91.2 | O(2^N) | DB: 60)
    * *Intent:* /** * A hidden direction mark (LRM or RLM), depending on the language direction. * Unlike getDirMark...
  * `getNamespaceIds` (Impact: 65.2 | O(2^N) | DB: 10)
    * *Intent:* /**
  * `tsToHebrew` (Impact: 43.1 | O(N^1) | DB: 28)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 732`, `structural_boundaries: 747`, `args: 158`, `func_start: 153`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 384`, `high_risk_execution: 2`, `state_mutation: 2003`, `dead_code: 6`, `planned_debt: 8`, `fragile_debt: 4`, `orphaned_logic: 35`
* *Architecture:* `io: 1`, `api: 137`, `import: 91`
* *Defense:* `safety: 45`, `doc: 559`, `test: 41`, `immutability_locks: 20`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.405
  * `Choke Point (Betweenness):` 0.002091 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 20):` DateTimeInterface, Wikimedia\ReplacementArray, 'years', MediaWiki\Message\Message, 'decades', RuntimeException, NumberFormatter, MediaWiki\User\UserTimeCorrection...
  * `Imported By (In-Degree: 156):` (Excluded from Brief to save tokens)

### `includes/EditPage/EditPage.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.494 IQR)
- **Top Global Matches:** file_cluster_13: 14.494, file_cluster_8: 14.824, file_cluster_7: 14.905
- **Magnitude:** 2494.92 | **LOC:** 4507 | **CtrlFlow:** 53.1% | **Authorship Centralization:** 47.2%
- **Algorithmic:** O(N^2) | **DB Complexity:** 333
- **Risk Profile:** Cognitive Load (45.89%), Tech Debt (12.2413%)
**Top Internal Functions/Classes:**
  * `__construct` (Impact: 1161.0 | O(N^2) | DB: 333)
  * `spamPageWithContent` (Impact: 25.5 | O(N^1) | DB: 7)
  * `getCheckboxesWidget` (Impact: 21.2 | O(N^1) | DB: 14)
  * `getEditToolbar` (Impact: 17.3 | O(N^1) | DB: 6)
  * `getTemplates` (Impact: 11.2 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 352`, `structural_boundaries: 311`, `args: 48`, `func_start: 48`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 1126`, `dead_code: 5`, `planned_debt: 4`, `fragile_debt: 5`
* *Architecture:* `io: 3`, `api: 44`, `import: 105`
* *Defense:* `safety: 40`, `doc: 241`, `test: 6`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.938
  * `Choke Point (Betweenness):` 0.000965 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 87):` MediaWiki\User\TempUser\CreateStatus, OOUI\FieldLayout, MediaWiki\Content\Content, MediaWiki\User\TempUser\TempUserCreator, MediaWiki\Page\CategoryPage, MediaWiki\Message\Message, MediaWiki\Revision\RevisionRecord, 'sharedupload-desc-create'...
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `includes/Permissions/PermissionManager.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.29 IQR)
- **Top Global Matches:** file_cluster_13: 13.29, file_cluster_8: 13.389, file_cluster_7: 13.52
- **Magnitude:** 2419.76 | **LOC:** 1925 | **CtrlFlow:** 63.6% | **Authorship Centralization:** 42.9%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 165
- **Risk Profile:** Cognitive Load (43.8018%), Tech Debt (24.96%)
**Top Internal Functions/Classes:**
  * `getPermissionStatus` (Impact: 1835.0 | O(2^N) | DB: 165)
  * `__construct` (Impact: 5.7 | O(N^1) | DB: 15)
  * `overrideUserRightsForTesting` (Impact: 5.5 | O(N^1) | DB: 1)
  * `addTemporaryUserRights` (Impact: 3.9 | O(N^1) | DB: 2)
    * *Intent:* /**
  * `userCan` (Impact: 2.4 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 369`, `structural_boundaries: 211`, `args: 39`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 124`, `high_risk_execution: 3`, `state_mutation: 511`, `dead_code: 2`, `planned_debt: 11`, `fragile_debt: 4`, `orphaned_logic: 3`
* *Architecture:* `api: 22`, `import: 52`
* *Defense:* `safety: 18`, `doc: 177`, `test: 22`, `immutability_locks: 7`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.315
  * `Choke Point (Betweenness):` 0.00021 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 29):` s a full User object
			$this->hookRunner->onUserGetRightsRemove( $userObj,  is set to a special page, MediaWiki\Message\Message, s a full User object
			$this->hookRunner->onUserGetRights( $userObj, MediaWiki\Block\AbstractBlock, MediaWiki\HookContainer\HookContainer, MediaWiki\Title\TitleFormatter, Wikimedia\Message\MessageValue...
  * `Imported By (In-Degree: 26):` (Excluded from Brief to save tokens)

### `tests/phpunit/MediaWikiIntegrationTestCase.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.542 IQR)
- **Top Global Matches:** file_cluster_13: 13.542, file_cluster_8: 13.694, file_cluster_7: 13.827
- **Magnitude:** 1833.06 | **LOC:** 2793 | **CtrlFlow:** 45.3% | **Authorship Centralization:** 37.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (14.4196%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `installMockMwServices` (Impact: 49.5 | O(N^1) | DB: 13)
    * *Intent:* * If called with no parameters, this method restores all services to their default state. * This is ...
  * `stashMwGlobals` (Impact: 44.6 | O(N^1) | DB: 9)
    * *Intent:* /** * Overrides a set of config settings for the duration of the current test case. * The original v...
  * `mediaWikiTearDown` (Impact: 41.4 | O(N^1) | DB: 15)
  * `listTables` (Impact: 40.6 | O(2^N) | DB: 4)
  * `mediaWikiSetUp` (Impact: 40.2 | O(2^N) | DB: 6)
    * *Intent:* /** * @return bool
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 408`, `structural_boundaries: 492`, `args: 110`, `func_start: 99`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 263`, `high_risk_execution: 3`, `state_mutation: 758`, `dead_code: 4`, `planned_debt: 13`, `fragile_debt: 2`
* *Architecture:* `api: 49`, `import: 73`
* *Defense:* `safety: 62`, `doc: 284`, `test: 129`, `immutability_locks: 9`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.462
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 42):` MediaWiki\Content\Content, MediaWikiGroupValidator, MediaWiki\Revision\RevisionRecord, $condition, MediaWiki\Context\DerivativeContext, MediaWikiCoversValidator, array $join_conds = []
	) 
		if ( !self::needsDB() ) 
			throw new LogicException( 'When testing database state, MediaWiki\DB\CloneDatabase...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `includes/Revision/RevisionStore.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.192 IQR)
- **Top Global Matches:** file_cluster_13: 14.192, file_cluster_8: 14.516, file_cluster_11: 14.577
- **Magnitude:** 1816.42 | **LOC:** 3443 | **CtrlFlow:** 45.0% | **Authorship Centralization:** 30.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 120
- **Risk Profile:** Cognitive Load (44.7421%), Tech Debt (13.3817%)
**Top Internal Functions/Classes:**
  * `loadSlotContent` (Impact: 1111.7 | O(2^N) | DB: 120)
    * *Intent:* /** * @param IDatabase $dbw * @param RevisionRecord $rev * @param int $parentId * * @return array a ...
  * `insertRevisionInternal` (Impact: 17.5 | O(N^1) | DB: 10)
  * `insertRevisionOn` (Impact: 17.0 | O(N^1) | DB: 9)
  * `insertSlotOn` (Impact: 13.6 | O(N^1) | DB: 5)
  * `insertRevisionRowOn` (Impact: 12.6 | O(N^1) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 184`, `structural_boundaries: 225`, `args: 43`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 502`, `dead_code: 2`, `planned_debt: 8`, `fragile_debt: 2`
* *Architecture:* `api: 28`, `import: 62`
* *Defense:* `safety: 70`, `doc: 186`, `sync_locks: 3`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.628
  * `Choke Point (Betweenness):` 0.000556 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 41):` stdClass>>>
	 *         a status containing, ?RevisionRecord $new = null, MediaWiki\Content\Content, ?RevisionRecord $old = null, $new, 'rev_page', MediaWiki\RecentChanges\RecentChange, stdClass...
  * `Imported By (In-Degree: 51):` (Excluded from Brief to save tokens)

### `includes/Output/OutputPage.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.453 IQR)
- **Top Global Matches:** file_cluster_13: 13.453, file_cluster_8: 13.528, file_cluster_7: 13.646
- **Magnitude:** 1659.96 | **LOC:** 5226 | **CtrlFlow:** 44.0% | **Authorship Centralization:** 7.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 303
- **Risk Profile:** Cognitive Load (34.4271%), Tech Debt (17.4995%)
**Top Internal Functions/Classes:**
  * `setPageTitle` (Impact: 782.7 | O(N^2) | DB: 303)
    * *Intent:* /**
  * `setIndexPolicy` (Impact: 14.0 | O(2^N) | DB: 2)
  * `getRobotsContent` (Impact: 7.6 | O(N^1) | DB: 3)
  * `getIndexPolicy` (Impact: 7.4 | O(2^N) | DB: 3)
  * `setRobotPolicy` (Impact: 7.2 | O(N^1) | DB: 1)
    * *Intent:* /** * @var string Contains all of the "<body>" content. Should be private we * got set/get accessors...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 226`, `structural_boundaries: 288`, `args: 96`, `func_start: 91`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 303`, `high_risk_execution: 1`, `state_mutation: 675`, `dead_code: 3`, `planned_debt: 4`, `fragile_debt: 5`, `orphaned_logic: 6`
* *Architecture:* `io: 21`, `api: 84`, `import: 66`
* *Defense:* `safety: 31`, `doc: 300`, `test: 9`, `immutability_locks: 7`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.12
  * `Choke Point (Betweenness):` 0.001909 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 42):` MediaWiki\Content\Content, MediaWiki\Message\Message, Wikimedia\Message\MessageParam, 
	public function setPrintable() 
		$this->mPrintable = true, must-revalidate, MediaWiki\Request\FauxRequest, Wikimedia\Rdbms\IResultWrapper, MediaWiki\Parser\Parser...
  * `Imported By (In-Degree: 77):` (Excluded from Brief to save tokens)

### `includes/libs/ObjectCache/WANObjectCache.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.063 IQR)
- **Top Global Matches:** file_cluster_13: 15.063, file_cluster_8: 15.196, file_cluster_7: 15.211
- **Magnitude:** 1611.1 | **LOC:** 3089 | **CtrlFlow:** 58.9% | **Authorship Centralization:** 20.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 209
- **Risk Profile:** Cognitive Load (45.5937%), Tech Debt (12.0711%)
**Top Internal Functions/Classes:**
  * `getMulti` (Impact: 884.6 | O(2^N) | DB: 209)
  * `__construct` (Impact: 25.5 | O(N^1) | DB: 9)
  * `setLogger` (Impact: 2.6 | O(N^1) | DB: 1)
    * *Intent:* /** Idiom for getWithSetCallback() meaning "no cache stampede mutex" */
  * `newEmpty` (Impact: 1.9 | O(N^1))
    * *Intent:* /** Idiom for set()/getWithSetCallback() meaning "no post-expiration grace period" */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 198`, `structural_boundaries: 138`, `args: 42`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 644`, `dead_code: 1`, `planned_debt: 1`, `orphaned_logic: 2`
* *Architecture:* `api: 35`, `import: 14`
* *Defense:* `safety: 50`, `doc: 263`, `test: 1`, `immutability_locks: 66`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.324
  * `Choke Point (Betweenness):` 0.000171 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` and a wildcard routing prefix for the 'broadcastRoutingPrefix' parameter.
 *        Configure mcrouter, List-of-Route-Handles#failoverroute
 *   - B) Set up dynomite, which have high TTLs, d keys into the in-process warmup cache
		$this->warmupCache = $this->fetchWrappedValuesForWarmupCache(
			$this->getNonProcessCachedMultiKeys( $keyedIds, d, $setOpts, which
	 *        effects any lockTSE logic in getWithSetCallback()
	 *   - c) Since "check" keys are initialized only on the server the key hashes
	 *        to, Wikimedia\Stats\StatsFactory...
  * `Imported By (In-Degree: 52):` (Excluded from Brief to save tokens)

### `includes/libs/Rdbms/Database/Database.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.352 IQR)
- **Top Global Matches:** file_cluster_13: 14.352, file_cluster_8: 14.483, file_cluster_7: 14.504
- **Magnitude:** 1578.34 | **LOC:** 3606 | **CtrlFlow:** 36.1% | **Authorship Centralization:** 20.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 78
- **Risk Profile:** Cognitive Load (44.0494%), Tech Debt (83.205%)
**Top Internal Functions/Classes:**
  * `cancelAtomic` (Impact: 210.9 | O(2^N) | DB: 78)
  * `__construct` (Impact: 61.8 | O(N^1) | DB: 28)
  * `insertSelect` (Impact: 45.9 | O(2^N) | DB: 9)
    * *Intent:* /** * Check if callers outside of Database can run the given query given the session state * * In or...
  * `upsert` (Impact: 33.6 | O(N^1) | DB: 22)
  * `executeQuery` (Impact: 28.9 | O(N^1) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 204`, `structural_boundaries: 361`, `args: 149`, `func_start: 145`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 685`, `dead_code: 3`, `planned_debt: 2`, `fragile_debt: 1`, `orphaned_logic: 33`
* *Architecture:* `api: 121`, `import: 19`
* *Defense:* `safety: 48`, `doc: 343`, `sync_locks: 5`, `immutability_locks: 31`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.342
  * `Choke Point (Betweenness):` 0.000281 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` query, Wikimedia\Telemetry\TracerInterface, RuntimeException, $sql->getSQL(), ROLLBACK before allowing any other queries from outside callers
	 *         $this->completeCriticalSection( __METHOD__, $trxError, Wikimedia\Rdbms\Platform\SQLPlatform, 
	protected function completeCriticalSection(
		string $fname...
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `includes/Skin/Skin.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.056 IQR)
- **Top Global Matches:** file_cluster_13: 14.056, file_cluster_8: 14.237, file_cluster_7: 14.341
- **Magnitude:** 1556.82 | **LOC:** 2584 | **CtrlFlow:** 49.4% | **Authorship Centralization:** 18.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 152
- **Risk Profile:** Cognitive Load (45.5171%), Tech Debt (9.6571%)
**Top Internal Functions/Classes:**
  * `getUndeleteLink` (Impact: 519.7 | O(2^N) | DB: 152)
  * `getTemplateData` (Impact: 45.3 | O(2^N) | DB: 17)
  * `getDefaultModules` (Impact: 42.2 | O(N^1) | DB: 13)
    * *Intent:* // Don't return the default immediately; // in a misconfiguration we need to fall back.
  * `getCategoryLinks` (Impact: 34.3 | O(2^N) | DB: 22)
  * `getRelevantUser` (Impact: 24.2 | O(N^1) | DB: 11)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 223`, `structural_boundaries: 228`, `args: 54`, `func_start: 53`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 705`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `api: 49`, `import: 36`
* *Defense:* `safety: 26`, `doc: 161`, `test: 4`, `immutability_locks: 14`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.155
  * `Choke Point (Betweenness):` 0.001088 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 26):` an 'oldid' specifier, MediaWiki\Skin\Components\SkinComponentRegistryContext, MediaWiki\Skin\Components\SkinComponentLink, $item, generally in lowercase to comply with conventions
	 *     for interface message keys and CSS class names which embed this value.
	 *
	 *  - `format`: Enable rendering of skin, MediaWiki\HookContainer\ProtectedHookAccessorTrait, set $item['tooltiponly'] = true, 
	final public function makeListItem( $key...
  * `Imported By (In-Degree: 67):` (Excluded from Brief to save tokens)

### `includes/libs/Rdbms/LoadBalancer/LoadBalancer.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.235 IQR)
- **Top Global Matches:** file_cluster_8: 14.235, file_cluster_13: 14.242, file_cluster_7: 14.352
- **Magnitude:** 1511.66 | **LOC:** 2046 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 20.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (35.7046%), Tech Debt (47.2262%)
**Top Internal Functions/Classes:**
  * `configure` (Impact: 67.4 | O(N^1) | DB: 25)
    * *Intent:* /** @var int Idiom for getExistingReaderIndex() meaning "no index selected" */
  * `reallyOpenConnection` (Impact: 55.4 | O(N^1) | DB: 12)
    * *Intent:* /** * Get the server index chosen for DB_REPLICA connections for the given query group
  * `runPrimaryTransactionIdleCallbacks` (Impact: 51.0 | O(N^1) | DB: 14)
    * *Intent:* /** * Sanity check to make sure that the right domain is selected *
  * `getReaderIndex` (Impact: 47.9 | O(N^1) | DB: 20)
  * `waitForPrimaryPos` (Impact: 33.9 | O(N^1) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 265`, `structural_boundaries: 237`, `args: 70`, `func_start: 66`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 58`, `state_mutation: 661`, `orphaned_logic: 28`
* *Architecture:* `api: 46`, `concurrency: 2`, `import: 14`
* *Defense:* `safety: 62`, `doc: 192`, `test: 4`, `immutability_locks: 17`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):`  Note that callbacks should already be suppressed due to finalizePrimaryChanges().
		foreach ( $this->getOpenPrimaryConnections(),  Use low timeouts, RuntimeException, Wikimedia\ObjectCache\BagOStuff, Wikimedia\ObjectCache\EmptyBagOStuff, DatabaseDomain $domain, UnexpectedValueException,  attempts in order to be resolved into a real server index.
			$attributes = $this->getServerAttributes( ServerInfo::WRITER_INDEX...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `includes/Title/Title.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.483 IQR)
- **Top Global Matches:** file_cluster_13: 14.483, file_cluster_8: 14.835, file_cluster_7: 14.862
- **Magnitude:** 1460.04 | **LOC:** 3898 | **CtrlFlow:** 41.0% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 316
- **Risk Profile:** Cognitive Load (45.6421%), Tech Debt (12.0233%)
**Top Internal Functions/Classes:**
  * `newFromLinkTarget` (Impact: 442.5 | O(N^1) | DB: 316)
    * *Intent:* /** * Text form including namespace/interwiki, initialised on demand
  * `newFromDBkey` (Impact: 7.2 | O(N^1) | DB: 1)
  * `getTitleFormatter` (Impact: 3.6 | O(2^N))
    * *Intent:* /***************************************************************************/ // region Private memb...
  * `getInterwikiLookup` (Impact: 3.6 | O(2^N))
  * `getPageLanguageConverter` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 218`, `structural_boundaries: 314`, `args: 86`, `func_start: 85`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 894`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 3`
* *Architecture:* `api: 80`, `import: 54`
* *Defense:* `safety: 27`, `doc: 246`, `test: 11`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 36):` a proper page is one that can
	 * exist in the page table. That is, s this Title to be a "proper page" in the sense
	 * defined by PageIdentity should call this method.
	 *
	 * For the purpose of the Title class, 
	public function getCanonicalURL( $query = '' ) 
		$services = MediaWikiServices::getInstance(, MediaWiki\Message\Message, MediaWiki\Deferred\LinksUpdate\TemplateLinksTable, MediaWiki\Exception\MWException, 
	public function hasSubpages() 
		if (
			!MediaWikiServices::getInstance()->getNamespaceInfo()->
				hasSubpages( $this->mNamespace )
		) 
			# Duh
			return false, RuntimeException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `includes/FileRepo/File/LocalFile.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.706 IQR)
- **Top Global Matches:** file_cluster_13: 13.706, file_cluster_8: 13.832, file_cluster_7: 13.946
- **Magnitude:** 1417.18 | **LOC:** 2809 | **CtrlFlow:** 49.1% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 90
- **Risk Profile:** Cognitive Load (44.1746%), Tech Debt (25.2953%)
**Top Internal Functions/Classes:**
  * `upgradeRow` (Impact: 188.7 | O(N^1) | DB: 90)
    * *Intent:* /** * Returns the list of object properties that are included as-is in the * cache, only when they'r...
  * `recordUpload3` (Impact: 153.8 | O(N^1) | DB: 57)
  * `maybeUpgradeRow` (Impact: 40.6 | O(N^1) | DB: 15)
    * *Intent:* /** * @return LocalRepo|false */
  * `loadFromDB` (Impact: 29.1 | O(N^1) | DB: 15)
  * `move` (Impact: 24.8 | O(2^N) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 230`, `structural_boundaries: 238`, `args: 56`, `func_start: 52`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 55`, `state_mutation: 716`, `planned_debt: 4`, `orphaned_logic: 11`
* *Architecture:* `api: 39`, `import: 46`
* *Defense:* `safety: 25`, `doc: 213`, `test: 7`, `sync_locks: 3`, `immutability_locks: 8`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.358
  * `Choke Point (Betweenness):` 0.000399 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 37):` '1.41', only when they're not too big, MediaWiki\FileRepo\FileRepo, Wikimedia\FileBackend\FileBackendError, d as-is in the
	 * cache, RuntimeException, stdClass, MediaWiki\FileRepo\FileBackendDBRepoWrapper...
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `includes/Parser/CoreParserFunctions.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.239 IQR)
- **Top Global Matches:** file_cluster_13: 15.239, file_cluster_11: 15.505, file_cluster_0: 15.555
- **Magnitude:** 1394.34 | **LOC:** 2116 | **CtrlFlow:** 47.3% | **Authorship Centralization:** 30.0%
- **Algorithmic:** O(N) | **DB Complexity:** 283
- **Risk Profile:** Cognitive Load (45.9451%), Tech Debt (12.0587%)
**Top Internal Functions/Classes:**
  * `urlencode` (Impact: 412.2 | O(N^1) | DB: 283)
  * `register` (Impact: 16.5 | O(N^1) | DB: 3)
  * `ns` (Impact: 11.0 | O(N^1) | DB: 4)
  * `formatDate` (Impact: 10.8 | O(N^1) | DB: 8)
  * `intFunction` (Impact: 6.5 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 201`, `structural_boundaries: 224`, `args: 62`, `func_start: 59`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 859`, `dead_code: 7`, `fragile_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 57`, `import: 21`
* *Defense:* `safety: 14`, `doc: 262`, `test: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` Wikimedia\RemexHtml\Tokenizer\PlainAttributes, MediaWiki\Language\LanguageNameUtils, MediaWiki\Revision\RevisionRecord, MediaWiki\Content\ContentHandler, MediaWiki\Category\Category, d,  Fall back to Parser's "revision user" for the current title
			$parser->getOutput()->setOutputFlag( ParserOutputFlags::VARY_USER, MediaWiki\SpecialPage\SpecialPage...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `includes/Auth/AuthManager.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.278 IQR)
- **Top Global Matches:** file_cluster_13: 13.278, file_cluster_8: 13.423, file_cluster_7: 13.632
- **Magnitude:** 1354.32 | **LOC:** 3021 | **CtrlFlow:** 55.7% | **Authorship Centralization:** 23.1%
- **Algorithmic:** O(N^2) | **DB Complexity:** 70
- **Risk Profile:** Cognitive Load (34.5181%), Tech Debt (15.5135%)
**Top Internal Functions/Classes:**
  * `securitySensitiveOperationStatus` (Impact: 349.1 | O(N^2) | DB: 70)
  * `continueAuthentication` (Impact: 251.7 | O(N^2) | DB: 38)
    * *Intent:* /** * AuthManager is the authentication system in MediaWiki and serves entry point for authenticatio...
  * `autoCreateUser` (Impact: 232.3 | O(N^1) | DB: 54)
  * `autocreatingTempUserToAppealBlock` (Impact: 16.8 | O(N^1) | DB: 3)
  * `logAutocreationAttempt` (Impact: 14.2 | O(N^1) | DB: 1)
    * *Intent:* /** * Change authentication data (e.g. passwords) * * If $req was returned for AuthManager::ACTION_C...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 249`, `structural_boundaries: 198`, `args: 25`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 450`, `dead_code: 2`, `fragile_debt: 2`, `orphaned_logic: 3`
* *Architecture:* `api: 16`, `import: 51`
* *Defense:* `safety: 27`, `doc: 89`, `test: 5`, `sync_locks: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.752
  * `Choke Point (Betweenness):` 0.000432 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 41):` MediaWiki\User\BotPasswordStore, array $reqs, MediaWiki\Session\SessionManagerInterface, MediaWiki\User\Options\UserOptionsManager, MediaWiki\User\TempUser\TempUserCreator, d request if from a Primary, d === AuthenticationRequest::REQUIRED
					|| $reqs[$id]->required === AuthenticationRequest::OPTIONAL
				) 
					$reqs[$id] = $req, code>
	 * returns true...
  * `Imported By (In-Degree: 35):` (Excluded from Brief to save tokens)

### `includes/Specials/SpecialUndelete.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.509 IQR)
- **Top Global Matches:** file_cluster_13: 13.509, file_cluster_8: 13.685, file_cluster_7: 13.881
- **Magnitude:** 1259.52 | **LOC:** 1679 | **CtrlFlow:** 49.1% | **Authorship Centralization:** 20.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 97
- **Risk Profile:** Cognitive Load (32.3314%), Tech Debt (18.2895%)
**Top Internal Functions/Classes:**
  * `showHistory` (Impact: 210.7 | O(N^2) | DB: 97)
  * `showRevision` (Impact: 72.5 | O(N^1) | DB: 29)
  * `loadRequest` (Impact: 65.1 | O(N^1) | DB: 42)
  * `execute` (Impact: 45.8 | O(N^1) | DB: 9)
  * `redirectToRevDel` (Impact: 21.2 | O(N^1) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 190`, `structural_boundaries: 197`, `args: 28`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 673`, `dead_code: 1`, `planned_debt: 5`, `fragile_debt: 3`, `orphaned_logic: 1`
* *Architecture:* `io: 3`, `api: 6`, `import: 62`
* *Defense:* `safety: 28`, `doc: 95`, `test: 3`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.078
  * `Choke Point (Betweenness):` 0.000246 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 45):` MediaWiki\RecentChanges\ChangesList, MediaWiki\FileRepo\File\ArchivedFile, OOUI\ButtonInputWidget, OOUI\FieldLayout, MediaWiki\Message\Message, MediaWiki\Revision\RevisionRecord, MediaWiki\Logging\LogPage, MediaWiki\Page\UndeletePageFactory...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `includes/libs/FileBackend/FileBackendStore.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.127 IQR)
- **Top Global Matches:** file_cluster_13: 14.127, file_cluster_8: 14.354, file_cluster_7: 14.412
- **Magnitude:** 1137.42 | **LOC:** 2088 | **CtrlFlow:** 47.9% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 38
- **Risk Profile:** Cognitive Load (45.0128%), Tech Debt (81.6112%)
**Top Internal Functions/Classes:**
  * `doQuickOperationsInternal` (Impact: 139.2 | O(N^1) | DB: 38)
  * `doClean` (Impact: 51.3 | O(2^N) | DB: 7)
  * `getFileStat` (Impact: 44.5 | O(N^1) | DB: 13)
  * `doConcatenate` (Impact: 32.8 | O(N^1) | DB: 19)
    * *Intent:* /** * Copy a file from one storage path to another in the backend. * This will overwrite any file th...
  * `getFileXAttributes` (Impact: 21.4 | O(N^1) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 193`, `structural_boundaries: 210`, `args: 63`, `func_start: 63`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 497`, `dead_code: 3`, `planned_debt: 2`, `orphaned_logic: 23`
* *Architecture:* `io: 3`, `api: 25`, `import: 24`
* *Defense:* `safety: 32`, `doc: 210`, `test: 2`, `immutability_locks: 41`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` 
		$ps = $this->scopedProfileSection( __METHOD__ . "-$this->name", loading the persistent stat cache will likely yield the SHA-1.
				( $requireSHA1 && is_array( $stat ) && !isset( $stat['sha1'] ) )
			) 
				$this->primeFileCache( [ $path ], value map
	 *   - async               : StatusValue will be returned immediately if supported.
	 *                           If the StatusValue is OK, value map
	 *   - async         : StatusValue will be returned immediately if supported.
	 *                     If the StatusValue is OK, value map
	 *   - async       : StatusValue will be returned immediately if supported.
	 *                   If the StatusValue is OK, SHA1 || isset( $stat['sha1'] ) )
			) 
				return $stat, Wikimedia\FileBackend\FileOpHandle\FileBackendStoreOpHandle, Wikimedia\ObjectCache\BagOStuff...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `includes/GlobalFunctions.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.045 IQR)
- **Top Global Matches:** file_cluster_13: 15.045, file_cluster_8: 15.331, file_cluster_11: 15.384
- **Magnitude:** 1122.82 | **LOC:** 1966 | **CtrlFlow:** 55.4% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 57
- **Risk Profile:** Cognitive Load (38.4676%), Tech Debt (99.3224%)
**Top Internal Functions/Classes:**
  * `wfStripIllegalFilenameChars` (Impact: 100.3 | O(N^1) | DB: 36)
    * *Intent:* /** * Send a line to a supplementary debug log file, if configured, or main debug * log if not. * * ...
  * `wfArrayToCgi` (Impact: 57.8 | O(2^N) | DB: 15)
    * *Intent:* /** * Recursively converts the parameter (an object) to an array with the same data * * @phpcs:ignor...
  * `wfMerge` (Impact: 57.7 | O(N^1) | DB: 57)
    * *Intent:* * 3) Verifies that the protocol is on the $wgUrlProtocols allowed list. * 4) Rejects some invalid UR...
  * `wfResetOutputBuffers` (Impact: 35.9 | O(N^1) | DB: 5)
  * `wfCgiToArray` (Impact: 35.4 | O(N^1) | DB: 15)
    * *Intent:* /** * Get a random string containing a number of pseudo-random hex characters. *
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 169`, `structural_boundaries: 136`, `args: 44`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 17`, `high_risk_execution: 2`, `state_mutation: 574`, `dead_code: 1`, `fragile_debt: 3`, `orphaned_logic: 25`
* *Architecture:* `io: 10`, `import: 23`
* *Defense:* `safety: 20`, `doc: 156`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` Wikimedia\ParamValidator\TypeDef\ExpiryDef, ProtocolRelative If false, 
function wfUrlProtocols( $includeProtocolRelative = true ) 
	wfDeprecated( __FUNCTION__, 
function wfStripIllegalFilenameChars( $name ) 
	global $wgIllegalFileChars, 
function wfDeprecatedMsg( $msg, ', which urlencode encodes by default.  According to RFC 1738, MediaWiki\Message\Message...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `includes/libs/Diff/DiffEngine.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.894 IQR)
- **Top Global Matches:** file_cluster_8: 13.894, file_cluster_13: 14.094, file_cluster_7: 14.106
- **Magnitude:** 1070.68 | **LOC:** 803 | **CtrlFlow:** 79.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 116
- **Risk Profile:** Cognitive Load (37.9102%), Tech Debt (36.8171%)
**Top Internal Functions/Classes:**
  * `find_middle_snake` (Impact: 183.1 | O(N^1) | DB: 116)
  * `shiftBoundaries` (Impact: 81.8 | O(N^1) | DB: 28)
    * *Intent:* /** * This diff implementation is mainly lifted from the LCS algorithm of the Eclipse project which ...
  * `diffInternal` (Impact: 63.5 | O(N^1) | DB: 46)
    * *Intent:* /** * Adjust inserts/deletes of identical lines to join changes * as much as possible. * * We do som...
  * `lcs_rec` (Impact: 49.7 | O(2^N) | DB: 9)
    * *Intent:* // remember initial lengths
  * `findMostProgress` (Impact: 44.1 | O(N^1) | DB: 28)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 162`, `structural_boundaries: 41`, `args: 7`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 50`, `state_mutation: 627`, `dead_code: 1`, `fragile_debt: 2`, `orphaned_logic: 4`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `safety: 8`, `doc: 36`, `test: 8`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` array $other_changed ) 
		$i = 0, identical line at the other.
	 * We are free to choose which identical line is included.
	 * `compareseq' usually chooses the one at the beginning, 
			$max = min( $this->m, array &$changed, $this->n, a
	 * line at one end and has an excluded, 
	private function shiftBoundaries( array $lines
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `includes/Page/WikiPage.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.95 IQR)
- **Top Global Matches:** file_cluster_13: 13.95, file_cluster_8: 14.289, file_cluster_7: 14.336
- **Magnitude:** 1062.42 | **LOC:** 2985 | **CtrlFlow:** 43.1% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 209
- **Risk Profile:** Cognitive Load (45.5874%), Tech Debt (15.8766%)
**Top Internal Functions/Classes:**
  * `getContentModel` (Impact: 336.2 | O(N^1) | DB: 209)
  * `convertSelectType` (Impact: 14.1 | O(N^1))
    * *Intent:* /** * @var RevisionRecord|null */
  * `__construct` (Impact: 5.4 | O(N^1) | DB: 2)
    * *Intent:* /**
  * `getQueryInfo` (Impact: 4.9 | O(N^1) | DB: 2)
  * `getContentHandler` (Impact: 3.7 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 168`, `structural_boundaries: 222`, `args: 58`, `func_start: 54`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 599`, `dead_code: 2`, `planned_debt: 14`, `fragile_debt: 1`
* *Architecture:* `api: 50`, `import: 64`
* *Defense:* `safety: 4`, `doc: 200`, `test: 2`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.279
  * `Choke Point (Betweenness):` 0.004338 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 49):`  Only for the main slot, MediaWiki\Content\Content, MediaWiki\Revision\RevisionRecord, MediaWiki\RecentChanges\RecentChange, stdClass, this page
		DeferredUpdates::addCallableUpdate( static function () use ( $title ) 
			self::queueBacklinksJobs( $title, [ 'causeAction' => $causeAction ], Wikimedia\NonSerializable\NonSerializableTrait...
  * `Imported By (In-Degree: 62):` (Excluded from Brief to save tokens)

### `tests/phpunit/integration/includes/libs/FileBackend/FileBackendIntegrationTestBase.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.98 IQR)
- **Top Global Matches:** file_cluster_8: 11.98, file_cluster_7: 12.4, file_cluster_13: 12.454
- **Magnitude:** 1055.98 | **LOC:** 2106 | **CtrlFlow:** 45.7% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 32
- **Risk Profile:** Cognitive Load (47.0261%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testDoQuickOperations` (Impact: 37.9 | O(N^1) | DB: 2)
  * `testGetDirectoryList` (Impact: 33.1 | O(N^1) | DB: 32)
  * `testConcatenate` (Impact: 27.5 | O(N^1) | DB: 20)
  * `testCopy` (Impact: 21.7 | O(N^1) | DB: 8)
  * `testMove` (Impact: 21.7 | O(N^1) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 132`, `args: 52`, `func_start: 52`, `class_start: 1`
* *Risk/State:* `state_mutation: 565`, `dead_code: 1`, `fragile_debt: 10`, `orphaned_logic: 42`
* *Architecture:* `io: 16`, `api: 41`, `import: 10`
* *Defense:* `safety: 9`, `doc: 26`, `test: 136`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` MediaWiki\Config\ServiceOptions, Wikimedia\FileBackend\FSFile\TempFSFile, MediaWiki\Http\HttpRequestFactory, Wikimedia\FileBackend\FileBackend, MediaWiki\Status\Status, Wikimedia\FileBackend\FSFileBackend, Wikimedia\FileBackend\FSFile\FSFile, Shellbox\Shellbox...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `includes/RecentChanges/ChangesListQuery/ChangesListQuery.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.616 IQR)
- **Top Global Matches:** file_cluster_13: 13.616, file_cluster_8: 13.822, file_cluster_7: 13.881
- **Magnitude:** 1043.54 | **LOC:** 1781 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 37.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (43.4728%), Tech Debt (95.0924%)
**Top Internal Functions/Classes:**
  * `prepareAudienceCondition` (Impact: 36.0 | O(N^1) | DB: 6)
  * `doPartitionUnion` (Impact: 25.3 | O(2^N) | DB: 2)
  * `applyLinkTarget` (Impact: 20.9 | O(N^1) | DB: 6)
  * `emulateUnion` (Impact: 20.6 | O(2^N) | DB: 2)
    * *Intent:* /** * Call all modules asking them to populate fields, joins, etc. */
  * `doPartitionQuery` (Impact: 20.3 | O(N^1) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 326`, `args: 103`, `func_start: 98`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 387`, `planned_debt: 2`, `orphaned_logic: 35`
* *Architecture:* `api: 64`, `import: 50`
* *Defense:* `safety: 12`, `doc: 283`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.182
  * `Choke Point (Betweenness):` 4.4e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 29):` $namespaces, 
	public function requireSubpageOf( LinkTarget|PageReference $page ) 
		$this->getSubpageOfCondition()->require( $page, MediaWiki\Revision\RevisionRecord, $watchTypes, MediaWiki\RecentChanges\RecentChange, 
	public function applyAction( string $verb, stdClass, that the changes come from the specified sources...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `resources/src/mediawiki.api/AbortController.js` (JAVASCRIPT) | Magnitude: 40.44 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 20, concurrency: 18, state_mutation: 16, panics_and_aborts: 16
- `includes/libs/MappedIterator.php` (PHP) | Magnitude: 96.92 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 58, state_mutation: 33, doc: 18, structural_boundaries: 17
- `includes/libs/FileBackend/FileIteration/SwiftFileBackendFileList.php` (PHP) | Magnitude: 18.46 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 13, structural_boundaries: 8, state_mutation: 7, doc: 7
- `resources/src/mediawiki.watchstar.widgets/WatchlistPopup.js` (JAVASCRIPT) | Magnitude: 121.02 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 86, branch: 21, listeners: 17, doc: 10
- `resources/src/mediawiki.rcfilters/UriProcessor.js` (JAVASCRIPT) | Magnitude: 167.34 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 120, state_mutation: 70, doc: 34, branch: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `resources/src/mediawiki.rcfilters/ui/ChangesLimitPopupWidget.js` (JAVASCRIPT) | Magnitude: 42.94 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 33, state_mutation: 28, doc: 10, func_start: 4
- `resources/src/mediawiki.rcfilters/ui/CheckboxInputWidget.js` (JAVASCRIPT) | Magnitude: 16.78 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: doc: 6, indent_tabs: 6, func_start: 4, state_mutation: 4
- `includes/DomainEvent/DomainEventDispatcher.php` (PHP) | Magnitude: 33.96 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, indent_tabs: 4, doc: 2, branch: 1
- `includes/Notification/NotificationHandler.php` (PHP) | Magnitude: 31.88 | Delta: **0.245 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, doc: 2, branch: 1, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `includes/DevelopmentSettings.php` (PHP) | Magnitude: 71.62 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 55, indent_tabs: 43, branch: 10, doc: 6
- `resources/src/mediawiki.ForeignStructuredUpload.BookletLayout/ForeignStructuredUpload.js` (JAVASCRIPT) | Magnitude: 82.74 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 73, state_mutation: 55, doc: 24, args: 17
- `resources/src/mediawiki.rcfilters/ui/FilterMenuOptionWidget.js` (JAVASCRIPT) | Magnitude: 68.02 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 40, indent_tabs: 28, doc: 10, branch: 7
- `includes/libs/ObjectCache/Utils/MemcachedClient.php` (PHP) | Magnitude: 780.1 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 376, state_mutation: 370, branch: 100, doc: 88
- `resources/src/startup/mediawiki.loader.js` (JAVASCRIPT) | Magnitude: 725.54 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 553, state_mutation: 338, branch: 136, structural_boundaries: 107

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `tests/phpunit/MediaWikiGroupValidator.php` (PHP) | Magnitude: 4.14 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 5, doc: 4, indent_tabs: 4, branch: 1
- `resources/src/mediawiki.rcfilters/ui/LiveUpdateButtonWidget.js` (JAVASCRIPT) | Magnitude: 22.7 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 12, state_mutation: 11, doc: 6, func_start: 4
- `resources/src/mediawiki.widgets/MediaSearch/mw.widgets.MediaUserUploadsProvider.js` (JAVASCRIPT) | Magnitude: 47.86 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 26, state_mutation: 16, args: 7, doc: 7
- `resources/src/mediawiki.widgets/MediaSearch/mw.widgets.MediaSearchProvider.js` (JAVASCRIPT) | Magnitude: 32.52 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 24, state_mutation: 12, args: 7, doc: 7
- `resources/src/mediawiki.rcfilters/ui/TagItemWidget.js` (JAVASCRIPT) | Magnitude: 24.46 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: sec_state_mutation: 11, doc: 10, state_mutation: 7, indent_tabs: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `includes/libs/Stats/NullStatsdDataFactory.php` (PHP) | Magnitude: 40.64 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 40, doc: 33, structural_boundaries: 27, args: 12
- `includes/ResourceLoader/ReplayMinifierState.php` (PHP) | Magnitude: 36.7 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 34, structural_boundaries: 23, doc: 10, args: 9
- `includes/Specials/SpecialTags.php` (PHP) | Magnitude: 207.02 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 213, state_mutation: 85, structural_boundaries: 45, branch: 40
- `tests/phpunit/includes/Content/validateContentTestData.php` (PHP) | Magnitude: 77.32 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 89, structural_boundaries: 26, state_mutation: 25, branch: 17
- `includes/Session/SessionId.php` (PHP) | Magnitude: 14.96 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 13, structural_boundaries: 10, doc: 10, args: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `resources/src/mediawiki.Uri/Uri.js` (JAVASCRIPT) | Magnitude: 249.92 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 94, state_mutation: 48, branch: 38, doc: 26
- `resources/src/mediawiki.api/rest.js` (JAVASCRIPT) | Magnitude: 71.5 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 88, doc: 34, state_mutation: 24, args: 13
- `resources/src/mediawiki.template.js` (JAVASCRIPT) | Magnitude: 51.22 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 54, doc: 38, args: 9, closures: 9
- `resources/src/mediawiki.widgets/MediaSearch/mw.widgets.MediaResultWidget.js` (JAVASCRIPT) | Magnitude: 161.54 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 135, state_mutation: 117, doc: 27, args: 17
- `resources/src/mediawiki.widgets/MediaSearch/mw.widgets.APIResultsQueue.js` (JAVASCRIPT) | Magnitude: 273.88 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: state_mutation: 178, indent_tabs: 102, doc: 33, concurrency: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `resources/src/mediawiki.special.changeslist.legend.js` (JAVASCRIPT) | Magnitude: 16.12 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 4, state_mutation: 3, args: 2, closures: 2
- `resources/src/mediawiki.rcfilters/dm/FilterGroup.js` (JAVASCRIPT) | Magnitude: 427.7 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: state_mutation: 269, indent_tabs: 228, doc: 82, branch: 72
- `includes/ExternalStore/ExternalStoreMemory.php` (PHP) | Magnitude: 51.94 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 33, state_mutation: 24, structural_boundaries: 15, doc: 13
- `includes/HTMLForm/Field/HTMLNamespacesMultiselectField.php` (PHP) | Magnitude: 106.88 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 64, state_mutation: 27, structural_boundaries: 26, branch: 23
- `resources/src/mediawiki.widgets/mw.widgets.LanguageSelectWidget.js` (JAVASCRIPT) | Magnitude: 32.2 | Delta: **0.08 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 53, branch: 10, args: 9, structural_boundaries: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `resources/src/mediawiki.widgets/mw.widgets.ExpiryInputWidget.js` (JAVASCRIPT) | Magnitude: 125.18 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 72, state_mutation: 57, branch: 10, structural_boundaries: 9
- `resources/src/mediawiki.widgets/mw.widgets.ComplexTitleInputWidget.js` (JAVASCRIPT) | Magnitude: 62.9 | Delta: **0.068 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 63, state_mutation: 26, doc: 9, structural_boundaries: 8
- `tests/phpunit/includes/Logging/LogTests.i18n.php` (PHP) | Magnitude: 17.16 | Delta: **0.112 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 4, state_mutation: 3, test: 3, scientific: 3
- `resources/src/mediawiki.widgets/mw.widgets.SizeFilterWidget.js` (JAVASCRIPT) | Magnitude: 35.02 | Delta: **0.144 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 54, state_mutation: 15, doc: 8, ui_framework: 8
- `resources/src/mediawiki.action/mediawiki.action.edit.checkboxes.less` (CSS) | Magnitude: 12.6 | Delta: **0.384 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 3, ui_framework: 2, class_start: 1, doc: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `resources/src/mediawiki.widgets/MediaSearch/mw.widgets.MediaSearchQueue.js` (JAVASCRIPT) | Magnitude: 36.98 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 32, state_mutation: 16, doc: 9, args: 6
- `tests/selenium/wdio-mediawiki/Util.js` (JAVASCRIPT) | Magnitude: 27.32 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 23, structural_boundaries: 18, doc: 11, args: 10
- `resources/src/mediawiki.widgets/MediaSearch/mw.widgets.MediaResourceProvider.js` (JAVASCRIPT) | Magnitude: 267.6 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 161, state_mutation: 130, doc: 41, structural_boundaries: 33
- `tests/api-testing/action/UserInfo.js` (JAVASCRIPT) | Magnitude: 32.16 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 29, concurrency: 25, structural_boundaries: 17, immutability_locks: 11
- `includes/Deferred/LinksUpdate/InterwikiLinksTable.php` (PHP) | Magnitude: 80.12 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 70, structural_boundaries: 32, state_mutation: 25, doc: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `includes/RenameUser/Hook/RenameUserWarningHook.php` (PHP) | Magnitude: 32.88 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 5, structural_boundaries: 3, branch: 1, args: 1
- `includes/ResourceLoader/Hook/ResourceLoaderSiteModulePagesHook.php` (PHP) | Magnitude: 32.88 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 5, structural_boundaries: 3, branch: 1, args: 1
- `includes/ResourceLoader/Hook/ResourceLoaderSiteStylesModulePagesHook.php` (PHP) | Magnitude: 32.88 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 5, structural_boundaries: 3, branch: 1, args: 1
- `includes/Language/Hook/MessageCacheFetchOverridesHook.php` (PHP) | Magnitude: 35.4 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 5, structural_boundaries: 4, state_mutation: 3, branch: 1
- `includes/Language/Hook/LocalisationCacheRecacheHook.php` (PHP) | Magnitude: 35.4 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 9, structural_boundaries: 4, state_mutation: 3, branch: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `includes/Interwiki/Interwiki.php` (PHP) | Magnitude: 59.76 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 43, doc: 38, state_mutation: 27, structural_boundaries: 18
- `includes/Title/ForeignTitleFactory.php` (PHP) | Magnitude: 35.4 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 8, structural_boundaries: 4, state_mutation: 3, branch: 1
- `includes/libs/WRStats/WRStatsFactory.php` (PHP) | Magnitude: 45.82 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 32, state_mutation: 23, doc: 20, structural_boundaries: 13
- `includes/libs/Rdbms/Database/Utils/GeneralizedSql.php` (PHP) | Magnitude: 30.4 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 26, doc: 19, state_mutation: 14, structural_boundaries: 11
- `includes/Search/SearchIndexField.php` (PHP) | Magnitude: 78.43 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 27, api: 17, indent_tabs: 17, immutability_locks: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `resources/src/mediawiki.page.gallery.js` (JAVASCRIPT) | Magnitude: 79.86 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 106, state_mutation: 40, branch: 19, immutability_locks: 13
- `includes/EditPage/IntroMessageBuilder.php` (PHP) | Magnitude: 468.64 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 474, state_mutation: 189, branch: 87, structural_boundaries: 77
- `includes/Specials/SpecialUnusedImages.php` (PHP) | Magnitude: 64.14 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 69, state_mutation: 30, structural_boundaries: 24, doc: 11
- `includes/libs/FileBackend/FileOps/CopyFileOp.php` (PHP) | Magnitude: 73.98 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 62, state_mutation: 39, structural_boundaries: 25, branch: 12
- `maintenance/resetAuthenticationThrottle.php` (PHP) | Magnitude: 139.46 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 137, state_mutation: 67, structural_boundaries: 27, branch: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `languages/messages/MessagesKu_arab.php` (PHP) | Magnitude: 26.4 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 12, state_mutation: 11, ownership: 6, branch: 1
- `languages/messages/MessagesGan.php` (PHP) | Magnitude: 20.16 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 6, dead_code: 3, branch: 1, structural_boundaries: 1
- `resources/src/mediawiki.page.ready/toggleAllCollapsibles.js` (JAVASCRIPT) | Magnitude: 21.9 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 42, structural_boundaries: 9, state_mutation: 6, branch: 5
- `languages/messages/MessagesMn.php` (PHP) | Magnitude: 21.56 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 20, ownership: 10, state_mutation: 6, doc: 2
- `languages/messages/MessagesTk.php` (PHP) | Magnitude: 19.38 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 15, ownership: 8, state_mutation: 4, branch: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `includes/Specials/SpecialWatchlistLabels.php` -> Churn: **70.34%** | Cog Load: 6.8602% | Debt: 91.2033%
- `includes/Specials/SpecialWatchlist.php` -> Churn: **63.46%** | Cog Load: 17.5287% | Debt: 87.267%
- `includes/Specials/Pager/EditWatchlistPager.php` -> Churn: **61.35%** | Cog Load: 31.0004% | Debt: 68.0313%
- `includes/Installer/PostgresUpdater.php` -> Churn: **60.95%** | Cog Load: 35.3089% | Debt: 78.4868%
- `includes/Watchlist/WatchlistLabelStore.php` -> Churn: **60.91%** | Cog Load: 17.4999% | Debt: 99.708%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `includes/Parser/Preprocessor_Hash.php` -> **Func** (100.0% isolated ownership) | Magnitude: 1022.17
- `includes/libs/ObjectCache/MediumSpecificBagOStuff.php` -> **Sam Reed** (100.0% isolated ownership) | Magnitude: 917.08
- `includes/Parser/BlockLevelPass.php` -> **Daimona Eaytoy** (100.0% isolated ownership) | Magnitude: 873.88
- `resources/src/mediawiki.widgets.datetime/DiscordianDateTimeFormatter.js` -> **Ed Sanders** (100.0% isolated ownership) | Magnitude: 835.9
- `resources/src/mediawiki.rcfilters/Controller.js` -> **Cormac Parle** (100.0% isolated ownership) | Magnitude: 795.64

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `includes/SpecialPage/SpecialPageFactory.php` -> **Severity: 0.807** (Bridge: 0.0113 * Flux: 71.2953%)
- `includes/MediaWikiServices.php` -> **Severity: 0.588** (Bridge: 0.0322 * Flux: 18.2498%)
- `includes/Page/WikiPage.php` -> **Severity: 0.434** (Bridge: 0.0043 * Flux: 100.0%)
- `includes/Status/Status.php` -> **Severity: 0.343** (Bridge: 0.0035 * Flux: 99.3259%)
- `includes/Revision/RevisionRecord.php` -> **Severity: 0.34** (Bridge: 0.0034 * Flux: 99.9999%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `includes/MediaWikiServices.php` -> **Severity: 2004.5** (Blast Radius: 20.045 * Doc Risk: 100.0%)
- `includes/libs/NonSerializable/NonSerializableTrait.php` -> **Severity: 601.516** (Blast Radius: 6.159 * Doc Risk: 97.6645%)
- `includes/libs/Rdbms/IDBAccessObject.php` -> **Severity: 321.5** (Blast Radius: 3.215 * Doc Risk: 100.0%)
- `includes/DAO/WikiAwareEntity.php` -> **Severity: 199.464** (Blast Radius: 15.212 * Doc Risk: 13.1123%)
- `includes/libs/LightweightObjectStore/ExpirationAwareness.php` -> **Severity: 192.4** (Blast Radius: 1.924 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
