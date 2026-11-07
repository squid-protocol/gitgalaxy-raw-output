# ARCHITECTURAL_BRIEF: Carbon
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/briannesbitt/Carbon.git` |
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
- **Scope:** 1999 analyzed artifact(s), 168637 LOC.
- **Load-bearing artifact:** `tests/AbstractTestCase.php` -- 166 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/Carbon/Traits/Date.php` -- pulls in 47 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/Carbon/CarbonInterface.php` at magnitude 12178.12 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 1999 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 35 |
| Total LOC | 168637 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 98.3% |
| Dominant Lang | PHP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3929 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3458 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.1646 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 17 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PHP | 1977 | 168022 | 98.9% |
| YAML | 13 | 486 | 0.7% |
| MARKDOWN | 4 | 0 | 0.2% |
| XML | 3 | 0 | 0.2% |
| BATCH | 1 | 4 | 0.1% |
| JSON | 1 | 125 | 0.1% |

## 4.1 SOURCE ENCODINGS
All 1999 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 62%, Data / Markup / Trivial 24%, Interface Declarations Files 7%, Large Core Modules 2%, Large Core Modules (2) 1%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1995 | 99.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 4 | 0.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 35*

**Composition by Extension & Reason:**
- `.php`: 10x Excluded (Saturation: Line 28 exceeds 500 chars), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 26 exceeds 500 chars)
- `no_extension`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.neon`: 4x Excluded (Unsupported Extension: '.neon')
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.dist`: 1x Excluded (Unsupported Extension: '.dist')
- `.txt`: 1x Excluded (Binary Format Detected)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 70.9 | 1.8 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 94.7 | 8.8 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 1.1 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 3.9 | 3.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 0.6 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 3.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 14.9 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 4.2 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 76.8 | 0.5 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 11.8 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1717 | 193 | 0 | `src/Carbon/CarbonInterval.php` |
| cleanup | 43 | 10 | 0 | `src/Carbon/CarbonInterval.php` |
| guards | 3045 | 998 | 2 | `src/Carbon/CarbonPeriod.php` |
| danger | 358 | 75 | 0 | `phpdoc.php` |
| concurrency | 398 | 30 | 0 | `tests/Carbon/IssetTest.php` |
| connectivity | 6096 | 1115 | 3 | `src/Carbon/CarbonInterface.php` |
| io | 18 | 7 | 0 | `phpdoc.php` |
| crypto | 0 | 0 | 0 | - |
| ipc | 27 | 4 | 0 | `build.php` |
| time | 411 | 67 | 0 | `tests/CarbonImmutable/IsTest.php` |
| serialization | 80 | 17 | 0 | `tests/Carbon/SerializationTest.php` |
| regex | 143 | 38 | 0 | `phpdoc.php` |
| events | 26 | 10 | 0 | `tests/Laravel/ServiceProviderTest.php` |
| tests | 7509 | 1015 | 1 | `tests/Carbon/IsTest.php` |
| docs | 7330 | 1984 | 1 | `src/Carbon/CarbonInterface.php` |
| debt | 152 | 66 | 0 | `tests/CarbonInterval/ComparisonTest.php` |
| mutation | 9780 | 1175 | 4 | `src/Carbon/CarbonInterval.php` |
| dead_code | 3084 | 219 | 1 | `tests/Carbon/DiffTest.php` |
| credential | 1 | 1 | 0 | `phpdoc.php` |
| threat | 127 | 77 | 0 | `tests/Localization/ShnMmTest.php` |
| ml_ai | 128 | 22 | 0 | `tests/Localization/ShiLatnTest.php` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `phpdoc.php` (Hits: 6)
- `.github/workflows/laravel.yml` (Hits: 3)
- `sponsors.php` (Hits: 3)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **AbstractTestCase.php** (`tests/AbstractTestCase.php`) — 166 inbound connections
2. **Carbon.php** (`src/Carbon/Carbon.php`) — 103 inbound connections
3. **CarbonImmutable.php** (`src/Carbon/CarbonImmutable.php`) — 81 inbound connections
4. **CarbonInterval.php** (`src/Carbon/CarbonInterval.php`) — 71 inbound connections
5. **CarbonInterface.php** (`src/Carbon/CarbonInterface.php`) — 62 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **Date.php** (`src/Carbon/Traits/Date.php`) — 47 outbound dependencies
2. **CarbonInterval.php** (`src/Carbon/CarbonInterval.php`) — 37 outbound dependencies
3. **CarbonPeriod.php** (`src/Carbon/CarbonPeriod.php`) — 35 outbound dependencies
4. **CarbonInterface.php** (`src/Carbon/CarbonInterface.php`) — 23 outbound dependencies
5. **Creator.php** (`src/Carbon/Traits/Creator.php`) — 21 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `forHumans` **(Many-Argument Workhorses)** (@ `src/Carbon/CarbonInterval.php`) -> Impact: **141.9** | LOC: 200
  * *Intent:* * if int passed, it adds modifiers: * Possible values: * - CarbonInterface::DIFF_ABSOLUTE no modifiers * - CarbonInterface::DIFF_RELATIVE_TO_NOW add a...
- `__construct` **(Many-Argument Workhorses)** (@ `src/Carbon/CarbonInterval.php`) -> Impact: **129.8** | LOC: 135
  * *Intent:* /** * Create a new CarbonInterval instance. * * @param Closure|DateInterval|string|int|null $years * @param int|float|null $months * @param int|float|...
- `fromString` **(Compute Cores)** (@ `src/Carbon/CarbonInterval.php`) -> Impact: **107.2** | LOC: 165
  * *Intent:* * * e. g. `1w 3d 4h 32m 23s` is converted to 10 days 4 hours 32 minutes and 23 seconds. * * Special cases: * - An empty string will return a zero inte...
- `set` **(Many-Argument Workhorses)** (@ `src/Carbon/Traits/Date.php`) -> Impact: **103.2** | LOC: 158
  * *Intent:* /** * Set a part of the Carbon object. * * @throws ImmutableException|UnknownSetterException * * @return $this */
- `__call` **(Many-Argument Workhorses)** (@ `src/Carbon/CarbonPeriod.php`) -> Impact: **101.0** | LOC: 149
  * *Intent:* /** * Add aliases for setters. * * CarbonPeriod::days(3)->hours(5)->invert() * ->sinceNow()->until('2010-01-10') * ->filter(...) * ->count() * * Note:...
- `get` **(Compute Cores)** (@ `src/Carbon/Traits/Date.php`) -> Impact: **88.2** | LOC: 265
  * *Intent:* /** * Get a part of the Carbon object. * * @throws UnknownGetterException * * @return string|int|bool|DateTimeZone */
- `translateTimeString` **(Many-Argument Workhorses)** (@ `src/Carbon/Traits/Localization.php`) -> Impact: **76.5** | LOC: 98
  * *Intent:* * * @param string $timeString date/time/duration string to translate (may also contain English) * @param string|null $from input locale of the $timeSt...
- `__construct` **(Defensive Guards)** (@ `src/Carbon/CarbonPeriod.php`) -> Impact: **75.8** | LOC: 130
  * *Intent:* /** * CarbonPeriod constructor. * * @SuppressWarnings(ElseExpression) * * @throws InvalidArgumentException */
- `getOpenCollectiveSponsors` **(I/O & Config Routines)** (@ `sponsors.php`) -> Impact: **66.2** | LOC: 223
- `set` **(Many-Argument Workhorses)** (@ `src/Carbon/CarbonInterval.php`) -> Impact: **63.8** | LOC: 98
  * *Intent:* /** * Set a part of the CarbonInterval object. * * @param Unit|string|array $name * @param int $value * * @throws UnknownSetterException * * @return $...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/Carbon` | 20 | 18085.86 | 30.65% | 0.5% |
