# ARCHITECTURAL_BRIEF: mediawiki
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/mediawiki` |
| **Timestamp** | `2026-08-07T05:09:02.532625+00:00` |
| **Scan Duration** | `21.86s` |
| **Git Branch** | `master` |
| **Git Commit** | `8863834e673e4f297bfbc40cd4d54ee9027ad876` |
| **Git Remote** | `https://github.com/wikimedia/mediawiki.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 4471 malicious artifacts.

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
> **Architectural Drift Z-Score:** `5.772`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 4798 | 61.3% |
| file_cluster_13 | 2456 | 31.4% |
| file_cluster_9 | 82 | 1.0% |
| file_cluster_6 | 78 | 1.0% |
| file_cluster_4 | 46 | 0.6% |
| file_cluster_15 | 37 | 0.5% |
| file_cluster_0 | 23 | 0.3% |
| file_cluster_7 | 23 | 0.3% |
| file_cluster_17 | 20 | 0.3% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 13.6 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.8 | 36.2 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 32.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 9.9 | 2.3 | 2.3 |
| API Exposure | 0.0 | 14.5 | 2.0 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 1.9 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 41.2 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 91.7 | 0.3 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 83.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 3.8 | 0.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 6.3 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 23.0 | 17.9 | 0.0 |
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

