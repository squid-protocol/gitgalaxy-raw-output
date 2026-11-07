# ARCHITECTURAL_BRIEF: python-dateutil
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
- **Scope:** 27 analyzed artifact(s), 10597 LOC.
- **Load-bearing artifact:** `python-dateutil-2.6.1/dateutil/__init__.py` -- 4 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `python-dateutil-2.6.1/dateutil/rrule.py` -- pulls in 12 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `python-dateutil-2.6.1/dateutil/rrule.py` at magnitude 2316.7 (structural weight, not risk).
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
| Total Artifacts | 32 |
| Analyzed Artifacts (Scanned) | 27 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 5 |
| Total LOC | 10597 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 84.4% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3194 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0732 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 11.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 5 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 24 | 10572 | 88.9% |
| PLAINTEXT | 2 | 0 | 7.4% |
| JSON | 1 | 25 | 3.7% |

## 4.1 SOURCE ENCODINGS
All 27 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Micro Repo (<30 files)`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 30%, Large Core Modules (3) 30%, Parameter Forwarders Files 19%, Large Core Modules (2) 7%, Compute Cores Files 4%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 25 | 92.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 7.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 5*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.rst`: 1x Excluded (Unsupported Extension: '.rst')
- `.gz`: 1x Excluded (Explicitly Denied Extension: '.gz')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 91.7 | 27.7 | 22.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 86.4 | 53.9 | 56.1 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 82.5 | 12.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 20.2 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 65.6 | 19.4 | 14.9 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 47.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 11.7 | 0.7 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 52.6 | 58.6 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 460 | 11 | 17 | `python-dateutil-2.6.1/dateutil/test/test_rrule.py` |
| cleanup | 1 | 1 | 0 | `python-dateutil-2.6.1/dateutil/test/_common.py` |
| guards | 395 | 15 | 28 | `python-dateutil-2.6.1/dateutil/rrule.py` |
| danger | 183 | 15 | 11 | `python-dateutil-2.6.1/dateutil/tz/tz.py` |
| concurrency | 6 | 1 | 0 | `python-dateutil-2.6.1/dateutil/rrule.py` |
| connectivity | 1261 | 19 | 67 | `python-dateutil-2.6.1/dateutil/test/test_rrule.py` |
| io | 33 | 8 | 2 | `python-dateutil-2.6.1/dateutil/tz/tz.py` |
| crypto | 1 | 1 | 0 | `python-dateutil-2.6.1/updatezinfo.py` |
| ipc | 5 | 2 | 0 | `python-dateutil-2.6.1/dateutil/test/_common.py` |
| time | 154 | 10 | 14 | `python-dateutil-2.6.1/dateutil/test/test_tz.py` |
| serialization | 2 | 1 | 0 | `python-dateutil-2.6.1/dateutil/test/_common.py` |
| regex | 1 | 1 | 0 | `python-dateutil-2.6.1/dateutil/parser.py` |
| events | 1 | 1 | 0 | `python-dateutil-2.6.1/dateutil/zoneinfo/rebuild.py` |
| tests | 82 | 7 | 5 | `python-dateutil-2.6.1/dateutil/test/test_tz.py` |
| docs | 121 | 16 | 11 | `python-dateutil-2.6.1/dateutil/tz/tz.py` |
| debt | 39 | 11 | 4 | `python-dateutil-2.6.1/dateutil/tz/tz.py` |
| mutation | 5349 | 21 | 441 | `python-dateutil-2.6.1/dateutil/test/test_rrule.py` |
| dead_code | 986 | 8 | 65 | `python-dateutil-2.6.1/dateutil/test/test_rrule.py` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.25**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `python-dateutil-2.6.1/dateutil/tz/tz.py` (Hits: 13)
- `python-dateutil-2.6.1/dateutil/zoneinfo/rebuild.py` (Hits: 8)
- `python-dateutil-2.6.1/updatezinfo.py` (Hits: 4)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **__init__.py** (`python-dateutil-2.6.1/dateutil/__init__.py`) — 4 inbound connections
2. **parser.py** (`python-dateutil-2.6.1/dateutil/parser.py`) — 4 inbound connections
3. **relativedelta.py** (`python-dateutil-2.6.1/dateutil/relativedelta.py`) — 4 inbound connections
4. **_common.py** (`python-dateutil-2.6.1/dateutil/test/_common.py`) — 4 inbound connections
5. **__init__.py** (`python-dateutil-2.6.1/dateutil/tz/__init__.py`) — 4 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **rrule.py** (`python-dateutil-2.6.1/dateutil/rrule.py`) — 12 outbound dependencies
2. **parser.py** (`python-dateutil-2.6.1/dateutil/parser.py`) — 11 outbound dependencies
3. **test_imports.py** (`python-dateutil-2.6.1/dateutil/test/test_imports.py`) — 11 outbound dependencies
4. **test_tz.py** (`python-dateutil-2.6.1/dateutil/test/test_tz.py`) — 11 outbound dependencies
5. **tz.py** (`python-dateutil-2.6.1/dateutil/tz/tz.py`) — 11 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `__init__` **(Stateful Encapsulated Methods)** (@ `python-dateutil-2.6.1/dateutil/rrule.py`) -> Impact: **466.0** | LOC: 254
- `_parse` **(Many-Argument Workhorses)** (@ `python-dateutil-2.6.1/dateutil/parser.py`) -> Impact: **382.1** | LOC: 446
- `_parse_rfc` **(Many-Argument Workhorses)** (@ `python-dateutil-2.6.1/dateutil/rrule.py`) -> Impact: **166.8** | LOC: 111
- `_iter` **(Stateful Encapsulated Methods)** (@ `python-dateutil-2.6.1/dateutil/rrule.py`) -> Impact: **162.7** | LOC: 255
- `__init__` **(Many-Argument Workhorses)** (@ `python-dateutil-2.6.1/dateutil/relativedelta.py`) -> Impact: **159.7** | LOC: 125
- `parse` **(Many-Argument Workhorses)** (@ `python-dateutil-2.6.1/dateutil/parser.py`) -> Impact: **113.3** | LOC: 152
- `rebuild` **(Many-Argument Workhorses)** (@ `python-dateutil-2.6.1/dateutil/rrule.py`) -> Impact: **94.5** | LOC: 129
  * *Intent:* # Every mask is 7 days longer to handle cross-year weekly periods. rr = self.rrule if year != self.lastyear: self.yearlen = 365 + calendar.isleap(year...
