# ARCHITECTURAL_BRIEF: isodate
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 19 analyzed artifact(s), 1525 LOC.
- **Load-bearing artifact:** `isodate-0.7.2/src/isodate/isoerror.py` -- 6 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `isodate-0.7.2/src/isodate/__init__.py` -- pulls in 10 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `isodate-0.7.2/src/isodate/duration.py` at magnitude 263.28 (structural weight, not risk).
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
| Total Artifacts | 27 |
| Analyzed Artifacts (Scanned) | 19 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 8 |
| Total LOC | 1525 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 70.4% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.1282 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4051 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.4048 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 17 | 1525 | 89.5% |
| PLAINTEXT | 2 | 0 | 10.5% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Micro Repo (<30 files)`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (2) 32%, Data / Markup / Trivial 16%, Parameter Forwarders Files 16%, Compute Cores Files 11%, Declarative / Non-Code 11%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 17 | 89.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 10.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 8*

**Composition by Extension & Reason:**
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rst`: 1x Excluded (Unsupported Extension: '.rst')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')
- `.ini`: 1x Excluded (Unsupported Extension: '.ini')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 52.4 | 22.2 | 17.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 96.0 | 66.4 | 80.3 | 56.2 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.8 | 12.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 19.8 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 65.0 | 23.2 | 21.5 | 20.7 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 49.6 | 31.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 14.7 | 2.6 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 60.0 | 14.7 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 54 | 8 | 8 | `isodate-0.7.2/src/isodate/isotime.py` |
| cleanup | 0 | 0 | 0 | - |
| guards | 91 | 11 | 4 | `isodate-0.7.2/tests/test_duration.py` |
| danger | 32 | 9 | 5 | `isodate-0.7.2/src/isodate/duration.py` |
| concurrency | 0 | 0 | 0 | - |
| connectivity | 83 | 16 | 15 | `isodate-0.7.2/tests/test_duration.py` |
| io | 0 | 0 | 0 | - |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 61 | 7 | 5 | `isodate-0.7.2/tests/test_duration.py` |
| serialization | 3 | 1 | 0 | `isodate-0.7.2/tests/test_pickle.py` |
| regex | 6 | 5 | 1 | `isodate-0.7.2/src/isodate/isostrf.py` |
| events | 0 | 0 | 0 | - |
| tests | 71 | 6 | 7 | `isodate-0.7.2/tests/test_duration.py` |
| docs | 93 | 16 | 16 | `isodate-0.7.2/src/isodate/tzinfo.py` |
| debt | 9 | 5 | 2 | `isodate-0.7.2/src/isodate/isoduration.py` |
| mutation | 489 | 16 | 59 | `isodate-0.7.2/src/isodate/duration.py` |
| dead_code | 35 | 9 | 3 | `isodate-0.7.2/tests/test_duration.py` |
| credential | 0 | 0 | 0 | - |
| threat | 8 | 2 | 0 | `isodate-0.7.2/src/isodate/duration.py` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `isodate-0.7.2/CHANGES.txt` (Hits: 0)
- `isodate-0.7.2/TODO.txt` (Hits: 0)
- `isodate-0.7.2/src/isodate/__init__.py` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **isoerror.py** (`isodate-0.7.2/src/isodate/isoerror.py`) — 6 inbound connections
2. **isostrf.py** (`isodate-0.7.2/src/isodate/isostrf.py`) — 5 inbound connections
3. **duration.py** (`isodate-0.7.2/src/isodate/duration.py`) — 4 inbound connections
4. **isotzinfo.py** (`isodate-0.7.2/src/isodate/isotzinfo.py`) — 3 inbound connections
5. **isodates.py** (`isodate-0.7.2/src/isodate/isodates.py`) — 2 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **__init__.py** (`isodate-0.7.2/src/isodate/__init__.py`) — 10 outbound dependencies
2. **isoduration.py** (`isodate-0.7.2/src/isodate/isoduration.py`) — 7 outbound dependencies
3. **isotime.py** (`isodate-0.7.2/src/isodate/isotime.py`) — 6 outbound dependencies
4. **isodatetime.py** (`isodate-0.7.2/src/isodate/isodatetime.py`) — 5 outbound dependencies
5. **isodates.py** (`isodate-0.7.2/src/isodate/isodates.py`) — 4 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `parse_date` **(Many-Argument Workhorses)** (@ `isodate-0.7.2/src/isodate/isodates.py`) -> Impact: **62.5** | LOC: 75
  * *Intent:* """ Parse an ISO 8601 date string into a datetime.date object. As the datetime.date implementation is limited to dates starting from 0001-01-01, negat...
- `_strfduration` **(Many-Argument Workhorses)** (@ `isodate-0.7.2/src/isodate/isostrf.py`) -> Impact: **54.4** | LOC: 48
  * *Intent:* """ this is the work method for timedelta and Duration instances. see strftime for more details. """
- `parse_duration` **(Many-Argument Workhorses)** (@ `isodate-0.7.2/src/isodate/isoduration.py`) -> Impact: **44.5** | LOC: 93
  * *Intent:* # regular expression to parse ISO duration strings. """ Parses an ISO 8601 durations into datetime.timedelta or Duration objects. If the ISO date stri...
