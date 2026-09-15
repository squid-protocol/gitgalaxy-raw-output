# ARCHITECTURAL_BRIEF: wordpress
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/WordPress/WordPress.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
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
## 2. THE 13-POINT STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (EQUATIONS & CONTEXT)
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

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 6068 |
| Analyzed Artifacts (Scanned) | 2680 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3388 |
| Total LOC | 572466 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 44.2% |
| Dominant Lang | PHP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5641 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1977 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.3733 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 18 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PHP | 1688 | 338309 | 63.0% |
| CSS | 458 | 91560 | 17.1% |
| JAVASCRIPT | 220 | 119447 | 8.2% |
| JSON | 168 | 22785 | 6.3% |
| HTML | 59 | 350 | 2.2% |
| PLAINTEXT | 52 | 3 | 1.9% |
| XML | 32 | 12 | 1.2% |
| MARKDOWN | 3 | 0 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Flat Modular Platform` (z -0.85; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 34%, Data / Markup / Trivial 22%, Large Core Modules 16%, Interface Declarations Files 9%, I/O & Config Routines Files 5%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 2614 | 97.5% |
| Unknown | 3 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 52 | 1.9% |
| Static: Minified & Vendor Opaque Mass | 11 | 0.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3388*

**Composition by Extension & Reason:**
- `.css`: 1223x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 14x Excluded (Machine-Generated Source Code Signature: 814 LOC), 4x Excluded (Saturation: Line 6 exceeds 500 chars)
- `.js`: 506x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded (Saturation: Line 11 exceeds 500 chars), 2x Excluded (Saturation: Line 3 exceeds 500 chars)
- `.svg`: 332x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 63 LOC), 1x Excluded (Machine-Generated Source Code Signature: 132 LOC)
- `.woff2`: 315x Excluded (Explicitly Denied Extension: '.woff2')
- `.php`: 254x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded (Saturation: Line 36 exceeds 500 chars), 2x Excluded (Saturation: Line 26 exceeds 500 chars)
- `.png`: 160x Excluded (Explicitly Denied Extension: '.png')
- `.scss`: 109x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 3 exceeds 500 chars), 1x Excluded (Saturation: Line 10 exceeds 500 chars)
- `.jpg`: 85x Excluded (Explicitly Denied Extension: '.jpg')
- `.gif`: 62x Excluded (Explicitly Denied Extension: '.gif')
- `.woff`: 54x Excluded (Explicitly Denied Extension: '.woff')
- `.map`: 52x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.webp`: 46x Excluded (Explicitly Denied Extension: '.webp')
- `.json`: 21x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Static Asset Blob without Intent: 1726 LOC), 1x Excluded (Massive Static Asset Blob: 6791 LOC)
- `.txt`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ttf`: 13x Excluded (Explicitly Denied Extension: '.ttf')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 19.8 | 9.7 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 54.1 | 69.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 18.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 17.5 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 64.0 | 2.4 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.6 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 57.9 | 96.1 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 85.7 | 0.5 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 60.8 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.7 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 4.2 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 8.8 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 8050 | 747 | 6 | `wp-includes/class-wp-xmlrpc-server.php` |
| cleanup | 1419 | 380 | 1 | `wp-includes/ID3/module.tag.id3v2.php` |
| guards | 25019 | 1288 | 23 | `wp-includes/js/codemirror/esprima.js` |
| danger | 5459 | 589 | 4 | `wp-includes/ID3/module.tag.id3v2.php` |
| concurrency | 751 | 122 | 0 | `wp-includes/js/tinymce/plugins/paste/plugin.js` |
| connectivity | 8808 | 728 | 10 | `wp-content/themes/twentytwentyone/style-rtl.css` |
| io | 5557 | 619 | 4 | `wp-admin/includes/ajax-actions.php` |
| crypto | 0 | 0 | 0 | - |
| ipc | 117 | 47 | 0 | `wp-admin/includes/misc.php` |
| time | 729 | 190 | 0 | `wp-includes/js/jquery/ui/datepicker.js` |
| serialization | 235 | 119 | 0 | `wp-admin/js/image-edit.js` |
| regex | 2319 | 347 | 1 | `wp-includes/js/codemirror/esprima.js` |
| events | 3893 | 226 | 0 | `wp-includes/js/tinymce/themes/modern/theme.js` |
| tests | 90 | 13 | 0 | `wp-includes/js/codemirror/esprima.js` |
| docs | 26884 | 1962 | 25 | `wp-includes/js/media-views.js` |
| debt | 5860 | 797 | 5 | `wp-admin/includes/meta-boxes.php` |
| mutation | 130510 | 1771 | 105 | `wp-includes/js/tinymce/themes/inlite/theme.js` |
| dead_code | 5671 | 837 | 5 | `wp-includes/deprecated.php` |
| credential | 30 | 20 | 0 | `wp-includes/pluggable.php` |
| threat | 1715 | 277 | 1 | `wp-includes/js/codemirror/esprima.js` |
| ml_ai | 85 | 33 | 0 | `wp-login.php` |
| ui | 3611 | 513 | 2 | `wp-content/themes/twentytwentyone/style-rtl.css` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `wp-admin/includes/ajax-actions.php` (Hits: 369)
- `wp-admin/includes/class-custom-image-header.php` (Hits: 198)
- `wp-login.php` (Hits: 111)

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

- `encoding` **(Compute Cores)** (@ `wp-includes/SimplePie/src/Misc.php`) -> Impact: **1212.5** | LOC: 1312
  * *Intent:* /** * Normalize an encoding name * * This is automatically generated by create.php * * To generate it, run `php create.php` on the command line, and c...
- `QuicktimeParseAtom` **(Many-Argument Workhorses)** (@ `wp-includes/ID3/module.audio-video.quicktime.php`) -> Impact: **1165.5** | LOC: 1033
  * *Intent:* /** * @param string $atomname * @param int $atomsize * @param string $atom_data * @param int $baseoffset * @param array $atomHierarchy * @param bool $...
- `map_meta_cap` **(Many-Argument Workhorses)** (@ `wp-includes/capabilities.php`) -> Impact: **679.8** | LOC: 836
  * *Intent:* * @since 5.2.0 Added the `resume_plugin` and `resume_theme` capabilities. * @since 5.3.0 Formalized the existing and already documented `...$args` par...
- `parseEBML` **(Compute Cores)** (@ `wp-includes/ID3/module.audio-video.matroska.php`) -> Impact: **559.9** | LOC: 733
  * *Intent:* /** * @param array $info */
- `redirect_canonical` **(Many-Argument Workhorses)** (@ `wp-includes/canonical.php`) -> Impact: **509.8** | LOC: 808
  * *Intent:* * or query in an attempt to figure the correct page to go to. * * @since 2.3.0 * * @global WP_Rewrite $wp_rewrite WordPress rewrite component. * @glob...
- `ParseID3v2Frame` **(Compute Cores)** (@ `wp-includes/ID3/module.tag.id3v2.php`) -> Impact: **500.7** | LOC: 1161
  * *Intent:* /** * @param array $parsedFrame * * @return bool */
- `get_posts` **(Compute Cores)** (@ `wp-includes/class-wp-query.php`) -> Impact: **470.7** | LOC: 1774
  * *Intent:* /** * Retrieves an array of posts based on query variables. * * There are a few filters and actions that can be used to modify the post * database que...
- `init` **(Many-Argument Workhorses)** (@ `wp-includes/js/codemirror/csslint.js`) -> Impact: **420.1** | LOC: 1751
  * *Intent:* // initialization
- `xmlEncode` **(Compute Cores)** (@ `wp-includes/js/plupload/plupload.js`) -> Impact: **367.6** | LOC: 1695
  * *Intent:* /** * Encodes the specified string. * * @method xmlEncode * @static * @param {String} s String to encode. * @return {String} Encoded string. */
- `wp_insert_post` **(Many-Argument Workhorses)** (@ `wp-includes/post.php`) -> Impact: **349.4** | LOC: 707
  * *Intent:* * @type array $tax_input An array of taxonomy terms keyed by their taxonomy name. * If the taxonomy is hierarchical, the term list needs to be * eithe...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `wp-includes` | 250 | 136067.58 | 31.06% | 50.09% |
| `wp-admin/includes` | 104 | 55758.66 | 38.07% | 52.16% |
| `wp-includes/js` | 47 | 33449.59 | 46.1% | 27.96% |
| `wp-admin/js` | 49 | 21827.32 | 37.56% | 18.89% |
| `wp-includes/ID3` | 17 | 20502.58 | 57.88% | 13.93% |
| `wp-includes/rest-api/endpoints` | 45 | 16058.48 | 32.13% | 31.97% |
| `wp-includes/js/codemirror` | 5 | 13382.16 | 60.45% | 4.95% |
| `wp-includes/SimplePie/src` | 22 | 13069.72 | 35.64% | 60.15% |
| `wp-includes/js/jquery/ui` | 36 | 12058.22 | 58.85% | 32.53% |
| `wp-admin` | 91 | 9868.4 | 34.09% | 1.89% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `wp-admin/includes/class-wp-internal-pointers.php` -> **100.0%** Exposure
- `wp-admin/includes/ms-deprecated.php` -> **100.0%** Exposure
- `wp-admin/includes/noop.php` -> **100.0%** Exposure
- `wp-includes/SimplePie/src/HTTP/Psr7Response.php` -> **100.0%** Exposure
- `wp-includes/SimplePie/src/HTTP/RawTextResponse.php` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `wp-admin/admin-header.php` -> **100.0%** Exposure
- `wp-admin/comment.php` -> **100.0%** Exposure
- `wp-admin/edit-comments.php` -> **100.0%** Exposure
- `wp-admin/edit-form-blocks.php` -> **100.0%** Exposure
- `wp-admin/edit-tags.php` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `wp-includes/deprecated.php` -> **205** Orphaned Functions | **0** Duplicates
- `wp-includes/functions.php` -> **113** Orphaned Functions | **0** Duplicates
- `wp-includes/sodium_compat/src/Compat.php` -> **110** Orphaned Functions | **0** Duplicates
- `wp-admin/includes/ajax-actions.php` -> **94** Orphaned Functions | **0** Duplicates
- `wp-admin/includes/deprecated.php` -> **69** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `175` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `12945` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `wp-includes/js/jquery/ui/mouse.js` (JAVASCRIPT) -> Cumulative Risk: **710.42**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.22)
- **Magnitude:** 136.64 | **LOC:** 238 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9963%), Cognitive Load (92.8816%)
- **Heaviest Functions:** `_mouseMove` (Compute Cores, Impact: 32.1), `_mouseDown` (Defensive Guards, Impact: 21.6), `_mouseUp` (Defensive Guards, Impact: 6.9)

### 2. `wp-includes/js/backbone.js` (JAVASCRIPT) -> Cumulative Risk: **704.3**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.47)
- **Magnitude:** 1790.12 | **LOC:** 2158 | **CtrlFlow:** 32.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (98.4778%)
- **Heaviest Functions:** `set` (Compute Cores, Impact: 87.1), `sync` (Defensive Guards, Impact: 45.0), `offApi` (Many-Argument Workhorses, Impact: 44.9)

### 3. `wp-includes/js/quicktags.js` (JAVASCRIPT) -> Cumulative Risk: **674.89**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.53)
- **Magnitude:** 875.5 | **LOC:** 750 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.8772%), Tech Debt (92.2656%)
- **Heaviest Functions:** `_escape` (Compute Cores, Impact: 208.1), `QTags` (Defensive Guards, Impact: 40.7), `_domReady` (Defensive Guards, Impact: 19.5)

### 4. `wp-includes/js/tinymce/plugins/paste/plugin.js` (JAVASCRIPT) -> Cumulative Risk: **672.85**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.34)
- **Magnitude:** 2195.04 | **LOC:** 2368 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9817%)
- **Heaviest Functions:** `isWordContent` (Compute Cores, Impact: 165.5), `registerEventHandlers` (Many-Argument Workhorses, Impact: 85.5), `setup` (Many-Argument Workhorses, Impact: 47.0)

### 5. `wp-includes/js/hoverIntent.js` (JAVASCRIPT) -> Cumulative Risk: **671.28**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +1.23)
- **Magnitude:** 133.42 | **LOC:** 170 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9991%)
- **Heaviest Functions:** `hoverIntent` (Many-Argument Workhorses, Impact: 29.4), `handleHover` (Compute Cores, Impact: 13.7), `compare` (Many-Argument Workhorses, Impact: 7.7)

### 6. `wp-admin/js/privacy-tools.js` (JAVASCRIPT) -> Cumulative Risk: **661.79**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.63)
- **Magnitude:** 237.06 | **LOC:** 347 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9996%), Concurrency (99.989%)
- **Heaviest Functions:** `doNextErasure` (Callbacks & Closures, Impact: 21.1), `onErasureDoneSuccess` (Defensive Guards, Impact: 13.2), `doNextExport` (Callbacks & Closures, Impact: 12.3)

### 7. `wp-includes/js/tinymce/utils/form_utils.js` (JAVASCRIPT) -> Cumulative Risk: **644.38**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.52)
- **Magnitude:** 207.8 | **LOC:** 223 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.8292%), Safety Score (99.2827%)
- **Heaviest Functions:** `selectByValue` (Many-Argument Workhorses, Impact: 31.0), `addClassesToList` (Compute Cores, Impact: 9.9), `setBrowserDisabled` (Compute Cores, Impact: 9.6)

### 8. `wp-includes/js/underscore.js` (JAVASCRIPT) -> Cumulative Risk: **632.23**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.12)
- **Magnitude:** 1229.4 | **LOC:** 2047 | **CtrlFlow:** 29.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (96.109%)
- **Heaviest Functions:** `deepEq` (Many-Argument Workhorses, Impact: 110.2), `eq` (Defensive Guards, Impact: 20.8), `collectNonEnumProps` (Defensive Guards, Impact: 16.4)

### 9. `wp-admin/includes/class-ftp.php` (PHP) -> Cumulative Risk: **629.28**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.14)
- **Magnitude:** 1214.34 | **LOC:** 924 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.7777%)
- **Heaviest Functions:** `mget` (Many-Argument Workhorses, Impact: 35.9), `mput` (Many-Argument Workhorses, Impact: 35.6), `parselisting` (Compute Cores, Impact: 29.9)

### 10. `wp-includes/js/tinymce/plugins/wptextpattern/plugin.js` (JAVASCRIPT) -> Cumulative Risk: **625.7**
- **Archetype:** `file_cluster_4` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.12)
- **Magnitude:** 168.96 | **LOC:** 349 | **CtrlFlow:** 29.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9973%), Concurrency (99.3921%), Cognitive Load (87.4727%)
- **Heaviest Functions:** `inline` (I/O & Config Routines, Impact: 21.9), `enter` (Compute Cores, Impact: 18.9), `firstTextNode` (Defensive Guards, Impact: 15.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `wp-includes/js/wplink.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 13482.89 | **LOC:** 805 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.688%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 101 instances
* *Concurrency (weighted view):* 32
* *State Mutation (weighted view):* 331
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 164`, `structural_boundaries: 60`, `args: 59`, `func_start: 38`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 129`
* *Architecture:* `concurrency: 7`
* *Defense:* `safety: 31`, `doc: 1`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.338
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/js/codemirror/csslint.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 6814.08 | **LOC:** 10859 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (65.6422%), Tech Debt (24.7478%)
**Top Internal Functions/Classes:**
  * `init` **(Many-Argument Workhorses)** (Impact: 420.1)
    * *Intent:* // initialization
  * `prototype` **(Compute Cores)** (Impact: 297.2)
  * `PropertyValuePart` **(Many-Argument Workhorses)** (Impact: 280.8)
    * *Intent:* /** * Represents a single part of a CSS property value, meaning that it represents * just one part o...
  * `clone` **(Many-Argument Workhorses)** (Impact: 127.8)
    * *Intent:* * Caution: if `circular` is false and `parent` contains circular references, * your program may ente...
  * `parse` **(Defensive Guards)** (Impact: 113.4)
    * *Intent:* /** Simple recursive-descent grammar to build matchers from strings. */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 858 instances
