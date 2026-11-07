# ARCHITECTURAL_BRIEF: sentry
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/getsentry/sentry.git` |
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
- **Scope:** 17858 analyzed artifact(s), 2464932 LOC.
- **Load-bearing artifact:** `src/sentry/testutils/cases.py` -- 1804 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/sentry/api/urls.py` -- pulls in 475 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `.npmrc` at magnitude 5000.0 (structural weight, not risk).
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
| Total Artifacts | 20173 |
| Analyzed Artifacts (Scanned) | 17858 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2315 |
| Total LOC | 2464932 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 88.5% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5589 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1084 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 8.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | n/a (not computed) | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 1084 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 8762 | 1164418 | 49.1% |
| PYTHON | 7608 | 1187698 | 42.6% |
| JSON | 683 | 90347 | 3.8% |
| XML | 216 | 566 | 1.2% |
| HTML | 183 | 8387 | 1.0% |
| PLAINTEXT | 154 | 3 | 0.9% |
| MARKDOWN | 104 | 0 | 0.6% |
| YAML | 51 | 3738 | 0.3% |
| CSS | 37 | 5940 | 0.2% |
| JAVASCRIPT | 35 | 1499 | 0.2% |
| LUA | 12 | 1747 | 0.1% |
| SHELL | 11 | 312 | 0.1% |
| MAKEFILE | 1 | 202 | 0.0% |
| DOCKERFILE | 1 | 75 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 17855 |
| unknown | unknown | 3 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Generic / Templated Code Files 22%, Large Core Modules (2) 18%, Data / Markup / Trivial 17%, Declarative / Non-Code 15%, Callbacks & Closures Files 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 17467 | 97.8% |
| Unknown | 3 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 255 | 1.4% |
| Static: Minified & Vendor Opaque Mass | 133 | 0.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2315*

