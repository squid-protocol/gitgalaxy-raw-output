# ARCHITECTURAL_BRIEF: pip
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/pypa/pip.git` |
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
- **Scope:** 578 analyzed artifact(s), 88424 LOC.
- **Load-bearing artifact:** `tests/lib/__init__.py` -- 84 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/pip/_vendor/rich/console.py` -- pulls in 52 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/pip/_vendor/pkg_resources/__init__.py` at magnitude 2558.58 (structural weight, not risk).
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
| Total Artifacts | 1017 |
| Analyzed Artifacts (Scanned) | 578 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 439 |
| Total LOC | 88424 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 56.8% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5592 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1822 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 25.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.0223 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 36 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 509 | 87825 | 88.1% |
| PLAINTEXT | 39 | 0 | 6.7% |
| HTML | 14 | 98 | 2.4% |
| YAML | 10 | 499 | 1.7% |
| MARKDOWN | 4 | 0 | 0.7% |
| M4 | 1 | 2 | 0.2% |
| C | 1 | 0 | 0.2% |

## 4.1 SOURCE ENCODINGS
All 578 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Generic / Templated Code Files 33%, Data / Markup / Trivial 27%, Large Core Modules (2) 13%, Large Core Modules (3) 9%, Many-Argument Workhorses Files 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 535 | 92.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 43 | 7.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 439*

**Composition by Extension & Reason:**
- `.py`: 134x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rst`: 68x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 8x Excluded (Unsupported Extension: '.rst')
- `.gz`: 53x Excluded (Explicitly Denied Extension: '.gz')
- `.md`: 41x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.whl`: 33x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded (Unsupported Extension: '.whl')
- `no_extension`: 25x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cfg`: 13x Unsupported Format (.cfg), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.typed`: 8x Unsupported Format (.typed), 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.patch`: 8x Unsupported Format (.patch)
- `.exe`: 6x Excluded (Explicitly Denied Extension: '.exe')
- `.txt`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 23 LOC)
- `.toml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.toml')
- `.zip`: 3x Excluded (Explicitly Denied Extension: '.zip')
- `.pending`: 3x Unsupported Format (.pending)
- `.yml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 87.3 | 22.0 | 12.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 84.6 | 47.0 | 52.4 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 5.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 18.7 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 22.3 | 10.7 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 98.8 | 0.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 45.5 | 11.9 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 20.9 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 6.5 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 5.2 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 52.9 | 60.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 98.9 | 0.2 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1390 | 233 | 6 | `tests/functional/test_install.py` |
| cleanup | 59 | 27 | 0 | `src/pip/_vendor/urllib3/response.py` |
| guards | 6093 | 364 | 28 | `src/pip/_vendor/pkg_resources/__init__.py` |
| danger | 2123 | 283 | 10 | `src/pip/_vendor/pkg_resources/__init__.py` |
| concurrency | 777 | 123 | 4 | `src/pip/_vendor/rich/segment.py` |
| connectivity | 5509 | 425 | 24 | `src/pip/_vendor/pkg_resources/__init__.py` |
| io | 2535 | 262 | 12 | `src/pip/_vendor/pkg_resources/__init__.py` |
| crypto | 56 | 32 | 0 | `src/pip/_vendor/urllib3/util/ssl_.py` |
| ipc | 117 | 36 | 0 | `tests/lib/__init__.py` |
| time | 77 | 22 | 0 | `tests/unit/test_index.py` |
| serialization | 1 | 1 | 0 | `tests/functional/test_configuration.py` |
| regex | 106 | 48 | 0 | `src/pip/_vendor/pkg_resources/__init__.py` |
| events | 387 | 77 | 2 | `src/pip/_internal/cli/cmdoptions.py` |
| tests | 3616 | 140 | 18 | `tests/unit/test_vcs.py` |
| docs | 3487 | 385 | 17 | `src/pip/_vendor/pkg_resources/__init__.py` |
| debt | 473 | 154 | 2 | `src/pip/_vendor/rich/_win32_console.py` |
| mutation | 32712 | 459 | 161 | `src/pip/_vendor/pkg_resources/__init__.py` |
| dead_code | 1833 | 163 | 9 | `tests/functional/test_install.py` |
| credential | 7 | 5 | 0 | `src/pip/_vendor/urllib3/util/url.py` |
| threat | 2 | 2 | 0 | `src/pip/_internal/utils/unpacking.py` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 71 | 24 | 0 | `src/pip/_vendor/rich/console.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.8782**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/pip/_vendor/pkg_resources/__init__.py` (Hits: 105)
- `tests/lib/__init__.py` (Hits: 94)
- `tests/unit/test_utils_unpacking.py` (Hits: 86)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **__init__.py** (`tests/lib/__init__.py`) — 84 inbound connections
2. **exceptions.py** (`src/pip/_internal/exceptions.py`) — 81 inbound connections
3. **misc.py** (`src/pip/_internal/utils/misc.py`) — 70 inbound connections
4. **console.py** (`src/pip/_vendor/rich/console.py`) — 56 inbound connections
5. **__init__.py** (`src/pip/_internal/metadata/__init__.py`) — 34 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **console.py** (`src/pip/_vendor/rich/console.py`) — 52 outbound dependencies
2. **req_install.py** (`src/pip/_internal/req/req_install.py`) — 39 outbound dependencies
3. **__init__.py** (`src/pip/_vendor/pkg_resources/__init__.py`) — 38 outbound dependencies
4. **session.py** (`src/pip/_internal/network/session.py`) — 37 outbound dependencies
5. **__init__.py** (`tests/lib/__init__.py`) — 36 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `__init__` **(Stateful Encapsulated Methods)** (@ `src/pip/_vendor/rich/style.py`) -> Impact: **247.8** | LOC: 75
- `__init__` **(Many-Argument Workhorses)** (@ `src/pip/_vendor/rich/console.py`) -> Impact: **225.7** | LOC: 133
- `traverse` **(Many-Argument Workhorses)** (@ `src/pip/_vendor/rich/pretty.py`) -> Impact: **184.7** | LOC: 296
- `urlopen` **(Many-Argument Workhorses)** (@ `src/pip/_vendor/urllib3/connectionpool.py`) -> Impact: **158.4** | LOC: 379
- `_traverse` **(Many-Argument Workhorses)** (@ `src/pip/_vendor/rich/pretty.py`) -> Impact: **156.6** | LOC: 252
  * *Intent:* """Walk the object depth first."""
