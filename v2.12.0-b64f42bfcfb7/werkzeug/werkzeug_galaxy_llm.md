# ARCHITECTURAL_BRIEF: werkzeug
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
- **Scope:** 192 analyzed artifact(s), 22284 LOC.
- **Load-bearing artifact:** `werkzeug-3.1.8/src/werkzeug/exceptions.py` -- 32 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `werkzeug-3.1.8/src/werkzeug/serving.py` -- pulls in 33 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `werkzeug-3.1.8/src/werkzeug/test.py` at magnitude 1140.14 (structural weight, not risk).
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
| Total Artifacts | 220 |
| Analyzed Artifacts (Scanned) | 192 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 28 |
| Total LOC | 22284 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 87.3% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.39 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0512 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 21.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.6619 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 13 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 133 | 20930 | 69.3% |
| HTML | 41 | 757 | 21.4% |
| PLAINTEXT | 7 | 0 | 3.6% |
| CSS | 7 | 597 | 3.6% |
| MARKDOWN | 3 | 0 | 1.6% |
| XML | 1 | 0 | 0.5% |

## 4.1 SOURCE ENCODINGS
All 192 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 35%, Generic / Templated Code Files 17%, Parameter Forwarders Files 16%, Large Core Modules (2) 12%, Declarative / Non-Code 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 182 | 94.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 10 | 5.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 28*

