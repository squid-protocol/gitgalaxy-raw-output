# ARCHITECTURAL_BRIEF: wordpress
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/wordpress` |
| **Timestamp** | `2026-08-07T05:41:10.876148+00:00` |
| **Scan Duration** | `12.66s` |
| **Git Branch** | `master` |
| **Git Commit** | `5f913088f4a04816043be019737a6e4590eae845` |
| **Git Remote** | `https://github.com/WordPress/WordPress.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1891 malicious artifacts.

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
| Total Artifacts | 6068 |
| Analyzed Artifacts (Scanned) | 2649 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3419 |
| Total LOC | 419721 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 43.7% |
| Dominant Lang | PHP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5621 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.197 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.1467 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 17 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PHP | 1671 | 234383 | 63.1% |
| CSS | 449 | 78524 | 16.9% |
| JAVASCRIPT | 220 | 83927 | 8.3% |
| JSON | 165 | 22522 | 6.2% |
| HTML | 59 | 350 | 2.2% |
| PLAINTEXT | 52 | 3 | 2.0% |
| XML | 30 | 12 | 1.1% |
| MARKDOWN | 3 | 0 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `7.081`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 2165 | 81.7% |
| file_cluster_13 | 232 | 8.8% |
| file_cluster_2 | 68 | 2.6% |
| file_cluster_0 | 30 | 1.1% |
| file_cluster_17 | 26 | 1.0% |
| file_cluster_7 | 23 | 0.9% |
| file_cluster_15 | 15 | 0.6% |
| file_cluster_9 | 7 | 0.3% |
| file_cluster_11 | 7 | 0.3% |
| file_cluster_1 | 4 | 0.2% |
| file_cluster_4 | 4 | 0.2% |
| Unknown | 3 | 0.1% |
| file_cluster_6 | 2 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 52 | 2.0% |
| Static: Minified & Vendor Opaque Mass | 11 | 0.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3419*

**Composition by Extension & Reason:**
- `.css`: 1233x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 14x Excluded (Machine-Generated Source Code Signature: 814 LOC), 4x Excluded (Saturation: Line 6 exceeds 500 chars)
- `.js`: 506x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded (Saturation: Line 11 exceeds 500 chars), 2x Excluded (Saturation: Line 3 exceeds 500 chars)
- `.svg`: 334x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 63 LOC), 1x Excluded (Machine-Generated Source Code Signature: 132 LOC)
- `.woff2`: 315x Excluded (Explicitly Denied Extension: '.woff2')
- `.php`: 276x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Saturation: Line 36 exceeds 500 chars), 2x Excluded (Saturation: Line 14 exceeds 500 chars)
- `.png`: 160x Excluded (Explicitly Denied Extension: '.png')
- `.scss`: 110x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 3 exceeds 500 chars), 1x Excluded (Saturation: Line 10 exceeds 500 chars)
- `.jpg`: 85x Excluded (Explicitly Denied Extension: '.jpg')
- `.gif`: 62x Excluded (Explicitly Denied Extension: '.gif')
- `.woff`: 54x Excluded (Explicitly Denied Extension: '.woff')
- `.map`: 52x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.webp`: 46x Excluded (Explicitly Denied Extension: '.webp')
- `.json`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Static Asset Blob without Intent: 1726 LOC), 1x Excluded (Massive Static Asset Blob: 6791 LOC)
- `.txt`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ttf`: 13x Excluded (Explicitly Denied Extension: '.ttf')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 27.2 | 24.3 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 53.3 | 69.8 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 25.1 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 18.5 | 2.3 | 2.3 |
| API Exposure | 0.0 | 12.6 | 1.6 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 62.0 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 64.0 | 0.4 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 86.9 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.7 | 0.1 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 4.2 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 19.5 | 13.4 | 11.9 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `wp-admin/includes/ajax-actions.php` (Hits: 223)
- `wp-admin/includes/class-custom-image-header.php` (Hits: 130)
- `wp-includes/theme.php` (Hits: 61)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **InvalidArgumentException.php** (`wp-includes/php-ai-client/src/Common/Exception/InvalidArgumentException.php`) — 38 inbound connections
2. **AbstractDataTransferObject.php** (`wp-includes/php-ai-client/src/Common/AbstractDataTransferObject.php`) — 21 inbound connections
3. **Message.php** (`wp-includes/php-ai-client/src/Messages/DTO/Message.php`) — 20 inbound connections
4. **InvalidArgument.php** (`wp-includes/Requests/src/Exception/InvalidArgument.php`) — 16 inbound connections
5. **RuntimeException.php** (`wp-includes/php-ai-client/src/Common/Exception/RuntimeException.php`) — 16 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **blocks-json.php** (`wp-includes/blocks/blocks-json.php`) — 1031 outbound dependencies
2. **update-core.php** (`wp-admin/includes/update-core.php`) — 866 outbound dependencies
3. **script-loader.php** (`wp-includes/script-loader.php`) — 431 outbound dependencies
4. **wp-settings.php** (`wp-settings.php`) — 337 outbound dependencies
5. **post.php** (`wp-includes/post.php`) — 225 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `step` (@ `wp-includes/html-api/class-wp-html-processor.php`) -> Impact: **1776.0** | LOC: 1972
- `next_visitable_token` (@ `wp-includes/html-api/class-wp-html-processor.php`) -> Impact: **1167.0** | LOC: 1967
  * *Intent:* * that the document will eventually be placed in. It becomes important * when special elements have different rules than others, such as inside * a TE...