- `_render` **(Many-Argument Workhorses)** (@ `src/pip/_vendor/rich/table.py`) -> Impact: **152.1** | LOC: 180
- `extract` **(Many-Argument Workhorses)** (@ `src/pip/_vendor/rich/traceback.py`) -> Impact: **152.1** | LOC: 189
- `get_scheme` **(Many-Argument Workhorses)** (@ `src/pip/_internal/locations/__init__.py`) -> Impact: **137.8** | LOC: 164
- `export_svg` **(Many-Argument Workhorses)** (@ `src/pip/_vendor/rich/console.py`) -> Impact: **122.8** | LOC: 250
- `call_subprocess` **(Many-Argument Workhorses)** (@ `src/pip/_internal/utils/subprocess.py`) -> Impact: **122.6** | LOC: 166

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/pip/_vendor/rich` | 77 | 16375.38 | 32.73% | 5.1% |
| `tests/functional` | 67 | 7560.32 | 7.47% | 0.0% |
| `tests/unit` | 60 | 6811.5 | 9.3% | 0.0% |
| `src/pip/_vendor/urllib3` | 12 | 2953.7 | 31.03% | 9.58% |
| `src/pip/_vendor/pkg_resources` | 1 | 2558.58 | 47.04% | 67.76% |
| `src/pip/_internal/utils` | 26 | 2514.18 | 34.07% | 6.6% |
| `src/pip/_internal/req` | 8 | 2266.6 | 47.89% | 8.07% |
| `src/pip/_internal/commands` | 19 | 2199.02 | 33.97% | 26.2% |
| `src/pip/_vendor/urllib3/util` | 13 | 2085.78 | 40.42% | 9.87% |
| `tests/lib` | 15 | 2036.58 | 12.37% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `.github/ISSUE_TEMPLATE/bug-report.yml` -> **99.9859%** Exposure
- `src/pip/_internal/resolution/resolvelib/requirements.py` -> **99.8388%** Exposure
- `src/pip/_vendor/urllib3/contrib/pyopenssl.py` -> **99.7743%** Exposure
- `src/pip/_internal/resolution/resolvelib/candidates.py` -> **98.6206%** Exposure
- `src/pip/_vendor/rich/bar.py` -> **98.1139%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/pip/_internal/build_env.py` -> **100.0%** Exposure
- `src/pip/_internal/cli/autocompletion.py` -> **100.0%** Exposure
- `src/pip/_internal/cli/index_command.py` -> **100.0%** Exposure
- `src/pip/_internal/cli/main_parser.py` -> **100.0%** Exposure
- `src/pip/_internal/cli/parser.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/functional/test_install.py` -> **119** Orphaned Functions | **0** Duplicates
- `tests/functional/test_new_resolver.py` -> **73** Orphaned Functions | **0** Duplicates
- `tests/unit/test_req_file.py` -> **68** Orphaned Functions | **0** Duplicates
- `tests/unit/test_req.py` -> **56** Orphaned Functions | **4** Duplicates
- `tests/unit/test_utils.py` -> **60** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `src/pip/_vendor/urllib3/contrib/_securetransport/low_level.py` -> **98.86%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `10` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3592` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/pip/_vendor/pkg_resources/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.873)
- **Top Global Matches:** file_cluster_5: 7.873, file_cluster_12: 8.489, file_cluster_0: 10.117
- **Magnitude:** 2558.58 | **LOC:** 3677 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **38**; blast radius 0.636; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.4%), Debt Markers (formerly Tech Debt) (67.8%)
- **Documentation Coverage:** 59.2593% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `insert_on` **(Many-Argument Workhorses)** (Impact: 50.6)
    * *Intent:* # FIXME: 'Distribution.insert_on' is too complex (13)
  * `compatible_platforms` **(Compute Cores)** (Impact: 31.8)
    * *Intent:* """Can code for the `provided` platform run on the `required` platform? Returns true if either platf...
  * `_resolve_dist` **(Many-Argument Workhorses)** (Impact: 31.5)
  * `dist_factory` **(Compute Cores)** (Impact: 22.9)
    * *Intent:* """Return a dist_factory for the given entry."""
  * `_extract_resource` **(Many-Argument Workhorses)** (Impact: 22.6)
    * *Intent:* # FIXME: 'ZipProvider._extract_resource' is too complex (12)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 302 instances
* *State Mutation (weighted view):* 1045
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 396`, `structural_boundaries: 700`, `args: 283`, `func_start: 280`, `class_start: 34`
* *Risk/State:* `safety_bypasses: 50`, `high_risk_execution: 4`, `state_mutation: 441`, `planned_debt: 7`, `fragile_debt: 9`, `duplicate_logic: 4`, `unreferenced_by_name: 20`
* *Architecture:* `io: 105`, `api: 189`, `import: 49`
* *Defense:* `safety: 97`, `doc: 158`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.636
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` __future__, __main__, _imp, _typeshed, collections, email.parser, errno, functools...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/pip/_vendor/rich/console.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.459)
- **Top Global Matches:** file_cluster_5: 8.459, file_cluster_4: 9.87, file_cluster_12: 10.171
- **Magnitude:** 2242.86 | **LOC:** 2681 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **56** in-repo importer(s); it depends on **52**; blast radius 36.154; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.3%), Connectivity (formerly Api Exposure) (69.9%)
- **Documentation Coverage:** 46.0784% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 225.7)
  * `export_svg` **(Many-Argument Workhorses)** (Impact: 122.8)
  * `print` **(Many-Argument Workhorses)** (Impact: 83.2)
  * `render_str` **(Many-Argument Workhorses)** (Impact: 50.4)
  * `export_html` **(Many-Argument Workhorses)** (Impact: 50.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 256 instances
* *Concurrency (weighted view):* 19
* *State Mutation (weighted view):* 859
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 320`, `structural_boundaries: 373`, `args: 116`, `func_start: 116`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 347`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 21`, `api: 96`, `concurrency: 4`, `import: 54`
* *Defense:* `safety: 41`, `doc: 118`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 36.154
  * `Choke Point (Betweenness):` 0.036382 | `Ripple Effect (Closeness):` 0.210745
  * `Imports (Out-Degree: 36):` ._emoji_replace, ._export_format, ._fileno, ._log_render, ._windows, .align, .color, .control...
  * `Imported By (In-Degree: 56):` (Excluded from Brief to save tokens)

