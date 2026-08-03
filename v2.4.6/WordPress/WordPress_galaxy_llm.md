# ARCHITECTURAL_BRIEF: WordPress
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_php/WordPress` |
| **Timestamp** | `2026-08-03T19:30:58.672191+00:00` |
| **Scan Duration** | `13.07s` |
| **Git Branch** | `master` |
| **Git Commit** | `29c8a8073453a3e6f735206fd6d3988a573c0128` |
| **Git Remote** | `https://github.com/WordPress/WordPress.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1893 malicious artifacts.

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
| Total Artifacts | 5167 |
| Analyzed Artifacts (Scanned) | 2648 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2519 |
| Total LOC | 419690 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 51.2% |
| Dominant Lang | PHP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5582 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.196 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.1287 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 18 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PHP | 1674 | 234961 | 63.2% |
| CSS | 445 | 78573 | 16.8% |
| JAVASCRIPT | 219 | 83276 | 8.3% |
| JSON | 165 | 22514 | 6.2% |
| HTML | 59 | 350 | 2.2% |
| PLAINTEXT | 52 | 3 | 2.0% |
| XML | 31 | 13 | 1.2% |
| MARKDOWN | 3 | 0 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `7.053`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 2156 | 81.4% |
| file_cluster_13 | 238 | 9.0% |
| file_cluster_2 | 69 | 2.6% |
| file_cluster_0 | 31 | 1.2% |
| file_cluster_17 | 23 | 0.9% |
| file_cluster_7 | 23 | 0.9% |
| file_cluster_15 | 15 | 0.6% |
| file_cluster_11 | 8 | 0.3% |
| file_cluster_9 | 7 | 0.3% |
| file_cluster_4 | 5 | 0.2% |
| file_cluster_1 | 4 | 0.2% |
| Unknown | 3 | 0.1% |
| file_cluster_6 | 2 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 52 | 2.0% |
| Static: Minified & Vendor Opaque Mass | 12 | 0.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2519*