- `repl` **(Compute Cores)** (@ `isodate-0.7.2/src/isodate/isostrf.py`) -> Impact: **38.7** | LOC: 39
  * *Intent:* """ lookup format command and return corresponding replacement. """
- `parse_time` **(Type Conversions)** (@ `isodate-0.7.2/src/isodate/isotime.py`) -> Impact: **23.4** | LOC: 73
  * *Intent:* """ Parses ISO 8601 times into datetime.time objects. Following ISO 8601 formats are supported: (as decimal separator a ',' or a '.' is allowed) hhmms...
- `tz_isoformat` **(Compute Cores)** (@ `isodate-0.7.2/src/isodate/isotzinfo.py`) -> Impact: **20.7** | LOC: 33
  * *Intent:* """ return time zone offset ISO 8601 formatted. The various ISO formats can be chosen with the format parameter. if tzinfo is None returns '' if tzinf...
- `totimedelta` **(Compute Cores)** (@ `isodate-0.7.2/src/isodate/duration.py`) -> Impact: **16.7** | LOC: 14
  * *Intent:* """ Convert this duration into a timedelta object. This method requires a start datetime or end datetimem, but raises an exception if both are given. ...
- `__add__` **(Defensive Guards)** (@ `isodate-0.7.2/src/isodate/duration.py`) -> Impact: **16.2** | LOC: 46
  * *Intent:* """ Durations can be added with Duration, timedelta, date and datetime objects. """
- `__rsub__` **(Type Conversions)** (@ `isodate-0.7.2/src/isodate/duration.py`) -> Impact: **15.9** | LOC: 41
  * *Intent:* """ It is possible to subtract Duration objects from date, datetime and timedelta objects. TODO: there is some weird behaviour in date - timedelta ......