### `src/pip/_vendor/rich/text.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.319)
- **Top Global Matches:** file_cluster_5: 8.319, file_cluster_0: 8.424, file_cluster_12: 9.0
- **Magnitude:** 1346.68 | **LOC:** 1362 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **34** in-repo importer(s); it depends on **21**; blast radius 14.899; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (83.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.7%)
- **Documentation Coverage:** 46.4% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `wrap` **(Many-Argument Workhorses)** (Impact: 39.1)
  * `divide` **(Many-Argument Workhorses)** (Impact: 35.1)
    * *Intent:* """Divide text in to a number of lines at given offsets. Args: offsets (Iterable[int]): Offsets used...
  * `split` **(Many-Argument Workhorses)** (Impact: 33.5)
  * `highlight_regex` **(Many-Argument Workhorses)** (Impact: 33.3)
  * `with_indent_guides` **(Many-Argument Workhorses)** (Impact: 31.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 198 instances
* *State Mutation (weighted view):* 628
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 224`, `structural_boundaries: 179`, `args: 65`, `func_start: 65`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 232`, `planned_debt: 2`
* *Architecture:* `api: 62`, `import: 22`
* *Defense:* `safety: 16`, `doc: 56`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.899
  * `Choke Point (Betweenness):` 0.008019 | `Ripple Effect (Closeness):` 0.201975
  * `Imports (Out-Degree: 15):` ._loop, ._pick, ._wrap, .align, .ansi, .cells, .console, .containers...
  * `Imported By (In-Degree: 34):` (Excluded from Brief to save tokens)

### `src/pip/_vendor/rich/progress.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.935)
- **Top Global Matches:** file_cluster_0: 6.935, file_cluster_5: 7.554, file_cluster_12: 8.9
- **Magnitude:** 1159.18 | **LOC:** 1716 | **CtrlFlow:** 13.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **32**; blast radius 0.9; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.6%), Connectivity (formerly Api Exposure) (62.1%)
- **Documentation Coverage:** 57.8947% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `update` **(Many-Argument Workhorses)** (Impact: 47.3)
  * `open` **(Many-Argument Workhorses)** (Impact: 40.3)
  * `track` **(Many-Argument Workhorses)** (Impact: 27.7)
  * `reset` **(Many-Argument Workhorses)** (Impact: 22.9)
  * `open` **(Many-Argument Workhorses)** (Impact: 21.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 133 instances
* *State Mutation (weighted view):* 461
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 151`, `structural_boundaries: 281`, `args: 97`, `func_start: 96`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 195`
* *Architecture:* `io: 8`, `api: 90`, `concurrency: 1`, `import: 34`
* *Defense:* `safety: 7`, `doc: 80`, `sync_locks: 6`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.9
  * `Choke Point (Betweenness):` 0.001841 | `Ripple Effect (Closeness):` 0.093552
  * `Imports (Out-Degree: 14):` .console, .filesize, .get_console, .highlighter, .jupyter, .live, .panel, .progress_bar...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/lib/__init__.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.21)
- **Top Global Matches:** file_cluster_5: 7.21, file_cluster_12: 9.08, file_cluster_0: 9.794
- **Magnitude:** 1073.4 | **LOC:** 1432 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 54.5%
- **Blast Radius:** changing it is visible to **84** in-repo importer(s); it depends on **36**; blast radius 22.139; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (96.1%), Guard Balance (formerly Safety Score) (70.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (63.7%), Complexity Load (formerly Cognitive Load) (32.3%)
- **Documentation Coverage:** 96.9512% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assert_installed` **(Many-Argument Workhorses)** (Impact: 81.6)
  * `run` **(Many-Argument Workhorses)** (Impact: 61.0)
  * `diff_states` **(Many-Argument Workhorses)** (Impact: 26.1)
    * *Intent:* # FIXME ScriptTest does something similar, but only within a single # ProcResult; this generalizes i...
  * `create_basic_wheel_for_package` **(Many-Argument Workhorses)** (Impact: 22.7)
  * `pip_install_local` **(Many-Argument Workhorses)** (Impact: 18.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 125 instances
* *State Mutation (weighted view):* 434
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 147`, `structural_boundaries: 265`, `args: 86`, `func_start: 86`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 184`, `fragile_debt: 3`
* *Architecture:* `io: 94`, `api: 81`, `import: 37`
* *Defense:* `safety: 31`, `doc: 30`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 22.139
  * `Choke Point (Betweenness):` 0.038562 | `Ripple Effect (Closeness):` 0.145581
  * `Imports (Out-Degree: 14):` __future__, base64, collections.abc, contextlib, datetime, hashlib, io, json...
  * `Imported By (In-Degree: 84):` (Excluded from Brief to save tokens)

### `tests/functional/test_install.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.307)
- **Top Global Matches:** file_cluster_0: 7.307, file_cluster_15: 9.371, file_cluster_13: 9.622
- **Magnitude:** 1025.74 | **LOC:** 2830 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **26**; blast radius 0.636; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (69.4%), Guard Balance (formerly Safety Score) (47.7%), Connectivity (formerly Api Exposure) (11.8%), Complexity Load (formerly Cognitive Load) (10.4%)
- **Documentation Coverage:** 81.9277% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_install_dry_run_nothing_installed` **(Defensive Guards)** (Impact: 15.0)
  * `test_install_builds_wheels` **(Type Conversions)** (Impact: 14.1)
    * *Intent:* # We need to use a subprocess to get the right value on Windows. res = script.run( "python", "-c", (...
  * `install_find_links` **(Many-Argument Workhorses)** (Impact: 13.5)
  * `test_pep518_uses_build_env` **(Many-Argument Workhorses)** (Impact: 11.0)
  * `test_install_editable_with_wrong_egg_name` **(Type Conversions)** (Impact: 10.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 39 instances
* *State Mutation (weighted view):* 412
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 378`, `args: 126`, `func_start: 126`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 334`, `planned_debt: 1`, `unreferenced_by_name: 119`
* *Architecture:* `io: 38`, `api: 123`, `import: 25`
* *Defense:* `safety: 168`, `doc: 93`, `test: 158`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.636
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` __future__, collections.abc, hashlib, io, lzma, os, os.path, pathlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/pip/_vendor/rich/table.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.152)
- **Top Global Matches:** file_cluster_6: 8.152, file_cluster_4: 9.961, file_cluster_5: 16.675
- **Magnitude:** 995.66 | **LOC:** 1007 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **19**; blast radius 4.483; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.5%), Connectivity (formerly Api Exposure) (48.2%)
- **Documentation Coverage:** 56.8627% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_render` **(Many-Argument Workhorses)** (Impact: 152.1)
  * `_calculate_column_widths` **(Many-Argument Workhorses)** (Impact: 65.2)
  * `_get_cells` **(Many-Argument Workhorses)** (Impact: 52.8)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 40.2)
  * `_collapse_widths` **(Stateful Encapsulated Methods)** (Impact: 37.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 121 instances
* *State Mutation (weighted view):* 414
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 184`, `structural_boundaries: 101`, `args: 28`, `func_start: 28`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 172`
* *Architecture:* `api: 24`, `import: 18`
* *Defense:* `safety: 2`, `doc: 43`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.483
  * `Choke Point (Betweenness):` 0.003611 | `Ripple Effect (Closeness):` 0.15025
  * `Imports (Out-Degree: 16):` ._loop, ._pick, ._ratio, ._timer, .align, .box, .console, .errors...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `src/pip/_vendor/rich/pretty.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.723)
- **Top Global Matches:** file_cluster_5: 8.723, file_cluster_12: 10.741, file_cluster_4: 11.094
- **Magnitude:** 976.12 | **LOC:** 1017 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **25**; blast radius 3.125; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.5%), Complexity Load (formerly Cognitive Load) (63.5%)
- **Documentation Coverage:** 56.25% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `traverse` **(Many-Argument Workhorses)** (Impact: 184.7)
  * `_traverse` **(Many-Argument Workhorses)** (Impact: 156.6)
    * *Intent:* """Walk the object depth first."""
  * `install` **(Many-Argument Workhorses)** (Impact: 28.0)
  * `_ipy_display_hook` **(Many-Argument Workhorses)** (Impact: 24.4)
  * `__rich_console__` **(Many-Argument Workhorses)** (Impact: 19.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 104 instances
* *State Mutation (weighted view):* 344
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 146`, `structural_boundaries: 155`, `args: 44`, `func_start: 34`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 136`
* *Architecture:* `io: 3`, `api: 25`, `import: 31`
* *Defense:* `safety: 25`, `doc: 24`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.125
  * `Choke Point (Betweenness):` 0.001183 | `Ripple Effect (Closeness):` 0.151816
  * `Imports (Out-Degree: 11):` ._loop, ._pick, .abc, .cells, .console, .get_console, .highlighter, .jupyter...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `src/pip/_vendor/rich/style.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.254)
- **Top Global Matches:** file_cluster_5: 8.254, file_cluster_12: 10.297, file_cluster_4: 10.667
- **Magnitude:** 925.36 | **LOC:** 793 | **CtrlFlow:** 32.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **30** in-repo importer(s); it depends on **10**; blast radius 11.521; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.0%), Connectivity (formerly Api Exposure) (63.2%)
- **Documentation Coverage:** 29.2683% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 247.8)
  * `__str__` **(Compute Cores)** (Impact: 70.1)
    * *Intent:* """Re-generate style definition from attributes."""
  * `_make_ansi_codes` **(Stateful Encapsulated Methods)** (Impact: 28.1)
    * *Intent:* """Generate ANSI codes for this style. Args: color_system (ColorSystem): Color system. Returns: str:...
  * `get_html_style` **(Compute Cores)** (Impact: 24.3)
    * *Intent:* """Get a CSS style rule."""
  * `parse` **(Defensive Guards)** (Impact: 24.0)
    * *Intent:* """Parse a style definition. Args: style_definition (str): A string containing a style. Raises: erro...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 90 instances
* *State Mutation (weighted view):* 329
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 183`, `structural_boundaries: 116`, `args: 41`, `func_start: 41`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 149`
* *Architecture:* `io: 1`, `api: 36`, `import: 10`
* *Defense:* `safety: 9`, `doc: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.521
  * `Choke Point (Betweenness):` 0.001069 | `Ripple Effect (Closeness):` 0.175429
  * `Imports (Out-Degree: 4):` .color, .errors, .repr, .terminal_theme, functools, operator, pickle, random...
  * `Imported By (In-Degree: 30):` (Excluded from Brief to save tokens)

### `src/pip/_vendor/urllib3/packages/six.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.665)
- **Top Global Matches:** file_cluster_12: 6.665, file_cluster_15: 7.491, file_cluster_16: 8.088
- **Magnitude:** 804.9 | **LOC:** 1077 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **10**; blast radius 3.231; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.5%), Complexity Load (formerly Cognitive Load) (63.1%)
- **Documentation Coverage:** 75.8389% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `print_` **(Defensive Guards)** (Impact: 46.1)
    * *Intent:* """The new-style print function for Python 2.4 and 2.5."""
  * `__init__` **(Many-Argument Workhorses)** (Impact: 22.0)
  * `ensure_str` **(Defensive Guards)** (Impact: 15.1)
    * *Intent:* """Coerce *s* to `str`. For Python 2: - `unicode` -> encoded to `str` - `str` -> `str` For Python 3:...
  * `_update_wrapper` **(Stateful Encapsulated Methods)** (Impact: 9.8)
    * *Intent:* # This does exactly the same what the :func:`py3:functools.update_wrapper` # function does on Python...
  * `__new__` **(Compute Cores)** (Impact: 9.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 130 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 436
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 191`, `args: 70`, `func_start: 69`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 2`, `state_mutation: 176`, `fragile_debt: 1`
* *Architecture:* `io: 23`, `api: 59`, `import: 11`
* *Defense:* `safety: 40`, `doc: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.231
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.10515
  * `Imports (Out-Degree: 0):` StringIO, __future__, functools, importlib.util, io, itertools, operator, struct...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/pip/_vendor/urllib3/response.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 7.231)
- **Top Global Matches:** file_cluster_16: 7.231, file_cluster_12: 7.241, file_cluster_15: 7.717
- **Magnitude:** 756.98 | **LOC:** 880 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **14**; blast radius 0.866; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.6%), Debt Markers (formerly Tech Debt) (64.3%)
- **Documentation Coverage:** 67.0886% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 46.9)
  * `read` **(Many-Argument Workhorses)** (Impact: 34.9)
    * *Intent:* """ Similar to :meth:`http.client.HTTPResponse.read`, but with two additional parameters: ``decode_c...
  * `read_chunked` **(Many-Argument Workhorses)** (Impact: 33.5)
    * *Intent:* """ Similar to :meth:`HTTPResponse.read`, but with an additional parameter: ``decode_content``. :par...
  * `_fp_read` **(Stateful Encapsulated Methods)** (Impact: 30.1)
    * *Intent:* """ Read a response with the thought that reading the number of bytes larger than can fit in a 32-bi...
  * `_init_length` **(Stateful Encapsulated Methods)** (Impact: 23.3)
    * *Intent:* """ Set initial length value for Response content if available. """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 105 instances
* *State Mutation (weighted view):* 336
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 145`, `structural_boundaries: 149`, `args: 44`, `func_start: 44`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 126`, `fragile_debt: 4`, `duplicate_logic: 2`
* *Architecture:* `io: 3`, `api: 34`, `import: 15`
* *Defense:* `safety: 32`, `doc: 17`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.866
  * `Choke Point (Betweenness):` 6.3e-05 | `Ripple Effect (Closeness):` 0.092925
  * `Imports (Out-Degree: 6):` ._collections, .connection, .exceptions, .packages, .util, .util.response, __future__, contextlib...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/pip/_internal/index/package_finder.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.062)
- **Top Global Matches:** file_cluster_4: 9.062, file_cluster_5: 9.157, file_cluster_0: 9.237
- **Magnitude:** 748.76 | **LOC:** 1126 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 88.9%
- **Blast Radius:** changing it is visible to **18** in-repo importer(s); it depends on **34**; blast radius 3.164; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (69.2%), Complexity Load (formerly Cognitive Load) (58.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (54.6%)
- **Documentation Coverage:** 89.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `evaluate_link` **(Many-Argument Workhorses)** (Impact: 75.6)
    * *Intent:* """ Determine whether a link is a candidate for installation. :return: A tuple (result, detail), whe...
  * `find_requirement` **(Many-Argument Workhorses)** (Impact: 39.0)
  * `filter_unallowed_hashes` **(Many-Argument Workhorses)** (Impact: 29.6)
  * `find_all_candidates` **(Many-Argument Workhorses)** (Impact: 21.9)
    * *Intent:* """Find all available InstallationCandidate for project_name This checks index_urls and find_links. ...
  * `get_applicable_candidates` **(Many-Argument Workhorses)** (Impact: 19.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 92 instances
* *State Mutation (weighted view):* 324
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 187`, `args: 43`, `func_start: 43`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 140`
* *Architecture:* `api: 39`, `import: 35`
* *Defense:* `safety: 19`, `doc: 27`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.164
  * `Choke Point (Betweenness):` 0.017353 | `Ripple Effect (Closeness):` 0.134003
  * `Imports (Out-Degree: 21):` __future__, collections.abc, dataclasses, datetime, enum, functools, itertools, logging...
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `src/pip/_vendor/rich/traceback.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.833)
- **Top Global Matches:** file_cluster_4: 9.833, file_cluster_6: 11.567, file_cluster_5: 12.942
- **Magnitude:** 737.64 | **LOC:** 900 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **25**; blast radius 2.432; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.2%), Complexity Load (formerly Cognitive Load) (57.0%)
- **Documentation Coverage:** 90.2439% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `extract` **(Many-Argument Workhorses)** (Impact: 152.1)
  * `install` **(Many-Argument Workhorses)** (Impact: 56.8)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 54.6)
  * `_render_stack` **(Many-Argument Workhorses)** (Impact: 44.4)
  * `__rich_console__` **(Many-Argument Workhorses)** (Impact: 31.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 67 instances
* *State Mutation (weighted view):* 240
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 112`, `args: 21`, `func_start: 20`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 106`
* *Architecture:* `io: 15`, `api: 21`, `import: 28`
* *Defense:* `safety: 12`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.432
  * `Choke Point (Betweenness):` 0.001013 | `Ripple Effect (Closeness):` 0.1511
  * `Imports (Out-Degree: 13):` ._loop, .columns, .console, .constrain, .highlighter, .panel, .pretty, .scope...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/pip/_vendor/tomli/_parser.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.04)
