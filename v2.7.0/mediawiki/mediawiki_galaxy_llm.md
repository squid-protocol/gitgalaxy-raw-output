# ARCHITECTURAL_BRIEF: mediawiki
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/wikimedia/mediawiki.git` |
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
| Total Artifacts | 12231 |
| Analyzed Artifacts (Scanned) | 11083 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1148 |
| Total LOC | 1215783 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 90.6% |
| Dominant Lang | PHP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1306 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 7.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 464 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PHP | 5403 | 700028 | 48.8% |
| JSON | 3148 | 371716 | 28.4% |
| XML | 1243 | 0 | 11.2% |
| JAVASCRIPT | 686 | 111646 | 6.2% |
| CSS | 284 | 19723 | 2.6% |
| SQLITE | 149 | 8385 | 1.3% |
| PLAINTEXT | 67 | 4 | 0.6% |
| MARKDOWN | 56 | 0 | 0.5% |
| HTML | 37 | 3423 | 0.3% |
| SHELL | 5 | 68 | 0.0% |
| YAML | 3 | 430 | 0.0% |
| MAKEFILE | 2 | 360 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 10802 | 97.5% |
| Unknown | 4 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Minified & Vendor Opaque Mass | 158 | 1.4% |
| Static: Literature & Documentation | 119 | 1.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1148*

**Composition by Extension & Reason:**
- `.json`: 30x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Static Asset Blob without Intent: 1121 LOC), 2x Excluded (Static Asset Blob without Intent: 1973 LOC)
- `.js`: 149x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 14x Excluded (Saturation: Line 1 exceeds 500 chars), 2x Excluded (Saturation: Line 6 exceeds 500 chars)
- `.css`: 108x Excluded (Saturation: Line 1 exceeds 500 chars), 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 491 LOC)
- `.png`: 80x Excluded (Explicitly Denied Extension: '.png')
- `.php`: 36x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Machine-Generated Source Code Signature: 45 LOC), 2x Excluded (Machine-Generated Source Code Signature: 42 LOC)
- `no_extension`: 48x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable), 2x Excluded (Unsupported Extension: '.data-parsoid')
- `.cjs`: 42x Excluded (Saturation: Line 1 exceeds 500 chars), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jpg`: 32x Excluded (Explicitly Denied Extension: '.jpg')
- `.md`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 45 LOC), 1x Excluded (Machine-Generated Source Code Signature: 56 LOC)
- `.mustache`: 22x Excluded (Unsupported Extension: '.mustache')
- `.manual`: 16x Excluded (Unsupported Extension: '.manual')
- `.txt`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Binary Format Detected), 1x Excluded (Lexical Monotony: High structural repetition detected in 4348 LOC)
- `.xsd`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.zip`: 12x Excluded (Explicitly Denied Extension: '.zip')
- `.serialized`: 11x Excluded (Unsupported Extension: '.serialized')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 9.5 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 33.7 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 19.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 3.8 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 89.5 | 3.4 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 3.8 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 25.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.4 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 52.3 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.8 | 0.4 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 5.6 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 13.2 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 93.2 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 19394 | 2799 | 4 | `includes/ServiceWiring.php` |
| cleanup | 1098 | 498 | 0 | `resources/lib/ooui/oojs-ui-core.js` |
| guards | 47247 | 3823 | 11 | `resources/lib/vue-test-utils/vue-test-utils.browser.js` |
| danger | 9572 | 1727 | 2 | `includes/Language/Language.php` |
| concurrency | 6347 | 702 | 0 | `tests/phpunit/unit/includes/libs/Leximorph/Handler/GrammarTest.php` |
| connectivity | 34470 | 5050 | 8 | `includes/MainConfigSchema.php` |
| io | 2575 | 480 | 0 | `tests/phan/TaintCheckAnnotationsTest.php` |
| crypto | 0 | 0 | 0 | - |
| ipc | 129 | 76 | 0 | `tests/phan/TaintCheckAnnotationsTest.php` |
| time | 826 | 262 | 0 | `tests/phpunit/includes/Language/LanguageIntegrationTest.php` |
| serialization | 731 | 334 | 0 | `includes/JobQueue/JobQueueRedis.php` |
| regex | 2551 | 641 | 0 | `resources/lib/vue-test-utils/vue-test-utils.browser.js` |
| events | 1827 | 265 | 0 | `resources/lib/qunitjs/qunit.js` |
| tests | 20112 | 1406 | 2 | `tests/phpunit/includes/Auth/AuthManagerTest.php` |
| docs | 47404 | 5693 | 11 | `includes/MainConfigSchema.php` |
| debt | 4935 | 1806 | 1 | `tests/phan/TaintCheckAnnotationsTest.php` |
| mutation | 153163 | 5254 | 31 | `resources/lib/vue-test-utils/vue-test-utils.browser.js` |
| dead_code | 26073 | 3947 | 7 | `includes/MediaWikiServices.php` |
| credential | 105 | 51 | 0 | `tests/phpunit/includes/ExternalLinks/LinkFilterTest.php` |
| threat | 3797 | 429 | 0 | `resources/lib/ooui/oojs-ui-core.js` |
| ml_ai | 588 | 199 | 0 | `includes/Api/ApiUpload.php` |
| ui | 1457 | 285 | 0 | `resources/lib/vue-compiler-dom/compiler-dom.global.js` |

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

1. **MediaWikiServices.php** (`includes/MediaWikiServices.php`) — 481 inbound connections
2. **UserIdentity.php** (`includes/User/UserIdentity.php`) — 296 inbound connections
3. **MediaWikiIntegrationTestCase.php** (`tests/phpunit/MediaWikiIntegrationTestCase.php`) — 273 inbound connections
4. **Status.php** (`includes/Status/Status.php`) — 243 inbound connections
5. **ServiceOptions.php** (`includes/Config/ServiceOptions.php`) — 241 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **MessagesSr_ec.php** (`languages/messages/MessagesSr_ec.php`) — 1213 outbound dependencies
2. **MessagesSr_el.php** (`languages/messages/MessagesSr_el.php`) — 1175 outbound dependencies
3. **MessagesFr.php** (`languages/messages/MessagesFr.php`) — 927 outbound dependencies
4. **MessagesUk.php** (`languages/messages/MessagesUk.php`) — 897 outbound dependencies
5. **MessagesArz.php** (`languages/messages/MessagesArz.php`) — 891 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `sprintfDate` (@ `includes/Language/Language.php`) -> Impact: **1229.0** | LOC: 1862
  * *Intent:* * $ts is UTC if $zone is not given. * * @param string $format * @param string $ts 14-character timestamp * YYYYMMDDHHMMSS * 01234567890123 * @param Da...
- `getPermissionStatus` (@ `includes/Permissions/PermissionManager.php`) -> Impact: **953.2** | LOC: 1428
  * *Intent:* * interface methods instead. * * @param string $action Action that permission needs to be checked for * @param User $user User to check * @param LinkT...
- `internalParse` (@ `includes/Parser/Parser.php`) -> Impact: **951.4** | LOC: 1868
  * *Intent:* /** * Helper function for parse() that transforms wiki markup into half-parsed * HTML. Only called for $mOutputType == self::OT_HTML. * * @internal * ...
- `requireBeautifier$1` (@ `resources/lib/vue-test-utils/vue-test-utils.browser.js`) -> Impact: **781.1** | LOC: 1454
- `handleExternalLinks` (@ `includes/Parser/Parser.php`) -> Impact: **712.1** | LOC: 1910
  * *Intent:* /** * Replace external links (REL) * * Note: this is all very hackish and the order of execution matters a lot. * Make sure to run tests/parser/parser...
- `handleTables` (@ `includes/Parser/Parser.php`) -> Impact: **691.8** | LOC: 1872
  * *Intent:* /** * Parse the wiki syntax used to render tables. * * @param string $text * @return string */
- `handleInternalLinks2` (@ `includes/Parser/Parser.php`) -> Impact: **683.6** | LOC: 1877
  * *Intent:* /** * Process [[ ]] wikilinks (RIL) * @param string &$s * @return LinkHolderArray */
- `cleanSig` (@ `includes/Parser/Parser.php`) -> Impact: **647.2** | LOC: 1721
  * *Intent:* /** * Clean up signature text * * 1) Strip 3, 4 or 5 tildes out of signatures, see {@link cleanSigInSig} * 2) Substitute all transclusions * * @param ...
- `makeFormattedData` (@ `includes/Media/FormatMetadata.php`) -> Impact: **558.7** | LOC: 709
  * *Intent:* /** * Numbers given by Exif user agents are often magical, that is they * should be replaced by a detailed explanation depending on their * value whic...
- `requireTokenizer` (@ `resources/lib/vue-test-utils/vue-test-utils.browser.js`) -> Impact: **501.4** | LOC: 1427

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `includes/Api` | 145 | 31582.08 | 40.84% | 76.53% |
| `includes/Parser` | 44 | 21497.29 | 27.49% | 71.98% |
| `tests/phpunit/integration/includes/Json` | 5 | 20030.96 | 3.36% | 0.0% |
| `includes/Specials` | 132 | 19918.52 | 26.24% | 78.12% |
| `maintenance` | 200 | 18249.56 | 36.43% | 34.25% |
| `languages/messages` | 517 | 10839.12 | 2.22% | 0.17% |
| `includes/Language` | 32 | 10661.21 | 22.2% | 66.97% |
| `includes/Page` | 49 | 10021.72 | 21.19% | 50.95% |
| `languages/i18n/datetime` | 578 | 9541.42 | 0.0% | 0.0% |
| `includes/Media` | 38 | 8309.9 | 27.9% | 63.18% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `resources/src/moment/moment-locale-overrides.js` -> **100.0%** Exposure
- `includes/Api/ApiLinkAccount.php` -> **100.0%** Exposure
- `includes/Auth/AbstractPrimaryAuthenticationProvider.php` -> **100.0%** Exposure
- `includes/Auth/AbstractSecondaryAuthenticationProvider.php` -> **100.0%** Exposure
- `includes/Auth/EmailNotificationSecondaryAuthenticationProvider.php` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `resources/lib/CLDRPluralRuleParser/CLDRPluralRuleParser.js` -> **100.0%** Exposure
- `resources/lib/fetch-polyfill/fetch.umd.js` -> **100.0%** Exposure
- `resources/lib/intersection-observer/intersection-observer.js` -> **100.0%** Exposure
- `resources/lib/jquery.i18n/src/languages/fi.js` -> **100.0%** Exposure
- `resources/lib/jquery.i18n/src/languages/ga.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `includes/MediaWikiServices.php` -> **244** Orphaned Functions | **0** Duplicates
- `tests/phpunit/includes/Title/TitleTest.php` -> **149** Orphaned Functions | **0** Duplicates
- `includes/libs/Rdbms/Database/DBConnRef.php` -> **135** Orphaned Functions | **0** Duplicates
- `resources/lib/ooui/oojs-ui-core.js` -> **112** Orphaned Functions | **16** Duplicates
- `tests/phpunit/includes/Output/OutputPageTest.php` -> **123** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `tests/phpunit/includes/Api/ApiLoginTest.php` -> **93.201%** Exposure
- `tests/phpunit/includes/Auth/TemporaryPasswordPrimaryAuthenticationProviderTest.php` -> **34.68%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `19` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `96071` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `maintenance/rebuildLocalisationCache.php` (PHP) -> Cumulative Risk: **681.44**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 219.28 | **LOC:** 277 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (97.7755%), Safety Score (96.6717%)
- **Heaviest Functions:** `finalSetup` (Impact: 74.8), `__construct` (Impact: 5.0)

