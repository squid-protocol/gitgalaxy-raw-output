# ARCHITECTURAL_BRIEF: Carbon
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/briannesbitt/Carbon.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 1983 analyzed artifact(s), 166367 LOC.
- **Load-bearing artifact:** `tests/AbstractTestCase.php` -- 166 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/Carbon/Lang/so.php` -- pulls in 97 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/Carbon/CarbonInterval.php` at magnitude 2800.76 (structural weight, not risk).
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
| Total Artifacts | 2034 |
| Analyzed Artifacts (Scanned) | 1983 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 51 |
| Total LOC | 166367 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 97.5% |
| Dominant Lang | PHP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3923 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3257 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.7836 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 15 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PHP | 1974 | 166206 | 99.5% |
| YAML | 3 | 32 | 0.2% |
| MARKDOWN | 2 | 0 | 0.1% |
| XML | 2 | 0 | 0.1% |
| BATCH | 1 | 4 | 0.1% |
| JSON | 1 | 125 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Mid Flat Project`
> **Architectural Drift Z-Score:** `4.438`
> **Composition Archetype:** `Mid Flat Project` (z +4.44; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 63%, Data / Markup / Trivial 23%, Interface Declarations Files 7%, Large Core Modules 2%, Large Core Modules (2) 1%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1981 | 99.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 51*

**Composition by Extension & Reason:**
- `.php`: 10x Excluded (Saturation: Line 28 exceeds 500 chars), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 26 exceeds 500 chars)
- `.yml`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.neon`: 4x Excluded (Unsupported Extension: '.neon')
- `.md`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.dist`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 1x Excluded (Binary Format Detected)
- `.xml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 74.5 | 1.9 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.8 | 10.1 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 0.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 1.1 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 3.6 | 3.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 0.6 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 3.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 14.9 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 4.2 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 30.3 | 0.4 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 11.4 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1665 | 191 | 0 | `src/Carbon/CarbonInterval.php` |
| cleanup | 43 | 10 | 0 | `src/Carbon/CarbonInterval.php` |
| guards | 2950 | 994 | 2 | `src/Carbon/CarbonPeriod.php` |
| danger | 319 | 73 | 0 | `phpdoc.php` |
| concurrency | 391 | 27 | 0 | `tests/Carbon/IssetTest.php` |
| connectivity | 5655 | 1112 | 3 | `tests/Carbon/DiffTest.php` |
| io | 12 | 4 | 0 | `phpdoc.php` |
| crypto | 0 | 0 | 0 | - |
| ipc | 6 | 3 | 0 | `tests/Cli/InvokerTest.php` |
| time | 399 | 65 | 0 | `tests/CarbonImmutable/IsTest.php` |
| serialization | 79 | 16 | 0 | `tests/Carbon/SerializationTest.php` |
| regex | 131 | 36 | 0 | `phpdoc.php` |
| events | 16 | 6 | 0 | `tests/Laravel/ServiceProviderTest.php` |
| tests | 7509 | 1015 | 1 | `tests/Carbon/IsTest.php` |
| docs | 5188 | 1973 | 1 | `src/Carbon/CarbonImmutable.php` |
| debt | 136 | 58 | 0 | `tests/CarbonInterval/ComparisonTest.php` |
| mutation | 9215 | 1169 | 4 | `src/Carbon/CarbonInterval.php` |
| dead_code | 3253 | 232 | 1 | `tests/Carbon/DiffTest.php` |
| credential | 1 | 1 | 0 | `phpdoc.php` |
| threat | 379 | 182 | 0 | `src/Carbon/Lang/af_NA.php` |
| ml_ai | 126 | 21 | 0 | `tests/Localization/ShiLatnTest.php` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.25**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `phpdoc.php` (Hits: 6)
- `sponsors.php` (Hits: 3)
- `tests/remove-comments-in-switch.php` (Hits: 2)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **AbstractTestCase.php** (`tests/AbstractTestCase.php`) — 166 inbound connections
2. **Carbon.php** (`src/Carbon/Carbon.php`) — 102 inbound connections
3. **CarbonImmutable.php** (`src/Carbon/CarbonImmutable.php`) — 77 inbound connections
4. **CarbonInterval.php** (`src/Carbon/CarbonInterval.php`) — 69 inbound connections
5. **InvalidArgumentException.php** (`src/Carbon/Exceptions/InvalidArgumentException.php`) — 57 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **so.php** (`src/Carbon/Lang/so.php`) — 97 outbound dependencies
2. **ku.php** (`src/Carbon/Lang/ku.php`) — 93 outbound dependencies
3. **lzh_TW.php** (`src/Carbon/Lang/lzh_TW.php`) — 93 outbound dependencies
4. **yi_US.php** (`src/Carbon/Lang/yi_US.php`) — 92 outbound dependencies
5. **ksh.php** (`src/Carbon/Lang/ksh.php`) — 88 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `__construct` **(Many-Argument Workhorses)** (@ `src/Carbon/CarbonInterval.php`) -> Impact: **261.8** | LOC: 135
  * *Intent:* /** * Create a new CarbonInterval instance. * * @param Closure|DateInterval|string|int|null $years * @param int|float|null $months * @param int|float|...
- `forHumans` **(Many-Argument Workhorses)** (@ `src/Carbon/CarbonInterval.php`) -> Impact: **141.9** | LOC: 200
  * *Intent:* * if int passed, it adds modifiers: * Possible values: * - CarbonInterface::DIFF_ABSOLUTE no modifiers * - CarbonInterface::DIFF_RELATIVE_TO_NOW add a...
- `fromString` **(Compute Cores)** (@ `src/Carbon/CarbonInterval.php`) -> Impact: **111.5** | LOC: 165
  * *Intent:* * * e. g. `1w 3d 4h 32m 23s` is converted to 10 days 4 hours 32 minutes and 23 seconds. * * Special cases: * - An empty string will return a zero inte...
- `__call` **(Many-Argument Workhorses)** (@ `src/Carbon/CarbonPeriod.php`) -> Impact: **101.0** | LOC: 149
  * *Intent:* /** * Add aliases for setters. * * CarbonPeriod::days(3)->hours(5)->invert() * ->sinceNow()->until('2010-01-10') * ->filter(...) * ->count() * * Note:...
- `__construct` **(Defensive Guards)** (@ `src/Carbon/CarbonPeriod.php`) -> Impact: **84.3** | LOC: 130
  * *Intent:* /** * CarbonPeriod constructor. * * @SuppressWarnings(ElseExpression) * * @throws InvalidArgumentException */