- **Top Global Matches:** file_cluster_5: 8.04, file_cluster_12: 9.385, file_cluster_0: 11.383
- **Magnitude:** 730.84 | **LOC:** 778 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 1.177; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.9%), Complexity Load (formerly Cognitive Load) (62.3%)
- **Documentation Coverage:** 91.1765% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_value` **(Many-Argument Workhorses)** (Impact: 50.7)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 36.7)
  * `loads` **(Defensive Guards)** (Impact: 20.8)
    * *Intent:* """Parse TOML from a string."""
  * `parse_inline_table` **(Many-Argument Workhorses)** (Impact: 19.5)
  * `parse_basic_str` **(Defensive Guards)** (Impact: 19.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 101 instances
* *State Mutation (weighted view):* 317
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 136`, `args: 36`, `func_start: 36`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 115`
* *Architecture:* `io: 2`, `api: 37`, `import: 8`
* *Defense:* `safety: 48`, `doc: 7`, `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.177
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.001733
  * `Imports (Out-Degree: 2):` ._re, ._types, __future__, collections.abc, sys, types, typing, warnings
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/pip/_vendor/rich/syntax.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.633)
- **Top Global Matches:** file_cluster_4: 7.633, file_cluster_0: 10.22, file_cluster_12: 10.638
- **Magnitude:** 678.42 | **LOC:** 986 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **27**; blast radius 2.149; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.0%), Complexity Load (formerly Cognitive Load) (42.4%)
- **Documentation Coverage:** 44.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_get_syntax` **(Many-Argument Workhorses)** (Impact: 76.8)
  * `highlight` **(Many-Argument Workhorses)** (Impact: 46.2)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 17.9)
  * `_apply_stylized_ranges` **(Stateful Encapsulated Methods)** (Impact: 17.2)
    * *Intent:* """ Apply stylized ranges to a text instance, using the given code to determine the right portion to...
  * `guess_lexer` **(Defensive Guards)** (Impact: 16.0)
    * *Intent:* """Guess the alias of the Pygments lexer to use based on a path and an optional string of code. If c...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 99 instances
* *State Mutation (weighted view):* 327
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 133`, `args: 31`, `func_start: 31`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 129`, `duplicate_logic: 2`
* *Architecture:* `io: 5`, `api: 24`, `import: 28`
* *Defense:* `safety: 20`, `doc: 28`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.149
  * `Choke Point (Betweenness):` 0.000209 | `Ripple Effect (Closeness):` 0.132698
  * `Imports (Out-Degree: 11):` ._loop, .cells, .color, .console, .jupyter, .measure, .segment, .style...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/pip/_internal/resolution/resolvelib/factory.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.262)
- **Top Global Matches:** file_cluster_4: 8.262, file_cluster_6: 9.705, file_cluster_5: 13.61
- **Magnitude:** 666.42 | **LOC:** 857 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **29**; blast radius 1.165; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (67.4%), Guard Balance (formerly Safety Score) (66.5%)
- **Documentation Coverage:** 90.2439% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_installation_error` **(Many-Argument Workhorses)** (Impact: 61.9)
  * `find_candidates` **(Many-Argument Workhorses)** (Impact: 46.2)
  * `_iter_found_candidates` **(Many-Argument Workhorses)** (Impact: 44.7)
  * `_report_single_requirement_conflict` **(Many-Argument Workhorses)** (Impact: 41.1)
  * `_make_requirements_from_install_req` **(Many-Argument Workhorses)** (Impact: 34.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 75 instances
* *State Mutation (weighted view):* 242
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 156`, `args: 29`, `func_start: 27`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 92`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `api: 17`, `import: 29`
* *Defense:* `safety: 22`, `doc: 7`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.165
  * `Choke Point (Betweenness):` 0.002435 | `Ripple Effect (Closeness):` 0.082086
  * `Imports (Out-Degree: 19):` .base, .candidates, .found_candidates, .requirements, __future__, collections.abc, contextlib, functools...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/pip/_internal/req/req_install.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.24)