**Composition by Extension & Reason:**
- `.pysnap`: 1524x Excluded (Unsupported Extension: '.pysnap')
- `.py`: 259x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 5 exceeds 500 chars), 1x Excluded (Saturation: Line 88 exceeds 500 chars)
- `.tsx`: 79x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Machine-Generated Source Code Signature: 1895 LOC), 1x Excluded (Machine-Generated Source Code Signature: 35 LOC)
- `.png`: 76x Excluded (Explicitly Denied Extension: '.png')
- `.md`: 69x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mo`: 44x Excluded (Binary Format Detected), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.po`: 44x Unsupported Format (.po), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 19x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable), 3x Excluded (Binary Format Detected)
- `.json`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 1478 LOC), 1x Excluded (Static Asset Blob without Intent: 1142 LOC)
- `.js`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.woff2`: 15x Excluded (Explicitly Denied Extension: '.woff2')
- `.map`: 12x Excluded (Saturation: Line 1 exceeds 500 chars), 2x Unresolved Ambiguity (No Retainable Structure)
- `.ts`: 4x Unsupported Format (.undeterminable), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 432 LOC)
- `.jpg`: 9x Excluded (Explicitly Denied Extension: '.jpg')
- `.pegjs`: 8x Excluded (Unsupported Extension: '.pegjs'), 1x Excluded (Saturation: Line 14 exceeds 500 chars)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 12.3 | 5.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.4 | 31.6 | 45.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 8.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 5.5 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 18.0 | 7.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 8.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 25.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.0 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.3 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 5.6 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 61.6 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.4 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 17863 | 4525 | 2 | `tests/snuba/search/test_backend.py` |
| cleanup | 498 | 263 | 0 | `static/app/views/navigation/useCollapsedNavigation.tsx` |
| guards | 121344 | 9155 | 15 | `tests/snuba/api/endpoints/test_organization_events.py` |
| danger | 35290 | 6403 | 5 | `tests/sentry/scm/test_fixtures.py` |
| concurrency | 29295 | 2945 | 3 | `static/app/components/searchQueryBuilder/index.spec.tsx` |
| connectivity | 85477 | 13644 | 12 | `src/sentry/testutils/cases.py` |
| io | 12064 | 3025 | 1 | `static/gsApp/components/features/illustrations/performanceBackground.tsx` |
| crypto | 183 | 135 | 0 | `src/sentry/backup/crypto.py` |
| ipc | 139 | 56 | 0 | `src/sentry/preprod/snapshots/image_diff/odiff.py` |
| time | 8406 | 1400 | 0 | `tests/sentry/replays/endpoints/test_organization_replay_index.py` |
| serialization | 560 | 241 | 0 | `static/app/utils/profiling/renderers/flamegraphRendererWebGL.spec.tsx` |
| regex | 1350 | 605 | 0 | `static/app/data/controlsiloUrlPatterns.ts` |
| events | 7489 | 2230 | 1 | `tests/sentry/workflow_engine/processors/test_detector.py` |
| tests | 105229 | 4454 | 17 | `static/app/components/searchQueryBuilder/index.spec.tsx` |
| docs | 20296 | 4670 | 3 | `static/less/includes/bootstrap/variables.less` |
| debt | 5254 | 2165 | 1 | `eslint.config.ts` |
| mutation | 670967 | 14929 | 86 | `tests/snuba/api/endpoints/test_organization_events.py` |
| dead_code | 30085 | 5712 | 4 | `tests/sentry/dashboards/endpoints/test_organization_dashboard_details.py` |
| credential | 871 | 252 | 0 | `fixtures/vsts.py` |
| threat | 61 | 42 | 0 | `src/sentry_plugins/anonymizeip.py` |
| ml_ai | 1329 | 469 | 0 | `static/app/views/seerExplorer/hooks/useAsciiSnapshot.tsx` |
| ui | 66531 | 5951 | 11 | `static/app/components/searchQueryBuilder/index.spec.tsx` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.2**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `static/gsApp/components/features/illustrations/performanceBackground.tsx` (Hits: 492)
- `static/app/router/routes.tsx` (Hits: 420)
- `static/app/components/illustrations/NoProjectEmptyState.tsx` (Hits: 282)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **cases.py** (`src/sentry/testutils/cases.py`) — 1804 inbound connections
2. **reactTestingLibrary.tsx** (`tests/js/sentry-test/reactTestingLibrary.tsx`) — 1498 inbound connections
3. **__init__.py** (`src/sentry/__init__.py`) — 1085 inbound connections
4. **__init__.py** (`src/sentry/utils/__init__.py`) — 744 inbound connections
5. **silo.py** (`src/sentry/testutils/silo.py`) — 717 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **urls.py** (`src/sentry/api/urls.py`) — 475 outbound dependencies
2. **routes.tsx** (`static/app/router/routes.tsx`) — 310 outbound dependencies
3. **index.tsx** (`static/app/icons/index.tsx`) — 149 outbound dependencies
4. **factories.py** (`src/sentry/testutils/factories.py`) — 148 outbound dependencies
5. **cases.py** (`src/sentry/testutils/cases.py`) — 137 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `ReleaseComparisonChart` **(Many-Argument Workhorses)** (@ `static/app/views/releases/detail/overview/releaseComparisonChart/index.tsx`) -> Impact: **378.9** | LOC: 1044
- `put` **(Many-Argument Workhorses)** (@ `src/sentry/core/endpoints/project_details.py`) -> Impact: **357.6** | LOC: 511
  * *Intent:* """ Update various attributes and configurable settings for the given project. Note that solely having the **`project:read`** scope restricts updatabl...
- `update_alert_rule` **(Many-Argument Workhorses)** (@ `src/sentry/incidents/logic.py`) -> Impact: **353.8** | LOC: 266
- `devserver` **(Many-Argument Workhorses)** (@ `src/sentry/runner/commands/devserver.py`) -> Impact: **314.9** | LOC: 359
- `Visualize` **(Defensive Guards)** (@ `static/app/views/dashboards/widgetBuilder/components/visualize/index.tsx`) -> Impact: **298.6** | LOC: 880
- `getGroupActivityItem` **(Many-Argument Workhorses)** (@ `static/app/views/issueDetails/streamline/sidebar/groupActivityItem.tsx`) -> Impact: **291.4** | LOC: 685
- `useWidgetBuilderState` **(I/O & Config Routines)** (@ `static/app/views/dashboards/widgetBuilder/hooks/useWidgetBuilderState.tsx`) -> Impact: **284.8** | LOC: 915
- `Flamegraph` **(I/O & Config Routines)** (@ `static/app/components/profiling/flamegraph/flamegraph.tsx`) -> Impact: **270.5** | LOC: 1350
- `ContinuousFlamegraph` **(I/O & Config Routines)** (@ `static/app/components/profiling/flamegraph/continuousFlamegraph.tsx`) -> Impact: **268.1** | LOC: 1361
- `query` **(Many-Argument Workhorses)** (@ `src/sentry/search/snuba/executors.py`) -> Impact: **235.6** | LOC: 299

*Function archetypes referenced above:*
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `tests/snuba/api/endpoints` | 67 | 22344.92 | 12.12% | 0.0% |
| `src/sentry/api/endpoints` | 156 | 19012.04 | 39.65% | 2.44% |
| `tests/sentry/api/endpoints` | 145 | 13672.9 | 8.87% | 0.0% |
| `src/sentry/utils` | 98 | 12137.68 | 41.13% | 5.79% |
| `src/sentry/models` | 122 | 12018.8 | 33.34% | 5.99% |
| `static/app/components` | 222 | 8589.1 | 7.42% | 16.68% |
| `src/sentry/api/serializers/models` | 58 | 8567.54 | 41.93% | 9.14% |
| `src/sentry/snuba` | 35 | 8392.02 | 32.92% | 10.66% |
| `static/app/utils` | 263 | 7960.34 | 8.54% | 28.5% |
| `src/sentry/testutils` | 15 | 7843.52 | 45.71% | 20.08% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/sentry/db/models/fields/bounded.py` -> **100.0%** Exposure
- `src/sentry/integrations/services/github_copilot_identity/service.py` -> **100.0%** Exposure
- `src/sentry/relocation/services/relocation_export/service.py` -> **100.0%** Exposure
- `src/sentry/seer/entrypoints/types.py` -> **100.0%** Exposure
- `src/sentry/workflow_engine/utils/log_context.py` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `.github/workflows/scripts/compute-sentry-selected-tests.py` -> **100.0%** Exposure
- `.github/workflows/scripts/selective-testing/compute-selected-tests.py` -> **100.0%** Exposure
- `bin/benchmark_detectors` -> **100.0%** Exposure
- `bin/dump-command-help` -> **100.0%** Exposure
- `bin/find-good-catalogs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/sentry/integrations/github/test_platform_detection.py` -> **161** Orphaned Functions | **9** Duplicates
- `tests/sentry/dashboards/endpoints/test_organization_dashboard_details.py` -> **161** Orphaned Functions | **2** Duplicates
- `tests/sentry/core/endpoints/test_organization_details.py` -> **144** Orphaned Functions | **2** Duplicates
- `tests/sentry/issues/endpoints/test_organization_group_index.py` -> **134** Orphaned Functions | **2** Duplicates
- `tests/sentry/tasks/test_post_process.py` -> **111** Orphaned Functions | **15** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `src/sentry/data/samples/expectct.json` -> **100.0%** Exposure
- `src/sentry/data/samples/hpkp.json` -> **100.0%** Exposure
- `tests/sentry/grouping/grouping_inputs/expectct.json` -> **100.0%** Exposure
- `tests/sentry/grouping/grouping_inputs/hpkp.json` -> **100.0%** Exposure
- `fixtures/github.py` -> **100.0%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `78` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `131296` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `api-docs/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/sentry/testutils/pytest/template/credentials.json` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/sentry/testutils/cases.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.727)
- **Top Global Matches:** file_cluster_12: 6.727, file_cluster_5: 7.986, file_cluster_4: 9.201
- **Magnitude:** 3556.38 | **LOC:** 4265 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 20.0%
- **Blast Radius:** changing it is visible to **1804** in-repo importer(s); it depends on **137**; blast radius 9.688; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (82.9%), Guard Balance (formerly Safety Score) (68.2%)
- **Documentation Coverage:** 92.0097% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create_eap_uptime_result` **(Many-Argument Workhorses)** (Impact: 106.2)
  * `store_segment` **(Many-Argument Workhorses)** (Impact: 75.3)
  * `login_as` **(Many-Argument Workhorses)** (Impact: 67.0)
    * *Intent:* # TODO(dcramer): ideally superuser_sso would be False by default, but that would require # a lot of ...
  * `store_indexed_span` **(Many-Argument Workhorses)** (Impact: 64.5)
  * `create_processing_error` **(Many-Argument Workhorses)** (Impact: 55.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 409 instances
* *Concurrency (weighted view):* 25
* *State Mutation (weighted view):* 1420
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 415`, `structural_boundaries: 863`, `args: 202`, `func_start: 202`, `class_start: 61`
* *Risk/State:* `safety_bypasses: 75`, `state_mutation: 602`, `planned_debt: 17`, `fragile_debt: 8`, `duplicate_logic: 6`
* *Architecture:* `io: 21`, `api: 254`, `concurrency: 5`, `import: 156`
* *Defense:* `safety: 124`, `doc: 26`, `test: 67`, `sync_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 9.688
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 97):` ..shared_integrations.client.proxy, ..snuba.metrics, ..snuba.metrics.naming_layer.mri, ..types.cell, .asserts, .factories, .fixtures, .helpers...
  * `Imported By (In-Degree: 1804):` (Excluded from Brief to save tokens)