- `parse` **(Many-Argument Workhorses)** (@ `python-dateutil-2.6.1/dateutil/parser.py`) -> Impact: **93.7** | LOC: 127
  * *Intent:* """ Parse the date/time string into a :class:`datetime.datetime` object. :param timestr: Any date/time string using the supported formats. :param defa...
- `resolve_ymd` **(Many-Argument Workhorses)** (@ `python-dateutil-2.6.1/dateutil/parser.py`) -> Impact: **90.9** | LOC: 73
- `_read_tzfile` **(Many-Argument Workhorses)** (@ `python-dateutil-2.6.1/dateutil/tz/tz.py`) -> Impact: **82.0** | LOC: 219

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `python-dateutil-2.6.1/dateutil` | 8 | 4721.96 | 40.08% | 3.17% |
| `python-dateutil-2.6.1/dateutil/test` | 8 | 4031.54 | 9.3% | 0.0% |
| `python-dateutil-2.6.1/dateutil/tz` | 4 | 1897.02 | 40.56% | 22.93% |
| `python-dateutil-2.6.1/dateutil/zoneinfo` | 2 | 143.6 | 34.7% | 60.15% |
| `python-dateutil-2.6.1` | 5 | 76.14 | 12.93% | 12.45% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `python-dateutil-2.6.1/dateutil/zoneinfo/__init__.py` -> **82.5498%** Exposure
- `python-dateutil-2.6.1/dateutil/tz/tz.py` -> **81.6473%** Exposure
- `python-dateutil-2.6.1/setup.py` -> **62.2459%** Exposure
- `python-dateutil-2.6.1/dateutil/zoneinfo/rebuild.py` -> **37.7541%** Exposure
- `python-dateutil-2.6.1/dateutil/tz/_common.py` -> **10.0529%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `python-dateutil-2.6.1/dateutil/easter.py` -> **100.0%** Exposure
- `python-dateutil-2.6.1/dateutil/parser.py` -> **100.0%** Exposure
- `python-dateutil-2.6.1/dateutil/relativedelta.py` -> **100.0%** Exposure
- `python-dateutil-2.6.1/dateutil/rrule.py` -> **100.0%** Exposure
- `python-dateutil-2.6.1/dateutil/tz/_common.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `python-dateutil-2.6.1/dateutil/test/test_rrule.py` -> **543** Orphaned Functions | **0** Duplicates
- `python-dateutil-2.6.1/dateutil/test/test_parser.py` -> **184** Orphaned Functions | **0** Duplicates
- `python-dateutil-2.6.1/dateutil/test/test_tz.py` -> **163** Orphaned Functions | **6** Duplicates
- `python-dateutil-2.6.1/dateutil/test/test_relativedelta.py` -> **65** Orphaned Functions | **0** Duplicates
- `python-dateutil-2.6.1/dateutil/test/test_imports.py` -> **23** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `119` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `python-dateutil-2.6.1/dateutil/rrule.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.981)
- **Top Global Matches:** file_cluster_4: 6.981, file_cluster_6: 9.934, file_cluster_12: 12.216
- **Magnitude:** 2316.7 | **LOC:** 1611 | **CtrlFlow:** 37.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **12**; blast radius 25.749; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.1%), Complexity Load (formerly Cognitive Load) (80.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 69.0476% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 466.0)
  * `_parse_rfc` **(Many-Argument Workhorses)** (Impact: 166.8)
  * `_iter` **(Stateful Encapsulated Methods)** (Impact: 162.7)
  * `rebuild` **(Many-Argument Workhorses)** (Impact: 94.5)
    * *Intent:* # Every mask is 7 days longer to handle cross-year weekly periods. rr = self.rrule if year != self.l...
  * `between` **(Many-Argument Workhorses)** (Impact: 38.3)
    * *Intent:* """ Returns all the occurrences of the rrule between after and before. The inc keyword defines what ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 314 instances
