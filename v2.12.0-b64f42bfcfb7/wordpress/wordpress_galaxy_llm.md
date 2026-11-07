# ARCHITECTURAL_BRIEF: wordpress
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/WordPress/WordPress.git` |
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
- **Scope:** 2980 analyzed artifact(s), 536229 LOC.
- **Load-bearing artifact:** `wp-includes/functions.php` -- 361 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `wp-settings.php` -- pulls in 322 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `wp-includes/js/mediaelement/mediaelement-and-player.js` at magnitude 10930.32 (structural weight, not risk).
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
| Total Artifacts | 6068 |
| Analyzed Artifacts (Scanned) | 2980 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3088 |
| Total LOC | 536229 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 49.1% |
| Dominant Lang | PHP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3721 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1545 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 9.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.7022 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 70 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PHP | 1582 | 308926 | 53.1% |
| CSS | 576 | 110931 | 19.3% |
| XML | 358 | 10 | 12.0% |
| JAVASCRIPT | 210 | 93046 | 7.0% |
| JSON | 168 | 22964 | 5.6% |
| HTML | 59 | 350 | 2.0% |
| PLAINTEXT | 27 | 2 | 0.9% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 2978 |
| unknown | unknown | 2 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 33%, Data / Markup / Trivial 30%, Large Core Modules (3) 9%, Large Core Modules 8%, Large Core Modules (2) 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 2942 | 98.7% |
| Unknown | 2 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 25 | 0.8% |
| Static: Minified & Vendor Opaque Mass | 11 | 0.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3088*

**Composition by Extension & Reason:**
- `.css`: 1214x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 14x Excluded (Machine-Generated Source Code Signature: 814 LOC), 2x Excluded (Machine-Generated Source Code Signature: 820 LOC)
- `.js`: 523x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 8 exceeds 500 chars), 1x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.php`: 373x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Saturation: Line 36 exceeds 500 chars), 2x Excluded (Saturation: Line 26 exceeds 500 chars)
- `.woff2`: 315x Excluded (Explicitly Denied Extension: '.woff2')
- `.png`: 160x Excluded (Explicitly Denied Extension: '.png')
- `.jpg`: 85x Excluded (Explicitly Denied Extension: '.jpg')
- `.gif`: 62x Excluded (Explicitly Denied Extension: '.gif')
- `.woff`: 54x Excluded (Explicitly Denied Extension: '.woff')
- `.map`: 52x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.webp`: 46x Excluded (Explicitly Denied Extension: '.webp')
- `.txt`: 38x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 21x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Static Asset Blob without Intent: 1726 LOC), 1x Excluded (Massive Static Asset Blob: 6791 LOC)
- `.ttf`: 13x Excluded (Explicitly Denied Extension: '.ttf')
- `.scss`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 3 exceeds 500 chars), 1x Excluded (Saturation: Line 10 exceeds 500 chars)
- `.svg`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.9 | 14.6 | 3.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 96.0 | 34.4 | 50.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 14.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 14.1 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 1.5 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 47.3 | 23.1 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 11.4 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.7 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 5.6 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 7.6 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 6108 | 679 | 4 | `wp-includes/class-wp-xmlrpc-server.php` |
| cleanup | 1178 | 355 | 1 | `wp-admin/includes/class-pclzip.php` |
| guards | 23715 | 1242 | 19 | `wp-includes/js/mediaelement/mediaelement-and-player.js` |
| danger | 4695 | 530 | 2 | `wp-admin/includes/class-pclzip.php` |
| concurrency | 803 | 117 | 0 | `wp-includes/js/mediaelement/mediaelement-and-player.js` |
| connectivity | 7832 | 641 | 7 | `wp-content/themes/twentytwentyone/assets/css/style-editor.css` |
| io | 5519 | 586 | 4 | `wp-admin/includes/ajax-actions.php` |
| crypto | 0 | 0 | 0 | - |
| ipc | 112 | 46 | 0 | `wp-admin/includes/misc.php` |
| time | 712 | 187 | 0 | `wp-includes/js/mediaelement/mediaelement-and-player.js` |
| serialization | 234 | 115 | 0 | `wp-admin/js/image-edit.js` |
| regex | 2033 | 325 | 1 | `wp-includes/js/codemirror/esprima.js` |
| events | 3112 | 212 | 0 | `wp-includes/js/media-views.js` |
| tests | 91 | 14 | 0 | `wp-includes/js/codemirror/esprima.js` |
| docs | 24894 | 1901 | 23 | `wp-includes/js/media-views.js` |
| debt | 5684 | 748 | 4 | `wp-admin/includes/meta-boxes.php` |
| mutation | 110215 | 1645 | 84 | `wp-includes/js/mediaelement/mediaelement-and-player.js` |
| dead_code | 5386 | 767 | 5 | `wp-includes/deprecated.php` |
| credential | 27 | 18 | 0 | `wp-includes/pluggable.php` |
| threat | 153 | 40 | 0 | `wp-includes/functions.php` |
| ml_ai | 67 | 28 | 0 | `wp-login.php` |
| ui | 3996 | 533 | 2 | `wp-content/themes/twentytwenty/style-rtl.css` |

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

1. **functions.php** (`wp-includes/functions.php`) — 361 inbound connections
2. **formatting.php** (`wp-includes/formatting.php`) — 301 inbound connections
3. **load.php** (`wp-includes/load.php`) — 245 inbound connections
4. **plugin.php** (`wp-includes/plugin.php`) — 186 inbound connections
5. **post.php** (`wp-includes/post.php`) — 169 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **wp-settings.php** (`wp-settings.php`) — 322 outbound dependencies
2. **class-wp-customize-manager.php** (`wp-includes/class-wp-customize-manager.php`) — 42 outbound dependencies
3. **csslint.js** (`wp-includes/js/codemirror/csslint.js`) — 34 outbound dependencies
4. **style.scss** (`wp-content/themes/twentytwentyone/assets/sass/style.scss`) — 32 outbound dependencies
5. **admin.php** (`wp-admin/includes/admin.php`) — 31 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `encoding` **(Compute Cores)** (@ `wp-includes/SimplePie/src/Misc.php`) -> Impact: **1211.1** | LOC: 1312
  * *Intent:* /** * Normalize an encoding name * * This is automatically generated by create.php * * To generate it, run `php create.php` on the command line, and c...
- `map_meta_cap` **(Many-Argument Workhorses)** (@ `wp-includes/capabilities.php`) -> Impact: **653.8** | LOC: 836
  * *Intent:* * @since 5.3.0 Formalized the existing and already documented `...$args` parameter * by adding it to the function signature. * @since 5.7.0 Added the ...
- `MediaElementPlayer` **(Compute Cores)** (@ `wp-includes/js/mediaelement/mediaelement-and-player.js`) -> Impact: **583.6** | LOC: 1673
- `_plural` **(Defensive Guards)** (@ `wp-includes/js/mediaelement/mediaelement-and-player.js`) -> Impact: **538.5** | LOC: 170
- `_plural` **(Defensive Guards)** (@ `wp-includes/js/mediaelement/mediaelement.js`) -> Impact: **538.5** | LOC: 170
- `get_enclosures` **(I/O & Config Routines)** (@ `wp-includes/SimplePie/src/Item.php`) -> Impact: **473.2** | LOC: 1365
  * *Intent:* /** * Get all available enclosures (podcasts, etc.) * * Supports the <enclosure> RSS tag, as well as Media RSS and iTunes RSS. * * At this point, we'r...
- `get_posts` **(I/O & Config Routines)** (@ `wp-includes/class-wp-query.php`) -> Impact: **470.7** | LOC: 1774
  * *Intent:* /** * Retrieves an array of posts based on query variables. * * There are a few filters and actions that can be used to modify the post * database que...
- `redirect_canonical` **(Many-Argument Workhorses)** (@ `wp-includes/canonical.php`) -> Impact: **466.5** | LOC: 808
  * *Intent:* * * @since 2.3.0 * * @global WP_Rewrite $wp_rewrite WordPress rewrite component. * @global bool $is_IIS * @global WP_Query $wp_query WordPress Query o...
- `init` **(Many-Argument Workhorses)** (@ `wp-includes/js/codemirror/csslint.js`) -> Impact: **430.2** | LOC: 1987
  * *Intent:* // initialization
- `prototype` **(I/O & Config Routines)** (@ `wp-includes/js/codemirror/csslint.js`) -> Impact: **410.4** | LOC: 2488

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `wp-includes` | 254 | 133137.06 | 30.42% | 50.54% |
| `wp-admin/includes` | 105 | 57777.2 | 37.17% | 55.73% |
| `wp-admin/js` | 49 | 21538.62 | 37.16% | 13.32% |
| `wp-includes/js` | 48 | 19659.96 | 44.63% | 23.64% |
| `wp-includes/js/mediaelement` | 9 | 16986.49 | 41.63% | 22.85% |
| `wp-includes/rest-api/endpoints` | 45 | 15087.78 | 31.11% | 28.12% |
| `wp-includes/SimplePie/src` | 22 | 13152.82 | 35.51% | 67.12% |
| `wp-includes/js/codemirror` | 5 | 13149.56 | 60.34% | 15.55% |
| `wp-includes/js/jquery/ui` | 37 | 12933.78 | 59.63% | 29.79% |
| `wp-includes/blocks` | 83 | 9695.7 | 33.61% | 1.1% |

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
- `wp-admin/includes/ajax-actions.php` -> **94** Orphaned Functions | **0** Duplicates
- `wp-includes/js/mediaelement/mediaelement-and-player.js` -> **10** Orphaned Functions | **66** Duplicates
- `wp-includes/post.php` -> **70** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `387` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2009` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `wp-includes/js/mediaelement/mediaelement-and-player.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.144)
- **Top Global Matches:** file_cluster_4: 9.144, file_cluster_6: 11.644, file_cluster_12: 14.833
- **Magnitude:** 10930.32 | **LOC:** 8541 | **CtrlFlow:** 32.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (98.9%), Concurrency Surface (formerly Concurrency) (89.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 99.6778% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MediaElementPlayer` **(Compute Cores)** (Impact: 583.6)
  * `_plural` **(Defensive Guards)** (Impact: 538.5)
  * `t` **(Defensive Guards)** (Impact: 405.0)
  * `buildprogress` **(Many-Argument Workhorses)** (Impact: 325.2)
  * `_pluralForms` **(Defensive Guards)** (Impact: 269.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 10 instances
* *Amplified Race Conditions:* 56 instances
* *Amplified Cascading Flux:* 1099 instances
* *High Risk Execution (weighted view):* 19
* *Concurrency (weighted view):* 367
* *State Mutation (weighted view):* 3650
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2260`, `structural_boundaries: 1413`, `args: 696`, `func_start: 660`
* *Risk/State:* `safety_bypasses: 45`, `high_risk_execution: 29`, `state_mutation: 1452`, `duplicate_logic: 66`, `unreferenced_by_name: 10`
* *Architecture:* `io: 3`, `api: 109`, `concurrency: 87`
* *Defense:* `safety: 764`, `doc: 3`, `cleanup: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.169
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/js/codemirror/csslint.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.394)
- **Top Global Matches:** file_cluster_4: 9.394, file_cluster_12: 12.197, file_cluster_10: 12.313
- **Magnitude:** 6648.98 | **LOC:** 10859 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **34**; blast radius 0.169; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (65.1%), Guard Balance (formerly Safety Score) (64.0%)
- **Documentation Coverage:** 49.5146% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `init` **(Many-Argument Workhorses)** (Impact: 430.2)
    * *Intent:* // initialization
  * `prototype` **(I/O & Config Routines)** (Impact: 410.4)
  * `PropertyValuePart` **(Many-Argument Workhorses)** (Impact: 207.0)
    * *Intent:* /** * Represents a single part of a CSS property value, meaning that it represents * just one part o...
  * `clone` **(Many-Argument Workhorses)** (Impact: 127.8)
    * *Intent:* * Caution: if `circular` is false and `parent` contains circular references, * your program may ente...
  * `parse` **(Defensive Guards)** (Impact: 103.5)
    * *Intent:* /** Simple recursive-descent grammar to build matchers from strings. */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 826 instances
