# ARCHITECTURAL_BRIEF: CodeIgniter
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/bcit-ci/CodeIgniter.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 237 analyzed artifact(s), 20218 LOC.
- **Load-bearing artifact:** `system/database/DB.php` -- 1 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `system/core/Loader.php` -- pulls in 53 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `system/database/DB_query_builder.php` at magnitude 1807.88 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 237 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 319 |
| Total LOC | 20218 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 42.6% |
| Dominant Lang | PHP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PHP | 174 | 19115 | 73.4% |
| HTML | 41 | 774 | 17.3% |
| XML | 9 | 0 | 3.8% |
| PYTHON | 4 | 35 | 1.7% |
| MARKDOWN | 3 | 0 | 1.3% |
| PLAINTEXT | 2 | 0 | 0.8% |
| JAVASCRIPT | 2 | 154 | 0.8% |
| JSON | 1 | 35 | 0.4% |
| MAKEFILE | 1 | 105 | 0.4% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Mid Flat Project`
> **Architectural Drift Z-Score:** `2.35`
> **Composition Archetype:** `Mid Flat Project` (z +2.35; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 30%, Declarative / Non-Code 19%, Encapsulated Accessors Files 15%, Large Core Modules (3) 11%, Large Core Modules (2) 5%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 232 | 97.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 5 | 2.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 319*

**Composition by Extension & Reason:**
- `.rst`: 142x Excluded (Unsupported Extension: '.rst'), 30x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.php`: 106x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 476 LOC), 1x Excluded (Saturation: Line 98 exceeds 500 chars)
- `.html`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 15 exceeds 500 chars)
- `no_extension`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gif`: 5x Excluded (Explicitly Denied Extension: '.gif')
- `.css`: 2x Excluded (Saturation: Line 1 exceeds 500 chars), 1x Excluded (Saturation: Line 17 exceeds 500 chars)
- `.ttf`: 2x Excluded (Explicitly Denied Extension: '.ttf')
- `.ico`: 2x Excluded (Explicitly Denied Extension: '.ico')
- `.jpg`: 2x Excluded (Explicitly Denied Extension: '.jpg')
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.otf`: 1x Excluded (Explicitly Denied Extension: '.otf')
- `.eot`: 1x Excluded (Explicitly Denied Extension: '.eot')
- `.woff`: 1x Excluded (Explicitly Denied Extension: '.woff')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 66.8 | 17.9 | 8.5 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.6 | 63.0 | 79.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 32.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 16.1 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 15.0 | 1.7 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 52.1 | 85.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 18.4 | 0.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 4.0 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 167 | 58 | 2 | `system/database/DB_query_builder.php` |
| cleanup | 62 | 32 | 1 | `system/helpers/form_helper.php` |
| guards | 1338 | 118 | 18 | `system/database/DB_query_builder.php` |
| danger | 474 | 161 | 4 | `system/core/Common.php` |
| concurrency | 12 | 5 | 0 | `system/core/Output.php` |
| connectivity | 1035 | 87 | 9 | `user_guide_src/source/_themes/sphinx_rtd_theme/layout_old.html` |
| io | 238 | 37 | 2 | `system/core/Output.php` |
| crypto | 0 | 0 | 0 | - |
| ipc | 17 | 5 | 0 | `system/core/Security.php` |
| time | 35 | 7 | 0 | `system/helpers/date_helper.php` |
| serialization | 4 | 2 | 0 | `system/core/Output.php` |
| regex | 155 | 47 | 2 | `system/core/Security.php` |
| events | 20 | 4 | 0 | `user_guide_src/source/_themes/sphinx_rtd_theme/static/js/theme.js` |
| tests | 4 | 2 | 0 | `tests/Bootstrap.php` |
| docs | 1671 | 182 | 17 | `system/database/DB_query_builder.php` |
| debt | 286 | 156 | 2 | `user_guide_src/Makefile` |
| mutation | 4697 | 203 | 50 | `system/database/DB_query_builder.php` |
| dead_code | 683 | 110 | 8 | `system/database/DB_query_builder.php` |
| credential | 5 | 4 | 0 | `system/core/Security.php` |
| threat | 27 | 15 | 0 | `system/database/DB_query_builder.php` |
| ml_ai | 9 | 5 | 0 | `system/helpers/captcha_helper.php` |
| ui | 8 | 5 | 0 | `system/helpers/text_helper.php` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `system/core/Output.php` (Hits: 29)
- `user_guide_src/source/_themes/sphinx_rtd_theme/layout_old.html` (Hits: 28)
- `system/core/Security.php` (Hits: 20)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **DB.php** (`system/database/DB.php`) — 1 inbound connections
2. **DCO.txt** (`DCO.txt`) — 0 inbound connections
3. **license.txt** (`license.txt`) — 0 inbound connections
4. **autoload.php** (`application/config/autoload.php`) — 0 inbound connections
5. **constants.php** (`application/config/constants.php`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **Loader.php** (`system/core/Loader.php`) — 53 outbound dependencies
2. **Common.php** (`system/core/Common.php`) — 49 outbound dependencies
3. **CodeIgniter.php** (`system/core/CodeIgniter.php`) — 31 outbound dependencies
4. **DB_query_builder.php** (`system/database/DB_query_builder.php`) — 28 outbound dependencies
5. **DB_driver.php** (`system/database/DB_driver.php`) — 26 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `protect_identifiers` **(Many-Argument Workhorses)** (@ `system/database/DB_driver.php`) -> Impact: **95.4** | LOC: 164
  * *Intent:* * * SELECT m.member_id, m.member_name FROM members AS m * * Since the column name can include up to four segments (host, DB, table, column) * or also ...
- `create_captcha` **(Many-Argument Workhorses)** (@ `system/helpers/captcha_helper.php`) -> Impact: **93.8** | LOC: 321
  * *Intent:* /** * Create CAPTCHA * * @param array $data Data for the CAPTCHA * @return array */
- `set_cookie` **(Many-Argument Workhorses)** (@ `system/core/Input.php`) -> Impact: **89.8** | LOC: 88
  * *Intent:* * Accepts an arbitrary number of parameters (up to 7) or an associative * array in the first parameter containing all the values. * * @param string|mi...
- `xss_clean` **(Many-Argument Workhorses)** (@ `system/core/Security.php`) -> Impact: **89.0** | LOC: 222
  * *Intent:* * runtime processing. * * @link http://channel.bitflux.ch/wiki/XSS_Prevention * Based in part on some code and ideas from Bitflux. * * @link http://ha...
- `hash_pbkdf2` **(Many-Argument Workhorses)** (@ `system/core/compat/hash.php`) -> Impact: **70.1** | LOC: 132
  * *Intent:* /** * hash_pbkdf2() * * @link https://secure.php.net/hash_pbkdf2 * @param string $algo * @param string $password * @param string $salt * @param int $i...
- `query` **(Many-Argument Workhorses)** (@ `system/database/DB_driver.php`) -> Impact: **63.0** | LOC: 140
  * *Intent:* /** * Execute the query * * Accepts an SQL string as input and returns a result object upon * successful execution of a "read" type query. Returns boo...
- `model` **(Many-Argument Workhorses)** (@ `system/core/Loader.php`) -> Impact: **58.5** | LOC: 129
  * *Intent:* // -------------------------------------------------------------------- /** * Model Loader * * Loads and instantiates models. * * @param mixed $model ...
- `timespan` **(Many-Argument Workhorses)** (@ `system/helpers/date_helper.php`) -> Impact: **56.4** | LOC: 87
  * *Intent:* /** * Timespan * * Returns a span of seconds in this format: * 10 days 14 hours 36 minutes 47 seconds * * @param int a number of seconds * @param int ...
- `load` **(Many-Argument Workhorses)** (@ `system/core/Lang.php`) -> Impact: **55.9** | LOC: 90
  * *Intent:* // -------------------------------------------------------------------- /** * Load a language file * * @param mixed $langfile Language file name * @pa...
- `password_hash` **(Many-Argument Workhorses)** (@ `system/core/compat/password.php`) -> Impact: **54.6** | LOC: 93
  * *Intent:* /** * password_hash() * * @link https://secure.php.net/password_hash * @param string $password * @param int $algo * @param array $options * @return mi...

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `system/database` | 8 | 4232.06 | 33.43% | 60.1% |
| `system/core` | 18 | 4205.0 | 29.38% | 52.23% |
| `system/helpers` | 20 | 3463.6 | 30.95% | 0.63% |
| `system/database/drivers/pdo/subdrivers` | 25 | 2581.62 | 35.02% | 89.71% |
| `user_guide_src/source/_themes/sphinx_rtd_theme` | 8 | 1574.59 | 6.34% | 9.69% |
| `system/database/drivers/mysqli` | 5 | 578.66 | 28.89% | 58.25% |
| `system/language/english` | 14 | 535.24 | 12.66% | 0.0% |
| `system/database/drivers/mysql` | 5 | 506.38 | 26.42% | 58.12% |
| `system/database/drivers/oci8` | 5 | 496.3 | 20.54% | 68.7% |
| `system/database/drivers/postgre` | 5 | 483.62 | 19.74% | 70.38% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `system/database/drivers/sqlite3/sqlite3_driver.php` -> **100.0%** Exposure
- `system/database/drivers/mysql/mysql_driver.php` -> **99.9999%** Exposure
- `system/database/drivers/sqlite3/sqlite3_forge.php` -> **99.9999%** Exposure
- `system/database/drivers/cubrid/cubrid_result.php` -> **99.9993%** Exposure
- `system/database/drivers/sqlsrv/sqlsrv_result.php` -> **99.9989%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `application/config/autoload.php` -> **100.0%** Exposure
- `application/config/migration.php` -> **100.0%** Exposure
- `system/core/CodeIgniter.php` -> **100.0%** Exposure
- `system/core/Config.php` -> **100.0%** Exposure
- `system/core/Exceptions.php` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `system/database/DB_query_builder.php` -> **46** Orphaned Functions | **0** Duplicates
- `system/database/DB_driver.php` -> **28** Orphaned Functions | **0** Duplicates
- `system/database/drivers/postgre/postgre_driver.php` -> **19** Orphaned Functions | **0** Duplicates
- `system/database/drivers/mssql/mssql_driver.php` -> **18** Orphaned Functions | **0** Duplicates
- `system/database/drivers/oci8/oci8_driver.php` -> **18** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `4` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2075` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `system/database/DB_query_builder.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1807.88 | **LOC:** 2882 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **28**; blast radius 4.204; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (98.3%), Debt Markers (formerly Tech Debt) (93.9%), Mutation Surface (formerly State Flux) (85.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_like` **(Many-Argument Workhorses)** (Impact: 53.0)
    * *Intent:* * * @used-by like() * @used-by or_like() * @used-by not_like() * @used-by or_not_like() * * @param m...
  * `_wh` **(Many-Argument Workhorses)** (Impact: 41.8)
    * *Intent:* * WHERE, HAVING * * @used-by where() * @used-by or_where() * @used-by having() * @used-by or_having(...
  * `join` **(Many-Argument Workhorses)** (Impact: 41.7)
    * *Intent:* // -------------------------------------------------------------------- /** * JOIN * * Generates the...
  * `delete` **(Many-Argument Workhorses)** (Impact: 34.0)
    * *Intent:* // -------------------------------------------------------------------- /** * Delete * * Compiles a ...
  * `update_batch` **(Many-Argument Workhorses)** (Impact: 33.9)
    * *Intent:* // -------------------------------------------------------------------- /** * Update_Batch * * Compi...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 304 instances
* *State Mutation (weighted view):* 1002
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 268`, `structural_boundaries: 232`, `args: 84`, `func_start: 84`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 394`, `dead_code: 3`, `planned_debt: 1`, `unreferenced_by_name: 46`
* *Architecture:* `api: 57`
* *Defense:* `safety: 35`, `doc: 117`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` $c = count($this->$qb_key, $c = count($this->qb_groupby, $this->_like_escape_chr, * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 *
 * @package	CodeIgniter
 * @author	EllisLab Dev Team
 * @copyright	Copyright (c) 2008 - 2014, 
	protected function _compile_wh($qb_key)
	
		if (count($this->$qb_key) > 0)
		
			for ($i = 0, ARISING FROM, )
 * @copyright	Copyright (c) 2019 - 2022...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `system/database/DB_driver.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1016.14 | **LOC:** 1941 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **26**; blast radius 4.204; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (95.9%), Debt Markers (formerly Tech Debt) (94.5%), Mutation Surface (formerly State Flux) (85.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `protect_identifiers` **(Many-Argument Workhorses)** (Impact: 95.4)
    * *Intent:* * * SELECT m.member_id, m.member_name FROM members AS m * * Since the column name can include up to ...
  * `query` **(Many-Argument Workhorses)** (Impact: 63.0)
    * *Intent:* /** * Execute the query * * Accepts an SQL string as input and returns a result object upon * succes...
  * `escape_identifiers` **(Compute Cores)** (Impact: 32.1)
    * *Intent:* // -------------------------------------------------------------------- /** * Escape the SQL Identif...
  * `display_error` **(Many-Argument Workhorses)** (Impact: 22.2)
    * *Intent:* // -------------------------------------------------------------------- /** * Display an error messa...
  * `compile_binds` **(Many-Argument Workhorses)** (Impact: 20.1)
    * *Intent:* // -------------------------------------------------------------------- /** * Compile Bindings * * @...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 152 instances
* *Api Near Db Sink:* 1 instances
* *State Mutation (weighted view):* 491
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 179`, `structural_boundaries: 167`, `args: 57`, `func_start: 56`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 187`, `dead_code: 1`, `fragile_debt: 1`, `unreferenced_by_name: 28`
* *Architecture:* `io: 1`, `api: 77`, `import: 1`
* *Defense:* `safety: 20`, `doc: 98`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` $field_exists = TRUE)
	
		if ( ! is_bool($protect_identifiers))
		
			$protect_identifiers = $this->_protect_identifiers, $prefix_single = FALSE, $protect_identifiers = NULL, * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 *
 * @package	CodeIgniter
 * @author	EllisLab Dev Team
 * @copyright	Copyright (c) 2008 - 2014, ARISING FROM, )
 * @copyright	Copyright (c) 2019 - 2022, 
defined('BASEPATH') OR exit('No direct script access allowed'...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `user_guide_src/source/_themes/sphinx_rtd_theme/layout.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 889.05 | **LOC:** 167 | **CtrlFlow:** 14.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **23**; blast radius 4.204; role: Isolated/Orphan
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (7.0%), Complexity Load (formerly Cognitive Load) (6.4%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 14`, `args: 14`, `func_start: 5`
* *Risk/State:* None
* *Architecture:* `io: 20`, `api: 5`, `import: 2`
* *Defense:* `safety: 1`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` 1), 400italic, 700, 700&subset=latin, 700italic|Roboto+Slab:400, 700|Inconsolata:400, cyrillic, modernizr.min.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `system/core/Loader.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 812.02 | **LOC:** 1435 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **53**; blast radius 4.204; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.6%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (44.3%)
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
* *Structure:* `branch: 154`, `structural_boundaries: 151`, `args: 29`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 162`, `planned_debt: 1`, `unreferenced_by_name: 10`
* *Architecture:* `api: 22`, `import: 25`
* *Defense:* `safety: 35`, `doc: 43`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` $_ci_path, $_ci_vars, '.strtolower($class).'.php', '.ucfirst(strtolower($class)).'.php', '.strtolower($class).'.php', '.ucfirst(strtolower($class)).'.php', '', ')...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `system/helpers/form_helper.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 724.76 | **LOC:** 1037 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 4.204; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (38.0%)
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
* *Structure:* `branch: 136`, `structural_boundaries: 86`, `args: 54`, `func_start: 27`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 151`
* *Architecture:* `io: 4`
* *Defense:* `safety: 16`, `doc: 29`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 *
 * @package	CodeIgniter
 * @author	EllisLab Dev Team
 * @copyright	Copyright (c) 2008 - 2014, ARISING FROM, )
 * @copyright	Copyright (c) 2019 - 2022, 
defined('BASEPATH') OR exit('No direct script access allowed', DAMAGES OR OTHER
 * LIABILITY, EXPRESS OR
 * IMPLIED, EllisLab...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `system/database/DB_forge.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 629.62 | **LOC:** 1039 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 4.204; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (93.6%), Mutation Surface (formerly State Flux) (85.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (36.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_process_fields` **(Defensive Guards)** (Impact: 47.1)
    * *Intent:* // -------------------------------------------------------------------- /** * Process fields * * @pa...
  * `create_table` **(Many-Argument Workhorses)** (Impact: 26.4)
    * *Intent:* // -------------------------------------------------------------------- /** * Create Table * * @para...
  * `_attr_default` **(Stateful Encapsulated Methods)** (Impact: 22.5)
    * *Intent:* // -------------------------------------------------------------------- /** * Field attribute DEFAUL...
  * `_create_table` **(Many-Argument Workhorses)** (Impact: 18.1)
    * *Intent:* // -------------------------------------------------------------------- /** * Create Table * * @para...
  * `_attr_unsigned` **(Stateful Encapsulated Methods)** (Impact: 17.1)
    * *Intent:* * * Depending on the _unsigned property value: * * - TRUE will always set $field['unsigned'] to 'UNS...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 95 instances
* *State Mutation (weighted view):* 303
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 76`, `args: 25`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 113`, `unreferenced_by_name: 8`
* *Architecture:* `api: 15`
* *Defense:* `safety: 27`, `doc: 42`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` $primary, * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 *
 * @package	CodeIgniter
 * @author	EllisLab Dev Team
 * @copyright	Copyright (c) 2008 - 2014, ARISING FROM, )
 * @copyright	Copyright (c) 2019 - 2022, 
defined('BASEPATH') OR exit('No direct script access allowed', DAMAGES OR OTHER
 * LIABILITY, EXPRESS OR
 * IMPLIED...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `system/core/Security.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 530.2 | **LOC:** 1089 | **CtrlFlow:** 28.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 4.204; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (37.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `xss_clean` **(Many-Argument Workhorses)** (Impact: 89.0)
    * *Intent:* * runtime processing. * * @link http://channel.bitflux.ch/wiki/XSS_Prevention * Based in part on som...
  * `_sanitize_naughty_html` **(Compute Cores)** (Impact: 25.2)
    * *Intent:* // -------------------------------------------------------------------- /** * Sanitize Naughty HTML ...
  * `entity_decode` **(Many-Argument Workhorses)** (Impact: 22.9)
    * *Intent:* * A replacement for html_entity_decode() * * The reason we are not using html_entity_decode() by its...
  * `get_random_bytes` **(Defensive Guards)** (Impact: 15.1)
    * *Intent:* // -------------------------------------------------------------------- /** * Get random bytes * * @...
  * `csrf_verify` **(I/O & Config Routines)** (Impact: 13.4)
    * *Intent:* // -------------------------------------------------------------------- /** * CSRF Verify * * @retur...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 80 instances
* *State Mutation (weighted view):* 247
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 144`, `structural_boundaries: 66`, `args: 24`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 87`, `dead_code: 2`, `unreferenced_by_name: 6`
* *Architecture:* `io: 20`, `api: 14`
* *Defense:* `safety: 11`, `doc: 33`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 *
 * @package	CodeIgniter
 * @author	EllisLab Dev Team
 * @copyright	Copyright (c) 2008 - 2014, ARISING FROM, )
 * @copyright	Copyright (c) 2019 - 2022, 
defined('BASEPATH') OR exit('No direct script access allowed', DAMAGES OR OTHER
 * LIABILITY, EXPRESS OR
 * IMPLIED, EllisLab...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `system/core/Input.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 515.16 | **LOC:** 705 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 4.204; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.2%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (61.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `set_cookie` **(Many-Argument Workhorses)** (Impact: 89.8)
    * *Intent:* * Accepts an arbitrary number of parameters (up to 7) or an associative * array in the first paramet...
  * `ip_address` **(I/O & Config Routines)** (Impact: 35.4)
    * *Intent:* // -------------------------------------------------------------------- /** * Fetch the IP Address *...
  * `_fetch_from_array` **(Many-Argument Workhorses)** (Impact: 28.6)
    * *Intent:* // -------------------------------------------------------------------- /** * Fetch from array * * I...
  * `valid_ip` **(Compute Cores)** (Impact: 14.7)
    * *Intent:* // -------------------------------------------------------------------- /** * Validate IP Address * ...
  * `get_request_header` **(Defensive Guards)** (Impact: 11.6)
    * *Intent:* // -------------------------------------------------------------------- /** * Get Request Header * *...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 85 instances
* *State Mutation (weighted view):* 267
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 49`, `args: 19`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 97`, `dead_code: 1`, `unreferenced_by_name: 10`
* *Architecture:* `io: 14`, `api: 17`
* *Defense:* `safety: 18`, `doc: 25`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 *
 * @package	CodeIgniter
 * @author	EllisLab Dev Team
 * @copyright	Copyright (c) 2008 - 2014, ARISING FROM, )
 * @copyright	Copyright (c) 2019 - 2022, 
defined('BASEPATH') OR exit('No direct script access allowed', DAMAGES OR OTHER
 * LIABILITY, EXPRESS OR
 * IMPLIED, EllisLab...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `system/core/Output.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 467.58 | **LOC:** 845 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 4.204; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.2%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (71.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_display` **(I/O & Config Routines)** (Impact: 40.4)
    * *Intent:* /** * Display Output * * Processes and sends finalized output data to the browser along * with any s...
  * `_write_cache` **(Compute Cores)** (Impact: 30.0)
    * *Intent:* // -------------------------------------------------------------------- /** * Write Cache * * @param...
  * `_display_cache` **(Many-Argument Workhorses)** (Impact: 27.6)
    * *Intent:* // -------------------------------------------------------------------- /** * Update/serve cached ou...
  * `delete_cache` **(Compute Cores)** (Impact: 19.1)
    * *Intent:* // -------------------------------------------------------------------- /** * Delete cache * * @para...
  * `set_content_type` **(Defensive Guards)** (Impact: 11.9)
    * *Intent:* // -------------------------------------------------------------------- /** * Set Content-Type Heade...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 79 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 252
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 55`, `args: 20`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 2`, `state_mutation: 94`, `planned_debt: 1`, `unreferenced_by_name: 8`
* *Architecture:* `io: 29`, `api: 23`
* *Defense:* `safety: 19`, `doc: 32`, `sync_locks: 5`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 *
 * @package	CodeIgniter
 * @author	EllisLab Dev Team
 * @copyright	Copyright (c) 2008 - 2014, ARISING FROM, )
 * @copyright	Copyright (c) 2019 - 2022, 
defined('BASEPATH') OR exit('No direct script access allowed', DAMAGES OR OTHER
 * LIABILITY, EXPRESS OR
 * IMPLIED, EllisLab...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `system/helpers/url_helper.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 433.64 | **LOC:** 560 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 4.204; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (39.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `safe_mailto` **(Many-Argument Workhorses)** (Impact: 38.7)
    * *Intent:* /** * Encoded Mailto Link * * Create a spam-protected mailto link written in Javascript * * @param s...
  * `redirect` **(Many-Argument Workhorses)** (Impact: 35.9)
    * *Intent:* /** * Header Redirect * * Header redirect in two flavors * For very fine grained control over header...
  * `auto_link` **(Many-Argument Workhorses)** (Impact: 27.9)
    * *Intent:* /** * Auto-linker * * Automatically links URL and Email addresses. * Note: There's a bit of extra co...
  * `anchor_popup` **(Many-Argument Workhorses)** (Impact: 22.2)
    * *Intent:* /** * Anchor Link - Pop-up version * * Creates an anchor based on the local URL. The link * opens a ...
  * `anchor` **(Many-Argument Workhorses)** (Impact: 13.0)
    * *Intent:* /** * Anchor Link * * Creates an anchor based on the local URL. * * @param string the URL * @param s...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 84 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 262
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 36`, `args: 26`, `func_start: 13`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 94`, `dead_code: 2`
* *Architecture:* `io: 2`
* *Defense:* `safety: 6`, `doc: 15`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 *
 * @package	CodeIgniter
 * @author	EllisLab Dev Team
 * @copyright	Copyright (c) 2008 - 2014, ARISING FROM, )
 * @copyright	Copyright (c) 2019 - 2022, 
defined('BASEPATH') OR exit('No direct script access allowed', DAMAGES OR OTHER
 * LIABILITY, EXPRESS OR
 * IMPLIED, EllisLab...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `system/helpers/date_helper.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 428.52 | **LOC:** 638 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 4.204; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (46.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `timespan` **(Many-Argument Workhorses)** (Impact: 56.4)
    * *Intent:* /** * Timespan * * Returns a span of seconds in this format: * 10 days 14 hours 36 minutes 47 second...
  * `date_range` **(Many-Argument Workhorses)** (Impact: 31.8)
    * *Intent:* * Date range * * Returns a list of dates within a specified period. * * @param int unix_start UNIX t...
  * `human_to_unix` **(Defensive Guards)** (Impact: 18.7)
    * *Intent:* /** * Convert "human" date to GMT * * Reverses the above process * * @param string format: us or eur...
  * `days_in_month` **(Compute Cores)** (Impact: 15.5)
    * *Intent:* /** * Number of days in a month * * Takes a month/year as input and returns the number of days * for...
  * `timezone_menu` **(Many-Argument Workhorses)** (Impact: 12.4)
    * *Intent:* /** * Timezone Menu * * Generates a drop-down menu of timezones. * * @param string timezone * @param...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 78 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 243
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 47`, `args: 24`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 1`, `state_mutation: 87`, `fragile_debt: 1`
* *Architecture:* None
* *Defense:* `safety: 5`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 *
 * @package	CodeIgniter
 * @author	EllisLab Dev Team
 * @copyright	Copyright (c) 2008 - 2014, ARISING FROM, )
 * @copyright	Copyright (c) 2019 - 2022, 
defined('BASEPATH') OR exit('No direct script access allowed', DAMAGES OR OTHER
 * LIABILITY, EXPRESS OR
 * IMPLIED, EllisLab...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `system/helpers/text_helper.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 392.5 | **LOC:** 569 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 4.204; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (46.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `word_wrap` **(Many-Argument Workhorses)** (Impact: 30.0)
    * *Intent:* /** * Word Wrap * * Wraps text at the specified character. Maintains the integrity of words. * Anyth...
  * `ascii_to_entities` **(Compute Cores)** (Impact: 18.2)
    * *Intent:* /** * High ASCII to Entities * * Converts high ASCII text and MS Word special characters to characte...
  * `word_censor` **(Many-Argument Workhorses)** (Impact: 18.2)
    * *Intent:* /** * Word Censoring Function * * Supply a string and an array of disallowed words and any * matched...
  * `entities_to_ascii` **(Compute Cores)** (Impact: 14.1)
    * *Intent:* /** * Entities to ASCII * * Converts character entities back to ASCII * * @param string * @param boo...
  * `character_limiter` **(Many-Argument Workhorses)** (Impact: 13.3)
    * *Intent:* /** * Character Limiter * * Limits the string based on the character count. Preserves complete words...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 80 instances
* *State Mutation (weighted view):* 243
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 33`, `args: 20`, `func_start: 10`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 83`, `dead_code: 1`
* *Architecture:* `import: 2`
* *Defense:* `safety: 1`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 *
 * @package	CodeIgniter
 * @author	EllisLab Dev Team
 * @copyright	Copyright (c) 2008 - 2014, foreign_chars.php', foreign_chars.php', ARISING FROM, )
 * @copyright	Copyright (c) 2019 - 2022, 
defined('BASEPATH') OR exit('No direct script access allowed', DAMAGES OR OTHER
 * LIABILITY...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `user_guide_src/source/_themes/sphinx_rtd_theme/layout_old.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 378.42 | **LOC:** 206 | **CtrlFlow:** 4.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 4.204; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (15.3%), Complexity Load (formerly Cognitive Load) (5.8%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 20`, `args: 9`, `func_start: 2`
* *Risk/State:* `fragile_debt: 1`
* *Architecture:* `io: 28`, `import: 3`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` 1), next.link|e, parents[-1].link|e, ' + favicon, ' + style, opensearch.xml', pygments.css', pathto('about')...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `system/core/URI.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 362.28 | **LOC:** 663 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **21**; blast radius 4.204; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.4%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (70.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_uri_to_assoc` **(Many-Argument Workhorses)** (Impact: 24.9)
    * *Intent:* // -------------------------------------------------------------------- /** * Internal URI-to-assoc ...
  * `__construct` **(Compute Cores)** (Impact: 21.7)
    * *Intent:* /** * Class constructor * * @return void */
  * `_set_uri_string` **(Many-Argument Workhorses)** (Impact: 20.2)
    * *Intent:* // -------------------------------------------------------------------- /** * Set URI String * * @pa...
  * `_parse_request_uri` **(I/O & Config Routines)** (Impact: 15.4)
    * *Intent:* // -------------------------------------------------------------------- /** * Parse REQUEST_URI * * ...
  * `filter_uri` **(Defensive Guards)** (Impact: 7.4)
    * *Intent:* // -------------------------------------------------------------------- /** * Filter URI * * Filters...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 63 instances
* *State Mutation (weighted view):* 200
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 56`, `args: 22`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 74`, `unreferenced_by_name: 9`
* *Architecture:* `io: 2`, `api: 19`
* *Defense:* `safety: 16`, `doc: 29`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` $query, ', ') === '' && strncmp($query, * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 *
 * @package	CodeIgniter
 * @author	EllisLab Dev Team
 * @copyright	Copyright (c) 2008 - 2014, 1) === 0)
		
			$query = explode('?', 2, ARISING FROM...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `system/core/Common.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 332.66 | **LOC:** 854 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **49**; blast radius 4.204; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (89.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (34.5%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` $file_path, * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 *
 * @package	CodeIgniter
 * @author	EllisLab Dev Team
 * @copyright	Copyright (c) 2008 - 2014, 403	=> 'Forbidden', 404	=> 'Not Found', 405	=> 'Method Not Allowed', 406	=> 'Not Acceptable', 407	=> 'Proxy Authentication Required'...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `system/helpers/file_helper.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 330.44 | **LOC:** 436 | **CtrlFlow:** 35.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 4.204; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (48.7%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` $_recursion = FALSE)
	
		static $_filedata = array(, $include_path = FALSE, * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 *
 * @package	CodeIgniter
 * @author	EllisLab Dev Team
 * @copyright	Copyright (c) 2008 - 2014, ARISING FROM, )
 * @copyright	Copyright (c) 2019 - 2022, 
defined('BASEPATH') OR exit('No direct script access allowed', DAMAGES OR OTHER
 * LIABILITY...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `system/helpers/captcha_helper.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Drift: 0.0 IQR)
- **Magnitude:** 320.54 | **LOC:** 383 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 4.204; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (66.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create_captcha` **(Many-Argument Workhorses)** (Impact: 93.8)
    * *Intent:* /** * Create CAPTCHA * * @param array $data Data for the CAPTCHA * @return array */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 72 instances
* *State Mutation (weighted view):* 222
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 11`, `args: 5`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `state_mutation: 78`, `dead_code: 1`
* *Architecture:* `io: 2`
* *Defense:* `safety: 9`, `doc: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 *
 * @package	CodeIgniter
 * @author	EllisLab Dev Team
 * @copyright	Copyright (c) 2008 - 2014, ARISING FROM, )
 * @copyright	Copyright (c) 2019 - 2022, 
defined('BASEPATH') OR exit('No direct script access allowed', DAMAGES OR OTHER
 * LIABILITY, EXPRESS OR
 * IMPLIED, EllisLab...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `system/database/DB_result.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 319.22 | **LOC:** 667 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 4.204; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (95.6%), Mutation Surface (formerly State Flux) (85.0%), Debt Markers (formerly Tech Debt) (83.1%), Test Surface (formerly Verification) (80.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 *
 * @package	CodeIgniter
 * @author	EllisLab Dev Team
 * @copyright	Copyright (c) 2008 - 2014, ARISING FROM, )
 * @copyright	Copyright (c) 2019 - 2022, 
defined('BASEPATH') OR exit('No direct script access allowed', DAMAGES OR OTHER
 * LIABILITY, EXPRESS OR
 * IMPLIED, EllisLab...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `system/helpers/html_helper.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 298.7 | **LOC:** 392 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 4.204; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (39.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `link_tag` **(Many-Argument Workhorses)** (Impact: 45.1)
    * *Intent:* /** * Link * * Generates link to a CSS file * * @param mixed stylesheet hrefs or an array * @param s...
  * `meta` **(Many-Argument Workhorses)** (Impact: 28.9)
    * *Intent:* /** * Generates meta tags from an array of key/values * * @param array * @param string * @param stri...
  * `img` **(Many-Argument Workhorses)** (Impact: 23.8)
    * *Intent:* /** * Image * * Generates an <img /> element * * @param mixed * @param bool * @param mixed * @return...
  * `_list` **(Many-Argument Workhorses)** (Impact: 13.1)
    * *Intent:* /** * Generates the list * * Generates an HTML ordered list from an single or multi-dimensional arra...
  * `doctype` **(Defensive Guards)** (Impact: 9.8)
    * *Intent:* /** * Doctype * * Generates a page document type declaration * * Examples of valid options: html5, x...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 54 instances
* *State Mutation (weighted view):* 168
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 24`, `args: 16`, `func_start: 8`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 60`
* *Architecture:* `import: 2`
* *Defense:* `safety: 9`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 *
 * @package	CodeIgniter
 * @author	EllisLab Dev Team
 * @copyright	Copyright (c) 2008 - 2014, doctypes.php', doctypes.php', ARISING FROM, )
 * @copyright	Copyright (c) 2019 - 2022, 
defined('BASEPATH') OR exit('No direct script access allowed', DAMAGES OR OTHER
 * LIABILITY...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `system/database/drivers/postgre/postgre_driver.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 290.54 | **LOC:** 606 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 4.204; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.3%), Guard Balance (formerly Safety Score) (95.8%), Mutation Surface (formerly State Flux) (85.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `db_connect` **(Defensive Guards)** (Impact: 14.2)
    * *Intent:* // -------------------------------------------------------------------- /** * Database connection * ...
  * `order_by` **(Type Conversions)** (Impact: 13.2)
    * *Intent:* // -------------------------------------------------------------------- /** * ORDER BY * * @param st...
  * `insert_id` **(I/O & Config Routines)** (Impact: 11.8)
    * *Intent:* // -------------------------------------------------------------------- /** * Insert ID * * @return ...
  * `_update_batch` **(Stateful Encapsulated Methods)** (Impact: 11.4)
    * *Intent:* // -------------------------------------------------------------------- /** * Update_Batch statement...
  * `_build_dsn` **(I/O & Config Routines)** (Impact: 11.3)
    * *Intent:* // -------------------------------------------------------------------- /** * Build DSN * * @return ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 51 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 160
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 60`, `args: 23`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 58`, `unreferenced_by_name: 19`
* *Architecture:* `api: 12`
* *Defense:* `safety: 6`, `doc: 28`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 *
 * @package	CodeIgniter
 * @author	EllisLab Dev Team
 * @copyright	Copyright (c) 2008 - 2014, ARISING FROM, )
 * @copyright	Copyright (c) 2019 - 2022, 
defined('BASEPATH') OR exit('No direct script access allowed', DAMAGES OR OTHER
 * LIABILITY, EXPRESS OR
 * IMPLIED, EllisLab...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `system/database/drivers/oci8/oci8_driver.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 276.56 | **LOC:** 618 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 4.204; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Guard Balance (formerly Safety Score) (96.3%), Mutation Surface (formerly State Flux) (85.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__construct` **(Compute Cores)** (Impact: 35.0)
    * *Intent:* // -------------------------------------------------------------------- /** * Class constructor * * ...
  * `field_data` **(Compute Cores)** (Impact: 15.1)
    * *Intent:* // -------------------------------------------------------------------- /** * Returns an object with...
  * `_limit` **(Stateful Encapsulated Methods)** (Impact: 6.4)
    * *Intent:* // -------------------------------------------------------------------- /** * LIMIT * * Generates a ...
  * `error` **(I/O & Config Routines)** (Impact: 6.2)
    * *Intent:* // -------------------------------------------------------------------- /** * Error * * Returns an a...
  * `version` **(Defensive Guards)** (Impact: 5.9)
    * *Intent:* // -------------------------------------------------------------------- /** * Database version numbe...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 47 instances
* *State Mutation (weighted view):* 154
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 53`, `args: 19`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 60`, `dead_code: 1`, `fragile_debt: 1`, `unreferenced_by_name: 18`
* *Architecture:* `api: 10`
* *Defense:* `safety: 6`, `doc: 30`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 *
 * @package	CodeIgniter
 * @author	EllisLab Dev Team
 * @copyright	Copyright (c) 2008 - 2014, ARISING FROM, )
 * @copyright	Copyright (c) 2019 - 2022, 
defined('BASEPATH') OR exit('No direct script access allowed', DAMAGES OR OTHER
 * LIABILITY, EXPRESS OR
 * IMPLIED, EllisLab...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/mocks/ci_testcase.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 267.62 | **LOC:** 401 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 4.204; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (94.2%), Complexity Load (formerly Cognitive Load) (24.8%), Connectivity (formerly Api Exposure) (9.4%)
- **Documentation Coverage:** 58.5366% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ci_vfs_create` **(Many-Argument Workhorses)** (Impact: 32.4)
    * *Intent:* // -------------------------------------------------------------------- /** * Create VFS content * *...
  * `ci_vfs_clone` **(Compute Cores)** (Impact: 10.1)
    * *Intent:* // -------------------------------------------------------------------- /** * Clone a real file into...
  * `ci_set_config` **(Defensive Guards)** (Impact: 9.8)
    * *Intent:* // --------------------------------------------------------------------
  * `setExpectedException` **(Compute Cores)** (Impact: 8.7)
  * `ci_core_class` **(Defensive Guards)** (Impact: 8.4)
    * *Intent:* // -------------------------------------------------------------------- /** * Grab a core class * * ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 40 instances
* *State Mutation (weighted view):* 132
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 47`, `args: 19`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 52`, `planned_debt: 1`, `unreferenced_by_name: 15`
* *Architecture:* `io: 1`, `api: 23`, `import: 3`
* *Defense:* `safety: 7`, `doc: 7`, `test: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` '.$name.'_lang.php', '.$class_name.'.php', '.$name.'_helper.php'
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `system/database/drivers/sqlsrv/sqlsrv_driver.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 259.46 | **LOC:** 545 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 4.204; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.7%), Guard Balance (formerly Safety Score) (96.8%), Mutation Surface (formerly State Flux) (85.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_limit` **(Stateful Encapsulated Methods)** (Impact: 20.8)
    * *Intent:* // -------------------------------------------------------------------- /** * LIMIT * * Generates a ...
  * `db_connect` **(Defensive Guards)** (Impact: 17.2)
    * *Intent:* // -------------------------------------------------------------------- /** * Database connection * ...
  * `error` **(Defensive Guards)** (Impact: 7.3)
    * *Intent:* // -------------------------------------------------------------------- /** * Error * * Returns an a...
  * `field_data` **(Compute Cores)** (Impact: 6.9)
    * *Intent:* // -------------------------------------------------------------------- /** * Returns an object with...
  * `_insert_batch` **(Stateful Encapsulated Methods)** (Impact: 6.5)
    * *Intent:* // -------------------------------------------------------------------- /** * Insert batch statement...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 47 instances
* *Api Near Db Sink:* 1 instances
* *State Mutation (weighted view):* 149
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 50`, `args: 20`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 55`, `unreferenced_by_name: 18`
* *Architecture:* `api: 10`
* *Defense:* `safety: 12`, `doc: 26`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 *
 * @package	CodeIgniter
 * @author	EllisLab Dev Team
 * @copyright	Copyright (c) 2008 - 2014, ARISING FROM, )
 * @copyright	Copyright (c) 2019 - 2022, 
defined('BASEPATH') OR exit('No direct script access allowed', DAMAGES OR OTHER
 * LIABILITY, EXPRESS OR
 * IMPLIED, EllisLab...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `system/database/DB_utility.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 236.16 | **LOC:** 416 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 4.204; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (97.3%), Mutation Surface (formerly State Flux) (85.0%), Debt Markers (formerly Tech Debt) (83.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `backup` **(Compute Cores)** (Impact: 34.7)
    * *Intent:* // -------------------------------------------------------------------- /** * Database Backup * * @p...
  * `xml_from_result` **(Compute Cores)** (Impact: 10.2)
    * *Intent:* // -------------------------------------------------------------------- /** * Generate XML data from...
  * `csv_from_result` **(Many-Argument Workhorses)** (Impact: 10.1)
    * *Intent:* // -------------------------------------------------------------------- /** * Generate CSV from a qu...
  * `list_databases` **(I/O & Config Routines)** (Impact: 7.3)
    * *Intent:* // -------------------------------------------------------------------- /** * List databases * * @re...
  * `optimize_table` **(Compute Cores)** (Impact: 6.5)
    * *Intent:* // -------------------------------------------------------------------- /** * Optimize Table * * @pa...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 44 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 138
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 37`, `args: 11`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 50`, `unreferenced_by_name: 8`
* *Architecture:* `api: 9`
* *Defense:* `safety: 3`, `doc: 15`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` $prefs['filename'], $prefs['filename']))
				
					$prefs['filename'] = str_replace('.zip', '', * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 *
 * @package	CodeIgniter
 * @author	EllisLab Dev Team
 * @copyright	Copyright (c) 2008 - 2014, ARISING FROM, )
 * @copyright	Copyright (c) 2019 - 2022, 
defined('BASEPATH') OR exit('No direct script access allowed'...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `system/database/drivers/mssql/mssql_driver.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 228.6 | **LOC:** 508 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 4.204; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.9%), Guard Balance (formerly Safety Score) (97.9%), Mutation Surface (formerly State Flux) (85.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_limit` **(Stateful Encapsulated Methods)** (Impact: 19.0)
    * *Intent:* // -------------------------------------------------------------------- /** * LIMIT * * Generates a ...
  * `db_connect` **(Compute Cores)** (Impact: 12.9)
    * *Intent:* // -------------------------------------------------------------------- /** * Non-persistent databas...
  * `field_data` **(Compute Cores)** (Impact: 6.9)
    * *Intent:* // -------------------------------------------------------------------- /** * Returns an object with...
  * `_insert_batch` **(Stateful Encapsulated Methods)** (Impact: 6.5)
    * *Intent:* // -------------------------------------------------------------------- /** * Insert batch statement...
  * `db_select` **(Compute Cores)** (Impact: 5.1)
    * *Intent:* // -------------------------------------------------------------------- /** * Select the database * ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 42 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 134
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 48`, `args: 20`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `state_mutation: 50`, `unreferenced_by_name: 18`
* *Architecture:* `api: 8`
* *Defense:* `safety: 4`, `doc: 25`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.204
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` $this->conn_id))
		
			$this->database = $database, '9', '>=') && $this->qb_offset && ! empty($this->qb_orderby))
		
			$orderby = $this->_compile_order_by(, * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 *
 * @package	CodeIgniter
 * @author	EllisLab Dev Team
 * @copyright	Copyright (c) 2008 - 2014, ARISING FROM, )
 * @copyright	Copyright (c) 2019 - 2022, 
defined('BASEPATH') OR exit('No direct script access allowed'...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `system/database/DB.php` -> **Severity: 0.383** (Embedded: 0.0042 * Error Risk: 90.3391%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tests/mocks/autoloader.php` -> **Severity: 420.4** (Blast Radius: 4.204 * Doc Risk: 100.0%)
- `tests/mocks/ci_testconfig.php` -> **Severity: 420.4** (Blast Radius: 4.204 * Doc Risk: 100.0%)
- `tests/mocks/core/security.php` -> **Severity: 420.4** (Blast Radius: 4.204 * Doc Risk: 100.0%)
- `tests/mocks/core/uri.php` -> **Severity: 420.4** (Blast Radius: 4.204 * Doc Risk: 100.0%)
- `user_guide_src/cilexer/cilexer/cilexer.py` -> **Severity: 420.4** (Blast Radius: 4.204 * Doc Risk: 100.0%)

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
