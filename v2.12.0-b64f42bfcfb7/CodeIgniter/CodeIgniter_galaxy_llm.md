# ARCHITECTURAL_BRIEF: CodeIgniter
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/bcit-ci/CodeIgniter.git` |
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
- **Scope:** 337 analyzed artifact(s), 36058 LOC.
- **Load-bearing artifact:** `system/core/Common.php` -- 31 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `system/core/Loader.php` -- pulls in 24 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `system/database/DB_query_builder.php` at magnitude 1777.08 (structural weight, not risk).
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
| Total Artifacts | 556 |
| Analyzed Artifacts (Scanned) | 337 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 219 |
| Total LOC | 36058 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 60.6% |
| Dominant Lang | PHP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7123 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2298 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.6345 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 23 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PHP | 277 | 35361 | 82.2% |
| HTML | 39 | 351 | 11.6% |
| XML | 9 | 0 | 2.7% |
| MARKDOWN | 3 | 0 | 0.9% |
| PYTHON | 3 | 28 | 0.9% |
| PLAINTEXT | 2 | 0 | 0.6% |
| YAML | 1 | 112 | 0.3% |
| SHELL | 1 | 66 | 0.3% |
| JSON | 1 | 35 | 0.3% |
| MAKEFILE | 1 | 105 | 0.3% |

## 4.1 SOURCE ENCODINGS
> 1 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 336 |
| latin-1 | latin-1-fallback | 1 |

> 1 guessed file(s) read as double-byte text that decodes strictly as gbk: if that is the estate's code page, rescan with `--source-encoding gbk` (or the right one of those). E.g. `tests/codeigniter/core/Utf8_test.php`.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 22%, Interface Declarations Files 16%, Declarative / Non-Code 15%, Encapsulated Accessors Files 11%, Large Core Modules (3) 11%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 332 | 98.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 5 | 1.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 219*

**Composition by Extension & Reason:**
- `.rst`: 170x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Unsupported Extension: '.rst')
- `.html`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.php`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 98 exceeds 500 chars)
- `.gif`: 5x Excluded (Explicitly Denied Extension: '.gif')
- `.css`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ttf`: 2x Excluded (Explicitly Denied Extension: '.ttf')
- `.py`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ico`: 2x Excluded (Explicitly Denied Extension: '.ico')
- `.js`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jpg`: 2x Excluded (Explicitly Denied Extension: '.jpg')
- `.otf`: 1x Excluded (Explicitly Denied Extension: '.otf')
- `.eot`: 1x Excluded (Explicitly Denied Extension: '.eot')
- `.svg`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.woff`: 1x Excluded (Explicitly Denied Extension: '.woff')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 66.5 | 16.0 | 6.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 87.6 | 50.0 | 57.1 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 27.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 16.9 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 12.0 | 3.1 | 1.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 51.7 | 77.9 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 18.4 | 0.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 15.6 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 397 | 108 | 3 | `system/libraries/Xmlrpcs.php` |
| cleanup | 103 | 48 | 1 | `system/libraries/Session/Session.php` |
| guards | 1989 | 184 | 18 | `system/database/DB_query_builder.php` |
| danger | 689 | 202 | 4 | `system/libraries/Upload.php` |
| concurrency | 33 | 11 | 0 | `system/libraries/Session/drivers/Session_redis_driver.php` |
| connectivity | 1745 | 180 | 12 | `system/libraries/Xmlrpc.php` |
| io | 286 | 50 | 2 | `system/core/Output.php` |
| crypto | 0 | 0 | 0 | - |
| ipc | 44 | 13 | 0 | `tests/codeigniter/core/Lang_test.php` |
| time | 96 | 25 | 0 | `system/helpers/date_helper.php` |
| serialization | 9 | 4 | 0 | `system/libraries/Cache/drivers/Cache_file.php` |
| regex | 256 | 67 | 2 | `system/core/Security.php` |
| events | 2 | 1 | 0 | `system/libraries/Xmlrpc.php` |
| tests | 1000 | 59 | 7 | `tests/codeigniter/libraries/Form_validation_test.php` |
| docs | 2745 | 252 | 21 | `system/database/DB_query_builder.php` |
| debt | 420 | 204 | 2 | `user_guide_src/Makefile` |
| mutation | 7958 | 293 | 58 | `system/database/DB_query_builder.php` |
| dead_code | 1431 | 207 | 10 | `system/database/DB_query_builder.php` |
| credential | 20 | 4 | 0 | `system/libraries/Profiler.php` |
| threat | 35 | 13 | 0 | `tests/codeigniter/libraries/Encryption_test.php` |
| ml_ai | 15 | 9 | 0 | `system/helpers/captcha_helper.php` |
| ui | 20 | 8 | 0 | `system/libraries/Xmlrpc.php` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.3333**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `system/core/Output.php` (Hits: 29)
- `tests/codeigniter/libraries/Form_validation_test.php` (Hits: 28)
- `system/core/Security.php` (Hits: 20)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Common.php** (`system/core/Common.php`) — 31 inbound connections
2. **skeleton.php** (`tests/mocks/database/schema/skeleton.php`) — 17 inbound connections
3. **mbstring.php** (`system/core/compat/mbstring.php`) — 12 inbound connections
4. **security.php** (`tests/mocks/core/security.php`) — 7 inbound connections
5. **Input.php** (`system/core/Input.php`) — 4 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **Loader.php** (`system/core/Loader.php`) — 24 outbound dependencies
2. **CodeIgniter.php** (`system/core/CodeIgniter.php`) — 13 outbound dependencies
3. **Bootstrap.php** (`tests/Bootstrap.php`) — 9 outbound dependencies
4. **DB.php** (`system/database/DB.php`) — 6 outbound dependencies
5. **test-phpunit.yml** (`.github/workflows/test-phpunit.yml`) — 5 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_execute` **(Many-Argument Workhorses)** (@ `system/libraries/Form_validation.php`) -> Impact: **135.3** | LOC: 202
  * *Intent:* // -------------------------------------------------------------------- /** * Executes the Validation routines * * @param array * @param array * @para...
- `create_captcha` **(Many-Argument Workhorses)** (@ `system/helpers/captcha_helper.php`) -> Impact: **92.4** | LOC: 321
  * *Intent:* /** * Create CAPTCHA * * @param array $data Data for the CAPTCHA * @return array */
- `set_cookie` **(Many-Argument Workhorses)** (@ `system/core/Input.php`) -> Impact: **89.8** | LOC: 88
  * *Intent:* * Accepts an arbitrary number of parameters (up to 7) or an associative * array in the first parameter containing all the values. * * @param string|mi...
- `closing_tag` **(Many-Argument Workhorses)** (@ `system/libraries/Xmlrpc.php`) -> Impact: **89.3** | LOC: 124
  * *Intent:* // -------------------------------------------------------------------- /** * End Element Handler * * @param string * @param string * @return void */
- `protect_identifiers` **(Many-Argument Workhorses)** (@ `system/database/DB_driver.php`) -> Impact: **84.2** | LOC: 164
  * *Intent:* * * SELECT m.member_id, m.member_name FROM members AS m * * Since the column name can include up to four segments (host, DB, table, column) * or also ...
- `do_upload` **(Compute Cores)** (@ `system/libraries/Upload.php`) -> Impact: **74.2** | LOC: 211
  * *Intent:* // -------------------------------------------------------------------- /** * Perform the file upload * * @param string $field * @return bool */
- `hash_pbkdf2` **(Many-Argument Workhorses)** (@ `system/core/compat/hash.php`) -> Impact: **70.1** | LOC: 132
  * *Intent:* /** * hash_pbkdf2() * * @link https://secure.php.net/hash_pbkdf2 * @param string $algo * @param string $password * @param string $salt * @param int $i...
- `generate` **(Many-Argument Workhorses)** (@ `system/libraries/Calendar.php`) -> Impact: **70.1** | LOC: 162
  * *Intent:* // -------------------------------------------------------------------- /** * Generate the calendar * * @param int the year * @param int the month * @...
- `open_tag` **(Compute Cores)** (@ `system/libraries/Xmlrpc.php`) -> Impact: **68.6** | LOC: 91
  * *Intent:* // params - used to store parameters in method calls // method - used to store method name // stack - array with parent tree of the xml element, // us...
- `create_links` **(I/O & Config Routines)** (@ `system/libraries/Pagination.php`) -> Impact: **62.9** | LOC: 258
  * *Intent:* // -------------------------------------------------------------------- /** * Generate the pagination links * * @return string */

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `system/libraries` | 21 | 9445.22 | 35.45% | 50.54% |
| `system/database` | 8 | 4131.16 | 33.01% | 61.02% |
| `system/core` | 18 | 4075.4 | 28.96% | 46.53% |
| `system/helpers` | 20 | 3396.3 | 30.59% | 0.56% |
| `system/database/drivers/pdo/subdrivers` | 25 | 2535.92 | 35.53% | 86.67% |
| `tests/codeigniter/libraries` | 10 | 804.96 | 7.51% | 0.0% |
| `system/libraries/Session/drivers` | 5 | 793.88 | 26.69% | 58.8% |
| `system/libraries/Session` | 7 | 759.58 | 9.6% | 50.85% |
| `tests/codeigniter/core` | 12 | 721.98 | 12.09% | 0.0% |
| `system/libraries/Cache/drivers` | 8 | 622.84 | 23.28% | 86.36% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `system/libraries/Cache/drivers/Cache_dummy.php` -> **100.0%** Exposure
- `system/libraries/Session/OldSessionWrapper.php` -> **100.0%** Exposure
- `system/libraries/Session/PHP8SessionWrapper.php` -> **100.0%** Exposure
- `system/libraries/Session/Session_driver.php` -> **100.0%** Exposure
- `system/database/drivers/mysql/mysql_driver.php` -> **99.9998%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `application/config/autoload.php` -> **100.0%** Exposure
- `application/config/config.php` -> **100.0%** Exposure
- `application/config/migration.php` -> **100.0%** Exposure
- `system/core/CodeIgniter.php` -> **100.0%** Exposure
- `system/core/Config.php` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `system/database/DB_query_builder.php` -> **46** Orphaned Functions | **0** Duplicates
- `tests/codeigniter/libraries/Form_validation_test.php` -> **46** Orphaned Functions | **0** Duplicates
- `system/libraries/Form_validation.php` -> **39** Orphaned Functions | **0** Duplicates
- `system/database/DB_driver.php` -> **28** Orphaned Functions | **0** Duplicates
- `tests/codeigniter/core/Loader_test.php` -> **24** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `97` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `system/database/DB_query_builder.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.347)
- **Top Global Matches:** file_cluster_15: 6.347, file_cluster_16: 6.355, file_cluster_11: 8.226
- **Magnitude:** 1777.08 | **LOC:** 2882 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (93.5%), Mutation Surface (formerly State Flux) (85.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_like` **(Many-Argument Workhorses)** (Impact: 53.0)
    * *Intent:* * * @used-by like() * @used-by or_like() * @used-by not_like() * @used-by or_not_like() * * @param m...
  * `_wh` **(Many-Argument Workhorses)** (Impact: 34.4)
    * *Intent:* * WHERE, HAVING * * @used-by where() * @used-by or_where() * @used-by having() * @used-by or_having(...
  * `delete` **(Many-Argument Workhorses)** (Impact: 34.0)
    * *Intent:* // -------------------------------------------------------------------- /** * Delete * * Compiles a ...
  * `update_batch` **(Many-Argument Workhorses)** (Impact: 33.9)
    * *Intent:* // -------------------------------------------------------------------- /** * Update_Batch * * Compi...
  * `join` **(Many-Argument Workhorses)** (Impact: 32.8)
    * *Intent:* // -------------------------------------------------------------------- /** * JOIN * * Generates the...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 301 instances
* *State Mutation (weighted view):* 996
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 255`, `structural_boundaries: 232`, `args: 84`, `func_start: 84`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 394`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 46`
* *Architecture:* `api: 57`
* *Defense:* `safety: 35`, `doc: 117`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.18
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `system/libraries/Email.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.672)
- **Top Global Matches:** file_cluster_4: 5.672, file_cluster_16: 7.967, file_cluster_15: 8.58
- **Magnitude:** 1373.28 | **LOC:** 2419 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.7%), Debt Markers (formerly Tech Debt) (45.3%)
- **Documentation Coverage:** 1.1111% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_send_command` **(Many-Argument Workhorses)** (Impact: 41.4)
    * *Intent:* // -------------------------------------------------------------------- /** * Send SMTP command * * ...
  * `_build_message` **(I/O & Config Routines)** (Impact: 36.3)
    * *Intent:* // -------------------------------------------------------------------- /** * Build Final Body and a...
  * `word_wrap` **(Many-Argument Workhorses)** (Impact: 31.8)
    * *Intent:* // -------------------------------------------------------------------- /** * Word Wrap * * @param s...
  * `send` **(Defensive Guards)** (Impact: 20.6)
    * *Intent:* // -------------------------------------------------------------------- /** * Send Email * * @param ...
  * `_prep_quoted_printable` **(I/O & Config Routines)** (Impact: 18.9)
    * *Intent:* // -------------------------------------------------------------------- /** * Prep Quoted Printable ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 245 instances
* *State Mutation (weighted view):* 800
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 249`, `structural_boundaries: 169`, `args: 64`, `func_start: 61`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 2`, `state_mutation: 310`, `fragile_debt: 2`, `unreferenced_by_name: 16`
* *Architecture:* `io: 4`, `api: 51`, `import: 7`
* *Defense:* `safety: 30`, `doc: 105`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.18
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `system/libraries/Xmlrpc.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.38)
- **Top Global Matches:** file_cluster_4: 5.38, file_cluster_6: 9.708, file_cluster_15: 11.386
- **Magnitude:** 1306.68 | **LOC:** 1920 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 4.032; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (45.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `closing_tag` **(Many-Argument Workhorses)** (Impact: 89.3)
    * *Intent:* // -------------------------------------------------------------------- /** * End Element Handler * ...
  * `open_tag` **(Compute Cores)** (Impact: 68.6)
    * *Intent:* // params - used to store parameters in method calls // method - used to store method name // stack ...
  * `serializedata` **(Compute Cores)** (Impact: 38.8)
    * *Intent:* // -------------------------------------------------------------------- /** * Serialize data * * @pa...
  * `parseResponse` **(Compute Cores)** (Impact: 33.6)
    * *Intent:* // -------------------------------------------------------------------- /** * Parse External XML-RPC...
  * `sendPayload` **(Compute Cores)** (Impact: 24.9)
    * *Intent:* // -------------------------------------------------------------------- /** * Send payload * * @para...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 221 instances
* *Memory Alloc (weighted view):* 19
* *State Mutation (weighted view):* 734
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 217`, `structural_boundaries: 138`, `args: 44`, `func_start: 43`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 1`, `state_mutation: 292`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 11`
* *Architecture:* `io: 4`, `api: 93`
* *Defense:* `safety: 12`, `doc: 99`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.032
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002976
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `system/libraries/Image_lib.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.734)
- **Top Global Matches:** file_cluster_8: 8.734, file_cluster_6: 8.996, file_cluster_4: 17.133
- **Magnitude:** 1104.32 | **LOC:** 1880 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.4%), Complexity Load (formerly Cognitive Load) (35.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `initialize` **(Compute Cores)** (Impact: 58.3)
    * *Intent:* // -------------------------------------------------------------------- /** * initialize image prefe...
  * `image_process_netpbm` **(Compute Cores)** (Impact: 42.2)
    * *Intent:* // -------------------------------------------------------------------- /** * Image Process Using Ne...
  * `text_watermark` **(I/O & Config Routines)** (Impact: 32.1)
    * *Intent:* // -------------------------------------------------------------------- /** * Watermark - Text Versi...
  * `image_save_gd` **(Compute Cores)** (Impact: 31.5)
    * *Intent:* // -------------------------------------------------------------------- /** * Write image file to di...
  * `image_process_gd` **(Compute Cores)** (Impact: 28.7)
    * *Intent:* // -------------------------------------------------------------------- /** * Image Process Using GD...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 184 instances
* *State Mutation (weighted view):* 633
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 224`, `structural_boundaries: 96`, `args: 41`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 3`, `state_mutation: 265`, `fragile_debt: 2`, `unreferenced_by_name: 8`
* *Architecture:* `io: 4`, `api: 68`
* *Defense:* `safety: 5`, `doc: 74`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.18
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `system/database/DB_driver.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.077)
- **Top Global Matches:** file_cluster_4: 7.077, file_cluster_15: 7.156, file_cluster_16: 7.562
- **Magnitude:** 969.84 | **LOC:** 1941 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 2.18; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (94.0%), Mutation Surface (formerly State Flux) (85.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `protect_identifiers` **(Many-Argument Workhorses)** (Impact: 84.2)
    * *Intent:* * * SELECT m.member_id, m.member_name FROM members AS m * * Since the column name can include up to ...
  * `query` **(Many-Argument Workhorses)** (Impact: 61.0)
    * *Intent:* /** * Execute the query * * Accepts an SQL string as input and returns a result object upon * succes...
  * `escape_identifiers` **(Many-Argument Workhorses)** (Impact: 23.4)
    * *Intent:* // -------------------------------------------------------------------- /** * Escape the SQL Identif...
  * `display_error` **(Many-Argument Workhorses)** (Impact: 22.2)
    * *Intent:* // -------------------------------------------------------------------- /** * Display an error messa...
  * `compile_binds` **(Many-Argument Workhorses)** (Impact: 20.1)
    * *Intent:* // -------------------------------------------------------------------- /** * Compile Bindings * * @...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 144 instances
* *Api Near Db Sink:* 1 instances
* *State Mutation (weighted view):* 475
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 161`, `structural_boundaries: 167`, `args: 57`, `func_start: 56`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 187`, `fragile_debt: 1`, `unreferenced_by_name: 28`
* *Architecture:* `io: 1`, `api: 77`, `import: 1`
* *Defense:* `safety: 20`, `doc: 98`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.18
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` DB_cache.php'
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `system/libraries/Form_validation.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.37)
- **Top Global Matches:** file_cluster_4: 6.37, file_cluster_15: 8.668, file_cluster_16: 9.611
- **Magnitude:** 870.26 | **LOC:** 1589 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 2.797; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_execute` **(Many-Argument Workhorses)** (Impact: 135.3)
    * *Intent:* // -------------------------------------------------------------------- /** * Executes the Validatio...
  * `set_rules` **(Many-Argument Workhorses)** (Impact: 44.6)
    * *Intent:* /** * Set Rules * * This function takes an array of field names and validation * rules as input, any...
  * `run` **(Defensive Guards)** (Impact: 33.5)
    * *Intent:* // -------------------------------------------------------------------- /** * Run the Validator * * ...
  * `_prepare_rules` **(Stateful Encapsulated Methods)** (Impact: 19.0)
    * *Intent:* /** * Prepare rules * * Re-orders the provided rules in order of importance, so that * they can easi...
  * `set_select` **(Many-Argument Workhorses)** (Impact: 17.4)
    * *Intent:* // -------------------------------------------------------------------- /** * Set Select * * Enables...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 107 instances
* *State Mutation (weighted view):* 341
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 179`, `structural_boundaries: 158`, `args: 55`, `func_start: 53`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 127`, `fragile_debt: 1`, `unreferenced_by_name: 39`
* *Architecture:* `io: 3`, `api: 47`
* *Defense:* `safety: 46`, `doc: 64`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.797
  * `Choke Point (Betweenness):` 1.3e-05 | `Ripple Effect (Closeness):` 0.002976
  * `Imports (Out-Degree: 2):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `system/core/Loader.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.861)
- **Top Global Matches:** file_cluster_6: 5.861, file_cluster_4: 7.307, file_cluster_15: 15.326
- **Magnitude:** 809.22 | **LOC:** 1435 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **24**; blast radius 11.723; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.0%), Debt Markers (formerly Tech Debt) (41.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `model` **(Many-Argument Workhorses)** (Impact: 58.5)
    * *Intent:* // -------------------------------------------------------------------- /** * Model Loader * * Loads...
  * `_ci_init_library` **(Many-Argument Workhorses)** (Impact: 40.2)
    * *Intent:* * Internal CI Library Instantiator * * @used-by CI_Loader::_ci_load_stock_library() * @used-by CI_Lo...
  * `_ci_load` **(Many-Argument Workhorses)** (Impact: 34.9)
    * *Intent:* /** * Internal CI Data Loader * * Used to load views and files. * * Variables are prefixed with _ci_...
  * `_ci_load_stock_library` **(Many-Argument Workhorses)** (Impact: 32.5)
    * *Intent:* // -------------------------------------------------------------------- /** * Internal CI Stock Libr...
  * `_ci_load_library` **(Many-Argument Workhorses)** (Impact: 32.0)
    * *Intent:* // -------------------------------------------------------------------- /** * Internal CI Library Lo...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 126 instances
* *State Mutation (weighted view):* 414
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 151`, `args: 29`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 162`, `planned_debt: 1`, `unreferenced_by_name: 10`
* *Architecture:* `api: 22`, `import: 25`
* *Defense:* `safety: 35`, `doc: 43`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.723
  * `Choke Point (Betweenness):` 8e-05 | `Ripple Effect (Closeness):` 0.027551
  * `Imports (Out-Degree: 1):` $_ci_path, $app_path.$class.'.php', $app_path.'Model.php', $base_helper, $driver_path, $filepath, '.$path.$model.'.php', $path...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `system/helpers/form_helper.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.624)
- **Top Global Matches:** file_cluster_4: 6.624, file_cluster_15: 6.893, file_cluster_9: 8.67
- **Magnitude:** 722.76 | **LOC:** 1037 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 4.032; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.4%), Complexity Load (formerly Cognitive Load) (38.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `form_dropdown` **(Many-Argument Workhorses)** (Impact: 46.5)
    * *Intent:* /** * Drop-down Menu * * @param mixed $data * @param mixed $options * @param mixed $selected * @para...
  * `form_open` **(Many-Argument Workhorses)** (Impact: 31.7)
    * *Intent:* /** * Form Declaration * * Creates the opening portion of the form. * * @param string the URI segmen...
  * `set_checkbox` **(Many-Argument Workhorses)** (Impact: 21.8)
    * *Intent:* /** * Set Checkbox * * Let's you set the selected value of a checkbox via the value in the POST arra...
  * `set_radio` **(Many-Argument Workhorses)** (Impact: 21.8)
    * *Intent:* /** * Set Radio * * Let's you set the selected value of a radio field via info in the POST array. * ...
  * `set_select` **(Many-Argument Workhorses)** (Impact: 21.5)
    * *Intent:* /** * Set Select * * Let's you set the selected value of a <select> menu via data in the POST array....
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 133 instances
* *State Mutation (weighted view):* 417
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 135`, `structural_boundaries: 86`, `args: 54`, `func_start: 27`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 151`
* *Architecture:* `io: 4`
* *Defense:* `safety: 16`, `doc: 29`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.032
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.002976
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `system/libraries/Upload.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.58)
- **Top Global Matches:** file_cluster_4: 7.58, file_cluster_6: 9.862, file_cluster_12: 12.233
- **Magnitude:** 703.42 | **LOC:** 1326 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 3.106; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.1%), Debt Markers (formerly Tech Debt) (75.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `do_upload` **(Compute Cores)** (Impact: 74.2)
    * *Intent:* // -------------------------------------------------------------------- /** * Perform the file uploa...
  * `_file_mime_type` **(Compute Cores)** (Impact: 32.3)
    * *Intent:* // -------------------------------------------------------------------- /** * File MIME type * * Det...
  * `initialize` **(Many-Argument Workhorses)** (Impact: 28.7)
    * *Intent:* // -------------------------------------------------------------------- /** * Initialize preferences...
  * `do_xss_clean` **(I/O & Config Routines)** (Impact: 21.2)
    * *Intent:* // -------------------------------------------------------------------- /** * Runs the file through ...
  * `is_allowed_filetype` **(Defensive Guards)** (Impact: 14.7)
    * *Intent:* // -------------------------------------------------------------------- /** * Verify that the filety...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 106 instances
* *State Mutation (weighted view):* 361
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 144`, `structural_boundaries: 98`, `args: 36`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `high_risk_execution: 4`, `state_mutation: 149`, `fragile_debt: 2`, `unreferenced_by_name: 12`
* *Architecture:* `io: 7`, `api: 55`
* *Defense:* `safety: 12`, `doc: 64`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.106
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.002976
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `system/database/DB_forge.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.224)
- **Top Global Matches:** file_cluster_4: 7.224, file_cluster_9: 8.027, file_cluster_16: 8.381
- **Magnitude:** 614.42 | **LOC:** 1039 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (85.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.5%), Complexity Load (formerly Cognitive Load) (36.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_process_fields` **(Defensive Guards)** (Impact: 45.7)
    * *Intent:* // -------------------------------------------------------------------- /** * Process fields * * @pa...
  * `create_table` **(Many-Argument Workhorses)** (Impact: 24.4)
    * *Intent:* // -------------------------------------------------------------------- /** * Create Table * * @para...
  * `_create_table` **(Many-Argument Workhorses)** (Impact: 18.1)
    * *Intent:* // -------------------------------------------------------------------- /** * Create Table * * @para...
  * `_attr_default` **(Stateful Encapsulated Methods)** (Impact: 17.3)
    * *Intent:* // -------------------------------------------------------------------- /** * Field attribute DEFAUL...
  * `_attr_unsigned` **(Stateful Encapsulated Methods)** (Impact: 17.1)
    * *Intent:* * * Depending on the _unsigned property value: * * - TRUE will always set $field['unsigned'] to 'UNS...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 94 instances
* *State Mutation (weighted view):* 301
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 76`, `args: 25`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 113`, `unreferenced_by_name: 8`
* *Architecture:* `api: 15`
* *Defense:* `safety: 27`, `doc: 42`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.18
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `system/libraries/Session/Session.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.653)
- **Top Global Matches:** file_cluster_4: 6.653, file_cluster_15: 10.149, file_cluster_9: 10.86
- **Magnitude:** 569.38 | **LOC:** 1031 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 2.18; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.7%), Debt Markers (formerly Tech Debt) (56.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__construct` **(Compute Cores)** (Impact: 40.0)
    * *Intent:* // ------------------------------------------------------------------------ /** * Class constructor ...
  * `_configure` **(Defensive Guards)** (Impact: 27.1)
    * *Intent:* // ------------------------------------------------------------------------ /** * Configuration * * ...
  * `_ci_load_classes` **(Compute Cores)** (Impact: 24.4)
    * *Intent:* // ------------------------------------------------------------------------ /** * CI Load Classes * ...
  * `_configure_sid_length` **(I/O & Config Routines)** (Impact: 17.8)
    * *Intent:* * Configure session ID length * * To make life easier, we used to force SHA-1 and 4 bits per * chara...
  * `mark_as_temp` **(Defensive Guards)** (Impact: 16.1)
    * *Intent:* // ------------------------------------------------------------------------ /** * Mark as temp * * @...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 95 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 292
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 92`, `args: 28`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 102`, `unreferenced_by_name: 16`
* *Architecture:* `io: 14`, `api: 25`, `import: 8`
* *Defense:* `safety: 49`, `doc: 31`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.18
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` $file_path, '.$wrapper.'.php', CI_Session_driver_interface.php'
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `system/core/Input.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.304)
- **Top Global Matches:** file_cluster_4: 6.304, file_cluster_6: 8.288, file_cluster_15: 12.974
- **Magnitude:** 513.16 | **LOC:** 705 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); blast radius 4.958; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.6%), Debt Markers (formerly Tech Debt) (58.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `set_cookie` **(Many-Argument Workhorses)** (Impact: 89.8)
    * *Intent:* * Accepts an arbitrary number of parameters (up to 7) or an associative * array in the first paramet...
  * `ip_address` **(I/O & Config Routines)** (Impact: 35.4)
    * *Intent:* // -------------------------------------------------------------------- /** * Fetch the IP Address *...
  * `_fetch_from_array` **(Many-Argument Workhorses)** (Impact: 26.6)
    * *Intent:* // -------------------------------------------------------------------- /** * Fetch from array * * I...
  * `valid_ip` **(Compute Cores)** (Impact: 14.7)
    * *Intent:* // -------------------------------------------------------------------- /** * Validate IP Address * ...
  * `get_request_header` **(Defensive Guards)** (Impact: 11.6)
    * *Intent:* // -------------------------------------------------------------------- /** * Get Request Header * *...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 85 instances
* *State Mutation (weighted view):* 267
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 49`, `args: 19`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 97`, `dead_code: 1`, `unreferenced_by_name: 10`
* *Architecture:* `io: 14`, `api: 17`
* *Defense:* `safety: 18`, `doc: 25`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.958
  * `Choke Point (Betweenness):` 3.1e-05 | `Ripple Effect (Closeness):` 0.011905
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `system/libraries/Encryption.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.567)
- **Top Global Matches:** file_cluster_16: 6.567, file_cluster_9: 7.485, file_cluster_15: 8.101
- **Magnitude:** 485.58 | **LOC:** 940 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (85.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_get_params` **(Defensive Guards)** (Impact: 24.9)
    * *Intent:* // -------------------------------------------------------------------- /** * Get params * * @param ...
  * `_mcrypt_decrypt` **(Many-Argument Workhorses)** (Impact: 19.9)
    * *Intent:* // -------------------------------------------------------------------- /** * Decrypt via MCrypt * *...
  * `_mcrypt_initialize` **(Stateful Encapsulated Methods)** (Impact: 19.5)
    * *Intent:* // -------------------------------------------------------------------- /** * Initialize MCrypt * * ...
  * `_mcrypt_encrypt` **(Many-Argument Workhorses)** (Impact: 16.6)
    * *Intent:* // -------------------------------------------------------------------- /** * Encrypt via MCrypt * *...
  * `decrypt` **(Many-Argument Workhorses)** (Impact: 16.3)
    * *Intent:* // -------------------------------------------------------------------- /** * Decrypt * * @param str...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 83 instances
* *State Mutation (weighted view):* 257
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 60`, `args: 20`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 91`, `fragile_debt: 2`, `unreferenced_by_name: 12`
* *Architecture:* `api: 7`
* *Defense:* `safety: 42`, `doc: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.18
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `system/core/Output.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.285)
- **Top Global Matches:** file_cluster_4: 7.285, file_cluster_12: 8.039, file_cluster_15: 10.021
- **Magnitude:** 454.08 | **LOC:** 845 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.1%), Debt Markers (formerly Tech Debt) (67.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_display` **(I/O & Config Routines)** (Impact: 39.0)
    * *Intent:* /** * Display Output * * Processes and sends finalized output data to the browser along * with any s...
  * `_write_cache` **(Compute Cores)** (Impact: 25.7)
    * *Intent:* // -------------------------------------------------------------------- /** * Write Cache * * @param...
  * `_display_cache` **(Many-Argument Workhorses)** (Impact: 24.1)
    * *Intent:* // -------------------------------------------------------------------- /** * Update/serve cached ou...
  * `delete_cache` **(Compute Cores)** (Impact: 14.8)
    * *Intent:* // -------------------------------------------------------------------- /** * Delete cache * * @para...
  * `set_content_type` **(Defensive Guards)** (Impact: 11.9)
    * *Intent:* // -------------------------------------------------------------------- /** * Set Content-Type Heade...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 79 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 252
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 55`, `args: 20`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 2`, `state_mutation: 94`, `planned_debt: 1`, `unreferenced_by_name: 8`
* *Architecture:* `io: 29`, `api: 23`
* *Defense:* `safety: 19`, `doc: 32`, `sync_locks: 5`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.18
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `system/core/Security.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.789)
- **Top Global Matches:** file_cluster_4: 6.789, file_cluster_16: 7.973, file_cluster_15: 8.739
- **Magnitude:** 427.1 | **LOC:** 1089 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.2%), Complexity Load (formerly Cognitive Load) (32.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `xss_clean` **(Many-Argument Workhorses)** (Impact: 40.5)
    * *Intent:* * runtime processing. * * @link http://channel.bitflux.ch/wiki/XSS_Prevention * Based in part on som...
  * `_sanitize_naughty_html` **(Compute Cores)** (Impact: 19.5)
    * *Intent:* // -------------------------------------------------------------------- /** * Sanitize Naughty HTML ...
  * `get_random_bytes` **(Defensive Guards)** (Impact: 15.1)
    * *Intent:* // -------------------------------------------------------------------- /** * Get random bytes * * @...
  * `entity_decode` **(Many-Argument Workhorses)** (Impact: 14.2)
    * *Intent:* * A replacement for html_entity_decode() * * The reason we are not using html_entity_decode() by its...
  * `csrf_verify` **(I/O & Config Routines)** (Impact: 13.4)
    * *Intent:* // -------------------------------------------------------------------- /** * CSRF Verify * * @retur...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 74 instances
* *State Mutation (weighted view):* 235
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 66`, `args: 24`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 87`, `dead_code: 1`, `unreferenced_by_name: 6`
* *Architecture:* `io: 20`, `api: 14`
* *Defense:* `safety: 11`, `doc: 33`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.18
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `system/helpers/date_helper.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.651)
- **Top Global Matches:** file_cluster_4: 6.651, file_cluster_12: 10.685, file_cluster_6: 10.962
- **Magnitude:** 421.02 | **LOC:** 638 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 7.46; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.2%), Complexity Load (formerly Cognitive Load) (45.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `timespan` **(Many-Argument Workhorses)** (Impact: 56.4)
    * *Intent:* /** * Timespan * * Returns a span of seconds in this format: * 10 days 14 hours 36 minutes 47 second...
  * `date_range` **(Many-Argument Workhorses)** (Impact: 31.8)
    * *Intent:* * Date range * * Returns a list of dates within a specified period. * * @param int unix_start UNIX t...
  * `days_in_month` **(Compute Cores)** (Impact: 15.5)
    * *Intent:* /** * Number of days in a month * * Takes a month/year as input and returns the number of days * for...
  * `human_to_unix` **(Defensive Guards)** (Impact: 13.0)
    * *Intent:* /** * Convert "human" date to GMT * * Reverses the above process * * @param string format: us or eur...
  * `timezone_menu` **(Many-Argument Workhorses)** (Impact: 12.4)
    * *Intent:* /** * Timezone Menu * * Generates a drop-down menu of timezones. * * @param string timezone * @param...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 78 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 243
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 47`, `args: 24`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 1`, `state_mutation: 87`, `fragile_debt: 1`
* *Architecture:* None
* *Defense:* `safety: 5`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.46
  * `Choke Point (Betweenness):` 2.7e-05 | `Ripple Effect (Closeness):` 0.006696
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `system/helpers/url_helper.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.599)
- **Top Global Matches:** file_cluster_6: 6.599, file_cluster_4: 9.483, file_cluster_8: 16.41
- **Magnitude:** 411.64 | **LOC:** 560 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 4.032; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (38.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `safe_mailto` **(Many-Argument Workhorses)** (Impact: 38.7)
    * *Intent:* /** * Encoded Mailto Link * * Create a spam-protected mailto link written in Javascript * * @param s...
  * `redirect` **(Many-Argument Workhorses)** (Impact: 33.9)
    * *Intent:* /** * Header Redirect * * Header redirect in two flavors * For very fine grained control over header...
  * `auto_link` **(Many-Argument Workhorses)** (Impact: 21.9)
    * *Intent:* /** * Auto-linker * * Automatically links URL and Email addresses. * Note: There's a bit of extra co...
  * `anchor_popup` **(Many-Argument Workhorses)** (Impact: 20.2)
    * *Intent:* /** * Anchor Link - Pop-up version * * Creates an anchor based on the local URL. The link * opens a ...
  * `anchor` **(Many-Argument Workhorses)** (Impact: 11.0)
    * *Intent:* /** * Anchor Link * * Creates an anchor based on the local URL. * * @param string the URL * @param s...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 80 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 254
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 36`, `args: 26`, `func_start: 13`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 94`, `dead_code: 2`
* *Architecture:* `io: 2`
* *Defense:* `safety: 6`, `doc: 15`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.032
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.002976
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `system/libraries/Xmlrpcs.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.429)
- **Top Global Matches:** file_cluster_4: 6.429, file_cluster_15: 9.852, file_cluster_11: 10.794
- **Magnitude:** 408.5 | **LOC:** 621 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (35.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_execute` **(Compute Cores)** (Impact: 30.2)
    * *Intent:* // -------------------------------------------------------------------- /** * Executes the Method * ...
  * `parseRequest` **(Compute Cores)** (Impact: 18.7)
    * *Intent:* // -------------------------------------------------------------------- /** * Parse Server Request *...
  * `do_multicall` **(Compute Cores)** (Impact: 16.5)
    * *Intent:* // -------------------------------------------------------------------- /** * Multi-call Function: P...
  * `initialize` **(Defensive Guards)** (Impact: 11.0)
    * *Intent:* // -------------------------------------------------------------------- /** * Initialize Prefs and S...
  * `methodSignature` **(Compute Cores)** (Impact: 8.6)
    * *Intent:* // -------------------------------------------------------------------- /** * Server Function: Retur...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 86 instances
* *State Mutation (weighted view):* 268
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 92`, `args: 14`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 96`, `unreferenced_by_name: 5`
* *Architecture:* `io: 2`, `api: 16`
* *Defense:* `safety: 11`, `doc: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.18
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `system/libraries/Calendar.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.457)
- **Top Global Matches:** file_cluster_4: 7.457, file_cluster_6: 9.052, file_cluster_12: 12.766
- **Magnitude:** 390.38 | **LOC:** 548 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 4.032; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (34.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generate` **(Many-Argument Workhorses)** (Impact: 70.1)
    * *Intent:* // -------------------------------------------------------------------- /** * Generate the calendar ...
  * `get_day_names` **(Compute Cores)** (Impact: 11.3)
    * *Intent:* // -------------------------------------------------------------------- /** * Get Day Names * * Retu...
  * `parse_template` **(I/O & Config Routines)** (Impact: 8.6)
    * *Intent:* // -------------------------------------------------------------------- /** * Parse Template * * Har...
  * `adjust_date` **(Compute Cores)** (Impact: 8.2)
    * *Intent:* // -------------------------------------------------------------------- /** * Adjust Date * * This f...
  * `initialize` **(Defensive Guards)** (Impact: 8.0)
    * *Intent:* // -------------------------------------------------------------------- /** * Initialize the user pr...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 77 instances
* *State Mutation (weighted view):* 249
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 21`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 1`, `state_mutation: 95`, `unreferenced_by_name: 2`
* *Architecture:* `api: 17`
* *Defense:* `safety: 8`, `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.032
  * `Choke Point (Betweenness):` 1.8e-05 | `Ripple Effect (Closeness):` 0.002976
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `system/helpers/text_helper.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.181)
- **Top Global Matches:** file_cluster_9: 6.181, file_cluster_15: 7.727, file_cluster_16: 8.427
- **Magnitude:** 373.6 | **LOC:** 569 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 5.885; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (44.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `word_wrap` **(Many-Argument Workhorses)** (Impact: 28.2)
    * *Intent:* /** * Word Wrap * * Wraps text at the specified character. Maintains the integrity of words. * Anyth...
  * `ascii_to_entities` **(Compute Cores)** (Impact: 18.2)
    * *Intent:* /** * High ASCII to Entities * * Converts high ASCII text and MS Word special characters to characte...
  * `word_censor` **(Many-Argument Workhorses)** (Impact: 14.2)
    * *Intent:* /** * Word Censoring Function * * Supply a string and an array of disallowed words and any * matched...
  * `entities_to_ascii` **(Compute Cores)** (Impact: 14.1)
    * *Intent:* /** * Entities to ASCII * * Converts character entities back to ASCII * * @param string * @param boo...
  * `character_limiter` **(Many-Argument Workhorses)** (Impact: 13.3)
    * *Intent:* /** * Character Limiter * * Limits the string based on the character count. Preserves complete words...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 78 instances
* *State Mutation (weighted view):* 239
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 33`, `args: 20`, `func_start: 10`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 83`
* *Architecture:* `import: 2`
* *Defense:* `safety: 1`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.885
  * `Choke Point (Betweenness):` 1.8e-05 | `Ripple Effect (Closeness):` 0.005952
  * `Imports (Out-Degree: 1):` foreign_chars.php', foreign_chars.php'
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `system/core/URI.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.356)
- **Top Global Matches:** file_cluster_12: 6.356, file_cluster_15: 7.259, file_cluster_16: 7.526
- **Magnitude:** 360.28 | **LOC:** 663 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.5%), Debt Markers (formerly Tech Debt) (66.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_uri_to_assoc` **(Many-Argument Workhorses)** (Impact: 24.9)
    * *Intent:* // -------------------------------------------------------------------- /** * Internal URI-to-assoc ...
  * `__construct` **(Compute Cores)** (Impact: 21.7)
    * *Intent:* /** * Class constructor * * @return void */
  * `_set_uri_string` **(Many-Argument Workhorses)** (Impact: 20.2)
    * *Intent:* // -------------------------------------------------------------------- /** * Set URI String * * @pa...
  * `_parse_request_uri` **(I/O & Config Routines)** (Impact: 14.4)
    * *Intent:* // -------------------------------------------------------------------- /** * Parse REQUEST_URI * * ...
  * `filter_uri` **(Defensive Guards)** (Impact: 7.4)
    * *Intent:* // -------------------------------------------------------------------- /** * Filter URI * * Filters...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 63 instances
* *State Mutation (weighted view):* 200
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 56`, `args: 22`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 74`, `unreferenced_by_name: 9`
* *Architecture:* `io: 2`, `api: 19`
* *Defense:* `safety: 16`, `doc: 29`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.18
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `system/core/Common.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.663)
- **Top Global Matches:** file_cluster_12: 6.663, file_cluster_15: 6.741, file_cluster_11: 8.473
- **Magnitude:** 332.66 | **LOC:** 854 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **31** in-repo importer(s); it depends on **4**; blast radius 63.076; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.5%), Complexity Load (formerly Cognitive Load) (34.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `load_class` **(Many-Argument Workhorses)** (Impact: 22.9)
    * *Intent:* /** * Class registry * * This function acts as a singleton. If the requested class does not * exist ...
  * `set_status_header` **(Many-Argument Workhorses)** (Impact: 20.2)
    * *Intent:* /** * Set HTTP Status Header * * @param int the status code * @param string * @return void */
  * `_error_handler` **(Many-Argument Workhorses)** (Impact: 13.1)
    * *Intent:* * This is the custom error handler that is declared at the (relative) * top of CodeIgniter.php. The ...
  * `get_config` **(Defensive Guards)** (Impact: 12.0)
    * *Intent:* /** * Loads the main config.php file * * This function lets us grab the config file even if the Conf...
  * `_stringify_attributes` **(Defensive Guards)** (Impact: 9.8)
    * *Intent:* /** * Stringify attributes for use in HTML tags. * * Helper function used to convert a string, array...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Amplified Cascading Flux:* 55 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 169
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 62`, `args: 41`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 8`, `state_mutation: 59`, `fragile_debt: 2`
* *Architecture:* `io: 4`, `import: 6`
* *Defense:* `safety: 20`, `doc: 22`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 63.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.099343
  * `Imports (Out-Degree: 0):` $file_path, '.$class.'.php', '.$name.'.php', mimes.php')
  * `Imported By (In-Degree: 31):` (Excluded from Brief to save tokens)

### `system/helpers/file_helper.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.867)
- **Top Global Matches:** file_cluster_8: 8.867, file_cluster_6: 10.627, file_cluster_4: 18.747
- **Magnitude:** 330.44 | **LOC:** 436 | **CtrlFlow:** 35.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); blast radius 6.147; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (48.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_file_info` **(Compute Cores)** (Impact: 38.6)
    * *Intent:* /** * Get File Info * * Given a file and path, returns the name, path, size, date modified * Second ...
  * `symbolic_permissions` **(Compute Cores)** (Impact: 36.5)
    * *Intent:* /** * Symbolic Permissions * * Takes a numeric value representing a file's permissions and returns *...
  * `delete_files` **(Many-Argument Workhorses)** (Impact: 26.2)
    * *Intent:* /** * Delete Files * * Deletes all files contained in the supplied directory path. * Files must be w...
  * `get_dir_file_info` **(Many-Argument Workhorses)** (Impact: 17.8)
    * *Intent:* /** * Get Directory File Information * * Reads the specified directory and builds an array containin...
  * `get_filenames` **(Many-Argument Workhorses)** (Impact: 17.6)
    * *Intent:* /** * Get Filenames * * Reads the specified directory and builds an array containing the filenames. ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 56 instances
* *State Mutation (weighted view):* 168
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 24`, `args: 16`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 1`, `state_mutation: 56`
* *Architecture:* `io: 2`
* *Defense:* `safety: 2`, `doc: 10`, `sync_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.147
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.009524
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `system/libraries/Pagination.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.733)
- **Top Global Matches:** file_cluster_6: 6.733, file_cluster_8: 12.261, file_cluster_4: 13.472
- **Magnitude:** 327.06 | **LOC:** 698 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (35.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create_links` **(I/O & Config Routines)** (Impact: 62.9)
    * *Intent:* // -------------------------------------------------------------------- /** * Generate the paginatio...
  * `initialize` **(Compute Cores)** (Impact: 11.3)
    * *Intent:* // -------------------------------------------------------------------- /** * Initialize Preferences...
  * `__construct` **(Defensive Guards)** (Impact: 5.2)
    * *Intent:* // -------------------------------------------------------------------- /** * Constructor * * @param...
  * `_parse_attributes` **(Stateful Encapsulated Methods)** (Impact: 4.9)
    * *Intent:* // -------------------------------------------------------------------- /** * Parse attributes * * @...
  * `_attr_rel` **(Stateful Encapsulated Methods)** (Impact: 3.3)
    * *Intent:* // -------------------------------------------------------------------- /** * Add "rel" attribute * ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 63 instances
* *State Mutation (weighted view):* 229
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 15`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 103`, `unreferenced_by_name: 2`
* *Architecture:* `api: 5`
* *Defense:* `safety: 7`, `doc: 44`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.18
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `system/database/DB_result.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.565)
- **Top Global Matches:** file_cluster_15: 5.565, file_cluster_11: 6.514, file_cluster_16: 7.102
- **Magnitude:** 319.22 | **LOC:** 667 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 2.797; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (85.0%), Debt Markers (formerly Tech Debt) (80.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `custom_result_object` **(Compute Cores)** (Impact: 15.1)
    * *Intent:* // -------------------------------------------------------------------- /** * Custom query result. *...
  * `set_row` **(Compute Cores)** (Impact: 11.5)
    * *Intent:* // -------------------------------------------------------------------- /** * Assigns an item into a...
  * `row` **(Defensive Guards)** (Impact: 9.7)
    * *Intent:* // -------------------------------------------------------------------- /** * Row * * A wrapper meth...
  * `result_object` **(I/O & Config Routines)** (Impact: 7.7)
    * *Intent:* // -------------------------------------------------------------------- /** * Query result. "object"...
  * `result_array` **(I/O & Config Routines)** (Impact: 7.7)
    * *Intent:* // -------------------------------------------------------------------- /** * Query result. "array" ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 54 instances
* *State Mutation (weighted view):* 171
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 74`, `args: 23`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 63`, `unreferenced_by_name: 11`
* *Architecture:* `api: 29`
* *Defense:* `safety: 11`, `doc: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.797
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002976
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `system/libraries/Session/PHP8SessionWrapper.php` (PHP) | Magnitude: 25.96 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 39, structural_boundaries: 19, args: 9, func_start: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `system/core/Common.php` (PHP) | Magnitude: 332.66 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 386, branch: 83, structural_boundaries: 62, state_mutation: 59
- `system/database/drivers/pdo/subdrivers/pdo_sqlite_forge.php` (PHP) | Magnitude: 76.84 | Delta: **0.128** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 78, structural_boundaries: 18, branch: 15, state_mutation: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `system/database/DB_query_builder.php` (PHP) | Magnitude: 1777.08 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 1345, state_mutation: 394, branch: 255, structural_boundaries: 232
- `system/helpers/xml_helper.php` (PHP) | Magnitude: 25.1 | Delta: **0.125** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 20, state_mutation: 6, bitwise_ops: 5, regex_execution: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `tests/codeigniter/core/compat/password_test.php` (PHP) | Magnitude: 29.6 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 82, test: 30, args: 10, structural_boundaries: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `system/database/DB_driver.php` (PHP) | Magnitude: 969.84 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 838, state_mutation: 187, structural_boundaries: 167, branch: 161

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `tests/mocks/database/schema/skeleton.php` -> **Severity: 0.053** (Bridge: 0.0008 * Flux: 70.7216%)
- `tests/mocks/database/db.php` -> **Severity: 0.011** (Bridge: 0.0001 * Flux: 85.0%)
- `system/core/Loader.php` -> **Severity: 0.008** (Bridge: 0.0001 * Flux: 100.0%)
- `system/core/Input.php` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 100.0%)
- `system/helpers/date_helper.php` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `system/core/Common.php` -> **Severity: 6.608** (Embedded: 0.0993 * Error Risk: 66.5149%)
- `tests/mocks/database/schema/skeleton.php` -> **Severity: 2.874** (Embedded: 0.0506 * Error Risk: 56.8037%)
- `tests/mocks/ci_testcase.php` -> **Severity: 2.771** (Embedded: 0.039 * Error Risk: 71.1186%)
- `system/core/compat/mbstring.php` -> **Severity: 2.272** (Embedded: 0.0413 * Error Risk: 54.9834%)
- `tests/mocks/database/db.php` -> **Severity: 2.088** (Embedded: 0.0322 * Error Risk: 64.9102%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tests/mocks/ci_testconfig.php` -> **Severity: 2165.4** (Blast Radius: 21.654 * Doc Risk: 100.0%)
- `tests/mocks/ci_testcase.php` -> **Severity: 1340.898** (Blast Radius: 22.907 * Doc Risk: 58.5366%)
- `tests/mocks/core/security.php` -> **Severity: 866.4** (Blast Radius: 8.664 * Doc Risk: 100.0%)
- `tests/mocks/core/uri.php` -> **Severity: 403.2** (Blast Radius: 4.032 * Doc Risk: 100.0%)
- `tests/mocks/libraries/table.php` -> **Severity: 403.2** (Blast Radius: 4.032 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 6694 call pairs -- scoped 13.0%, unique 3.8%, ambiguous 23.6%, external 59.6%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| php | 6684 | 13.0% | 3.8% | 23.7% | 59.5% |
| shell | 8 | 0.0% | 0.0% | 0.0% | 100.0% |
| python | 2 | 0.0% | 0.0% | 0.0% | 100.0% |

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