* *State Mutation (weighted view):* 1004
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 431`, `structural_boundaries: 156`, `args: 52`, `func_start: 50`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 376`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 36`, `import: 15`
* *Defense:* `safety: 33`, `doc: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 25.749
  * `Choke Point (Betweenness):` 0.016154 | `Ripple Effect (Closeness):` 0.076923
  * `Imports (Out-Degree: 3):` ._common, calendar, datetime, dateutil, fractions, heapq, itertools, math...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `python-dateutil-2.6.1/dateutil/test/test_rrule.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.521)
- **Top Global Matches:** file_cluster_15: 6.521, file_cluster_2: 8.214, file_cluster_11: 8.236
- **Magnitude:** 1710.12 | **LOC:** 4705 | **CtrlFlow:** 0.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 16.816; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (14.9%), Complexity Load (formerly Cognitive Load) (2.9%)
- **Documentation Coverage:** 98.8128% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testLongIntegers` **(Type Conversions)** (Impact: 3.8)
  * `testCachePost` **(Type Conversions)** (Impact: 3.8)
  * `testCachePostInternal` **(Compute Cores)** (Impact: 3.8)
  * `testSetRRuleCount` **(Compute Cores)** (Impact: 3.8)
    * *Intent:* # Test that the count is updated when an rrule is added rrset = rruleset(cache=False) for cache in (...
  * `testSetRDateCount` **(Compute Cores)** (Impact: 3.8)
    * *Intent:* # Test that the count is updated when an rdate is added rrset = rruleset(cache=False) for cache in (...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 71
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 576`, `args: 549`, `func_start: 549`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 43`, `fragile_debt: 2`, `unreferenced_by_name: 543`
* *Architecture:* `api: 551`, `import: 6`
* *Defense:* `safety: 3`, `doc: 7`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.816
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ._common, __future__, datetime, dateutil.rrule, six
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python-dateutil-2.6.1/dateutil/parser.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.272)
- **Top Global Matches:** file_cluster_4: 7.272, file_cluster_6: 8.266, file_cluster_12: 13.937
- **Magnitude:** 1589.4 | **LOC:** 1375 | **CtrlFlow:** 43.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **11**; blast radius 31.513; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (85.3%), Guard Balance (formerly Safety Score) (81.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 78.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_parse` **(Many-Argument Workhorses)** (Impact: 382.1)
  * `parse` **(Many-Argument Workhorses)** (Impact: 113.3)
  * `parse` **(Many-Argument Workhorses)** (Impact: 93.7)
    * *Intent:* """ Parse the date/time string into a :class:`datetime.datetime` object. :param timestr: Any date/ti...
  * `resolve_ymd` **(Many-Argument Workhorses)** (Impact: 90.9)
  * `get_token` **(Compute Cores)** (Impact: 64.8)
    * *Intent:* """ This function breaks the time string into lexical units (tokens), which can be parsed by the par...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 206 instances
* *State Mutation (weighted view):* 644
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 353`, `structural_boundaries: 152`, `args: 41`, `func_start: 41`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 232`, `fragile_debt: 1`
* *Architecture:* `api: 29`, `import: 11`
* *Defense:* `safety: 37`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 31.513
  * `Choke Point (Betweenness):` 0.024359 | `Ripple Effect (Closeness):` 0.160256
  * `Imports (Out-Degree: 3):` .relativedelta, .tz, __future__, calendar, collections, datetime, io, re...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `python-dateutil-2.6.1/dateutil/tz/tz.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.858)
