# ARCHITECTURAL_BRIEF: sentry
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/getsentry/sentry.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
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
## 2. THE 13-POINT STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (EQUATIONS & CONTEXT)
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

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 20173 |
| Analyzed Artifacts (Scanned) | 17849 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2324 |
| Total LOC | 2456855 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 88.5% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5676 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0919 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 7.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 6.3131 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 775 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 8651 | 1158848 | 48.5% |
| PYTHON | 7763 | 1189104 | 43.5% |
| JSON | 678 | 89673 | 3.8% |
| XML | 215 | 566 | 1.2% |
| HTML | 183 | 8387 | 1.0% |
| PLAINTEXT | 153 | 3 | 0.9% |
| MARKDOWN | 101 | 0 | 0.6% |
| CSS | 37 | 5940 | 0.2% |
| JAVASCRIPT | 35 | 1499 | 0.2% |
| LUA | 12 | 1747 | 0.1% |
| SHELL | 11 | 312 | 0.1% |
| YAML | 8 | 499 | 0.0% |
| MAKEFILE | 1 | 202 | 0.0% |
| DOCKERFILE | 1 | 75 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +0.45; from the repo's file-archetype mix)
> **File Composition:** Generic / Templated Code Files 18%, Data / Markup / Trivial 17%, Declarative / Non-Code 16%, Defensive Guards Files 15%, Large Core Modules 10%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 17462 | 97.8% |
| Unknown | 3 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 251 | 1.4% |
| Static: Minified & Vendor Opaque Mass | 133 | 0.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2324*

