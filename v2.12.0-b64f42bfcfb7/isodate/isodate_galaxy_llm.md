# ARCHITECTURAL_BRIEF: isodate
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
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
- **Scope:** 21 analyzed artifact(s), 1570 LOC.
- **Load-bearing artifact:** `isodate-0.7.2/src/isodate/__init__.py` -- 6 in-repo importer(s) depend on it. Changes here propagate furthest.
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
| Total Artifacts | 29 |
| Analyzed Artifacts (Scanned) | 21 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 8 |
| Total LOC | 1570 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 72.4% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.1658 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3429 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.6262 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 17 | 1525 | 81.0% |
| YAML | 2 | 45 | 9.5% |
| PLAINTEXT | 2 | 0 | 9.5% |

## 4.1 SOURCE ENCODINGS
All 21 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Micro Repo (<30 files)`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (2) 29%, Data / Markup / Trivial 24%, Parameter Forwarders Files 14%, Compute Cores Files 10%, Declarative / Non-Code 10%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 19 | 90.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 9.5% |

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
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 52.4 | 19.9 | 13.2 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 73.6 | 51.3 | 54.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.6 | 10.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 18.0 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 65.0 | 20.8 | 20.7 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 45.3 | 16.8 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 11.9 | 1.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 18.4 | 0.0 | 0.0 |
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
| io | 1 | 1 | 0 | `isodate-0.7.2/.github/workflows/test.yml` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 61 | 7 | 5 | `isodate-0.7.2/tests/test_duration.py` |
| serialization | 3 | 1 | 0 | `isodate-0.7.2/tests/test_pickle.py` |
| regex | 6 | 5 | 1 | `isodate-0.7.2/src/isodate/isostrf.py` |
| events | 0 | 0 | 0 | - |
| tests | 71 | 6 | 7 | `isodate-0.7.2/tests/test_duration.py` |
| docs | 96 | 18 | 16 | `isodate-0.7.2/src/isodate/tzinfo.py` |
| debt | 9 | 5 | 2 | `isodate-0.7.2/src/isodate/isoduration.py` |
| mutation | 490 | 17 | 59 | `isodate-0.7.2/src/isodate/duration.py` |
| dead_code | 31 | 7 | 2 | `isodate-0.7.2/tests/test_duration.py` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.5714**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `isodate-0.7.2/.github/workflows/test.yml` (Hits: 1)
- `isodate-0.7.2/.github/workflows/lint.yml` (Hits: 0)
- `isodate-0.7.2/CHANGES.txt` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **__init__.py** (`isodate-0.7.2/src/isodate/__init__.py`) — 6 inbound connections
2. **isoerror.py** (`isodate-0.7.2/src/isodate/isoerror.py`) — 6 inbound connections
3. **isostrf.py** (`isodate-0.7.2/src/isodate/isostrf.py`) — 6 inbound connections
4. **duration.py** (`isodate-0.7.2/src/isodate/duration.py`) — 5 inbound connections
5. **isodatetime.py** (`isodate-0.7.2/src/isodate/isodatetime.py`) — 4 inbound connections

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
| `isodate-0.7.2/src/isodate` | 11 | 992.88 | 30.52% | 17.52% |
| `isodate-0.7.2/tests` | 6 | 235.02 | 6.95% | 0.0% |
| `isodate-0.7.2/.github/workflows` | 2 | 19.1 | 0.0% | 0.0% |
| `isodate-0.7.2` | 2 | 3.58 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `isodate-0.7.2/src/isodate/tzinfo.py` -> **99.6183%** Exposure
- `isodate-0.7.2/src/isodate/isoduration.py` -> **56.15%** Exposure
- `isodate-0.7.2/src/isodate/isodates.py` -> **27.1931%** Exposure
- `isodate-0.7.2/src/isodate/duration.py` -> **9.791%** Exposure
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
- **Unknown Dependencies:** `69` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `isodate-0.7.2/src/isodate/duration.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.906)
- **Top Global Matches:** file_cluster_12: 6.906, file_cluster_15: 9.414, file_cluster_7: 9.448
- **Magnitude:** 263.28 | **LOC:** 317 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **2**; blast radius 91.824; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.6%), Connectivity (formerly Api Exposure) (65.0%)
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
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 48`, `planned_debt: 1`
* *Architecture:* `api: 16`, `import: 2`
* *Defense:* `safety: 16`, `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 91.824
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.378947
  * `Imports (Out-Degree: 0):` datetime, decimal
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `isodate-0.7.2/src/isodate/isostrf.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 12.158)
- **Top Global Matches:** file_cluster_8: 12.158, file_cluster_3: 14.144, file_cluster_6: 24.165
- **Magnitude:** 192.32 | **LOC:** 190 | **CtrlFlow:** 33.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **4**; blast radius 94.586; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 94.586
  * `Choke Point (Betweenness):` 0.023684 | `Ripple Effect (Closeness):` 0.378125
  * `Imports (Out-Degree: 2):` datetime, isodate.duration, isodate.isotzinfo, re
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `isodate-0.7.2/src/isodate/isodates.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.36)
- **Top Global Matches:** file_cluster_8: 9.36, file_cluster_6: 10.607, file_cluster_4: 18.354
- **Magnitude:** 135.78 | **LOC:** 204 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **4**; blast radius 51.335; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
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
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 18`, `fragile_debt: 1`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 51.335
  * `Choke Point (Betweenness):` 0.002632 | `Ripple Effect (Closeness):` 0.27
  * `Imports (Out-Degree: 2):` datetime, isodate.isoerror, isodate.isostrf, re
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `isodate-0.7.2/tests/test_duration.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 7.02)
- **Top Global Matches:** file_cluster_11: 7.02, file_cluster_13: 7.45, file_cluster_15: 7.727
- **Magnitude:** 107.9 | **LOC:** 437 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 24.047; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (33.8%), Connectivity (formerly Api Exposure) (10.0%), Dead Code Surface (formerly Dead Code) (7.0%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 24.047
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` datetime, isodate, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `isodate-0.7.2/src/isodate/isoduration.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 7.5)
- **Top Global Matches:** file_cluster_3: 7.5, file_cluster_8: 21.275, file_cluster_6: 34.079
- **Magnitude:** 106.32 | **LOC:** 148 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **7**; blast radius 36.958; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.8%), Debt Markers (formerly Tech Debt) (56.1%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 36.958
  * `Choke Point (Betweenness):` 0.003947 | `Ripple Effect (Closeness):` 0.204167
  * `Imports (Out-Degree: 4):` datetime, decimal, isodate.duration, isodate.isodatetime, isodate.isoerror, isodate.isostrf, re
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `isodate-0.7.2/src/isodate/isotzinfo.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.134)
- **Top Global Matches:** file_cluster_9: 6.134, file_cluster_15: 12.239, file_cluster_16: 12.533
- **Magnitude:** 79.22 | **LOC:** 92 | **CtrlFlow:** 47.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **3**; blast radius 83.924; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (68.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (42.7%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 83.924
  * `Choke Point (Betweenness):` 0.015789 | `Ripple Effect (Closeness):` 0.342857
  * `Imports (Out-Degree: 2):` isodate.isoerror, isodate.tzinfo, re
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `isodate-0.7.2/src/isodate/isotime.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.201)
- **Top Global Matches:** file_cluster_12: 7.201, file_cluster_15: 7.625, file_cluster_16: 9.19
- **Magnitude:** 77.16 | **LOC:** 156 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **6**; blast radius 47.928; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (69.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (45.6%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 47.928
  * `Choke Point (Betweenness):` 0.006579 | `Ripple Effect (Closeness):` 0.27
  * `Imports (Out-Degree: 3):` datetime, decimal, isodate.isoerror, isodate.isostrf, isodate.isotzinfo, re
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `isodate-0.7.2/src/isodate/tzinfo.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.039)
- **Top Global Matches:** file_cluster_15: 6.039, file_cluster_16: 6.419, file_cluster_11: 7.832
- **Magnitude:** 71.24 | **LOC:** 167 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **2**; blast radius 79.438; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.6%), Guard Balance (formerly Safety Score) (59.9%), Connectivity (formerly Api Exposure) (52.1%)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 79.438
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.338
  * `Imports (Out-Degree: 0):` datetime, time
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `isodate-0.7.2/tests/test_strf.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.874)
- **Top Global Matches:** file_cluster_15: 6.874, file_cluster_13: 7.388, file_cluster_2: 7.722
- **Magnitude:** 38.66 | **LOC:** 84 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 24.047; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (54.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (17.6%), Connectivity (formerly Api Exposure) (6.2%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 24.047
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` datetime, isodate, pytest, time
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `isodate-0.7.2/tests/test_pickle.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 8.516)
- **Top Global Matches:** file_cluster_7: 8.516, file_cluster_12: 10.038, file_cluster_5: 10.619
- **Magnitude:** 28.52 | **LOC:** 33 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 24.047; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (58.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (13.2%), Connectivity (formerly Api Exposure) (7.1%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 24.047
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` isodate, isodate.duration, pickle
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `isodate-0.7.2/src/isodate/version.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 5.161)
- **Top Global Matches:** file_cluster_0: 5.161, file_cluster_2: 6.021, file_cluster_17: 7.236
- **Magnitude:** 28.24 | **LOC:** 17 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 30.145; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (59.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (31.9%)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 30.145
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.188462
  * `Imports (Out-Degree: 0):` typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `isodate-0.7.2/tests/test_date.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 6.703)
- **Top Global Matches:** file_cluster_13: 6.703, file_cluster_2: 6.886, file_cluster_15: 6.905
- **Magnitude:** 21.54 | **LOC:** 84 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 24.047; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (45.5%), Connectivity (formerly Api Exposure) (4.9%), Complexity Load (formerly Cognitive Load) (3.3%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 24.047
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` datetime, isodate, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `isodate-0.7.2/tests/test_datetime.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.138)
- **Top Global Matches:** file_cluster_2: 6.138, file_cluster_15: 6.666, file_cluster_13: 6.878
- **Magnitude:** 20.26 | **LOC:** 165 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 24.047; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (46.8%), Connectivity (formerly Api Exposure) (4.3%), Complexity Load (formerly Cognitive Load) (2.2%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 24.047
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` datetime, isodate, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `isodate-0.7.2/src/isodate/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.959)
- **Top Global Matches:** file_cluster_2: 4.959, file_cluster_17: 5.603, file_cluster_13: 6.337
- **Magnitude:** 18.9 | **LOC:** 104 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **10**; blast radius 71.739; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (20.7%), Mutation Surface (formerly State Flux) (12.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 21`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`, `import: 10`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 71.739
  * `Choke Point (Betweenness):` 0.107895 | `Ripple Effect (Closeness):` 0.3
  * `Imports (Out-Degree: 10):` isodate.duration, isodate.isodates, isodate.isodatetime, isodate.isoduration, isodate.isoerror, isodate.isostrf, isodate.isotime, isodate.isotzinfo...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `isodate-0.7.2/tests/test_time.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.315)
- **Top Global Matches:** file_cluster_2: 6.315, file_cluster_15: 6.683, file_cluster_13: 6.739
- **Magnitude:** 18.14 | **LOC:** 130 | **CtrlFlow:** 3.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 24.047; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (45.8%), Connectivity (formerly Api Exposure) (4.5%), Complexity Load (formerly Cognitive Load) (2.1%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 24.047
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` datetime, isodate, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `isodate-0.7.2/.github/workflows/lint.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.967)
- **Top Global Matches:** file_cluster_2: 2.967, file_cluster_17: 4.203, file_cluster_13: 5.14
- **Magnitude:** 15.22 | **LOC:** 15 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 24.047; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`, `args: 1`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `import: 3`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.047
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` checkout@v4, setup-python@v5, action@v3.0.1
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `isodate-0.7.2/src/isodate/isoerror.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.901)
- **Top Global Matches:** file_cluster_2: 4.901, file_cluster_17: 5.583, file_cluster_13: 6.139
- **Magnitude:** 11.52 | **LOC:** 8 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); blast radius 120.033; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (24.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 120.033
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.4225
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `isodate-0.7.2/src/isodate/isodatetime.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.582)
- **Top Global Matches:** file_cluster_15: 6.582, file_cluster_11: 7.852, file_cluster_2: 8.072
- **Magnitude:** 8.9 | **LOC:** 46 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **5**; blast radius 51.625; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (48.1%), Connectivity (formerly Api Exposure) (34.1%), Mutation Surface (formerly State Flux) (31.0%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 51.625
  * `Choke Point (Betweenness):` 0.015789 | `Ripple Effect (Closeness):` 0.266667
  * `Imports (Out-Degree: 4):` datetime, isodate.isodates, isodate.isoerror, isodate.isostrf, isodate.isotime
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `isodate-0.7.2/.github/workflows/test.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.792)
- **Top Global Matches:** file_cluster_2: 4.792, file_cluster_17: 6.295, file_cluster_11: 6.514
- **Magnitude:** 3.88 | **LOC:** 44 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 24.047; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (16.8%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Install dependencies` **(I/O & Config Routines)** (Impact: 1.1)
  * `Tox tests` **(I/O & Config Routines)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 5`, `args: 4`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `io: 1`, `import: 3`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.047
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` checkout@v4, setup-python@v5, codecov-action@v4
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `isodate-0.7.2/CHANGES.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 2.58 | **LOC:** 129 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.047
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `isodate-0.7.2/TODO.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.0 | **LOC:** 40 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.047
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

*No file sits within 2% of a second archetype -- no mixed-responsibility candidates.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `isodate-0.7.2/src/isodate/isostrf.py` -> **Severity: 2.368** (Bridge: 0.0237 * Flux: 100.0%)
- `isodate-0.7.2/src/isodate/isotzinfo.py` -> **Severity: 1.579** (Bridge: 0.0158 * Flux: 100.0%)
- `isodate-0.7.2/src/isodate/__init__.py` -> **Severity: 1.31** (Bridge: 0.1079 * Flux: 12.1431%)
- `isodate-0.7.2/src/isodate/isotime.py` -> **Severity: 0.658** (Bridge: 0.0066 * Flux: 100.0%)
- `isodate-0.7.2/src/isodate/isodatetime.py` -> **Severity: 0.49** (Bridge: 0.0158 * Flux: 31.0026%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `isodate-0.7.2/src/isodate/duration.py` -> **Severity: 27.875** (Embedded: 0.3789 * Error Risk: 73.5579%)
- `isodate-0.7.2/src/isodate/isostrf.py` -> **Severity: 27.29** (Embedded: 0.3781 * Error Risk: 72.1706%)
- `isodate-0.7.2/src/isodate/isotzinfo.py` -> **Severity: 23.488** (Embedded: 0.3429 * Error Risk: 68.5064%)
- `isodate-0.7.2/src/isodate/tzinfo.py` -> **Severity: 20.236** (Embedded: 0.338 * Error Risk: 59.8688%)
- `isodate-0.7.2/src/isodate/isodates.py` -> **Severity: 19.349** (Embedded: 0.27 * Error Risk: 71.6615%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `isodate-0.7.2/src/isodate/isodatetime.py` -> **Severity: 2581.25** (Blast Radius: 51.625 * Doc Risk: 50.0%)
- `isodate-0.7.2/src/isodate/duration.py` -> **Severity: 2295.6** (Blast Radius: 91.824 * Doc Risk: 25.0%)
- `isodate-0.7.2/tests/test_strf.py` -> **Severity: 1442.82** (Blast Radius: 24.047 * Doc Risk: 60.0%)
- `isodate-0.7.2/src/isodate/isodates.py` -> **Severity: 1283.375** (Blast Radius: 51.335 * Doc Risk: 25.0%)
- `isodate-0.7.2/tests/test_date.py` -> **Severity: 1202.35** (Blast Radius: 24.047 * Doc Risk: 50.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 219 call pairs -- scoped 32.4%, unique 0.0%, ambiguous 0.0%, external 67.6%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 219 | 32.4% | 0.0% | 0.0% | 67.6% |

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
