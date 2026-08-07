# ARCHITECTURAL_BRIEF: sentry
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_python/sentry` |
| **Timestamp** | `2026-08-07T04:03:46.589557+00:00` |
| **Scan Duration** | `63.03s` |
| **Git Branch** | `master` |
| **Git Commit** | `9dd18724889684bca65cbd14dd34918bf2bbeb63` |
| **Git Remote** | `https://github.com/getsentry/sentry.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 14213 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are a Senior Technical Storyteller and Codebase Architect. GitGalaxy has translated the non-visual architecture of this repository into measurable Structural Signatures (regex-derived counts, not an AST or compiler pass). Your job is to weave those signatures into a coherent, factual narrative about how this system is built -- its architecture, design patterns, and complexity -- not to render a verdict.
> 
> **CORE DIRECTIVES:**
> 1. **Narrate the Architecture, Don't Judge the Author:** Frame every observation as a blameless description of the system's physical reality. High Risk Exposure (e.g., Cognitive Load Exposure) describes where the architecture may be drifting into fragile territory, not developer incompetence -- it is a prompt to investigate, never a verdict.
> 2. **The Physical Reality Rule:** Base your narrative strictly on the provided Structural Signatures and the numbers derived from them. Do not hallucinate meaning, and do not restate a heuristic's raw label (e.g. a 'Logic Bomb' or 'O(2^N)' flag) as a confirmed finding of malice or a guaranteed defect -- explain what the signature actually measures, weave it into the story of the file, and let the reader draw their own conclusion.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`. Tell that balance as part of the narrative, not as an isolated alarm.
> 
> **THE STRUCTURAL SIGNATURE LEXICON:**
> * **Structure & Mass:** `branch` (splits), `linear` (paths), `args` (coupling), `func_start` (entry points).
> * **Risk & Volatility:** `danger` (dynamic execution), `flux` (state mutation), `graveyard` (commented-out logic), `safety_neg` (security bypasses).
> * **Architecture & Domain:** `io` (network latency), `concurrency` (async orchestration), `api` (public surface), `import` (dependencies).
> * **Defensive Guardrails:** `safety` (Error handling), `freeze_hits` (immutability), `cleanup` (state destruction).
## 2. THE 13-POINT RISK EXPOSURE ANALYSIS (EQUATIONS & CONTEXT)
> **How the SAST Engine Calculates Risk Exposure (Lower Risk 0 - Higher Risk Exposure 100%):**
> Most scores use a Sigmoid curve based on density (Hits / LOC) to prevent massive files from mathematically hiding their flaws.
> 
> 1. **Cognitive Load Exposure:** Measures the mental effort required for a developer to read and understand the file. `Density(Branches + (Flux * 2) + Async/Danger)` mitigated by `Doc Coverage`.
> 2. **Error & Exception Risk Exposure:** Measures structural integrity and resilience against runtime errors. `Net Exposure = (Danger + Safety_Neg + Flux) - (Safety + Tests + Docs)`.
> 3. **Tech Debt Exposure:** Measures the density of developer-annotated structural stress. `Density(TODOs [1x] + FIXMEs/Hacks [3x] + Empty Stubs [0.5x])`.
> 4. **Verification Risk Exposure:** Evaluates test coverage by comparing a function's structural complexity against the scope of the tests validating it.
> 5. **API Risk Exposure:** Measures the public surface area of a module. `Ratio(API Hits / Total Functions & Classes)`.
> 6. **Concurrency Risk Exposure:** Measures the density of asynchronous operations, threading, and parallel execution logic.
> 7. **State Flux Risk Exposure:** Measures the frequency of data mutation and variable reassignment.
> 8. **Commented Logic (dead code):** Measures the presence of abandoned, commented-out logic blocks.
> 9. **Spec Match Risk Exposure:** Measures how closely code aligns with formal specifications or architectural requirements.
> 10. **Stability:** Measures the recency of edits relative to the repository's entire lifespan.
> 11. **Deep Churn:** Measures the historical volatility and frequency of modification.
> 12. **Documentation Risk Exposure:** Measures the lack of structured documentation and ownership metadata.
> 13. **Indentation Consistency:** Measures formatting alignment (Tabs vs. Spaces). Provided for codebase standardization context, not a functional risk.
> 
> **--- THE SECURITY & VULNERABILITY LENS ---**
> 14. **Obfuscation & Evasion Risk:** Measures the density of obfuscated logic, packed strings, and non-standard encoding.
> 15. **Logic Bomb / Sabotage Risk:** Measures condition-heavy execution leading to destructive OS, memory, or process commands.
> 16. **Injection Surface Risk Exposure:** Measures external network/I/O input flowing directly into dynamic execution contexts (XSS, SQLi, RCE).
> 17. **Memory Corruption Risk Exposure:** Measures the density of raw pointer math and manual memory allocations (Buffer Overflows, UAF).
> 18. **Secrets Risk Exposure:** Measures the presence of hardcoded credentials exposed to logs or globals.
> 
> **--- STRUCTURAL MAGNITUDE (NOT RISK) ---**
> **19. Function Magnitude (Impact Score):** Measures the physical footprint and 'heaviness' of a specific function. `((BranchHits + 1) * (Args + 1) + (0.05 * LOC)) * 10`. This is NOT a risk score.
> **20. File Magnitude (Total Impact):** Measures the total structural impact of a file. `Sum(Function Impacts) + API + Concurrency + Flux + (LOC / 50)`. This is NOT a risk score.

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 20173 |
| Analyzed Artifacts (Scanned) | 15456 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 4717 |
| Total LOC | 1994755 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 76.6% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0947 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 8.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 691 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 7645 | 1169084 | 49.5% |
| TYPESCRIPT | 6516 | 728747 | 42.2% |
| JSON | 559 | 79579 | 3.6% |
| XML | 210 | 421 | 1.4% |
| HTML | 183 | 8507 | 1.2% |
| PLAINTEXT | 152 | 3 | 1.0% |
| MARKDOWN | 95 | 0 | 0.6% |
| CSS | 37 | 5062 | 0.2% |
| JAVASCRIPT | 27 | 1431 | 0.2% |
| LUA | 12 | 836 | 0.1% |
| SHELL | 11 | 312 | 0.1% |
| YAML | 7 | 497 | 0.0% |
| MAKEFILE | 1 | 201 | 0.0% |
| DOCKERFILE | 1 | 75 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.416`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 7925 | 51.3% |
| file_cluster_13 | 6148 | 39.8% |
| file_cluster_16 | 365 | 2.4% |
| file_cluster_2 | 248 | 1.6% |
| file_cluster_0 | 229 | 1.5% |
| file_cluster_17 | 152 | 1.0% |
| file_cluster_4 | 17 | 0.1% |
| file_cluster_11 | 5 | 0.0% |
| file_cluster_9 | 3 | 0.0% |
| file_cluster_12 | 3 | 0.0% |
| Unknown | 3 | 0.0% |
| file_cluster_6 | 2 | 0.0% |
| file_cluster_1 | 1 | 0.0% |
| file_cluster_7 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 244 | 1.6% |
| Static: Minified & Vendor Opaque Mass | 110 | 0.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 4717*

**Composition by Extension & Reason:**
- `.tsx`: 2155x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 79x Excluded (Saturation: Line 7 exceeds 500 chars), 5x Excluded (Saturation: Line 12 exceeds 500 chars)
- `.pysnap`: 1502x Excluded (Unsupported Extension: '.pysnap'), 22x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 188x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 9x Excluded (Machine-Generated Source Code Signature: 26 LOC), 6x Excluded (Machine-Generated Source Code Signature: 20 LOC)
- `.json`: 128x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 1478 LOC), 1x Excluded (Static Asset Blob without Intent: 1142 LOC)
- `.png`: 76x Excluded (Explicitly Denied Extension: '.png')
- `.ts`: 69x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Unsupported Format (.undeterminable), 1x Excluded (Machine-Generated Source Code Signature: 432 LOC)
- `.md`: 71x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mo`: 49x Excluded (Binary Format Detected)
- `.po`: 12x Unsupported Format (.po), 4x Excluded (Monolithic Amalgamation: 45259 LOC exceeds safe regex boundaries), 2x Excluded (Monolithic Amalgamation: 45266 LOC exceeds safe regex boundaries)
- `.yml`: 46x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable), 3x Excluded (Binary Format Detected)
- `.js`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.woff2`: 15x Excluded (Explicitly Denied Extension: '.woff2')
- `.map`: 11x Excluded (Unsupported Extension: '.map'), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jpg`: 9x Excluded (Explicitly Denied Extension: '.jpg')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 9.4 | 5.9 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 23.8 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 22.6 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 7.1 | 2.3 | 0.0 |
| API Exposure | 0.0 | 20.0 | 4.8 | 4.6 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 3.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 9.7 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 99.0 | 0.4 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 88.0 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.3 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 5.4 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 27.7 | 19.9 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `static/app/components/illustrations/NoProjectEmptyState.tsx` (Hits: 282)
- `static/gsApp/components/features/illustrations/discoverBackground.tsx` (Hits: 102)
- `tests/sentry/backup/test_imports.py` (Hits: 98)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **react.tsx** (`static/app/components/events/contexts/platformContext/react.tsx`) — 2980 inbound connections
2. **cases.py** (`src/sentry/testutils/cases.py`) — 1750 inbound connections
3. **datetime.py** (`src/sentry/testutils/helpers/datetime.py`) — 1368 inbound connections
4. **useOrganization.tsx** (`static/app/utils/useOrganization.tsx`) — 1309 inbound connections
5. **layout.html** (`src/sentry/templates/sentry/layout.html`) — 1222 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **urls.py** (`src/sentry/api/urls.py`) — 475 outbound dependencies
2. **routes.tsx** (`static/app/router/routes.tsx`) — 310 outbound dependencies
3. **index.tsx** (`static/app/icons/index.tsx`) — 149 outbound dependencies
4. **factories.py** (`src/sentry/testutils/factories.py`) — 148 outbound dependencies
5. **cases.py** (`src/sentry/testutils/cases.py`) — 137 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `translate_wildcard` (@ `src/sentry/api/event_search.py`) -> Impact: **675.5** | LOC: 1711
- `test_project_in_query_not_in_header` (@ `tests/snuba/api/endpoints/test_organization_events.py`) -> Impact: **531.8** | LOC: 5474
- `get_snuba_column_name` (@ `src/sentry/utils/snuba.py`) -> Impact: **469.6** | LOC: 1009
  * *Intent:* # Our calls to snuba frequently fail due to network issues. We want to # automatically retry most requests. Some of our POSTs and all of our DELETEs #...