- **Top Global Matches:** file_cluster_0: 8.24, file_cluster_16: 9.168, file_cluster_12: 9.306
- **Magnitude:** 643.56 | **LOC:** 829 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **31** in-repo importer(s); it depends on **39**; blast radius 9.293; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (74.7%), Guard Balance (formerly Safety Score) (65.9%)
- **Documentation Coverage:** 68.3544% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 65.4)
  * `check_if_exists` **(Compute Cores)** (Impact: 22.6)
    * *Intent:* """Find an installed distribution that satisfies or conflicts with this requirement, and set self.sa...
  * `archive` **(Many-Argument Workhorses)** (Impact: 22.4)
    * *Intent:* """Saves archive to provided build_dir. Used for saving downloaded VCS requirements as part of `pip ...
  * `__str__` **(Defensive Guards)** (Impact: 18.1)
  * `ensure_build_location` **(Many-Argument Workhorses)** (Impact: 17.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 81 instances
* *State Mutation (weighted view):* 264
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 203`, `args: 40`, `func_start: 40`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 102`, `fragile_debt: 2`
* *Architecture:* `io: 19`, `api: 38`, `import: 40`
* *Defense:* `safety: 38`, `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.293
  * `Choke Point (Betweenness):` 0.037681 | `Ripple Effect (Closeness):` 0.171399
  * `Imports (Out-Degree: 22):` __future__, collections.abc, functools, logging, optparse, os, pathlib, pip._internal.build_env...
  * `Imported By (In-Degree: 31):` (Excluded from Brief to save tokens)