| `tests/Localization` | 828 | 15945.72 | 0.0% | 0.0% |
| `src/Carbon/Lang` | 803 | 10907.04 | 0.54% | 0.03% |
| `src/Carbon/Traits` | 28 | 5829.26 | 24.59% | 1.32% |
| `tests/Carbon` | 46 | 5467.42 | 5.98% | 0.0% |
| `tests/CarbonImmutable` | 45 | 4471.46 | 3.97% | 0.0% |
| `tests/CarbonPeriod` | 16 | 1900.56 | 15.61% | 0.0% |
| `tests/CarbonInterval` | 27 | 1512.3 | 4.23% | 0.0% |
| `__monolith__` | 9 | 948.08 | 17.99% | 0.0% |
| `tests/Jenssegers` | 11 | 591.18 | 9.43% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/Carbon/PHPStan/MacroMethodReflection.php` -> **99.9995%** Exposure
- `lazy/Carbon/MessageFormatter/MessageFormatterMapperWeakType.php` -> **81.7574%** Exposure
- `lazy/Carbon/TranslatorStrongType.php` -> **81.7574%** Exposure
- `lazy/Carbon/MessageFormatter/MessageFormatterMapperStrongType.php` -> **37.7541%** Exposure
- `lazy/Carbon/TranslatorWeakType.php` -> **37.7541%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `build.php` -> **100.0%** Exposure
- `phpdoc.php` -> **100.0%** Exposure
- `sponsors.php` -> **100.0%** Exposure
- `src/Carbon/CarbonInterface.php` -> **100.0%** Exposure
- `src/Carbon/CarbonInterval.php` -> **100.0%** Exposure
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
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2665` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/Carbon/CarbonInterface.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 5.374)
- **Top Global Matches:** file_cluster_13: 5.374, file_cluster_17: 5.64, file_cluster_2: 5.767
- **Magnitude:** 12178.12 | **LOC:** 4849 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **62** in-repo importer(s); it depends on **23**; blast radius 15.371; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (78.8%), Complexity Load (formerly Cognitive Load) (34.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 110 instances
* *State Mutation (weighted view):* 521
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 404`, `args: 376`, `func_start: 376`, `class_start: 1`
* *Risk/State:* `state_mutation: 301`
* *Architecture:* `api: 376`, `import: 23`
* *Defense:* `safety: 1`, `doc: 1182`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 15.371
  * `Choke Point (Betweenness):` 0.000532 | `Ripple Effect (Closeness):` 0.066422
  * `Imports (Out-Degree: 12):` BadMethodCallException, Carbon\Constants\DiffOptions, Carbon\Constants\Format, Carbon\Constants\TranslationOptions, Carbon\Constants\UnitValue, Carbon\Exceptions\BadComparisonUnitException, Carbon\Exceptions\ImmutableException, Carbon\Exceptions\InvalidDateException...
  * `Imported By (In-Degree: 62):` (Excluded from Brief to save tokens)

### `src/Carbon/CarbonInterval.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.377)
- **Top Global Matches:** file_cluster_4: 5.377, file_cluster_15: 9.51, file_cluster_16: 9.669
- **Magnitude:** 2634.76 | **LOC:** 3574 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **71** in-repo importer(s); it depends on **37**; blast radius 12.734; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (75.8%), Guard Balance (formerly Safety Score) (74.4%)
- **Documentation Coverage:** 13.0045% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `forHumans` **(Many-Argument Workhorses)** (Impact: 141.9)
    * *Intent:* * if int passed, it adds modifiers: * Possible values: * - CarbonInterface::DIFF_ABSOLUTE no modifie...
  * `__construct` **(Many-Argument Workhorses)** (Impact: 129.8)
    * *Intent:* /** * Create a new CarbonInterval instance. * * @param Closure|DateInterval|string|int|null $years *...
  * `fromString` **(Compute Cores)** (Impact: 107.2)
    * *Intent:* * * e. g. `1w 3d 4h 32m 23s` is converted to 10 days 4 hours 32 minutes and 23 seconds. * * Special ...
  * `set` **(Many-Argument Workhorses)** (Impact: 63.8)
    * *Intent:* /** * Set a part of the CarbonInterval object. * * @param Unit|string|array $name * @param int $valu...
  * `getForHumansParameters` **(Many-Argument Workhorses)** (Impact: 50.9)
    * *Intent:* /** * @param mixed $syntax * @param mixed $short * @param mixed $parts * @param mixed $options * * @...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 387 instances
* *State Mutation (weighted view):* 1288
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 516`, `structural_boundaries: 405`, `args: 133`, `func_start: 122`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 514`
* *Architecture:* `api: 105`, `import: 39`
* *Defense:* `safety: 101`, `doc: 254`, `immutability_locks: 12`, `cleanup: 21`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.734
  * `Choke Point (Betweenness):` 0.001279 | `Ripple Effect (Closeness):` 0.053759
  * `Imports (Out-Degree: 25):` Carbon\Constants\UnitValue, Carbon\Exceptions\BadFluentConstructorException, Carbon\Exceptions\BadFluentSetterException, Carbon\Exceptions\InvalidCastException, Carbon\Exceptions\InvalidFormatException, Carbon\Exceptions\InvalidIntervalException, Carbon\Exceptions\OutOfRangeException, Carbon\Exceptions\ParseErrorException...
  * `Imported By (In-Degree: 71):` (Excluded from Brief to save tokens)

### `src/Carbon/CarbonPeriod.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.593)
- **Top Global Matches:** file_cluster_15: 7.593, file_cluster_16: 7.648, file_cluster_4: 7.733
- **Magnitude:** 1643.72 | **LOC:** 2719 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **22** in-repo importer(s); it depends on **35**; blast radius 4.744; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (67.1%), Guard Balance (formerly Safety Score) (64.9%)
- **Documentation Coverage:** 7.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__call` **(Many-Argument Workhorses)** (Impact: 101.0)
    * *Intent:* /** * Add aliases for setters. * * CarbonPeriod::days(3)->hours(5)->invert() * ->sinceNow()->until('...
  * `__construct` **(Defensive Guards)** (Impact: 75.8)
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
* *Structure:* `branch: 383`, `structural_boundaries: 411`, `args: 143`, `func_start: 134`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 256`, `fragile_debt: 3`
* *Architecture:* `api: 109`, `concurrency: 2`, `import: 38`
* *Defense:* `safety: 101`, `doc: 262`, `immutability_locks: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.744
  * `Choke Point (Betweenness):` 0.000818 | `Ripple Effect (Closeness):` 0.052738
  * `Imports (Out-Degree: 22):` Carbon\Constants\UnitValue, Carbon\Exceptions\EndLessPeriodException, Carbon\Exceptions\InvalidCastException, Carbon\Exceptions\InvalidIntervalException, Carbon\Exceptions\InvalidPeriodDateException, Carbon\Exceptions\InvalidPeriodParameterException, Carbon\Exceptions\NotACarbonClassException, Carbon\Exceptions\NotAPeriodException...
  * `Imported By (In-Degree: 22):` (Excluded from Brief to save tokens)

### `src/Carbon/Traits/Date.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.065)
- **Top Global Matches:** file_cluster_4: 7.065, file_cluster_15: 7.714, file_cluster_16: 7.896
- **Magnitude:** 1360.0 | **LOC:** 2974 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **47**; blast radius 27.384; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (60.9%), Connectivity (formerly Api Exposure) (48.1%), Complexity Load (formerly Cognitive Load) (46.4%)
- **Documentation Coverage:** 15.2866% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `set` **(Many-Argument Workhorses)** (Impact: 103.2)
    * *Intent:* /** * Set a part of the Carbon object. * * @throws ImmutableException|UnknownSetterException * * @re...
  * `get` **(Compute Cores)** (Impact: 88.2)
    * *Intent:* /** * Get a part of the Carbon object. * * @throws UnknownGetterException * * @return string|int|boo...
  * `isoFormat` **(Many-Argument Workhorses)** (Impact: 47.7)
    * *Intent:* /** * Format in the current language using ISO replacement patterns. * * @param string|null $origina...
  * `translatedFormat` **(Compute Cores)** (Impact: 22.0)
    * *Intent:* /** * Format as ->format() do (using date replacements patterns from https://php.net/manual/en/funct...
  * `getTranslatedFormByRegExp` **(Stateful Encapsulated Methods)** (Impact: 18.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 190 instances
* *State Mutation (weighted view):* 600
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 288`, `structural_boundaries: 330`, `args: 111`, `func_start: 84`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 220`
* *Architecture:* `api: 63`, `concurrency: 3`, `import: 47`
* *Defense:* `safety: 66`, `doc: 941`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 27.384
  * `Choke Point (Betweenness):` 0.002254 | `Ripple Effect (Closeness):` 0.050555
  * `Imports (Out-Degree: 36):` BadMethodCallException, Boundaries, Carbon\Carbon, Carbon\CarbonInterface, Carbon\CarbonPeriod, Carbon\CarbonTimeZone, Carbon\Exceptions\BadComparisonUnitException, Carbon\Exceptions\ImmutableException...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/Carbon/Traits/Creator.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.238)
- **Top Global Matches:** file_cluster_4: 5.238, file_cluster_6: 9.284, file_cluster_16: 11.809
- **Magnitude:** 749.66 | **LOC:** 932 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **21**; blast radius 1.329; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.5%), Connectivity (formerly Api Exposure) (48.0%)
- **Documentation Coverage:** 7.6923% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create` **(Many-Argument Workhorses)** (Impact: 62.3)
    * *Intent:* * will be 0. * * @param DateTimeInterface|string|int|null $year * @param int|null $month * @param in...
  * `createSafe` **(Many-Argument Workhorses)** (Impact: 38.2)
    * *Intent:* * will be thrown. * * @param int|null $year * @param int|null $month * @param int|null $day * @param...
  * `rawCreateFromFormat` **(Many-Argument Workhorses)** (Impact: 35.2)
    * *Intent:* /** * Create a Carbon instance from a specific format. * * @param string $format Datetime format * @...
  * `createFromIsoFormat` **(Many-Argument Workhorses)** (Impact: 33.5)
    * *Intent:* /** * Create a Carbon instance from a specific ISO format (same replacements as ->isoFormat()). * * ...
  * `__construct` **(Defensive Guards)** (Impact: 31.7)
    * *Intent:* /** * Create a new Carbon instance. * * Please see the testing aids section (specifically static::se...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 112 instances
* *State Mutation (weighted view):* 361
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 125`, `args: 36`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 137`, `fragile_debt: 1`
* *Architecture:* `api: 24`, `import: 21`
* *Defense:* `safety: 42`, `doc: 30`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.329
  * `Choke Point (Betweenness):` 7e-05 | `Ripple Effect (Closeness):` 0.036136
  * `Imports (Out-Degree: 15):` Carbon\Carbon, Carbon\CarbonImmutable, Carbon\CarbonInterface, Carbon\Exceptions\InvalidDateException, Carbon\Exceptions\InvalidFormatException, Carbon\Exceptions\InvalidTimeZoneException, Carbon\Exceptions\OutOfRangeException, Carbon\Exceptions\UnitException...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `tests/Carbon/DiffTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 9.486)
- **Top Global Matches:** file_cluster_10: 9.486, file_cluster_11: 10.338, file_cluster_15: 10.815
- **Magnitude:** 718.24 | **LOC:** 2223 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.37; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (43.2%), Connectivity (formerly Api Exposure) (13.8%), Complexity Load (formerly Cognitive Load) (7.1%)
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
* *Risk/State:* `state_mutation: 184`, `fragile_debt: 1`, `unreferenced_by_name: 205`
* *Architecture:* `api: 206`, `import: 11`
* *Defense:* `doc: 4`, `test: 439`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.37
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` Carbon\Carbon, Carbon\CarbonInterface, Carbon\CarbonInterval, Carbon\Exceptions\InvalidFormatException, Carbon\Exceptions\UnknownUnitException, Carbon\Unit, Closure, DateTime...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/Carbon/SettersTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.019)
- **Top Global Matches:** file_cluster_4: 8.019, file_cluster_11: 8.055, file_cluster_12: 8.645
- **Magnitude:** 687.56 | **LOC:** 1190 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.37; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (63.1%), Complexity Load (formerly Cognitive Load) (38.6%), Connectivity (formerly Api Exposure) (11.2%)
- **Documentation Coverage:** 94.3548% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testSubUnitNoOverflow` **(I/O & Config Routines)** (Impact: 37.6)
  * `testAddUnitNoOverflow` **(I/O & Config Routines)** (Impact: 30.7)
  * `failOperation` **(Many-Argument Workhorses)** (Impact: 24.4)
    * *Intent:* /** * @SuppressWarnings(TooManyFields) */
  * `testSetUnitNoOverflow` **(I/O & Config Routines)** (Impact: 22.6)
  * `testTimeZoneOfUnserialized` **(I/O & Config Routines)** (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 86 instances
* *State Mutation (weighted view):* 399
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 114`, `args: 62`, `func_start: 61`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 227`, `unreferenced_by_name: 58`
* *Architecture:* `api: 60`, `import: 14`
* *Defense:* `safety: 7`, `doc: 12`, `test: 138`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.37
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` BadMethodCallException, Carbon\Carbon, Carbon\Exceptions\InvalidFormatException, Carbon\Exceptions\InvalidIntervalException, Carbon\Exceptions\UnitException, Carbon\Exceptions\UnsupportedUnitException, Carbon\Month, Carbon\Unit...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/CarbonImmutable/DiffTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 9.168)
- **Top Global Matches:** file_cluster_10: 9.168, file_cluster_11: 9.999, file_cluster_15: 10.66
- **Magnitude:** 664.04 | **LOC:** 1965 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.37; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (43.1%), Connectivity (formerly Api Exposure) (14.0%), Complexity Load (formerly Cognitive Load) (6.8%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.37
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` Carbon\CarbonImmutable, Carbon\CarbonInterface, Carbon\CarbonInterval, Carbon\Exceptions\InvalidFormatException, Carbon\Exceptions\UnknownUnitException, Closure, DateTime, Tests\AbstractTestCase...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `phpdoc.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 10.99)
- **Top Global Matches:** file_cluster_6: 10.99, file_cluster_4: 11.289, file_cluster_12: 14.806
- **Magnitude:** 589.18 | **LOC:** 862 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.37; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (35.2%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compileDoc` **(Many-Argument Workhorses)** (Impact: 34.0)
  * `dumpType` **(Defensive Guards)** (Impact: 27.1)
  * `dumpParameter` **(Defensive Guards)** (Impact: 11.8)
  * `cleanClassName` **(Defensive Guards)** (Impact: 6.5)
  * `dumpValue` **(Compute Cores)** (Impact: 5.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 134 instances
* *State Mutation (weighted view):* 478
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 145`, `structural_boundaries: 68`, `args: 12`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 47`, `state_mutation: 210`
* *Architecture:* `io: 6`, `import: 6`
* *Defense:* `safety: 27`, `doc: 47`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.37
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` Carbon\Carbon, Carbon\CarbonImmutable, Carbon\CarbonInterface, Carbon\Factory, Carbon\FactoryImmutable, autoload.php'
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Carbon/Traits/Localization.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.604)
- **Top Global Matches:** file_cluster_4: 7.604, file_cluster_15: 8.054, file_cluster_16: 8.102
- **Magnitude:** 587.52 | **LOC:** 748 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **11**; blast radius 0.902; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (70.3%), Connectivity (formerly Api Exposure) (40.6%), Complexity Load (formerly Cognitive Load) (39.6%)
- **Documentation Coverage:** 1.7857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `translateTimeString` **(Many-Argument Workhorses)** (Impact: 76.5)
    * *Intent:* * * @param string $timeString date/time/duration string to translate (may also contain English) * @p...
  * `getTranslationMessageWith` **(Defensive Guards)** (Impact: 21.0)
    * *Intent:* /** * Returns raw translation message for a given key. * * @param TranslatorInterface|null $translat...
  * `translateNumber` **(Compute Cores)** (Impact: 20.5)
    * *Intent:* /** * Returns the alternative number for a given integer if available in the current locale. * * @pa...
  * `locale` **(Defensive Guards)** (Impact: 15.2)
    * *Intent:* /** * Get/set the locale for the current instance. * * @param string|null $locale * @param string .....
  * `setFallbackLocale` **(Defensive Guards)** (Impact: 14.3)
    * *Intent:* /** * Set the fallback locale. * * @see https://symfony.com/doc/current/components/translation.html#...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 86 instances
* *State Mutation (weighted view):* 264
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 121`, `args: 40`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `state_mutation: 92`, `planned_debt: 1`
* *Architecture:* `api: 23`, `import: 11`
* *Defense:* `safety: 35`, `doc: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.902
  * `Choke Point (Betweenness):` 0.000252 | `Ripple Effect (Closeness):` 0.032658
  * `Imports (Out-Degree: 7):` Carbon\CarbonInterface, Carbon\Exceptions\InvalidTypeException, Carbon\Exceptions\NotLocaleAwareException, Carbon\Language, Carbon\Translator, Carbon\TranslatorStrongTypeInterface, Closure, StaticLocalization...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Carbon/Traits/Difference.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.507)
- **Top Global Matches:** file_cluster_15: 5.507, file_cluster_16: 7.339, file_cluster_11: 7.441
- **Magnitude:** 583.44 | **LOC:** 856 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 1.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.9%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (56.6%)
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
* *Risk/State:* `state_mutation: 159`, `fragile_debt: 2`
* *Architecture:* `api: 31`, `import: 10`
* *Defense:* `safety: 11`, `doc: 41`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.015
  * `Choke Point (Betweenness):` 1.7e-05 | `Ripple Effect (Closeness):` 0.035966
  * `Imports (Out-Degree: 7):` Carbon\Carbon, Carbon\CarbonImmutable, Carbon\CarbonInterface, Carbon\CarbonInterval, Carbon\CarbonPeriod, Carbon\Exceptions\UnknownUnitException, Carbon\Unit, Closure...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/Carbon/IsTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 7.642)
- **Top Global Matches:** file_cluster_11: 7.642, file_cluster_13: 8.579, file_cluster_15: 9.12
- **Magnitude:** 468.7 | **LOC:** 1481 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 0.37; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (29.8%), Connectivity (formerly Api Exposure) (13.7%), Complexity Load (formerly Cognitive Load) (4.7%)
- **Documentation Coverage:** 96.6216% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testIs` **(I/O & Config Routines)** (Impact: 4.8)
  * `testIsSameMonthOfSameYear` **(I/O & Config Routines)** (Impact: 4.2)
  * `testIsFebruary29` **(Annotated & Test Methods)** (Impact: 3.4)
  * `testIsSameQuarterFalseWithDateTime` **(Interface Declarations)** (Impact: 2.6)
  * `testIsSameMonth` **(I/O & Config Routines)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 78
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 207`, `args: 148`, `func_start: 148`, `class_start: 1`
* *Risk/State:* `state_mutation: 52`, `unreferenced_by_name: 147`
* *Architecture:* `api: 148`, `import: 13`
* *Defense:* `safety: 1`, `doc: 7`, `test: 598`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.37
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` BadMethodCallException, Carbon\Carbon, Carbon\CarbonInterval, Carbon\Month, Carbon\Unit, Carbon\WeekDay, DateInterval, DateTime...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Carbon/Traits/Comparison.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.598)
- **Top Global Matches:** file_cluster_15: 5.598, file_cluster_12: 6.691, file_cluster_11: 6.943
- **Magnitude:** 467.18 | **LOC:** 1362 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **13**; blast radius 1.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (65.9%), Guard Balance (formerly Safety Score) (60.7%), Complexity Load (formerly Cognitive Load) (36.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `is` **(Compute Cores)** (Impact: 25.2)
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
* *Amplified Cascading Flux:* 42 instances
* *State Mutation (weighted view):* 155
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 194`, `args: 78`, `func_start: 72`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 71`
* *Architecture:* `api: 72`, `import: 17`
* *Defense:* `safety: 14`, `doc: 79`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.015
  * `Choke Point (Betweenness):` 3.1e-05 | `Ripple Effect (Closeness):` 0.036008
  * `Imports (Out-Degree: 9):` BackedEnum, BadMethodCallException, Carbon\CarbonConverterInterface, Carbon\CarbonInterface, Carbon\Exceptions\BadComparisonUnitException, Carbon\FactoryImmutable, Carbon\Month, Carbon\Unit...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/AbstractTestCase.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 7.059)
- **Top Global Matches:** file_cluster_16: 7.059, file_cluster_4: 7.097, file_cluster_15: 7.751
- **Magnitude:** 453.92 | **LOC:** 502 | **CtrlFlow:** 16.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **166** in-repo importer(s); it depends on **20**; blast radius 19.694; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (73.4%), Complexity Load (formerly Cognitive Load) (22.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (12.9%), Connectivity (formerly Api Exposure) (2.5%)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.694
  * `Choke Point (Betweenness):` 0.001925 | `Ripple Effect (Closeness):` 0.083083
  * `Imports (Out-Degree: 9):` AssertObjectHasPropertyTrait, Carbon\Carbon, Carbon\CarbonImmutable, Carbon\CarbonInterface, Carbon\CarbonInterval, Carbon\CarbonPeriod, Carbon\CarbonPeriodImmutable, Carbon\CarbonTimeZone...
  * `Imported By (In-Degree: 166):` (Excluded from Brief to save tokens)

### `src/Carbon/Traits/Units.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.448)
- **Top Global Matches:** file_cluster_6: 5.448, file_cluster_4: 8.828, file_cluster_8: 16.044
- **Magnitude:** 419.22 | **LOC:** 473 | **CtrlFlow:** 31.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **12**; blast radius 1.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.1%), Complexity Load (formerly Cognitive Load) (47.2%)
- **Documentation Coverage:** 4.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addUTCUnit` **(Many-Argument Workhorses)** (Impact: 62.5)
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
* *Structure:* `branch: 81`, `structural_boundaries: 55`, `args: 14`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 76`
* *Architecture:* `api: 12`, `import: 12`
* *Defense:* `safety: 21`, `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.015
  * `Choke Point (Betweenness):` 0.000147 | `Ripple Effect (Closeness):` 0.036051
  * `Imports (Out-Degree: 9):` Carbon\CarbonConverterInterface, Carbon\CarbonInterface, Carbon\CarbonInterval, Carbon\Exceptions\InvalidFormatException, Carbon\Exceptions\InvalidIntervalException, Carbon\Exceptions\UnitException, Carbon\Exceptions\UnsupportedUnitException, Carbon\Unit...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/CarbonImmutable/IsTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 7.633)
- **Top Global Matches:** file_cluster_11: 7.633, file_cluster_13: 8.929, file_cluster_15: 9.152
- **Magnitude:** 418.02 | **LOC:** 1164 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.37; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (34.1%), Connectivity (formerly Api Exposure) (13.7%), Complexity Load (formerly Cognitive Load) (7.1%)
- **Documentation Coverage:** 96.8254% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testIsSameMonthOfSameYear` **(I/O & Config Routines)** (Impact: 4.2)
  * `testIsSameQuarterFalseWithDateTime` **(Interface Declarations)** (Impact: 2.6)
  * `testIsSameMonth` **(I/O & Config Routines)** (Impact: 2.5)
  * `testIsSameMonthTrueWithDateTime` **(Interface Declarations)** (Impact: 2.5)
  * `dataForFormatLetters` **(I/O & Config Routines)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 95
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 182`, `args: 126`, `func_start: 126`, `class_start: 1`
* *Risk/State:* `state_mutation: 63`, `unreferenced_by_name: 125`
* *Architecture:* `api: 126`, `import: 10`
* *Defense:* `doc: 5`, `test: 405`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.37
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` Carbon\CarbonImmutable, Carbon\CarbonInterval, Carbon\Unit, DateInterval, DateTime, InvalidArgumentException, PHPUnit\Framework\Attributes\DataProvider, Tests\AbstractTestCase...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Carbon/Factory.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.867)
- **Top Global Matches:** file_cluster_15: 5.867, file_cluster_11: 6.876, file_cluster_12: 6.877
- **Magnitude:** 402.32 | **LOC:** 852 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **9**; blast radius 3.531; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (60.2%), Guard Balance (formerly Safety Score) (59.9%), Complexity Load (formerly Cognitive Load) (45.2%)
- **Documentation Coverage:** 37.7778% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__call` **(Defensive Guards)** (Impact: 24.9)
  * `setTestNowAndTimezone` **(Defensive Guards)** (Impact: 20.3)
    * *Intent:* * - When a null (or blank string) is passed to the constructor or parse(), ex. new Carbon(null) * - ...
  * `handleTestNowClosure` **(Defensive Guards)** (Impact: 18.9)
  * `setDefaultTimezone` **(Stateful Encapsulated Methods)** (Impact: 9.9)
  * `getMockedTestNow` **(Stateful Encapsulated Methods)** (Impact: 6.4)
    * *Intent:* /** * Get the mocked date passed in setTestNow() and if it's a Closure, execute it. */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 52 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 178
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 92`, `args: 47`, `func_start: 45`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 74`
* *Architecture:* `api: 42`, `import: 9`
* *Defense:* `safety: 39`, `doc: 97`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.531
  * `Choke Point (Betweenness):` 3.6e-05 | `Ripple Effect (Closeness):` 0.035138
  * `Imports (Out-Degree: 5):` Closure, DateTimeImmutable, DateTimeInterface, DateTimeZone, InvalidArgumentException, ReflectionMethod, RuntimeException, Symfony\Contracts\Translation\TranslatorInterface...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `tests/CarbonPeriod/CreateTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.863)