- `factory` (@ `wp-includes/js/jquery/ui/datepicker.js`) -> Impact: **1135.0** | LOC: 1579
- `QuicktimeParseAtom` (@ `wp-includes/ID3/module.audio-video.quicktime.php`) -> Impact: **1126.8** | LOC: 1212
- `rest_ensure_response` (@ `wp-includes/rest-api.php`) -> Impact: **969.8** | LOC: 1731
- `_updateDatepicker` (@ `wp-includes/js/jquery/ui/datepicker.js`) -> Impact: **942.0** | LOC: 1279
- `define` (@ `wp-includes/js/plupload/moxie.js`) -> Impact: **885.6** | LOC: 2513
- `get_custom_logo` (@ `wp-includes/general-template.php`) -> Impact: **875.8** | LOC: 1588
  * *Intent:* * @since 3.0.0 * @since 6.6.0 Added `required_username` and `required_password` arguments. * * @param array $args { * Optional. Array of options to co...
- `define` (@ `wp-includes/js/plupload/moxie.js`) -> Impact: **822.1** | LOC: 2443
- `setTimeout` (@ `wp-includes/js/jquery/ui/datepicker.js`) -> Impact: **807.1** | LOC: 1246
  * *Intent:* /* Retrieve the instance data for the target control. * @param target element - the target input field or division or span * @return object - the asso...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `wp-includes` | 249 | 93795.32 | 30.75% | 52.52% |
| `wp-admin/includes` | 105 | 45427.52 | 36.12% | 48.3% |
| `wp-includes/js` | 47 | 28416.47 | 39.85% | 59.89% |
| `wp-admin/js` | 49 | 19055.46 | 29.28% | 57.83% |
| `wp-includes/js/jquery/ui` | 36 | 18524.84 | 56.31% | 45.16% |
| `wp-content/themes/twentytwentyfive/patterns` | 92 | 15324.52 | 51.55% | 0.0% |
| `wp-admin` | 90 | 12181.21 | 41.09% | 4.07% |
| `wp-includes/js/plupload` | 5 | 11490.42 | 33.36% | 79.99% |
| `wp-includes/rest-api/endpoints` | 45 | 9618.54 | 22.86% | 40.85% |
| `wp-includes/ID3` | 17 | 8345.72 | 35.4% | 25.61% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `wp-admin/includes/class-automatic-upgrader-skin.php` -> **100.0%** Exposure
- `wp-admin/includes/class-wp-internal-pointers.php` -> **100.0%** Exposure
- `wp-admin/includes/class-wp-privacy-policy-content.php` -> **100.0%** Exposure
- `wp-admin/includes/deprecated.php` -> **100.0%** Exposure
- `wp-admin/includes/ms-deprecated.php` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `wp-admin/admin-footer.php` -> **100.0%** Exposure
- `wp-admin/admin.php` -> **100.0%** Exposure
- `wp-admin/comment.php` -> **100.0%** Exposure
- `wp-admin/edit-comments.php` -> **100.0%** Exposure
- `wp-admin/edit-form-advanced.php` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `wp-includes/js/tinymce/themes/modern/theme.js` -> **0** Orphaned Functions | **266** Duplicates
- `wp-includes/js/tinymce/themes/inlite/theme.js` -> **0** Orphaned Functions | **244** Duplicates
- `wp-includes/js/plupload/moxie.js` -> **27** Orphaned Functions | **95** Duplicates
- `wp-includes/js/media-views.js` -> **0** Orphaned Functions | **120** Duplicates
- `wp-includes/js/tinymce/plugins/paste/plugin.js` -> **0** Orphaned Functions | **104** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`wp-admin/admin-header.php`** -> AI Confidence: **99.48%**
2. **`wp-admin/admin.php`** -> AI Confidence: **99.48%**
3. **`wp-admin/edit-form-advanced.php`** -> AI Confidence: **99.48%**
4. **`wp-admin/edit-form-blocks.php`** -> AI Confidence: **99.48%**
5. **`wp-admin/edit-link-form.php`** -> AI Confidence: **99.48%**
6. **`wp-admin/edit-tag-form.php`** -> AI Confidence: **99.48%**
7. **`wp-admin/edit-tags.php`** -> AI Confidence: **99.48%**
8. **`wp-admin/erase-personal-data.php`** -> AI Confidence: **99.48%**
9. **`wp-admin/export.php`** -> AI Confidence: **99.48%**
10. **`wp-admin/includes/ajax-actions.php`** -> AI Confidence: **99.48%**
11. **`wp-admin/includes/class-custom-background.php`** -> AI Confidence: **99.48%**
12. **`wp-admin/includes/class-custom-image-header.php`** -> AI Confidence: **99.48%**
13. **`wp-admin/includes/class-wp-debug-data.php`** -> AI Confidence: **99.48%**
14. **`wp-admin/includes/class-wp-posts-list-table.php`** -> AI Confidence: **99.48%**
15. **`wp-admin/includes/image-edit.php`** -> AI Confidence: **99.48%**
16. **`wp-admin/includes/image.php`** -> AI Confidence: **99.48%**
17. **`wp-admin/includes/meta-boxes.php`** -> AI Confidence: **99.48%**
18. **`wp-admin/includes/plugin-install.php`** -> AI Confidence: **99.48%**
19. **`wp-admin/includes/theme-install.php`** -> AI Confidence: **99.48%**
20. **`wp-admin/includes/update-core.php`** -> AI Confidence: **99.48%**
21. **`wp-admin/install.php`** -> AI Confidence: **99.48%**
22. **`wp-admin/media-upload.php`** -> AI Confidence: **99.48%**
23. **`wp-admin/network.php`** -> AI Confidence: **99.48%**
24. **`wp-admin/options-general.php`** -> AI Confidence: **99.48%**
25. **`wp-admin/options-permalink.php`** -> AI Confidence: **99.48%**
26. **`wp-admin/options.php`** -> AI Confidence: **99.48%**
27. **`wp-admin/plugins.php`** -> AI Confidence: **99.48%**
28. **`wp-admin/themes.php`** -> AI Confidence: **99.48%**
29. **`wp-admin/upgrade.php`** -> AI Confidence: **99.48%**
30. **`wp-admin/user-new.php`** -> AI Confidence: **99.48%**
31. **`wp-content/themes/twentyeleven/functions.php`** -> AI Confidence: **99.48%**
32. **`wp-content/themes/twentyfifteen/index.php`** -> AI Confidence: **99.48%**
33. **`wp-content/themes/twentyfourteen/index.php`** -> AI Confidence: **99.48%**
34. **`wp-content/themes/twentysixteen/index.php`** -> AI Confidence: **99.48%**
35. **`wp-includes/ID3/module.audio-video.quicktime.php`** -> AI Confidence: **99.48%**
36. **`wp-includes/ID3/module.audio-video.riff.php`** -> AI Confidence: **99.48%**
37. **`wp-includes/ID3/module.audio.ac3.php`** -> AI Confidence: **99.48%**
38. **`wp-includes/SimplePie/src/IRI.php`** -> AI Confidence: **99.48%**
39. **`wp-includes/block-supports/duotone.php`** -> AI Confidence: **99.48%**
40. **`wp-includes/blocks/blocks-json.php`** -> AI Confidence: **99.48%**
41. **`wp-includes/blocks/term-template.php`** -> AI Confidence: **99.48%**
42. **`wp-includes/cache-compat.php`** -> AI Confidence: **99.48%**
43. **`wp-includes/class-IXR.php`** -> AI Confidence: **99.48%**
44. **`wp-includes/class-walker-page.php`** -> AI Confidence: **99.48%**
45. **`wp-includes/class-wp-comment-query.php`** -> AI Confidence: **99.48%**
46. **`wp-includes/class-wp-editor.php`** -> AI Confidence: **99.48%**
47. **`wp-includes/class-wp-meta-query.php`** -> AI Confidence: **99.48%**
48. **`wp-includes/default-filters.php`** -> AI Confidence: **99.48%**
49. **`wp-includes/default-widgets.php`** -> AI Confidence: **99.48%**
50. **`wp-includes/feed-rss2-comments.php`** -> AI Confidence: **99.48%**
51. **`wp-includes/html-api/class-wp-html-doctype-info.php`** -> AI Confidence: **99.48%**
52. **`wp-login.php`** -> AI Confidence: **99.48%**
53. **`wp-signup.php`** -> AI Confidence: **99.48%**
54. **`wp-admin/includes/class-wp-automatic-updater.php`** -> AI Confidence: **99.39%**
55. **`wp-admin/includes/class-wp-ms-themes-list-table.php`** -> AI Confidence: **99.39%**
56. **`wp-admin/includes/class-wp-themes-list-table.php`** -> AI Confidence: **99.39%**
57. **`wp-admin/includes/media.php`** -> AI Confidence: **99.39%**
58. **`wp-admin/includes/ms.php`** -> AI Confidence: **99.39%**
59. **`wp-admin/includes/nav-menu.php`** -> AI Confidence: **99.39%**
60. **`wp-admin/includes/post.php`** -> AI Confidence: **99.39%**
61. **`wp-admin/includes/upgrade.php`** -> AI Confidence: **99.39%**
62. **`wp-admin/menu.php`** -> AI Confidence: **99.39%**
63. **`wp-admin/options-privacy.php`** -> AI Confidence: **99.39%**
64. **`wp-admin/site-editor.php`** -> AI Confidence: **99.39%**
65. **`wp-admin/theme-install.php`** -> AI Confidence: **99.39%**
66. **`wp-admin/update-core.php`** -> AI Confidence: **99.39%**
67. **`wp-admin/user-edit.php`** -> AI Confidence: **99.39%**
68. **`wp-content/themes/twentysixteen/functions.php`** -> AI Confidence: **99.39%**
69. **`wp-includes/ID3/getid3.php`** -> AI Confidence: **99.39%**
70. **`wp-includes/ID3/module.tag.id3v2.php`** -> AI Confidence: **99.39%**
71. **`wp-includes/PHPMailer/PHPMailer.php`** -> AI Confidence: **99.39%**
72. **`wp-includes/bookmark-template.php`** -> AI Confidence: **99.39%**
73. **`wp-includes/bookmark.php`** -> AI Confidence: **99.39%**
74. **`wp-includes/class-snoopy.php`** -> AI Confidence: **99.39%**
75. **`wp-includes/class-walker-nav-menu.php`** -> AI Confidence: **99.39%**
76. **`wp-includes/class-wp-block-processor.php`** -> AI Confidence: **99.39%**
77. **`wp-includes/class-wp-customize-manager.php`** -> AI Confidence: **99.39%**
78. **`wp-includes/class-wp-date-query.php`** -> AI Confidence: **99.39%**
79. **`wp-includes/class-wp-http-streams.php`** -> AI Confidence: **99.39%**
80. **`wp-includes/class-wp-query.php`** -> AI Confidence: **99.39%**
81. **`wp-includes/class-wp-site-query.php`** -> AI Confidence: **99.39%**
82. **`wp-includes/class-wp-term-query.php`** -> AI Confidence: **99.39%**
83. **`wp-includes/general-template.php`** -> AI Confidence: **99.39%**
84. **`wp-includes/html-api/class-wp-html-processor.php`** -> AI Confidence: **99.39%**
85. **`wp-includes/media.php`** -> AI Confidence: **99.39%**
86. **`wp-includes/pluggable.php`** -> AI Confidence: **99.39%**
87. **`wp-includes/post-template.php`** -> AI Confidence: **99.39%**
88. **`wp-includes/update.php`** -> AI Confidence: **99.39%**
89. **`wp-includes/widgets.php`** -> AI Confidence: **99.39%**
90. **`wp-load.php`** -> AI Confidence: **99.39%**
91. **`wp-admin/includes/class-wp-media-list-table.php`** -> AI Confidence: **99.35%**
92. **`wp-admin/includes/class-wp-plugin-install-list-table.php`** -> AI Confidence: **99.35%**
93. **`wp-includes/class-wp-customize-control.php`** -> AI Confidence: **99.35%**
94. **`wp-admin/admin-ajax.php`** -> AI Confidence: **99.34%**
95. **`wp-admin/authorize-application.php`** -> AI Confidence: **99.34%**
96. **`wp-admin/includes/revision.php`** -> AI Confidence: **99.34%**
97. **`wp-admin/nav-menus.php`** -> AI Confidence: **99.34%**
98. **`wp-admin/network/settings.php`** -> AI Confidence: **99.34%**
99. **`wp-admin/network/upgrade.php`** -> AI Confidence: **99.34%**
100. **`wp-admin/options-discussion.php`** -> AI Confidence: **99.34%**
101. **`wp-admin/post.php`** -> AI Confidence: **99.34%**
102. **`wp-admin/revision.php`** -> AI Confidence: **99.34%**
103. **`wp-admin/upload.php`** -> AI Confidence: **99.34%**
104. **`wp-includes/Text/Diff/Engine/native.php`** -> AI Confidence: **99.34%**
105. **`wp-includes/block-supports/typography.php`** -> AI Confidence: **99.34%**
106. **`wp-includes/compat-utf8.php`** -> AI Confidence: **99.34%**
107. **`wp-includes/feed-atom-comments.php`** -> AI Confidence: **99.34%**
108. **`wp-includes/feed-rdf.php`** -> AI Confidence: **99.34%**
109. **`wp-includes/nav-menu-template.php`** -> AI Confidence: **99.34%**
110. **`wp-includes/widgets/class-wp-widget-archives.php`** -> AI Confidence: **99.34%**
111. **`wp-includes/widgets/class-wp-widget-categories.php`** -> AI Confidence: **99.34%**
112. **`wp-includes/widgets/class-wp-widget-meta.php`** -> AI Confidence: **99.34%**
113. **`wp-includes/widgets/class-wp-widget-recent-posts.php`** -> AI Confidence: **99.34%**
114. **`wp-includes/widgets/class-wp-widget-tag-cloud.php`** -> AI Confidence: **99.34%**
115. **`wp-includes/wp-diff.php`** -> AI Confidence: **99.34%**
116. **`wp-activate.php`** -> AI Confidence: **99.32%**
117. **`wp-admin/admin-functions.php`** -> AI Confidence: **99.32%**
118. **`wp-admin/custom-background.php`** -> AI Confidence: **99.32%**
119. **`wp-admin/custom-header.php`** -> AI Confidence: **99.32%**
120. **`wp-admin/customize.php`** -> AI Confidence: **99.32%**
121. **`wp-admin/edit-comments.php`** -> AI Confidence: **99.32%**
122. **`wp-admin/edit-form-comment.php`** -> AI Confidence: **99.32%**
123. **`wp-admin/edit.php`** -> AI Confidence: **99.32%**
124. **`wp-admin/import.php`** -> AI Confidence: **99.32%**
125. **`wp-admin/includes/network.php`** -> AI Confidence: **99.32%**
126. **`wp-admin/link.php`** -> AI Confidence: **99.32%**
127. **`wp-admin/ms-delete-site.php`** -> AI Confidence: **99.32%**
128. **`wp-admin/network/site-settings.php`** -> AI Confidence: **99.32%**
129. **`wp-admin/network/site-themes.php`** -> AI Confidence: **99.32%**
130. **`wp-admin/network/site-users.php`** -> AI Confidence: **99.32%**
131. **`wp-admin/network/sites.php`** -> AI Confidence: **99.32%**
132. **`wp-admin/network/users.php`** -> AI Confidence: **99.32%**
133. **`wp-admin/options-media.php`** -> AI Confidence: **99.32%**
134. **`wp-admin/options-writing.php`** -> AI Confidence: **99.32%**
135. **`wp-admin/plugin-editor.php`** -> AI Confidence: **99.32%**
136. **`wp-admin/theme-editor.php`** -> AI Confidence: **99.32%**
137. **`wp-admin/users.php`** -> AI Confidence: **99.32%**
138. **`wp-content/themes/twentyfourteen/inc/widgets.php`** -> AI Confidence: **99.32%**
139. **`wp-content/themes/twentyfourteen/page-templates/full-width.php`** -> AI Confidence: **99.32%**
140. **`wp-content/themes/twentyfourteen/page.php`** -> AI Confidence: **99.32%**
141. **`wp-content/themes/twentyfourteen/single.php`** -> AI Confidence: **99.32%**
142. **`wp-content/themes/twentytwentyone/index.php`** -> AI Confidence: **99.32%**
143. **`wp-includes/block-bindings/term-data.php`** -> AI Confidence: **99.32%**
144. **`wp-includes/class-wp-oembed.php`** -> AI Confidence: **99.32%**
145. **`wp-links-opml.php`** -> AI Confidence: **99.32%**
146. **`wp-admin/includes/class-core-upgrader.php`** -> AI Confidence: **99.31%**
147. **`wp-admin/includes/class-language-pack-upgrader.php`** -> AI Confidence: **99.31%**
148. **`wp-admin/includes/class-plugin-installer-skin.php`** -> AI Confidence: **99.31%**
149. **`wp-admin/includes/class-theme-installer-skin.php`** -> AI Confidence: **99.31%**
150. **`wp-admin/includes/class-theme-upgrader.php`** -> AI Confidence: **99.31%**
151. **`wp-admin/includes/class-wp-comments-list-table.php`** -> AI Confidence: **99.31%**
152. **`wp-admin/includes/class-wp-community-events.php`** -> AI Confidence: **99.31%**
153. **`wp-admin/includes/class-wp-filesystem-base.php`** -> AI Confidence: **99.31%**
154. **`wp-admin/includes/class-wp-filesystem-direct.php`** -> AI Confidence: **99.31%**
155. **`wp-admin/includes/class-wp-filesystem-ftpext.php`** -> AI Confidence: **99.31%**
156. **`wp-admin/includes/class-wp-filesystem-ssh2.php`** -> AI Confidence: **99.31%**
157. **`wp-admin/includes/class-wp-list-table.php`** -> AI Confidence: **99.31%**
158. **`wp-admin/includes/class-wp-plugins-list-table.php`** -> AI Confidence: **99.31%**
159. **`wp-admin/includes/class-wp-screen.php`** -> AI Confidence: **99.31%**
160. **`wp-admin/includes/class-wp-site-health-auto-updates.php`** -> AI Confidence: **99.31%**
161. **`wp-admin/includes/class-wp-site-health.php`** -> AI Confidence: **99.31%**
162. **`wp-admin/includes/class-wp-terms-list-table.php`** -> AI Confidence: **99.31%**
163. **`wp-admin/includes/class-wp-upgrader.php`** -> AI Confidence: **99.31%**
164. **`wp-admin/includes/dashboard.php`** -> AI Confidence: **99.31%**
165. **`wp-admin/includes/file.php`** -> AI Confidence: **99.31%**
166. **`wp-admin/includes/plugin.php`** -> AI Confidence: **99.31%**
167. **`wp-admin/includes/privacy-tools.php`** -> AI Confidence: **99.31%**
168. **`wp-admin/includes/schema.php`** -> AI Confidence: **99.31%**
169. **`wp-admin/includes/template.php`** -> AI Confidence: **99.31%**
170. **`wp-admin/includes/theme.php`** -> AI Confidence: **99.31%**
171. **`wp-admin/includes/update.php`** -> AI Confidence: **99.31%**
172. **`wp-admin/install-helper.php`** -> AI Confidence: **99.31%**
173. **`wp-admin/load-styles.php`** -> AI Confidence: **99.31%**
174. **`wp-admin/network/site-new.php`** -> AI Confidence: **99.31%**
175. **`wp-admin/press-this.php`** -> AI Confidence: **99.31%**
176. **`wp-admin/privacy-policy-guide.php`** -> AI Confidence: **99.31%**
177. **`wp-admin/site-health.php`** -> AI Confidence: **99.31%**
178. **`wp-admin/widgets-form-blocks.php`** -> AI Confidence: **99.31%**
179. **`wp-content/themes/twentyeleven/inc/theme-options.php`** -> AI Confidence: **99.31%**
180. **`wp-content/themes/twentyfifteen/inc/back-compat.php`** -> AI Confidence: **99.31%**
181. **`wp-content/themes/twentyfourteen/functions.php`** -> AI Confidence: **99.31%**
182. **`wp-content/themes/twentyfourteen/inc/back-compat.php`** -> AI Confidence: **99.31%**
183. **`wp-content/themes/twentynineteen/functions.php`** -> AI Confidence: **99.31%**
184. **`wp-content/themes/twentynineteen/inc/back-compat.php`** -> AI Confidence: **99.31%**
185. **`wp-content/themes/twentyseventeen/inc/back-compat.php`** -> AI Confidence: **99.31%**
186. **`wp-content/themes/twentysixteen/inc/back-compat.php`** -> AI Confidence: **99.31%**
187. **`wp-content/themes/twentyten/functions.php`** -> AI Confidence: **99.31%**
188. **`wp-content/themes/twentythirteen/functions.php`** -> AI Confidence: **99.31%**
189. **`wp-content/themes/twentythirteen/inc/back-compat.php`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `195` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `12918` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `wp-includes/js/tinymce/plugins/paste/plugin.js` (JAVASCRIPT) -> Cumulative Risk: **680.02**
- **Archetype:** `file_cluster_4` (Distance: 13.879 IQR)
- **Magnitude:** 2974.64 | **LOC:** 2368 | **CtrlFlow:** 42.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), State Flux (99.9998%), Tech Debt (99.9837%)
- **Heaviest Functions:** `o` (Impact: 220.5), `isWordContent` (Impact: 218.2), `registerEventHandlers` (Impact: 85.5)

### 2. `wp-includes/js/jquery/ui/mouse.js` (JAVASCRIPT) -> Cumulative Risk: **648.45**
- **Archetype:** `file_cluster_8` (Distance: 14.263 IQR)
- **Magnitude:** 344.46 | **LOC:** 238 | **CtrlFlow:** 66.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.3577%), Cognitive Load (96.9231%)
- **Heaviest Functions:** `factory` (Impact: 83.7), `_mouseMove` (Impact: 44.5), `_mouseUp` (Impact: 9.2)

### 3. `wp-includes/js/backbone.js` (JAVASCRIPT) -> Cumulative Risk: **640.78**
- **Archetype:** `file_cluster_11` (Distance: 14.656 IQR)
- **Magnitude:** 1464.24 | **LOC:** 2158 | **CtrlFlow:** 49.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.4196%), Tech Debt (98.6978%)
- **Heaviest Functions:** `set` (Impact: 129.3), `offApi` (Impact: 47.1), `navigate` (Impact: 26.2)

### 4. `wp-includes/js/tinymce/plugins/image/plugin.js` (JAVASCRIPT) -> Cumulative Risk: **612.26**
- **Archetype:** `file_cluster_8` (Distance: 12.628 IQR)
- **Magnitude:** 1256.08 | **LOC:** 1210 | **CtrlFlow:** 37.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), State Flux (99.9998%), Tech Debt (99.9765%)
- **Heaviest Functions:** `mergeMargins` (Impact: 46.6), `Dialog` (Impact: 30.9), `showDialog` (Impact: 26.8)

### 5. `wp-admin/themes.php` (PHP) -> Cumulative Risk: **601.31**
- **Archetype:** `file_cluster_8` (Distance: 11.659 IQR)
- **Magnitude:** 529.32 | **LOC:** 1330 | **CtrlFlow:** 83.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.8265%), Tech Debt (99.5275%), Verification (80.0%)
- **Heaviest Functions:** `wp_update_php_annotation` (Impact: 30.1), `wp_update_php_annotation` (Impact: 23.1), `printf` (Impact: 22.9)

### 6. `wp-includes/js/tinymce/plugins/media/plugin.js` (JAVASCRIPT) -> Cumulative Risk: **601.15**
- **Archetype:** `file_cluster_8` (Distance: 12.72 IQR)
- **Magnitude:** 1111.42 | **LOC:** 1307 | **CtrlFlow:** 41.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), State Flux (99.9999%), Tech Debt (84.1568%)
- **Heaviest Functions:** `updateHtml` (Impact: 81.3), `start` (Impact: 58.8), `global$4` (Impact: 58.7)

### 7. `wp-includes/html-api/class-wp-html-open-elements.php` (PHP) -> Cumulative Risk: **599.29**
- **Archetype:** `file_cluster_8` (Distance: 12.592 IQR)
- **Magnitude:** 416.98 | **LOC:** 853 | **CtrlFlow:** 63.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9897%), Tech Debt (99.4196%), Verification (80.0%)
- **Heaviest Functions:** `after_element_push` (Impact: 65.6), `after_element_pop` (Impact: 60.3), `pop_until` (Impact: 20.7)

### 8. `wp-includes/js/tinymce/themes/modern/theme.js` (JAVASCRIPT) -> Cumulative Risk: **597.84**
- **Archetype:** `file_cluster_8` (Distance: 14.019 IQR)
- **Magnitude:** 7440.16 | **LOC:** 9608 | **CtrlFlow:** 45.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), State Flux (99.9998%), Tech Debt (98.9323%)
- **Heaviest Functions:** `checked` (Impact: 134.5), `recalc` (Impact: 118.1), `recalc` (Impact: 80.7)

### 9. `wp-includes/js/tinymce/themes/inlite/theme.js` (JAVASCRIPT) -> Cumulative Risk: **597.48**
- **Archetype:** `file_cluster_8` (Distance: 14.031 IQR)
- **Magnitude:** 7197.64 | **LOC:** 9793 | **CtrlFlow:** 43.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Cognitive Load (99.903%), Tech Debt (97.8855%)
- **Heaviest Functions:** `checked` (Impact: 134.5), `recalc` (Impact: 118.1), `recalc` (Impact: 80.7)

### 10. `wp-admin/includes/class-wp-internal-pointers.php` (PHP) -> Cumulative Risk: **596.03**
- **Archetype:** `file_cluster_8` (Distance: 13.097 IQR)
- **Magnitude:** 99.04 | **LOC:** 176 | **CtrlFlow:** 52.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9768%), Documentation (96.281%)
- **Heaviest Functions:** `enqueue_scripts` (Impact: 20.1), `print_js` (Impact: 12.3), `close` (Impact: 4.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `wp-includes/js/wplink.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.73 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.488 IQR)
- **Top Global Matches:** file_cluster_8: 12.73, file_cluster_11: 13.095, file_cluster_15: 13.101
- **Magnitude:** 13422.89 | **LOC:** 805 | **CtrlFlow:** 73.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.057%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 164`, `structural_boundaries: 60`, `args: 59`, `func_start: 45`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 286`
* *Architecture:* `io: 6`, `concurrency: 17`
* *Defense:* `safety: 31`, `doc: 1`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/js/plupload/moxie.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.164 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.164 IQR)
- **Top Global Matches:** file_cluster_11: 14.164, file_cluster_15: 14.278, file_cluster_0: 14.358
- **Magnitude:** 10585.78 | **LOC:** 9905 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.6093%), Tech Debt (99.9998%)
**Top Internal Functions/Classes:**
  * `define` (Impact: 885.6)
  * `define` (Impact: 822.1)
  * `extList2mimes` (Impact: 749.2)
    * *Intent:* /** * Pseudo sprintf implementation - simple way to replace tokens with specified values. * * @param...
  * `define` (Impact: 736.5)
  * `XMLHttpRequest` (Impact: 646.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 558`, `structural_boundaries: 392`, `args: 261`, `func_start: 227`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 4`, `state_mutation: 809`, `dead_code: 23`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 95`, `orphaned_logic: 27`
* *Architecture:* `io: 15`, `api: 8`, `concurrency: 17`, `import: 2`
* *Defense:* `safety: 144`, `doc: 279`, `test: 1`, `cleanup: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/js/tinymce/themes/modern/theme.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.019 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.25 IQR)
- **Top Global Matches:** file_cluster_8: 14.019, file_cluster_11: 14.158, file_cluster_15: 14.26
- **Magnitude:** 7440.16 | **LOC:** 9608 | **CtrlFlow:** 45.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (98.9323%)
**Top Internal Functions/Classes:**
  * `checked` (Impact: 134.5)
  * `recalc` (Impact: 118.1)
  * `recalc` (Impact: 80.7)
  * `addContextualToolbars` (Impact: 74.5)
  * `createFormatMenu` (Impact: 37.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1678`, `structural_boundaries: 2053`, `args: 1075`, `func_start: 1006`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 12`, `state_mutation: 3688`, `duplicate_logic: 266`
* *Architecture:* `io: 7`, `api: 31`, `concurrency: 57`
* *Defense:* `safety: 454`, `immutability_locks: 7`, `cleanup: 47`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/js/tinymce/themes/inlite/theme.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.031 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.2 IQR)
- **Top Global Matches:** file_cluster_8: 14.031, file_cluster_11: 14.168, file_cluster_15: 14.268
- **Magnitude:** 7197.64 | **LOC:** 9793 | **CtrlFlow:** 43.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (99.903%), Tech Debt (97.8855%)
**Top Internal Functions/Classes:**
  * `checked` (Impact: 134.5)
  * `recalc` (Impact: 118.1)
  * `recalc` (Impact: 80.7)
  * `createFormatMenu` (Impact: 37.8)
  * `init` (Impact: 36.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1659`, `structural_boundaries: 2171`, `args: 1131`, `func_start: 1074`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 12`, `state_mutation: 3795`, `duplicate_logic: 244`
* *Architecture:* `io: 9`, `api: 29`, `concurrency: 65`
* *Defense:* `safety: 455`, `immutability_locks: 4`, `cleanup: 47`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/html-api/class-wp-html-processor.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.494 IQR)
- **Top Global Matches:** file_cluster_8: 13.494, file_cluster_7: 13.661, file_cluster_11: 13.792
- **Magnitude:** 6044.24 | **LOC:** 6708 | **CtrlFlow:** 70.4% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (48.8484%), Tech Debt (32.5697%)
**Top Internal Functions/Classes:**
  * `step` (Impact: 1776.0)
  * `next_visitable_token` (Impact: 1167.0)
    * *Intent:* * that the document will eventually be placed in. It becomes important * when special elements have ...
  * `step_in_cell` (Impact: 616.5)
    * *Intent:* /* * > A character token that is one of U+0009 CHARACTER TABULATION, * > U+000A LINE FEED (LF), U+00...
  * `step_in_head` (Impact: 355.2)
    * *Intent:* * the underlying Tag Processor class is seeking to a bookmark. * * This doesn't currently have a way...
  * `step_in_frameset` (Impact: 292.6)
    * *Intent:* /* * > A character token that is one of U+0009 CHARACTER TABULATION, * > U+000A LINE FEED (LF), U+00...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 816`, `structural_boundaries: 343`, `args: 48`, `func_start: 46`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 37`, `high_risk_execution: 1`, `state_mutation: 715`, `planned_debt: 29`, `orphaned_logic: 7`
* *Architecture:* `api: 27`
* *Defense:* `safety: 37`, `doc: 163`, `test: 8`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` they are limited and require
	 * a name. They should not be created with programmatically-made
	 * names, 'NOFRAMES', 
	private function is_html_integration_point(): bool 
		$current_token = $this->state->current_token, `TR`, p>', __( 'Cannot set bookmarks on tokens that do no appear in the original HTML text.' ), the HTML `<table><td>` stops at tags `TABLE`, d.'...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-admin/js/customize-controls.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.328 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.511 IQR)
- **Top Global Matches:** file_cluster_8: 13.328, file_cluster_15: 13.4, file_cluster_7: 13.508
- **Magnitude:** 5825.06 | **LOC:** 9390 | **CtrlFlow:** 68.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.6725%), Tech Debt (99.8858%)
**Top Internal Functions/Classes:**
  * `onInstallSuccess` (Impact: 615.9)
  * `installTheme` (Impact: 614.0)
  * `initializeNewQuery` (Impact: 583.5)
  * `linkElements` (Impact: 518.6)
  * `initialize` (Impact: 295.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 696`, `structural_boundaries: 326`, `args: 343`, `func_start: 229`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 632`, `planned_debt: 5`, `fragile_debt: 1`, `duplicate_logic: 76`, `orphaned_logic: 23`
* *Architecture:* `io: 2`, `concurrency: 23`
* *Defense:* `safety: 178`, `doc: 443`, `sync_locks: 2`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/js/jquery/ui/datepicker.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.095 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.15 IQR)
- **Top Global Matches:** file_cluster_8: 14.095, file_cluster_11: 14.187, file_cluster_17: 14.209
- **Magnitude:** 5357.86 | **LOC:** 2241 | **CtrlFlow:** 79.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.7109%), Tech Debt (81.1341%)
**Top Internal Functions/Classes:**
  * `factory` (Impact: 1135.0)
  * `_updateDatepicker` (Impact: 942.0)
  * `setTimeout` (Impact: 807.1)
    * *Intent:* /* Retrieve the instance data for the target control. * @param target element - the target input fie...
  * `_generateHTML` (Impact: 409.1)
  * `Datepicker` (Impact: 180.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 575`, `structural_boundaries: 153`, `args: 87`, `func_start: 98`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 6`, `state_mutation: 775`, `dead_code: 2`, `duplicate_logic: 20`, `orphaned_logic: 9`
* *Architecture:* `concurrency: 6`
* *Defense:* `safety: 141`, `doc: 34`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/js/codemirror/csslint.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.543 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.247 IQR)
- **Top Global Matches:** file_cluster_11: 14.543, file_cluster_0: 14.569, file_cluster_13: 14.598
- **Magnitude:** 5159.28 | **LOC:** 10859 | **CtrlFlow:** 65.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (47.7292%), Tech Debt (98.5094%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 447.8)
  * `many` (Impact: 398.8)
  * `prototype` (Impact: 341.9)
  * `PropertyValuePart` (Impact: 300.7)
  * `_selector` (Impact: 278.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 738`, `structural_boundaries: 382`, `args: 242`, `func_start: 188`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 1713`, `dead_code: 16`, `planned_debt: 2`, `fragile_debt: 24`, `duplicate_logic: 51`
* *Architecture:* `io: 16`, `api: 38`, `concurrency: 6`, `import: 47`
* *Defense:* `safety: 162`, `doc: 339`, `sync_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Pseudos, EventTarget, SyntaxError, Selector, TokenStreamBase, Validation, ValidationTypes, TokenStreamBase...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-content/themes/twentytwenty/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-content/themes/twentytwentyone/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/certificates/ca-bundle.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/link-template.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 16.402 IQR)
- **Top Global Matches:** file_cluster_8: 16.402, file_cluster_7: 16.439, file_cluster_13: 16.565
- **Magnitude:** 4167.24 | **LOC:** 4905 | **CtrlFlow:** 64.5% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (47.1247%), Tech Debt (44.5227%)
**Top Internal Functions/Classes:**
  * `get_attachment_link` (Impact: 775.5)
    * *Intent:* // Protected posts don't have plain links if getting a sample URL.
  * `get_posts_nav_link` (Impact: 374.5)
    * *Intent:* /** * Retrieves the permalink for a post type archive feed. * * @since 3.1.0 * * @param string $post...
  * `get_adjacent_post` (Impact: 74.0)
    * *Intent:* /** * Retrieves the feed link for a given author.
  * `get_term_feed_link` (Impact: 38.6)
  * `get_pagenum_link` (Impact: 36.2)
    * *Intent:* /** * Retrieves the permalink for a search.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 446`, `structural_boundaries: 246`, `args: 99`, `func_start: 99`
* *Risk/State:* `state_mutation: 1820`, `orphaned_logic: 35`
* *Architecture:* None
* *Defense:* `safety: 67`, `doc: 630`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` $taxonomy, $order, $in_same_term, $location, 
		$private_states = get_post_stati( array( 'private' => true ), 
		$title = apply_filters( 'the_title', 'rpc', $post->ID...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-admin/user-edit.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.021 IQR)
- **Top Global Matches:** file_cluster_8: 11.021, file_cluster_13: 11.384, file_cluster_7: 11.478
- **Magnitude:** 4095.27 | **LOC:** 1026 | **CtrlFlow:** 77.8% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (38.3356%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 221`, `structural_boundaries: 63`, `args: 2`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 78`
* *Architecture:* `io: 6`, `import: 5`
* *Defense:* `safety: 4`, `doc: 18`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` translation-install.php', admin.php', d)', but not to update the user.', admin-footer.php', s HTTPS, admin-header.php', which is not enabled on this site.'...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/js/media-views.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_15` (Drift: 14.515 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.298 IQR)
- **Top Global Matches:** file_cluster_15: 14.515, file_cluster_11: 14.638, file_cluster_8: 14.666
- **Magnitude:** 3974.52 | **LOC:** 10605 | **CtrlFlow:** 56.2% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (45.6085%), Tech Debt (99.9986%)
**Top Internal Functions/Classes:**
  * `__webpack_modules__` (Impact: 165.3)
    * *Intent:* /******/ (() => { // webpackBootstrap
  * `toggleSelectionHandler` (Impact: 122.3)
  * `createToolbar` (Impact: 71.8)
  * `setUserSetting` (Impact: 49.1)
  * `elementShouldBeHidden` (Impact: 44.5)
    * *Intent:* * If one is not supplied, a collection of all attachments will be created. * @param {wp.media.model....
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 414`, `structural_boundaries: 323`, `args: 322`, `func_start: 246`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 2207`, `dead_code: 1`, `planned_debt: 5`, `duplicate_logic: 120`
* *Architecture:* `io: 3`, `api: 74`, `concurrency: 18`
* *Defense:* `safety: 69`, `doc: 543`, `test: 10`, `immutability_locks: 1`, `cleanup: 47`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/general-template.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.611 IQR)
- **Top Global Matches:** file_cluster_8: 15.611, file_cluster_7: 15.703, file_cluster_13: 15.834
- **Magnitude:** 3375.3 | **LOC:** 5424 | **CtrlFlow:** 71.8% | **Authorship Centralization:** 55.6%
- **Risk Profile:** Cognitive Load (46.9839%), Tech Debt (26.3735%)
**Top Internal Functions/Classes:**
  * `get_custom_logo` (Impact: 875.8)
    * *Intent:* * @since 3.0.0 * @since 6.6.0 Added `required_username` and `required_password` arguments. * * @para...
  * `wp_get_archives` (Impact: 140.0)
  * `paginate_links` (Impact: 124.8)
    * *Intent:* /** * Displays or retrieves page title for taxonomy term archive. * * Useful for taxonomy term templ...
  * `get_bloginfo` (Impact: 108.2)
  * `get_calendar` (Impact: 94.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 416`, `structural_boundaries: 163`, `args: 63`, `func_start: 61`
* *Risk/State:* `high_risk_execution: 17`, `state_mutation: 1381`, `orphaned_logic: 23`
* *Architecture:* `io: 4`, `import: 1`
* *Defense:* `safety: 34`, `doc: 334`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` 'comment', $result->post_title, 
function get_template_part( $slug, $relation_type, * `readonly` is a reserved keyword and cannot be used, d default values.
	$args = array_merge( $defaults, 'id_username'       => 'user_login', esc_attr( $args['id_submit'] )...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/functions.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.263 IQR)
- **Top Global Matches:** file_cluster_8: 15.263, file_cluster_7: 15.361, file_cluster_13: 15.45
- **Magnitude:** 3336.0 | **LOC:** 9256 | **CtrlFlow:** 65.4% | **Authorship Centralization:** 44.4%
- **Risk Profile:** Cognitive Load (38.2702%), Tech Debt (80.6794%)
**Top Internal Functions/Classes:**
  * `do_enclose` (Impact: 299.9)
    * *Intent:* /** * Filters the number formatted based on the locale. * * @since 2.8.0 * @since 4.9.0 The `$number...
  * `win_is_writable` (Impact: 81.0)
  * `_wp_upload_dir` (Impact: 72.8)
  * `add_query_arg` (Impact: 70.4)
  * `_wp_die_process_input` (Impact: 55.7)
    * *Intent:* /** * Retrieves or displays original referer hidden field for forms. * * The input name is '_wp_orig...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 614`, `structural_boundaries: 325`, `args: 144`, `func_start: 110`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 31`, `high_risk_execution: 1`, `state_mutation: 1391`, `dead_code: 3`, `planned_debt: 3`, `fragile_debt: 2`, `orphaned_logic: 58`
* *Architecture:* `io: 15`, `api: 2`, `concurrency: 30`, `import: 4`
* *Defense:* `safety: 67`, `doc: 493`, `test: 4`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` option.php', 406 => 'Not Acceptable', $wp_query->is_comment_feed, 503 => 'Service Unavailable', d ) ) 
		$trimmed = trim( $required, 410 => 'Gone', 423 => 'Locked', $display = true ) 
	$name        = esc_attr( $name...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/formatting.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.475 IQR)
- **Top Global Matches:** file_cluster_8: 15.475, file_cluster_7: 15.562, file_cluster_13: 15.66
- **Magnitude:** 3019.48 | **LOC:** 6293 | **CtrlFlow:** 59.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (45.8221%), Tech Debt (71.0449%)
**Top Internal Functions/Classes:**
  * `force_balance_tags` (Impact: 561.5)
  * `translate_smiley` (Impact: 314.1)
    * *Intent:* /** * Converts a number of HTML entities into their special characters. * * Specifically deals with:...
  * `wp_iso_descrambler` (Impact: 246.4)
  * `sanitize_email` (Impact: 204.9)
  * `esc_url` (Impact: 58.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 285`, `structural_boundaries: 198`, `args: 71`, `func_start: 66`
* *Risk/State:* `safety_bypasses: 43`, `high_risk_execution: 7`, `state_mutation: 1095`, `dead_code: 4`, `planned_debt: 2`, `fragile_debt: 2`, `orphaned_logic: 29`
* *Architecture:* None
* *Defense:* `safety: 31`, `doc: 341`, `test: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` 
		$text = wp_kses_normalize_entities( $text, 
		return apply_filters( 'sanitize_email', 
			'between'          => sprintf( __( '%1$s, a>' ), '%' characters will be replaced with a placeholder string, ', nbsp entities, $sanitized_email...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/js/tinymce/plugins/paste/plugin.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.879 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.788 IQR)
- **Top Global Matches:** file_cluster_4: 13.879, file_cluster_8: 13.922, file_cluster_11: 13.976
- **Magnitude:** 2974.64 | **LOC:** 2368 | **CtrlFlow:** 42.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (99.9837%)
**Top Internal Functions/Classes:**
  * `o` (Impact: 220.5)
  * `isWordContent` (Impact: 218.2)
  * `registerEventHandlers` (Impact: 85.5)
  * `setup` (Impact: 47.0)
  * `removeWebKitStyles` (Impact: 43.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 484`, `structural_boundaries: 655`, `args: 363`, `func_start: 343`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 3`, `state_mutation: 904`, `duplicate_logic: 104`
* *Architecture:* `io: 1`, `api: 33`, `concurrency: 165`, `import: 5`
* *Defense:* `safety: 178`, `immutability_locks: 2`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` browser.js, promise-polyfill, timers
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/rest-api.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.557 IQR)
- **Top Global Matches:** file_cluster_8: 14.557, file_cluster_7: 14.669, file_cluster_13: 14.77
- **Magnitude:** 2848.94 | **LOC:** 3501 | **CtrlFlow:** 53.6% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (46.8602%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `rest_ensure_response` (Impact: 969.8)
  * `rest_validate_value_from_schema` (Impact: 116.5)
  * `rest_preload_api_request` (Impact: 100.2)
    * *Intent:* // If there is only one error left, simply return it.
  * `rest_sanitize_value_from_schema` (Impact: 97.5)
  * `rest_validate_number_value_from_schema` (Impact: 71.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 439`, `structural_boundaries: 380`, `args: 65`, `func_start: 64`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 650`
* *Architecture:* `io: 5`, `api: 21`
* *Defense:* `safety: 113`, `doc: 248`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` 
					sprintf( __( '%1$s is a required property of %2$s.' ), those titles in the error message.
		if ( count( $schema_titles ) === count( $matching_schemas ) ) 
			return new WP_Error(
				'rest_one_of_multiple_matches', d values and may fall-back to a given default, 
function rest_filter_response_fields( $response, *
		 * Non-namespaced routes are not allowed, $value ) ) 
				return new WP_Error(
					'rest_property_required', determine whether the provided field should be included
 * in the response body.
 *
 * If a parent field is passed in, plugin.
 * @param string $route           The base URL for route you are adding.
 * @param array  $args            Optional. Either an array of options for the endpoint...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/class-wp-xmlrpc-server.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.996 IQR)
- **Top Global Matches:** file_cluster_8: 14.996, file_cluster_7: 15.095, file_cluster_13: 15.159
- **Magnitude:** 2834.74 | **LOC:** 7228 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (45.9243%), Tech Debt (20.6782%)
**Top Internal Functions/Classes:**
  * `mw_newPost` (Impact: 530.7)
  * `mw_editPost` (Impact: 276.0)
  * `wp_newComment` (Impact: 80.0)
  * `wp_getRevisions` (Impact: 34.5)
  * `wp_editProfile` (Impact: 32.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 491`, `structural_boundaries: 346`, `args: 57`, `func_start: 57`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 1138`, `dead_code: 1`, `fragile_debt: 2`, `orphaned_logic: 12`
* *Architecture:* `api: 51`, `import: 1`
* *Defense:* `safety: 129`, `doc: 279`, `immutability_locks: 31`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` 'mt.setPostCategories', d
	 * in the response array. This should be a list of field names. 'user_id' will
	 * always be included in the response regardless of the value of $fields.
	 *
	 * Instead of, 'pingback.extensions.getPingbacks', 'wp.getPage', 'taxonomies', 'blogger.editPost', 'wp.newPost', 'pingback.ping'...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/class-wp-theme-json.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.77 IQR)
- **Top Global Matches:** file_cluster_8: 14.77, file_cluster_7: 14.931, file_cluster_13: 14.945
- **Magnitude:** 2790.22 | **LOC:** 4835 | **CtrlFlow:** 64.8% | **Authorship Centralization:** 35.7%
- **Risk Profile:** Cognitive Load (45.5835%), Tech Debt (20.6949%)
**Top Internal Functions/Classes:**
  * `compute_preset_classes` (Impact: 477.8)
  * `sanitize` (Impact: 242.4)
  * `remove_insecure_styles` (Impact: 210.8)
  * `get_data` (Impact: 159.6)
    * *Intent:* /** * Gets the CSS layout rules for a particular block from theme.json layout definitions. * * @sinc...
  * `remove_insecure_properties` (Impact: 51.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 381`, `structural_boundaries: 207`, `args: 48`, `func_start: 44`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 34`, `high_risk_execution: 9`, `state_mutation: 991`, `dead_code: 2`, `orphaned_logic: 19`
* *Architecture:* `api: 12`, `import: 3`
* *Defense:* `safety: 115`, `doc: 186`, `test: 2`, `immutability_locks: 14`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` d in any `PRESETS_METADATA` value are allowed.
		static::remove_indirect_properties( $input, _node_paths_only = $options['include_node_paths_only'] ?? false, _node_paths_only ) 
			$selectors = empty( $selectors ) ? static::get_blocks_metadata() : $selectors, $options = array() ) 
		if ( null === $origins ) 
			$origins = static::VALID_ORIGINS, 
				unset( $node[ $feature ], $nested_selector, 'variations', d.
	 *
	 *      @type int    $steps      The number of steps in the scale. (up to 10 steps are supported.)
	 *      @type float  $mediumStep The middle value that gets the slug '50'. (For even number of steps...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-admin/includes/media.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.901 IQR)
- **Top Global Matches:** file_cluster_8: 14.901, file_cluster_13: 15.03, file_cluster_7: 15.073
- **Magnitude:** 2653.16 | **LOC:** 3887 | **CtrlFlow:** 73.2% | **Authorship Centralization:** 42.9%
- **Risk Profile:** Cognitive Load (41.4939%), Tech Debt (8.807%)
**Top Internal Functions/Classes:**
  * `attachment_submitbox_metadata` (Impact: 249.6)
  * `edit_form_image_editor` (Impact: 194.6)
  * `media_upload_library_form` (Impact: 167.8)
  * `get_compat_media_markup` (Impact: 87.2)
  * `media_handle_upload` (Impact: 76.4)
    * *Intent:* /** * Filters the image HTML markup to send to the editor when inserting an image. * * @since 2.5.0 ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 851`, `structural_boundaries: 311`, `args: 51`, `func_start: 45`
* *Risk/State:* `safety_bypasses: 69`, `high_risk_execution: 5`, `state_mutation: 1149`, `dead_code: 1`, `fragile_debt: 2`
* *Architecture:* `io: 45`, `api: 22`, `import: 4`
* *Defense:* `safety: 139`, `doc: 206`, `test: 2`, `immutability_locks: 10`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` 
	$form_action_url = apply_filters( 'media_upload_form_url', d, getid3.php', $form_action_url, 'value'         => '', sanitize_url( $src ), 
		if ( ! apply_filters( 'disable_captions', button>.' )...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/media.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.991 IQR)
- **Top Global Matches:** file_cluster_8: 14.991, file_cluster_7: 15.084, file_cluster_13: 15.162
- **Magnitude:** 2575.54 | **LOC:** 6564 | **CtrlFlow:** 70.3% | **Authorship Centralization:** 80.0%
- **Risk Profile:** Cognitive Load (46.482%), Tech Debt (8.8721%)
**Top Internal Functions/Classes:**
  * `image_resize_dimensions` (Impact: 355.5)
    * *Intent:* * A plugin may use the {@see 'image_downsize'} filter to hook into and offer image * resizing servic...
  * `wp_prepare_attachment_for_js` (Impact: 309.9)
  * `wp_audio_shortcode` (Impact: 265.7)
    * *Intent:* * Retrieves the image's intermediate size (resized) path, width, and height. * * The $size parameter...
  * `wp_get_registered_image_subsizes` (Impact: 232.5)
  * `wp_calculate_image_srcset` (Impact: 188.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 301`, `structural_boundaries: 127`, `args: 34`, `func_start: 34`
* *Risk/State:* `safety_bypasses: 60`, `high_risk_execution: 2`, `state_mutation: 726`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `api: 19`, `import: 1`
* *Defense:* `safety: 53`, `doc: 225`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` 'video' => ( $show_video_playlist ) ? 1 : 0, timestamp in milliseconds.
 *     @type string $name                  Name, then it will be stripped out of
 * the return.
 *
 * @since 2.5.0
 *
 * @param int|string $width  Image width in pixels.
 * @param int|string $height Image height in pixels.
 * @return string HTML attributes for width and, 
	return apply_filters( "$adjacent_image_link", 
function wp_prepare_attachment_for_js( $attachment ) 
	$attachment = get_post( $attachment, 
	wp_scripts()->add_data(
		'wp-upload-media', 
function image_hwstring( $width, $image_src...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-admin/includes/template.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_2` (Drift: 14.689 IQR)
- **Top Global Matches:** file_cluster_2: 14.689, file_cluster_8: 14.71, file_cluster_13: 14.731
- **Magnitude:** 2571.98 | **LOC:** 2843 | **CtrlFlow:** 67.9% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (40.0586%), Tech Debt (8.8467%)
**Top Internal Functions/Classes:**
  * `get_inline_data` (Impact: 648.9)
  * `do_meta_boxes` (Impact: 231.1)
  * `meta_form` (Impact: 110.0)
    * *Intent:* /**
  * `do_accordion_sections` (Impact: 85.3)
    * *Intent:* /** * Filters the maximum allowed upload size for import files. * * @since 2.3.0 * * @see wp_max_upl...
  * `add_meta_box` (Impact: 77.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 394`, `structural_boundaries: 186`, `args: 32`, `func_start: 32`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 785`, `fragile_debt: 1`
* *Architecture:* `io: 7`, `api: 21`, `import: 5`
* *Defense:* `safety: 54`, `doc: 149`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` 
				echo esc_html( apply_filters( 'the_category', 'reading', 'media', class-walker-category-checklist.php', primary, 
		$name    = esc_html( apply_filters( 'the_category', '', $term->name...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/theme.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.667 IQR)
- **Top Global Matches:** file_cluster_8: 14.667, file_cluster_13: 14.761, file_cluster_7: 14.799
- **Magnitude:** 2548.8 | **LOC:** 4423 | **CtrlFlow:** 66.4% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (47.0882%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `search_theme_directories` (Impact: 757.4)
    * *Intent:* /**
  * `is_header_video_active` (Impact: 243.7)
  * `get_theme_starter_content` (Impact: 221.3)
    * *Intent:* /** * Checks that the active theme has the required files. * * Standalone themes need to have a `tem...
  * `add_theme_support` (Impact: 130.8)
    * *Intent:* /** * Removes theme modifications option for the active theme.
  * `get_header_image_tag` (Impact: 52.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 356`, `structural_boundaries: 180`, `args: 52`, `func_start: 51`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 585`
* *Architecture:* `io: 61`, `api: 22`, `import: 6`
* *Defense:* `safety: 77`, `doc: 171`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.342
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` 'search-form' for backward compatibility.
 * @since 3.9.0 The `html5` feature now also accepts 'gallery' and 'caption'.
 * @since 4.1.0 The `title-tag` feature was added.
 * @since 4.5.0 The `customize-selective-refresh-widgets` feature was added.
 * @since 4.7.0 The `starter-content` feature was added.
 * @since 5.0.0 The `responsive-embeds`, 
function register_theme_feature( $feature, 
	return apply_filters( "theme_mod_$name", array(
					'title' => _x( 'Recent Comments', 'object'    => 'page', 'link_pinterest'  => array(
				'title' => _x( 'Pinterest', ments['requires'], array(
					'title' => _x( 'Search'...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `wp-includes/rest-api/class-wp-rest-request.php` (PHP) | Magnitude: 317.52 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 267, state_mutation: 134, doc: 96, structural_boundaries: 72
- `wp-includes/class-wp-matchesmapregex.php` (PHP) | Magnitude: 27.0 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 22, indent_tabs: 21, state_mutation: 11, structural_boundaries: 9
- `wp-includes/sodium_compat/src/Core32/Poly1305/State.php` (PHP) | Magnitude: 284.5 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 284, state_mutation: 219, doc: 71, structural_boundaries: 18
- `wp-includes/class-wp-role.php` (PHP) | Magnitude: 25.92 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 22, doc: 21, structural_boundaries: 7, api: 6
- `wp-includes/customize/class-wp-customize-partial.php` (PHP) | Magnitude: 114.48 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 70, state_mutation: 59, doc: 26, structural_boundaries: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `wp-admin/js/editor-expand.js` (JAVASCRIPT) | Magnitude: 401.56 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 495, branch: 144, events: 79, doc: 53
- `wp-admin/js/custom-background.js` (JAVASCRIPT) | Magnitude: 14.9 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 59, doc: 16, args: 11, closures: 11
- `wp-includes/class-wp-http-requests-hooks.php` (PHP) | Magnitude: 26.0 | Delta: **0.142 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 18, indent_tabs: 16, state_mutation: 14, structural_boundaries: 5
- `wp-includes/Requests/src/HookManager.php` (PHP) | Magnitude: 43.76 | Delta: **0.193 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 10, structural_boundaries: 4, state_mutation: 4, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `wp-includes/js/codemirror/csslint.js` (JAVASCRIPT) | Magnitude: 5159.28 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 3313, state_mutation: 1713, branch: 738, structural_boundaries: 382
- `wp-includes/js/jquery/ui/sortable.js` (JAVASCRIPT) | Magnitude: 1447.32 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 1372, indent_tabs: 824, branch: 274, safety: 87
- `wp-includes/class-json.php` (PHP) | Magnitude: 854.06 | Delta: **0.079 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 398, indent_spaces: 395, branch: 140, structural_boundaries: 57
- `wp-includes/blocks/gallery.php` (PHP) | Magnitude: 201.5 | Delta: **0.104 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 124, indent_tabs: 83, branch: 32, doc: 13
- `wp-includes/js/tinymce/utils/mctabs.js` (JAVASCRIPT) | Magnitude: 105.1 | Delta: **0.108 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 81, state_mutation: 28, branch: 19, args: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `wp-admin/includes/schema.php` (PHP) | Magnitude: 201.54 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 132, indent_tabs: 116, doc: 31, branch: 22
- `wp-includes/blocks/navigation-link.php` (PHP) | Magnitude: 342.08 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 186, state_mutation: 185, branch: 70, structural_boundaries: 27
- `wp-admin/import.php` (PHP) | Magnitude: 34.14 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 28, branch: 20, state_mutation: 18, io: 7
- `wp-includes/class-wp-fatal-error-handler.php` (PHP) | Magnitude: 116.04 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 103, state_mutation: 37, branch: 35, doc: 23
- `wp-includes/Requests/src/Utility/InputValidator.php` (PHP) | Magnitude: 34.34 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 30, structural_boundaries: 21, doc: 20, branch: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `wp-includes/js/customize-loader.js` (JAVASCRIPT) | Magnitude: 151.42 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 128, state_mutation: 61, branch: 33, globals: 22
- `wp-includes/js/mediaelement/wp-playlist.js` (JAVASCRIPT) | Magnitude: 341.6 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 264, indent_tabs: 143, branch: 26, args: 17
- `wp-admin/js/tags-box.js` (JAVASCRIPT) | Magnitude: 92.82 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 107, doc: 30, branch: 22, state_mutation: 20
- `wp-includes/js/customize-base.js` (JAVASCRIPT) | Magnitude: 172.0 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 198, state_mutation: 70, doc: 61, structural_boundaries: 34
- `wp-includes/js/customize-models.js` (JAVASCRIPT) | Magnitude: 91.52 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 74, state_mutation: 46, args: 13, closures: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `wp-includes/ID3/module.audio.mp3.php` (PHP) | Magnitude: 1221.94 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 776, state_mutation: 570, branch: 280, safety: 78
- `wp-content/themes/twentyfifteen/js/functions.js` (JAVASCRIPT) | Magnitude: 64.8 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 108, branch: 21, state_mutation: 17, events: 16
- `wp-admin/includes/comment.php` (PHP) | Magnitude: 165.06 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 103, state_mutation: 84, io: 32, branch: 28
- `wp-admin/includes/class-wp-ms-themes-list-table.php` (PHP) | Magnitude: 529.4 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 295, state_mutation: 214, branch: 86, doc: 48
- `wp-includes/js/jquery/ui/accordion.js` (JAVASCRIPT) | Magnitude: 726.32 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 395, state_mutation: 312, branch: 86, args: 26

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `wp-trackback.php` (PHP) | Magnitude: 69.2 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 55, indent_tabs: 30, branch: 29, io: 13
- `wp-includes/class-wp-customize-panel.php` (PHP) | Magnitude: 41.6 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 62, structural_boundaries: 27, branch: 18, doc: 11
- `wp-admin/includes/template.php` (PHP) | Magnitude: 2571.98 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 1065, state_mutation: 785, branch: 394, structural_boundaries: 186
- `wp-includes/js/wp-embed.js` (JAVASCRIPT) | Magnitude: 62.22 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 69, branch: 27, globals: 14, state_mutation: 9
- `wp-admin/includes/class-wp-application-passwords-list-table.php` (PHP) | Magnitude: 149.04 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 133, branch: 49, doc: 30, structural_boundaries: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `wp-includes/js/hoverIntent.js` (JAVASCRIPT) | Magnitude: 139.72 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 78, state_mutation: 41, structural_boundaries: 26, branch: 23
- `wp-includes/js/zxcvbn-async.js` (JAVASCRIPT) | Magnitude: 13.36 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 14, concurrency: 7, globals: 5, state_mutation: 4
- `wp-includes/js/tinymce/plugins/paste/plugin.js` (JAVASCRIPT) | Magnitude: 2974.64 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 2318, state_mutation: 904, structural_boundaries: 655, branch: 484
- `wp-includes/html-api/class-wp-html-active-formatting-elements.php` (PHP) | Magnitude: 108.56 | Delta: **0.078 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 56, state_mutation: 42, structural_boundaries: 28, doc: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `wp-admin/includes/class-automatic-upgrader-skin.php` (PHP) | Magnitude: 30.84 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 15, indent_tabs: 14, doc: 9, structural_boundaries: 5
- `wp-includes/customize/class-wp-sidebar-block-editor-control.php` (PHP) | Magnitude: 7.02 | Delta: **0.069 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 5, structural_boundaries: 3, state_mutation: 3, indent_tabs: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `wp-includes/html-api/class-wp-html-text-replacement.php` (PHP) | Magnitude: 9.42 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 12, indent_tabs: 8, api: 4, state_mutation: 3
- `wp-includes/html-api/class-wp-html-stack-event.php` (PHP) | Magnitude: 9.46 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 14, indent_tabs: 10, api: 4, state_mutation: 3
- `wp-includes/class-wp-session-tokens.php` (PHP) | Magnitude: 67.48 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 65, doc: 50, structural_boundaries: 26, args: 18
- `wp-includes/class-wp-dependency.php` (PHP) | Magnitude: 44.16 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 29, doc: 28, state_mutation: 20, api: 11
- `wp-includes/ms-deprecated.php` (PHP) | Magnitude: 27.96 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 19, indent_tabs: 18, state_mutation: 13, branch: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `wp-includes/class-wp-theme-json-schema.php` (PHP) | Magnitude: 39.14 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 27, indent_tabs: 23, doc: 12, structural_boundaries: 7
- `wp-includes/blocks/image/theme-rtl.css` (CSS) | Magnitude: 0.86 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 25, indent_spaces: 5, branch: 2, class_start: 2
- `wp-includes/blocks/image/theme.css` (CSS) | Magnitude: 0.86 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 25, indent_spaces: 5, branch: 2, class_start: 2
- `wp-includes/sodium_compat/src/Core32/Curve25519/Ge/Cached.php` (PHP) | Magnitude: 63.98 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: state_mutation: 46, indent_spaces: 28, doc: 14, structural_boundaries: 7
- `wp-includes/sodium_compat/src/Core32/Curve25519/Ge/P3.php` (PHP) | Magnitude: 63.98 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: state_mutation: 46, indent_spaces: 28, doc: 14, structural_boundaries: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `wp-includes/PHPMailer/DSNConfigurator.php` (PHP) | Magnitude: 163.12 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 131, state_mutation: 59, branch: 47, doc: 28
- `wp-includes/blocks/video.php` (PHP) | Magnitude: 10.64 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 10, branch: 5, doc: 5, structural_boundaries: 3
- `wp-includes/SimplePie/src/Net/IPv6.php` (PHP) | Magnitude: 153.26 | Delta: **0.151 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 86, indent_spaces: 78, branch: 26, structural_boundaries: 14
- `wp-includes/PHPMailer/POP3.php` (PHP) | Magnitude: 86.6 | Delta: **0.217 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 107, state_mutation: 33, doc: 25, structural_boundaries: 21
- `wp-includes/class-IXR.php` (PHP) | Magnitude: 10.52 | Delta: **0.364 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: ownership: 2, branch: 1, doc: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `wp-includes/js/codemirror/csslint.js` -> **Weston Ruter** (100.0% isolated ownership) | Magnitude: 5159.28
- `wp-includes/class-wp-xmlrpc-server.php` -> **Weston Ruter** (100.0% isolated ownership) | Magnitude: 2834.74
- `wp-includes/js/codemirror/esprima.js` -> **Weston Ruter** (100.0% isolated ownership) | Magnitude: 2235.4
- `wp-admin/includes/upgrade.php` -> **fabiankaegy** (100.0% isolated ownership) | Magnitude: 1930.04
- `wp-includes/comment-template.php` -> **Sergey Biryukov** (100.0% isolated ownership) | Magnitude: 1641.04

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `wp-includes/php-ai-client/src/Results/DTO/GenerativeAiResult.php` -> **Severity: 0.006** (Bridge: 0.0001 * Flux: 100.0%)
- `wp-includes/php-ai-client/src/Providers/DTO/ProviderMetadata.php` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 100.0%)
- `wp-includes/php-ai-client/src/Common/AbstractDataTransferObject.php` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)
- `wp-includes/php-ai-client/src/Providers/Http/DTO/Request.php` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)
- `wp-includes/php-ai-client/src/Providers/Http/Exception/ServerException.php` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `wp-includes/php-ai-client/src/Common/Contracts/AiClientExceptionInterface.php` -> **Severity: 201.362** (Blast Radius: 18.073 * Doc Risk: 11.1416%)
- `wp-includes/php-ai-client/src/Common/Exception/InvalidArgumentException.php` -> **Severity: 164.138** (Blast Radius: 14.732 * Doc Risk: 11.1416%)
- `wp-includes/php-ai-client/src/Common/AbstractEnum.php` -> **Severity: 150.052** (Blast Radius: 8.392 * Doc Risk: 17.8804%)
- `wp-includes/php-ai-client/src/Common/AbstractDataTransferObject.php` -> **Severity: 106.406** (Blast Radius: 5.951 * Doc Risk: 17.8804%)
- `wp-includes/php-ai-client/src/Common/Exception/RuntimeException.php` -> **Severity: 67.964** (Blast Radius: 6.1 * Doc Risk: 11.1416%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
