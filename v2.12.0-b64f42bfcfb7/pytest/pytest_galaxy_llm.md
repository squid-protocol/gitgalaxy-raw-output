# ARCHITECTURAL_BRIEF: pytest
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
- **Scope:** 313 analyzed artifact(s), 63874 LOC.
- **Load-bearing artifact:** `pytest-9.0.2/src/pytest/__init__.py` -- 132 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `pytest-9.0.2/src/_pytest/config/__init__.py` -- pulls in 46 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `pytest-9.0.2/src/_pytest/terminal.py` at magnitude 1767.64 (structural weight, not risk).
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
| Total Artifacts | 620 |
| Analyzed Artifacts (Scanned) | 313 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 307 |
| Total LOC | 63874 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 50.5% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2368 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3839 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 11.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.3843 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 4 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 272 | 63218 | 86.9% |
| YAML | 14 | 592 | 4.5% |
| XML | 13 | 0 | 4.2% |
| PLAINTEXT | 5 | 0 | 1.6% |
| MARKDOWN | 4 | 0 | 1.3% |
| JSON | 2 | 12 | 0.6% |
| MAKEFILE | 1 | 27 | 0.3% |
| CSS | 1 | 18 | 0.3% |
| HTML | 1 | 7 | 0.3% |

## 4.1 SOURCE ENCODINGS
All 313 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 36%, Generic / Templated Code Files 22%, Large Core Modules (2) 15%, Large Core Modules (3) 10%, Parameter Forwarders Files 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 304 | 97.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 9 | 2.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 307*