### `tests/functional/test_new_resolver.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.714)
- **Top Global Matches:** file_cluster_0: 7.714, file_cluster_16: 8.93, file_cluster_15: 8.932
- **Magnitude:** 617.42 | **LOC:** 2547 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.636; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (49.2%), Connectivity (formerly Api Exposure) (10.4%), Complexity Load (formerly Cognitive Load) (6.7%)
- **Documentation Coverage:** 98.6928% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_new_resolver_dont_backtrack_on_conflicting_constraints_on_extras` **(Many-Argument Workhorses)** (Impact: 19.9)
  * `test_new_resolver_presents_messages_when_backtracking_a_lot` **(Defensive Guards)** (Impact: 19.7)
  * `test_new_resolver_succeeds_on_matching_constraint_and_requirement` **(Many-Argument Workhorses)** (Impact: 12.3)
  * `test_new_resolver_dont_backtrack_on_extra_if_base_constrained_in_requirement` **(Many-Argument Workhorses)** (Impact: 11.7)
  * `test_new_resolver_lazy_fetch_candidates` **(Many-Argument Workhorses)** (Impact: 10.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 193
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 168`, `args: 79`, `func_start: 79`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 147`, `planned_debt: 1`, `fragile_debt: 2`, `unreferenced_by_name: 73`
* *Architecture:* `io: 25`, `api: 75`, `import: 10`
* *Defense:* `safety: 57`, `doc: 12`, `test: 112`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.636
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` os, pathlib, pytest, setuptools, sys, tests.conftest, tests.lib, tests.lib.venv...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/pip/_vendor/urllib3/connectionpool.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.217)
- **Top Global Matches:** file_cluster_12: 7.217, file_cluster_4: 7.599, file_cluster_16: 8.474
- **Magnitude:** 615.16 | **LOC:** 1141 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **25**; blast radius 1.18; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.2%), Complexity Load (formerly Cognitive Load) (45.0%)
- **Documentation Coverage:** 43.9024% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `urlopen` **(Many-Argument Workhorses)** (Impact: 158.4)
  * `_make_request` **(Many-Argument Workhorses)** (Impact: 28.6)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 25.6)
  * `_raise_timeout` **(Stateful Encapsulated Methods)** (Impact: 14.6)
    * *Intent:* """Is the error actually a timeout? Will raise a ReadTimeout or pass"""
  * `_get_conn` **(Stateful Encapsulated Methods)** (Impact: 14.0)
    * *Intent:* """ Get a connection. Will return a pooled connection if one is available. If no connections are ava...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 68 instances
* *State Mutation (weighted view):* 244
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 124`, `args: 27`, `func_start: 27`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 108`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 5`, `api: 11`, `import: 29`
* *Defense:* `safety: 37`, `doc: 21`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.18
  * `Choke Point (Betweenness):` 0.008594 | `Ripple Effect (Closeness):` 0.116041
  * `Imports (Out-Degree: 16):` ._collections, .connection, .exceptions, .packages, .packages.backports.weakref_finalize, .packages.six.moves, .request, .response...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/pip/_vendor/rich/segment.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.061)
- **Top Global Matches:** file_cluster_0: 8.061, file_cluster_5: 8.485, file_cluster_12: 9.118
- **Magnitude:** 600.68 | **LOC:** 753 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **21** in-repo importer(s); it depends on **13**; blast radius 8.221; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (77.5%), Guard Balance (formerly Safety Score) (74.5%)
- **Documentation Coverage:** 46.9388% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `divide` **(Many-Argument Workhorses)** (Impact: 33.4)
  * `adjust_line_length` **(Many-Argument Workhorses)** (Impact: 29.1)
  * `split_and_crop_lines` **(Many-Argument Workhorses)** (Impact: 28.7)
  * `apply_style` **(Many-Argument Workhorses)** (Impact: 26.5)
  * `_split_cells` **(Many-Argument Workhorses)** (Impact: 22.3)
    * *Intent:* """Split a segment in to two at a given cell position. Note that splitting a double-width character,...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 76 instances
* *State Mutation (weighted view):* 253
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 94`, `args: 27`, `func_start: 27`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 101`
* *Architecture:* `api: 26`, `import: 13`
* *Defense:* `safety: 3`, `doc: 27`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.221
  * `Choke Point (Betweenness):` 0.001358 | `Ripple Effect (Closeness):` 0.172222
  * `Imports (Out-Degree: 6):` .cells, .console, .repr, .style, enum, functools, itertools, logging...
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `src/pip/_internal/operations/install/wheel.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.231)
- **Top Global Matches:** file_cluster_5: 8.231, file_cluster_12: 10.39, file_cluster_4: 11.121
- **Magnitude:** 600.3 | **LOC:** 746 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **31**; blast radius 1.037; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.6%), Complexity Load (formerly Cognitive Load) (73.8%)
- **Documentation Coverage:** 81.25% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_install_wheel` **(Many-Argument Workhorses)** (Impact: 92.3)
  * `message_about_scripts_not_on_PATH` **(Compute Cores)** (Impact: 29.0)
    * *Intent:* """Determine if any scripts are not on PATH and format a warning. Returns a warning message if one o...
  * `get_csv_rows_for_installed` **(Many-Argument Workhorses)** (Impact: 28.4)
  * `get_console_script_specs` **(Compute Cores)** (Impact: 23.4)
    * *Intent:* """ Given the mapping from entrypoint name to callable, return the relevant console script specs. ""...
  * `is_entrypoint_wrapper` **(Compute Cores)** (Impact: 9.2)
    * *Intent:* # EP, EP.exe and EP-script.py are scripts generated for # entry point EP by setuptools path = file.d...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 78 instances
* *State Mutation (weighted view):* 280
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 151`, `args: 36`, `func_start: 36`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 124`, `fragile_debt: 2`
* *Architecture:* `io: 49`, `api: 31`, `import: 31`
* *Defense:* `safety: 8`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.037
  * `Choke Point (Betweenness):` 0.00057 | `Ripple Effect (Closeness):` 0.122544
  * `Imports (Out-Degree: 10):` __future__, base64, collections, collections.abc, compileall, contextlib, csv, email.message...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/pip/_internal/exceptions.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.933)