### `tests/snuba/api/endpoints/test_organization_events.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.805)
- **Top Global Matches:** file_cluster_15: 7.805, file_cluster_0: 7.893, file_cluster_16: 8.565
- **Magnitude:** 2923.72 | **LOC:** 7447 | **CtrlFlow:** 2.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **23** in-repo importer(s); it depends on **28**; blast radius 0.232; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (98.8%), Guard Balance (formerly Safety Score) (44.7%), Complexity Load (formerly Cognitive Load) (22.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (20.9%)
- **Documentation Coverage:** 94.4186% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_functions_dataset_simple` **(I/O & Config Routines)** (Impact: 25.5)
  * `run_test_in_query` **(Defensive Guards)** (Impact: 15.6)
  * `test_profiles_dataset_simple` **(Many-Argument Workhorses)** (Impact: 15.2)
  * `test_count_if` **(Defensive Guards)** (Impact: 13.1)
  * `test_semver` **(Defensive Guards)** (Impact: 12.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 192 instances
* *State Mutation (weighted view):* 1628
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 180`, `structural_boundaries: 1535`, `args: 218`, `func_start: 216`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 1244`, `planned_debt: 2`, `fragile_debt: 4`, `duplicate_logic: 4`
* *Architecture:* `io: 2`, `api: 228`, `import: 28`
* *Defense:* `safety: 1065`, `doc: 13`, `test: 221`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.232
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 19):` datetime, django.test, django.urls, django.utils, math, pytest, sentry.discover.models, sentry.issues.grouptype...
  * `Imported By (In-Degree: 23):` (Excluded from Brief to save tokens)

### `tests/sentry/integrations/github/test_platform_detection.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.317)
- **Top Global Matches:** file_cluster_0: 8.317, file_cluster_15: 9.551, file_cluster_12: 9.751
- **Magnitude:** 2352.08 | **LOC:** 2335 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (61.5%), Complexity Load (formerly Cognitive Load) (27.7%), Connectivity (formerly Api Exposure) (14.1%)
- **Documentation Coverage:** 93.6264% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_full_stack_repo_only_detects_top_language` **(Defensive Guards)** (Impact: 18.9)
    * *Intent:* """In a multi-language repo, only the top language's platform is processed. Only one suggestion is s...
  * `test_framework_sort_determines_ranking` **(Defensive Guards)** (Impact: 11.2)
  * `test_framework_detection_gives_high_confidence` **(Defensive Guards)** (Impact: 10.9)
  * `test_no_rule_has_match_content_without_file_source` **(Defensive Guards)** (Impact: 8.9)
  * `test_cloudflare_pages_supersedes_workers` **(Defensive Guards)** (Impact: 8.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 288 instances
* *State Mutation (weighted view):* 1063
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 240`, `structural_boundaries: 727`, `args: 228`, `func_start: 228`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 487`, `duplicate_logic: 9`, `unreferenced_by_name: 161`
* *Architecture:* `io: 2`, `api: 240`, `import: 8`
* *Defense:* `safety: 247`, `doc: 22`, `test: 168`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 3):` __future__, base64, collections, pytest, sentry.integrations.github.platform_detection, sentry.shared_integrations.exceptions, sentry.utils, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/sentry/testutils/factories.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.134)
- **Top Global Matches:** file_cluster_12: 7.134, file_cluster_5: 7.867, file_cluster_15: 9.199
- **Magnitude:** 2059.64 | **LOC:** 2808 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **76** in-repo importer(s); it depends on **148**; blast radius 0.477; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.8%)
- **Documentation Coverage:** 99.6269% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create_service_hook` **(Many-Argument Workhorses)** (Impact: 44.3)
  * `create_preprod_artifact_size_metrics` **(Many-Argument Workhorses)** (Impact: 40.5)
  * `create_release` **(Many-Argument Workhorses)** (Impact: 40.0)
  * `create_project_rule` **(Many-Argument Workhorses)** (Impact: 30.8)
  * `create_incident` **(Many-Argument Workhorses)** (Impact: 29.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 230 instances
* *State Mutation (weighted view):* 761
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 296`, `structural_boundaries: 656`, `args: 136`, `func_start: 136`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 301`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 13`, `api: 134`, `import: 155`
* *Defense:* `safety: 18`, `doc: 3`, `test: 2`, `sync_locks: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.477
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 119):` __future__, base64, binascii, collections.abc, contextlib, copy, datetime, django.conf...
  * `Imported By (In-Degree: 76):` (Excluded from Brief to save tokens)

### `src/sentry/search/events/builder/metrics.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 10.367)
- **Top Global Matches:** file_cluster_6: 10.367, file_cluster_4: 12.186, file_cluster_5: 16.365
- **Magnitude:** 1975.6 | **LOC:** 1920 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **35**; blast radius 0.053; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (79.8%), Complexity Load (formerly Cognitive Load) (72.1%), Connectivity (formerly Api Exposure) (53.2%)
- **Documentation Coverage:** 62.037% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run_query` **(Many-Argument Workhorses)** (Impact: 124.4)
  * `resolve_snql_function` **(Many-Argument Workhorses)** (Impact: 61.2)
  * `_get_metrics_query_from_on_demand_spec` **(Many-Argument Workhorses)** (Impact: 57.6)
  * `default_filter_converter` **(Many-Argument Workhorses)** (Impact: 53.9)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 48.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 276 instances
* *State Mutation (weighted view):* 865
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 425`, `structural_boundaries: 293`, `args: 62`, `func_start: 62`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 78`, `state_mutation: 313`, `planned_debt: 6`, `duplicate_logic: 3`
* *Architecture:* `api: 50`, `import: 37`
* *Defense:* `safety: 31`, `doc: 23`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 28):` __future__, collections, collections.abc, datetime, django.utils.functional, sentry, sentry.api.event_search, sentry.exceptions...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `static/app/views/dashboards/widgets/tableWidget/tableWidgetVisualization.stories.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 5.459)
- **Top Global Matches:** file_cluster_0: 5.459, file_cluster_10: 7.332, file_cluster_2: 7.674
- **Magnitude:** 1958.5 | **LOC:** 520 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.025; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (42.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (17.6%), Mutation Surface (formerly State Flux) (10.6%), Complexity Load (formerly Cognitive Load) (6.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 81`, `args: 31`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2`
* *Architecture:* `io: 7`, `api: 1`, `import: 14`
* *Defense:* `safety: 41`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` styled, badge, button, code, react, stories, eventView, fieldRenderers...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `static/app/components/searchQueryBuilder/index.spec.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.803)
- **Top Global Matches:** file_cluster_4: 9.803, file_cluster_10: 10.399, file_cluster_0: 10.842
- **Magnitude:** 1823.08 | **LOC:** 5936 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 60.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (94.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (45.6%), Guard Balance (formerly Safety Score) (39.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AskSeerTestComponent` **(Defensive Guards)** (Impact: 25.0)
  * `mutationFn` **(Defensive Guards)** (Impact: 22.9)
  * `aggregateGetFieldDefinition` **(Compute Cores)** (Impact: 9.5)
  * `parameterDependentValueType` **(Defensive Guards)** (Impact: 5.9)
  * `getSuggestedFilterKey` **(Compute Cores)** (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 109 instances
* *Concurrency (weighted view):* 1610
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 1308`, `args: 419`, `func_start: 249`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 32`, `fragile_debt: 3`, `duplicate_logic: 2`, `unreferenced_by_name: 2`
* *Architecture:* `io: 1`, `concurrency: 1065`, `import: 14`
* *Defense:* `safety: 64`, `test: 945`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 3):` live-announcer, react, reactTestingLibrary, utils, datePicker, searchQueryBuilder, askSeerComboBox, context...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/sentry/search/events/builder/base.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.61)
- **Top Global Matches:** file_cluster_6: 9.61, file_cluster_4: 12.605, file_cluster_8: 17.422
- **Magnitude:** 1812.54 | **LOC:** 1675 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **44** in-repo importer(s); it depends on **29**; blast radius 0.157; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.1%)
- **Documentation Coverage:** 64.7059% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `default_filter_converter` **(Many-Argument Workhorses)** (Impact: 130.0)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 86.1)
  * `resolve_function` **(Many-Argument Workhorses)** (Impact: 67.6)
  * `resolve_boolean_conditions` **(Many-Argument Workhorses)** (Impact: 54.4)
  * `resolve_orderby` **(Defensive Guards)** (Impact: 54.2)
    * *Intent:* """Given a list of public aliases, optionally prefixed by a `-` to represent direction, construct a ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 235 instances
* *State Mutation (weighted view):* 724
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 433`, `structural_boundaries: 255`, `args: 63`, `func_start: 62`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 254`, `planned_debt: 8`
* *Architecture:* `api: 58`, `import: 30`
* *Defense:* `safety: 58`, `doc: 25`, `sync_locks: 34`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 21):` __future__, collections.abc, datetime, django.utils.functional, parsimonious.exceptions, re, sentry, sentry.api...
  * `Imported By (In-Degree: 44):` (Excluded from Brief to save tokens)