**Composition by Extension & Reason:**
- `.png`: 15x Excluded (Explicitly Denied Extension: '.png')
- `.http`: 6x Excluded (Unsupported Extension: '.http')
- `.rst`: 2x Excluded (Unsupported Extension: '.rst')
- `no_extension`: 1x Unsupported Format (.undeterminable)
- `.ico`: 1x Excluded (Explicitly Denied Extension: '.ico')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 98.1 | 23.4 | 16.8 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 92.6 | 38.1 | 49.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 3.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 13.8 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 99.3 | 22.4 | 8.8 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.6 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 23.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 7.3 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 48.2 | 52.9 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 346 | 67 | 7 | `werkzeug-3.1.8/tests/test_datastructures.py` |
| cleanup | 69 | 19 | 0 | `werkzeug-3.1.8/tests/test_send_file.py` |
| guards | 2705 | 94 | 27 | `werkzeug-3.1.8/tests/test_datastructures.py` |
| danger | 842 | 81 | 13 | `werkzeug-3.1.8/src/werkzeug/datastructures/mixins.py` |
| concurrency | 157 | 29 | 2 | `werkzeug-3.1.8/tests/test_local.py` |
| connectivity | 2273 | 149 | 31 | `werkzeug-3.1.8/tests/test_datastructures.py` |
| io | 491 | 79 | 7 | `werkzeug-3.1.8/src/werkzeug/_reloader.py` |
| crypto | 15 | 5 | 0 | `werkzeug-3.1.8/src/werkzeug/serving.py` |
| ipc | 9 | 3 | 0 | `werkzeug-3.1.8/tests/conftest.py` |
| time | 31 | 12 | 0 | `werkzeug-3.1.8/src/werkzeug/http.py` |
| serialization | 2 | 1 | 0 | `werkzeug-3.1.8/tests/test_datastructures.py` |
| regex | 51 | 15 | 0 | `werkzeug-3.1.8/tests/test_debug.py` |
| events | 35 | 12 | 0 | `werkzeug-3.1.8/src/werkzeug/serving.py` |
| tests | 937 | 27 | 7 | `werkzeug-3.1.8/tests/test_routing.py` |
| docs | 761 | 108 | 11 | `werkzeug-3.1.8/src/werkzeug/test.py` |
| debt | 102 | 26 | 1 | `werkzeug-3.1.8/src/werkzeug/datastructures/structures.py` |
| mutation | 9514 | 155 | 136 | `werkzeug-3.1.8/tests/test_routing.py` |
| dead_code | 602 | 39 | 3 | `werkzeug-3.1.8/tests/test_routing.py` |
| credential | 2 | 2 | 0 | `werkzeug-3.1.8/src/werkzeug/http.py` |
| threat | 2 | 1 | 0 | `werkzeug-3.1.8/examples/cupoftee/network.py` |
| ml_ai | 4 | 2 | 0 | `werkzeug-3.1.8/src/werkzeug/local.py` |
| ui | 33 | 15 | 0 | `werkzeug-3.1.8/examples/coolmagic/utils.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `werkzeug-3.1.8/src/werkzeug/_reloader.py` (Hits: 51)
- `werkzeug-3.1.8/src/werkzeug/serving.py` (Hits: 50)
- `werkzeug-3.1.8/src/werkzeug/utils.py` (Hits: 20)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **exceptions.py** (`werkzeug-3.1.8/src/werkzeug/exceptions.py`) — 32 inbound connections
2. **__init__.py** (`werkzeug-3.1.8/src/werkzeug/wrappers/__init__.py`) — 32 inbound connections
3. **response.py** (`werkzeug-3.1.8/src/werkzeug/wrappers/response.py`) — 28 inbound connections
4. **__init__.py** (`werkzeug-3.1.8/src/werkzeug/datastructures/__init__.py`) — 26 inbound connections
5. **http.py** (`werkzeug-3.1.8/src/werkzeug/http.py`) — 25 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **serving.py** (`werkzeug-3.1.8/src/werkzeug/serving.py`) — 33 outbound dependencies
2. **test.py** (`werkzeug-3.1.8/src/werkzeug/test.py`) — 25 outbound dependencies
3. **utils.py** (`werkzeug-3.1.8/src/werkzeug/utils.py`) — 23 outbound dependencies
4. **test_serving.py** (`werkzeug-3.1.8/tests/test_serving.py`) — 23 outbound dependencies
5. **shared_data.py** (`werkzeug-3.1.8/src/werkzeug/middleware/shared_data.py`) — 17 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `send_file` **(Many-Argument Workhorses)** (@ `werkzeug-3.1.8/src/werkzeug/utils.py`) -> Impact: **158.7** | LOC: 217
- `__init__` **(Many-Argument Workhorses)** (@ `werkzeug-3.1.8/src/werkzeug/test.py`) -> Impact: **156.9** | LOC: 97
- `match` **(Many-Argument Workhorses)** (@ `werkzeug-3.1.8/src/werkzeug/routing/matcher.py`) -> Impact: **121.8** | LOC: 134
- `match` **(Many-Argument Workhorses)** (@ `werkzeug-3.1.8/src/werkzeug/routing/map.py`) -> Impact: **82.7** | LOC: 173
- `build` **(Many-Argument Workhorses)** (@ `werkzeug-3.1.8/src/werkzeug/routing/map.py`) -> Impact: **78.6** | LOC: 101
- `_match` **(Many-Argument Workhorses)** (@ `werkzeug-3.1.8/src/werkzeug/routing/matcher.py`) -> Impact: **76.4** | LOC: 88
- `dump_cookie` **(Many-Argument Workhorses)** (@ `werkzeug-3.1.8/src/werkzeug/http.py`) -> Impact: **76.2** | LOC: 153
- `__init__` **(Many-Argument Workhorses)** (@ `werkzeug-3.1.8/src/werkzeug/serving.py`) -> Impact: **71.1** | LOC: 102
- `is_resource_modified` **(Many-Argument Workhorses)** (@ `werkzeug-3.1.8/src/werkzeug/sansio/http.py`) -> Impact: **70.3** | LOC: 77
- `proxy_to` **(Many-Argument Workhorses)** (@ `werkzeug-3.1.8/src/werkzeug/middleware/http_proxy.py`) -> Impact: **66.4** | LOC: 121

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `werkzeug-3.1.8/src/werkzeug` | 15 | 6125.86 | 39.82% | 0.54% |
| `werkzeug-3.1.8/tests` | 17 | 4705.96 | 23.52% | 0.0% |
| `werkzeug-3.1.8/src/werkzeug/datastructures` | 11 | 2553.54 | 37.88% | 46.8% |
| `werkzeug-3.1.8/src/werkzeug/routing` | 6 | 2083.56 | 42.4% | 0.0% |
| `werkzeug-3.1.8/src/werkzeug/sansio` | 6 | 1240.04 | 35.28% | 4.81% |
| `werkzeug-3.1.8/src/werkzeug/middleware` | 7 | 939.72 | 42.33% | 0.0% |
| `werkzeug-3.1.8/src/werkzeug/wrappers` | 3 | 699.4 | 30.87% | 2.88% |
| `werkzeug-3.1.8/examples/simplewiki` | 6 | 443.38 | 30.89% | 0.0% |
| `werkzeug-3.1.8/examples/cupoftee` | 6 | 413.18 | 50.7% | 0.0% |
| `werkzeug-3.1.8/examples` | 11 | 380.3 | 30.33% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `werkzeug-3.1.8/src/werkzeug/datastructures/mixins.py` -> **100.0%** Exposure
- `werkzeug-3.1.8/src/werkzeug/datastructures/structures.py` -> **99.9999%** Exposure
- `werkzeug-3.1.8/src/werkzeug/datastructures/auth.py` -> **99.9918%** Exposure
- `werkzeug-3.1.8/src/werkzeug/datastructures/range.py` -> **99.9901%** Exposure
- `werkzeug-3.1.8/src/werkzeug/datastructures/accept.py` -> **94.9539%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `werkzeug-3.1.8/src/werkzeug/_internal.py` -> **100.0%** Exposure
- `werkzeug-3.1.8/src/werkzeug/_reloader.py` -> **100.0%** Exposure
- `werkzeug-3.1.8/src/werkzeug/datastructures/cache_control.py` -> **100.0%** Exposure
- `werkzeug-3.1.8/src/werkzeug/datastructures/file_storage.py` -> **100.0%** Exposure
- `werkzeug-3.1.8/src/werkzeug/exceptions.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `werkzeug-3.1.8/tests/test_routing.py` -> **82** Orphaned Functions | **2** Duplicates
- `werkzeug-3.1.8/tests/test_wrappers.py` -> **81** Orphaned Functions | **0** Duplicates
- `werkzeug-3.1.8/tests/test_datastructures.py` -> **62** Orphaned Functions | **0** Duplicates
- `werkzeug-3.1.8/tests/test_http.py` -> **60** Orphaned Functions | **0** Duplicates
- `werkzeug-3.1.8/tests/test_local.py` -> **58** Orphaned Functions | **2** Duplicates

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
- **Unknown Dependencies:** `717` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `werkzeug-3.1.8/src/werkzeug/test.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.906)
- **Top Global Matches:** file_cluster_5: 6.906, file_cluster_12: 9.805, file_cluster_7: 10.887
- **Magnitude:** 1140.14 | **LOC:** 1465 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **21** in-repo importer(s); it depends on **25**; blast radius 17.785; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.6%), Connectivity (formerly Api Exposure) (60.5%)
- **Documentation Coverage:** 52.0325% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 156.9)
  * `stream_encode_multipart` **(Many-Argument Workhorses)** (Impact: 46.9)
  * `open` **(Many-Argument Workhorses)** (Impact: 34.4)
  * `resolve_redirect` **(Many-Argument Workhorses)** (Impact: 27.1)
  * `_from_response_header` **(Stateful Encapsulated Methods)** (Impact: 23.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 143 instances
* *State Mutation (weighted view):* 484
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 165`, `structural_boundaries: 238`, `args: 65`, `func_start: 65`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 198`
* *Architecture:* `io: 11`, `api: 54`, `import: 48`
* *Defense:* `safety: 31`, `doc: 60`, `test: 1`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.785
  * `Choke Point (Betweenness):` 0.010773 | `Ripple Effect (Closeness):` 0.236535
  * `Imports (Out-Degree: 13):` ._internal, .datastructures, .http, .sansio.multipart, .urls, .utils, .wrappers.request, .wrappers.response...
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `werkzeug-3.1.8/src/werkzeug/http.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.61)
- **Top Global Matches:** file_cluster_5: 8.61, file_cluster_4: 9.682, file_cluster_12: 9.724
- **Magnitude:** 918.04 | **LOC:** 1444 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **25** in-repo importer(s); it depends on **14**; blast radius 59.722; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.8%), Connectivity (formerly Api Exposure) (62.1%)
- **Documentation Coverage:** 53.8462% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dump_cookie` **(Many-Argument Workhorses)** (Impact: 76.2)
  * `parse_options_header` **(Compute Cores)** (Impact: 50.1)
    * *Intent:* """Parse a header that consists of a value with ``key=value`` parameters separated by semicolons ``;...
  * `parse_range_header` **(Defensive Guards)** (Impact: 28.8)
  * `parse_list_header` **(Compute Cores)** (Impact: 19.9)
    * *Intent:* """Parse a header value that consists of a list of comma separated items according to `RFC 9110 <htt...
  * `parse_accept_header` **(Many-Argument Workhorses)** (Impact: 19.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 141 instances
* *State Mutation (weighted view):* 437
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 172`, `structural_boundaries: 180`, `args: 40`, `func_start: 39`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 155`, `planned_debt: 1`
* *Architecture:* `api: 41`, `import: 21`
* *Defense:* `safety: 25`, `doc: 34`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 59.722
  * `Choke Point (Betweenness):` 0.006076 | `Ripple Effect (Closeness):` 0.292531
  * `Imports (Out-Degree: 3):` ._internal, .datastructures, .sansio, __future__, _typeshed.wsgi, datetime, email.utils, enum...
  * `Imported By (In-Degree: 25):` (Excluded from Brief to save tokens)

### `werkzeug-3.1.8/tests/test_routing.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.461)
- **Top Global Matches:** file_cluster_15: 7.461, file_cluster_12: 7.76, file_cluster_11: 8.141
- **Magnitude:** 894.18 | **LOC:** 1557 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 1.363; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (39.8%), Guard Balance (formerly Safety Score) (38.8%), Connectivity (formerly Api Exposure) (12.5%)
- **Documentation Coverage:** 95.7895% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_basic_routing` **(Defensive Guards)** (Impact: 22.6)
  * `test_path` **(Defensive Guards)** (Impact: 19.9)
  * `test_strict_slashes_redirect` **(Defensive Guards)** (Impact: 17.6)
  * `test_merge_slashes_match` **(Defensive Guards)** (Impact: 14.1)
  * `test_complex_routing_rules` **(Defensive Guards)** (Impact: 14.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 89 instances
* *State Mutation (weighted view):* 410
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 175`, `structural_boundaries: 486`, `args: 106`, `func_start: 94`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 232`, `duplicate_logic: 2`, `unreferenced_by_name: 82`
* *Architecture:* `api: 98`, `import: 11`
* *Defense:* `safety: 275`, `doc: 4`, `test: 160`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.363
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` gc, pytest, typing, uuid, werkzeug, werkzeug.datastructures, werkzeug.exceptions, werkzeug.test...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `werkzeug-3.1.8/src/werkzeug/serving.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.889)
- **Top Global Matches:** file_cluster_4: 8.889, file_cluster_5: 10.664, file_cluster_12: 11.134
- **Magnitude:** 836.66 | **LOC:** 1127 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **16** in-repo importer(s); it depends on **33**; blast radius 8.608; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.0%), Connectivity (formerly Api Exposure) (65.1%)
- **Documentation Coverage:** 81.0811% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 71.1)
  * `run_wsgi` **(Defensive Guards)** (Impact: 45.5)
  * `run_simple` **(Many-Argument Workhorses)** (Impact: 45.4)
  * `make_environ` **(Compute Cores)** (Impact: 26.6)
  * `make_server` **(Many-Argument Workhorses)** (Impact: 21.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 120 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 382
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 185`, `args: 38`, `func_start: 38`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 19`, `high_risk_execution: 1`, `state_mutation: 142`
* *Architecture:* `io: 50`, `api: 38`, `import: 41`
* *Defense:* `safety: 48`, `doc: 19`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.608
  * `Choke Point (Betweenness):` 0.006801 | `Ripple Effect (Closeness):` 0.100441
  * `Imports (Out-Degree: 7):` ._internal, ._reloader, .debug, .debug.tbtools, .exceptions, .http, .middleware.shared_data, .urls...
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `werkzeug-3.1.8/src/werkzeug/datastructures/structures.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.551)
- **Top Global Matches:** file_cluster_5: 6.551, file_cluster_0: 10.219, file_cluster_12: 10.415
- **Magnitude:** 813.46 | **LOC:** 1240 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **19** in-repo importer(s); it depends on **10**; blast radius 43.6; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (88.7%), Guard Balance (formerly Safety Score) (64.2%)
- **Documentation Coverage:** 74.8899% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Defensive Guards)** (Impact: 20.6)
  * `__eq__` **(Defensive Guards)** (Impact: 16.8)
  * `iter_multi_items` **(Defensive Guards)** (Impact: 12.4)
  * `items` **(Generic / Templated Code)** (Impact: 11.0)
  * `get` **(Generic / Templated Code)** (Impact: 9.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 68 instances
* *State Mutation (weighted view):* 214
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 314`, `args: 134`, `func_start: 134`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 78`, `planned_debt: 1`, `duplicate_logic: 30`
* *Architecture:* `api: 101`, `import: 14`
* *Defense:* `safety: 38`, `doc: 48`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 43.6
  * `Choke Point (Betweenness):` 0.003656 | `Ripple Effect (Closeness):` 0.266432
  * `Imports (Out-Degree: 4):` .._internal, ..exceptions, ..http, .mixins, __future__, collections.abc, copy, typing...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `werkzeug-3.1.8/src/werkzeug/routing/rules.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.467)
- **Top Global Matches:** file_cluster_5: 8.467, file_cluster_12: 11.309, file_cluster_7: 11.996
- **Magnitude:** 797.94 | **LOC:** 928 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **12**; blast radius 8.576; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.8%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 68.8525% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_compile_builder` **(Stateful Encapsulated Methods)** (Impact: 58.6)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 47.8)
  * `_parse_rule` **(Many-Argument Workhorses)** (Impact: 46.2)
  * `suitable_for` **(Many-Argument Workhorses)** (Impact: 25.6)
  * `get_rules` **(Defensive Guards)** (Impact: 15.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 123 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 400
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 133`, `structural_boundaries: 114`, `args: 38`, `func_start: 37`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 36`, `high_risk_execution: 2`, `state_mutation: 154`
* *Architecture:* `api: 32`, `import: 13`
* *Defense:* `safety: 16`, `doc: 24`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.576
  * `Choke Point (Betweenness):` 0.002704 | `Ripple Effect (Closeness):` 0.10733
  * `Imports (Out-Degree: 6):` ..datastructures, ..urls, .converters, .map, __future__, ast, dataclasses, re...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `werkzeug-3.1.8/src/werkzeug/routing/map.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 11.84)
- **Top Global Matches:** file_cluster_4: 11.84, file_cluster_5: 12.585, file_cluster_6: 12.928
- **Magnitude:** 691.02 | **LOC:** 929 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **17**; blast radius 13.179; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 70.8333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `match` **(Many-Argument Workhorses)** (Impact: 82.7)
  * `build` **(Many-Argument Workhorses)** (Impact: 78.6)
  * `bind_to_environ` **(Many-Argument Workhorses)** (Impact: 45.6)
  * `_partial_build` **(Many-Argument Workhorses)** (Impact: 26.5)
  * `bind` **(Many-Argument Workhorses)** (Impact: 24.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 80 instances
* *State Mutation (weighted view):* 257
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 154`, `args: 28`, `func_start: 27`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 97`
* *Architecture:* `api: 23`, `concurrency: 1`, `import: 33`
* *Defense:* `safety: 21`, `doc: 18`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.179
  * `Choke Point (Betweenness):` 0.00754 | `Ripple Effect (Closeness):` 0.112834
  * `Imports (Out-Degree: 11):` .._internal, ..datastructures, ..exceptions, ..urls, ..wrappers.request, ..wsgi, .converters, .exceptions...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `werkzeug-3.1.8/tests/test_datastructures.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.137)