**Composition by Extension & Reason:**
- `.rst`: 270x Excluded (Unsupported Extension: '.rst')
- `no_extension`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.undeterminable)
- `.png`: 8x Excluded (Explicitly Denied Extension: '.png')
- `.ini`: 7x Excluded (Unsupported Extension: '.ini')
- `.toml`: 2x Excluded (Unsupported Extension: '.toml'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.typed`: 2x Excluded (Unsupported Extension: '.typed')
- `.jpg`: 1x Excluded (Explicitly Denied Extension: '.jpg')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')
- `.feature`: 1x Excluded (Unsupported Extension: '.feature')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.2 | 15.1 | 3.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 85.9 | 39.4 | 48.2 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 4.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 8.4 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 87.0 | 15.8 | 7.9 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 24.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 30.8 | 0.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 67.9 | 87.5 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1111 | 105 | 12 | `pytest-9.0.2/testing/_py/test_local.py` |
| cleanup | 53 | 18 | 0 | `pytest-9.0.2/src/_pytest/capture.py` |
| guards | 7118 | 180 | 75 | `pytest-9.0.2/testing/_py/test_local.py` |
| danger | 1833 | 165 | 18 | `pytest-9.0.2/testing/python/raises_group.py` |
| concurrency | 389 | 72 | 5 | `pytest-9.0.2/src/_pytest/capture.py` |
| connectivity | 5830 | 247 | 62 | `pytest-9.0.2/testing/python/fixtures.py` |
| io | 1158 | 110 | 8 | `pytest-9.0.2/src/_pytest/_py/path.py` |
| crypto | 3 | 2 | 0 | `pytest-9.0.2/testing/_py/test_local.py` |
| ipc | 68 | 17 | 0 | `pytest-9.0.2/src/_pytest/pytester.py` |
| time | 16 | 6 | 0 | `pytest-9.0.2/testing/_py/test_local.py` |
| serialization | 5 | 4 | 0 | `pytest-9.0.2/src/_pytest/assertion/rewrite.py` |
| regex | 53 | 27 | 0 | `pytest-9.0.2/src/_pytest/pytester.py` |
| events | 92 | 11 | 0 | `pytest-9.0.2/testing/logging/test_fixture.py` |
| tests | 6080 | 227 | 54 | `pytest-9.0.2/testing/test_config.py` |
| docs | 3931 | 158 | 39 | `pytest-9.0.2/testing/python/fixtures.py` |
| debt | 452 | 86 | 4 | `pytest-9.0.2/src/_pytest/hookspec.py` |
| mutation | 23898 | 196 | 248 | `pytest-9.0.2/testing/_py/test_local.py` |
| dead_code | 3024 | 172 | 29 | `pytest-9.0.2/testing/_py/test_local.py` |
| credential | 0 | 0 | 0 | - |
| threat | 15 | 5 | 0 | `pytest-9.0.2/testing/test_assertrewrite.py` |
| ml_ai | 3 | 1 | 0 | `pytest-9.0.2/src/_pytest/python_api.py` |
| ui | 7 | 2 | 0 | `pytest-9.0.2/testing/code/test_excinfo.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.7917**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `pytest-9.0.2/src/_pytest/_py/path.py` (Hits: 96)
- `pytest-9.0.2/testing/test_capture.py` (Hits: 75)
- `pytest-9.0.2/src/_pytest/config/__init__.py` (Hits: 69)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **__init__.py** (`pytest-9.0.2/src/pytest/__init__.py`) — 132 inbound connections
2. **__init__.py** (`pytest-9.0.2/src/_pytest/config/__init__.py`) — 69 inbound connections
3. **python.py** (`pytest-9.0.2/src/_pytest/python.py`) — 66 inbound connections
4. **pytester.py** (`pytest-9.0.2/src/_pytest/pytester.py`) — 61 inbound connections
5. **monkeypatch.py** (`pytest-9.0.2/src/_pytest/monkeypatch.py`) — 46 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **__init__.py** (`pytest-9.0.2/src/_pytest/config/__init__.py`) — 46 outbound dependencies
2. **pytester.py** (`pytest-9.0.2/src/_pytest/pytester.py`) — 38 outbound dependencies
3. **python.py** (`pytest-9.0.2/src/_pytest/python.py`) — 36 outbound dependencies
4. **rewrite.py** (`pytest-9.0.2/src/_pytest/assertion/rewrite.py`) — 33 outbound dependencies
5. **test_assertrewrite.py** (`pytest-9.0.2/testing/test_assertrewrite.py`) — 33 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_check_exceptions` **(Stateful Encapsulated Methods)** (@ `pytest-9.0.2/src/_pytest/raises.py`) -> Impact: **97.1** | LOC: 142
- `parametrize` **(Many-Argument Workhorses)** (@ `pytest-9.0.2/src/_pytest/python.py`) -> Impact: **83.0** | LOC: 189
- `__init__` **(Defensive Guards)** (@ `pytest-9.0.2/src/_pytest/raises.py`) -> Impact: **72.5** | LOC: 51
- `_getini_toml` **(Many-Argument Workhorses)** (@ `pytest-9.0.2/src/_pytest/config/__init__.py`) -> Impact: **70.3** | LOC: 83
- `matches` **(Stateful Encapsulated Methods)** (@ `pytest-9.0.2/src/_pytest/raises.py`) -> Impact: **70.2** | LOC: 122
- `__init__` **(Many-Argument Workhorses)** (@ `pytest-9.0.2/src/_pytest/raises.py`) -> Impact: **68.2** | LOC: 62
- `assertrepr_compare` **(Many-Argument Workhorses)** (@ `pytest-9.0.2/src/_pytest/assertion/util.py`) -> Impact: **67.1** | LOC: 68
- `_getini_ini` **(Many-Argument Workhorses)** (@ `pytest-9.0.2/src/_pytest/config/__init__.py`) -> Impact: **66.5** | LOC: 60
- `make_numbered_dir` **(Many-Argument Workhorses)** (@ `pytest-9.0.2/src/_pytest/_py/path.py`) -> Impact: **57.0** | LOC: 160
- `_safe_repr` **(Many-Argument Workhorses)** (@ `pytest-9.0.2/src/_pytest/_io/pprint.py`) -> Impact: **56.7** | LOC: 57

*Function archetypes referenced above:*
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `pytest-9.0.2/src/_pytest` | 48 | 17294.98 | 44.52% | 18.61% |
| `pytest-9.0.2/testing` | 56 | 15921.06 | 10.87% | 0.0% |
| `pytest-9.0.2/testing/python` | 8 | 3862.84 | 8.99% | 0.0% |
| `pytest-9.0.2/src/_pytest/config` | 5 | 2288.06 | 30.1% | 1.67% |
| `pytest-9.0.2/src/_pytest/assertion` | 4 | 2012.56 | 51.99% | 10.84% |
| `pytest-9.0.2/src/_pytest/_code` | 3 | 1561.7 | 33.35% | 4.79% |
| `pytest-9.0.2/src/_pytest/_py` | 3 | 1555.04 | 37.06% | 4.29% |
| `pytest-9.0.2/testing/code` | 3 | 1539.58 | 25.9% | 0.0% |
| `pytest-9.0.2/testing/_py` | 1 | 1198.7 | 41.66% | 0.0% |
| `pytest-9.0.2/src/_pytest/_io` | 5 | 912.52 | 39.92% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `pytest-9.0.2/src/_pytest/hookspec.py` -> **99.9673%** Exposure
- `pytest-9.0.2/src/_pytest/threadexception.py` -> **99.3307%** Exposure
- `pytest-9.0.2/src/_pytest/setupplan.py` -> **97.0688%** Exposure
- `pytest-9.0.2/src/_pytest/setuponly.py` -> **93.6719%** Exposure
- `pytest-9.0.2/src/_pytest/pastebin.py` -> **90.0777%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `pytest-9.0.2/extra/get_issues.py` -> **100.0%** Exposure
- `pytest-9.0.2/scripts/generate-gh-release-notes.py` -> **100.0%** Exposure
- `pytest-9.0.2/scripts/prepare-release-pr.py` -> **100.0%** Exposure
- `pytest-9.0.2/scripts/update-plugin-list.py` -> **100.0%** Exposure
- `pytest-9.0.2/src/_pytest/_argcomplete.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `pytest-9.0.2/testing/_py/test_local.py` -> **173** Orphaned Functions | **0** Duplicates
- `pytest-9.0.2/testing/test_terminal.py` -> **154** Orphaned Functions | **0** Duplicates
- `pytest-9.0.2/testing/test_config.py` -> **143** Orphaned Functions | **4** Duplicates
- `pytest-9.0.2/testing/python/metafunc.py` -> **109** Orphaned Functions | **29** Duplicates
- `pytest-9.0.2/testing/test_assertion.py` -> **122** Orphaned Functions | **2** Duplicates

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
- **Unknown Dependencies:** `2031` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `pytest-9.0.2/src/_pytest/terminal.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.145)
- **Top Global Matches:** file_cluster_4: 8.145, file_cluster_5: 9.989, file_cluster_0: 10.166
- **Magnitude:** 1767.64 | **LOC:** 1764 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **17** in-repo importer(s); it depends on **29**; blast radius 8.618; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.9%), Complexity Load (formerly Cognitive Load) (67.3%)
- **Documentation Coverage:** 90.9574% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pytest_runtest_logreport` **(Many-Argument Workhorses)** (Impact: 52.2)
  * `short_test_summary` **(Generic / Templated Code)** (Impact: 37.9)
  * `report_collect` **(Stateful Encapsulated Methods)** (Impact: 31.2)
  * `summary_warnings` **(Stateful Encapsulated Methods)** (Impact: 30.9)
  * `_printcollecteditems` **(Stateful Encapsulated Methods)** (Impact: 29.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 246 instances
* *State Mutation (weighted view):* 791
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 347`, `structural_boundaries: 315`, `args: 105`, `func_start: 105`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 299`, `planned_debt: 2`, `fragile_debt: 2`
* *Architecture:* `io: 8`, `api: 78`, `import: 48`
* *Defense:* `safety: 42`, `doc: 19`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.618
  * `Choke Point (Betweenness):` 0.007552 | `Ripple Effect (Closeness):` 0.274196
  * `Imports (Out-Degree: 19):` __future__, _pytest, _pytest._code, _pytest._code.code, _pytest._io, _pytest._io.wcwidth, _pytest._version, _pytest.compat...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `pytest-9.0.2/src/_pytest/config/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.261)
- **Top Global Matches:** file_cluster_5: 7.261, file_cluster_12: 8.344, file_cluster_0: 10.621
- **Magnitude:** 1501.86 | **LOC:** 2198 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **69** in-repo importer(s); it depends on **46**; blast radius 23.756; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (65.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (49.3%)
- **Documentation Coverage:** 65.3179% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_getini_toml` **(Many-Argument Workhorses)** (Impact: 70.3)
  * `_getini_ini` **(Many-Argument Workhorses)** (Impact: 66.5)
  * `_decide_args` **(Many-Argument Workhorses)** (Impact: 39.0)
  * `parse` **(Stateful Encapsulated Methods)** (Impact: 33.4)
    * *Intent:* # Parse given cmdline arguments into this config object. assert self.args == [], ( "can only parse c...
  * `_set_initial_conftests` **(Stateful Encapsulated Methods)** (Impact: 24.6)
    * *Intent:* # # Internal API for local conftest plugin handling. #
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 176 instances
* *State Mutation (weighted view):* 596
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 276`, `structural_boundaries: 455`, `args: 97`, `func_start: 95`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 244`, `fragile_debt: 1`
* *Architecture:* `io: 69`, `api: 61`, `import: 85`
* *Defense:* `safety: 113`, `doc: 61`, `test: 22`, `immutability_locks: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 23.756
  * `Choke Point (Betweenness):` 0.018901 | `Ripple Effect (Closeness):` 0.336044
  * `Imports (Out-Degree: 25):` .compat, .exceptions, .findpaths, __future__, _pytest, _pytest._code, _pytest._code.code, _pytest._io...
  * `Imported By (In-Degree: 69):` (Excluded from Brief to save tokens)

### `pytest-9.0.2/src/_pytest/_py/path.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.121)
- **Top Global Matches:** file_cluster_12: 7.121, file_cluster_5: 8.332, file_cluster_7: 9.805
- **Magnitude:** 1478.68 | **LOC:** 1476 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **25**; blast radius 5.988; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (75.3%), Guard Balance (formerly Safety Score) (71.7%)
- **Documentation Coverage:** 42.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `make_numbered_dir` **(Many-Argument Workhorses)** (Impact: 57.0)
  * `pyimport` **(Many-Argument Workhorses)** (Impact: 40.4)
    * *Intent:* """Return path as an imported python module. If modname is None, look for the containing package and...
  * `sysfind` **(Many-Argument Workhorses)** (Impact: 40.3)
    * *Intent:* """Return a path object found by looking at the systems underlying PATH specification. If the checke...
  * `copy` **(Many-Argument Workhorses)** (Impact: 28.6)
    * *Intent:* """Copy path to target. If mode is True, will copy permission from path to target. If stat is True, ...
  * `_evaluate` **(Stateful Encapsulated Methods)** (Impact: 26.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 188 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 601
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 245`, `structural_boundaries: 369`, `args: 122`, `func_start: 119`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 32`, `high_risk_execution: 2`, `state_mutation: 225`, `fragile_debt: 4`
* *Architecture:* `io: 96`, `api: 112`, `import: 47`
* *Defense:* `safety: 100`, `doc: 71`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.988
  * `Choke Point (Betweenness):` 8.5e-05 | `Ripple Effect (Closeness):` 0.140653
  * `Imports (Out-Degree: 2):` .._code.source, .error, __future__, atexit, collections.abc, contextlib, fnmatch, grp...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pytest-9.0.2/src/_pytest/fixtures.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.093)
- **Top Global Matches:** file_cluster_5: 6.093, file_cluster_12: 8.658, file_cluster_7: 10.678
- **Magnitude:** 1417.64 | **LOC:** 2048 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **35** in-repo importer(s); it depends on **30**; blast radius 18.829; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.2%), Connectivity (formerly Api Exposure) (68.3%)
- **Documentation Coverage:** 68.9474% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `reorder_items_atscope` **(Many-Argument Workhorses)** (Impact: 47.9)
  * `_showfixtures_main` **(Many-Argument Workhorses)** (Impact: 28.7)
  * `_get_active_fixturedef` **(Many-Argument Workhorses)** (Impact: 26.3)
  * `getfixtureclosure` **(Many-Argument Workhorses)** (Impact: 25.6)
  * `parsefactories` **(Many-Argument Workhorses)** (Impact: 25.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 176 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 586
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 229`, `structural_boundaries: 399`, `args: 107`, `func_start: 105`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 55`, `state_mutation: 234`, `dead_code: 1`, `planned_debt: 5`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 8`, `api: 78`, `concurrency: 2`, `import: 78`
* *Defense:* `safety: 54`, `doc: 48`, `test: 30`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.829
  * `Choke Point (Betweenness):` 0.005862 | `Ripple Effect (Closeness):` 0.294039
  * `Imports (Out-Degree: 19):` __future__, _pytest, _pytest._code, _pytest._code.code, _pytest._io, _pytest.compat, _pytest.config, _pytest.config.argparsing...
  * `Imported By (In-Degree: 35):` (Excluded from Brief to save tokens)

### `pytest-9.0.2/src/_pytest/python.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.196)
- **Top Global Matches:** file_cluster_5: 8.196, file_cluster_12: 8.719, file_cluster_4: 9.248
- **Magnitude:** 1360.78 | **LOC:** 1773 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **66** in-repo importer(s); it depends on **36**; blast radius 18.936; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.8%), Complexity Load (formerly Cognitive Load) (53.4%)
- **Documentation Coverage:** 70.8333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parametrize` **(Many-Argument Workhorses)** (Impact: 83.0)
  * `make_unique_parameterset_ids` **(Compute Cores)** (Impact: 27.3)
    * *Intent:* """Make a unique identifier for each ParameterSet, that may be used to identify the parametrization ...
  * `collect` **(Defensive Guards)** (Impact: 26.5)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 25.7)
  * `_genfunctions` **(Many-Argument Workhorses)** (Impact: 24.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 167 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 534
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 272`, `structural_boundaries: 402`, `args: 85`, `func_start: 85`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 200`, `planned_debt: 5`, `fragile_debt: 4`
* *Architecture:* `io: 8`, `api: 62`, `concurrency: 3`, `import: 74`
* *Defense:* `safety: 51`, `doc: 44`, `test: 14`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.936
  * `Choke Point (Betweenness):` 0.008757 | `Ripple Effect (Closeness):` 0.314746
  * `Imports (Out-Degree: 19):` __future__, _pytest, _pytest._code, _pytest._code.code, _pytest._io.saferepr, _pytest.compat, _pytest.config, _pytest.config.argparsing...
  * `Imported By (In-Degree: 66):` (Excluded from Brief to save tokens)

### `pytest-9.0.2/src/_pytest/_code/code.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.899)
- **Top Global Matches:** file_cluster_5: 6.899, file_cluster_12: 8.743, file_cluster_0: 9.388
- **Magnitude:** 1294.36 | **LOC:** 1566 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **35** in-repo importer(s); it depends on **22**; blast radius 18.498; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (82.1%), Guard Balance (formerly Safety Score) (71.6%), Complexity Load (formerly Cognitive Load) (50.3%)
- **Documentation Coverage:** 66.4865% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_source` **(Many-Argument Workhorses)** (Impact: 41.6)
  * `_group_contains` **(Stateful Encapsulated Methods)** (Impact: 41.1)
  * `cut` **(Many-Argument Workhorses)** (Impact: 40.9)
  * `repr_traceback_entry` **(Many-Argument Workhorses)** (Impact: 38.5)
  * `repr_excinfo` **(Many-Argument Workhorses)** (Impact: 31.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 159 instances
* *State Mutation (weighted view):* 519
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 219`, `structural_boundaries: 366`, `args: 104`, `func_start: 103`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 26`, `high_risk_execution: 2`, `state_mutation: 201`, `dead_code: 1`, `fragile_debt: 5`
* *Architecture:* `io: 12`, `api: 94`, `import: 46`
* *Defense:* `safety: 55`, `doc: 50`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.498
  * `Choke Point (Betweenness):` 0.001836 | `Ripple Effect (Closeness):` 0.263809
  * `Imports (Out-Degree: 8):` __future__, _pytest, _pytest._code.source, _pytest._io, _pytest._io.saferepr, _pytest.compat, _pytest.deprecated, _pytest.pathlib...
  * `Imported By (In-Degree: 35):` (Excluded from Brief to save tokens)

### `pytest-9.0.2/src/_pytest/pytester.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.098)
- **Top Global Matches:** file_cluster_5: 6.098, file_cluster_12: 8.468, file_cluster_0: 9.539
- **Magnitude:** 1233.64 | **LOC:** 1792 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **61** in-repo importer(s); it depends on **38**; blast radius 18.94; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (86.2%), Guard Balance (formerly Safety Score) (71.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 60.5634% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_match_lines` **(Many-Argument Workhorses)** (Impact: 40.0)
  * `_makefile` **(Stateful Encapsulated Methods)** (Impact: 28.7)
  * `matchreport` **(Many-Argument Workhorses)** (Impact: 28.3)
  * `copy_example` **(Compute Cores)** (Impact: 26.5)
    * *Intent:* """Copy file from project's directory into the testdir. :param name: The name of the file to copy. :...
  * `inline_run` **(Many-Argument Workhorses)** (Impact: 24.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 134 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 497
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 171`, `structural_boundaries: 369`, `args: 120`, `func_start: 117`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 31`, `high_risk_execution: 4`, `state_mutation: 229`, `fragile_debt: 1`
* *Architecture:* `io: 48`, `api: 106`, `import: 65`
* *Defense:* `safety: 42`, `doc: 73`, `test: 10`, `immutability_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.94
  * `Choke Point (Betweenness):` 0.012659 | `Ripple Effect (Closeness):` 0.308234
  * `Imports (Out-Degree: 21):` __future__, _pytest, _pytest._code, _pytest.capture, _pytest.compat, _pytest.config, _pytest.config.argparsing, _pytest.deprecated...
  * `Imported By (In-Degree: 61):` (Excluded from Brief to save tokens)

### `pytest-9.0.2/testing/_py/test_local.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.472)
- **Top Global Matches:** file_cluster_12: 7.472, file_cluster_15: 8.585, file_cluster_10: 9.444
- **Magnitude:** 1198.7 | **LOC:** 1580 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **21**; blast radius 1.307; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (41.7%), Guard Balance (formerly Safety Score) (32.9%), Concurrency Surface (formerly Concurrency) (17.3%)
- **Documentation Coverage:** 99.4764% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_visit_breadthfirst` **(Defensive Guards)** (Impact: 10.9)
  * `test_make_numbered_dir` **(Defensive Guards)** (Impact: 9.4)
  * `test_chmod_rec_int` **(Type Conversions)** (Impact: 7.7)
    * *Intent:* # XXX fragile test def recfilter(x): return x.check(dotfile=0, link=0) oldmodes = {} for x in path1....
  * `test_visit_sort` **(Defensive Guards)** (Impact: 7.4)
  * `test_move_file` **(Defensive Guards)** (Impact: 5.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 63 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 500
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 646`, `args: 203`, `func_start: 191`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 1`, `state_mutation: 374`, `dead_code: 3`, `planned_debt: 3`, `fragile_debt: 3`, `unreferenced_by_name: 173`
* *Architecture:* `io: 31`, `api: 200`, `concurrency: 2`, `import: 25`
* *Defense:* `safety: 388`, `doc: 3`, `test: 221`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.307
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` .b, __future__, contextlib, grp, hashlib, multiprocessing, os, pickle...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pytest-9.0.2/testing/test_config.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.773)
- **Top Global Matches:** file_cluster_0: 8.773, file_cluster_12: 8.886, file_cluster_5: 9.345
- **Magnitude:** 1190.88 | **LOC:** 3053 | **CtrlFlow:** 4.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 1.307; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (40.3%), Connectivity (formerly Api Exposure) (13.2%), Complexity Load (formerly Cognitive Load) (9.8%)
- **Documentation Coverage:** 80.8696% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_type_errors` **(Many-Argument Workhorses)** (Impact: 32.2)
    * *Intent:* """Test all possible TypeError cases in getini."""
  * `test_disable_plugin_autoload` **(Many-Argument Workhorses)** (Impact: 30.7)
  * `test_pytest_plugins_in_non_top_level_conftest_unsupported_pyargs` **(Defensive Guards)** (Impact: 15.2)
  * `test_missing_required_plugins` **(Many-Argument Workhorses)** (Impact: 13.2)
  * `test_plugin_preparse_prevents_setuptools_loading` **(Defensive Guards)** (Impact: 11.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 380
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 599`, `args: 179`, `func_start: 167`, `class_start: 33`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 290`, `duplicate_logic: 4`, `unreferenced_by_name: 143`
* *Architecture:* `io: 12`, `api: 198`, `import: 33`
* *Defense:* `safety: 246`, `doc: 182`, `test: 321`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.307
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` __future__, _pytest._code, _pytest.config, _pytest.config.argparsing, _pytest.config.exceptions, _pytest.config.findpaths, _pytest.monkeypatch, _pytest.pathlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pytest-9.0.2/testing/python/fixtures.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.646)
- **Top Global Matches:** file_cluster_0: 7.646, file_cluster_15: 9.608, file_cluster_12: 10.353
- **Magnitude:** 1189.32 | **LOC:** 5368 | **CtrlFlow:** 1.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 1.307; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (71.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (42.2%), Complexity Load (formerly Cognitive Load) (6.8%)
- **Documentation Coverage:** 78.9976% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_deterministic_fixture_collection` **(Many-Argument Workhorses)** (Impact: 12.2)
  * `test_pytest_fixture_setup_and_post_finalizer_hook` **(Compute Cores)** (Impact: 9.1)
  * `test_non_relative_path` **(Many-Argument Workhorses)** (Impact: 8.2)
  * `test_request_subrequest_addfinalizer_exceptions` **(Many-Argument Workhorses)** (Impact: 5.7)
  * `test_funcarg_lookup_error` **(Compute Cores)** (Impact: 5.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 295
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 423`, `args: 228`, `func_start: 212`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 277`, `planned_debt: 1`, `fragile_debt: 4`, `duplicate_logic: 8`
* *Architecture:* `io: 4`, `api: 218`, `import: 20`
* *Defense:* `safety: 134`, `doc: 324`, `test: 266`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.307
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` __future__, _pytest.compat, _pytest.config, _pytest.fixtures, _pytest.monkeypatch, _pytest.pytester, _pytest.python, functools...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pytest-9.0.2/testing/test_terminal.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.47)
- **Top Global Matches:** file_cluster_0: 7.47, file_cluster_12: 9.196, file_cluster_15: 9.335
- **Magnitude:** 1139.8 | **LOC:** 3551 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **19**; blast radius 1.692; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (44.6%), Connectivity (formerly Api Exposure) (12.8%), Complexity Load (formerly Cognitive Load) (7.2%)
- **Documentation Coverage:** 92.7978% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_tb_option` **(Defensive Guards)** (Impact: 13.3)
  * `test_execute_skipped_positive_2` **(Compute Cores)** (Impact: 9.6)
    * *Intent:* # expected: one test case per line (with file name), word describing result, full reason p = TestFin...
  * `test_pass_skip_fail` **(Defensive Guards)** (Impact: 9.4)
  * `test_line_with_reprcrash` **(C Struct Operations)** (Impact: 8.2)
  * `test_fail_extra_reporting` **(Many-Argument Workhorses)** (Impact: 7.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 368
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 511`, `args: 212`, `func_start: 177`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 1`, `state_mutation: 338`, `unreferenced_by_name: 154`
* *Architecture:* `io: 16`, `api: 196`, `import: 34`
* *Defense:* `safety: 186`, `doc: 159`, `test: 265`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.692
  * `Choke Point (Betweenness):` 9.6e-05 | `Ripple Effect (Closeness):` 0.181683
  * `Imports (Out-Degree: 10):` Errlkjqweqwe, __future__, _pytest._io.wcwidth, _pytest.config, _pytest.monkeypatch, _pytest.pytester, _pytest.reports, _pytest.terminal...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pytest-9.0.2/src/_pytest/raises.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.427)
- **Top Global Matches:** file_cluster_4: 9.427, file_cluster_5: 9.761, file_cluster_12: 11.175
- **Magnitude:** 1081.5 | **LOC:** 1518 | **CtrlFlow:** 30.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **16**; blast radius 4.757; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.3%), Guard Balance (formerly Safety Score) (64.2%)
- **Documentation Coverage:** 92.5926% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_check_exceptions` **(Stateful Encapsulated Methods)** (Impact: 97.1)
  * `__init__` **(Defensive Guards)** (Impact: 72.5)
  * `matches` **(Stateful Encapsulated Methods)** (Impact: 70.2)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 68.2)
  * `_parse_exc` **(Defensive Guards)** (Impact: 31.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 106 instances
* *State Mutation (weighted view):* 328
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 281`, `structural_boundaries: 292`, `args: 60`, `func_start: 59`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 116`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 27`, `import: 32`
* *Defense:* `safety: 57`, `doc: 16`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.757
  * `Choke Point (Betweenness):` 0.002446 | `Ripple Effect (Closeness):` 0.245571
  * `Imports (Out-Degree: 5):` __future__, _pytest._code, _pytest._code.code, _pytest.assertion.util, _pytest.outcomes, _pytest.warning_types, abc, collections.abc...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `pytest-9.0.2/testing/code/test_excinfo.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.946)