- **Top Global Matches:** file_cluster_0: 6.933, file_cluster_12: 7.973, file_cluster_5: 8.011
- **Magnitude:** 582.66 | **LOC:** 972 | **CtrlFlow:** 14.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **81** in-repo importer(s); it depends on **26**; blast radius 32.556; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (98.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.1%)
- **Documentation Coverage:** 90.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__rich_console__` **(Many-Argument Workhorses)** (Impact: 28.9)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 26.5)
  * `__init__` **(Compute Cores)** (Impact: 16.9)
  * `__init__` **(Compute Cores)** (Impact: 11.5)
  * `__init__` **(Compute Cores)** (Impact: 11.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 69 instances
* *State Mutation (weighted view):* 244
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 187`, `args: 52`, `func_start: 50`, `class_start: 42`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 106`, `planned_debt: 1`
* *Architecture:* `io: 3`, `api: 51`, `import: 26`
* *Defense:* `safety: 14`, `doc: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 32.556
  * `Choke Point (Betweenness):` 0.074523 | `Ripple Effect (Closeness):` 0.217225
  * `Imports (Out-Degree: 10):` __future__, collections.abc, configparser, contextlib, hashlib, itertools, locale, logging...
  * `Imported By (In-Degree: 81):` (Excluded from Brief to save tokens)