### 2. `includes/OutputTransform/Stages/ParsoidLanguageConverter.php` (PHP) -> Cumulative Risk: **665.1**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 340.68 | **LOC:** 398 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (98.7966%), Safety Score (95.3568%)
- **Heaviest Functions:** `convertNode` (Impact: 122.0), `transformDOM` (Impact: 28.2), `shouldRun` (Impact: 8.3)

### 3. `resources/lib/fetch-polyfill/fetch.umd.js` (JAVASCRIPT) -> Cumulative Risk: **659.61**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 11.77 | **LOC:** 621 | **CtrlFlow:** 29.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (99.5754%), Safety Score (88.8973%)
- **Heaviest Functions:** `normalizeName` (Impact: 63.5), `Request` (Impact: 58.3), `fetch` (Impact: 46.4)

### 4. `resources/src/mediawiki.Upload.js` (JAVASCRIPT) -> Cumulative Risk: **633.37**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 209.14 | **LOC:** 426 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9568%), Tech Debt (99.9332%)
- **Heaviest Functions:** `upload` (Impact: 9.4), `setFilenameFromFile` (Impact: 8.8), `uploadToStash` (Impact: 8.4)

### 5. `resources/src/mediawiki.feedback/FeedbackDialog.js` (JAVASCRIPT) -> Cumulative Risk: **623.27**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 178.66 | **LOC:** 345 | **CtrlFlow:** 7.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9996%), Concurrency (99.9947%), Safety Score (88.4109%)
- **Heaviest Functions:** `getActionProcess` (Impact: 12.0), `postMessage` (Impact: 11.2), `getSetupProcess` (Impact: 9.7)

### 6. `resources/lib/pinia/pinia.iife.js` (JAVASCRIPT) -> Cumulative Risk: **618.61**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 33.54 | **LOC:** 2127 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (91.1178%), State Flux (84.9848%), Verification (80.0%)
- **Heaviest Functions:** `createSetupStore` (Impact: 217.6), `registerPiniaDevtools` (Impact: 62.6), `set` (Impact: 42.4)

### 7. `includes/Deferred/LinksUpdate/CategoryLinksTable.php` (PHP) -> Cumulative Risk: **616.9**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 191.38 | **LOC:** 400 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (96.1159%), Safety Score (91.4116%)
- **Heaviest Functions:** `setParserOutput` (Impact: 9.2), `finishUpdate` (Impact: 7.8), `__construct` (Impact: 5.3)

### 8. `resources/src/mediawiki.widgets/MediaSearch/mw.widgets.MediaResourceProvider.js` (JAVASCRIPT) -> Cumulative Risk: **615.36**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 152.06 | **LOC:** 316 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.8557%), Tech Debt (96.1541%)
- **Heaviest Functions:** `fetchAPIresults` (Impact: 16.6), `getResults` (Impact: 8.7), `MwWidgetsMediaResourceProvider` (Impact: 7.9)

### 9. `resources/src/mediawiki.authenticationPopup/AuthPopup.js` (JAVASCRIPT) -> Cumulative Risk: **613.03**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 199.78 | **LOC:** 460 | **CtrlFlow:** 12.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.7916%), Concurrency (98.3768%), Verification (80.0%)
- **Heaviest Functions:** `openBrowserWindowCoveringElement` (Impact: 32.1), `showDialog` (Impact: 23.6), `getWindowDimensions` (Impact: 15.7)