- `translateTimeString` **(Many-Argument Workhorses)** (@ `src/Carbon/Traits/Localization.php`) -> Impact: **80.9** | LOC: 98
  * *Intent:* * * @param string $timeString date/time/duration string to translate (may also contain English) * @param string|null $from input locale of the $timeSt...
- `getOpenCollectiveSponsors` **(I/O & Config Routines)** (@ `sponsors.php`) -> Impact: **77.2** | LOC: 223
- `addUTCUnit` **(Many-Argument Workhorses)** (@ `src/Carbon/Traits/Units.php`) -> Impact: **64.2** | LOC: 107
  * *Intent:* /** * Add seconds to the instance using timestamp. Positive $value travels * forward while negative $value travels into the past. * * @param string $u...
- `set` **(Many-Argument Workhorses)** (@ `src/Carbon/CarbonInterval.php`) -> Impact: **63.8** | LOC: 98
  * *Intent:* /** * Set a part of the CarbonInterval object. * * @param Unit|string|array $name * @param int $value * * @throws UnknownSetterException * * @return $...
- `create` **(Many-Argument Workhorses)** (@ `src/Carbon/Traits/Creator.php`) -> Impact: **62.3** | LOC: 58
  * *Intent:* * will be 0. * * @param DateTimeInterface|string|int|null $year * @param int|null $month * @param int|null $day * @param int|null $hour * @param int|n...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `tests/Localization` | 828 | 15945.72 | 0.03% | 0.0% |
| `src/Carbon/Lang` | 803 | 10917.04 | 0.98% | 0.05% |
| `src/Carbon` | 19 | 6114.84 | 30.59% | 0.54% |
| `tests/Carbon` | 46 | 5499.02 | 6.16% | 0.0% |
| `src/Carbon/Traits` | 27 | 4576.46 | 24.14% | 37.24% |
| `tests/CarbonImmutable` | 45 | 4479.86 | 4.2% | 0.0% |
| `tests/CarbonPeriod` | 16 | 1902.46 | 15.59% | 0.0% |
| `tests/CarbonInterval` | 27 | 1517.3 | 5.04% | 0.0% |
| `__monolith__` | 8 | 897.7 | 13.96% | 0.0% |
| `tests/Jenssegers` | 11 | 591.18 | 9.43% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/Carbon/Traits/Boundaries.php` -> **99.9998%** Exposure
- `src/Carbon/PHPStan/MacroMethodReflection.php` -> **99.9997%** Exposure
- `src/Carbon/Traits/Converter.php` -> **99.9928%** Exposure
- `src/Carbon/Traits/Comparison.php` -> **99.9743%** Exposure
- `src/Carbon/Traits/Difference.php` -> **99.9675%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `phpdoc.php` -> **100.0%** Exposure
- `sponsors.php` -> **100.0%** Exposure
- `src/Carbon/CarbonInterval.php` -> **100.0%** Exposure
- `src/Carbon/CarbonPeriod.php` -> **100.0%** Exposure
- `src/Carbon/Factory.php` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/Carbon/DiffTest.php` -> **205** Orphaned Functions | **0** Duplicates
- `tests/CarbonImmutable/DiffTest.php` -> **198** Orphaned Functions | **0** Duplicates
- `tests/Carbon/IsTest.php` -> **147** Orphaned Functions | **0** Duplicates
- `tests/CarbonImmutable/IsTest.php` -> **125** Orphaned Functions | **0** Duplicates
- `tests/Carbon/StartEndOfTest.php` -> **81** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `15295` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/Carbon/CarbonInterval.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2800.76 | **LOC:** 3574 | **CtrlFlow:** 29.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **69** in-repo importer(s); it depends on **41**; blast radius 11.773; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.2%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (75.8%)
- **Documentation Coverage:** 13.0045% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__construct` **(Many-Argument Workhorses)** (Impact: 261.8)
    * *Intent:* /** * Create a new CarbonInterval instance. * * @param Closure|DateInterval|string|int|null $years *...
  * `forHumans` **(Many-Argument Workhorses)** (Impact: 141.9)
    * *Intent:* * if int passed, it adds modifiers: * Possible values: * - CarbonInterface::DIFF_ABSOLUTE no modifie...
  * `fromString` **(Compute Cores)** (Impact: 111.5)
    * *Intent:* * * e. g. `1w 3d 4h 32m 23s` is converted to 10 days 4 hours 32 minutes and 23 seconds. * * Special ...
  * `set` **(Many-Argument Workhorses)** (Impact: 63.8)
    * *Intent:* /** * Set a part of the CarbonInterval object. * * @param Unit|string|array $name * @param int $valu...
  * `getForHumansParameters` **(Many-Argument Workhorses)** (Impact: 50.9)
    * *Intent:* /** * @param mixed $syntax * @param mixed $short * @param mixed $parts * @param mixed $options * * @...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 392 instances
* *State Mutation (weighted view):* 1298
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 575`, `structural_boundaries: 405`, `args: 133`, `func_start: 122`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 514`
* *Architecture:* `api: 105`, `import: 39`
* *Defense:* `safety: 101`, `doc: 254`, `immutability_locks: 12`, `cleanup: 21`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.773
  * `Choke Point (Betweenness):` 0.001206 | `Ripple Effect (Closeness):` 0.05771
  * `Imports (Out-Degree: 22):` * we recommend to use the explicit methods ->betweenIncluded() or ->betweenExcluded() instead.
     *
     * @example
     * ```
     * CarbonInterval::hours(48)->between(CarbonInterval::day(), CarbonInterval::days(3), Carbon\Constants\UnitValue, Carbon\Exceptions\BadFluentConstructorException, Carbon\Exceptions\BadFluentSetterException, Carbon\Exceptions\InvalidCastException, Carbon\Exceptions\InvalidFormatException, Carbon\Exceptions\InvalidIntervalException...
  * `Imported By (In-Degree: 69):` (Excluded from Brief to save tokens)

### `src/Carbon/CarbonPeriod.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 1654.62 | **LOC:** 2719 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **21** in-repo importer(s); it depends on **83**; blast radius 4.926; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.5%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (66.8%)
- **Documentation Coverage:** 7.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__call` **(Many-Argument Workhorses)** (Impact: 101.0)
    * *Intent:* /** * Add aliases for setters. * * CarbonPeriod::days(3)->hours(5)->invert() * ->sinceNow()->until('...
  * `__construct` **(Defensive Guards)** (Impact: 84.3)
    * *Intent:* /** * CarbonPeriod constructor. * * @SuppressWarnings(ElseExpression) * * @throws InvalidArgumentExc...
  * `initializeSerialization` **(Defensive Guards)** (Impact: 36.0)
  * `__unserialize` **(Defensive Guards)** (Impact: 30.9)
  * `parseIso8601` **(Stateful Encapsulated Methods)** (Impact: 21.1)
    * *Intent:* /** * Parse given ISO 8601 string into an array of arguments. * * @SuppressWarnings(ElseExpression) ...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 223 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 702
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 391`, `structural_boundaries: 411`, `args: 143`, `func_start: 134`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 256`, `fragile_debt: 3`
* *Architecture:* `api: 109`, `concurrency: 2`, `import: 38`
* *Defense:* `safety: 101`, `doc: 262`, `immutability_locks: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.926
  * `Choke Point (Betweenness):` 0.000734 | `Ripple Effect (Closeness):` 0.04859
  * `Imports (Out-Degree: 19):` $info["\0*\0constructed"], $info['constructed'], $info['include_end_date'], $this->timezoneSetting instanceof DateTimeZone => $this->timezoneSetting->getName(), 'current' => [$this, 'current'], 'include_end_date' => $values['include_end_date'] ?? false, 'include_end_date' => [$this...
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `src/Carbon/Traits/Creator.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 788.56 | **LOC:** 932 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **26**; blast radius 0.778; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.8%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (46.7%)
- **Documentation Coverage:** 7.6923% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create` **(Many-Argument Workhorses)** (Impact: 62.3)
    * *Intent:* * will be 0. * * @param DateTimeInterface|string|int|null $year * @param int|null $month * @param in...
  * `rawCreateFromFormat` **(Many-Argument Workhorses)** (Impact: 53.2)
    * *Intent:* /** * Create a Carbon instance from a specific format. * * @param string $format Datetime format * @...
  * `createFromIsoFormat` **(Many-Argument Workhorses)** (Impact: 48.2)
    * *Intent:* /** * Create a Carbon instance from a specific ISO format (same replacements as ->isoFormat()). * * ...
  * `createSafe` **(Many-Argument Workhorses)** (Impact: 38.2)
    * *Intent:* * will be thrown. * * @param int|null $year * @param int|null $month * @param int|null $day * @param...
  * `__construct` **(Defensive Guards)** (Impact: 31.7)
    * *Intent:* /** * Create a new Carbon instance. * * Please see the testing aids section (specifically static::se...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 113 instances
* *State Mutation (weighted view):* 363
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 138`, `structural_boundaries: 125`, `args: 36`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 137`, `fragile_debt: 1`
* *Architecture:* `api: 24`, `import: 21`
* *Defense:* `safety: 42`, `doc: 30`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.778
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.001009
  * `Imports (Out-Degree: 14):` '', 'now'], Carbon\Carbon, Carbon\CarbonImmutable, Carbon\CarbonInterface, Carbon\Exceptions\InvalidDateException, Carbon\Exceptions\InvalidFormatException, Carbon\Exceptions\InvalidTimeZoneException...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tests/Carbon/DiffTest.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 718.24 | **LOC:** 2223 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.421; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (30.9%), Connectivity (formerly Api Exposure) (13.8%), Complexity Load (formerly Cognitive Load) (7.1%), Dead Code Surface (formerly Dead Code) (4.9%)
- **Documentation Coverage:** 98.5437% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `wrapWithTestNow` **(Compute Cores)** (Impact: 5.4)
  * `testDiffInMonthsWithTimezone` **(Type Conversions)** (Impact: 3.0)
  * `testDiffInHoursFilteredWorkHoursPerWeek` **(Callbacks & Closures)** (Impact: 2.5)
  * `testDiffForHumansWithMagicMethods` **(I/O & Config Routines)** (Impact: 2.5)
  * `testDiffWithTimezones` **(I/O & Config Routines)** (Impact: 2.5)
    * *Intent:* /** * DST will be ignored (i.e. a day will be considered 23 hours/25 hours if it has a DST) * only i...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 186
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 377`, `args: 322`, `func_start: 206`, `class_start: 1`
* *Risk/State:* `state_mutation: 184`, `dead_code: 1`, `fragile_debt: 1`, `unreferenced_by_name: 205`
* *Architecture:* `api: 206`, `import: 11`
* *Defense:* `doc: 4`, `test: 439`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.421
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` Carbon\Carbon, Carbon\CarbonInterface, Carbon\CarbonInterval, Carbon\Exceptions\InvalidFormatException, Carbon\Exceptions\UnknownUnitException, Carbon\Unit, Closure, DateTime...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/Carbon/SettersTest.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 698.76 | **LOC:** 1190 | **CtrlFlow:** 8.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.421; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (83.7%), Complexity Load (formerly Cognitive Load) (38.6%), Connectivity (formerly Api Exposure) (11.2%)
- **Documentation Coverage:** 94.3548% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testSubUnitNoOverflow` **(I/O & Config Routines)** (Impact: 37.6)
  * `failOperation` **(Many-Argument Workhorses)** (Impact: 35.6)
    * *Intent:* /** * @SuppressWarnings(TooManyFields) */
  * `testAddUnitNoOverflow` **(I/O & Config Routines)** (Impact: 30.7)
  * `testSetUnitNoOverflow` **(I/O & Config Routines)** (Impact: 22.6)
  * `testTimeZoneOfUnserialized` **(I/O & Config Routines)** (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 86 instances
* *State Mutation (weighted view):* 399
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 114`, `args: 62`, `func_start: 61`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 227`, `unreferenced_by_name: 58`
* *Architecture:* `api: 60`, `import: 14`
* *Defense:* `safety: 7`, `doc: 12`, `test: 138`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.421
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` BadMethodCallException, Carbon\Carbon, Carbon\Exceptions\InvalidFormatException, Carbon\Exceptions\InvalidIntervalException, Carbon\Exceptions\UnitException, Carbon\Exceptions\UnsupportedUnitException, Carbon\Month, Carbon\Unit...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/CarbonImmutable/DiffTest.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 664.04 | **LOC:** 1965 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.421; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (30.5%), Connectivity (formerly Api Exposure) (14.0%), Complexity Load (formerly Cognitive Load) (6.8%)
- **Documentation Coverage:** 98.995% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `wrapWithTestNow` **(Compute Cores)** (Impact: 5.4)
  * `testDiffInHoursFilteredWorkHoursPerWeek` **(Callbacks & Closures)** (Impact: 2.5)
  * `testDiffForHumansWithMagicMethods` **(I/O & Config Routines)** (Impact: 2.5)
  * `testDiffInHoursWithTimezones` **(I/O & Config Routines)** (Impact: 2.0)
  * `testDiffForHumansWithOptions` **(Annotated & Test Methods)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 158
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 356`, `args: 315`, `func_start: 199`, `class_start: 1`
* *Risk/State:* `state_mutation: 156`, `fragile_debt: 1`, `unreferenced_by_name: 198`
* *Architecture:* `api: 199`, `import: 9`
* *Defense:* `doc: 3`, `test: 388`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.421
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` Carbon\CarbonImmutable, Carbon\CarbonInterface, Carbon\CarbonInterval, Carbon\Exceptions\InvalidFormatException, Carbon\Exceptions\UnknownUnitException, Closure, DateTime, Tests\AbstractTestCase...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Carbon/Traits/Localization.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 633.82 | **LOC:** 748 | **CtrlFlow:** 36.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **11**; blast radius 0.984; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.7%), Complexity Load (formerly Cognitive Load) (41.6%), Connectivity (formerly Api Exposure) (40.6%)
- **Documentation Coverage:** 1.7857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `translateTimeString` **(Many-Argument Workhorses)** (Impact: 80.9)
    * *Intent:* * * @param string $timeString date/time/duration string to translate (may also contain English) * @p...
  * `cleanWordFromTranslationString` **(Stateful Encapsulated Methods)** (Impact: 30.3)
    * *Intent:* /** * Return the word cleaned from its translation codes. * * @param string $word * * @return string...
  * `getTranslationMessageWith` **(Defensive Guards)** (Impact: 21.0)
    * *Intent:* /** * Returns raw translation message for a given key. * * @param TranslatorInterface|null $translat...
  * `translateNumber` **(Compute Cores)** (Impact: 20.5)
    * *Intent:* /** * Returns the alternative number for a given integer if available in the current locale. * * @pa...
  * `setFallbackLocale` **(Defensive Guards)** (Impact: 18.5)
    * *Intent:* /** * Set the fallback locale. * * @see https://symfony.com/doc/current/components/translation.html#...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 88 instances
* *State Mutation (weighted view):* 268
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 121`, `args: 40`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `state_mutation: 92`, `planned_debt: 1`
* *Architecture:* `api: 23`, `import: 11`
* *Defense:* `safety: 35`, `doc: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.984
  * `Choke Point (Betweenness):` 0.000246 | `Ripple Effect (Closeness):` 0.026746
  * `Imports (Out-Degree: 6):` Carbon\CarbonInterface, Carbon\Exceptions\InvalidTypeException, Carbon\Exceptions\NotLocaleAwareException, Carbon\Language, Carbon\Translator, Carbon\TranslatorStrongTypeInterface, Closure, StaticLocalization...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `phpdoc.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 605.38 | **LOC:** 862 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.421; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (37.1%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compileDoc` **(Many-Argument Workhorses)** (Impact: 34.0)
  * `dumpType` **(Defensive Guards)** (Impact: 29.1)
  * `dumpParameter` **(Defensive Guards)** (Impact: 11.8)
  * `cleanClassName` **(Defensive Guards)** (Impact: 10.7)
  * `dumpValue` **(Compute Cores)** (Impact: 5.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 139 instances
* *State Mutation (weighted view):* 488
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 180`, `structural_boundaries: 68`, `args: 12`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 47`, `state_mutation: 210`, `dead_code: 2`
* *Architecture:* `io: 6`, `import: 6`
* *Defense:* `safety: 27`, `doc: 47`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.421
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Carbon\Carbon, Carbon\CarbonImmutable, Carbon\CarbonInterface, Carbon\Factory, Carbon\FactoryImmutable, autoload.php'
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Carbon/Traits/Difference.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 583.44 | **LOC:** 856 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.421; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Guard Balance (formerly Safety Score) (99.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 1.5873% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `diffForHumans` **(Defensive Guards)** (Impact: 33.2)
    * *Intent:* * ⦿ 'minimumUnit' entry determines the smallest unit of time to display can be long or * ` short for...
  * `diffInMonths` **(Many-Argument Workhorses)** (Impact: 24.3)
    * *Intent:* /** * Get the difference in months. * * @param \Carbon\CarbonInterface|\DateTimeInterface|string|nul...
  * `calendar` **(Defensive Guards)** (Impact: 16.8)
    * *Intent:* /** * Returns either day of week + time (e.g. "Last Friday at 3:30 PM") if reference time is within ...
  * `diffInDays` **(Many-Argument Workhorses)** (Impact: 15.2)
    * *Intent:* /** * Get the difference in days. * * @param \Carbon\CarbonInterface|\DateTimeInterface|string|null ...
  * `diffInYears` **(Many-Argument Workhorses)** (Impact: 13.7)
    * *Intent:* /** * Get the difference in years * * @param \Carbon\CarbonInterface|\DateTimeInterface|string|null ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 98 instances
* *State Mutation (weighted view):* 355
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 80`, `args: 36`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `state_mutation: 159`, `fragile_debt: 2`, `unreferenced_by_name: 17`
* *Architecture:* `api: 31`, `import: 10`
* *Defense:* `safety: 11`, `doc: 41`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.421
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` Carbon\Carbon, Carbon\CarbonImmutable, Carbon\CarbonInterface, Carbon\CarbonInterval, Carbon\CarbonPeriod, Carbon\Exceptions\UnknownUnitException, Carbon\Unit, Closure...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Carbon/Traits/Comparison.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 476.28 | **LOC:** 1362 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.421; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Guard Balance (formerly Safety Score) (79.7%), Complexity Load (formerly Cognitive Load) (37.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `is` **(Compute Cores)** (Impact: 32.3)
    * *Intent:* * var_dump(Carbon::parse('2019-06-02 12:23:45')->is('06-02')); // true * var_dump(Carbon::parse('201...
  * `isStartOfDay` **(Many-Argument Workhorses)** (Impact: 15.9)
    * *Intent:* * ``` * Carbon::parse('2019-02-28 00:00:00')->isStartOfDay(); // true * Carbon::parse('2019-02-28 00...
  * `isEndOfDay` **(Compute Cores)** (Impact: 15.8)
    * *Intent:* * Carbon::parse('2019-02-28 23:59:59.123456')->isEndOfDay(); // true * Carbon::parse('2019-02-28 23:...
  * `isStartOfUnit` **(Defensive Guards)** (Impact: 13.1)
    * *Intent:* /** * Check if the instance is start of a given unit (tolerating a given interval). * * @example * `...
  * `isEndOfUnit` **(Defensive Guards)** (Impact: 13.1)
    * *Intent:* /** * Check if the instance is end of a given unit (tolerating a given interval). * * @example * ```...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 43 instances
* *State Mutation (weighted view):* 157
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 194`, `args: 78`, `func_start: 72`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 71`, `unreferenced_by_name: 57`
* *Architecture:* `api: 72`, `import: 17`
* *Defense:* `safety: 14`, `doc: 79`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.421
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` '2018-08-01', * we recommend to use the explicit methods ->betweenIncluded() or ->betweenExcluded() instead.
     *
     * @example
     * ```
     * Carbon::parse('2018-07-25')->between('2018-07-14', BackedEnum, BadMethodCallException, Carbon\CarbonConverterInterface, Carbon\CarbonInterface, Carbon\Exceptions\BadComparisonUnitException, Carbon\FactoryImmutable...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/Carbon/IsTest.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 476.1 | **LOC:** 1481 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 0.421; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (13.7%), Guard Balance (formerly Safety Score) (7.3%), Complexity Load (formerly Cognitive Load) (4.9%)
- **Documentation Coverage:** 96.6216% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testIs` **(I/O & Config Routines)** (Impact: 4.8)
  * `testIsSameMonthOfSameYear` **(I/O & Config Routines)** (Impact: 4.2)
  * `testHasFormatWithModifiers` **(I/O & Config Routines)** (Impact: 3.9)
  * `testIsFebruary29` **(Annotated & Test Methods)** (Impact: 3.4)
  * `testHasFormatWithSingleLetter` **(Annotated & Test Methods)** (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 82
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 207`, `args: 148`, `func_start: 148`, `class_start: 1`
* *Risk/State:* `state_mutation: 52`, `unreferenced_by_name: 147`
* *Architecture:* `api: 148`, `import: 13`
* *Defense:* `safety: 1`, `doc: 7`, `test: 598`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.421
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` BadMethodCallException, Carbon\Carbon, Carbon\CarbonInterval, Carbon\Month, Carbon\Unit, Carbon\WeekDay, DateInterval, DateTime...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/AbstractTestCase.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 453.92 | **LOC:** 502 | **CtrlFlow:** 16.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **166** in-repo importer(s); it depends on **20**; blast radius 22.797; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (95.7%), Complexity Load (formerly Cognitive Load) (22.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (12.4%), Connectivity (formerly Api Exposure) (2.5%)
- **Documentation Coverage:** 71.4286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assertSameIntervals` **(Many-Argument Workhorses)** (Impact: 36.8)
  * `assertCarbonInterval` **(Many-Argument Workhorses)** (Impact: 27.4)
  * `assertCarbon` **(Many-Argument Workhorses)** (Impact: 16.8)
  * `acceptClosuresFrom` **(Stateful Encapsulated Methods)** (Impact: 16.5)
  * `assertCarbonTime` **(Many-Argument Workhorses)** (Impact: 13.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 77 instances
* *State Mutation (weighted view):* 255
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 70`, `args: 26`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `state_mutation: 101`, `unreferenced_by_name: 19`
* *Architecture:* `api: 10`, `import: 20`
* *Defense:* `safety: 19`, `doc: 13`, `test: 13`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 22.797
  * `Choke Point (Betweenness):` 0.001595 | `Ripple Effect (Closeness):` 0.083754
  * `Imports (Out-Degree: 8):` AssertObjectHasPropertyTrait, Carbon\Carbon, Carbon\CarbonImmutable, Carbon\CarbonInterface, Carbon\CarbonInterval, Carbon\CarbonPeriod, Carbon\CarbonPeriodImmutable, Carbon\CarbonTimeZone...
  * `Imported By (In-Degree: 166):` (Excluded from Brief to save tokens)

### `src/Carbon/Factory.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 429.42 | **LOC:** 852 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **9**; blast radius 1.677; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.2%), Connectivity (formerly Api Exposure) (60.2%), Complexity Load (formerly Cognitive Load) (46.1%)
- **Documentation Coverage:** 37.7778% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__call` **(Defensive Guards)** (Impact: 24.9)
  * `setTestNowAndTimezone` **(Defensive Guards)** (Impact: 20.3)
    * *Intent:* * - When a null (or blank string) is passed to the constructor or parse(), ex. new Carbon(null) * - ...
  * `handleTestNowClosure` **(Defensive Guards)** (Impact: 18.9)
  * `setDefaultTimezone` **(Stateful Encapsulated Methods)** (Impact: 15.1)
  * `matchFormatPattern` **(Stateful Encapsulated Methods)** (Impact: 14.8)
    * *Intent:* * given list of pattern replacements. * * @example * ``` * Carbon::hasFormat('11:12:45', 'h:i:s'); /...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 57 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 188
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 92`, `args: 47`, `func_start: 45`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 74`
* *Architecture:* `api: 42`, `import: 9`
* *Defense:* `safety: 39`, `doc: 97`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.677
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.028753
  * `Imports (Out-Degree: 2):` Closure, DateTimeImmutable, DateTimeInterface, DateTimeZone, InvalidArgumentException, ReflectionMethod, RuntimeException, Symfony\Contracts\Translation\TranslatorInterface...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `tests/CarbonImmutable/IsTest.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 421.42 | **LOC:** 1164 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.421; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (13.7%), Guard Balance (formerly Safety Score) (12.5%), Complexity Load (formerly Cognitive Load) (7.2%)
- **Documentation Coverage:** 96.8254% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testIsSameMonthOfSameYear` **(I/O & Config Routines)** (Impact: 4.2)
  * `testHasFormatWithSingleLetter` **(Annotated & Test Methods)** (Impact: 3.1)
  * `testIsSameQuarterFalseWithDateTime` **(Interface Declarations)** (Impact: 2.6)
  * `testIsSameMonth` **(I/O & Config Routines)** (Impact: 2.5)
  * `testIsSameMonthTrueWithDateTime` **(Interface Declarations)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 97
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 182`, `args: 126`, `func_start: 126`, `class_start: 1`
* *Risk/State:* `state_mutation: 63`, `unreferenced_by_name: 125`
* *Architecture:* `api: 126`, `import: 10`
* *Defense:* `doc: 5`, `test: 405`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.421
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` Carbon\CarbonImmutable, Carbon\CarbonInterval, Carbon\Unit, DateInterval, DateTime, InvalidArgumentException, PHPUnit\Framework\Attributes\DataProvider, Tests\AbstractTestCase...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Carbon/Traits/Units.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 420.92 | **LOC:** 473 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.421; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.7%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (60.6%)
- **Documentation Coverage:** 4.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addUTCUnit` **(Many-Argument Workhorses)** (Impact: 64.2)
    * *Intent:* /** * Add seconds to the instance using timestamp. Positive $value travels * forward while negative ...
  * `addUnit` **(Many-Argument Workhorses)** (Impact: 56.2)
    * *Intent:* /** * Add given units to the current instance. */
  * `add` **(Defensive Guards)** (Impact: 21.7)
    * *Intent:* /** * Add given units or interval to the current instance. * * @example $date->add('hour', 3) * @exa...
  * `sub` **(Many-Argument Workhorses)** (Impact: 21.7)
    * *Intent:* /** * Subtract given units or interval to the current instance. * * @example $date->sub('hour', 3) *...
  * `subtract` **(Compute Cores)** (Impact: 8.4)
    * *Intent:* /** * Subtract given units or interval to the current instance. * * @see sub() * * @param Unit|int|s...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 67 instances
* *State Mutation (weighted view):* 210
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 55`, `args: 14`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 76`, `unreferenced_by_name: 7`
* *Architecture:* `api: 12`, `import: 12`
* *Defense:* `safety: 21`, `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.421
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` Carbon\CarbonConverterInterface, Carbon\CarbonInterface, Carbon\CarbonInterval, Carbon\Exceptions\InvalidFormatException, Carbon\Exceptions\InvalidIntervalException, Carbon\Exceptions\UnitException, Carbon\Exceptions\UnsupportedUnitException, Carbon\Unit...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/CarbonPeriod/CreateTest.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 333.72 | **LOC:** 962 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 0.421; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (88.8%), Guard Balance (formerly Safety Score) (49.6%), Complexity Load (formerly Cognitive Load) (23.1%), Connectivity (formerly Api Exposure) (11.1%)
- **Documentation Coverage:** 95.4545% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testEnums` **(I/O & Config Routines)** (Impact: 7.5)
  * `testCast` **(Interface Declarations)** (Impact: 3.7)
  * `testStartAndEndFallback` **(I/O & Config Routines)** (Impact: 3.7)
  * `dataForStartDateAndIntervalAndEndDate` **(I/O & Config Routines)** (Impact: 3.0)
  * `testInstance` **(I/O & Config Routines)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 136
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 152`, `args: 45`, `func_start: 44`, `class_start: 1`
* *Risk/State:* `state_mutation: 112`, `fragile_debt: 3`, `duplicate_logic: 2`, `unreferenced_by_name: 34`
* *Architecture:* `api: 44`, `concurrency: 42`, `import: 19`
* *Defense:* `safety: 1`, `doc: 5`, `test: 139`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.421
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` BadMethodCallException, Carbon\Carbon, Carbon\CarbonImmutable, Carbon\CarbonInterface, Carbon\CarbonInterval, Carbon\CarbonPeriod, Carbon\CarbonPeriodImmutable, Carbon\Exceptions\InvalidPeriodParameterException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/CarbonPeriod/IteratorTest.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 330.64 | **LOC:** 564 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.421; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (89.2%), Complexity Load (formerly Cognitive Load) (28.4%), Concurrency Surface (formerly Concurrency) (24.7%), Connectivity (formerly Api Exposure) (10.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testChangingParametersShouldNotCauseInfiniteLoop` **(I/O & Config Routines)** (Impact: 5.8)
  * `testChangeStartDateDuringIteration` **(I/O & Config Routines)** (Impact: 5.5)
  * `testSkip` **(I/O & Config Routines)** (Impact: 5.5)
  * `testChangeEndDateDuringIteration` **(I/O & Config Routines)** (Impact: 5.4)
  * `testKeepIncreasingRecurrencesDuringIteration` **(I/O & Config Routines)** (Impact: 5.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 55 instances
* *State Mutation (weighted view):* 202
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 75`, `args: 30`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 92`, `unreferenced_by_name: 27`
* *Architecture:* `api: 28`, `concurrency: 5`, `import: 7`
* *Defense:* `doc: 3`, `test: 51`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.421
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` Carbon\Carbon, Carbon\CarbonInterval, Carbon\CarbonPeriod, Generator, PHPUnit\Framework\Attributes\DataProvider, Tests\AbstractTestCase, Tests\CarbonPeriod\Fixtures\CarbonPeriodFactory
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Carbon/AbstractTranslator.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 314.68 | **LOC:** 1300 | **CtrlFlow:** 4.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **18**; blast radius 0.472; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.2%), Connectivity (formerly Api Exposure) (27.1%)
- **Documentation Coverage:** 28.5714% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setLocale` **(Defensive Guards)** (Impact: 22.7)
    * *Intent:* /** * Set the current translator locale and indicate if the source locale file exists * * @param str...
  * `translate` **(Stateful Encapsulated Methods)** (Impact: 16.9)
  * `get` **(Defensive Guards)** (Impact: 10.7)
    * *Intent:* /** * Return a singleton instance of Translator. * * @param string|null $locale optional initial loc...
  * `resetMessages` **(Compute Cores)** (Impact: 10.4)
    * *Intent:* /** * Reset messages of a locale (all locale if no locale passed). * Remove custom messages and relo...
  * `compareChunkLists` **(Stateful Encapsulated Methods)** (Impact: 9.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 44 instances
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 149
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 84`, `args: 33`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 61`
* *Architecture:* `api: 18`, `import: 10`
* *Defense:* `safety: 17`, `doc: 22`, `immutability_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.472
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000505
  * `Imports (Out-Degree: 1):` $file, $this->getLocalesFiles($prefix), ') + 1, ), -4), Carbon\MessageFormatter\MessageFormatterMapper, Closure, ReflectionException...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/Carbon/StartEndOfTest.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 291.84 | **LOC:** 575 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.421; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (76.9%), Connectivity (formerly Api Exposure) (13.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testEndOfQuarter` **(Parameter Forwarders)** (Impact: 2.2)
  * `testStartOfQuarter` **(Parameter Forwarders)** (Impact: 2.0)
  * `testStartOf` **(Interface Declarations)** (Impact: 1.6)
  * `testEndOf` **(Interface Declarations)** (Impact: 1.6)
  * `testAverageWithCloseDates` **(Interface Declarations)** (Impact: 1.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 93`, `args: 81`, `func_start: 81`, `class_start: 1`
* *Risk/State:* `state_mutation: 99`, `unreferenced_by_name: 81`
* *Architecture:* `api: 81`, `import: 5`
* *Defense:* `doc: 1`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.421
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Carbon\Carbon, Carbon\Unit, InvalidArgumentException, PHPUnit\Framework\Attributes\TestWith, Tests\AbstractTestCase
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/Carbon/LocalizationTest.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 264.52 | **LOC:** 1044 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.421; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (52.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (12.4%), Connectivity (formerly Api Exposure) (10.8%), Complexity Load (formerly Cognitive Load) (7.7%)
- **Documentation Coverage:** 95.2381% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testSetLocaleToAutoFallback` **(I/O & Config Routines)** (Impact: 4.0)
  * `testSetLocaleToAutoFromUnsupportedLocale` **(I/O & Config Routines)** (Impact: 3.7)
  * `testShortMonthNameInFormat` **(I/O & Config Routines)** (Impact: 3.6)
  * `testFallbackLocales` **(I/O & Config Routines)** (Impact: 3.5)
  * `testSetLocaleWithMalformedLocale` **(Compute Cores)** (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 120
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 78`, `args: 43`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `state_mutation: 108`, `planned_debt: 1`, `unreferenced_by_name: 41`
* *Architecture:* `api: 42`, `import: 16`
* *Defense:* `safety: 6`, `doc: 24`, `test: 91`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.421
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` Carbon\Carbon, Carbon\CarbonInterface, Carbon\CarbonInterval, Carbon\Language, Carbon\Translator, InvalidArgumentException, PHPUnit\Framework\Attributes\DataProvider, PHPUnit\Framework\Attributes\Group...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/CarbonPeriod/SettersTest.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 239.16 | **LOC:** 484 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.421; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (82.9%), Complexity Load (formerly Cognitive Load) (39.7%), Connectivity (formerly Api Exposure) (10.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testFluentSetters` **(I/O & Config Routines)** (Impact: 9.7)
  * `testInvertDateInterval` **(I/O & Config Routines)** (Impact: 4.2)
  * `testSetDateClass` **(I/O & Config Routines)** (Impact: 3.4)
  * `testToggleOptionsOnAndOff` **(I/O & Config Routines)** (Impact: 2.4)
  * `testToggleOptions` **(I/O & Config Routines)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 152
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 76`, `args: 26`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `state_mutation: 120`, `planned_debt: 1`, `unreferenced_by_name: 26`
* *Architecture:* `api: 26`, `import: 8`
* *Defense:* `doc: 1`, `test: 55`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.421
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` Carbon\Carbon, Carbon\CarbonImmutable, Carbon\CarbonInterval, DateInterval, DateTime, InvalidArgumentException, Tests\AbstractTestCase, Tests\CarbonPeriod\Fixtures\AbstractCarbon
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sponsors.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 235.98 | **LOC:** 269 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.421; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.5%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getOpenCollectiveSponsors` **(I/O & Config Routines)** (Impact: 77.2)
  * `getMaxHistoryMonthsByAmount` **(Compute Cores)** (Impact: 4.8)
  * `getHtmlAttribute` **(Type Conversions)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 49 instances
* *State Mutation (weighted view):* 148
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 19`, `args: 7`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 50`
* *Architecture:* `io: 3`, `import: 2`
* *Defense:* `safety: 8`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.421
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Carbon\CarbonImmutable, autoload.php',  ceil($createdAt->floatDiffInMonths()))
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/CarbonImmutable/StartEndOfTest.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 230.66 | **LOC:** 447 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.421; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (77.5%), Connectivity (formerly Api Exposure) (13.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testEndOfQuarter` **(Parameter Forwarders)** (Impact: 2.2)
  * `testStartOfQuarter` **(Parameter Forwarders)** (Impact: 2.0)
  * `testAverageWithCloseDates` **(Interface Declarations)** (Impact: 1.4)
  * `testAverageWithFarDates` **(Interface Declarations)** (Impact: 1.4)
  * `testStartOfDay` **(Interface Declarations)** (Impact: 1.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 72`, `args: 64`, `func_start: 64`, `class_start: 1`
* *Risk/State:* `state_mutation: 79`, `unreferenced_by_name: 64`
* *Architecture:* `api: 64`, `import: 3`
* *Defense:* `doc: 1`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.421
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Carbon\CarbonImmutable, PHPUnit\Framework\Attributes\TestWith, Tests\AbstractTestCase
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/Carbon/GettersTest.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 229.14 | **LOC:** 549 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.421; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (27.8%), Connectivity (formerly Api Exposure) (13.0%)
- **Documentation Coverage:** 96.6102% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testMillenniumGetter` **(I/O & Config Routines)** (Impact: 2.0)
  * `testQuarterFirstOfMonth` **(Annotated & Test Methods)** (Impact: 2.0)
  * `testQuarterMiddleOfMonth` **(Annotated & Test Methods)** (Impact: 2.0)
  * `testQuarterLastOfMonth` **(Annotated & Test Methods)** (Impact: 2.0)
  * `testGetUtcTrue` **(Annotated & Test Methods)** (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 69`, `args: 59`, `func_start: 59`, `class_start: 1`
* *Risk/State:* `state_mutation: 77`, `unreferenced_by_name: 58`
* *Architecture:* `api: 59`, `import: 4`
* *Defense:* `doc: 4`, `test: 156`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.421
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Carbon\Carbon, InvalidArgumentException, PHPUnit\Framework\Attributes\DataProvider, Tests\AbstractTestCase
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/CarbonImmutable/LocalizationTest.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 228.32 | **LOC:** 927 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.421; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (24.6%), Connectivity (formerly Api Exposure) (10.4%), Complexity Load (formerly Cognitive Load) (6.8%)
- **Documentation Coverage:** 97.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testSetLocaleToAutoFallback` **(I/O & Config Routines)** (Impact: 4.0)
  * `testSetLocaleToAutoFromUnsupportedLocale` **(I/O & Config Routines)** (Impact: 3.7)
  * `testShortMonthNameInFormat` **(I/O & Config Routines)** (Impact: 3.6)
  * `testFallbackLocales` **(I/O & Config Routines)** (Impact: 3.5)
  * `testSetLocaleWithMalformedLocale` **(Compute Cores)** (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 100
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 69`, `args: 38`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `state_mutation: 96`, `planned_debt: 1`, `unreferenced_by_name: 37`
* *Architecture:* `api: 37`, `import: 14`
* *Defense:* `safety: 6`, `doc: 23`, `test: 85`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.421
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` Carbon\CarbonImmutable, Carbon\CarbonInterval, Carbon\Language, Carbon\Translator, InvalidArgumentException, PHPUnit\Framework\Attributes\DataProvider, PHPUnit\Framework\Attributes\Group, PHPUnit\Framework\Attributes\TestWith...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/Carbon/CarbonInterval.php` -> **kylekatarnls** (100.0% isolated ownership) | Magnitude: 2800.76
- `src/Carbon/CarbonPeriod.php` -> **kylekatarnls** (100.0% isolated ownership) | Magnitude: 1654.62
- `src/Carbon/Traits/Creator.php` -> **Sam Anglin** (100.0% isolated ownership) | Magnitude: 788.56
- `src/Carbon/Traits/Localization.php` -> **kylekatarnls** (100.0% isolated ownership) | Magnitude: 633.82
- `phpdoc.php` -> **kylekatarnls** (100.0% isolated ownership) | Magnitude: 605.38

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/Carbon/CarbonInterval.php` -> **Severity: 0.121** (Bridge: 0.0012 * Flux: 100.0%)
- `src/Carbon/CarbonPeriod.php` -> **Severity: 0.073** (Bridge: 0.0007 * Flux: 100.0%)
- `src/Carbon/Traits/Options.php` -> **Severity: 0.034** (Bridge: 0.0003 * Flux: 100.0%)
- `src/Carbon/Traits/Localization.php` -> **Severity: 0.025** (Bridge: 0.0002 * Flux: 100.0%)
- `src/Carbon/CarbonTimeZone.php` -> **Severity: 0.011** (Bridge: 0.0001 * Flux: 99.9999%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `tests/AbstractTestCase.php` -> **Severity: 8.019** (Embedded: 0.0838 * Error Risk: 95.739%)
- `src/Carbon/CarbonInterval.php` -> **Severity: 5.553** (Embedded: 0.0577 * Error Risk: 96.2177%)
- `src/Carbon/CarbonPeriod.php` -> **Severity: 4.204** (Embedded: 0.0486 * Error Risk: 86.5269%)
- `src/Carbon/CarbonTimeZone.php` -> **Severity: 3.772** (Embedded: 0.0439 * Error Risk: 85.8857%)
- `src/Carbon/CarbonPeriodImmutable.php` -> **Severity: 3.118** (Embedded: 0.0495 * Error Risk: 62.9816%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tests/AbstractTestCase.php` -> **Severity: 1628.358** (Blast Radius: 22.797 * Doc Risk: 71.4286%)
- `src/Carbon/CarbonImmutable.php` -> **Severity: 439.8** (Blast Radius: 13.194 * Doc Risk: 33.3333%)
- `src/Carbon/CarbonInterval.php` -> **Severity: 153.102** (Blast Radius: 11.773 * Doc Risk: 13.0045%)
- `src/Carbon/Traits/LocalFactory.php` -> **Severity: 148.0** (Blast Radius: 2.96 * Doc Risk: 50.0%)
- `tests/AbstractTestCaseWithOldNow.php` -> **Severity: 147.6** (Blast Radius: 1.476 * Doc Risk: 100.0%)

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