- **Top Global Matches:** file_cluster_12: 7.858, file_cluster_7: 9.644, file_cluster_4: 9.847
- **Magnitude:** 1417.98 | **LOC:** 1512 | **CtrlFlow:** 30.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **11**; blast radius 108.559; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.4%), Debt Markers (formerly Tech Debt) (81.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 78.0488% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_read_tzfile` **(Many-Argument Workhorses)** (Impact: 82.0)
  * `_parse_rfc` **(Many-Argument Workhorses)** (Impact: 80.3)
  * `gettz` **(Defensive Guards)** (Impact: 44.6)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 39.1)
  * `_delta` **(Stateful Encapsulated Methods)** (Impact: 30.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 228 instances
* *State Mutation (weighted view):* 726
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 250`, `structural_boundaries: 244`, `args: 79`, `func_start: 79`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 270`, `duplicate_logic: 13`
* *Architecture:* `io: 13`, `api: 40`, `import: 16`
* *Defense:* `safety: 29`, `doc: 23`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 108.559
  * `Choke Point (Betweenness):` 0.053333 | `Ripple Effect (Closeness):` 0.202429
  * `Imports (Out-Degree: 4):` ._common, .win, bisect, datetime, dateutil, dateutil.zoneinfo, os, six...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `python-dateutil-2.6.1/dateutil/test/test_tz.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.465)