- **Top Global Matches:** file_cluster_11: 6.863, file_cluster_13: 7.816, file_cluster_15: 8.319
- **Magnitude:** 333.72 | **LOC:** 962 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 0.37; role: Pure Consumer (Orchestrator)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.37
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` BadMethodCallException, Carbon\Carbon, Carbon\CarbonImmutable, Carbon\CarbonInterface, Carbon\CarbonInterval, Carbon\CarbonPeriod, Carbon\CarbonPeriodImmutable, Carbon\Exceptions\InvalidPeriodParameterException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/CarbonPeriod/IteratorTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.083)
- **Top Global Matches:** file_cluster_11: 6.083, file_cluster_13: 7.178, file_cluster_10: 7.298
- **Magnitude:** 330.64 | **LOC:** 564 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.37; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (66.5%), Complexity Load (formerly Cognitive Load) (28.4%), Concurrency Surface (formerly Concurrency) (24.7%), Connectivity (formerly Api Exposure) (10.3%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.37
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` Carbon\Carbon, Carbon\CarbonInterval, Carbon\CarbonPeriod, Generator, PHPUnit\Framework\Attributes\DataProvider, Tests\AbstractTestCase, Tests\CarbonPeriod\Fixtures\CarbonPeriodFactory
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Carbon/AbstractTranslator.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.572)
- **Top Global Matches:** file_cluster_12: 6.572, file_cluster_15: 6.992, file_cluster_16: 7.04
- **Magnitude:** 314.68 | **LOC:** 1300 | **CtrlFlow:** 4.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 0.414; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.1%), Connectivity (formerly Api Exposure) (27.1%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000501
  * `Imports (Out-Degree: 1):` $file, Carbon\MessageFormatter\MessageFormatterMapper, Closure, ReflectionException, ReflectionFunction, ReflectionProperty, Symfony\Component\Translation\Formatter\MessageFormatterInterface, Symfony\Component\Translation\Loader\ArrayLoader...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/Carbon/StartEndOfTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 3.727)