- **Top Global Matches:** file_cluster_12: 7.137, file_cluster_15: 7.885, file_cluster_11: 8.889
- **Magnitude:** 656.32 | **LOC:** 1298 | **CtrlFlow:** 2.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 1.363; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (32.8%), Guard Balance (formerly Safety Score) (29.7%), Connectivity (formerly Api Exposure) (12.8%)
- **Documentation Coverage:** 97.6471% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_basic_interface` **(Defensive Guards)** (Impact: 10.4)
  * `test_mime_accept` **(Defensive Guards)** (Impact: 7.5)
  * `test_pickle` **(Defensive Guards)** (Impact: 6.9)
  * `test_ordered_interface` **(Defensive Guards)** (Impact: 6.1)
  * `create_instance` **(Compute Cores)** (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 36 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 314
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 533`, `args: 89`, `func_start: 85`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 2`, `state_mutation: 242`, `planned_debt: 1`, `unreferenced_by_name: 62`
* *Architecture:* `io: 3`, `api: 106`, `import: 14`
* *Defense:* `safety: 324`, `doc: 2`, `test: 126`, `immutability_locks: 23`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.363
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` __future__, contextlib, copy, io, pickle, pytest, tempfile, typing...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `werkzeug-3.1.8/tests/test_test.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.137)
- **Top Global Matches:** file_cluster_12: 7.137, file_cluster_15: 7.14, file_cluster_13: 8.176
- **Magnitude:** 580.48 | **LOC:** 928 | **CtrlFlow:** 4.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 1.363; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (38.2%), Complexity Load (formerly Cognitive Load) (35.1%), Connectivity (formerly Api Exposure) (13.4%)
- **Documentation Coverage:** 95.6522% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_follow_redirect_body` **(Defensive Guards)** (Impact: 11.5)
  * `app` **(Defensive Guards)** (Impact: 9.1)
  * `test_run_wsgi_apps` **(Defensive Guards)** (Impact: 9.1)
  * `redirect_with_get_app` **(Compute Cores)** (Impact: 7.6)
  * `app` **(Compute Cores)** (Impact: 6.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 236
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 361`, `args: 99`, `func_start: 96`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 182`, `duplicate_logic: 2`, `unreferenced_by_name: 52`
* *Architecture:* `io: 19`, `api: 96`, `import: 20`
* *Defense:* `safety: 177`, `doc: 4`, `test: 70`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.363
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` functools, io, json, pytest, sys, werkzeug.datastructures, werkzeug.formparser, werkzeug.test...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `werkzeug-3.1.8/tests/test_wrappers.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.769)
- **Top Global Matches:** file_cluster_15: 6.769, file_cluster_11: 7.01, file_cluster_12: 7.432
- **Magnitude:** 557.4 | **LOC:** 1382 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 1.363; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (29.8%), Complexity Load (formerly Cognitive Load) (23.9%), Connectivity (formerly Api Exposure) (12.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_new_response_iterator_behavior` **(Defensive Guards)** (Impact: 4.8)
  * `test_base_response` **(Defensive Guards)** (Impact: 4.3)
  * `test_common_response_descriptors` **(Defensive Guards)** (Impact: 4.3)
  * `test_base_request` **(Defensive Guards)** (Impact: 3.2)
  * `test_type_forcing` **(Defensive Guards)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 258
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 528`, `args: 105`, `func_start: 95`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 242`, `fragile_debt: 4`, `unreferenced_by_name: 81`
* *Architecture:* `io: 12`, `api: 100`, `import: 34`
* *Defense:* `safety: 322`, `test: 99`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.363
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` contextlib, datetime, io, json, os, pytest, werkzeug, werkzeug.datastructures...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `werkzeug-3.1.8/src/werkzeug/utils.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.251)
- **Top Global Matches:** file_cluster_4: 8.251, file_cluster_12: 10.39, file_cluster_5: 10.826
- **Magnitude:** 543.1 | **LOC:** 685 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **23**; blast radius 21.46; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.8%), Connectivity (formerly Api Exposure) (64.1%)
- **Documentation Coverage:** 80.4348% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `send_file` **(Many-Argument Workhorses)** (Impact: 158.7)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 23.4)
  * `find_modules` **(Many-Argument Workhorses)** (Impact: 15.6)
  * `__get__` **(Compute Cores)** (Impact: 15.0)
  * `send_from_directory` **(Many-Argument Workhorses)** (Impact: 10.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 75 instances
* *State Mutation (weighted view):* 231
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 101`, `args: 16`, `func_start: 16`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 81`
* *Architecture:* `io: 20`, `api: 18`, `import: 30`
* *Defense:* `safety: 17`, `doc: 12`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 21.46
  * `Choke Point (Betweenness):` 0.011245 | `Ripple Effect (Closeness):` 0.256882
  * `Imports (Out-Degree: 9):` ._internal, .datastructures, .exceptions, .security, .wrappers, .wrappers.request, .wrappers.response, .wsgi...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `werkzeug-3.1.8/src/werkzeug/testapp.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 4.397)
