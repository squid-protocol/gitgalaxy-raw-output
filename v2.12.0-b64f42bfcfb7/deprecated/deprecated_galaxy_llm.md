# ARCHITECTURAL_BRIEF: deprecated
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
- **Scope:** 27 analyzed artifact(s), 1443 LOC.
- **Load-bearing artifact:** `deprecated-1.3.1/deprecated/classic.py` -- 5 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `deprecated-1.3.1/tests/test_sphinx.py` -- pulls in 7 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `deprecated-1.3.1/tests/test_sphinx.py` at magnitude 178.74 (structural weight, not risk).
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
| Total Artifacts | 41 |
| Analyzed Artifacts (Scanned) | 27 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 14 |
| Total LOC | 1443 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 65.9% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5311 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.2043 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.2857 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 4 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 19 | 1358 | 70.4% |
| MARKDOWN | 4 | 0 | 14.8% |
| YAML | 2 | 57 | 7.4% |
| PLAINTEXT | 1 | 0 | 3.7% |
| MAKEFILE | 1 | 28 | 3.7% |

## 4.1 SOURCE ENCODINGS
All 27 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Micro Repo (<30 files)`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 37%, Parameter Forwarders Files 19%, Type Conversions Files 11%, Large Core Modules (2) 7%, Compute Cores Files 4%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 22 | 81.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 5 | 18.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 14*

**Composition by Extension & Reason:**
- `.rst`: 5x Excluded (Unsupported Extension: '.rst')
- `.cfg`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.cfg')
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.spec`: 1x Excluded (Unsupported Extension: '.spec')
- `.ini`: 1x Excluded (Unsupported Extension: '.ini')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 48.5 | 13.5 | 3.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 79.9 | 38.8 | 45.4 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 52.2 | 2.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 7.9 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 64.3 | 12.8 | 7.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 16.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 14.8 | 0.7 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 60.8 | 85.7 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 24 | 6 | 2 | `deprecated-1.3.1/tests/test_sphinx.py` |
| cleanup | 3 | 1 | 0 | `deprecated-1.3.1/Makefile` |
| guards | 192 | 15 | 29 | `deprecated-1.3.1/tests/test_sphinx.py` |
| danger | 69 | 14 | 10 | `deprecated-1.3.1/tests/test_deprecated.py` |
| concurrency | 0 | 0 | 0 | - |
| connectivity | 196 | 18 | 22 | `deprecated-1.3.1/tests/test_deprecated.py` |
| io | 15 | 6 | 1 | `deprecated-1.3.1/tests/test_sphinx_class.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 4 | 2 | 0 | `deprecated-1.3.1/deprecated/sphinx.py` |
| events | 2 | 1 | 0 | `deprecated-1.3.1/.github/workflows/codeql-analysis.yml` |
| tests | 127 | 14 | 8 | `deprecated-1.3.1/tests/test_sphinx.py` |
| docs | 45 | 16 | 5 | `deprecated-1.3.1/deprecated/sphinx.py` |
| debt | 39 | 9 | 4 | `deprecated-1.3.1/tests/test_deprecated.py` |
| mutation | 477 | 17 | 40 | `deprecated-1.3.1/tests/test_sphinx.py` |
| dead_code | 63 | 13 | 7 | `deprecated-1.3.1/tests/test_sphinx.py` |
| credential | 0 | 0 | 0 | - |
| threat | 1 | 1 | 0 | `deprecated-1.3.1/deprecated/params.py` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.5**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `deprecated-1.3.1/tests/test_sphinx_class.py` (Hits: 6)
- `deprecated-1.3.1/.github/workflows/python-package.yml` (Hits: 3)
- `deprecated-1.3.1/tests/test_sphinx.py` (Hits: 3)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **classic.py** (`deprecated-1.3.1/deprecated/classic.py`) — 5 inbound connections
2. **params.py** (`deprecated-1.3.1/deprecated/params.py`) — 5 inbound connections
3. **sphinx.py** (`deprecated-1.3.1/deprecated/sphinx.py`) — 4 inbound connections
4. **__init__.py** (`deprecated-1.3.1/deprecated/__init__.py`) — 1 inbound connections
5. **CODE_OF_CONDUCT.md** (`deprecated-1.3.1/.github/CODE_OF_CONDUCT.md`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **test_sphinx.py** (`deprecated-1.3.1/tests/test_sphinx.py`) — 7 outbound dependencies
2. **test_sphinx_class.py** (`deprecated-1.3.1/tests/test_sphinx_class.py`) — 7 outbound dependencies
3. **classic.py** (`deprecated-1.3.1/deprecated/classic.py`) — 6 outbound dependencies
4. **params.py** (`deprecated-1.3.1/deprecated/params.py`) — 5 outbound dependencies
5. **test_demo_paragraph.py** (`deprecated-1.3.1/tests/deprecated_params/test_demo_paragraph.py`) — 5 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `__call__` **(Compute Cores)** (@ `deprecated-1.3.1/deprecated/sphinx.py`) -> Impact: **30.0** | LOC: 46
  * *Intent:* """ Add the Sphinx directive to your class or function. :param wrapped: Wrapped class or function. :return: the decorated class or function. """
- `get_deprecated_msg` **(Compute Cores)** (@ `deprecated-1.3.1/deprecated/classic.py`) -> Impact: **25.2** | LOC: 25
  * *Intent:* """ Get the deprecation warning message for the user. :param wrapped: Wrapped class or function. :param instance: The object to which the wrapped func...
- `__call__` **(Compute Cores)** (@ `deprecated-1.3.1/deprecated/classic.py`) -> Impact: **18.2** | LOC: 52
  * *Intent:* """ Decorate your class or function. :param wrapped: Wrapped class or function. :return: the decorated class or function. .. versionchanged:: 1.2.4 Do...
- `deprecated` **(Many-Argument Workhorses)** (@ `deprecated-1.3.1/deprecated/classic.py`) -> Impact: **15.0** | LOC: 93
  * *Intent:* """ This is a decorator which can be used to mark functions as deprecated. It will result in a warning being emitted when the function is used. **Clas...
- `test_has_sphinx_docstring` **(Many-Argument Workhorses)** (@ `deprecated-1.3.1/tests/test_sphinx.py`) -> Impact: **14.0** | LOC: 36
  * *Intent:* # The function: def foo(x, y): return x + y # with docstring: foo.__doc__ = docstring # is decorated with: decorator_factory = getattr(deprecated.sphi...
- `test_cls_has_sphinx_docstring` **(Many-Argument Workhorses)** (@ `deprecated-1.3.1/tests/test_sphinx.py`) -> Impact: **14.0** | LOC: 36
  * *Intent:* # The class: class Foo(object): pass # with docstring: Foo.__doc__ = docstring # is decorated with: decorator_factory = getattr(deprecated.sphinx, dir...
- `integrate` **(Type Conversions)** (@ `deprecated-1.3.1/tests/deprecated_params/test_demo_versions.py`) -> Impact: **10.8** | LOC: 4
- `populate_messages` **(Defensive Guards)** (@ `deprecated-1.3.1/deprecated/params.py`) -> Impact: **10.4** | LOC: 9
- `__init__` **(Many-Argument Workhorses)** (@ `deprecated-1.3.1/deprecated/classic.py`) -> Impact: **10.0** | LOC: 42
  * *Intent:* """ Construct a wrapper adapter. :type reason: str :param reason: Reason message which documents the deprecation in your library (can be omitted). :ty...
- `area` **(Stateful Encapsulated Methods)** (@ `deprecated-1.3.1/tests/deprecated_params/test_demo_area.py`) -> Impact: **9.4** | LOC: 15

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a
  * **Type Conversions**: cast- and conversion-heavy function

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `deprecated-1.3.1/tests` | 9 | 642.06 | 13.08% | 0.0% |
| `deprecated-1.3.1/deprecated` | 4 | 373.12 | 36.1% | 0.0% |
| `deprecated-1.3.1/tests/deprecated_params` | 5 | 109.66 | 6.42% | 0.0% |
| `deprecated-1.3.1` | 4 | 35.44 | 0.73% | 13.04% |
| `deprecated-1.3.1/.github/workflows` | 2 | 20.44 | 0.0% | 0.0% |
| `deprecated-1.3.1/.github` | 3 | 3.48 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `deprecated-1.3.1/setup.py` -> **52.1538%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `deprecated-1.3.1/deprecated/classic.py` -> **100.0%** Exposure
- `deprecated-1.3.1/deprecated/params.py` -> **100.0%** Exposure
- `deprecated-1.3.1/deprecated/sphinx.py` -> **100.0%** Exposure
- `deprecated-1.3.1/deprecated/__init__.py` -> **68.9974%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `deprecated-1.3.1/tests/test_deprecated.py` -> **13** Orphaned Functions | **16** Duplicates
- `deprecated-1.3.1/tests/test_sphinx.py` -> **15** Orphaned Functions | **6** Duplicates
- `deprecated-1.3.1/tests/test_deprecated_metaclass.py` -> **5** Orphaned Functions | **4** Duplicates
- `deprecated-1.3.1/tests/test_sphinx_metaclass.py` -> **5** Orphaned Functions | **4** Duplicates
- `deprecated-1.3.1/tests/test_deprecated_class.py` -> **8** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `70` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `deprecated-1.3.1/tests/test_sphinx.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.367)
- **Top Global Matches:** file_cluster_12: 7.367, file_cluster_7: 8.008, file_cluster_5: 9.264
- **Magnitude:** 178.74 | **LOC:** 425 | **CtrlFlow:** 4.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 23.523; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (45.4%), Complexity Load (formerly Cognitive Load) (16.3%), Connectivity (formerly Api Exposure) (11.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_has_sphinx_docstring` **(Many-Argument Workhorses)** (Impact: 14.0)
    * *Intent:* # The function: def foo(x, y): return x + y # with docstring: foo.__doc__ = docstring # is decorated...
  * `test_cls_has_sphinx_docstring` **(Many-Argument Workhorses)** (Impact: 14.0)
    * *Intent:* # The class: class Foo(object): pass # with docstring: Foo.__doc__ = docstring # is decorated with: ...
  * `test_sphinx_deprecated_class_method__warns` **(Defensive Guards)** (Impact: 6.3)
    * *Intent:* # noinspection PyShadowingNames
  * `test_sphinx_deprecated_function__warns` **(Defensive Guards)** (Impact: 3.2)
    * *Intent:* # noinspection PyShadowingNames
  * `test_sphinx_deprecated_static_method__warns` **(Defensive Guards)** (Impact: 3.2)
    * *Intent:* # noinspection PyShadowingNames
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 132`, `args: 34`, `func_start: 33`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 35`, `duplicate_logic: 6`, `unreferenced_by_name: 15`
* *Architecture:* `io: 3`, `api: 39`, `import: 7`
* *Defense:* `safety: 42`, `doc: 7`, `test: 36`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 23.523
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, deprecated.sphinx, pytest, re, sys, textwrap, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/deprecated/classic.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.526)
- **Top Global Matches:** file_cluster_9: 6.526, file_cluster_15: 8.032, file_cluster_16: 8.723
- **Magnitude:** 171.98 | **LOC:** 302 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **6**; blast radius 189.972; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 23.8095% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_deprecated_msg` **(Compute Cores)** (Impact: 25.2)
    * *Intent:* """ Get the deprecation warning message for the user. :param wrapped: Wrapped class or function. :pa...
  * `__call__` **(Compute Cores)** (Impact: 18.2)
    * *Intent:* """ Decorate your class or function. :param wrapped: Wrapped class or function. :return: the decorat...
  * `deprecated` **(Many-Argument Workhorses)** (Impact: 15.0)
    * *Intent:* """ This is a decorator which can be used to mark functions as deprecated. It will result in a warni...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 10.0)
    * *Intent:* """ Construct a wrapper adapter. :type reason: str :param reason: Reason message which documents the...
  * `wrapped_cls` **(Compute Cores)** (Impact: 8.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 79
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 29`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 27`
* *Architecture:* `api: 7`, `import: 6`
* *Defense:* `safety: 3`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 189.972
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.25641
  * `Imports (Out-Degree: 0):` functools, inspect, platform, warnings, wrapt, wrapt._wrappers
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `deprecated-1.3.1/tests/test_deprecated.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.943)
- **Top Global Matches:** file_cluster_7: 7.943, file_cluster_12: 9.167, file_cluster_5: 9.824
- **Magnitude:** 157.6 | **LOC:** 325 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 23.523; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (45.3%), Complexity Load (formerly Cognitive Load) (16.3%), Connectivity (formerly Api Exposure) (13.0%)
- **Documentation Coverage:** 92.3077% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_classic_deprecated_class_method__warns` **(Defensive Guards)** (Impact: 7.7)
    * *Intent:* # noinspection PyShadowingNames
  * `classic_deprecated_static_method` **(Annotated & Test Methods)** (Impact: 5.2)
  * `classic_deprecated_class_method` **(Annotated & Test Methods)** (Impact: 5.2)
  * `classic_deprecated_method` **(Annotated & Test Methods)** (Impact: 5.1)
  * `classic_deprecated_function` **(Annotated & Test Methods)** (Impact: 5.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 137`, `args: 36`, `func_start: 36`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 17`, `duplicate_logic: 16`, `unreferenced_by_name: 13`
* *Architecture:* `io: 1`, `api: 46`, `import: 5`
* *Defense:* `safety: 39`, `doc: 2`, `test: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 23.523
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` deprecated.classic, inspect, pytest, sys, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/deprecated/sphinx.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.349)
- **Top Global Matches:** file_cluster_6: 6.349, file_cluster_4: 10.427, file_cluster_8: 15.301
- **Magnitude:** 118.18 | **LOC:** 282 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **3**; blast radius 103.499; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 14.2857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__call__` **(Compute Cores)** (Impact: 30.0)
    * *Intent:* """ Add the Sphinx directive to your class or function. :param wrapped: Wrapped class or function. :...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 9.1)
  * `deprecated` **(Many-Argument Workhorses)** (Impact: 4.7)
    * *Intent:* """ This decorator can be used to insert a "deprecated" directive in your function/class docstring i...
  * `versionadded` **(Many-Argument Workhorses)** (Impact: 3.4)
    * *Intent:* """ This decorator can be used to insert a "versionadded" directive in your function/class docstring...
  * `versionchanged` **(Many-Argument Workhorses)** (Impact: 3.4)
    * *Intent:* """ This decorator can be used to insert a "versionchanged" directive in your function/class docstri...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 56
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 20`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 26`
* *Architecture:* `api: 7`, `import: 4`
* *Defense:* `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 103.499
  * `Choke Point (Betweenness):` 0.006154 | `Ripple Effect (Closeness):` 0.153846
  * `Imports (Out-Degree: 1):` deprecated.classic, re, textwrap
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `deprecated-1.3.1/tests/test_deprecated_metaclass.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.594)
- **Top Global Matches:** file_cluster_12: 7.594, file_cluster_13: 8.089, file_cluster_15: 8.413
- **Magnitude:** 69.74 | **LOC:** 116 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 23.523; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (45.8%), Complexity Load (formerly Cognitive Load) (42.6%), Connectivity (formerly Api Exposure) (10.8%)
- **Documentation Coverage:** 85.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__call__` **(Parameter Forwarders)** (Impact: 4.2)
  * `test_with_singleton_metaclass` **(Annotated & Test Methods)** (Impact: 3.4)
  * `with_metaclass` **(Parameter Forwarders)** (Impact: 2.5)
    * *Intent:* """Create a base class with a metaclass."""
  * `__new__` **(Parameter Forwarders)** (Impact: 2.3)
  * `__new__` **(Parameter Forwarders)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 56`, `args: 14`, `func_start: 14`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 19`, `duplicate_logic: 4`, `unreferenced_by_name: 5`
* *Architecture:* `api: 12`, `import: 2`
* *Defense:* `safety: 15`, `doc: 1`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 23.523
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` deprecated.classic, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/tests/test_sphinx_metaclass.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.594)
- **Top Global Matches:** file_cluster_12: 7.594, file_cluster_13: 8.089, file_cluster_15: 8.413
- **Magnitude:** 69.74 | **LOC:** 116 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 23.523; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (45.8%), Complexity Load (formerly Cognitive Load) (42.6%), Connectivity (formerly Api Exposure) (10.8%)
- **Documentation Coverage:** 85.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__call__` **(Parameter Forwarders)** (Impact: 4.2)
  * `test_with_singleton_metaclass` **(Annotated & Test Methods)** (Impact: 3.4)
  * `with_metaclass` **(Parameter Forwarders)** (Impact: 2.5)
    * *Intent:* """Create a base class with a metaclass."""
  * `__new__` **(Parameter Forwarders)** (Impact: 2.3)
  * `__new__` **(Parameter Forwarders)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 56`, `args: 14`, `func_start: 14`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 19`, `duplicate_logic: 4`, `unreferenced_by_name: 5`
* *Architecture:* `api: 12`, `import: 2`
* *Defense:* `safety: 15`, `doc: 1`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 23.523
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` deprecated.sphinx, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/deprecated/params.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.446)
- **Top Global Matches:** file_cluster_12: 6.446, file_cluster_7: 8.349, file_cluster_15: 8.819
- **Magnitude:** 65.84 | **LOC:** 80 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **5**; blast radius 121.994; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (65.0%), Connectivity (formerly Api Exposure) (64.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `populate_messages` **(Defensive Guards)** (Impact: 10.4)
  * `check_params` **(Compute Cores)** (Impact: 6.9)
  * `__call__` **(Parameter Forwarders)** (Impact: 4.0)
    * *Intent:* # type: (callable) -> callable signature = inspect.signature(f) @functools.wraps(f) def wrapper(*arg...
  * `warn_messages` **(Parameter Forwarders)** (Impact: 3.7)
    * *Intent:* # type: (list[str]) -> None for message in messages: warnings.warn(message, category=self.category, ...
  * `wrapper` **(Parameter Forwarders)** (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 16`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 11`
* *Architecture:* `api: 7`, `import: 5`
* *Defense:* `safety: 4`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 121.994
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.197802
  * `Imports (Out-Degree: 0):` collections, functools, inspect, inspect2, warnings
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `deprecated-1.3.1/tests/test_deprecated_class.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.758)
- **Top Global Matches:** file_cluster_7: 7.758, file_cluster_12: 9.922, file_cluster_5: 10.278
- **Magnitude:** 63.98 | **LOC:** 156 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 23.523; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (42.1%), Connectivity (formerly Api Exposure) (12.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_class_deprecation_using_wrapper` **(Defensive Guards)** (Impact: 2.4)
    * *Intent:* # stream is used to store the deprecation message for testing stream = io.StringIO() class MyBaseCla...
  * `test_class_deprecation_using_a_simple_decorator` **(Annotated & Test Methods)** (Impact: 2.4)
    * *Intent:* # stream is used to store the deprecation message for testing stream = io.StringIO() # To deprecated...
  * `__new__` **(Parameter Forwarders)** (Impact: 2.1)
  * `wrapped_new` **(Parameter Forwarders)** (Impact: 2.1)
  * `wrapped_new` **(Parameter Forwarders)** (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 74`, `args: 12`, `func_start: 12`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 16`, `unreferenced_by_name: 8`
* *Architecture:* `api: 22`, `import: 5`
* *Defense:* `safety: 29`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 23.523
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, deprecated.classic, inspect, io, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/tests/test_sphinx_class.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.963)
- **Top Global Matches:** file_cluster_7: 7.963, file_cluster_14: 10.078, file_cluster_5: 10.646
- **Magnitude:** 50.44 | **LOC:** 150 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 23.523; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (40.3%), Connectivity (formerly Api Exposure) (12.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_class_deprecation_using_a_simple_decorator` **(Annotated & Test Methods)** (Impact: 2.4)
    * *Intent:* # stream is used to store the deprecation message for testing stream = io.StringIO() # To deprecated...
  * `wrapped_new` **(Parameter Forwarders)** (Impact: 2.1)
  * `simple_decorator` **(Parameter Forwarders)** (Impact: 1.9)
    * *Intent:* # To deprecated the class, we use a simple decorator # which patches the original ``__new__`` method...
  * `test_subclass_deprecation_using_deprecated_decorator` **(Annotated & Test Methods)** (Impact: 1.9)
  * `test_class_deprecation_using_deprecated_decorator` **(Annotated & Test Methods)** (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 67`, `args: 9`, `func_start: 9`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 10`, `unreferenced_by_name: 7`
* *Architecture:* `io: 6`, `api: 22`, `import: 7`
* *Defense:* `safety: 30`, `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 23.523
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, deprecated.sphinx, inspect, io, pytest, sys, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/tests/deprecated_params/test_demo_paragraph.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.379)
- **Top Global Matches:** file_cluster_15: 7.379, file_cluster_13: 7.697, file_cluster_2: 8.243
- **Magnitude:** 36.46 | **LOC:** 67 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 23.523; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (64.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (15.4%), Connectivity (formerly Api Exposure) (5.2%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `paragraph` **(Compute Cores)** (Impact: 8.4)
    * *Intent:* """Create a styled HTML paragraphe."""
  * `test_paragraph` **(Type Conversions)** (Impact: 4.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 12`, `args: 2`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 7`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 2`, `import: 5`
* *Defense:* `safety: 1`, `doc: 3`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 23.523
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` deprecated.params, pytest, sys, warnings, xml.sax.saxutils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/tests/test_sphinx_adapter.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.697)
- **Top Global Matches:** file_cluster_12: 6.697, file_cluster_7: 7.797, file_cluster_11: 9.027
- **Magnitude:** 35.12 | **LOC:** 129 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 23.523; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (53.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (8.0%)
- **Documentation Coverage:** 85.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_sphinx_adapter` **(Defensive Guards)** (Impact: 3.0)
  * `test_sphinx_adapter__empty_docstring` **(Defensive Guards)** (Impact: 2.7)
  * `test_decorator_accept_line_length` **(Defensive Guards)** (Impact: 2.7)
  * `foo` **(Interface Declarations)** (Impact: 1.1)
    * *Intent:* """ Description of foo :return: nothing """
  * `foo` **(Interface Declarations)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 21`, `args: 6`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 16`, `duplicate_logic: 2`, `unreferenced_by_name: 3`
* *Architecture:* `api: 6`, `import: 6`
* *Defense:* `safety: 3`, `doc: 5`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 23.523
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` deprecated.sphinx, pytest, textwrap
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/tests/deprecated_params/test_demo_versions.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.748)
- **Top Global Matches:** file_cluster_12: 7.748, file_cluster_7: 8.068, file_cluster_5: 9.544
- **Magnitude:** 26.12 | **LOC:** 46 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 23.523; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (56.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (7.1%), Complexity Load (formerly Cognitive Load) (6.7%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `integrate` **(Type Conversions)** (Impact: 10.8)
  * `test_only_one_warning_for_each_parameter` **(Callbacks & Closures)** (Impact: 2.8)
    * *Intent:* """ This unit test checks that only one warning message is emitted for each deprecated parameter. Ho...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 11`, `args: 3`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* `safety: 1`, `doc: 2`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 23.523
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` deprecated.params, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/tests/deprecated_params/test_demo_area.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 7.138)
- **Top Global Matches:** file_cluster_16: 7.138, file_cluster_13: 7.945, file_cluster_15: 8.379
- **Magnitude:** 21.42 | **LOC:** 63 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 23.523; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (44.9%), Complexity Load (formerly Cognitive Load) (5.7%), Connectivity (formerly Api Exposure) (3.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `area` **(Stateful Encapsulated Methods)** (Impact: 9.4)
  * `test_area` **(Type Conversions)** (Impact: 4.3)
  * `_area_impl` **(Encapsulated Accessors)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 14`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 1`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `safety: 1`, `doc: 1`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 23.523
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` deprecated.params, pytest, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/deprecated/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.951)
- **Top Global Matches:** file_cluster_2: 3.951, file_cluster_17: 5.141, file_cluster_13: 5.629
- **Magnitude:** 17.12 | **LOC:** 17 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 43.517; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (69.0%), Guard Balance (formerly Safety Score) (52.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `import: 2`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 43.517
  * `Choke Point (Betweenness):` 0.003077 | `Ripple Effect (Closeness):` 0.038462
  * `Imports (Out-Degree: 2):` deprecated.classic, deprecated.params
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `deprecated-1.3.1/Makefile` (MAKEFILE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.212)
- **Top Global Matches:** file_cluster_2: 6.212, file_cluster_13: 8.01, file_cluster_17: 8.052
- **Magnitude:** 16.86 | **LOC:** 41 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (7.1%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `clean-pyc` **(I/O & Config Routines)** (Impact: 1.2)
  * `all` **(State Mutators)** (Impact: 1.1)
  * `install-dev` **(I/O & Config Routines)** (Impact: 1.1)
  * `test` **(I/O & Config Routines)** (Impact: 1.1)
  * `coverage` **(I/O & Config Routines)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `func_start: 12`
* *Risk/State:* None
* *Architecture:* `api: 3`
* *Defense:* `test: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.523
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/.github/workflows/codeql-analysis.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.419)
- **Top Global Matches:** file_cluster_2: 3.419, file_cluster_17: 4.708, file_cluster_13: 5.64
- **Magnitude:** 16.62 | **LOC:** 72 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 23.523; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Dead Code Surface (formerly Dead Code) (14.8%), Connectivity (formerly Api Exposure) (3.2%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`, `args: 1`, `class_start: 1`
* *Risk/State:* `dead_code: 1`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `safety: 1`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.523
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` checkout@v4, analyze@v1, autobuild@v1, init@v1
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/setup.py` (PYTHON | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 1.736)
- **Top Global Matches:** file_cluster_2: 1.736, file_cluster_17: 4.561, file_cluster_13: 5.679
- **Magnitude:** 16.16 | **LOC:** 200 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 23.523; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (52.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (2.9%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 2`
* *Risk/State:* `fragile_debt: 1`
* *Architecture:* `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.523
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` setuptools
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/tests/deprecated_params/test_demo_pow2.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.899)
- **Top Global Matches:** file_cluster_15: 6.899, file_cluster_13: 7.433, file_cluster_11: 8.044
- **Magnitude:** 15.14 | **LOC:** 59 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 23.523; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (53.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (5.4%), Complexity Load (formerly Cognitive Load) (4.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_pow2` **(Type Conversions)** (Impact: 4.3)
  * `pow2` **(Parameter Forwarders)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 11`, `args: 2`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 2`, `import: 4`
* *Defense:* `safety: 1`, `doc: 2`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 23.523
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` deprecated.params, pytest, sys, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/tests/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.523
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/tests/deprecated_params/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.523
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/tests/test.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.089)
- **Top Global Matches:** file_cluster_15: 8.089, file_cluster_11: 8.152, file_cluster_13: 8.254
- **Magnitude:** 6.18 | **LOC:** 28 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 23.523; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (43.6%), Connectivity (formerly Api Exposure) (5.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_deprecated_has_version` **(Defensive Guards)** (Impact: 1.8)
    * *Intent:* # The deprecated package must have a valid version number assert deprecated.__version__ is not None ...
  * `test_deprecated_has_docstring` **(Defensive Guards)** (Impact: 1.2)
    * *Intent:* # The deprecated package must have a docstring assert deprecated.__doc__ is not None assert "Depreca...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 8`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `safety: 4`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 23.523
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` deprecated, pkg_resources
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/.github/workflows/python-package.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.751)
- **Top Global Matches:** file_cluster_2: 5.751, file_cluster_13: 7.061, file_cluster_17: 7.163
- **Magnitude:** 3.82 | **LOC:** 34 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 23.523; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (3.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Install dependencies` **(I/O & Config Routines)** (Impact: 1.2)
  * `Test with pytest` **(I/O & Config Routines)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`, `args: 1`, `func_start: 2`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `io: 3`, `api: 1`, `import: 2`
* *Defense:* `doc: 1`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.523
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` checkout@v4, setup-python@v5
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/.github/CODE_OF_CONDUCT.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.48 | **LOC:** 74 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.523
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.42 | **LOC:** 71 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.523
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/.github/ISSUE_TEMPLATE.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.0 | **LOC:** 32 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.523
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `deprecated-1.3.1/tests/test.py` (PYTHON) | Magnitude: 6.18 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 5, safety: 4, args: 2

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `deprecated-1.3.1/deprecated/sphinx.py` -> **Severity: 0.615** (Bridge: 0.0062 * Flux: 100.0%)
- `deprecated-1.3.1/deprecated/__init__.py` -> **Severity: 0.212** (Bridge: 0.0031 * Flux: 68.9974%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `deprecated-1.3.1/deprecated/classic.py` -> **Severity: 20.49** (Embedded: 0.2564 * Error Risk: 79.9115%)
- `deprecated-1.3.1/deprecated/params.py` -> **Severity: 12.849** (Embedded: 0.1978 * Error Risk: 64.9568%)
- `deprecated-1.3.1/deprecated/sphinx.py` -> **Severity: 11.54** (Embedded: 0.1538 * Error Risk: 75.0071%)
- `deprecated-1.3.1/deprecated/__init__.py` -> **Severity: 2.027** (Embedded: 0.0385 * Error Risk: 52.7116%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `deprecated-1.3.1/deprecated/params.py` -> **Severity: 12199.4** (Blast Radius: 121.994 * Doc Risk: 100.0%)
- `deprecated-1.3.1/deprecated/classic.py` -> **Severity: 4523.138** (Blast Radius: 189.972 * Doc Risk: 23.8095%)
- `deprecated-1.3.1/tests/deprecated_params/test_demo_area.py` -> **Severity: 2352.3** (Blast Radius: 23.523 * Doc Risk: 100.0%)
- `deprecated-1.3.1/tests/deprecated_params/test_demo_pow2.py` -> **Severity: 2352.3** (Blast Radius: 23.523 * Doc Risk: 100.0%)
- `deprecated-1.3.1/tests/test.py` -> **Severity: 2352.3** (Blast Radius: 23.523 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 5 literal sites + 3 sites through wrappers = 8

- `fun` (function, debug_prints, primitive): 3 call sites in 1 files -- `deprecated-1.3.1/tests/test_deprecated.py`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 443 call pairs -- scoped 29.1%, unique 0.0%, ambiguous 0.5%, external 70.4%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 443 | 29.1% | 0.0% | 0.5% | 70.4% |

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