### 10. `resources/src/mediawiki.widgets/mw.widgets.LanguageSelectWidget.js` (JAVASCRIPT) -> Cumulative Risk: **609.66**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 46.5 | **LOC:** 91 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9977%), Tech Debt (99.9887%)
- **Heaviest Functions:** `replaceWithVue` (Impact: 15.5), `onLanguageChange` (Impact: 6.7), `menuItemSlot` (Impact: 1.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `includes/Parser/Parser.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 9114.26 | **LOC:** 6513 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 28.6%
- **Risk Profile:** Cognitive Load (54.2915%), Tech Debt (46.6546%)
**Top Internal Functions/Classes:**
  * `internalParse` (Impact: 951.4)
    * *Intent:* /** * Helper function for parse() that transforms wiki markup into half-parsed * HTML. Only called f...
  * `handleExternalLinks` (Impact: 712.1)
    * *Intent:* /** * Replace external links (REL) * * Note: this is all very hackish and the order of execution mat...
  * `handleTables` (Impact: 691.8)
    * *Intent:* /** * Parse the wiki syntax used to render tables. * * @param string $text * @return string */
  * `handleInternalLinks2` (Impact: 683.6)
    * *Intent:* /** * Process [[ ]] wikilinks (RIL) * @param string &$s * @return LinkHolderArray */
  * `cleanSig` (Impact: 647.2)
    * *Intent:* /** * Clean up signature text * * 1) Strip 3, 4 or 5 tildes out of signatures, see {@link cleanSigIn...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 1082 instances
* *Amplified Sql Injection:* 1 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 3445
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1172`, `structural_boundaries: 630`, `args: 160`, `func_start: 150`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 182`, `state_mutation: 1281`, `dead_code: 26`, `planned_debt: 7`, `fragile_debt: 17`, `unreferenced_by_name: 42`
* *Architecture:* `io: 3`, `api: 129`, `concurrency: 1`, `import: 110`
* *Defense:* `safety: 112`, `doc: 193`, `sync_locks: 11`, `immutability_locks: 16`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.515
  * `Choke Point (Betweenness):` 0.000912 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 57):` 
			&			# 1. entity prefix
			(?=			# 2. followed by:
			(?:			#  a. one of the legacy semicolon-less named entities
				A(?:Elig|MP|acute|circ|grave|ring|tilde|uml)|
				C(?:OPY|cedil)|E(?:TH|acute|circ|grave|uml)|
				GT|I(?:acute|circ|grave|uml)|LT|Ntilde|
				O(?:acute|circ|grave|slash|tilde|uml)|QUOT|REG|THORN|
				U(?:acute|circ|grave|uml)|Yacute|
				a(?:acute|c(?:irc|ute)|elig|grave|mp|ring|tilde|uml)|brvbar|
				c(?:cedil|edil|urren)|cent(?!erdot, $flags = 0 ) 
		$oldVal = $this->mFunctionHooks[$id][0] ?? null, $params = [] ) 
		$msg = new RawMessage( $text, $size ) 
		if ( $this->mIncludeSizes[$type] + $size > $this->mOptions->getMaxIncludeSize() ) 
			return false, 'general' or 'nowiki'.
	 *
	 * @param string $tag The tag to use, *    including equals signs. For the section before the first heading, noinclude tags should be handled
			# depth=0 means this is the top-level document, ?ILanguageConverter $converter
	) 
		if ( $tocData === null ) 
			return...
  * `Imported By (In-Degree: 67):` (Excluded from Brief to save tokens)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.051
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.051
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.051
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.051
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `includes/Language/Language.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4787.26 | **LOC:** 5079 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (49.5784%), Tech Debt (28.4897%)
**Top Internal Functions/Classes:**
  * `sprintfDate` (Impact: 1229.0)
    * *Intent:* * $ts is UTC if $zone is not given. * * @param string $format * @param string $ts 14-character times...
  * `truncateInternal` (Impact: 202.4)
    * *Intent:* * one common method, allowing users to provide the length measurement function and * function for fi...
  * `formatNumInternal` (Impact: 76.8)
    * *Intent:* /** * Internal implementation function, shared between formatNum and formatNumNoSeparators. * * @par...
  * `formatTimePeriod` (Impact: 47.9)
    * *Intent:* /** * Formats a time given in seconds into a string representation of that time. * * @param int|floa...
  * `translateBlockExpiry` (Impact: 32.0)
    * *Intent:* /** * @todo Maybe translate block durations. Note that this function is somewhat misnamed: it * deal...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 832 instances
* *State Mutation (weighted view):* 2592
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1030`, `structural_boundaries: 774`, `args: 162`, `func_start: 157`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 421`, `state_mutation: 928`, `dead_code: 6`, `planned_debt: 11`, `fragile_debt: 4`, `unreferenced_by_name: 32`
* *Architecture:* `io: 1`, `api: 139`, `import: 93`
* *Defense:* `safety: 45`, `doc: 198`, `immutability_locks: 20`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.665
  * `Choke Point (Betweenness):` 0.001182 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 20):` $styles, 'centuries', 'days', 'decades', 'hours', 'minutes', 'seconds'
			], 'years'...
  * `Imported By (In-Degree: 197):` (Excluded from Brief to save tokens)