- **Top Global Matches:** file_cluster_7: 4.397, file_cluster_12: 5.359, file_cluster_5: 6.906
- **Magnitude:** 491.4 | **LOC:** 195 | **CtrlFlow:** 11.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 1.363; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (69.4%), Complexity Load (formerly Cognitive Load) (53.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 56
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 37`, `args: 3`, `func_start: 1`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 20`
* *Architecture:* `io: 5`, `import: 12`
* *Defense:* `safety: 3`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.363
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` .serving, .wrappers.request, .wrappers.response, __future__, hooks, importlib.metadata, markupsafe, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `werkzeug-3.1.8/tests/test_local.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.612)
- **Top Global Matches:** file_cluster_12: 6.612, file_cluster_7: 9.177, file_cluster_15: 9.723
- **Magnitude:** 453.08 | **LOC:** 616 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 1.363; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (48.7%), Guard Balance (formerly Safety Score) (34.2%)
- **Documentation Coverage:** 98.4375% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_basic_local` **(Callbacks & Closures)** (Impact: 5.3)
  * `test_proxy_aiter` **(Interface Declarations)** (Impact: 4.3)
  * `test_proxy_numeric` **(Defensive Guards)** (Impact: 4.0)
  * `test_proxy_attributes` **(Defensive Guards)** (Impact: 4.0)
  * `__round__` **(Parameter Forwarders)** (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 22 instances
* *Amplified Cascading Flux:* 7 instances
* *Concurrency (weighted view):* 143
* *State Mutation (weighted view):* 99
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 275`, `args: 79`, `func_start: 75`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 85`, `duplicate_logic: 2`, `unreferenced_by_name: 58`
* *Architecture:* `api: 59`, `concurrency: 33`, `import: 9`
* *Defense:* `safety: 125`, `doc: 1`, `test: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.363
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` asyncio, contextvars, copy, math, operator, pytest, threading, time...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `werkzeug-3.1.8/src/werkzeug/wrappers/response.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.404)
- **Top Global Matches:** file_cluster_5: 6.404, file_cluster_12: 8.601, file_cluster_0: 9.587
- **Magnitude:** 442.8 | **LOC:** 839 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **28** in-repo importer(s); it depends on **16**; blast radius 25.601; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.2%), Connectivity (formerly Api Exposure) (66.1%)
- **Documentation Coverage:** 54.4304% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_wsgi_headers` **(Many-Argument Workhorses)** (Impact: 33.5)
    * *Intent:* """This is automatically called right before the response is started and returns headers modified fo...
  * `make_conditional` **(Many-Argument Workhorses)** (Impact: 26.2)
  * `_process_range_request` **(Many-Argument Workhorses)** (Impact: 20.5)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 13.0)
  * `get_app_iter` **(Compute Cores)** (Impact: 11.7)
    * *Intent:* """Returns the application iterator for the given environ. Depending on the request method and the c...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 46 instances
* *State Mutation (weighted view):* 158
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 130`, `args: 42`, `func_start: 42`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 66`, `planned_debt: 1`
* *Architecture:* `api: 37`, `import: 26`
* *Defense:* `safety: 12`, `doc: 27`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 25.601
  * `Choke Point (Betweenness):` 0.01353 | `Ripple Effect (Closeness):` 0.275654
  * `Imports (Out-Degree: 12):` .._internal, ..datastructures, ..exceptions, ..http, ..sansio.response, ..test, ..urls, ..utils...
  * `Imported By (In-Degree: 28):` (Excluded from Brief to save tokens)

### `werkzeug-3.1.8/src/werkzeug/datastructures/headers.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.171)
- **Top Global Matches:** file_cluster_5: 8.171, file_cluster_7: 11.884, file_cluster_14: 12.239
- **Magnitude:** 442.02 | **LOC:** 663 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **11**; blast radius 31.935; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (61.8%)
- **Documentation Coverage:** 74.0385% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `update` **(Many-Argument Workhorses)** (Impact: 28.2)
  * `set` **(Many-Argument Workhorses)** (Impact: 19.8)
    * *Intent:* """Remove all header tuples for `key` and add a new one. The newly added key either appears at the e...
  * `getlist` **(Many-Argument Workhorses)** (Impact: 13.8)
  * `__setitem__` **(Defensive Guards)** (Impact: 10.6)
  * `extend` **(Generic / Templated Code)** (Impact: 9.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 127
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 152`, `args: 64`, `func_start: 64`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 54`, `state_mutation: 45`, `planned_debt: 1`
* *Architecture:* `api: 42`, `import: 12`
* *Defense:* `safety: 27`, `doc: 22`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 31.935
  * `Choke Point (Betweenness):` 0.002453 | `Ripple Effect (Closeness):` 0.276719
  * `Imports (Out-Degree: 5):` .._internal, ..exceptions, ..http, .mixins, .structures, __future__, _typeshed.wsgi, collections.abc...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `werkzeug-3.1.8/src/werkzeug/sansio/response.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 5.428)
- **Top Global Matches:** file_cluster_0: 5.428, file_cluster_16: 8.963, file_cluster_13: 9.034
- **Magnitude:** 441.5 | **LOC:** 764 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **8**; blast radius 9.132; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (65.9%), Guard Balance (formerly Safety Score) (64.6%)
- **Documentation Coverage:** 64.557% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 25.8)
  * `_set_property` **(Stateful Encapsulated Methods)** (Impact: 13.2)
  * `_clean_status` **(Stateful Encapsulated Methods)** (Impact: 10.1)
  * `www_authenticate` **(Generic / Templated Code)** (Impact: 9.7)
  * `retry_after` **(Defensive Guards)** (Impact: 9.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 50 instances
* *State Mutation (weighted view):* 177
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 147`, `args: 44`, `func_start: 40`, `class_start: 1`
* *Risk/State:* `state_mutation: 77`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 39`, `import: 33`
* *Defense:* `safety: 14`, `doc: 33`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.132
  * `Choke Point (Betweenness):` 0.002189 | `Ripple Effect (Closeness):` 0.228978
  * `Imports (Out-Degree: 9):` ..datastructures, ..datastructures.cache_control, ..http, ..utils, __future__, datetime, http, typing
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `werkzeug-3.1.8/src/werkzeug/exceptions.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 4.801)
- **Top Global Matches:** file_cluster_5: 4.801, file_cluster_12: 8.025, file_cluster_7: 9.219
- **Magnitude:** 401.66 | **LOC:** 906 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **32** in-repo importer(s); it depends on **11**; blast radius 47.622; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (94.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.3%)
- **Documentation Coverage:** 90.9091% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__call__` **(Defensive Guards)** (Impact: 9.5)
  * `get_headers` **(Generic / Templated Code)** (Impact: 8.9)
  * `get_response` **(Generic / Templated Code)** (Impact: 7.2)
  * `__init__` **(Compute Cores)** (Impact: 7.1)
  * `get_description` **(Generic / Templated Code)** (Impact: 6.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 62 instances
* *State Mutation (weighted view):* 223
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 128`, `args: 27`, `func_start: 27`, `class_start: 38`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 99`
* *Architecture:* `api: 52`, `import: 17`
* *Defense:* `safety: 10`, `doc: 48`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 47.622
  * `Choke Point (Betweenness):` 0.01427 | `Ripple Effect (Closeness):` 0.31026
  * `Imports (Out-Degree: 7):` ._internal, .datastructures, .http, .sansio.response, .wrappers.request, .wrappers.response, __future__, _typeshed.wsgi...
  * `Imported By (In-Degree: 32):` (Excluded from Brief to save tokens)

### `werkzeug-3.1.8/src/werkzeug/_reloader.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.855)
- **Top Global Matches:** file_cluster_5: 7.855, file_cluster_12: 9.868, file_cluster_7: 11.621
- **Magnitude:** 385.84 | **LOC:** 466 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **15**; blast radius 2.574; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (89.1%), Guard Balance (formerly Safety Score) (80.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 65.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_find_stat_paths` **(Stateful Encapsulated Methods)** (Impact: 19.8)
  * `_get_args_for_reloading` **(I/O & Config Routines)** (Impact: 18.9)
    * *Intent:* """Determine how the script was executed, and return the args needed to execute it again in a new pr...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 14.2)
  * `_find_common_roots` **(Stateful Encapsulated Methods)** (Impact: 11.1)
  * `__init__` **(Generic / Templated Code)** (Impact: 9.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 60 instances
* *High Risk Execution (weighted view):* 3
* *Concurrency (weighted view):* 18
* *State Mutation (weighted view):* 185
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 90`, `args: 27`, `func_start: 26`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 5`, `state_mutation: 65`
* *Architecture:* `io: 51`, `api: 16`, `concurrency: 3`, `import: 22`
* *Defense:* `safety: 11`, `doc: 11`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.574
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.063149
  * `Imports (Out-Degree: 1):` ._internal, __future__, fnmatch, itertools, os, pathlib, signal, subprocess...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `werkzeug-3.1.8/src/werkzeug/sansio/multipart.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 11.505)
- **Top Global Matches:** file_cluster_8: 11.505, file_cluster_3: 17.689, file_cluster_6: 22.064
- **Magnitude:** 365.54 | **LOC:** 332 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **8**; blast radius 3.921; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `next_event` **(Stateful Encapsulated Methods)** (Impact: 50.9)
  * `_parse_data` **(Stateful Encapsulated Methods)** (Impact: 37.6)
  * `send_event` **(Defensive Guards)** (Impact: 29.3)
  * `_last_partial_boundary_index` **(Stateful Encapsulated Methods)** (Impact: 9.8)
    * *Intent:* # Find the last index following which a partial boundary # could be present in the data. This will b...
  * `receive_data` **(Generic / Templated Code)** (Impact: 9.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 58 instances
* *State Mutation (weighted view):* 199
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 52`, `args: 8`, `func_start: 8`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 83`
* *Architecture:* `api: 13`, `import: 9`
* *Defense:* `safety: 11`, `doc: 1`, `sync_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.921
  * `Choke Point (Betweenness):` 0.000214 | `Ripple Effect (Closeness):` 0.174805
  * `Imports (Out-Degree: 4):` ..datastructures, ..exceptions, ..http, __future__, dataclasses, enum, re, typing
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `werkzeug-3.1.8/src/werkzeug/wsgi.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 5.866)
- **Top Global Matches:** file_cluster_5: 5.866, file_cluster_12: 8.761, file_cluster_0: 10.013
- **Magnitude:** 344.26 | **LOC:** 610 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **17** in-repo importer(s); it depends on **8**; blast radius 25.106; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.9%), Connectivity (formerly Api Exposure) (55.9%)
- **Documentation Coverage:** 71.9298% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_input_stream` **(Many-Argument Workhorses)** (Impact: 21.3)
  * `readinto` **(Defensive Guards)** (Impact: 16.2)
  * `get_current_url` **(Many-Argument Workhorses)** (Impact: 11.6)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 10.9)
  * `_next` **(Stateful Encapsulated Methods)** (Impact: 9.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 47 instances
* *State Mutation (weighted view):* 151
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 105`, `args: 36`, `func_start: 35`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 57`
* *Architecture:* `api: 24`, `import: 11`
* *Defense:* `safety: 14`, `doc: 16`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 25.106
  * `Choke Point (Betweenness):` 0.005485 | `Ripple Effect (Closeness):` 0.266432
  * `Imports (Out-Degree: 3):` .exceptions, .sansio, .sansio.utils, __future__, _typeshed.wsgi, functools, io, typing
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `werkzeug-3.1.8/src/werkzeug/local.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.732)
- **Top Global Matches:** file_cluster_5: 7.732, file_cluster_7: 10.792, file_cluster_14: 11.531
- **Magnitude:** 341.6 | **LOC:** 654 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **9**; blast radius 6.344; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 75.4098% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 27.3)
  * `__get__` **(Defensive Guards)** (Impact: 13.3)
  * `__init__` **(Generic / Templated Code)** (Impact: 11.4)
  * `__init__` **(Type Conversions)** (Impact: 7.5)
  * `__delattr__` **(Type Conversions)** (Impact: 5.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 179
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 111`, `args: 47`, `func_start: 38`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 131`
* *Architecture:* `api: 18`, `import: 13`
* *Defense:* `safety: 13`, `doc: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.344
  * `Choke Point (Betweenness):` 0.000637 | `Ripple Effect (Closeness):` 0.078616
  * `Imports (Out-Degree: 1):` .wsgi, __future__, _typeshed.wsgi, contextvars, copy, functools, math, operator...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `werkzeug-3.1.8/tests/test_http.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.324)
- **Top Global Matches:** file_cluster_15: 7.324, file_cluster_13: 7.946, file_cluster_11: 8.203
- **Magnitude:** 339.86 | **LOC:** 821 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 1.363; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (23.5%), Complexity Load (formerly Cognitive Load) (16.9%), Connectivity (formerly Api Exposure) (12.4%)
- **Documentation Coverage:** 98.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_cache_control_header` **(Defensive Guards)** (Impact: 9.8)
  * `test_cookie_maxsize` **(Defensive Guards)** (Impact: 4.7)
  * `test_accept_invalid_float` **(Defensive Guards)** (Impact: 4.7)
  * `test_authorization_header` **(Defensive Guards)** (Impact: 4.2)
  * `test_if_range_parsing` **(Defensive Guards)** (Impact: 4.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 131
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 340`, `args: 61`, `func_start: 60`, `class_start: 3`
* *Risk/State:* `state_mutation: 111`, `fragile_debt: 6`, `unreferenced_by_name: 60`
* *Architecture:* `io: 2`, `api: 63`, `import: 13`
* *Defense:* `safety: 234`, `doc: 1`, `test: 78`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.363
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` base64, datetime, pytest, urllib.parse, werkzeug, werkzeug._internal, werkzeug.datastructures, werkzeug.test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `werkzeug-3.1.8/src/werkzeug/routing/matcher.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.833)
- **Top Global Matches:** file_cluster_8: 9.833, file_cluster_6: 18.555, file_cluster_3: 21.317
- **Magnitude:** 328.24 | **LOC:** 203 | **CtrlFlow:** 38.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **7**; blast radius 3.334; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.2%), Complexity Load (formerly Cognitive Load) (76.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `match` **(Many-Argument Workhorses)** (Impact: 121.8)
  * `_match` **(Many-Argument Workhorses)** (Impact: 76.4)
  * `add` **(Compute Cores)** (Impact: 12.9)
  * `update` **(Stateful Encapsulated Methods)** (Impact: 4.9)
    * *Intent:* # For every state the dynamic transitions should be sorted by # the weight of the transition state =...
  * `_update_state` **(Encapsulated Accessors)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 96
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 45`, `args: 8`, `func_start: 6`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 36`
* *Architecture:* `api: 7`, `import: 11`
* *Defense:* `safety: 6`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.334
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.075871
  * `Imports (Out-Degree: 3):` .converters, .exceptions, .rules, __future__, dataclasses, re, typing
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `werkzeug-3.1.8/src/werkzeug/middleware/lint.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.983)
- **Top Global Matches:** file_cluster_5: 9.983, file_cluster_4: 10.142, file_cluster_12: 11.548
- **Magnitude:** 279.06 | **LOC:** 440 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 1.942; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.5%), Complexity Load (formerly Cognitive Load) (51.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check_start_response` **(Many-Argument Workhorses)** (Impact: 45.0)
  * `close` **(Compute Cores)** (Impact: 25.0)
  * `__call__` **(Many-Argument Workhorses)** (Impact: 18.7)
  * `check_environ` **(Compute Cores)** (Impact: 17.7)
  * `check_headers` **(Compute Cores)** (Impact: 16.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 58
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 81`, `args: 25`, `func_start: 25`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 30`
* *Architecture:* `api: 22`, `import: 11`
* *Defense:* `safety: 6`, `doc: 4`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.942
  * `Choke Point (Betweenness):` 0.000164 | `Ripple Effect (Closeness):` 0.005236
  * `Imports (Out-Degree: 4):` ..datastructures, ..http, ..wsgi, __future__, _typeshed.wsgi, types, typing, urllib.parse...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `werkzeug-3.1.8/src/werkzeug/datastructures/accept.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.885)