- `getPermissionStatus` (@ `includes/Permissions/PermissionManager.php`) -> Impact: **953.2** | LOC: 1428
- `__construct` (@ `includes/EditPage/EditPage.php`) -> Impact: **802.1** | LOC: 1688
- `convertDateFormatToJs` (@ `includes/Language/Language.php`) -> Impact: **724.3** | LOC: 1561
- `importFormData` (@ `includes/EditPage/EditPage.php`) -> Impact: **701.9** | LOC: 1650
- `setPageTitle` (@ `includes/Output/OutputPage.php`) -> Impact: **544.6** | LOC: 1366
  * *Intent:* /**
- `parseInternal` (@ `includes/Output/OutputPage.php`) -> Impact: **471.8** | LOC: 781
  * *Intent:* /**
- `getMulti` (@ `includes/libs/ObjectCache/WANObjectCache.php`) -> Impact: **468.7** | LOC: 1056
- `newFromLinkTarget` (@ `includes/Title/Title.php`) -> Impact: **442.5** | LOC: 1402
  * *Intent:* /** * Text form including namespace/interwiki, initialised on demand
- `urlencode` (@ `includes/Parser/CoreParserFunctions.php`) -> Impact: **412.2** | LOC: 925
- `loadSlotContent` (@ `includes/Revision/RevisionStore.php`) -> Impact: **396.5** | LOC: 777
  * *Intent:* /** * @param IDatabase $dbw * @param RevisionRecord $rev * @param int $parentId * * @return array a revision table row * * @throws MWException * @thro...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `includes/Api` | 144 | 22589.34 | 38.87% | 68.88% |
| `tests/phpunit/integration/includes/Json` | 4 | 20000.0 | 0.0% | 0.0% |
| `maintenance` | 194 | 16707.8 | 37.12% | 43.41% |
| `includes/Specials` | 130 | 16516.78 | 24.7% | 66.67% |
| `languages/messages` | 517 | 12467.08 | 13.36% | 0.29% |
| `includes/Parser` | 44 | 11924.16 | 27.55% | 63.94% |
| `languages/i18n/datetime` | 578 | 9541.42 | 0.52% | 0.0% |
| `includes/Page` | 49 | 8808.14 | 23.24% | 48.41% |
| `includes/Language` | 32 | 8290.21 | 27.13% | 67.77% |
| `languages/i18n/preferences` | 366 | 6637.88 | 0.4% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `resources/src/mediawiki.DateFormatter/DateFormatter.js` -> **100.0%** Exposure
- `resources/src/mediawiki.Upload.js` -> **100.0%** Exposure
- `resources/src/mediawiki.action/mediawiki.action.protect.js` -> **100.0%** Exposure
- `resources/src/mediawiki.checkboxtoggle.js` -> **100.0%** Exposure
- `resources/src/mediawiki.confirmCloseWindow.js` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `maintenance/mediawiki.Title/generateJsToUpperCaseList.js` -> **100.0%** Exposure
- `resources/src/mediawiki.ForeignApi/mediawiki.ForeignApi.core.js` -> **100.0%** Exposure
- `resources/src/mediawiki.ForeignApi/mediawiki.ForeignRest.core.js` -> **100.0%** Exposure
- `resources/src/mediawiki.ForeignStructuredUpload.BookletLayout/BookletLayout.js` -> **100.0%** Exposure
- `resources/src/mediawiki.ForeignStructuredUpload.BookletLayout/ForeignStructuredUpload.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `includes/MediaWikiServices.php` -> **244** Orphaned Functions | **0** Duplicates
- `tests/phpunit/data/db/sqlite/tables-1.45.sql` -> **0** Orphaned Functions | **193** Duplicates
- `tests/phpunit/data/db/sqlite/tables-1.40.sql` -> **0** Orphaned Functions | **191** Duplicates
- `tests/phpunit/data/db/sqlite/tables-1.44.sql` -> **0** Orphaned Functions | **191** Duplicates
- `tests/phpunit/data/db/sqlite/tables-1.39.sql` -> **0** Orphaned Functions | **190** Duplicates

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
112. **`includes/SetupDynamicConfig.php`** -> AI Confidence: **99.39%**
113. **`includes/libs/Mime/XmlTypeCheck.php`** -> AI Confidence: **99.39%**
114. **`languages/messages/MessagesAf.php`** -> AI Confidence: **99.39%**
115. **`languages/messages/MessagesBe_tarask.php`** -> AI Confidence: **99.39%**
116. **`languages/messages/MessagesBg.php`** -> AI Confidence: **99.39%**
117. **`languages/messages/MessagesCy.php`** -> AI Confidence: **99.39%**
118. **`languages/messages/MessagesEl.php`** -> AI Confidence: **99.39%**
119. **`languages/messages/MessagesEn.php`** -> AI Confidence: **99.39%**
120. **`languages/messages/MessagesHe.php`** -> AI Confidence: **99.39%**
121. **`languages/messages/MessagesHy.php`** -> AI Confidence: **99.39%**
122. **`languages/messages/MessagesIs.php`** -> AI Confidence: **99.39%**
123. **`languages/messages/MessagesKk_arab.php`** -> AI Confidence: **99.39%**
124. **`languages/messages/MessagesKk_cyrl.php`** -> AI Confidence: **99.39%**
125. **`languages/messages/MessagesKk_latn.php`** -> AI Confidence: **99.39%**
126. **`languages/messages/MessagesKo.php`** -> AI Confidence: **99.39%**
127. **`languages/messages/MessagesLzh.php`** -> AI Confidence: **99.39%**
128. **`languages/messages/MessagesSr_ec.php`** -> AI Confidence: **99.39%**
129. **`languages/messages/MessagesSr_el.php`** -> AI Confidence: **99.39%**
130. **`languages/messages/MessagesZh_hans.php`** -> AI Confidence: **99.39%**
131. **`languages/messages/MessagesEn_gb.php`** -> AI Confidence: **99.34%**
132. **`languages/messages/MessagesHyw.php`** -> AI Confidence: **99.34%**
133. **`languages/messages/MessagesNan_latn_pehoeji.php`** -> AI Confidence: **99.34%**
134. **`languages/messages/MessagesVro.php`** -> AI Confidence: **99.34%**
135. **`includes/Languages/LanguageKk_cyrl.php`** -> AI Confidence: **99.32%**
136. **`includes/Languages/LanguageOs.php`** -> AI Confidence: **99.32%**
137. **`includes/Languages/LanguageTyv.php`** -> AI Confidence: **99.32%**
138. **`includes/Parser/BlockLevelPass.php`** -> AI Confidence: **99.32%**
139. **`includes/Parser/DateFormatter.php`** -> AI Confidence: **99.32%**
140. **`languages/messages/MessagesGot.php`** -> AI Confidence: **99.32%**
141. **`languages/messages/MessagesLfn.php`** -> AI Confidence: **99.32%**
142. **`resources/src/mediawiki.page.ready/ready.js`** -> AI Confidence: **99.31%**
143. **`includes/Actions/ActionEntryPoint.php`** -> AI Confidence: **99.31%**
144. **`includes/Actions/RawAction.php`** -> AI Confidence: **99.31%**
145. **`includes/Api/ApiComparePages.php`** -> AI Confidence: **99.31%**
146. **`includes/Api/ApiEditPage.php`** -> AI Confidence: **99.31%**
147. **`includes/Api/ApiErrorFormatter.php`** -> AI Confidence: **99.31%**
148. **`includes/Api/ApiExpandTemplates.php`** -> AI Confidence: **99.31%**
149. **`includes/Api/ApiLogin.php`** -> AI Confidence: **99.31%**
150. **`includes/Api/ApiMergeHistory.php`** -> AI Confidence: **99.31%**
151. **`includes/Api/ApiPageSet.php`** -> AI Confidence: **99.31%**
152. **`includes/Api/ApiParamInfo.php`** -> AI Confidence: **99.31%**
153. **`includes/Api/ApiQueryAllDeletedRevisions.php`** -> AI Confidence: **99.31%**
154. **`includes/Api/ApiQueryAllImages.php`** -> AI Confidence: **99.31%**
155. **`includes/Api/ApiQueryAllLinks.php`** -> AI Confidence: **99.31%**
156. **`includes/Api/ApiQueryAllMessages.php`** -> AI Confidence: **99.31%**
157. **`includes/Api/ApiQueryAllPages.php`** -> AI Confidence: **99.31%**
158. **`includes/Api/ApiQueryAllUsers.php`** -> AI Confidence: **99.31%**
159. **`includes/Api/ApiQueryBacklinks.php`** -> AI Confidence: **99.31%**
160. **`includes/Api/ApiQueryBacklinksprop.php`** -> AI Confidence: **99.31%**
161. **`includes/Api/ApiQueryBlocks.php`** -> AI Confidence: **99.31%**
162. **`includes/Api/ApiQueryCategoryMembers.php`** -> AI Confidence: **99.31%**
163. **`includes/Api/ApiQueryDeletedRevisions.php`** -> AI Confidence: **99.31%**
164. **`includes/Api/ApiQueryDeletedrevs.php`** -> AI Confidence: **99.31%**
165. **`includes/Api/ApiQueryFilearchive.php`** -> AI Confidence: **99.31%**
166. **`includes/Api/ApiQueryIWLinks.php`** -> AI Confidence: **99.31%**
167. **`includes/Api/ApiQueryImageInfo.php`** -> AI Confidence: **99.31%**
168. **`includes/Api/ApiQueryInfo.php`** -> AI Confidence: **99.31%**
169. **`includes/Api/ApiQueryLangLinks.php`** -> AI Confidence: **99.31%**
170. **`includes/Api/ApiQueryLanguageinfo.php`** -> AI Confidence: **99.31%**
171. **`includes/Api/ApiQueryLinks.php`** -> AI Confidence: **99.31%**
172. **`includes/Api/ApiQueryLogEvents.php`** -> AI Confidence: **99.31%**
173. **`includes/Api/ApiQueryRandom.php`** -> AI Confidence: **99.31%**
174. **`includes/Api/ApiQueryRecentChanges.php`** -> AI Confidence: **99.31%**
175. **`includes/Api/ApiQueryRevisions.php`** -> AI Confidence: **99.31%**
176. **`includes/Api/ApiQueryRevisionsBase.php`** -> AI Confidence: **99.31%**
177. **`includes/Api/ApiQuerySearch.php`** -> AI Confidence: **99.31%**
178. **`includes/Api/ApiQueryUserContribs.php`** -> AI Confidence: **99.31%**
179. **`includes/Api/ApiQueryUserInfo.php`** -> AI Confidence: **99.31%**
180. **`includes/Api/ApiQueryUsers.php`** -> AI Confidence: **99.31%**
181. **`includes/Api/ApiRevisionDelete.php`** -> AI Confidence: **99.31%**
182. **`includes/Api/ApiTag.php`** -> AI Confidence: **99.31%**
183. **`includes/Auth/AuthManager.php`** -> AI Confidence: **99.31%**
184. **`includes/Auth/AuthenticationRequest.php`** -> AI Confidence: **99.31%**
185. **`includes/Auth/Hook/AuthenticationAttemptThrottledHook.php`** -> AI Confidence: **99.31%**
186. **`includes/Auth/Throttler.php`** -> AI Confidence: **99.31%**
187. **`includes/Block/BlockUser.php`** -> AI Confidence: **99.31%**
188. **`includes/Cache/HTMLCacheUpdater.php`** -> AI Confidence: **99.31%**
189. **`includes/Category/CategoryViewer.php`** -> AI Confidence: **99.31%**
190. **`includes/Category/TrackingCategories.php`** -> AI Confidence: **99.31%**
191. **`includes/ChangeTags/ChangeTagsStore.php`** -> AI Confidence: **99.31%**
192. **`includes/CommentStore/CommentStore.php`** -> AI Confidence: **99.31%**
193. **`includes/Config/EtcdConfig.php`** -> AI Confidence: **99.31%**
194. **`includes/Content/Renderer/ContentRenderer.php`** -> AI Confidence: **99.31%**
195. **`includes/EditPage/EditPage.php`** -> AI Confidence: **99.31%**
196. **`includes/EditPage/IntroMessageBuilder.php`** -> AI Confidence: **99.31%**
197. **`includes/Exception/MWExceptionHandler.php`** -> AI Confidence: **99.31%**
198. **`includes/Export/WikiExporter.php`** -> AI Confidence: **99.31%**
199. **`includes/Export/XmlDumpWriter.php`** -> AI Confidence: **99.31%**
200. **`includes/FileRepo/AuthenticatedFileEntryPoint.php`** -> AI Confidence: **99.31%**
201. **`includes/FileRepo/File/LocalFile.php`** -> AI Confidence: **99.31%**
202. **`includes/FileRepo/File/LocalFileDeleteBatch.php`** -> AI Confidence: **99.31%**
203. **`includes/FileRepo/File/LocalFileRestoreBatch.php`** -> AI Confidence: **99.31%**
204. **`includes/FileRepo/File/MediaFileTrait.php`** -> AI Confidence: **99.31%**
205. **`includes/FileRepo/ThumbnailEntryPoint.php`** -> AI Confidence: **99.31%**
206. **`includes/GlobalFunctions.php`** -> AI Confidence: **99.31%**
207. **`includes/HTMLForm/Field/HTMLAutoCompleteSelectField.php`** -> AI Confidence: **99.31%**
208. **`includes/HTMLForm/Field/HTMLDateTimeField.php`** -> AI Confidence: **99.31%**
209. **`includes/HTMLForm/Field/HTMLFormFieldCloner.php`** -> AI Confidence: **99.31%**
210. **`includes/HTMLForm/Field/HTMLMultiSelectField.php`** -> AI Confidence: **99.31%**
211. **`includes/HTMLForm/Field/HTMLSelectLanguageField.php`** -> AI Confidence: **99.31%**
212. **`includes/HTMLForm/Field/HTMLSelectOrOtherField.php`** -> AI Confidence: **99.31%**
213. **`includes/HookContainer/DeprecatedHooks.php`** -> AI Confidence: **99.31%**
214. **`includes/Html/Html.php`** -> AI Confidence: **99.31%**
215. **`includes/Http/GuzzleHttpRequest.php`** -> AI Confidence: **99.31%**
216. **`includes/Http/HttpRequestFactory.php`** -> AI Confidence: **99.31%**
217. **`includes/Import/WikiImporter.php`** -> AI Confidence: **99.31%**
218. **`includes/Installer/CliInstaller.php`** -> AI Confidence: **99.31%**
219. **`includes/Installer/LocalSettingsGenerator.php`** -> AI Confidence: **99.31%**
220. **`includes/Installer/PostgresUpdater.php`** -> AI Confidence: **99.31%**
221. **`includes/Installer/WebInstallerName.php`** -> AI Confidence: **99.31%**
222. **`includes/Installer/WebInstallerOptions.php`** -> AI Confidence: **99.31%**
223. **`includes/Interwiki/ClassicInterwikiLookup.php`** -> AI Confidence: **99.31%**
224. **`includes/JobQueue/JobQueueGroup.php`** -> AI Confidence: **99.31%**
225. **`includes/JobQueue/JobRunner.php`** -> AI Confidence: **99.31%**
226. **`includes/Language/ConverterRule.php`** -> AI Confidence: **99.31%**
227. **`includes/Language/LCStoreStaticArray.php`** -> AI Confidence: **99.31%**
228. **`includes/Language/Language.php`** -> AI Confidence: **99.31%**
229. **`includes/Language/LanguageCode.php`** -> AI Confidence: **99.31%**
230. **`includes/Language/LanguageConverter.php`** -> AI Confidence: **99.31%**
231. **`includes/Language/LocalisationCache.php`** -> AI Confidence: **99.31%**
232. **`includes/Linker/Linker.php`** -> AI Confidence: **99.31%**
233. **`includes/Logging/BlockLogFormatter.php`** -> AI Confidence: **99.31%**
234. **`includes/Logging/LogEventsList.php`** -> AI Confidence: **99.31%**
235. **`includes/Logging/LogFormatter.php`** -> AI Confidence: **99.31%**
236. **`includes/Logging/Pager/LogPager.php`** -> AI Confidence: **99.31%**
237. **`includes/MainConfigSchema.php`** -> AI Confidence: **99.31%**
238. **`includes/Media/BitmapHandler.php`** -> AI Confidence: **99.31%**
239. **`includes/OutputTransform/Stages/HandleTOCMarkersDOM.php`** -> AI Confidence: **99.31%**
240. **`includes/Page/Article.php`** -> AI Confidence: **99.31%**
241. **`includes/Page/Event/PageRecordChangedEvent.php`** -> AI Confidence: **99.31%**
242. **`includes/Page/File/BadFileLookup.php`** -> AI Confidence: **99.31%**
243. **`includes/Page/File/FileDeleteForm.php`** -> AI Confidence: **99.31%**
244. **`includes/Page/ImageHistoryList.php`** -> AI Confidence: **99.31%**
245. **`includes/Page/ImageHistoryPseudoPager.php`** -> AI Confidence: **99.31%**
246. **`includes/Page/ImagePage.php`** -> AI Confidence: **99.31%**
247. **`includes/Page/ParserOutputAccess.php`** -> AI Confidence: **99.31%**
248. **`includes/Page/ProtectionForm.php`** -> AI Confidence: **99.31%**
249. **`includes/Pager/IndexPager.php`** -> AI Confidence: **99.31%**
250. **`includes/ParamValidator/TypeDef/UserDef.php`** -> AI Confidence: **99.31%**
251. **`includes/Parser/CoreParserFunctions.php`** -> AI Confidence: **99.31%**
252. **`includes/Parser/CoreTagHooks.php`** -> AI Confidence: **99.31%**
253. **`includes/Parser/ParserOutput.php`** -> AI Confidence: **99.31%**
254. **`includes/Parser/Parsoid/Config/DataAccess.php`** -> AI Confidence: **99.31%**
255. **`includes/Parser/Sanitizer.php`** -> AI Confidence: **99.31%**
256. **`includes/Password/UserPasswordPolicy.php`** -> AI Confidence: **99.31%**
257. **`includes/Permissions/PermissionManager.php`** -> AI Confidence: **99.31%**
258. **`includes/Permissions/RateLimiter.php`** -> AI Confidence: **99.31%**
259. **`includes/Preferences/DefaultPreferencesFactory.php`** -> AI Confidence: **99.31%**
260. **`includes/Profiler/ProfilerXhprof.php`** -> AI Confidence: **99.31%**
261. **`includes/RecentChanges/ChangesListBooleanFilter.php`** -> AI Confidence: **99.31%**
262. **`includes/RecentChanges/ChangesListQuery/WatchedCondition.php`** -> AI Confidence: **99.31%**
263. **`includes/RecentChanges/EnhancedChangesList.php`** -> AI Confidence: **99.31%**
264. **`includes/RecentChanges/RecentChangeMailComposer.php`** -> AI Confidence: **99.31%**
265. **`includes/RecentChanges/RecentChangeNotifier.php`** -> AI Confidence: **99.31%**
266. **`includes/Registration/ExtensionProcessor.php`** -> AI Confidence: **99.31%**
267. **`includes/RenameUser/Job/RenameUserTableJob.php`** -> AI Confidence: **99.31%**
268. **`includes/Request/ContentSecurityPolicy.php`** -> AI Confidence: **99.31%**
269. **`includes/Request/PathRouter.php`** -> AI Confidence: **99.31%**
270. **`includes/Request/WebRequest.php`** -> AI Confidence: **99.31%**
271. **`includes/ResourceLoader/FileModule.php`** -> AI Confidence: **99.31%**
272. **`includes/ResourceLoader/ForeignResourceManager.php`** -> AI Confidence: **99.31%**
273. **`includes/ResourceLoader/ResourceLoader.php`** -> AI Confidence: **99.31%**
274. **`includes/ResourceLoader/StartUpModule.php`** -> AI Confidence: **99.31%**
275. **`includes/Rest/ConditionalHeaderUtil.php`** -> AI Confidence: **99.31%**
276. **`includes/Revision/MainSlotRoleHandler.php`** -> AI Confidence: **99.31%**
277. **`includes/Search/PrefixSearch.php`** -> AI Confidence: **99.31%**
278. **`includes/Search/TitleMatcher.php`** -> AI Confidence: **99.31%**
279. **`includes/Session/SessionManager.php`** -> AI Confidence: **99.31%**
280. **`includes/Skin/Components/SkinComponentLink.php`** -> AI Confidence: **99.31%**
281. **`includes/Skin/Skin.php`** -> AI Confidence: **99.31%**
282. **`includes/Skin/SkinTemplate.php`** -> AI Confidence: **99.31%**
283. **`includes/SpecialPage/ContributionsSpecialPage.php`** -> AI Confidence: **99.31%**
284. **`includes/SpecialPage/LoginSignupSpecialPage.php`** -> AI Confidence: **99.31%**
285. **`includes/Specials/Forms/UploadForm.php`** -> AI Confidence: **99.31%**
286. **`includes/Specials/Pager/BlockListPager.php`** -> AI Confidence: **99.31%**
287. **`includes/Specials/Pager/ContribsPager.php`** -> AI Confidence: **99.31%**
288. **`includes/Specials/Pager/PagerTools.php`** -> AI Confidence: **99.31%**
289. **`includes/Specials/Pager/ProtectedPagesPager.php`** -> AI Confidence: **99.31%**
290. **`includes/Specials/Pager/UsersPager.php`** -> AI Confidence: **99.31%**
291. **`includes/Specials/SpecialAllPages.php`** -> AI Confidence: **99.31%**
292. **`includes/Specials/SpecialBlock.php`** -> AI Confidence: **99.31%**
293. **`includes/Specials/SpecialEditWatchlist.php`** -> AI Confidence: **99.31%**
294. **`includes/Specials/SpecialExport.php`** -> AI Confidence: **99.31%**
295. **`includes/Specials/SpecialImport.php`** -> AI Confidence: **99.31%**
296. **`includes/Specials/SpecialInterwiki.php`** -> AI Confidence: **99.31%**
297. **`includes/Specials/SpecialListGroupRights.php`** -> AI Confidence: **99.31%**
298. **`includes/Specials/SpecialMovePage.php`** -> AI Confidence: **99.31%**
299. **`includes/Specials/SpecialRecentChanges.php`** -> AI Confidence: **99.31%**
300. **`includes/Specials/SpecialRevisionDelete.php`** -> AI Confidence: **99.31%**
301. **`includes/Specials/SpecialTags.php`** -> AI Confidence: **99.31%**
302. **`includes/Specials/SpecialUnblock.php`** -> AI Confidence: **99.31%**
303. **`includes/Specials/SpecialUndelete.php`** -> AI Confidence: **99.31%**
304. **`includes/Specials/SpecialUpload.php`** -> AI Confidence: **99.31%**
305. **`includes/Specials/SpecialVersion.php`** -> AI Confidence: **99.31%**
306. **`includes/Tidy/RemexCompatFormatter.php`** -> AI Confidence: **99.31%**
307. **`includes/Title/TitleParser.php`** -> AI Confidence: **99.31%**
308. **`includes/Upload/UploadVerification.php`** -> AI Confidence: **99.31%**
309. **`includes/User/UserGroupAssignmentService.php`** -> AI Confidence: **99.31%**
310. **`includes/User/UserTimeCorrection.php`** -> AI Confidence: **99.31%**
311. **`includes/Utils/GitInfo.php`** -> AI Confidence: **99.31%**
312. **`includes/Utils/UrlUtils.php`** -> AI Confidence: **99.31%**
313. **`includes/Watchlist/WatchedItemQueryService.php`** -> AI Confidence: **99.31%**
314. **`includes/WebStart.php`** -> AI Confidence: **99.31%**
315. **`includes/libs/FileBackend/FSFileBackend.php`** -> AI Confidence: **99.31%**
316. **`includes/libs/FileBackend/FileBackendStore.php`** -> AI Confidence: **99.31%**
317. **`includes/libs/FileBackend/SwiftFileBackend.php`** -> AI Confidence: **99.31%**
318. **`includes/libs/Http/HttpStatus.php`** -> AI Confidence: **99.31%**
319. **`includes/libs/Http/MultiHttpClient.php`** -> AI Confidence: **99.31%**
320. **`includes/libs/Leximorph/Provider/TextDirection.php`** -> AI Confidence: **99.31%**
321. **`includes/libs/LockManager/MemcLockManager.php`** -> AI Confidence: **99.31%**
322. **`includes/libs/ObjectCache/MediumSpecificBagOStuff.php`** -> AI Confidence: **99.31%**
323. **`includes/libs/ObjectCache/RESTBagOStuff.php`** -> AI Confidence: **99.31%**
324. **`includes/libs/ObjectCache/RedisBagOStuff.php`** -> AI Confidence: **99.31%**
325. **`includes/libs/ObjectCache/WANObjectCache.php`** -> AI Confidence: **99.31%**
326. **`includes/libs/ParamValidator/TypeDef/UploadDef.php`** -> AI Confidence: **99.31%**
327. **`includes/libs/Rdbms/ChronologyProtector.php`** -> AI Confidence: **99.31%**
328. **`includes/libs/Rdbms/Database/DatabaseFactory.php`** -> AI Confidence: **99.31%**
329. **`includes/libs/Rdbms/LBFactory/LBFactoryMulti.php`** -> AI Confidence: **99.31%**
330. **`includes/libs/Rdbms/LoadBalancer/LoadBalancer.php`** -> AI Confidence: **99.31%**
331. **`includes/libs/Rdbms/LoadMonitor/LoadMonitor.php`** -> AI Confidence: **99.31%**
332. **`includes/libs/Rdbms/Platform/SQLPlatform.php`** -> AI Confidence: **99.31%**
333. **`includes/libs/Rdbms/TransactionProfiler.php`** -> AI Confidence: **99.31%**
334. **`includes/libs/XhprofData.php`** -> AI Confidence: **99.31%**
335. **`languages/messages/MessagesAn.php`** -> AI Confidence: **99.31%**
336. **`languages/messages/MessagesArc.php`** -> AI Confidence: **99.31%**
337. **`languages/messages/MessagesAst.php`** -> AI Confidence: **99.31%**
338. **`languages/messages/MessagesBcl.php`** -> AI Confidence: **99.31%**
339. **`languages/messages/MessagesBlk.php`** -> AI Confidence: **99.31%**
340. **`languages/messages/MessagesBs.php`** -> AI Confidence: **99.31%**
341. **`languages/messages/MessagesCe.php`** -> AI Confidence: **99.31%**
342. **`languages/messages/MessagesCs.php`** -> AI Confidence: **99.31%**
343. **`languages/messages/MessagesDe.php`** -> AI Confidence: **99.31%**
344. **`languages/messages/MessagesEo.php`** -> AI Confidence: **99.31%**
345. **`languages/messages/MessagesEs.php`** -> AI Confidence: **99.31%**
346. **`languages/messages/MessagesFa.php`** -> AI Confidence: **99.31%**
347. **`languages/messages/MessagesFr.php`** -> AI Confidence: **99.31%**
348. **`languages/messages/MessagesGa.php`** -> AI Confidence: **99.31%**
349. **`languages/messages/MessagesHaw.php`** -> AI Confidence: **99.31%**
350. **`languages/messages/MessagesHr.php`** -> AI Confidence: **99.31%**
351. **`languages/messages/MessagesHu.php`** -> AI Confidence: **99.31%**
352. **`languages/messages/MessagesJa.php`** -> AI Confidence: **99.31%**
353. **`languages/messages/MessagesKa.php`** -> AI Confidence: **99.31%**
354. **`languages/messages/MessagesKm.php`** -> AI Confidence: **99.31%**
355. **`languages/messages/MessagesLb.php`** -> AI Confidence: **99.31%**
356. **`languages/messages/MessagesMg.php`** -> AI Confidence: **99.31%**
357. **`languages/messages/MessagesMk.php`** -> AI Confidence: **99.31%**
358. **`languages/messages/MessagesMr.php`** -> AI Confidence: **99.31%**
359. **`languages/messages/MessagesMs.php`** -> AI Confidence: **99.31%**
360. **`languages/messages/MessagesMt.php`** -> AI Confidence: **99.31%**
361. **`languages/messages/MessagesMyv.php`** -> AI Confidence: **99.31%**
362. **`languages/messages/MessagesMzn.php`** -> AI Confidence: **99.31%**
363. **`languages/messages/MessagesNds.php`** -> AI Confidence: **99.31%**
364. **`languages/messages/MessagesNds_nl.php`** -> AI Confidence: **99.31%**
365. **`languages/messages/MessagesNl.php`** -> AI Confidence: **99.31%**
366. **`languages/messages/MessagesOc.php`** -> AI Confidence: **99.31%**
367. **`languages/messages/MessagesOr.php`** -> AI Confidence: **99.31%**
368. **`languages/messages/MessagesPl.php`** -> AI Confidence: **99.31%**
369. **`languages/messages/MessagesPs.php`** -> AI Confidence: **99.31%**
370. **`languages/messages/MessagesPt.php`** -> AI Confidence: **99.31%**
371. **`languages/messages/MessagesPt_br.php`** -> AI Confidence: **99.31%**
372. **`languages/messages/MessagesQu.php`** -> AI Confidence: **99.31%**
373. **`languages/messages/MessagesRo.php`** -> AI Confidence: **99.31%**
374. **`languages/messages/MessagesSa.php`** -> AI Confidence: **99.31%**
375. **`languages/messages/MessagesSd.php`** -> AI Confidence: **99.31%**
376. **`languages/messages/MessagesSh_latn.php`** -> AI Confidence: **99.31%**
377. **`languages/messages/MessagesSi.php`** -> AI Confidence: **99.31%**
378. **`languages/messages/MessagesSq.php`** -> AI Confidence: **99.31%**
379. **`languages/messages/MessagesSrn.php`** -> AI Confidence: **99.31%**
380. **`languages/messages/MessagesSv.php`** -> AI Confidence: **99.31%**
381. **`languages/messages/MessagesTly.php`** -> AI Confidence: **99.31%**
382. **`languages/messages/MessagesTt_cyrl.php`** -> AI Confidence: **99.31%**
383. **`languages/messages/MessagesTt_latn.php`** -> AI Confidence: **99.31%**
384. **`languages/messages/MessagesUr.php`** -> AI Confidence: **99.31%**
385. **`languages/messages/MessagesUz.php`** -> AI Confidence: **99.31%**
386. **`languages/messages/MessagesVi.php`** -> AI Confidence: **99.31%**
387. **`languages/messages/MessagesYi.php`** -> AI Confidence: **99.31%**
388. **`languages/messages/MessagesZh.php`** -> AI Confidence: **99.31%**
389. **`languages/messages/MessagesZh_hant.php`** -> AI Confidence: **99.31%**
390. **`maintenance/Maintenance.php`** -> AI Confidence: **99.31%**
391. **`maintenance/cleanupImages.php`** -> AI Confidence: **99.31%**
392. **`maintenance/cleanupInvalidDbKeys.php`** -> AI Confidence: **99.31%**
393. **`maintenance/cleanupUploadStash.php`** -> AI Confidence: **99.31%**
394. **`maintenance/convertExtensionToRegistration.php`** -> AI Confidence: **99.31%**
395. **`maintenance/createAndPromote.php`** -> AI Confidence: **99.31%**
396. **`maintenance/deleteEqualMessages.php`** -> AI Confidence: **99.31%**
397. **`maintenance/dumpBackup.php`** -> AI Confidence: **99.31%**
398. **`maintenance/dumpUploads.php`** -> AI Confidence: **99.31%**
399. **`maintenance/eval.php`** -> AI Confidence: **99.31%**
400. **`maintenance/extractClaimsFromJwt.php`** -> AI Confidence: **99.31%**
401. **`maintenance/findBadBlobs.php`** -> AI Confidence: **99.31%**
402. **`maintenance/findMissingActors.php`** -> AI Confidence: **99.31%**
403. **`maintenance/findMissingFiles.php`** -> AI Confidence: **99.31%**
404. **`maintenance/generateConfigSchema.php`** -> AI Confidence: **99.31%**
405. **`maintenance/generateJsonI18n.php`** -> AI Confidence: **99.31%**
406. **`maintenance/generateJwt.php`** -> AI Confidence: **99.31%**
407. **`maintenance/getConfiguration.php`** -> AI Confidence: **99.31%**
408. **`maintenance/grep.php`** -> AI Confidence: **99.31%**
409. **`maintenance/importDump.php`** -> AI Confidence: **99.31%**
410. **`maintenance/importTextFiles.php`** -> AI Confidence: **99.31%**
411. **`maintenance/includes/MaintenanceParameters.php`** -> AI Confidence: **99.31%**
412. **`maintenance/includes/TextPassDumper.php`** -> AI Confidence: **99.31%**
413. **`maintenance/install.php`** -> AI Confidence: **99.31%**
414. **`maintenance/language/generateNormalizerDataAr.php`** -> AI Confidence: **99.31%**
415. **`maintenance/mwdoc-filter.php`** -> AI Confidence: **99.31%**
416. **`maintenance/mysql.php`** -> AI Confidence: **99.31%**
417. **`maintenance/purgeParserCache.php`** -> AI Confidence: **99.31%**
418. **`maintenance/rebuildLocalisationCache.php`** -> AI Confidence: **99.31%**
419. **`maintenance/rebuildrecentchanges.php`** -> AI Confidence: **99.31%**
420. **`maintenance/recountCategories.php`** -> AI Confidence: **99.31%**
421. **`maintenance/refreshImageMetadata.php`** -> AI Confidence: **99.31%**
422. **`maintenance/removeUnusedAccounts.php`** -> AI Confidence: **99.31%**
423. **`maintenance/renameUsersMatchingPattern.php`** -> AI Confidence: **99.31%**
424. **`maintenance/resetAuthenticationThrottle.php`** -> AI Confidence: **99.31%**
425. **`maintenance/storage/compressOld.php`** -> AI Confidence: **99.31%**
426. **`maintenance/storage/moveToExternal.php`** -> AI Confidence: **99.31%**
427. **`maintenance/storage/recompressTracked.php`** -> AI Confidence: **99.31%**
428. **`maintenance/storage/trackBlobs.php`** -> AI Confidence: **99.31%**
429. **`maintenance/update.php`** -> AI Confidence: **99.31%**
430. **`maintenance/updateCollation.php`** -> AI Confidence: **99.31%**
431. **`maintenance/updateExtensionJsonSchema.php`** -> AI Confidence: **99.31%**
432. **`maintenance/userOptions.php`** -> AI Confidence: **99.31%**
433. **`maintenance/wrapOldPasswords.php`** -> AI Confidence: **99.31%**
434. **`tests/parser/editTests.php`** -> AI Confidence: **99.31%**
435. **`tests/parser/parserTests.php`** -> AI Confidence: **99.31%**
436. **`tests/phpunit/bootstrap.php`** -> AI Confidence: **99.31%**
437. **`tests/phpunit/suites/ParserTestTopLevelSuite.php`** -> AI Confidence: **99.31%**
438. **`Gruntfile.js`** -> AI Confidence: **99.29%**
439. **`resources/lib/jquery.i18n/src/languages/bs.js`** -> AI Confidence: **99.29%**
440. **`resources/lib/jquery.i18n/src/languages/dsb.js`** -> AI Confidence: **99.29%**
441. **`resources/lib/jquery.i18n/src/languages/fi.js`** -> AI Confidence: **99.29%**
442. **`resources/lib/jquery.i18n/src/languages/ga.js`** -> AI Confidence: **99.29%**
443. **`resources/lib/jquery.i18n/src/languages/he.js`** -> AI Confidence: **99.29%**
444. **`resources/lib/jquery.i18n/src/languages/hsb.js`** -> AI Confidence: **99.29%**
445. **`resources/lib/jquery.i18n/src/languages/hu.js`** -> AI Confidence: **99.29%**
446. **`resources/lib/jquery.i18n/src/languages/hy.js`** -> AI Confidence: **99.29%**
447. **`resources/lib/jquery.i18n/src/languages/la.js`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `24` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `82895` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `includes/Deferred/LinksUpdate/CategoryLinksTable.php` (PHP) -> Cumulative Risk: **654.48**
- **Archetype:** `file_cluster_13` (Distance: 12.694 IQR)
- **Magnitude:** 192.92 | **LOC:** 400 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Tech Debt (99.3467%), Concurrency (98.7797%)
- **Heaviest Functions:** `setParserOutput` (Impact: 13.8), `deduplicateLinkIds` (Impact: 7.2), `fetchExistingLinks` (Impact: 5.7)

### 2. `resources/src/mediawiki.widgets/MediaSearch/mw.widgets.APIResultsQueue.js` (JAVASCRIPT) -> Cumulative Risk: **641.53**
- **Archetype:** `file_cluster_15` (Distance: 15.619 IQR)
- **Magnitude:** 264.28 | **LOC:** 242 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9998%), Tech Debt (99.8688%)
- **Heaviest Functions:** `queryProviders` (Impact: 10.0), `setParams` (Impact: 9.7), `get` (Impact: 7.7)

### 3. `maintenance/language/StatOutputs.php` (PHP) -> Cumulative Risk: **638.33**
- **Archetype:** `file_cluster_8` (Distance: 13.305 IQR)
- **Magnitude:** 126.88 | **LOC:** 148 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `formatPercent` (Impact: 14.9), `heading` (Impact: 9.7), `element` (Impact: 3.6)

### 4. `resources/src/mediawiki.widgets/mw.widgets.DateInputWidget.js` (JAVASCRIPT) -> Cumulative Risk: **636.61**
- **Archetype:** `file_cluster_15` (Distance: 14.831 IQR)
- **Magnitude:** 297.02 | **LOC:** 710 | **CtrlFlow:** 62.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.8855%), Concurrency (98.3194%)
- **Heaviest Functions:** `getDisplayFormat` (Impact: 25.7), `setValidityFlag` (Impact: 12.2), `onTextInputChange` (Impact: 11.7)

### 5. `maintenance/rebuildLocalisationCache.php` (PHP) -> Cumulative Risk: **634.66**
- **Archetype:** `file_cluster_13` (Distance: 12.195 IQR)
- **Magnitude:** 271.98 | **LOC:** 277 | **CtrlFlow:** 56.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (98.0981%), Safety Score (92.4971%)
- **Heaviest Functions:** `finalSetup` (Impact: 122.4), `__construct` (Impact: 7.1)

### 6. `includes/Language/TrivialLanguageConverter.php` (PHP) -> Cumulative Risk: **633.1**
- **Archetype:** `file_cluster_13` (Distance: 13.358 IQR)
- **Magnitude:** 151.72 | **LOC:** 209 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `validateVariant` (Impact: 8.3), `convertSplitTitle` (Impact: 7.5), `__construct` (Impact: 5.5)

### 7. `includes/Language/Converters/MniConverter.php` (PHP) -> Cumulative Risk: **632.75**
- **Archetype:** `file_cluster_4` (Distance: 10.97 IQR)
- **Magnitude:** 217.22 | **LOC:** 288 | **CtrlFlow:** 49.3% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9999%), State Flux (99.838%), Verification (80.0%)
- **Heaviest Functions:** `mteiToBengali` (Impact: 74.2), `isEndOfWord` (Impact: 5.2), `transliterate` (Impact: 5.2)

### 8. `resources/src/mediawiki.notification/notification.js` (JAVASCRIPT) -> Cumulative Risk: **631.25**
- **Archetype:** `file_cluster_8` (Distance: 12.124 IQR)
- **Magnitude:** 188.9 | **LOC:** 587 | **CtrlFlow:** 69.8% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9989%), State Flux (99.9824%), Concurrency (83.7298%)
- **Heaviest Functions:** `Notification` (Impact: 34.1), `start` (Impact: 17.0), `announceToAriaLive` (Impact: 16.1)

### 9. `includes/Deferred/LinksUpdate/ExternalLinksTable.php` (PHP) -> Cumulative Risk: **631.18**
- **Archetype:** `file_cluster_4` (Distance: 12.797 IQR)
- **Magnitude:** 101.98 | **LOC:** 138 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9997%), Tech Debt (99.999%), Concurrency (99.8616%)
- **Heaviest Functions:** `setParserOutput` (Impact: 7.7), `getExistingLinks` (Impact: 7.4), `getNewLinkIDs` (Impact: 5.5)

### 10. `includes/Rest/StringStream.php` (PHP) -> Cumulative Risk: **630.68**
- **Archetype:** `file_cluster_13` (Distance: 12.951 IQR)
- **Magnitude:** 149.68 | **LOC:** 159 | **CtrlFlow:** 38.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9995%)
- **Heaviest Functions:** `seek` (Impact: 22.0), `read` (Impact: 12.8), `write` (Impact: 7.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `tests/phpunit/integration/includes/Json/key1.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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
- **Global Archetype:** `file_cluster_13` (Drift: 14.733 IQR)
- **Top Global Matches:** file_cluster_13: 14.733, file_cluster_8: 14.954, file_cluster_7: 15.003
- **Magnitude:** 4037.44 | **LOC:** 5079 | **CtrlFlow:** 49.3% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (46.1974%), Tech Debt (44.2753%)
**Top Internal Functions/Classes:**
  * `convertDateFormatToJs` (Impact: 724.3)
  * `truncateInternal` (Impact: 202.4)
  * `formatNumInternal` (Impact: 76.8)
  * `formatTimePeriod` (Impact: 47.9)
    * *Intent:* /** * A hidden direction mark (LRM or RLM), depending on the language direction. * Unlike getDirMark...
  * `tsToHebrew` (Impact: 43.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 723`, `structural_boundaries: 744`, `args: 158`, `func_start: 153`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 384`, `high_risk_execution: 2`, `state_mutation: 1997`, `dead_code: 6`, `planned_debt: 8`, `fragile_debt: 4`, `orphaned_logic: 40`
* *Architecture:* `io: 1`, `api: 137`, `import: 91`
* *Defense:* `safety: 45`, `doc: 559`, `test: 41`, `immutability_locks: 20`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.405
  * `Choke Point (Betweenness):` 0.002091 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 20):` MediaWiki\MainConfigNames, MediaWiki\Html\Html, MediaWiki\User\UserTimeCorrection, MediaWiki\Config\Config, 
	public function getBlockDurations( $includeOther = true ): array 
		$msg = $this->msg( 'ipboptions' )->text(, NumberFormatter, string> List of localized namespace names, DateTimeZone...
  * `Imported By (In-Degree: 156):` (Excluded from Brief to save tokens)

### `includes/Output/OutputPage.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.462 IQR)
- **Top Global Matches:** file_cluster_13: 13.462, file_cluster_8: 13.538, file_cluster_7: 13.655
- **Magnitude:** 3492.86 | **LOC:** 5226 | **CtrlFlow:** 44.6% | **Authorship Centralization:** 7.7%
- **Risk Profile:** Cognitive Load (33.9152%), Tech Debt (57.1694%)
**Top Internal Functions/Classes:**
  * `setPageTitle` (Impact: 544.6)
    * *Intent:* /**
  * `parseInternal` (Impact: 471.8)
    * *Intent:* /**
  * `addParserOutput` (Impact: 357.6)
    * *Intent:* /** * Add or replace a head item to the output * * Whenever possible, use more specific options like...
  * `parserOptions` (Impact: 350.4)
  * `sendCacheControl` (Impact: 278.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 226`, `structural_boundaries: 281`, `args: 96`, `func_start: 91`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 303`, `high_risk_execution: 1`, `state_mutation: 669`, `dead_code: 3`, `planned_debt: 4`, `fragile_debt: 5`, `orphaned_logic: 37`
* *Architecture:* `io: 21`, `api: 84`, `import: 66`
* *Defense:* `safety: 31`, `doc: 300`, `test: 9`, `immutability_locks: 7`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.12
  * `Choke Point (Betweenness):` 0.001909 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 42):` redirect URLs to be absolute, MediaWiki\Skin\QuickTemplate, '1.44', MediaWiki\Debug\DeprecationHelper, waiting for
	 * HTTP caches to expire before configuration changes take effect everywhere.
	 *
	 * By default,  2. Dynamically-loaded styles, Wikimedia\Message\MessageParam, $query )...
  * `Imported By (In-Degree: 77):` (Excluded from Brief to save tokens)

### `includes/Title/Title.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.498 IQR)
- **Top Global Matches:** file_cluster_13: 14.498, file_cluster_8: 14.864, file_cluster_7: 14.882
- **Magnitude:** 3445.94 | **LOC:** 3898 | **CtrlFlow:** 41.8% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (45.6938%), Tech Debt (12.0233%)
**Top Internal Functions/Classes:**
  * `newFromLinkTarget` (Impact: 442.5)
    * *Intent:* /** * Text form including namespace/interwiki, initialised on demand
  * `getLocalURL` (Impact: 365.3)
  * `getNsText` (Impact: 311.5)
    * *Intent:* /** * Create a new Title from an article ID * * @param int $id The page_id corresponding to the Titl...
  * `canExist` (Impact: 304.0)
  * `isMovable` (Impact: 295.7)
    * *Intent:* /** * Load Title object fields from a DB row.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 218`, `structural_boundaries: 304`, `args: 86`, `func_start: 85`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 880`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 3`
* *Architecture:* `api: 118`, `import: 54`
* *Defense:* `safety: 27`, `doc: 246`, `test: 11`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 36):` MediaWiki\MainConfigNames, MediaWiki\Html\Html, Stringable, we just return a link
	 * to the fragment.
	 *
	 * The result obviously should not be URL-escaped, MediaWiki\Linker\LinkTarget, Wikimedia\Assert\Assert, Wikimedia\Parsoid\Core\LinkTargetTrait, MediaWiki\Language\ILanguageConverter...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `includes/EditPage/EditPage.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.486 IQR)
- **Top Global Matches:** file_cluster_13: 14.486, file_cluster_8: 14.82, file_cluster_7: 14.898
- **Magnitude:** 3284.72 | **LOC:** 4507 | **CtrlFlow:** 54.1% | **Authorship Centralization:** 47.2%
- **Risk Profile:** Cognitive Load (45.5557%), Tech Debt (12.2413%)
**Top Internal Functions/Classes:**
  * `__construct` (Impact: 802.1)
  * `importFormData` (Impact: 701.9)
  * `doPostEditRedirect` (Impact: 106.2)
    * *Intent:* // If raw HTML is enabled, disable preview on open // since it has to be posted with a token for
  * `getContentObject` (Impact: 72.5)
  * `handleFailedConstraint` (Impact: 63.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 347`, `structural_boundaries: 294`, `args: 48`, `func_start: 48`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 1110`, `dead_code: 5`, `planned_debt: 4`, `fragile_debt: 5`
* *Architecture:* `io: 3`, `api: 55`, `import: 105`
* *Defense:* `safety: 40`, `doc: 241`, `test: 6`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.938
  * `Choke Point (Betweenness):` 0.000965 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 87):`  TODO: Remove the suppressIntro feature from EditPage, MediaWiki\Actions\WatchAction, MediaWiki\EditPage\Constraint\ChangeTagsConstraint, MediaWiki\Debug\DeprecationHelper, MediaWiki\EditPage\Constraint\EditConstraintFactory, # headline would need to be parsed to improve this.
				if ( $hasmatch && $matches[2] !== '' ) 
					$sectionAnchor = $this->pageEditingHelper->guessSectionName( $matches[2], ] : [], 'accesskey-foo'
	 *  - 'label-id' (optional): 'id' attribute for the `<label>`
	 *  - 'legacy-name' (optional): short name for backwards-compatibility
	 *  - 'class' (optional): PHP class name of the OOUI widget to use. Defaults to
	 *    CheckboxInputWidget.
	 *  - 'options' (optional): options to use for DropdownInputWidget...
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `includes/Parser/CoreParserFunctions.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.229 IQR)
- **Top Global Matches:** file_cluster_13: 15.229, file_cluster_11: 15.496, file_cluster_0: 15.546
- **Magnitude:** 2923.74 | **LOC:** 2116 | **CtrlFlow:** 47.4% | **Authorship Centralization:** 30.0%
- **Risk Profile:** Cognitive Load (46.323%), Tech Debt (12.0587%)
**Top Internal Functions/Classes:**
  * `urlencode` (Impact: 412.2)
  * `displaytitle` (Impact: 349.9)
    * *Intent:* /** * @param Parser $parser * @param string $s
  * `getLegacyFormatNum` (Impact: 327.1)
  * `pagesize` (Impact: 255.2)
  * `tagObj` (Impact: 153.9)
    * *Intent:* /** * Helper function for preprocessing an optional argument which represents * a title. * @param Pa...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 201`, `structural_boundaries: 223`, `args: 62`, `func_start: 59`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 853`, `dead_code: 7`, `fragile_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 57`, `import: 21`
* *Defense:* `safety: 14`, `doc: 262`, `test: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` MediaWiki\MainConfigNames, MediaWiki\Language\LanguageCode, MediaWiki\Language\LanguageNameUtils, MediaWiki\Title\Title, Wikimedia\Timestamp\TimestampFormat, MediaWiki\Revision\RevisionRecord, MediaWiki\Category\Category, Wikimedia\RemexHtml\Tokenizer\PlainAttributes...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `includes/Revision/RevisionStore.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.189 IQR)
- **Top Global Matches:** file_cluster_13: 14.189, file_cluster_8: 14.518, file_cluster_11: 14.574
- **Magnitude:** 2076.92 | **LOC:** 3443 | **CtrlFlow:** 45.0% | **Authorship Centralization:** 30.0%
- **Risk Profile:** Cognitive Load (44.3583%), Tech Debt (13.3817%)
**Top Internal Functions/Classes:**
  * `loadSlotContent` (Impact: 396.5)
    * *Intent:* /** * @param IDatabase $dbw * @param RevisionRecord $rev * @param int $parentId * * @return array a ...
  * `getRevisionByTitle` (Impact: 297.6)
  * `getRevisionByPageId` (Impact: 283.6)
  * `ensureRevisionRowMatchesPage` (Impact: 122.0)
  * `newRevisionFromRowAndSlots` (Impact: 76.4)
    * *Intent:* /** * Loads a Content object based on a slot row. *
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 184`, `structural_boundaries: 225`, `args: 43`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 502`, `dead_code: 2`, `planned_debt: 8`, `fragile_debt: 2`
* *Architecture:* `api: 32`, `import: 62`
* *Defense:* `safety: 70`, `doc: 186`, `sync_locks: 3`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.628
  * `Choke Point (Betweenness):` 0.000556 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 41):` RevisionRecord::DELETED_TEXT ) . " = 0", last revision, 'fields' => [
				'slot_revision_id', 
	public function getRevisionById( $id, 'joins'  => [], MediaWiki\RecentChanges\RecentChangeLookup, 'rev_minor_edit', if isOK() returns true...
  * `Imported By (In-Degree: 51):` (Excluded from Brief to save tokens)

### `includes/Page/WikiPage.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.942 IQR)
- **Top Global Matches:** file_cluster_13: 13.942, file_cluster_8: 14.294, file_cluster_7: 14.333
- **Magnitude:** 1889.52 | **LOC:** 2985 | **CtrlFlow:** 43.1% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (45.077%), Tech Debt (15.8766%)
**Top Internal Functions/Classes:**
  * `getContentModel` (Impact: 336.2)
  * `replaceSectionContent` (Impact: 309.9)
    * *Intent:* /** * Tests if the page is new (only has one revision).
  * `doEditUpdates` (Impact: 220.2)
  * `replaceSectionAtRev` (Impact: 26.4)
    * *Intent:* /** * Returns the page's content model id (see the CONTENT_MODEL_XXX constants).
  * `doUserEditContent` (Impact: 25.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 168`, `structural_boundaries: 222`, `args: 58`, `func_start: 54`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 585`, `dead_code: 2`, `planned_debt: 14`, `fragile_debt: 1`
* *Architecture:* `api: 72`, `import: 64`
* *Defense:* `safety: 4`, `doc: 200`, `test: 2`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.279
  * `Choke Point (Betweenness):` 0.004338 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 49):` MediaWiki\User\UserArrayFromResult, Stringable, s
	 * secondary data updates). This method is provided for partial purges.
	 *
	 * @note This does not update the parser cache. Use updateParserCache() for that.
	 *
	 * @param array $options
	 *   - recursive (bool, 
	public function getCategories() 
		$services = MediaWikiServices::getInstance(, Wikimedia\Rdbms\IReadableDatabase, MediaWiki\Context\IContextSource, MediaWiki\Title\Title, MediaWiki\Content\Content...
  * `Imported By (In-Degree: 62):` (Excluded from Brief to save tokens)

### `includes/Skin/Skin.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.064 IQR)
- **Top Global Matches:** file_cluster_13: 14.064, file_cluster_8: 14.256, file_cluster_7: 14.353
- **Magnitude:** 1773.12 | **LOC:** 2584 | **CtrlFlow:** 50.3% | **Authorship Centralization:** 18.2%
- **Risk Profile:** Cognitive Load (45.6116%), Tech Debt (9.6571%)
**Top Internal Functions/Classes:**
  * `getUndeleteLink` (Impact: 280.7)
  * `getLanguages` (Impact: 226.8)
  * `getPersonalToolsForMakeListItem` (Impact: 65.6)
  * `getDefaultModules` (Impact: 42.2)
    * *Intent:* // Don't return the default immediately; // in a misconfiguration we need to fall back.
  * `makeToolbox` (Impact: 30.2)
    * *Intent:* /** * If url string starts with http, consider as external URL, else * internal * @param string $nam...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 223`, `structural_boundaries: 220`, `args: 54`, `func_start: 53`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 703`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `api: 66`, `import: 36`
* *Defense:* `safety: 26`, `doc: 161`, `test: 4`, `immutability_locks: 14`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.155
  * `Choke Point (Betweenness):` 0.001088 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 26):` $options = [] ) 
		$component = new SkinComponentListItem(
			$key, MediaWiki\MainConfigNames, MediaWiki\Html\Html, the sidebar), MediaWiki\Skin\Components\SkinComponentFooter, MediaWiki\ResourceLoader, MediaWiki\Output\OutputPage, *     set this to `false`.
	 *
	 *     See ParserOutput::getText() for the implementation logic.
	 *
	 *     Default: `true`
	 *
	 *  - `bodyClasses`: An array of extra class names to add to the HTML `<body>` element.
	 *     Default: `[]`
	 *
	 *  - `clientPrefEnabled`: Enable support for mw.user.clientPrefs.
	 *     This instructs OutputPage and ResourceLoader\ClientHtml to include an inline script
	 *     in web responses for unregistered users to switch HTML classes...
  * `Imported By (In-Degree: 67):` (Excluded from Brief to save tokens)

### `tests/phpunit/MediaWikiIntegrationTestCase.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.55 IQR)
- **Top Global Matches:** file_cluster_13: 13.55, file_cluster_8: 13.702, file_cluster_7: 13.834
- **Magnitude:** 1767.76 | **LOC:** 2793 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 37.5%
- **Risk Profile:** Cognitive Load (14.264%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `installMockMwServices` (Impact: 49.5)
    * *Intent:* * If called with no parameters, this method restores all services to their default state. * This is ...
  * `stashMwGlobals` (Impact: 44.6)
    * *Intent:* /** * Overrides a set of config settings for the duration of the current test case. * The original v...
  * `mediaWikiTearDown` (Impact: 41.4)
  * `setUpSchema` (Impact: 34.7)
    * *Intent:* /** * @throws LogicException if the given database connection is not set-up to use * mock tables. * ...
  * `getExistingTestPage` (Impact: 31.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 408`, `structural_boundaries: 476`, `args: 110`, `func_start: 99`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 263`, `high_risk_execution: 3`, `state_mutation: 758`, `dead_code: 4`, `planned_debt: 13`, `fragile_debt: 2`
* *Architecture:* `api: 49`, `import: 73`
* *Defense:* `safety: 62`, `doc: 284`, `test: 129`, `immutability_locks: 9`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.462
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 42):` MediaWiki\Logger\LogCapturingSpi, $summary = '', the test must use @group Database', MediaWiki\Title\Title, MediaWiki\Content\Content, the test mut use @group Database.', which can be enabled with
	 * "@group Database".
	 *
	 * @param string|PageIdentity|LinkTarget|WikiPage $page the page to edit
	 * @param string|Content $content the new content of the page
	 * @param string $summary Optional summary string for the revision
	 * @param int $defaultNs Optional namespace id
	 * @param Authority|null $performer If null, s a named or temp account actor
		$context = new DerivativeContext( RequestContext::getMain()...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `includes/libs/ObjectCache/WANObjectCache.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.074 IQR)
- **Top Global Matches:** file_cluster_13: 15.074, file_cluster_8: 15.207, file_cluster_7: 15.222
- **Magnitude:** 1753.1 | **LOC:** 3089 | **CtrlFlow:** 58.9% | **Authorship Centralization:** 20.0%
- **Risk Profile:** Cognitive Load (46.2529%), Tech Debt (39.106%)
**Top Internal Functions/Classes:**
  * `getMulti` (Impact: 468.7)
  * `fetchOrRegenerate` (Impact: 136.0)
  * `setMainValue` (Impact: 126.5)
    * *Intent:* /** Key to the cache timestamp; stored in blobs */
  * `getMultiWithUnionSetCallback` (Impact: 33.8)
  * `getWithSetCallback` (Impact: 29.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 198`, `structural_boundaries: 138`, `args: 42`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 642`, `dead_code: 1`, `planned_debt: 1`, `orphaned_logic: 11`
* *Architecture:* `api: 35`, `import: 14`
* *Defense:* `safety: 50`, `doc: 263`, `test: 1`, `immutability_locks: 66`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.324
  * `Choke Point (Betweenness):` 0.000171 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` $opts, then solutions must be sought outside WANCache.
 *
 * Write operations like delete() and the "set" part of getWithSetCallback(), causing any get()
	 * after the reset to treat the key, $newTTLsById,  Map of cache keys to entity IDs
	 *         $cache->makeMultiKeys(
	 *             $this->fileVersionIds(), malformed
	 *   - WANObjectCache::KEY_VERSION: value version number, may return true, ArrayIterator...
  * `Imported By (In-Degree: 52):` (Excluded from Brief to save tokens)

### `includes/libs/Rdbms/Database/Database.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.364 IQR)
- **Top Global Matches:** file_cluster_13: 14.364, file_cluster_8: 14.495, file_cluster_7: 14.516
- **Magnitude:** 1729.74 | **LOC:** 3606 | **CtrlFlow:** 36.3% | **Authorship Centralization:** 20.0%
- **Risk Profile:** Cognitive Load (44.8684%), Tech Debt (95.6097%)
**Top Internal Functions/Classes:**
  * `cancelAtomic` (Impact: 122.5)
  * `__construct` (Impact: 61.8)
  * `upsert` (Impact: 33.6)
  * `executeQuery` (Impact: 28.9)
  * `startAtomic` (Impact: 25.6)
    * *Intent:* // Transaction automatically rolled back, breaking the expectations of callers
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 204`, `structural_boundaries: 358`, `args: 149`, `func_start: 145`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 683`, `dead_code: 3`, `planned_debt: 2`, `fragile_debt: 1`, `orphaned_logic: 46`
* *Architecture:* `api: 121`, `import: 19`
* *Defense:* `safety: 48`, `doc: 343`, `sync_locks: 5`, `immutability_locks: 31`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.342
  * `Choke Point (Betweenness):` 0.000281 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` ROLLBACK before allowing any other queries from outside callers
	 *         $this->completeCriticalSection( __METHOD__, Stringable, Wikimedia\RequestTimeout\CriticalSectionProvider,  master connection for writes to persistent tables.
			if ( $this->hasPermanentTable( $sql ) ) 
				$isPermWrite = true, Psr\Log\LoggerAwareInterface, $cs,  Temporary table creation is allowed
			return false, Wikimedia\ScopedCallback...
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `includes/Permissions/PermissionManager.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.291 IQR)
- **Top Global Matches:** file_cluster_13: 13.291, file_cluster_8: 13.389, file_cluster_7: 13.52
- **Magnitude:** 1537.96 | **LOC:** 1925 | **CtrlFlow:** 63.7% | **Authorship Centralization:** 42.9%
- **Risk Profile:** Cognitive Load (43.5094%), Tech Debt (24.96%)
**Top Internal Functions/Classes:**
  * `getPermissionStatus` (Impact: 953.2)
  * `__construct` (Impact: 5.7)
  * `overrideUserRightsForTesting` (Impact: 5.5)
  * `addTemporaryUserRights` (Impact: 3.9)
    * *Intent:* /**
  * `userCan` (Impact: 2.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 369`, `structural_boundaries: 210`, `args: 39`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 124`, `high_risk_execution: 3`, `state_mutation: 511`, `dead_code: 2`, `planned_debt: 11`, `fragile_debt: 4`, `orphaned_logic: 3`
* *Architecture:* `api: 22`, `import: 52`
* *Defense:* `safety: 18`, `doc: 177`, `test: 22`, `immutability_locks: 7`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.315
  * `Choke Point (Betweenness):` 0.00021 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 29):` rewrite sysop -> editprotected
					if ( $right === 'sysop' ) 
						$right = 'editprotected', MediaWiki\Context\IContextSource, MediaWiki\Title\Title, Wikimedia\ScopedCallback, MediaWiki\Title\NamespaceInfo, $this->options->get( MainConfigNames::AvailableRights )
				),  restriction level is not redundant if,  First...
  * `Imported By (In-Degree: 26):` (Excluded from Brief to save tokens)

### `includes/Auth/AuthManager.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.26 IQR)
- **Top Global Matches:** file_cluster_13: 13.26, file_cluster_8: 13.404, file_cluster_7: 13.614
- **Magnitude:** 1531.12 | **LOC:** 3021 | **CtrlFlow:** 56.0% | **Authorship Centralization:** 23.1%
- **Risk Profile:** Cognitive Load (34.5181%), Tech Debt (23.1578%)
**Top Internal Functions/Classes:**
  * `securitySensitiveOperationStatus` (Impact: 244.0)
  * `autoCreateUser` (Impact: 232.3)
  * `continueAuthentication` (Impact: 173.3)
    * *Intent:* /** * AuthManager is the authentication system in MediaWiki and serves entry point for authenticatio...
  * `continueAccountCreation` (Impact: 148.9)
    * *Intent:* // T390051: Don't use the $user provided to ::autoCreateUser for the "user being authenticated // ag...
  * `getAuthenticationRequests` (Impact: 44.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 249`, `structural_boundaries: 196`, `args: 25`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 450`, `dead_code: 2`, `fragile_debt: 2`, `orphaned_logic: 7`
* *Architecture:* `api: 16`, `import: 51`
* *Defense:* `safety: 27`, `doc: 89`, `test: 5`, `sync_locks: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.752
  * `Choke Point (Betweenness):` 0.000432 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 41):` MediaWiki\MainConfigNames, d === AuthenticationRequest::REQUIRED
					|| $reqs[$id]->required === AuthenticationRequest::OPTIONAL
				) 
					$reqs[$id] = $req, MediaWiki\Session\SessionManager, MediaWiki\Profiler\Profiler, $returnToUrl ) 
		$session = $this->request->getSession(, MediaWiki\Config\Config, 
	public function canAuthenticateNow() 
		return $this->request->getSession()->canSetUser(, MediaWiki\Exception\MWExceptionHandler...
  * `Imported By (In-Degree: 35):` (Excluded from Brief to save tokens)

### `resources/src/startup/mediawiki.loader.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.722 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.093 IQR)
- **Top Global Matches:** file_cluster_11: 14.722, file_cluster_17: 14.753, file_cluster_0: 14.78
- **Magnitude:** 1486.04 | **LOC:** 2147 | **CtrlFlow:** 56.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.2413%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `resolveStubbornly` (Impact: 253.7)
    * *Intent:* // Make sure the next call to addEmbeddedCSS() starts a new buffer. // This must be done before we r...
  * `sortDependencies` (Impact: 163.6)
  * `makeRequireFunction` (Impact: 140.6)
  * `require` (Impact: 126.7)
  * `doPropagation` (Impact: 43.3)
    * *Intent:* * - store-eval: could not evaluate module code cached in localStorage * - store-localstorage-json: J...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 107`, `args: 49`, `func_start: 78`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 332`, `dead_code: 5`, `planned_debt: 2`, `duplicate_logic: 27`, `orphaned_logic: 8`
* *Architecture:* `io: 1`, `api: 1`, `concurrency: 1`, `import: 1`
* *Defense:* `safety: 50`, `doc: 99`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` jquery
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `includes/libs/Rdbms/LoadBalancer/LoadBalancer.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.241 IQR)
- **Top Global Matches:** file_cluster_8: 14.241, file_cluster_13: 14.249, file_cluster_7: 14.358
- **Magnitude:** 1473.06 | **LOC:** 2046 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 20.0%
- **Risk Profile:** Cognitive Load (35.7046%), Tech Debt (47.2262%)
**Top Internal Functions/Classes:**
  * `configure` (Impact: 67.4)
    * *Intent:* /** @var int Idiom for getExistingReaderIndex() meaning "no index selected" */
  * `reallyOpenConnection` (Impact: 55.4)
    * *Intent:* /** * Get the server index chosen for DB_REPLICA connections for the given query group
  * `runPrimaryTransactionIdleCallbacks` (Impact: 51.0)
    * *Intent:* /** * Sanity check to make sure that the right domain is selected *
  * `getReaderIndex` (Impact: 47.9)
  * `waitForPrimaryPos` (Impact: 33.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 265`, `structural_boundaries: 228`, `args: 70`, `func_start: 66`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 58`, `state_mutation: 661`, `orphaned_logic: 28`
* *Architecture:* `api: 46`, `concurrency: 2`, `import: 14`
* *Defense:* `safety: 62`, `doc: 192`, `test: 4`, `immutability_locks: 17`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` Wikimedia\Stats\StatsFactory, 
	private function reuseOrOpenConnectionForNewRef( $i, use autocommit mode, UnexpectedValueException, Wikimedia\ScopedCallback, Wikimedia\ObjectCache\BagOStuff,  Note that callbacks should already be suppressed due to finalizePrimaryChanges().
		foreach ( $this->getOpenPrimaryConnections(),  transaction is active or if there is any other meaningful session state.
			$isShareable = !(
				$poolConn->databasesAreIndependent() &&
				$domain->getDatabase() !== null &&
				$domain->getDatabase() !== $poolConn->getDBname()...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `includes/FileRepo/File/LocalFile.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.707 IQR)
- **Top Global Matches:** file_cluster_13: 13.707, file_cluster_8: 13.832, file_cluster_7: 13.946
- **Magnitude:** 1397.88 | **LOC:** 2809 | **CtrlFlow:** 49.6% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (44.2521%), Tech Debt (27.3297%)
**Top Internal Functions/Classes:**
  * `upgradeRow` (Impact: 188.7)
    * *Intent:* /** * Returns the list of object properties that are included as-is in the * cache, only when they'r...
  * `recordUpload3` (Impact: 153.8)
  * `maybeUpgradeRow` (Impact: 40.6)
    * *Intent:* /** * @return LocalRepo|false */
  * `loadFromDB` (Impact: 29.1)
  * `getDescriptionText` (Impact: 21.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 230`, `structural_boundaries: 234`, `args: 56`, `func_start: 52`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 55`, `state_mutation: 712`, `planned_debt: 4`, `orphaned_logic: 12`
* *Architecture:* `api: 39`, `import: 46`
* *Defense:* `safety: 25`, `doc: 213`, `test: 7`, `sync_locks: 3`, `immutability_locks: 8`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.358
  * `Choke Point (Betweenness):` 0.000399 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 37):` in the `$table` to `IDatabase->select()` or `SelectQueryBuilder::tables`
	 *   - fields: (string[]) to include in the `$vars` to `IDatabase->select()` or `SelectQueryBuilder::fields`
	 *   - joins: (array) to include in the `$join_conds` to `IDatabase->select()` or `SelectQueryBuilder::joinConds`
	 * @phan-return arraytables:string[], MediaWiki\MainConfigNames, MediaWiki\JobQueue\Jobs\ThumbnailRenderJob, MediaWiki\Deferred\SiteStatsUpdate, Wikimedia\Rdbms\Database, MediaWiki\FileRepo\FileRepo, Wikimedia\Rdbms\IReadableDatabase, UnexpectedValueException...
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `includes/libs/FileBackend/FileBackendStore.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.136 IQR)
- **Top Global Matches:** file_cluster_13: 14.136, file_cluster_8: 14.363, file_cluster_7: 14.421
- **Magnitude:** 1234.52 | **LOC:** 2088 | **CtrlFlow:** 48.2% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (34.9959%), Tech Debt (89.489%)
**Top Internal Functions/Classes:**
  * `doQuickOperationsInternal` (Impact: 139.2)
  * `getFileStat` (Impact: 44.5)
  * `primeFileCache` (Impact: 36.9)
  * `doConcatenate` (Impact: 32.8)
    * *Intent:* /** * Copy a file from one storage path to another in the backend. * This will overwrite any file th...
  * `primeContainerCache` (Impact: 28.5)
    * *Intent:* /** * @see FileBackendStore::getLocalReferenceMulti() * @stable to override * @param array $params
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 193`, `structural_boundaries: 207`, `args: 63`, `func_start: 63`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 497`, `dead_code: 3`, `planned_debt: 2`, `orphaned_logic: 27`
* *Architecture:* `io: 3`, `api: 25`, `import: 24`
* *Defense:* `safety: 32`, `doc: 210`, `test: 2`, `immutability_locks: 41`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` Wikimedia\FileBackend\FileOps\CopyFileOp, Wikimedia\FileBackend\FileOps\NullFileOp, 
	final protected function getContainerHashLevels( $container ) 
		if ( isset( $this->shardViaHashLevels[$container] ) ) 
			$config = $this->shardViaHashLevels[$container], StatusValue, Wikimedia\FileBackend\FileOps\DescribeFileOp, value map
	 *   - async       : StatusValue will be returned immediately if supported.
	 *                   If the StatusValue is OK, :
	 *   - srvCache     : BagOStuff object to use for server-local persistent caching.
	 *   - wanCache     : WANObjectCache object to use for server-shared persistent caching.
	 *   - mimeCallback : Callback that takes (storage path, content...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `includes/Specials/SpecialUndelete.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.506 IQR)
- **Top Global Matches:** file_cluster_13: 13.506, file_cluster_8: 13.681, file_cluster_7: 13.878
- **Magnitude:** 1231.22 | **LOC:** 1679 | **CtrlFlow:** 49.2% | **Authorship Centralization:** 20.0%
- **Risk Profile:** Cognitive Load (43.3064%), Tech Debt (22.0833%)
**Top Internal Functions/Classes:**
  * `showHistory` (Impact: 150.0)
  * `showRevision` (Impact: 72.5)
  * `loadRequest` (Impact: 65.1)
  * `execute` (Impact: 45.8)
  * `undelete` (Impact: 21.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 188`, `structural_boundaries: 194`, `args: 28`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 673`, `dead_code: 1`, `planned_debt: 5`, `fragile_debt: 3`, `orphaned_logic: 3`
* *Architecture:* `io: 3`, `api: 6`, `import: 62`
* *Defense:* `safety: 28`, `doc: 95`, `test: 3`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.078
  * `Choke Point (Betweenness):` 0.000246 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 45):` MediaWiki\Exception\ErrorPageError, MediaWiki\Html\Html, MediaWiki\MainConfigNames, the undisplayed row beyond the display limit.
			$history .= $this->formatRevisionRow( $row, OOUI\HorizontalLayout, MediaWiki\Linker\LinkTarget, MediaWiki\Exception\PermissionsError, MediaWiki\Context\DerivativeContext...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `includes/Parser/ParserOutput.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.708 IQR)
- **Top Global Matches:** file_cluster_13: 14.708, file_cluster_11: 15.017, file_cluster_8: 15.057
- **Magnitude:** 1215.38 | **LOC:** 3448 | **CtrlFlow:** 46.8% | **Authorship Centralization:** 53.8%
- **Risk Profile:** Cognitive Load (46.4194%), Tech Debt (14.0712%)
**Top Internal Functions/Classes:**
  * `getWarnings` (Impact: 169.6)
  * `initFromJson` (Impact: 127.8)
    * *Intent:* /**
  * `addOutputPageMetadata` (Impact: 67.7)
  * `addLanguageLink` (Impact: 19.0)
  * `isLinkInternal` (Impact: 17.8)
    * *Intent:* * - userLang: (Language) Language object used for localizing UX messages, * for example the heading ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 182`, `args: 83`, `func_start: 81`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 3`, `state_mutation: 335`, `dead_code: 1`, `planned_debt: 6`, `fragile_debt: 1`
* *Architecture:* `io: 2`, `api: 141`, `import: 25`
* *Defense:* `safety: 48`, `doc: 227`, `immutability_locks: 4`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.967
  * `Choke Point (Betweenness):` 0.00029 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` DebugInfo' => false, assuming
	 *     section edit link tokens are present in the HTML. Default is true, $this->getOutputStrings( $name ), and extension data, MediaWiki\Json\JsonDeserializable, and CSP src.)
		foreach ( ParserOutputStringSets::values(), $source->mExtensionData, *    meaning a wrapper div will be added if getWrapperDivClass() returns
	 *    a non-empty string.
	 *  - wrapperDivClass: (string) Wrap the output in a div and apply the given
	 *    CSS class to that div. This overrides the output of getWrapperDivClass().
	 *    Setting this to an empty string has the same effect...
  * `Imported By (In-Degree: 104):` (Excluded from Brief to save tokens)

### `maintenance/includes/Maintenance.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.968 IQR)
- **Top Global Matches:** file_cluster_13: 13.968, file_cluster_7: 14.241, file_cluster_8: 14.249
- **Magnitude:** 1192.28 | **LOC:** 1682 | **CtrlFlow:** 39.2% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (46.8021%), Tech Debt (9.7593%)
**Top Internal Functions/Classes:**
  * `setBatchSize` (Impact: 267.9)
  * `purgeRedundantText` (Impact: 167.0)
  * `readlineEmulation` (Impact: 74.2)
    * *Intent:* # Script-dependent options:
  * `finalSetup` (Impact: 32.6)
    * *Intent:* /**
  * `readconsole` (Impact: 23.7)
    * *Intent:* /** * Does the script need different DB access? By default, we give Maintenance * scripts normal rig...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 146`, `args: 60`, `func_start: 57`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 300`, `planned_debt: 2`
* *Architecture:* `io: 3`, `api: 53`, `concurrency: 12`, `import: 25`
* *Defense:* `safety: 7`, `doc: 207`, `test: 2`, `immutability_locks: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` MediaWiki\MainConfigNames, :bool, Wikimedia\Rdbms\ILBFactory, MediaWiki\Config\Config, $multiOccurrence, StatusValue, MediaWiki\Config\ConfigException, MaintenanceParameters.php'...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `includes/ResourceLoader/ResourceLoader.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.632 IQR)
- **Top Global Matches:** file_cluster_13: 14.632, file_cluster_11: 15.008, file_cluster_8: 15.048
- **Magnitude:** 1159.94 | **LOC:** 2222 | **CtrlFlow:** 46.6% | **Authorship Centralization:** 12.5%
- **Risk Profile:** Cognitive Load (45.8842%), Tech Debt (91.4338%)
**Top Internal Functions/Classes:**
  * `makeModuleResponse` (Impact: 188.9)
    * *Intent:* /** * Add an error to the 'errors' array and log it. * * @internal For use by StartUpModule.
  * `addOneModuleResponse` (Impact: 62.5)
    * *Intent:* // As of MediaWiki 1.28, the server and client use the same algorithm for combining // version hashe...
  * `addImplementScript` (Impact: 41.8)
  * `addFileContent` (Impact: 33.5)
  * `sendResponseHeaders` (Impact: 32.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 180`, `structural_boundaries: 206`, `args: 58`, `func_start: 52`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 505`, `dead_code: 1`, `planned_debt: 3`, `fragile_debt: 2`, `orphaned_logic: 22`
* *Architecture:* `io: 19`, `api: 41`, `import: 49`
* *Defense:* `safety: 56`, `doc: 216`, `test: 1`, `immutability_locks: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.539
  * `Choke Point (Betweenness):` 0.001042 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` MediaWiki\MainConfigNames, MediaWiki\Html\Html, Wikimedia\Minify\IndexMap, MediaWiki\Config\Config, Wikimedia\Stats\StatsFactory,  of "". Force them to objects.
		$extraArgs = [
			(object)$styles, MediaWiki\Exception\MWExceptionHandler, MediaWiki\Output\OutputPage...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `resources/src/mediawiki.api/AbortController.js` (JAVASCRIPT) | Magnitude: 40.44 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 20, concurrency: 18, state_mutation: 16, panics_and_aborts: 16
- `includes/libs/MappedIterator.php` (PHP) | Magnitude: 74.72 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 58, state_mutation: 33, doc: 18, structural_boundaries: 17
- `includes/libs/FileBackend/FileIteration/SwiftFileBackendFileList.php` (PHP) | Magnitude: 14.96 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 13, structural_boundaries: 7, state_mutation: 7, doc: 7
- `resources/src/mediawiki.rcfilters/UriProcessor.js` (JAVASCRIPT) | Magnitude: 164.94 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 120, state_mutation: 70, doc: 34, branch: 23
- `includes/HistoryBlob/ConcatenatedGzipHistoryBlob.php` (PHP) | Magnitude: 93.96 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 65, state_mutation: 37, doc: 34, structural_boundaries: 20

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
- `resources/src/mediawiki.ForeignStructuredUpload.BookletLayout/ForeignStructuredUpload.js` (JAVASCRIPT) | Magnitude: 127.64 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 73, state_mutation: 55, doc: 24, args: 17
- `resources/src/startup/mediawiki.loader.js` (JAVASCRIPT) | Magnitude: 1486.04 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 553, state_mutation: 332, branch: 136, structural_boundaries: 107
- `includes/libs/ObjectCache/Utils/MemcachedClient.php` (PHP) | Magnitude: 673.1 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 376, state_mutation: 370, branch: 96, doc: 88
- `resources/src/mediawiki.rcfilters/ui/FilterMenuOptionWidget.js` (JAVASCRIPT) | Magnitude: 66.22 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 40, indent_tabs: 28, doc: 10, branch: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `tests/phpunit/MediaWikiGroupValidator.php` (PHP) | Magnitude: 4.14 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, doc: 4, indent_tabs: 4, branch: 1
- `resources/src/mediawiki.rcfilters/ui/LiveUpdateButtonWidget.js` (JAVASCRIPT) | Magnitude: 22.7 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 12, state_mutation: 11, doc: 6, func_start: 4
- `resources/src/mediawiki.widgets/MediaSearch/mw.widgets.MediaUserUploadsProvider.js` (JAVASCRIPT) | Magnitude: 37.66 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 26, state_mutation: 16, args: 7, doc: 7
- `resources/src/mediawiki.widgets/MediaSearch/mw.widgets.MediaSearchProvider.js` (JAVASCRIPT) | Magnitude: 26.82 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 24, state_mutation: 12, args: 7, doc: 7
- `resources/src/mediawiki.rcfilters/ui/TagItemWidget.js` (JAVASCRIPT) | Magnitude: 21.06 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: sec_state_mutation: 11, doc: 10, state_mutation: 7, indent_tabs: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `includes/ResourceLoader/ReplayMinifierState.php` (PHP) | Magnitude: 36.7 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 34, structural_boundaries: 23, doc: 10, args: 9
- `includes/Specials/SpecialTags.php` (PHP) | Magnitude: 204.22 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 213, state_mutation: 85, structural_boundaries: 44, branch: 40
- `includes/Session/SessionId.php` (PHP) | Magnitude: 14.96 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 13, structural_boundaries: 10, doc: 10, args: 4
- `includes/ResourceLoader/ImageModule.php` (PHP) | Magnitude: 375.16 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 276, state_mutation: 173, doc: 73, branch: 68
- `includes/User/Hook/UserGroupsChangedHook.php` (PHP) | Magnitude: 37.6 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 9, indent_tabs: 9, structural_boundaries: 6, import: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `resources/src/mediawiki.Uri/Uri.js` (JAVASCRIPT) | Magnitude: 169.62 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 94, state_mutation: 48, branch: 38, doc: 26
- `resources/src/mediawiki.api/rest.js` (JAVASCRIPT) | Magnitude: 66.3 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 88, doc: 34, state_mutation: 24, args: 13
- `resources/src/mediawiki.widgets/MediaSearch/mw.widgets.MediaResultWidget.js` (JAVASCRIPT) | Magnitude: 161.54 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 135, state_mutation: 117, doc: 27, args: 17
- `resources/src/mediawiki.template.js` (JAVASCRIPT) | Magnitude: 42.82 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 54, doc: 38, args: 9, closures: 9
- `resources/src/mediawiki.widgets/MediaSearch/mw.widgets.APIResultsQueue.js` (JAVASCRIPT) | Magnitude: 264.28 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: state_mutation: 178, indent_tabs: 102, doc: 33, concurrency: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `resources/src/mediawiki.page.gallery.js` (JAVASCRIPT) | Magnitude: 81.76 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 106, state_mutation: 40, branch: 19, immutability_locks: 13
- `resources/src/mediawiki.special.changeslist.legend.js` (JAVASCRIPT) | Magnitude: 16.12 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 4, state_mutation: 3, args: 2, closures: 2
- `includes/ExternalStore/ExternalStoreMemory.php` (PHP) | Magnitude: 51.94 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 33, state_mutation: 24, structural_boundaries: 15, doc: 13
- `includes/HTMLForm/Field/HTMLNamespacesMultiselectField.php` (PHP) | Magnitude: 89.58 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 64, state_mutation: 27, branch: 23, structural_boundaries: 20
- `resources/src/mediawiki.widgets/mw.widgets.SelectWithInputWidget.js` (JAVASCRIPT) | Magnitude: 159.66 | Delta: **0.091 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: state_mutation: 101, indent_tabs: 101, doc: 17, branch: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `resources/src/mediawiki.widgets/mw.widgets.ExpiryInputWidget.js` (JAVASCRIPT) | Magnitude: 94.38 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 72, state_mutation: 57, branch: 10, structural_boundaries: 9
- `resources/src/mediawiki.widgets/mw.widgets.ComplexTitleInputWidget.js` (JAVASCRIPT) | Magnitude: 50.4 | Delta: **0.068 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 63, state_mutation: 26, doc: 9, structural_boundaries: 8
- `tests/phpunit/includes/Logging/LogTests.i18n.php` (PHP) | Magnitude: 17.16 | Delta: **0.112 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 4, state_mutation: 3, test: 3, scientific: 3
- `resources/src/mediawiki.widgets/mw.widgets.SizeFilterWidget.js` (JAVASCRIPT) | Magnitude: 29.22 | Delta: **0.144 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 54, state_mutation: 15, doc: 8, ui_framework: 8
- `resources/src/mediawiki.action/mediawiki.action.edit.checkboxes.less` (CSS) | Magnitude: 12.6 | Delta: **0.384 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 3, ui_framework: 2, class_start: 1, doc: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `resources/src/mediawiki.page.image.pagination.js` (JAVASCRIPT) | Magnitude: 82.76 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 55, state_mutation: 16, branch: 10, args: 10
- `resources/src/mediawiki.widgets/MediaSearch/mw.widgets.MediaSearchQueue.js` (JAVASCRIPT) | Magnitude: 34.38 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 32, state_mutation: 16, doc: 9, args: 6
- `tests/selenium/wdio-mediawiki/Util.js` (JAVASCRIPT) | Magnitude: 27.02 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 23, structural_boundaries: 18, doc: 11, args: 10
- `resources/src/mediawiki.widgets/MediaSearch/mw.widgets.MediaResourceProvider.js` (JAVASCRIPT) | Magnitude: 251.4 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 161, state_mutation: 130, doc: 41, structural_boundaries: 33
- `tests/api-testing/REST/PageHistory.js` (JAVASCRIPT) | Magnitude: 72.72 | Delta: **0.041 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: sec_high_risk_execution: 103, indent_tabs: 73, structural_boundaries: 28, concurrency: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `includes/RenameUser/Hook/RenameUserWarningHook.php` (PHP) | Magnitude: 32.88 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 5, structural_boundaries: 3, branch: 1, args: 1
- `includes/ResourceLoader/Hook/ResourceLoaderSiteModulePagesHook.php` (PHP) | Magnitude: 32.88 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 5, structural_boundaries: 3, branch: 1, args: 1
- `includes/ResourceLoader/Hook/ResourceLoaderSiteStylesModulePagesHook.php` (PHP) | Magnitude: 32.88 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 5, structural_boundaries: 3, branch: 1, args: 1
- `includes/Language/Hook/LocalisationCacheRecacheHook.php` (PHP) | Magnitude: 35.4 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 9, structural_boundaries: 3, state_mutation: 3, branch: 1
- `includes/Language/Hook/MessageCacheFetchOverridesHook.php` (PHP) | Magnitude: 35.4 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 5, structural_boundaries: 3, state_mutation: 3, branch: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `includes/Interwiki/Interwiki.php` (PHP) | Magnitude: 59.76 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 43, doc: 38, state_mutation: 27, structural_boundaries: 17
- `includes/libs/WRStats/WRStatsFactory.php` (PHP) | Magnitude: 45.82 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 32, state_mutation: 23, doc: 20, structural_boundaries: 13
- `includes/Title/ForeignTitleFactory.php` (PHP) | Magnitude: 35.4 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 8, structural_boundaries: 3, state_mutation: 3, branch: 1
- `includes/libs/Rdbms/Database/Utils/GeneralizedSql.php` (PHP) | Magnitude: 30.4 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 26, doc: 19, state_mutation: 14, structural_boundaries: 11
- `includes/Search/SearchIndexField.php` (PHP) | Magnitude: 78.43 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 27, api: 17, indent_tabs: 17, immutability_locks: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `includes/libs/FileBackend/FileOps/CopyFileOp.php` (PHP) | Magnitude: 73.98 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 62, state_mutation: 39, structural_boundaries: 24, branch: 12
- `includes/libs/Stats/NullStatsdDataFactory.php` (PHP) | Magnitude: 40.64 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 40, doc: 33, structural_boundaries: 26, args: 12
- `resources/src/mediawiki.rcfilters/ui/HighlightColorPickerWidget.js` (JAVASCRIPT) | Magnitude: 94.4 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 57, indent_tabs: 56, doc: 10, branch: 9
- `includes/SpecialPage/Hook/RedirectSpecialArticleRedirectParamsHook.php` (PHP) | Magnitude: 32.88 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 4, structural_boundaries: 3, branch: 1, args: 1
- `includes/User/Options/Hook/ConditionalDefaultOptionsAddConditionHook.php` (PHP) | Magnitude: 32.88 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 4, structural_boundaries: 3, branch: 1, args: 1

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

- `includes/MediaWikiServices.php` -> Churn: **74.32%** | Cog Load: 3.21% | Debt: 100.0%
- `includes/Specials/SpecialWatchlistLabels.php` -> Churn: **70.34%** | Cog Load: 6.8602% | Debt: 91.2033%
- `includes/Api/ApiQueryInfo.php` -> Churn: **69.5%** | Cog Load: 33.768% | Debt: 59.666%
- `includes/Specials/SpecialWatchlist.php` -> Churn: **63.46%** | Cog Load: 28.386% | Debt: 98.9846%
- `includes/User/UserRequirementsConditionChecker.php` -> Churn: **63.46%** | Cog Load: 46.3344% | Debt: 59.1182%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `resources/src/mediawiki.rcfilters/Controller.js` -> **Cormac Parle** (100.0% isolated ownership) | Magnitude: 1056.04
- `includes/Parser/Preprocessor_Hash.php` -> **Func** (100.0% isolated ownership) | Magnitude: 1022.17
- `includes/libs/ObjectCache/MediumSpecificBagOStuff.php` -> **Sam Reed** (100.0% isolated ownership) | Magnitude: 891.68
- `includes/Parser/BlockLevelPass.php` -> **Daimona Eaytoy** (100.0% isolated ownership) | Magnitude: 769.98
- `includes/libs/Rdbms/Database/TransactionManager.php` -> **Sam Reed** (100.0% isolated ownership) | Magnitude: 694.8

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
- `includes/libs/NonSerializable/NonSerializableTrait.php` -> **Severity: 377.138** (Blast Radius: 6.159 * Doc Risk: 61.2336%)
- `includes/libs/Rdbms/IDBAccessObject.php` -> **Severity: 279.094** (Blast Radius: 3.215 * Doc Risk: 86.8098%)
- `includes/DAO/WikiAwareEntity.php` -> **Severity: 199.464** (Blast Radius: 15.212 * Doc Risk: 13.1123%)
- `includes/libs/LightweightObjectStore/ExpirationAwareness.php` -> **Severity: 192.4** (Blast Radius: 1.924 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