### `includes/Output/OutputPage.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3823.44 | **LOC:** 5226 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 7.7%
- **Risk Profile:** Cognitive Load (45.3489%), Tech Debt (85.8891%)
**Top Internal Functions/Classes:**
  * `showPermissionStatus` (Impact: 484.9)
    * *Intent:* /** * Output a standard permission error page * * @param PermissionStatus $status * @param string|nu...
  * `sendCacheControl` (Impact: 326.1)
    * *Intent:* /** * Send cache control HTTP headers */
  * `getHeadLinksSyndicationArray` (Impact: 85.0)
    * *Intent:* /** * Get head links relating to syndication feeds. * * @param Config $config * @return array */
  * `getJSVars` (Impact: 58.3)
    * *Intent:* * in other words, page-independent/site-wide variables (without state). * These would add a blocking...
  * `addParserOutputMetadata` (Impact: 47.1)
    * *Intent:* /** * Add all metadata associated with a ParserOutput object, but without the actual HTML. This * in...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 506 instances
* *State Mutation (weighted view):* 1732
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 533`, `structural_boundaries: 605`, `args: 211`, `func_start: 204`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 131`, `state_mutation: 720`, `dead_code: 5`, `planned_debt: 8`, `fragile_debt: 8`, `unreferenced_by_name: 77`
* *Architecture:* `io: 34`, `api: 181`, `import: 80`
* *Defense:* `safety: 60`, `doc: 272`, `immutability_locks: 7`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.606
  * `Choke Point (Betweenness):` 0.00216 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 42):` $includeStyle = true ) 
		$config = $this->getConfig(, $linkItem, $path ) 
		$localDir = MW_INSTALL_PATH, $query ), $query = [] ) 
		$this->addSubtitle( self::buildBacklinkSubtitle( $title,  Callers will typically have a PageRecord
			if ( $page->isRedirect() ) 
				$query['redirect'] = 'no', $this->buildCssLinksArray() ) . $this->mInlineStyles, '1.44'...
  * `Imported By (In-Degree: 99):` (Excluded from Brief to save tokens)

### `includes/EditPage/EditPage.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2925.8 | **LOC:** 4507 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 47.2%
- **Risk Profile:** Cognitive Load (44.9217%), Tech Debt (14.4759%)
**Top Internal Functions/Classes:**
  * `getPreviewText` (Impact: 125.1)
    * *Intent:* /** * Get the rendered text for previewing. * @throws MWException * @return string */
  * `internalAttemptSave` (Impact: 116.0)
    * *Intent:* * @param bool $markAsBot True if edit is being made under the bot right * and the bot wishes the edi...
  * `handleStatus` (Impact: 85.5)
    * *Intent:* /** * Handle status, such as after attempt save * * @param EditPageStatus $status * @param array|fal...
  * `importFormDataPosted` (Impact: 77.9)
  * `edit` (Impact: 49.5)
    * *Intent:* /** * This is the function that gets called for "action=edit". It * sets up various member variables...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 484 instances
* *State Mutation (weighted view):* 1634
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 612`, `structural_boundaries: 446`, `args: 94`, `func_start: 93`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 666`, `dead_code: 6`, `planned_debt: 10`, `fragile_debt: 11`
* *Architecture:* `io: 3`, `api: 56`, `import: 108`
* *Defense:* `safety: 53`, `doc: 157`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.676
  * `Choke Point (Betweenness):` 0.000636 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 87):` # headline would need to be parsed to improve this.
				if ( $hasmatch && $matches[2] !== '' ) 
					$sectionAnchor = $this->pageEditingHelper->guessSectionName( $matches[2], $this->context->getUser()->getEditToken() ) .
			"\n", 'accesskey-foo'
	 *  - 'label-id' (optional): 'id' attribute for the `<label>`
	 *  - 'legacy-name' (optional): short name for backwards-compatibility
	 *  - 'class' (optional): PHP class name of the OOUI widget to use. Defaults to
	 *    CheckboxInputWidget.
	 *  - 'options' (optional): options to use for DropdownInputWidget, 'blocked-notice-logextract', 'code-editing-intro', 'newarticletext', 'newarticletextanon', 'recreate-moveddeleted-warn'...
  * `Imported By (In-Degree: 26):` (Excluded from Brief to save tokens)

### `includes/libs/Rdbms/Database/Database.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2375.62 | **LOC:** 3606 | **CtrlFlow:** 15.5% | **Authorship Centralization:** 20.0%
- **Risk Profile:** Cognitive Load (44.2995%), Tech Debt (99.3618%)
**Top Internal Functions/Classes:**
  * `sourceStream` (Impact: 52.4)
    * *Intent:* /** @inheritDoc */
  * `assessConnectionLoss` (Impact: 48.3)
    * *Intent:* * is considered acceptable for DBO_TRX logic. * * If state was lost, but that loss was discovered du...
  * `__construct` (Impact: 37.0)
    * *Intent:* /** * @note exceptions for missing libraries/drivers should be thrown in initConnection() * @param a...
  * `attemptQuery` (Impact: 34.5)
    * *Intent:* * - write callers * - last write time * - affected row count of the last write * - whether writes oc...
  * `handleErroredQuery` (Impact: 32.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 332 instances
* *Amplified Sql Injection:* 9 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 82
* *State Mutation (weighted view):* 1119
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 340`, `structural_boundaries: 512`, `args: 202`, `func_start: 197`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 1`, `state_mutation: 455`, `dead_code: 3`, `planned_debt: 3`, `fragile_debt: 1`, `unreferenced_by_name: 107`
* *Architecture:* `io: 1`, `api: 156`, `import: 24`
* *Defense:* `safety: 71`, `doc: 254`, `sync_locks: 7`, `immutability_locks: 41`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.428
  * `Choke Point (Betweenness):` 0.000202 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` $cs, $errno, $fname, $sql->getSQL(), $trxError, ?CriticalSectionScope $csm, ?Throwable $trxError = null
	) 
		if ( $csm !== null ) 
			if ( $this->csmId === null ) 
				throw new LogicException( "$fname critical section is not active", Exception...
  * `Imported By (In-Degree: 30):` (Excluded from Brief to save tokens)

### `includes/Title/Title.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2298.42 | **LOC:** 3898 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (33.7839%), Tech Debt (12.0528%)
**Top Internal Functions/Classes:**
  * `secureAndSplit` (Impact: 256.9)
    * *Intent:* * * Assumes that $text is urldecoded * and uses underscores, but not otherwise munged. This function...
  * `getLocalURL` (Impact: 39.2)
    * *Intent:* * $wgServer is prepended to make an absolute URL. * * @see self::getFullURL to always get an absolut...
  * `convertByteClassToUnicodeClass` (Impact: 38.6)
    * *Intent:* /** * Utility method for converting a character sequence from bytes to Unicode. * * Primary usecase ...
  * `makeName` (Impact: 18.2)
    * *Intent:* /** * Make a prefixed DB key from a DB key and a namespace index * * @param int $ns Numerical repres...
  * `loadFromRow` (Impact: 15.6)
    * *Intent:* /** * Load Title object fields from a DB row. * If false is given, the title will be treated as non-...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 348 instances
* *State Mutation (weighted view):* 1139
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 353`, `structural_boundaries: 526`, `args: 165`, `func_start: 163`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 443`, `dead_code: 4`, `planned_debt: 10`, `fragile_debt: 3`
* *Architecture:* `api: 148`, `import: 53`
* *Defense:* `safety: 40`, `doc: 192`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.051
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 36):` 'This Title instance does not represent a proper page, InvalidArgumentException, LinkTargetTrait, MediaWiki\Context\RequestContext, MediaWiki\DAO\WikiAwareEntityTrait, MediaWiki\Deferred\AutoCommitUpdate, MediaWiki\Deferred\DeferredUpdates, MediaWiki\Deferred\LinksUpdate\CategoryLinksTable...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `includes/Linker/Linker.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2228.78 | **LOC:** 2040 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 20.0%
- **Risk Profile:** Cognitive Load (45.5832%), Tech Debt (54.6593%)
**Top Internal Functions/Classes:**
  * `makeImageLink` (Impact: 198.8)
    * *Intent:* * link-url URL to link to * link-title LinkTarget object to link to * link-target Value for the targ...
  * `makeThumbLink2` (Impact: 195.6)
    * *Intent:* /** * @param LinkTarget $title * @param File|false $file * @param array $frameParams * @param array ...
  * `formatHiddenCategories` (Impact: 66.8)
    * *Intent:* /** * Returns HTML for the "hidden categories on this page" list. * * @since 1.16.3 * @param array $...
  * `makeBrokenImageLinkObj` (Impact: 42.0)
    * *Intent:* /** * Make a "broken" link to an image * * @since 1.16.3 * @param LinkTarget $title * @param string ...
  * `userToolLinkArray` (Impact: 39.8)
    * *Intent:* * @param int $userId User identifier * @param string $userText User name or IP address * @param bool...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 378 instances
* *State Mutation (weighted view):* 1180
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 331`, `structural_boundaries: 225`, `args: 47`, `func_start: 45`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 424`, `planned_debt: 8`, `fragile_debt: 1`, `unreferenced_by_name: 17`
* *Architecture:* `api: 45`, `import: 27`
* *Defense:* `safety: 77`, `doc: 49`, `immutability_locks: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.661
  * `Choke Point (Betweenness):` 0.000331 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 20):` "extiw").  Only use the class attribute
	 *       provided, "mw-redirect", $altUserName = false, $attributes = []
	) 
		if ( $userName === '' || $userName === false || $userName === null ) 
			wfDebug( __METHOD__ . ' received an empty username. Are there database errors ' .
				'that need to be fixed?', $customAttribs = [], $delete = true ) 
		$sp = SpecialPage::getTitleFor( 'Revisiondelete', $html = null, $isPublic = false...
  * `Imported By (In-Degree: 66):` (Excluded from Brief to save tokens)

### `tests/Common/Parser/ParserTestRunner.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2224.22 | **LOC:** 3281 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 69.2%
- **Risk Profile:** Cognitive Load (47.7513%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `addParserOutputInfo` (Impact: 125.1)
    * *Intent:* /** * Add information from the parser output to the result string * * @param string &$out The "actua...
  * `processResults` (Impact: 69.6)
    * *Intent:* /** * This processes test results and updates the known failures info for the test * * @param Parser...
  * `runParsoidTest` (Impact: 60.0)
    * *Intent:* * running in 'integrated' mode, and compare the output against the * expected results. * * Prints st...
  * `wt2html` (Impact: 50.8)
    * *Intent:* /** * Run wt2html on the test * * @param Parsoid $parsoid * @param PageConfig $pageConfig * @param P...
  * `updateTests` (Impact: 46.8)
    * *Intent:* /** * @param string $filename The parser test file * @param TestFileReader $testFileInfo * @param bo...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Cascading Flux:* 331 instances
* *Memory Alloc (weighted view):* 61
* *State Mutation (weighted view):* 1168
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 393`, `structural_boundaries: 409`, `args: 105`, `func_start: 65`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 506`, `dead_code: 8`, `planned_debt: 5`, `fragile_debt: 2`, `unreferenced_by_name: 6`
* *Architecture:* `io: 5`, `api: 30`, `import: 81`
* *Defense:* `safety: 113`, `doc: 71`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.051
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 45):` " .
				"which isn't provided by any loaded extension.", $nextTeardown = null ): ScopedCallback 
		$teardown = [], $test->testName, 'functionHook' => $this->requireFunctionHook( $requirement['name'] ), BadMethodCallException, FunctionHook( $name ) 
		$parser = MediaWikiServices::getInstance()->getParser(, Hook( $name ) 
		$parser = MediaWikiServices::getInstance()->getParser(, MediaWikiIntegrationTestCase...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `includes/Revision/RevisionStore.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2115.64 | **LOC:** 3443 | **CtrlFlow:** 17.0% | **Authorship Centralization:** 30.0%
- **Risk Profile:** Cognitive Load (42.2447%), Tech Debt (13.6426%)
**Top Internal Functions/Classes:**
  * `newRevisionsFromBatch` (Impact: 94.5)
    * *Intent:* * always be loaded. * 'content' - whether the actual content of the slots should be * preloaded. * '...
  * `newRevisionFromRowAndSlots` (Impact: 71.5)
    * *Intent:* * @param stdClass $row A database row generated from a query based on RevisionSelectQueryBuilder * @...
  * `getSlotRowsForBatch` (Impact: 48.9)
    * *Intent:* * all slots are fetched * 'blobs' - whether the serialized content of each slot should be loaded. * ...
  * `newRevisionFromArchiveRowAndSlots` (Impact: 47.0)
    * *Intent:* * @param stdClass $row * @param null|stdClass[]|RevisionSlots $slots * - Database rows generated fro...
  * `getRevisionIdsBetween` (Impact: 41.9)
    * *Intent:* * @param string|array $options Single option, or an array of options: * RevisionStore::INCLUDE_OLD I...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 315 instances
* *State Mutation (weighted view):* 1018
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 351`, `structural_boundaries: 369`, `args: 86`, `func_start: 74`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 388`, `dead_code: 5`, `planned_debt: 14`, `fragile_debt: 4`
* *Architecture:* `api: 47`, `import: 60`
* *Defense:* `safety: 91`, `doc: 75`, `sync_locks: 2`, `immutability_locks: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.526
  * `Choke Point (Betweenness):` 0.000363 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 41):` "actor_rev_user.actor_id = rev_actor" ], $flags, $flags = 0, $flags = 0 ) 
		$conds = $this->getPageConditions( $page, $flags = 0 ) 
		$conds = [ 'page_id' => $pageId ], $flags = 0 ) 
		if ( $this->wikiId !== RevisionRecord::LOCAL ) 
			throw new PreconditionException( 'RecentChangeLookup is only available for the local wiki', $flags = IDBAccessObject::READ_NORMAL ) 
		return $this->getRelativeRevision( $rev, $max...
  * `Imported By (In-Degree: 65):` (Excluded from Brief to save tokens)

### `includes/FileRepo/File/LocalFile.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2087.82 | **LOC:** 2809 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (44.7544%), Tech Debt (31.7115%)
**Top Internal Functions/Classes:**
  * `upgradeRow` (Impact: 325.6)
    * *Intent:* /** * Fix assorted version-related problems with the image row by reloading it from the file * @stab...
  * `recordUpload3` (Impact: 153.9)
    * *Intent:* * @since 1.35 * @stable to override * @param string $oldver * @param string $comment * @param string...
  * `upload` (Impact: 67.1)
    * *Intent:* * @param array|false $props File properties, if known. This can be used to * reduce the upload time ...
  * `publishTo` (Impact: 33.9)
    * *Intent:* * object with the archive name in the "value" member on success. * * The archive name should be pass...
  * `getHistory` (Impact: 25.1)
    * *Intent:* /** purgeDescription inherited */ /** purgeEverything inherited */ /** * @stable to override * @para...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 336 instances
* *Memory Alloc (weighted view):* 25
* *State Mutation (weighted view):* 1086
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 305`, `structural_boundaries: 309`, `args: 82`, `func_start: 74`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 58`, `state_mutation: 414`, `planned_debt: 4`, `unreferenced_by_name: 19`
* *Architecture:* `api: 56`, `import: 46`
* *Defense:* `safety: 35`, `doc: 158`, `sync_locks: 3`, `immutability_locks: 10`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.285
  * `Choke Point (Betweenness):` 0.000227 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 37):` '1.41', InvalidArgumentException, MediaWiki\Content\ContentHandler, MediaWiki\Context\RequestContext, MediaWiki\Deferred\AutoCommitUpdate, MediaWiki\Deferred\DeferredUpdates, MediaWiki\Deferred\LinksUpdate\LinksUpdate, MediaWiki\Deferred\SiteStatsUpdate...
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `includes/Skin/Skin.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1929.36 | **LOC:** 2584 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 18.2%
- **Risk Profile:** Cognitive Load (34.4286%), Tech Debt (8.5173%)
**Top Internal Functions/Classes:**
  * `getPersonalToolsForMakeListItem` (Impact: 79.5)
    * *Intent:* /** * Create an array of personal tools items from the data in the quicktemplate * stored by SkinTem...
  * `buildNavUrls` (Impact: 47.8)
    * *Intent:* /** * Build array of common navigation links. * Assumes thispage property has been set before execut...
  * `makeToolbox` (Impact: 30.2)
    * *Intent:* /** * Create an array of common toolbox items from the data in the quicktemplate * stored by SkinTem...
  * `createSidebarItem` (Impact: 27.1)
    * *Intent:* /** * Generates an array item for the sidebar * @param string $target Target link in the form of an ...
  * `getDefaultModules` (Impact: 26.9)
    * *Intent:* /** * Defines the ResourceLoader modules that should be added to the skin * It is recommended that s...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 385 instances
* *Memory Alloc (weighted view):* 6
* *State Mutation (weighted view):* 1237
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 315`, `structural_boundaries: 265`, `args: 70`, `func_start: 68`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 467`, `dead_code: 1`, `planned_debt: 3`
* *Architecture:* `api: 55`, `import: 33`
* *Defense:* `safety: 35`, `doc: 80`, `immutability_locks: 17`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.721
  * `Choke Point (Betweenness):` 0.000934 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 26):` $item, $options, $options = [] ) 
		$component = new SkinComponentListItem(
			$key, $section, $sectionTitle, $this->defaultLinkOptions, $this->getContext(), 'actions'...
  * `Imported By (In-Degree: 75):` (Excluded from Brief to save tokens)

### `includes/Diff/DifferenceEngine.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1915.84 | **LOC:** 2494 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (45.2527%), Tech Debt (13.4253%)
**Top Internal Functions/Classes:**
  * `showDiffPage` (Impact: 438.1)
    * *Intent:* /** * @param bool $diffOnly */
  * `getDiffBody` (Impact: 28.6)
    * *Intent:* /** * Get the diff table body, without header * * @return string|false */
  * `addHeader` (Impact: 27.9)
    * *Intent:* /** * Add the header to a diff body * * @param string $diff Diff body * @param string $otitle Old re...
  * `loadRevisionData` (Impact: 26.4)
    * *Intent:* /** * Load revision metadata for the specified revisions. If newid is 0, then compare * the old revi...
  * `getMultiNotice` (Impact: 24.7)
    * *Intent:* /** * If there are revisions between the ones being compared, return a note saying so. * * @return s...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 287 instances
* *State Mutation (weighted view):* 940
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 303`, `structural_boundaries: 313`, `args: 71`, `func_start: 70`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 366`, `dead_code: 2`, `planned_debt: 4`, `fragile_debt: 5`
* *Architecture:* `io: 19`, `api: 47`, `import: 47`
* *Defense:* `safety: 34`, `doc: 101`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.593
  * `Choke Point (Betweenness):` 9.9e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 35):` * selecting and invoking the diff generator class for the individual slots, BadMethodCallException, DeprecationHelper, Exception, InvalidArgumentException, LogicException, MediaWiki\ChangeTags\ChangeTags, MediaWiki\CommentFormatter\CommentFormatter...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `includes/Parser/ParserOutput.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1912.42 | **LOC:** 3448 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 53.8%
- **Risk Profile:** Cognitive Load (46.7102%), Tech Debt (10.6337%)
**Top Internal Functions/Classes:**
  * `initFromJson` (Impact: 109.8)
    * *Intent:* /** * Initialize member fields from an array returned by jsonSerialize(). * @param array $jsonData *...
  * `getLinkList` (Impact: 95.9)
    * *Intent:* * the metadata. * * Each element of the returned array has a LinkTarget as the 'link' * property. Lo...
  * `collectMetadata` (Impact: 71.2)
    * *Intent:* /** * Adds the metadata collected in this ParserOutput to the supplied * ContentMetadataCollector. T...
  * `mergeMapStrategy` (Impact: 35.2)
  * `mergeInternalMetaDataFrom` (Impact: 27.4)
    * *Intent:* /** * Merges internal metadata such as flags, accessed options, and profiling info * from $source in...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 258 instances
* *State Mutation (weighted view):* 847
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 405`, `structural_boundaries: 382`, `args: 161`, `func_start: 155`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 331`, `dead_code: 2`, `planned_debt: 8`, `fragile_debt: 1`
* *Architecture:* `io: 2`, `api: 144`, `import: 25`
* *Defense:* `safety: 96`, `doc: 188`, `immutability_locks: 9`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.803
  * `Choke Point (Betweenness):` 0.000149 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):`  Don't record interwikis in pagelinks
			$this->addInterwikiLink( $link, $page_id,  Will throw an InvalidArgumentException in a future release.
			throw new InvalidArgumentException( __METHOD__ . " with interwiki link", $source->mExtensionData, $tag = false ): void 
		if ( $tag !== false ) 
			$this->mHeadItems[$tag] = $section, $this->getOutputStrings( $name ), *     but might be statefully overridden.
	 *  - userLang: (Language) Language object used for localizing UX messages, *    for example the heading of the table of contents. If omitted...
  * `Imported By (In-Degree: 155):` (Excluded from Brief to save tokens)

### `includes/libs/Rdbms/Platform/SQLPlatform.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1899.08 | **LOC:** 2144 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (46.6264%), Tech Debt (98.1671%)
**Top Internal Functions/Classes:**
  * `selectSQLText` (Impact: 136.8)
    * *Intent:* /** @inheritDoc */
  * `makeList` (Impact: 104.5)
    * *Intent:* /** @inheritDoc */
  * `tableNamesWithIndexClauseOrJOIN` (Impact: 42.6)
    * *Intent:* /** * Get the aliased table name clause for a FROM clause * which might have a JOIN and/or USE INDEX...
  * `assertValidUpsertSetArray` (Impact: 28.1)
    * *Intent:* /** * @param array $set Combined column/literal assignment map and SQL assignment list * @param stri...
  * `buildSuperlative` (Impact: 25.3)
    * *Intent:* /** * Build a superlative function statement comparing columns/values * * Integer and float values i...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Cascading Flux:* 280 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 64
* *State Mutation (weighted view):* 865
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 383`, `structural_boundaries: 348`, `args: 101`, `func_start: 99`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 35`, `high_risk_execution: 1`, `state_mutation: 305`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 56`
* *Architecture:* `api: 76`, `import: 18`
* *Defense:* `safety: 70`, `doc: 100`, `sync_locks: 5`, `immutability_locks: 7`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.78
  * `Choke Point (Betweenness):` 7.6e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` $rowColumns ) . ') ' .
					'instead of expected (' . implode( ', $tupleColumns ) . '), ', InvalidArgumentException, Null ) 
						$list .= " OR $field IS NULL)",  Group subconditions to ensure correct precedence
						$list .= '(', Null ) 
					throw new InvalidArgumentException(
						__METHOD__ . ": empty input for field $field", Null = false...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `tests/phpunit/includes/Auth/AuthManagerTest.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1897.68 | **LOC:** 4607 | **CtrlFlow:** 5.1% | **Authorship Centralization:** 20.0%
- **Risk Profile:** Cognitive Load (27.6106%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testAccountCreation` (Impact: 97.8)
    * *Intent:* /** * @dataProvider provideAccountCreation */
  * `testAuthentication` (Impact: 96.7)
    * *Intent:* /** * @dataProvider provideAuthentication */
  * `testAccountLink` (Impact: 54.8)
    * *Intent:* /** * @dataProvider provideAccountLink */
  * `initializeManager` (Impact: 40.7)
    * *Intent:* /** * Initialize $this->manager * @param bool $regen Force a call to $this->initializeConfig() */
  * `testGetAuthenticationRequests` (Impact: 38.5)
    * *Intent:* /** * @dataProvider provideGetAuthenticationRequests * @param string $action * @param array $expect ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 204 instances
* *Concurrency (weighted view):* 8
* *Memory Alloc (weighted view):* 78
* *State Mutation (weighted view):* 1101
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 207`, `structural_boundaries: 503`, `args: 160`, `func_start: 70`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 693`, `fragile_debt: 3`, `unreferenced_by_name: 61`
* *Architecture:* `api: 61`, `concurrency: 3`, `import: 82`
* *Defense:* `safety: 99`, `doc: 34`, `test: 389`, `sync_locks: 7`, `immutability_locks: 1`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.051
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 60):` $makeReq( "bar", $makeReq( "baz", $makeReq( "foo", $makeReq( "optional", $makeReq( "optional2", $makeReq( "required", $makeReq( "required2", $this->getServiceContainer()->getBlockTargetFactory()...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `includes/Auth/AuthManager.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1841.86 | **LOC:** 3021 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 23.1%
- **Risk Profile:** Cognitive Load (49.7114%), Tech Debt (23.4181%)
**Top Internal Functions/Classes:**
  * `autoCreateUser` (Impact: 128.2)
    * *Intent:* * - the ID of a PrimaryAuthenticationProvider, * - one of the self::AUTOCREATE_SOURCE_* constants * ...
  * `continueAuthentication` (Impact: 118.6)
    * *Intent:* * new AuthenticationRequests should be made (if any), then * AuthManager::continueAuthentication() s...
  * `continueAccountCreation` (Impact: 115.3)
    * *Intent:* /** * Continue an account creation flow * @param AuthenticationRequest[] $reqs * @return Authenticat...
  * `getAuthenticationRequestsInternal` (Impact: 47.9)
    * *Intent:* /** * Internal request lookup for self::getAuthenticationRequests * * @param string $providerAction ...
  * `getAuthenticationRequests` (Impact: 44.6)
    * *Intent:* * - ACTION_LOGIN: Valid for passing to beginAuthentication * - ACTION_LOGIN_CONTINUE: Valid for pass...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 272 instances
* *State Mutation (weighted view):* 876
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 394`, `structural_boundaries: 328`, `args: 57`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 332`, `dead_code: 2`, `fragile_debt: 3`, `unreferenced_by_name: 13`
* *Architecture:* `api: 52`, `import: 51`
* *Defense:* `safety: 64`, `doc: 91`, `sync_locks: 6`, `immutability_locks: 45`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.69
  * `Choke Point (Betweenness):` 0.000345 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 41):` $returnToUrl ) 
		$session = $this->request->getSession(, InvalidArgumentException, LogicException, MediaWiki\Auth\Hook\AuthManagerVerifyAuthenticationHook, MediaWiki\Block\AbstractBlock, MediaWiki\Block\BlockManager, MediaWiki\ChangeTags\ChangeTagsStore, MediaWiki\Config\Config...
  * `Imported By (In-Degree: 55):` (Excluded from Brief to save tokens)

### `includes/Parser/CoreParserFunctions.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1827.36 | **LOC:** 2116 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 30.0%
- **Risk Profile:** Cognitive Load (35.496%), Tech Debt (13.781%)
**Top Internal Functions/Classes:**
  * `urlFunction` (Impact: 60.6)
    * *Intent:* /** * @param string $func * @param string $s * @param string|null $arg * @return array|string */
  * `displaytitle` (Impact: 38.4)
    * *Intent:* /** * Override the title of the page when viewed, provided we've been given a * title which will nor...
  * `revisionid` (Impact: 31.8)
    * *Intent:* /** * Get the id from the last revision of a specified page. * @param Parser $parser * @param string...
  * `tagObj` (Impact: 31.1)
    * *Intent:* /** * Parser function to extension tag adaptor * @param Parser $parser * @param PPFrame $frame * @pa...
  * `getCachedRevisionObject` (Impact: 31.1)
    * *Intent:* /** * Fetched the current revision of the given title and return this. * Will increment the expensiv...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 295 instances
* *State Mutation (weighted view):* 942
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 277`, `structural_boundaries: 321`, `args: 95`, `func_start: 91`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 352`, `dead_code: 8`, `planned_debt: 2`, `fragile_debt: 2`, `unreferenced_by_name: 1`
* *Architecture:* `api: 86`, `import: 21`
* *Defense:* `safety: 20`, `doc: 94`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.066
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` $processNowiki, InvalidArgumentException, MediaWiki\Category\Category, MediaWiki\Config\ServiceOptions, MediaWiki\Content\ContentHandler, MediaWiki\Language\Language, MediaWiki\Language\LanguageCode, MediaWiki\Language\LanguageNameUtils...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `includes/Preferences/DefaultPreferencesFactory.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1760.78 | **LOC:** 2302 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (47.6303%), Tech Debt (15.9924%)
**Top Internal Functions/Classes:**
  * `profilePreferences` (Impact: 156.1)
    * *Intent:* /** * @todo Inject user Language instead of using context. * @param User $user * @param IContextSour...
  * `getResetKinds` (Impact: 65.8)
    * *Intent:* /** * @param User $user * @param IContextSource $context * @param array|null $options * @return stri...
  * `__construct` (Impact: 50.6)
    * *Intent:* * @param AuthManager $authManager * @param LinkRenderer $linkRenderer * @param NamespaceInfo $nsInfo...
  * `getOptionFromUser` (Impact: 50.1)
    * *Intent:* /** * Pull option from a user account. Handles stuff like array-type preferences. * * @deprecated si...
  * `watchlistPreferences` (Impact: 44.7)
    * *Intent:* /** * @param User $user * @param IContextSource $context * @param array &$defaultPreferences */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 280 instances