- **Top Global Matches:** file_cluster_0: 6.885, file_cluster_5: 9.449, file_cluster_16: 10.268
- **Magnitude:** 273.88 | **LOC:** 351 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **6**; blast radius 5.885; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (95.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.3%)
- **Documentation Coverage:** 59.6154% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_value_matches` **(Stateful Encapsulated Methods)** (Impact: 31.9)
    * *Intent:* # item comes from the client, can't match if it's invalid. if "/" not in item: return False # value ...
  * `best_match` **(Many-Argument Workhorses)** (Impact: 21.4)
  * `best_match` **(Many-Argument Workhorses)** (Impact: 18.4)
  * `_best_single_match` **(Stateful Encapsulated Methods)** (Impact: 9.0)
  * `__init__` **(Defensive Guards)** (Impact: 7.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 75
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 87`, `args: 34`, `func_start: 33`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 25`, `duplicate_logic: 4`
* *Architecture:* `api: 23`, `import: 6`
* *Defense:* `safety: 7`, `doc: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.885
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.203032
  * `Imports (Out-Degree: 1):` .structures, __future__, codecs, collections.abc, re, typing
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `werkzeug-3.1.8/src/werkzeug/security.py` (PYTHON) | Magnitude: 121.88 | Delta: **0.119** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 86, branch: 28, core_var_decl: 25, design_snake_case: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `werkzeug-3.1.8/tests/live_apps/data_app.py` (PYTHON) | Magnitude: 4.72 | Delta: **0.088** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 7, import: 3, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `werkzeug-3.1.8/tests/middleware/test_lint.py` (PYTHON) | Magnitude: 57.74 | Delta: **0.076** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 34, core_var_decl: 18, design_snake_case: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `werkzeug-3.1.8/tests/test_test.py` (PYTHON) | Magnitude: 580.48 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 619, structural_boundaries: 361, core_var_decl: 186, design_snake_case: 186

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `werkzeug-3.1.8/examples/shortly/templates/short_link_details.html` (HTML) | Magnitude: 15.26 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: ssr_boundaries: 12, structural_boundaries: 9, indent_spaces: 9, io: 4
- `werkzeug-3.1.8/examples/cupoftee/templates/layout.html` (HTML) | Magnitude: 15.4 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 17, io: 9, core_var_decl: 7, design_snake_case: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `werkzeug-3.1.8/tests/test_internal.py` (PYTHON) | Magnitude: 10.64 | Delta: **0.089** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 15, safety: 8, state_mutation: 7
- `werkzeug-3.1.8/tests/test_wsgi.py` (PYTHON) | Magnitude: 168.42 | Delta: **0.1** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 230, structural_boundaries: 129, core_var_decl: 78, design_snake_case: 77

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `werkzeug-3.1.8/tests/res/index.html` (HTML) | Magnitude: 14.68 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, indent_spaces: 2, core_var_decl: 2, design_snake_case: 2
- `werkzeug-3.1.8/examples/cupoftee/templates/serverlist.html` (HTML) | Magnitude: 17.24 | Delta: **0.094** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 42, ssr_boundaries: 30, args: 18, structural_boundaries: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `werkzeug-3.1.8/src/werkzeug/sansio/request.py` (PYTHON) | Magnitude: 128.88 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 213, structural_boundaries: 141, generics: 39, core_var_decl: 39
- `werkzeug-3.1.8/src/werkzeug/middleware/lint.py` (PYTHON) | Magnitude: 279.06 | Delta: **0.159** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 311, structural_boundaries: 81, branch: 69, core_var_decl: 56

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `werkzeug-3.1.8/examples/plnt/views.py` (PYTHON) | Magnitude: 29.86 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 14, indent_spaces: 12, state_mutation: 8, core_var_decl: 8

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `werkzeug-3.1.8/src/werkzeug/wrappers/request.py` -> **Severity: 2.395** (Bridge: 0.024 * Flux: 99.9962%)
- `werkzeug-3.1.8/src/werkzeug/exceptions.py` -> **Severity: 1.427** (Bridge: 0.0143 * Flux: 100.0%)
- `werkzeug-3.1.8/src/werkzeug/wrappers/response.py` -> **Severity: 1.353** (Bridge: 0.0135 * Flux: 100.0%)
- `werkzeug-3.1.8/src/werkzeug/utils.py` -> **Severity: 1.125** (Bridge: 0.0112 * Flux: 100.0%)
- `werkzeug-3.1.8/src/werkzeug/test.py` -> **Severity: 1.077** (Bridge: 0.0108 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `werkzeug-3.1.8/src/werkzeug/exceptions.py` -> **Severity: 23.672** (Embedded: 0.3103 * Error Risk: 76.2966%)
- `werkzeug-3.1.8/src/werkzeug/http.py` -> **Severity: 22.761** (Embedded: 0.2925 * Error Risk: 77.8081%)
- `werkzeug-3.1.8/src/werkzeug/datastructures/headers.py` -> **Severity: 22.138** (Embedded: 0.2767 * Error Risk: 80.0%)
- `werkzeug-3.1.8/src/werkzeug/_internal.py` -> **Severity: 21.989** (Embedded: 0.2986 * Error Risk: 73.6339%)
- `werkzeug-3.1.8/src/werkzeug/urls.py` -> **Severity: 20.174** (Embedded: 0.2342 * Error Risk: 86.135%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `werkzeug-3.1.8/src/werkzeug/_internal.py` -> **Severity: 6495.568** (Blast Radius: 80.545 * Doc Risk: 80.6452%)
- `werkzeug-3.1.8/src/werkzeug/datastructures/__init__.py` -> **Severity: 5002.3** (Blast Radius: 50.023 * Doc Risk: 100.0%)
- `werkzeug-3.1.8/src/werkzeug/exceptions.py` -> **Severity: 4329.273** (Blast Radius: 47.622 * Doc Risk: 90.9091%)
- `werkzeug-3.1.8/src/werkzeug/wrappers/request.py` -> **Severity: 3658.874** (Blast Radius: 93.135 * Doc Risk: 39.2857%)
- `werkzeug-3.1.8/src/werkzeug/datastructures/structures.py` -> **Severity: 3265.2** (Blast Radius: 43.6 * Doc Risk: 74.8899%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`panics_and_aborts`:** 205 literal sites + 2 sites through wrappers = 207

- `do_something` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `werkzeug-3.1.8/tests/test_debug.py`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 5478 call pairs -- scoped 35.4%, unique 0.0%, ambiguous 15.8%, external 48.8%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 5478 | 35.4% | 0.0% | 15.8% | 48.8% |

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