- **Top Global Matches:** file_cluster_15: 7.465, file_cluster_12: 8.288, file_cluster_16: 8.332
- **Magnitude:** 1193.74 | **LOC:** 2162 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 16.816; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (65.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (35.4%), Connectivity (formerly Api Exposure) (13.2%)
- **Documentation Coverage:** 99.7748% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_get_no_support_tzinfo_class` **(C Struct Operations)** (Impact: 16.8)
    * *Intent:* # Generates a class of tzinfo with no support for is_ambiguous # where dates between dt_start and dt...
  * `_test_us_zone` **(Stateful Encapsulated Methods)** (Impact: 13.0)
    * *Intent:* # Test performance
  * `get_utc_transitions` **(Many-Argument Workhorses)** (Impact: 7.6)
  * `utcoffset` **(Compute Cores)** (Impact: 7.3)
  * `dst` **(Compute Cores)** (Impact: 7.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 455
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 361`, `args: 231`, `func_start: 231`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 393`, `planned_debt: 3`, `fragile_debt: 1`, `duplicate_logic: 6`, `unreferenced_by_name: 163`
* *Architecture:* `io: 1`, `api: 231`, `import: 19`
* *Defense:* `safety: 2`, `doc: 9`, `test: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.816
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` ._common, __future__, base64, copy, datetime, dateutil, dateutil.parser, dateutil.relativedelta...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python-dateutil-2.6.1/dateutil/relativedelta.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.438)
- **Top Global Matches:** file_cluster_8: 6.438, file_cluster_6: 11.75, file_cluster_4: 20.25
- **Magnitude:** 684.6 | **LOC:** 550 | **CtrlFlow:** 36.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **7**; blast radius 36.72; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (91.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.0%)
- **Documentation Coverage:** 93.1034% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 159.7)
  * `__add__` **(Many-Argument Workhorses)** (Impact: 70.1)
  * `__eq__` **(Compute Cores)** (Impact: 46.3)
  * `__sub__` **(Compute Cores)** (Impact: 34.3)
  * `__bool__` **(Compute Cores)** (Impact: 23.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 80 instances
* *State Mutation (weighted view):* 276
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 147`, `structural_boundaries: 57`, `args: 18`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 116`, `planned_debt: 1`
* *Architecture:* `api: 10`, `import: 7`
* *Defense:* `safety: 18`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 36.72
  * `Choke Point (Betweenness):` 0.006923 | `Ripple Effect (Closeness):` 0.171329
  * `Imports (Out-Degree: 1):` ._common, calendar, datetime, math, operator, six, warnings
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `python-dateutil-2.6.1/dateutil/test/test_parser.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.452)
- **Top Global Matches:** file_cluster_15: 5.452, file_cluster_11: 7.252, file_cluster_2: 7.672
- **Magnitude:** 554.68 | **LOC:** 898 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 16.816; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (53.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (15.4%), Complexity Load (formerly Cognitive Load) (5.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testIncreasingCTime` **(Compute Cores)** (Impact: 3.3)
    * *Intent:* # This test will check 200 different years, every month, every day, # every hour, every minute, ever...
  * `testMicrosecondPrecisionErrorReturns` **(Compute Cores)** (Impact: 3.3)
    * *Intent:* # One more precision issue, discovered by Eric Brown. This should # be the last one, as we're no lon...
  * `testDateCommandFormatWithLong` **(Parameter Forwarders)** (Impact: 3.1)
  * `testIncreasingISOFormat` **(Parameter Forwarders)** (Impact: 3.1)
  * `testParseUnicodeWords` **(Parameter Forwarders)** (Impact: 2.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 47
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 221`, `args: 184`, `func_start: 184`, `class_start: 5`
* *Risk/State:* `state_mutation: 39`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 184`
* *Architecture:* `api: 188`, `import: 10`
* *Defense:* `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.816
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` ._common, __future__, datetime, dateutil.parser, dateutil.tz, six, six.moves
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python-dateutil-2.6.1/dateutil/test/test_relativedelta.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.13)
- **Top Global Matches:** file_cluster_15: 5.13, file_cluster_2: 6.384, file_cluster_11: 6.576
- **Magnitude:** 246.78 | **LOC:** 578 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 16.816; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (56.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (13.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testAddTimedeltaToPopulatedRelativeDelta` **(I/O & Config Routines)** (Impact: 2.9)
  * `testRelativeDeltaFractionalNegativeOverflow` **(I/O & Config Routines)** (Impact: 2.8)
    * *Intent:* # Equivalent to (days=-1) rd1 = relativedelta(days=-0.5, hours=-12) self.assertEqual(rd1.normalized(...
  * `testInheritance` **(Parameter Forwarders)** (Impact: 2.7)
    * *Intent:* # Ensure that relativedelta is inheritance-friendly. class rdChildClass(relativedelta): pass ccRD = ...
  * `testRelativeDeltaFractionalAbsolutes` **(Parameter Forwarders)** (Impact: 2.6)
    * *Intent:* # Fractional absolute values will soon be unsupported, # check for the deprecation warning. with sel...
  * `testAddTimedeltaToUnpopulatedRelativedelta` **(I/O & Config Routines)** (Impact: 2.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 104`, `args: 66`, `func_start: 65`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 54`, `unreferenced_by_name: 65`
* *Architecture:* `api: 67`, `import: 5`
* *Defense:* `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.816
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ._common, __future__, calendar, datetime, dateutil.relativedelta
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python-dateutil-2.6.1/dateutil/tz/_common.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.174)
- **Top Global Matches:** file_cluster_16: 6.174, file_cluster_15: 6.305, file_cluster_13: 8.223
- **Magnitude:** 238.64 | **LOC:** 395 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **3**; blast radius 91.006; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 57.1429% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fromutc` **(Compute Cores)** (Impact: 13.7)
    * *Intent:* """ Given a datetime in UTC, return local time """
  * `_isdst` **(Stateful Encapsulated Methods)** (Impact: 13.1)
  * `_fromutc` **(Stateful Encapsulated Methods)** (Impact: 8.7)
    * *Intent:* """ Given a timezone-aware datetime in a given timezone, calculates a timezone-aware datetime in a n...
  * `enfold` **(Compute Cores)** (Impact: 8.3)
    * *Intent:* """ Provides a unified interface for assigning the ``fold`` attribute to datetimes both before and a...
  * `utcoffset` **(Compute Cores)** (Impact: 7.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 93
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 70`, `args: 24`, `func_start: 24`, `class_start: 3`
* *Risk/State:* `state_mutation: 39`, `planned_debt: 1`
* *Architecture:* `api: 18`, `import: 3`
* *Defense:* `safety: 3`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 91.006
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.203125
  * `Imports (Out-Degree: 0):` datetime, functools, six
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `python-dateutil-2.6.1/dateutil/tz/win.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.108)
- **Top Global Matches:** file_cluster_12: 6.108, file_cluster_16: 7.705, file_cluster_15: 7.827
- **Magnitude:** 227.32 | **LOC:** 333 | **CtrlFlow:** 12.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **6**; blast radius 57.74; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.1%), Complexity Load (formerly Cognitive Load) (51.8%)
- **Documentation Coverage:** 58.6207% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__eq__` **(Defensive Guards)** (Impact: 23.4)
    * *Intent:* # Compare on all relevant dimensions, including name. if not isinstance(other, tzwinbase): return No...
  * `valuestodict` **(Compute Cores)** (Impact: 12.5)
    * *Intent:* """Convert a registry key's values to a dictionary."""
  * `picknthweekday` **(Many-Argument Workhorses)** (Impact: 5.9)
    * *Intent:* """ dayofweek == 0 means Sunday, whichweek 5 means last instance """
  * `transitions` **(Compute Cores)** (Impact: 5.0)
    * *Intent:* """ For a given year, get the DST on and off transition times, expressed always on the standard time...
  * `name_from_string` **(Defensive Guards)** (Impact: 4.9)
    * *Intent:* """ Parse strings as returned from the Windows registry into the time zone name as defined in the re...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 128
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 69`, `args: 20`, `func_start: 20`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 76`
* *Architecture:* `api: 14`, `import: 7`
* *Defense:* `safety: 8`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 57.74
  * `Choke Point (Betweenness):` 0.002051 | `Ripple Effect (Closeness):` 0.190981
  * `Imports (Out-Degree: 1):` ._common, ctypes, datetime, six, six.moves, struct
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `python-dateutil-2.6.1/dateutil/test/_common.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.566)
- **Top Global Matches:** file_cluster_12: 6.566, file_cluster_16: 7.393, file_cluster_15: 7.457
- **Magnitude:** 203.26 | **LOC:** 293 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **10**; blast radius 36.725; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (75.9%), Connectivity (formerly Api Exposure) (51.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (22.6%)
- **Documentation Coverage:** 85.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assertPicklable` **(Many-Argument Workhorses)** (Impact: 12.9)
  * `__enter__` **(Compute Cores)** (Impact: 8.8)
  * `assertWarns` **(Many-Argument Workhorses)** (Impact: 7.7)
  * `set_current_tz` **(Compute Cores)** (Impact: 7.3)
  * `__exit__` **(Defensive Guards)** (Impact: 6.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 81
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 72`, `args: 28`, `func_start: 28`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 4`, `state_mutation: 51`
* *Architecture:* `api: 20`, `import: 10`
* *Defense:* `safety: 5`, `doc: 11`, `test: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 36.725
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.153846
  * `Imports (Out-Degree: 0):` __future__, datetime, os, pickle, subprocess, tempfile, time, unittest...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `python-dateutil-2.6.1/dateutil/zoneinfo/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.745)
- **Top Global Matches:** file_cluster_15: 5.745, file_cluster_16: 8.122, file_cluster_11: 8.277
- **Magnitude:** 108.48 | **LOC:** 184 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **7**; blast radius 70.259; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (82.5%), Guard Balance (formerly Safety Score) (70.6%), Connectivity (formerly Api Exposure) (57.7%)
- **Documentation Coverage:** 47.0588% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Defensive Guards)** (Impact: 17.1)
  * `gettz` **(Compute Cores)** (Impact: 7.5)
    * *Intent:* """ This retrieves a time zone from the local zoneinfo tarball that is packaged with dateutil. :para...
  * `get_zonefile_instance` **(Compute Cores)** (Impact: 7.0)
    * *Intent:* """ This is a convenience function which provides a :class:`ZoneInfoFile` instance using the data pr...
  * `gettz_db_metadata` **(I/O & Config Routines)** (Impact: 5.0)
    * *Intent:* """ Get the zonefile metadata See `zonefile_metadata`_ :returns: A dictionary with the database meta...
  * `get` **(Parameter Forwarders)** (Impact: 2.8)
    * *Intent:* """ Wrapper for :func:`ZoneInfoFile.zones.get`. This is a convenience method for retrieving zones fr...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 52
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 33`, `args: 8`, `func_start: 8`, `class_start: 2`
* *Risk/State:* `state_mutation: 20`, `dead_code: 2`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `io: 2`, `api: 11`, `import: 7`
* *Defense:* `safety: 5`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 70.259
  * `Choke Point (Betweenness):` 0.02 | `Ripple Effect (Closeness):` 0.202429
  * `Imports (Out-Degree: 1):` contextlib, dateutil.tz, io, json, pkgutil, tarfile, warnings
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `python-dateutil-2.6.1/dateutil/test/test_imports.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.898)
- **Top Global Matches:** file_cluster_15: 5.898, file_cluster_11: 7.705, file_cluster_13: 7.794
- **Magnitude:** 92.34 | **LOC:** 167 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 16.816; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (43.6%), Connectivity (formerly Api Exposure) (13.5%), Complexity Load (formerly Cognitive Load) (4.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testTzAll` **(Compute Cores)** (Impact: 6.7)
  * `testRRuleAll` **(Parameter Forwarders)** (Impact: 3.8)
  * `testParserAll` **(Parameter Forwarders)** (Impact: 3.3)
    * *Intent:* # All interface from dateutil.parser import parse from dateutil.parser import parserinfo # Other pub...
  * `testRelativeDeltaAll` **(Parameter Forwarders)** (Impact: 3.3)
  * `testZoneinfoStar` **(Parameter Forwarders)** (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 117`, `args: 23`, `func_start: 23`, `class_start: 8`
* *Risk/State:* `state_mutation: 4`, `unreferenced_by_name: 23`
* *Architecture:* `io: 2`, `api: 31`, `import: 48`
* *Defense:* `safety: 3`, `doc: 7`, `test: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.816
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` dateutil, dateutil.easter, dateutil.parser, dateutil.relativedelta, dateutil.rrule, dateutil.tz, dateutil.tzwin, dateutil.zoneinfo...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python-dateutil-2.6.1/dateutil/easter.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.441)
- **Top Global Matches:** file_cluster_9: 6.441, file_cluster_15: 12.399, file_cluster_16: 12.407
- **Magnitude:** 60.64 | **LOC:** 90 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 32.896; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (77.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (35.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `easter` **(Many-Argument Workhorses)** (Impact: 14.1)
    * *Intent:* """ This method was ported from the work done by GM Arts, on top of the algorithm by Claus Tondering...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 3`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 32.896
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.076923
  * `Imports (Out-Degree: 0):` datetime
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `python-dateutil-2.6.1/dateutil/zoneinfo/rebuild.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.492)
- **Top Global Matches:** file_cluster_12: 7.492, file_cluster_7: 9.022, file_cluster_5: 10.113
- **Magnitude:** 35.12 | **LOC:** 53 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 16.816; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (57.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Debt Markers (formerly Tech Debt) (37.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `rebuild` **(Defensive Guards)** (Impact: 11.2)
    * *Intent:* """Rebuild the internal timezone info in dateutil/zoneinfo/zoneinfo*tar* filename is the timezone ta...
  * `_print_on_nosuchfile` **(Stateful Encapsulated Methods)** (Impact: 6.2)
    * *Intent:* """Print helpful troubleshooting message e is an exception raised by subprocess.check_call() """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 18`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 6`, `unreferenced_by_name: 1`
* *Architecture:* `io: 8`, `api: 1`, `import: 7`
* *Defense:* `safety: 4`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.816
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` dateutil.zoneinfo, json, logging, os, shutil, subprocess, tempfile
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python-dateutil-2.6.1/updatezinfo.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 7.054)
- **Top Global Matches:** file_cluster_9: 7.054, file_cluster_15: 12.664, file_cluster_16: 12.838
- **Magnitude:** 34.62 | **LOC:** 56 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 16.816; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (63.2%), Complexity Load (formerly Cognitive Load) (61.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Defensive Guards)** (Impact: 7.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 25
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 21`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `io: 4`, `api: 1`, `import: 7`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.816
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` dateutil.zoneinfo, hashlib, io, json, os, six.moves.urllib
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python-dateutil-2.6.1/dateutil/_common.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.515)
- **Top Global Matches:** file_cluster_15: 5.515, file_cluster_11: 7.782, file_cluster_2: 7.914
- **Magnitude:** 31.98 | **LOC:** 35 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 55.324; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Connectivity (formerly Api Exposure) (65.6%), Guard Balance (formerly Safety Score) (53.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__eq__` **(Defensive Guards)** (Impact: 5.5)
  * `__call__` **(Compute Cores)** (Impact: 5.4)
  * `__repr__` **(Compute Cores)** (Impact: 4.5)
  * `__init__` **(Parameter Forwarders)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 12`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `api: 5`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 55.324
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.164103
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `python-dateutil-2.6.1/dateutil/test/test_easter.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 4.742)
- **Top Global Matches:** file_cluster_15: 4.742, file_cluster_2: 6.051, file_cluster_11: 6.371
- **Magnitude:** 20.1 | **LOC:** 100 | **CtrlFlow:** 4.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 16.816; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (47.4%), Connectivity (formerly Api Exposure) (7.8%), Complexity Load (formerly Cognitive Load) (3.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testEasterWestern` **(Parameter Forwarders)** (Impact: 3.0)
  * `testEasterOrthodox` **(Parameter Forwarders)** (Impact: 3.0)
  * `testEasterJulian` **(Parameter Forwarders)** (Impact: 3.0)
  * `testEasterBadMethod` **(Parameter Forwarders)** (Impact: 1.6)
    * *Intent:* # Invalid methods raise ValueError with self.assertRaises(ValueError): easter(1975, 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 15`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`, `unreferenced_by_name: 4`
* *Architecture:* `api: 5`, `import: 5`
* *Defense:* `safety: 2`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.816
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` datetime, dateutil.easter, unittest, unittest2
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python-dateutil-2.6.1/dateutil/_version.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.822)
- **Top Global Matches:** file_cluster_2: 2.822, file_cluster_17: 5.46, file_cluster_13: 6.53
- **Magnitude:** 17.6 | **LOC:** 11 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 74.467; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (83.2%), Guard Balance (formerly Safety Score) (53.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* `state_mutation: 5`
* *Architecture:* None
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 74.467
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.180556
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `python-dateutil-2.6.1/setup.py` (PYTHON | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.091)
- **Top Global Matches:** file_cluster_2: 3.091, file_cluster_17: 4.833, file_cluster_13: 5.543
- **Magnitude:** 15.82 | **LOC:** 48 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 16.816; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (62.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (2.9%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 9`
* *Risk/State:* `fragile_debt: 1`
* *Architecture:* `io: 2`, `import: 6`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.816
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` codecs, dateutil._version, os, os.path, re, setuptools
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python-dateutil-2.6.1/zonefile_metadata.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.015)
- **Top Global Matches:** file_cluster_2: 2.015, file_cluster_17: 4.891, file_cluster_13: 6.239
- **Magnitude:** 15.5 | **LOC:** 25 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.816
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python-dateutil-2.6.1/dateutil/tz/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Centroid distance: 4.791)
- **Top Global Matches:** file_cluster_14: 4.791, file_cluster_7: 6.837, file_cluster_5: 11.196
- **Magnitude:** 13.08 | **LOC:** 6 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **1**; blast radius 90.825; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (52.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (22.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 90.825
  * `Choke Point (Betweenness):` 0.024359 | `Ripple Effect (Closeness):` 0.226244
  * `Imports (Out-Degree: 1):` .tz
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `python-dateutil-2.6.1/dateutil/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.887)
- **Top Global Matches:** file_cluster_2: 4.887, file_cluster_17: 5.617, file_cluster_13: 5.993
- **Magnitude:** 10.52 | **LOC:** 3 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **1**; blast radius 51.01; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`
* *Risk/State:* None
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 51.01
  * `Choke Point (Betweenness):` 0.016923 | `Ripple Effect (Closeness):` 0.202341
  * `Imports (Out-Degree: 1):` ._version
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `python-dateutil-2.6.1/dateutil/test/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Centroid distance: 0.0)
- **Magnitude:** 10.52 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.816
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python-dateutil-2.6.1/dateutil/tzwin.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Centroid distance: 6.522)
- **Top Global Matches:** file_cluster_14: 6.522, file_cluster_7: 13.634, file_cluster_5: 17.036
- **Magnitude:** 10.52 | **LOC:** 3 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 18.602; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (52.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.602
  * `Choke Point (Betweenness):` 0.002051 | `Ripple Effect (Closeness):` 0.038462
  * `Imports (Out-Degree: 1):` .tz.win
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

*No file sits within 2% of a second archetype -- no mixed-responsibility candidates.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `python-dateutil-2.6.1/dateutil/tz/tz.py` -> **Severity: 5.333** (Bridge: 0.0533 * Flux: 100.0%)
- `python-dateutil-2.6.1/dateutil/parser.py` -> **Severity: 2.436** (Bridge: 0.0244 * Flux: 100.0%)
- `python-dateutil-2.6.1/dateutil/zoneinfo/__init__.py` -> **Severity: 2.0** (Bridge: 0.02 * Flux: 100.0%)
- `python-dateutil-2.6.1/dateutil/rrule.py` -> **Severity: 1.615** (Bridge: 0.0162 * Flux: 100.0%)
- `python-dateutil-2.6.1/dateutil/relativedelta.py` -> **Severity: 0.692** (Bridge: 0.0069 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `python-dateutil-2.6.1/dateutil/tz/tz.py` -> **Severity: 17.492** (Embedded: 0.2024 * Error Risk: 86.4113%)
- `python-dateutil-2.6.1/dateutil/tz/_common.py` -> **Severity: 14.555** (Embedded: 0.2031 * Error Risk: 71.6562%)
- `python-dateutil-2.6.1/dateutil/tz/win.py` -> **Severity: 14.537** (Embedded: 0.191 * Error Risk: 76.1192%)
- `python-dateutil-2.6.1/dateutil/zoneinfo/__init__.py` -> **Severity: 14.294** (Embedded: 0.2024 * Error Risk: 70.6116%)
- `python-dateutil-2.6.1/dateutil/relativedelta.py` -> **Severity: 13.029** (Embedded: 0.1713 * Error Risk: 76.0466%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `python-dateutil-2.6.1/dateutil/tz/tz.py` -> **Severity: 8472.9** (Blast Radius: 108.559 * Doc Risk: 78.0488%)
- `python-dateutil-2.6.1/dateutil/_common.py` -> **Severity: 5532.4** (Blast Radius: 55.324 * Doc Risk: 100.0%)
- `python-dateutil-2.6.1/dateutil/tz/_common.py` -> **Severity: 5200.347** (Blast Radius: 91.006 * Doc Risk: 57.1429%)
- `python-dateutil-2.6.1/dateutil/relativedelta.py` -> **Severity: 3418.757** (Blast Radius: 36.72 * Doc Risk: 93.1034%)
- `python-dateutil-2.6.1/dateutil/tz/win.py` -> **Severity: 3384.759** (Blast Radius: 57.74 * Doc Risk: 58.6207%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 4413 call pairs -- scoped 32.2%, unique 0.0%, ambiguous 3.7%, external 64.1%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 4413 | 32.2% | 0.0% | 3.7% | 64.1% |

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