- **Top Global Matches:** file_cluster_12: 7.946, file_cluster_0: 8.339, file_cluster_5: 9.091
- **Magnitude:** 1052.72 | **LOC:** 2008 | **CtrlFlow:** 6.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 1.307; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (35.2%), Complexity Load (formerly Cognitive Load) (26.0%), Connectivity (formerly Api Exposure) (12.5%)
- **Documentation Coverage:** 90.6615% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_exceptiongroup_common` **(Many-Argument Workhorses)** (Impact: 21.4)
  * `test_exc_chain_repr` **(Defensive Guards)** (Impact: 16.6)
  * `test_exc_chain_repr_cycle` **(Many-Argument Workhorses)** (Impact: 13.1)
  * `test_traceback_repr_style` **(Defensive Guards)** (Impact: 12.3)
  * `test_exc_repr_chain_suppression` **(Defensive Guards)** (Impact: 10.6)
    * *Intent:* """Check that exc repr does not show chained exceptions in Python 3. - When the exception is raised ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Amplified Cascading Flux:* 75 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 474
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 631`, `args: 159`, `func_start: 137`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 5`, `state_mutation: 324`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 4`, `duplicate_logic: 6`, `unreferenced_by_name: 98`
* *Architecture:* `io: 16`, `api: 120`, `import: 30`
* *Defense:* `safety: 369`, `doc: 48`, `test: 192`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.307
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` __future__, _pytest._code, _pytest._code.code, _pytest._io, _pytest.monkeypatch, _pytest.pathlib, _pytest.pytester, exceptiongroup...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pytest-9.0.2/testing/test_assertrewrite.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.277)
- **Top Global Matches:** file_cluster_0: 8.277, file_cluster_12: 9.938, file_cluster_5: 10.042
- **Magnitude:** 1035.28 | **LOC:** 2407 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **33**; blast radius 1.307; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (33.2%), Connectivity (formerly Api Exposure) (13.4%), Complexity Load (formerly Cognitive Load) (13.3%)
- **Documentation Coverage:** 92.3684% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_positions_are_preserved` **(I/O & Config Routines)** (Impact: 26.9)
    * *Intent:* """Ensure AST positions are preserved during rewriting (#12818)."""
  * `test_boolop` **(Defensive Guards)** (Impact: 26.5)
  * `getmsg` **(Defensive Guards)** (Impact: 13.2)
  * `preserved` **(Defensive Guards)** (Impact: 10.6)
  * `test_place_initial_imports` **(Defensive Guards)** (Impact: 10.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 7 instances
* *Amplified Cascading Flux:* 43 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 309
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 672`, `args: 216`, `func_start: 187`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 7`, `state_mutation: 223`, `planned_debt: 1`, `fragile_debt: 8`, `duplicate_logic: 2`, `unreferenced_by_name: 113`
* *Architecture:* `io: 20`, `api: 187`, `import: 50`
* *Defense:* `safety: 333`, `doc: 127`, `test: 159`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.307
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` __future__, _pytest._code, _pytest._io.saferepr, _pytest.assertion, _pytest.assertion.rewrite, _pytest.config, _pytest.pathlib, _pytest.pytester...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pytest-9.0.2/src/_pytest/assertion/rewrite.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.848)
- **Top Global Matches:** file_cluster_4: 9.848, file_cluster_5: 9.996, file_cluster_12: 11.397
- **Magnitude:** 1019.06 | **LOC:** 1203 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **33**; blast radius 3.418; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.8%), Complexity Load (formerly Cognitive Load) (60.7%)
- **Documentation Coverage:** 54.5455% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run` **(Defensive Guards)** (Impact: 48.9)
    * *Intent:* """Find all assert statements in *mod* and rewrite them."""
  * `visit_Assert` **(Many-Argument Workhorses)** (Impact: 35.4)
    * *Intent:* """Return the AST statements to replace the ast.Assert instance. This rewrites the test of an assert...
  * `find_spec` **(Many-Argument Workhorses)** (Impact: 33.8)
  * `_get_assertion_exprs` **(Stateful Encapsulated Methods)** (Impact: 30.9)
    * *Intent:* """Return a mapping from {lineno: "assertion test expression"}."""
  * `visit_Compare` **(Many-Argument Workhorses)** (Impact: 30.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 143 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 533
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 175`, `structural_boundaries: 239`, `args: 52`, `func_start: 52`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 26`, `high_risk_execution: 2`, `state_mutation: 247`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `io: 28`, `api: 35`, `import: 44`
* *Defense:* `safety: 54`, `doc: 28`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.418
  * `Choke Point (Betweenness):` 0.001275 | `Ripple Effect (Closeness):` 0.20885
  * `Imports (Out-Degree: 10):` __future__, _pytest._io.saferepr, _pytest._version, _pytest.assertion, _pytest.assertion.util, _pytest.config, _pytest.fixtures, _pytest.main...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `pytest-9.0.2/testing/test_assertion.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.53)
- **Top Global Matches:** file_cluster_0: 8.53, file_cluster_12: 9.041, file_cluster_5: 9.599
- **Magnitude:** 976.04 | **LOC:** 2201 | **CtrlFlow:** 3.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 1.307; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (44.3%), Concurrency Surface (formerly Concurrency) (15.4%), Complexity Load (formerly Cognitive Load) (13.4%)
- **Documentation Coverage:** 91.4062% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_installed_plugin_rewrite` **(Many-Argument Workhorses)** (Impact: 39.6)
  * `test_truncation_with_ini` **(Many-Argument Workhorses)** (Impact: 15.5)
  * `test_conftest_assertion_rewrite` **(Many-Argument Workhorses)** (Impact: 14.9)
  * `test_comparisons_handle_colors` **(Many-Argument Workhorses)** (Impact: 12.9)
  * `test_pytest_plugins_rewrite` **(Defensive Guards)** (Impact: 9.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 55 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 376
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 442`, `args: 148`, `func_start: 133`, `class_start: 30`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 266`, `fragile_debt: 6`, `duplicate_logic: 2`, `unreferenced_by_name: 122`
* *Architecture:* `io: 3`, `api: 149`, `concurrency: 1`, `import: 15`
* *Defense:* `safety: 216`, `doc: 74`, `test: 158`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.307
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` __future__, _pytest, _pytest.assertion, _pytest.config, _pytest.monkeypatch, _pytest.pytester, attr, collections.abc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pytest-9.0.2/testing/test_junitxml.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.592)
- **Top Global Matches:** file_cluster_0: 7.592, file_cluster_5: 8.252, file_cluster_12: 8.608
- **Magnitude:** 880.76 | **LOC:** 1834 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 1.307; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (18.3%), Connectivity (formerly Api Exposure) (12.1%)
- **Documentation Coverage:** 93.7824% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_failure_function` **(Many-Argument Workhorses)** (Impact: 15.5)
  * `test_xfail_captures_output_once` **(Many-Argument Workhorses)** (Impact: 12.5)
  * `test_logging_passing_tests_disabled_logs_output_for_failing_test_issue5430` **(Defensive Guards)** (Impact: 10.9)
  * `assert_attr` **(Generic / Templated Code)** (Impact: 9.2)
  * `test_junit_duration_report` **(Many-Argument Workhorses)** (Impact: 8.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 67 instances
* *State Mutation (weighted view):* 368
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 316`, `args: 103`, `func_start: 99`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 234`, `fragile_debt: 3`, `unreferenced_by_name: 77`
* *Architecture:* `io: 7`, `api: 102`, `import: 25`
* *Defense:* `safety: 125`, `doc: 75`, `test: 121`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.307
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` __future__, _pytest, _pytest.config, _pytest.junitxml, _pytest.monkeypatch, _pytest.pytester, _pytest.reports, _pytest.stash...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pytest-9.0.2/src/_pytest/main.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.576)
- **Top Global Matches:** file_cluster_4: 8.576, file_cluster_6: 11.179, file_cluster_5: 11.789
- **Magnitude:** 838.94 | **LOC:** 1204 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **21** in-repo importer(s); it depends on **26**; blast radius 10.962; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.2%), Connectivity (formerly Api Exposure) (58.9%)
- **Documentation Coverage:** 92.4051% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `collect` **(Compute Cores)** (Impact: 51.4)
    * *Intent:* # This is a cache for the root directories of the initial paths. # We can't use collection_cache for...
  * `resolve_collection_argument` **(Many-Argument Workhorses)** (Impact: 43.0)
  * `perform_collect` **(Stateful Encapsulated Methods)** (Impact: 38.8)
  * `pytest_addoption` **(I/O & Config Routines)** (Impact: 30.8)
  * `pytest_ignore_collect` **(Compute Cores)** (Impact: 29.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 106 instances
* *State Mutation (weighted view):* 355
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 179`, `structural_boundaries: 216`, `args: 43`, `func_start: 41`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 143`, `planned_debt: 1`
* *Architecture:* `io: 16`, `api: 41`, `import: 46`
* *Defense:* `safety: 30`, `doc: 19`, `test: 2`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.962
  * `Choke Point (Betweenness):` 0.003239 | `Ripple Effect (Closeness):` 0.281094
  * `Imports (Out-Degree: 17):` __future__, _pytest, _pytest._code, _pytest.config, _pytest.config.argparsing, _pytest.config.compat, _pytest.fixtures, _pytest.outcomes...
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `pytest-9.0.2/testing/python/metafunc.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.816)
- **Top Global Matches:** file_cluster_5: 6.816, file_cluster_12: 8.519, file_cluster_0: 10.073
- **Magnitude:** 804.76 | **LOC:** 2275 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 1.307; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (46.1%), Connectivity (formerly Api Exposure) (13.2%), Complexity Load (formerly Cognitive Load) (9.1%)
- **Documentation Coverage:** 80.7947% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_parametrize_marked_value` **(Many-Argument Workhorses)** (Impact: 7.0)
  * `test_xfail_passing_is_xpass` **(Many-Argument Workhorses)** (Impact: 6.9)
  * `test_parametrize_indirect_wrong_type` **(Generic / Templated Code)** (Impact: 6.2)
  * `test_parametrize_request_name` **(Generic / Templated Code)** (Impact: 5.8)
    * *Intent:* """Show proper error when 'request' is used as a parameter name in parametrize (#6183)"""
  * `test_parametrize_error_iterator` **(Generic / Templated Code)** (Impact: 5.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 214
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 380`, `args: 157`, `func_start: 151`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 156`, `fragile_debt: 6`, `duplicate_logic: 29`, `unreferenced_by_name: 109`
* *Architecture:* `api: 162`, `import: 24`
* *Defense:* `safety: 107`, `doc: 110`, `test: 187`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.307
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` __future__, _pytest, _pytest.compat, _pytest.outcomes, _pytest.pytester, _pytest.python, _pytest.scope, collections.abc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pytest-9.0.2/testing/test_collection.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.119)
- **Top Global Matches:** file_cluster_0: 7.119, file_cluster_15: 8.393, file_cluster_13: 9.369
- **Magnitude:** 800.36 | **LOC:** 2799 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 1.307; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (41.6%), Connectivity (formerly Api Exposure) (12.1%), Complexity Load (formerly Cognitive Load) (6.3%)
- **Documentation Coverage:** 52.5346% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_testpaths_ini` **(Defensive Guards)** (Impact: 13.8)
  * `test_strict_parametrization_ids` **(Many-Argument Workhorses)** (Impact: 8.7)
  * `test_check_collect_hashes` **(Defensive Guards)** (Impact: 7.8)
  * `get_reported_items` **(Generic / Templated Code)** (Impact: 7.4)
    * *Intent:* """Return pytest.Item instances reported by the pytest_collectreport hook"""
  * `test_collect_short_file_windows` **(Defensive Guards)** (Impact: 6.8)
    * *Intent:* """Reproducer for #11895: short paths not collected on Windows."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 285
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 431`, `args: 153`, `func_start: 109`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 239`, `fragile_debt: 4`, `unreferenced_by_name: 102`
* *Architecture:* `io: 7`, `api: 122`, `import: 23`
* *Defense:* `safety: 188`, `doc: 149`, `test: 194`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.307
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` __future__, _pytest.compat, _pytest.config, _pytest.fixtures, _pytest.main, _pytest.monkeypatch, _pytest.nodes, _pytest.pathlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pytest-9.0.2/src/_pytest/assertion/util.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 13.397)
- **Top Global Matches:** file_cluster_6: 13.397, file_cluster_4: 14.673, file_cluster_5: 15.969
- **Magnitude:** 727.36 | **LOC:** 616 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **14**; blast radius 2.406; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.1%)
- **Documentation Coverage:** 88.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assertrepr_compare` **(Many-Argument Workhorses)** (Impact: 67.1)
  * `_compare_eq_any` **(Stateful Encapsulated Methods)** (Impact: 50.9)
  * `_compare_eq_cls` **(Many-Argument Workhorses)** (Impact: 49.6)
  * `_compare_eq_dict` **(Many-Argument Workhorses)** (Impact: 42.4)
  * `_compare_eq_sequence` **(Many-Argument Workhorses)** (Impact: 29.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 107 instances
* *State Mutation (weighted view):* 335
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 117`, `args: 28`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 121`, `fragile_debt: 1`
* *Architecture:* `api: 13`, `import: 23`
* *Defense:* `safety: 22`, `doc: 9`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.406
  * `Choke Point (Betweenness):` 0.002246 | `Ripple Effect (Closeness):` 0.180217
  * `Imports (Out-Degree: 8):` __future__, _pytest, _pytest._code, _pytest._io.pprint, _pytest._io.saferepr, _pytest.compat, _pytest.config, _pytest.python_api...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pytest-9.0.2/src/_pytest/pathlib.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.228)
- **Top Global Matches:** file_cluster_5: 8.228, file_cluster_12: 9.309, file_cluster_4: 10.433
- **Magnitude:** 713.7 | **LOC:** 1064 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **23** in-repo importer(s); it depends on **26**; blast radius 11.634; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (85.5%), Guard Balance (formerly Safety Score) (68.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 42.2222% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `import_path` **(Many-Argument Workhorses)** (Impact: 44.2)
  * `_import_module_using_spec` **(Many-Argument Workhorses)** (Impact: 44.1)
  * `on_rm_rf_error` **(Many-Argument Workhorses)** (Impact: 25.2)
  * `resolve_pkg_root_and_module_name` **(Compute Cores)** (Impact: 21.2)
  * `fnmatch_ex` **(Compute Cores)** (Impact: 15.6)
    * *Intent:* """A port of FNMatcher from py.path.common which works with PurePath() instances. The difference bet...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 93 instances
* *State Mutation (weighted view):* 302
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 212`, `args: 45`, `func_start: 45`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 116`, `planned_debt: 1`
* *Architecture:* `io: 64`, `api: 43`, `import: 41`
* *Defense:* `safety: 54`, `doc: 39`, `test: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.634
  * `Choke Point (Betweenness):` 0.000235 | `Ripple Effect (Closeness):` 0.257476
  * `Imports (Out-Degree: 3):` __future__, _pytest.compat, _pytest.outcomes, _pytest.warning_types, atexit, collections.abc, contextlib, enum...
  * `Imported By (In-Degree: 23):` (Excluded from Brief to save tokens)

### `pytest-9.0.2/src/_pytest/capture.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.639)
- **Top Global Matches:** file_cluster_5: 6.639, file_cluster_0: 9.176, file_cluster_12: 9.307
- **Magnitude:** 680.96 | **LOC:** 1145 | **CtrlFlow:** 12.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **20**; blast radius 7.552; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (70.4%), Guard Balance (formerly Safety Score) (60.6%), Debt Markers (formerly Tech Debt) (56.5%)
- **Documentation Coverage:** 86.0465% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_windowsconsoleio_workaround` **(Stateful Encapsulated Methods)** (Impact: 16.8)
    * *Intent:* """Workaround for Windows Unicode console handling. Python 3.6 implemented Unicode console handling ...
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 14.1)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 12.4)
  * `global_and_fixture_disabled` **(Defensive Guards)** (Impact: 10.6)
    * *Intent:* # Helper context managers """Context manager to temporarily disable global and current fixture captu...
  * `pytest_make_collect_report` **(Defensive Guards)** (Impact: 9.5)
    * *Intent:* # Hooks
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 53 instances
* *State Mutation (weighted view):* 194
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 284`, `args: 117`, `func_start: 117`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 88`, `planned_debt: 1`, `fragile_debt: 2`, `duplicate_logic: 4`
* *Architecture:* `io: 34`, `api: 110`, `import: 37`
* *Defense:* `safety: 37`, `doc: 30`, `test: 9`, `immutability_locks: 2`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.552
  * `Choke Point (Betweenness):` 0.000201 | `Ripple Effect (Closeness):` 0.275039
  * `Imports (Out-Degree: 6):` __future__, _pytest.config, _pytest.config.argparsing, _pytest.deprecated, _pytest.fixtures, _pytest.nodes, _pytest.reports, abc...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `pytest-9.0.2/testing/test_capture.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.359)
- **Top Global Matches:** file_cluster_0: 7.359, file_cluster_12: 9.43, file_cluster_15: 9.519
- **Magnitude:** 638.22 | **LOC:** 1736 | **CtrlFlow:** 4.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 1.307; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (37.7%), Connectivity (formerly Api Exposure) (12.7%), Complexity Load (formerly Cognitive Load) (9.6%)
- **Documentation Coverage:** 90.1478% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_disabled_capture_fixture` **(Many-Argument Workhorses)** (Impact: 14.7)
  * `StdCaptureFD` **(Compute Cores)** (Impact: 14.4)
    * *Intent:* # note: py.io capture tests where copied from # pylib 1.4.20.dev2 (rev 13d9af95547e)
  * `StdCapture` **(Compute Cores)** (Impact: 14.4)
  * `TeeStdCapture` **(Compute Cores)** (Impact: 14.4)
  * `test_capturing_basic_api` **(Defensive Guards)** (Impact: 8.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 190
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 352`, `args: 105`, `func_start: 101`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 156`, `planned_debt: 1`, `fragile_debt: 4`, `unreferenced_by_name: 85`
* *Architecture:* `io: 75`, `api: 113`, `import: 25`
* *Defense:* `safety: 150`, `doc: 69`, `test: 143`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.307
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` __future__, _pytest, _pytest.capture, _pytest.config, _pytest.monkeypatch, _pytest.pytester, collections.abc, contextlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pytest-9.0.2/testing/acceptance_test.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.923)
- **Top Global Matches:** file_cluster_0: 6.923, file_cluster_15: 9.529, file_cluster_12: 9.73
- **Magnitude:** 614.38 | **LOC:** 1654 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **21**; blast radius 1.307; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (42.1%), Concurrency Surface (formerly Concurrency) (37.8%), Complexity Load (formerly Cognitive Load) (12.7%)
- **Documentation Coverage:** 85.8586% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_early_load_setuptools_name` **(Many-Argument Workhorses)** (Impact: 13.4)
  * `check_tests_in_output` **(Defensive Guards)** (Impact: 10.6)
  * `test_cmdline_python_legacy_namespace_package` **(Many-Argument Workhorses)** (Impact: 10.1)
  * `test_cmdline_python_package_symlink` **(Many-Argument Workhorses)** (Impact: 6.9)
  * `test_docstring_on_hookspec` **(Defensive Guards)** (Impact: 6.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 16 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 18
* *State Mutation (weighted view):* 191
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 286`, `args: 117`, `func_start: 96`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 2`, `state_mutation: 159`, `fragile_debt: 2`, `unreferenced_by_name: 93`
* *Architecture:* `io: 14`, `api: 103`, `concurrency: 8`, `import: 19`
* *Defense:* `safety: 92`, `doc: 83`, `test: 151`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.307
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` .logging, .pytest_plugins, __future__, _pytest, _pytest.config, _pytest.pathlib, _pytest.pytester, collections.abc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `pytest-9.0.2/testing/test_monkeypatch.py` (PYTHON) | Magnitude: 190.98 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 297, structural_boundaries: 170, safety: 69, core_var_decl: 57
- `pytest-9.0.2/testing/example_scripts/dataclasses/test_compare_dataclasses.py` (PYTHON) | Magnitude: 5.72 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 7, core_var_decl: 4, design_snake_case: 4
- `pytest-9.0.2/testing/example_scripts/dataclasses/test_compare_dataclasses_field_comparison_off.py` (PYTHON) | Magnitude: 5.72 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 7, core_var_decl: 4, design_snake_case: 4
- `pytest-9.0.2/testing/example_scripts/dataclasses/test_compare_dataclasses_verbose.py` (PYTHON) | Magnitude: 5.72 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 7, core_var_decl: 4, design_snake_case: 4
- `pytest-9.0.2/testing/test_config.py` (PYTHON) | Magnitude: 1190.88 | Delta: **0.113** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 1903, structural_boundaries: 599, core_var_decl: 444, design_snake_case: 435

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `pytest-9.0.2/testing/example_scripts/unittest/test_unittest_plain_async.py` (PYTHON) | Magnitude: 4.6 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, test: 4, api: 2, import: 2
- `pytest-9.0.2/testing/example_scripts/fixtures/fill_fixtures/test_extend_fixture_conftest_conftest/pkg/test_spam.py` (PYTHON) | Magnitude: 0.0 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 4, args: 1, func_start: 1, safety: 1
- `pytest-9.0.2/testing/freeze/tests/test_trivial.py` (PYTHON) | Magnitude: 4.3 | Delta: **0.068** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 6, args: 2, func_start: 2, safety: 2
- `pytest-9.0.2/testing/example_scripts/doctest/main_py/__main__.py` (PYTHON) | Magnitude: 2.16 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 4, args: 1, func_start: 1, safety: 1
- `pytest-9.0.2/doc/en/example/fixtures/test_fixtures_request_different_scope.py` (PYTHON) | Magnitude: 0.02 | Delta: **0.091** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 14, indent_spaces: 12, test: 11, api: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `pytest-9.0.2/testing/test_main.py` (PYTHON) | Magnitude: 123.66 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 251, core_var_decl: 89, design_snake_case: 89, structural_boundaries: 68

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `pytest-9.0.2/doc/en/example/fixtures/test_fixtures_order_scope.py` (PYTHON) | Magnitude: 0.02 | Delta: **0.073** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 16, test: 14, api: 8, indent_spaces: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `pytest-9.0.2/testing/example_scripts/marks/marks_considered_keywords/test_marks_as_keywords.py` (PYTHON) | Magnitude: 2.2 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 5, test: 3, import: 2, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `pytest-9.0.2/src/pytest/__init__.py` (PYTHON) | Magnitude: 21.56 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 178, import: 88, indent_spaces: 87, state_mutation: 2
- `pytest-9.0.2/testing/test_error_diffs.py` (PYTHON) | Magnitude: 16.74 | Delta: **0.073** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 41, doc: 25, core_var_decl: 16, test: 15
- `pytest-9.0.2/testing/test_stash.py` (PYTHON) | Magnitude: 19.14 | Delta: **0.147** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 47, structural_boundaries: 38, safety: 22, state_mutation: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `pytest-9.0.2/src/_pytest/assertion/rewrite.py` (PYTHON) | Magnitude: 1019.06 | Delta: **0.148** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 748, state_mutation: 247, structural_boundaries: 239, core_var_decl: 203

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `pytest-9.0.2/scripts/generate-gh-release-notes.py` (PYTHON) | Magnitude: 48.36 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 18, core_var_decl: 13, design_snake_case: 13
- `pytest-9.0.2/testing/test_runner.py` (PYTHON) | Magnitude: 443.94 | Delta: **0.111** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 605, structural_boundaries: 346, safety: 193, core_var_decl: 134

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `pytest-9.0.2/doc/en/example/xfail_demo.py` (PYTHON) | Magnitude: 18.18 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 15, test: 11, indent_spaces: 8, args: 7

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `pytest-9.0.2/src/_pytest/config/__init__.py` -> **Severity: 1.89** (Bridge: 0.0189 * Flux: 100.0%)
- `pytest-9.0.2/src/_pytest/pytester.py` -> **Severity: 1.266** (Bridge: 0.0127 * Flux: 100.0%)
- `pytest-9.0.2/src/_pytest/python.py` -> **Severity: 0.876** (Bridge: 0.0088 * Flux: 100.0%)
- `pytest-9.0.2/src/_pytest/terminal.py` -> **Severity: 0.755** (Bridge: 0.0076 * Flux: 100.0%)
- `pytest-9.0.2/src/pytest/__init__.py` -> **Severity: 0.678** (Bridge: 0.0545 * Flux: 12.4492%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `pytest-9.0.2/src/_pytest/stash.py` -> **Severity: 22.131** (Embedded: 0.2766 * Error Risk: 80.0%)
- `pytest-9.0.2/src/_pytest/pytester.py` -> **Severity: 22.09** (Embedded: 0.3082 * Error Risk: 71.6666%)
- `pytest-9.0.2/src/_pytest/config/__init__.py` -> **Severity: 21.87** (Embedded: 0.336 * Error Risk: 65.0819%)
- `pytest-9.0.2/src/_pytest/config/argparsing.py` -> **Severity: 21.681** (Embedded: 0.2928 * Error Risk: 74.0575%)
- `pytest-9.0.2/src/_pytest/python.py` -> **Severity: 21.656** (Embedded: 0.3147 * Error Risk: 68.806%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `pytest-9.0.2/src/_pytest/outcomes.py` -> **Severity: 3125.5** (Blast Radius: 31.255 * Doc Risk: 100.0%)
- `pytest-9.0.2/src/_pytest/deprecated.py` -> **Severity: 2014.6** (Blast Radius: 20.146 * Doc Risk: 100.0%)
- `pytest-9.0.2/src/_pytest/warning_types.py` -> **Severity: 1782.57** (Blast Radius: 62.39 * Doc Risk: 28.5714%)
- `pytest-9.0.2/src/_pytest/_io/terminalwriter.py` -> **Severity: 1753.966** (Blast Radius: 20.346 * Doc Risk: 86.2069%)
- `pytest-9.0.2/src/_pytest/config/__init__.py` -> **Severity: 1551.692** (Blast Radius: 23.756 * Doc Risk: 65.3179%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 114 literal sites + 6 sites through wrappers = 120
- **`panics_and_aborts`:** 661 literal sites + 64 sites through wrappers = 725

- `fail` (function, panics_and_aborts, primitive): 44 call sites in 14 files -- `pytest-9.0.2/testing/code/test_excinfo.py`
- `add_skip` (function, panics_and_aborts, primitive): 5 call sites in 1 files -- `pytest-9.0.2/src/_pytest/unittest.py`
- `log` (function, debug_prints, primitive): 3 call sites in 1 files -- `pytest-9.0.2/testing/code/test_excinfo.py`
- `_parse_expression` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `pytest-9.0.2/src/_pytest/mark/__init__.py`
- `annotated_getattr` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `pytest-9.0.2/src/_pytest/monkeypatch.py`
- `fix` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `pytest-9.0.2/testing/python/fixtures.py`
- `handle_timeout` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `pytest-9.0.2/src/_pytest/pytester.py`
- `xyz` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `pytest-9.0.2/testing/code/test_excinfo.py`
- `_try_repr_or_str` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `pytest-9.0.2/src/_pytest/_io/saferepr.py`
- `check_links` (function, debug_prints, primitive): 1 call sites in 1 files -- `pytest-9.0.2/scripts/release.py`
- `do_stuff` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `pytest-9.0.2/testing/code/test_excinfo.py`
- `fix_formatting` (function, debug_prints, primitive): 1 call sites in 1 files -- `pytest-9.0.2/scripts/release.py`
*(+4 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 18316 call pairs -- scoped 54.2%, unique 0.0%, ambiguous 13.5%, external 32.3%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 18316 | 54.2% | 0.0% | 13.5% | 32.3% |

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
