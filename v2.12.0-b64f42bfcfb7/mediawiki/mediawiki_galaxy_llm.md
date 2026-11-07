# ARCHITECTURAL_BRIEF: mediawiki
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/wikimedia/mediawiki.git` |
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
- **Scope:** 9391 analyzed artifact(s), 1160727 LOC.
- **Load-bearing artifact:** `includes/GlobalFunctions.php` -- 683 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `includes/ServiceWiring.php` -- pulls in 302 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `includes/Parser/Parser.php` at magnitude 7250.96 (structural weight, not risk).
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
| Total Artifacts | 12231 |
| Analyzed Artifacts (Scanned) | 9391 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2840 |
| Total LOC | 1160727 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 76.8% |
| Dominant Lang | PHP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4459 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1167 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 11.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.3422 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 416 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PHP | 5409 | 707280 | 57.6% |
| JSON | 2879 | 360436 | 30.7% |
| JAVASCRIPT | 458 | 70698 | 4.9% |
| CSS | 234 | 9661 | 2.5% |
| XML | 121 | 0 | 1.3% |
| SQLITE | 104 | 8054 | 1.1% |
| PLAINTEXT | 57 | 2 | 0.6% |
| POSTGRESQL | 45 | 331 | 0.5% |
| MARKDOWN | 37 | 0 | 0.4% |
| HTML | 37 | 3423 | 0.4% |
| SHELL | 5 | 68 | 0.1% |
| YAML | 3 | 430 | 0.0% |
| MAKEFILE | 1 | 2 | 0.0% |
| PYTHON | 1 | 342 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 9388 |
| unknown | unknown | 2 |
| utf-8 | bom | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 43%, Declarative / Non-Code 12%, Large Core Modules (3) 10%, Interface Declarations Files 8%, Parameter Forwarders Files 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 9145 | 97.4% |
| Unknown | 2 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Minified & Vendor Opaque Mass | 152 | 1.6% |
| Static: Literature & Documentation | 92 | 1.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2840*

**Composition by Extension & Reason:**
- `.svg`: 1122x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 301x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Static Asset Blob without Intent: 1121 LOC), 2x Excluded (Static Asset Blob without Intent: 1973 LOC)
- `.js`: 382x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 7x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.css`: 132x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 1 exceeds 500 chars), 1x Excluded (Saturation: Line 11 exceeds 500 chars)
- `.png`: 80x Excluded (Explicitly Denied Extension: '.png')
- `.php`: 61x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 4683 LOC), 1x Excluded (Machine-Generated Source Code Signature: 45 LOC)
- `no_extension`: 53x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable), 2x Excluded (Unsupported Extension: '.data-parsoid')
- `.cjs`: 54x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 48x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 56 LOC)
- `.less`: 32x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jpg`: 32x Excluded (Explicitly Denied Extension: '.jpg')
- `.mustache`: 22x Excluded (Unsupported Extension: '.mustache')
- `.txt`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 4348 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 18083 LOC)
- `.manual`: 16x Excluded (Unsupported Extension: '.manual')
- `.xsd`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 10.2 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.8 | 30.5 | 48.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 20.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 3.6 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 89.5 | 3.4 | 1.2 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 4.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 28.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 98.5 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 4.8 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 5.1 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 13.9 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 93.2 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 19432 | 2792 | 5 | `includes/ServiceWiring.php` |
| cleanup | 1128 | 515 | 0 | `resources/src/mediawiki.authenticationPopup/AuthPopup.js` |
| guards | 43403 | 3621 | 11 | `resources/lib/sinonjs/sinon.js` |
| danger | 9415 | 1706 | 2 | `includes/Language/Language.php` |
| concurrency | 6801 | 672 | 0 | `tests/phpunit/unit/includes/libs/Leximorph/Handler/PluralTest.php` |
| connectivity | 33896 | 4890 | 9 | `includes/MainConfigSchema.php` |
| io | 2573 | 473 | 0 | `tests/phan/TaintCheckAnnotationsTest.php` |
| crypto | 0 | 0 | 0 | - |
| ipc | 129 | 76 | 0 | `tests/phan/TaintCheckAnnotationsTest.php` |
| time | 827 | 248 | 0 | `tests/phpunit/includes/Language/LanguageIntegrationTest.php` |
| serialization | 727 | 327 | 0 | `includes/JobQueue/JobQueueRedis.php` |
| regex | 1652 | 497 | 0 | `resources/lib/sinonjs/sinon.js` |
| events | 1352 | 233 | 0 | `resources/lib/qunitjs/qunit.js` |
| tests | 20326 | 1413 | 3 | `tests/phpunit/includes/Auth/AuthManagerTest.php` |
| docs | 46740 | 5624 | 12 | `includes/MainConfigSchema.php` |
| debt | 4834 | 1782 | 1 | `tests/phan/TaintCheckAnnotationsTest.php` |
| mutation | 143630 | 5003 | 35 | `resources/lib/sinonjs/sinon.js` |
| dead_code | 25549 | 3871 | 8 | `includes/HookContainer/HookRunner.php` |
| credential | 605 | 131 | 0 | `includes/Installer/i18n/ja.json` |
| threat | 4519 | 214 | 0 | `languages/i18n/jv-java.json` |
| ml_ai | 594 | 201 | 0 | `includes/Api/ApiUpload.php` |
| ui | 995 | 253 | 0 | `tests/phpunit/includes/Api/ApiComparePagesTest.php` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/phan/TaintCheckAnnotationsTest.php` (Hits: 786)
- `tests/uidesign/confirmable.html` (Hits: 75)
- `includes/Api/ApiMain.php` (Hits: 48)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **GlobalFunctions.php** (`includes/GlobalFunctions.php`) — 683 inbound connections
2. **Title.php** (`includes/Title/Title.php`) — 579 inbound connections
3. **MediaWikiServices.php** (`includes/MediaWikiServices.php`) — 485 inbound connections
4. **User.php** (`includes/User/User.php`) — 407 inbound connections
5. **UserIdentity.php** (`includes/User/UserIdentity.php`) — 299 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ServiceWiring.php** (`includes/ServiceWiring.php`) — 302 outbound dependencies
2. **MediaWikiServices.php** (`includes/MediaWikiServices.php`) — 241 outbound dependencies
3. **sinon.js** (`resources/lib/sinonjs/sinon.js`) — 164 outbound dependencies
4. **SpecialPageFactory.php** (`includes/SpecialPage/SpecialPageFactory.php`) — 159 outbound dependencies
5. **EditPage.php** (`includes/EditPage/EditPage.php`) — 104 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `internalStop` **(I/O & Config Routines)** (@ `resources/lib/qunitjs/qunit.js`) -> Impact: **969.6** | LOC: 4272
  * *Intent:* * This is close to impossible because this error only happens if the original test * succesfully finished first (since other failure scenarios kill pa...
- `internalParse` **(Many-Argument Workhorses)** (@ `includes/Parser/Parser.php`) -> Impact: **691.4** | LOC: 1868
  * *Intent:* /** * Helper function for parse() that transforms wiki markup into half-parsed * HTML. Only called for $mOutputType == self::OT_HTML. * * @internal * ...
- `sprintfDate` **(Many-Argument Workhorses)** (@ `includes/Language/Language.php`) -> Impact: **670.0** | LOC: 1862
  * *Intent:* * $ts is UTC if $zone is not given. * * @param string $format * @param string $ts 14-character timestamp * YYYYMMDDHHMMSS * 01234567890123 * @param Da...
- `handleExternalLinks` **(Many-Argument Workhorses)** (@ `includes/Parser/Parser.php`) -> Impact: **600.4** | LOC: 1910
  * *Intent:* /** * Replace external links (REL) * * Note: this is all very hackish and the order of execution matters a lot. * Make sure to run tests/parser/parser...
- `handleInternalLinks2` **(Many-Argument Workhorses)** (@ `includes/Parser/Parser.php`) -> Impact: **557.7** | LOC: 1877
  * *Intent:* /** * Process [[ ]] wikilinks (RIL) * @param string &$s * @return LinkHolderArray */
- `makeFormattedData` **(Many-Argument Workhorses)** (@ `includes/Media/FormatMetadata.php`) -> Impact: **538.9** | LOC: 709
  * *Intent:* /** * Numbers given by Exif user agents are often magical, that is they * should be replaced by a detailed explanation depending on their * value whic...
- `handleTables` **(Many-Argument Workhorses)** (@ `includes/Parser/Parser.php`) -> Impact: **461.3** | LOC: 1872
  * *Intent:* /** * Parse the wiki syntax used to render tables. * * @param string $text * @return string */
- `withGlobal` **(Many-Argument Workhorses)** (@ `resources/lib/sinonjs/sinon.js`) -> Impact: **449.0** | LOC: 1710
  * *Intent:* */ /* eslint-enable jsdoc/require-property-description */ /* eslint-disable complexity */ /** * Mocks available features in the specified global names...
- `showDiffPage` **(Many-Argument Workhorses)** (@ `includes/Diff/DifferenceEngine.php`) -> Impact: **422.5** | LOC: 1747
  * *Intent:* /** * @param bool $diffOnly */
- `cleanSig` **(Many-Argument Workhorses)** (@ `includes/Parser/Parser.php`) -> Impact: **397.8** | LOC: 1721
  * *Intent:* /** * Clean up signature text * * 1) Strip 3, 4 or 5 tildes out of signatures, see {@link cleanSigInSig} * 2) Substitute all transclusions * * @param ...

*Function archetypes referenced above:*
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `includes/Api` | 147 | 31144.4 | 40.14% | 74.63% |
| `includes/Specials` | 132 | 19081.02 | 25.52% | 73.62% |
| `includes/Parser` | 44 | 18472.69 | 25.93% | 64.92% |
| `maintenance` | 201 | 17829.7 | 35.34% | 28.55% |
| `languages/messages` | 519 | 10241.32 | 0.22% | 0.12% |
| `tests/phpunit/integration/includes/Json` | 3 | 10024.16 | 3.59% | 0.0% |
| `languages/i18n/datetime` | 578 | 9541.42 | 0.0% | 0.0% |
| `includes/Page` | 49 | 9501.92 | 20.85% | 47.89% |
| `includes/Language` | 32 | 8778.61 | 21.23% | 63.42% |
| `includes/Media` | 38 | 7873.8 | 26.69% | 59.64% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `resources/src/moment/moment-locale-overrides.js` -> **100.0%** Exposure
- `includes/Api/ApiLinkAccount.php` -> **100.0%** Exposure
- `includes/Auth/AbstractPrimaryAuthenticationProvider.php` -> **100.0%** Exposure
- `includes/Auth/AbstractSecondaryAuthenticationProvider.php` -> **100.0%** Exposure
- `includes/Category/CategoriesRdf.php` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `resources/lib/CLDRPluralRuleParser/CLDRPluralRuleParser.js` -> **100.0%** Exposure
- `resources/lib/intersection-observer/intersection-observer.js` -> **100.0%** Exposure
- `resources/lib/jquery.i18n/src/languages/fi.js` -> **100.0%** Exposure
- `resources/lib/jquery.i18n/src/languages/ga.js` -> **100.0%** Exposure
- `resources/lib/jquery.i18n/src/languages/la.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `includes/HookContainer/HookRunner.php` -> **540** Orphaned Functions | **0** Duplicates
- `includes/MediaWikiServices.php` -> **244** Orphaned Functions | **0** Duplicates
- `tests/phpunit/includes/Title/TitleTest.php` -> **149** Orphaned Functions | **0** Duplicates
- `includes/libs/Rdbms/Database/DBConnRef.php` -> **135** Orphaned Functions | **0** Duplicates
- `tests/phpunit/includes/Output/OutputPageTest.php` -> **123** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `tests/phpunit/includes/Api/ApiLoginTest.php` -> **93.201%** Exposure
- `tests/phpunit/includes/Auth/TemporaryPasswordPrimaryAuthenticationProviderTest.php` -> **34.68%** Exposure
- `tests/phpunit/includes/Auth/LocalPasswordPrimaryAuthenticationProviderTest.php` -> **17.6514%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `16` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `29016` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `includes/Parser/Parser.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.697)
- **Top Global Matches:** file_cluster_6: 8.697, file_cluster_4: 10.177, file_cluster_12: 15.853
- **Magnitude:** 7250.96 | **LOC:** 6513 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 29.6%
- **Blast Radius:** changing it is visible to **72** in-repo importer(s); it depends on **82**; blast radius 1.632; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (80.4%), Guard Balance (formerly Safety Score) (80.3%), Complexity Load (formerly Cognitive Load) (52.3%)
- **Documentation Coverage:** 1.5789% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `internalParse` **(Many-Argument Workhorses)** (Impact: 691.4)
    * *Intent:* /** * Helper function for parse() that transforms wiki markup into half-parsed * HTML. Only called f...
  * `handleExternalLinks` **(Many-Argument Workhorses)** (Impact: 600.4)
    * *Intent:* /** * Replace external links (REL) * * Note: this is all very hackish and the order of execution mat...
  * `handleInternalLinks2` **(Many-Argument Workhorses)** (Impact: 557.7)
    * *Intent:* /** * Process [[ ]] wikilinks (RIL) * @param string &$s * @return LinkHolderArray */
  * `handleTables` **(Many-Argument Workhorses)** (Impact: 461.3)
    * *Intent:* /** * Parse the wiki syntax used to render tables. * * @param string $text * @return string */
  * `cleanSig` **(Many-Argument Workhorses)** (Impact: 397.8)
    * *Intent:* /** * Clean up signature text * * 1) Strip 3, 4 or 5 tildes out of signatures, see {@link cleanSigIn...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 814 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 2909
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 753`, `structural_boundaries: 630`, `args: 160`, `func_start: 150`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 182`, `state_mutation: 1281`, `dead_code: 4`, `planned_debt: 7`, `fragile_debt: 17`, `unreferenced_by_name: 42`
* *Architecture:* `io: 3`, `api: 129`, `concurrency: 1`, `import: 110`
* *Defense:* `safety: 112`, `doc: 193`, `sync_locks: 11`, `immutability_locks: 16`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.632
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.12806
  * `Imports (Out-Degree: 68):` BadMethodCallException, DateTime, DateTimeZone, DeprecationHelper, Exception, InvalidArgumentException, LogicException, MediaWiki\Category\TrackingCategories...
  * `Imported By (In-Degree: 72):` (Excluded from Brief to save tokens)

### `tests/phpunit/integration/includes/Json/key1.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.052
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/phpunit/integration/includes/Json/key2.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.052
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `includes/Output/OutputPage.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.881)
- **Top Global Matches:** file_cluster_12: 7.881, file_cluster_7: 10.229, file_cluster_4: 10.439
- **Magnitude:** 3384.94 | **LOC:** 5226 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 9.1%
- **Blast Radius:** changing it is visible to **100** in-repo importer(s); it depends on **62**; blast radius 2.351; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (85.6%), Guard Balance (formerly Safety Score) (75.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (54.3%)
- **Documentation Coverage:** 1.6713% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `showPermissionStatus` **(Many-Argument Workhorses)** (Impact: 384.1)
    * *Intent:* /** * Output a standard permission error page * * @param PermissionStatus $status * @param string|nu...
  * `sendCacheControl` **(I/O & Config Routines)** (Impact: 250.2)
    * *Intent:* /** * Send cache control HTTP headers */
  * `addParserOutputMetadata` **(Compute Cores)** (Impact: 47.1)
    * *Intent:* /** * Add all metadata associated with a ParserOutput object, but without the actual HTML. This * in...
  * `getJSVars` **(Compute Cores)** (Impact: 45.6)
    * *Intent:* * in other words, page-independent/site-wide variables (without state). * These would add a blocking...
  * `output` **(Compute Cores)** (Impact: 45.5)
    * *Intent:* /** * Finally, all the text has been munged and accumulated into * the object, let's actually output...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 439 instances
* *State Mutation (weighted view):* 1598
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 389`, `structural_boundaries: 605`, `args: 211`, `func_start: 204`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 131`, `state_mutation: 720`, `dead_code: 1`, `planned_debt: 8`, `fragile_debt: 8`, `unreferenced_by_name: 77`
* *Architecture:* `io: 34`, `api: 181`, `import: 80`
* *Defense:* `safety: 60`, `doc: 272`, `immutability_locks: 7`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.351
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.11726
  * `Imports (Out-Degree: 47):` CSSJanus, DeprecationHelper, Exception, InvalidArgumentException, MediaWiki\Config\Config, MediaWiki\Content\Content, MediaWiki\Content\JavaScriptContent, MediaWiki\Content\TextContent...
  * `Imported By (In-Degree: 100):` (Excluded from Brief to save tokens)

### `includes/Language/Language.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 10.421)
- **Top Global Matches:** file_cluster_12: 10.421, file_cluster_7: 10.566, file_cluster_5: 11.38
- **Magnitude:** 3355.56 | **LOC:** 5079 | **CtrlFlow:** 11.7% | **Authorship Centralization:** 28.6%
- **Blast Radius:** changing it is visible to **198** in-repo importer(s); it depends on **38**; blast radius 6.567; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (65.4%), Complexity Load (formerly Cognitive Load) (46.2%)
- **Documentation Coverage:** 1.227% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sprintfDate` **(Many-Argument Workhorses)** (Impact: 670.0)
    * *Intent:* * $ts is UTC if $zone is not given. * * @param string $format * @param string $ts 14-character times...
  * `truncateInternal` **(Many-Argument Workhorses)** (Impact: 101.9)
    * *Intent:* * one common method, allowing users to provide the length measurement function and * function for fi...
  * `formatTimePeriod` **(Many-Argument Workhorses)** (Impact: 47.9)
    * *Intent:* /** * Formats a time given in seconds into a string representation of that time. * * @param int|floa...
  * `formatNumInternal` **(Many-Argument Workhorses)** (Impact: 47.3)
    * *Intent:* /** * Internal implementation function, shared between formatNum and formatNumNoSeparators. * * @par...
  * `translateBlockExpiry` **(Many-Argument Workhorses)** (Impact: 26.1)
    * *Intent:* /** * @todo Maybe translate block durations. Note that this function is somewhat misnamed: it * deal...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 481 instances
* *State Mutation (weighted view):* 1890
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 489`, `structural_boundaries: 774`, `args: 162`, `func_start: 157`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 421`, `state_mutation: 928`, `planned_debt: 11`, `fragile_debt: 4`, `unreferenced_by_name: 32`
* *Architecture:* `io: 1`, `api: 139`, `import: 93`
* *Defense:* `safety: 45`, `doc: 198`, `immutability_locks: 20`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.567
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.147003
  * `Imports (Out-Degree: 23):` CLDRPluralRuleParser\Evaluator, DateTime, DateTimeImmutable, DateTimeInterface, DateTimeZone, DebugInfoTrait, InvalidArgumentException, Locale...
  * `Imported By (In-Degree: 198):` (Excluded from Brief to save tokens)

### `includes/EditPage/EditPage.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.69)
- **Top Global Matches:** file_cluster_4: 5.69, file_cluster_6: 8.013, file_cluster_16: 12.626
- **Magnitude:** 2684.7 | **LOC:** 4507 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 51.5%
- **Blast Radius:** changing it is visible to **26** in-repo importer(s); it depends on **104**; blast radius 0.673; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (74.2%), Guard Balance (formerly Safety Score) (71.7%), Complexity Load (formerly Cognitive Load) (33.2%)
- **Documentation Coverage:** 15.6522% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `internalAttemptSave` **(Many-Argument Workhorses)** (Impact: 104.0)
    * *Intent:* * @param bool $markAsBot True if edit is being made under the bot right * and the bot wishes the edi...
  * `getPreviewText` **(I/O & Config Routines)** (Impact: 89.1)
    * *Intent:* /** * Get the rendered text for previewing. * @throws MWException * @return string */
  * `handleStatus` **(Many-Argument Workhorses)** (Impact: 85.5)
    * *Intent:* /** * Handle status, such as after attempt save * * @param EditPageStatus $status * @param array|fal...
  * `edit` **(I/O & Config Routines)** (Impact: 49.5)
    * *Intent:* /** * This is the function that gets called for "action=edit". It * sets up various member variables...
  * `generateUndoEditSummary` **(Many-Argument Workhorses)** (Impact: 46.3)
    * *Intent:* /** * When using the "undo" action, generate a default edit summary and save it * to $this->summary ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 427 instances
* *State Mutation (weighted view):* 1520
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 520`, `structural_boundaries: 446`, `args: 94`, `func_start: 93`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 666`, `planned_debt: 10`, `fragile_debt: 11`, `unreferenced_by_name: 5`
* *Architecture:* `io: 3`, `api: 56`, `import: 108`
* *Defense:* `safety: 53`, `doc: 157`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.673
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.079372
  * `Imports (Out-Degree: 93):` BadMethodCallException, DeprecationHelper, MediaWiki\Actions\WatchAction, MediaWiki\Auth\AuthManager, MediaWiki\CommentStore\CommentStore, MediaWiki\CommentStore\CommentStoreComment, MediaWiki\Config\Config, MediaWiki\Content\Content...
  * `Imported By (In-Degree: 26):` (Excluded from Brief to save tokens)

### `includes/libs/Rdbms/Database/Database.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.798)
- **Top Global Matches:** file_cluster_15: 6.798, file_cluster_16: 7.038, file_cluster_12: 7.695
- **Magnitude:** 2366.82 | **LOC:** 3606 | **CtrlFlow:** 15.3% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **30** in-repo importer(s); it depends on **19**; blast radius 0.527; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.3%), Mutation Surface (formerly State Flux) (85.0%), Guard Balance (formerly Safety Score) (70.2%), Complexity Load (formerly Cognitive Load) (44.3%)
- **Documentation Coverage:** 1.4793% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sourceStream` **(Many-Argument Workhorses)** (Impact: 52.4)
    * *Intent:* /** @inheritDoc */
  * `assessConnectionLoss` **(Many-Argument Workhorses)** (Impact: 48.3)
    * *Intent:* * is considered acceptable for DBO_TRX logic. * * If state was lost, but that loss was discovered du...
  * `__construct` **(Defensive Guards)** (Impact: 37.0)
    * *Intent:* /** * @note exceptions for missing libraries/drivers should be thrown in initConnection() * @param a...
  * `attemptQuery` **(Many-Argument Workhorses)** (Impact: 34.5)
    * *Intent:* * - write callers * - last write time * - affected row count of the last write * - whether writes oc...
  * `handleErroredQuery` **(Many-Argument Workhorses)** (Impact: 32.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 331 instances
* *Api Near Db Sink:* 4 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 82
* *State Mutation (weighted view):* 1117
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 335`, `structural_boundaries: 512`, `args: 202`, `func_start: 197`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 1`, `state_mutation: 455`, `planned_debt: 3`, `fragile_debt: 1`, `unreferenced_by_name: 107`
* *Architecture:* `io: 1`, `api: 156`, `import: 24`
* *Defense:* `safety: 71`, `doc: 254`, `sync_locks: 7`, `immutability_locks: 41`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.527
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.114572
  * `Imports (Out-Degree: 29):` Exception, InvalidArgumentException, LogicException, Psr\Log\LoggerAwareInterface, Psr\Log\LoggerInterface, Psr\Log\NullLogger, RuntimeException, Stringable...
  * `Imported By (In-Degree: 30):` (Excluded from Brief to save tokens)

### `tests/Common/Parser/ParserTestRunner.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.578)
- **Top Global Matches:** file_cluster_4: 6.578, file_cluster_6: 7.106, file_cluster_16: 14.035
- **Magnitude:** 2191.72 | **LOC:** 3281 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 69.2%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **75**; blast radius 0.074; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (70.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (63.7%), Complexity Load (formerly Cognitive Load) (47.4%)
- **Documentation Coverage:** 20.4301% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addParserOutputInfo` **(Many-Argument Workhorses)** (Impact: 125.1)
    * *Intent:* /** * Add information from the parser output to the result string * * @param string &$out The "actua...
  * `processResults` **(Many-Argument Workhorses)** (Impact: 69.6)
    * *Intent:* /** * This processes test results and updates the known failures info for the test * * @param Parser...
  * `runParsoidTest` **(Many-Argument Workhorses)** (Impact: 58.2)
    * *Intent:* * running in 'integrated' mode, and compare the output against the * expected results. * * Prints st...
  * `wt2html` **(Many-Argument Workhorses)** (Impact: 48.5)
    * *Intent:* /** * Run wt2html on the test * * @param Parsoid $parsoid * @param PageConfig $pageConfig * @param P...
  * `runLegacyTest` **(Defensive Guards)** (Impact: 46.7)
    * *Intent:* /** * Run a given wikitext input through a freshly-constructed instance * of the legacy wiki parser,...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Cascading Flux:* 326 instances
* *Memory Alloc (weighted view):* 61
* *State Mutation (weighted view):* 1158
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 380`, `structural_boundaries: 409`, `args: 105`, `func_start: 65`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 506`, `dead_code: 2`, `planned_debt: 5`, `fragile_debt: 2`, `unreferenced_by_name: 6`
* *Architecture:* `io: 5`, `api: 30`, `import: 81`
* *Defense:* `safety: 113`, `doc: 71`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.074
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.000426
  * `Imports (Out-Degree: 53):` BadMethodCallException, MediaWikiIntegrationTestCase, MediaWiki\Config\ServiceOptions, MediaWiki\Content\WikitextContent, MediaWiki\Context\IContextSource, MediaWiki\Context\RequestContext, MediaWiki\FileRepo\RepoGroup, MediaWiki\HookContainer\HookRunner...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `includes/Title/Title.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.936)
- **Top Global Matches:** file_cluster_12: 7.936, file_cluster_15: 9.838, file_cluster_16: 10.024
- **Magnitude:** 2182.92 | **LOC:** 3898 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 28.6%
- **Blast Radius:** changing it is visible to **579** in-repo importer(s); it depends on **49**; blast radius 8.194; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (97.2%), Guard Balance (formerly Safety Score) (74.5%), Complexity Load (formerly Cognitive Load) (33.1%)
- **Documentation Coverage:** 2.349% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `secureAndSplit` **(Many-Argument Workhorses)** (Impact: 211.8)
    * *Intent:* * * Assumes that $text is urldecoded * and uses underscores, but not otherwise munged. This function...
  * `convertByteClassToUnicodeClass` **(Compute Cores)** (Impact: 38.6)
    * *Intent:* /** * Utility method for converting a character sequence from bytes to Unicode. * * Primary usecase ...
  * `getLocalURL` **(Compute Cores)** (Impact: 37.8)
    * *Intent:* * $wgServer is prepended to make an absolute URL. * * @see self::getFullURL to always get an absolut...
  * `makeName` **(Many-Argument Workhorses)** (Impact: 18.2)
    * *Intent:* /** * Make a prefixed DB key from a DB key and a namespace index * * @param int $ns Numerical repres...
  * `loadFromRow` **(Defensive Guards)** (Impact: 15.6)
    * *Intent:* /** * Load Title object fields from a DB row. * If false is given, the title will be treated as non-...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 316 instances
* *State Mutation (weighted view):* 1075
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 322`, `structural_boundaries: 526`, `args: 165`, `func_start: 163`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 443`, `dead_code: 1`, `planned_debt: 10`, `fragile_debt: 3`, `unreferenced_by_name: 69`
* *Architecture:* `api: 147`, `import: 53`
* *Defense:* `safety: 40`, `doc: 192`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.194
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.158084
  * `Imports (Out-Degree: 39):` InvalidArgumentException, LinkTargetTrait, MediaWiki\Context\RequestContext, MediaWiki\DAO\WikiAwareEntityTrait, MediaWiki\Deferred\AutoCommitUpdate, MediaWiki\Deferred\DeferredUpdates, MediaWiki\Deferred\LinksUpdate\CategoryLinksTable, MediaWiki\Deferred\LinksUpdate\ImageLinksTable...
  * `Imported By (In-Degree: 579):` (Excluded from Brief to save tokens)

### `includes/Revision/RevisionStore.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.2)
- **Top Global Matches:** file_cluster_4: 5.2, file_cluster_16: 8.391, file_cluster_15: 8.82
- **Magnitude:** 2079.74 | **LOC:** 3443 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **67** in-repo importer(s); it depends on **57**; blast radius 0.469; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (69.3%), Debt Markers (formerly Tech Debt) (60.1%), Complexity Load (formerly Cognitive Load) (41.8%)
- **Documentation Coverage:** 5.2632% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `newRevisionsFromBatch` **(Many-Argument Workhorses)** (Impact: 87.8)
    * *Intent:* * always be loaded. * 'content' - whether the actual content of the slots should be * preloaded. * '...
  * `newRevisionFromRowAndSlots` **(Many-Argument Workhorses)** (Impact: 69.0)
    * *Intent:* * @param stdClass $row A database row generated from a query based on RevisionSelectQueryBuilder * @...
  * `getSlotRowsForBatch` **(Many-Argument Workhorses)** (Impact: 46.9)
    * *Intent:* * all slots are fetched * 'blobs' - whether the serialized content of each slot should be loaded. * ...
  * `newRevisionFromArchiveRowAndSlots` **(Many-Argument Workhorses)** (Impact: 44.5)
    * *Intent:* * @param stdClass $row * @param null|stdClass[]|RevisionSlots $slots * - Database rows generated fro...
  * `getRevisionIdsBetween` **(Many-Argument Workhorses)** (Impact: 41.9)
    * *Intent:* * @param string|array $options Single option, or an array of options: * RevisionStore::INCLUDE_OLD I...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 314 instances
* *State Mutation (weighted view):* 1016
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 334`, `structural_boundaries: 369`, `args: 86`, `func_start: 74`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 388`, `planned_debt: 14`, `fragile_debt: 4`, `unreferenced_by_name: 27`
* *Architecture:* `api: 47`, `import: 60`
* *Defense:* `safety: 91`, `doc: 75`, `sync_locks: 2`, `immutability_locks: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.469
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.125044
  * `Imports (Out-Degree: 54):` InvalidArgumentException, LegacyArticleIdAccess, LogicException, MediaWiki\CommentStore\CommentStore, MediaWiki\CommentStore\CommentStoreComment, MediaWiki\Content\Content, MediaWiki\Content\FallbackContent, MediaWiki\Content\IContentHandlerFactory...
  * `Imported By (In-Degree: 67):` (Excluded from Brief to save tokens)

### `includes/Linker/Linker.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.908)
- **Top Global Matches:** file_cluster_4: 6.908, file_cluster_12: 9.957, file_cluster_15: 11.825
- **Magnitude:** 2040.08 | **LOC:** 2040 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **66** in-repo importer(s); it depends on **26**; blast radius 0.609; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.1%), Debt Markers (formerly Tech Debt) (53.2%), Complexity Load (formerly Cognitive Load) (43.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `makeImageLink` **(Many-Argument Workhorses)** (Impact: 195.8)
    * *Intent:* * link-url URL to link to * link-title LinkTarget object to link to * link-target Value for the targ...
  * `makeThumbLink2` **(Many-Argument Workhorses)** (Impact: 120.6)
    * *Intent:* /** * @param LinkTarget $title * @param File|false $file * @param array $frameParams * @param array ...
  * `formatHiddenCategories` **(Compute Cores)** (Impact: 65.4)
    * *Intent:* /** * Returns HTML for the "hidden categories on this page" list. * * @since 1.16.3 * @param array $...
  * `makeBrokenImageLinkObj` **(Many-Argument Workhorses)** (Impact: 42.0)
    * *Intent:* /** * Make a "broken" link to an image * * @since 1.16.3 * @param LinkTarget $title * @param string ...
  * `userToolLinkArray` **(Many-Argument Workhorses)** (Impact: 39.8)
    * *Intent:* * @param int $userId User identifier * @param string $userText User name or IP address * @param bool...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 339 instances
* *State Mutation (weighted view):* 1102
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 281`, `structural_boundaries: 225`, `args: 47`, `func_start: 45`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 424`, `planned_debt: 8`, `fragile_debt: 1`, `unreferenced_by_name: 17`
* *Architecture:* `api: 45`, `import: 27`
* *Defense:* `safety: 77`, `doc: 49`, `immutability_locks: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.609
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.103701
  * `Imports (Out-Degree: 22):` MediaWiki\Context\ContextSource, MediaWiki\Context\DerivativeContext, MediaWiki\Context\IContextSource, MediaWiki\Context\RequestContext, MediaWiki\FileRepo\File\File, MediaWiki\HookContainer\HookRunner, MediaWiki\Html\Html, MediaWiki\Html\HtmlHelper...
  * `Imported By (In-Degree: 66):` (Excluded from Brief to save tokens)

### `includes/Diff/DifferenceEngine.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.629)
- **Top Global Matches:** file_cluster_4: 5.629, file_cluster_16: 10.337, file_cluster_12: 10.68
- **Magnitude:** 1886.54 | **LOC:** 2494 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 27.3%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **46**; blast radius 0.586; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (74.8%), Complexity Load (formerly Cognitive Load) (45.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (40.2%)
- **Documentation Coverage:** 2.6087% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `showDiffPage` **(Many-Argument Workhorses)** (Impact: 422.5)
    * *Intent:* /** * @param bool $diffOnly */
  * `getDiffBody` **(I/O & Config Routines)** (Impact: 28.6)
    * *Intent:* /** * Get the diff table body, without header * * @return string|false */
  * `addHeader` **(Many-Argument Workhorses)** (Impact: 27.9)
    * *Intent:* /** * Add the header to a diff body * * @param string $diff Diff body * @param string $otitle Old re...
  * `loadRevisionData` **(I/O & Config Routines)** (Impact: 26.4)
    * *Intent:* /** * Load revision metadata for the specified revisions. If newid is 0, then compare * the old revi...
  * `getMultiNotice` **(I/O & Config Routines)** (Impact: 24.7)
    * *Intent:* /** * If there are revisions between the ones being compared, return a note saying so. * * @return s...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 281 instances
* *State Mutation (weighted view):* 928
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 292`, `structural_boundaries: 313`, `args: 71`, `func_start: 70`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 366`, `dead_code: 1`, `planned_debt: 4`, `fragile_debt: 5`
* *Architecture:* `io: 19`, `api: 47`, `import: 47`
* *Defense:* `safety: 34`, `doc: 101`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.586
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.083663
  * `Imports (Out-Degree: 37):` BadMethodCallException, DeprecationHelper, Exception, InvalidArgumentException, LogicException, MediaWiki\ChangeTags\ChangeTags, MediaWiki\CommentFormatter\CommentFormatter, MediaWiki\Content\Content...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `includes/Parser/ParserOutput.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.723)
- **Top Global Matches:** file_cluster_15: 7.723, file_cluster_4: 7.88, file_cluster_16: 8.356
- **Magnitude:** 1879.42 | **LOC:** 3448 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 53.8%
- **Blast Radius:** changing it is visible to **161** in-repo importer(s); it depends on **24**; blast radius 2.848; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (67.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (60.3%), Connectivity (formerly Api Exposure) (49.1%)
- **Documentation Coverage:** 5.4237% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `initFromJson` **(Defensive Guards)** (Impact: 109.8)
    * *Intent:* /** * Initialize member fields from an array returned by jsonSerialize(). * @param array $jsonData *...
  * `getLinkList` **(Many-Argument Workhorses)** (Impact: 95.9)
    * *Intent:* * the metadata. * * Each element of the returned array has a LinkTarget as the 'link' * property. Lo...
  * `collectMetadata` **(Compute Cores)** (Impact: 71.2)
    * *Intent:* /** * Adds the metadata collected in this ParserOutput to the supplied * ContentMetadataCollector. T...
  * `mergeMapStrategy` **(Stateful Encapsulated Methods)** (Impact: 33.5)
  * `mergeInternalMetaDataFrom` **(Compute Cores)** (Impact: 27.4)
    * *Intent:* /** * Merges internal metadata such as flags, accessed options, and profiling info * from $source in...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 251 instances
* *State Mutation (weighted view):* 833
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 393`, `structural_boundaries: 382`, `args: 161`, `func_start: 155`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 331`, `planned_debt: 8`, `fragile_debt: 1`
* *Architecture:* `io: 2`, `api: 144`, `import: 25`
* *Defense:* `safety: 96`, `doc: 188`, `immutability_locks: 9`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.848
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.11971
  * `Imports (Out-Degree: 16):` ContentMetadataCollectorCompat, InvalidArgumentException, LogicException, MediaWiki\DAO\WikiAwareEntity, MediaWiki\Edit\ParsoidRenderID, MediaWiki\Json\JsonDeserializable, MediaWiki\MainConfigNames, MediaWiki\MediaWikiServices...
  * `Imported By (In-Degree: 161):` (Excluded from Brief to save tokens)

### `includes/libs/Rdbms/Platform/SQLPlatform.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.434)
- **Top Global Matches:** file_cluster_12: 7.434, file_cluster_4: 8.752, file_cluster_15: 9.999
- **Magnitude:** 1869.18 | **LOC:** 2144 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **18**; blast radius 0.501; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (98.1%), Guard Balance (formerly Safety Score) (76.5%), Complexity Load (formerly Cognitive Load) (46.5%)
- **Documentation Coverage:** 2.2857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `selectSQLText` **(Many-Argument Workhorses)** (Impact: 136.8)
    * *Intent:* /** @inheritDoc */
  * `makeList` **(Many-Argument Workhorses)** (Impact: 101.1)
    * *Intent:* /** @inheritDoc */
  * `tableNamesWithIndexClauseOrJOIN` **(Many-Argument Workhorses)** (Impact: 42.6)
    * *Intent:* /** * Get the aliased table name clause for a FROM clause * which might have a JOIN and/or USE INDEX...
  * `assertValidUpsertSetArray` **(Many-Argument Workhorses)** (Impact: 26.1)
    * *Intent:* /** * @param array $set Combined column/literal assignment map and SQL assignment list * @param stri...
  * `buildSuperlative` **(Stateful Encapsulated Methods)** (Impact: 25.3)
    * *Intent:* /** * Build a superlative function statement comparing columns/values * * Integer and float values i...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Cascading Flux:* 280 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 64
* *State Mutation (weighted view):* 865
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 366`, `structural_boundaries: 348`, `args: 101`, `func_start: 99`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 35`, `high_risk_execution: 1`, `state_mutation: 305`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 56`
* *Architecture:* `api: 76`, `import: 18`
* *Defense:* `safety: 70`, `doc: 100`, `sync_locks: 5`, `immutability_locks: 7`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.501
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.089333
  * `Imports (Out-Degree: 11):` InvalidArgumentException, Psr\Log\LoggerInterface, Psr\Log\NullLogger, RuntimeException, Throwable, Wikimedia\Assert\Assert, Wikimedia\Rdbms\DBLanguageError, Wikimedia\Rdbms\DatabaseDomain...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `includes/Skin/Skin.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 4.923)
- **Top Global Matches:** file_cluster_4: 4.923, file_cluster_6: 9.912, file_cluster_16: 11.232
- **Magnitude:** 1868.06 | **LOC:** 2584 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 20.0%
- **Blast Radius:** changing it is visible to **77** in-repo importer(s); it depends on **31**; blast radius 1.62; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.0%), Debt Markers (formerly Tech Debt) (72.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (40.4%)
- **Documentation Coverage:** 1.7857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getPersonalToolsForMakeListItem` **(Many-Argument Workhorses)** (Impact: 50.1)
    * *Intent:* /** * Create an array of personal tools items from the data in the quicktemplate * stored by SkinTem...
  * `buildNavUrls` **(I/O & Config Routines)** (Impact: 47.8)
    * *Intent:* /** * Build array of common navigation links. * Assumes thispage property has been set before execut...
  * `makeToolbox` **(Defensive Guards)** (Impact: 30.2)
    * *Intent:* /** * Create an array of common toolbox items from the data in the quicktemplate * stored by SkinTem...
  * `getDefaultModules` **(I/O & Config Routines)** (Impact: 26.9)
    * *Intent:* /** * Defines the ResourceLoader modules that should be added to the skin * It is recommended that s...
  * `createSidebarItem` **(Many-Argument Workhorses)** (Impact: 25.4)
    * *Intent:* /** * Generates an array item for the sidebar * @param string $target Target link in the form of an ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 377 instances
* *Memory Alloc (weighted view):* 6
* *State Mutation (weighted view):* 1221
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 293`, `structural_boundaries: 265`, `args: 70`, `func_start: 68`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 467`, `planned_debt: 3`, `unreferenced_by_name: 35`
* *Architecture:* `api: 46`, `import: 33`
* *Defense:* `safety: 35`, `doc: 80`, `immutability_locks: 17`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.62
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.11681
  * `Imports (Out-Degree: 31):` MediaWiki\Context\ContextSource, MediaWiki\HookContainer\ProtectedHookAccessorTrait, MediaWiki\Html\Html, MediaWiki\Language\Language, MediaWiki\Language\LanguageCode, MediaWiki\MainConfigNames, MediaWiki\MediaWikiServices, MediaWiki\Output\OutputPage...
  * `Imported By (In-Degree: 77):` (Excluded from Brief to save tokens)

### `tests/phpunit/includes/Auth/AuthManagerTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.05)
- **Top Global Matches:** file_cluster_4: 7.05, file_cluster_16: 10.073, file_cluster_11: 10.45
- **Magnitude:** 1859.78 | **LOC:** 4607 | **CtrlFlow:** 4.7% | **Authorship Centralization:** 20.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **82**; blast radius 0.052; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (57.9%), Guard Balance (formerly Safety Score) (53.4%), Complexity Load (formerly Cognitive Load) (27.2%), Connectivity (formerly Api Exposure) (6.2%)
- **Documentation Coverage:** 61.3636% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testAuthentication` **(Many-Argument Workhorses)** (Impact: 96.7)
    * *Intent:* /** * @dataProvider provideAuthentication */
  * `testAccountCreation` **(Many-Argument Workhorses)** (Impact: 95.3)
    * *Intent:* /** * @dataProvider provideAccountCreation */
  * `testAccountLink` **(Many-Argument Workhorses)** (Impact: 54.8)
    * *Intent:* /** * @dataProvider provideAccountLink */
  * `initializeManager` **(Defensive Guards)** (Impact: 40.7)
    * *Intent:* /** * Initialize $this->manager * @param bool $regen Force a call to $this->initializeConfig() */
  * `testGetAuthenticationRequests` **(Many-Argument Workhorses)** (Impact: 38.5)
    * *Intent:* /** * @dataProvider provideGetAuthenticationRequests * @param string $action * @param array $expect ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 196 instances
* *Concurrency (weighted view):* 8
* *Memory Alloc (weighted view):* 78
* *State Mutation (weighted view):* 1085
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 191`, `structural_boundaries: 503`, `args: 160`, `func_start: 70`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 693`, `fragile_debt: 3`, `unreferenced_by_name: 61`
* *Architecture:* `api: 61`, `concurrency: 3`, `import: 82`
* *Defense:* `safety: 99`, `doc: 34`, `test: 389`, `sync_locks: 7`, `immutability_locks: 1`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.052
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 63):` Closure, DomainException, DummySessionProvider, Exception, InvalidArgumentException, LogicException, MediaWikiIntegrationTestCase, MediaWiki\Auth\AbstractPreAuthenticationProvider...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `includes/HookContainer/HookRunner.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.781)
- **Top Global Matches:** file_cluster_15: 7.781, file_cluster_11: 9.237, file_cluster_16: 9.443
- **Magnitude:** 1854.36 | **LOC:** 5264 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 36.8%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **32**; blast radius 0.052; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (72.3%), Guard Balance (formerly Safety Score) (48.8%), Connectivity (formerly Api Exposure) (14.7%)
- **Documentation Coverage:** 0.1852% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `onBeforeParserFetchTemplateRevisionRecord` **(Compute Cores)** (Impact: 7.2)
    * *Intent:* /** @inheritDoc */
  * `onAuthenticationAttemptThrottled` **(Compute Cores)** (Impact: 6.2)
    * *Intent:* /** @inheritDoc */
  * `onUserRequirementsCondition` **(Many-Argument Workhorses)** (Impact: 5.3)
    * *Intent:* /** @inheritDoc */
  * `onOutputPageRenderCategoryLink` **(Many-Argument Workhorses)** (Impact: 5.1)
    * *Intent:* /** @inheritDoc */
  * `onAuthManagerVerifyAuthentication` **(Parameter Forwarders)** (Impact: 5.0)
    * *Intent:* /** @inheritDoc */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 1073`, `args: 540`, `func_start: 540`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 2`, `unreferenced_by_name: 540`
* *Architecture:* `api: 540`, `import: 32`
* *Defense:* `safety: 2`, `doc: 540`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.052
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 31):` MediaWiki\Auth\AuthManager, MediaWiki\Auth\AuthenticationResponse, MediaWiki\Content\ContentHandler, MediaWiki\Content\JsonContent, MediaWiki\Context\IContextSource, MediaWiki\FileRepo\File\File, MediaWiki\Linker\LinkRenderer, MediaWiki\Linker\LinkTarget...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `includes/Auth/AuthManager.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.024)
- **Top Global Matches:** file_cluster_6: 6.024, file_cluster_4: 7.69, file_cluster_16: 15.463
- **Magnitude:** 1812.16 | **LOC:** 3021 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 16.7%
- **Blast Radius:** changing it is visible to **56** in-repo importer(s); it depends on **51**; blast radius 0.712; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (63.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (61.9%), Complexity Load (formerly Cognitive Load) (49.5%)
- **Documentation Coverage:** 10.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `autoCreateUser` **(Many-Argument Workhorses)** (Impact: 128.2)
    * *Intent:* * - the ID of a PrimaryAuthenticationProvider, * - one of the self::AUTOCREATE_SOURCE_* constants * ...
  * `continueAuthentication` **(Many-Argument Workhorses)** (Impact: 117.2)
    * *Intent:* * new AuthenticationRequests should be made (if any), then * AuthManager::continueAuthentication() s...
  * `continueAccountCreation` **(Many-Argument Workhorses)** (Impact: 113.9)
    * *Intent:* /** * Continue an account creation flow * @param AuthenticationRequest[] $reqs * @return Authenticat...
  * `getAuthenticationRequestsInternal` **(Many-Argument Workhorses)** (Impact: 47.9)
    * *Intent:* /** * Internal request lookup for self::getAuthenticationRequests * * @param string $providerAction ...
  * `getAuthenticationRequests` **(Compute Cores)** (Impact: 44.6)
    * *Intent:* * - ACTION_LOGIN: Valid for passing to beginAuthentication * - ACTION_LOGIN_CONTINUE: Valid for pass...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 270 instances
* *State Mutation (weighted view):* 872
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 375`, `structural_boundaries: 328`, `args: 57`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 332`, `fragile_debt: 3`, `unreferenced_by_name: 13`
* *Architecture:* `api: 52`, `import: 51`
* *Defense:* `safety: 64`, `doc: 91`, `sync_locks: 6`, `immutability_locks: 45`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.712
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.126336
  * `Imports (Out-Degree: 48):` InvalidArgumentException, LogicException, MediaWiki\Auth\Hook\AuthManagerVerifyAuthenticationHook, MediaWiki\Block\AbstractBlock, MediaWiki\Block\BlockManager, MediaWiki\ChangeTags\ChangeTagsStore, MediaWiki\Config\Config, MediaWiki\Context\RequestContext...
  * `Imported By (In-Degree: 56):` (Excluded from Brief to save tokens)

### `includes/FileRepo/File/LocalFile.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.525)
- **Top Global Matches:** file_cluster_4: 7.525, file_cluster_6: 10.994, file_cluster_12: 11.395
- **Magnitude:** 1794.52 | **LOC:** 2809 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 28.6%
- **Blast Radius:** changing it is visible to **23** in-repo importer(s); it depends on **45**; blast radius 0.262; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (74.0%), Complexity Load (formerly Cognitive Load) (42.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (40.6%)
- **Documentation Coverage:** 1.0309% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `upgradeRow` **(I/O & Config Routines)** (Impact: 238.7)
    * *Intent:* /** * Fix assorted version-related problems with the image row by reloading it from the file * @stab...
  * `recordUpload3` **(Many-Argument Workhorses)** (Impact: 128.6)
    * *Intent:* * @since 1.35 * @stable to override * @param string $oldver * @param string $comment * @param string...
  * `upload` **(Many-Argument Workhorses)** (Impact: 67.1)
    * *Intent:* * @param array|false $props File properties, if known. This can be used to * reduce the upload time ...
  * `publishTo` **(Many-Argument Workhorses)** (Impact: 33.9)
    * *Intent:* * object with the archive name in the "value" member on success. * * The archive name should be pass...
  * `getHistory` **(Many-Argument Workhorses)** (Impact: 25.1)
    * *Intent:* /** purgeDescription inherited */ /** purgeEverything inherited */ /** * @stable to override * @para...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 249 instances
* *Memory Alloc (weighted view):* 25
* *State Mutation (weighted view):* 912
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 213`, `structural_boundaries: 309`, `args: 82`, `func_start: 74`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 58`, `state_mutation: 414`, `planned_debt: 4`, `unreferenced_by_name: 19`
* *Architecture:* `api: 56`, `import: 46`
* *Defense:* `safety: 35`, `doc: 158`, `sync_locks: 3`, `immutability_locks: 10`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.262
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.098509
  * `Imports (Out-Degree: 45):` InvalidArgumentException, MediaWiki\Content\ContentHandler, MediaWiki\Context\RequestContext, MediaWiki\Deferred\AutoCommitUpdate, MediaWiki\Deferred\DeferredUpdates, MediaWiki\Deferred\LinksUpdate\LinksUpdate, MediaWiki\Deferred\SiteStatsUpdate, MediaWiki\FileRepo\FileBackendDBRepoWrapper...
  * `Imported By (In-Degree: 23):` (Excluded from Brief to save tokens)

### `includes/Parser/CoreParserFunctions.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.407)
- **Top Global Matches:** file_cluster_12: 6.407, file_cluster_15: 7.064, file_cluster_4: 7.892
- **Magnitude:** 1723.56 | **LOC:** 2116 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **21**; blast radius 0.081; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (55.6%), Complexity Load (formerly Cognitive Load) (34.5%)
- **Documentation Coverage:** 1.7341% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `displaytitle` **(Many-Argument Workhorses)** (Impact: 38.4)
    * *Intent:* /** * Override the title of the page when viewed, provided we've been given a * title which will nor...
  * `revisionid` **(Compute Cores)** (Impact: 31.8)
    * *Intent:* /** * Get the id from the last revision of a specified page. * @param Parser $parser * @param string...
  * `getCachedRevisionObject` **(Many-Argument Workhorses)** (Impact: 31.1)
    * *Intent:* /** * Fetched the current revision of the given title and return this. * Will increment the expensiv...
  * `tagObj` **(Many-Argument Workhorses)** (Impact: 29.1)
    * *Intent:* /** * Parser function to extension tag adaptor * @param Parser $parser * @param PPFrame $frame * @pa...
  * `filepath` **(Many-Argument Workhorses)** (Impact: 24.1)
    * *Intent:* /** * Usage {{filepath|300}}, {{filepath|nowiki}}, {{filepath|nowiki|300}} * or {{filepath|300|nowik...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 272 instances
* *State Mutation (weighted view):* 896
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 247`, `structural_boundaries: 321`, `args: 95`, `func_start: 91`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 352`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 2`, `unreferenced_by_name: 1`
* *Architecture:* `api: 86`, `import: 21`
* *Defense:* `safety: 20`, `doc: 94`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.081
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.095935
  * `Imports (Out-Degree: 17):` InvalidArgumentException, MediaWiki\Category\Category, MediaWiki\Config\ServiceOptions, MediaWiki\Content\ContentHandler, MediaWiki\Language\Language, MediaWiki\Language\LanguageCode, MediaWiki\Language\LanguageNameUtils, MediaWiki\Linker\Linker...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `includes/User/User.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.396)
- **Top Global Matches:** file_cluster_15: 6.396, file_cluster_12: 7.1, file_cluster_16: 7.459
- **Magnitude:** 1711.92 | **LOC:** 3429 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 18.8%
- **Blast Radius:** changing it is visible to **407** in-repo importer(s); it depends on **59**; blast radius 7.048; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (98.3%), Guard Balance (formerly Safety Score) (71.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (62.3%)
- **Documentation Coverage:** 1.9011% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadFromRow` **(Many-Argument Workhorses)** (Impact: 53.7)
    * *Intent:* /** * Initialize this object from a row from the user table. * * @param stdClass $row Row from the u...
  * `load` **(Compute Cores)** (Impact: 46.0)
    * *Intent:* /** * Load the user table data for this object from the source given by mFrom. * * @param int $flags...
  * `newSystemUser` **(Many-Argument Workhorses)** (Impact: 23.3)
    * *Intent:* * - validate: Type of validation to use: * - false No validation * - 'valid' Valid for batch process...
  * `setEmailWithConfirmation` **(Compute Cores)** (Impact: 20.9)
    * *Intent:* /** * Set the user's e-mail address and send a confirmation mail if needed. * * @since 1.20 * @param...
  * `clearInstanceCache` **(Compute Cores)** (Impact: 19.1)
    * *Intent:* /** * Clear various cached data stored in this object. The cache of the user table * data (i.e. self...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 254 instances
* *Memory Alloc (weighted view):* 19
* *State Mutation (weighted view):* 855
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 286`, `structural_boundaries: 418`, `args: 145`, `func_start: 137`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 347`, `planned_debt: 4`, `fragile_debt: 3`, `unreferenced_by_name: 70`
* *Architecture:* `api: 137`, `import: 59`
* *Defense:* `safety: 26`, `doc: 169`, `immutability_locks: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.048
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.133321
  * `Imports (Out-Degree: 45):` AllowDynamicProperties, ArrayIterator, BadMethodCallException, DebugInfoTrait, InvalidArgumentException, MWCryptHash, MediaWiki\Auth\AuthManager, MediaWiki\Auth\AuthenticationRequest...
  * `Imported By (In-Degree: 407):` (Excluded from Brief to save tokens)

### `includes/Page/WikiPage.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.737)
- **Top Global Matches:** file_cluster_12: 6.737, file_cluster_15: 8.028, file_cluster_16: 8.382
- **Magnitude:** 1680.16 | **LOC:** 2985 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **103** in-repo importer(s); it depends on **63**; blast radius 1.99; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (50.6%)
- **Documentation Coverage:** 1.0929% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `doUpdateRestrictions` **(Many-Argument Workhorses)** (Impact: 124.3)
    * *Intent:* /** * Update the article's restriction field, and leave a log entry. * This works for protection bot...
  * `doUserEditContent` **(Many-Argument Workhorses)** (Impact: 34.6)
    * *Intent:* * edit-already-exists: In creation mode, but the article already exists. * * Extensions may define a...
  * `getDerivedDataUpdater` **(Many-Argument Workhorses)** (Impact: 28.9)
    * *Intent:* * * @since 1.32 * * @param UserIdentity|null $forUser The user that will be used for, or was used fo...
  * `replaceSectionAtRev` **(Many-Argument Workhorses)** (Impact: 21.9)
    * *Intent:* /** * @param string|int|null|false $sectionId Section identifier as a number or string * (e.g. 0, 1 ...
  * `updateRevisionOn` **(Many-Argument Workhorses)** (Impact: 21.4)
    * *Intent:* * @internal Low level interface, not safe for use in extensions! * * @todo Factor out into a PageSto...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 252 instances
* *State Mutation (weighted view):* 853
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 254`, `structural_boundaries: 321`, `args: 104`, `func_start: 97`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 349`, `planned_debt: 28`, `fragile_debt: 3`
* *Architecture:* `api: 85`, `import: 63`
* *Defense:* `safety: 10`, `doc: 112`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.99
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.128977
  * `Imports (Out-Degree: 53):` BadMethodCallException, InvalidArgumentException, MediaWiki\Actions\InfoAction, MediaWiki\Category\Category, MediaWiki\CommentStore\CommentStoreComment, MediaWiki\Content\Content, MediaWiki\Content\ContentHandler, MediaWiki\Context\IContextSource...
  * `Imported By (In-Degree: 103):` (Excluded from Brief to save tokens)

### `includes/Preferences/DefaultPreferencesFactory.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.969)
- **Top Global Matches:** file_cluster_6: 6.969, file_cluster_4: 7.26, file_cluster_9: 14.15
- **Magnitude:** 1644.98 | **LOC:** 2302 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 27.3%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **56**; blast radius 0.061; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (71.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (60.0%), Complexity Load (formerly Cognitive Load) (46.1%)
- **Documentation Coverage:** 4.878% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `profilePreferences` **(Many-Argument Workhorses)** (Impact: 128.1)
    * *Intent:* /** * @todo Inject user Language instead of using context. * @param User $user * @param IContextSour...
  * `getResetKinds` **(Defensive Guards)** (Impact: 65.8)
    * *Intent:* /** * @param User $user * @param IContextSource $context * @param array|null $options * @return stri...
  * `__construct` **(Many-Argument Workhorses)** (Impact: 50.6)
    * *Intent:* * @param AuthManager $authManager * @param LinkRenderer $linkRenderer * @param NamespaceInfo $nsInfo...
  * `getOptionFromUser` **(Defensive Guards)** (Impact: 50.1)
    * *Intent:* /** * Pull option from a user account. Handles stuff like array-type preferences. * * @deprecated si...
  * `watchlistPreferences` **(Many-Argument Workhorses)** (Impact: 36.7)
    * *Intent:* /** * @param User $user * @param IContextSource $context * @param array &$defaultPreferences */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 261 instances
* *Memory Alloc (weighted view):* 23
* *State Mutation (weighted view):* 897
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 270`, `structural_boundaries: 233`, `args: 40`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 375`, `planned_debt: 3`, `fragile_debt: 3`, `unreferenced_by_name: 3`
* *Architecture:* `api: 10`, `import: 56`
* *Defense:* `safety: 55`, `doc: 50`, `immutability_locks: 1`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.061
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.000444
  * `Imports (Out-Degree: 45):` LoggerAwareTrait, MediaWiki\Actions\WatchAction, MediaWiki\Auth\AuthManager, MediaWiki\Auth\PasswordAuthenticationRequest, MediaWiki\Config\ServiceOptions, MediaWiki\Context\IContextSource, MediaWiki\HTMLForm\Field\HTMLCheckMatrix, MediaWiki\HTMLForm\Field\HTMLInfoField...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `includes/libs/FileBackend/SwiftFileBackend.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.979)
- **Top Global Matches:** file_cluster_4: 5.979, file_cluster_16: 9.042, file_cluster_12: 9.258
- **Magnitude:** 1610.78 | **LOC:** 2042 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **17**; blast radius 0.183; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (74.9%), Debt Markers (formerly Tech Debt) (70.9%), Complexity Load (formerly Cognitive Load) (36.0%)
- **Documentation Coverage:** 2.9412% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getDirListPageInternal` **(Many-Argument Workhorses)** (Impact: 54.9)
    * *Intent:* /** * Do not call this function outside of SwiftFileBackendFileList * * @param string $fullCont Reso...
  * `getFileListPageInternal` **(Many-Argument Workhorses)** (Impact: 34.1)
    * *Intent:* /** * Do not call this function outside of SwiftFileBackendFileList * * @param string $fullCont Reso...
  * `requestMultiWithAuth` **(Stateful Encapsulated Methods)** (Impact: 31.4)
    * *Intent:* /** * Perform a batch of authenticated HTTP requests * * @param array $reqs An array of request data...
  * `objectListing` **(Many-Argument Workhorses)** (Impact: 31.2)
    * *Intent:* /** * Get a list of objects under a container. * Either just the names or a list of stdClass objects...
  * `__construct` **(Defensive Guards)** (Impact: 26.3)
    * *Intent:* * - rgwS3SecretKey : Rados Gateway S3 "secret key" value on the account. * Do not set this until it ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 283 instances
* *State Mutation (weighted view):* 876
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 317`, `structural_boundaries: 225`, `args: 63`, `func_start: 56`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 310`, `fragile_debt: 1`, `unreferenced_by_name: 29`
* *Architecture:* `io: 8`, `api: 12`, `import: 17`
* *Defense:* `safety: 76`, `doc: 87`, `immutability_locks: 2`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.183
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.000426
  * `Imports (Out-Degree: 13):` Exception, Psr\Log\LoggerInterface, Shellbox\Command\BoxedCommand, StatusValue, Wikimedia\FileBackend\FSFile\TempFSFile, Wikimedia\FileBackend\FileIteration\SwiftFileBackendDirList, Wikimedia\FileBackend\FileIteration\SwiftFileBackendFileList, Wikimedia\FileBackend\FileOpHandle\SwiftFileOpHandle...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `includes/libs/ObjectCache/WANObjectCache.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.445)
- **Top Global Matches:** file_cluster_4: 5.445, file_cluster_16: 8.579, file_cluster_15: 9.086
- **Magnitude:** 1582.28 | **LOC:** 3089 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **76** in-repo importer(s); it depends on **14**; blast radius 1.219; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (76.9%), Debt Markers (formerly Tech Debt) (42.1%), Complexity Load (formerly Cognitive Load) (34.8%)
- **Documentation Coverage:** 2.5974% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fetchOrRegenerate` **(Many-Argument Workhorses)** (Impact: 131.1)
    * *Intent:* * * @see WANObjectCache::getWithSetCallback() * * @param string $key Cache key made with makeKey()/m...
  * `setMainValue` **(Many-Argument Workhorses)** (Impact: 119.3)
    * *Intent:* * @param string $key Cache key made with makeKey()/makeGlobalKey() * @param mixed $value * @param in...
  * `fetchKeys` **(Many-Argument Workhorses)** (Impact: 55.0)
    * *Intent:* * Fetch the value and key metadata of several keys from cache * * $checkKeys holds the "check" keys ...
  * `getMultiWithUnionSetCallback` **(Many-Argument Workhorses)** (Impact: 33.8)
    * *Intent:* * return $rows; * }, * ] * ); * $files = array_map( self::newFromRow( ... ), $rows ); * @endcode * *...
  * `getWithSetCallback` **(Many-Argument Workhorses)** (Impact: 29.2)
    * *Intent:* * most sense for values that are moderately to highly expensive to regenerate and easy * to query fo...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 259 instances
* *State Mutation (weighted view):* 826
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 234`, `structural_boundaries: 181`, `args: 56`, `func_start: 51`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 308`, `planned_debt: 1`, `unreferenced_by_name: 16`
* *Architecture:* `api: 39`, `import: 14`
* *Defense:* `safety: 56`, `doc: 138`, `immutability_locks: 68`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.219
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.131308
  * `Imports (Out-Degree: 7):` ArrayIterator, Closure, Exception, Psr\Log\LoggerAwareInterface, Psr\Log\LoggerInterface, Psr\Log\NullLogger, RuntimeException, UnexpectedValueException...
  * `Imported By (In-Degree: 76):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `includes/Search/StringPrefixSearch.php` (PHP) | Magnitude: 3.58 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 10, indent_tabs: 8, doc: 5, args: 3
- `resources/src/jquery.spinner/spinner.less` (CSS) | Magnitude: 3.66 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 108, closures: 15, thread_sleeps: 12, class_start: 9
- `tests/phpunit/integration/includes/Html/TemplateParserIntegrationTest.php` (PHP) | Magnitude: 88.82 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 264, structural_boundaries: 46, state_mutation: 36, test: 35
- `resources/src/mediawiki.hlist/default.less` (CSS) | Magnitude: 15.86 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 41, closures: 6, class_start: 1, ownership: 1
- `resources/src/mediawiki.rcfilters/utils.js` (JAVASCRIPT) | Magnitude: 37.54 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 25, branch: 7, structural_boundaries: 5, state_mutation: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `includes/User/BotPassword.php` (PHP) | Magnitude: 264.62 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 237, structural_boundaries: 84, state_mutation: 53, branch: 35
- `tests/phpunit/includes/Permissions/PermissionManagerTest.php` (PHP) | Magnitude: 567.86 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 1475, structural_boundaries: 234, state_mutation: 176, test: 70
- `tests/phpunit/includes/Media/ThumbnailImageTest.php` (PHP) | Magnitude: 67.1 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 64, state_mutation: 27, structural_boundaries: 16, test: 7
- `maintenance/migrateRevisionCommentTemp.php` (PHP) | Magnitude: 52.4 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 68, structural_boundaries: 13, state_mutation: 12, branch: 7
- `includes/Revision/RevisionStoreCacheRecord.php` (PHP) | Magnitude: 36.92 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 38, structural_boundaries: 14, state_mutation: 7, doc: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `resources/src/mediawiki.rcfilters/styles/mw.rcfilters.ui.FilterWrapperWidget.less` (CSS) | Magnitude: 10.6 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 84, class_start: 16, branch: 4, func_start: 3
- `resources/src/mediawiki.router/router.js` (JAVASCRIPT) | Magnitude: 92.1 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 115, branch: 21, args: 16, doc: 15
- `includes/Revision/RevisionArchiveRecord.php` (PHP) | Magnitude: 119.86 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 85, structural_boundaries: 39, state_mutation: 19, branch: 16
- `includes/libs/FileBackend/FileBackendStore.php` (PHP) | Magnitude: 1238.12 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 1083, structural_boundaries: 272, branch: 238, state_mutation: 231
- `includes/JobQueue/JobQueueGroup.php` (PHP) | Magnitude: 290.52 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 230, state_mutation: 64, branch: 53, structural_boundaries: 51

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `resources/src/mediawiki.special.block/components/BlockDetailsField.vue` (HTML) | Magnitude: 5.7 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 45, class_start: 7, decorators: 7, ssr_boundaries: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `resources/src/mediawiki.page.ready/teleportTarget.less` (CSS) | Magnitude: 12.6 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 2, class_start: 1, safety_bypasses: 1, ui_framework: 1
- `tests/phpunit/includes/Collation/IcuCollationTest.php` (PHP) | Magnitude: 9.0 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 16, structural_boundaries: 7, safety_bypasses: 4, state_mutation: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `tests/phpunit/integration/includes/Rest/Handler/CreationHandlerTest.php` (PHP) | Magnitude: 126.74 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 454, structural_boundaries: 99, memory_alloc: 37, state_mutation: 33
- `includes/FileRepo/FileBackendDBRepoWrapper.php` (PHP) | Magnitude: 254.94 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 227, structural_boundaries: 90, state_mutation: 45, doc: 43
- `tests/phpunit/includes/Auth/TemporaryPasswordPrimaryAuthenticationProviderTest.php` (PHP) | Magnitude: 576.1 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 770, state_mutation: 189, structural_boundaries: 169, args: 54
- `includes/OutputTransform/OutputTransformPipeline.php` (PHP) | Magnitude: 39.56 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 26, structural_boundaries: 11, state_mutation: 8, branch: 6
- `includes/RecentChanges/ChangesListQuery/TitleConditionValue.php` (PHP) | Magnitude: 37.4 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 29, structural_boundaries: 15, api: 6, state_mutation: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `tests/phpunit/MediaWikiLoggerPHPUnitExtension.php` (PHP) | Magnitude: 70.0 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 79, structural_boundaries: 29, doc: 14, scientific: 14
- `includes/Utils/GitInfo.php` (PHP) | Magnitude: 295.58 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 260, state_mutation: 68, branch: 56, structural_boundaries: 51
- `includes/Installer/Task/Task.php` (PHP) | Magnitude: 81.58 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 113, structural_boundaries: 68, doc: 25, args: 24
- `includes/libs/LockManager/NullLockManager.php` (PHP) | Magnitude: 33.44 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 26, structural_boundaries: 10, branch: 8, doc: 5
- `tests/phpunit/maintenance/UpdateArticleCountTest.php` (PHP) | Magnitude: 35.0 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 52, structural_boundaries: 21, state_mutation: 6, args: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `includes/Api/Hook/ApiCheckCanExecuteHook.php` (PHP) | Magnitude: 19.82 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 7, import: 4, doc: 2, args: 1
- `includes/Api/Hook/ApiQueryCheckCanExecuteHook.php` (PHP) | Magnitude: 19.82 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 7, import: 4, doc: 2, args: 1
- `includes/Revision/RevisionLookup.php` (PHP) | Magnitude: 177.97 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 16, structural_boundaries: 15, state_mutation: 12, doc: 11
- `tests/phpunit/unit/includes/Settings/Source/ExampleDefinitionsClass.php` (PHP) | Magnitude: 19.44 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 18, structural_boundaries: 5, api: 4, immutability_locks: 4
- `includes/Content/Transform/PreSaveTransformParams.php` (PHP) | Magnitude: 28.2 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 8, args: 3, func_start: 3, api: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `tests/phpunit/includes/Config/TestAllServiceOptionsUsed.php` (PHP) | Magnitude: 8.48 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 21, structural_boundaries: 4, state_mutation: 3, doc: 3
- `tests/phpunit/maintenance/PatchSqlTest.php` (PHP) | Magnitude: 6.32 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 16, structural_boundaries: 7, args: 2, func_start: 2
- `includes/RecentChanges/Hook/FetchChangesListHook.php` (PHP) | Magnitude: 20.34 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 7, import: 4, doc: 3, args: 1
- `includes/Logging/LogEntry.php` (PHP) | Magnitude: 58.46 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 17, doc: 15, args: 12, func_start: 12
- `resources/src/mediawiki.special.block/components/BlockTypeField.vue` (HTML) | Magnitude: 8.36 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 71, args: 11, class_start: 11, decorators: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `includes/Settings/Config/ConfigSchemaAggregator.php` (PHP) | Magnitude: 256.78 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 242, structural_boundaries: 69, branch: 51, state_mutation: 43
- `includes/Page/UndeletePage.php` (PHP) | Magnitude: 364.36 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 433, state_mutation: 104, structural_boundaries: 85, branch: 50
- `maintenance/categoryChangesAsRdf.php` (PHP) | Magnitude: 306.16 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 369, structural_boundaries: 74, state_mutation: 65, branch: 46
- `resources/src/startup/mediawiki.loader.js` (JAVASCRIPT) | Magnitude: 1002.64 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 934, branch: 219, state_mutation: 172, core_var_decl: 160
- `includes/Request/PathRouter.php` (PHP) | Magnitude: 244.42 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 240, state_mutation: 59, structural_boundaries: 53, branch: 43

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `maintenance/storage/moveToExternal.php` (PHP) | Magnitude: 268.86 | Delta: **0.133** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 245, state_mutation: 66, branch: 52, structural_boundaries: 35

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `tests/Common/Parser/ParserTestPrinter.php` (PHP) | Magnitude: 99.08 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 214, structural_boundaries: 42, state_mutation: 42, doc: 25
- `maintenance/checkImages.php` (PHP) | Magnitude: 56.6 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 46, state_mutation: 13, branch: 12, structural_boundaries: 10
- `tests/phpunit/maintenance/GrepPagesTest.php` (PHP) | Magnitude: 27.62 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 70, structural_boundaries: 20, args: 7, func_start: 7
- `tests/qunit/resources/mediawiki.pager.codex/limitSelectors.test.js` (JAVASCRIPT) | Magnitude: 15.18 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 47, structural_boundaries: 12, core_var_decl: 12, design_camel_case: 11
- `includes/Permissions/PermissionManager.php` (PHP) | Magnitude: 403.52 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 1341, structural_boundaries: 217, state_mutation: 170, safety_bypasses: 124

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `maintenance/CheckSignatures.php` (PHP) | Magnitude: 64.44 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 44, state_mutation: 19, structural_boundaries: 10, branch: 8
- `maintenance/formatInstallDoc.php` (PHP) | Magnitude: 50.2 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 40, state_mutation: 14, structural_boundaries: 10, branch: 7
- `maintenance/lag.php` (PHP) | Magnitude: 44.34 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 45, state_mutation: 10, branch: 9, structural_boundaries: 9
- `maintenance/makeTestEdits.php` (PHP) | Magnitude: 61.96 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 48, structural_boundaries: 17, state_mutation: 17, branch: 7
- `maintenance/migrateUserGroup.php` (PHP) | Magnitude: 56.44 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 94, state_mutation: 22, structural_boundaries: 10, branch: 7

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `includes/Parser/Parser.php` -> Churn: **80.43%** | Cog Load: 52.286% | Debt: 46.243%
- `includes/Page/Article.php` -> Churn: **76.71%** | Cog Load: 55.9373% | Debt: 32.2027%
- `includes/HookContainer/HookRunner.php` -> Churn: **72.31%** | Cog Load: 2.4303% | Debt: 99.9971%
- `includes/MediaWikiServices.php` -> Churn: **72.31%** | Cog Load: 4.8198% | Debt: 100.0%
- `includes/Skin/SkinTemplate.php` -> Churn: **65.36%** | Cog Load: 53.2444% | Debt: 16.5122%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `includes/HTMLForm/HTMLFormField.php` -> **Bartosz Dziewoński** (100.0% isolated ownership) | Magnitude: 997.62
- `includes/Language/LanguageConverter.php` -> **C. Scott Ananian** (100.0% isolated ownership) | Magnitude: 986.3
- `includes/libs/ObjectCache/Utils/MemcachedClient.php` -> **Ori Livneh** (100.0% isolated ownership) | Magnitude: 985.82
- `includes/Parser/Preprocessor_Hash.php` -> **Func** (100.0% isolated ownership) | Magnitude: 865.52
- `includes/libs/Rdbms/Database/DatabasePostgres.php` -> **Daimona Eaytoy** (100.0% isolated ownership) | Magnitude: 827.42

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `includes/GlobalFunctions.php` -> **Severity: 15.513** (Embedded: 0.1872 * Error Risk: 82.8718%)
- `includes/Language/Language.php` -> **Severity: 11.885** (Embedded: 0.147 * Error Risk: 80.8517%)
- `includes/Title/Title.php` -> **Severity: 11.783** (Embedded: 0.1581 * Error Risk: 74.539%)
- `includes/Request/WebRequest.php` -> **Severity: 10.772** (Embedded: 0.1424 * Error Risk: 75.6625%)
- `includes/Language/Message/Message.php` -> **Severity: 10.622** (Embedded: 0.1509 * Error Risk: 70.3713%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `includes/libs/Message/ScalarParam.php` -> **Severity: 106.967** (Blast Radius: 3.209 * Doc Risk: 33.3333%)
- `includes/Title/TitleValue.php` -> **Severity: 75.583** (Blast Radius: 1.814 * Doc Risk: 41.6667%)
- `includes/Context/RequestContext.php` -> **Severity: 74.066** (Blast Radius: 4.33 * Doc Risk: 17.1053%)
- `includes/Language/RawMessage.php` -> **Severity: 55.3** (Blast Radius: 1.659 * Doc Risk: 33.3333%)
- `includes/libs/Message/ListParam.php` -> **Severity: 50.025** (Blast Radius: 2.001 * Doc Risk: 25.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 1180 literal sites + 2 sites through wrappers = 1182
- **`panics_and_aborts`:** 3254 literal sites + 20 sites through wrappers = 3274

- `encoderError` (function, panics_and_aborts, primitive): 11 call sites in 1 files -- `resources/lib/sinonjs/sinon.js`
- `chdir` (function, panics_and_aborts, primitive): 3 call sites in 2 files -- `resources/lib/sinonjs/sinon.js`
- `throwLoggedError` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `resources/lib/sinonjs/sinon.js`
- `__construct` (function, debug_prints, primitive): 1 call sites in 1 files -- `maintenance/dumpIterator.php`
- `_nonIterableRest` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `resources/lib/qunitjs/qunit.js`
- `_nonIterableSpread` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `resources/lib/qunitjs/qunit.js`
- `_nonIterableSpread` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `resources/lib/sinonjs/sinon.js`
- `abortTestsButton` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `resources/lib/qunitjs/qunit.js`
- `outputCss` (function, debug_prints, primitive): 1 call sites in 1 files -- `includes/Installer/WebInstaller.php`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 181535 call pairs -- scoped 39.4%, unique 1.6%, ambiguous 30.8%, external 28.2%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| php | 171098 | 40.9% | 1.7% | 32.5% | 24.8% |
| javascript | 9922 | 14.4% | 0.0% | 2.5% | 83.1% |
| html | 360 | 9.4% | 0.0% | 0.0% | 90.6% |
| python | 135 | 18.5% | 0.0% | 0.0% | 81.5% |
| shell | 18 | 22.2% | 0.0% | 0.0% | 77.8% |
| postgresql | 2 | 100.0% | 0.0% | 0.0% | 0.0% |

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