**Composition by Extension & Reason:**
- `.pysnap`: 1524x Excluded (Unsupported Extension: '.pysnap')
- `.tsx`: 82x Excluded (Saturation: Line 7 exceeds 500 chars), 79x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Excluded (Saturation: Line 12 exceeds 500 chars)
- `.py`: 65x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 9x Excluded (Machine-Generated Source Code Signature: 26 LOC), 6x Excluded (Machine-Generated Source Code Signature: 20 LOC)
- `.png`: 76x Excluded (Explicitly Denied Extension: '.png')
- `.md`: 71x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mo`: 49x Excluded (Binary Format Detected)
- `.po`: 12x Unsupported Format (.po), 4x Excluded (Monolithic Amalgamation: 45259 LOC exceeds safe regex boundaries), 2x Excluded (Monolithic Amalgamation: 45266 LOC exceeds safe regex boundaries)
- `.yml`: 46x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable), 3x Excluded (Binary Format Detected)
- `.json`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 1478 LOC), 1x Excluded (Static Asset Blob without Intent: 1142 LOC)
- `.js`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.woff2`: 15x Excluded (Explicitly Denied Extension: '.woff2')
- `.map`: 14x Excluded (Unsupported Extension: '.map')
- `.ts`: 4x Unsupported Format (.undeterminable), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 432 LOC)
- `.jpg`: 9x Excluded (Explicitly Denied Extension: '.jpg')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 13.1 | 6.2 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.9 | 36.2 | 40.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 10.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 6.1 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 18.2 | 7.4 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 8.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 25.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.0 | 0.4 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 79.6 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.3 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 5.5 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 60.9 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 17898 | 4533 | 2 | `tests/snuba/search/test_backend.py` |
| cleanup | 496 | 261 | 0 | `static/app/views/navigation/useCollapsedNavigation.tsx` |
| guards | 121208 | 9131 | 15 | `tests/snuba/api/endpoints/test_organization_events.py` |
| danger | 34968 | 6410 | 5 | `tests/sentry/scm/test_fixtures.py` |
| concurrency | 29258 | 2929 | 3 | `static/app/components/searchQueryBuilder/index.spec.tsx` |
| connectivity | 84499 | 13605 | 12 | `src/sentry/testutils/cases.py` |
| io | 11266 | 2919 | 1 | `static/app/router/routes.tsx` |
| crypto | 243 | 193 | 0 | `src/sentry/utils/hashlib.py` |
| ipc | 143 | 58 | 0 | `src/sentry/preprod/snapshots/image_diff/odiff.py` |
| time | 8392 | 1396 | 0 | `tests/sentry/replays/endpoints/test_organization_replay_index.py` |
| serialization | 560 | 241 | 0 | `static/app/utils/profiling/renderers/flamegraphRendererWebGL.spec.tsx` |
| regex | 1342 | 605 | 0 | `static/app/data/controlsiloUrlPatterns.ts` |
| events | 7482 | 2224 | 1 | `tests/sentry/workflow_engine/processors/test_detector.py` |
| tests | 105157 | 4443 | 17 | `static/app/components/searchQueryBuilder/index.spec.tsx` |
| docs | 20272 | 4652 | 3 | `static/less/includes/bootstrap/variables.less` |
| debt | 4920 | 2101 | 1 | `eslint.config.ts` |
| mutation | 669886 | 14889 | 86 | `tests/snuba/api/endpoints/test_organization_events.py` |
| dead_code | 31364 | 6246 | 4 | `tests/sentry/dashboards/endpoints/test_organization_dashboard_details.py` |
| credential | 739 | 226 | 0 | `fixtures/vsts.py` |
| threat | 4180 | 1295 | 0 | `src/sentry/testutils/factories.py` |
| ml_ai | 6016 | 1068 | 0 | `tests/sentry/search/events/test_filter.py` |
| ui | 66342 | 5847 | 11 | `static/app/components/searchQueryBuilder/index.spec.tsx` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.2**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `static/app/router/routes.tsx` (Hits: 420)
- `static/app/components/illustrations/NoProjectEmptyState.tsx` (Hits: 282)
- `static/gsApp/components/features/illustrations/alertsBackground.tsx` (Hits: 173)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **react.tsx** (`static/app/components/events/contexts/platformContext/react.tsx`) — 3167 inbound connections
2. **cases.py** (`src/sentry/testutils/cases.py`) — 1794 inbound connections
3. **reactTestingLibrary.tsx** (`tests/js/sentry-test/reactTestingLibrary.tsx`) — 1497 inbound connections
4. **datetime.py** (`src/sentry/testutils/helpers/datetime.py`) — 1393 inbound connections
5. **useOrganization.tsx** (`static/app/utils/useOrganization.tsx`) — 1327 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **urls.py** (`src/sentry/api/urls.py`) — 475 outbound dependencies
2. **routes.tsx** (`static/app/router/routes.tsx`) — 310 outbound dependencies
3. **index.tsx** (`static/app/icons/index.tsx`) — 149 outbound dependencies
4. **factories.py** (`src/sentry/testutils/factories.py`) — 148 outbound dependencies
5. **cases.py** (`src/sentry/testutils/cases.py`) — 137 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `ReleaseComparisonChart` **(Compute Cores)** (@ `static/app/views/releases/detail/overview/releaseComparisonChart/index.tsx`) -> Impact: **400.1** | LOC: 1044
- `put` **(Many-Argument Workhorses)** (@ `src/sentry/core/endpoints/project_details.py`) -> Impact: **357.6** | LOC: 511
  * *Intent:* """ Update various attributes and configurable settings for the given project. Note that solely having the **`project:read`** scope restricts updatabl...
- `update_alert_rule` **(Many-Argument Workhorses)** (@ `src/sentry/incidents/logic.py`) -> Impact: **353.8** | LOC: 266
- `Visualize` **(Compute Cores)** (@ `static/app/views/dashboards/widgetBuilder/components/visualize/index.tsx`) -> Impact: **332.5** | LOC: 880
- `devserver` **(Many-Argument Workhorses)** (@ `src/sentry/runner/commands/devserver.py`) -> Impact: **314.9** | LOC: 359
- `useWidgetBuilderState` **(Compute Cores)** (@ `static/app/views/dashboards/widgetBuilder/hooks/useWidgetBuilderState.tsx`) -> Impact: **310.8** | LOC: 915
- `getGroupActivityItem` **(Many-Argument Workhorses)** (@ `static/app/views/issueDetails/streamline/sidebar/groupActivityItem.tsx`) -> Impact: **301.2** | LOC: 685
- `Flamegraph` **(Compute Cores)** (@ `static/app/components/profiling/flamegraph/flamegraph.tsx`) -> Impact: **277.5** | LOC: 1350
- `ContinuousFlamegraph` **(Compute Cores)** (@ `static/app/components/profiling/flamegraph/continuousFlamegraph.tsx`) -> Impact: **275.1** | LOC: 1361
- `IssueListOverview` **(Compute Cores)** (@ `static/app/views/issueList/overview.tsx`) -> Impact: **236.3** | LOC: 822

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `tests/snuba/api/endpoints` | 67 | 22297.92 | 12.12% | 0.0% |
| `src/sentry/api/endpoints` | 156 | 19012.04 | 39.65% | 3.25% |
| `tests/sentry/api/endpoints` | 145 | 13639.9 | 8.87% | 0.0% |
| `src/sentry/utils` | 98 | 12136.68 | 41.13% | 7.6% |
| `src/sentry/models` | 121 | 12001.3 | 33.62% | 7.16% |
| `static/app/components` | 221 | 11216.53 | 10.0% | 21.27% |
| `static/app/utils` | 263 | 10522.62 | 10.15% | 33.99% |
| `src/sentry/api/serializers/models` | 57 | 8541.5 | 42.66% | 11.06% |
| `src/sentry/snuba` | 35 | 8392.02 | 32.92% | 12.3% |
| `src/sentry/testutils` | 15 | 7843.52 | 45.71% | 26.82% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/sentry/apidocs/extensions.py` -> **100.0%** Exposure
- `src/sentry/db/models/fields/bounded.py` -> **100.0%** Exposure
- `src/sentry/integrations/services/github_copilot_identity/service.py` -> **100.0%** Exposure
- `src/sentry/relocation/services/relocation_export/service.py` -> **100.0%** Exposure
- `src/sentry/seer/entrypoints/types.py` -> **100.0%** Exposure
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
- `fixtures/github.py` -> **100.0%** Exposure
- `fixtures/vercel.py` -> **100.0%** Exposure
- `src/sentry_plugins/github/testutils.py` -> **100.0%** Exposure
- `tests/sentry/api/endpoints/test_auth_validate.py` -> **100.0%** Exposure
- `tests/sentry/event_manager/interfaces/test_expectct.py` -> **100.0%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `86` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `131545` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `static/app/utils/cursorPoller.tsx` (TYPESCRIPT) -> Cumulative Risk: **795.32**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.06)
- **Magnitude:** 116.98 | **LOC:** 120 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.8376%)
- **Heaviest Functions:** `success` (Defensive Guards, Impact: 27.2), `poll` (Defensive Guards, Impact: 20.4), `error` (Callbacks & Closures, Impact: 7.8)

### 2. `src/sentry/utils/http.py` (PYTHON) -> Cumulative Risk: **794.6**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +0.54)
- **Magnitude:** 244.42 | **LOC:** 287 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.956%), Documentation (95.2381%)
- **Heaviest Functions:** `is_valid_origin` (Many-Argument Workhorses, Impact: 44.5), `get_origins` (Compute Cores, Impact: 13.6), `parse_uri_match` (Compute Cores, Impact: 12.5)

### 3. `src/sentry/hybridcloud/rpc/caching/service.py` (PYTHON) -> Cumulative Risk: **753.52**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z -1.36)
- **Magnitude:** 229.42 | **LOC:** 374 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (94.7972%)
- **Heaviest Functions:** `get_many` (Many-Argument Workhorses, Impact: 19.7), `resolve_from` (Defensive Guards, Impact: 13.5), `resolve_from` (Defensive Guards, Impact: 9.1)

### 4. `static/app/components/replays/deserializeCanvasArgs.ts` (TYPESCRIPT) -> Cumulative Risk: **750.29**
- **Archetype:** `file_cluster_4` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z +1.08)
- **Magnitude:** 88.6 | **LOC:** 98 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `deserializeCanvasArg` (Many-Argument Workhorses, Impact: 39.4), `variableListFor` (Compute Cores, Impact: 5.8)

### 5. `src/sentry/lang/native/symbolicator.py` (PYTHON) -> Cumulative Risk: **732.18**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.16)
- **Magnitude:** 312.32 | **LOC:** 536 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9997%), Documentation (94.4444%), Safety Score (92.8001%)
- **Heaviest Functions:** `_request` (Many-Argument Workhorses, Impact: 28.4), `_process` (Many-Argument Workhorses, Impact: 23.4), `process_js` (Many-Argument Workhorses, Impact: 10.8)

### 6. `src/sentry/snuba/entity_subscription.py` (PYTHON) -> Cumulative Risk: **723.67**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +0.21)
- **Magnitude:** 568.14 | **LOC:** 701 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (96.4916%)
- **Heaviest Functions:** `build_rpc_request` (Many-Argument Workhorses, Impact: 37.7), `get_entity_subscription` (Many-Argument Workhorses, Impact: 28.7), `build_query_builder` (Many-Argument Workhorses, Impact: 23.7)

### 7. `src/sentry/notifications/notification_action/action_validation.py` (PYTHON) -> Cumulative Risk: **722.23**
- **Archetype:** `file_cluster_15` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z -0.86)
- **Magnitude:** 157.58 | **LOC:** 279 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9919%), State Flux (99.9686%)
- **Heaviest Functions:** `clean_data` (Defensive Guards, Impact: 18.9), `_get_teams` (Generic / Templated Code, Impact: 6.2), `_get_services` (Generic / Templated Code, Impact: 4.7)

### 8. `src/sentry/integrations/github_enterprise/webhook.py` (PYTHON) -> Cumulative Risk: **721.68**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +0.02)
- **Magnitude:** 207.24 | **LOC:** 364 | **CtrlFlow:** 11.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9995%), Tech Debt (92.1369%)
- **Heaviest Functions:** `_handle` (Many-Argument Workhorses, Impact: 40.1), `is_valid_signature` (Many-Argument Workhorses, Impact: 12.9), `get_secret` (Compute Cores, Impact: 6.3)

### 9. `src/sentry/integrations/vsts/client.py` (PYTHON) -> Cumulative Risk: **715.12**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z -1.14)
- **Magnitude:** 283.64 | **LOC:** 460 | **CtrlFlow:** 9.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9486%), Tech Debt (97.3207%), Documentation (95.3125%)
- **Heaviest Functions:** `update_work_item` (Many-Argument Workhorses, Impact: 35.0), `create_work_item` (Many-Argument Workhorses, Impact: 11.7), `_refresh_auth_if_expired` (Compute Cores, Impact: 9.9)

### 10. `src/sentry/api/serializers/models/rule.py` (PYTHON) -> Cumulative Risk: **715.06**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +0.65)
- **Magnitude:** 897.52 | **LOC:** 809 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 57.1%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (98.1094%)
- **Heaviest Functions:** `get_attrs` (Many-Argument Workhorses, Impact: 110.5), `get_attrs` (Many-Argument Workhorses, Impact: 101.8), `serialize` (Many-Argument Workhorses, Impact: 70.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `api-docs/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/sentry/testutils/pytest/template/credentials.json` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.000175
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `static/app/views/dashboards/widgets/tableWidget/tableWidgetVisualization.stories.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 4338.38 | **LOC:** 520 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (9.7359%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 81`, `args: 31`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2`
* *Architecture:* `io: 7`, `api: 1`, `import: 14`
* *Defense:* `safety: 41`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` styled, badge, button, code, react, stories, eventView, fieldRenderers...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `static/app/views/dashboards/widgetBuilder/components/visualize/index.spec.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 4217.37 | **LOC:** 1996 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (19.5185%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 257`, `args: 66`, `func_start: 55`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 2`
* *Architecture:* `concurrency: 202`, `import: 10`
* *Defense:* `safety: 11`, `test: 230`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` organization, reactTestingLibrary, group, fields, useCustomMeasurements, useNavigate, types, visualize...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/sentry/testutils/cases.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 3556.38 | **LOC:** 4265 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 20.0%
- **Risk Profile:** Cognitive Load (82.8607%), Tech Debt (28.1132%)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.949
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.100762
  * `Imports (Out-Degree: 85):` ..shared_integrations.client.proxy, ..snuba.metrics, ..snuba.metrics.naming_layer.mri, ..types.cell, .asserts, .factories, .fixtures, .helpers...
  * `Imported By (In-Degree: 1794):` (Excluded from Brief to save tokens)

### `tests/snuba/api/endpoints/test_organization_events.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 2915.72 | **LOC:** 7447 | **CtrlFlow:** 2.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (22.4374%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_functions_dataset_simple` **(Compute Cores)** (Impact: 25.5)
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
* *Architecture:* `io: 2`, `api: 220`, `import: 28`
* *Defense:* `safety: 1065`, `doc: 13`, `test: 221`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.123
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.001297
  * `Imports (Out-Degree: 18):` datetime, django.test, django.urls, django.utils, math, pytest, sentry.discover.models, sentry.issues.grouptype...
  * `Imported By (In-Degree: 23):` (Excluded from Brief to save tokens)

### `tests/sentry/integrations/github/test_platform_detection.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 2352.08 | **LOC:** 2335 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (27.6757%), Tech Debt (0.0%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` __future__, base64, collections, pytest, sentry.integrations.github.platform_detection, sentry.shared_integrations.exceptions, sentry.utils, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/sentry/testutils/factories.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 2059.64 | **LOC:** 2808 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (71.7844%), Tech Debt (8.3213%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.671
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.076482
  * `Imports (Out-Degree: 120):` __future__, base64, binascii, collections.abc, contextlib, copy, datetime, django.conf...
  * `Imported By (In-Degree: 74):` (Excluded from Brief to save tokens)

### `src/sentry/search/events/builder/metrics.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1975.6 | **LOC:** 1920 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.0835%), Tech Debt (19.9585%)
**Top Internal Functions/Classes:**
  * `run_query` **(Many-Argument Workhorses)** (Impact: 124.4)
  * `resolve_snql_function` **(Many-Argument Workhorses)** (Impact: 61.2)
  * `_get_metrics_query_from_on_demand_spec` **(Many-Argument Workhorses)** (Impact: 57.6)
  * `default_filter_converter` **(Compute Cores)** (Impact: 53.9)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 48.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 276 instances
* *State Mutation (weighted view):* 865
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 425`, `structural_boundaries: 293`, `args: 62`, `func_start: 62`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 78`, `state_mutation: 313`, `dead_code: 5`, `planned_debt: 6`, `duplicate_logic: 3`
* *Architecture:* `api: 50`, `import: 37`
* *Defense:* `safety: 31`, `doc: 23`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.052299
  * `Imports (Out-Degree: 24):` __future__, collections, collections.abc, datetime, django.utils.functional, sentry, sentry.api.event_search, sentry.exceptions...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `static/app/components/searchQueryBuilder/index.spec.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1887.68 | **LOC:** 5936 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (95.335%), Tech Debt (9.2279%)
**Top Internal Functions/Classes:**
  * `AskSeerTestComponent` **(Defensive Guards)** (Impact: 32.1)
  * `mutationFn` **(Defensive Guards)** (Impact: 30.3)
  * `parameterDependentValueType` **(Defensive Guards)** (Impact: 11.5)
  * `aggregateGetFieldDefinition` **(Compute Cores)** (Impact: 9.5)
  * `getSuggestedFilterKey` **(Interface Declarations)** (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 109 instances
* *Amplified Cascading Flux:* 18 instances
* *Concurrency (weighted view):* 1610
* *State Mutation (weighted view):* 68
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 232`, `structural_boundaries: 1308`, `args: 419`, `func_start: 249`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 32`, `dead_code: 3`, `fragile_debt: 3`, `unreferenced_by_name: 2`
* *Architecture:* `io: 1`, `concurrency: 1065`, `import: 14`
* *Defense:* `safety: 64`, `test: 945`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` live-announcer, react, reactTestingLibrary, utils, datePicker, searchQueryBuilder, askSeerComboBox, context...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `static/app/views/insights/pages/conversations/hooks/useConversation.spec.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1847.77 | **LOC:** 418 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (12.0124%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 58`, `args: 31`, `func_start: 9`
* *Risk/State:* None
* *Architecture:* `io: 2`, `concurrency: 18`, `import: 4`
* *Defense:* `safety: 20`, `test: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` useConversation, organization, reactTestingLibrary, types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/sentry/search/events/builder/base.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1812.54 | **LOC:** 1675 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.5777%), Tech Debt (10.4684%)
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
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 254`, `dead_code: 1`, `planned_debt: 8`
* *Architecture:* `api: 58`, `import: 30`
* *Defense:* `safety: 58`, `doc: 25`, `sync_locks: 34`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.092
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.059112
  * `Imports (Out-Degree: 19):` __future__, collections.abc, datetime, django.utils.functional, parsimonious.exceptions, re, sentry, sentry.api...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `src/sentry/event_manager.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1808.08 | **LOC:** 2797 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (58.3858%), Tech Debt (19.0282%)
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
* *Risk/State:* `safety_bypasses: 58`, `state_mutation: 352`, `dead_code: 4`, `planned_debt: 1`, `fragile_debt: 13`
* *Architecture:* `io: 3`, `api: 38`, `import: 110`
* *Defense:* `safety: 47`, `doc: 21`, `sync_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.353
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.068801
  * `Imports (Out-Degree: 81):` .ingest.types, .utils.event_tracker, __future__, collections.abc, dataclasses, datetime, django.conf, django.core.cache...
  * `Imported By (In-Degree: 57):` (Excluded from Brief to save tokens)

### `src/sentry/utils/snuba.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1801.28 | **LOC:** 2261 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (57.5458%), Tech Debt (13.008%)
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
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 272`, `dead_code: 1`, `planned_debt: 12`, `fragile_debt: 2`
* *Architecture:* `io: 4`, `api: 72`, `import: 45`
* *Defense:* `safety: 58`, `doc: 39`, `sync_locks: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.649
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.085125
  * `Imports (Out-Degree: 23):` __future__, collections, collections.abc, contextlib, copy, dataclasses, datetime, dateutil.parser...
  * `Imported By (In-Degree: 132):` (Excluded from Brief to save tokens)

### `src/sentry/incidents/logic.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1799.06 | **LOC:** 2052 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (60.34%), Tech Debt (9.0458%)
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
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 236`, `dead_code: 4`, `planned_debt: 5`
* *Architecture:* `api: 50`, `import: 70`
* *Defense:* `safety: 18`, `doc: 19`, `sync_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.092
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.069003
  * `Imports (Out-Degree: 48):` __future__, bisect, collections.abc, copy, dataclasses, datetime, django.db, django.db.models...
  * `Imported By (In-Degree: 33):` (Excluded from Brief to save tokens)

### `src/sentry/tagstore/snuba/backend.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1774.8 | **LOC:** 1992 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (65.2006%), Tech Debt (9.4761%)
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
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 261`, `dead_code: 1`, `planned_debt: 4`, `fragile_debt: 1`
* *Architecture:* `api: 36`, `import: 56`
* *Defense:* `safety: 9`, `doc: 4`, `sync_locks: 12`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.102
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.058858
  * `Imports (Out-Degree: 35):` __future__, collections, collections.abc, datetime, dateutil.parser, django.core.cache, functools, logging...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `static/eslint/eslintPluginSentry/no-default-exports.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1753.6 | **LOC:** 284 | **CtrlFlow:** 10.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (6.8464%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 89`, `args: 24`, `func_start: 22`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `api: 58`, `import: 2`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` no-default-exports, rule-tester
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `static/app/views/performance/newTraceDetails/traceModels/traceTree.autogrouping.spec.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1746.53 | **LOC:** 899 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.1533%), Tech Debt (8.2824%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 81`, `args: 59`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 36`, `planned_debt: 1`
* *Architecture:* `io: 9`, `concurrency: 34`, `import: 5`
* *Defense:* `safety: 2`, `test: 78`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` traceGuards, traceTree, organization, traceTreeTestUtils, tracePreferences
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/sentry/snuba/test_discover_query.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1692.48 | **LOC:** 3454 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.1646%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_snql_wip_project_threshold_config` **(Defensive Guards)** (Impact: 23.8)
  * `test_count_miserable_function` **(Compute Cores)** (Impact: 13.0)
  * `test_user_misery_function` **(Compute Cores)** (Impact: 13.0)
  * `test_apdex_function` **(Compute Cores)** (Impact: 12.2)
  * `test_failure_rate` **(Defensive Guards)** (Impact: 12.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 213 instances
* *Api Near Db Sink:* 29 instances
* *State Mutation (weighted view):* 978
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 172`, `structural_boundaries: 424`, `args: 107`, `func_start: 99`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 552`, `dead_code: 1`, `unreferenced_by_name: 95`
* *Architecture:* `api: 100`, `import: 16`
* *Defense:* `safety: 266`, `doc: 1`, `test: 111`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` __future__, datetime, django.utils, pytest, sentry.discover.arithmetic, sentry.discover.models, sentry.exceptions, sentry.models.projectteam...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `static/app/views/settings/components/dataScrubbing/modals/add.spec.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1677.68 | **LOC:** 1040 | **CtrlFlow:** 2.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (21.6834%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Concurrency (weighted view):* 140
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 155`, `args: 34`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 4`
* *Architecture:* `io: 3`, `concurrency: 95`, `import: 11`
* *Defense:* `safety: 12`, `test: 95`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` dataScrubbingRelayPiiConfig, log, organization, reactTestingLibrary, selectEvent, components, organizationContext, convertRelayPiiConfig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/sentry/issues/endpoints/test_organization_group_index.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1672.22 | **LOC:** 4525 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (21.7284%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_query_status_and_substatus_nonoverlapping` **(Type Conversions)** (Impact: 18.0)
  * `test_assigned_to_pagination` **(Defensive Guards)** (Impact: 15.1)
    * *Intent:* # This seems like a random override, but this test needed a way to override # the orderby being sent...
  * `test_query_status_and_substatus_overlapping` **(Compute Cores)** (Impact: 14.0)
  * `test_bulk_delete_for_many_projects_without_option` **(Defensive Guards)** (Impact: 13.2)
  * `test_semver` **(Defensive Guards)** (Impact: 13.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 72 instances
* *State Mutation (weighted view):* 889
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 1149`, `args: 145`, `func_start: 145`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 745`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 2`, `duplicate_logic: 2`, `unreferenced_by_name: 134`
* *Architecture:* `api: 146`, `import: 61`
* *Defense:* `safety: 789`, `doc: 10`, `test: 161`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 45):` __future__, collections, collections.abc, datetime, django.db.utils, django.urls, django.utils, functools...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/sentry/snuba/test_transactions.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1668.76 | **LOC:** 3170 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (26.479%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_snql_wip_project_threshold_config` **(Defensive Guards)** (Impact: 23.8)
  * `test_count_miserable_function` **(Compute Cores)** (Impact: 13.0)
  * `test_user_misery_function` **(Compute Cores)** (Impact: 13.0)
  * `test_apdex_function` **(Compute Cores)** (Impact: 12.2)
  * `test_failure_rate` **(Defensive Guards)** (Impact: 12.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 194 instances
* *Api Near Db Sink:* 31 instances
* *State Mutation (weighted view):* 1010
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 155`, `structural_boundaries: 408`, `args: 101`, `func_start: 94`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 622`, `dead_code: 1`, `unreferenced_by_name: 90`
* *Architecture:* `api: 95`, `import: 16`
* *Defense:* `safety: 255`, `doc: 1`, `test: 106`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` __future__, datetime, django.utils, pytest, sentry.discover.arithmetic, sentry.discover.models, sentry.exceptions, sentry.models.projectteam...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `static/app/views/dashboards/widgetBuilder/components/sortBySelector.spec.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1665.58 | **LOC:** 445 | **CtrlFlow:** 8.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.2597%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 76`, `args: 16`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1`
* *Architecture:* `concurrency: 62`, `import: 8`
* *Defense:* `safety: 19`, `test: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` organization, reactTestingLibrary, organization, unicode, useNavigate, sortBySelector, widgetBuilderContext
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `static/app/utils/useLocalStorageState.spec.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1613.74 | **LOC:** 253 | **CtrlFlow:** 9.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (13.4071%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 65`, `args: 55`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`
* *Architecture:* `io: 2`, `concurrency: 4`, `import: 3`
* *Defense:* `safety: 8`, `test: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` reactTestingLibrary, localStorage, useLocalStorageState
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/sentry/seer/autofix/autofix_agent.py` -> Churn: **67.12%** | Cog Load: 55.9729% | Debt: 0.0%
- `src/sentry/core/endpoints/organization_details.py` -> Churn: **60.99%** | Cog Load: 63.9944% | Debt: 9.0537%
- `src/sentry/spans/buffer.py` -> Churn: **60.99%** | Cog Load: 79.9493% | Debt: 10.1193%
- `src/sentry/testutils/cases.py` -> Churn: **60.99%** | Cog Load: 82.8607% | Debt: 28.1132%
- `src/sentry/seer/autofix/autofix.py` -> Churn: **58.56%** | Cog Load: 60.8562% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `static/app/views/dashboards/widgets/tableWidget/tableWidgetVisualization.stories.tsx` -> **Josh Goldberg ✨** (100.0% isolated ownership) | Magnitude: 4338.38
- `src/sentry/testutils/factories.py` -> **Lyn Nagara** (100.0% isolated ownership) | Magnitude: 2059.64
- `static/app/views/insights/pages/conversations/hooks/useConversation.spec.tsx` -> **Ogi** (100.0% isolated ownership) | Magnitude: 1847.77
- `static/eslint/eslintPluginSentry/no-default-exports.spec.ts` -> **Josh Goldberg ✨** (100.0% isolated ownership) | Magnitude: 1753.6
- `static/app/utils/useLocalStorageState.spec.tsx` -> **Josh Goldberg ✨** (100.0% isolated ownership) | Magnitude: 1613.74

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/sentry/types/group.py` -> **Severity: 18.829** (Embedded: 0.2399 * Error Risk: 78.474%)
- `src/sentry/constants.py` -> **Severity: 15.201** (Embedded: 0.1818 * Error Risk: 83.6275%)
- `src/sentry/seer/autofix/constants.py` -> **Severity: 13.385** (Embedded: 0.1365 * Error Risk: 98.0326%)
- `static/app/components/events/contexts/platformContext/react.tsx` -> **Severity: 13.196** (Embedded: 0.2179 * Error Risk: 60.5532%)
- `src/sentry/testutils/helpers/datetime.py` -> **Severity: 12.896** (Embedded: 0.1856 * Error Risk: 69.4842%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `static/app/components/events/contexts/platformContext/react.tsx` -> **Severity: 5561.7** (Blast Radius: 55.617 * Doc Risk: 100.0%)
- `src/sentry/metrics/logging.py` -> **Severity: 1907.3** (Blast Radius: 19.073 * Doc Risk: 100.0%)
- `src/sentry/utils/db.py` -> **Severity: 1359.5** (Blast Radius: 13.595 * Doc Risk: 100.0%)
- `src/sentry/testutils/helpers/datetime.py` -> **Severity: 1156.418** (Blast Radius: 14.134 * Doc Risk: 81.8182%)
- `src/sentry/metrics/sentry_sdk.py` -> **Severity: 906.546** (Blast Radius: 9.713 * Doc Risk: 93.3333%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