* *Concurrency (weighted view):* 18
* *State Mutation (weighted view):* 2742
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1163`, `structural_boundaries: 851`, `args: 488`, `func_start: 337`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 1090`, `dead_code: 6`, `planned_debt: 4`, `fragile_debt: 26`, `duplicate_logic: 9`, `unreferenced_by_name: 18`
* *Architecture:* `api: 31`, `concurrency: 3`, `import: 77`
* *Defense:* `safety: 392`, `doc: 206`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.169
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` EventTarget, StringReader, SyntaxError, SyntaxUnit, TokenStreamBase, Colors, Combinator, EventTarget...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/js/codemirror/esprima.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.311)
- **Top Global Matches:** file_cluster_4: 7.311, file_cluster_6: 11.272, file_cluster_10: 12.293
- **Magnitude:** 6403.8 | **LOC:** 6709 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.2%), Guard Balance (formerly Safety Score) (68.0%), Concurrency Surface (formerly Concurrency) (65.3%)
- **Documentation Coverage:** 99.4236% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseClassElement` **(Defensive Guards)** (Impact: 65.5)
    * *Intent:* // https://tc39.github.io/ecma262/#sec-class-definitions
  * `parseObjectProperty` **(Defensive Guards)** (Impact: 59.4)
  * `parseForStatement` **(I/O & Config Routines)** (Impact: 55.3)
    * *Intent:* // https://tc39.github.io/ecma262/#sec-for-statement // https://tc39.github.io/ecma262/#sec-for-in-a...
  * `isKeyword` **(Defensive Guards)** (Impact: 55.1)
    * *Intent:* // https://tc39.github.io/ecma262/#sec-keywords
  * `scanPunctuator` **(Defensive Guards)** (Impact: 54.0)
    * *Intent:* // https://tc39.github.io/ecma262/#sec-punctuators
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 33 instances
* *Amplified Cascading Flux:* 935 instances
* *High Risk Execution (weighted view):* 6
* *Concurrency (weighted view):* 210
* *State Mutation (weighted view):* 3427
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1505`, `structural_boundaries: 1420`, `args: 430`, `func_start: 315`
* *Risk/State:* `safety_bypasses: 30`, `high_risk_execution: 8`, `state_mutation: 1557`, `dead_code: 6`, `unreferenced_by_name: 1`
* *Architecture:* `api: 122`, `concurrency: 45`
* *Defense:* `safety: 538`, `doc: 65`, `test: 77`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.169
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/js/mediaelement/mediaelement.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.769)
- **Top Global Matches:** file_cluster_4: 7.769, file_cluster_6: 10.932, file_cluster_12: 13.295
- **Magnitude:** 5776.96 | **LOC:** 3985 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (99.6%), Complexity Load (formerly Cognitive Load) (99.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 99.5839% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_plural` **(Defensive Guards)** (Impact: 538.5)
  * `t` **(Defensive Guards)** (Impact: 405.0)
  * `_pluralForms` **(Defensive Guards)** (Impact: 269.1)
  * `MediaElement` **(Many-Argument Workhorses)** (Impact: 262.7)
  * `create` **(Many-Argument Workhorses)** (Impact: 196.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 48 instances
* *Amplified Cascading Flux:* 516 instances
* *High Risk Execution (weighted view):* 2
* *Concurrency (weighted view):* 308
* *State Mutation (weighted view):* 1725
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1134`, `structural_boundaries: 770`, `args: 354`, `func_start: 330`
* *Risk/State:* `safety_bypasses: 24`, `high_risk_execution: 3`, `state_mutation: 693`, `duplicate_logic: 29`, `unreferenced_by_name: 10`
* *Architecture:* `io: 3`, `api: 100`, `concurrency: 68`
* *Defense:* `safety: 488`, `doc: 3`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.169
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/functions.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.201)
- **Top Global Matches:** file_cluster_4: 5.201, file_cluster_6: 9.995, file_cluster_15: 11.255
- **Magnitude:** 5302.96 | **LOC:** 9256 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 44.4%
- **Blast Radius:** changing it is visible to **361** in-repo importer(s); it depends on **7**; blast radius 50.211; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (85.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `wp_unique_filename` **(Many-Argument Workhorses)** (Impact: 86.2)
    * *Intent:* * before the extension, and will continue adding numbers until the filename * is unique. * * The cal...
  * `wp_timezone_choice` **(Many-Argument Workhorses)** (Impact: 75.3)
    * *Intent:* /** * Gives a nicely-formatted list of timezone strings. * * @since 2.9.0 * @since 4.7.0 Added the `...
  * `wp_check_filetype_and_ext` **(Many-Argument Workhorses)** (Impact: 73.5)
    * *Intent:* * * @param string $file Full path to the file. * @param string $filename The name of the file (may d...
  * `recurse_dirsize` **(Many-Argument Workhorses)** (Impact: 69.8)
    * *Intent:* * @since 5.6.0 The `$directory_cache` parameter was added. * * @param string $directory Full path of...
  * `wp_date` **(Many-Argument Workhorses)** (Impact: 56.0)
    * *Intent:* * * Note that, unlike `date_i18n()`, this function accepts a true Unix timestamp, not summed * with ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 904 instances
* *High Risk Execution (weighted view):* 10
* *Concurrency (weighted view):* 30
* *State Mutation (weighted view):* 2841
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1033`, `structural_boundaries: 669`, `args: 251`, `func_start: 214`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 22`, `high_risk_execution: 12`, `state_mutation: 1033`, `planned_debt: 4`, `fragile_debt: 4`, `unreferenced_by_name: 113`
* *Architecture:* `io: 30`, `concurrency: 5`, `import: 11`
* *Defense:* `safety: 143`, `doc: 295`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 50.211
  * `Choke Point (Betweenness):` 0.007555 | `Ripple Effect (Closeness):` 0.144138
  * `Imports (Out-Degree: 36):` file.php', class-IXR.php', class-phpass.php', default-widgets.php', option.php', version.php', db-error.php'
  * `Imported By (In-Degree: 361):` (Excluded from Brief to save tokens)

### `wp-content/themes/twentytwenty/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.169
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-content/themes/twentytwentyone/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.169
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-admin/js/customize-controls.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.511)
- **Top Global Matches:** file_cluster_4: 8.511, file_cluster_10: 9.694, file_cluster_15: 10.262
- **Magnitude:** 4828.72 | **LOC:** 9390 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.8%), Complexity Load (formerly Cognitive Load) (46.5%)
- **Documentation Coverage:** 24.3792% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `save` **(Many-Argument Workhorses)** (Impact: 88.1)
    * *Intent:* * Updates to the changeset are transactional. If any of the settings * are invalid then none of them...
  * `initialize` **(Many-Argument Workhorses)** (Impact: 58.6)
    * *Intent:* */
  * `submit` **(I/O & Config Routines)** (Impact: 58.0)
  * `initStickyHeaders` **(I/O & Config Routines)** (Impact: 51.2)
    * *Intent:* /* * Sticky header feature. */
  * `requestChangesetUpdate` **(Many-Argument Workhorses)** (Impact: 44.1)
    * *Intent:* * * * If not provided, then the changes will still be obtained from unsaved dirty settings. */...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 698 instances