### `tests/unit/test_req_file.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.974)
- **Top Global Matches:** file_cluster_0: 7.974, file_cluster_5: 8.747, file_cluster_12: 9.065
- **Magnitude:** 507.34 | **LOC:** 1083 | **CtrlFlow:** 2.5% | **Authorship Centralization:** 40.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **21**; blast radius 0.636; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (63.5%), Guard Balance (formerly Safety Score) (40.5%), Connectivity (formerly Api Exposure) (12.8%), Complexity Load (formerly Cognitive Load) (11.0%)
- **Documentation Coverage:** 93.9394% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `process_line` **(Many-Argument Workhorses)** (Impact: 12.7)
  * `parse_reqfile` **(Many-Argument Workhorses)** (Impact: 11.9)
  * `test_recursive_requirements_file` **(Type Conversions)** (Impact: 11.8)
  * `test_relative_local_find_links` **(Many-Argument Workhorses)** (Impact: 8.8)
  * `line_processor` **(Generic / Templated Code)** (Impact: 8.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 139
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 289`, `args: 82`, `func_start: 81`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 117`, `unreferenced_by_name: 68`
* *Architecture:* `io: 24`, `api: 88`, `import: 22`
* *Defense:* `safety: 105`, `doc: 24`, `test: 117`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.636
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` __future__, codecs, collections, collections.abc, logging, optparse, os, pathlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/pip/_internal/req/req_uninstall.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.934)
- **Top Global Matches:** file_cluster_5: 7.934, file_cluster_12: 9.876, file_cluster_4: 11.7
- **Magnitude:** 505.66 | **LOC:** 640 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **17**; blast radius 1.389; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.4%), Complexity Load (formerly Cognitive Load) (45.4%)
- **Documentation Coverage:** 52.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `from_dist` **(Many-Argument Workhorses)** (Impact: 66.6)
  * `compress_for_output_listing` **(Type Conversions)** (Impact: 19.3)
    * *Intent:* """Returns a tuple of 2 sets of which paths to display to user The first set contains paths that wou...
  * `compress_for_rename` **(Type Conversions)** (Impact: 15.7)
    * *Intent:* """Returns a set containing the paths that need to be renamed. This set may include directories when...
  * `remove` **(Many-Argument Workhorses)** (Impact: 15.4)
    * *Intent:* """Remove paths in ``self._paths`` with confirmation (unless ``auto_confirm`` is True)."""
  * `remove` **(Stateful Encapsulated Methods)** (Impact: 12.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 63 instances
* *State Mutation (weighted view):* 203
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 115`, `args: 30`, `func_start: 30`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 77`, `fragile_debt: 2`
* *Architecture:* `io: 62`, `api: 23`, `import: 17`
* *Defense:* `safety: 13`, `doc: 17`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.389
  * `Choke Point (Betweenness):` 0.001084 | `Ripple Effect (Closeness):` 0.123423
  * `Imports (Out-Degree: 10):` __future__, collections.abc, functools, importlib.util, os, pip._internal.exceptions, pip._internal.locations, pip._internal.metadata...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/pip/_internal/commands/install.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 11.639)
- **Top Global Matches:** file_cluster_8: 11.639, file_cluster_3: 13.86, file_cluster_6: 23.829
- **Magnitude:** 504.48 | **LOC:** 811 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 57.1%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **33**; blast radius 1.269; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.4%), Complexity Load (formerly Cognitive Load) (53.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run` **(Many-Argument Workhorses)** (Impact: 79.3)
  * `_handle_target_dir` **(Many-Argument Workhorses)** (Impact: 40.7)
  * `decide_user_install` **(Many-Argument Workhorses)** (Impact: 37.6)
  * `create_os_error_message` **(Many-Argument Workhorses)** (Impact: 37.3)
  * `add_options` **(I/O & Config Routines)** (Impact: 32.3)
    * *Intent:* %prog [options] <requirement specifier> [package-index-options] ... %prog [options] -r <requirements...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 63 instances
* *State Mutation (weighted view):* 208
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 108`, `args: 10`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 82`
* *Architecture:* `io: 17`, `api: 8`, `import: 33`
* *Defense:* `safety: 8`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.269
  * `Choke Point (Betweenness):` 0.014032 | `Ripple Effect (Closeness):` 0.0995
  * `Imports (Out-Degree: 23):` __future__, errno, json, operator, optparse, os, pathlib, pip._internal.cache...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tests/functional/test_pep660.py` (PYTHON) | Magnitude: 70.02 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 120, structural_boundaries: 33, core_var_decl: 26, state_mutation: 24
- `tests/unit/test_vcs_mercurial.py` (PYTHON) | Magnitude: 9.84 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 14, indent_spaces: 14, io: 6, state_mutation: 6
- `tests/unit/test_req_uninstall.py` (PYTHON) | Magnitude: 226.38 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 328, structural_boundaries: 89, io: 69, state_mutation: 57
- `src/pip/_vendor/rich/box.py` (PYTHON) | Magnitude: 160.68 | Delta: **0.112** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 307, core_var_decl: 57, state_mutation: 38, structural_boundaries: 35
- `tests/functional/test_config_settings.py` (PYTHON) | Magnitude: 81.02 | Delta: **0.115** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 172, structural_boundaries: 75, core_var_decl: 54, design_snake_case: 49

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/pip/_vendor/tomli/_re.py` (PYTHON) | Magnitude: 62.04 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 47, structural_boundaries: 21, branch: 20, core_var_decl: 19
- `src/pip/_vendor/truststore/_windows.py` (PYTHON) | Magnitude: 290.76 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 345, state_mutation: 139, core_var_decl: 102, design_upper_case: 39
- `src/pip/__pip-runner__.py` (PYTHON) | Magnitude: 19.2 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 15, indent_spaces: 13, core_var_decl: 5, io: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tests/functional/test_install_cleanup.py` (PYTHON) | Magnitude: 5.22 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 7, test: 4, import: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `tests/functional/test_new_resolver_errors.py` (PYTHON) | Magnitude: 44.78 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 136, core_var_decl: 47, design_snake_case: 47, structural_boundaries: 21
- `tests/functional/test_lock.py` (PYTHON) | Magnitude: 46.08 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 191, structural_boundaries: 23, core_var_decl: 22, design_snake_case: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/pip/_vendor/urllib3/response.py` (PYTHON) | Magnitude: 756.98 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 509, structural_boundaries: 149, branch: 145, state_mutation: 126
- `src/pip/_vendor/urllib3/contrib/pyopenssl.py` (PYTHON) | Magnitude: 3.22 | Delta: **0.114** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 277, structural_boundaries: 121, branch: 62, state_mutation: 59

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/pip/_internal/index/package_finder.py` (PYTHON) | Magnitude: 748.76 | Delta: **0.095** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 683, core_var_decl: 188, structural_boundaries: 187, design_snake_case: 165
- `src/pip/_vendor/rich/progress_bar.py` (PYTHON) | Magnitude: 255.64 | Delta: **0.136** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 148, state_mutation: 51, core_var_decl: 49, branch: 46

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `src/pip/_internal/commands/debug.py` (PYTHON) | Magnitude: 176.06 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 112, structural_boundaries: 66, state_mutation: 36, core_var_decl: 33
- `src/pip/_vendor/rich/_windows.py` (PYTHON) | Magnitude: 47.16 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 40, structural_boundaries: 16, core_var_decl: 16, design_snake_case: 16
- `tests/unit/test_search_scope.py` (PYTHON) | Magnitude: 15.24 | Delta: **0.055** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 17, core_var_decl: 13, design_snake_case: 13
- `src/pip/_internal/vcs/git.py` (PYTHON) | Magnitude: 384.12 | Delta: **0.074** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 350, core_var_decl: 116, design_snake_case: 112, structural_boundaries: 83
- `tools/update-rtd-redirects.py` (PYTHON) | Magnitude: 0.07 | Delta: **0.098** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 67, structural_boundaries: 30, core_var_decl: 26, state_mutation: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `src/pip/_internal/locations/_sysconfig.py` (PYTHON) | Magnitude: 168.96 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 97, structural_boundaries: 43, branch: 39, core_var_decl: 34

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/pip/_vendor/rich/screen.py` (PYTHON) | Magnitude: 44.38 | Delta: **0.139** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 16, state_mutation: 9, branch: 8

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `noxfile.py` -> Churn: **69.86%** | Cog Load: 51.0619% | Debt: 78.8108%
- `src/pip/_internal/index/package_finder.py` -> Churn: **54.58%** | Cog Load: 58.6881% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/pip/_internal/index/package_finder.py` -> **Damian Shaw** (88.9% isolated ownership) | Magnitude: 748.76
- `src/pip/_internal/resolution/resolvelib/factory.py` -> **Damian Shaw** (100.0% isolated ownership) | Magnitude: 666.42
- `src/pip/_internal/operations/install/wheel.py` -> **Aarni Koskela** (100.0% isolated ownership) | Magnitude: 600.3
- `src/pip/_internal/exceptions.py` -> **Richard Si** (100.0% isolated ownership) | Magnitude: 582.66
- `src/pip/_internal/operations/prepare.py` -> **Richard Si** (100.0% isolated ownership) | Magnitude: 478.88

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/pip/_internal/exceptions.py` -> **Severity: 7.452** (Bridge: 0.0745 * Flux: 99.9999%)
- `src/pip/_internal/req/req_install.py` -> **Severity: 3.768** (Bridge: 0.0377 * Flux: 100.0%)
- `src/pip/_vendor/rich/console.py` -> **Severity: 3.638** (Bridge: 0.0364 * Flux: 100.0%)
- `src/pip/_internal/build_env.py` -> **Severity: 3.47** (Bridge: 0.0347 * Flux: 100.0%)
- `src/pip/_internal/utils/misc.py` -> **Severity: 1.776** (Bridge: 0.0178 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/pip/_vendor/rich/text.py` -> **Severity: 16.092** (Embedded: 0.202 * Error Risk: 79.6716%)
- `src/pip/_vendor/rich/console.py` -> **Severity: 15.449** (Embedded: 0.2107 * Error Risk: 73.3085%)
- `src/pip/_internal/utils/misc.py` -> **Severity: 15.092** (Embedded: 0.2136 * Error Risk: 70.6484%)
- `src/pip/_internal/exceptions.py` -> **Severity: 14.57** (Embedded: 0.2172 * Error Risk: 67.074%)
- `src/pip/_vendor/rich/markup.py` -> **Severity: 14.284** (Embedded: 0.1948 * Error Risk: 73.3081%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/pip/_internal/exceptions.py` -> **Severity: 2930.04** (Blast Radius: 32.556 * Doc Risk: 90.0%)
- `tests/lib/__init__.py` -> **Severity: 2146.403** (Blast Radius: 22.139 * Doc Risk: 96.9512%)
- `src/pip/_vendor/rich/console.py` -> **Severity: 1665.918** (Blast Radius: 36.154 * Doc Risk: 46.0784%)
- `src/pip/_internal/utils/misc.py` -> **Severity: 1511.215** (Blast Radius: 29.712 * Doc Risk: 50.8621%)
- `src/pip/_internal/utils/compat.py` -> **Severity: 1422.201** (Blast Radius: 21.333 * Doc Risk: 66.6667%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 272 literal sites + 1 sites through wrappers = 273
- **`panics_and_aborts`:** 756 literal sites + 5 sites through wrappers = 761

- `read_wheel_metadata_file` (function, panics_and_aborts, primitive): 3 call sites in 3 files -- `src/pip/_internal/utils/wheel.py`
- `bar` (function, debug_prints, primitive): 1 call sites in 1 files -- `src/pip/_vendor/rich/traceback.py`
- `raise_from` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `src/pip/_vendor/urllib3/packages/six.py`
- `req_error_context` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `src/pip/_internal/operations/install/wheel.py`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 19270 call pairs -- scoped 40.9%, unique 0.0%, ambiguous 16.3%, external 42.9%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 19270 | 40.9% | 0.0% | 16.3% | 42.9% |

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