### `src/sentry/event_manager.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.363)
- **Top Global Matches:** file_cluster_5: 8.363, file_cluster_4: 9.097, file_cluster_12: 9.188
- **Magnitude:** 1808.08 | **LOC:** 2797 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **58** in-repo importer(s); it depends on **107**; blast radius 0.409; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.7%), Complexity Load (formerly Cognitive Load) (58.4%)
- **Documentation Coverage:** 81.25% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `save_error_events` **(Many-Argument Workhorses)** (Impact: 45.0)
  * `_handle_regression` **(Many-Argument Workhorses)** (Impact: 45.0)
  * `_get_severity_metadata_for_group` **(Many-Argument Workhorses)** (Impact: 43.2)
  * `save_attachment` **(Many-Argument Workhorses)** (Impact: 34.1)
  * `save` **(Many-Argument Workhorses)** (Impact: 32.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 267 instances
* *State Mutation (weighted view):* 886
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 306`, `structural_boundaries: 446`, `args: 77`, `func_start: 77`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 58`, `state_mutation: 352`, `planned_debt: 1`, `fragile_debt: 13`
* *Architecture:* `io: 3`, `api: 38`, `import: 110`
* *Defense:* `safety: 47`, `doc: 21`, `sync_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.409
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 88):` .ingest.types, .utils.event_tracker, __future__, collections.abc, dataclasses, datetime, django.conf, django.core.cache...
  * `Imported By (In-Degree: 58):` (Excluded from Brief to save tokens)

### `src/sentry/utils/snuba.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.936)
- **Top Global Matches:** file_cluster_6: 7.936, file_cluster_4: 9.376, file_cluster_12: 15.692
- **Magnitude:** 1801.28 | **LOC:** 2261 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **132** in-repo importer(s); it depends on **45**; blast radius 0.864; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (89.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.1%)
- **Documentation Coverage:** 77.8761% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `aliased_query_params` **(Many-Argument Workhorses)** (Impact: 124.4)
  * `resolve_column` **(Defensive Guards)** (Impact: 85.9)
  * `query` **(Many-Argument Workhorses)** (Impact: 65.4)
  * `get_snuba_column_name` **(Defensive Guards)** (Impact: 60.0)
    * *Intent:* """ Get corresponding Snuba column name from Sentry snuba map, if not found the column is assumed to...
  * `_resolve_column` **(Defensive Guards)** (Impact: 56.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 227 instances
* *State Mutation (weighted view):* 726
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 383`, `structural_boundaries: 331`, `args: 83`, `func_start: 69`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 272`, `planned_debt: 12`, `fragile_debt: 2`
* *Architecture:* `io: 4`, `api: 72`, `import: 45`
* *Defense:* `safety: 58`, `doc: 39`, `sync_locks: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.864
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 18):` __future__, collections, collections.abc, contextlib, copy, dataclasses, datetime, dateutil.parser...
  * `Imported By (In-Degree: 132):` (Excluded from Brief to save tokens)

### `src/sentry/incidents/logic.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.45)
- **Top Global Matches:** file_cluster_4: 8.45, file_cluster_5: 9.527, file_cluster_12: 9.707
- **Magnitude:** 1799.06 | **LOC:** 2052 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **33** in-repo importer(s); it depends on **68**; blast radius 0.103; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.1%), Connectivity (formerly Api Exposure) (64.6%)
- **Documentation Coverage:** 91.7526% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `update_alert_rule` **(Many-Argument Workhorses)** (Impact: 353.8)
  * `create_alert_rule` **(Many-Argument Workhorses)** (Impact: 146.7)
  * `update_alert_rule_trigger_action` **(Many-Argument Workhorses)** (Impact: 54.6)
  * `create_alert_rule_trigger_action` **(Many-Argument Workhorses)** (Impact: 47.0)
  * `get_column_from_aggregate` **(Compute Cores)** (Impact: 43.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 185 instances
* *State Mutation (weighted view):* 606
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 307`, `structural_boundaries: 338`, `args: 61`, `func_start: 57`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 236`, `planned_debt: 5`
* *Architecture:* `api: 50`, `import: 70`
* *Defense:* `safety: 18`, `doc: 19`, `sync_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.103
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 56):` __future__, bisect, collections.abc, copy, dataclasses, datetime, django.db, django.db.models...
  * `Imported By (In-Degree: 33):` (Excluded from Brief to save tokens)

### `src/sentry/tagstore/snuba/backend.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.106)
- **Top Global Matches:** file_cluster_4: 7.106, file_cluster_6: 9.029, file_cluster_12: 13.337
- **Magnitude:** 1774.8 | **LOC:** 1992 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **50**; blast radius 0.135; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.3%), Complexity Load (formerly Cognitive Load) (65.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_tag_value_paginator_for_projects` **(Many-Argument Workhorses)** (Impact: 232.7)
  * `__get_tag_key_and_top_values` **(Many-Argument Workhorses)** (Impact: 111.3)
  * `__get_tag_keys_for_projects` **(Many-Argument Workhorses)** (Impact: 85.0)
  * `get_group_tag_keys_and_top_values` **(Many-Argument Workhorses)** (Impact: 58.8)
  * `get_generic_groups_user_counts` **(Many-Argument Workhorses)** (Impact: 39.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 200 instances
* *State Mutation (weighted view):* 661
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 258`, `structural_boundaries: 254`, `args: 56`, `func_start: 54`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 261`, `planned_debt: 4`, `fragile_debt: 1`
* *Architecture:* `api: 36`, `import: 56`
* *Defense:* `safety: 9`, `doc: 4`, `sync_locks: 12`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.135
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 33):` __future__, collections, collections.abc, datetime, dateutil.parser, django.core.cache, functools, logging...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `static/app/views/insights/pages/conversations/hooks/useConversation.spec.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 3.979)
- **Top Global Matches:** file_cluster_10: 3.979, file_cluster_2: 6.025, file_cluster_13: 6.782
- **Magnitude:** 1734.63 | **LOC:** 418 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (97.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (15.2%), Complexity Load (formerly Cognitive Load) (11.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 58`, `args: 31`, `func_start: 9`
* *Risk/State:* None
* *Architecture:* `io: 2`, `concurrency: 18`, `import: 4`
* *Defense:* `safety: 20`, `test: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 2):` useConversation, organization, reactTestingLibrary, types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/sentry/snuba/test_discover_query.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.401)
- **Top Global Matches:** file_cluster_0: 7.401, file_cluster_15: 7.874, file_cluster_2: 8.461
- **Magnitude:** 1692.48 | **LOC:** 3454 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (55.6%), Complexity Load (formerly Cognitive Load) (22.2%), Connectivity (formerly Api Exposure) (11.2%)
- **Documentation Coverage:** 98.9848% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_snql_wip_project_threshold_config` **(Defensive Guards)** (Impact: 23.8)
  * `test_count_miserable_function` **(I/O & Config Routines)** (Impact: 13.0)
  * `test_user_misery_function` **(I/O & Config Routines)** (Impact: 13.0)
  * `test_apdex_function` **(I/O & Config Routines)** (Impact: 12.2)
  * `test_failure_rate` **(Defensive Guards)** (Impact: 12.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 213 instances
* *Api Near Db Sink:* 29 instances
* *State Mutation (weighted view):* 978
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 172`, `structural_boundaries: 424`, `args: 107`, `func_start: 99`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 552`, `unreferenced_by_name: 95`
* *Architecture:* `api: 100`, `import: 16`
* *Defense:* `safety: 266`, `doc: 1`, `test: 111`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 12):` __future__, datetime, django.utils, pytest, sentry.discover.arithmetic, sentry.discover.models, sentry.exceptions, sentry.models.projectteam...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/sentry/issues/endpoints/test_organization_group_index.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.684)
- **Top Global Matches:** file_cluster_0: 7.684, file_cluster_12: 8.553, file_cluster_15: 8.704
- **Magnitude:** 1672.22 | **LOC:** 4525 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **61**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (39.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (34.8%), Complexity Load (formerly Cognitive Load) (21.7%), Connectivity (formerly Api Exposure) (11.7%)
- **Documentation Coverage:** 93.7063% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_query_status_and_substatus_nonoverlapping` **(Type Conversions)** (Impact: 18.0)
  * `test_assigned_to_pagination` **(Defensive Guards)** (Impact: 15.1)
    * *Intent:* # This seems like a random override, but this test needed a way to override # the orderby being sent...
  * `test_query_status_and_substatus_overlapping` **(Type Conversions)** (Impact: 14.0)
  * `test_bulk_delete_for_many_projects_without_option` **(Defensive Guards)** (Impact: 13.2)
  * `test_semver` **(Defensive Guards)** (Impact: 13.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 72 instances
* *State Mutation (weighted view):* 889
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 1149`, `args: 145`, `func_start: 145`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 745`, `planned_debt: 1`, `fragile_debt: 2`, `duplicate_logic: 2`, `unreferenced_by_name: 134`
* *Architecture:* `api: 146`, `import: 61`
* *Defense:* `safety: 789`, `doc: 10`, `test: 161`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 48):` __future__, collections, collections.abc, datetime, django.db.utils, django.urls, django.utils, functools...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/sentry/snuba/test_transactions.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.349)
- **Top Global Matches:** file_cluster_0: 7.349, file_cluster_15: 7.861, file_cluster_2: 8.478
- **Magnitude:** 1668.76 | **LOC:** 3170 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (57.2%), Complexity Load (formerly Cognitive Load) (26.5%), Connectivity (formerly Api Exposure) (11.2%)
- **Documentation Coverage:** 98.9305% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_snql_wip_project_threshold_config` **(Defensive Guards)** (Impact: 23.8)
  * `test_count_miserable_function` **(I/O & Config Routines)** (Impact: 13.0)
  * `test_user_misery_function` **(I/O & Config Routines)** (Impact: 13.0)
  * `test_apdex_function` **(I/O & Config Routines)** (Impact: 12.2)
  * `test_failure_rate` **(Defensive Guards)** (Impact: 12.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 194 instances
* *Api Near Db Sink:* 31 instances
* *State Mutation (weighted view):* 1010
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 155`, `structural_boundaries: 408`, `args: 101`, `func_start: 94`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 622`, `unreferenced_by_name: 90`
* *Architecture:* `api: 95`, `import: 16`
* *Defense:* `safety: 255`, `doc: 1`, `test: 106`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 12):` __future__, datetime, django.utils, pytest, sentry.discover.arithmetic, sentry.discover.models, sentry.exceptions, sentry.models.projectteam...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/snuba/api/endpoints/test_organization_events_span_indexed.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.792)
- **Top Global Matches:** file_cluster_15: 7.792, file_cluster_0: 8.062, file_cluster_2: 8.153
- **Magnitude:** 1616.52 | **LOC:** 7325 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **13**; blast radius 0.039; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (70.5%), Guard Balance (formerly Safety Score) (41.4%), Complexity Load (formerly Cognitive Load) (6.7%)
- **Documentation Coverage:** 95.977% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_test_simple_measurements` **(Many-Argument Workhorses)** (Impact: 9.8)
  * `test_has_in_filter` **(Defensive Guards)** (Impact: 9.8)
  * `test_pagination_samples` **(Defensive Guards)** (Impact: 9.5)
  * `test_short_trace_id_filter` **(Defensive Guards)** (Impact: 7.5)
  * `test_semver` **(Defensive Guards)** (Impact: 6.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 652
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 1085`, `args: 176`, `func_start: 175`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 578`, `planned_debt: 5`
* *Architecture:* `io: 12`, `api: 181`, `import: 14`
* *Defense:* `safety: 829`, `doc: 7`, `test: 197`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.039
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 7):` datetime, django.utils.timezone, pytest, sentry.insights.models, sentry.search.events.constants, sentry.testutils.helpers, sentry.testutils.helpers.datetime, sentry.utils.snuba_rpc...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tests/snuba/api/endpoints/test_organization_events_stats.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.197)
- **Top Global Matches:** file_cluster_0: 7.197, file_cluster_15: 7.885, file_cluster_2: 8.482
- **Magnitude:** 1587.26 | **LOC:** 3978 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **21**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (46.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (20.9%), Complexity Load (formerly Cognitive Load) (12.5%), Connectivity (formerly Api Exposure) (11.8%)
- **Documentation Coverage:** 93.9655% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_functions_dataset_simple` **(Defensive Guards)** (Impact: 16.1)
  * `test_functions_dataset_simple` **(Defensive Guards)** (Impact: 14.1)
  * `setUp` **(I/O & Config Routines)** (Impact: 12.9)
    * *Intent:* # This is implemented almost exactly the same as spans, add a simple test case for a sanity check
  * `test_aggregate_function_apdex` **(Defensive Guards)** (Impact: 12.8)
  * `setUp` **(I/O & Config Routines)** (Impact: 12.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 144 instances
* *State Mutation (weighted view):* 738
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 204`, `structural_boundaries: 710`, `args: 117`, `func_start: 116`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 450`, `fragile_debt: 2`, `duplicate_logic: 6`, `unreferenced_by_name: 86`
* *Architecture:* `api: 138`, `import: 22`
* *Defense:* `safety: 424`, `doc: 8`, `test: 144`, `sync_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 9):` __future__, collections, datetime, django.urls, pytest, sentry.constants, sentry.issues.grouptype, sentry.models.project...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `static/app/views/performance/newTraceDetails/traceModels/traceTree.autogrouping.spec.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 5.429)
- **Top Global Matches:** file_cluster_7: 5.429, file_cluster_12: 6.645, file_cluster_5: 8.585
- **Magnitude:** 1581.62 | **LOC:** 899 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (91.4%), Guard Balance (formerly Safety Score) (52.9%), Complexity Load (formerly Cognitive Load) (9.1%), Debt Markers (formerly Tech Debt) (8.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 81`, `args: 59`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 36`, `planned_debt: 1`
* *Architecture:* `io: 9`, `concurrency: 34`, `import: 5`
* *Defense:* `safety: 2`, `test: 78`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 2):` traceGuards, traceTree, organization, traceTreeTestUtils, tracePreferences
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/sentry/search/events/fields.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.19)
- **Top Global Matches:** file_cluster_12: 8.19, file_cluster_4: 8.477, file_cluster_0: 9.2
- **Magnitude:** 1546.18 | **LOC:** 2339 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **35** in-repo importer(s); it depends on **21**; blast radius 0.164; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (68.6%), Guard Balance (formerly Safety Score) (63.2%)
- **Documentation Coverage:** 92.3977% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolve_function` **(Many-Argument Workhorses)** (Impact: 71.2)
  * `parse_arguments` **(Compute Cores)** (Impact: 65.8)
    * *Intent:* """ Some functions take a quoted string for their arguments that may contain commas, which requires ...
  * `project_threshold_config_expression` **(Many-Argument Workhorses)** (Impact: 33.9)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 30.2)
  * `get_json_meta_type` **(Compute Cores)** (Impact: 29.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 149 instances
* *State Mutation (weighted view):* 518
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 339`, `structural_boundaries: 320`, `args: 102`, `func_start: 96`, `class_start: 33`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 220`, `planned_debt: 8`, `fragile_debt: 2`, `duplicate_logic: 7`
* *Architecture:* `api: 108`, `import: 23`
* *Defense:* `safety: 48`, `doc: 22`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.164
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 11):` __future__, collections, collections.abc, copy, datetime, re, sentry.discover.models, sentry.exceptions...
  * `Imported By (In-Degree: 35):` (Excluded from Brief to save tokens)

### `static/app/views/dashboards/widgetBuilder/components/visualize/index.spec.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.316)
- **Top Global Matches:** file_cluster_0: 6.316, file_cluster_10: 6.45, file_cluster_2: 7.3
- **Magnitude:** 1524.91 | **LOC:** 1996 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (43.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (21.7%), Complexity Load (formerly Cognitive Load) (18.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 257`, `args: 66`, `func_start: 55`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 2`
* *Architecture:* `concurrency: 202`, `import: 10`
* *Defense:* `safety: 11`, `test: 230`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 2):` organization, reactTestingLibrary, group, fields, useCustomMeasurements, useNavigate, types, visualize...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/sentry/dashboards/endpoints/test_organization_dashboard_details.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.468)
- **Top Global Matches:** file_cluster_12: 7.468, file_cluster_0: 8.094, file_cluster_15: 8.768
- **Magnitude:** 1519.9 | **LOC:** 4874 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **21**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (45.5%), Connectivity (formerly Api Exposure) (12.5%), Complexity Load (formerly Cognitive Load) (12.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_ondemand_updates_existing_widget` **(Many-Argument Workhorses)** (Impact: 9.6)
  * `test_ondemand_updates_new_widget` **(Many-Argument Workhorses)** (Impact: 9.6)
  * `test_does_not_update_non_table_dashboard_links` **(I/O & Config Routines)** (Impact: 7.2)
  * `test_add_widget_with_field_aliases` **(Defensive Guards)** (Impact: 5.9)
  * `test_ondemand_hits_card_limit` **(Defensive Guards)** (Impact: 5.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 685
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 883`, `args: 187`, `func_start: 187`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 50`, `state_mutation: 625`, `duplicate_logic: 2`, `unreferenced_by_name: 161`
* *Architecture:* `api: 203`, `import: 22`
* *Defense:* `safety: 522`, `doc: 1`, `test: 185`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 13):` __future__, datetime, django.urls, django.utils, pytest, sentry.dashboards.endpoints.organization_dashboards, sentry.discover.models, sentry.explore.translation.dashboards_translation...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tests/sentry/preprod/vcs/status_checks/size/test_templates.py` (PYTHON) | Magnitude: 466.56 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 1477, core_var_decl: 919, design_snake_case: 919, structural_boundaries: 192
- `static/app/components/projects/missingProjectMembership.tsx` (TYPESCRIPT) | Magnitude: 44.86 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 130, structural_boundaries: 40, core_var_decl: 25, ui_framework: 20
- `src/sentry/api/endpoints/organization_sampling_project_span_counts.py` (PYTHON) | Magnitude: 34.74 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 45, indent_spaces: 40, core_var_decl: 21, design_snake_case: 21
- `static/app/components/forms/fields/checkboxField.tsx` (TYPESCRIPT) | Magnitude: 17.42 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 48, core_var_decl: 16, structural_boundaries: 14, generics: 11
- `static/app/views/navigation/primary/userDropdown.spec.tsx` (TYPESCRIPT) | Magnitude: 83.68 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 39, structural_boundaries: 17, test: 12, concurrency: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `static/app/views/insights/pages/backend/backendOverviewPage.spec.tsx` (TYPESCRIPT) | Magnitude: 9.08 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 137, structural_boundaries: 15, import: 7, args: 6
- `static/app/components/events/contexts/knownContext/profile.spec.tsx` (TYPESCRIPT) | Magnitude: 16.94 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 83, core_var_decl: 13, structural_boundaries: 11, test: 9
- `static/app/views/dashboards/widgetCard/widgetFrame.spec.tsx` (TYPESCRIPT) | Magnitude: 32.42 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 205, test: 50, structural_boundaries: 42, core_var_decl: 38
- `static/app/views/settings/components/dataScrubbing/modals/edit.spec.tsx` (TYPESCRIPT) | Magnitude: 188.93 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 290, core_var_decl: 111, structural_boundaries: 54, design_camel_case: 48
- `static/app/views/explore/metrics/hooks/useMetricAggregatesTable.spec.tsx` (TYPESCRIPT) | Magnitude: 13.34 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 174, structural_boundaries: 31, core_var_decl: 17, test: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `static/app/utils/performance/contexts/performanceDisplayContext.tsx` (TYPESCRIPT) | Magnitude: 3.36 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 5, api: 2, import: 2
- `tests/relay_integration/lang/javascript/fixtures/example/test.js` (JAVASCRIPT) | Magnitude: 0.02 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 18, args: 5, core_var_decl: 5, structural_boundaries: 4
- `tests/symbolicator/fixtures/test.js` (JAVASCRIPT) | Magnitude: 0.02 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 18, args: 5, core_var_decl: 5, structural_boundaries: 4
- `tests/sentry/api/endpoints/test_relay_projectconfigs_v3.py` (PYTHON) | Magnitude: 77.4 | Delta: **0.128** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 91, structural_boundaries: 55, test: 30, core_var_decl: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `static/app/views/automations/components/dataConditionNodes.tsx` (TYPESCRIPT) | Magnitude: 15.48 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 362, structural_boundaries: 38, import: 23, branch: 7
- `src/sentry/models/groupmeta.py` (PYTHON) | Magnitude: 97.42 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 64, structural_boundaries: 36, state_mutation: 25, core_var_decl: 17
- `tests/sentry/uptime/consumers/test_tasks.py` (PYTHON) | Magnitude: 46.54 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 146, structural_boundaries: 47, core_var_decl: 27, design_snake_case: 27
- `.github/actions/collect-test-data/action.yml` (YAML) | Magnitude: 15.66 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 29, args: 11, doc: 8, branch: 7
- `src/sentry/issues/suspect_flags.py` (PYTHON) | Magnitude: 162.24 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 250, core_var_decl: 82, design_snake_case: 82, structural_boundaries: 41

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tests/sentry/spans/log_analyzer/test_analyzer.py` (PYTHON) | Magnitude: 42.12 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 58, structural_boundaries: 34, core_var_decl: 26, design_snake_case: 26
- `tests/sentry/integrations/slack/webhooks/events/test_app_mention.py` (PYTHON) | Magnitude: 40.58 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 83, structural_boundaries: 43, test: 22, safety: 18
- `src/sentry/issues/endpoints/team_groups_old.py` (PYTHON) | Magnitude: 26.24 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 27, import: 12, core_var_decl: 9
- `tests/sentry/utils/sdk_crashes/test_sdk_crash_detection_java.py` (PYTHON) | Magnitude: 104.56 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 302, structural_boundaries: 74, core_var_decl: 59, design_snake_case: 59
- `static/app/gettingStartedDocs/react-native/onboarding.tsx` (TYPESCRIPT) | Magnitude: 20.62 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 75, structural_boundaries: 15, io: 5, core_var_decl: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `tests/snuba/metrics/naming_layer/test_mri.py` (PYTHON) | Magnitude: 7.72 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 18, indent_spaces: 10, safety: 8, test: 6
- `src/sentry/workflow_engine/endpoints/validators/incident_groupopenperiod.py` (PYTHON) | Magnitude: 17.38 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 7, branch: 5, safety_bypasses: 4
- `src/sentry/workflow_engine/endpoints/serializers/data_condition_group_serializer.py` (PYTHON) | Magnitude: 51.44 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 15, state_mutation: 10, safety_bypasses: 9
- `tests/sentry/tasks/conftest.py` (PYTHON) | Magnitude: 6.22 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 16, indent_spaces: 8, test: 6, generics: 6
- `src/sentry/notifications/notifications/activity/resolved.py` (PYTHON) | Magnitude: 5.68 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 12, import: 4, indent_spaces: 4, safety_bypasses: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/sentry/management/commands/create_sample_event.py` (PYTHON) | Magnitude: 42.22 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 12, branch: 10, core_var_decl: 9
- `static/gsApp/hooks/usePlanMigrations.tsx` (TYPESCRIPT) | Magnitude: 9.78 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 12, import: 6, branch: 4
- `tests/sentry/models/test_releaseenvironment.py` (PYTHON) | Magnitude: 17.36 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 23, core_var_decl: 15, design_snake_case: 15
- `static/app/utils/profiling/renderers/selectedFrameRenderer.tsx` (TYPESCRIPT) | Magnitude: 16.92 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 8, state_mutation: 4, import: 3
- `static/app/utils/userselect.tsx` (TYPESCRIPT) | Magnitude: 22.78 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 15, globals: 8, structural_boundaries: 5, branch: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/sentry/notifications/platform/slack/renderers/metric_alert.py` (PYTHON) | Magnitude: 61.06 | Delta: **0.089** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 68, structural_boundaries: 43, core_var_decl: 32, design_snake_case: 32
- `src/sentry/core/endpoints/organization_projects_experiment.py` (PYTHON) | Magnitude: 89.78 | Delta: **0.096** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 140, structural_boundaries: 71, core_var_decl: 60, design_snake_case: 56
- `src/sentry/monitors/logic/incident_occurrence.py` (PYTHON) | Magnitude: 127.9 | Delta: **0.121** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 164, structural_boundaries: 67, core_var_decl: 62, design_snake_case: 61
- `src/sentry/utils/outcomes.py` (PYTHON) | Magnitude: 231.66 | Delta: **0.157** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 181, core_var_decl: 72, structural_boundaries: 63, design_snake_case: 51
- `src/sentry/issues/endpoints/group_current_release.py` (PYTHON) | Magnitude: 42.4 | Delta: **0.181** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 49, structural_boundaries: 35, core_var_decl: 18, design_snake_case: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `static/app/gettingStartedDocs/python/index.tsx` (TYPESCRIPT) | Magnitude: 16.42 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 12, import: 10, indent_spaces: 9, api: 1
- `src/sentry/models/files/__init__.py` (PYTHON) | Magnitude: 17.48 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 18, indent_spaces: 13, import: 9, api: 1
- `.github/workflows/codeql.yml` (YAML) | Magnitude: 16.76 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 4, args: 4, import: 3
- `src/sentry/auth/providers/google/constants.py` (PYTHON) | Magnitude: 34.2 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: state_mutation: 7, core_var_decl: 7, design_upper_case: 7, structural_boundaries: 4
- `src/sentry/eventstore/__init__.py` (PYTHON) | Magnitude: 19.6 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 6, import: 3, branch: 2, state_mutation: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `tests/sentry/preprod/test_models_size_metrics.py` (PYTHON) | Magnitude: 88.96 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 192, core_var_decl: 86, design_snake_case: 86, structural_boundaries: 62
- `src/sentry/preprod/eap/read.py` (PYTHON) | Magnitude: 55.66 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 196, core_var_decl: 114, design_snake_case: 110, structural_boundaries: 28
- `static/app/components/charts/series/barSeries.tsx` (TYPESCRIPT) | Magnitude: 4.26 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 4, branch: 1, args: 1
- `src/sentry/analytics/events/integration_commit_context_all_frames.py` (PYTHON) | Magnitude: 17.5 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 4, class_start: 2, api: 2
- `static/app/utils/url/safeURL.tsx` (TYPESCRIPT) | Magnitude: 4.94 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 5, structural_boundaries: 3, safety: 2, branch: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/sentry/ingest/consumer/processors.py` (PYTHON) | Magnitude: 203.84 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 242, structural_boundaries: 103, core_var_decl: 71, design_snake_case: 69
- `src/sentry/api/endpoints/artifact_lookup.py` (PYTHON) | Magnitude: 191.5 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 180, structural_boundaries: 82, core_var_decl: 54, design_snake_case: 51
- `src/sentry/relay/config/__init__.py` (PYTHON) | Magnitude: 527.8 | Delta: **0.071** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 1002, structural_boundaries: 160, branch: 94, state_mutation: 92
- `static/app/components/profiling/flamegraph/flamegraphContextMenu.tsx` (TYPESCRIPT) | Magnitude: 237.72 | Delta: **0.088** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 611, ui_framework: 190, structural_boundaries: 124, core_var_decl: 102
- `src/sentry/http.py` (PYTHON) | Magnitude: 224.78 | Delta: **0.096** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 145, structural_boundaries: 71, core_var_decl: 60, design_snake_case: 58

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `src/sentry/issues/escalating/escalating.py` (PYTHON) | Magnitude: 432.66 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 405, core_var_decl: 148, design_snake_case: 132, structural_boundaries: 109
- `tools/migrations/compare.py` (PYTHON) | Magnitude: 6.58 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 87, state_mutation: 34, core_var_decl: 26, branch: 25
- `static/app/utils/profiling/differentialFlamegraph.tsx` (TYPESCRIPT) | Magnitude: 185.9 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 180, state_mutation: 34, core_var_decl: 32, branch: 28
- `tests/sentry/integrations/api/endpoints/test_user_organizationintegration.py` (PYTHON) | Magnitude: 29.42 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 49, structural_boundaries: 21, state_mutation: 13, core_var_decl: 13
- `src/sentry/integrations/discord/webhooks/base.py` (PYTHON) | Magnitude: 29.64 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 56, structural_boundaries: 46, import: 17, core_var_decl: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `static/app/components/core/alert/alert.tsx` (TYPESCRIPT) | Magnitude: 86.08 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 237, structural_boundaries: 66, branch: 38, args: 33
- `src/sentry/core/endpoints/scim/members.py` (PYTHON) | Magnitude: 390.62 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 472, core_var_decl: 160, design_snake_case: 157, structural_boundaries: 132
- `static/app/components/searchQueryBuilder/hooks/useQueryBuilderState.tsx` (TYPESCRIPT) | Magnitude: 493.28 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 788, branch: 198, structural_boundaries: 193, core_var_decl: 116
- `static/app/components/avatarChooser/index.tsx` (TYPESCRIPT) | Magnitude: 151.24 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 285, structural_boundaries: 84, core_var_decl: 68, branch: 52
- `src/sentry/web/frontend/oauth_token.py` (PYTHON) | Magnitude: 270.74 | Delta: **0.139** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 440, core_var_decl: 163, design_snake_case: 160, structural_boundaries: 116

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `tests/sentry/scm/unit/test_stream.py` (PYTHON) | Magnitude: 14.72 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 14, args: 5, func_start: 5
- `static/app/utils/consolidatedScopes.spec.tsx` (TYPESCRIPT) | Magnitude: 17.66 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 30, test: 8, structural_boundaries: 6, args: 5
- `src/sentry/preprod/api/endpoints/project_preprod_distribution.py` (PYTHON) | Magnitude: 14.74 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 33, indent_spaces: 32, import: 15, core_var_decl: 10
- `static/app/components/events/contexts/platformContext/react.tsx` (TYPESCRIPT) | Magnitude: 9.16 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 12, branch: 3, import: 3
- `static/app/views/insights/browser/webVitals/utils/useWebVitalsSort.tsx` (TYPESCRIPT) | Magnitude: 9.48 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 9, core_var_decl: 6, branch: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/sentry/models/deploy.py` (PYTHON) | Magnitude: 57.52 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 60, structural_boundaries: 31, core_var_decl: 28, design_snake_case: 28
- `src/sentry/integrations/api/endpoints/organization_integration_channels.py` (PYTHON) | Magnitude: 155.8 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 166, structural_boundaries: 66, core_var_decl: 41, design_snake_case: 40
- `static/app/components/stackTrace/stackTraceProvider.tsx` (TYPESCRIPT) | Magnitude: 32.6 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 129, structural_boundaries: 35, args: 16, core_var_decl: 15
- `src/sentry/features/flagpole_context.py` (PYTHON) | Magnitude: 129.74 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 73, structural_boundaries: 37, state_mutation: 31, branch: 18
- `static/app/components/feedback/useMutateFeedback.tsx` (TYPESCRIPT) | Magnitude: 32.5 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 31, core_var_decl: 12, import: 9

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/sentry/seer/autofix/autofix_agent.py` -> Churn: **67.12%** | Cog Load: 55.9729% | Debt: 0.0%
- `src/sentry/core/endpoints/organization_details.py` -> Churn: **60.99%** | Cog Load: 63.9944% | Debt: 8.741%
- `src/sentry/spans/buffer.py` -> Churn: **60.99%** | Cog Load: 79.9493% | Debt: 9.4231%
- `src/sentry/testutils/cases.py` -> Churn: **60.99%** | Cog Load: 82.8607% | Debt: 27.6771%
- `src/sentry/seer/autofix/autofix.py` -> Churn: **58.56%** | Cog Load: 60.8562% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/sentry/testutils/factories.py` -> **Lyn Nagara** (100.0% isolated ownership) | Magnitude: 2059.64
- `static/app/views/dashboards/widgets/tableWidget/tableWidgetVisualization.stories.tsx` -> **Josh Goldberg ✨** (100.0% isolated ownership) | Magnitude: 1958.5
- `static/app/views/insights/pages/conversations/hooks/useConversation.spec.tsx` -> **Ogi** (100.0% isolated ownership) | Magnitude: 1734.63
- `src/sentry/search/events/fields.py` -> **William Mak** (100.0% isolated ownership) | Magnitude: 1546.18
- `src/sentry/seer/explorer/tools.py` -> **Andrew Liu** (100.0% isolated ownership) | Magnitude: 1394.22

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tests/js/sentry-test/reactTestingLibrary.tsx` -> **Severity: 1879.895** (Blast Radius: 23.812 * Doc Risk: 78.9474%)
- `src/sentry/monkey/__init__.py` -> **Severity: 1505.4** (Blast Radius: 15.054 * Doc Risk: 100.0%)
- `src/sentry/__init__.py` -> **Severity: 1252.001** (Blast Radius: 17.528 * Doc Risk: 71.4286%)
- `src/sentry/testutils/cases.py` -> **Severity: 891.39** (Blast Radius: 9.688 * Doc Risk: 92.0097%)
- `src/sentry/constants.py` -> **Severity: 817.0** (Blast Radius: 8.17 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 478 literal sites + 170 sites through wrappers = 648
- **`panics_and_aborts`:** 6150 literal sites + 93 sites through wrappers = 6243

- `print` (function, debug_prints, primitive): 165 call sites in 27 files -- `static/app/views/performance/newTraceDetails/traceModels/traceTree.tsx`
- `not_supported` (function, panics_and_aborts, primitive): 20 call sites in 2 files -- `src/sentry/replays/lib/new_query/conditions.py`
- `parse_headers` (function, panics_and_aborts, primitive): 7 call sites in 2 files -- `src/sentry/replays/consumers/recording.py`
- `retry_task` (function, panics_and_aborts, primitive): 7 call sites in 5 files -- `src/sentry/taskworker/tasks/examples.py`
- `operator` (function, panics_and_aborts, primitive): 6 call sites in 3 files -- `src/sentry/replays/lib/eap/snuba_transpiler.py`
- `validate_json_schema` (function, panics_and_aborts, primitive): 6 call sites in 4 files -- `src/sentry/workflow_engine/endpoints/validators/utils.py`
- `_run` (function, debug_prints, primitive): 5 call sites in 1 files -- `tools/migrations/quick_drift_compare.py`
- `add_raise_scm_error` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `tests/sentry/scm/endpoints/test_scm_rpc.py`
- `raise_after` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `tests/sentry/tsdb/test_redis.py`
- `_validate_headers` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `src/sentry/uptime/endpoints/validators.py`
- `parse_request_message` (function, panics_and_aborts, primitive): 3 call sites in 2 files -- `src/sentry/replays/consumers/recording.py`
- `task_that_raises_retry_error` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `tests/sentry/tasks/test_base.py`
*(+22 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 307832 call pairs -- scoped 33.8%, unique 0.0%, ambiguous 32.0%, external 34.2%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 235448 | 40.9% | 0.0% | 30.6% | 28.5% |
| typescript | 71482 | 10.6% | 0.0% | 36.9% | 52.5% |
| lua | 521 | 32.6% | 0.0% | 0.0% | 67.4% |
| javascript | 256 | 22.7% | 0.0% | 14.5% | 62.9% |
| html | 70 | 20.0% | 0.0% | 0.0% | 80.0% |
| shell | 55 | 7.3% | 0.0% | 0.0% | 92.7% |

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