**Composition by Extension & Reason:**
- `.css`: 553x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 14x Excluded (Machine-Generated Source Code Signature: 801 LOC), 4x Excluded (Saturation: Line 6 exceeds 500 chars)
- `.js`: 454x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded (Saturation: Line 11 exceeds 500 chars), 2x Excluded (Saturation: Line 3 exceeds 500 chars)
- `.svg`: 334x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 63 LOC), 1x Excluded (Machine-Generated Source Code Signature: 132 LOC)
- `.woff2`: 315x Excluded (Explicitly Denied Extension: '.woff2')
- `.php`: 176x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Saturation: Line 36 exceeds 500 chars), 2x Excluded (Saturation: Line 14 exceeds 500 chars)
- `.png`: 161x Excluded (Explicitly Denied Extension: '.png')
- `.scss`: 110x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 3 exceeds 500 chars), 1x Excluded (Saturation: Line 10 exceeds 500 chars)
- `.jpg`: 85x Excluded (Explicitly Denied Extension: '.jpg')
- `.gif`: 62x Excluded (Explicitly Denied Extension: '.gif')
- `.woff`: 54x Excluded (Explicitly Denied Extension: '.woff')
- `.webp`: 46x Excluded (Explicitly Denied Extension: '.webp')
- `.txt`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ttf`: 13x Excluded (Explicitly Denied Extension: '.ttf')
- `.json`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Static Asset Blob without Intent: 1726 LOC), 1x Excluded (Massive Static Asset Blob: 6791 LOC)
- `.eot`: 7x Excluded (Explicitly Denied Extension: '.eot')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 27.1 | 24.4 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 30.2 | 15.6 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 22.5 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 20.0 | 2.3 | 2.3 |
| API Exposure | 0.0 | 12.6 | 1.6 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 1.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 62.0 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 64.0 | 0.4 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 87.0 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 2.7 | 0.5 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 3.9 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 25.4 | 15.9 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 9.9 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 7.6 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `wp-admin/includes/ajax-actions.php` (Hits: 223)
- `wp-admin/includes/class-custom-image-header.php` (Hits: 130)
- `wp-includes/theme.php` (Hits: 68)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **InvalidArgumentException.php** (`wp-includes/php-ai-client/src/Common/Exception/InvalidArgumentException.php`) — 40 inbound connections
2. **Message.php** (`wp-includes/php-ai-client/src/Messages/DTO/Message.php`) — 22 inbound connections
3. **AbstractDataTransferObject.php** (`wp-includes/php-ai-client/src/Common/AbstractDataTransferObject.php`) — 21 inbound connections
4. **InvalidArgument.php** (`wp-includes/Requests/src/Exception/InvalidArgument.php`) — 16 inbound connections
5. **RuntimeException.php** (`wp-includes/php-ai-client/src/Common/Exception/RuntimeException.php`) — 16 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **blocks-json.php** (`wp-includes/blocks/blocks-json.php`) — 1033 outbound dependencies
2. **update-core.php** (`wp-admin/includes/update-core.php`) — 866 outbound dependencies
3. **script-loader.php** (`wp-includes/script-loader.php`) — 431 outbound dependencies
4. **wp-settings.php** (`wp-settings.php`) — 338 outbound dependencies
5. **post.php** (`wp-includes/post.php`) — 225 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `next_visitable_token` (@ `wp-includes/html-api/class-wp-html-processor.php`) -> Impact: **3304.4** | LOC: 1967
  * *Intent:* * that the document will eventually be placed in. It becomes important * when special elements have different rules than others, such as inside * a TE...
- `QuicktimeParseAtom` (@ `wp-includes/ID3/module.audio-video.quicktime.php`) -> Impact: **2765.4** | LOC: 1203
- `_updateDatepicker` (@ `wp-includes/js/jquery/ui/datepicker.js`) -> Impact: **2697.9** | LOC: 1279
- `define` (@ `wp-includes/js/plupload/moxie.js`) -> Impact: **2694.1** | LOC: 2443
- `parse` (@ `wp-includes/js/codemirror/csslint.js`) -> Impact: **2654.0** | LOC: 1603
- `search_theme_directories` (@ `wp-includes/theme.php`) -> Impact: **2102.2** | LOC: 1246
  * *Intent:* /**
- `PropertyValuePart` (@ `wp-includes/js/codemirror/csslint.js`) -> Impact: **1951.0** | LOC: 514
- `get_custom_logo` (@ `wp-includes/general-template.php`) -> Impact: **1699.0** | LOC: 1596
  * *Intent:* * @since 3.0.0 * @since 6.6.0 Added `required_username` and `required_password` arguments. * * @param array $args { * Optional. Array of options to co...
- `_encode` (@ `wp-includes/class-json.php`) -> Impact: **1587.9** | LOC: 477
  * *Intent:* * * Brief example of use: * * <code> * // create a new instance of Services_JSON * $json = new Services_JSON(); * * // convert a complex value to JSON...
- `isEqual` (@ `wp-includes/js/underscore.js`) -> Impact: **1577.3** | LOC: 1200

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `embed` (@ `wp-includes/SimplePie/src/Enclosure.php`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * Get the language * * @link http://tools.ietf.org/html/rfc3066 * @return string|null Language code as per RFC 3066 */
- `__construct` (@ `wp-includes/SimplePie/src/File.php`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * @var ?string Body of the HTTP response * @deprecated Use `get_body_content()` method. */
- `value` (@ `wp-includes/SimplePie/src/HTTP/Parser.php`) -> **O(2^N) [Recursive]**
- `extension` (@ `wp-includes/SimplePie/src/Locator.php`) -> **O(2^N) [Recursive]**
- `get_rel_link` (@ `wp-includes/SimplePie/src/Locator.php`) -> **O(2^N) [Recursive]**
- `parse` (@ `wp-includes/SimplePie/src/Parser.php`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * @return void
- `parse_hcard` (@ `wp-includes/SimplePie/src/Parser.php`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * @return array{string, string}
- `diff` (@ `wp-includes/Text/Diff/Engine/shell.php`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * Class used internally by Diff to actually compute the diffs. * * This class uses the Unix `diff` program via shell_exec to compute the * differe...
- `_encode` (@ `wp-includes/class-json.php`) -> **O(2^N) [Recursive]**
  * *Intent:* * * Brief example of use: * * <code> * // create a new instance of Services_JSON * $json = new Services_JSON(); * * // convert a complex value to JSON...
- `convertEmptyArraysToObjects` (@ `wp-includes/php-ai-client/src/Common/AbstractDataTransferObject.php`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `ge_double_scalarmult_vartime` (@ `wp-includes/sodium_compat/src/Core32/Curve25519.php`) -> DB Complexity: **689**
- `get_attachment_link` (@ `wp-includes/link-template.php`) -> DB Complexity: **606**
  * *Intent:* // Protected posts don't have plain links if getting a sample URL.
- `get_custom_logo` (@ `wp-includes/general-template.php`) -> DB Complexity: **396**
  * *Intent:* * @since 3.0.0 * @since 6.6.0 Added `required_username` and `required_password` arguments. * * @param array $args { * Optional. Array of options to co...
- `search_theme_directories` (@ `wp-includes/theme.php`) -> DB Complexity: **369**
  * *Intent:* /**
- `sc25519_mul` (@ `wp-includes/sodium_compat/src/Core/Curve25519.php`) -> DB Complexity: **342**
- `parse` (@ `wp-includes/js/codemirror/csslint.js`) -> DB Complexity: **323**
- `fe_mul` (@ `wp-includes/sodium_compat/src/Core/Curve25519.php`) -> DB Complexity: **318**
- `force_balance_tags` (@ `wp-includes/formatting.php`) -> DB Complexity: **291**
- `isEqual` (@ `wp-includes/js/underscore.js`) -> DB Complexity: **272**
- `sc_reduce` (@ `wp-includes/sodium_compat/src/Core/Curve25519.php`) -> DB Complexity: **249**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `wp-includes` | 249 | 89659.96 | 31.14% | 48.48% |
| `wp-admin/includes` | 105 | 47024.32 | 35.98% | 45.3% |
| `wp-includes/js` | 47 | 28313.25 | 38.75% | 40.17% |
| `wp-content/themes/twentytwentyfive/patterns` | 92 | 15324.52 | 51.55% | 0.0% |
| `wp-admin/js` | 49 | 14603.74 | 28.26% | 38.32% |
| `wp-includes/SimplePie/src` | 22 | 14099.26 | 32.23% | 59.68% |
| `wp-includes/js/jquery/ui` | 36 | 13969.14 | 51.43% | 34.0% |
| `wp-admin` | 91 | 12022.59 | 41.0% | 2.27% |
| `wp-includes/ID3` | 17 | 11217.0 | 35.43% | 21.43% |
| `wp-includes/js/codemirror` | 4 | 11168.88 | 39.45% | 18.51% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `wp-admin/includes/class-automatic-upgrader-skin.php` -> **100.0%** Exposure
- `wp-admin/includes/class-wp-internal-pointers.php` -> **100.0%** Exposure
- `wp-admin/includes/class-wp-privacy-policy-content.php` -> **100.0%** Exposure
- `wp-admin/includes/ms-deprecated.php` -> **100.0%** Exposure
- `wp-admin/includes/noop.php` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `wp-admin/admin-footer.php` -> **100.0%** Exposure
- `wp-admin/admin.php` -> **100.0%** Exposure
- `wp-admin/comment.php` -> **100.0%** Exposure
- `wp-admin/edit-comments.php` -> **100.0%** Exposure
- `wp-admin/edit-form-advanced.php` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `wp-content/themes/twentytwentyone/style-rtl.css` -> **1** Orphaned Functions | **78** Duplicates
- `wp-content/themes/twentytwentyone/style.css` -> **0** Orphaned Functions | **78** Duplicates
- `wp-includes/js/tinymce/themes/modern/theme.js` -> **0** Orphaned Functions | **59** Duplicates
- `wp-includes/js/tinymce/themes/inlite/theme.js` -> **0** Orphaned Functions | **58** Duplicates
- `wp-admin/includes/deprecated.php` -> **55** Orphaned Functions | **2** Duplicates

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
14. **`wp-admin/includes/image.php`** -> AI Confidence: **99.48%**
15. **`wp-admin/includes/meta-boxes.php`** -> AI Confidence: **99.48%**
16. **`wp-admin/includes/plugin-install.php`** -> AI Confidence: **99.48%**
17. **`wp-admin/includes/theme-install.php`** -> AI Confidence: **99.48%**
18. **`wp-admin/includes/update-core.php`** -> AI Confidence: **99.48%**
19. **`wp-admin/install.php`** -> AI Confidence: **99.48%**
20. **`wp-admin/media-upload.php`** -> AI Confidence: **99.48%**
21. **`wp-admin/network.php`** -> AI Confidence: **99.48%**
22. **`wp-admin/options-general.php`** -> AI Confidence: **99.48%**
23. **`wp-admin/options-permalink.php`** -> AI Confidence: **99.48%**
24. **`wp-admin/options.php`** -> AI Confidence: **99.48%**
25. **`wp-admin/plugins.php`** -> AI Confidence: **99.48%**
26. **`wp-admin/themes.php`** -> AI Confidence: **99.48%**
27. **`wp-admin/upgrade.php`** -> AI Confidence: **99.48%**
28. **`wp-admin/user-new.php`** -> AI Confidence: **99.48%**
29. **`wp-content/themes/twentyeleven/functions.php`** -> AI Confidence: **99.48%**
30. **`wp-content/themes/twentyfifteen/index.php`** -> AI Confidence: **99.48%**
31. **`wp-content/themes/twentyfourteen/index.php`** -> AI Confidence: **99.48%**
32. **`wp-content/themes/twentysixteen/index.php`** -> AI Confidence: **99.48%**
33. **`wp-includes/ID3/module.audio-video.quicktime.php`** -> AI Confidence: **99.48%**
34. **`wp-includes/ID3/module.audio-video.riff.php`** -> AI Confidence: **99.48%**
35. **`wp-includes/ID3/module.audio.ac3.php`** -> AI Confidence: **99.48%**
36. **`wp-includes/SimplePie/src/IRI.php`** -> AI Confidence: **99.48%**
37. **`wp-includes/block-supports/duotone.php`** -> AI Confidence: **99.48%**
38. **`wp-includes/blocks/blocks-json.php`** -> AI Confidence: **99.48%**
39. **`wp-includes/blocks/term-template.php`** -> AI Confidence: **99.48%**
40. **`wp-includes/cache-compat.php`** -> AI Confidence: **99.48%**
41. **`wp-includes/class-IXR.php`** -> AI Confidence: **99.48%**
42. **`wp-includes/class-walker-page.php`** -> AI Confidence: **99.48%**
43. **`wp-includes/class-wp-comment-query.php`** -> AI Confidence: **99.48%**
44. **`wp-includes/class-wp-editor.php`** -> AI Confidence: **99.48%**
45. **`wp-includes/class-wp-meta-query.php`** -> AI Confidence: **99.48%**
46. **`wp-includes/default-filters.php`** -> AI Confidence: **99.48%**
47. **`wp-includes/default-widgets.php`** -> AI Confidence: **99.48%**
48. **`wp-includes/feed-rss2-comments.php`** -> AI Confidence: **99.48%**
49. **`wp-includes/html-api/class-wp-html-doctype-info.php`** -> AI Confidence: **99.48%**
50. **`wp-login.php`** -> AI Confidence: **99.48%**
51. **`wp-signup.php`** -> AI Confidence: **99.48%**
52. **`wp-admin/includes/class-wp-automatic-updater.php`** -> AI Confidence: **99.39%**
53. **`wp-admin/includes/class-wp-ms-themes-list-table.php`** -> AI Confidence: **99.39%**
54. **`wp-admin/includes/class-wp-posts-list-table.php`** -> AI Confidence: **99.39%**
55. **`wp-admin/includes/class-wp-themes-list-table.php`** -> AI Confidence: **99.39%**
56. **`wp-admin/includes/image-edit.php`** -> AI Confidence: **99.39%**
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
78. **`wp-includes/class-wp-http-streams.php`** -> AI Confidence: **99.39%**
79. **`wp-includes/class-wp-query.php`** -> AI Confidence: **99.39%**
80. **`wp-includes/class-wp-site-query.php`** -> AI Confidence: **99.39%**
81. **`wp-includes/class-wp-term-query.php`** -> AI Confidence: **99.39%**
82. **`wp-includes/general-template.php`** -> AI Confidence: **99.39%**
83. **`wp-includes/media.php`** -> AI Confidence: **99.39%**
84. **`wp-includes/pluggable.php`** -> AI Confidence: **99.39%**
85. **`wp-includes/update.php`** -> AI Confidence: **99.39%**
86. **`wp-includes/widgets.php`** -> AI Confidence: **99.39%**
87. **`wp-load.php`** -> AI Confidence: **99.39%**
88. **`wp-admin/includes/class-wp-plugin-install-list-table.php`** -> AI Confidence: **99.35%**
89. **`wp-includes/class-wp-customize-control.php`** -> AI Confidence: **99.35%**
90. **`wp-includes/class-wp-date-query.php`** -> AI Confidence: **99.35%**
91. **`wp-includes/html-api/class-wp-html-processor.php`** -> AI Confidence: **99.35%**
92. **`wp-includes/post-template.php`** -> AI Confidence: **99.35%**
93. **`wp-admin/admin-ajax.php`** -> AI Confidence: **99.34%**
94. **`wp-admin/authorize-application.php`** -> AI Confidence: **99.34%**
95. **`wp-admin/nav-menus.php`** -> AI Confidence: **99.34%**
96. **`wp-admin/network/settings.php`** -> AI Confidence: **99.34%**
97. **`wp-admin/network/upgrade.php`** -> AI Confidence: **99.34%**
98. **`wp-admin/options-discussion.php`** -> AI Confidence: **99.34%**
99. **`wp-admin/post.php`** -> AI Confidence: **99.34%**
100. **`wp-admin/revision.php`** -> AI Confidence: **99.34%**
101. **`wp-admin/upload.php`** -> AI Confidence: **99.34%**
102. **`wp-includes/Text/Diff/Engine/native.php`** -> AI Confidence: **99.34%**
103. **`wp-includes/block-supports/typography.php`** -> AI Confidence: **99.34%**
104. **`wp-includes/compat-utf8.php`** -> AI Confidence: **99.34%**
105. **`wp-includes/feed-atom-comments.php`** -> AI Confidence: **99.34%**
106. **`wp-includes/feed-rdf.php`** -> AI Confidence: **99.34%**
107. **`wp-includes/nav-menu-template.php`** -> AI Confidence: **99.34%**
108. **`wp-includes/widgets/class-wp-widget-archives.php`** -> AI Confidence: **99.34%**
109. **`wp-includes/widgets/class-wp-widget-categories.php`** -> AI Confidence: **99.34%**
110. **`wp-includes/widgets/class-wp-widget-meta.php`** -> AI Confidence: **99.34%**
111. **`wp-includes/widgets/class-wp-widget-recent-posts.php`** -> AI Confidence: **99.34%**
112. **`wp-includes/widgets/class-wp-widget-tag-cloud.php`** -> AI Confidence: **99.34%**
113. **`wp-includes/wp-diff.php`** -> AI Confidence: **99.34%**
114. **`wp-activate.php`** -> AI Confidence: **99.32%**
115. **`wp-admin/admin-functions.php`** -> AI Confidence: **99.32%**
116. **`wp-admin/custom-background.php`** -> AI Confidence: **99.32%**
117. **`wp-admin/custom-header.php`** -> AI Confidence: **99.32%**
118. **`wp-admin/edit-comments.php`** -> AI Confidence: **99.32%**
119. **`wp-admin/edit-form-comment.php`** -> AI Confidence: **99.32%**
120. **`wp-admin/edit.php`** -> AI Confidence: **99.32%**
121. **`wp-admin/import.php`** -> AI Confidence: **99.32%**
122. **`wp-admin/includes/network.php`** -> AI Confidence: **99.32%**
123. **`wp-admin/link.php`** -> AI Confidence: **99.32%**
124. **`wp-admin/ms-delete-site.php`** -> AI Confidence: **99.32%**
125. **`wp-admin/network/site-settings.php`** -> AI Confidence: **99.32%**
126. **`wp-admin/network/site-themes.php`** -> AI Confidence: **99.32%**
127. **`wp-admin/network/site-users.php`** -> AI Confidence: **99.32%**
128. **`wp-admin/network/sites.php`** -> AI Confidence: **99.32%**
129. **`wp-admin/network/users.php`** -> AI Confidence: **99.32%**
130. **`wp-admin/options-media.php`** -> AI Confidence: **99.32%**
131. **`wp-admin/options-writing.php`** -> AI Confidence: **99.32%**
132. **`wp-admin/plugin-editor.php`** -> AI Confidence: **99.32%**
133. **`wp-admin/theme-editor.php`** -> AI Confidence: **99.32%**
134. **`wp-admin/users.php`** -> AI Confidence: **99.32%**
135. **`wp-content/themes/twentyfourteen/inc/widgets.php`** -> AI Confidence: **99.32%**
136. **`wp-content/themes/twentyfourteen/page-templates/full-width.php`** -> AI Confidence: **99.32%**
137. **`wp-content/themes/twentyfourteen/page.php`** -> AI Confidence: **99.32%**
138. **`wp-content/themes/twentyfourteen/single.php`** -> AI Confidence: **99.32%**
139. **`wp-content/themes/twentytwentyone/index.php`** -> AI Confidence: **99.32%**
140. **`wp-includes/block-bindings/term-data.php`** -> AI Confidence: **99.32%**
141. **`wp-includes/class-wp-oembed.php`** -> AI Confidence: **99.32%**
142. **`wp-links-opml.php`** -> AI Confidence: **99.32%**
143. **`wp-admin/includes/class-core-upgrader.php`** -> AI Confidence: **99.31%**
144. **`wp-admin/includes/class-language-pack-upgrader.php`** -> AI Confidence: **99.31%**
145. **`wp-admin/includes/class-plugin-installer-skin.php`** -> AI Confidence: **99.31%**
146. **`wp-admin/includes/class-theme-installer-skin.php`** -> AI Confidence: **99.31%**
147. **`wp-admin/includes/class-theme-upgrader.php`** -> AI Confidence: **99.31%**
148. **`wp-admin/includes/class-wp-comments-list-table.php`** -> AI Confidence: **99.31%**
149. **`wp-admin/includes/class-wp-community-events.php`** -> AI Confidence: **99.31%**
150. **`wp-admin/includes/class-wp-filesystem-direct.php`** -> AI Confidence: **99.31%**
151. **`wp-admin/includes/class-wp-filesystem-ftpext.php`** -> AI Confidence: **99.31%**
152. **`wp-admin/includes/class-wp-filesystem-ssh2.php`** -> AI Confidence: **99.31%**
153. **`wp-admin/includes/class-wp-list-table.php`** -> AI Confidence: **99.31%**
154. **`wp-admin/includes/class-wp-media-list-table.php`** -> AI Confidence: **99.31%**
155. **`wp-admin/includes/class-wp-plugins-list-table.php`** -> AI Confidence: **99.31%**
156. **`wp-admin/includes/class-wp-screen.php`** -> AI Confidence: **99.31%**
157. **`wp-admin/includes/class-wp-site-health-auto-updates.php`** -> AI Confidence: **99.31%**
158. **`wp-admin/includes/class-wp-site-health.php`** -> AI Confidence: **99.31%**
159. **`wp-admin/includes/class-wp-terms-list-table.php`** -> AI Confidence: **99.31%**
160. **`wp-admin/includes/class-wp-upgrader.php`** -> AI Confidence: **99.31%**
161. **`wp-admin/includes/dashboard.php`** -> AI Confidence: **99.31%**
162. **`wp-admin/includes/file.php`** -> AI Confidence: **99.31%**
163. **`wp-admin/includes/plugin.php`** -> AI Confidence: **99.31%**
164. **`wp-admin/includes/privacy-tools.php`** -> AI Confidence: **99.31%**
165. **`wp-admin/includes/revision.php`** -> AI Confidence: **99.31%**
166. **`wp-admin/includes/schema.php`** -> AI Confidence: **99.31%**
167. **`wp-admin/includes/template.php`** -> AI Confidence: **99.31%**
168. **`wp-admin/includes/theme.php`** -> AI Confidence: **99.31%**
169. **`wp-admin/includes/update.php`** -> AI Confidence: **99.31%**
170. **`wp-admin/install-helper.php`** -> AI Confidence: **99.31%**
171. **`wp-admin/load-styles.php`** -> AI Confidence: **99.31%**
172. **`wp-admin/network/site-new.php`** -> AI Confidence: **99.31%**
173. **`wp-admin/press-this.php`** -> AI Confidence: **99.31%**
174. **`wp-admin/privacy-policy-guide.php`** -> AI Confidence: **99.31%**
175. **`wp-admin/site-health.php`** -> AI Confidence: **99.31%**
176. **`wp-admin/widgets-form-blocks.php`** -> AI Confidence: **99.31%**
177. **`wp-content/themes/twentyeleven/inc/theme-options.php`** -> AI Confidence: **99.31%**
178. **`wp-content/themes/twentyfifteen/inc/back-compat.php`** -> AI Confidence: **99.31%**
179. **`wp-content/themes/twentyfourteen/functions.php`** -> AI Confidence: **99.31%**
180. **`wp-content/themes/twentyfourteen/inc/back-compat.php`** -> AI Confidence: **99.31%**
181. **`wp-content/themes/twentynineteen/functions.php`** -> AI Confidence: **99.31%**
182. **`wp-content/themes/twentynineteen/inc/back-compat.php`** -> AI Confidence: **99.31%**
183. **`wp-content/themes/twentyseventeen/inc/back-compat.php`** -> AI Confidence: **99.31%**
184. **`wp-content/themes/twentysixteen/inc/back-compat.php`** -> AI Confidence: **99.31%**
185. **`wp-content/themes/twentyten/functions.php`** -> AI Confidence: **99.31%**
186. **`wp-content/themes/twentythirteen/functions.php`** -> AI Confidence: **99.31%**
187. **`wp-content/themes/twentythirteen/inc/back-compat.php`** -> AI Confidence: **99.31%**
188. **`wp-content/themes/twentytwelve/functions.php`** -> AI Confidence: **99.31%**
189. **`wp-includes/ID3/module.audio-video.asf.php`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `wp-includes/class-wp-token-map.php` -> **0.0131%** Exposure
- `wp-includes/js/codemirror/esprima.js` -> **0.0008%** Exposure
- `wp-admin/js/word-count.js` -> **0.0003%** Exposure
- `wp-includes/js/wp-emoji-loader.js` -> **0.0002%** Exposure
### Exploit Generation Surface
- `wp-admin/includes/class-ftp-pure.php` -> **100.0%** Exposure
- `wp-admin/includes/class-wp-list-table.php` -> **100.0%** Exposure
- `wp-admin/includes/class-wp-site-health.php` -> **100.0%** Exposure
- `wp-admin/includes/file.php` -> **100.0%** Exposure
- `wp-admin/includes/network.php` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `wp-admin/import.php` -> **100.0%** Exposure
- `wp-admin/includes/class-wp-site-health.php` -> **100.0%** Exposure
- `wp-includes/Requests/src/Transport/Curl.php` -> **100.0%** Exposure
- `wp-includes/SimplePie/src/Cache/MySQL.php` -> **100.0%** Exposure
- `wp-includes/SimplePie/src/Locator.php` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `wp-admin/includes/class-theme-upgrader.php` -> **100.0%** Exposure
- `wp-admin/includes/class-walker-nav-menu-edit.php` -> **100.0%** Exposure
- `wp-admin/includes/class-wp-automatic-updater.php` -> **100.0%** Exposure
- `wp-admin/includes/class-wp-debug-data.php` -> **100.0%** Exposure
- `wp-admin/includes/class-wp-privacy-data-export-requests-list-table.php` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `195` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `12949` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `wp-includes/SimplePie/src/Cache/MySQL.php` (PHP) -> Cumulative Risk: **869.36**
- **Archetype:** `file_cluster_8` (Distance: 13.354 IQR)
- **Magnitude:** 552.86 | **LOC:** 345 | **CtrlFlow:** 58.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `save` (Impact: 157.3), `load` (Impact: 105.6), `__construct` (Impact: 47.8)

### 2. `wp-includes/SimplePie/src/Locator.php` (PHP) -> Cumulative Risk: **822.37**
- **Archetype:** `file_cluster_13` (Distance: 14.197 IQR)
- **Magnitude:** 1252.46 | **LOC:** 479 | **CtrlFlow:** 57.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `search_elements_by_tag` (Impact: 184.4), `extension` (Impact: 183.4), `get_rel_link` (Impact: 170.4)

### 3. `wp-includes/js/tinymce/plugins/paste/plugin.js` (JAVASCRIPT) -> Cumulative Risk: **819.31**
- **Archetype:** `file_cluster_4` (Distance: 13.896 IQR)
- **Magnitude:** 3682.84 | **LOC:** 2368 | **CtrlFlow:** 42.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `isWordContent` (Impact: 420.8), `registerEventHandlers` (Impact: 165.4), `removeWebKitStyles` (Impact: 157.1)

### 4. `wp-includes/IXR/class-IXR-client.php` (PHP) -> Cumulative Risk: **818.99**
- **Archetype:** `file_cluster_8` (Distance: 13.288 IQR)
- **Magnitude:** 272.2 | **LOC:** 173 | **CtrlFlow:** 47.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `query` (Impact: 90.7), `__construct` (Impact: 51.6), `getResponse` (Impact: 2.8)

### 5. `wp-includes/SimplePie/src/Enclosure.php` (PHP) -> Cumulative Risk: **799.74**
- **Archetype:** `file_cluster_8` (Distance: 14.304 IQR)
- **Magnitude:** 1698.7 | **LOC:** 1218 | **CtrlFlow:** 50.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `embed` (Impact: 576.2), `__construct` (Impact: 392.9), `get_duration` (Impact: 19.0)

### 6. `wp-includes/SimplePie/src/Net/IPv6.php` (PHP) -> Cumulative Risk: **799.66**
- **Archetype:** `file_cluster_9` (Distance: 13.762 IQR)
- **Magnitude:** 273.16 | **LOC:** 225 | **CtrlFlow:** 68.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `compress` (Impact: 79.5), `uncompress` (Impact: 62.0), `check_ipv6` (Impact: 24.4)

### 7. `wp-includes/SimplePie/src/Sanitize.php` (PHP) -> Cumulative Risk: **788.93**
- **Archetype:** `file_cluster_13` (Distance: 14.272 IQR)
- **Magnitude:** 1378.64 | **LOC:** 832 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `sanitize` (Impact: 301.6), `do_strip_htmltags` (Impact: 115.8), `strip_htmltags` (Impact: 112.4)

### 8. `wp-includes/php-ai-client/src/Operations/DTO/GenerativeAiOperation.php` (PHP) -> Cumulative Risk: **787.61**
- **Archetype:** `file_cluster_13` (Distance: 13.356 IQR)
- **Magnitude:** 145.16 | **LOC:** 151 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `fromArray` (Impact: 24.7), `getJsonSchema` (Impact: 21.2), `toArray` (Impact: 14.3)

### 9. `wp-includes/SimplePie/src/Source.php` (PHP) -> Cumulative Risk: **784.61**
- **Archetype:** `file_cluster_8` (Distance: 14.445 IQR)
- **Magnitude:** 976.98 | **LOC:** 513 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `get_links` (Impact: 165.6), `get_authors` (Impact: 85.0), `get_contributors` (Impact: 71.6)

### 10. `wp-includes/sodium_compat/src/Core32/Int32.php` (PHP) -> Cumulative Risk: **784.58**
- **Archetype:** `file_cluster_8` (Distance: 14.831 IQR)
- **Magnitude:** 993.82 | **LOC:** 873 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `shiftRight` (Impact: 68.9), `mulInt32Fast` (Impact: 62.1), `mulIntFast` (Impact: 41.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `wp-includes/js/wplink.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.73 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.488 IQR)
- **Top Global Matches:** file_cluster_8: 12.73, file_cluster_11: 13.095, file_cluster_15: 13.101
- **Magnitude:** 13422.89 | **LOC:** 805 | **CtrlFlow:** 73.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (79.057%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 164`, `structural_boundaries: 60`, `args: 59`, `func_start: 45`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 286`
* *Architecture:* `io: 6`, `concurrency: 17`
* *Defense:* `safety: 31`, `doc: 1`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.341
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/js/codemirror/csslint.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.572 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.254 IQR)
- **Top Global Matches:** file_cluster_11: 14.572, file_cluster_0: 14.603, file_cluster_13: 14.628
- **Magnitude:** 8243.18 | **LOC:** 10859 | **CtrlFlow:** 65.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 323
- **Risk Profile:** Cognitive Load (47.779%), Tech Debt (74.044%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 2654.0 | O(2^N) | DB: 323)
  * `PropertyValuePart` (Impact: 1951.0 | O(2^N) | DB: 108)
  * `atRuleToken` (Impact: 337.3 | O(N^6) | DB: 22)
  * `_getToken` (Impact: 298.0 | O(N^6) | DB: 27)
    * *Intent:* /** * Helper method used for parsing subparts of a style sheet. * @return {void} * @method _verifyEn...
  * `readEscape` (Impact: 91.4 | O(N^5) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 738`, `structural_boundaries: 382`, `args: 242`, `func_start: 188`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 1737`, `dead_code: 16`, `planned_debt: 2`, `fragile_debt: 24`, `duplicate_logic: 20`
* *Architecture:* `io: 16`, `api: 30`, `concurrency: 6`, `import: 47`
* *Defense:* `safety: 162`, `doc: 339`, `sync_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.341
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Combinator, SyntaxUnit, Properties, ValidationTypes, Specificity, EventTarget, Matcher, TokenStreamBase...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/js/tinymce/themes/inlite/theme.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.025 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.899 IQR)
- **Top Global Matches:** file_cluster_8: 14.025, file_cluster_11: 14.178, file_cluster_15: 14.278
- **Magnitude:** 6571.64 | **LOC:** 9793 | **CtrlFlow:** 43.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (99.9403%), Tech Debt (27.0874%)
**Top Internal Functions/Classes:**
  * `recalc` (Impact: 299.0 | O(2^N) | DB: 14)
  * `init` (Impact: 85.7 | O(N^4) | DB: 10)
  * `postRender` (Impact: 64.6 | O(N^5) | DB: 7)
  * `init` (Impact: 58.1 | O(N^4) | DB: 4)
  * `parseBox` (Impact: 46.6 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1659`, `structural_boundaries: 2171`, `args: 1131`, `func_start: 1074`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 12`, `state_mutation: 3829`, `duplicate_logic: 58`
* *Architecture:* `io: 9`, `api: 15`, `concurrency: 70`
* *Defense:* `safety: 455`, `immutability_locks: 4`, `cleanup: 47`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.341
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/js/tinymce/themes/modern/theme.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.006 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.909 IQR)
- **Top Global Matches:** file_cluster_8: 14.006, file_cluster_11: 14.167, file_cluster_15: 14.269
- **Magnitude:** 6449.76 | **LOC:** 9608 | **CtrlFlow:** 45.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (28.1539%)
**Top Internal Functions/Classes:**
  * `addContextualToolbars` (Impact: 170.6 | O(N^4) | DB: 23)
  * `init` (Impact: 85.7 | O(N^4) | DB: 10)
  * `createMenu` (Impact: 80.4 | O(N^4) | DB: 7)
  * `render` (Impact: 75.0 | O(N^4) | DB: 8)
  * `postRender` (Impact: 64.6 | O(N^5) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1678`, `structural_boundaries: 2053`, `args: 1075`, `func_start: 1006`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 12`, `state_mutation: 3724`, `duplicate_logic: 59`
* *Architecture:* `io: 7`, `api: 11`, `concurrency: 57`
* *Defense:* `safety: 454`, `immutability_locks: 7`, `cleanup: 47`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.341
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-content/themes/twentytwenty/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.341
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-content/themes/twentytwentyone/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.341
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/certificates/ca-bundle.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.341
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/js/plupload/moxie.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.219 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 3.955 IQR)
- **Top Global Matches:** file_cluster_11: 14.219, file_cluster_15: 14.326, file_cluster_0: 14.427
- **Magnitude:** 4708.58 | **LOC:** 9905 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 225
- **Risk Profile:** Cognitive Load (47.0763%), Tech Debt (19.7273%)
**Top Internal Functions/Classes:**
  * `define` (Impact: 2694.1 | O(2^N) | DB: 225)
  * `define` (Impact: 701.0 | O(2^N) | DB: 60)
  * `SLONG` (Impact: 95.6 | O(2^N) | DB: 21)
  * `define` (Impact: 83.4 | O(N^1) | DB: 4)
  * `define` (Impact: 68.5 | O(N^1) | DB: 15)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 558`, `structural_boundaries: 392`, `args: 261`, `func_start: 227`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 3`, `state_mutation: 843`, `dead_code: 23`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 6`, `orphaned_logic: 1`
* *Architecture:* `io: 15`, `api: 8`, `concurrency: 17`, `import: 2`
* *Defense:* `safety: 144`, `doc: 279`, `test: 1`, `cleanup: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.341
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/html-api/class-wp-html-processor.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.473 IQR)
- **Top Global Matches:** file_cluster_8: 13.473, file_cluster_7: 13.641, file_cluster_11: 13.784
- **Magnitude:** 4590.66 | **LOC:** 6746 | **CtrlFlow:** 69.2% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 207
- **Risk Profile:** Cognitive Load (48.8371%), Tech Debt (22.2352%)
**Top Internal Functions/Classes:**
  * `next_visitable_token` (Impact: 3304.4 | O(2^N) | DB: 207)
    * *Intent:* * that the document will eventually be placed in. It becomes important * when special elements have ...
  * `is_special` (Impact: 217.8 | O(N^1) | DB: 2)
    * *Intent:* /* * > A start tag whose tag name is "html" */
  * `next_tag` (Impact: 101.8 | O(N^1) | DB: 7)
    * *Intent:* /** * Stores context for why the parser bailed on unsupported HTML, if it did. * * @see self::get_un...
  * `__construct` (Impact: 69.0 | O(2^N) | DB: 15)
    * *Intent:* * // ----- Matches here, because IMG must be a direct child of the implicit BODY. * $processor->next...
  * `is_void` (Impact: 41.4 | O(N^1) | DB: 1)
    * *Intent:* /* * > Otherwise, if there is a node in the stack of open elements that is not either a * > dd eleme...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 816`, `structural_boundaries: 364`, `args: 48`, `func_start: 46`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 38`, `high_risk_execution: 1`, `state_mutation: 717`, `planned_debt: 26`, `orphaned_logic: 2`
* *Architecture:* `api: 27`
* *Defense:* `safety: 37`, `doc: 163`, `test: 8`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.341
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` $tag_name
				), p>', d.', 
		if (
			'html' === $namespace &&
			in_array( $tag_name, the HTML `<table><td>` stops at tags `TABLE`, `TR`, such, 'TEXTAREA'...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-admin/user-edit.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.01 IQR)
- **Top Global Matches:** file_cluster_8: 11.01, file_cluster_13: 11.373, file_cluster_7: 11.467
- **Magnitude:** 4095.27 | **LOC:** 1026 | **CtrlFlow:** 77.8% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (38.9921%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 221`, `structural_boundaries: 63`, `args: 2`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 78`
* *Architecture:* `io: 6`, `import: 5`
* *Defense:* `safety: 4`, `doc: 18`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.341
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` admin.php', d)', d fields are indicated, admin-header.php', translation-install.php', s HTTPS, >
											<p class="description" id="new_application_password_name_desc"><?php _e( 'Required to create an Application Password, but not to update the user.'...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/js/jquery/ui/datepicker.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.113 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.046 IQR)
- **Top Global Matches:** file_cluster_8: 14.113, file_cluster_11: 14.21, file_cluster_17: 14.241
- **Magnitude:** 3884.86 | **LOC:** 2241 | **CtrlFlow:** 79.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 226
- **Risk Profile:** Cognitive Load (78.3295%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_updateDatepicker` (Impact: 2697.9 | O(2^N) | DB: 226)
  * `Datepicker` (Impact: 262.7 | O(N^2) | DB: 78)
  * `_showDatepicker` (Impact: 50.1 | O(N^1) | DB: 1)
  * `datepicker_getZindex` (Impact: 19.1 | O(N^1) | DB: 1)
  * `_doKeyPress` (Impact: 14.5 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 575`, `structural_boundaries: 153`, `args: 87`, `func_start: 98`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 6`, `state_mutation: 789`, `dead_code: 2`
* *Architecture:* `concurrency: 6`
* *Defense:* `safety: 141`, `doc: 34`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.341
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/ID3/module.audio-video.quicktime.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.685 IQR)
- **Top Global Matches:** file_cluster_8: 13.685, file_cluster_0: 13.869, file_cluster_7: 13.882
- **Magnitude:** 3808.9 | **LOC:** 3213 | **CtrlFlow:** 87.7% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 119
- **Risk Profile:** Cognitive Load (48.4385%), Tech Debt (20.2642%)
**Top Internal Functions/Classes:**
  * `QuicktimeParseAtom` (Impact: 2765.4 | O(N^4) | DB: 119)
  * `Analyze` (Impact: 265.3 | O(N^2) | DB: 47)
    * *Intent:* /** audio-video.quicktime * return all parsed data from all atoms if true, otherwise just returned p...
  * `CopyToAppropriateCommentsSection` (Impact: 31.5 | O(N^1) | DB: 11)
  * `search_tag_by_pair` (Impact: 30.0 | O(2^N) | DB: 5)
    * *Intent:* // https://exiftool.org/TagNames/Nikon.html // Nikon-specific QuickTime tags found in the NCDT atom ...
  * `search_tag_by_key` (Impact: 23.0 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 556`, `structural_boundaries: 78`, `args: 23`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 55`, `state_mutation: 554`, `dead_code: 8`, `planned_debt: 1`, `fragile_debt: 4`, `orphaned_logic: 4`
* *Architecture:* `io: 4`, `api: 24`
* *Defense:* `safety: 70`, `doc: 87`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.341
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Dependency(GETID3_INCLUDEPATH.'module.audio.mp3.php',  The placeholder atom has a type of kWideAtomPlaceholderType ( 'wide' ).
					break, s 16 bytes. Therefore, Dependency(GETID3_INCLUDEPATH.'module.tag.nikon-nctg.php', d,  In this way, s the 4+4 bytes for key_size and key_namespace

						$info['quicktime']['temp_meta_key_names'][($keys_index_base + $i)] = $atom_structure['keys'][($keys_index_base + $i)]['key_value'], d'...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/js/tinymce/plugins/paste/plugin.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.896 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.29 IQR)
- **Top Global Matches:** file_cluster_4: 13.896, file_cluster_8: 13.949, file_cluster_11: 14.009
- **Magnitude:** 3682.84 | **LOC:** 2368 | **CtrlFlow:** 42.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (15.1253%)
**Top Internal Functions/Classes:**
  * `isWordContent` (Impact: 420.8 | O(N^3) | DB: 25)
  * `registerEventHandlers` (Impact: 165.4 | O(N^3) | DB: 9)
  * `removeWebKitStyles` (Impact: 157.1 | O(2^N) | DB: 19)
  * `setup` (Impact: 113.0 | O(N^4) | DB: 6)
  * `all` (Impact: 62.1 | O(N^6) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 484`, `structural_boundaries: 655`, `args: 363`, `func_start: 343`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 4`, `state_mutation: 906`, `duplicate_logic: 7`
* *Architecture:* `io: 1`, `api: 32`, `concurrency: 190`, `import: 5`
* *Defense:* `safety: 178`, `immutability_locks: 2`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.341
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` timers, promise-polyfill, browser.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-admin/js/customize-controls.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.388 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.481 IQR)
- **Top Global Matches:** file_cluster_8: 13.388, file_cluster_15: 13.455, file_cluster_7: 13.568
- **Magnitude:** 3487.76 | **LOC:** 9390 | **CtrlFlow:** 68.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 173
- **Risk Profile:** Cognitive Load (31.8155%), Tech Debt (23.1556%)
**Top Internal Functions/Classes:**
  * `initialize` (Impact: 1049.1 | O(2^N) | DB: 31)
  * `initializeNewQuery` (Impact: 828.6 | O(N^2) | DB: 173)
  * `initialize` (Impact: 265.2 | O(2^N) | DB: 15)
  * `areElementListsEqual` (Impact: 139.4 | O(N^2) | DB: 14)
  * `embed` (Impact: 92.9 | O(N^2) | DB: 9)
    * *Intent:* /** * Return browser supported `transitionend` event name.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 696`, `structural_boundaries: 326`, `args: 343`, `func_start: 229`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 664`, `planned_debt: 5`, `fragile_debt: 1`, `duplicate_logic: 8`, `orphaned_logic: 6`
* *Architecture:* `io: 2`, `concurrency: 23`
* *Defense:* `safety: 178`, `doc: 443`, `sync_locks: 2`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.341
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/general-template.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.618 IQR)
- **Top Global Matches:** file_cluster_8: 15.618, file_cluster_7: 15.709, file_cluster_13: 15.84
- **Magnitude:** 3447.16 | **LOC:** 5438 | **CtrlFlow:** 72.1% | **Authorship Centralization:** 47.1%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 396
- **Risk Profile:** Cognitive Load (47.8558%), Tech Debt (10.3689%)
**Top Internal Functions/Classes:**
  * `get_custom_logo` (Impact: 1699.0 | O(2^N) | DB: 396)
    * *Intent:* * @since 3.0.0 * @since 6.6.0 Added `required_username` and `required_password` arguments. * * @para...
  * `get_bloginfo` (Impact: 108.2 | O(N^1) | DB: 29)
  * `wp_login_form` (Impact: 33.8 | O(N^1) | DB: 8)
    * *Intent:* /** * Fires before the specified template part file is loaded. * * The dynamic portion of the hook n...
  * `get_site_icon_url` (Impact: 33.3 | O(2^N) | DB: 9)
  * `wp_register` (Impact: 17.1 | O(N^1) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 421`, `structural_boundaries: 163`, `args: 63`, `func_start: 61`
* *Risk/State:* `high_risk_execution: 17`, `state_mutation: 1410`, `orphaned_logic: 5`
* *Architecture:* `io: 4`, `import: 1`
* *Defense:* `safety: 34`, `doc: 334`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.341
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` by default is 1. The 'mid_size' argument is how many
 * numbers to either side of current page, 
		sprintf( __( 'Required fields are marked %s' ), p>', esc_attr( $args['id_remember'] ), 'id_username'       => 'user_login', 'remember'          => true, 
	do_action( "get_template_part_$slug", 'label_username'    => __( 'Username or Email Address' )...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/sodium_compat/src/Compat.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.817 IQR)
- **Top Global Matches:** file_cluster_8: 12.817, file_cluster_0: 12.836, file_cluster_7: 12.861
- **Magnitude:** 3378.58 | **LOC:** 4531 | **CtrlFlow:** 41.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 77
- **Risk Profile:** Cognitive Load (28.4655%), Tech Debt (41.6572%)
**Top Internal Functions/Classes:**
  * `crypto_pwhash_str_needs_rehash` (Impact: 1101.8 | O(N^5) | DB: 77)
    * *Intent:* /** * Decrypt a message previously encrypted with crypto_box().
  * `crypto_kx` (Impact: 150.1 | O(2^N) | DB: 1)
  * `crypto_generichash_final` (Impact: 88.4 | O(2^N) | DB: 5)
    * *Intent:* * * Algorithm: * XChaCha20-Poly1305 * * This mode uses a 64-bit random nonce with a 64-bit counter. ...
  * `crypto_generichash` (Impact: 81.8 | O(2^N) | DB: 3)
  * `crypto_aead_chacha20poly1305_decrypt` (Impact: 81.1 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 344`, `structural_boundaries: 490`, `args: 109`, `func_start: 109`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 389`, `dead_code: 1`, `planned_debt: 9`, `orphaned_logic: 27`
* *Architecture:* `io: 5`, `api: 112`
* *Defense:* `safety: 21`, `doc: 640`, `test: 2`, `immutability_locks: 105`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.341
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` 
        ParagonIE_Sodium_Core_Util::declareScalarType($ciphertext, 'string', 1, 
    public static function crypto_box_seal_open(
        $ciphertext
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/functions.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.406 IQR)
- **Top Global Matches:** file_cluster_8: 15.406, file_cluster_7: 15.504, file_cluster_13: 15.59
- **Magnitude:** 3043.14 | **LOC:** 9285 | **CtrlFlow:** 65.4% | **Authorship Centralization:** 30.8%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 173
- **Risk Profile:** Cognitive Load (38.3286%), Tech Debt (58.9209%)
**Top Internal Functions/Classes:**
  * `do_enclose` (Impact: 302.1 | O(N^1) | DB: 173)
    * *Intent:* /** * Filters the number formatted based on the locale. * * @since 2.8.0 * @since 4.9.0 The `$number...
  * `human_readable_duration` (Impact: 87.7 | O(2^N) | DB: 9)
    * *Intent:* * will be used instead. * * Note that due to the way WP typically generates a sum of timestamp and o...
  * `_wp_json_sanity_check` (Impact: 64.5 | O(2^N) | DB: 9)
  * `_wp_die_process_input` (Impact: 55.7 | O(N^1) | DB: 11)
  * `_default_wp_die_handler` (Impact: 55.3 | O(N^1) | DB: 18)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 615`, `structural_boundaries: 326`, `args: 144`, `func_start: 110`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 31`, `high_risk_execution: 1`, `state_mutation: 1406`, `dead_code: 3`, `planned_debt: 3`, `fragile_debt: 2`, `orphaned_logic: 41`
* *Architecture:* `io: 15`, `api: 2`, `concurrency: 30`, `import: 4`
* *Defense:* `safety: 68`, `doc: 494`, `test: 4`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.341
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` max-age=0, 
function wp_find_hierarchy_loop_tortoise_hare( $callback, 
	if ( is_serialized( $data, 
	do_action( 'deprecated_file_included', 0, class-IXR.php', version.php', 413 => 'Request Entity Too Large'...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/theme.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.301 IQR)
- **Top Global Matches:** file_cluster_8: 14.301, file_cluster_7: 14.483, file_cluster_13: 14.533
- **Magnitude:** 3000.92 | **LOC:** 4425 | **CtrlFlow:** 66.0% | **Authorship Centralization:** 41.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 369
- **Risk Profile:** Cognitive Load (46.3478%), Tech Debt (8.0326%)
**Top Internal Functions/Classes:**
  * `search_theme_directories` (Impact: 2102.2 | O(2^N) | DB: 369)
    * *Intent:* /**
  * `create_initial_theme_features` (Impact: 90.6 | O(N^2) | DB: 14)
  * `wp_get_themes` (Impact: 50.8 | O(N^1) | DB: 17)
    * *Intent:* /** * Theme, template, and stylesheet functions.
  * `_wp_keep_alive_customize_changeset_depen` (Impact: 30.2 | O(N^1) | DB: 5)
    * *Intent:* /** * Checks if random header image is in use.
  * `register_theme_directory` (Impact: 14.6 | O(N^1) | DB: 4)
    * *Intent:* /** * Whether a child theme is in use. * * @since 3.0.0 * @since 6.5.0 Makes use of global template ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 345`, `structural_boundaries: 178`, `args: 58`, `func_start: 54`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 614`, `planned_debt: 1`
* *Architecture:* `io: 68`, `api: 9`, `concurrency: 1`, `import: 4`
* *Defense:* `safety: 74`, `doc: 165`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.341
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` 'categories'         => array(
				'categories', ments = validate_theme_requirements( $stylesheet, s postMessage and CORS (if the site is cross domain).
			b[c] += ( window.postMessage && request ? ' ' : ' no-' ) + cs, class-custom-background.php', 'link_linkedin'   => array(
				'title' => _x( 'LinkedIn', d in
 *                                    the Themes REST API schema. Intended for developers.
 *     @type bool|array $show_in_rest 
 *         Whether this feature should be included in the Themes REST API endpoint.
 *         Defaults to not being included. When registering an 'array' or 'object' type, the "properties" keyword.' ), array(
					'title' => _x( 'Search'...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/js/tinymce/plugins/lists/plugin.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.709 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.758 IQR)
- **Top Global Matches:** file_cluster_8: 13.709, file_cluster_11: 13.873, file_cluster_17: 13.931
- **Magnitude:** 2869.5 | **LOC:** 2149 | **CtrlFlow:** 31.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (13.3138%)
**Top Internal Functions/Classes:**
  * `createTextBlock` (Impact: 89.0 | O(N^4) | DB: 5)
  * `getSelectedTextBlocks` (Impact: 54.0 | O(N^3) | DB: 10)
  * `resolveBookmark` (Impact: 50.5 | O(N^3) | DB: 4)
  * `findNextCaretContainer` (Impact: 48.4 | O(N^2) | DB: 3)
  * `mergeLiElements` (Impact: 43.7 | O(N^2) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 368`, `structural_boundaries: 789`, `args: 313`, `func_start: 328`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 1155`, `duplicate_logic: 5`
* *Architecture:* `io: 2`, `api: 15`
* *Defense:* `safety: 105`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.341
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/js/codemirror/esprima.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.35 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.452 IQR)
- **Top Global Matches:** file_cluster_8: 14.35, file_cluster_11: 14.46, file_cluster_13: 14.627
- **Magnitude:** 2861.3 | **LOC:** 6709 | **CtrlFlow:** 65.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 56
- **Risk Profile:** Cognitive Load (57.3279%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `scanTemplate` (Impact: 309.5 | O(N^6) | DB: 56)
  * `lexJSX` (Impact: 264.7 | O(N^6) | DB: 31)
  * `scanXHTMLEntity` (Impact: 202.6 | O(N^6) | DB: 11)
  * `isRegexStart` (Impact: 115.9 | O(N^5) | DB: 19)
  * `getQualifiedElementName` (Impact: 87.8 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 321`, `structural_boundaries: 166`, `args: 55`, `func_start: 44`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 1005`
* *Architecture:* `api: 33`
* *Defense:* `safety: 103`, `doc: 47`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.341
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` foo
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/link-template.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 16.458 IQR)
- **Top Global Matches:** file_cluster_8: 16.458, file_cluster_7: 16.494, file_cluster_13: 16.619
- **Magnitude:** 2815.34 | **LOC:** 4905 | **CtrlFlow:** 64.4% | **Authorship Centralization:** 35.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 606
- **Risk Profile:** Cognitive Load (47.5893%), Tech Debt (12.4109%)
**Top Internal Functions/Classes:**
  * `get_attachment_link` (Impact: 777.2 | O(N^1) | DB: 606)
    * *Intent:* // Protected posts don't have plain links if getting a sample URL.
  * `wp_force_plain_post_permalink` (Impact: 24.3 | O(N^1) | DB: 7)
    * *Intent:* /** * Retrieves a trailing-slashed string if the site is set for adding trailing slashes. * * Condit...
  * `get_permalink` (Impact: 21.0 | O(N^1) | DB: 7)
  * `permalink_anchor` (Impact: 19.2 | O(N^1) | DB: 3)
    * *Intent:* /** * Filters the display of the permalink for the current post. * * @since 1.5.0 * @since 4.4.0 Add...
  * `get_theme_file_path` (Impact: 14.1 | O(N^1) | DB: 7)
    * *Intent:* /** * Displays relational links for the posts adjacent to the current post for single post pages. *
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 447`, `structural_boundaries: 247`, `args: 99`, `func_start: 99`
* *Risk/State:* `state_mutation: 1856`, `orphaned_logic: 8`
* *Architecture:* None
* *Defense:* `safety: 67`, `doc: 630`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.341
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` $in_same_term, 
	$where = apply_filters( "get_$adjacent_post_where", :
	 *
	 *  - `get_next_post_sort`
	 *  - `get_previous_post_sort`
	 *
	 * @since 2.5.0
	 * @since 4.4.0 Added the `$post` parameter.
	 * @since 4.9.0 Added the `$order` parameter.
	 * @since 6.9.0 Adds ID sort to ensure deterministic ordering for posts with identical dates.
	 *
	 * @param string $order_by The `ORDER BY` clause in the SQL.
	 * @param WP_Post $post    WP_Post object.
	 * @param string  $order   Sort order. 'DESC' for previous post, private posts belonging to the current user, 
	return apply_filters( "$adjacent_post_rel_link", 
function includes_url( $path = '', *                            'login_post', 
		$private_states = get_post_stati( array( 'private' => true )...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-admin/includes/media.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.985 IQR)
- **Top Global Matches:** file_cluster_8: 14.985, file_cluster_13: 15.112, file_cluster_11: 15.155
- **Magnitude:** 2783.04 | **LOC:** 3905 | **CtrlFlow:** 71.8% | **Authorship Centralization:** 46.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 67
- **Risk Profile:** Cognitive Load (41.8205%), Tech Debt (8.7985%)
**Top Internal Functions/Classes:**
  * `attachment_submitbox_metadata` (Impact: 249.6 | O(N^1) | DB: 26)
  * `edit_form_image_editor` (Impact: 194.6 | O(N^1) | DB: 25)
  * `media_upload_library_form` (Impact: 167.8 | O(N^1) | DB: 67)
  * `wp_read_video_metadata` (Impact: 103.7 | O(2^N) | DB: 6)
  * `get_compat_media_markup` (Impact: 87.2 | O(N^1) | DB: 44)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 857`, `structural_boundaries: 336`, `args: 51`, `func_start: 45`
* *Risk/State:* `safety_bypasses: 69`, `high_risk_execution: 5`, `state_mutation: 1159`, `dead_code: 1`, `fragile_debt: 2`
* *Architecture:* `io: 45`, `api: 22`, `import: 4`
* *Defense:* `safety: 139`, `doc: 207`, `test: 2`, `immutability_locks: 10`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.341
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` $post_data = array(), getid3.php', 
	$args = apply_filters( 'get_media_item_args', '\n', '', button>.' ), d to get the `created_timestamp` value.
	$id3->options_audiovideo_quicktime_ReturnAtomData = true, *                      'alignleft'...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/sodium_compat/src/Core32/Curve25519.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.448 IQR)
- **Top Global Matches:** file_cluster_8: 14.448, file_cluster_7: 14.544, file_cluster_13: 14.728
- **Magnitude:** 2706.42 | **LOC:** 3162 | **CtrlFlow:** 40.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 689
- **Risk Profile:** Cognitive Load (40.7321%), Tech Debt (9.4275%)
**Top Internal Functions/Classes:**
  * `ge_double_scalarmult_vartime` (Impact: 226.5 | O(N^6) | DB: 689)
  * `slide` (Impact: 99.2 | O(N^6) | DB: 10)
  * `fe_pow22523` (Impact: 65.3 | O(N^3) | DB: 51)
  * `ge_select` (Impact: 52.4 | O(N^6) | DB: 15)
  * `ge_frombytes_negate_vartime` (Impact: 46.3 | O(N^5) | DB: 23)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 145`, `args: 42`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1860`, `dead_code: 10`, `orphaned_logic: 5`
* *Architecture:* `api: 42`
* *Defense:* `safety: 2`, `doc: 411`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.341
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/class-wp-xmlrpc-server.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.064 IQR)
- **Top Global Matches:** file_cluster_8: 15.064, file_cluster_7: 15.162, file_cluster_13: 15.225
- **Magnitude:** 2511.14 | **LOC:** 7229 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 83.3%
- **Algorithmic:** O(N) | **DB Complexity:** 166
- **Risk Profile:** Cognitive Load (36.455%), Tech Debt (19.4821%)
**Top Internal Functions/Classes:**
  * `mw_newPost` (Impact: 530.7 | O(N^1) | DB: 166)
    * *Intent:* * * @param array $args { * Method arguments. Note: arguments must be ordered as documented. * * @typ...
  * `wp_newComment` (Impact: 80.0 | O(N^1) | DB: 16)
  * `wp_getRevisions` (Impact: 34.5 | O(N^1) | DB: 9)
  * `wp_editProfile` (Impact: 32.5 | O(N^1) | DB: 6)
    * *Intent:* /** * Prepares term data for return in an XML-RPC object. * * @param array|object $term The unprepar...
  * `wp_getPage` (Impact: 32.3 | O(N^1) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 491`, `structural_boundaries: 346`, `args: 57`, `func_start: 57`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 1138`, `dead_code: 1`, `fragile_debt: 2`, `orphaned_logic: 11`
* *Architecture:* `api: 51`, `import: 1`
* *Defense:* `safety: 129`, `doc: 279`, `immutability_locks: 31`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.341
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` 'mt.getTrackbackPings', 'wp.getPostStatusList', 'wp.newTerm', 'wp.getPageList', 'terms', 'custom_fields', false, 
			$fields = apply_filters( 'xmlrpc_default_posttype_fields'...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/class-wp-query.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.868 IQR)
- **Top Global Matches:** file_cluster_8: 14.868, file_cluster_7: 14.931, file_cluster_13: 14.968
- **Magnitude:** 2445.92 | **LOC:** 5114 | **CtrlFlow:** 71.5% | **Authorship Centralization:** 30.8%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 225
- **Risk Profile:** Cognitive Load (46.8542%), Tech Debt (9.012%)
**Top Internal Functions/Classes:**
  * `get_posts` (Impact: 1017.3 | O(2^N) | DB: 225)
    * *Intent:* * @type int $hour Hour of the day. Default empty. Accepts numbers 0-23. * @type int|bool $ignore_sti...
  * `parse_query` (Impact: 287.7 | O(N^1) | DB: 59)
    * *Intent:* /**
  * `parse_orderby` (Impact: 95.4 | O(N^1) | DB: 26)
  * `fill_query_vars` (Impact: 14.8 | O(N^1) | DB: 2)
    * *Intent:* /** * Signifies whether the current query is for a page. * * @since 1.5.0 * @var bool */
  * `parse_order` (Impact: 11.7 | O(N^1))
    * *Intent:* * @since 5.1.0 Introduced the `$meta_compare_key` parameter. * @since 5.3.0 Introduced the `$meta_ty...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 338`, `structural_boundaries: 135`, `args: 35`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 91`, `high_risk_execution: 4`, `state_mutation: 901`, `dead_code: 1`, `orphaned_logic: 2`
* *Architecture:* `api: 74`, `import: 2`
* *Defense:* `safety: 54`, `doc: 251`, `test: 1`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.341
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` $this, array( null, tag, array( 'LIMIT ' . get_option( 'posts_per_rss' ), 
		$search_columns = (array) apply_filters( 'post_search_columns', category, 
		$this->allow_query_attachment_by_filename = apply_filters( 'wp_allow_query_attachment_by_filename', * passed to the filter by reference. If WP_Query does not perform a database
		 * query...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `wp-includes/rest-api/class-wp-rest-request.php` (PHP) | Magnitude: 317.52 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 267, state_mutation: 134, doc: 96, structural_boundaries: 72
- `wp-includes/class-wp-matchesmapregex.php` (PHP) | Magnitude: 27.0 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 22, indent_tabs: 21, state_mutation: 11, structural_boundaries: 9
- `wp-includes/class-wp-theme-json-schema.php` (PHP) | Magnitude: 39.14 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 27, indent_tabs: 23, doc: 12, structural_boundaries: 9
- `wp-includes/sodium_compat/src/Core32/Poly1305/State.php` (PHP) | Magnitude: 360.2 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 284, state_mutation: 219, doc: 71, structural_boundaries: 18
- `wp-includes/class-wp-role.php` (PHP) | Magnitude: 30.02 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 22, doc: 21, structural_boundaries: 7, api: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `wp-admin/js/editor-expand.js` (JAVASCRIPT) | Magnitude: 467.76 | Delta: **0.053 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 495, branch: 144, events: 79, doc: 53
- `wp-admin/js/custom-background.js` (JAVASCRIPT) | Magnitude: 14.9 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 59, doc: 16, args: 11, closures: 11
- `wp-includes/class-wp-http-requests-hooks.php` (PHP) | Magnitude: 33.0 | Delta: **0.142 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 18, indent_tabs: 16, state_mutation: 14, structural_boundaries: 5
- `wp-includes/Requests/src/HookManager.php` (PHP) | Magnitude: 43.76 | Delta: **0.193 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 10, structural_boundaries: 4, state_mutation: 4, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `wp-includes/js/jquery/ui/sortable.js` (JAVASCRIPT) | Magnitude: 1426.02 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 1372, indent_tabs: 824, branch: 274, safety: 87
- `wp-includes/js/codemirror/csslint.js` (JAVASCRIPT) | Magnitude: 8243.18 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 3313, state_mutation: 1737, branch: 738, structural_boundaries: 382
- `wp-includes/class-json.php` (PHP) | Magnitude: 2092.56 | Delta: **0.087 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 404, indent_spaces: 395, branch: 140, structural_boundaries: 63
- `wp-includes/js/tinymce/utils/mctabs.js` (JAVASCRIPT) | Magnitude: 118.7 | Delta: **0.096 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 81, state_mutation: 28, branch: 19, args: 17
- `wp-includes/blocks/gallery.php` (PHP) | Magnitude: 201.5 | Delta: **0.105 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 124, indent_tabs: 83, branch: 32, doc: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `wp-includes/blocks/navigation-link.php` (PHP) | Magnitude: 342.08 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 186, state_mutation: 185, branch: 70, structural_boundaries: 27
- `wp-admin/import.php` (PHP) | Magnitude: 34.14 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 28, branch: 20, state_mutation: 18, io: 7
- `wp-admin/includes/schema.php` (PHP) | Magnitude: 205.44 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 144, indent_tabs: 116, doc: 31, branch: 22
- `wp-includes/class-wp-fatal-error-handler.php` (PHP) | Magnitude: 116.04 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 103, state_mutation: 37, branch: 35, doc: 23
- `wp-admin/includes/plugin.php` (PHP) | Magnitude: 823.54 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 647, state_mutation: 375, branch: 220, doc: 155

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `wp-includes/js/customize-loader.js` (JAVASCRIPT) | Magnitude: 167.72 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 128, state_mutation: 61, branch: 33, globals: 22
- `wp-includes/js/customize-models.js` (JAVASCRIPT) | Magnitude: 83.42 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 74, state_mutation: 54, args: 13, closures: 13
- `wp-includes/js/mediaelement/wp-playlist.js` (JAVASCRIPT) | Magnitude: 341.6 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 264, indent_tabs: 143, branch: 26, args: 17
- `wp-includes/js/customize-base.js` (JAVASCRIPT) | Magnitude: 185.9 | Delta: **0.04 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 198, state_mutation: 72, doc: 61, structural_boundaries: 34
- `wp-admin/js/tags-box.js` (JAVASCRIPT) | Magnitude: 119.32 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 107, doc: 30, branch: 22, state_mutation: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `wp-includes/ID3/module.audio.mp3.php` (PHP) | Magnitude: 2187.94 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 776, state_mutation: 570, branch: 280, safety: 78
- `wp-admin/includes/comment.php` (PHP) | Magnitude: 194.56 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 103, state_mutation: 84, io: 32, branch: 28
- `xmlrpc.php` (PHP) | Magnitude: 20.16 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 6, doc: 3, branch: 2, io: 2
- `wp-admin/includes/class-wp-ms-themes-list-table.php` (PHP) | Magnitude: 454.2 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 295, state_mutation: 214, branch: 85, doc: 48
- `wp-admin/includes/class-wp-upgrader-skin.php` (PHP) | Magnitude: 173.12 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 117, state_mutation: 57, doc: 40, branch: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `wp-trackback.php` (PHP) | Magnitude: 69.2 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 55, indent_tabs: 30, branch: 29, io: 13
- `wp-includes/class-wp-customize-panel.php` (PHP) | Magnitude: 41.6 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 62, structural_boundaries: 27, branch: 18, doc: 11
- `wp-admin/includes/template.php` (PHP) | Magnitude: 2085.68 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 1065, state_mutation: 795, branch: 397, structural_boundaries: 190
- `wp-includes/js/wp-embed.js` (JAVASCRIPT) | Magnitude: 62.22 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 69, branch: 27, globals: 14, state_mutation: 9
- `wp-admin/includes/class-wp-application-passwords-list-table.php` (PHP) | Magnitude: 149.04 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 133, branch: 49, doc: 30, structural_boundaries: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `wp-content/themes/twentynineteen/js/priority-menu.js` (JAVASCRIPT) | Magnitude: 49.54 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 45, doc: 18, state_mutation: 14, structural_boundaries: 11
- `wp-includes/js/zxcvbn-async.js` (JAVASCRIPT) | Magnitude: 13.36 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 14, concurrency: 7, globals: 5, state_mutation: 4
- `wp-includes/js/tinymce/plugins/paste/plugin.js` (JAVASCRIPT) | Magnitude: 3682.84 | Delta: **0.053 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 2318, state_mutation: 906, structural_boundaries: 655, branch: 484
- `wp-includes/html-api/class-wp-html-active-formatting-elements.php` (PHP) | Magnitude: 113.76 | Delta: **0.079 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 56, state_mutation: 42, structural_boundaries: 28, doc: 20
- `wp-includes/js/hoverIntent.js` (JAVASCRIPT) | Magnitude: 126.82 | Delta: **0.373 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 78, state_mutation: 41, structural_boundaries: 26, branch: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `wp-admin/includes/class-automatic-upgrader-skin.php` (PHP) | Magnitude: 25.14 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
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
- `wp-content/themes/twentyfifteen/js/functions.js` (JAVASCRIPT) | Magnitude: 63.0 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 108, branch: 21, state_mutation: 17, events: 16
- `wp-includes/sodium_compat/src/Core32/Curve25519/Ge/Cached.php` (PHP) | Magnitude: 75.18 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: state_mutation: 46, indent_spaces: 28, doc: 14, structural_boundaries: 7
- `wp-includes/sodium_compat/src/Core32/Curve25519/Ge/P3.php` (PHP) | Magnitude: 75.18 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: state_mutation: 46, indent_spaces: 28, doc: 14, structural_boundaries: 7
- `wp-includes/class-wp-site-query.php` (PHP) | Magnitude: 399.64 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 261, state_mutation: 210, branch: 73, doc: 57
- `wp-includes/blocks/image/theme-rtl.css` (CSS) | Magnitude: 0.86 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 25, indent_spaces: 5, branch: 2, class_start: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `wp-includes/PHPMailer/DSNConfigurator.php` (PHP) | Magnitude: 340.52 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 131, state_mutation: 59, branch: 47, doc: 28
- `wp-includes/blocks/video.php` (PHP) | Magnitude: 10.64 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 10, branch: 5, doc: 5, structural_boundaries: 3
- `wp-includes/SimplePie/src/Net/IPv6.php` (PHP) | Magnitude: 273.16 | Delta: **0.154 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 86, indent_spaces: 78, branch: 30, structural_boundaries: 14
- `wp-includes/PHPMailer/POP3.php` (PHP) | Magnitude: 139.2 | Delta: **0.215 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 107, state_mutation: 33, doc: 25, structural_boundaries: 21
- `wp-includes/class-IXR.php` (PHP) | Magnitude: 10.52 | Delta: **0.364 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: ownership: 2, branch: 1, doc: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `wp-includes/js/codemirror/csslint.js` -> **Weston Ruter** (100.0% isolated ownership) | Magnitude: 8243.18
- `wp-admin/js/customize-controls.js` -> **joedolson** (100.0% isolated ownership) | Magnitude: 3487.76
- `wp-includes/sodium_compat/src/Compat.php` -> **Sergey Biryukov** (100.0% isolated ownership) | Magnitude: 3378.58
- `wp-includes/js/codemirror/esprima.js` -> **Weston Ruter** (100.0% isolated ownership) | Magnitude: 2861.3
- `wp-includes/class-wp-xmlrpc-server.php` -> **Weston Ruter** (83.3% isolated ownership) | Magnitude: 2511.14

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `wp-includes/php-ai-client/src/Providers/DTO/ProviderMetadata.php` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 100.0%)
- `wp-includes/php-ai-client/src/Providers/Models/DTO/ModelConfig.php` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 99.9336%)
- `wp-includes/php-ai-client/src/Common/AbstractDataTransferObject.php` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)
- `wp-includes/php-ai-client/src/Common/AbstractEnum.php` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)
- `wp-includes/php-ai-client/src/Providers/Http/DTO/Request.php` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `wp-includes/php-ai-client/src/Common/AbstractDataTransferObject.php` -> **Severity: 597.7** (Blast Radius: 5.977 * Doc Risk: 100.0%)
- `wp-includes/php-ai-client/src/Common/Contracts/AiClientExceptionInterface.php` -> **Severity: 427.272** (Blast Radius: 18.466 * Doc Risk: 23.1383%)
- `wp-includes/php-ai-client/src/Common/Exception/InvalidArgumentException.php` -> **Severity: 350.268** (Blast Radius: 15.138 * Doc Risk: 23.1383%)
- `wp-includes/php-ai-client/src/Messages/DTO/Message.php` -> **Severity: 259.6** (Blast Radius: 2.596 * Doc Risk: 100.0%)
- `wp-includes/php-ai-client/src/Results/DTO/GenerativeAiResult.php` -> **Severity: 160.5** (Blast Radius: 1.605 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