* *Memory Alloc (weighted view):* 23
* *State Mutation (weighted view):* 935
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 311`, `structural_boundaries: 233`, `args: 40`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 375`, `dead_code: 2`, `planned_debt: 3`, `fragile_debt: 3`, `unreferenced_by_name: 3`
* *Architecture:* `api: 10`, `import: 56`
* *Defense:* `safety: 55`, `doc: 50`, `immutability_locks: 1`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.064
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 42):` 'disabled' => !$user->getEmail(), 'help-message' => 'prefs-help-requireemail', 'label-message' => 'tog-requireemail', email', LoggerAwareTrait, MediaWiki\Actions\WatchAction, MediaWiki\Auth\AuthManager, MediaWiki\Auth\PasswordAuthenticationRequest...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `includes/User/User.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1720.52 | **LOC:** 3429 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 15.0%
- **Risk Profile:** Cognitive Load (33.3225%), Tech Debt (98.3637%)
**Top Internal Functions/Classes:**
  * `loadFromRow` (Impact: 53.7)
    * *Intent:* /** * Initialize this object from a row from the user table. * * @param stdClass $row Row from the u...
  * `load` (Impact: 48.8)
    * *Intent:* /** * Load the user table data for this object from the source given by mFrom. * * @param int $flags...
  * `newSystemUser` (Impact: 23.3)
    * *Intent:* * - validate: Type of validation to use: * - false No validation * - 'valid' Valid for batch process...
  * `setEmailWithConfirmation` (Impact: 20.9)
    * *Intent:* /** * Set the user's e-mail address and send a confirmation mail if needed. * * @since 1.20 * @param...
  * `clearInstanceCache` (Impact: 19.1)
    * *Intent:* /** * Clear various cached data stored in this object. The cache of the user table * data (i.e. self...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 254 instances
* *Memory Alloc (weighted view):* 19
* *State Mutation (weighted view):* 855
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 293`, `structural_boundaries: 418`, `args: 145`, `func_start: 137`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 347`, `dead_code: 4`, `planned_debt: 4`, `fragile_debt: 3`, `unreferenced_by_name: 70`
* *Architecture:* `api: 137`, `import: 59`
* *Defense:* `safety: 26`, `doc: 169`, `immutability_locks: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.051
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 39):` $options = [] ) 
		$options += [
			'validate' => UserRigorOptions::RIGOR_VALID, 'create' => true, 'fields' => [
				'user_id', 'joins' => [
				'user_actor' => [ 'JOIN', 'steal' => false, 'user_actor' => 'actor' ], 'user_actor.actor_id', 'user_actor.actor_user = user_id' ]...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `includes/Page/WikiPage.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1684.66 | **LOC:** 2985 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (33.149%), Tech Debt (21.9491%)
**Top Internal Functions/Classes:**
  * `doUpdateRestrictions` (Impact: 124.3)
    * *Intent:* /** * Update the article's restriction field, and leave a log entry. * This works for protection bot...
  * `doUserEditContent` (Impact: 34.6)
    * *Intent:* * edit-already-exists: In creation mode, but the article already exists. * * Extensions may define a...
  * `getDerivedDataUpdater` (Impact: 28.9)
    * *Intent:* * * @since 1.32 * * @param UserIdentity|null $forUser The user that will be used for, or was used fo...
  * `replaceSectionAtRev` (Impact: 26.4)
    * *Intent:* /** * @param string|int|null|false $sectionId Section identifier as a number or string * (e.g. 0, 1 ...
  * `updateRevisionOn` (Impact: 21.4)
    * *Intent:* * @internal Low level interface, not safe for use in extensions! * * @todo Factor out into a PageSto...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 252 instances
* *State Mutation (weighted view):* 853
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 256`, `structural_boundaries: 321`, `args: 104`, `func_start: 97`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 349`, `dead_code: 4`, `planned_debt: 28`, `fragile_debt: 3`
* *Architecture:* `api: 85`, `import: 63`
* *Defense:* `safety: 10`, `doc: 112`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.07
  * `Choke Point (Betweenness):` 0.002113 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 49):` $actorNormalization->findActorId( $user, $dbr ) ), $serialFormat = null, $title->getDBkey()
				), $useStash = true
	) 
		$slots = RevisionSlotsUpdate::newFromContent( [ SlotRecord::MAIN => $content ], '!=', '1.32', 'actor_name' ] )
			->orderBy( 'timestamp'...
  * `Imported By (In-Degree: 98):` (Excluded from Brief to save tokens)

### `includes/libs/FileBackend/SwiftFileBackend.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1618.08 | **LOC:** 2042 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (36.1038%), Tech Debt (72.0511%)
**Top Internal Functions/Classes:**
  * `getDirListPageInternal` (Impact: 54.9)
    * *Intent:* /** * Do not call this function outside of SwiftFileBackendFileList * * @param string $fullCont Reso...
  * `getFileListPageInternal` (Impact: 34.1)
    * *Intent:* /** * Do not call this function outside of SwiftFileBackendFileList * * @param string $fullCont Reso...
  * `requestMultiWithAuth` (Impact: 31.4)
    * *Intent:* /** * Perform a batch of authenticated HTTP requests * * @param array $reqs An array of request data...
  * `objectListing` (Impact: 31.2)
    * *Intent:* /** * Get a list of objects under a container. * Either just the names or a list of stdClass objects...
  * `__construct` (Impact: 26.3)
    * *Intent:* * - rgwS3SecretKey : Rados Gateway S3 "secret key" value on the account. * Do not set this until it ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 283 instances
* *State Mutation (weighted view):* 876
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 322`, `structural_boundaries: 225`, `args: 63`, `func_start: 56`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 310`, `dead_code: 4`, `fragile_debt: 1`, `unreferenced_by_name: 29`
* *Architecture:* `io: 8`, `api: 12`, `import: 17`
* *Defense:* `safety: 76`, `doc: 87`, `immutability_locks: 2`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` $path, *     the request will refer to the container itself.
	 *   - headers: An array of request headers to send, abc")
	 *   - cacheAuthInfo      : Whether to cache authentication tokens in APC, :
	 *   - swiftAuthUrl       : Swift authentication server URL
	 *   - swiftUser          : Swift user used by MediaWiki (account:username)
	 *   - swiftKey           : Swift authentication key for the above user
	 *   - swiftAuthTTL       : Swift authentication TTL (seconds)
	 *   - swiftTempUrlKey    : Swift "X-Account-Meta-Temp-URL-Key" value on the account.
	 *                          Do not set this until it has been set in the backend.
	 *   - canShellboxGetTempUrl : Set this to true to generate a TempURL allowing Shellbox to
	 *                          directly fetch files from Swift. swiftTempUrlKey should be set.
	 *   - shellboxIpRange    : An IP range string to use when generating TempURLs for Shellbox.
	 *                          Specifying this will improve security by preventing exfiltrated
	 *                          TempURLs from being usable outside the server.
	 *   - swiftStorageUrl    : Swift storage URL (overrides that of the authentication response).
	 *                          This is useful to set if a TLS proxy is in use.
	 *   - shardViaHashLevels : Map of container names to sharding config with:
	 *                             - base   : base of hash characters, Exception, Psr\Log\LoggerInterface, SHA1'] ) ) 
					$rhdrs = $this->addMissingHashMetadata( $rhdrs, Shellbox\Command\BoxedCommand...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `includes/Parser/Parser.php` -> Churn: **80.97%** | Cog Load: 54.2915% | Debt: 46.6546%
- `includes/Page/Article.php` -> Churn: **76.42%** | Cog Load: 57.554% | Debt: 33.2764%
- `includes/MediaWikiServices.php` -> Churn: **74.32%** | Cog Load: 4.8198% | Debt: 100.0%
- `includes/User/User.php` -> Churn: **67.07%** | Cog Load: 33.3225% | Debt: 98.3637%
- `includes/Skin/SkinTemplate.php` -> Churn: **66.67%** | Cog Load: 54.5513% | Debt: 9.9135%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `includes/Parser/Preprocessor_Hash.php` -> **Func** (100.0% isolated ownership) | Magnitude: 1106.02
- `includes/HTMLForm/HTMLFormField.php` -> **Bartosz Dziewoński** (100.0% isolated ownership) | Magnitude: 1033.52
- `includes/libs/ObjectCache/MediumSpecificBagOStuff.php` -> **Sam Reed** (100.0% isolated ownership) | Magnitude: 856.6
- `includes/Language/ConverterRule.php` -> **C. Scott Ananian** (83.3% isolated ownership) | Magnitude: 792.54
- `resources/src/mediawiki.widgets.datetime/DiscordianDateTimeFormatter.js` -> **Ed Sanders** (100.0% isolated ownership) | Magnitude: 763.5

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `includes/MediaWikiServices.php` -> **Severity: 0.985** (Bridge: 0.023 * Flux: 42.8204%)
- `includes/SpecialPage/SpecialPageFactory.php` -> **Severity: 0.797** (Bridge: 0.0084 * Flux: 94.6894%)
- `includes/Content/ContentHandler.php` -> **Severity: 0.216** (Bridge: 0.0022 * Flux: 100.0%)
- `includes/Output/OutputPage.php` -> **Severity: 0.216** (Bridge: 0.0022 * Flux: 100.0%)
- `includes/Page/WikiPage.php` -> **Severity: 0.211** (Bridge: 0.0021 * Flux: 100.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `resources/lib/moment/moment.js` -> **Severity: 303.222** (Blast Radius: 6.089 * Doc Risk: 49.7984%)
- `includes/Context/RequestContext.php` -> **Severity: 78.12** (Blast Radius: 4.567 * Doc Risk: 17.1053%)
- `includes/Title/TitleValue.php` -> **Severity: 62.167** (Blast Radius: 1.492 * Doc Risk: 41.6667%)
- `includes/Language/RawMessage.php` -> **Severity: 57.7** (Blast Radius: 1.731 * Doc Risk: 33.3333%)
- `includes/Parser/Sanitizer.php` -> **Severity: 40.716** (Blast Radius: 3.212 * Doc Risk: 12.6761%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