* *Concurrency (weighted view):* 61
* *State Mutation (weighted view):* 2434
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1082`, `structural_boundaries: 545`, `args: 640`, `func_start: 320`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1038`, `planned_debt: 9`, `fragile_debt: 1`, `duplicate_logic: 2`, `unreferenced_by_name: 19`
* *Architecture:* `io: 1`, `concurrency: 11`
* *Defense:* `safety: 295`, `doc: 258`, `sync_locks: 2`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.169
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/post.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.15)
- **Top Global Matches:** file_cluster_4: 6.15, file_cluster_15: 11.3, file_cluster_6: 11.692
- **Magnitude:** 4705.0 | **LOC:** 8698 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 44.4%
- **Blast Radius:** changing it is visible to **169** in-repo importer(s); blast radius 10.754; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.1%), Debt Markers (formerly Tech Debt) (53.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `wp_insert_post` **(Many-Argument Workhorses)** (Impact: 345.4)
    * *Intent:* * If the taxonomy is hierarchical, the term list needs to be * either an array of term IDs or a comm...
  * `wp_unique_post_slug` **(Many-Argument Workhorses)** (Impact: 113.9)
    * *Intent:* * Computes a unique slug for the post, when given the desired slug and some post details. * * @since...
  * `sanitize_post_field` **(Many-Argument Workhorses)** (Impact: 61.5)
    * *Intent:* * Possible context values are: 'raw', 'edit', 'db', 'display', 'attribute' and * 'js'. The 'display'...
  * `wp_mime_type_icon` **(Many-Argument Workhorses)** (Impact: 60.8)
    * *Intent:* /** * Retrieves the icon for a MIME type or attachment. * * @since 2.1.0 * @since 6.5.0 Added the `$...
  * `get_pages` **(Many-Argument Workhorses)** (Impact: 51.3)
    * *Intent:* * @type int $parent Page ID to return direct children of. Default -1, or no restriction. * @type str...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 818 instances
* *Memory Alloc (weighted view):* 15
* *State Mutation (weighted view):* 2559
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 865`, `structural_boundaries: 561`, `args: 148`, `func_start: 145`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 923`, `planned_debt: 1`, `unreferenced_by_name: 70`
* *Architecture:* `io: 1`, `import: 10`
* *Defense:* `safety: 155`, `doc: 259`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.754
  * `Choke Point (Betweenness):` 0.001312 | `Ripple Effect (Closeness):` 0.112353
  * `Imports (Out-Degree: 29):` None
  * `Imported By (In-Degree: 169):` (Excluded from Brief to save tokens)

### `wp-includes/class-wp-xmlrpc-server.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.864)
- **Top Global Matches:** file_cluster_4: 5.864, file_cluster_6: 9.687, file_cluster_9: 12.332
- **Magnitude:** 4685.98 | **LOC:** 7228 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.3%), Complexity Load (formerly Cognitive Load) (35.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mw_newPost` **(Many-Argument Workhorses)** (Impact: 173.3)
    * *Intent:* * * @since 1.5.0 * * @param array $args { * Method arguments. Note: arguments must be ordered as doc...
  * `mw_editPost` **(Many-Argument Workhorses)** (Impact: 166.8)
    * *Intent:* * * @since 1.5.0 * * @param array $args { * Method arguments. Note: arguments must be ordered as doc...
  * `_insert_post` **(Many-Argument Workhorses)** (Impact: 141.2)
    * *Intent:* /** * Helper method for wp_newPost() and wp_editPost(), containing shared logic. * * @since 3.4.0 * ...
  * `pingback_ping` **(Many-Argument Workhorses)** (Impact: 53.2)
    * *Intent:* * Retrieves a pingback and registers it. * * @since 1.5.0 * * @global wpdb $wpdb WordPress database ...
  * `wp_newComment` **(Compute Cores)** (Impact: 49.3)
    * *Intent:* * * @since 2.7.0 * * @param array $args { * Method arguments. Note: arguments must be ordered as doc...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 18 instances
* *Amplified Cascading Flux:* 883 instances
* *Memory Alloc (weighted view):* 190
* *State Mutation (weighted view):* 2790
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 894`, `structural_boundaries: 789`, `args: 107`, `func_start: 106`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1024`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 2`, `unreferenced_by_name: 6`
* *Architecture:* `api: 92`, `import: 1`
* *Defense:* `safety: 234`, `doc: 224`, `immutability_locks: 31`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.169
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 37):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/media.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.007)
- **Top Global Matches:** file_cluster_6: 6.007, file_cluster_8: 11.354, file_cluster_4: 13.307
- **Magnitude:** 4379.54 | **LOC:** 6564 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 80.0%
- **Blast Radius:** changing it is visible to **57** in-repo importer(s); it depends on **5**; blast radius 3.893; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.7%), Complexity Load (formerly Cognitive Load) (37.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `wp_video_shortcode` **(Many-Argument Workhorses)** (Impact: 95.4)
    * *Intent:* * @type int $height Height of the video embed in pixels. Default 360. * @type int $width Width of th...
  * `wp_get_loading_optimization_attributes` **(Many-Argument Workhorses)** (Impact: 86.7)
    * *Intent:* * * If any of these attributes are already present in the given attributes, they will not be modifie...
  * `wp_calculate_image_srcset` **(Many-Argument Workhorses)** (Impact: 83.9)
    * *Intent:* * * @since 4.4.0 * * @param int[] $size_array { * An array of width and height values. * * @type int...
  * `wp_prepare_attachment_for_js` **(Many-Argument Workhorses)** (Impact: 81.3)
    * *Intent:* * (landscape or portrait). * @type array $sizes If the attachment is an image, contains an array of ...
  * `image_resize_dimensions` **(Many-Argument Workhorses)** (Impact: 75.1)
    * *Intent:* * @param int $orig_w Original width in pixels. * @param int $orig_h Original height in pixels. * @pa...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 803 instances
* *Concurrency (weighted view):* 7
* *Memory Alloc (weighted view):* 8
* *State Mutation (weighted view):* 2514
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 822`, `structural_boundaries: 407`, `args: 104`, `func_start: 99`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 1`, `state_mutation: 908`, `planned_debt: 2`, `fragile_debt: 3`, `unreferenced_by_name: 34`
* *Architecture:* `io: 4`, `concurrency: 2`, `import: 17`
* *Defense:* `safety: 169`, `doc: 186`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.893
  * `Choke Point (Betweenness):` 0.001539 | `Ripple Effect (Closeness):` 0.096464
  * `Imports (Out-Degree: 35):` class-avif-info.php', class-wp-image-editor-gd.php', class-wp-image-editor-imagick.php', class-wp-image-editor.php', media-template.php'
  * `Imported By (In-Degree: 57):` (Excluded from Brief to save tokens)

### `wp-admin/includes/class-pclzip.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 14.284)
- **Top Global Matches:** file_cluster_8: 14.284, file_cluster_3: 21.951, file_cluster_6: 22.308
- **Magnitude:** 4005.44 | **LOC:** 5733 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.265; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `privParseOptions` **(Many-Argument Workhorses)** (Impact: 211.9)
    * *Intent:* // Function : privParseOptions() // Description : // This internal methods reads the variable list o...
  * `privExtractByRule` **(Many-Argument Workhorses)** (Impact: 183.0)
    * *Intent:* // Description : // Extract a file or directory depending of rules (by index, by name, ...) // Param...
  * `privExtractFile` **(Many-Argument Workhorses)** (Impact: 166.7)
    * *Intent:* // -------------------------------------------------------------------------------- // -------------...
  * `privDeleteByRule` **(Many-Argument Workhorses)** (Impact: 99.7)
    * *Intent:* // -------------------------------------------------------------------------------- // -------------...
  * `privAddFile` **(Many-Argument Workhorses)** (Impact: 99.4)
    * *Intent:* // -------------------------------------------------------------------------------- // -------------...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 702 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 2213
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 755`, `structural_boundaries: 294`, `args: 59`, `func_start: 57`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 437`, `high_risk_execution: 1`, `state_mutation: 809`, `dead_code: 30`, `fragile_debt: 1`, `unreferenced_by_name: 9`
* *Architecture:* `io: 66`, `api: 1`
* *Defense:* `safety: 73`, `cleanup: 39`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.265
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.060941
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `wp-includes/class-wp-query.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.736)
- **Top Global Matches:** file_cluster_4: 6.736, file_cluster_6: 9.673, file_cluster_12: 13.191
- **Magnitude:** 3984.96 | **LOC:** 5114 | **CtrlFlow:** 31.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **39** in-repo importer(s); blast radius 2.293; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (48.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_posts` **(I/O & Config Routines)** (Impact: 470.7)
    * *Intent:* /** * Retrieves an array of posts based on query variables. * * There are a few filters and actions ...
  * `parse_query` **(Many-Argument Workhorses)** (Impact: 236.9)
    * *Intent:* * @type array $tax_query An associative array of WP_Tax_Query arguments. * See WP_Tax_Query::__const...
  * `parse_tax_query` **(Many-Argument Workhorses)** (Impact: 77.4)
    * *Intent:* /** * Parses various taxonomy related query vars. * * For BC, this method is not marked as protected...
  * `parse_orderby` **(Compute Cores)** (Impact: 62.5)
    * *Intent:* /** * Converts the given orderby alias (if allowed) to a properly-prefixed value. * * @since 4.0.0 *...
  * `parse_search` **(Many-Argument Workhorses)** (Impact: 38.0)
    * *Intent:* /** * Generates SQL for the WHERE clause based on passed search terms. * * @since 3.7.0 * * @global ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 791 instances
* *Api Near Db Sink:* 1 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 2535
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 841`, `structural_boundaries: 235`, `args: 71`, `func_start: 68`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 953`, `planned_debt: 1`, `unreferenced_by_name: 12`
* *Architecture:* `io: 1`, `api: 110`
* *Defense:* `safety: 204`, `doc: 192`, `cleanup: 24`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.293
  * `Choke Point (Betweenness):` 0.000287 | `Ripple Effect (Closeness):` 0.082067
  * `Imports (Out-Degree: 19):` None
  * `Imported By (In-Degree: 39):` (Excluded from Brief to save tokens)

### `wp-includes/formatting.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.5)
- **Top Global Matches:** file_cluster_4: 6.5, file_cluster_15: 10.121, file_cluster_16: 11.41
- **Magnitude:** 3767.72 | **LOC:** 6293 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **301** in-repo importer(s); blast radius 26.134; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.5%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (74.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sanitize_option` **(Many-Argument Workhorses)** (Impact: 245.9)
    * *Intent:* /** * Sanitizes various option values based on the nature of the option. * * This is basically a swi...
  * `wptexturize` **(Many-Argument Workhorses)** (Impact: 84.4)
    * *Intent:* * * Code within certain HTML blocks are skipped. * * Do not use this function before the {@see 'init...
  * `esc_url` **(Many-Argument Workhorses)** (Impact: 53.0)
    * *Intent:* * is applied to the returned cleaned URL. * * @since 2.8.0 * @since 6.9.0 Prepends `https://` to the...
  * `force_balance_tags` **(I/O & Config Routines)** (Impact: 41.5)
    * *Intent:* * 1.0 First Version} * * @since 2.0.4 * @since 5.3.0 Improve accuracy and add support for custom ele...
  * `human_time_diff` **(Many-Argument Workhorses)** (Impact: 39.9)
    * *Intent:* /** * Determines the difference between two timestamps. * * The difference is returned in a human-re...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 709 instances
* *State Mutation (weighted view):* 2314
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 606`, `structural_boundaries: 340`, `args: 128`, `func_start: 120`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 896`, `planned_debt: 2`, `fragile_debt: 4`, `unreferenced_by_name: 66`
* *Architecture:* `io: 5`
* *Defense:* `safety: 58`, `doc: 191`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 26.134
  * `Choke Point (Betweenness):` 0.003784 | `Ripple Effect (Closeness):` 0.131532
  * `Imports (Out-Degree: 21):` None
  * `Imported By (In-Degree: 301):` (Excluded from Brief to save tokens)

### `wp-includes/js/media-views.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.456)
- **Top Global Matches:** file_cluster_10: 8.456, file_cluster_15: 9.681, file_cluster_16: 10.227
- **Magnitude:** 3762.06 | **LOC:** 10605 | **CtrlFlow:** 12.6% | **Authorship Centralization:** 66.7%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (61.5%), Complexity Load (formerly Cognitive Load) (32.5%)
- **Documentation Coverage:** 38.126% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createToolbar` **(I/O & Config Routines)** (Impact: 49.2)
  * `toggleSelectionHandler` **(Defensive Guards)** (Impact: 32.2)
    * *Intent:* /** */
  * `toggleSelection` **(Defensive Guards)** (Impact: 31.9)
    * *Intent:* /** */
  * `set` **(Many-Argument Workhorses)** (Impact: 21.9)
    * *Intent:* /** */
  * `update` **(Compute Cores)** (Impact: 20.6)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 472 instances
* *Concurrency (weighted view):* 16
* *State Mutation (weighted view):* 1806
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 741`, `structural_boundaries: 623`, `args: 590`, `func_start: 434`
* *Risk/State:* `state_mutation: 862`, `planned_debt: 9`, `fragile_debt: 1`, `duplicate_logic: 23`, `unreferenced_by_name: 3`
* *Architecture:* `io: 5`, `api: 77`, `concurrency: 6`
* *Defense:* `safety: 144`, `doc: 667`, `cleanup: 26`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.169
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/general-template.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.188)
- **Top Global Matches:** file_cluster_6: 6.188, file_cluster_4: 8.646, file_cluster_15: 16.308
- **Magnitude:** 3657.18 | **LOC:** 5424 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 55.6%
- **Blast Radius:** changing it is visible to **96** in-repo importer(s); it depends on **3**; blast radius 7.095; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (46.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `wp_get_code_editor_settings` **(Many-Argument Workhorses)** (Impact: 134.8)
    * *Intent:* * @param array $args { * Args. * * @type string $type The MIME type of the file to be edited. * @typ...
  * `get_bloginfo` **(Many-Argument Workhorses)** (Impact: 105.6)
    * *Intent:* * * Deprecated arguments include: * * - 'siteurl' - Use 'url' instead * - 'home' - Use 'url' instead...
  * `get_calendar` **(Many-Argument Workhorses)** (Impact: 82.1)
    * *Intent:* * @global int $monthnum * @global int $year * @global WP_Locale $wp_locale WordPress date and time l...
  * `wp_get_archives` **(Many-Argument Workhorses)** (Impact: 80.8)
    * *Intent:* * @type string $before Markup to prepend to the beginning of each link. Default empty. * @type strin...
  * `wp_title` **(Many-Argument Workhorses)** (Impact: 74.7)
    * *Intent:* * using the seplocation parameter and setting the value to 'right'. This change * was introduced aro...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 717 instances
* *State Mutation (weighted view):* 2227
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 710`, `structural_boundaries: 271`, `args: 97`, `func_start: 94`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 793`, `unreferenced_by_name: 49`
* *Architecture:* `io: 4`, `import: 6`
* *Defense:* `safety: 74`, `doc: 195`, `immutability_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.095
  * `Choke Point (Betweenness):` 0.000971 | `Ripple Effect (Closeness):` 0.102315
  * `Imports (Out-Degree: 32):` $search_form_template, class-wp-editor.php', readonly.php'
  * `Imported By (In-Degree: 96):` (Excluded from Brief to save tokens)

### `wp-includes/link-template.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.735)
- **Top Global Matches:** file_cluster_4: 5.735, file_cluster_15: 9.087, file_cluster_16: 10.286
- **Magnitude:** 3635.08 | **LOC:** 4905 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **148** in-repo importer(s); blast radius 13.474; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.3%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (52.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_avatar_data` **(Many-Argument Workhorses)** (Impact: 101.1)
    * *Intent:* * Default null. * @type array $processed_args When the function returns, the value will be the proce...
  * `get_adjacent_post` **(Many-Argument Workhorses)** (Impact: 77.8)
    * *Intent:* * @since 2.5.0 * * @global wpdb $wpdb WordPress database abstraction object. * * @param bool $in_sam...
  * `get_permalink` **(Many-Argument Workhorses)** (Impact: 43.4)
    * *Intent:* /** * Retrieves the full permalink for the current post or post ID. * * @since 1.0.0 * * @param int|...
  * `get_attachment_link` **(Many-Argument Workhorses)** (Impact: 37.8)
    * *Intent:* /** * Retrieves the permalink for an attachment. * * This can be used in the WordPress Loop or outsi...
  * `get_boundary_post` **(Many-Argument Workhorses)** (Impact: 33.8)
    * *Intent:* * Boundary being either the first or last post by publish date within the constraints specified * by...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 712 instances
* *State Mutation (weighted view):* 2254
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 544`, `structural_boundaries: 290`, `args: 117`, `func_start: 117`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 830`, `unreferenced_by_name: 52`
* *Architecture:* `io: 1`
* *Defense:* `safety: 93`, `doc: 203`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 13.474
  * `Choke Point (Betweenness):` 0.00128 | `Ripple Effect (Closeness):` 0.104894
  * `Imports (Out-Degree: 26):` None
  * `Imported By (In-Degree: 148):` (Excluded from Brief to save tokens)

### `wp-admin/includes/ajax-actions.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.374)
- **Top Global Matches:** file_cluster_8: 9.374, file_cluster_6: 9.894, file_cluster_4: 17.662
- **Magnitude:** 3616.44 | **LOC:** 5648 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 0.169; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (82.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `wp_ajax_replyto_comment` **(Many-Argument Workhorses)** (Impact: 51.5)
    * *Intent:* /** * Handles replying to a comment via AJAX. * * @since 3.1.0 * * @param string $action Action to p...
  * `_wp_ajax_delete_comment_response` **(Many-Argument Workhorses)** (Impact: 45.8)
    * *Intent:* // Ajax helpers. // /** * Sends back current comment total and new page links if they need to be upd...
  * `wp_ajax_parse_embed` **(I/O & Config Routines)** (Impact: 40.6)
    * *Intent:* /** * Applies [embed] Ajax handlers to a string. * * @since 4.0.0 * * @global WP_Post $post Global p...
  * `wp_ajax_wp_privacy_erase_personal_data` **(I/O & Config Routines)** (Impact: 38.5)
    * *Intent:* /** * Handles erasing personal data via AJAX. * * @since 4.9.6 */
  * `wp_ajax_wp_privacy_export_personal_data` **(I/O & Config Routines)** (Impact: 35.2)
    * *Intent:* /** * Handles exporting a user's personal data via AJAX. * * @since 4.9.6 */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 723 instances
* *Memory Alloc (weighted view):* 27
* *State Mutation (weighted view):* 2255
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 897`, `structural_boundaries: 212`, `args: 99`, `func_start: 96`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 809`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 94`
* *Architecture:* `io: 369`, `import: 28`
* *Defense:* `safety: 242`, `doc: 136`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.169
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 61):` class-wp-community-events.php', class-wp-debug-data.php', class-wp-site-health.php', class-wp-site-icon.php', class-wp-upgrader.php', dashboard.php', edit-tag-messages.php', image-edit.php'...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/PHPMailer/PHPMailer.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.777)
- **Top Global Matches:** file_cluster_4: 5.777, file_cluster_6: 7.47, file_cluster_15: 13.743
- **Magnitude:** 3609.98 | **LOC:** 5526 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.313; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.5%), Debt Markers (formerly Tech Debt) (46.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createBody` **(I/O & Config Routines)** (Impact: 59.0)
    * *Intent:* /** * Assemble the message body. * Returns an empty string on failure. * * @throws Exception * * @re...
  * `smtpConnect` **(Compute Cores)** (Impact: 58.2)
    * *Intent:* /** * Initiate a connection to an SMTP server. * Returns false if the operation failed. * * @param a...
  * `wrapText` **(Many-Argument Workhorses)** (Impact: 56.5)
    * *Intent:* /** * Word-wrap message. * For use with mailers that do not automatically perform wrapping * and for...
  * `msgHTML` **(Many-Argument Workhorses)** (Impact: 55.0)
    * *Intent:* * If you don't provide a $basedir, relative paths will be left untouched (and thus probably break in...
  * `encodeHeader` **(Many-Argument Workhorses)** (Impact: 54.5)
    * *Intent:* /** * Encode a header value (not including its label) optimally. * Picks shortest of Q, B, or none. ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 597 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 36
* *State Mutation (weighted view):* 1990
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 677`, `structural_boundaries: 392`, `args: 138`, `func_start: 128`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 2`, `state_mutation: 796`, `dead_code: 4`, `fragile_debt: 4`, `unreferenced_by_name: 42`
* *Architecture:* `io: 46`, `api: 149`
* *Defense:* `safety: 125`, `doc: 220`, `immutability_locks: 33`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.313
  * `Choke Point (Betweenness):` 4.5e-05 | `Ripple Effect (Closeness):` 0.000335
  * `Imports (Out-Degree: 3):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `wp-includes/class-wp-theme-json.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.357)
- **Top Global Matches:** file_cluster_6: 6.357, file_cluster_8: 11.354, file_cluster_4: 13.641
- **Magnitude:** 3419.86 | **LOC:** 4835 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 35.7%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); blast radius 1.638; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.4%), Complexity Load (formerly Cognitive Load) (46.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_layout_styles` **(Many-Argument Workhorses)** (Impact: 125.6)
    * *Intent:* /** * Gets the CSS layout rules for a particular block from theme.json layout definitions. * * @sinc...
  * `compute_style_properties` **(Many-Argument Workhorses)** (Impact: 89.8)
    * *Intent:* * @since 5.9.0 Added the `$settings` and `$properties` parameters. * @since 6.1.0 Added `$theme_json...
  * `get_styles_for_block` **(Many-Argument Workhorses)** (Impact: 84.5)
    * *Intent:* /** * Gets the CSS rules for a particular block from theme.json. * * @since 6.1.0 * @since 6.6.0 Set...
  * `sanitize` **(Many-Argument Workhorses)** (Impact: 69.6)
    * *Intent:* /** * Sanitizes the input according to the schemas. * * @since 5.8.0 * @since 5.9.0 Added the `$vali...
  * `get_block_nodes` **(Many-Argument Workhorses)** (Impact: 64.2)
    * *Intent:* * @since 6.3.0 Refactored and stabilized selectors API. * @since 6.6.0 Added optional selectors and ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 604 instances
* *State Mutation (weighted view):* 1956
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 673`, `structural_boundaries: 331`, `args: 78`, `func_start: 73`, `class_start: 1`
* *Risk/State:* `state_mutation: 748`, `unreferenced_by_name: 15`
* *Architecture:* `api: 21`
* *Defense:* `safety: 231`, `doc: 96`, `immutability_locks: 18`, `cleanup: 22`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.638
  * `Choke Point (Betweenness):` 0.000588 | `Ripple Effect (Closeness):` 0.0747
  * `Imports (Out-Degree: 13):` None
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `wp-includes/deprecated.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.311)
- **Top Global Matches:** file_cluster_12: 8.311, file_cluster_15: 9.486, file_cluster_4: 10.299
- **Magnitude:** 3198.58 | **LOC:** 6531 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 28.6%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 0.175; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.5%)
- **Documentation Coverage:** 0.4115% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_links` **(Many-Argument Workhorses)** (Impact: 90.6)
    * *Intent:* * @param bool $show_images Optional. Whether to show images (if defined). Default true. * @param str...
  * `_wp_theme_json_webfonts_handler` **(I/O & Config Routines)** (Impact: 88.7)
    * *Intent:* * b. It does not expose API ins or outs for consumption. * c. It only works with a theme's `theme.js...
  * `block_core_navigation_submenu_build_css_colors` **(Many-Argument Workhorses)** (Impact: 41.0)
    * *Intent:* /** * Build an array with CSS classes and inline styles defining the colors * which will be applied ...
  * `the_content_rss` **(Many-Argument Workhorses)** (Impact: 29.0)
    * *Intent:* * will be removed. * * @since 0.71 * * @deprecated 2.9.0 Use the_content_feed() * @see the_content_f...
  * `wp_get_loading_attr_default` **(Compute Cores)** (Impact: 26.1)
    * *Intent:* * within the main content. If the element is the very first content element, the `loading` attribute...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 535 instances
* *State Mutation (weighted view):* 1824
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 467`, `structural_boundaries: 608`, `args: 263`, `func_start: 243`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 41`, `high_risk_execution: 1`, `state_mutation: 754`, `planned_debt: 3`, `unreferenced_by_name: 205`
* *Architecture:* `io: 8`, `import: 2`
* *Defense:* `safety: 79`, `doc: 271`, `immutability_locks: 14`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.175
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.000335
  * `Imports (Out-Degree: 45):` class-wp-press-this-plugin.php'
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `wp-includes/class-wp-customize-manager.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.185)
- **Top Global Matches:** file_cluster_4: 7.185, file_cluster_6: 8.83, file_cluster_15: 13.907
- **Magnitude:** 3167.74 | **LOC:** 6163 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **42**; blast radius 0.439; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.3%), Complexity Load (formerly Cognitive Load) (47.5%)
- **Documentation Coverage:** 0.4405% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `import_theme_starter_content` **(Defensive Guards)** (Impact: 207.5)
    * *Intent:* /** * Imports theme starter content into the customized state. * * @since 4.7.0 * * @param array $st...
  * `save_changeset_post` **(Many-Argument Workhorses)** (Impact: 124.5)
    * *Intent:* * @param array $args { * Args for changeset post. * * @type array $data Optional additional changese...
  * `save` **(I/O & Config Routines)** (Impact: 56.5)
    * *Intent:* /** * Handles customize_save WP Ajax request to save/update a changeset. * * @since 3.4.0 * @since 4...
  * `_publish_changeset_values` **(Compute Cores)** (Impact: 42.3)
    * *Intent:* * called directly and instead `wp_publish_post()` should be used. * * Please note that if the settin...
  * `register_controls` **(I/O & Config Routines)** (Impact: 40.0)
    * *Intent:* /** * Registers some default controls. * * @since 3.4.0 */
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 541 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 1749
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 764`, `structural_boundaries: 515`, `args: 131`, `func_start: 118`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 667`, `planned_debt: 3`, `unreferenced_by_name: 21`
* *Architecture:* `io: 63`, `api: 112`, `import: 43`
* *Defense:* `safety: 182`, `doc: 178`, `sync_locks: 10`, `immutability_locks: 4`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.439
  * `Choke Point (Betweenness):` 0.00278 | `Ripple Effect (Closeness):` 0.071573
  * `Imports (Out-Degree: 52):` file.php', image.php', media.php', theme.php', update.php', class-wp-customize-control.php', class-wp-customize-nav-menus.php', class-wp-customize-panel.php'...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `wp-includes/html-api/class-wp-html-processor.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.003)
- **Top Global Matches:** file_cluster_8: 7.003, file_cluster_6: 14.707, file_cluster_4: 23.155
- **Magnitude:** 2949.48 | **LOC:** 6708 | **CtrlFlow:** 44.9% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 0.288; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.9%), Complexity Load (formerly Cognitive Load) (56.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `step_in_body` **(I/O & Config Routines)** (Impact: 322.4)
    * *Intent:* * Parses next element in the 'in body' insertion mode. * * This internal function performs the 'in b...
  * `is_special` **(Compute Cores)** (Impact: 139.8)
    * *Intent:* /** * Returns whether an element of a given name is in the HTML special category. * * @since 6.4.0 *...
  * `step_in_foreign_content` **(I/O & Config Routines)** (Impact: 121.2)
    * *Intent:* * Parses next element in the 'in foreign content' insertion mode. * * This internal function perform...
  * `step` **(Compute Cores)** (Impact: 79.3)
    * *Intent:* /** * Steps through the HTML document and stop at the next tag, if any. * * @since 6.4.0 * * @throws...
  * `step_in_table` **(I/O & Config Routines)** (Impact: 67.0)
    * *Intent:* * Parses next element in the 'in table' insertion mode. * * This internal function performs the 'in ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 341 instances
* *Memory Alloc (weighted view):* 13
* *State Mutation (weighted view):* 1073
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1307`, `structural_boundaries: 544`, `args: 82`, `func_start: 79`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 391`, `planned_debt: 59`, `fragile_debt: 1`, `unreferenced_by_name: 12`
* *Architecture:* `api: 37`
* *Defense:* `safety: 44`, `doc: 99`, `immutability_locks: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.288
  * `Choke Point (Betweenness):` 0.000414 | `Ripple Effect (Closeness):` 0.06149
  * `Imports (Out-Degree: 6):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `wp-includes/SimplePie/src/Item.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.809)