- **Top Global Matches:** file_cluster_11: 3.727, file_cluster_13: 6.003, file_cluster_15: 6.492
- **Magnitude:** 291.84 | **LOC:** 575 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.37; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (59.5%), Connectivity (formerly Api Exposure) (13.9%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.37
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Carbon\Carbon, Carbon\Unit, InvalidArgumentException, PHPUnit\Framework\Attributes\TestWith, Tests\AbstractTestCase
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/Carbon/LocalizationTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.735)
- **Top Global Matches:** file_cluster_11: 5.735, file_cluster_15: 6.743, file_cluster_13: 6.839
- **Magnitude:** 261.52 | **LOC:** 1044 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.37; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (12.9%), Connectivity (formerly Api Exposure) (10.8%), Complexity Load (formerly Cognitive Load) (7.7%)
- **Documentation Coverage:** 95.2381% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testSetLocaleToAutoFallback` **(I/O & Config Routines)** (Impact: 4.0)
  * `testSetLocaleToAutoFromUnsupportedLocale` **(I/O & Config Routines)** (Impact: 3.7)
  * `testFallbackLocales` **(I/O & Config Routines)** (Impact: 3.5)
  * `testSetLocaleWithMalformedLocale` **(Compute Cores)** (Impact: 3.3)
  * `testSetLocaleToAutoFromSupportedLocale` **(Defensive Guards)** (Impact: 2.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 120
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 78`, `args: 43`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `state_mutation: 108`, `planned_debt: 1`, `unreferenced_by_name: 41`
* *Architecture:* `api: 42`, `import: 16`
* *Defense:* `safety: 6`, `doc: 24`, `test: 91`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.37
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` Carbon\Carbon, Carbon\CarbonInterface, Carbon\CarbonInterval, Carbon\Language, Carbon\Translator, InvalidArgumentException, PHPUnit\Framework\Attributes\DataProvider, PHPUnit\Framework\Attributes\Group...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/CarbonPeriod/SettersTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.4)
- **Top Global Matches:** file_cluster_11: 5.4, file_cluster_15: 7.373, file_cluster_2: 7.395
- **Magnitude:** 239.16 | **LOC:** 484 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.37; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (62.4%), Complexity Load (formerly Cognitive Load) (39.7%), Connectivity (formerly Api Exposure) (10.7%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.37
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` Carbon\Carbon, Carbon\CarbonImmutable, Carbon\CarbonInterval, DateInterval, DateTime, InvalidArgumentException, Tests\AbstractTestCase, Tests\CarbonPeriod\Fixtures\AbstractCarbon
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/CarbonImmutable/StartEndOfTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 3.877)
- **Top Global Matches:** file_cluster_11: 3.877, file_cluster_13: 5.956, file_cluster_15: 6.56
- **Magnitude:** 230.66 | **LOC:** 447 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.37; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (59.6%), Connectivity (formerly Api Exposure) (13.7%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.37
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Carbon\CarbonImmutable, PHPUnit\Framework\Attributes\TestWith, Tests\AbstractTestCase
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/Carbon/GettersTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.069)
- **Top Global Matches:** file_cluster_11: 6.069, file_cluster_13: 7.044, file_cluster_2: 7.608
- **Magnitude:** 229.14 | **LOC:** 549 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.37; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (41.7%), Connectivity (formerly Api Exposure) (13.0%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.37
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Carbon\Carbon, InvalidArgumentException, PHPUnit\Framework\Attributes\DataProvider, Tests\AbstractTestCase
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `tests/CarbonImmutable/TestingAidsTest.php` (PHP) | Magnitude: 86.88 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 225, test: 109, structural_boundaries: 51, state_mutation: 28
- `tests/CarbonImmutable/MacroTest.php` (PHP) | Magnitude: 93.22 | Delta: **0.126** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 176, structural_boundaries: 67, args: 32, state_mutation: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `tests/Carbon/Exceptions/NotLocaleAwareExceptionTest.php` (PHP) | Magnitude: 9.38 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 16, import: 5, test: 3
- `tests/Carbon/TestingAidsTest.php` (PHP) | Magnitude: 124.86 | Delta: **0.111** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 328, test: 127, structural_boundaries: 73, state_mutation: 43

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `tests/Language/TranslatorTest.php` (PHP) | Magnitude: 42.0 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 70, structural_boundaries: 30, state_mutation: 18, test: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tests/CarbonInterval/FromStringTest.php` (PHP) | Magnitude: 68.1 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 116, indent_spaces: 73, concurrency: 51, memory_alloc: 51
- `tests/CarbonInterval/ParseFromLocaleTest.php` (PHP) | Magnitude: 65.44 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 110, indent_spaces: 70, concurrency: 48, memory_alloc: 48
- `tests/CarbonPeriod/ToStringTest.php` (PHP) | Magnitude: 45.72 | Delta: **0.113** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 204, structural_boundaries: 26, state_mutation: 15, test: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/Carbon/CarbonPeriod.php` (PHP) | Magnitude: 1643.72 | Delta: **0.055** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 1427, structural_boundaries: 411, branch: 383, doc: 262
- `tests/CarbonInterval/CascadeTest.php` (PHP) | Magnitude: 92.82 | Delta: **0.06** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 274, structural_boundaries: 40, test: 25, state_mutation: 20
- `src/Carbon/FactoryImmutable.php` (PHP) | Magnitude: 43.02 | Delta: **0.068** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: doc: 64, indent_spaces: 34, structural_boundaries: 25, branch: 9
- `src/Carbon/Traits/Timestamp.php` (PHP) | Magnitude: 104.04 | Delta: **0.116** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 75, state_mutation: 27, structural_boundaries: 25, bitwise_ops: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `tests/PHPStan/FeaturesTest.php` (PHP) | Magnitude: 15.04 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 42, structural_boundaries: 14, args: 5, func_start: 5
- `tests/AbstractTestCase.php` (PHP) | Magnitude: 453.92 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 351, state_mutation: 101, structural_boundaries: 70, branch: 63

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/Carbon/Lang/es.php` (PHP) | Magnitude: 16.88 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 90, bitwise_ops: 21, structural_boundaries: 12, branch: 5
- `src/Carbon/Lang/ka.php` (PHP) | Magnitude: 29.82 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 137, structural_boundaries: 22, bitwise_ops: 15, state_mutation: 12
- `tests/CarbonPeriod/ComparisonTest.php` (PHP) | Magnitude: 68.04 | Delta: **0.104** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 198, test: 120, structural_boundaries: 36, state_mutation: 32

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `tests/Carbon/SettersTest.php` (PHP) | Magnitude: 687.56 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 928, state_mutation: 227, test: 138, structural_boundaries: 114

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/Carbon/Traits/IntervalRounding.php` (PHP) | Magnitude: 43.1 | Delta: **0.137** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 12, branch: 10, state_mutation: 6

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/Carbon/CarbonInterface.php` -> **kylekatarnls** (100.0% isolated ownership) | Magnitude: 12178.12
- `src/Carbon/CarbonInterval.php` -> **kylekatarnls** (100.0% isolated ownership) | Magnitude: 2634.76
- `src/Carbon/CarbonPeriod.php` -> **kylekatarnls** (100.0% isolated ownership) | Magnitude: 1643.72
- `src/Carbon/Traits/Date.php` -> **kylekatarnls** (100.0% isolated ownership) | Magnitude: 1360.0
- `src/Carbon/Traits/Creator.php` -> **Sam Anglin** (100.0% isolated ownership) | Magnitude: 749.66

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/Carbon/Traits/Date.php` -> **Severity: 0.225** (Bridge: 0.0023 * Flux: 100.0%)
- `src/Carbon/CarbonInterval.php` -> **Severity: 0.128** (Bridge: 0.0013 * Flux: 100.0%)
- `src/Carbon/CarbonImmutable.php` -> **Severity: 0.102** (Bridge: 0.0011 * Flux: 91.6827%)
- `src/Carbon/CarbonPeriod.php` -> **Severity: 0.082** (Bridge: 0.0008 * Flux: 100.0%)
- `src/Carbon/CarbonInterface.php` -> **Severity: 0.053** (Bridge: 0.0005 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `tests/AbstractTestCase.php` -> **Severity: 6.102** (Embedded: 0.0831 * Error Risk: 73.4421%)
- `src/Carbon/CarbonInterface.php` -> **Severity: 5.232** (Embedded: 0.0664 * Error Risk: 78.7742%)
- `src/Carbon/CarbonInterval.php` -> **Severity: 3.997** (Embedded: 0.0538 * Error Risk: 74.3563%)
- `src/Carbon/CarbonTimeZone.php` -> **Severity: 3.57** (Embedded: 0.056 * Error Risk: 63.7171%)
- `src/Carbon/CarbonPeriod.php` -> **Severity: 3.423** (Embedded: 0.0527 * Error Risk: 64.8975%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tests/AbstractTestCase.php` -> **Severity: 1406.715** (Blast Radius: 19.694 * Doc Risk: 71.4286%)
- `src/Carbon/WrapperClock.php` -> **Severity: 789.39** (Blast Radius: 8.771 * Doc Risk: 90.0%)
- `src/Carbon/CarbonImmutable.php` -> **Severity: 495.533** (Blast Radius: 14.866 * Doc Risk: 33.3333%)
- `src/Carbon/Traits/Date.php` -> **Severity: 418.608** (Blast Radius: 27.384 * Doc Risk: 15.2866%)
- `src/Carbon/Unit.php` -> **Severity: 236.0** (Blast Radius: 2.655 * Doc Risk: 88.8889%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 16356 call pairs -- scoped 24.8%, unique 0.2%, ambiguous 35.7%, external 39.4%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| php | 16356 | 24.8% | 0.2% | 35.7% | 39.4% |

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