* *Concurrency (weighted view):* 18
* *State Mutation (weighted view):* 2806
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1351`, `structural_boundaries: 851`, `args: 488`, `func_start: 337`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 1090`, `dead_code: 34`, `planned_debt: 4`, `fragile_debt: 26`, `duplicate_logic: 9`
* *Architecture:* `api: 49`, `concurrency: 3`, `import: 77`
* *Defense:* `safety: 392`, `doc: 206`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.338
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` EventTarget, StringReader, SyntaxError, SyntaxUnit, TokenStreamBase, Colors, Combinator, EventTarget...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/js/tinymce/themes/modern/theme.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 6519.46 | **LOC:** 9608 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (99.4794%), Tech Debt (11.0001%)
**Top Internal Functions/Classes:**
  * `recalc` **(Compute Cores)** (Impact: 94.9)
  * `recalc` **(Compute Cores)** (Impact: 67.4)
  * `addContextualToolbars` **(Compute Cores)** (Impact: 62.7)
  * `createMenu` **(Many-Argument Workhorses)** (Impact: 33.5)
  * `render` **(Many-Argument Workhorses)** (Impact: 33.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 1184 instances
* *High Risk Execution (weighted view):* 6
* *Concurrency (weighted view):* 47
* *State Mutation (weighted view):* 3778
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1638`, `structural_boundaries: 2087`, `args: 1075`, `func_start: 775`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 8`, `state_mutation: 1410`, `duplicate_logic: 12`, `unreferenced_by_name: 8`
* *Architecture:* `concurrency: 12`
* *Defense:* `safety: 454`, `immutability_locks: 2`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.338
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/js/codemirror/esprima.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 6470.3 | **LOC:** 6709 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (88.2994%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `isKeyword` **(Defensive Guards)** (Impact: 66.4)
    * *Intent:* // https://tc39.github.io/ecma262/#sec-keywords
  * `parseClassElement` **(Defensive Guards)** (Impact: 65.5)
    * *Intent:* // https://tc39.github.io/ecma262/#sec-class-definitions
  * `parseObjectProperty` **(Defensive Guards)** (Impact: 59.4)
  * `parseForStatement` **(Compute Cores)** (Impact: 57.3)
    * *Intent:* // https://tc39.github.io/ecma262/#sec-for-statement // https://tc39.github.io/ecma262/#sec-for-in-a...
  * `scanPunctuator` **(Defensive Guards)** (Impact: 57.0)
    * *Intent:* // https://tc39.github.io/ecma262/#sec-punctuators
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 33 instances
* *Amplified Cascading Flux:* 941 instances
* *High Risk Execution (weighted view):* 6
* *Concurrency (weighted view):* 210
* *State Mutation (weighted view):* 3439
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1553`, `structural_boundaries: 1420`, `args: 430`, `func_start: 315`
* *Risk/State:* `safety_bypasses: 30`, `high_risk_execution: 8`, `state_mutation: 1557`, `dead_code: 9`
* *Architecture:* `api: 123`, `concurrency: 45`
* *Defense:* `safety: 538`, `doc: 65`, `test: 77`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.338
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` foo
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/js/tinymce/themes/inlite/theme.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 6188.94 | **LOC:** 9793 | **CtrlFlow:** 16.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (99.2552%), Tech Debt (10.6307%)
**Top Internal Functions/Classes:**
  * `recalc` **(Compute Cores)** (Impact: 94.9)
  * `recalc` **(Compute Cores)** (Impact: 67.4)
  * `createFormatMenu` **(Compute Cores)** (Impact: 32.7)
  * `init` **(Defensive Guards)** (Impact: 30.3)
  * `showMenu` **(Defensive Guards)** (Impact: 28.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 1161 instances
* *High Risk Execution (weighted view):* 6
* *Concurrency (weighted view):* 55
* *State Mutation (weighted view):* 3731
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1619`, `structural_boundaries: 2205`, `args: 1131`, `func_start: 834`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 8`, `state_mutation: 1409`, `duplicate_logic: 12`, `unreferenced_by_name: 5`
* *Architecture:* `concurrency: 15`
* *Defense:* `safety: 455`, `immutability_locks: 2`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.338
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/js/plupload/moxie.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 5883.74 | **LOC:** 9905 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.3183%), Tech Debt (13.2554%)
**Top Internal Functions/Classes:**
  * `XMLHttpRequest` **(Compute Cores)** (Impact: 132.0)
  * `HTML5Image` **(Compute Cores)** (Impact: 98.4)
  * `XMLHttpRequest` **(Compute Cores)** (Impact: 93.0)
  * `Runtime` **(Many-Argument Workhorses)** (Impact: 85.1)
    * *Intent:* */
  * `send` **(Many-Argument Workhorses)** (Impact: 81.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 655 instances
* *High Risk Execution (weighted view):* 5
* *Concurrency (weighted view):* 74
* *State Mutation (weighted view):* 2113
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1150`, `structural_boundaries: 764`, `args: 544`, `func_start: 367`
* *Risk/State:* `safety_bypasses: 26`, `high_risk_execution: 6`, `state_mutation: 803`, `dead_code: 54`, `planned_debt: 5`, `fragile_debt: 6`, `unreferenced_by_name: 11`
* *Architecture:* `io: 55`, `api: 8`, `concurrency: 14`, `import: 2`
* *Defense:* `safety: 308`, `doc: 280`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.338
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/functions.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 5448.56 | **LOC:** 9256 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 44.4%
- **Risk Profile:** Cognitive Load (37.974%), Tech Debt (85.5719%)
**Top Internal Functions/Classes:**
  * `wp_unique_filename` **(Many-Argument Workhorses)** (Impact: 88.2)
    * *Intent:* * If the filename is not unique, then a number will be added to the filename * before the extension,...
  * `wp_timezone_choice` **(Many-Argument Workhorses)** (Impact: 75.3)
  * `wp_check_filetype_and_ext` **(Many-Argument Workhorses)** (Impact: 73.5)
    * *Intent:* * @since 3.0.0 * * @param string $file Full path to the file. * @param string $filename The name of ...
  * `recurse_dirsize` **(Many-Argument Workhorses)** (Impact: 69.8)
    * *Intent:* /** * Gets the size of a directory recursively. * * Used by get_dirsize() to get a directory size wh...
  * `wp_date` **(Many-Argument Workhorses)** (Impact: 58.0)
    * *Intent:* * This is a newer function, intended to replace `date_i18n()` without legacy quirks in it. * * Note ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Rce:* 2 instances
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 922 instances
* *High Risk Execution (weighted view):* 10
* *Concurrency (weighted view):* 30
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 2877
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1109`, `structural_boundaries: 669`, `args: 251`, `func_start: 214`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 22`, `high_risk_execution: 12`, `state_mutation: 1033`, `dead_code: 4`, `planned_debt: 4`, `fragile_debt: 4`, `unreferenced_by_name: 113`
* *Architecture:* `io: 30`, `concurrency: 5`, `import: 11`
* *Defense:* `safety: 143`, `doc: 295`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.338
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` $_return_loop = false ) 
	$tortoise        = $start, $args = array() ) 
	global $wp_query, $callback_args = array(), $charset ) )
	) 
		return 'ISO-8859-1', $charset ) ) ||
		( 0 === strcasecmp( 'iso8859-1', $display = true ) 
	$name        = esc_attr( $name, $feed, $file...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-content/themes/twentytwenty/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.338
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-content/themes/twentytwentyone/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.338
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/certificates/ca-bundle.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.338
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-admin/js/customize-controls.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 4859.82 | **LOC:** 9390 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.0471%), Tech Debt (15.286%)
**Top Internal Functions/Classes:**
  * `save` **(Compute Cores)** (Impact: 88.1)
    * *Intent:* * Updates to the changeset are transactional. If any of the settings * are invalid then none of them...
  * `initialize` **(Compute Cores)** (Impact: 65.5)
    * *Intent:* * @param {string} [options.templateId] - Template ID for control's content. * @param {string} [optio...
  * `submit` **(Compute Cores)** (Impact: 58.0)
  * `initStickyHeaders` **(Compute Cores)** (Impact: 51.2)
    * *Intent:* /* * Sticky header feature. */
  * `requestChangesetUpdate` **(Many-Argument Workhorses)** (Impact: 44.1)
    * *Intent:* * @alias wp.customize.requestChangesetUpdate * * @since 4.7.0 * @access public * * @param {Object} [...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 703 instances
* *Concurrency (weighted view):* 61
* *State Mutation (weighted view):* 2444
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1106`, `structural_boundaries: 545`, `args: 640`, `func_start: 320`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1038`, `planned_debt: 9`, `fragile_debt: 1`, `duplicate_logic: 2`, `unreferenced_by_name: 19`
* *Architecture:* `io: 1`, `concurrency: 11`
* *Defense:* `safety: 295`, `doc: 258`, `sync_locks: 2`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.338
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/post.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 4811.7 | **LOC:** 8698 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 44.4%
- **Risk Profile:** Cognitive Load (35.394%), Tech Debt (7.7632%)
**Top Internal Functions/Classes:**
  * `wp_insert_post` **(Many-Argument Workhorses)** (Impact: 349.4)
    * *Intent:* * @type array $tax_input An array of taxonomy terms keyed by their taxonomy name. * If the taxonomy ...
  * `wp_unique_post_slug` **(Many-Argument Workhorses)** (Impact: 116.4)
    * *Intent:* /** * Computes a unique slug for the post, when given the desired slug and some post details. * * @s...
  * `wp_mime_type_icon` **(Many-Argument Workhorses)** (Impact: 67.7)
    * *Intent:* /** * Retrieves the icon for a MIME type or attachment. * * @since 2.1.0 * @since 6.5.0 Added the `$...
  * `sanitize_post_field` **(Many-Argument Workhorses)** (Impact: 61.5)
    * *Intent:* * * Possible context values are: 'raw', 'edit', 'db', 'display', 'attribute' and * 'js'. The 'displa...
  * `get_pages` **(Compute Cores)** (Impact: 51.3)
    * *Intent:* * @type string $authors A comma-separated list of author IDs. Default empty. * @type int $parent Pag...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 821 instances
* *Memory Alloc (weighted view):* 15
* *State Mutation (weighted view):* 2565
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 884`, `structural_boundaries: 561`, `args: 148`, `func_start: 145`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 923`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 70`, `import: 10`
* *Defense:* `safety: 155`, `doc: 259`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.338
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` $args = array() ) 
	global $wp_post_statuses, $args->capability_type . 's', $context, $counted_statuses, $counts, $filter, $filter = 'raw' ) 
	if ( empty( $post ) && isset( $GLOBALS['post'] ) ) 
		$post = $GLOBALS['post'], $filter = 'raw' ) 
	return get_post( $page...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/class-wp-xmlrpc-server.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 4719.08 | **LOC:** 7228 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (35.9663%), Tech Debt (10.7715%)
**Top Internal Functions/Classes:**
  * `mw_newPost` **(Compute Cores)** (Impact: 173.3)
    * *Intent:* * * @since 1.5.0 * * @param array $args { * Method arguments. Note: arguments must be ordered as doc...
  * `mw_editPost` **(Compute Cores)** (Impact: 166.8)
    * *Intent:* * * @since 1.5.0 * * @param array $args { * Method arguments. Note: arguments must be ordered as doc...
  * `_insert_post` **(Many-Argument Workhorses)** (Impact: 141.2)
    * *Intent:* /** * Helper method for wp_newPost() and wp_editPost(), containing shared logic. * * @since 3.4.0 * ...
  * `pingback_ping` **(Compute Cores)** (Impact: 63.1)
    * *Intent:* * Retrieves a pingback and registers it. * * @since 1.5.0 * * @global wpdb $wpdb WordPress database ...
  * `wp_newComment` **(Compute Cores)** (Impact: 52.2)
    * *Intent:* * * @since 2.7.0 * * @param array $args { * Method arguments. Note: arguments must be ordered as doc...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 18 instances
* *Amplified Cascading Flux:* 888 instances
* *Memory Alloc (weighted view):* 190
* *State Mutation (weighted view):* 2800
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 910`, `structural_boundaries: 789`, `args: 107`, `func_start: 106`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1024`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 2`, `unreferenced_by_name: 6`
* *Architecture:* `api: 92`, `import: 1`
* *Defense:* `safety: 234`, `doc: 224`, `immutability_locks: 31`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.338
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` $args, $comment, $post_id, $this, $url, ' . get_bloginfo( 'version' ) . ', '__return_false', 'blogger.deletePost'...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/media.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 4504.74 | **LOC:** 6564 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 80.0%
- **Risk Profile:** Cognitive Load (37.9601%), Tech Debt (9.0377%)
**Top Internal Functions/Classes:**
  * `wp_video_shortcode` **(Many-Argument Workhorses)** (Impact: 105.8)
    * *Intent:* * @type string $src URL to the source of the video file. Default empty. * @type int $height Height o...
  * `wp_get_loading_optimization_attributes` **(Many-Argument Workhorses)** (Impact: 86.7)
    * *Intent:* * - `decoding` attribute with a value of "async" * * If any of these attributes are already present ...
  * `wp_calculate_image_srcset` **(Many-Argument Workhorses)** (Impact: 83.9)
    * *Intent:* * A helper function to calculate the image sources to include in a 'srcset' attribute. * * @since 4....
  * `wp_prepare_attachment_for_js` **(Compute Cores)** (Impact: 81.3)
    * *Intent:* * @type string $orientation If the attachment is an image, represents the image orientation * (lands...
  * `get_post_galleries` **(Many-Argument Workhorses)** (Impact: 78.4)
    * *Intent:* /** * Retrieves galleries from the passed post's content. * * @since 3.6.0 * * @param int|WP_Post $p...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 828 instances
* *Concurrency (weighted view):* 7
* *Memory Alloc (weighted view):* 8
* *State Mutation (weighted view):* 2564
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 866`, `structural_boundaries: 407`, `args: 104`, `func_start: 99`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 1`, `state_mutation: 908`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 3`
* *Architecture:* `io: 4`, `api: 34`, `concurrency: 2`, `import: 17`
* *Defense:* `safety: 169`, `doc: 186`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.338
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` $attachment, $attachment->ID, $attachment_id, **
	 * Pre-filters the image meta to be able to fix inconsistencies in the stored data.
	 *
	 * @since 4.5.0
	 *
	 * @param array  $image_meta    The image meta data, $attr, $context, $context = null ) 
	if ( null === $context ) 
		$context = current_filter(, $data...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/formatting.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 4139.22 | **LOC:** 6293 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (45.9521%), Tech Debt (75.3896%)
**Top Internal Functions/Classes:**
  * `sanitize_option` **(Many-Argument Workhorses)** (Impact: 249.4)
    * *Intent:* /** * Sanitizes various option values based on the nature of the option. *
  * `wptexturize` **(Many-Argument Workhorses)** (Impact: 132.9)
    * *Intent:* * &#8217;cause today&#8217;s effort makes it worth tomorrow&#8217;s &#8220;holiday&#8221; &#8230; * ...
  * `wpautop` **(Many-Argument Workhorses)** (Impact: 61.7)
    * *Intent:* /** * Replaces double line breaks with paragraph elements. * * A group of regex replaces used to ide...
  * `esc_url` **(Many-Argument Workhorses)** (Impact: 59.0)
    * *Intent:* * (the default behavior) ampersands are also replaced. The {@see 'clean_url'} filter * is applied to...
  * `wptexturize_primes` **(Many-Argument Workhorses)** (Impact: 51.8)
    * *Intent:* /** * Implements a logic tree to determine whether or not "7'." represents seven feet, * then conver...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 785 instances
* *State Mutation (weighted view):* 2466
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 748`, `structural_boundaries: 340`, `args: 128`, `func_start: 120`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 896`, `dead_code: 4`, `planned_debt: 2`, `fragile_debt: 4`, `unreferenced_by_name: 66`
* *Architecture:* `io: 5`
* *Defense:* `safety: 58`, `doc: 191`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.338
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` $content_type, $email, $filename, $filename_raw, $format = 'Y-m-d H:i:s' ) 
	$datetime = date_create( $date_string, $img, ', $sanitized_email...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/ID3/module.audio-video.quicktime.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 4018.5 | **LOC:** 3158 | **CtrlFlow:** 34.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (85.7516%), Tech Debt (14.1826%)
**Top Internal Functions/Classes:**
  * `QuicktimeParseAtom` **(Many-Argument Workhorses)** (Impact: 1165.5)
    * *Intent:* /** * @param string $atomname * @param int $atomsize * @param string $atom_data * @param int $baseof...
  * `Analyze` **(Compute Cores)** (Impact: 108.6)
    * *Intent:* /** * @return bool */
  * `CopyToAppropriateCommentsSection` **(Many-Argument Workhorses)** (Impact: 32.4)
    * *Intent:* /** * @param string $keyname * @param string|array $data * @param string $boxname * * @return bool *...
  * `QuicktimeParseContainerAtom` **(Many-Argument Workhorses)** (Impact: 26.4)
    * *Intent:* /** * @param string $atom_data * @param int $baseoffset * @param array $atomHierarchy * @param bool ...
  * `LociString` **(Compute Cores)** (Impact: 20.5)
    * *Intent:* /** * @param string $lstring * @param int $count * * @return string */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 616 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 2461
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 853`, `structural_boundaries: 93`, `args: 25`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 85`, `high_risk_execution: 1`, `state_mutation: 1229`, `dead_code: 45`, `fragile_debt: 6`, `unreferenced_by_name: 2`
* *Architecture:* `io: 5`, `api: 26`
* *Defense:* `safety: 87`, `doc: 27`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.338
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Dependency(GETID3_INCLUDEPATH.'module.audio.mp3.php', Dependency(GETID3_INCLUDEPATH.'module.tag.id3v2.php', Dependency(GETID3_INCLUDEPATH.'module.tag.nikon-nctg.php',  In this way, __FILE__, d, d', if the atom needs to be converted from a 32-bit to a 64-bit atom...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/class-wp-query.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Drift: 0.0 IQR)
- **Magnitude:** 3991.66 | **LOC:** 5114 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (47.9959%), Tech Debt (14.6167%)
**Top Internal Functions/Classes:**
  * `get_posts` **(Compute Cores)** (Impact: 470.7)
    * *Intent:* /** * Retrieves an array of posts based on query variables. * * There are a few filters and actions ...
  * `parse_query` **(Compute Cores)** (Impact: 238.3)
    * *Intent:* * @type array $tax_query An associative array of WP_Tax_Query arguments. * See WP_Tax_Query::__const...
  * `parse_tax_query` **(Compute Cores)** (Impact: 77.4)
    * *Intent:* /** * Parses various taxonomy related query vars. * * For BC, this method is not marked as protected...
  * `parse_orderby` **(Compute Cores)** (Impact: 62.5)
    * *Intent:* /** * Converts the given orderby alias (if allowed) to a properly-prefixed value. * * @since 4.0.0 *...
  * `parse_search` **(Compute Cores)** (Impact: 40.9)
    * *Intent:* /** * Generates SQL for the WHERE clause based on passed search terms. * * @since 3.7.0 * * @global ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 791 instances
* *Api Near Db Sink:* 1 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 2535
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 846`, `structural_boundaries: 235`, `args: 71`, `func_start: 68`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 953`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 12`
* *Architecture:* `io: 1`, `api: 110`
* *Defense:* `safety: 204`, `doc: 192`, `cleanup: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.338
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` $query_vars['s'], $search_columns, $this, &$this ), 'pillow -sofa' will
	 *                                                   return posts containing 'pillow' but not 'sofa'. The
	 *                                                   character used for exclusion can be modified using the
	 *                                                   the 'wp_query_search_exclusion_prefix' filter.
	 *     @type string[]        $search_columns         Array of column names to be searched. Accepts 'post_title', *                                                   'post_excerpt' and 'post_content'. Default empty array.
	 *     @type int             $second                 Second of the minute. Default empty. Accepts numbers 0-59.
	 *     @type bool            $sentence               Whether to search by phrase. Default false.
	 *     @type bool            $suppress_filters       Whether to suppress filters. Default false.
	 *     @type string          $tag                    Tag slug. Comma-separated (either), 
		$this->posts = apply_filters_ref_array( 'posts_pre_query', 
	public function is_archive() 
		return (bool) $this->is_archive...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/PHPMailer/PHPMailer.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 3820.98 | **LOC:** 5526 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (46.4196%), Tech Debt (46.6705%)
**Top Internal Functions/Classes:**
  * `validateAddress` **(Compute Cores)** (Impact: 145.9)
    * *Intent:* * * ```php * PHPMailer::validateAddress('user@example.com', function($address) { * return (strpos($a...
  * `encodeHeader` **(Compute Cores)** (Impact: 70.1)
    * *Intent:* /** * Encode a header value (not including its label) optimally. * Picks shortest of Q, B, or none. ...
  * `msgHTML` **(Many-Argument Workhorses)** (Impact: 67.0)
    * *Intent:* * If you don't provide a $basedir, relative paths will be left untouched (and thus probably break in...
  * `smtpConnect` **(Compute Cores)** (Impact: 65.3)
    * *Intent:* /** * Initiate a connection to an SMTP server. * Returns false if the operation failed. * * @param a...
  * `createBody` **(I/O & Config Routines)** (Impact: 59.0)
    * *Intent:* /** * Assemble the message body. * Returns an empty string on failure. * * @throws Exception * * @re...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Rce:* 2 instances
* *Amplified Cascading Flux:* 599 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 36
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 1994
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 799`, `structural_boundaries: 392`, `args: 138`, `func_start: 128`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 2`, `state_mutation: 796`, `dead_code: 11`, `fragile_debt: 4`, `unreferenced_by_name: 42`
* *Architecture:* `io: 46`, `api: 149`
* *Defense:* `safety: 125`, `doc: 220`, `immutability_locks: 33`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.338
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` $autoSignHeaders, 
    protected $all_recipients = [], $cc,  Emit a runtime notice to recommend using the IMAP extension for full RFC822 parsing
        trigger_error(self::lang('imap_recommended'), $host)
        ) 
            return false, $position = 'text')
    
        $position = strtolower($position, '@', *...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/js/media-views.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 3796.56 | **LOC:** 10605 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (28.5823%), Tech Debt (31.2239%)
**Top Internal Functions/Classes:**
  * `createToolbar` **(I/O & Config Routines)** (Impact: 55.2)
  * `toggleSelectionHandler` **(Defensive Guards)** (Impact: 32.2)
    * *Intent:* /** * @param {Object} event */
  * `toggleSelection` **(Defensive Guards)** (Impact: 31.9)
    * *Intent:* /** * @param {Object} options */
  * `set` **(Many-Argument Workhorses)** (Impact: 21.9)
    * *Intent:* /** * @param {string} id * @param {wp.media.View|Object} view * @param {Object} options * @return {w...
  * `update` **(Compute Cores)** (Impact: 20.6)
    * *Intent:* /** * @param {string} key */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 480 instances
* *Concurrency (weighted view):* 16
* *State Mutation (weighted view):* 1822
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 762`, `structural_boundaries: 623`, `args: 590`, `func_start: 434`
* *Risk/State:* `state_mutation: 862`, `dead_code: 1`, `planned_debt: 9`, `fragile_debt: 1`, `duplicate_logic: 23`, `unreferenced_by_name: 3`
* *Architecture:* `io: 5`, `api: 77`, `concurrency: 6`
* *Defense:* `safety: 144`, `doc: 667`, `cleanup: 26`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.338
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/link-template.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 3699.58 | **LOC:** 4905 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (38.0619%), Tech Debt (53.3176%)
**Top Internal Functions/Classes:**
  * `get_avatar_data` **(Many-Argument Workhorses)** (Impact: 114.9)
    * *Intent:* * the {@see 'pre_get_avatar_data'} filter to customize avatars. * Default null. * @type array $proce...
  * `get_adjacent_post` **(Many-Argument Workhorses)** (Impact: 77.8)
    * *Intent:* * * @since 2.5.0 * * @global wpdb $wpdb WordPress database abstraction object. * * @param bool $in_s...
  * `get_permalink` **(Many-Argument Workhorses)** (Impact: 45.1)
    * *Intent:* /** * Retrieves the full permalink for the current post or post ID. * * @since 1.0.0 * * @param int|...
  * `get_attachment_link` **(Compute Cores)** (Impact: 41.3)
    * *Intent:* /** * Retrieves the permalink for an attachment. * * This can be used in the WordPress Loop or outsi...
  * `get_term_feed_link` **(Many-Argument Workhorses)** (Impact: 39.7)
    * *Intent:* /** * Retrieves the feed link for a term. * * Returns a link to the feed for all posts in a given te...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 715 instances
* *State Mutation (weighted view):* 2260
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 578`, `structural_boundaries: 290`, `args: 117`, `func_start: 117`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 830`, `unreferenced_by_name: 52`
* *Architecture:* `io: 1`
* *Defense:* `safety: 93`, `doc: 203`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.338
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` "ORDER BY p.post_date $order, $adjacent, $args, $comment_id, $context, $context = 'display' ) 
	$comment = get_comment( $comment_id, $excluded_terms, $feed...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/general-template.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 3686.58 | **LOC:** 5424 | **CtrlFlow:** 28.2% | **Authorship Centralization:** 55.6%
- **Risk Profile:** Cognitive Load (46.7008%), Tech Debt (35.9641%)
**Top Internal Functions/Classes:**
  * `wp_get_code_editor_settings` **(Compute Cores)** (Impact: 134.8)
    * *Intent:* * * @param array $args { * Args. * * @type string $type The MIME type of the file to be edited. * @t...
  * `get_bloginfo` **(Compute Cores)** (Impact: 109.1)
    * *Intent:* * These options will trigger the _deprecated_argument() function. * * Deprecated arguments include: ...
  * `get_calendar` **(Compute Cores)** (Impact: 82.1)
    * *Intent:* * @global int $m * @global int $monthnum * @global int $year * @global WP_Locale $wp_locale WordPres...
  * `wp_get_archives` **(Compute Cores)** (Impact: 80.8)
    * *Intent:* * with $before preceding and $after succeeding. Default 'html'. * @type string $before Markup to pre...
  * `wp_title` **(Many-Argument Workhorses)** (Impact: 74.7)
    * *Intent:* * to the right with most browsers supporting tabs. You can achieve this by * using the seplocation p...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 720 instances
* *State Mutation (weighted view):* 2233
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 727`, `structural_boundaries: 271`, `args: 97`, `func_start: 94`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 793`, `unreferenced_by_name: 49`
* *Architecture:* `io: 4`, `import: 6`
* *Defense:* `safety: 74`, `doc: 195`, `immutability_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.338
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` "$file-rtl", $args, 
	do_action( 'get_footer', 
	do_action( 'get_header', 
	do_action( 'get_sidebar', **
	 * Fires before the specified template part file is loaded.
	 *
	 * The dynamic portion of the hook name, $args['before_page_number'] . number_format_i18n( $n ) . $args['after_page_number'], $args['next_text']...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-admin/includes/ajax-actions.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Drift: 0.0 IQR)
- **Magnitude:** 3659.94 | **LOC:** 5648 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (45.9797%), Tech Debt (82.4435%)
**Top Internal Functions/Classes:**
  * `wp_ajax_replyto_comment` **(Compute Cores)** (Impact: 51.5)
    * *Intent:* /** * Handles replying to a comment via AJAX. * * @since 3.1.0 * * @param string $action Action to p...
  * `_wp_ajax_delete_comment_response` **(Many-Argument Workhorses)** (Impact: 45.8)
    * *Intent:* // // Ajax helpers. // /** * Sends back current comment total and new page links if they need to be ...
  * `wp_ajax_parse_embed` **(I/O & Config Routines)** (Impact: 40.6)
    * *Intent:* /** * Applies [embed] Ajax handlers to a string. * * @since 4.0.0 * * @global WP_Post $post Global p...
  * `wp_ajax_wp_privacy_erase_personal_data` **(I/O & Config Routines)** (Impact: 38.5)
    * *Intent:* /** * Handles erasing personal data via AJAX. * * @since 4.9.6
  * `wp_ajax_wp_privacy_export_personal_data` **(I/O & Config Routines)** (Impact: 35.2)
    * *Intent:* /** * Handles exporting a user's personal data via AJAX. * * @since 4.9.6
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 731 instances
* *Memory Alloc (weighted view):* 27
* *State Mutation (weighted view):* 2271
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 924`, `structural_boundaries: 212`, `args: 99`, `func_start: 96`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 809`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 94`
* *Architecture:* `io: 369`, `import: 28`
* *Defense:* `safety: 242`, `doc: 136`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.338
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` $_POST['menu'], $args, $attachment, $attachment_data, $attachment_id, $cropped, $eraser_index ), $exporter_key )...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/class-wp-theme-json.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 3439.86 | **LOC:** 4835 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 35.7%
- **Risk Profile:** Cognitive Load (47.0488%), Tech Debt (12.9339%)
**Top Internal Functions/Classes:**
  * `get_layout_styles` **(Many-Argument Workhorses)** (Impact: 127.3)
    * *Intent:* /** * Gets the CSS layout rules for a particular block from theme.json layout definitions. * * @sinc...
  * `compute_style_properties` **(Many-Argument Workhorses)** (Impact: 89.8)
    * *Intent:* * @since 5.9.0 Added the `$settings` and `$properties` parameters. * @since 6.1.0 Added `$theme_json...
  * `get_styles_for_block` **(Compute Cores)** (Impact: 85.9)
    * *Intent:* /** * Gets the CSS rules for a particular block from theme.json. * * @since 6.1.0 * @since 6.6.0 Set...
  * `sanitize` **(Many-Argument Workhorses)** (Impact: 69.6)
    * *Intent:* /** * Sanitizes the input according to the schemas. * * @since 5.8.0 * @since 5.9.0 Added the `$vali...
  * `get_block_nodes` **(Many-Argument Workhorses)** (Impact: 64.2)
    * *Intent:* * @since 6.3.0 Refactored and stabilized selectors API. * @since 6.6.0 Added optional selectors and ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 604 instances
* *State Mutation (weighted view):* 1956
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 686`, `structural_boundaries: 331`, `args: 78`, `func_start: 73`, `class_start: 1`
* *Risk/State:* `state_mutation: 748`, `dead_code: 3`, `unreferenced_by_name: 15`
* *Architecture:* `api: 21`
* *Defense:* `safety: 231`, `doc: 96`, `immutability_locks: 18`, `cleanup: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.338
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` $class_name, $name, $nested_selector, $nested_selector )
					: static::append_to_selector( $selector, $node ) 
		$node['selector'] = static::scope_selector( $scope, $node['selector'], $options = array() ) 
		$nodes = array(, $options = array() ) 
		if ( null === $origins ) 
			$origins = static::VALID_ORIGINS...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/class-wp-customize-manager.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 3274.64 | **LOC:** 6163 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (48.0757%), Tech Debt (17.1601%)
**Top Internal Functions/Classes:**
  * `import_theme_starter_content` **(Compute Cores)** (Impact: 218.8)
    * *Intent:* /** * Imports theme starter content into the customized state. * * @since 4.7.0 * * @param array $st...
  * `save_changeset_post` **(Compute Cores)** (Impact: 124.5)
    * *Intent:* * @param array $args { * Args for changeset post. * * @type array $data Optional additional changese...
  * `register_controls` **(I/O & Config Routines)** (Impact: 87.6)
    * *Intent:* /** * Registers some default controls. * * @since 3.4.0 */
  * `save` **(I/O & Config Routines)** (Impact: 56.5)
    * *Intent:* /** * Handles customize_save WP Ajax request to save/update a changeset. * * @since 3.4.0 * @since 4...
  * `_publish_changeset_values` **(Compute Cores)** (Impact: 46.6)
    * *Intent:* * called directly and instead `wp_publish_post()` should be used. * * Please note that if the settin...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 544 instances
* *High Risk Execution (weighted view):* 0
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 1755
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 860`, `structural_boundaries: 515`, `args: 131`, `func_start: 118`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 667`, `dead_code: 1`, `planned_debt: 3`, `unreferenced_by_name: 21`
* *Architecture:* `io: 63`, `api: 112`, `import: 43`
* *Defense:* `safety: 182`, `doc: 178`, `sync_locks: 10`, `immutability_locks: 4`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.338
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` $args, $args ) 
		if ( 'edit_post' === $cap && ! empty( $args[0] ) && 'customize_changeset' === get_post_type( $args[0] ) ) 
			$post_type_obj = get_post_type_object( 'customize_changeset', $attachment['file'] ) ) 
				continue, $cap, $class, $id, $post, $post->ID...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/deprecated.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 3269.58 | **LOC:** 6531 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 28.6%
- **Risk Profile:** Cognitive Load (45.2999%), Tech Debt (99.9936%)
**Top Internal Functions/Classes:**
  * `get_links` **(Many-Argument Workhorses)** (Impact: 90.6)
    * *Intent:* * Not used if no image or $show_images is true. Default ' '. * @param bool $show_images Optional. Wh...
  * `_wp_theme_json_webfonts_handler` **(Compute Cores)** (Impact: 88.7)
    * *Intent:* * a. It hides the inner-workings. * b. It does not expose API ins or outs for consumption. * c. It o...
  * `block_core_navigation_submenu_build_css_colors` **(Many-Argument Workhorses)** (Impact: 41.0)
    * *Intent:* /** * Build an array with CSS classes and inline styles defining the colors * which will be applied ...
  * `wp_tinycolor_string_to_rgb` **(Compute Cores)** (Impact: 38.6)
    * *Intent:* * Direct port of TinyColor's function, lightly simplified to maintain * consistency with TinyColor. ...
  * `the_content_rss` **(Many-Argument Workhorses)** (Impact: 29.0)
    * *Intent:* * If there is content left over, then dots will be added and the rest of the content * will be remov...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 551 instances
* *State Mutation (weighted view):* 1856
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 496`, `structural_boundaries: 608`, `args: 263`, `func_start: 243`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 41`, `high_risk_execution: 1`, `state_mutation: 754`, `planned_debt: 3`, `unreferenced_by_name: 205`
* *Architecture:* `io: 8`, `import: 2`
* *Defense:* `safety: 79`, `doc: 271`, `immutability_locks: 14`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.338
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` "__return_true" )', $context, $crop = false, $dest_path = null, $fullsize = false, $image, $include_unapproved = false ) 
	_deprecated_function( __FUNCTION__, $jpeg_quality = 90 ) 
	_deprecated_function( __FUNCTION__...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `wp-includes/js/codemirror/csslint.js` -> **Weston Ruter** (100.0% isolated ownership) | Magnitude: 6814.08
- `wp-includes/js/codemirror/esprima.js` -> **Weston Ruter** (100.0% isolated ownership) | Magnitude: 6470.3
- `wp-includes/class-wp-xmlrpc-server.php` -> **Weston Ruter** (100.0% isolated ownership) | Magnitude: 4719.08
- `wp-includes/PHPMailer/PHPMailer.php` -> **Sergey Biryukov** (100.0% isolated ownership) | Magnitude: 3820.98
- `wp-includes/class-wp-customize-manager.php` -> **Weston Ruter** (100.0% isolated ownership) | Magnitude: 3274.64

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `wp-includes/php-ai-client/src/AiClient.php` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 100.0%)
- `wp-includes/php-ai-client/src/Providers/DTO/ProviderMetadata.php` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 99.9928%)
- `wp-includes/php-ai-client/src/Results/DTO/GenerativeAiResult.php` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 99.9999%)
- `wp-includes/php-ai-client/src/Builders/PromptBuilder.php` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 99.9999%)
- `wp-includes/php-ai-client/src/Common/AbstractDataTransferObject.php` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `wp-includes/php-ai-client/src/Common/AbstractEnum.php` -> **Severity: 0.969** (Embedded: 0.0115 * Error Risk: 84.1026%)
- `wp-includes/php-ai-client/src/Common/AbstractDataTransferObject.php` -> **Severity: 0.616** (Embedded: 0.0138 * Error Risk: 44.505%)
- `wp-includes/php-ai-client/src/Messages/DTO/Message.php` -> **Severity: 0.526** (Embedded: 0.007 * Error Risk: 75.5335%)
- `wp-includes/php-ai-client/src/Providers/Models/DTO/ModelMetadata.php` -> **Severity: 0.457** (Embedded: 0.0069 * Error Risk: 66.0499%)
- `wp-includes/php-ai-client/src/Providers/Http/DTO/Request.php` -> **Severity: 0.452** (Embedded: 0.0048 * Error Risk: 93.8884%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `wp-includes/js/jquery/ui/tabs.js` -> **Severity: 62.5** (Blast Radius: 0.625 * Doc Risk: 100.0%)
- `wp-includes/js/underscore.js` -> **Severity: 62.5** (Blast Radius: 0.625 * Doc Risk: 100.0%)
- `wp-includes/Requests/src/Hooks.php` -> **Severity: 42.8** (Blast Radius: 1.284 * Doc Risk: 33.3333%)
- `wp-admin/admin-header.php` -> **Severity: 33.8** (Blast Radius: 0.338 * Doc Risk: 100.0%)
- `wp-admin/includes/class-ftp.php` -> **Severity: 33.8** (Blast Radius: 0.338 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