- `validate_slug` (@ `src/sentry/core/endpoints/project_details.py`) -> Impact: **438.8** | LOC: 878
- `test_invalid_field` (@ `tests/sentry/releases/endpoints/test_organization_release_health_data.py`) -> Impact: **392.4** | LOC: 2548
- `onChange` (@ `static/app/views/discover/table/queryField.tsx`) -> Impact: **329.4** | LOC: 627
- `get_new_issue_fields` (@ `src/sentry_plugins/jira/plugin.py`) -> Impact: **321.9** | LOC: 511
- `cross_region_export_timeout_check` (@ `src/sentry/relocation/tasks/process.py`) -> Impact: **320.8** | LOC: 1216
- `run_post_process_job` (@ `src/sentry/tasks/post_process.py`) -> Impact: **320.4** | LOC: 927
- `escapeBashString` (@ `static/app/components/events/interfaces/utils.tsx`) -> Impact: **304.8** | LOC: 415
  * *Intent:* /**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/sentry/integrations/jira_server` | 6 | 14665.88 | 7.24% | 7.09% |
| `tests/snuba/api/endpoints` | 67 | 14015.42 | 3.37% | 0.0% |
| `src/sentry/integrations/jira` | 5 | 13789.73 | 5.75% | 9.08% |
| `src/sentry/api/endpoints` | 156 | 10294.25 | 9.2% | 10.43% |
| `tests/sentry/api/endpoints` | 144 | 8405.0 | 3.36% | 0.0% |
| `src/sentry/models` | 122 | 7430.54 | 10.03% | 12.82% |
| `src/sentry/utils` | 98 | 6687.35 | 17.1% | 20.68% |
| `__monolith__` | 20 | 5321.38 | 3.28% | 11.75% |
| `src/sentry/testutils/pytest/template` | 2 | 5015.54 | 3.31% | 0.0% |
| `api-docs` | 4 | 5008.5 | 15.17% | 24.23% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `fixtures/page_objects/base.py` -> **100.0%** Exposure
- `fixtures/schema_validation.py` -> **100.0%** Exposure
- `fixtures/stubs-for-mypy/rediscluster/client.pyi` -> **100.0%** Exposure
- `src/flagpole/conditions.py` -> **100.0%** Exposure
- `src/sentry/api/decorators.py` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `bin/dump-command-help` -> **100.0%** Exposure
- `src/sentry/api/helpers/error_upsampling.py` -> **100.0%** Exposure
- `src/sentry/api/helpers/teams.py` -> **100.0%** Exposure
- `src/sentry/deletions/defaults/workflow.py` -> **100.0%** Exposure
- `src/sentry/digests/backends/base.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `static/app/utils/discover/eventView.spec.tsx` -> **0** Orphaned Functions | **287** Duplicates
- `static/app/views/dashboards/widgetBuilder/hooks/useWidgetBuilderState.spec.tsx` -> **2** Orphaned Functions | **275** Duplicates
- `static/gsApp/utils/billing.spec.tsx` -> **0** Orphaned Functions | **202** Duplicates
- `tests/sentry/dashboards/endpoints/test_organization_dashboard_details.py` -> **147** Orphaned Functions | **34** Duplicates
- `tests/sentry/tasks/test_post_process.py` -> **99** Orphaned Functions | **58** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`.github/workflows/scripts/compute-sentry-selected-tests.py`** -> AI Confidence: **99.39%**
2. **`bin/preprod/trigger_size_status_check`** -> AI Confidence: **99.39%**
3. **`src/sentry/explore/translation/discover_translation.py`** -> AI Confidence: **99.39%**
4. **`static/app/views/insights/browser/webVitals/queries/useSpanSamplesWebVitalsQuery.tsx`** -> AI Confidence: **99.39%**
5. **`static/app/views/performance/newTraceDetails/traceApi/useTrace.tsx`** -> AI Confidence: **99.39%**
6. **`static/app/views/releases/detail/overview/releaseComparisonChart/index.tsx`** -> AI Confidence: **99.39%**
7. **`static/app/views/seerExplorer/hooks/useAsciiSnapshot.tsx`** -> AI Confidence: **99.39%**
8. **`static/gsAdmin/components/customers/pendingChanges.tsx`** -> AI Confidence: **99.39%**
9. **`static/gsApp/utils/pendo.tsx`** -> AI Confidence: **99.39%**
10. **`build-utils/ts-extract-gettext.ts`** -> AI Confidence: **99.34%**
11. **`static/app/views/insights/sessions/queries/useOrganizationReleases.tsx`** -> AI Confidence: **99.34%**
12. **`.github/workflows/scripts/selective-testing/compute-selected-tests.py`** -> AI Confidence: **99.31%**
13. **`bin/preprod/trigger_pr_comment`** -> AI Confidence: **99.31%**
14. **`bin/send_metrics.py`** -> AI Confidence: **99.31%**
15. **`devenv/sync.py`** -> AI Confidence: **99.31%**
16. **`src/sentry/api/endpoints/organization_events_trace.py`** -> AI Confidence: **99.31%**
17. **`src/sentry/api/endpoints/organization_releases.py`** -> AI Confidence: **99.31%**
18. **`src/sentry/api/endpoints/project_symbol_sources.py`** -> AI Confidence: **99.31%**
19. **`src/sentry/api/endpoints/relay/project_configs.py`** -> AI Confidence: **99.31%**
20. **`src/sentry/api/endpoints/release_thresholds/health_checks/is_crash_free_rate_healthy.py`** -> AI Confidence: **99.31%**
21. **`src/sentry/api/endpoints/source_map_debug_blue_thunder_edition.py`** -> AI Confidence: **99.31%**
22. **`src/sentry/api/helpers/group_index/update.py`** -> AI Confidence: **99.31%**
23. **`src/sentry/api/paginator.py`** -> AI Confidence: **99.31%**
24. **`src/sentry/api/serializers/models/activity.py`** -> AI Confidence: **99.31%**
25. **`src/sentry/api/serializers/models/dashboard.py`** -> AI Confidence: **99.31%**
26. **`src/sentry/api/serializers/models/discoversavedquery.py`** -> AI Confidence: **99.31%**
27. **`src/sentry/api/serializers/models/group_stream.py`** -> AI Confidence: **99.31%**
28. **`src/sentry/api/serializers/models/plugin.py`** -> AI Confidence: **99.31%**
29. **`src/sentry/api/serializers/models/projectcodeowners.py`** -> AI Confidence: **99.31%**
30. **`src/sentry/api/serializers/models/release.py`** -> AI Confidence: **99.31%**
31. **`src/sentry/api/serializers/models/rule.py`** -> AI Confidence: **99.31%**
32. **`src/sentry/api/serializers/rest_framework/dashboard.py`** -> AI Confidence: **99.31%**
33. **`src/sentry/api/serializers/rest_framework/organizationmemberinvite.py`** -> AI Confidence: **99.31%**
34. **`src/sentry/api/validators/project_codeowners.py`** -> AI Confidence: **99.31%**
35. **`src/sentry/apidocs/hooks.py`** -> AI Confidence: **99.31%**
36. **`src/sentry/apidocs/spectacular_ports.py`** -> AI Confidence: **99.31%**
37. **`src/sentry/backup/comparators.py`** -> AI Confidence: **99.31%**
38. **`src/sentry/backup/imports.py`** -> AI Confidence: **99.31%**
39. **`src/sentry/backup/validate.py`** -> AI Confidence: **99.31%**
40. **`src/sentry/core/endpoints/organization_member_index.py`** -> AI Confidence: **99.31%**
41. **`src/sentry/core/endpoints/project_details.py`** -> AI Confidence: **99.31%**
42. **`src/sentry/dashboards/endpoints/organization_dashboards.py`** -> AI Confidence: **99.31%**
43. **`src/sentry/db/deletion.py`** -> AI Confidence: **99.31%**
44. **`src/sentry/discover/dashboard_widget_split.py`** -> AI Confidence: **99.31%**
45. **`src/sentry/discover/dataset_split.py`** -> AI Confidence: **99.31%**
46. **`src/sentry/discover/translation/mep_to_eap.py`** -> AI Confidence: **99.31%**
47. **`src/sentry/eventstream/item_helpers.py`** -> AI Confidence: **99.31%**
48. **`src/sentry/explore/endpoints/serializers.py`** -> AI Confidence: **99.31%**
49. **`src/sentry/explore/translation/dashboards_translation.py`** -> AI Confidence: **99.31%**
50. **`src/sentry/grouping/enhancer/__init__.py`** -> AI Confidence: **99.31%**
51. **`src/sentry/grouping/fingerprinting/utils.py`** -> AI Confidence: **99.31%**
52. **`src/sentry/grouping/ingest/grouphash_metadata.py`** -> AI Confidence: **99.31%**
53. **`src/sentry/grouping/parameterization.py`** -> AI Confidence: **99.31%**
54. **`src/sentry/hybridcloud/tasks/deliver_webhooks.py`** -> AI Confidence: **99.31%**
55. **`src/sentry/incidents/endpoints/serializers/alert_rule.py`** -> AI Confidence: **99.31%**
56. **`src/sentry/incidents/endpoints/serializers/workflow_engine_detector.py`** -> AI Confidence: **99.31%**
57. **`src/sentry/incidents/logic.py`** -> AI Confidence: **99.31%**
58. **`src/sentry/integrations/github/platform_detection.py`** -> AI Confidence: **99.31%**
59. **`src/sentry/integrations/perforce/client.py`** -> AI Confidence: **99.31%**
60. **`src/sentry/integrations/slack/message_builder/issues.py`** -> AI Confidence: **99.31%**
61. **`src/sentry/integrations/slack/unfurl/discover.py`** -> AI Confidence: **99.31%**
62. **`src/sentry/interfaces/stacktrace.py`** -> AI Confidence: **99.31%**
63. **`src/sentry/issue_detection/detectors/sql_injection_detector.py`** -> AI Confidence: **99.31%**
64. **`src/sentry/issues/auto_source_code_config/code_mapping.py`** -> AI Confidence: **99.31%**
65. **`src/sentry/killswitches.py`** -> AI Confidence: **99.31%**
66. **`src/sentry/lang/java/processing.py`** -> AI Confidence: **99.31%**
67. **`src/sentry/lang/javascript/processing.py`** -> AI Confidence: **99.31%**
68. **`src/sentry/lang/native/applecrashreport.py`** -> AI Confidence: **99.31%**
69. **`src/sentry/lang/native/processing.py`** -> AI Confidence: **99.31%**
70. **`src/sentry/management/commands/generate_controlsilo_urls.py`** -> AI Confidence: **99.31%**
71. **`src/sentry/management/commands/merge_users.py`** -> AI Confidence: **99.31%**
72. **`src/sentry/monitors/validators.py`** -> AI Confidence: **99.31%**
73. **`src/sentry/preprod/api/endpoints/preprod_artifact_admin_info.py`** -> AI Confidence: **99.31%**
74. **`src/sentry/preprod/api/endpoints/preprod_artifact_snapshot.py`** -> AI Confidence: **99.31%**
75. **`src/sentry/preprod/api/endpoints/project_preprod_artifact_update.py`** -> AI Confidence: **99.31%**
76. **`src/sentry/preprod/api/models/project_preprod_build_details_models.py`** -> AI Confidence: **99.31%**
77. **`src/sentry/preprod/artifact_search.py`** -> AI Confidence: **99.31%**
78. **`src/sentry/preprod/build_distribution_utils.py`** -> AI Confidence: **99.31%**
79. **`src/sentry/preprod/size_analysis/compare.py`** -> AI Confidence: **99.31%**
80. **`src/sentry/preprod/size_analysis/grouptype.py`** -> AI Confidence: **99.31%**
81. **`src/sentry/preprod/size_analysis/tasks.py`** -> AI Confidence: **99.31%**
82. **`src/sentry/preprod/snapshots/tasks.py`** -> AI Confidence: **99.31%**
83. **`src/sentry/preprod/tasks.py`** -> AI Confidence: **99.31%**
84. **`src/sentry/preprod/vcs/status_checks/size/tasks.py`** -> AI Confidence: **99.31%**
85. **`src/sentry/preprod/vcs/status_checks/size/templates.py`** -> AI Confidence: **99.31%**
86. **`src/sentry/preprod/vcs/status_checks/snapshots/tasks.py`** -> AI Confidence: **99.31%**
87. **`src/sentry/processing/backpressure/health.py`** -> AI Confidence: **99.31%**
88. **`src/sentry/profiles/flamegraph.py`** -> AI Confidence: **99.31%**
89. **`src/sentry/profiles/task.py`** -> AI Confidence: **99.31%**
90. **`src/sentry/quotas/redis.py`** -> AI Confidence: **99.31%**
91. **`src/sentry/release_health/eap_sessions_rollout.py`** -> AI Confidence: **99.31%**
92. **`src/sentry/release_health/metrics.py`** -> AI Confidence: **99.31%**
93. **`src/sentry/replays/usecases/ingest/event_parser.py`** -> AI Confidence: **99.31%**
94. **`src/sentry/replays/usecases/replay_counts.py`** -> AI Confidence: **99.31%**
95. **`src/sentry/replays/usecases/summarize.py`** -> AI Confidence: **99.31%**
96. **`src/sentry/rules/history/preview.py`** -> AI Confidence: **99.31%**
97. **`src/sentry/runner/commands/configoptions.py`** -> AI Confidence: **99.31%**
98. **`src/sentry/runner/commands/devserver.py`** -> AI Confidence: **99.31%**
99. **`src/sentry/search/eap/occurrences/common_queries.py`** -> AI Confidence: **99.31%**
100. **`src/sentry/search/eap/resolver.py`** -> AI Confidence: **99.31%**
101. **`src/sentry/search/eap/spans/filter_aliases.py`** -> AI Confidence: **99.31%**
102. **`src/sentry/search/events/builder/base.py`** -> AI Confidence: **99.31%**
103. **`src/sentry/search/events/builder/discover.py`** -> AI Confidence: **99.31%**
104. **`src/sentry/search/events/builder/metrics.py`** -> AI Confidence: **99.31%**
105. **`src/sentry/search/events/datasets/filter_aliases.py`** -> AI Confidence: **99.31%**
106. **`src/sentry/search/events/fields.py`** -> AI Confidence: **99.31%**
107. **`src/sentry/search/events/filter.py`** -> AI Confidence: **99.31%**
108. **`src/sentry/search/snuba/executors.py`** -> AI Confidence: **99.31%**
109. **`src/sentry/search/utils.py`** -> AI Confidence: **99.31%**
110. **`src/sentry/seer/assisted_query/discover_tools.py`** -> AI Confidence: **99.31%**
111. **`src/sentry/seer/assisted_query/issues_tools.py`** -> AI Confidence: **99.31%**
112. **`src/sentry/seer/autofix/autofix.py`** -> AI Confidence: **99.31%**
113. **`src/sentry/seer/autofix/autofix_agent.py`** -> AI Confidence: **99.31%**
114. **`src/sentry/seer/autofix/coding_agent.py`** -> AI Confidence: **99.31%**
115. **`src/sentry/seer/code_review/utils.py`** -> AI Confidence: **99.31%**
116. **`src/sentry/seer/explorer/client.py`** -> AI Confidence: **99.31%**
117. **`src/sentry/seer/explorer/context_engine_utils.py`** -> AI Confidence: **99.31%**
118. **`src/sentry/seer/explorer/explorer_service_map_utils.py`** -> AI Confidence: **99.31%**
119. **`src/sentry/seer/explorer/tools.py`** -> AI Confidence: **99.31%**
120. **`src/sentry/seer/explorer/utils.py`** -> AI Confidence: **99.31%**
121. **`src/sentry/services/eventstore/snuba/backend.py`** -> AI Confidence: **99.31%**
122. **`src/sentry/snuba/discover.py`** -> AI Confidence: **99.31%**
123. **`src/sentry/snuba/metrics/datasource.py`** -> AI Confidence: **99.31%**
124. **`src/sentry/snuba/metrics/mqb_query_transformer.py`** -> AI Confidence: **99.31%**
125. **`src/sentry/snuba/metrics/query.py`** -> AI Confidence: **99.31%**
126. **`src/sentry/snuba/metrics/query_builder.py`** -> AI Confidence: **99.31%**
127. **`src/sentry/snuba/metrics_layer/query.py`** -> AI Confidence: **99.31%**
128. **`src/sentry/snuba/metrics_performance.py`** -> AI Confidence: **99.31%**
129. **`src/sentry/snuba/rpc_dataset_common.py`** -> AI Confidence: **99.31%**
130. **`src/sentry/snuba/trace.py`** -> AI Confidence: **99.31%**
131. **`src/sentry/spans/buffer.py`** -> AI Confidence: **99.31%**
132. **`src/sentry/spans/buffer_logger.py`** -> AI Confidence: **99.31%**
133. **`src/sentry/spans/consumers/process/flusher.py`** -> AI Confidence: **99.31%**
134. **`src/sentry/spans/consumers/process_segments/convert.py`** -> AI Confidence: **99.31%**
135. **`src/sentry/stacktraces/functions.py`** -> AI Confidence: **99.31%**
136. **`src/sentry/stacktraces/processing.py`** -> AI Confidence: **99.31%**
137. **`src/sentry/tagstore/snuba/backend.py`** -> AI Confidence: **99.31%**
138. **`src/sentry/tasks/summaries/organization_report_context_factory.py`** -> AI Confidence: **99.31%**
139. **`src/sentry/testutils/pytest/metrics.py`** -> AI Confidence: **99.31%**
140. **`src/sentry/tsdb/redis.py`** -> AI Confidence: **99.31%**
141. **`src/sentry/tsdb/snuba.py`** -> AI Confidence: **99.31%**
142. **`src/sentry/users/services/user/serial.py`** -> AI Confidence: **99.31%**
143. **`src/sentry/utils/committers.py`** -> AI Confidence: **99.31%**
144. **`src/sentry/utils/email/manager.py`** -> AI Confidence: **99.31%**
145. **`src/sentry/utils/event_frames.py`** -> AI Confidence: **99.31%**
146. **`src/sentry/utils/query.py`** -> AI Confidence: **99.31%**
147. **`src/sentry/utils/safe.py`** -> AI Confidence: **99.31%**
148. **`src/sentry/utils/samples.py`** -> AI Confidence: **99.31%**
149. **`src/sentry/utils/snuba.py`** -> AI Confidence: **99.31%**
150. **`src/sentry/web/frontend/js_sdk_loader.py`** -> AI Confidence: **99.31%**
151. **`src/sentry/web/frontend/oauth_authorize.py`** -> AI Confidence: **99.31%**
152. **`src/sentry/workflow_engine/migration_helpers/issue_alert_dual_write.py`** -> AI Confidence: **99.31%**
153. **`src/sentry/workflow_engine/migrations/0084_crons_dedupe_workflows.py`** -> AI Confidence: **99.31%**
154. **`src/sentry/workflow_engine/migrations/0086_fix_cron_to_cron_workflow_links.py`** -> AI Confidence: **99.31%**
155. **`src/sentry/workflow_engine/migrations/0107_fix_email_action_fallthrough_type.py`** -> AI Confidence: **99.31%**
156. **`src/sentry/workflow_engine/processors/workflow.py`** -> AI Confidence: **99.31%**
157. **`src/sentry_plugins/github/webhooks/events/push.py`** -> AI Confidence: **99.31%**
158. **`src/sentry_plugins/jira/plugin.py`** -> AI Confidence: **99.31%**
159. **`tests/sentry/deletions/test_validate_group_related_models.py`** -> AI Confidence: **99.31%**
160. **`tests/sentry/grouping/test_categorization.py`** -> AI Confidence: **99.31%**
161. **`tests/sentry/rules/conditions/test_event_attribute.py`** -> AI Confidence: **99.31%**
162. **`tests/sentry/snuba/metrics/test_mqb_query_transformer.py`** -> AI Confidence: **99.31%**
163. **`tests/sentry/workflow_engine/handlers/condition/test_event_attribute_handler.py`** -> AI Confidence: **99.31%**
164. **`tools/flake8_plugin.py`** -> AI Confidence: **99.31%**
165. **`tools/migrations/squash.py`** -> AI Confidence: **99.31%**
166. **`tools/mypy_helpers/make_stub_ignores.py`** -> AI Confidence: **99.31%**
167. **`rspack.config.ts`** -> AI Confidence: **99.31%**
168. **`static/app/actionCreators/dashboards.tsx`** -> AI Confidence: **99.31%**
169. **`static/app/actionCreators/monitors.tsx`** -> AI Confidence: **99.31%**
170. **`static/app/actionCreators/navigation.tsx`** -> AI Confidence: **99.31%**
171. **`static/app/actionCreators/tags.tsx`** -> AI Confidence: **99.31%**
172. **`static/app/api.tsx`** -> AI Confidence: **99.31%**
173. **`static/app/bootstrap/initializeSdk.tsx`** -> AI Confidence: **99.31%**
174. **`static/app/components/actions/resolve.tsx`** -> AI Confidence: **99.31%**
175. **`static/app/components/activity/item/index.tsx`** -> AI Confidence: **99.31%**
176. **`static/app/components/alerts/snoozeAlert.tsx`** -> AI Confidence: **99.31%**
177. **`static/app/components/assistant/guideAnchor.tsx`** -> AI Confidence: **99.31%**
178. **`static/app/components/charts/baseChart.tsx`** -> AI Confidence: **99.31%**
179. **`static/app/components/charts/chartZoom.tsx`** -> AI Confidence: **99.31%**
180. **`static/app/components/charts/eventsChart.tsx`** -> AI Confidence: **99.31%**
181. **`static/app/components/charts/eventsRequest.tsx`** -> AI Confidence: **99.31%**
182. **`static/app/components/charts/miniBarChart.tsx`** -> AI Confidence: **99.31%**
183. **`static/app/components/charts/releaseSeries.tsx`** -> AI Confidence: **99.31%**
184. **`static/app/components/charts/useChartXRangeSelection.tsx`** -> AI Confidence: **99.31%**
185. **`static/app/components/core/avatar/avatarList.tsx`** -> AI Confidence: **99.31%**
186. **`static/app/components/core/code/codeBlock.tsx`** -> AI Confidence: **99.31%**
187. **`static/app/components/core/input/numberDragInput.tsx`** -> AI Confidence: **99.31%**
188. **`static/app/components/core/inspector.tsx`** -> AI Confidence: **99.31%**
189. **`static/app/components/core/menuListItem/menuListItem.tsx`** -> AI Confidence: **99.31%**
190. **`static/app/components/core/tabs/tab.tsx`** -> AI Confidence: **99.31%**
191. **`static/app/components/createAlertButton.tsx`** -> AI Confidence: **99.31%**
192. **`static/app/components/deprecatedforms/form.tsx`** -> AI Confidence: **99.31%**
193. **`static/app/components/deprecatedforms/formField.tsx`** -> AI Confidence: **99.31%**
194. **`static/app/components/dropdownMenu/item.tsx`** -> AI Confidence: **99.31%**
195. **`static/app/components/editableText.tsx`** -> AI Confidence: **99.31%**
196. **`static/app/components/events/autofix/autofixHighlightWrapper.tsx`** -> AI Confidence: **99.31%**
197. **`static/app/components/events/autofix/autofixRootCause.tsx`** -> AI Confidence: **99.31%**
198. **`static/app/components/events/autofix/autofixSteps.tsx`** -> AI Confidence: **99.31%**
199. **`static/app/components/events/autofix/insights/autofixInsightSources.tsx`** -> AI Confidence: **99.31%**
200. **`static/app/components/events/autofix/useAutofix.tsx`** -> AI Confidence: **99.31%**
201. **`static/app/components/events/autofix/useExplorerAutofix.tsx`** -> AI Confidence: **99.31%**
202. **`static/app/components/events/autofix/v2/autofixStatusCard.tsx`** -> AI Confidence: **99.31%**
203. **`static/app/components/events/autofix/v2/nextSteps.tsx`** -> AI Confidence: **99.31%**
204. **`static/app/components/events/breadcrumbs/breadcrumbItemContent.tsx`** -> AI Confidence: **99.31%**
205. **`static/app/components/events/contexts/knownContext/device.tsx`** -> AI Confidence: **99.31%**
206. **`static/app/components/events/contexts/knownContext/trace.tsx`** -> AI Confidence: **99.31%**
207. **`static/app/components/events/contexts/utils.tsx`** -> AI Confidence: **99.31%**
208. **`static/app/components/events/eventAttachmentActions.tsx`** -> AI Confidence: **99.31%**
209. **`static/app/components/events/eventSdk.tsx`** -> AI Confidence: **99.31%**
210. **`static/app/components/events/eventTags/eventTagsTreeRow.tsx`** -> AI Confidence: **99.31%**
211. **`static/app/components/events/groupingInfo/groupingVariant.tsx`** -> AI Confidence: **99.31%**
212. **`static/app/components/events/interfaces/analyzeFrames.tsx`** -> AI Confidence: **99.31%**
213. **`static/app/components/events/interfaces/crashContent/stackTrace/content.tsx`** -> AI Confidence: **99.31%**
214. **`static/app/components/events/interfaces/crashContent/stackTrace/nativeContent.tsx`** -> AI Confidence: **99.31%**
215. **`static/app/components/events/interfaces/frame/context.tsx`** -> AI Confidence: **99.31%**
216. **`static/app/components/events/interfaces/frame/deprecatedLine.tsx`** -> AI Confidence: **99.31%**
217. **`static/app/components/events/interfaces/frame/stacktraceLink.tsx`** -> AI Confidence: **99.31%**
218. **`static/app/components/events/interfaces/frame/usePrismTokensSourceContext.tsx`** -> AI Confidence: **99.31%**
219. **`static/app/components/events/interfaces/frame/utils.tsx`** -> AI Confidence: **99.31%**
220. **`static/app/components/events/interfaces/message.tsx`** -> AI Confidence: **99.31%**
221. **`static/app/components/events/interfaces/performance/spanEvidenceKeyValueList.tsx`** -> AI Confidence: **99.31%**
222. **`static/app/components/events/interfaces/request/index.tsx`** -> AI Confidence: **99.31%**
223. **`static/app/components/events/interfaces/stackTrace.tsx`** -> AI Confidence: **99.31%**
224. **`static/app/components/events/interfaces/threads.tsx`** -> AI Confidence: **99.31%**
225. **`static/app/components/events/interfaces/threads/threadSelector/index.tsx`** -> AI Confidence: **99.31%**
226. **`static/app/components/events/interfaces/utils.tsx`** -> AI Confidence: **99.31%**
227. **`static/app/components/events/traceEventDataSection.tsx`** -> AI Confidence: **99.31%**
228. **`static/app/components/events/viewHierarchy/utils.tsx`** -> AI Confidence: **99.31%**
229. **`static/app/components/featureFlags/hooks/useFlagsInEvent.tsx`** -> AI Confidence: **99.31%**
230. **`static/app/components/feedback/feedbackItem/feedbackActions.tsx`** -> AI Confidence: **99.31%**
231. **`static/app/components/feedback/feedbackItem/feedbackItemUsername.tsx`** -> AI Confidence: **99.31%**
232. **`static/app/components/feedback/feedbackItem/feedbackUrl.tsx`** -> AI Confidence: **99.31%**
233. **`static/app/components/feedback/useFetchFeedbackData.tsx`** -> AI Confidence: **99.31%**
234. **`static/app/components/forms/controls/rangeSlider/index.tsx`** -> AI Confidence: **99.31%**
235. **`static/app/components/forms/fieldGroup/index.tsx`** -> AI Confidence: **99.31%**
236. **`static/app/components/forms/formPanel.tsx`** -> AI Confidence: **99.31%**
237. **`static/app/components/forms/jsonForm.tsx`** -> AI Confidence: **99.31%**
238. **`static/app/components/globalDrawer/index.tsx`** -> AI Confidence: **99.31%**
239. **`static/app/components/group/groupSummary.tsx`** -> AI Confidence: **99.31%**
240. **`static/app/components/issueDiff/index.tsx`** -> AI Confidence: **99.31%**
241. **`static/app/components/keyValueData/index.tsx`** -> AI Confidence: **99.31%**
242. **`static/app/components/modals/debugFileCustomRepository/http.tsx`** -> AI Confidence: **99.31%**
243. **`static/app/components/modals/explore/saveQueryModal.tsx`** -> AI Confidence: **99.31%**
244. **`static/app/components/modals/privateGamingSdkAccessModal.tsx`** -> AI Confidence: **99.31%**
245. **`static/app/components/onboarding/gettingStartedDoc/utils/useLoadGettingStarted.ts`** -> AI Confidence: **99.31%**
246. **`static/app/components/onboarding/productSelection.tsx`** -> AI Confidence: **99.31%**
247. **`static/app/components/onboarding/useRecentCreatedProject.ts`** -> AI Confidence: **99.31%**
248. **`static/app/components/onboardingPanel.stories.tsx`** -> AI Confidence: **99.31%**
249. **`static/app/components/pageFilters/actions.tsx`** -> AI Confidence: **99.31%**
250. **`static/app/components/pageFilters/parse.tsx`** -> AI Confidence: **99.31%**
251. **`static/app/components/panels/panelTable.tsx`** -> AI Confidence: **99.31%**
252. **`static/app/components/preprod/preprodBuildsDistributionTable.tsx`** -> AI Confidence: **99.31%**
253. **`static/app/components/preprod/preprodBuildsTable.tsx`** -> AI Confidence: **99.31%**
254. **`static/app/components/preprod/preprodBuildsTableCommon.tsx`** -> AI Confidence: **99.31%**
255. **`static/app/components/profiling/flamegraph/continuousFlamegraph.tsx`** -> AI Confidence: **99.31%**
256. **`static/app/components/profiling/flamegraph/flamegraphContextMenu.tsx`** -> AI Confidence: **99.31%**
257. **`static/app/components/profiling/flamegraph/flamegraphDrawer/profileDetails.tsx`** -> AI Confidence: **99.31%**
258. **`static/app/components/profiling/suspectFunctions/suspectFunctionsTable.tsx`** -> AI Confidence: **99.31%**
259. **`static/app/components/replays/breadcrumbs/replayTimelineTooltip.tsx`** -> AI Confidence: **99.31%**
260. **`static/app/components/replays/replayContext.tsx`** -> AI Confidence: **99.31%**
261. **`static/app/components/scrollCarousel.tsx`** -> AI Confidence: **99.31%**
262. **`static/app/components/searchBar/searchDropdown.tsx`** -> AI Confidence: **99.31%**
263. **`static/app/components/searchQueryBuilder/askSeerCombobox/useAskSeerPolling.tsx`** -> AI Confidence: **99.31%**
264. **`static/app/components/searchQueryBuilder/hooks/useQueryBuilderGridItem.tsx`** -> AI Confidence: **99.31%**
265. **`static/app/components/searchQueryBuilder/hooks/useQueryBuilderState.tsx`** -> AI Confidence: **99.31%**
266. **`static/app/components/searchQueryBuilder/hooks/useUndoStack.tsx`** -> AI Confidence: **99.31%**
267. **`static/app/components/searchQueryBuilder/tokens/filter/valueSuggestions/utils.tsx`** -> AI Confidence: **99.31%**
268. **`static/app/components/slider/index.tsx`** -> AI Confidence: **99.31%**
269. **`static/app/components/stackTrace/frame/frameHeader.tsx`** -> AI Confidence: **99.31%**
270. **`static/app/components/stackTrace/issueStackTrace/issueSourceLinkAction.tsx`** -> AI Confidence: **99.31%**
271. **`static/app/components/stackTrace/issueStackTrace/issueSourceMapsDebuggerAction.tsx`** -> AI Confidence: **99.31%**
272. **`static/app/components/stackTrace/issueStackTrace/issueStackTraceFrameContext.tsx`** -> AI Confidence: **99.31%**
273. **`static/app/components/stream/group.tsx`** -> AI Confidence: **99.31%**
274. **`static/app/components/structuredEventData/index.tsx`** -> AI Confidence: **99.31%**
275. **`static/app/components/structuredEventData/recursiveStructuredData.tsx`** -> AI Confidence: **99.31%**
276. **`static/app/components/superuserStaffAccessForm.tsx`** -> AI Confidence: **99.31%**
277. **`static/app/components/timeRangeSelector/index.tsx`** -> AI Confidence: **99.31%**
278. **`static/app/components/timeSince.tsx`** -> AI Confidence: **99.31%**
279. **`static/app/components/tokenizedInput/token/comboBox.tsx`** -> AI Confidence: **99.31%**
280. **`static/app/components/tokenizedInput/token/inputBox.tsx`** -> AI Confidence: **99.31%**
281. **`static/app/components/version.tsx`** -> AI Confidence: **99.31%**
282. **`static/app/components/waitingForEvents.tsx`** -> AI Confidence: **99.31%**
283. **`static/app/components/workflowEngine/gridCell/titleCell.tsx`** -> AI Confidence: **99.31%**
284. **`static/app/plugins/components/issueActions.tsx`** -> AI Confidence: **99.31%**
285. **`static/app/stores/guideStore.tsx`** -> AI Confidence: **99.31%**
286. **`static/app/stories/apiReference.tsx`** -> AI Confidence: **99.31%**
287. **`static/app/stories/view/storyTree.tsx`** -> AI Confidence: **99.31%**
288. **`static/app/utils/discover/charts.tsx`** -> AI Confidence: **99.31%**
289. **`static/app/utils/discover/eventView.tsx`** -> AI Confidence: **99.31%**
290. **`static/app/utils/discover/genericDiscoverQuery.tsx`** -> AI Confidence: **99.31%**
291. **`static/app/utils/event/useEventCanShowReplayUpsell.tsx`** -> AI Confidence: **99.31%**
292. **`static/app/utils/events.tsx`** -> AI Confidence: **99.31%**
293. **`static/app/utils/profiling/flamegraph.ts`** -> AI Confidence: **99.31%**
294. **`static/app/utils/profiling/flamegraph/flamegraphStateProvider/flamegraphQueryParamSync.tsx`** -> AI Confidence: **99.31%**
295. **`static/app/utils/profiling/hooks/useProfileTopEventsStats.tsx`** -> AI Confidence: **99.31%**
296. **`static/app/utils/profiling/hooks/useVirtualizedTree/useVirtualizedTree.tsx`** -> AI Confidence: **99.31%**
297. **`static/app/utils/profiling/renderers/spansRenderer.tsx`** -> AI Confidence: **99.31%**
298. **`static/app/utils/projects.tsx`** -> AI Confidence: **99.31%**
299. **`static/app/utils/replays/hooks/useDeleteReplays.tsx`** -> AI Confidence: **99.31%**
300. **`static/app/utils/replays/replayDataUtils.tsx`** -> AI Confidence: **99.31%**
301. **`static/app/utils/tabularData/scaleTabularDataColumn.tsx`** -> AI Confidence: **99.31%**
302. **`static/app/utils/timeSeries/scaleTimeSeriesData.tsx`** -> AI Confidence: **99.31%**
303. **`static/app/utils/timeSeries/useFetchEventsTimeSeries.tsx`** -> AI Confidence: **99.31%**
304. **`static/app/utils/useProjects.tsx`** -> AI Confidence: **99.31%**
305. **`static/app/utils/useTeams.tsx`** -> AI Confidence: **99.31%**
306. **`static/app/views/alerts/list/rules/alertRuleStatus.tsx`** -> AI Confidence: **99.31%**
307. **`static/app/views/alerts/rules/metric/create.tsx`** -> AI Confidence: **99.31%**
308. **`static/app/views/alerts/rules/metric/details/header.tsx`** -> AI Confidence: **99.31%**
309. **`static/app/views/alerts/rules/metric/eapMetricsField.tsx`** -> AI Confidence: **99.31%**
310. **`static/app/views/alerts/rules/metric/utils/getMetricDatasetQueryExtras.tsx`** -> AI Confidence: **99.31%**
311. **`static/app/views/alerts/rules/uptime/formErrors.tsx`** -> AI Confidence: **99.31%**
312. **`static/app/views/alerts/utils/getMetricRuleDiscoverUrl.tsx`** -> AI Confidence: **99.31%**
313. **`static/app/views/alerts/wizard/panelContent.tsx`** -> AI Confidence: **99.31%**
314. **`static/app/views/alerts/wizard/utils.tsx`** -> AI Confidence: **99.31%**
315. **`static/app/views/automations/components/automationFormData.tsx`** -> AI Confidence: **99.31%**
316. **`static/app/views/automations/components/connectedMonitorsList.tsx`** -> AI Confidence: **99.31%**
317. **`static/app/views/automations/hooks/utils.tsx`** -> AI Confidence: **99.31%**
318. **`static/app/views/dashboards/createFromSeer.tsx`** -> AI Confidence: **99.31%**
319. **`static/app/views/dashboards/datasetConfig/utils/getSeriesRequestData.tsx`** -> AI Confidence: **99.31%**
320. **`static/app/views/dashboards/orgDashboards.tsx`** -> AI Confidence: **99.31%**
321. **`static/app/views/dashboards/sortableWidget.tsx`** -> AI Confidence: **99.31%**
322. **`static/app/views/dashboards/utils.tsx`** -> AI Confidence: **99.31%**
323. **`static/app/views/dashboards/utils/getWidgetExploreUrl.tsx`** -> AI Confidence: **99.31%**
324. **`static/app/views/dashboards/utils/transformSessionsResponseToSeries.tsx`** -> AI Confidence: **99.31%**
325. **`static/app/views/dashboards/utils/usePrebuiltDashboardUrl.tsx`** -> AI Confidence: **99.31%**
326. **`static/app/views/dashboards/utils/useWidgetSlideout.tsx`** -> AI Confidence: **99.31%**
327. **`static/app/views/dashboards/widgetBuilder/components/sortBySelector.tsx`** -> AI Confidence: **99.31%**
328. **`static/app/views/dashboards/widgetBuilder/components/visualize/index.tsx`** -> AI Confidence: **99.31%**
329. **`static/app/views/dashboards/widgetBuilder/components/visualize/selectRow.tsx`** -> AI Confidence: **99.31%**
330. **`static/app/views/dashboards/widgetBuilder/components/visualize/traceMetrics/metricSelectRow.tsx`** -> AI Confidence: **99.31%**
331. **`static/app/views/dashboards/widgetBuilder/utils/convertBuilderStateToWidget.ts`** -> AI Confidence: **99.31%**
332. **`static/app/views/dashboards/widgetCard/confidenceFooter.tsx`** -> AI Confidence: **99.31%**
333. **`static/app/views/dashboards/widgetCard/genericWidgetQueries.tsx`** -> AI Confidence: **99.31%**
334. **`static/app/views/dashboards/widgetCard/hooks/utils/releases.tsx`** -> AI Confidence: **99.31%**
335. **`static/app/views/dashboards/widgetCard/index.tsx`** -> AI Confidence: **99.31%**
336. **`static/app/views/dashboards/widgetCard/releaseWidgetQueries.tsx`** -> AI Confidence: **99.31%**
337. **`static/app/views/dashboards/widgetCard/toolbar.tsx`** -> AI Confidence: **99.31%**
338. **`static/app/views/dashboards/widgetCard/transformWidgetSeriesToTimeSeries.tsx`** -> AI Confidence: **99.31%**
339. **`static/app/views/dashboards/widgetCard/visualizationWidget.tsx`** -> AI Confidence: **99.31%**
340. **`static/app/views/dashboards/widgetCard/widgetCardChartContainer.tsx`** -> AI Confidence: **99.31%**
341. **`static/app/views/dashboards/widgetCard/widgetFrame.tsx`** -> AI Confidence: **99.31%**
342. **`static/app/views/dashboards/widgetCard/widgetQueries.tsx`** -> AI Confidence: **99.31%**
343. **`static/app/views/dashboards/widgets/bigNumberWidget/bigNumberWidgetVisualization.tsx`** -> AI Confidence: **99.31%**
344. **`static/app/views/dashboards/widgets/categoricalSeriesWidget/categoricalSeriesWidgetVisualization.tsx`** -> AI Confidence: **99.31%**
345. **`static/app/views/dashboards/widgets/categoricalSeriesWidget/plottables/bars.tsx`** -> AI Confidence: **99.31%**
346. **`static/app/views/dashboards/widgets/tableWidget/tableWidgetVisualization.stories.tsx`** -> AI Confidence: **99.31%**
347. **`static/app/views/dashboards/widgets/widget/widget.tsx`** -> AI Confidence: **99.31%**
348. **`static/app/views/detectors/components/connectedAutomationList.tsx`** -> AI Confidence: **99.31%**
349. **`static/app/views/detectors/components/details/metric/charts/metricDetectorChartOptions.tsx`** -> AI Confidence: **99.31%**
350. **`static/app/views/detectors/components/details/metric/getDetectorOpenInDestination.tsx`** -> AI Confidence: **99.31%**
351. **`static/app/views/detectors/components/detectorListTable/actions.tsx`** -> AI Confidence: **99.31%**
352. **`static/app/views/detectors/components/forms/metric/metricFormData.tsx`** -> AI Confidence: **99.31%**
353. **`static/app/views/detectors/components/forms/metric/metricIssuePreview.tsx`** -> AI Confidence: **99.31%**
354. **`static/app/views/detectors/components/forms/metric/metricsVisualize.tsx`** -> AI Confidence: **99.31%**
355. **`static/app/views/detectors/components/forms/metric/resolveSection.tsx`** -> AI Confidence: **99.31%**
356. **`static/app/views/detectors/components/forms/metric/useAutoMetricDetectorName.tsx`** -> AI Confidence: **99.31%**
357. **`static/app/views/detectors/components/forms/uptime/connectedAssertionSuggestionsButton.tsx`** -> AI Confidence: **99.31%**
358. **`static/app/views/detectors/hooks/useMetricDetectorAnomalyPeriods.tsx`** -> AI Confidence: **99.31%**
359. **`static/app/views/detectors/hooks/useMetricDetectorSeries.tsx`** -> AI Confidence: **99.31%**
360. **`static/app/views/detectors/list/common/detectorListContent.tsx`** -> AI Confidence: **99.31%**
361. **`static/app/views/discover/table/cellAction.tsx`** -> AI Confidence: **99.31%**
362. **`static/app/views/discover/table/columnEditCollection.tsx`** -> AI Confidence: **99.31%**
363. **`static/app/views/discover/table/queryField.tsx`** -> AI Confidence: **99.31%**
364. **`static/app/views/discover/utils.tsx`** -> AI Confidence: **99.31%**
365. **`static/app/views/explore/components/attributeBreakdowns/tooltips.tsx`** -> AI Confidence: **99.31%**
366. **`static/app/views/explore/components/toolbar/toolbarVisualize/index.tsx`** -> AI Confidence: **99.31%**
367. **`static/app/views/explore/components/typeBadge.tsx`** -> AI Confidence: **99.31%**
368. **`static/app/views/explore/contexts/traceItemAttributeContext.tsx`** -> AI Confidence: **99.31%**
369. **`static/app/views/explore/hooks/useAnalytics.tsx`** -> AI Confidence: **99.31%**
370. **`static/app/views/explore/hooks/useAttributeBreakdownsTooltip.tsx`** -> AI Confidence: **99.31%**
371. **`static/app/views/explore/hooks/useMetricOptions.tsx`** -> AI Confidence: **99.31%**
372. **`static/app/views/explore/metrics/confidenceFooter.tsx`** -> AI Confidence: **99.31%**
373. **`static/app/views/explore/metrics/hooks/useAddMetricToDashboard.tsx`** -> AI Confidence: **99.31%**
374. **`static/app/views/explore/metrics/hooks/useMetricSamplesTable.tsx`** -> AI Confidence: **99.31%**
375. **`static/app/views/explore/metrics/metricToolbar/metricSelector.tsx`** -> AI Confidence: **99.31%**
376. **`static/app/views/explore/multiQueryMode/locationUtils.tsx`** -> AI Confidence: **99.31%**
377. **`static/app/views/explore/queryParams/readableQueryParams.ts`** -> AI Confidence: **99.31%**
378. **`static/app/views/explore/queryParams/visualize.ts`** -> AI Confidence: **99.31%**
379. **`static/app/views/explore/spans/charts/confidenceFooter.tsx`** -> AI Confidence: **99.31%**
380. **`static/app/views/explore/spans/spansExport.tsx`** -> AI Confidence: **99.31%**
381. **`static/app/views/explore/spans/spansTabSeerComboBox.tsx`** -> AI Confidence: **99.31%**
382. **`static/app/views/explore/starSavedQueryButton.tsx`** -> AI Confidence: **99.31%**
383. **`static/app/views/explore/tables/spansTable.tsx`** -> AI Confidence: **99.31%**
384. **`static/app/views/explore/useRawCounts.tsx`** -> AI Confidence: **99.31%**
385. **`static/app/views/explore/utils.tsx`** -> AI Confidence: **99.31%**
386. **`static/app/views/insights/browser/resources/views/resourceSummaryPage.tsx`** -> AI Confidence: **99.31%**
387. **`static/app/views/insights/browser/webVitals/components/performanceScoreRingWithTooltips.tsx`** -> AI Confidence: **99.31%**
388. **`static/app/views/insights/browser/webVitals/components/webVitalDescription.tsx`** -> AI Confidence: **99.31%**
389. **`static/app/views/insights/browser/webVitals/queries/storedScoreQueries/useTransactionSamplesWebVitalsScoresQuery.tsx`** -> AI Confidence: **99.31%**
390. **`static/app/views/insights/browser/webVitals/queries/storedScoreQueries/useTransactionWebVitalsScoresQuery.tsx`** -> AI Confidence: **99.31%**
391. **`static/app/views/insights/browser/webVitals/utils/useHasSeerWebVitalsSuggestions.tsx`** -> AI Confidence: **99.31%**
392. **`static/app/views/insights/common/components/chart.tsx`** -> AI Confidence: **99.31%**
393. **`static/app/views/insights/common/components/insightsTimeSeriesWidget.tsx`** -> AI Confidence: **99.31%**
394. **`static/app/views/insights/common/components/spanDescription.tsx`** -> AI Confidence: **99.31%**
395. **`static/app/views/insights/common/queries/useDiscover.ts`** -> AI Confidence: **99.31%**
396. **`static/app/views/insights/common/queries/useSortedTimeSeries.tsx`** -> AI Confidence: **99.31%**
397. **`static/app/views/insights/common/queries/useSpansQuery.tsx`** -> AI Confidence: **99.31%**
398. **`static/app/views/insights/common/utils/getAlertsUrl.tsx`** -> AI Confidence: **99.31%**
399. **`static/app/views/insights/common/views/spanSummaryPage/sampleList/durationChart/index.tsx`** -> AI Confidence: **99.31%**
400. **`static/app/views/insights/common/views/spanSummaryPage/sampleList/sampleTable/sampleTable.tsx`** -> AI Confidence: **99.31%**
401. **`static/app/views/insights/crons/components/mockTimelineVisualization.tsx`** -> AI Confidence: **99.31%**
402. **`static/app/views/insights/mobile/screenload/components/tables/screenLoadSpansTable.tsx`** -> AI Confidence: **99.31%**
403. **`static/app/views/insights/pages/agents/components/tracesTable.tsx`** -> AI Confidence: **99.31%**
404. **`static/app/views/insights/pages/conversations/hooks/useConversation.tsx`** -> AI Confidence: **99.31%**
405. **`static/app/views/insights/pages/platform/nextjs/webVitalsWidget.tsx`** -> AI Confidence: **99.31%**
406. **`static/app/views/insights/pages/platform/shared/toolbar.tsx`** -> AI Confidence: **99.31%**
407. **`static/app/views/issueDetails/eventCreatedTooltip.tsx`** -> AI Confidence: **99.31%**
408. **`static/app/views/issueDetails/groupCheckIns.tsx`** -> AI Confidence: **99.31%**
409. **`static/app/views/issueDetails/groupEventAttachments/useGroupEventAttachments.tsx`** -> AI Confidence: **99.31%**
410. **`static/app/views/issueDetails/groupUptimeChecks.tsx`** -> AI Confidence: **99.31%**
411. **`static/app/views/issueDetails/metricIssues/useMetricEventStats.tsx`** -> AI Confidence: **99.31%**
412. **`static/app/views/issueDetails/profilePreviewSection.tsx`** -> AI Confidence: **99.31%**
413. **`static/app/views/issueDetails/streamline/hooks/useCopyIssueDetails.tsx`** -> AI Confidence: **99.31%**
414. **`static/app/views/issueDetails/streamline/sidebar/autofixSection.tsx`** -> AI Confidence: **99.31%**
415. **`static/app/views/issueDetails/streamline/sidebar/detectorSection.tsx`** -> AI Confidence: **99.31%**
416. **`static/app/views/issueDetails/streamline/sidebar/seerNotices.tsx`** -> AI Confidence: **99.31%**
417. **`static/app/views/issueDetails/streamline/sidebar/seerSectionCtaButton.tsx`** -> AI Confidence: **99.31%**
418. **`static/app/views/issueDetails/useGroupEvent.tsx`** -> AI Confidence: **99.31%**
419. **`static/app/views/issueList/issueListSeerComboBox.tsx`** -> AI Confidence: **99.31%**
420. **`static/app/views/issueList/monitorsDropdown.tsx`** -> AI Confidence: **99.31%**
421. **`static/app/views/organizationContext.tsx`** -> AI Confidence: **99.31%**
422. **`static/app/views/performance/eap/useSegmentSpansQuery.tsx`** -> AI Confidence: **99.31%**
423. **`static/app/views/performance/landing/vitalsCards.tsx`** -> AI Confidence: **99.31%**
424. **`static/app/views/performance/newTraceDetails/traceApi/useTraceRootEvent.tsx`** -> AI Confidence: **99.31%**
425. **`static/app/views/performance/newTraceDetails/traceDrawer/details/highlightedAttributes.tsx`** -> AI Confidence: **99.31%**
426. **`static/app/views/performance/newTraceDetails/traceDrawer/details/missingInstrumentation.tsx`** -> AI Confidence: **99.31%**
427. **`static/app/views/performance/newTraceDetails/traceDrawer/details/span/eapSections/aiInput.tsx`** -> AI Confidence: **99.31%**
428. **`static/app/views/performance/newTraceDetails/traceDrawer/details/span/eapSections/aiOutput.tsx`** -> AI Confidence: **99.31%**
429. **`static/app/views/performance/newTraceDetails/traceDrawer/details/span/index.tsx`** -> AI Confidence: **99.31%**
430. **`static/app/views/performance/newTraceDetails/traceDrawer/details/transaction/sections/builtIn.tsx`** -> AI Confidence: **99.31%**
431. **`static/app/views/performance/newTraceDetails/traceDrawer/traceDrawer.tsx`** -> AI Confidence: **99.31%**
432. **`static/app/views/performance/newTraceDetails/traceModels/traceTree.tsx`** -> AI Confidence: **99.31%**
433. **`static/app/views/performance/newTraceDetails/traceModels/traceTreeNode/eapSpanNode.tsx`** -> AI Confidence: **99.31%**
434. **`static/app/views/performance/newTraceDetails/traceRenderers/virtualizedViewManager.tsx`** -> AI Confidence: **99.31%**
435. **`static/app/views/performance/newTraceDetails/traceRow/traceEAPSpanRow.tsx`** -> AI Confidence: **99.31%**
436. **`static/app/views/performance/newTraceDetails/traceRow/traceSpanRow.tsx`** -> AI Confidence: **99.31%**
437. **`static/app/views/performance/newTraceDetails/traceRow/traceUptimeCheckNode.tsx`** -> AI Confidence: **99.31%**
438. **`static/app/views/performance/newTraceDetails/traceRow/traceUptimeCheckTimingNode.tsx`** -> AI Confidence: **99.31%**
439. **`static/app/views/performance/newTraceDetails/useTraceStateAnalytics.tsx`** -> AI Confidence: **99.31%**
440. **`static/app/views/performance/traceDetails/utils.tsx`** -> AI Confidence: **99.31%**
441. **`static/app/views/performance/trends/chart.tsx`** -> AI Confidence: **99.31%**
442. **`static/app/views/preprod/buildComparison/main/insights/fileInsightDiffTable.tsx`** -> AI Confidence: **99.31%**
443. **`static/app/views/preprod/buildComparison/main/insights/groupInsightDiffTable.tsx`** -> AI Confidence: **99.31%**
444. **`static/app/views/preprod/buildComparison/main/sizeCompareItemDiffTable.tsx`** -> AI Confidence: **99.31%**
445. **`static/app/views/preprod/buildComparison/main/sizeCompareMainContent.tsx`** -> AI Confidence: **99.31%**
446. **`static/app/views/preprod/buildComparison/main/sizeCompareSelectedBuilds.tsx`** -> AI Confidence: **99.31%**
447. **`static/app/views/preprod/buildComparison/main/sizeCompareSelectionContent.tsx`** -> AI Confidence: **99.31%**
448. **`static/app/views/preprod/buildDetails/main/buildDetailsMetricCards.tsx`** -> AI Confidence: **99.31%**
449. **`static/app/views/preprod/buildDetails/main/insights/appSizeInsightsSidebarRow.tsx`** -> AI Confidence: **99.31%**
450. **`static/app/views/preprod/buildDetails/sidebar/buildDetailsSidebarAppInfo.tsx`** -> AI Confidence: **99.31%**
451. **`static/app/views/preprod/components/installDetailsContent.tsx`** -> AI Confidence: **99.31%**
452. **`static/app/views/preprod/components/visualizations/appSizeTreemap.tsx`** -> AI Confidence: **99.31%**
453. **`static/app/views/preprod/hooks/usePreprodBuildsAnalytics.tsx`** -> AI Confidence: **99.31%**
454. **`static/app/views/preprod/redirects/legacyUrlRedirect.tsx`** -> AI Confidence: **99.31%**
455. **`static/app/views/preprod/snapshots/snapshots.tsx`** -> AI Confidence: **99.31%**
456. **`static/app/views/projectDetail/missingFeatureButtons/missingReleasesButtons.tsx`** -> AI Confidence: **99.31%**
457. **`static/app/views/projectDetail/projectCharts.tsx`** -> AI Confidence: **99.31%**
458. **`static/app/views/projectDetail/projectScoreCards/projectVelocityScoreCard.tsx`** -> AI Confidence: **99.31%**
459. **`static/app/views/releases/detail/commitsAndFiles/preprodBuilds.tsx`** -> AI Confidence: **99.31%**
460. **`static/app/views/releases/detail/overview/releaseComparisonChart/releaseSessionsChart.tsx`** -> AI Confidence: **99.31%**
461. **`static/app/views/releases/drawer/commitsFilesSection.tsx`** -> AI Confidence: **99.31%**
462. **`static/app/views/releases/drawer/generalCard.tsx`** -> AI Confidence: **99.31%**
463. **`static/app/views/replays/detail/ai/ai.tsx`** -> AI Confidence: **99.31%**
464. **`static/app/views/replays/detail/ai/useReplaySummary.tsx`** -> AI Confidence: **99.31%**
465. **`static/app/views/replays/detail/browserOSIcons.tsx`** -> AI Confidence: **99.31%**
466. **`static/app/views/replays/detail/network/details/sections.tsx`** -> AI Confidence: **99.31%**
467. **`static/app/views/replays/list/bulkDeleteAlert.tsx`** -> AI Confidence: **99.31%**
468. **`static/app/views/seerExplorer/explorerMenu.tsx`** -> AI Confidence: **99.31%**
469. **`static/app/views/seerExplorer/explorerPanel.tsx`** -> AI Confidence: **99.31%**
470. **`static/app/views/seerExplorer/hooks/useSeerExplorer.tsx`** -> AI Confidence: **99.31%**
471. **`static/app/views/seerExplorer/panelContainers.tsx`** -> AI Confidence: **99.31%**
472. **`static/app/views/seerExplorer/prWidget.tsx`** -> AI Confidence: **99.31%**
473. **`static/app/views/seerExplorer/utils.tsx`** -> AI Confidence: **99.31%**
474. **`static/app/views/settings/organizationConsoleSdkInvites/index.tsx`** -> AI Confidence: **99.31%**
475. **`static/app/views/settings/organizationIntegrations/sentryAppExternalForm.tsx`** -> AI Confidence: **99.31%**
476. **`static/app/views/settings/project/projectKeys/details/loaderSettings.tsx`** -> AI Confidence: **99.31%**
477. **`static/app/views/settings/project/projectOwnership/modal.tsx`** -> AI Confidence: **99.31%**
478. **`static/app/views/settings/projectSeer/autofixRepositories.tsx`** -> AI Confidence: **99.31%**
479. **`static/app/views/settings/seer/overview/autofixOverviewSection.tsx`** -> AI Confidence: **99.31%**
480. **`static/app/views/settings/seer/seerAgentHooks.tsx`** -> AI Confidence: **99.31%**
481. **`static/app/views/setupWizard/wizardProjectSelection.tsx`** -> AI Confidence: **99.31%**
482. **`static/gsAdmin/components/addGiftEventsAction.tsx`** -> AI Confidence: **99.31%**
483. **`static/gsAdmin/components/customers/customerStats.tsx`** -> AI Confidence: **99.31%**
484. **`static/gsAdmin/components/customers/updateRetentionSettingsModal.tsx`** -> AI Confidence: **99.31%**
485. **`static/gsAdmin/components/debounceSearch.tsx`** -> AI Confidence: **99.31%**
486. **`static/gsAdmin/components/detailsPage.tsx`** -> AI Confidence: **99.31%**
487. **`static/gsAdmin/components/promoCodes/promoCodeModal.tsx`** -> AI Confidence: **99.31%**
488. **`static/gsAdmin/views/customerContractDetails.tsx`** -> AI Confidence: **99.31%**
489. **`static/gsApp/components/ai/AiSetupDataConsent.tsx`** -> AI Confidence: **99.31%**
490. **`static/gsApp/components/billingDetails/panel.tsx`** -> AI Confidence: **99.31%**
491. **`static/gsApp/components/crons/cronsBillingBanner.tsx`** -> AI Confidence: **99.31%**
492. **`static/gsApp/components/navBillingStatus.tsx`** -> AI Confidence: **99.31%**
493. **`static/gsApp/components/performance/quotaExceededAlert.tsx`** -> AI Confidence: **99.31%**
494. **`static/gsApp/components/productTrial/productTrialAlert.tsx`** -> AI Confidence: **99.31%**
495. **`static/gsApp/components/productTrial/productTrialTag.tsx`** -> AI Confidence: **99.31%**
496. **`static/gsApp/components/upgradeNowModal/planTable.tsx`** -> AI Confidence: **99.31%**
497. **`static/gsApp/hooks/analyticsInitUser.tsx`** -> AI Confidence: **99.31%**
498. **`static/gsApp/hooks/organizationMembershipSettingsForm.tsx`** -> AI Confidence: **99.31%**
499. **`static/gsApp/hooks/spendVisibility/enhancedUsageStatsOrganization.tsx`** -> AI Confidence: **99.31%**
500. **`static/gsApp/hooks/useMaxPickableDays.tsx`** -> AI Confidence: **99.31%**
501. **`static/gsApp/utils/billing.tsx`** -> AI Confidence: **99.31%**
502. **`static/gsApp/utils/dataCategory.tsx`** -> AI Confidence: **99.31%**
503. **`static/gsApp/views/legalAndCompliance/policyRow.tsx`** -> AI Confidence: **99.31%**
504. **`static/gsApp/views/seerAutomation/components/projectTable/seerProjectTableRow.tsx`** -> AI Confidence: **99.31%**
505. **`static/gsApp/views/spendAllocations/components/allocationForm.tsx`** -> AI Confidence: **99.31%**
506. **`static/gsApp/views/spendLimits/utils.tsx`** -> AI Confidence: **99.31%**
507. **`static/gsApp/views/subscriptionPage/pendingChanges.tsx`** -> AI Confidence: **99.31%**
508. **`static/gsApp/views/subscriptionPage/planMigrationActive/planMigrationRow.tsx`** -> AI Confidence: **99.31%**
509. **`static/gsApp/views/subscriptionPage/planMigrationActive/planMigrationTable.tsx`** -> AI Confidence: **99.31%**
510. **`static/gsApp/views/subscriptionPage/reservedUsageChart.tsx`** -> AI Confidence: **99.31%**
511. **`static/gsApp/views/subscriptionPage/usageOverview/components/breakdownInfo.tsx`** -> AI Confidence: **99.31%**
512. **`static/gsApp/views/subscriptionPage/usageOverview/components/cta.tsx`** -> AI Confidence: **99.31%**
513. **`static/gsApp/views/subscriptionPage/usageOverview/components/panel.tsx`** -> AI Confidence: **99.31%**
514. **`static/gsApp/views/subscriptionPage/usageOverview/index.tsx`** -> AI Confidence: **99.31%**
515. **`self-hosted/sentry.conf.py`** -> AI Confidence: **99.29%**
516. **`src/sentry/api/helpers/android_models.py`** -> AI Confidence: **99.29%**
517. **`src/sentry/apidocs/api_publish_status_allowlist_dont_modify.py`** -> AI Confidence: **99.29%**
518. **`src/sentry/apidocs/examples/integration_examples.py`** -> AI Confidence: **99.29%**
519. **`src/sentry/models/releases/constants.py`** -> AI Confidence: **99.29%**
520. **`.github/workflows/scripts/migration-check.sh`** -> AI Confidence: **99.29%**
521. **`config/hooks/post-checkout`** -> AI Confidence: **99.29%**
522. **`config/hooks/post-merge`** -> AI Confidence: **99.29%**
523. **`scripts/post-release.sh`** -> AI Confidence: **99.29%**
524. **`self-hosted/docker-entrypoint.sh`** -> AI Confidence: **99.29%**
525. **`static/app/bootstrap/printConsoleBanner.ts`** -> AI Confidence: **99.29%**
526. **`static/app/utils/analytics/stackTraceAnalyticsEvents.tsx`** -> AI Confidence: **99.29%**
527. **`static/app/views/dashboards/widgets/timeSeriesWidget/formatters/formatXAxisTimestamp.tsx`** -> AI Confidence: **99.29%**
528. **`static/app/views/dashboards/widgets/timeSeriesWidget/formatters/formatYAxisDuration.tsx`** -> AI Confidence: **99.29%**
529. **`tests/js/fixtures/replayRecord.ts`** -> AI Confidence: **99.29%**
530. **`bin/load-integration-data`** -> AI Confidence: **99.24%**
531. **`src/sentry/api/authentication.py`** -> AI Confidence: **99.24%**
532. **`src/sentry/api/bases/organization.py`** -> AI Confidence: **99.24%**
533. **`src/sentry/api/bases/organization_events.py`** -> AI Confidence: **99.24%**
534. **`src/sentry/api/client.py`** -> AI Confidence: **99.24%**
535. **`src/sentry/api/endpoints/admin_project_configs.py`** -> AI Confidence: **99.24%**
536. **`src/sentry/api/endpoints/broadcast_index.py`** -> AI Confidence: **99.24%**
537. **`src/sentry/api/endpoints/organization_events_facets_performance.py`** -> AI Confidence: **99.24%**
538. **`src/sentry/api/endpoints/organization_events_meta.py`** -> AI Confidence: **99.24%**
539. **`src/sentry/api/endpoints/organization_events_stats.py`** -> AI Confidence: **99.24%**
540. **`src/sentry/api/endpoints/organization_stats.py`** -> AI Confidence: **99.24%**
541. **`src/sentry/api/endpoints/organization_stats_summary.py`** -> AI Confidence: **99.24%**
542. **`src/sentry/api/endpoints/organization_trace_item_attributes_ranked.py`** -> AI Confidence: **99.24%**
543. **`src/sentry/api/endpoints/organization_traces.py`** -> AI Confidence: **99.24%**
544. **`src/sentry/api/endpoints/project_trace_item_details.py`** -> AI Confidence: **99.24%**
545. **`src/sentry/api/endpoints/prompts_activity.py`** -> AI Confidence: **99.24%**
546. **`src/sentry/api/endpoints/system_options.py`** -> AI Confidence: **99.24%**
547. **`src/sentry/api/event_search.py`** -> AI Confidence: **99.24%**
548. **`src/sentry/api/helpers/group_index/validators/group.py`** -> AI Confidence: **99.24%**
549. **`src/sentry/api/helpers/source_map_helper.py`** -> AI Confidence: **99.24%**
550. **`src/sentry/api/serializers/models/group.py`** -> AI Confidence: **99.24%**
551. **`src/sentry/api/serializers/models/organization_member/base.py`** -> AI Confidence: **99.24%**
552. **`src/sentry/api/serializers/models/project.py`** -> AI Confidence: **99.24%**
553. **`src/sentry/api/utils.py`** -> AI Confidence: **99.24%**
554. **`src/sentry/auth/helper.py`** -> AI Confidence: **99.24%**
555. **`src/sentry/auth/staff.py`** -> AI Confidence: **99.24%**
556. **`src/sentry/auth/superuser.py`** -> AI Confidence: **99.24%**
557. **`src/sentry/backup/dependencies.py`** -> AI Confidence: **99.24%**
558. **`src/sentry/backup/sanitize.py`** -> AI Confidence: **99.24%**
559. **`src/sentry/backup/services/import_export/impl.py`** -> AI Confidence: **99.24%**
560. **`src/sentry/buffer/base.py`** -> AI Confidence: **99.24%**
561. **`src/sentry/buffer/redis.py`** -> AI Confidence: **99.24%**
562. **`src/sentry/conf/server.py`** -> AI Confidence: **99.24%**
563. **`src/sentry/core/endpoints/organization_details.py`** -> AI Confidence: **99.24%**
564. **`src/sentry/core/endpoints/organization_member_details.py`** -> AI Confidence: **99.24%**
565. **`src/sentry/core/endpoints/project_index.py`** -> AI Confidence: **99.24%**
566. **`src/sentry/data_export/endpoints/data_export.py`** -> AI Confidence: **99.24%**
567. **`src/sentry/data_export/processors/issues_by_tag.py`** -> AI Confidence: **99.24%**
568. **`src/sentry/db/models/manager/base.py`** -> AI Confidence: **99.24%**
569. **`src/sentry/digests/notifications.py`** -> AI Confidence: **99.24%**
570. **`src/sentry/discover/compare_tables.py`** -> AI Confidence: **99.24%**
571. **`src/sentry/discover/endpoints/serializers.py`** -> AI Confidence: **99.24%**
572. **`src/sentry/dynamic_sampling/tasks/boost_low_volume_transactions.py`** -> AI Confidence: **99.24%**
573. **`src/sentry/event_manager.py`** -> AI Confidence: **99.24%**
574. **`src/sentry/explore/endpoints/explore_saved_queries.py`** -> AI Confidence: **99.24%**
575. **`src/sentry/explore/translation/alerts_translation.py`** -> AI Confidence: **99.24%**
576. **`src/sentry/feedback/endpoints/organization_feedback_categories.py`** -> AI Confidence: **99.24%**
577. **`src/sentry/feedback/usecases/ingest/create_feedback.py`** -> AI Confidence: **99.24%**
578. **`src/sentry/grouping/api.py`** -> AI Confidence: **99.24%**
579. **`src/sentry/grouping/ingest/seer.py`** -> AI Confidence: **99.24%**
580. **`src/sentry/hybridcloud/services/organizationmember_mapping/impl.py`** -> AI Confidence: **99.24%**
581. **`src/sentry/incidents/charts.py`** -> AI Confidence: **99.24%**
582. **`src/sentry/incidents/endpoints/serializers/workflow_engine_data_condition.py`** -> AI Confidence: **99.24%**
583. **`src/sentry/incidents/metric_issue_detector.py`** -> AI Confidence: **99.24%**
584. **`src/sentry/incidents/serializers/alert_rule.py`** -> AI Confidence: **99.24%**
585. **`src/sentry/incidents/serializers/alert_rule_trigger_action.py`** -> AI Confidence: **99.24%**
586. **`src/sentry/integrations/api/endpoints/organization_code_mappings_bulk.py`** -> AI Confidence: **99.24%**
587. **`src/sentry/integrations/api/endpoints/organization_repository_settings.py`** -> AI Confidence: **99.24%**
588. **`src/sentry/integrations/aws_lambda/utils.py`** -> AI Confidence: **99.24%**
589. **`src/sentry/integrations/cursor/integration.py`** -> AI Confidence: **99.24%**
590. **`src/sentry/integrations/data_forwarding/splunk/forwarder.py`** -> AI Confidence: **99.24%**
591. **`src/sentry/integrations/jira/integration.py`** -> AI Confidence: **99.24%**
592. **`src/sentry/integrations/jira_server/integration.py`** -> AI Confidence: **99.24%**
593. **`src/sentry/integrations/messaging/message_builder.py`** -> AI Confidence: **99.24%**
594. **`src/sentry/integrations/opsgenie/tasks.py`** -> AI Confidence: **99.24%**
595. **`src/sentry/integrations/source_code_management/repo_trees.py`** -> AI Confidence: **99.24%**
596. **`src/sentry/integrations/utils/scope.py`** -> AI Confidence: **99.24%**
597. **`src/sentry/issue_detection/detectors/mn_plus_one_db_span_detector.py`** -> AI Confidence: **99.24%**
598. **`src/sentry/issue_detection/detectors/n_plus_one_api_calls_detector.py`** -> AI Confidence: **99.24%**
599. **`src/sentry/issue_detection/detectors/n_plus_one_db_span_detector.py`** -> AI Confidence: **99.24%**
600. **`src/sentry/issue_detection/detectors/uncompressed_asset_detector.py`** -> AI Confidence: **99.24%**
601. **`src/sentry/issue_detection/performance_detection.py`** -> AI Confidence: **99.24%**
602. **`src/sentry/issues/attributes.py`** -> AI Confidence: **99.24%**
603. **`src/sentry/issues/endpoints/organization_group_index.py`** -> AI Confidence: **99.24%**
604. **`src/sentry/issues/endpoints/organization_issue_timeseries.py`** -> AI Confidence: **99.24%**
605. **`src/sentry/issues/endpoints/project_ownership.py`** -> AI Confidence: **99.24%**
606. **`src/sentry/issues/escalating/escalating.py`** -> AI Confidence: **99.24%**
607. **`src/sentry/issues/ignored.py`** -> AI Confidence: **99.24%**
608. **`src/sentry/lang/dart/utils.py`** -> AI Confidence: **99.24%**
609. **`src/sentry/middleware/ratelimit.py`** -> AI Confidence: **99.24%**
610. **`src/sentry/models/dashboard.py`** -> AI Confidence: **99.24%**
611. **`src/sentry/models/debugfile.py`** -> AI Confidence: **99.24%**
612. **`src/sentry/models/projectownership.py`** -> AI Confidence: **99.24%**
613. **`src/sentry/models/releases/set_commits.py`** -> AI Confidence: **99.24%**
614. **`src/sentry/models/releases/util.py`** -> AI Confidence: **99.24%**
615. **`src/sentry/monitors/consumers/monitor_consumer.py`** -> AI Confidence: **99.24%**
616. **`src/sentry/monitors/endpoints/organization_monitor_index.py`** -> AI Confidence: **99.24%**
617. **`src/sentry/monitors/logic/incidents.py`** -> AI Confidence: **99.24%**
618. **`src/sentry/monitors/serializers.py`** -> AI Confidence: **99.24%**
619. **`src/sentry/monitors/system_incidents.py`** -> AI Confidence: **99.24%**
620. **`src/sentry/notifications/api/serializers/notification_action_request.py`** -> AI Confidence: **99.24%**
621. **`src/sentry/notifications/notificationcontroller.py`** -> AI Confidence: **99.24%**
622. **`src/sentry/notifications/platform/service.py`** -> AI Confidence: **99.24%**
623. **`src/sentry/notifications/utils/participants.py`** -> AI Confidence: **99.24%**
624. **`src/sentry/preprod/api/endpoints/project_preprod_check_for_updates.py`** -> AI Confidence: **99.24%**
625. **`src/sentry/preprod/api/endpoints/size_analysis/project_preprod_size_analysis_compare.py`** -> AI Confidence: **99.24%**
626. **`src/sentry/preprod/api/models/public/size_analysis.py`** -> AI Confidence: **99.24%**
627. **`src/sentry/preprod/eap/write.py`** -> AI Confidence: **99.24%**
628. **`src/sentry/preprod/helpers/deletion.py`** -> AI Confidence: **99.24%**
629. **`src/sentry/preprod/pull_request/adapters.py`** -> AI Confidence: **99.24%**
630. **`src/sentry/preprod/snapshots/image_diff/compare.py`** -> AI Confidence: **99.24%**
631. **`src/sentry/preprod/snapshots/image_diff/odiff.py`** -> AI Confidence: **99.24%**
632. **`src/sentry/receivers/features.py`** -> AI Confidence: **99.24%**
633. **`src/sentry/receivers/releases.py`** -> AI Confidence: **99.24%**
634. **`src/sentry/relay/config/__init__.py`** -> AI Confidence: **99.24%**
635. **`src/sentry/relay/config/metric_extraction.py`** -> AI Confidence: **99.24%**
636. **`src/sentry/relay/datascrubbing.py`** -> AI Confidence: **99.24%**
637. **`src/sentry/release_health/metrics_sessions_v2.py`** -> AI Confidence: **99.24%**
638. **`src/sentry/releases/use_cases/release.py`** -> AI Confidence: **99.24%**
639. **`src/sentry/relocation/tasks/process.py`** -> AI Confidence: **99.24%**
640. **`src/sentry/replays/lib/eap/snuba_transpiler.py`** -> AI Confidence: **99.24%**
641. **`src/sentry/replays/usecases/query/__init__.py`** -> AI Confidence: **99.24%**
642. **`src/sentry/replays/usecases/query/fields.py`** -> AI Confidence: **99.24%**
643. **`src/sentry/runner/commands/createuser.py`** -> AI Confidence: **99.24%**
644. **`src/sentry/runner/commands/performance.py`** -> AI Confidence: **99.24%**
645. **`src/sentry/runner/commands/presenters/webhookpresenter.py`** -> AI Confidence: **99.24%**
646. **`src/sentry/runner/commands/upgrade.py`** -> AI Confidence: **99.24%**
647. **`src/sentry/runner/initializer.py`** -> AI Confidence: **99.24%**
648. **`src/sentry/runner/settings.py`** -> AI Confidence: **99.24%**
649. **`src/sentry/search/eap/spans/attributes.py`** -> AI Confidence: **99.24%**
650. **`src/sentry/search/events/builder/profile_functions.py`** -> AI Confidence: **99.24%**
651. **`src/sentry/search/events/datasets/discover.py`** -> AI Confidence: **99.24%**
652. **`src/sentry/search/events/datasets/metrics.py`** -> AI Confidence: **99.24%**
653. **`src/sentry/search/snuba/backend.py`** -> AI Confidence: **99.24%**
654. **`src/sentry/seer/anomaly_detection/store_data.py`** -> AI Confidence: **99.24%**
655. **`src/sentry/seer/anomaly_detection/store_data_workflow_engine.py`** -> AI Confidence: **99.24%**
656. **`src/sentry/seer/autofix/issue_summary.py`** -> AI Confidence: **99.24%**
657. **`src/sentry/seer/autofix/on_completion_hook.py`** -> AI Confidence: **99.24%**
658. **`src/sentry/seer/endpoints/organization_autofix_automation_settings.py`** -> AI Confidence: **99.24%**
659. **`src/sentry/seer/entrypoints/operator.py`** -> AI Confidence: **99.24%**
660. **`src/sentry/seer/explorer/coding_agent_handoff.py`** -> AI Confidence: **99.24%**
661. **`src/sentry/seer/explorer/index_data.py`** -> AI Confidence: **99.24%**
662. **`src/sentry/seer/similarity/similar_issues.py`** -> AI Confidence: **99.24%**
663. **`src/sentry/seer/similarity/utils.py`** -> AI Confidence: **99.24%**
664. **`src/sentry/sentry_apps/api/parsers/sentry_app.py`** -> AI Confidence: **99.24%**
665. **`src/sentry/sentry_apps/services/hook/impl.py`** -> AI Confidence: **99.24%**
666. **`src/sentry/sentry_metrics/consumers/indexer/batch.py`** -> AI Confidence: **99.24%**
667. **`src/sentry/services/filestore/s3.py`** -> AI Confidence: **99.24%**
668. **`src/sentry/services/nodestore/bigtable/backend.py`** -> AI Confidence: **99.24%**
669. **`src/sentry/snuba/errors.py`** -> AI Confidence: **99.24%**
670. **`src/sentry/snuba/functions.py`** -> AI Confidence: **99.24%**
671. **`src/sentry/snuba/metrics/extraction.py`** -> AI Confidence: **99.24%**
672. **`src/sentry/snuba/outcomes.py`** -> AI Confidence: **99.24%**
673. **`src/sentry/snuba/snuba_query_validator.py`** -> AI Confidence: **99.24%**
674. **`src/sentry/snuba/spans_indexed.py`** -> AI Confidence: **99.24%**
675. **`src/sentry/snuba/spans_metrics.py`** -> AI Confidence: **99.24%**
676. **`src/sentry/snuba/tasks.py`** -> AI Confidence: **99.24%**
677. **`src/sentry/spans/debug_trace_logger.py`** -> AI Confidence: **99.24%**
678. **`src/sentry/statistical_detectors/detector.py`** -> AI Confidence: **99.24%**
679. **`src/sentry/tasks/merge.py`** -> AI Confidence: **99.24%**
680. **`src/sentry/tasks/on_demand_metrics.py`** -> AI Confidence: **99.24%**
681. **`src/sentry/tasks/relay.py`** -> AI Confidence: **99.24%**
682. **`src/sentry/tasks/seer/explorer_index.py`** -> AI Confidence: **99.24%**
683. **`src/sentry/tasks/statistical_detectors.py`** -> AI Confidence: **99.24%**
684. **`src/sentry/tasks/summaries/utils.py`** -> AI Confidence: **99.24%**
685. **`src/sentry/testutils/helpers/features.py`** -> AI Confidence: **99.24%**
686. **`src/sentry/testutils/pytest/stale_database_reads.py`** -> AI Confidence: **99.24%**
687. **`src/sentry/testutils/silo.py`** -> AI Confidence: **99.24%**
688. **`src/sentry/uptime/consumers/eap_converter.py`** -> AI Confidence: **99.24%**
689. **`src/sentry/uptime/consumers/results_consumer.py`** -> AI Confidence: **99.24%**
690. **`src/sentry/uptime/endpoints/validators.py`** -> AI Confidence: **99.24%**
691. **`src/sentry/uptime/migrations/0055_backfill_2xx_status_assertion.py`** -> AI Confidence: **99.24%**
692. **`src/sentry/uptime/seer_assertions.py`** -> AI Confidence: **99.24%**
693. **`src/sentry/users/api/endpoints/user_index.py`** -> AI Confidence: **99.24%**
694. **`src/sentry/users/models/user_option.py`** -> AI Confidence: **99.24%**
695. **`src/sentry/utils/dates.py`** -> AI Confidence: **99.24%**
696. **`src/sentry/utils/eventuser.py`** -> AI Confidence: **99.24%**
697. **`src/sentry/utils/metrics.py`** -> AI Confidence: **99.24%**
698. **`src/sentry/utils/sdk.py`** -> AI Confidence: **99.24%**
699. **`src/sentry/utils/sdk_crashes/sdk_crash_detector.py`** -> AI Confidence: **99.24%**
700. **`src/sentry/web/client_config.py`** -> AI Confidence: **99.24%**
701. **`src/sentry/web/frontend/csrf_failure.py`** -> AI Confidence: **99.24%**
702. **`src/sentry/web/frontend/oauth_device.py`** -> AI Confidence: **99.24%**
703. **`src/sentry/web/frontend/oauth_token.py`** -> AI Confidence: **99.24%**
704. **`src/sentry/web/frontend/organization_auth_settings.py`** -> AI Confidence: **99.24%**
705. **`src/sentry/workflow_engine/endpoints/validators/base/workflow.py`** -> AI Confidence: **99.24%**
706. **`src/sentry/workflow_engine/handlers/condition/event_frequency_query_handlers.py`** -> AI Confidence: **99.24%**
707. **`src/sentry/workflow_engine/handlers/detector/stateful.py`** -> AI Confidence: **99.24%**
708. **`src/sentry/workflow_engine/migration_helpers/alert_rule.py`** -> AI Confidence: **99.24%**
709. **`src/sentry/workflow_engine/migration_helpers/issue_alert_migration.py`** -> AI Confidence: **99.24%**
710. **`src/sentry/workflow_engine/migrations/0068_migrate_anomaly_detection_alerts.py`** -> AI Confidence: **99.24%**
711. **`src/sentry/workflow_engine/migrations/0070_migrate_remaining_anomaly_detection_alerts.py`** -> AI Confidence: **99.24%**
712. **`src/sentry/workflow_engine/migrations/0071_migrate_remaining_metric_alerts.py`** -> AI Confidence: **99.24%**
713. **`src/sentry/workflow_engine/migrations/0087_relink_crons_to_compatible_issue_workflows.py`** -> AI Confidence: **99.24%**
714. **`src/sentry/workflow_engine/processors/data_condition_group.py`** -> AI Confidence: **99.24%**
715. **`src/sentry/workflow_engine/processors/delayed_workflow.py`** -> AI Confidence: **99.24%**
716. **`src/sentry/workflow_engine/processors/schedule.py`** -> AI Confidence: **99.24%**
717. **`src/sentry_plugins/github/webhooks/events/pull_request.py`** -> AI Confidence: **99.24%**
718. **`src/sentry_plugins/redmine/plugin.py`** -> AI Confidence: **99.24%**
719. **`src/sentry_plugins/slack/plugin.py`** -> AI Confidence: **99.24%**
720. **`src/sentry_plugins/splunk/plugin.py`** -> AI Confidence: **99.24%**
721. **`src/social_auth/backends/__init__.py`** -> AI Confidence: **99.24%**
722. **`src/social_auth/views.py`** -> AI Confidence: **99.24%**
723. **`tests/acceptance/test_organization_dashboards.py`** -> AI Confidence: **99.24%**
724. **`tests/sentry/models/test_organizationslugreservation.py`** -> AI Confidence: **99.24%**
725. **`tests/sentry/snuba/metrics/test_query.py`** -> AI Confidence: **99.24%**
726. **`tests/sentry/tasks/seer/test_explorer_index.py`** -> AI Confidence: **99.24%**
727. **`tests/sentry/tasks/test_statistical_detectors.py`** -> AI Confidence: **99.24%**
728. **`tests/sentry/taskworker/test_config.py`** -> AI Confidence: **99.24%**
729. **`tests/sentry/workflow_engine/handlers/condition/test_tagged_event_handler.py`** -> AI Confidence: **99.24%**
730. **`tests/snuba/api/endpoints/test_organization_events_histogram.py`** -> AI Confidence: **99.24%**
731. **`static/app/actionCreators/events.tsx`** -> AI Confidence: **99.24%**
732. **`static/app/actionCreators/organization.tsx`** -> AI Confidence: **99.24%**
733. **`static/app/actionCreators/prompts.tsx`** -> AI Confidence: **99.24%**
734. **`static/app/bootstrap/exportGlobals.tsx`** -> AI Confidence: **99.24%**
735. **`static/app/chartcuterie/discover.tsx`** -> AI Confidence: **99.24%**
736. **`static/app/components/acl/feature.tsx`** -> AI Confidence: **99.24%**
737. **`static/app/components/activity/note/input.tsx`** -> AI Confidence: **99.24%**
738. **`static/app/components/avatarChooser/index.tsx`** -> AI Confidence: **99.24%**
739. **`static/app/components/backendJsonFormAdapter/index.tsx`** -> AI Confidence: **99.24%**
740. **`static/app/components/backendJsonFormAdapter/projectMapperAdapter.tsx`** -> AI Confidence: **99.24%**
741. **`static/app/components/charts/groupStatusChart.tsx`** -> AI Confidence: **99.24%**
742. **`static/app/components/charts/sessionsRequest.tsx`** -> AI Confidence: **99.24%**
743. **`static/app/components/checkInTimeline/gridLines.tsx`** -> AI Confidence: **99.24%**
744. **`static/app/components/commandPalette/useDsnLookupActions.tsx`** -> AI Confidence: **99.24%**
745. **`static/app/components/commitLink.tsx`** -> AI Confidence: **99.24%**
746. **`static/app/components/contextPickerModal.tsx`** -> AI Confidence: **99.24%**
747. **`static/app/components/core/avatar/useAvatar.ts`** -> AI Confidence: **99.24%**
748. **`static/app/components/core/compactSelect/listBox/index.tsx`** -> AI Confidence: **99.24%**
749. **`static/app/components/core/compactSelect/utils.tsx`** -> AI Confidence: **99.24%**
750. **`static/app/components/deprecatedAsyncComponent.tsx`** -> AI Confidence: **99.24%**
751. **`static/app/components/deprecatedforms/genericField.tsx`** -> AI Confidence: **99.24%**
752. **`static/app/components/events/autofix/autofixDiff.tsx`** -> AI Confidence: **99.24%**
753. **`static/app/components/events/autofix/autofixHighlightPopup.tsx`** -> AI Confidence: **99.24%**
754. **`static/app/components/events/autofix/autofixOutputStream.tsx`** -> AI Confidence: **99.24%**
755. **`static/app/components/events/autofix/codingAgentIntegrationCta.tsx`** -> AI Confidence: **99.24%**
756. **`static/app/components/events/breadcrumbs/utils.tsx`** -> AI Confidence: **99.24%**
757. **`static/app/components/events/contexts/contextCard.tsx`** -> AI Confidence: **99.24%**
758. **`static/app/components/events/eventStatisticalDetector/eventRegressionTable.tsx`** -> AI Confidence: **99.24%**
759. **`static/app/components/events/groupingInfo/groupingInfo.tsx`** -> AI Confidence: **99.24%**
760. **`static/app/components/events/highlights/highlightsDataSection.tsx`** -> AI Confidence: **99.24%**
761. **`static/app/components/events/interfaces/crashContent/exception/actionableItems.tsx`** -> AI Confidence: **99.24%**
762. **`static/app/components/events/interfaces/crashContent/exception/banners/stacktraceBanners.tsx`** -> AI Confidence: **99.24%**
763. **`static/app/components/events/interfaces/debugMeta/debugImageDetails/candidate/information/index.tsx`** -> AI Confidence: **99.24%**
764. **`static/app/components/events/interfaces/frame/defaultTitle/index.tsx`** -> AI Confidence: **99.24%**
765. **`static/app/components/events/interfaces/request/graphQlRequestBody.tsx`** -> AI Confidence: **99.24%**
766. **`static/app/components/events/interfaces/spans/spanTreeModel.tsx`** -> AI Confidence: **99.24%**
767. **`static/app/components/events/interfaces/threads/threadSelector/option.tsx`** -> AI Confidence: **99.24%**
768. **`static/app/components/events/profileEventEvidence.tsx`** -> AI Confidence: **99.24%**
769. **`static/app/components/events/viewHierarchy/wireframe.tsx`** -> AI Confidence: **99.24%**
770. **`static/app/components/featureFeedback/feedbackModal.tsx`** -> AI Confidence: **99.24%**
771. **`static/app/components/feedback/feedbackItem/feedbackItemLoader.tsx`** -> AI Confidence: **99.24%**
772. **`static/app/components/feedback/feedbackItem/feedbackReplay.tsx`** -> AI Confidence: **99.24%**
773. **`static/app/components/feedback/feedbackItem/traceDataSection.tsx`** -> AI Confidence: **99.24%**
774. **`static/app/components/forms/fields/selectField.tsx`** -> AI Confidence: **99.24%**
775. **`static/app/components/forms/formField/index.tsx`** -> AI Confidence: **99.24%**
776. **`static/app/components/forms/model.tsx`** -> AI Confidence: **99.24%**
777. **`static/app/components/group/tagFacets/tagFacetsDistributionMeter.tsx`** -> AI Confidence: **99.24%**
778. **`static/app/components/groupMetaRow.tsx`** -> AI Confidence: **99.24%**
779. **`static/app/components/groupPreviewTooltip/stackTracePreview.tsx`** -> AI Confidence: **99.24%**
780. **`static/app/components/idBadge/projectBadge.tsx`** -> AI Confidence: **99.24%**
781. **`static/app/components/issues/groupList.tsx`** -> AI Confidence: **99.24%**
782. **`static/app/components/issues/suspect/useLegacyEventSuspectFlags.tsx`** -> AI Confidence: **99.24%**
783. **`static/app/components/layouts/thirds.tsx`** -> AI Confidence: **99.24%**
784. **`static/app/components/modals/sudoModal.tsx`** -> AI Confidence: **99.24%**
785. **`static/app/components/onboardingWizard/content.tsx`** -> AI Confidence: **99.24%**
786. **`static/app/components/pageFilters/container.tsx`** -> AI Confidence: **99.24%**
787. **`static/app/components/pageFilters/project/projectPageFilterTrigger.tsx`** -> AI Confidence: **99.24%**
788. **`static/app/components/pageOverlay.tsx`** -> AI Confidence: **99.24%**
789. **`static/app/components/pagination.tsx`** -> AI Confidence: **99.24%**
790. **`static/app/components/performance/searchBar.tsx`** -> AI Confidence: **99.24%**
791. **`static/app/components/preprod/preprodOnboardingPanel.tsx`** -> AI Confidence: **99.24%**
792. **`static/app/components/profiling/flamegraph/flamegraphChart.tsx`** -> AI Confidence: **99.24%**
793. **`static/app/components/profiling/flamegraph/flamegraphSpans.tsx`** -> AI Confidence: **99.24%**
794. **`static/app/components/profiling/flamegraph/flamegraphToolbar/flamegraphSearch.tsx`** -> AI Confidence: **99.24%**
795. **`static/app/components/profiling/flamegraph/flamegraphZoomView.tsx`** -> AI Confidence: **99.24%**
796. **`static/app/components/replays/bulkDelete/replayBulkDeleteAuditLogTable.tsx`** -> AI Confidence: **99.24%**
797. **`static/app/components/replays/diff/replayTextDiff.tsx`** -> AI Confidence: **99.24%**
798. **`static/app/components/replays/replayBadge.tsx`** -> AI Confidence: **99.24%**
799. **`static/app/components/replays/replayCurrentUrl.tsx`** -> AI Confidence: **99.24%**
800. **`static/app/components/replays/replayPlayer.tsx`** -> AI Confidence: **99.24%**
801. **`static/app/components/replays/table/replayTableHeader.tsx`** -> AI Confidence: **99.24%**
802. **`static/app/components/search/sources/apiSource.tsx`** -> AI Confidence: **99.24%**
803. **`static/app/components/search/sources/commandSource.tsx`** -> AI Confidence: **99.24%**
804. **`static/app/components/searchQueryBuilder/askSeerCombobox/askSeerComboBox.tsx`** -> AI Confidence: **99.24%**
805. **`static/app/components/searchQueryBuilder/index.tsx`** -> AI Confidence: **99.24%**
806. **`static/app/components/searchQueryBuilder/selectionKeyHandler.tsx`** -> AI Confidence: **99.24%**
807. **`static/app/components/searchQueryBuilder/tokens/combobox.tsx`** -> AI Confidence: **99.24%**
808. **`static/app/components/searchQueryBuilder/tokens/filter/parametersCombobox.tsx`** -> AI Confidence: **99.24%**
809. **`static/app/components/searchQueryBuilder/tokens/filterKeyListBox/useFilterKeyListBox.tsx`** -> AI Confidence: **99.24%**
810. **`static/app/components/searchQueryBuilder/tokens/freeText.tsx`** -> AI Confidence: **99.24%**
811. **`static/app/components/searchQueryBuilder/tokens/invalidTokenTooltip.tsx`** -> AI Confidence: **99.24%**
812. **`static/app/components/stackTrace/issueStackTrace/index.tsx`** -> AI Confidence: **99.24%**
813. **`static/app/components/timeRangeSelector/utils.tsx`** -> AI Confidence: **99.24%**
814. **`static/app/stores/groupingStore.tsx`** -> AI Confidence: **99.24%**
815. **`static/app/stories/view/storyExports.tsx`** -> AI Confidence: **99.24%**
816. **`static/app/types/event.tsx`** -> AI Confidence: **99.24%**
817. **`static/app/utils/integrationUtil.tsx`** -> AI Confidence: **99.24%**
818. **`static/app/utils/performance/contexts/metricsCardinality.tsx`** -> AI Confidence: **99.24%**
819. **`static/app/utils/profiling/renderers/flamegraphTextRenderer.tsx`** -> AI Confidence: **99.24%**
820. **`static/app/utils/profiling/renderers/spansTextRenderer.tsx`** -> AI Confidence: **99.24%**
821. **`static/app/utils/replays/getFrameDetails.tsx`** -> AI Confidence: **99.24%**
822. **`static/app/utils/replays/hooks/useInitialTimeOffsetMs.tsx`** -> AI Confidence: **99.24%**
823. **`static/app/utils/replays/hydrateBreadcrumbs.tsx`** -> AI Confidence: **99.24%**
824. **`static/app/utils/sessions.tsx`** -> AI Confidence: **99.24%**
825. **`static/app/utils/useMaxPickableDays.tsx`** -> AI Confidence: **99.24%**
826. **`static/app/utils/useMembers.tsx`** -> AI Confidence: **99.24%**
827. **`static/app/utils/useOverlay.tsx`** -> AI Confidence: **99.24%**
828. **`static/app/views/acceptOrganizationInvite/index.tsx`** -> AI Confidence: **99.24%**
829. **`static/app/views/acceptProjectTransfer/index.tsx`** -> AI Confidence: **99.24%**
830. **`static/app/views/alerts/create.tsx`** -> AI Confidence: **99.24%**
831. **`static/app/views/alerts/rules/issue/index.tsx`** -> AI Confidence: **99.24%**
832. **`static/app/views/alerts/rules/metric/details/errorMigrationWarning.tsx`** -> AI Confidence: **99.24%**
833. **`static/app/views/alerts/rules/metric/details/index.tsx`** -> AI Confidence: **99.24%**
834. **`static/app/views/alerts/rules/metric/details/metricHistory.tsx`** -> AI Confidence: **99.24%**
835. **`static/app/views/alerts/rules/metric/eapField.tsx`** -> AI Confidence: **99.24%**
836. **`static/app/views/alerts/rules/metric/ruleForm.tsx`** -> AI Confidence: **99.24%**
837. **`static/app/views/alerts/rules/metric/triggers/thresholdControl.tsx`** -> AI Confidence: **99.24%**
838. **`static/app/views/alerts/rules/metric/wizardField.tsx`** -> AI Confidence: **99.24%**
839. **`static/app/views/alerts/rules/uptime/testUptimeMonitorButton.tsx`** -> AI Confidence: **99.24%**
840. **`static/app/views/alerts/rules/uptime/uptimeChecksGrid.tsx`** -> AI Confidence: **99.24%**
841. **`static/app/views/alerts/rules/utils.tsx`** -> AI Confidence: **99.24%**
842. **`static/app/views/auth/login.tsx`** -> AI Confidence: **99.24%**
843. **`static/app/views/automations/components/actions/email.tsx`** -> AI Confidence: **99.24%**
844. **`static/app/views/automations/components/automationHistoryList.tsx`** -> AI Confidence: **99.24%**
845. **`static/app/views/automations/components/automationListTable/actions.tsx`** -> AI Confidence: **99.24%**
846. **`static/app/views/automations/components/automationListTable/index.tsx`** -> AI Confidence: **99.24%**
847. **`static/app/views/automations/list.tsx`** -> AI Confidence: **99.24%**
848. **`static/app/views/dashboards/dashboardChatPanel.tsx`** -> AI Confidence: **99.24%**
849. **`static/app/views/dashboards/datasetConfig/base.tsx`** -> AI Confidence: **99.24%**
850. **`static/app/views/dashboards/datasetConfig/mobileAppSize.tsx`** -> AI Confidence: **99.24%**
851. **`static/app/views/dashboards/filtersBar.tsx`** -> AI Confidence: **99.24%**
852. **`static/app/views/dashboards/widgetBuilder/buildSteps/groupByStep/queryField.tsx`** -> AI Confidence: **99.24%**
853. **`static/app/views/dashboards/widgetBuilder/components/newWidgetBuilder.tsx`** -> AI Confidence: **99.24%**
854. **`static/app/views/dashboards/widgetBuilder/components/visualize/traceMetrics/aggregateSelector.tsx`** -> AI Confidence: **99.24%**
855. **`static/app/views/dashboards/widgetBuilder/components/visualize/visualizeGhostField.tsx`** -> AI Confidence: **99.24%**
856. **`static/app/views/dashboards/widgetBuilder/hooks/useWidgetBuilderTraceItemConfig.ts`** -> AI Confidence: **99.24%**
857. **`static/app/views/dashboards/widgetCard/chart.tsx`** -> AI Confidence: **99.24%**
858. **`static/app/views/dashboards/widgetCard/hooks/useErrorsAndTransactionsWidgetQuery.tsx`** -> AI Confidence: **99.24%**
859. **`static/app/views/dashboards/widgetCard/hooks/useErrorsWidgetQuery.tsx`** -> AI Confidence: **99.24%**
860. **`static/app/views/dashboards/widgetCard/hooks/useIssuesWidgetQuery.tsx`** -> AI Confidence: **99.24%**
861. **`static/app/views/dashboards/widgetCard/hooks/useLogsWidgetQuery.tsx`** -> AI Confidence: **99.24%**
862. **`static/app/views/dashboards/widgetCard/hooks/useReleasesWidgetQuery.tsx`** -> AI Confidence: **99.24%**
863. **`static/app/views/dashboards/widgetCard/hooks/useTraceMetricsWidgetQuery.tsx`** -> AI Confidence: **99.24%**
864. **`static/app/views/dashboards/widgetCard/hooks/useTransactionsWidgetQuery.tsx`** -> AI Confidence: **99.24%**
865. **`static/app/views/dashboards/widgetCard/hooks/useWidgetRawCounts.tsx`** -> AI Confidence: **99.24%**
866. **`static/app/views/dashboards/widgets/tableWidget/tableWidgetVisualization.tsx`** -> AI Confidence: **99.24%**
867. **`static/app/views/dashboards/widgets/timeSeriesWidget/formatters/formatTooltipValue.tsx`** -> AI Confidence: **99.24%**
868. **`static/app/views/dashboards/widgets/timeSeriesWidget/plottables/continuousTimeSeries.tsx`** -> AI Confidence: **99.24%**
869. **`static/app/views/dashboards/widgets/timeSeriesWidget/plottables/samples.tsx`** -> AI Confidence: **99.24%**
870. **`static/app/views/dataExport/dataDownload.tsx`** -> AI Confidence: **99.24%**
871. **`static/app/views/detectors/components/details/common/assignee.tsx`** -> AI Confidence: **99.24%**
872. **`static/app/views/detectors/components/details/metric/timePeriodSelect.tsx`** -> AI Confidence: **99.24%**
873. **`static/app/views/detectors/components/detectorLink.tsx`** -> AI Confidence: **99.24%**
874. **`static/app/views/detectors/components/forms/metric/visualize.tsx`** -> AI Confidence: **99.24%**
875. **`static/app/views/detectors/datasetConfig/utils/discoverSeries.tsx`** -> AI Confidence: **99.24%**
876. **`static/app/views/detectors/hooks/useMetricDetectorAnomalyThresholds.tsx`** -> AI Confidence: **99.24%**
877. **`static/app/views/discover/results.tsx`** -> AI Confidence: **99.24%**
878. **`static/app/views/discover/results/resultsSearchQueryBuilder.tsx`** -> AI Confidence: **99.24%**
879. **`static/app/views/discover/savedQuery/utils.tsx`** -> AI Confidence: **99.24%**
880. **`static/app/views/discover/table/quickContext/releaseContext.tsx`** -> AI Confidence: **99.24%**
881. **`static/app/views/explore/components/traceItemAttributes/attributesTreeValue.tsx`** -> AI Confidence: **99.24%**
882. **`static/app/views/explore/hooks/useGetSavedQueries.tsx`** -> AI Confidence: **99.24%**
883. **`static/app/views/explore/hooks/useTraces.tsx`** -> AI Confidence: **99.24%**
884. **`static/app/views/explore/metrics/metricInfoTabs/aggregatesTab.tsx`** -> AI Confidence: **99.24%**
885. **`static/app/views/explore/metrics/metricInfoTabs/metricsSamplesTable.tsx`** -> AI Confidence: **99.24%**
886. **`static/app/views/explore/metrics/utils.tsx`** -> AI Confidence: **99.24%**
887. **`static/app/views/explore/savedQueries/savedQueriesTable.tsx`** -> AI Confidence: **99.24%**
888. **`static/app/views/explore/spans/droppedFieldsAlert.tsx`** -> AI Confidence: **99.24%**
889. **`static/app/views/explore/spans/spansQueryParams.tsx`** -> AI Confidence: **99.24%**
890. **`static/app/views/explore/toolbar/toolbarSaveAs.tsx`** -> AI Confidence: **99.24%**
891. **`static/app/views/insights/browser/resources/components/sampleImages.tsx`** -> AI Confidence: **99.24%**
892. **`static/app/views/insights/browser/webVitals/components/charts/webVitalStatusLineChart.tsx`** -> AI Confidence: **99.24%**
893. **`static/app/views/insights/browser/webVitals/components/pageOverviewSidebar.tsx`** -> AI Confidence: **99.24%**
894. **`static/app/views/insights/browser/webVitals/components/webVitalsDetailPanel.tsx`** -> AI Confidence: **99.24%**
895. **`static/app/views/insights/browser/webVitals/queries/useWebVitalsIssuesQuery.tsx`** -> AI Confidence: **99.24%**
896. **`static/app/views/insights/common/components/fullSpanDescription.tsx`** -> AI Confidence: **99.24%**
897. **`static/app/views/insights/common/components/tableCells/starredSegmentCell.tsx`** -> AI Confidence: **99.24%**
898. **`static/app/views/insights/common/components/tableCells/timeSpentCell.tsx`** -> AI Confidence: **99.24%**
899. **`static/app/views/insights/common/views/spans/selectors/domainSelector.tsx`** -> AI Confidence: **99.24%**
900. **`static/app/views/insights/database/components/databasePageFilters.tsx`** -> AI Confidence: **99.24%**
901. **`static/app/views/insights/database/views/databaseLandingPage.tsx`** -> AI Confidence: **99.24%**
902. **`static/app/views/insights/http/components/httpSamplesPanel.tsx`** -> AI Confidence: **99.24%**
903. **`static/app/views/insights/http/queries/useSpanSamples.tsx`** -> AI Confidence: **99.24%**
904. **`static/app/views/insights/mobile/appStarts/components/eventSamples.tsx`** -> AI Confidence: **99.24%**
905. **`static/app/views/insights/pages/conversations/components/conversationSummary.tsx`** -> AI Confidence: **99.24%**
906. **`static/app/views/insights/pages/domainViewHeader.tsx`** -> AI Confidence: **99.24%**
907. **`static/app/views/insights/sessions/queries/useCrashFreeSessions.tsx`** -> AI Confidence: **99.24%**
908. **`static/app/views/insights/sessions/queries/useErroredSessions.tsx`** -> AI Confidence: **99.24%**
909. **`static/app/views/insights/sessions/queries/useSessionProjectTotal.tsx`** -> AI Confidence: **99.24%**
910. **`static/app/views/integrationOrganizationLink/index.tsx`** -> AI Confidence: **99.24%**
911. **`static/app/views/issueDetails/groupSimilarIssues/similarStackTrace/toolbar.tsx`** -> AI Confidence: **99.24%**
912. **`static/app/views/issueDetails/groupTags/tagDetailsDrawerContent.tsx`** -> AI Confidence: **99.24%**
913. **`static/app/views/issueDetails/streamline/eventGraph.tsx`** -> AI Confidence: **99.24%**
914. **`static/app/views/issueDetails/streamline/foldSection.tsx`** -> AI Confidence: **99.24%**
915. **`static/app/views/issueDetails/streamline/hooks/useIssueDetailsDiscoverQuery.tsx`** -> AI Confidence: **99.24%**
916. **`static/app/views/issueDetails/streamline/instrumentationFixSection.tsx`** -> AI Confidence: **99.24%**
917. **`static/app/views/issueDetails/streamline/occurrenceSummary.tsx`** -> AI Confidence: **99.24%**
918. **`static/app/views/issueDetails/streamline/sidebar/firstLastSeenSection.tsx`** -> AI Confidence: **99.24%**
919. **`static/app/views/issueDetails/streamline/sidebar/groupActivityItem.tsx`** -> AI Confidence: **99.24%**
920. **`static/app/views/issueDetails/streamline/sidebar/metricDetectorTriggeredSection.tsx`** -> AI Confidence: **99.24%**
921. **`static/app/views/issueDetails/streamline/sidebar/note.tsx`** -> AI Confidence: **99.24%**
922. **`static/app/views/issueDetails/streamline/sidebar/sizeAnalysisTriggeredSection.tsx`** -> AI Confidence: **99.24%**
923. **`static/app/views/issueDetails/traceTimeline/traceTimeline.tsx`** -> AI Confidence: **99.24%**
924. **`static/app/views/issueDetails/utils.tsx`** -> AI Confidence: **99.24%**
925. **`static/app/views/issueList/issueViews/createIssueViewModal.tsx`** -> AI Confidence: **99.24%**
926. **`static/app/views/issueList/issueViewsHeader.tsx`** -> AI Confidence: **99.24%**
927. **`static/app/views/issueList/noGroupsHandler/index.tsx`** -> AI Confidence: **99.24%**
928. **`static/app/views/issueList/utils/useFetchIssueTags.tsx`** -> AI Confidence: **99.24%**
929. **`static/app/views/navigation/navigationTour.tsx`** -> AI Confidence: **99.24%**
930. **`static/app/views/navigation/primary/onboarding.tsx`** -> AI Confidence: **99.24%**
931. **`static/app/views/navigation/primary/userDropdown.tsx`** -> AI Confidence: **99.24%**
932. **`static/app/views/organizationStats/mapSeriesToChart.ts`** -> AI Confidence: **99.24%**
933. **`static/app/views/organizationStats/teamInsights/controls.tsx`** -> AI Confidence: **99.24%**
934. **`static/app/views/organizationStats/teamInsights/health.tsx`** -> AI Confidence: **99.24%**
935. **`static/app/views/organizationStats/teamInsights/issues.tsx`** -> AI Confidence: **99.24%**
936. **`static/app/views/organizationStats/teamInsights/teamIssuesBreakdown.tsx`** -> AI Confidence: **99.24%**
937. **`static/app/views/organizationStats/usageChart/index.tsx`** -> AI Confidence: **99.24%**
938. **`static/app/views/performance/breadcrumb.tsx`** -> AI Confidence: **99.24%**
939. **`static/app/views/performance/charts/chart.tsx`** -> AI Confidence: **99.24%**
940. **`static/app/views/performance/newTraceDetails/traceApi/useReplayTraceMeta.tsx`** -> AI Confidence: **99.24%**
941. **`static/app/views/performance/newTraceDetails/traceApi/useTraceMeta.tsx`** -> AI Confidence: **99.24%**
942. **`static/app/views/performance/newTraceDetails/traceApi/useTraceTree.tsx`** -> AI Confidence: **99.24%**
943. **`static/app/views/performance/newTraceDetails/traceDrawer/details/profiling/profilePreview.tsx`** -> AI Confidence: **99.24%**
944. **`static/app/views/performance/newTraceDetails/traceDrawer/details/span/sections/description.tsx`** -> AI Confidence: **99.24%**
945. **`static/app/views/performance/newTraceDetails/traceDrawer/details/span/sections/keys.tsx`** -> AI Confidence: **99.24%**
946. **`static/app/views/performance/newTraceDetails/traceDrawer/details/transaction/sections/measurements.tsx`** -> AI Confidence: **99.24%**
947. **`static/app/views/performance/newTraceDetails/traceDrawer/details/utils.tsx`** -> AI Confidence: **99.24%**
948. **`static/app/views/performance/newTraceDetails/traceModels/traceTreeNode/transactionNode.tsx`** -> AI Confidence: **99.24%**
949. **`static/app/views/performance/newTraceDetails/traceOpenInExploreButton.tsx`** -> AI Confidence: **99.24%**
950. **`static/app/views/performance/newTraceDetails/traceRow/traceErrorRow.tsx`** -> AI Confidence: **99.24%**
951. **`static/app/views/performance/newTraceDetails/traceTypeWarnings/errorsOnlyWarnings.tsx`** -> AI Confidence: **99.24%**
952. **`static/app/views/performance/newTraceDetails/traceWaterfall.tsx`** -> AI Confidence: **99.24%**
953. **`static/app/views/performance/table.tsx`** -> AI Confidence: **99.24%**
954. **`static/app/views/performance/transactionSummary/transactionEvents/index.tsx`** -> AI Confidence: **99.24%**
955. **`static/app/views/performance/transactionSummary/transactionEvents/utils.tsx`** -> AI Confidence: **99.24%**
956. **`static/app/views/performance/transactionSummary/transactionOverview/trendChart/index.tsx`** -> AI Confidence: **99.24%**
957. **`static/app/views/performance/trends/utils/index.tsx`** -> AI Confidence: **99.24%**
958. **`static/app/views/preprod/buildDetails/header/buildDetailsHeaderContent.tsx`** -> AI Confidence: **99.24%**
959. **`static/app/views/preprod/install/buildInstallHeader.tsx`** -> AI Confidence: **99.24%**
960. **`static/app/views/preprod/snapshots/header/snapshotHeaderActions.tsx`** -> AI Confidence: **99.24%**
961. **`static/app/views/preprod/snapshots/header/snapshotHeaderContent.tsx`** -> AI Confidence: **99.24%**
962. **`static/app/views/profiling/profileSummary/regressedProfileFunctions.tsx`** -> AI Confidence: **99.24%**
963. **`static/app/views/projectDetail/projectLatestReleases.tsx`** -> AI Confidence: **99.24%**
964. **`static/app/views/projectEventRedirect.tsx`** -> AI Confidence: **99.24%**
965. **`static/app/views/projectInstall/createProject.tsx`** -> AI Confidence: **99.24%**
966. **`static/app/views/projectInstall/issueAlertNotificationOptions.tsx`** -> AI Confidence: **99.24%**
967. **`static/app/views/pullRequest/details/pullRequestDetails.tsx`** -> AI Confidence: **99.24%**
968. **`static/app/views/releases/detail/overview/releaseComparisonChart/releaseEventsChart.tsx`** -> AI Confidence: **99.24%**
969. **`static/app/views/releases/detail/overview/releaseIssues.tsx`** -> AI Confidence: **99.24%**
970. **`static/app/views/releases/detail/overview/sidebar/releaseAdoption.tsx`** -> AI Confidence: **99.24%**
971. **`static/app/views/releases/detail/utils.tsx`** -> AI Confidence: **99.24%**
972. **`static/app/views/releases/drawer/releasesDrawer.tsx`** -> AI Confidence: **99.24%**
973. **`static/app/views/releases/drawer/releasesDrawerDetails.tsx`** -> AI Confidence: **99.24%**
974. **`static/app/views/releases/list/mobileBuilds.tsx`** -> AI Confidence: **99.24%**
975. **`static/app/views/releases/list/mobileBuildsChart.tsx`** -> AI Confidence: **99.24%**
976. **`static/app/views/releases/list/releaseListInner.tsx`** -> AI Confidence: **99.24%**
977. **`static/app/views/releases/list/releasesRequest.tsx`** -> AI Confidence: **99.24%**
978. **`static/app/views/relocation/uploadBackup.tsx`** -> AI Confidence: **99.24%**
979. **`static/app/views/replays/detail/breadcrumbs/index.tsx`** -> AI Confidence: **99.24%**
980. **`static/app/views/replays/detail/console/index.tsx`** -> AI Confidence: **99.24%**
981. **`static/app/views/replays/detail/errorList/index.tsx`** -> AI Confidence: **99.24%**
982. **`static/app/views/replays/detail/network/details/content.tsx`** -> AI Confidence: **99.24%**
983. **`static/app/views/replays/detail/network/index.tsx`** -> AI Confidence: **99.24%**
984. **`static/app/views/replays/detail/trace/useReplayTraces.tsx`** -> AI Confidence: **99.24%**
985. **`static/app/views/routeError.tsx`** -> AI Confidence: **99.24%**
986. **`static/app/views/seerExplorer/blockComponents.tsx`** -> AI Confidence: **99.24%**
987. **`static/app/views/settings/account/accountNotificationFineTuning.tsx`** -> AI Confidence: **99.24%**
988. **`static/app/views/settings/account/accountSecurity/accountSecurityEnroll.tsx`** -> AI Confidence: **99.24%**
989. **`static/app/views/settings/account/accountSecurity/index.tsx`** -> AI Confidence: **99.24%**
990. **`static/app/views/settings/account/notifications/notificationSettingsByType.tsx`** -> AI Confidence: **99.24%**
991. **`static/app/views/settings/components/dataScrubbing/modals/dataScrubFormModal.tsx`** -> AI Confidence: **99.24%**
992. **`static/app/views/settings/components/dataScrubbing/modals/form/attributeField.tsx`** -> AI Confidence: **99.24%**
993. **`static/app/views/settings/organizationAuditLog/index.tsx`** -> AI Confidence: **99.24%**
994. **`static/app/views/settings/organizationDataForwarding/components/projectOverrideForm.tsx`** -> AI Confidence: **99.24%**
995. **`static/app/views/settings/organizationDeveloperSettings/sentryApplicationDetails.tsx`** -> AI Confidence: **99.24%**
996. **`static/app/views/settings/organizationGeneralSettings/organizationSettingsForm.tsx`** -> AI Confidence: **99.24%**
997. **`static/app/views/settings/organizationIntegrations/integrationDetailedView.tsx`** -> AI Confidence: **99.24%**
998. **`static/app/views/settings/organizationIntegrations/repositoryProjectPathConfigForm.tsx`** -> AI Confidence: **99.24%**
999. **`static/app/views/settings/organizationIntegrations/sentryAppDetailedView.tsx`** -> AI Confidence: **99.24%**
1000. **`static/app/views/settings/organizationSecurityAndPrivacy/index.tsx`** -> AI Confidence: **99.24%**
1001. **`static/app/views/settings/project/projectKeys/credentials/index.tsx`** -> AI Confidence: **99.24%**
1002. **`static/app/views/settings/project/projectOwnership/ownerInput.tsx`** -> AI Confidence: **99.24%**
1003. **`static/gsAdmin/components/customers/customerStatsFilters.tsx`** -> AI Confidence: **99.24%**
1004. **`static/gsAdmin/components/resultGrid.tsx`** -> AI Confidence: **99.24%**
1005. **`static/gsAdmin/components/users/userOverview.tsx`** -> AI Confidence: **99.24%**
1006. **`static/gsAdmin/views/broadcastDetails.tsx`** -> AI Confidence: **99.24%**
1007. **`static/gsAdmin/views/customerDetails.tsx`** -> AI Confidence: **99.24%**
1008. **`static/gsAdmin/views/invoiceDetails.tsx`** -> AI Confidence: **99.24%**
1009. **`static/gsApp/components/creditCardEdit/intentForms/innerIntentForm.tsx`** -> AI Confidence: **99.24%**
1010. **`static/gsApp/components/features/insightsDateRangeQueryLimitFooter.tsx`** -> AI Confidence: **99.24%**
1011. **`static/gsApp/components/gsBanner.tsx`** -> AI Confidence: **99.24%**
1012. **`static/gsApp/components/upgradeNowModal/usePreviewData.tsx`** -> AI Confidence: **99.24%**
1013. **`static/gsApp/components/upgradeNowModal/useUpgradeNowParams.tsx`** -> AI Confidence: **99.24%**
1014. **`static/gsApp/components/upgradeOrTrialButton.tsx`** -> AI Confidence: **99.24%**
1015. **`static/gsApp/components/upsellModal/details.tsx`** -> AI Confidence: **99.24%**
1016. **`static/gsApp/components/withSubscription.tsx`** -> AI Confidence: **99.24%**
1017. **`static/gsApp/views/seerAutomation/components/projectDetails/agentSettings/codingAgentSettings.tsx`** -> AI Confidence: **99.24%**
1018. **`static/gsApp/views/seerAutomation/components/projectDetails/agentSettings/seerAgentSettings.tsx`** -> AI Confidence: **99.24%**
1019. **`static/gsApp/views/seerAutomation/components/projectDetails/autofixRepositoriesItem.tsx`** -> AI Confidence: **99.24%**
1020. **`static/gsApp/views/seerAutomation/components/repoTable/seerRepoTableHeader.tsx`** -> AI Confidence: **99.24%**
1021. **`static/gsApp/views/seerAutomation/components/seerAutomationDefault.tsx`** -> AI Confidence: **99.24%**
1022. **`static/gsApp/views/seerAutomation/onboarding/wrapUpStep.tsx`** -> AI Confidence: **99.24%**
1023. **`static/gsApp/views/seerAutomation/repoDetails.tsx`** -> AI Confidence: **99.24%**
1024. **`static/gsApp/views/seerAutomation/settings.tsx`** -> AI Confidence: **99.24%**
1025. **`static/gsApp/views/subscriptionPage/headerCards/headerCards.tsx`** -> AI Confidence: **99.24%**
1026. **`static/gsApp/views/subscriptionPage/headerCards/nextBillCard.tsx`** -> AI Confidence: **99.24%**
1027. **`static/gsApp/views/subscriptionPage/paymentHistory.tsx`** -> AI Confidence: **99.24%**
1028. **`static/gsApp/views/subscriptionPage/subscriptionUpsellBanner.tsx`** -> AI Confidence: **99.24%**
1029. **`static/gsApp/views/subscriptionPage/usageAlert.tsx`** -> AI Confidence: **99.24%**
1030. **`static/gsApp/views/subscriptionPage/usageOverview/components/billedSeats.tsx`** -> AI Confidence: **99.24%**
1031. **`static/gsApp/views/subscriptionPage/usageOverview/components/charts.tsx`** -> AI Confidence: **99.24%**
1032. **`.github/workflows/scripts/calculate-backend-test-shards.py`** -> AI Confidence: **99.23%**
1033. **`bin/preprod/trigger_snapshot_status_check`** -> AI Confidence: **99.23%**
1034. **`bin/split-silo-database`** -> AI Confidence: **99.23%**
1035. **`bin/update-migration`** -> AI Confidence: **99.23%**
1036. **`src/sentry/api/serializers/models/exploresavedquery.py`** -> AI Confidence: **99.23%**
1037. **`src/sentry/grouping/grouping_info.py`** -> AI Confidence: **99.23%**
1038. **`src/sentry/incidents/serializers/alert_rule_trigger.py`** -> AI Confidence: **99.23%**
1039. **`src/sentry/ingest/inbound_filters.py`** -> AI Confidence: **99.23%**
1040. **`src/sentry/integrations/cursor/client.py`** -> AI Confidence: **99.23%**
1041. **`src/sentry/integrations/data_forwarding/segment/forwarder.py`** -> AI Confidence: **99.23%**
1042. **`src/sentry/preprod/size_analysis/download.py`** -> AI Confidence: **99.23%**
1043. **`src/sentry/replays/usecases/ingest/issue_creation.py`** -> AI Confidence: **99.23%**
1044. **`src/sentry/search/events/datasets/function_aliases.py`** -> AI Confidence: **99.23%**
1045. **`src/sentry/seer/entrypoints/slack/mention.py`** -> AI Confidence: **99.23%**
1046. **`src/sentry/spans/consumers/process_segments/enrichment.py`** -> AI Confidence: **99.23%**
1047. **`src/sentry/spans/gcp_log_analyzer.py`** -> AI Confidence: **99.23%**
1048. **`src/sentry/spans/log_analyzer/fetchers.py`** -> AI Confidence: **99.23%**
1049. **`src/sentry/utils/env.py`** -> AI Confidence: **99.23%**
1050. **`src/sentry/workflow_engine/handlers/condition/event_attribute_handler.py`** -> AI Confidence: **99.23%**
1051. **`src/sentry/workflow_engine/handlers/condition/tagged_event_handler.py`** -> AI Confidence: **99.23%**
1052. **`src/sentry/workflow_engine/transformers.py`** -> AI Confidence: **99.23%**
1053. **`tools/fast_editable.py`** -> AI Confidence: **99.23%**
1054. **`static/app/components/activity/note/inputWithStorage.tsx`** -> AI Confidence: **99.23%**
1055. **`static/app/components/banner.tsx`** -> AI Confidence: **99.23%**
1056. **`static/app/components/core/badge/alertBadge.tsx`** -> AI Confidence: **99.23%**
1057. **`static/app/components/core/form/field/meta.tsx`** -> AI Confidence: **99.23%**
1058. **`static/app/components/events/autofix/autofixStepFeedback.tsx`** -> AI Confidence: **99.23%**
1059. **`static/app/components/events/autofix/utils.tsx`** -> AI Confidence: **99.23%**
1060. **`static/app/components/events/contexts/knownContext/profile.tsx`** -> AI Confidence: **99.23%**
1061. **`static/app/components/events/contexts/platformContext/utils.tsx`** -> AI Confidence: **99.23%**
1062. **`static/app/components/events/interfaces/threads/threadSelector/filterThreadInfo.tsx`** -> AI Confidence: **99.23%**
1063. **`static/app/components/events/meta/annotatedText/utils.tsx`** -> AI Confidence: **99.23%**
1064. **`static/app/components/feedback/useRedirectToFeedbackFromEvent.tsx`** -> AI Confidence: **99.23%**
1065. **`static/app/components/forms/fields/checkboxField.tsx`** -> AI Confidence: **99.23%**
1066. **`static/app/components/group/issueSeerBadge.tsx`** -> AI Confidence: **99.23%**
1067. **`static/app/components/idBadge/baseBadge.tsx`** -> AI Confidence: **99.23%**
1068. **`static/app/components/infiniteList/infiniteListItems.tsx`** -> AI Confidence: **99.23%**
1069. **`static/app/components/onboarding/gettingStartedDoc/sdkDocumentation.tsx`** -> AI Confidence: **99.23%**
1070. **`static/app/components/replays/player/replayCurrentTime.tsx`** -> AI Confidence: **99.23%**
1071. **`static/app/components/replays/player/replayLoadingState.tsx`** -> AI Confidence: **99.23%**
1072. **`static/app/components/replays/player/scrubber.tsx`** -> AI Confidence: **99.23%**
1073. **`static/app/components/repositories/scmIntegrationTree/useScmIntegrationTreeData.ts`** -> AI Confidence: **99.23%**
1074. **`static/app/components/searchBar/index.tsx`** -> AI Confidence: **99.23%**
1075. **`static/app/components/searchQueryBuilder/hooks/useQueryBuilderGrid.tsx`** -> AI Confidence: **99.23%**
1076. **`static/app/components/searchQueryBuilder/tokens/filterKeyListBox/keyDescription.tsx`** -> AI Confidence: **99.23%**
1077. **`static/app/components/searchQueryBuilder/tokens/utils.tsx`** -> AI Confidence: **99.23%**
1078. **`static/app/components/searchSyntax/parser.tsx`** -> AI Confidence: **99.23%**
1079. **`static/app/components/stackTrace/exceptionGroup.tsx`** -> AI Confidence: **99.23%**
1080. **`static/app/components/structuredEventData/collapsibleValue.tsx`** -> AI Confidence: **99.23%**
1081. **`static/app/components/tables/gridEditable/index.tsx`** -> AI Confidence: **99.23%**
1082. **`static/app/utils/demoMode/utils.tsx`** -> AI Confidence: **99.23%**
1083. **`static/app/utils/profiling/hooks/useAggregateFlamegraphQuery.ts`** -> AI Confidence: **99.23%**
1084. **`static/app/utils/profiling/hooks/useProfileEvents.tsx`** -> AI Confidence: **99.23%**
1085. **`static/app/utils/profiling/hooks/useProfileEventsStats.tsx`** -> AI Confidence: **99.23%**
1086. **`static/app/utils/profiling/hooks/useProfileFunctionTrends.tsx`** -> AI Confidence: **99.23%**
1087. **`static/app/utils/profiling/hooks/useProfileFunctions.tsx`** -> AI Confidence: **99.23%**
1088. **`static/app/utils/profiling/renderers/flamegraphRenderer.tsx`** -> AI Confidence: **99.23%**
1089. **`static/app/utils/replays/hooks/useDeadRageSelectors.tsx`** -> AI Confidence: **99.23%**
1090. **`static/app/utils/useEventWaiter.tsx`** -> AI Confidence: **99.23%**
1091. **`static/app/utils/useTeamsById.tsx`** -> AI Confidence: **99.23%**
1092. **`static/app/utils/useUserTeams.tsx`** -> AI Confidence: **99.23%**
1093. **`static/app/views/admin/adminMail.tsx`** -> AI Confidence: **99.23%**
1094. **`static/app/views/admin/options.tsx`** -> AI Confidence: **99.23%**
1095. **`static/app/views/alerts/list/rules/combinedAlertBadge.tsx`** -> AI Confidence: **99.23%**
1096. **`static/app/views/alerts/utils/getComparisonMarkLines.tsx`** -> AI Confidence: **99.23%**
1097. **`static/app/views/dashboards/widgets/timeSeriesWidget/formatters/formatYAxisValue.tsx`** -> AI Confidence: **99.23%**
1098. **`static/app/views/detectors/components/forms/common/footer.tsx`** -> AI Confidence: **99.23%**
1099. **`static/app/views/detectors/components/forms/metric/useInitialMetricDetectorFormData.tsx`** -> AI Confidence: **99.23%**
1100. **`static/app/views/explore/components/table.tsx`** -> AI Confidence: **99.23%**
1101. **`static/app/views/explore/hooks/useAttributeBreakdowns.tsx`** -> AI Confidence: **99.23%**
1102. **`static/app/views/explore/hooks/useSortByFields.tsx`** -> AI Confidence: **99.23%**
1103. **`static/app/views/insights/common/components/tableCells/renderHeadCell.tsx`** -> AI Confidence: **99.23%**
1104. **`static/app/views/insights/sessions/queries/useReleaseSessionCounts.tsx`** -> AI Confidence: **99.23%**
1105. **`static/app/views/insights/sessions/queries/useReleaseSessionPercentage.tsx`** -> AI Confidence: **99.23%**
1106. **`static/app/views/issueDetails/metricKitHangProfileSection.tsx`** -> AI Confidence: **99.23%**
1107. **`static/app/views/preprod/buildDetails/main/insights/optimizeImagesModal.tsx`** -> AI Confidence: **99.23%**
1108. **`static/app/views/seerExplorer/fileChangeApprovalBlock.tsx`** -> AI Confidence: **99.23%**
1109. **`static/app/views/settings/organizationIntegrations/addIntegration.tsx`** -> AI Confidence: **99.23%**
1110. **`static/app/views/settings/project/projectOwnership/rulesPanel.tsx`** -> AI Confidence: **99.23%**
1111. **`static/gsAdmin/components/trialSubscriptionAction.tsx`** -> AI Confidence: **99.23%**
1112. **`static/gsAdmin/views/invoices.tsx`** -> AI Confidence: **99.23%**
1113. **`static/app/components/events/interfaces/crashContent/exception/useSourceMapDebuggerData.tsx`** -> AI Confidence: **99.22%**
1114. **`static/app/views/performance/newTraceDetails/traceTypeWarnings/usePerformanceSubscriptionDetails.tsx`** -> AI Confidence: **99.2%**
1115. **`fixtures/integrations/mock_service.py`** -> AI Confidence: **99.18%**
1116. **`src/django_picklefield/fields.py`** -> AI Confidence: **99.18%**
1117. **`src/sentry/api/bases/organizationmember.py`** -> AI Confidence: **99.18%**
1118. **`src/sentry/api/bases/rule.py`** -> AI Confidence: **99.18%**
1119. **`src/sentry/api/endpoints/api_application_details.py`** -> AI Confidence: **99.18%**
1120. **`src/sentry/api/endpoints/assistant.py`** -> AI Confidence: **99.18%**
1121. **`src/sentry/api/endpoints/event_attachment_details.py`** -> AI Confidence: **99.18%**
1122. **`src/sentry/api/endpoints/event_attachments.py`** -> AI Confidence: **99.18%**
1123. **`src/sentry/api/endpoints/internal/environment.py`** -> AI Confidence: **99.18%**
1124. **`src/sentry/api/endpoints/internal/feature_flags.py`** -> AI Confidence: **99.18%**
1125. **`src/sentry/api/endpoints/organization_ai_conversation_details.py`** -> AI Confidence: **99.18%**
1126. **`src/sentry/api/endpoints/organization_fork.py`** -> AI Confidence: **99.18%**
1127. **`src/sentry/api/endpoints/organization_intercom_jwt.py`** -> AI Confidence: **99.18%**
1128. **`src/sentry/api/endpoints/organization_on_demand_metrics_estimation_stats.py`** -> AI Confidence: **99.18%**
1129. **`src/sentry/api/endpoints/organization_pipeline.py`** -> AI Confidence: **99.18%**
1130. **`src/sentry/api/endpoints/organization_profiling_functions.py`** -> AI Confidence: **99.18%**
1131. **`src/sentry/api/endpoints/organization_profiling_profiles.py`** -> AI Confidence: **99.18%**
1132. **`src/sentry/api/endpoints/organization_project_keys.py`** -> AI Confidence: **99.18%**
1133. **`src/sentry/api/endpoints/organization_sdk_updates.py`** -> AI Confidence: **99.18%**
1134. **`src/sentry/api/endpoints/organization_spans_fields.py`** -> AI Confidence: **99.18%**
1135. **`src/sentry/api/endpoints/organization_tags.py`** -> AI Confidence: **99.18%**
1136. **`src/sentry/api/endpoints/organization_trace_item_stats.py`** -> AI Confidence: **99.18%**
1137. **`src/sentry/api/endpoints/organization_trace_meta.py`** -> AI Confidence: **99.18%**
1138. **`src/sentry/api/endpoints/organization_unsubscribe.py`** -> AI Confidence: **99.18%**
1139. **`src/sentry/api/endpoints/project_plugin_details.py`** -> AI Confidence: **99.18%**
1140. **`src/sentry/api/endpoints/project_tags.py`** -> AI Confidence: **99.18%**
1141. **`src/sentry/api/endpoints/project_transaction_threshold.py`** -> AI Confidence: **99.18%**
1142. **`src/sentry/api/endpoints/project_transaction_threshold_override.py`** -> AI Confidence: **99.18%**
1143. **`src/sentry/api/endpoints/relay/register_challenge.py`** -> AI Confidence: **99.18%**
1144. **`src/sentry/api/endpoints/release_thresholds/utils/get_errors_counts_timeseries.py`** -> AI Confidence: **99.18%**
1145. **`src/sentry/api/endpoints/rule_snooze.py`** -> AI Confidence: **99.18%**
1146. **`src/sentry/api/helpers/environments.py`** -> AI Confidence: **99.18%**
1147. **`src/sentry/api/serializers/base.py`** -> AI Confidence: **99.18%**
1148. **`src/sentry/api/serializers/models/filechange.py`** -> AI Confidence: **99.18%**
1149. **`src/sentry/api/serializers/models/organizationmemberinvite.py`** -> AI Confidence: **99.18%**
1150. **`src/sentry/api/serializers/models/project_key.py`** -> AI Confidence: **99.18%**
1151. **`src/sentry/audit_log/events.py`** -> AI Confidence: **99.18%**
1152. **`src/sentry/auth/access.py`** -> AI Confidence: **99.18%**
1153. **`src/sentry/auth/authenticators/__init__.py`** -> AI Confidence: **99.18%**
1154. **`src/sentry/auth/authenticators/recovery_code.py`** -> AI Confidence: **99.18%**
1155. **`src/sentry/auth/authenticators/u2f.py`** -> AI Confidence: **99.18%**
1156. **`src/sentry/auth/email.py`** -> AI Confidence: **99.18%**
1157. **`src/sentry/auth/password_validation.py`** -> AI Confidence: **99.18%**
1158. **`src/sentry/auth/providers/google/views.py`** -> AI Confidence: **99.18%**
1159. **`src/sentry/auth/providers/oauth2.py`** -> AI Confidence: **99.18%**
1160. **`src/sentry/auth/providers/saml2/generic/views.py`** -> AI Confidence: **99.18%**
1161. **`src/sentry/auth/providers/saml2/provider.py`** -> AI Confidence: **99.18%**
1162. **`src/sentry/auth/services/access/service.py`** -> AI Confidence: **99.18%**
1163. **`src/sentry/auth/services/auth/impl.py`** -> AI Confidence: **99.18%**
1164. **`src/sentry/auth/services/orgauthtoken/impl.py`** -> AI Confidence: **99.18%**
1165. **`src/sentry/auth_v2/endpoints/auth_merge_user_accounts.py`** -> AI Confidence: **99.18%**
1166. **`src/sentry/auth_v2/utils/session.py`** -> AI Confidence: **99.18%**
1167. **`src/sentry/autopilot/tasks/sdk_update.py`** -> AI Confidence: **99.18%**
1168. **`src/sentry/autopilot/tasks/trace_instrumentation.py`** -> AI Confidence: **99.18%**
1169. **`src/sentry/billing/platform/services/usage/_outcomes_query.py`** -> AI Confidence: **99.18%**
1170. **`src/sentry/charts/chartcuterie.py`** -> AI Confidence: **99.18%**
1171. **`src/sentry/conduit/auth.py`** -> AI Confidence: **99.18%**
1172. **`src/sentry/consumers/dlq.py`** -> AI Confidence: **99.18%**
1173. **`src/sentry/core/endpoints/organization_member_invite/index.py`** -> AI Confidence: **99.18%**
1174. **`src/sentry/core/endpoints/organization_member_invite/reinvite.py`** -> AI Confidence: **99.18%**
1175. **`src/sentry/core/endpoints/organization_member_requests_invite_details.py`** -> AI Confidence: **99.18%**
1176. **`src/sentry/core/endpoints/organization_member_team_details.py`** -> AI Confidence: **99.18%**
1177. **`src/sentry/core/endpoints/organization_region.py`** -> AI Confidence: **99.18%**
1178. **`src/sentry/core/endpoints/organization_teams.py`** -> AI Confidence: **99.18%**
1179. **`src/sentry/core/endpoints/project_key_stats.py`** -> AI Confidence: **99.18%**
1180. **`src/sentry/core/endpoints/scim/utils.py`** -> AI Confidence: **99.18%**
1181. **`src/sentry/core/endpoints/team_projects.py`** -> AI Confidence: **99.18%**
1182. **`src/sentry/data_export/models.py`** -> AI Confidence: **99.18%**
1183. **`src/sentry/db/models/fields/gzippeddict.py`** -> AI Confidence: **99.18%**
1184. **`src/sentry/db/models/fields/jsonfield.py`** -> AI Confidence: **99.18%**
1185. **`src/sentry/db/models/manager/base_query_set.py`** -> AI Confidence: **99.18%**
1186. **`src/sentry/debug_files/debug_files.py`** -> AI Confidence: **99.18%**
1187. **`src/sentry/debug_files/release_files.py`** -> AI Confidence: **99.18%**
1188. **`src/sentry/deletions/base.py`** -> AI Confidence: **99.18%**
1189. **`src/sentry/deletions/tasks/hybrid_cloud.py`** -> AI Confidence: **99.18%**
1190. **`src/sentry/deletions/tasks/nodestore.py`** -> AI Confidence: **99.18%**
1191. **`src/sentry/digests/backends/base.py`** -> AI Confidence: **99.18%**
1192. **`src/sentry/discover/endpoints/discover_homepage_query.py`** -> AI Confidence: **99.18%**
1193. **`src/sentry/dynamic_sampling/rules/utils.py`** -> AI Confidence: **99.18%**
1194. **`src/sentry/dynamic_sampling/utils.py`** -> AI Confidence: **99.18%**
1195. **`src/sentry/eventstream/kafka/dispatch.py`** -> AI Confidence: **99.18%**
1196. **`src/sentry/explore/endpoints/explore_saved_query_starred.py`** -> AI Confidence: **99.18%**
1197. **`src/sentry/explore/models.py`** -> AI Confidence: **99.18%**
1198. **`src/sentry/feedback/endpoints/organization_feedback_summary.py`** -> AI Confidence: **99.18%**
1199. **`src/sentry/feedback/endpoints/project_user_reports.py`** -> AI Confidence: **99.18%**
1200. **`src/sentry/flags/endpoints/logs.py`** -> AI Confidence: **99.18%**
1201. **`src/sentry/flags/models.py`** -> AI Confidence: **99.18%**
1202. **`src/sentry/hybridcloud/outbox/base.py`** -> AI Confidence: **99.18%**
1203. **`src/sentry/hybridcloud/rpc/__init__.py`** -> AI Confidence: **99.18%**
1204. **`src/sentry/hybridcloud/rpc/caching/service.py`** -> AI Confidence: **99.18%**
1205. **`src/sentry/hybridcloud/services/control_organization_provisioning/impl.py`** -> AI Confidence: **99.18%**
1206. **`src/sentry/hybridcloud/services/replica/impl.py`** -> AI Confidence: **99.18%**
1207. **`src/sentry/identity/oauth2.py`** -> AI Confidence: **99.18%**
1208. **`src/sentry/identity/services/identity/impl.py`** -> AI Confidence: **99.18%**
1209. **`src/sentry/incidents/action_handlers.py`** -> AI Confidence: **99.18%**
1210. **`src/sentry/incidents/endpoints/organization_alert_rule_details.py`** -> AI Confidence: **99.18%**
1211. **`src/sentry/incidents/endpoints/organization_incident_details.py`** -> AI Confidence: **99.18%**
1212. **`src/sentry/incidents/endpoints/organization_incident_index.py`** -> AI Confidence: **99.18%**
1213. **`src/sentry/incidents/endpoints/serializers/incident.py`** -> AI Confidence: **99.18%**
1214. **`src/sentry/incidents/subscription_processor.py`** -> AI Confidence: **99.18%**
1215. **`src/sentry/incidents/tasks.py`** -> AI Confidence: **99.18%**
1216. **`src/sentry/incidents/utils/process_update_helpers.py`** -> AI Confidence: **99.18%**
1217. **`src/sentry/ingest/consumer/factory.py`** -> AI Confidence: **99.18%**
1218. **`src/sentry/ingest/transaction_clusterer/datasource/redis.py`** -> AI Confidence: **99.18%**
1219. **`src/sentry/ingest/transaction_clusterer/rules.py`** -> AI Confidence: **99.18%**
1220. **`src/sentry/ingest/transaction_clusterer/tasks.py`** -> AI Confidence: **99.18%**
1221. **`src/sentry/integrations/api/bases/doc_integrations.py`** -> AI Confidence: **99.18%**
1222. **`src/sentry/integrations/api/endpoints/integration_proxy.py`** -> AI Confidence: **99.18%**
1223. **`src/sentry/integrations/api/endpoints/organization_code_mappings.py`** -> AI Confidence: **99.18%**
1224. **`src/sentry/integrations/api/endpoints/organization_coding_agents.py`** -> AI Confidence: **99.18%**
1225. **`src/sentry/integrations/api/endpoints/organization_integration_direct_enable.py`** -> AI Confidence: **99.18%**
1226. **`src/sentry/integrations/aws_lambda/integration.py`** -> AI Confidence: **99.18%**
1227. **`src/sentry/integrations/bitbucket/issues.py`** -> AI Confidence: **99.18%**
1228. **`src/sentry/integrations/bitbucket/repository.py`** -> AI Confidence: **99.18%**
1229. **`src/sentry/integrations/bitbucket/webhook.py`** -> AI Confidence: **99.18%**
1230. **`src/sentry/integrations/bitbucket_server/repository.py`** -> AI Confidence: **99.18%**
1231. **`src/sentry/integrations/bitbucket_server/webhook.py`** -> AI Confidence: **99.18%**
1232. **`src/sentry/integrations/claude_code/integration.py`** -> AI Confidence: **99.18%**
1233. **`src/sentry/integrations/cursor/webhooks/handler.py`** -> AI Confidence: **99.18%**
1234. **`src/sentry/integrations/data_forwarding/amazon_sqs/forwarder.py`** -> AI Confidence: **99.18%**
1235. **`src/sentry/integrations/discord/actions/issue_alert/form.py`** -> AI Confidence: **99.18%**
1236. **`src/sentry/integrations/discord/client.py`** -> AI Confidence: **99.18%**
1237. **`src/sentry/integrations/discord/integration.py`** -> AI Confidence: **99.18%**
1238. **`src/sentry/integrations/github/client.py`** -> AI Confidence: **99.18%**
1239. **`src/sentry/integrations/github/tasks/link_all_repos.py`** -> AI Confidence: **99.18%**
1240. **`src/sentry/integrations/github/utils.py`** -> AI Confidence: **99.18%**
1241. **`src/sentry/integrations/github_enterprise/integration.py`** -> AI Confidence: **99.18%**
1242. **`src/sentry/integrations/github_enterprise/webhook.py`** -> AI Confidence: **99.18%**
1243. **`src/sentry/integrations/gitlab/issue_sync.py`** -> AI Confidence: **99.18%**
1244. **`src/sentry/integrations/gitlab/tasks.py`** -> AI Confidence: **99.18%**
1245. **`src/sentry/integrations/jira/endpoints/search.py`** -> AI Confidence: **99.18%**
1246. **`src/sentry/integrations/jira_server/search.py`** -> AI Confidence: **99.18%**
1247. **`src/sentry/integrations/messaging/commands.py`** -> AI Confidence: **99.18%**
1248. **`src/sentry/integrations/messaging/linkage.py`** -> AI Confidence: **99.18%**
1249. **`src/sentry/integrations/middleware/hybrid_cloud/parser.py`** -> AI Confidence: **99.18%**
1250. **`src/sentry/integrations/mixins/issues.py`** -> AI Confidence: **99.18%**
1251. **`src/sentry/integrations/msteams/actions/form.py`** -> AI Confidence: **99.18%**
1252. **`src/sentry/integrations/msteams/card_builder/notifications.py`** -> AI Confidence: **99.18%**
1253. **`src/sentry/integrations/msteams/notifications.py`** -> AI Confidence: **99.18%**
1254. **`src/sentry/integrations/msteams/webhook.py`** -> AI Confidence: **99.18%**
1255. **`src/sentry/integrations/opsgenie/actions/form.py`** -> AI Confidence: **99.18%**
1256. **`src/sentry/integrations/opsgenie/client.py`** -> AI Confidence: **99.18%**
1257. **`src/sentry/integrations/opsgenie/utils.py`** -> AI Confidence: **99.18%**
1258. **`src/sentry/integrations/pagerduty/actions/notification.py`** -> AI Confidence: **99.18%**
1259. **`src/sentry/integrations/pagerduty/client.py`** -> AI Confidence: **99.18%**
1260. **`src/sentry/integrations/pagerduty/integration.py`** -> AI Confidence: **99.18%**
1261. **`src/sentry/integrations/perforce/repository.py`** -> AI Confidence: **99.18%**
1262. **`src/sentry/integrations/repository/metric_alert.py`** -> AI Confidence: **99.18%**
1263. **`src/sentry/integrations/slack/message_builder/base/block.py`** -> AI Confidence: **99.18%**
1264. **`src/sentry/integrations/slack/message_builder/util.py`** -> AI Confidence: **99.18%**
1265. **`src/sentry/integrations/slack/requests/base.py`** -> AI Confidence: **99.18%**
1266. **`src/sentry/integrations/slack/tasks/find_channel_id_for_alert_rule.py`** -> AI Confidence: **99.18%**
1267. **`src/sentry/integrations/slack/unfurl/issues.py`** -> AI Confidence: **99.18%**
1268. **`src/sentry/integrations/slack/unfurl/metric_alerts.py`** -> AI Confidence: **99.18%**
1269. **`src/sentry/integrations/slack/utils/notifications.py`** -> AI Confidence: **99.18%**
1270. **`src/sentry/integrations/slack/utils/users.py`** -> AI Confidence: **99.18%**
1271. **`src/sentry/integrations/source_code_management/metrics.py`** -> AI Confidence: **99.18%**
1272. **`src/sentry/integrations/source_code_management/repository.py`** -> AI Confidence: **99.18%**
1273. **`src/sentry/integrations/tasks/migrate_repo.py`** -> AI Confidence: **99.18%**
1274. **`src/sentry/integrations/utils/codecov.py`** -> AI Confidence: **99.18%**
1275. **`src/sentry/integrations/utils/issue_summary_for_alerts.py`** -> AI Confidence: **99.18%**
1276. **`src/sentry/integrations/utils/metrics.py`** -> AI Confidence: **99.18%**
1277. **`src/sentry/integrations/utils/stacktrace_link.py`** -> AI Confidence: **99.18%**
1278. **`src/sentry/integrations/vercel/integration.py`** -> AI Confidence: **99.18%**
1279. **`src/sentry/integrations/vercel/webhook.py`** -> AI Confidence: **99.18%**
1280. **`src/sentry/integrations/vsts/client.py`** -> AI Confidence: **99.18%**
1281. **`src/sentry/integrations/vsts/integration.py`** -> AI Confidence: **99.18%**
1282. **`src/sentry/integrations/vsts/repository.py`** -> AI Confidence: **99.18%**
1283. **`src/sentry/integrations/vsts/tasks/subscription_check.py`** -> AI Confidence: **99.18%**
1284. **`src/sentry/integrations/vsts/webhooks.py`** -> AI Confidence: **99.18%**
1285. **`src/sentry/integrations/web/integration_extension_configuration.py`** -> AI Confidence: **99.18%**
1286. **`src/sentry/interfaces/contexts.py`** -> AI Confidence: **99.18%**
1287. **`src/sentry/issues/auto_source_code_config/task.py`** -> AI Confidence: **99.18%**
1288. **`src/sentry/issues/endpoints/bases/group.py`** -> AI Confidence: **99.18%**
1289. **`src/sentry/issues/endpoints/event_owners.py`** -> AI Confidence: **99.18%**
1290. **`src/sentry/issues/endpoints/group_attachments.py`** -> AI Confidence: **99.18%**
1291. **`src/sentry/issues/endpoints/group_reprocessing.py`** -> AI Confidence: **99.18%**
1292. **`src/sentry/issues/endpoints/group_similar_issues.py`** -> AI Confidence: **99.18%**
1293. **`src/sentry/issues/endpoints/group_similar_issues_embeddings.py`** -> AI Confidence: **99.18%**
1294. **`src/sentry/issues/endpoints/organization_group_search_view_details_starred.py`** -> AI Confidence: **99.18%**
1295. **`src/sentry/issues/endpoints/organization_group_search_views.py`** -> AI Confidence: **99.18%**
1296. **`src/sentry/issues/endpoints/project_stacktrace_link.py`** -> AI Confidence: **99.18%**
1297. **`src/sentry/issues/endpoints/serializers.py`** -> AI Confidence: **99.18%**
1298. **`src/sentry/issues/endpoints/shared_group_details.py`** -> AI Confidence: **99.18%**
1299. **`src/sentry/issues/escalating/forecasts.py`** -> AI Confidence: **99.18%**
1300. **`src/sentry/issues/issue_occurrence.py`** -> AI Confidence: **99.18%**
1301. **`src/sentry/issues/ongoing.py`** -> AI Confidence: **99.18%**
1302. **`src/sentry/issues/producer.py`** -> AI Confidence: **99.18%**
1303. **`src/sentry/issues/related/trace_connected.py`** -> AI Confidence: **99.18%**
1304. **`src/sentry/issues/services/issue/impl.py`** -> AI Confidence: **99.18%**
1305. **`src/sentry/issues/suspect_tags.py`** -> AI Confidence: **99.18%**
1306. **`src/sentry/issues/update_inbox.py`** -> AI Confidence: **99.18%**
1307. **`src/sentry/lang/javascript/plugin.py`** -> AI Confidence: **99.18%**
1308. **`src/sentry/mail/actions.py`** -> AI Confidence: **99.18%**
1309. **`src/sentry/mail/notifications.py`** -> AI Confidence: **99.18%**
1310. **`src/sentry/middleware/access_log.py`** -> AI Confidence: **99.18%**
1311. **`src/sentry/middleware/demo_mode_guard.py`** -> AI Confidence: **99.18%**
1312. **`src/sentry/middleware/integrations/parsers/github.py`** -> AI Confidence: **99.18%**
1313. **`src/sentry/middleware/integrations/parsers/msteams.py`** -> AI Confidence: **99.18%**
1314. **`src/sentry/middleware/stats.py`** -> AI Confidence: **99.18%**
1315. **`src/sentry/migrations/0952_fix_span_item_event_type_alerts.py`** -> AI Confidence: **99.18%**
1316. **`src/sentry/models/activity.py`** -> AI Confidence: **99.18%**
1317. **`src/sentry/models/artifactbundle.py`** -> AI Confidence: **99.18%**
1318. **`src/sentry/models/avatars/base.py`** -> AI Confidence: **99.18%**
1319. **`src/sentry/models/eventattachment.py`** -> AI Confidence: **99.18%**
1320. **`src/sentry/models/files/abstractfileblob.py`** -> AI Confidence: **99.18%**
1321. **`src/sentry/models/files/utils.py`** -> AI Confidence: **99.18%**
1322. **`src/sentry/models/groupassignee.py`** -> AI Confidence: **99.18%**
1323. **`src/sentry/models/grouphashmetadata.py`** -> AI Confidence: **99.18%**
1324. **`src/sentry/models/grouphistory.py`** -> AI Confidence: **99.18%**
1325. **`src/sentry/models/groupopenperiod.py`** -> AI Confidence: **99.18%**
1326. **`src/sentry/models/groupresolution.py`** -> AI Confidence: **99.18%**
1327. **`src/sentry/models/groupsearchviewstarred.py`** -> AI Confidence: **99.18%**
1328. **`src/sentry/models/options/organization_option.py`** -> AI Confidence: **99.18%**
1329. **`src/sentry/models/organization.py`** -> AI Confidence: **99.18%**
1330. **`src/sentry/models/organizationaccessrequest.py`** -> AI Confidence: **99.18%**
1331. **`src/sentry/models/organizationmember.py`** -> AI Confidence: **99.18%**
1332. **`src/sentry/models/project.py`** -> AI Confidence: **99.18%**
1333. **`src/sentry/models/projectcodeowners.py`** -> AI Confidence: **99.18%**
1334. **`src/sentry/models/projectsdk.py`** -> AI Confidence: **99.18%**
1335. **`src/sentry/models/release.py`** -> AI Confidence: **99.18%**
1336. **`src/sentry/models/releaseenvironment.py`** -> AI Confidence: **99.18%**
1337. **`src/sentry/models/releasefile.py`** -> AI Confidence: **99.18%**
1338. **`src/sentry/models/releaseprojectenvironment.py`** -> AI Confidence: **99.18%**
1339. **`src/sentry/monitors/endpoints/base.py`** -> AI Confidence: **99.18%**
1340. **`src/sentry/monitors/endpoints/base_monitor_details.py`** -> AI Confidence: **99.18%**
1341. **`src/sentry/monitors/endpoints/base_monitor_stats.py`** -> AI Confidence: **99.18%**
1342. **`src/sentry/monitors/logic/incident_occurrence.py`** -> AI Confidence: **99.18%**
1343. **`src/sentry/monitors/processing_errors/manager.py`** -> AI Confidence: **99.18%**
1344. **`src/sentry/monitors/tasks/detect_broken_monitor_envs.py`** -> AI Confidence: **99.18%**
1345. **`src/sentry/monitors/utils.py`** -> AI Confidence: **99.18%**
1346. **`src/sentry/notifications/helpers.py`** -> AI Confidence: **99.18%**
1347. **`src/sentry/notifications/notification_action/issue_alert_registry/handlers/opsgenie_issue_alert_handler.py`** -> AI Confidence: **99.18%**
1348. **`src/sentry/notifications/notification_action/issue_alert_registry/handlers/pagerduty_issue_alert_handler.py`** -> AI Confidence: **99.18%**
1349. **`src/sentry/notifications/notification_action/types.py`** -> AI Confidence: **99.18%**
1350. **`src/sentry/notifications/notifications/activity/release.py`** -> AI Confidence: **99.18%**
1351. **`src/sentry/notifications/notifications/base.py`** -> AI Confidence: **99.18%**
1352. **`src/sentry/notifications/notifications/digest.py`** -> AI Confidence: **99.18%**
1353. **`src/sentry/notifications/platform/discord/provider.py`** -> AI Confidence: **99.18%**
1354. **`src/sentry/notifications/platform/email/provider.py`** -> AI Confidence: **99.18%**
1355. **`src/sentry/notifications/platform/msteams/provider.py`** -> AI Confidence: **99.18%**
1356. **`src/sentry/notifications/platform/rollout.py`** -> AI Confidence: **99.18%**
1357. **`src/sentry/notifications/platform/slack/provider.py`** -> AI Confidence: **99.18%**
1358. **`src/sentry/notifications/services/impl.py`** -> AI Confidence: **99.18%**
1359. **`src/sentry/notifications/utils/avatar.py`** -> AI Confidence: **99.18%**
1360. **`src/sentry/objectstore/__init__.py`** -> AI Confidence: **99.18%**
1361. **`src/sentry/pipeline/base.py`** -> AI Confidence: **99.18%**
1362. **`src/sentry/plugins/bases/issue.py`** -> AI Confidence: **99.18%**
1363. **`src/sentry/plugins/bases/issue2.py`** -> AI Confidence: **99.18%**
1364. **`src/sentry/plugins/providers/repository.py`** -> AI Confidence: **99.18%**
1365. **`src/sentry/preprod/api/endpoints/preprod_artifact_admin_batch_delete.py`** -> AI Confidence: **99.18%**
1366. **`src/sentry/preprod/api/endpoints/project_preprod_artifact_assemble_generic.py`** -> AI Confidence: **99.18%**
1367. **`src/sentry/preprod/api/endpoints/project_preprod_artifact_download.py`** -> AI Confidence: **99.18%**
1368. **`src/sentry/preprod/api/endpoints/project_preprod_artifact_install_details.py`** -> AI Confidence: **99.18%**
1369. **`src/sentry/preprod/api/endpoints/public/organization_preprod_size_analysis.py`** -> AI Confidence: **99.18%**
1370. **`src/sentry/preprod/api/endpoints/public/project_preprod_build_distribution_latest.py`** -> AI Confidence: **99.18%**
1371. **`src/sentry/preprod/api/endpoints/pull_request/organization_pullrequest_comments.py`** -> AI Confidence: **99.18%**
1372. **`src/sentry/preprod/api/endpoints/pull_request/organization_pullrequest_details.py`** -> AI Confidence: **99.18%**
1373. **`src/sentry/preprod/models.py`** -> AI Confidence: **99.18%**
1374. **`src/sentry/preprod/quotas.py`** -> AI Confidence: **99.18%**
1375. **`src/sentry/processing_errors/detection.py`** -> AI Confidence: **99.18%**
1376. **`src/sentry/processing_errors/eap/producer.py`** -> AI Confidence: **99.18%**
1377. **`src/sentry/profiles/consumers/process/factory.py`** -> AI Confidence: **99.18%**
1378. **`src/sentry/projects/project_rules/updater.py`** -> AI Confidence: **99.18%**
1379. **`src/sentry/projects/services/project/serial.py`** -> AI Confidence: **99.18%**
1380. **`src/sentry/ratelimits/leaky_bucket.py`** -> AI Confidence: **99.18%**
1381. **`src/sentry/ratelimits/redis.py`** -> AI Confidence: **99.18%**
1382. **`src/sentry/receivers/core.py`** -> AI Confidence: **99.18%**
1383. **`src/sentry/receivers/onboarding.py`** -> AI Confidence: **99.18%**
1384. **`src/sentry/receivers/rules.py`** -> AI Confidence: **99.18%**
1385. **`src/sentry/receivers/sentry_apps.py`** -> AI Confidence: **99.18%**
1386. **`src/sentry/receivers/users.py`** -> AI Confidence: **99.18%**
1387. **`src/sentry/relay/projectconfig_cache/redis.py`** -> AI Confidence: **99.18%**
1388. **`src/sentry/releases/endpoints/organization_release_health_data.py`** -> AI Confidence: **99.18%**
1389. **`src/sentry/releases/endpoints/organization_release_meta.py`** -> AI Confidence: **99.18%**
1390. **`src/sentry/releases/endpoints/project_release_file_details.py`** -> AI Confidence: **99.18%**
1391. **`src/sentry/releases/endpoints/project_release_stats.py`** -> AI Confidence: **99.18%**
1392. **`src/sentry/releases/endpoints/project_releases.py`** -> AI Confidence: **99.18%**
1393. **`src/sentry/releases/endpoints/release_deploys.py`** -> AI Confidence: **99.18%**
1394. **`src/sentry/releases/serializers/release.py`** -> AI Confidence: **99.18%**
1395. **`src/sentry/relocation/api/endpoints/cancel.py`** -> AI Confidence: **99.18%**
1396. **`src/sentry/relocation/api/endpoints/index.py`** -> AI Confidence: **99.18%**
1397. **`src/sentry/relocation/api/endpoints/unpause.py`** -> AI Confidence: **99.18%**
1398. **`src/sentry/relocation/models/relocation.py`** -> AI Confidence: **99.18%**
1399. **`src/sentry/relocation/utils.py`** -> AI Confidence: **99.18%**
1400. **`src/sentry/remote_subscriptions/consumers/result_consumer.py`** -> AI Confidence: **99.18%**
1401. **`src/sentry/replays/data_export.py`** -> AI Confidence: **99.18%**
1402. **`src/sentry/replays/lib/eap/write.py`** -> AI Confidence: **99.18%**
1403. **`src/sentry/replays/lib/new_query/fields.py`** -> AI Confidence: **99.18%**
1404. **`src/sentry/replays/permissions.py`** -> AI Confidence: **99.18%**
1405. **`src/sentry/replays/scripts/delete_replays.py`** -> AI Confidence: **99.18%**
1406. **`src/sentry/replays/usecases/query/configs/scalar.py`** -> AI Confidence: **99.18%**
1407. **`src/sentry/rules/__init__.py`** -> AI Confidence: **99.18%**
1408. **`src/sentry/rules/conditions/level.py`** -> AI Confidence: **99.18%**
1409. **`src/sentry/rules/filters/assigned_to.py`** -> AI Confidence: **99.18%**
1410. **`src/sentry/rules/filters/issue_type.py`** -> AI Confidence: **99.18%**
1411. **`src/sentry/rules/filters/latest_release.py`** -> AI Confidence: **99.18%**
1412. **`src/sentry/rules/history/backends/postgres.py`** -> AI Confidence: **99.18%**
1413. **`src/sentry/runner/commands/createproject.py`** -> AI Confidence: **99.18%**
1414. **`src/sentry/scm/endpoints/scm_rpc.py`** -> AI Confidence: **99.18%**
1415. **`src/sentry/scm/private/helpers.py`** -> AI Confidence: **99.18%**
1416. **`src/sentry/scm/private/providers/github.py`** -> AI Confidence: **99.18%**
1417. **`src/sentry/scm/private/providers/gitlab.py`** -> AI Confidence: **99.18%**
1418. **`src/sentry/search/eap/columns.py`** -> AI Confidence: **99.18%**
1419. **`src/sentry/search/eap/trace_metrics/formulas.py`** -> AI Confidence: **99.18%**
1420. **`src/sentry/search/events/builder/errors.py`** -> AI Confidence: **99.18%**
1421. **`src/sentry/search/events/builder/sessions.py`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `fixtures/vercel.py` -> **100.0%** Exposure
- `src/sentry_plugins/github/testutils.py` -> **100.0%** Exposure
- `tests/sentry/api/endpoints/test_auth_validate.py` -> **100.0%** Exposure
- `tests/sentry/event_manager/interfaces/test_expectct.py` -> **100.0%** Exposure
- `tests/sentry/event_manager/interfaces/test_expectstaple.py` -> **100.0%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `102` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `119642` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `static/app/utils/cursorPoller.tsx` (TYPESCRIPT) -> Cumulative Risk: **735.37**
- **Archetype:** `file_cluster_4` (Distance: 14.148 IQR)
- **Magnitude:** 17.45 | **LOC:** 120 | **CtrlFlow:** 54.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9506%)
- **Heaviest Functions:** `poll` (Impact: 27.9), `success` (Impact: 27.2), `error` (Impact: 9.4)

### 2. `static/app/components/profiling/flamegraph/interactions/useViewKeyboardNavigation.tsx` (TYPESCRIPT) -> Cumulative Risk: **705.62**
- **Archetype:** `file_cluster_4` (Distance: 12.746 IQR)
- **Magnitude:** 27.67 | **LOC:** 177 | **CtrlFlow:** 52.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.8841%)
- **Heaviest Functions:** `useViewKeyboardNavigation` (Impact: 51.5), `onKeyDown` (Impact: 45.9), `useEffect` (Impact: 37.5)

### 3. `static/app/stores/alertStore.tsx` (TYPESCRIPT) -> Cumulative Risk: **681.68**
- **Archetype:** `file_cluster_17` (Distance: 11.336 IQR)
- **Magnitude:** 7.88 | **LOC:** 112 | **CtrlFlow:** 53.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Safety Score (99.941%), Tech Debt (99.708%)
- **Heaviest Functions:** `closeAlert` (Impact: 29.1), `addAlert` (Impact: 21.9), `init` (Impact: 1.8)

### 4. `static/app/stores/groupingStore.tsx` (TYPESCRIPT) -> Cumulative Risk: **679.61**
- **Archetype:** `file_cluster_17` (Distance: 12.119 IQR)
- **Magnitude:** 39.08 | **LOC:** 645 | **CtrlFlow:** 42.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9999%), Concurrency (98.7133%), Cognitive Load (94.7811%)
- **Heaviest Functions:** `triggerUnmergeState` (Impact: 56.7), `onFetch` (Impact: 24.8), `reject` (Impact: 16.7)

### 5. `src/sentry/hybridcloud/apigateway_async/circuitbreaker.py` (PYTHON) -> Cumulative Risk: **671.39**
- **Archetype:** `file_cluster_16` (Distance: 10.308 IQR)
- **Magnitude:** 68.18 | **LOC:** 105 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9513%), Concurrency (99.0973%)
- **Heaviest Functions:** `__aenter__` (Impact: 6.4), `_maybe_counter_flip` (Impact: 5.5), `__init__` (Impact: 2.4)

### 6. `static/app/views/onboarding/createSampleEventButton.tsx` (TYPESCRIPT) -> Cumulative Risk: **669.32**
- **Archetype:** `file_cluster_13` (Distance: 11.749 IQR)
- **Magnitude:** 13.63 | **LOC:** 215 | **CtrlFlow:** 35.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.999%)
- **Heaviest Functions:** `createSampleGroup` (Impact: 23.3), `addErrorMessage` (Impact: 5.5), `render` (Impact: 3.8)

### 7. `static/app/components/autoComplete.tsx` (TYPESCRIPT) -> Cumulative Risk: **668.07**
- **Archetype:** `file_cluster_11` (Distance: 14.262 IQR)
- **Magnitude:** 69.4 | **LOC:** 542 | **CtrlFlow:** 47.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.4071%)
- **Heaviest Functions:** `children` (Impact: 153.6), `makeHandleInputChange` (Impact: 121.0), `makeHandleInputKeydown` (Impact: 30.8)

### 8. `static/app/views/settings/organizationIntegrations/sentryAppExternalForm.tsx` (TYPESCRIPT) -> Cumulative Risk: **664.07**
- **Archetype:** `file_cluster_17` (Distance: 12.756 IQR)
- **Magnitude:** 21.55 | **LOC:** 484 | **CtrlFlow:** 47.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (98.2197%)
- **Heaviest Functions:** `resetStateFromProps` (Impact: 48.3), `getDefaultOptions` (Impact: 19.1), `hasValue` (Impact: 18.6)

### 9. `src/sentry/spans/consumers/process/flusher.py` (PYTHON) -> Cumulative Risk: **652.02**
- **Archetype:** `file_cluster_13` (Distance: 11.891 IQR)
- **Magnitude:** 250.3 | **LOC:** 528 | **CtrlFlow:** 52.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.3957%), State Flux (99.0283%), Concurrency (97.0497%)
- **Heaviest Functions:** `submit` (Impact: 32.7), `_ensure_processes_alive` (Impact: 21.2), `join` (Impact: 18.3)

### 10. `src/sentry/templates/sentry/error-page-embed.js` (JAVASCRIPT) -> Cumulative Risk: **650.98**
- **Archetype:** `file_cluster_11` (Distance: 13.787 IQR)
- **Magnitude:** 284.9 | **LOC:** 222 | **CtrlFlow:** 45.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (96.0052%)
- **Heaviest Functions:** `build` (Impact: 26.4), `submit` (Impact: 13.3), `handleFocus` (Impact: 13.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/sentry/integrations/jira_server/integration.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.433 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.56 IQR)
- **Top Global Matches:** file_cluster_8: 10.433, file_cluster_13: 10.68, file_cluster_7: 10.973
- **Magnitude:** 13295.7 | **LOC:** 1463 | **CtrlFlow:** 41.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.5757%), Tech Debt (16.2344%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 187`, `structural_boundaries: 269`, `args: 44`, `func_start: 43`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 35`, `dead_code: 1`, `planned_debt: 7`, `fragile_debt: 4`
* *Architecture:* `io: 2`, `api: 44`, `import: 42`
* *Defense:* `safety: 48`, `doc: 41`, `test: 4`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.033
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 21):` django.utils.decorators, sentry.integrations.models.integration_external_project, sentry.pipeline.views.base, django.core.validators, sentry.models.group, sentry.organizations.services.organization.service, sentry.users.models.identity, sentry.users.services.user...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/sentry/integrations/jira/integration.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.829 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.75 IQR)
- **Top Global Matches:** file_cluster_8: 10.829, file_cluster_13: 10.938, file_cluster_16: 11.281
- **Magnitude:** 12929.36 | **LOC:** 1248 | **CtrlFlow:** 43.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (8.9513%), Tech Debt (20.2144%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 181`, `structural_boundaries: 236`, `args: 45`, `func_start: 44`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 37`, `dead_code: 1`, `planned_debt: 9`, `fragile_debt: 4`
* *Architecture:* `io: 1`, `api: 41`, `import: 41`
* *Defense:* `safety: 50`, `doc: 34`, `test: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.035
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 22):` .utils, sentry.integrations.models.integration_external_project, sentry.pipeline.views.base, django.conf, sentry.models.group, sentry.organizations.services.organization.service, sentry.utils.strings, sentry.users.models.identity...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `api-docs/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/sentry/testutils/pytest/template/credentials.json` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/sentry/integrations/gitlab/integration.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.433 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.973 IQR)
- **Top Global Matches:** file_cluster_8: 9.433, file_cluster_13: 9.544, file_cluster_16: 9.709
- **Magnitude:** 2799.23 | **LOC:** 781 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (4.9801%), Tech Debt (12.7273%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 196`, `args: 38`, `func_start: 36`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 7`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `api: 40`, `import: 46`
* *Defense:* `safety: 9`, `doc: 24`, `test: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.044
  * `Choke Point (Betweenness):` 0.0002 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 26):` .utils, sentry.identity.pipeline, sentry.pipeline.views.base, sentry.models.group, rest_framework.fields, sentry.identity.gitlab.provider, sentry.users.models.identity, sentry.pipeline.views.nested...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/sentry/web/forms/accounts.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.807 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.178 IQR)
- **Top Global Matches:** file_cluster_8: 8.807, file_cluster_13: 8.905, file_cluster_7: 9.521
- **Magnitude:** 1690.68 | **LOC:** 261 | **CtrlFlow:** 33.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.2779%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 77`, `args: 15`, `func_start: 14`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 7`
* *Architecture:* `api: 15`, `import: 18`
* *Defense:* `safety: 3`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.039
  * `Choke Point (Betweenness):` 2.5e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` django.utils.text, sentry, sentry.utils.auth, typing, django.db.models, django.conf, sentry.utils.dates, sentry.web.forms.fields...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/sentry/integrations/bitbucket_server/integration.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.302 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.825 IQR)
- **Top Global Matches:** file_cluster_8: 9.302, file_cluster_13: 9.405, file_cluster_16: 9.717
- **Magnitude:** 1455.4 | **LOC:** 458 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (3.5352%), Tech Debt (12.709%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 130`, `args: 22`, `func_start: 21`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 6`, `fragile_debt: 1`
* *Architecture:* `io: 2`, `api: 27`, `import: 32`
* *Defense:* `safety: 10`, `doc: 22`, `test: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.04
  * `Choke Point (Betweenness):` 7e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` django.utils.decorators, sentry.pipeline.views.base, django.core.validators, sentry.users.models.identity, sentry.integrations.types, collections.abc, sentry.integrations.models.integration, django.utils.translation...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/sentry/integrations/discord/integration.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.09 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.767 IQR)
- **Top Global Matches:** file_cluster_13: 10.09, file_cluster_8: 10.144, file_cluster_16: 10.495
- **Magnitude:** 1442.52 | **LOC:** 335 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (8.9148%), Tech Debt (14.6202%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 96`, `args: 14`, `func_start: 14`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 11`, `fragile_debt: 1`
* *Architecture:* `api: 12`, `import: 26`
* *Defense:* `safety: 17`, `doc: 4`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.033
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` .utils, sentry.pipeline.views.base, sentry.integrations.types, collections.abc, sentry.integrations.discord.types, sentry.integrations.models.integration, sentry.notifications.platform.discord.provider, sentry.notifications.platform.target...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/sentry/integrations/opsgenie/integration.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.398 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.272 IQR)
- **Top Global Matches:** file_cluster_13: 9.398, file_cluster_8: 9.5, file_cluster_16: 9.914
- **Magnitude:** 1431.12 | **LOC:** 306 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.4983%), Tech Debt (15.661%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 84`, `args: 11`, `func_start: 11`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 8`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 14`, `import: 26`
* *Defense:* `safety: 7`, `doc: 6`, `test: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.000137 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` .utils, sentry.pipeline.views.base, sentry.integrations.opsgenie.metrics, sentry.integrations.types, collections.abc, sentry.integrations.on_call.metrics, sentry.integrations.opsgenie.tasks, logging...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/sentry/integrations/jira_server/client.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.039 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.921 IQR)
- **Top Global Matches:** file_cluster_8: 9.039, file_cluster_13: 9.135, file_cluster_7: 9.537
- **Magnitude:** 1287.82 | **LOC:** 338 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.9276%), Tech Debt (26.3198%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 112`, `args: 34`, `func_start: 34`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 6`, `fragile_debt: 2`
* *Architecture:* `io: 1`, `api: 34`, `import: 20`
* *Defense:* `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` sentry.identity.services.identity.model, sentry.integrations.services.integration.model, sentry.integrations.types, logging, sentry.integrations.models.integration, django.urls, requests, sentry.integrations.utils.metrics...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sentry/testutils/cases.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.123 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.715 IQR)
- **Top Global Matches:** file_cluster_13: 12.123, file_cluster_8: 12.223, file_cluster_0: 12.351
- **Magnitude:** 1276.48 | **LOC:** 4265 | **CtrlFlow:** 34.4% | **Authorship Centralization:** 20.0%
- **Risk Profile:** Cognitive Load (17.1948%), Tech Debt (40.2084%)
**Top Internal Functions/Classes:**
  * `store_outcomes` (Impact: 176.7)
  * `add_2fa_users_to_org` (Impact: 112.7)
  * `span_to_trace_item` (Impact: 34.5)
  * `store_session` (Impact: 30.6)
  * `get_response` (Impact: 19.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 439`, `structural_boundaries: 839`, `args: 202`, `func_start: 202`, `class_start: 61`
* *Risk/State:* `safety_bypasses: 75`, `state_mutation: 187`, `planned_debt: 17`, `fragile_debt: 8`, `duplicate_logic: 11`
* *Architecture:* `io: 21`, `api: 296`, `concurrency: 5`, `import: 156`
* *Defense:* `safety: 134`, `doc: 58`, `test: 171`, `sync_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.936
  * `Choke Point (Betweenness):` 0.00751 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 86):` django.conf, pytest, sentry.models.apitoken, io, sentry.models.dashboard, sentry.tagstore.snuba.backend, unittest, sentry.snuba.metrics.naming_layer.public...
  * `Imported By (In-Degree: 1750):` (Excluded from Brief to save tokens)

### `src/sentry/integrations/pagerduty/integration.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.234 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.78 IQR)
- **Top Global Matches:** file_cluster_13: 9.234, file_cluster_8: 9.429, file_cluster_16: 9.486
- **Magnitude:** 1247.56 | **LOC:** 259 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.2155%), Tech Debt (18.0232%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 81`, `args: 15`, `func_start: 12`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 6`, `fragile_debt: 1`
* *Architecture:* `api: 16`, `import: 24`
* *Defense:* `safety: 3`, `doc: 6`, `test: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 3.9e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` .utils, sentry.pipeline.views.base, sentry.integrations.types, collections.abc, sentry.integrations.on_call.metrics, logging, sentry.integrations.models.integration, django.db...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tests/snuba/api/endpoints/test_organization_events.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.73 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.278 IQR)
- **Top Global Matches:** file_cluster_8: 11.73, file_cluster_16: 12.278, file_cluster_7: 12.298
- **Magnitude:** 1223.32 | **LOC:** 7447 | **CtrlFlow:** 12.1% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (2.8131%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_project_in_query_not_in_header` (Impact: 531.8)
  * `test_functions_dataset_simple` (Impact: 29.0)
  * `test_profiles_dataset_simple` (Impact: 15.2)
  * `test_sort_upsampled_columns` (Impact: 13.1)
    * *Intent:* # A: 1 sampled event with client_sample_rate=0.1 -> upsampled_count=10, raw=1 # B: 2 unsampled event...
  * `test_sample_eps_with_allowlisted_project` (Impact: 11.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 208`, `structural_boundaries: 1510`, `args: 218`, `func_start: 216`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 17`, `planned_debt: 2`, `fragile_debt: 4`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 263`, `import: 28`
* *Defense:* `safety: 1070`, `doc: 26`, `test: 1283`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.134
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` snuba_sdk.column, django.test, sentry.testutils.cases, sentry.types.group, sentry.models.group, pytest, sentry.issues.grouptype, unittest...
  * `Imported By (In-Degree: 23):` (Excluded from Brief to save tokens)

### `tests/snuba/api/endpoints/test_organization_events_span_indexed.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.189 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 2.994 IQR)
- **Top Global Matches:** file_cluster_8: 10.189, file_cluster_7: 10.927, file_cluster_16: 10.993
- **Magnitude:** 1134.62 | **LOC:** 7325 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.4798%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_trace_id_glob` (Impact: 78.4)
  * `test_pagination_samples` (Impact: 10.8)
  * `_test_simple_measurements` (Impact: 9.8)
  * `test_semver` (Impact: 8.9)
  * `test_explore_sample_query` (Impact: 7.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 1082`, `args: 176`, `func_start: 175`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 20`, `planned_debt: 5`
* *Architecture:* `io: 12`, `api: 316`, `import: 14`
* *Defense:* `safety: 830`, `doc: 14`, `test: 1026`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.032
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` urllib3, uuid, django.utils.timezone, pytest, sentry.testutils.helpers.datetime, tests.snuba.api.endpoints.test_organization_events, sentry_protos.snuba.v1.trace_item_attribute_pb2, sentry.search.events.constants...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/sentry/search/eap/spans/attributes.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.824 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.291 IQR)
- **Top Global Matches:** file_cluster_8: 7.824, file_cluster_7: 8.879, file_cluster_13: 9.023
- **Magnitude:** 1075.93 | **LOC:** 709 | **CtrlFlow:** 45.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (6.5231%), Tech Debt (9.9982%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 44`, `args: 4`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 9`, `planned_debt: 3`
* *Architecture:* `io: 4`, `api: 3`, `import: 15`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.078
  * `Choke Point (Betweenness):` 4.7e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` sentry.search.utils, typing, os, logging, sentry.search.eap.columns, sentry.utils, sentry_protos.snuba.v1.trace_item_attribute_pb2, sentry.search.eap.spans.sentry_conventions...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `tests/snuba/api/endpoints/test_organization_events_stats.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.554 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.974 IQR)
- **Top Global Matches:** file_cluster_8: 11.554, file_cluster_17: 12.015, file_cluster_0: 12.074
- **Magnitude:** 1075.46 | **LOC:** 3978 | **CtrlFlow:** 29.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (3.4547%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_functions_dataset_simple` (Impact: 18.9)
  * `test_functions_dataset_simple` (Impact: 16.4)
  * `test_top_events_with_issue` (Impact: 16.1)
  * `test_top_events_with_issue` (Impact: 16.0)
  * `test_top_events_with_multiple_yaxis` (Impact: 16.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 273`, `structural_boundaries: 641`, `args: 117`, `func_start: 116`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 55`, `fragile_debt: 2`, `duplicate_logic: 31`, `orphaned_logic: 84`
* *Architecture:* `api: 123`, `import: 22`
* *Defense:* `safety: 424`, `doc: 16`, `test: 568`, `sync_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` snuba_sdk.column, sentry.testutils.cases, pytest, sentry.issues.grouptype, unittest, uuid, sentry.utils.samples, django.urls...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/sentry/integrations/slack/integration.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.615 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.358 IQR)
- **Top Global Matches:** file_cluster_8: 9.615, file_cluster_13: 9.827, file_cluster_16: 9.908
- **Magnitude:** 1054.7 | **LOC:** 406 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (3.5012%), Tech Debt (13.274%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 97`, `args: 18`, `func_start: 18`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `fragile_debt: 1`
* *Architecture:* `api: 16`, `import: 26`
* *Defense:* `safety: 22`, `doc: 16`, `test: 2`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.000469 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` slack_sdk.errors, sentry.identity.pipeline, sentry.pipeline.views.base, sentry.pipeline.views.nested, sentry.integrations.slack.tasks.link_slack_user_identities, sentry.integrations.types, sentry.integrations.mixins, slack_sdk...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `tests/sentry/dashboards/endpoints/test_organization_dashboard_details.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.148 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.671 IQR)
- **Top Global Matches:** file_cluster_8: 11.148, file_cluster_16: 11.674, file_cluster_7: 11.841
- **Magnitude:** 1045.3 | **LOC:** 4874 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.9372%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_does_not_update_non_table_dashboard` (Impact: 16.9)
  * `test_update_widget_with_field_links` (Impact: 14.4)
  * `test_deletes_widget_with_field_links` (Impact: 13.7)
  * `test_does_not_update_if_linked_dashboard` (Impact: 13.5)
  * `test_ondemand_updates_existing_widget` (Impact: 13.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 807`, `args: 187`, `func_start: 187`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 50`, `state_mutation: 35`, `duplicate_logic: 34`, `orphaned_logic: 147`
* *Architecture:* `api: 196`, `import: 22`
* *Defense:* `safety: 524`, `doc: 2`, `test: 706`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` sentry.dashboards.endpoints.organization_dashboards, sentry.testutils.cases, sentry.snuba.metrics.extraction, pytest, sentry.models.dashboard, sentry.models.organizationmember, unittest, sentry.discover.models...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/sentry/utils/snuba.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.872 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.04 IQR)
- **Top Global Matches:** file_cluster_13: 11.872, file_cluster_8: 11.902, file_cluster_16: 12.097
- **Magnitude:** 998.14 | **LOC:** 2261 | **CtrlFlow:** 57.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (21.2149%), Tech Debt (13.1486%)
**Top Internal Functions/Classes:**
  * `get_snuba_column_name` (Impact: 469.6)
    * *Intent:* # Our calls to snuba frequently fail due to network issues. We want to # automatically retry most re...
  * `resolve_condition` (Impact: 260.6)
  * `options_override` (Impact: 13.1)
  * `_passthrough_arg` (Impact: 7.3)
    * *Intent:* # Special case, if there is only one aggregate, just return the raw value
  * `log_snuba_info` (Impact: 7.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 410`, `structural_boundaries: 305`, `args: 83`, `func_start: 69`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 120`, `dead_code: 1`, `planned_debt: 12`, `fragile_debt: 2`
* *Architecture:* `io: 7`, `api: 75`, `import: 45`
* *Defense:* `safety: 61`, `doc: 78`, `test: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.705
  * `Choke Point (Betweenness):` 0.000485 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` os, urllib3, django.conf, sentry.models.group, sentry.utils.concurrent, copy, sqlparse, sentry.utils...
  * `Imported By (In-Degree: 131):` (Excluded from Brief to save tokens)

### `src/sentry/integrations/bitbucket/integration.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.94 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.073 IQR)
- **Top Global Matches:** file_cluster_8: 8.94, file_cluster_13: 8.955, file_cluster_16: 9.269
- **Magnitude:** 968.42 | **LOC:** 305 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (3.8838%), Tech Debt (15.8869%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 102`, `args: 16`, `func_start: 16`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 5`, `fragile_debt: 1`
* *Architecture:* `api: 19`, `import: 29`
* *Defense:* `safety: 4`, `doc: 14`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.05
  * `Choke Point (Betweenness):` 0.000124 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` .utils, sentry.identity.pipeline, sentry.pipeline.views.base, sentry.models.apitoken, sentry.pipeline.views.nested, sentry.integrations.types, collections.abc, sentry.integrations.models.integration...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/sentry/api/event_search.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.327 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.729 IQR)
- **Top Global Matches:** file_cluster_16: 11.327, file_cluster_8: 11.576, file_cluster_13: 11.653
- **Magnitude:** 908.9 | **LOC:** 1956 | **CtrlFlow:** 44.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.5885%), Tech Debt (9.9032%)
**Top Internal Functions/Classes:**
  * `translate_wildcard` (Impact: 675.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 294`, `structural_boundaries: 370`, `args: 128`, `func_start: 128`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 78`, `dead_code: 1`, `planned_debt: 4`, `fragile_debt: 1`
* *Architecture:* `api: 128`, `import: 21`
* *Defense:* `safety: 67`, `doc: 14`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.312
  * `Choke Point (Betweenness):` 0.000136 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` sentry.search.utils, sentry.exceptions, collections.abc, sentry.search.events.constants, datetime, sentry.search.events.types, parsimonious.nodes, sentry.snuba.dataset...
  * `Imported By (In-Degree: 60):` (Excluded from Brief to save tokens)

### `tests/sentry/issues/endpoints/test_organization_group_index.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.24 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.001 IQR)
- **Top Global Matches:** file_cluster_8: 12.24, file_cluster_13: 12.636, file_cluster_16: 12.683
- **Magnitude:** 890.82 | **LOC:** 4525 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (2.9733%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_assigned_or_suggested_search` (Impact: 59.9)
  * `test_query_status_and_substatus_nonoverl` (Impact: 21.5)
  * `test_resolve_with_integration` (Impact: 19.3)
  * `test_bulk_delete_for_many_projects_witho` (Impact: 17.2)
  * `test_query_status_and_substatus_overlapp` (Impact: 16.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 1123`, `args: 145`, `func_start: 145`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 40`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 2`, `duplicate_logic: 7`, `orphaned_logic: 119`
* *Architecture:* `api: 146`, `import: 61`
* *Defense:* `safety: 789`, `doc: 20`, `test: 949`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 46):` sentry.testutils.silo, sentry.models.groupinbox, sentry.testutils.helpers.features, sentry.sentry_apps.models.platformexternalissue, sentry.testutils.cases, sentry.types.group, sentry.models.group, tests.sentry.feedback...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/sentry/testutils/factories.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.244 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.01 IQR)
- **Top Global Matches:** file_cluster_0: 11.244, file_cluster_13: 11.291, file_cluster_8: 11.429
- **Magnitude:** 874.44 | **LOC:** 2808 | **CtrlFlow:** 32.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (41.5221%), Tech Debt (8.3213%)
**Top Internal Functions/Classes:**
  * `create_slack_project_rule` (Impact: 235.9)
  * `create_organization` (Impact: 31.2)
  * `create_member` (Impact: 19.4)
  * `_patch_artifact_manifest` (Impact: 17.7)
  * `create_team_membership` (Impact: 9.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 311`, `structural_boundaries: 643`, `args: 136`, `func_start: 136`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 85`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 14`, `api: 206`, `import: 155`
* *Defense:* `safety: 20`, `doc: 6`, `test: 16`, `sync_locks: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.715
  * `Choke Point (Betweenness):` 0.005358 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 120):` os, sentry.models.authidentity, django.conf, sentry.sentry_apps.token_exchange.grant_exchanger, sentry.models.apitoken, sentry.integrations.models.repository_project_path_config, sentry.types.token, sentry.models.orgauthtoken...
  * `Imported By (In-Degree: 73):` (Excluded from Brief to save tokens)

### `src/sentry/search/events/builder/metrics.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.11 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.544 IQR)
- **Top Global Matches:** file_cluster_13: 12.11, file_cluster_8: 12.234, file_cluster_16: 12.245
- **Magnitude:** 868.8 | **LOC:** 1920 | **CtrlFlow:** 62.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.6754%), Tech Debt (97.4953%)
**Top Internal Functions/Classes:**
  * `default_filter_converter` (Impact: 57.3)
  * `_create_query_framework` (Impact: 38.8)
  * `is_spans_metrics_query` (Impact: 32.7)
    * *Intent:* """This property is used to determine if a query is using at least one of the fields in the spans na...
  * `_environment_filter_converter` (Impact: 27.4)
  * `resolve_column_name` (Impact: 22.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 452`, `structural_boundaries: 273`, `args: 62`, `func_start: 62`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 78`, `state_mutation: 261`, `dead_code: 5`, `planned_debt: 6`, `duplicate_logic: 23`
* *Architecture:* `api: 56`, `import: 37`
* *Defense:* `safety: 37`, `doc: 47`, `test: 1`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.039
  * `Choke Point (Betweenness):` 0.000142 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` sentry.search.events.builder.utils, sentry.search.events.filter, sentry.search.utils, sentry.snuba.metrics.extraction, sentry.exceptions, collections.abc, sentry.snuba.metrics.query, sentry.sentry_metrics.use_case_id_registry...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tests/sentry/users/api/endpoints/test_user_identity_config.py` (PYTHON) | Magnitude: 117.64 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 301, structural_boundaries: 130, test: 90, safety: 63
- `tests/sentry/integrations/discord/test_utils.py` (PYTHON) | Magnitude: 94.8 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 97, structural_boundaries: 52, test: 39, test_skip: 27
- `tests/sentry/sentry_apps/api/endpoints/test_sentry_app_webhook_requests.py` (PYTHON) | Magnitude: 90.36 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 359, structural_boundaries: 102, test: 82, safety: 65
- `tests/sentry/preprod/api/endpoints/pull_request/test_organization_pullrequest_details.py` (PYTHON) | Magnitude: 49.52 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 212, structural_boundaries: 66, test: 63, safety: 41
- `static/app/views/integrationPipeline/components/footerWithButtons.tsx` (TYPESCRIPT) | Magnitude: 0.44 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 41, structural_boundaries: 13, branch: 7, args: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `src/sentry/hybridcloud/outbox/signals.py` (PYTHON) | Magnitude: 11.56 | Delta: **0.187 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: events: 3, structural_boundaries: 2, import: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `static/app/components/autoComplete.tsx` (TYPESCRIPT) | Magnitude: 69.4 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 303, state_mutation: 207, structural_boundaries: 91, branch: 82
- `static/app/plugins/pluginComponentBase.tsx` (TYPESCRIPT) | Magnitude: 13.56 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 116, state_mutation: 72, args: 27, structural_boundaries: 24
- `static/app/components/events/meta/metaProxy.tsx` (TYPESCRIPT) | Magnitude: 3.86 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 17, branch: 11, state_mutation: 7
- `static/app/components/deprecatedAsyncComponent.tsx` (TYPESCRIPT) | Magnitude: 14.65 | Delta: **0.06 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 147, state_mutation: 80, structural_boundaries: 45, branch: 38
- `src/sentry/templates/sentry/error-page-embed.js` (JAVASCRIPT) | Magnitude: 284.9 | Delta: **0.066 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 178, state_mutation: 151, structural_boundaries: 39, branch: 33

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/sudo/settings.py` (PYTHON) | Magnitude: 15.24 | Delta: **0.071 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: safety: 11, reflection_metaprogramming: 11, structural_boundaries: 2, doc: 2
- `config/hooks/post-merge` (SHELL) | Magnitude: 40.74 | Delta: **0.094 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: branch: 18, state_mutation: 17, indent_spaces: 17, reflection_metaprogramming: 14
- `scripts/upgrade-postgres.sh` (SHELL) | Magnitude: 5.92 | Delta: **0.305 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: reflection_metaprogramming: 41, state_mutation: 28, branch: 22, debug_prints: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/sentry/uptime/eap_utils.py` (PYTHON) | Magnitude: 8.16 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 7, generics: 4, api: 3
- `fixtures/stubs-for-mypy/pytest_rerunfailures.pyi` (PYTHON) | Magnitude: 0.02 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 2, test: 2, args: 1, func_start: 1
- `src/sentry/api/endpoints/organization_stats_v2.py` (PYTHON) | Magnitude: 50.0 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 176, structural_boundaries: 74, branch: 46, import: 27
- `src/sentry/db/pending_deletion.py` (PYTHON) | Magnitude: 25.38 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 75, structural_boundaries: 29, generics: 9, encapsulation: 9
- `src/sentry/sentry_metrics/aggregation_option_registry.py` (PYTHON) | Magnitude: 13.1 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 14, api: 4, import: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/sentry/ingest/transaction_clusterer/base.py` (PYTHON) | Magnitude: 9.02 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 9, doc: 6, indent_spaces: 6, api: 5
- `tests/sentry/sentry_apps/api/parsers/test_markdown.py` (PYTHON) | Magnitude: 12.94 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 16, indent_spaces: 15, test: 6, api: 5
- `tests/sentry/uptime/endpoints/__init__.py` (PYTHON) | Magnitude: 4.0 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 3, api: 2, args: 1
- `src/sentry/auth/manager.py` (PYTHON) | Magnitude: 28.68 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 26, indent_spaces: 22, api: 11, encapsulation: 11
- `tests/sentry/integrations/github_copilot/test_client.py` (PYTHON) | Magnitude: 64.0 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 181, test: 80, structural_boundaries: 71, safety: 35

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `static/app/views/insights/sessions/queries/useReleaseSessionPercentage.tsx` (TYPESCRIPT) | Magnitude: 1.15 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 104, structural_boundaries: 23, branch: 19, immutability_locks: 15
- `static/app/types/utils.tsx` (TYPESCRIPT) | Magnitude: 1.46 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 9, safety: 8, generics: 7
- `static/app/views/explore/hooks/useGetSavedQueries.tsx` (TYPESCRIPT) | Magnitude: 12.98 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 225, structural_boundaries: 64, branch: 52, state_mutation: 43
- `static/app/views/insights/common/components/chart.tsx` (TYPESCRIPT) | Magnitude: 25.35 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 533, branch: 156, structural_boundaries: 120, safety: 51
- `static/app/views/onboarding/components/useScmProviders.ts` (TYPESCRIPT) | Magnitude: 2.67 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 17, branch: 10, args: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `static/app/utils/useDispatchingReducer.tsx` (TYPESCRIPT) | Magnitude: 7.59 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 78, generics: 38, state_mutation: 33, structural_boundaries: 29
- `static/app/views/alerts/rules/uptime/detailsTimelineLegend.tsx` (TYPESCRIPT) | Magnitude: 0.41 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 87, ui_framework: 21, generics: 17, structural_boundaries: 11
- `static/app/views/detectors/components/detectorListTable/detectorListRow.tsx` (TYPESCRIPT) | Magnitude: 1.59 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 90, ui_framework: 34, generics: 33, structural_boundaries: 30
- `static/app/components/deprecatedDropdownMenu.tsx` (TYPESCRIPT) | Magnitude: 16.5 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 278, structural_boundaries: 95, branch: 69, args: 68
- `static/app/views/navigation/useResetActiveNavigationGroup.tsx` (TYPESCRIPT) | Magnitude: 6.09 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 55, structural_boundaries: 21, args: 15, ui_framework: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `static/app/utils/profiling/canvasScheduler.tsx` (TYPESCRIPT) | Magnitude: 22.84 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 148, state_mutation: 102, structural_boundaries: 53, args: 41
- `.github/workflows/scripts/wait-for-merge-commit.js` (JAVASCRIPT) | Magnitude: 24.06 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 42, branch: 10, concurrency: 10, state_mutation: 9
- `static/app/views/settings/organizationIntegrations/installedPlugin.tsx` (TYPESCRIPT) | Magnitude: 18.32 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 151, concurrency: 54, structural_boundaries: 42, state_mutation: 34
- `static/gsApp/stores/subscriptionStore.tsx` (TYPESCRIPT) | Magnitude: 13.03 | Delta: **0.041 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 76, state_mutation: 72, structural_boundaries: 24, concurrency: 18
- `static/app/components/replays/deserializeCanvasArgs.ts` (TYPESCRIPT) | Magnitude: 2.83 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 24, branch: 15, state_mutation: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `src/sentry/scripts/ratelimits/api_limiter.lua` (LUA) | Magnitude: 23.2 | Delta: **0.207 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 16, structural_boundaries: 11, encapsulation: 9, explicit_casts: 3
- `static/app/components/searchQueryBuilder/askSeer/askSeerConsentOption.tsx` (TYPESCRIPT) | Magnitude: 1.15 | Delta: **0.293 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 1, api: 1, planned_debt: 1, immutability_locks: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/sentry/utils/locking/__init__.py` (PYTHON) | Magnitude: 11.52 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 2, structural_boundaries: 1, class_start: 1, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/sentry/identity/manager.py` (PYTHON) | Magnitude: 43.48 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 17, api: 14, encapsulation: 13
- `src/sentry/integrations/slack/unfurl/discover.py` (PYTHON) | Magnitude: 53.08 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 217, structural_boundaries: 77, branch: 71, import: 28
- `src/sentry/notifications/notifications/activity/__init__.py` (PYTHON) | Magnitude: 15.46 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 23, import: 11, indent_spaces: 9, generics: 1
- `tests/sentry/integrations/services/test_assignment_source.py` (PYTHON) | Magnitude: 13.88 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 19, test: 15, safety: 8
- `tests/sentry/workflow_engine/migration_helpers/test_issue_alert_dual_write.py` (PYTHON) | Magnitude: 96.86 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 311, structural_boundaries: 105, test: 58, safety: 43

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/sentry/db/postgres/helpers.py` (PYTHON) | Magnitude: 11.74 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 8, branch: 4, dead_code: 4
- `static/app/utils/react/isHydrationError.tsx` (TYPESCRIPT) | Magnitude: 0.54 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 2, structural_boundaries: 2, indent_spaces: 2, args: 1
- `static/app/utils/oxfordizeArray.tsx` (TYPESCRIPT) | Magnitude: 3.14 | Delta: **0.083 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 3, structural_boundaries: 2, branch: 1, args: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `static/app/views/dashboards/createFromSeer.tsx` -> Churn: **73.51%** | Cog Load: 28.8982% | Debt: 99.191%
- `static/app/views/dashboards/detail.tsx` -> Churn: **68.88%** | Cog Load: 77.3933% | Debt: 61.164%
- `static/app/views/dashboards/manage/index.tsx` -> Churn: **68.88%** | Cog Load: 13.7846% | Debt: 99.6115%
- `static/app/components/events/autofix/v3/nextStep.tsx` -> Churn: **65.24%** | Cog Load: 9.2004% | Debt: 93.0305%
- `static/app/views/preprod/snapshots/snapshots.tsx` -> Churn: **65.24%** | Cog Load: 30.6171% | Debt: 81.5263%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/sentry/integrations/jira/integration.py` -> **Lyn Nagara** (100.0% isolated ownership) | Magnitude: 12929.36
- `src/sentry/integrations/bitbucket_server/integration.py` -> **Jay** (100.0% isolated ownership) | Magnitude: 1455.4
- `src/sentry/integrations/discord/integration.py` -> **Christinarlong** (100.0% isolated ownership) | Magnitude: 1442.52
- `src/sentry/integrations/bitbucket/integration.py` -> **Jay** (100.0% isolated ownership) | Magnitude: 968.42
- `src/sentry/testutils/factories.py` -> **Lyn Nagara** (100.0% isolated ownership) | Magnitude: 874.44

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/sentry/models/project.py` -> **Severity: 0.818** (Bridge: 0.0174 * Flux: 47.0159%)
- `src/sentry/utils/http.py` -> **Severity: 0.679** (Bridge: 0.0119 * Flux: 57.2909%)
- `src/sentry/users/models/user.py` -> **Severity: 0.537** (Bridge: 0.0061 * Flux: 87.8364%)
- `src/sentry/models/activity.py` -> **Severity: 0.361** (Bridge: 0.0038 * Flux: 95.9865%)
- `src/sentry/testutils/cases.py` -> **Severity: 0.353** (Bridge: 0.0075 * Flux: 47.0652%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/sentry/types/group.py` -> **Severity: 3488.941** (Blast Radius: 50.095 * Doc Risk: 69.6465%)
- `static/app/components/events/contexts/platformContext/react.tsx` -> **Severity: 2922.476** (Blast Radius: 48.212 * Doc Risk: 60.6172%)
- `src/sentry/metrics/logging.py` -> **Severity: 2016.958** (Blast Radius: 21.304 * Doc Risk: 94.6751%)
- `src/sentry/testutils/helpers/datetime.py` -> **Severity: 1537.112** (Blast Radius: 15.385 * Doc Risk: 99.9098%)
- `src/sentry/utils/db.py` -> **Severity: 1438.846** (Blast Radius: 15.58 * Doc Risk: 92.3521%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