- `duration_isoformat` **(Defensive Guards)** (@ `isodate-0.7.2/src/isodate/isoduration.py`) -> Impact: **15.0** | LOC: 22
  * *Intent:* """ Format duration strings. This method is just a wrapper around isodate.isostrf.strftime and uses P%P (D_DEFAULT) as default format. """

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Type Conversions**: cast- and conversion-heavy function

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `isodate-0.7.2/src/isodate` | 11 | 992.88 | 30.52% | 19.96% |
| `isodate-0.7.2/tests` | 6 | 235.02 | 6.95% | 0.0% |
| `isodate-0.7.2` | 2 | 3.58 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `isodate-0.7.2/src/isodate/tzinfo.py` -> **99.8292%** Exposure
- `isodate-0.7.2/src/isodate/isoduration.py` -> **68.9269%** Exposure
- `isodate-0.7.2/src/isodate/isodates.py` -> **38.23%** Exposure
- `isodate-0.7.2/src/isodate/duration.py` -> **12.5501%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `isodate-0.7.2/src/isodate/duration.py` -> **100.0%** Exposure
- `isodate-0.7.2/src/isodate/isodates.py` -> **100.0%** Exposure
- `isodate-0.7.2/src/isodate/isoduration.py` -> **100.0%** Exposure
- `isodate-0.7.2/src/isodate/isostrf.py` -> **100.0%** Exposure
- `isodate-0.7.2/src/isodate/isotime.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `isodate-0.7.2/tests/test_duration.py` -> **18** Orphaned Functions | **0** Duplicates
- `isodate-0.7.2/tests/test_pickle.py` -> **3** Orphaned Functions | **0** Duplicates
- `isodate-0.7.2/src/isodate/tzinfo.py` -> **0** Orphaned Functions | **2** Duplicates
- `isodate-0.7.2/tests/test_date.py` -> **2** Orphaned Functions | **0** Duplicates
- `isodate-0.7.2/tests/test_datetime.py` -> **2** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `64` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `isodate-0.7.2/src/isodate/duration.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 263.28 | **LOC:** 317 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **2**; blast radius 110.637; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (65.0%)
- **Documentation Coverage:** 25.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `totimedelta` **(Compute Cores)** (Impact: 16.7)
    * *Intent:* """ Convert this duration into a timedelta object. This method requires a start datetime or end date...
  * `__add__` **(Defensive Guards)** (Impact: 16.2)
    * *Intent:* """ Durations can be added with Duration, timedelta, date and datetime objects. """
  * `__rsub__` **(Type Conversions)** (Impact: 15.9)
    * *Intent:* """ It is possible to subtract Duration objects from date, datetime and timedelta objects. TODO: the...
  * `__eq__` **(Defensive Guards)** (Impact: 11.2)
    * *Intent:* """ If the years, month part and the timedelta part are both equal, then the two Durations are consi...
  * `__ne__` **(Defensive Guards)** (Impact: 11.2)
    * *Intent:* """ If the years, month part or the timedelta part is not equal, then the two Durations are consider...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 122
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 59`, `args: 17`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 48`, `dead_code: 3`, `planned_debt: 1`
* *Architecture:* `api: 16`, `import: 2`
* *Defense:* `safety: 16`, `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 110.637
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.272222
  * `Imports (Out-Degree: 0):` datetime, decimal
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `isodate-0.7.2/src/isodate/isostrf.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 192.32 | **LOC:** 190 | **CtrlFlow:** 33.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **4**; blast radius 87.091; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.4%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_strfduration` **(Many-Argument Workhorses)** (Impact: 54.4)
    * *Intent:* """ this is the work method for timedelta and Duration instances. see strftime for more details. """
  * `repl` **(Compute Cores)** (Impact: 38.7)
    * *Intent:* """ lookup format command and return corresponding replacement. """
  * `_strfdt` **(Stateful Encapsulated Methods)** (Impact: 12.8)
    * *Intent:* """ this is the work method for time and date instances. see strftime for more details. """
  * `repl` **(Compute Cores)** (Impact: 8.8)
    * *Intent:* """ lookup format command and return corresponding replacement. """
  * `strftime` **(Many-Argument Workhorses)** (Impact: 5.3)
    * *Intent:* """Directive Meaning Notes %d Day of the month as a decimal number [01,31]. %f Microsecond as a deci...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 67
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 22`, `args: 30`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 45`
* *Architecture:* `api: 3`, `import: 4`
* *Defense:* `safety: 2`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 87.091
  * `Choke Point (Betweenness):` 0.026144 | `Ripple Effect (Closeness):` 0.277778
  * `Imports (Out-Degree: 2):` datetime, isodate.duration, isodate.isotzinfo, re
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `isodate-0.7.2/src/isodate/isodates.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 135.78 | **LOC:** 204 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 46.392; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.2%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 25.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_date` **(Many-Argument Workhorses)** (Impact: 62.5)
    * *Intent:* """ Parse an ISO 8601 date string into a datetime.date object. As the datetime.date implementation i...
  * `build_date_regexps` **(Many-Argument Workhorses)** (Impact: 13.4)
    * *Intent:* # A dictionary to cache pre-compiled regular expressions. # A set of regular expressions is identifi...
  * `date_isoformat` **(Parameter Forwarders)** (Impact: 2.4)
    * *Intent:* """ Format date strings. This method is just a wrapper around isodate.isostrf.strftime and uses Date...
  * `add_re` **(Parameter Forwarders)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 50
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 18`, `args: 4`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 18`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 46.392
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.125
  * `Imports (Out-Degree: 2):` datetime, isodate.isoerror, isodate.isostrf, re
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `isodate-0.7.2/tests/test_duration.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 107.9 | **LOC:** 437 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 33.998; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (12.5%), Connectivity (formerly Api Exposure) (10.0%), Dead Code Surface (formerly Dead Code) (7.0%)
- **Documentation Coverage:** 15.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_ge` **(Defensive Guards)** (Impact: 8.4)
    * *Intent:* """Test operator > and <."""
  * `test_format_parse` **(Defensive Guards)** (Impact: 7.3)
    * *Intent:* """Take duration/timedelta object and create ISO string from it. This is the reverse test to test_pa...
  * `test_calc_date` **(Defensive Guards)** (Impact: 6.3)
    * *Intent:* """Test operator +."""
  * `test_sub` **(Defensive Guards)** (Impact: 2.8)
    * *Intent:* """ Test operator - (__sub__, __rsub__) """
  * `test_add` **(Defensive Guards)** (Impact: 2.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 91`, `args: 20`, `func_start: 20`