- **Top Global Matches:** file_cluster_6: 6.809, file_cluster_4: 10.616, file_cluster_8: 15.603
- **Magnitude:** 2931.56 | **LOC:** 2367 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.0%), Complexity Load (formerly Cognitive Load) (75.2%), Debt Markers (formerly Tech Debt) (26.0%)
- **Documentation Coverage:** 4.1667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_enclosures` **(I/O & Config Routines)** (Impact: 473.2)
    * *Intent:* /** * Get all available enclosures (podcasts, etc.) * * Supports the <enclosure> RSS tag, as well as...
  * `get_links` **(Defensive Guards)** (Impact: 30.9)
    * *Intent:* /** * Get all links for the item * * Uses `<atom:link>`, `<link>` or `<guid>` * * @since Beta 2 * @p...
  * `get_description` **(Compute Cores)** (Impact: 30.0)
    * *Intent:* * Get the content for the item * * Prefers summaries over full content , but will return full conten...
  * `get_date` **(Compute Cores)** (Impact: 27.6)
    * *Intent:* /** * Get the posting date/time for the item * * Uses `<atom:published>`, `<atom:updated>`, `<atom:i...
  * `get_authors` **(Defensive Guards)** (Impact: 26.1)
    * *Intent:* /** * Get all authors for the item * * Uses `<atom:author>`, `<author>`, `<dc:creator>` or `<itunes:...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 646 instances
* *State Mutation (weighted view):* 2091
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 579`, `structural_boundaries: 201`, `args: 36`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 799`, `planned_debt: 3`, `unreferenced_by_name: 16`
* *Architecture:* `api: 36`
* *Defense:* `safety: 251`, `doc: 39`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.169
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wp-includes/taxonomy.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.601)
- **Top Global Matches:** file_cluster_6: 5.601, file_cluster_4: 8.692, file_cluster_8: 16.301
- **Magnitude:** 2815.02 | **LOC:** 5160 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **73** in-repo importer(s); blast radius 4.818; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.5%), Debt Markers (formerly Tech Debt) (56.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `wp_insert_term` **(Many-Argument Workhorses)** (Impact: 88.4)
    * *Intent:* * * @type string $alias_of Slug of the term to make this term an alias of. * Default empty string. A...
  * `wp_set_object_terms` **(Many-Argument Workhorses)** (Impact: 66.1)
    * *Intent:* * exists under. * * @since 2.3.0 * * @global wpdb $wpdb WordPress database abstraction object. * * @...
  * `get_term_by` **(Many-Argument Workhorses)** (Impact: 57.0)
    * *Intent:* * @since 5.5.0 Added 'ID' as an alias of 'id' for the `$field` parameter. * * @see sanitize_term_fie...
  * `wp_update_term` **(Many-Argument Workhorses)** (Impact: 54.3)
    * *Intent:* * @param int $term_id The ID of the term. * @param string $taxonomy The taxonomy of the term. * @par...
  * `wp_delete_term` **(Many-Argument Workhorses)** (Impact: 54.1)
    * *Intent:* * @param string $taxonomy Taxonomy name. * @param array|string $args { * Optional. Array of argument...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 479 instances
* *Memory Alloc (weighted view):* 31
* *State Mutation (weighted view):* 1510
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 494`, `structural_boundaries: 359`, `args: 80`, `func_start: 80`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 3`, `state_mutation: 552`, `planned_debt: 2`, `unreferenced_by_name: 39`
* *Architecture:* `import: 2`
* *Defense:* `safety: 109`, `doc: 160`, `sync_locks: 2`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.818
  * `Choke Point (Betweenness):` 0.0006 | `Ripple Effect (Closeness):` 0.090847
  * `Imports (Out-Degree: 20):` None
  * `Imported By (In-Degree: 73):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `wp-admin/css/colors/_mixins.scss` (CSS) | Magnitude: 0.85 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 95, closures: 13, class_start: 7, safety: 6
- `wp-content/themes/twentytwentyone/assets/sass/05-blocks/social-icons/_style.scss` (CSS) | Magnitude: 0.76 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 12, class_start: 6, closures: 2
- `wp-content/themes/twentytwentyone/assets/sass/05-blocks/latest-posts/_editor.scss` (CSS) | Magnitude: 0.23 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 108, closures: 17, class_start: 14, branch: 4
- `wp-content/themes/twentytwentyone/assets/sass/05-blocks/group/_style.scss` (CSS) | Magnitude: 0.79 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 41, class_start: 14, closures: 6, branch: 2
- `wp-content/themes/twentytwentyone/assets/sass/style-dark-mode.scss` (CSS) | Magnitude: 1.66 | Delta: **0.066** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 84, class_start: 15, api: 11, closures: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `wp-includes/widgets/class-wp-widget-categories.php` (PHP) | Magnitude: 132.64 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 115, branch: 30, state_mutation: 28, debug_prints: 21
- `wp-admin/includes/class-automatic-upgrader-skin.php` (PHP) | Magnitude: 71.26 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 55, state_mutation: 14, structural_boundaries: 11, branch: 9
- `wp-includes/Requests/src/Response/Headers.php` (PHP) | Magnitude: 47.26 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 45, structural_boundaries: 21, branch: 11, doc: 7
- `wp-includes/js/mediaelement/mediaelementplayer-legacy.css` (CSS) | Magnitude: 0.97 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 417, class_start: 147, ui_framework: 38, immutability_locks: 11
- `wp-includes/js/mediaelement/mediaelementplayer.css` (CSS) | Magnitude: 0.97 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 417, class_start: 147, ui_framework: 38, immutability_locks: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `wp-admin/includes/class-wp-filesystem-direct.php` (PHP) | Magnitude: 428.06 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 285, structural_boundaries: 90, branch: 74, state_mutation: 68
- `wp-includes/ms-deprecated.php` (PHP) | Magnitude: 343.92 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 274, state_mutation: 83, structural_boundaries: 67, branch: 55
- `wp-admin/includes/class-ftp-pure.php` (PHP) | Magnitude: 204.38 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 139, state_mutation: 41, branch: 39, structural_boundaries: 38
- `wp-activate.php` (PHP) | Magnitude: 56.68 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 114, branch: 31, state_mutation: 17, core_var_decl: 17
- `wp-admin/js/post.js` (JAVASCRIPT) | Magnitude: 461.7 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 900, branch: 205, state_mutation: 117, core_var_decl: 117

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `wp-includes/class-walker-page-dropdown.php` (PHP) | Magnitude: 57.54 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 24, state_mutation: 16, doc: 6, branch: 4
- `wp-includes/pomo/translations.php` (PHP) | Magnitude: 271.86 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 201, structural_boundaries: 68, state_mutation: 47, branch: 44
- `wp-includes/pluggable-deprecated.php` (PHP) | Magnitude: 38.32 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 45, structural_boundaries: 18, args: 18, branch: 14
- `wp-includes/rest-api/endpoints/class-wp-rest-widget-types-controller.php` (PHP) | Magnitude: 257.58 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 416, structural_boundaries: 62, state_mutation: 57, branch: 39
- `wp-includes/blocks/comments-pagination.php` (PHP) | Magnitude: 16.1 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 24, structural_boundaries: 6, branch: 3, doc: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `wp-includes/sitemaps/providers/class-wp-sitemaps-posts.php` (PHP) | Magnitude: 117.26 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 95, state_mutation: 30, structural_boundaries: 19, doc: 13
- `wp-includes/rest-api/endpoints/class-wp-rest-post-statuses-controller.php` (PHP) | Magnitude: 166.4 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 222, structural_boundaries: 36, state_mutation: 32, branch: 26
- `wp-includes/class-wp-url-pattern-prefixer.php` (PHP) | Magnitude: 44.98 | Delta: **0.087** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 51, structural_boundaries: 11, state_mutation: 8, doc: 7
- `wp-includes/l10n/class-wp-translation-controller.php` (PHP) | Magnitude: 335.88 | Delta: **0.099** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 196, branch: 60, state_mutation: 59, structural_boundaries: 54
- `wp-includes/rest-api/endpoints/class-wp-rest-template-autosaves-controller.php` (PHP) | Magnitude: 108.18 | Delta: **0.122** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 146, state_mutation: 25, structural_boundaries: 22, doc: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `wp-includes/php-ai-client/src/Providers/Models/Contracts/ModelInterface.php` (PHP) | Magnitude: 33.12 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 10, doc: 5, args: 4, func_start: 4
- `wp-includes/php-ai-client/src/Results/Contracts/ResultInterface.php` (PHP) | Magnitude: 36.77 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 11, doc: 6, args: 5, func_start: 5
- `wp-content/themes/twentytwentyone/assets/sass/05-blocks/blocks-editor.scss` (CSS) | Magnitude: 0.78 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: import: 30
- `wp-content/themes/twentytwentyone/assets/sass/05-blocks/blocks.scss` (CSS) | Magnitude: 0.78 | Delta: **0.165** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: import: 31
- `wp-content/themes/twentytwentyone/assets/sass/style.scss` (CSS) | Magnitude: 0.78 | Delta: **0.261** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: import: 32, doc: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `wp-content/themes/twentytwentyone/assets/sass/04-elements/links.scss` (CSS) | Magnitude: 0.8 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 43, class_start: 12, safety: 6, closures: 6
- `wp-admin/css/wp-admin.css` (CSS) | Magnitude: 0.77 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: import: 15
- `wp-includes/js/codemirror/javascript-lint.js` (JAVASCRIPT) | Magnitude: 30.24 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 44, safety: 10, branch: 9, structural_boundaries: 9
- `wp-trackback.php` (PHP) | Magnitude: 84.06 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 71, state_mutation: 32, branch: 28, io: 14
- `wp-content/themes/twentytwentyone/assets/sass/05-blocks/rss/_editor.scss` (CSS) | Magnitude: 0.83 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 82, class_start: 23, closures: 11, branch: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `wp-admin/js/widgets/media-widgets.js` (JAVASCRIPT) | Magnitude: 689.7 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 718, state_mutation: 156, branch: 119, core_var_decl: 102
- `wp-includes/js/jquery/ui/effect.js` (JAVASCRIPT) | Magnitude: 681.08 | Delta: **0.086** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 672, branch: 167, state_mutation: 110, core_var_decl: 107
- `wp-includes/js/jquery/ui/tooltip.js` (JAVASCRIPT) | Magnitude: 271.68 | Delta: **0.094** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 350, branch: 64, state_mutation: 42, core_var_decl: 42
- `wp-includes/admin-bar.php` (PHP) | Magnitude: 631.58 | Delta: **0.095** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 890, branch: 168, structural_boundaries: 116, state_mutation: 106

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `wp-includes/js/autosave.js` (JAVASCRIPT) | Magnitude: 686.58 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 415, branch: 120, state_mutation: 74, core_var_decl: 67
- `wp-admin/includes/meta-boxes.php` (PHP) | Magnitude: 788.88 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 1010, core_var_decl: 254, design_snake_case: 254, branch: 234
- `wp-includes/SimplePie/src/Source.php` (PHP) | Magnitude: 539.28 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 357, state_mutation: 120, structural_boundaries: 103, branch: 101
- `wp-includes/php-ai-client/src/Providers/OpenAiCompatibleImplementation/AbstractOpenAiCompatibleTextGenerationModel.php` (PHP) | Magnitude: 411.38 | Delta: **0.066** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 298, structural_boundaries: 115, branch: 99, state_mutation: 79

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `wp-includes/js/admin-bar.js` (JAVASCRIPT) | Magnitude: 214.16 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 246, branch: 72, structural_boundaries: 33, state_mutation: 30
- `wp-includes/widgets/class-wp-widget-tag-cloud.php` (PHP) | Magnitude: 128.94 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 119, branch: 26, debug_prints: 26, state_mutation: 24
- `wp-admin/link-parse-opml.php` (PHP) | Magnitude: 58.26 | Delta: **0.114** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 31, branch: 12, state_mutation: 12, safety: 7

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `wp-includes/js/codemirror/csslint.js` -> **Weston Ruter** (100.0% isolated ownership) | Magnitude: 6648.98
- `wp-includes/js/codemirror/esprima.js` -> **Weston Ruter** (100.0% isolated ownership) | Magnitude: 6403.8
- `wp-includes/class-wp-xmlrpc-server.php` -> **Weston Ruter** (100.0% isolated ownership) | Magnitude: 4685.98
- `wp-includes/PHPMailer/PHPMailer.php` -> **Sergey Biryukov** (100.0% isolated ownership) | Magnitude: 3609.98
- `wp-includes/class-wp-customize-manager.php` -> **Weston Ruter** (100.0% isolated ownership) | Magnitude: 3167.74

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `wp-includes/functions.php` -> **Severity: 0.756** (Bridge: 0.0076 * Flux: 100.0%)
- `wp-includes/theme.php` -> **Severity: 0.603** (Bridge: 0.006 * Flux: 100.0%)
- `wp-includes/rest-api.php` -> **Severity: 0.468** (Bridge: 0.0047 * Flux: 100.0%)
- `wp-includes/formatting.php` -> **Severity: 0.378** (Bridge: 0.0038 * Flux: 100.0%)
- `wp-includes/blocks.php` -> **Severity: 0.292** (Bridge: 0.0029 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `wp-includes/functions.php` -> **Severity: 11.167** (Embedded: 0.1441 * Error Risk: 77.472%)
- `wp-includes/formatting.php` -> **Severity: 10.593** (Embedded: 0.1315 * Error Risk: 80.5332%)
- `wp-includes/link-template.php` -> **Severity: 9.26** (Embedded: 0.1049 * Error Risk: 88.2805%)
- `wp-includes/pluggable.php` -> **Severity: 8.793** (Embedded: 0.1079 * Error Risk: 81.5025%)
- `wp-includes/capabilities.php` -> **Severity: 8.545** (Embedded: 0.1096 * Error Risk: 77.9687%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `wp-includes/class-pop3.php` -> **Severity: 656.244** (Blast Radius: 7.944 * Doc Risk: 82.6087%)
- `wp-includes/class-phpass.php` -> **Severity: 177.3** (Blast Radius: 1.773 * Doc Risk: 100.0%)
- `wp-admin/includes/class-pclzip.php` -> **Severity: 26.5** (Blast Radius: 0.265 * Doc Risk: 100.0%)
- `wp-admin/includes/template.php` -> **Severity: 26.014** (Blast Radius: 2.558 * Doc Risk: 10.1695%)
- `wp-includes/IXR/class-IXR-date.php` -> **Severity: 24.05** (Blast Radius: 0.481 * Doc Risk: 50.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 4969 literal sites + 621 sites through wrappers = 5590
- **`panics_and_aborts`:** 1106 literal sites + 2 sites through wrappers = 1108

- `_e` (function, debug_prints, primitive): 488 call sites in 76 files -- `wp-includes/l10n.php`
- `esc_html_e` (function, debug_prints, primitive): 44 call sites in 7 files -- `wp-includes/l10n.php`
- `wp_print_inline_script_tag` (function, debug_prints, primitive): 17 call sites in 14 files -- `wp-includes/script-loader.php`
- `_ex` (function, debug_prints, primitive): 16 call sites in 13 files -- `wp-includes/l10n.php`
- `bloginfo` (function, debug_prints, primitive): 13 call sites in 7 files -- `wp-includes/general-template.php`
- `the_post_thumbnail` (function, debug_prints, primitive): 12 call sites in 5 files -- `wp-includes/post-thumbnail-template.php`
- `twentytwenty_the_theme_svg` (function, debug_prints, primitive): 6 call sites in 1 files -- `wp-content/themes/twentytwenty/inc/svg-icons.php`
- `language_attributes` (function, debug_prints, primitive): 4 call sites in 4 files -- `wp-includes/general-template.php`
- `comment_author_link` (function, debug_prints, primitive): 3 call sites in 3 files -- `wp-includes/comment-template.php`
- `comment_reply_link` (function, debug_prints, primitive): 3 call sites in 2 files -- `wp-includes/comment-template.php`
- `previous_post_link` (function, debug_prints, primitive): 3 call sites in 2 files -- `wp-includes/link-template.php`
- `next_post_link` (function, debug_prints, primitive): 2 call sites in 2 files -- `wp-includes/link-template.php`
*(+9 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 69901 call pairs -- scoped 13.6%, unique 23.6%, ambiguous 10.7%, external 52.1%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| php | 49537 | 17.7% | 33.3% | 14.7% | 34.2% |
| javascript | 20364 | 3.5% | 0.0% | 0.8% | 95.7% |

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