* *Risk/State:* `state_mutation: 29`, `dead_code: 2`, `fragile_debt: 2`, `unreferenced_by_name: 18`
* *Architecture:* `api: 20`, `import: 3`
* *Defense:* `safety: 51`, `doc: 18`, `test: 41`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 33.998
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` datetime, isodate, pdb, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `isodate-0.7.2/src/isodate/isoduration.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 106.32 | **LOC:** 148 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 36.887; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (89.9%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (68.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_duration` **(Many-Argument Workhorses)** (Impact: 44.5)
    * *Intent:* # regular expression to parse ISO duration strings. """ Parses an ISO 8601 durations into datetime.t...
  * `duration_isoformat` **(Defensive Guards)** (Impact: 15.0)
    * *Intent:* """ Format duration strings. This method is just a wrapper around isodate.isostrf.strftime and uses ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 43
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 18`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 15`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `api: 2`, `import: 7`
* *Defense:* `safety: 3`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 36.887
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.055556
  * `Imports (Out-Degree: 4):` datetime, decimal, isodate.duration, isodate.isodatetime, isodate.isoerror, isodate.isostrf, re
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `isodate-0.7.2/src/isodate/isotzinfo.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 79.22 | **LOC:** 92 | **CtrlFlow:** 47.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **3**; blast radius 87.045; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (42.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `tz_isoformat` **(Compute Cores)** (Impact: 20.7)
    * *Intent:* """ return time zone offset ISO 8601 formatted. The various ISO formats can be chosen with the forma...
  * `build_tzinfo` **(Compute Cores)** (Impact: 14.2)
    * *Intent:* """ create a tzinfo instance according to given parameters. tzname: 'Z' ... return UTC '' | None ......
  * `parse_tzinfo` **(Compute Cores)** (Impact: 12.4)
    * *Intent:* """ Parses ISO 8601 time zone designators to tzinfo objects. A time zone designator can be in the fo...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 28
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 17`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 10`
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 87.045
  * `Choke Point (Betweenness):` 0.019608 | `Ripple Effect (Closeness):` 0.222222
  * `Imports (Out-Degree: 2):` isodate.isoerror, isodate.tzinfo, re
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `isodate-0.7.2/src/isodate/isotime.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 77.16 | **LOC:** 156 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 46.392; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (45.6%)
- **Documentation Coverage:** 25.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_time` **(Type Conversions)** (Impact: 23.4)
    * *Intent:* """ Parses ISO 8601 times into datetime.time objects. Following ISO 8601 formats are supported: (as ...
  * `build_time_regexps` **(I/O & Config Routines)** (Impact: 4.5)
    * *Intent:* # used to cache regular expressions to parse ISO time strings. """ Build regular expressions to pars...
  * `time_isoformat` **(Parameter Forwarders)** (Impact: 2.1)
    * *Intent:* """ Format time strings. This method is just a wrapper around isodate.isostrf.strftime and uses Time...
  * `add_re` **(Parameter Forwarders)** (Impact: 1.5)
    * *Intent:* # fraction separators. # The letter 'T' is allowed as time designator in front of a time # expressio...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 20`, `args: 4`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 16`
* *Architecture:* `api: 4`, `import: 6`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 46.392
  * `Choke Point (Betweenness):` 0.003268 | `Ripple Effect (Closeness):` 0.125
  * `Imports (Out-Degree: 3):` datetime, decimal, isodate.isoerror, isodate.isostrf, isodate.isotzinfo, re
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `isodate-0.7.2/src/isodate/tzinfo.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 71.24 | **LOC:** 167 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 73.881; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.8%), Guard Balance (formerly Safety Score) (81.6%), Connectivity (formerly Api Exposure) (52.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `utcoffset` **(Compute Cores)** (Impact: 5.6)
    * *Intent:* """ Return offset from UTC in minutes of UTC. """
  * `dst` **(Compute Cores)** (Impact: 5.6)
    * *Intent:* """ Return daylight saving offset. """
  * `__init__` **(Encapsulated Accessors)** (Impact: 2.6)
    * *Intent:* """ Initialise an instance with time offset and name. The time offset should be positive for time zo...
  * `_isdst` **(Stateful Encapsulated Methods)** (Impact: 2.6)
    * *Intent:* """ Returns true if DST is active for given datetime object dt. """
  * `utcoffset` **(Parameter Forwarders)** (Impact: 2.0)
    * *Intent:* """ Return offset from UTC in minutes east of UTC, which is ZERO for UTC. """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 20
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 35`, `args: 14`, `func_start: 14`, `class_start: 3`
* *Risk/State:* `state_mutation: 12`, `duplicate_logic: 2`
* *Architecture:* `api: 15`, `import: 2`
* *Defense:* `doc: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 73.881
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.181481
  * `Imports (Out-Degree: 0):` datetime, time
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `isodate-0.7.2/tests/test_strf.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 38.66 | **LOC:** 84 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 33.998; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (70.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (17.6%), Connectivity (formerly Api Exposure) (6.2%)
- **Documentation Coverage:** 60.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_format` **(Defensive Guards)** (Impact: 7.2)
    * *Intent:* """Take date object and create ISO string from it. This is the reverse test to test_parse. """
  * `tz_patch` **(Compute Cores)** (Impact: 5.9)
    * *Intent:* # local time zone mock function localtime_orig = time.localtime def localtime_mock(secs): """Mock ti...
  * `localtime_mock` **(Compute Cores)** (Impact: 5.4)
    * *Intent:* """Mock time to fixed date. Mock time.localtime so that it always returns a time_struct with tm_dst=...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 12`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 6`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `import: 4`
* *Defense:* `safety: 1`, `doc: 3`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 33.998
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` datetime, isodate, pytest, time
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `isodate-0.7.2/tests/test_pickle.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 28.52 | **LOC:** 33 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 33.998; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (80.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (13.2%), Connectivity (formerly Api Exposure) (7.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_pickle_duration` **(Defensive Guards)** (Impact: 3.7)
    * *Intent:* """Pickle / unpickle duration objects."""
  * `test_pickle_datetime` **(Defensive Guards)** (Impact: 2.3)
    * *Intent:* """Parse an ISO datetime string and compare it to the expected value."""
  * `test_pickle_utc` **(Defensive Guards)** (Impact: 1.1)
    * *Intent:* """isodate.UTC objects remain the same after pickling."""
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 6 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 11`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 3`, `state_mutation: 6`, `unreferenced_by_name: 3`
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* `safety: 4`, `doc: 3`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 33.998
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` isodate, isodate.duration, pickle
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `isodate-0.7.2/src/isodate/version.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 28.24 | **LOC:** 17 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 36.887; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (31.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 2`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 36.887
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.055556
  * `Imports (Out-Degree: 0):` typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `isodate-0.7.2/tests/test_date.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 21.54 | **LOC:** 84 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 33.998; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (43.8%), Connectivity (formerly Api Exposure) (4.9%), Complexity Load (formerly Cognitive Load) (3.3%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_format` **(Defensive Guards)** (Impact: 7.2)
    * *Intent:* """ Take date object and create ISO string from it. This is the reverse test to test_parse. """
  * `test_parse` **(Defensive Guards)** (Impact: 7.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 11`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 2`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `safety: 2`, `doc: 2`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 33.998
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` datetime, isodate, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `isodate-0.7.2/tests/test_datetime.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 20.26 | **LOC:** 165 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 33.998; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (44.0%), Connectivity (formerly Api Exposure) (4.3%), Complexity Load (formerly Cognitive Load) (2.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_parse` **(Defensive Guards)** (Impact: 7.2)
    * *Intent:* """ Parse an ISO datetime string and compare it to the expected value. """
  * `test_format` **(Defensive Guards)** (Impact: 7.2)
    * *Intent:* """ Take datetime object and create ISO string from it. This is the reverse test to test_parse. """
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 11`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `safety: 2`, `doc: 3`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 33.998
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` datetime, isodate, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `isodate-0.7.2/src/isodate/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 18.9 | **LOC:** 104 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 33.998; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (56.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (20.7%), Mutation Surface (formerly State Flux) (12.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 21`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`, `import: 10`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 33.998
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` isodate.duration, isodate.isodates, isodate.isodatetime, isodate.isoduration, isodate.isoerror, isodate.isostrf, isodate.isotime, isodate.isotzinfo...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `isodate-0.7.2/tests/test_time.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 18.14 | **LOC:** 130 | **CtrlFlow:** 3.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 33.998; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (42.3%), Connectivity (formerly Api Exposure) (4.5%), Complexity Load (formerly Cognitive Load) (2.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_parse` **(Defensive Guards)** (Impact: 6.5)
    * *Intent:* """ Parse an ISO time string and compare it to the expected value. """
  * `test_format` **(Defensive Guards)** (Impact: 6.5)
    * *Intent:* """ Take time object and create ISO string from it. This is the reverse test to test_parse. """
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 11`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `safety: 2`, `doc: 3`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 33.998
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` datetime, isodate, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `isodate-0.7.2/src/isodate/isoerror.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 11.52 | **LOC:** 8 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); blast radius 124.084; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (24.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 124.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.340278
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `isodate-0.7.2/src/isodate/isodatetime.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 8.9 | **LOC:** 46 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 44.726; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (53.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (34.1%), Mutation Surface (formerly State Flux) (31.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_datetime` **(Defensive Guards)** (Impact: 2.3)
    * *Intent:* """ Parses ISO 8601 date-times into datetime.datetime objects. This function uses parse_date and par...
  * `datetime_isoformat` **(Parameter Forwarders)** (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 14`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* `safety: 2`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 44.726
  * `Choke Point (Betweenness):` 0.006536 | `Ripple Effect (Closeness):` 0.111111
  * `Imports (Out-Degree: 4):` datetime, isodate.isodates, isodate.isoerror, isodate.isostrf, isodate.isotime
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `isodate-0.7.2/CHANGES.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 2.58 | **LOC:** 129 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 33.998
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `isodate-0.7.2/TODO.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 40 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 33.998
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `isodate-0.7.2/src/isodate/isostrf.py` -> **Severity: 2.614** (Bridge: 0.0261 * Flux: 100.0%)
- `isodate-0.7.2/src/isodate/isotzinfo.py` -> **Severity: 1.961** (Bridge: 0.0196 * Flux: 100.0%)
- `isodate-0.7.2/src/isodate/isotime.py` -> **Severity: 0.327** (Bridge: 0.0033 * Flux: 100.0%)
- `isodate-0.7.2/src/isodate/isodatetime.py` -> **Severity: 0.203** (Bridge: 0.0065 * Flux: 31.0026%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `isodate-0.7.2/src/isodate/isostrf.py` -> **Severity: 26.504** (Embedded: 0.2778 * Error Risk: 95.4143%)
- `isodate-0.7.2/src/isodate/duration.py` -> **Severity: 26.146** (Embedded: 0.2722 * Error Risk: 96.0454%)
- `isodate-0.7.2/src/isodate/isotzinfo.py` -> **Severity: 20.789** (Embedded: 0.2222 * Error Risk: 93.5492%)
- `isodate-0.7.2/src/isodate/tzinfo.py` -> **Severity: 14.818** (Embedded: 0.1815 * Error Risk: 81.6481%)
- `isodate-0.7.2/src/isodate/isodates.py` -> **Severity: 11.899** (Embedded: 0.125 * Error Risk: 95.1886%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `isodate-0.7.2/src/isodate/duration.py` -> **Severity: 2765.925** (Blast Radius: 110.637 * Doc Risk: 25.0%)
- `isodate-0.7.2/src/isodate/isodatetime.py` -> **Severity: 2236.3** (Blast Radius: 44.726 * Doc Risk: 50.0%)
- `isodate-0.7.2/tests/test_strf.py` -> **Severity: 2039.88** (Blast Radius: 33.998 * Doc Risk: 60.0%)
- `isodate-0.7.2/tests/test_date.py` -> **Severity: 1699.9** (Blast Radius: 33.998 * Doc Risk: 50.0%)
- `isodate-0.7.2/src/isodate/isodates.py` -> **Severity: 1159.8** (Blast Radius: 46.392 * Doc Risk: 25.0%)

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
