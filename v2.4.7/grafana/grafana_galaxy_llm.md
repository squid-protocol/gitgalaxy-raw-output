# ARCHITECTURAL_BRIEF: grafana
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_web/grafana` |
| **Timestamp** | `2026-08-07T04:25:30.335173+00:00` |
| **Scan Duration** | `54.62s` |
| **Git Branch** | `main` |
| **Git Commit** | `d9c23be0842c8ffd27e9dd7e7b6c78f0ea2a916b` |
| **Git Remote** | `https://github.com/grafana/grafana.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 10567 malicious artifacts.

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
| Total Artifacts | 21474 |
| Analyzed Artifacts (Scanned) | 13842 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 7632 |
| Total LOC | 1272386 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 64.5% |
| Dominant Lang | GO |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1508 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 559 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 6618 | 673417 | 47.8% |
| GO | 2968 | 357353 | 21.4% |
| XML | 1702 | 335 | 12.3% |
| JSON | 886 | 205224 | 6.4% |
| SQLITE | 737 | 10399 | 5.3% |
| MARKDOWN | 332 | 0 | 2.4% |
| YAML | 185 | 6411 | 1.3% |
| PLAINTEXT | 117 | 17 | 0.8% |
| JAVASCRIPT | 103 | 5614 | 0.7% |
| SHELL | 72 | 2519 | 0.5% |
| MAKEFILE | 30 | 922 | 0.2% |
| CSV | 26 | 828 | 0.2% |
| DOCKERFILE | 25 | 364 | 0.2% |
| HTML | 18 | 4086 | 0.1% |
| PROTO | 12 | 866 | 0.1% |
| CSS | 8 | 4002 | 0.1% |
| POWERSHELL | 1 | 8 | 0.0% |
| RUBY | 1 | 19 | 0.0% |
| ASSEMBLY | 1 | 2 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.377`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 8307 | 60.0% |
| file_cluster_13 | 3495 | 25.2% |
| file_cluster_0 | 322 | 2.3% |
| file_cluster_4 | 245 | 1.8% |
| file_cluster_17 | 245 | 1.8% |
| file_cluster_2 | 229 | 1.7% |
| file_cluster_16 | 132 | 1.0% |
| file_cluster_11 | 64 | 0.5% |
| file_cluster_9 | 54 | 0.4% |
| file_cluster_15 | 16 | 0.1% |
| Unknown | 14 | 0.1% |
| file_cluster_12 | 13 | 0.1% |
| file_cluster_6 | 11 | 0.1% |
| file_cluster_7 | 8 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 434 | 3.1% |
| Static: Minified & Vendor Opaque Mass | 253 | 1.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 7632*

**Composition by Extension & Reason:**
- `.go`: 2819x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 9x Excluded (Saturation: Line 23 exceeds 500 chars), 5x Excluded (Machine-Generated Source Code Signature: 11 LOC)
- `.ts`: 1080x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 18 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 1769 LOC)
- `.tsx`: 994x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 296 LOC), 1x Excluded (Machine-Generated Source Code Signature: 75 LOC)
- `.md`: 754x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 4664 LOC), 1x Excluded (Machine-Generated Source Code Signature: 121 LOC)
- `.json`: 208x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 10x Excluded (Massive Static Asset Blob: 16576 LOC), 5x Excluded (Massive Static Asset Blob: 16488 LOC)
- `.cue`: 157x Excluded (Unsupported Extension: '.cue'), 32x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 13x Unsupported Format (.cue)
- `.jsonc`: 10x Excluded (Machine-Generated Source Code Signature: 76 LOC), 8x Excluded (Saturation: Line 50 exceeds 500 chars), 8x Excluded (Machine-Generated Source Code Signature: 113 LOC)
- `no_extension`: 132x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 15x Unsupported Format (.undeterminable)
- `.yml`: 110x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 1979 LOC)
- `.png`: 97x Excluded (Explicitly Denied Extension: '.png')
- `.yaml`: 84x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 83x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 20 LOC)
- `.snap`: 39x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 22x Unsupported Format (.snap), 1x Excluded (Monolithic Amalgamation: 36396 LOC exceeds safe regex boundaries)
- `.js`: 50x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 16 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 32 LOC)
- `.sum`: 35x Excluded (Unsupported Extension: '.sum'), 9x Unsupported Format (.sum), 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 17.9 | 7.1 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 28.3 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 22.8 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 8.6 | 2.3 | 0.0 |
| API Exposure | 0.0 | 19.6 | 4.2 | 4.2 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 8.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 24.5 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 81.4 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.1 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 6.8 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 39.4 | 30.4 | 6.2 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `packages/grafana-runtime/src/services/pluginMeta/test-fixtures/v0alpha1Response.ts` (Hits: 369)
- `packages/grafana-flamegraph/src/FlameGraph/testData/dataNestedSet.ts` (Hits: 257)
- `public/app/features/provisioning/utils/treeUtils.test.ts` (Hits: 163)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **react.svg** (`public/img/icons/unicons/react.svg`) — 2648 inbound connections
2. **i18n.tsx** (`packages/grafana-i18n/src/i18n.tsx`) — 1867 inbound connections
3. **log.go** (`pkg/apimachinery/errutil/log.go`) — 566 inbound connections
4. **setting.svg** (`public/img/icons/unicons/setting.svg`) — 391 inbound connections
5. **ThemeContext.tsx** (`packages/grafana-ui/src/themes/ThemeContext.tsx`) — 249 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **dialect_postgres.go** (`pkg/util/xorm/dialect_postgres.go`) — 754 outbound dependencies
2. **index.ts** (`packages/grafana-ui/src/index.ts`) — 267 outbound dependencies
3. **wire.go** (`pkg/server/wire.go`) — 202 outbound dependencies
4. **index.ts** (`packages/grafana-data/src/index.ts`) — 172 outbound dependencies
5. **dialect_mysql.go** (`pkg/util/xorm/dialect_mysql.go`) — 156 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `getStatementPosition` (@ `public/app/plugins/datasource/cloudwatch/language/cloudwatch-logs-sql/completion/statementPosition.ts`) -> Impact: **605.1** | LOC: 344
- `updateSchema` (@ `public/app/features/dashboard/state/DashboardMigrator.ts`) -> Impact: **562.8** | LOC: 933
  * *Intent:* /** * The current version of the dashboard schema. * * NOTE: Schema version 42 is the FINAL version for the v1 dashboard API. * DO NOT increment this ...
- `NewTestSqlKvBackend` (@ `pkg/storage/unified/testing/storage_backend_sql_compatibility.go`) -> Impact: **473.5** | LOC: 1510
- `prepConfig` (@ `public/app/plugins/panel/heatmap/utils.ts`) -> Impact: **349.9** | LOC: 478
- `jsonDataToMetaJSONData` (@ `apps/plugins/pkg/app/meta/converter.go`) -> Impact: **349.6** | LOC: 511
  * *Intent:* // jsonDataToMetaJSONData converts a plugins.JSONData to a pluginsv0alpha1.MetaJSONData. // nolint:gocyclo
- `convertToRowsLayout` (@ `public/app/features/dashboard/api/ResponseTransformers.ts`) -> Impact: **343.7** | LOC: 312
- `cleanupK8sDashboardResources` (@ `pkg/services/dashboards/service/dashboard_service.go`) -> Impact: **325.6** | LOC: 1054
  * *Intent:* // cleanupK8sDashboardResources cleans up resources marked for deletion in the k8s API. // It processes all organizations, finds dashboards with the t...
- `cleanupOrganizationK8sDashboards` (@ `pkg/services/dashboards/service/dashboard_service.go`) -> Impact: **319.1** | LOC: 1037
- `Generate` (@ `pkg/services/ngalert/models/testing.go`) -> Impact: **290.5** | LOC: 1248
- `getStatementPosition` (@ `public/app/plugins/datasource/cloudwatch/language/cloudwatch-sql/completion/statementPosition.ts`) -> Impact: **285.3** | LOC: 122
  * *Intent:* // about getStatementPosition: public/app/plugins/datasource/cloudwatch/language/cloudwatch-ppl/completion/statementPosition.ts

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `pkg/api` | 50 | 11834.24 | 39.03% | 26.03% |
| `pkg/util/xorm` | 41 | 11759.0 | 51.28% | 37.4% |
| `public/img/icons/unicons` | 1231 | 11363.34 | 4.32% | 0.0% |
| `pkg/storage/unified/resource` | 42 | 10435.16 | 32.76% | 33.84% |
| `devenv/docker/blocks/auth/authentik` | 4 | 10019.26 | 0.0% | 0.0% |
| `pkg/services/ldap/testdata` | 2 | 10000.0 | 0.0% | 0.0% |
| `pkg/services/ngalert/api` | 39 | 6989.96 | 29.33% | 51.36% |
| `apps/dashboard/pkg/migration/conversion` | 22 | 5672.7 | 44.5% | 43.87% |
| `devenv/docker/blocks/slow_proxy` | 4 | 5066.16 | 10.19% | 0.0% |
| `devenv/docker/blocks/postgres_tests` | 4 | 5035.34 | 3.75% | 25.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `.github/workflows/scripts/create-security-branch/create-security-branch.sh` -> **100.0%** Exposure
- `.github/workflows/scripts/validate-commit-in-head.sh` -> **100.0%** Exposure
- `devenv/docker/blocks/collectd/start_container` -> **100.0%** Exposure
- `devenv/docker/blocks/influxdb/setup_influxql.sh` -> **100.0%** Exposure
- `devenv/docker/blocks/smtp/bootstrap.sh` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `.github/workflows/scripts/determine-npm-tag.sh` -> **100.0%** Exposure
- `devenv/bulk-folders/bulk-folders.sh` -> **100.0%** Exposure
- `devenv/create_docker_compose.sh` -> **100.0%** Exposure
- `devenv/docker/blocks/smtp/bootstrap.sh` -> **100.0%** Exposure
- `devenv/frontend-service/local-init.sh` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/grafana-api-clients/src/clients/rtkq/legacy/endpoints.gen.ts` -> **0** Orphaned Functions | **281** Duplicates
- `public/app/features/alerting/unified/rule-list/hooks/grafanaFilter.test.ts` -> **0** Orphaned Functions | **207** Duplicates
- `packages/grafana-prometheus/src/datasource.test.ts` -> **2** Orphaned Functions | **172** Duplicates
- `packages/grafana-runtime/src/services/pluginMeta/panels.test.ts` -> **0** Orphaned Functions | **120** Duplicates
- `packages/grafana-ui/src/components/Table/TableNG/utils.test.ts` -> **0** Orphaned Functions | **110** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`public/app/features/canvas/runtime/element.tsx`** -> AI Confidence: **99.48%**
2. **`Dockerfile`** -> AI Confidence: **99.48%**
3. **`apps/plugins/pkg/app/meta/converter.go`** -> AI Confidence: **99.48%**
4. **`pkg/expr/classic/reduce.go`** -> AI Confidence: **99.48%**
5. **`pkg/middleware/middleware.go`** -> AI Confidence: **99.48%**
6. **`pkg/middleware/request_metrics.go`** -> AI Confidence: **99.48%**
7. **`pkg/registry/apis/dashboard/snapshot/conversions.go`** -> AI Confidence: **99.48%**
8. **`pkg/services/apiserver/builder/openapi.go`** -> AI Confidence: **99.48%**
9. **`pkg/services/dashboards/service/search/search.go`** -> AI Confidence: **99.48%**
10. **`pkg/services/ngalert/api/authorization.go`** -> AI Confidence: **99.48%**
11. **`pkg/services/ngalert/api/compat_contact_points.go`** -> AI Confidence: **99.48%**
12. **`pkg/services/store/kind/dashboard/dashboard.go`** -> AI Confidence: **99.48%**
13. **`pkg/setting/setting_feature_toggles.go`** -> AI Confidence: **99.48%**
14. **`pkg/tests/testinfra/testinfra.go`** -> AI Confidence: **99.48%**
15. **`pkg/tsdb/cloudwatch/get_dimension_values_for_wildcards.go`** -> AI Confidence: **99.48%**
16. **`pkg/tsdb/cloudwatch/log_query.go`** -> AI Confidence: **99.48%**
17. **`pkg/tsdb/cloudwatch/response_parser.go`** -> AI Confidence: **99.48%**
18. **`pkg/tsdb/influxdb/influxql/buffered/response_parser.go`** -> AI Confidence: **99.48%**
19. **`pkg/tsdb/jaeger/utils/grpc_utils.go`** -> AI Confidence: **99.48%**
20. **`pkg/util/proxyutil/proxyutil.go`** -> AI Confidence: **99.48%**
21. **`pkg/util/xorm/engine_cond.go`** -> AI Confidence: **99.48%**
22. **`pkg/services/ngalert/state/state.go`** -> AI Confidence: **99.44%**
23. **`public/app/features/alerting/unified/rule-list/hooks/grafanaFilter.ts`** -> AI Confidence: **99.39%**
24. **`public/app/features/canvas/elements/cloud.tsx`** -> AI Confidence: **99.39%**
25. **`public/app/features/canvas/elements/ellipse.tsx`** -> AI Confidence: **99.39%**
26. **`public/app/features/canvas/elements/parallelogram.tsx`** -> AI Confidence: **99.39%**
27. **`public/app/features/canvas/elements/triangle.tsx`** -> AI Confidence: **99.39%**
28. **`public/app/features/dashboard-scene/panel-edit/PanelEditNext/QueryEditor/Body/QueryEditorDetailsSidebar.tsx`** -> AI Confidence: **99.39%**
29. **`public/app/features/provisioning/Job/JobContent.tsx`** -> AI Confidence: **99.39%**
30. **`public/app/plugins/panel/canvas/components/connections/Connections.tsx`** -> AI Confidence: **99.39%**
31. **`public/app/plugins/panel/canvas/components/connections/Connections2.tsx`** -> AI Confidence: **99.39%**
32. **`public/app/plugins/panel/timeseries/migrations.ts`** -> AI Confidence: **99.39%**
33. **`public/app/plugins/panel/timeseries/plugins/AnnotationsPlugin2Cluster.tsx`** -> AI Confidence: **99.39%**
34. **`apps/dashboard/pkg/apis/dashboard/v2/validation.go`** -> AI Confidence: **99.39%**
35. **`apps/dashboard/pkg/apis/dashboard/v2alpha1/validation.go`** -> AI Confidence: **99.39%**
36. **`apps/dashboard/pkg/apis/dashboard/v2beta1/validation.go`** -> AI Confidence: **99.39%**
37. **`pkg/apiserver/storage/testing/store_tests.go`** -> AI Confidence: **99.39%**
38. **`pkg/expr/mathexp/exp.go`** -> AI Confidence: **99.39%**
39. **`pkg/registry/apis/iam/user/legacy_search.go`** -> AI Confidence: **99.39%**
40. **`pkg/registry/apis/provisioning/jobs/sync/changes.go`** -> AI Confidence: **99.39%**
41. **`pkg/registry/apis/secret/validator/secure_value.go`** -> AI Confidence: **99.39%**
42. **`pkg/registry/apps/alerting/notifications/routingtree/conversions.go`** -> AI Confidence: **99.39%**
43. **`pkg/registry/apps/annotation/search_handler.go`** -> AI Confidence: **99.39%**
44. **`pkg/services/apiserver/builder/request_handler.go`** -> AI Confidence: **99.39%**
45. **`pkg/services/authn/authnimpl/registration.go`** -> AI Confidence: **99.39%**
46. **`pkg/services/authz/zanzana/server/openfga_server.go`** -> AI Confidence: **99.39%**
47. **`pkg/services/cleanup/cleanup.go`** -> AI Confidence: **99.39%**
48. **`pkg/services/libraryelements/writers.go`** -> AI Confidence: **99.39%**
49. **`pkg/services/live/remotewrite/remotewrite.go`** -> AI Confidence: **99.39%**
50. **`pkg/services/navtree/navtreeimpl/admin.go`** -> AI Confidence: **99.39%**
51. **`pkg/services/navtree/navtreeimpl/applinks.go`** -> AI Confidence: **99.39%**
52. **`pkg/services/navtree/navtreeimpl/navtree.go`** -> AI Confidence: **99.39%**
53. **`pkg/services/pluginsintegration/pluginconfig/request.go`** -> AI Confidence: **99.39%**
54. **`pkg/services/preference/prefapi/api.go`** -> AI Confidence: **99.39%**
55. **`pkg/services/sqlstore/migrations/accesscontrol/managed_permission_migrator.go`** -> AI Confidence: **99.39%**
56. **`pkg/services/sqlstore/permissions/dashboard.go`** -> AI Confidence: **99.39%**
57. **`pkg/setting/setting_plugins.go`** -> AI Confidence: **99.39%**
58. **`pkg/setting/setting_unified_storage.go`** -> AI Confidence: **99.39%**
59. **`pkg/storage/unified/apistore/util.go`** -> AI Confidence: **99.39%**
60. **`pkg/storage/unified/testing/kv.go`** -> AI Confidence: **99.39%**
61. **`pkg/tsdb/cloudwatch/annotation_query.go`** -> AI Confidence: **99.39%**
62. **`pkg/tsdb/cloudwatch/metric_data_query_builder.go`** -> AI Confidence: **99.39%**
63. **`pkg/tsdb/grafana-testdata-datasource/csv_data.go`** -> AI Confidence: **99.39%**
64. **`pkg/util/xorm/session_convert.go`** -> AI Confidence: **99.39%**
65. **`pkg/util/xorm/session_insert.go`** -> AI Confidence: **99.39%**
66. **`pkg/util/xorm/statement.go`** -> AI Confidence: **99.39%**
67. **`scripts/openapi3/openapi3conv.go`** -> AI Confidence: **99.39%**
68. **`public/app/features/dashboard/api/ResponseTransformers.ts`** -> AI Confidence: **99.35%**
69. **`pkg/api/frontendsettings.go`** -> AI Confidence: **99.35%**
70. **`pkg/middleware/recovery.go`** -> AI Confidence: **99.35%**
71. **`pkg/registry/apis/dashboard/search.go`** -> AI Confidence: **99.35%**
72. **`pkg/registry/apps/alerting/rules/alertrule/compat.go`** -> AI Confidence: **99.35%**
73. **`pkg/services/apiserver/appinstaller/server.go`** -> AI Confidence: **99.35%**
74. **`pkg/services/apiserver/builder/helper.go`** -> AI Confidence: **99.35%**
75. **`pkg/services/ngalert/notifier/legacy_storage/routes.go`** -> AI Confidence: **99.35%**
76. **`pkg/storage/unified/testing/storage_backend_sql_compatibility.go`** -> AI Confidence: **99.35%**
77. **`pkg/tsdb/jaeger/utils/client_utils.go`** -> AI Confidence: **99.35%**
78. **`pkg/util/xorm/dialect_mysql.go`** -> AI Confidence: **99.35%**
79. **`pkg/expr/sql_schema.go`** -> AI Confidence: **99.34%**
80. **`pkg/registry/apis/provisioning/openapi_version.go`** -> AI Confidence: **99.34%**
81. **`pkg/registry/apps/annotation/memory_store.go`** -> AI Confidence: **99.34%**
82. **`pkg/services/ldap/api/support_bundle.go`** -> AI Confidence: **99.34%**
83. **`pkg/services/sqlstore/searchstore/builder.go`** -> AI Confidence: **99.34%**
84. **`pkg/services/team/search/search.go`** -> AI Confidence: **99.34%**
85. **`pkg/util/xorm/session_update.go`** -> AI Confidence: **99.34%**
86. **`public/app/features/provisioning/Wizard/hooks/useRepositoryStatus.ts`** -> AI Confidence: **99.32%**
87. **`public/app/plugins/panel/candlestick/utils.ts`** -> AI Confidence: **99.32%**
88. **`public/app/plugins/panel/piechart/migrations.ts`** -> AI Confidence: **99.32%**
89. **`pkg/services/featuremgmt/registry.go`** -> AI Confidence: **99.32%**
90. **`packages/grafana-data/src/dataframe/StreamingDataFrame.ts`** -> AI Confidence: **99.31%**
91. **`packages/grafana-data/src/field/displayProcessor.ts`** -> AI Confidence: **99.31%**
92. **`packages/grafana-data/src/field/fieldDisplay.ts`** -> AI Confidence: **99.31%**
93. **`packages/grafana-data/src/field/fieldOverrides.ts`** -> AI Confidence: **99.31%**
94. **`packages/grafana-data/src/panel/getPanelOptionsWithDefaults.ts`** -> AI Confidence: **99.31%**
95. **`packages/grafana-data/src/transformations/transformers/calculateField.ts`** -> AI Confidence: **99.31%**
96. **`packages/grafana-data/src/transformations/transformers/convertFieldType.ts`** -> AI Confidence: **99.31%**
97. **`packages/grafana-data/src/transformations/transformers/groupToNestedTable.ts`** -> AI Confidence: **99.31%**
98. **`packages/grafana-data/src/transformations/transformers/reduce.ts`** -> AI Confidence: **99.31%**
99. **`packages/grafana-data/src/utils/csv.ts`** -> AI Confidence: **99.31%**
100. **`packages/grafana-flamegraph/src/CallTree/FlameGraphCallTreeContainer.tsx`** -> AI Confidence: **99.31%**
101. **`packages/grafana-flamegraph/src/FlameGraphContainer.tsx`** -> AI Confidence: **99.31%**
102. **`packages/grafana-flamegraph/src/FlameGraphPane.tsx`** -> AI Confidence: **99.31%**
103. **`packages/grafana-o11y-ds-frontend/src/TraceToLogs/TraceToLogsSettings.tsx`** -> AI Confidence: **99.31%**
104. **`packages/grafana-prometheus/src/components/PromQueryField.tsx`** -> AI Confidence: **99.31%**
105. **`packages/grafana-prometheus/src/language_provider.ts`** -> AI Confidence: **99.31%**
106. **`packages/grafana-prometheus/src/language_utils.ts`** -> AI Confidence: **99.31%**
107. **`packages/grafana-prometheus/src/querybuilder/parsing.ts`** -> AI Confidence: **99.31%**
108. **`packages/grafana-sql/src/components/visual-query-builder/SelectFunctionParameters.tsx`** -> AI Confidence: **99.31%**
109. **`packages/grafana-ui/src/components/BarGauge/BarGauge.tsx`** -> AI Confidence: **99.31%**
110. **`packages/grafana-ui/src/components/BigValue/BigValueLayout.tsx`** -> AI Confidence: **99.31%**
111. **`packages/grafana-ui/src/components/BrowserLabel/Label.tsx`** -> AI Confidence: **99.31%**
112. **`packages/grafana-ui/src/components/Cascader/Cascader.tsx`** -> AI Confidence: **99.31%**
113. **`packages/grafana-ui/src/components/Collapse/CollapsableSection.tsx`** -> AI Confidence: **99.31%**
114. **`packages/grafana-ui/src/components/Combobox/ComboboxList.tsx`** -> AI Confidence: **99.31%**
115. **`packages/grafana-ui/src/components/Combobox/useComboboxFloat.ts`** -> AI Confidence: **99.31%**
116. **`packages/grafana-ui/src/components/ConfirmButton/ConfirmButton.tsx`** -> AI Confidence: **99.31%**
117. **`packages/grafana-ui/src/components/DateTimePickers/TimeRangePicker/TimePickerContent.tsx`** -> AI Confidence: **99.31%**
118. **`packages/grafana-ui/src/components/Forms/Field.tsx`** -> AI Confidence: **99.31%**
119. **`packages/grafana-ui/src/components/Forms/InlineField.tsx`** -> AI Confidence: **99.31%**
120. **`packages/grafana-ui/src/components/Forms/RadioButtonGroup/RadioButtonGroup.tsx`** -> AI Confidence: **99.31%**
121. **`packages/grafana-ui/src/components/Link/TextLink.tsx`** -> AI Confidence: **99.31%**
122. **`packages/grafana-ui/src/components/Menu/MenuItem.tsx`** -> AI Confidence: **99.31%**
123. **`packages/grafana-ui/src/components/Monaco/CodeEditor.tsx`** -> AI Confidence: **99.31%**
124. **`packages/grafana-ui/src/components/PageLayout/PageToolbar.tsx`** -> AI Confidence: **99.31%**
125. **`packages/grafana-ui/src/components/PanelChrome/PanelChrome.tsx`** -> AI Confidence: **99.31%**
126. **`packages/grafana-ui/src/components/RadialGauge/RadialArcPath.tsx`** -> AI Confidence: **99.31%**
127. **`packages/grafana-ui/src/components/RadialGauge/RadialGauge.story.tsx`** -> AI Confidence: **99.31%**
128. **`packages/grafana-ui/src/components/RadialGauge/RadialGauge.tsx`** -> AI Confidence: **99.31%**
129. **`packages/grafana-ui/src/components/RefreshPicker/RefreshPicker.tsx`** -> AI Confidence: **99.31%**
130. **`packages/grafana-ui/src/components/Slider/Slider.tsx`** -> AI Confidence: **99.31%**
131. **`packages/grafana-ui/src/components/Splitter/useSplitter.ts`** -> AI Confidence: **99.31%**
132. **`packages/grafana-ui/src/components/Switch/Switch.tsx`** -> AI Confidence: **99.31%**
133. **`packages/grafana-ui/src/components/Table/CellActions.tsx`** -> AI Confidence: **99.31%**
134. **`packages/grafana-ui/src/components/Table/Cells/JSONViewCell.tsx`** -> AI Confidence: **99.31%**
135. **`packages/grafana-ui/src/components/Table/TableNG/components/HeaderCell.tsx`** -> AI Confidence: **99.31%**
136. **`packages/grafana-ui/src/components/Table/TableNG/utils.ts`** -> AI Confidence: **99.31%**
137. **`packages/grafana-ui/src/components/Table/TableRT/HeaderRow.tsx`** -> AI Confidence: **99.31%**
138. **`packages/grafana-ui/src/components/Table/utils.ts`** -> AI Confidence: **99.31%**
139. **`packages/grafana-ui/src/components/Tabs/Tab.tsx`** -> AI Confidence: **99.31%**
140. **`packages/grafana-ui/src/components/TagsInput/TagsInput.tsx`** -> AI Confidence: **99.31%**
141. **`packages/grafana-ui/src/components/Text/Text.tsx`** -> AI Confidence: **99.31%**
142. **`packages/grafana-ui/src/components/Toggletip/Toggletip.tsx`** -> AI Confidence: **99.31%**
143. **`packages/grafana-ui/src/components/VizLegend/VizLegendTable.tsx`** -> AI Confidence: **99.31%**
144. **`packages/grafana-ui/src/graveyard/TimeSeries/utils.ts`** -> AI Confidence: **99.31%**
145. **`packages/grafana-ui/src/slate-plugins/suggestions.tsx`** -> AI Confidence: **99.31%**
146. **`public/app/core/components/AppChrome/AppChromeService.tsx`** -> AI Confidence: **99.31%**
147. **`public/app/core/components/AppChrome/MegaMenu/MegaMenuItemText.tsx`** -> AI Confidence: **99.31%**
148. **`public/app/core/components/AppChrome/TopBar/InviteUserButton.tsx`** -> AI Confidence: **99.31%**
149. **`public/app/core/components/NavLandingPage/NavLandingPage.tsx`** -> AI Confidence: **99.31%**
150. **`public/app/core/components/OptionsUI/slider.tsx`** -> AI Confidence: **99.31%**
151. **`public/app/core/components/RolePicker/RoleMenuOption.tsx`** -> AI Confidence: **99.31%**
152. **`public/app/core/components/RolePicker/RolePicker.tsx`** -> AI Confidence: **99.31%**
153. **`public/app/core/components/RolePicker/RolePickerInput.tsx`** -> AI Confidence: **99.31%**
154. **`public/app/core/components/RolePicker/UserRolePicker.tsx`** -> AI Confidence: **99.31%**
155. **`public/app/core/components/SharedPreferences/SharedPreferencesFunctional.tsx`** -> AI Confidence: **99.31%**
156. **`public/app/core/components/TimeSeries/utils.ts`** -> AI Confidence: **99.31%**
157. **`public/app/core/components/TimelineChart/timeline.ts`** -> AI Confidence: **99.31%**
158. **`public/app/core/components/TimelineChart/utils.ts`** -> AI Confidence: **99.31%**
159. **`public/app/core/utils/richHistory.ts`** -> AI Confidence: **99.31%**
160. **`public/app/features/admin/ServerStats.tsx`** -> AI Confidence: **99.31%**
161. **`public/app/features/admin/UserAdminPage.tsx`** -> AI Confidence: **99.31%**
162. **`public/app/features/alerting/unified/AlertGroups.tsx`** -> AI Confidence: **99.31%**
163. **`public/app/features/alerting/unified/api/alertingApi.ts`** -> AI Confidence: **99.31%**
164. **`public/app/features/alerting/unified/api/prometheusApi.ts`** -> AI Confidence: **99.31%**
165. **`public/app/features/alerting/unified/components/DynamicTable.tsx`** -> AI Confidence: **99.31%**
166. **`public/app/features/alerting/unified/components/RuleNotificationSection.tsx`** -> AI Confidence: **99.31%**
167. **`public/app/features/alerting/unified/components/notification-policies/PoliciesList.tsx`** -> AI Confidence: **99.31%**
168. **`public/app/features/alerting/unified/components/notification-policies/Policy.tsx`** -> AI Confidence: **99.31%**
169. **`public/app/features/alerting/unified/components/notification-policies/components/ActionButtons.tsx`** -> AI Confidence: **99.31%**
170. **`public/app/features/alerting/unified/components/receivers/form/fields/OptionField.tsx`** -> AI Confidence: **99.31%**
171. **`public/app/features/alerting/unified/components/receivers/form/fields/TemplateSelector.tsx`** -> AI Confidence: **99.31%**
172. **`public/app/features/alerting/unified/components/rule-editor/DashboardAnnotationField.tsx`** -> AI Confidence: **99.31%**
173. **`public/app/features/alerting/unified/components/rule-editor/GrafanaEvaluationBehavior.tsx`** -> AI Confidence: **99.31%**
174. **`public/app/features/alerting/unified/components/rule-editor/NotificationsStep.tsx`** -> AI Confidence: **99.31%**
175. **`public/app/features/alerting/unified/components/rule-editor/alert-rule-form/simplifiedRouting/route-settings/RouteTimings.tsx`** -> AI Confidence: **99.31%**
176. **`public/app/features/alerting/unified/components/rule-editor/notificaton-preview/JourneyPolicyCard.tsx`** -> AI Confidence: **99.31%**
177. **`public/app/features/alerting/unified/components/rule-editor/notificaton-preview/PolicyTreeSelector.tsx`** -> AI Confidence: **99.31%**
178. **`public/app/features/alerting/unified/components/rule-viewer/Details.tsx`** -> AI Confidence: **99.31%**
179. **`public/app/features/alerting/unified/components/settings/AlertmanagerCard.tsx`** -> AI Confidence: **99.31%**
180. **`public/app/features/alerting/unified/group-details/GroupDetailsPage.tsx`** -> AI Confidence: **99.31%**
181. **`public/app/features/alerting/unified/hooks/useFilteredRules.test.ts`** -> AI Confidence: **99.31%**
182. **`public/app/features/alerting/unified/hooks/useFilteredRules.ts`** -> AI Confidence: **99.31%**
183. **`public/app/features/alerting/unified/notifications/NotificationDetailActions.tsx`** -> AI Confidence: **99.31%**
184. **`public/app/features/alerting/unified/notifications/NotificationDetailAlerts.tsx`** -> AI Confidence: **99.31%**
185. **`public/app/features/alerting/unified/notifications/NotificationsListSceneObject.tsx`** -> AI Confidence: **99.31%**
186. **`public/app/features/alerting/unified/triage/instance-details/InstanceDetailsDrawerTitle.tsx`** -> AI Confidence: **99.31%**
187. **`public/app/features/alerting/unified/triage/instance-details/InstanceTimelineSection.tsx`** -> AI Confidence: **99.31%**
188. **`public/app/features/alerting/unified/triage/rows/GenericRow.tsx`** -> AI Confidence: **99.31%**
189. **`public/app/features/alerting/unified/utils/amroutes.ts`** -> AI Confidence: **99.31%**
190. **`public/app/features/alerting/unified/utils/routeTree.ts`** -> AI Confidence: **99.31%**
191. **`public/app/features/alerting/unified/utils/rule-form.ts`** -> AI Confidence: **99.31%**
192. **`public/app/features/annotations/components/AnnotationResultMapper.tsx`** -> AI Confidence: **99.31%**
193. **`public/app/features/auth-config/FieldRenderer.tsx`** -> AI Confidence: **99.31%**
194. **`public/app/features/browse-dashboards/components/CreateNewButton.tsx`** -> AI Confidence: **99.31%**
195. **`public/app/features/browse-dashboards/state/reducers.ts`** -> AI Confidence: **99.31%**
196. **`public/app/features/canvas/elements/button.tsx`** -> AI Confidence: **99.31%**
197. **`public/app/features/canvas/elements/droneFront.tsx`** -> AI Confidence: **99.31%**
198. **`public/app/features/canvas/elements/droneSide.tsx`** -> AI Confidence: **99.31%**
199. **`public/app/features/canvas/elements/metricValue.tsx`** -> AI Confidence: **99.31%**
200. **`public/app/features/canvas/elements/server/server.tsx`** -> AI Confidence: **99.31%**
201. **`public/app/features/canvas/elements/text.tsx`** -> AI Confidence: **99.31%**
202. **`public/app/features/canvas/elements/windTurbine.tsx`** -> AI Confidence: **99.31%**
203. **`public/app/features/canvas/runtime/frame.tsx`** -> AI Confidence: **99.31%**
204. **`public/app/features/canvas/runtime/sceneElementManagement.ts`** -> AI Confidence: **99.31%**
205. **`public/app/features/commandPalette/actions/staticActions.ts`** -> AI Confidence: **99.31%**
206. **`public/app/features/connections/hooks/useDataSourceSettingsNav.ts`** -> AI Confidence: **99.31%**
207. **`public/app/features/connections/hooks/useDataSourceTabNav.ts`** -> AI Confidence: **99.31%**
208. **`public/app/features/dashboard-scene/edit-pane/EditPaneHeader.tsx`** -> AI Confidence: **99.31%**
209. **`public/app/features/dashboard-scene/inspect/InspectJsonTab.tsx`** -> AI Confidence: **99.31%**
210. **`public/app/features/dashboard-scene/mutation-api/commands/addPanel.ts`** -> AI Confidence: **99.31%**
211. **`public/app/features/dashboard-scene/mutation-api/commands/addRow.ts`** -> AI Confidence: **99.31%**
212. **`public/app/features/dashboard-scene/mutation-api/commands/addTab.ts`** -> AI Confidence: **99.31%**
213. **`public/app/features/dashboard-scene/mutation-api/commands/listPanels.ts`** -> AI Confidence: **99.31%**
214. **`public/app/features/dashboard-scene/mutation-api/commands/movePanel.ts`** -> AI Confidence: **99.31%**
215. **`public/app/features/dashboard-scene/mutation-api/commands/movePanelsHelper.ts`** -> AI Confidence: **99.31%**
216. **`public/app/features/dashboard-scene/mutation-api/commands/updatePanel.ts`** -> AI Confidence: **99.31%**
217. **`public/app/features/dashboard-scene/panel-edit/PanelEditNext/PanelDataPaneNext.tsx`** -> AI Confidence: **99.31%**
218. **`public/app/features/dashboard-scene/panel-edit/PanelEditNext/QueryEditor/Footer/QueryEditorFooter.tsx`** -> AI Confidence: **99.31%**
219. **`public/app/features/dashboard-scene/panel-edit/PanelEditNext/QueryEditor/Header/HeaderActions.tsx`** -> AI Confidence: **99.31%**
220. **`public/app/features/dashboard-scene/panel-edit/PanelEditNext/QueryEditor/Sidebar/AddCardButton.tsx`** -> AI Confidence: **99.31%**
221. **`public/app/features/dashboard-scene/panel-edit/PanelEditNext/hooks.ts`** -> AI Confidence: **99.31%**
222. **`public/app/features/dashboard-scene/panel-edit/PanelOptions.tsx`** -> AI Confidence: **99.31%**
223. **`public/app/features/dashboard-scene/saving/getDashboardChanges.ts`** -> AI Confidence: **99.31%**
224. **`public/app/features/dashboard-scene/scene/DashboardControls.tsx`** -> AI Confidence: **99.31%**
225. **`public/app/features/dashboard-scene/scene/DashboardLayoutOrchestrator.tsx`** -> AI Confidence: **99.31%**
226. **`public/app/features/dashboard-scene/scene/DashboardScene.tsx`** -> AI Confidence: **99.31%**
227. **`public/app/features/dashboard-scene/scene/DashboardSceneUrlSync.ts`** -> AI Confidence: **99.31%**
228. **`public/app/features/dashboard-scene/scene/LibraryPanelBehavior.tsx`** -> AI Confidence: **99.31%**
229. **`public/app/features/dashboard-scene/scene/ManagedDashboardNavBarBadge.tsx`** -> AI Confidence: **99.31%**
230. **`public/app/features/dashboard-scene/scene/PanelNonApplicableDrilldownsSubHeader.tsx`** -> AI Confidence: **99.31%**
231. **`public/app/features/dashboard-scene/scene/VariableControls.tsx`** -> AI Confidence: **99.31%**
232. **`public/app/features/dashboard-scene/scene/dashboard-filters-overview/useFiltersOverviewState.ts`** -> AI Confidence: **99.31%**
233. **`public/app/features/dashboard-scene/scene/new-toolbar/LeftActions.tsx`** -> AI Confidence: **99.31%**
234. **`public/app/features/dashboard-scene/scene/new-toolbar/RightActions.tsx`** -> AI Confidence: **99.31%**
235. **`public/app/features/dashboard-scene/scene/setDashboardPanelContext.ts`** -> AI Confidence: **99.31%**
236. **`public/app/features/dashboard-scene/serialization/layoutSerializers/AutoGridLayoutSerializer.ts`** -> AI Confidence: **99.31%**
237. **`public/app/features/dashboard-scene/serialization/layoutSerializers/DefaultGridLayoutSerializer.ts`** -> AI Confidence: **99.31%**
238. **`public/app/features/dashboard-scene/serialization/sceneVariablesSetToVariables.ts`** -> AI Confidence: **99.31%**
239. **`public/app/features/dashboard-scene/serialization/transformSaveModelSchemaV2ToScene.ts`** -> AI Confidence: **99.31%**
240. **`public/app/features/dashboard-scene/serialization/transformSaveModelToScene.ts`** -> AI Confidence: **99.31%**
241. **`public/app/features/dashboard-scene/serialization/transformSceneToSaveModel.ts`** -> AI Confidence: **99.31%**
242. **`public/app/features/dashboard-scene/serialization/transformSceneToSaveModelSchemaV2.ts`** -> AI Confidence: **99.31%**
243. **`public/app/features/dashboard-scene/settings/variables/components/AdHocVariableForm.tsx`** -> AI Confidence: **99.31%**
244. **`public/app/features/dashboard-scene/sharing/ShareButton/share-externally/ShareAlerts.tsx`** -> AI Confidence: **99.31%**
245. **`public/app/features/dashboard-scene/utils/tracking.ts`** -> AI Confidence: **99.31%**
246. **`public/app/features/dashboard-scene/utils/variables.ts`** -> AI Confidence: **99.31%**
247. **`public/app/features/dashboard-scene/v2schema/DashboardSchemaEditor.tsx`** -> AI Confidence: **99.31%**
248. **`public/app/features/dashboard/components/GenAI/GenAIButton.tsx`** -> AI Confidence: **99.31%**
249. **`public/app/features/dashboard/components/PanelEditor/OptionsPaneCategory.tsx`** -> AI Confidence: **99.31%**
250. **`public/app/features/dashboard/components/PanelEditor/PanelEditorQueries.tsx`** -> AI Confidence: **99.31%**
251. **`public/app/features/dashboard/components/PanelEditor/getVisualizationOptions.tsx`** -> AI Confidence: **99.31%**
252. **`public/app/features/dashboard/components/PublicDashboard/DashboardBrandingFooter.tsx`** -> AI Confidence: **99.31%**
253. **`public/app/features/dashboard/components/SaveDashboard/SaveDashboardDiff.tsx`** -> AI Confidence: **99.31%**
254. **`public/app/features/dashboard/dashgrid/DashboardGrid.tsx`** -> AI Confidence: **99.31%**
255. **`public/app/features/dashboard/dashgrid/DashboardLibrary/utils/dashboardLibraryHelpers.ts`** -> AI Confidence: **99.31%**
256. **`public/app/features/dashboard/services/TimeSrv.ts`** -> AI Confidence: **99.31%**
257. **`public/app/features/dashboard/state/DashboardMigrator.ts`** -> AI Confidence: **99.31%**
258. **`public/app/features/dashboard/state/DashboardModel.ts`** -> AI Confidence: **99.31%**
259. **`public/app/features/dashboard/state/PanelModel.ts`** -> AI Confidence: **99.31%**
260. **`public/app/features/datasources/state/navModel.ts`** -> AI Confidence: **99.31%**
261. **`public/app/features/dimensions/editors/ColorDimensionEditor.tsx`** -> AI Confidence: **99.31%**
262. **`public/app/features/dimensions/editors/ResourceDimensionEditor.tsx`** -> AI Confidence: **99.31%**
263. **`public/app/features/dimensions/utils.ts`** -> AI Confidence: **99.31%**
264. **`public/app/features/explore/ContentOutline/ContentOutline.tsx`** -> AI Confidence: **99.31%**
265. **`public/app/features/explore/CorrelationEditorModeBar.tsx`** -> AI Confidence: **99.31%**
266. **`public/app/features/explore/PrometheusListView/RawListItem.tsx`** -> AI Confidence: **99.31%**
267. **`public/app/features/explore/TraceView/components/TraceTimelineViewer/SpanBarRow.tsx`** -> AI Confidence: **99.31%**
268. **`public/app/features/explore/TraceView/components/TraceTimelineViewer/SpanDetail/AccordianKeyValues.tsx`** -> AI Confidence: **99.31%**
269. **`public/app/features/explore/TraceView/createSpanLink.tsx`** -> AI Confidence: **99.31%**
270. **`public/app/features/explore/utils/decorators.ts`** -> AI Confidence: **99.31%**
271. **`public/app/features/inspector/QueryInspector.tsx`** -> AI Confidence: **99.31%**
272. **`public/app/features/live/dashboard/dashboardWatcher.ts`** -> AI Confidence: **99.31%**
273. **`public/app/features/manage-dashboards/import/utils/inputs.ts`** -> AI Confidence: **99.31%**
274. **`public/app/features/migrate-to-cloud/onprem/EmptyState/CallToAction/ConnectModal.tsx`** -> AI Confidence: **99.31%**
275. **`public/app/features/migrate-to-cloud/onprem/NameCell.tsx`** -> AI Confidence: **99.31%**
276. **`public/app/features/migrate-to-cloud/onprem/Page.tsx`** -> AI Confidence: **99.31%**
277. **`public/app/features/playlist/PlaylistPage.tsx`** -> AI Confidence: **99.31%**
278. **`public/app/features/plugins/admin/components/InstallControls/InstallControlsButton.tsx`** -> AI Confidence: **99.31%**
279. **`public/app/features/plugins/admin/components/PluginDetailsDisabledError.tsx`** -> AI Confidence: **99.31%**
280. **`public/app/features/plugins/admin/components/PluginDetailsPanel.tsx`** -> AI Confidence: **99.31%**
281. **`public/app/features/plugins/admin/components/VersionList.tsx`** -> AI Confidence: **99.31%**
282. **`public/app/features/plugins/admin/helpers.ts`** -> AI Confidence: **99.31%**
283. **`public/app/features/plugins/admin/hooks/usePluginDetailsTabs.tsx`** -> AI Confidence: **99.31%**
284. **`public/app/features/plugins/admin/hooks/usePluginInfo.tsx`** -> AI Confidence: **99.31%**
285. **`public/app/features/plugins/datasource_srv.ts`** -> AI Confidence: **99.31%**
286. **`public/app/features/plugins/extensions/registry/AddedLinksRegistry.ts`** -> AI Confidence: **99.31%**
287. **`public/app/features/plugins/extensions/usePluginLinks.tsx`** -> AI Confidence: **99.31%**
288. **`public/app/features/plugins/importer/importPluginModule.ts`** -> AI Confidence: **99.31%**
289. **`public/app/features/plugins/sandbox/distortions.ts`** -> AI Confidence: **99.31%**
290. **`public/app/features/profile/UserProfileEditForm.tsx`** -> AI Confidence: **99.31%**
291. **`public/app/features/provisioning/Config/ConfigForm.tsx`** -> AI Confidence: **99.31%**
292. **`public/app/features/provisioning/Connection/ConnectionForm.tsx`** -> AI Confidence: **99.31%**
293. **`public/app/features/provisioning/Connection/ConnectionFormPage.tsx`** -> AI Confidence: **99.31%**
294. **`public/app/features/provisioning/Connection/ConnectionListItem.tsx`** -> AI Confidence: **99.31%**
295. **`public/app/features/provisioning/File/FileHistoryPage.tsx`** -> AI Confidence: **99.31%**
296. **`public/app/features/provisioning/File/FileStatusPage.tsx`** -> AI Confidence: **99.31%**
297. **`public/app/features/provisioning/Job/FinishedJobStatus.tsx`** -> AI Confidence: **99.31%**
298. **`public/app/features/provisioning/Job/RecentJobs.tsx`** -> AI Confidence: **99.31%**
299. **`public/app/features/provisioning/Repository/DeleteRepositoryButton.tsx`** -> AI Confidence: **99.31%**
300. **`public/app/features/provisioning/Repository/RepositoryHealthCard.tsx`** -> AI Confidence: **99.31%**
301. **`public/app/features/provisioning/Repository/RepositoryListItem.tsx`** -> AI Confidence: **99.31%**
302. **`public/app/features/provisioning/Repository/RepositoryOverview.tsx`** -> AI Confidence: **99.31%**
303. **`public/app/features/provisioning/Repository/RepositoryPullStatusCard.tsx`** -> AI Confidence: **99.31%**
304. **`public/app/features/provisioning/Repository/RepositoryStatusPage.tsx`** -> AI Confidence: **99.31%**
305. **`public/app/features/provisioning/Shared/RepositoryList.tsx`** -> AI Confidence: **99.31%**
306. **`public/app/features/provisioning/Wizard/components/RepositoryField.tsx`** -> AI Confidence: **99.31%**
307. **`public/app/features/provisioning/Wizard/components/RepositoryTokenInput.tsx`** -> AI Confidence: **99.31%**
308. **`public/app/features/provisioning/Wizard/hooks/useWizardSubmission.ts`** -> AI Confidence: **99.31%**
309. **`public/app/features/provisioning/components/Dashboards/DashboardPreviewBanner.tsx`** -> AI Confidence: **99.31%**
310. **`public/app/features/provisioning/components/Dashboards/MoveProvisionedDashboardForm.tsx`** -> AI Confidence: **99.31%**
311. **`public/app/features/provisioning/components/Dashboards/SaveProvisionedDashboardForm.tsx`** -> AI Confidence: **99.31%**
312. **`public/app/features/provisioning/components/Folders/NewProvisionedFolderForm.tsx`** -> AI Confidence: **99.31%**
313. **`public/app/features/provisioning/components/Shared/PreviewBannerViewPR.tsx`** -> AI Confidence: **99.31%**
314. **`public/app/features/provisioning/components/Shared/ProvisioningAwareFolderPicker.tsx`** -> AI Confidence: **99.31%**
315. **`public/app/features/provisioning/components/Shared/ResourceEditFormSharedFields.tsx`** -> AI Confidence: **99.31%**
316. **`public/app/features/provisioning/hooks/useConnectionOptions.ts`** -> AI Confidence: **99.31%**
317. **`public/app/features/provisioning/hooks/useGetRepositoryFolders.ts`** -> AI Confidence: **99.31%**
318. **`public/app/features/provisioning/hooks/useGetResourceRepositoryView.ts`** -> AI Confidence: **99.31%**
319. **`public/app/features/provisioning/hooks/useProvisionedDashboardData.ts`** -> AI Confidence: **99.31%**
320. **`public/app/features/provisioning/hooks/useProvisionedRequestHandler.ts`** -> AI Confidence: **99.31%**
321. **`public/app/features/query/components/QueryGroupOptions.tsx`** -> AI Confidence: **99.31%**
322. **`public/app/features/query/state/DashboardQueryRunner/utils.ts`** -> AI Confidence: **99.31%**
323. **`public/app/features/query/state/PanelQueryRunner.ts`** -> AI Confidence: **99.31%**
324. **`public/app/features/query/state/runRequest.ts`** -> AI Confidence: **99.31%**
325. **`public/app/features/scopes/dashboards/ScopesDashboards.tsx`** -> AI Confidence: **99.31%**
326. **`public/app/features/scopes/dashboards/ScopesDashboardsTreeFolderItem.tsx`** -> AI Confidence: **99.31%**
327. **`public/app/features/scopes/dashboards/ScopesNavigationTreeLink.tsx`** -> AI Confidence: **99.31%**
328. **`public/app/features/scopes/selector/ScopesInput.tsx`** -> AI Confidence: **99.31%**
329. **`public/app/features/scopes/selector/ScopesSelectorService.ts`** -> AI Confidence: **99.31%**
330. **`public/app/features/scopes/selector/ScopesTree.tsx`** -> AI Confidence: **99.31%**
331. **`public/app/features/search/service/sql.ts`** -> AI Confidence: **99.31%**
332. **`public/app/features/search/service/unified.ts`** -> AI Confidence: **99.31%**
333. **`public/app/features/search/state/SearchStateManager.ts`** -> AI Confidence: **99.31%**
334. **`public/app/features/teams/create-team/CreateTeamAPICalls.tsx`** -> AI Confidence: **99.31%**
335. **`public/app/features/transformers/editors/FilterByNameTransformerEditor.tsx`** -> AI Confidence: **99.31%**
336. **`public/app/features/transformers/fieldToConfigMapping/FieldToConfigMappingEditor.tsx`** -> AI Confidence: **99.31%**
337. **`public/app/features/variables/query/operators.ts`** -> AI Confidence: **99.31%**
338. **`public/app/features/variables/query/reducer.ts`** -> AI Confidence: **99.31%**
339. **`public/app/plugins/datasource/azuremonitor/components/LogsQueryBuilder/AggregateItem.tsx`** -> AI Confidence: **99.31%**
340. **`public/app/plugins/datasource/azuremonitor/components/LogsQueryBuilder/FilterSection.tsx`** -> AI Confidence: **99.31%**
341. **`public/app/plugins/datasource/azuremonitor/components/LogsQueryBuilder/FuzzySearch.tsx`** -> AI Confidence: **99.31%**
342. **`public/app/plugins/datasource/azuremonitor/components/LogsQueryBuilder/OrderBySection.tsx`** -> AI Confidence: **99.31%**
343. **`public/app/plugins/datasource/azuremonitor/components/LogsQueryEditor/LogsQueryEditor.tsx`** -> AI Confidence: **99.31%**
344. **`public/app/plugins/datasource/azuremonitor/components/QueryEditor/QueryHeader.tsx`** -> AI Confidence: **99.31%**
345. **`public/app/plugins/datasource/azuremonitor/components/ResourcePicker/utils.ts`** -> AI Confidence: **99.31%**
346. **`public/app/plugins/datasource/azuremonitor/components/TracesQueryEditor/Filters.tsx`** -> AI Confidence: **99.31%**
347. **`public/app/plugins/datasource/azuremonitor/datasource.ts`** -> AI Confidence: **99.31%**
348. **`public/app/plugins/datasource/azuremonitor/module.ts`** -> AI Confidence: **99.31%**
349. **`public/app/plugins/datasource/cloud-monitoring/datasource.ts`** -> AI Confidence: **99.31%**
350. **`public/app/plugins/datasource/cloudwatch/components/QueryEditor/LogsQueryEditor/CloudWatchLink.tsx`** -> AI Confidence: **99.31%**
351. **`public/app/plugins/datasource/cloudwatch/components/shared/LogGroups/LogGroupsField.tsx`** -> AI Confidence: **99.31%**
352. **`public/app/plugins/datasource/cloudwatch/language/cloudwatch-logs-sql/completion/CompletionItemProvider.ts`** -> AI Confidence: **99.31%**
353. **`public/app/plugins/datasource/cloudwatch/language/cloudwatch-logs/CloudWatchLogsLanguageProvider.ts`** -> AI Confidence: **99.31%**
354. **`public/app/plugins/datasource/cloudwatch/language/cloudwatch-ppl/completion/PPLCompletionItemProvider.ts`** -> AI Confidence: **99.31%**
355. **`public/app/plugins/datasource/cloudwatch/language/cloudwatch-sql/completion/CompletionItemProvider.ts`** -> AI Confidence: **99.31%**
356. **`public/app/plugins/datasource/cloudwatch/tracking.ts`** -> AI Confidence: **99.31%**
357. **`public/app/plugins/datasource/grafana-postgresql-datasource/configuration/useAutoDetectFeatures.ts`** -> AI Confidence: **99.31%**
358. **`public/app/plugins/datasource/grafana-testdata-datasource/QueryEditor.tsx`** -> AI Confidence: **99.31%**
359. **`public/app/plugins/datasource/grafana-testdata-datasource/datasource.ts`** -> AI Confidence: **99.31%**
360. **`public/app/plugins/datasource/grafana/components/QueryEditor.tsx`** -> AI Confidence: **99.31%**
361. **`public/app/plugins/datasource/grafana/datasource.ts`** -> AI Confidence: **99.31%**
362. **`public/app/plugins/datasource/graphite/datasource.ts`** -> AI Confidence: **99.31%**
363. **`public/app/plugins/datasource/graphite/graphite_query.ts`** -> AI Confidence: **99.31%**
364. **`public/app/plugins/datasource/influxdb/components/editor/config-v2/AdvancedDBConnectionSettings.tsx`** -> AI Confidence: **99.31%**
365. **`public/app/plugins/datasource/influxdb/components/editor/config-v2/AuthSettings.tsx`** -> AI Confidence: **99.31%**
366. **`public/app/plugins/datasource/influxdb/datasource.ts`** -> AI Confidence: **99.31%**
367. **`public/app/plugins/datasource/loki/LanguageProvider.ts`** -> AI Confidence: **99.31%**
368. **`public/app/plugins/datasource/loki/querybuilder/parsing.ts`** -> AI Confidence: **99.31%**
369. **`public/app/plugins/datasource/loki/shardQuerySplitting.ts`** -> AI Confidence: **99.31%**
370. **`public/app/plugins/datasource/mssql/configuration/ConfigurationEditor.tsx`** -> AI Confidence: **99.31%**
371. **`public/app/plugins/datasource/mysql/configuration/ConfigurationEditor.tsx`** -> AI Confidence: **99.31%**
372. **`public/app/plugins/datasource/opentsdb/datasource.ts`** -> AI Confidence: **99.31%**
373. **`public/app/plugins/datasource/tempo/QueryField.tsx`** -> AI Confidence: **99.31%**
374. **`public/app/plugins/datasource/tempo/SearchTraceQLEditor/utils.ts`** -> AI Confidence: **99.31%**
375. **`public/app/plugins/datasource/tempo/datasource.ts`** -> AI Confidence: **99.31%**
376. **`public/app/plugins/datasource/tempo/resultTransformer.ts`** -> AI Confidence: **99.31%**
377. **`public/app/plugins/datasource/tempo/streaming.ts`** -> AI Confidence: **99.31%**
378. **`public/app/plugins/datasource/tempo/traceql/autocomplete.ts`** -> AI Confidence: **99.31%**
379. **`public/app/plugins/panel/alertlist/AlertInstances.tsx`** -> AI Confidence: **99.31%**
380. **`public/app/plugins/panel/alertlist/UnifiedAlertList.tsx`** -> AI Confidence: **99.31%**
381. **`public/app/plugins/panel/alertlist/util.ts`** -> AI Confidence: **99.31%**
382. **`public/app/plugins/panel/annolist/AnnoListPanel.tsx`** -> AI Confidence: **99.31%**
383. **`public/app/plugins/panel/barchart/BarChartLegend.tsx`** -> AI Confidence: **99.31%**
384. **`public/app/plugins/panel/barchart/BarChartPanel.tsx`** -> AI Confidence: **99.31%**
385. **`public/app/plugins/panel/barchart/bars.ts`** -> AI Confidence: **99.31%**
386. **`public/app/plugins/panel/barchart/utils.ts`** -> AI Confidence: **99.31%**
387. **`public/app/plugins/panel/canvas/components/CanvasTooltip.tsx`** -> AI Confidence: **99.31%**
388. **`public/app/plugins/panel/canvas/editor/element/APIEditor.tsx`** -> AI Confidence: **99.31%**
389. **`public/app/plugins/panel/canvas/editor/element/QuickPositioning.tsx`** -> AI Confidence: **99.31%**
390. **`public/app/plugins/panel/geomap/components/MarkersLegend.tsx`** -> AI Confidence: **99.31%**
391. **`public/app/plugins/panel/geomap/editor/MapViewEditor.tsx`** -> AI Confidence: **99.31%**
392. **`public/app/plugins/panel/geomap/layers/data/markersLayer.tsx`** -> AI Confidence: **99.31%**
393. **`public/app/plugins/panel/geomap/layers/data/networkLayer.tsx`** -> AI Confidence: **99.31%**
394. **`public/app/plugins/panel/geomap/layers/data/routeLayer.tsx`** -> AI Confidence: **99.31%**
395. **`public/app/plugins/panel/geomap/migrations.ts`** -> AI Confidence: **99.31%**
396. **`public/app/plugins/panel/geomap/style/markers.ts`** -> AI Confidence: **99.31%**
397. **`public/app/plugins/panel/geomap/utils/tooltip.ts`** -> AI Confidence: **99.31%**
398. **`public/app/plugins/panel/heatmap/HeatmapPanel.tsx`** -> AI Confidence: **99.31%**
399. **`public/app/plugins/panel/heatmap/HeatmapTooltip.tsx`** -> AI Confidence: **99.31%**
400. **`public/app/plugins/panel/heatmap/utils.ts`** -> AI Confidence: **99.31%**
401. **`public/app/plugins/panel/histogram/Histogram.tsx`** -> AI Confidence: **99.31%**
402. **`public/app/plugins/panel/logstable/hooks/useOrganizeFields.tsx`** -> AI Confidence: **99.31%**
403. **`public/app/plugins/panel/state-timeline/StateTimelineTooltip.tsx`** -> AI Confidence: **99.31%**
404. **`public/app/plugins/panel/timeseries/TimeSeriesPanel.tsx`** -> AI Confidence: **99.31%**
405. **`public/app/plugins/panel/timeseries/plugins/AnnotationsPlugin2.tsx`** -> AI Confidence: **99.31%**
406. **`public/app/plugins/panel/timeseries/plugins/annotations2-cluster/AnnotationTooltipHeader.tsx`** -> AI Confidence: **99.31%**
407. **`public/app/plugins/panel/timeseries/plugins/annotations2/AnnotationTooltip2.tsx`** -> AI Confidence: **99.31%**
408. **`public/app/plugins/panel/xychart/SeriesEditor.tsx`** -> AI Confidence: **99.31%**
409. **`public/app/plugins/panel/xychart/scatter.ts`** -> AI Confidence: **99.31%**
410. **`cypress.config.js`** -> AI Confidence: **99.31%**
411. **`e2e/cypress/plugins/index.js`** -> AI Confidence: **99.31%**
412. **`scripts/webpack/webpack.dev.js`** -> AI Confidence: **99.31%**
413. **`scripts/webpack/webpack.prod.js`** -> AI Confidence: **99.31%**
414. **`apps/advisor/pkg/app/checks/authchecks/list_format_validation.go`** -> AI Confidence: **99.31%**
415. **`apps/advisor/pkg/app/checkscheduler/checkscheduler.go`** -> AI Confidence: **99.31%**
416. **`apps/advisor/pkg/app/checktyperegisterer/checktyperegisterer.go`** -> AI Confidence: **99.31%**
417. **`apps/advisor/pkg/app/utils.go`** -> AI Confidence: **99.31%**
418. **`apps/alerting/historian/pkg/app/notification/lokireader.go`** -> AI Confidence: **99.31%**
419. **`apps/alerting/rules/pkg/app/alertrule/validator.go`** -> AI Confidence: **99.31%**
420. **`apps/alerting/rules/pkg/app/app.go`** -> AI Confidence: **99.31%**
421. **`apps/alerting/rules/pkg/app/recordingrule/validator.go`** -> AI Confidence: **99.31%**
422. **`apps/dashboard/pkg/apis/dashboard/v0alpha1/validation.go`** -> AI Confidence: **99.31%**
423. **`apps/dashboard/pkg/apis/dashboard/v1/validation.go`** -> AI Confidence: **99.31%**
424. **`apps/dashboard/pkg/migration/conversion/metrics.go`** -> AI Confidence: **99.31%**
425. **`apps/dashboard/pkg/migration/conversion/v0alpha1_to_v1.go`** -> AI Confidence: **99.31%**
426. **`apps/dashboard/pkg/migration/conversion/v1_to_v2alpha1.go`** -> AI Confidence: **99.31%**
427. **`apps/dashboard/pkg/migration/conversion/v2alpha1_to_v1.go`** -> AI Confidence: **99.31%**
428. **`apps/dashboard/pkg/migration/frontend_defaults.go`** -> AI Confidence: **99.31%**
429. **`apps/dashboard/pkg/migration/schemaversion/v16.go`** -> AI Confidence: **99.31%**
430. **`apps/dashboard/pkg/migration/schemaversion/v38.go`** -> AI Confidence: **99.31%**
431. **`apps/example/pkg/app/conversion.go`** -> AI Confidence: **99.31%**
432. **`apps/plugins/pkg/app/install/child_reconcile.go`** -> AI Confidence: **99.31%**
433. **`apps/plugins/pkg/app/meta/manager.go`** -> AI Confidence: **99.31%**
434. **`apps/provisioning/pkg/connection/mutator.go`** -> AI Confidence: **99.31%**
435. **`apps/provisioning/pkg/connection/validator.go`** -> AI Confidence: **99.31%**
436. **`apps/provisioning/pkg/jobs/validator.go`** -> AI Confidence: **99.31%**
437. **`apps/provisioning/pkg/repository/git/repository.go`** -> AI Confidence: **99.31%**
438. **`apps/provisioning/pkg/repository/local/watch.go`** -> AI Confidence: **99.31%**
439. **`apps/provisioning/pkg/repository/validator.go`** -> AI Confidence: **99.31%**
440. **`apps/provisioning/pkg/repository/verify.go`** -> AI Confidence: **99.31%**
441. **`devenv/docker/blocks/prometheus_high_card/main.go`** -> AI Confidence: **99.31%**
442. **`devenv/docker/blocks/slow_proxy/main.go`** -> AI Confidence: **99.31%**
443. **`devenv/scopes/scopes.go`** -> AI Confidence: **99.31%**
444. **`devenv/secrets/secrets.go`** -> AI Confidence: **99.31%**
445. **`e2e/internal/cmd/a11y/cmd.go`** -> AI Confidence: **99.31%**
446. **`e2e/internal/cmd/cypress/cmd.go`** -> AI Confidence: **99.31%**
447. **`pkg/api/admin.go`** -> AI Confidence: **99.31%**
448. **`pkg/api/annotations.go`** -> AI Confidence: **99.31%**
449. **`pkg/api/api.go`** -> AI Confidence: **99.31%**
450. **`pkg/api/apierrors/folder.go`** -> AI Confidence: **99.31%**
451. **`pkg/api/dashboard.go`** -> AI Confidence: **99.31%**
452. **`pkg/api/dashboard_permission.go`** -> AI Confidence: **99.31%**
453. **`pkg/api/folder_permission.go`** -> AI Confidence: **99.31%**
454. **`pkg/api/http_server.go`** -> AI Confidence: **99.31%**
455. **`pkg/api/index.go`** -> AI Confidence: **99.31%**
456. **`pkg/api/login_oauth.go`** -> AI Confidence: **99.31%**
457. **`pkg/api/org_invite.go`** -> AI Confidence: **99.31%**
458. **`pkg/api/password.go`** -> AI Confidence: **99.31%**
459. **`pkg/api/pluginproxy/ds_auth_provider.go`** -> AI Confidence: **99.31%**
460. **`pkg/api/pluginproxy/ds_proxy.go`** -> AI Confidence: **99.31%**
461. **`pkg/api/pluginproxy/pluginproxy.go`** -> AI Confidence: **99.31%**
462. **`pkg/api/plugins.go`** -> AI Confidence: **99.31%**
463. **`pkg/api/render.go`** -> AI Confidence: **99.31%**
464. **`pkg/api/search.go`** -> AI Confidence: **99.31%**
465. **`pkg/api/short_url.go`** -> AI Confidence: **99.31%**
466. **`pkg/api/signup.go`** -> AI Confidence: **99.31%**
467. **`pkg/api/static/static.go`** -> AI Confidence: **99.31%**
468. **`pkg/api/user_token.go`** -> AI Confidence: **99.31%**
469. **`pkg/apimachinery/utils/blob.go`** -> AI Confidence: **99.31%**
470. **`pkg/apiserver/endpoints/filters/requester.go`** -> AI Confidence: **99.31%**
471. **`pkg/apiserver/registry/generic/key.go`** -> AI Confidence: **99.31%**
472. **`pkg/apiserver/storage/testing/watcher_tests.go`** -> AI Confidence: **99.31%**
473. **`pkg/cmd/grafana-cli/commands/commands.go`** -> AI Confidence: **99.31%**
474. **`pkg/cmd/grafana-cli/commands/datamigrations/encrypt_datasource_passwords.go`** -> AI Confidence: **99.31%**
475. **`pkg/cmd/grafana-cli/commands/install_command.go`** -> AI Confidence: **99.31%**
476. **`pkg/cmd/grafana-cli/commands/secretsconsolidation/secretsconsolidation.go`** -> AI Confidence: **99.31%**
477. **`pkg/cmd/grafana-cli/commands/upgrade_all_command.go`** -> AI Confidence: **99.31%**
478. **`pkg/cmd/grafana-cli/services/api_client.go`** -> AI Confidence: **99.31%**
479. **`pkg/cmd/grafana-server/commands/cli.go`** -> AI Confidence: **99.31%**
480. **`pkg/cmd/grafana-server/commands/diagnostics.go`** -> AI Confidence: **99.31%**
481. **`pkg/components/dashdiffs/formatter_json.go`** -> AI Confidence: **99.31%**
482. **`pkg/components/imguploader/imguploader.go`** -> AI Confidence: **99.31%**
483. **`pkg/components/loki/lokihttp/client.go`** -> AI Confidence: **99.31%**
484. **`pkg/components/simplejson/simplejson.go`** -> AI Confidence: **99.31%**
485. **`pkg/expr/classic/classic.go`** -> AI Confidence: **99.31%**
486. **`pkg/expr/commands.go`** -> AI Confidence: **99.31%**
487. **`pkg/expr/converter.go`** -> AI Confidence: **99.31%**
488. **`pkg/expr/dataplane.go`** -> AI Confidence: **99.31%**
489. **`pkg/expr/graph.go`** -> AI Confidence: **99.31%**
490. **`pkg/expr/mathexp/funcs.go`** -> AI Confidence: **99.31%**
491. **`pkg/expr/sql/frame_db_conv.go`** -> AI Confidence: **99.31%**
492. **`pkg/expr/sql/parser_allow.go`** -> AI Confidence: **99.31%**
493. **`pkg/infra/filestorage/cdk_blob_filestorage.go`** -> AI Confidence: **99.31%**
494. **`pkg/infra/filestorage/db_filestorage.go`** -> AI Confidence: **99.31%**
495. **`pkg/infra/filestorage/wrapper.go`** -> AI Confidence: **99.31%**
496. **`pkg/infra/metrics/metricutil/utils.go`** -> AI Confidence: **99.31%**
497. **`pkg/infra/tracing/tracing_config.go`** -> AI Confidence: **99.31%**
498. **`pkg/infra/usagestats/service/service.go`** -> AI Confidence: **99.31%**
499. **`pkg/infra/usagestats/statscollector/service.go`** -> AI Confidence: **99.31%**
500. **`pkg/login/social/connectors/azuread_oauth.go`** -> AI Confidence: **99.31%**
501. **`pkg/login/social/connectors/common.go`** -> AI Confidence: **99.31%**
502. **`pkg/login/social/connectors/generic_oauth.go`** -> AI Confidence: **99.31%**
503. **`pkg/login/social/connectors/github_oauth.go`** -> AI Confidence: **99.31%**
504. **`pkg/login/social/connectors/gitlab_oauth.go`** -> AI Confidence: **99.31%**
505. **`pkg/login/social/connectors/google_oauth.go`** -> AI Confidence: **99.31%**
506. **`pkg/login/social/socialimpl/service.go`** -> AI Confidence: **99.31%**
507. **`pkg/login/social/socialimpl/support_bundle.go`** -> AI Confidence: **99.31%**
508. **`pkg/middleware/auth.go`** -> AI Confidence: **99.31%**
509. **`pkg/middleware/loggermw/logger.go`** -> AI Confidence: **99.31%**
510. **`pkg/middleware/org_redirect.go`** -> AI Confidence: **99.31%**
511. **`pkg/modules/tracing/listener.go`** -> AI Confidence: **99.31%**
512. **`pkg/plugins/backendplugin/grpcplugin/client_v2.go`** -> AI Confidence: **99.31%**
513. **`pkg/plugins/instrumentationutils/request_status.go`** -> AI Confidence: **99.31%**
514. **`pkg/plugins/manager/client/client.go`** -> AI Confidence: **99.31%**
515. **`pkg/plugins/manager/installer.go`** -> AI Confidence: **99.31%**
516. **`pkg/plugins/manager/loader/loader.go`** -> AI Confidence: **99.31%**
517. **`pkg/plugins/manager/pipeline/bootstrap/steps.go`** -> AI Confidence: **99.31%**
518. **`pkg/plugins/manager/sources/source_local_disk.go`** -> AI Confidence: **99.31%**
519. **`pkg/plugins/repo/client.go`** -> AI Confidence: **99.31%**
520. **`pkg/registry/apis/appplugin/register.go`** -> AI Confidence: **99.31%**
521. **`pkg/registry/apis/collections/legacy/stars.go`** -> AI Confidence: **99.31%**
522. **`pkg/registry/apis/collections/stars.go`** -> AI Confidence: **99.31%**
523. **`pkg/registry/apis/collections/stars_update.go`** -> AI Confidence: **99.31%**
524. **`pkg/registry/apis/dashboard/dashboard_storage.go`** -> AI Confidence: **99.31%**
525. **`pkg/registry/apis/dashboard/large.go`** -> AI Confidence: **99.31%**
526. **`pkg/registry/apis/dashboard/legacy/sql_dashboards.go`** -> AI Confidence: **99.31%**
527. **`pkg/registry/apis/dashboard/legacy/storage.go`** -> AI Confidence: **99.31%**
528. **`pkg/registry/apis/dashboard/mutate.go`** -> AI Confidence: **99.31%**
529. **`pkg/registry/apis/dashboard/register.go`** -> AI Confidence: **99.31%**
530. **`pkg/registry/apis/dashboard/schema_validation.go`** -> AI Confidence: **99.31%**
531. **`pkg/registry/apis/dashboard/snapshot/authorizer.go`** -> AI Confidence: **99.31%**
532. **`pkg/registry/apis/datasource/authorizer.go`** -> AI Confidence: **99.31%**
533. **`pkg/registry/apis/datasource/converter/converter.go`** -> AI Confidence: **99.31%**
534. **`pkg/registry/apis/datasource/legacy_store.go`** -> AI Confidence: **99.31%**
535. **`pkg/registry/apis/datasource/migrator/validator.go`** -> AI Confidence: **99.31%**
536. **`pkg/registry/apis/datasource/openapi.go`** -> AI Confidence: **99.31%**
537. **`pkg/registry/apis/datasource/register.go`** -> AI Confidence: **99.31%**
538. **`pkg/registry/apis/folders/conversions.go`** -> AI Confidence: **99.31%**
539. **`pkg/registry/apis/folders/hooks.go`** -> AI Confidence: **99.31%**
540. **`pkg/registry/apis/folders/parents.go`** -> AI Confidence: **99.31%**
541. **`pkg/registry/apis/folders/validate.go`** -> AI Confidence: **99.31%**
542. **`pkg/registry/apis/iam/authorizer/resource_permissions.go`** -> AI Confidence: **99.31%**
543. **`pkg/registry/apis/iam/authorizer/role_permission_validator.go`** -> AI Confidence: **99.31%**
544. **`pkg/registry/apis/iam/common/common.go`** -> AI Confidence: **99.31%**
545. **`pkg/registry/apis/iam/register.go`** -> AI Confidence: **99.31%**
546. **`pkg/registry/apis/iam/resource_permission_hooks.go`** -> AI Confidence: **99.31%**
547. **`pkg/registry/apis/iam/resourcepermission/search_handler.go`** -> AI Confidence: **99.31%**
548. **`pkg/registry/apis/iam/resourcepermission/sql.go`** -> AI Confidence: **99.31%**
549. **`pkg/registry/apis/iam/resourcepermission/storage_backend.go`** -> AI Confidence: **99.31%**
550. **`pkg/registry/apis/iam/role_binding_hooks.go`** -> AI Confidence: **99.31%**
551. **`pkg/registry/apis/iam/team/legacy_search.go`** -> AI Confidence: **99.31%**
552. **`pkg/registry/apis/iam/team/rest_members.go`** -> AI Confidence: **99.31%**
553. **`pkg/registry/apis/iam/team_search.go`** -> AI Confidence: **99.31%**
554. **`pkg/registry/apis/iam/teambinding/legacy_search.go`** -> AI Confidence: **99.31%**
555. **`pkg/registry/apis/iam/teambinding/store.go`** -> AI Confidence: **99.31%**
556. **`pkg/registry/apis/iam/user/rest_display.go`** -> AI Confidence: **99.31%**
557. **`pkg/registry/apis/iam/user/rest_user_team.go`** -> AI Confidence: **99.31%**
558. **`pkg/registry/apis/iam/user/search.go`** -> AI Confidence: **99.31%**
559. **`pkg/registry/apis/iam/user/validate.go`** -> AI Confidence: **99.31%**
560. **`pkg/registry/apis/ofrep/proxy.go`** -> AI Confidence: **99.31%**
561. **`pkg/registry/apis/preferences/legacy/sql.go`** -> AI Confidence: **99.31%**
562. **`pkg/registry/apis/provisioning/controller/finalizers.go`** -> AI Confidence: **99.31%**
563. **`pkg/registry/apis/provisioning/files.go`** -> AI Confidence: **99.31%**
564. **`pkg/registry/apis/provisioning/jobs/delete/worker.go`** -> AI Confidence: **99.31%**
565. **`pkg/registry/apis/provisioning/jobs/deleteresources/worker.go`** -> AI Confidence: **99.31%**
566. **`pkg/registry/apis/provisioning/jobs/driver.go`** -> AI Confidence: **99.31%**
567. **`pkg/registry/apis/provisioning/jobs/expired_job_cleanup.go`** -> AI Confidence: **99.31%**
568. **`pkg/registry/apis/provisioning/jobs/export/resources.go`** -> AI Confidence: **99.31%**
569. **`pkg/registry/apis/provisioning/jobs/export/worker.go`** -> AI Confidence: **99.31%**
570. **`pkg/registry/apis/provisioning/jobs/fixfoldermetadata/worker.go`** -> AI Confidence: **99.31%**
571. **`pkg/registry/apis/provisioning/jobs/loki_history.go`** -> AI Confidence: **99.31%**
572. **`pkg/registry/apis/provisioning/jobs/metrics.go`** -> AI Confidence: **99.31%**
573. **`pkg/registry/apis/provisioning/jobs/move/worker.go`** -> AI Confidence: **99.31%**
574. **`pkg/registry/apis/provisioning/jobs/persistentstore.go`** -> AI Confidence: **99.31%**
575. **`pkg/registry/apis/provisioning/jobs/progress.go`** -> AI Confidence: **99.31%**
576. **`pkg/registry/apis/provisioning/jobs/releaseresources/worker.go`** -> AI Confidence: **99.31%**
577. **`pkg/registry/apis/provisioning/jobs/sync/folder_metadata_incremental_diff.go`** -> AI Confidence: **99.31%**
578. **`pkg/registry/apis/provisioning/jobs/sync/full.go`** -> AI Confidence: **99.31%**
579. **`pkg/registry/apis/provisioning/jobs/sync/worker.go`** -> AI Confidence: **99.31%**
580. **`pkg/registry/apis/provisioning/register.go`** -> AI Confidence: **99.31%**
581. **`pkg/registry/apis/provisioning/resources/authorizer.go`** -> AI Confidence: **99.31%**
582. **`pkg/registry/apis/provisioning/resources/dualwriter.go`** -> AI Confidence: **99.31%**
583. **`pkg/registry/apis/provisioning/resources/parser.go`** -> AI Confidence: **99.31%**
584. **`pkg/registry/apis/provisioning/resources/resources.go`** -> AI Confidence: **99.31%**
585. **`pkg/registry/apis/provisioning/routes.go`** -> AI Confidence: **99.31%**
586. **`pkg/registry/apis/provisioning/usage/usage.go`** -> AI Confidence: **99.31%**
587. **`pkg/registry/apis/provisioning/webhooks/pullrequest/changes.go`** -> AI Confidence: **99.31%**
588. **`pkg/registry/apis/query/queryschema/oas_helper.go`** -> AI Confidence: **99.31%**
589. **`pkg/registry/apis/secret/decrypt/authorizer.go`** -> AI Confidence: **99.31%**
590. **`pkg/registry/apis/secret/encryption/manager/manager.go`** -> AI Confidence: **99.31%**
591. **`pkg/registry/apis/secret/garbagecollectionworker/worker.go`** -> AI Confidence: **99.31%**
592. **`pkg/registry/apis/secret/inline/inline_secure_value.go`** -> AI Confidence: **99.31%**
593. **`pkg/registry/apis/secret/service/consolidation.go`** -> AI Confidence: **99.31%**
594. **`pkg/registry/apis/secret/service/dev_tools/seed_values.go`** -> AI Confidence: **99.31%**
595. **`pkg/registry/apis/secret/testutils/model_gsm.go`** -> AI Confidence: **99.31%**
596. **`pkg/registry/apis/secret/validator/keeper.go`** -> AI Confidence: **99.31%**
597. **`pkg/registry/apps/alerting/notifications/inhibitionrule/authorize.go`** -> AI Confidence: **99.31%**
598. **`pkg/registry/apps/alerting/notifications/inhibitionrule/conversions.go`** -> AI Confidence: **99.31%**
599. **`pkg/registry/apps/alerting/notifications/receiver/authorize.go`** -> AI Confidence: **99.31%**
600. **`pkg/registry/apps/alerting/notifications/receiver/conversions.go`** -> AI Confidence: **99.31%**
601. **`pkg/registry/apps/alerting/notifications/routingtree/authorize.go`** -> AI Confidence: **99.31%**
602. **`pkg/registry/apps/alerting/notifications/templategroup/authorize.go`** -> AI Confidence: **99.31%**
603. **`pkg/registry/apps/alerting/notifications/templategroup/conversions.go`** -> AI Confidence: **99.31%**
604. **`pkg/registry/apps/alerting/notifications/timeinterval/authorize.go`** -> AI Confidence: **99.31%**
605. **`pkg/registry/apps/alerting/notifications/timeinterval/conversions.go`** -> AI Confidence: **99.31%**
606. **`pkg/registry/apps/alerting/rules/alertrule/authorize.go`** -> AI Confidence: **99.31%**
607. **`pkg/registry/apps/alerting/rules/recordingrule/authorize.go`** -> AI Confidence: **99.31%**
608. **`pkg/registry/apps/alerting/rules/recordingrule/compat.go`** -> AI Confidence: **99.31%**
609. **`pkg/registry/apps/alerting/rules/register.go`** -> AI Confidence: **99.31%**
610. **`pkg/registry/apps/annotation/k8s_adapter.go`** -> AI Confidence: **99.31%**
611. **`pkg/registry/apps/annotation/postgres_partitioned.go`** -> AI Confidence: **99.31%**
612. **`pkg/registry/apps/annotation/sql_adapter.go`** -> AI Confidence: **99.31%**
613. **`pkg/registry/apps/apps.go`** -> AI Confidence: **99.31%**
614. **`pkg/registry/apps/correlations/legacy_storage.go`** -> AI Confidence: **99.31%**
615. **`pkg/registry/apps/example/register.go`** -> AI Confidence: **99.31%**
616. **`pkg/registry/apps/logsdrilldown/authorizer.go`** -> AI Confidence: **99.31%**
617. **`pkg/services/accesscontrol/acimpl/service.go`** -> AI Confidence: **99.31%**
618. **`pkg/services/accesscontrol/database/database.go`** -> AI Confidence: **99.31%**
619. **`pkg/services/accesscontrol/database/seeder.go`** -> AI Confidence: **99.31%**
620. **`pkg/services/accesscontrol/dualwrite/reconciler.go`** -> AI Confidence: **99.31%**
621. **`pkg/services/accesscontrol/dualwrite/resource_reconciler.go`** -> AI Confidence: **99.31%**
622. **`pkg/services/accesscontrol/filter.go`** -> AI Confidence: **99.31%**
623. **`pkg/services/accesscontrol/middleware.go`** -> AI Confidence: **99.31%**
624. **`pkg/services/accesscontrol/migrator/migrator.go`** -> AI Confidence: **99.31%**
625. **`pkg/services/accesscontrol/ossaccesscontrol/receivers.go`** -> AI Confidence: **99.31%**
626. **`pkg/services/accesscontrol/resourcepermissions/api.go`** -> AI Confidence: **99.31%**
627. **`pkg/services/accesscontrol/resourcepermissions/api_adapter.go`** -> AI Confidence: **99.31%**
628. **`pkg/services/accesscontrol/resourcepermissions/service.go`** -> AI Confidence: **99.31%**
629. **`pkg/services/accesscontrol/resourcepermissions/store.go`** -> AI Confidence: **99.31%**
630. **`pkg/services/accesscontrol/seeding/seeder.go`** -> AI Confidence: **99.31%**
631. **`pkg/services/annotations/annotationsimpl/loki/historian_store.go`** -> AI Confidence: **99.31%**
632. **`pkg/services/annotations/annotationsimpl/xorm_store.go`** -> AI Confidence: **99.31%**
633. **`pkg/services/anonymous/anonimpl/impl.go`** -> AI Confidence: **99.31%**
634. **`pkg/services/anonymous/sortopts/sortopts.go`** -> AI Confidence: **99.31%**
635. **`pkg/services/apiserver/appinstaller/installer.go`** -> AI Confidence: **99.31%**
636. **`pkg/services/apiserver/builder/runner/admission.go`** -> AI Confidence: **99.31%**
637. **`pkg/services/apiserver/builder/runner/builder.go`** -> AI Confidence: **99.31%**
638. **`pkg/services/apiserver/builder/scheme.go`** -> AI Confidence: **99.31%**
639. **`pkg/services/apiserver/client/discovery.go`** -> AI Confidence: **99.31%**
640. **`pkg/services/apiserver/config.go`** -> AI Confidence: **99.31%**
641. **`pkg/services/apiserver/options/storage.go`** -> AI Confidence: **99.31%**
642. **`pkg/services/apiserver/preferred_version.go`** -> AI Confidence: **99.31%**
643. **`pkg/services/apiserver/service.go`** -> AI Confidence: **99.31%**
644. **`pkg/services/auth/jwt/key_sets.go`** -> AI Confidence: **99.31%**
645. **`pkg/services/auth/jwt/validation.go`** -> AI Confidence: **99.31%**
646. **`pkg/services/authn/authnimpl/service.go`** -> AI Confidence: **99.31%**
647. **`pkg/services/authn/authnimpl/sync/oauth_token_sync.go`** -> AI Confidence: **99.31%**
648. **`pkg/services/authn/authnimpl/sync/rbac_sync.go`** -> AI Confidence: **99.31%**
649. **`pkg/services/authn/authnimpl/sync/user_sync.go`** -> AI Confidence: **99.31%**
650. **`pkg/services/authn/clients/jwt.go`** -> AI Confidence: **99.31%**
651. **`pkg/services/authn/clients/password.go`** -> AI Confidence: **99.31%**
652. **`pkg/services/authz/rbac.go`** -> AI Confidence: **99.31%**
653. **`pkg/services/authz/rbac/resolver.go`** -> AI Confidence: **99.31%**
654. **`pkg/services/authz/rbac/service.go`** -> AI Confidence: **99.31%**
655. **`pkg/services/authz/zanzana/server/reconciler/namespace.go`** -> AI Confidence: **99.31%**
656. **`pkg/services/authz/zanzana/server/reconciler/reconciler.go`** -> AI Confidence: **99.31%**
657. **`pkg/services/authz/zanzana/server/reconciler/translators.go`** -> AI Confidence: **99.31%**
658. **`pkg/services/authz/zanzana/server/server_batch_check.go`** -> AI Confidence: **99.31%**
659. **`pkg/services/authz/zanzana/server/server_mutate.go`** -> AI Confidence: **99.31%**
660. **`pkg/services/authz/zanzana/server/server_mutate_folder.go`** -> AI Confidence: **99.31%**
661. **`pkg/services/authz/zanzana/server/server_store.go`** -> AI Confidence: **99.31%**
662. **`pkg/services/authz/zanzana/server/server_write.go`** -> AI Confidence: **99.31%**
663. **`pkg/services/authz/zanzana/store/migration/migrator.go`** -> AI Confidence: **99.31%**
664. **`pkg/services/cloudmigration/cloudmigrationimpl/snapshot_mgmt.go`** -> AI Confidence: **99.31%**
665. **`pkg/services/cloudmigration/cloudmigrationimpl/xorm_store.go`** -> AI Confidence: **99.31%**
666. **`pkg/services/cloudmigration/gmsclient/gms_client.go`** -> AI Confidence: **99.31%**
667. **`pkg/services/contexthandler/model/model.go`** -> AI Confidence: **99.31%**
668. **`pkg/services/dashboardimport/service/service.go`** -> AI Confidence: **99.31%**
669. **`pkg/services/dashboardimport/utils/dash_template_evaluator.go`** -> AI Confidence: **99.31%**
670. **`pkg/services/dashboards/database/database.go`** -> AI Confidence: **99.31%**
671. **`pkg/services/dashboards/service/dashboard_service.go`** -> AI Confidence: **99.31%**
672. **`pkg/services/dashboardsnapshots/service.go`** -> AI Confidence: **99.31%**
673. **`pkg/services/dashboardversion/dashverimpl/dashver.go`** -> AI Confidence: **99.31%**
674. **`pkg/services/datasources/fakes/fake_datasource_service.go`** -> AI Confidence: **99.31%**
675. **`pkg/services/datasources/service/cache.go`** -> AI Confidence: **99.31%**
676. **`pkg/services/datasources/service/datasource.go`** -> AI Confidence: **99.31%**
677. **`pkg/services/datasources/service/store.go`** -> AI Confidence: **99.31%**
678. **`pkg/services/extsvcauth/registry/service.go`** -> AI Confidence: **99.31%**
679. **`pkg/services/featuremgmt/models.go`** -> AI Confidence: **99.31%**
680. **`pkg/services/folder/folderimpl/conversions.go`** -> AI Confidence: **99.31%**
681. **`pkg/services/folder/folderimpl/dashboard_folder_store.go`** -> AI Confidence: **99.31%**
682. **`pkg/services/folder/folderimpl/folder_unifiedstorage.go`** -> AI Confidence: **99.31%**
683. **`pkg/services/folder/folderimpl/sqlstore.go`** -> AI Confidence: **99.31%**
684. **`pkg/services/folder/folderimpl/unifiedstore.go`** -> AI Confidence: **99.31%**
685. **`pkg/services/frontend/context_middleware.go`** -> AI Confidence: **99.31%**
686. **`pkg/services/frontend/csp_middleware.go`** -> AI Confidence: **99.31%**
687. **`pkg/services/frontend/request_config_middleware.go`** -> AI Confidence: **99.31%**
688. **`pkg/services/frontend/settings_service.go`** -> AI Confidence: **99.31%**
689. **`pkg/services/ldap/api/service.go`** -> AI Confidence: **99.31%**
690. **`pkg/services/ldap/multildap/multildap.go`** -> AI Confidence: **99.31%**
691. **`pkg/services/ldap/service/ldap.go`** -> AI Confidence: **99.31%**
692. **`pkg/services/ldap/settings.go`** -> AI Confidence: **99.31%**
693. **`pkg/services/libraryelements/accesscontrol.go`** -> AI Confidence: **99.31%**
694. **`pkg/services/libraryelements/api.go`** -> AI Confidence: **99.31%**
695. **`pkg/services/libraryelements/database.go`** -> AI Confidence: **99.31%**
696. **`pkg/services/live/live.go`** -> AI Confidence: **99.31%**
697. **`pkg/services/live/pipeline/devdata.go`** -> AI Confidence: **99.31%**
698. **`pkg/services/live/pipeline/frame_output_remote_write.go`** -> AI Confidence: **99.31%**
699. **`pkg/services/live/pushhttp/push.go`** -> AI Confidence: **99.31%**
700. **`pkg/services/live/pushws/push_pipeline.go`** -> AI Confidence: **99.31%**
701. **`pkg/services/live/pushws/push_stream.go`** -> AI Confidence: **99.31%**
702. **`pkg/services/live/pushws/ws.go`** -> AI Confidence: **99.31%**
703. **`pkg/services/live/survey/survey.go`** -> AI Confidence: **99.31%**
704. **`pkg/services/live/telemetry/telegraf/convert.go`** -> AI Confidence: **99.31%**
705. **`pkg/services/login/authinfoimpl/service.go`** -> AI Confidence: **99.31%**
706. **`pkg/services/loginattempt/loginattemptimpl/login_attempt.go`** -> AI Confidence: **99.31%**
707. **`pkg/services/ngalert/accesscontrol/rules.go`** -> AI Confidence: **99.31%**
708. **`pkg/services/ngalert/accesscontrol/silences.go`** -> AI Confidence: **99.31%**
709. **`pkg/services/ngalert/api/api_alertmanager_guards.go`** -> AI Confidence: **99.31%**
710. **`pkg/services/ngalert/api/api_alertmanager_silences.go`** -> AI Confidence: **99.31%**
711. **`pkg/services/ngalert/api/api_configuration.go`** -> AI Confidence: **99.31%**
712. **`pkg/services/ngalert/api/api_provisioning.go`** -> AI Confidence: **99.31%**
713. **`pkg/services/ngalert/api/api_ruler.go`** -> AI Confidence: **99.31%**
714. **`pkg/services/ngalert/api/api_ruler_export.go`** -> AI Confidence: **99.31%**
715. **`pkg/services/ngalert/api/compat/compat.go`** -> AI Confidence: **99.31%**
716. **`pkg/services/ngalert/api/prometheus/api_prometheus.go`** -> AI Confidence: **99.31%**
717. **`pkg/services/ngalert/api/validation/api_ruler_validation.go`** -> AI Confidence: **99.31%**
718. **`pkg/services/ngalert/backtesting/engine.go`** -> AI Confidence: **99.31%**
719. **`pkg/services/ngalert/backtesting/eval_data.go`** -> AI Confidence: **99.31%**
720. **`pkg/services/ngalert/eval/eval.go`** -> AI Confidence: **99.31%**
721. **`pkg/services/ngalert/models/alert_rule.go`** -> AI Confidence: **99.31%**
722. **`pkg/services/ngalert/models/notifications.go`** -> AI Confidence: **99.31%**
723. **`pkg/services/ngalert/models/receivers.go`** -> AI Confidence: **99.31%**
724. **`pkg/services/ngalert/models/receivers_diff.go`** -> AI Confidence: **99.31%**
725. **`pkg/services/ngalert/ngalert.go`** -> AI Confidence: **99.31%**
726. **`pkg/services/ngalert/notifier/autogen_alertmanager.go`** -> AI Confidence: **99.31%**
727. **`pkg/services/ngalert/notifier/compat.go`** -> AI Confidence: **99.31%**
728. **`pkg/services/ngalert/notifier/inhibition_rules/service.go`** -> AI Confidence: **99.31%**
729. **`pkg/services/ngalert/notifier/legacy_storage/imported.go`** -> AI Confidence: **99.31%**
730. **`pkg/services/ngalert/notifier/multiorg_alertmanager.go`** -> AI Confidence: **99.31%**
731. **`pkg/services/ngalert/notifier/redis_peer.go`** -> AI Confidence: **99.31%**
732. **`pkg/services/ngalert/prom/convert.go`** -> AI Confidence: **99.31%**
733. **`pkg/services/ngalert/provisioning/alert_rules.go`** -> AI Confidence: **99.31%**
734. **`pkg/services/ngalert/provisioning/compat.go`** -> AI Confidence: **99.31%**
735. **`pkg/services/ngalert/provisioning/contactpoints.go`** -> AI Confidence: **99.31%**
736. **`pkg/services/ngalert/provisioning/mute_timings.go`** -> AI Confidence: **99.31%**
737. **`pkg/services/ngalert/provisioning/templates.go`** -> AI Confidence: **99.31%**
738. **`pkg/services/ngalert/schedule/alert_rule.go`** -> AI Confidence: **99.31%**
739. **`pkg/services/ngalert/schedule/metrics.go`** -> AI Confidence: **99.31%**
740. **`pkg/services/ngalert/schedule/recording_rule.go`** -> AI Confidence: **99.31%**
741. **`pkg/services/ngalert/schedule/schedule.go`** -> AI Confidence: **99.31%**
742. **`pkg/services/ngalert/sender/notifier.go`** -> AI Confidence: **99.31%**
743. **`pkg/services/ngalert/sender/notifier_ext.go`** -> AI Confidence: **99.31%**
744. **`pkg/services/ngalert/sender/router.go`** -> AI Confidence: **99.31%**
745. **`pkg/services/ngalert/sender/sender.go`** -> AI Confidence: **99.31%**
746. **`pkg/services/ngalert/state/cache.go`** -> AI Confidence: **99.31%**
747. **`pkg/services/ngalert/state/compat.go`** -> AI Confidence: **99.31%**
748. **`pkg/services/ngalert/state/historian/annotation.go`** -> AI Confidence: **99.31%**
749. **`pkg/services/ngalert/state/historian/core.go`** -> AI Confidence: **99.31%**
750. **`pkg/services/ngalert/state/historian/loki.go`** -> AI Confidence: **99.31%**
751. **`pkg/services/ngalert/state/manager.go`** -> AI Confidence: **99.31%**
752. **`pkg/services/ngalert/state/persister_sync.go`** -> AI Confidence: **99.31%**
753. **`pkg/services/ngalert/state/template/funcs.go`** -> AI Confidence: **99.31%**
754. **`pkg/services/ngalert/state/template/template.go`** -> AI Confidence: **99.31%**
755. **`pkg/services/ngalert/store/alert_rule.go`** -> AI Confidence: **99.31%**
756. **`pkg/services/ngalert/store/instance_database.go`** -> AI Confidence: **99.31%**
757. **`pkg/services/ngalert/store/namespace.go`** -> AI Confidence: **99.31%**
758. **`pkg/services/ngalert/store/proto_instance_database.go`** -> AI Confidence: **99.31%**
759. **`pkg/services/ngalert/tests/fakes/rules.go`** -> AI Confidence: **99.31%**
760. **`pkg/services/notifications/mailer.go`** -> AI Confidence: **99.31%**
761. **`pkg/services/notifications/smtp.go`** -> AI Confidence: **99.31%**
762. **`pkg/services/oauthtoken/oauth_token.go`** -> AI Confidence: **99.31%**
763. **`pkg/services/org/orgimpl/store.go`** -> AI Confidence: **99.31%**
764. **`pkg/services/plugindashboards/service/dashboard_updater.go`** -> AI Confidence: **99.31%**
765. **`pkg/services/plugindashboards/service/service.go`** -> AI Confidence: **99.31%**
766. **`pkg/services/pluginsintegration/advisor/advisor.go`** -> AI Confidence: **99.31%**
767. **`pkg/services/pluginsintegration/angulardetectorsprovider/dynamic.go`** -> AI Confidence: **99.31%**
768. **`pkg/services/pluginsintegration/clientmiddleware/grafana_request_id_header_middleware.go`** -> AI Confidence: **99.31%**
769. **`pkg/services/pluginsintegration/clientmiddleware/oauthtoken_middleware.go`** -> AI Confidence: **99.31%**
770. **`pkg/services/pluginsintegration/clientmiddleware/tracing_header_middleware.go`** -> AI Confidence: **99.31%**
771. **`pkg/services/pluginsintegration/coreplugin/coreplugins.go`** -> AI Confidence: **99.31%**
772. **`pkg/services/pluginsintegration/installsync/syncer.go`** -> AI Confidence: **99.31%**
773. **`pkg/services/pluginsintegration/keyretriever/dynamic/dynamic_retriever.go`** -> AI Confidence: **99.31%**
774. **`pkg/services/pluginsintegration/pluginconfig/config.go`** -> AI Confidence: **99.31%**
775. **`pkg/services/pluginsintegration/pluginsources/pluginsources.go`** -> AI Confidence: **99.31%**
776. **`pkg/services/pluginsintegration/serviceregistration/serviceregistration.go`** -> AI Confidence: **99.31%**
777. **`pkg/services/provisioning/alerting/rules_provisioner.go`** -> AI Confidence: **99.31%**
778. **`pkg/services/provisioning/alerting/rules_types.go`** -> AI Confidence: **99.31%**
779. **`pkg/services/provisioning/dashboards/config_reader.go`** -> AI Confidence: **99.31%**
780. **`pkg/services/provisioning/dashboards/dashboard.go`** -> AI Confidence: **99.31%**
781. **`pkg/services/provisioning/dashboards/file_reader.go`** -> AI Confidence: **99.31%**
782. **`pkg/services/provisioning/datasources/config_reader.go`** -> AI Confidence: **99.31%**
783. **`pkg/services/provisioning/datasources/datasources.go`** -> AI Confidence: **99.31%**
784. **`pkg/services/provisioning/plugins/config_reader.go`** -> AI Confidence: **99.31%**
785. **`pkg/services/provisioning/plugins/plugin_provisioner.go`** -> AI Confidence: **99.31%**
786. **`pkg/services/publicdashboards/service/query.go`** -> AI Confidence: **99.31%**
787. **`pkg/services/query/query.go`** -> AI Confidence: **99.31%**
788. **`pkg/services/quota/quotaimpl/quota.go`** -> AI Confidence: **99.31%**
789. **`pkg/services/rendering/rendering.go`** -> AI Confidence: **99.31%**
790. **`pkg/services/search/service.go`** -> AI Confidence: **99.31%**
791. **`pkg/services/secrets/migrator/reencrypt.go`** -> AI Confidence: **99.31%**
792. **`pkg/services/secrets/migrator/rollback.go`** -> AI Confidence: **99.31%**
793. **`pkg/services/serviceaccounts/database/store.go`** -> AI Confidence: **99.31%**
794. **`pkg/services/serviceaccounts/extsvcaccounts/service.go`** -> AI Confidence: **99.31%**
795. **`pkg/services/serviceaccounts/manager/service.go`** -> AI Confidence: **99.31%**
796. **`pkg/services/serviceaccounts/proxy/service.go`** -> AI Confidence: **99.31%**
797. **`pkg/services/sqlstore/database_config.go`** -> AI Confidence: **99.31%**
798. **`pkg/services/sqlstore/migrations/accesscontrol/dashboard_permissions.go`** -> AI Confidence: **99.31%**
799. **`pkg/services/sqlstore/migrations/accesscontrol/permission_migrator.go`** -> AI Confidence: **99.31%**
800. **`pkg/services/sqlstore/migrations/annotation_mig.go`** -> AI Confidence: **99.31%**
801. **`pkg/services/sqlstore/migrations/cloud_migrations.go`** -> AI Confidence: **99.31%**
802. **`pkg/services/sqlstore/migrations/dashboard_mig.go`** -> AI Confidence: **99.31%**
803. **`pkg/services/sqlstore/migrations/ualert/alert_rule_version_guid_mig.go`** -> AI Confidence: **99.31%**
804. **`pkg/services/sqlstore/migrations/ualert/ualert.go`** -> AI Confidence: **99.31%**
805. **`pkg/services/sqlstore/migrations/user_mig.go`** -> AI Confidence: **99.31%**
806. **`pkg/services/sqlstore/migrator/mysql_dialect.go`** -> AI Confidence: **99.31%**
807. **`pkg/services/sqlstore/migrator/postgres_dialect.go`** -> AI Confidence: **99.31%**
808. **`pkg/services/sqlstore/migrator/sqlite_dialect.go`** -> AI Confidence: **99.31%**
809. **`pkg/services/sqlstore/sqlstore.go`** -> AI Confidence: **99.31%**
810. **`pkg/services/sqlstore/sqlutil/sqlutil.go`** -> AI Confidence: **99.31%**
811. **`pkg/services/sqlstore/user.go`** -> AI Confidence: **99.31%**
812. **`pkg/services/ssosettings/ssosettingsimpl/service.go`** -> AI Confidence: **99.31%**
813. **`pkg/services/store/kind/dashboard/summary.go`** -> AI Confidence: **99.31%**
814. **`pkg/services/store/resolver/ds_cache.go`** -> AI Confidence: **99.31%**
815. **`pkg/services/store/tree.go`** -> AI Confidence: **99.31%**
816. **`pkg/services/supportbundles/supportbundlesimpl/collectors.go`** -> AI Confidence: **99.31%**
817. **`pkg/services/supportbundles/supportbundlesimpl/service_bundle.go`** -> AI Confidence: **99.31%**
818. **`pkg/services/team/sortopts/sortopts.go`** -> AI Confidence: **99.31%**
819. **`pkg/services/team/teamapi/team_members.go`** -> AI Confidence: **99.31%**
820. **`pkg/services/team/teamapi/team_members_adapter.go`** -> AI Confidence: **99.31%**
821. **`pkg/services/team/teamimpl/store.go`** -> AI Confidence: **99.31%**
822. **`pkg/services/team/teamk8s/team.go`** -> AI Confidence: **99.31%**
823. **`pkg/services/updatemanager/plugins.go`** -> AI Confidence: **99.31%**
824. **`pkg/services/user/userimpl/store.go`** -> AI Confidence: **99.31%**
825. **`pkg/services/user/userimpl/verifier.go`** -> AI Confidence: **99.31%**
826. **`pkg/setting/setting_grpc.go`** -> AI Confidence: **99.31%**
827. **`pkg/storage/legacysql/dualwrite/dualwriter.go`** -> AI Confidence: **99.31%**
828. **`pkg/storage/secret/metadata/decrypt_store.go`** -> AI Confidence: **99.31%**
829. **`pkg/storage/secret/metadata/secure_value_model.go`** -> AI Confidence: **99.31%**
830. **`pkg/storage/unified/apistore/managed.go`** -> AI Confidence: **99.31%**
831. **`pkg/storage/unified/apistore/prepare.go`** -> AI Confidence: **99.31%**
832. **`pkg/storage/unified/client.go`** -> AI Confidence: **99.31%**
833. **`pkg/storage/unified/migrations/migrator.go`** -> AI Confidence: **99.31%**
834. **`pkg/storage/unified/migrations/resource_migration.go`** -> AI Confidence: **99.31%**
835. **`pkg/storage/unified/migrations/resources.go`** -> AI Confidence: **99.31%**
836. **`pkg/storage/unified/migrations/status_reader.go`** -> AI Confidence: **99.31%**
837. **`pkg/storage/unified/migrations/table_locker.go`** -> AI Confidence: **99.31%**
838. **`pkg/storage/unified/migrations/table_renamer.go`** -> AI Confidence: **99.31%**
839. **`pkg/storage/unified/migrations/testcases/testcases.go`** -> AI Confidence: **99.31%**
840. **`pkg/storage/unified/migrations/validator.go`** -> AI Confidence: **99.31%**
841. **`pkg/storage/unified/resource/bulk.go`** -> AI Confidence: **99.31%**
842. **`pkg/storage/unified/resource/datastore.go`** -> AI Confidence: **99.31%**
843. **`pkg/storage/unified/resource/kv/last_import_time.go`** -> AI Confidence: **99.31%**
844. **`pkg/storage/unified/resource/kv/sqlkv.go`** -> AI Confidence: **99.31%**
845. **`pkg/storage/unified/resource/list_with_field_selectors.go`** -> AI Confidence: **99.31%**
846. **`pkg/storage/unified/resource/notifier.go`** -> AI Confidence: **99.31%**
847. **`pkg/storage/unified/resource/search.go`** -> AI Confidence: **99.31%**
848. **`pkg/storage/unified/resource/search_client.go`** -> AI Confidence: **99.31%**
849. **`pkg/storage/unified/resource/server.go`** -> AI Confidence: **99.31%**
850. **`pkg/storage/unified/resource/storage_backend.go`** -> AI Confidence: **99.31%**
851. **`pkg/storage/unified/resource/table.go`** -> AI Confidence: **99.31%**
852. **`pkg/storage/unified/resource/tenant_deleter.go`** -> AI Confidence: **99.31%**
853. **`pkg/storage/unified/resource/tenant_watcher.go`** -> AI Confidence: **99.31%**
854. **`pkg/storage/unified/search/bleve.go`** -> AI Confidence: **99.31%**
855. **`pkg/storage/unified/search/bleve_mappings.go`** -> AI Confidence: **99.31%**
856. **`pkg/storage/unified/search/builders/dashboard.go`** -> AI Confidence: **99.31%**
857. **`pkg/storage/unified/sql/backend.go`** -> AI Confidence: **99.31%**
858. **`pkg/storage/unified/sql/backend_bulk.go`** -> AI Confidence: **99.31%**
859. **`pkg/storage/unified/sql/db/dbimpl/util.go`** -> AI Confidence: **99.31%**
860. **`pkg/storage/unified/sql/db/migrations/deletion_markers.go`** -> AI Confidence: **99.31%**
861. **`pkg/storage/unified/sql/notifier_sql.go`** -> AI Confidence: **99.31%**
862. **`pkg/storage/unified/sql/service.go`** -> AI Confidence: **99.31%**
863. **`pkg/storage/unified/sql/sqltemplate/mocks/test_snapshots.go`** -> AI Confidence: **99.31%**
864. **`pkg/storage/unified/testing/benchmark.go`** -> AI Confidence: **99.31%**
865. **`pkg/storage/unified/testing/storage_backend.go`** -> AI Confidence: **99.31%**
866. **`pkg/tests/apis/helper.go`** -> AI Confidence: **99.31%**
867. **`pkg/tests/apis/zanzana_reconcile.go`** -> AI Confidence: **99.31%**
868. **`pkg/tsdb/azuremonitor/loganalytics/azure-log-analytics-datasource.go`** -> AI Confidence: **99.31%**
869. **`pkg/tsdb/azuremonitor/loganalytics/azure-response-table-frame.go`** -> AI Confidence: **99.31%**
870. **`pkg/tsdb/azuremonitor/loganalytics/traces.go`** -> AI Confidence: **99.31%**
871. **`pkg/tsdb/azuremonitor/loganalytics/utils.go`** -> AI Confidence: **99.31%**
872. **`pkg/tsdb/azuremonitor/macros/macros.go`** -> AI Confidence: **99.31%**
873. **`pkg/tsdb/azuremonitor/metrics/azuremonitor-datasource.go`** -> AI Confidence: **99.31%**
874. **`pkg/tsdb/cloud-monitoring/cloudmonitoring.go`** -> AI Confidence: **99.31%**
875. **`pkg/tsdb/cloud-monitoring/converter/converter.go`** -> AI Confidence: **99.31%**
876. **`pkg/tsdb/cloud-monitoring/resource_handler.go`** -> AI Confidence: **99.31%**
877. **`pkg/tsdb/cloud-monitoring/time_series_filter.go`** -> AI Confidence: **99.31%**
878. **`pkg/tsdb/cloud-monitoring/time_series_query.go`** -> AI Confidence: **99.31%**
879. **`pkg/tsdb/cloudwatch/get_metric_data_executor.go`** -> AI Confidence: **99.31%**
880. **`pkg/tsdb/cloudwatch/log_anomalies_query.go`** -> AI Confidence: **99.31%**
881. **`pkg/tsdb/cloudwatch/log_sync_query.go`** -> AI Confidence: **99.31%**
882. **`pkg/tsdb/cloudwatch/metric_find_query.go`** -> AI Confidence: **99.31%**
883. **`pkg/tsdb/cloudwatch/models/cloudwatch_query.go`** -> AI Confidence: **99.31%**
884. **`pkg/tsdb/cloudwatch/resource_handler.go`** -> AI Confidence: **99.31%**
885. **`pkg/tsdb/cloudwatch/services/accounts.go`** -> AI Confidence: **99.31%**
886. **`pkg/tsdb/cloudwatch/services/list_metrics.go`** -> AI Confidence: **99.31%**
887. **`pkg/tsdb/cloudwatch/time_series_query.go`** -> AI Confidence: **99.31%**
888. **`pkg/tsdb/grafana-postgresql-datasource/macros.go`** -> AI Confidence: **99.31%**
889. **`pkg/tsdb/grafana-postgresql-datasource/sqleng/handler_checkhealth.go`** -> AI Confidence: **99.31%**
890. **`pkg/tsdb/grafana-postgresql-datasource/sqleng/sql_engine.go`** -> AI Confidence: **99.31%**
891. **`pkg/tsdb/grafana-pyroscope-datasource/query.go`** -> AI Confidence: **99.31%**
892. **`pkg/tsdb/grafana-testdata-datasource/resource_handler.go`** -> AI Confidence: **99.31%**
893. **`pkg/tsdb/grafana-testdata-datasource/scenarios.go`** -> AI Confidence: **99.31%**
894. **`pkg/tsdb/grafana-testdata-datasource/sims/engine.go`** -> AI Confidence: **99.31%**
895. **`pkg/tsdb/grafana-testdata-datasource/stream_handler.go`** -> AI Confidence: **99.31%**
896. **`pkg/tsdb/grafana-testdata-datasource/usa_stats.go`** -> AI Confidence: **99.31%**
897. **`pkg/tsdb/graphite/query.go`** -> AI Confidence: **99.31%**
898. **`pkg/tsdb/graphite/utils.go`** -> AI Confidence: **99.31%**
899. **`pkg/tsdb/influxdb/flux/executor.go`** -> AI Confidence: **99.31%**
900. **`pkg/tsdb/influxdb/flux/macros.go`** -> AI Confidence: **99.31%**
901. **`pkg/tsdb/influxdb/fsql/arrow.go`** -> AI Confidence: **99.31%**
902. **`pkg/tsdb/influxdb/fsql/fsql.go`** -> AI Confidence: **99.31%**
903. **`pkg/tsdb/influxdb/healthcheck.go`** -> AI Confidence: **99.31%**
904. **`pkg/tsdb/influxdb/influxql/converter/converter.go`** -> AI Confidence: **99.31%**
905. **`pkg/tsdb/influxdb/influxql/influxql.go`** -> AI Confidence: **99.31%**
906. **`pkg/tsdb/influxdb/influxql/util/util.go`** -> AI Confidence: **99.31%**
907. **`pkg/tsdb/influxdb/models/model_parser.go`** -> AI Confidence: **99.31%**
908. **`pkg/tsdb/influxdb/models/query.go`** -> AI Confidence: **99.31%**
909. **`pkg/tsdb/jaeger/client.go`** -> AI Confidence: **99.31%**
910. **`pkg/tsdb/jaeger/grpc_client.go`** -> AI Confidence: **99.31%**
911. **`pkg/tsdb/jaeger/querydata.go`** -> AI Confidence: **99.31%**
912. **`pkg/tsdb/loki/api.go`** -> AI Confidence: **99.31%**
913. **`pkg/tsdb/loki/frame.go`** -> AI Confidence: **99.31%**
914. **`pkg/tsdb/loki/parse_query.go`** -> AI Confidence: **99.31%**
915. **`pkg/tsdb/loki/streaming.go`** -> AI Confidence: **99.31%**
916. **`pkg/tsdb/mssql/kerberos/kerberos.go`** -> AI Confidence: **99.31%**
917. **`pkg/tsdb/mssql/sqleng/connection.go`** -> AI Confidence: **99.31%**
918. **`pkg/tsdb/mssql/sqleng/handler_checkhealth.go`** -> AI Confidence: **99.31%**
919. **`pkg/tsdb/mssql/sqleng/macros.go`** -> AI Confidence: **99.31%**
920. **`pkg/tsdb/mysql/macros.go`** -> AI Confidence: **99.31%**
921. **`pkg/tsdb/mysql/sqleng/handler_checkhealth.go`** -> AI Confidence: **99.31%**
922. **`pkg/tsdb/opentsdb/callresource.go`** -> AI Confidence: **99.31%**
923. **`pkg/tsdb/opentsdb/utils.go`** -> AI Confidence: **99.31%**
924. **`pkg/tsdb/tempo/search.go`** -> AI Confidence: **99.31%**
925. **`pkg/tsdb/tempo/tempo.go`** -> AI Confidence: **99.31%**
926. **`pkg/tsdb/tempo/trace.go`** -> AI Confidence: **99.31%**
927. **`pkg/tsdb/tempo/trace_transform.go`** -> AI Confidence: **99.31%**
928. **`pkg/tsdb/tempo/traceql/metrics.go`** -> AI Confidence: **99.31%**
929. **`pkg/tsdb/zipkin/handler_querydata.go`** -> AI Confidence: **99.31%**
930. **`pkg/util/encoding.go`** -> AI Confidence: **99.31%**
931. **`pkg/util/proxyutil/reverse_proxy.go`** -> AI Confidence: **99.31%**
932. **`pkg/util/sqlite/sqlite_nocgo.go`** -> AI Confidence: **99.31%**
933. **`pkg/util/xorm/dialect_postgres.go`** -> AI Confidence: **99.31%**
934. **`pkg/util/xorm/dialect_sqlite3.go`** -> AI Confidence: **99.31%**
935. **`pkg/util/xorm/engine.go`** -> AI Confidence: **99.31%**
936. **`pkg/util/xorm/session.go`** -> AI Confidence: **99.31%**
937. **`pkg/util/xorm/session_query.go`** -> AI Confidence: **99.31%**
938. **`pkg/util/xorm/tag.go`** -> AI Confidence: **99.31%**
939. **`pkg/web/binding.go`** -> AI Confidence: **99.31%**
940. **`scripts/modowners/modowners.go`** -> AI Confidence: **99.31%**
941. **`.github/workflows/scripts/determine-npm-tag.sh`** -> AI Confidence: **99.29%**
942. **`devenv/create_docker_compose.sh`** -> AI Confidence: **99.29%**
943. **`devenv/docker/blocks/smtp/bootstrap.sh`** -> AI Confidence: **99.29%**
944. **`devenv/docker/buildcontainer/build_circle.sh`** -> AI Confidence: **99.29%**
945. **`devenv/frontend-service/local-init.sh`** -> AI Confidence: **99.29%**
946. **`e2e-playwright/start-server`** -> AI Confidence: **99.29%**
947. **`e2e/start-and-run-suite`** -> AI Confidence: **99.29%**
948. **`packaging/deb/control/postinst`** -> AI Confidence: **99.29%**
949. **`packaging/deb/control/prerm`** -> AI Confidence: **99.29%**
950. **`packaging/docker/run.sh`** -> AI Confidence: **99.29%**
951. **`packaging/rpm/control/posttrans`** -> AI Confidence: **99.29%**
952. **`packaging/wrappers/grafana`** -> AI Confidence: **99.29%**
953. **`packaging/wrappers/grafana-cli`** -> AI Confidence: **99.29%**
954. **`packaging/wrappers/grafana-server`** -> AI Confidence: **99.29%**
955. **`scripts/check-breaking-changes.sh`** -> AI Confidence: **99.29%**
956. **`scripts/check-frontend-dev.sh`** -> AI Confidence: **99.29%**
957. **`scripts/ci/backend-tests/pkgs-with-tests-named.sh`** -> AI Confidence: **99.29%**
958. **`scripts/ci/backend-tests/shard.sh`** -> AI Confidence: **99.29%**
959. **`scripts/cleanup-husky.sh`** -> AI Confidence: **99.29%**
960. **`scripts/go-workspace/update-workspace.sh`** -> AI Confidence: **99.29%**
961. **`scripts/helpers/exit-if-fail.sh`** -> AI Confidence: **99.29%**
962. **`scripts/protobuf-check.sh`** -> AI Confidence: **99.29%**
963. **`scripts/publish-npm-packages.sh`** -> AI Confidence: **99.29%**
964. **`scripts/stripnulls.sh`** -> AI Confidence: **99.29%**
965. **`scripts/tag_release.sh`** -> AI Confidence: **99.29%**
966. **`scripts/validate-npm-packages.sh`** -> AI Confidence: **99.29%**
967. **`scripts/view-playwright-ci.sh`** -> AI Confidence: **99.29%**
968. **`.github/workflows/scripts/fr-notify.mts`** -> AI Confidence: **99.29%**
969. **`.github/workflows/scripts/pr-notify.mts`** -> AI Confidence: **99.29%**
970. **`packages/grafana-data/src/transformations/transformers/nulls/nullToUndefThreshold.ts`** -> AI Confidence: **99.29%**
971. **`packages/grafana-data/src/types/select.ts`** -> AI Confidence: **99.29%**
972. **`packages/grafana-runtime/src/utils/toDataQueryError.ts`** -> AI Confidence: **99.29%**
973. **`packages/grafana-ui/src/components/JSONFormatter/json_explorer/json_explorer.ts`** -> AI Confidence: **99.29%**
974. **`packages/grafana-ui/src/graveyard/GraphNG/nullToUndefThreshold.ts`** -> AI Confidence: **99.29%**
975. **`packages/grafana-ui/src/utils/logOptions.ts`** -> AI Confidence: **99.29%**
976. **`public/app/core/time_series2.ts`** -> AI Confidence: **99.29%**
977. **`public/app/features/alerting/unified/components/receivers/TemplateDataExamples.ts`** -> AI Confidence: **99.29%**
978. **`public/app/features/alerting/unified/utils/template-constants.ts`** -> AI Confidence: **99.29%**
979. **`public/app/plugins/datasource/azuremonitor/azureMetadata/resourceTypes.ts`** -> AI Confidence: **99.29%**
980. **`public/app/plugins/datasource/cloudwatch/language/cloudwatch-sql/completion/statementPosition.ts`** -> AI Confidence: **99.29%**
981. **`public/app/plugins/panel/heatmap/renderHistogram.tsx`** -> AI Confidence: **99.29%**
982. **`scripts/cli/themeTemplates/_variables.scss.tmpl.ts`** -> AI Confidence: **99.29%**
983. **`jest.config.js`** -> AI Confidence: **99.29%**
984. **`devenv/docker/blocks/mysql_opendata/Dockerfile`** -> AI Confidence: **99.29%**
985. **`packaging/docker/custom/Dockerfile`** -> AI Confidence: **99.29%**
986. **`scripts/verify-repo-update/Dockerfile.deb`** -> AI Confidence: **99.29%**
987. **`apps/advisor/Makefile`** -> AI Confidence: **99.29%**
988. **`apps/correlations/Makefile`** -> AI Confidence: **99.29%**
989. **`pkg/semconv/Makefile`** -> AI Confidence: **99.29%**
990. **`pkg/services/featuremgmt/strcase/snake.go`** -> AI Confidence: **99.29%**
991. **`pkg/services/pluginsintegration/pluginconfig/azure_settings.go`** -> AI Confidence: **99.29%**
992. **`pkg/services/queryhistory/writers.go`** -> AI Confidence: **99.29%**
993. **`pkg/services/sqlstore/migrations/usermig/service_account_multiple_org_login_migrator.go`** -> AI Confidence: **99.29%**
994. **`pkg/setting/setting_azure.go`** -> AI Confidence: **99.29%**
995. **`pkg/tsdb/azuremonitor/metrics/migrations.go`** -> AI Confidence: **99.29%**
996. **`pkg/util/xorm/session_delete.go`** -> AI Confidence: **99.29%**
997. **`devenv/docker/blocks/mysql_opendata/import_csv.sql`** -> AI Confidence: **99.29%**
998. **`pkg/registry/apis/iam/legacy/testdata/mysql--update_org_user-update_org_user_basic.sql`** -> AI Confidence: **99.29%**
999. **`pkg/registry/apis/iam/legacy/testdata/mysql--update_team-update_team_basic.sql`** -> AI Confidence: **99.29%**
1000. **`pkg/registry/apis/iam/legacy/testdata/mysql--update_team_member_query-update_team_member_basic.sql`** -> AI Confidence: **99.29%**
1001. **`pkg/registry/apis/iam/legacy/testdata/mysql--update_user-update_user_basic.sql`** -> AI Confidence: **99.29%**
1002. **`pkg/registry/apis/iam/legacy/testdata/postgres--update_org_user-update_org_user_basic.sql`** -> AI Confidence: **99.29%**
1003. **`pkg/registry/apis/iam/legacy/testdata/postgres--update_team-update_team_basic.sql`** -> AI Confidence: **99.29%**
1004. **`pkg/registry/apis/iam/legacy/testdata/postgres--update_team_member_query-update_team_member_basic.sql`** -> AI Confidence: **99.29%**
1005. **`pkg/registry/apis/iam/legacy/testdata/postgres--update_user-update_user_basic.sql`** -> AI Confidence: **99.29%**
1006. **`pkg/registry/apis/iam/legacy/testdata/sqlite--update_org_user-update_org_user_basic.sql`** -> AI Confidence: **99.29%**
1007. **`pkg/registry/apis/iam/legacy/testdata/sqlite--update_team-update_team_basic.sql`** -> AI Confidence: **99.29%**
1008. **`pkg/registry/apis/iam/legacy/testdata/sqlite--update_team_member_query-update_team_member_basic.sql`** -> AI Confidence: **99.29%**
1009. **`pkg/registry/apis/iam/legacy/testdata/sqlite--update_user-update_user_basic.sql`** -> AI Confidence: **99.29%**
1010. **`pkg/registry/apis/iam/legacy/update_org_user.sql`** -> AI Confidence: **99.29%**
1011. **`pkg/registry/apis/iam/legacy/update_team.sql`** -> AI Confidence: **99.29%**
1012. **`pkg/registry/apis/iam/legacy/update_team_member_query.sql`** -> AI Confidence: **99.29%**
1013. **`pkg/registry/apis/iam/legacy/update_user.sql`** -> AI Confidence: **99.29%**
1014. **`pkg/storage/secret/encryption/data/data_key_disable.sql`** -> AI Confidence: **99.29%**
1015. **`pkg/storage/secret/encryption/data/data_key_disable_all.sql`** -> AI Confidence: **99.29%**
1016. **`pkg/storage/secret/encryption/data/encrypted_value_update.sql`** -> AI Confidence: **99.29%**
1017. **`pkg/storage/secret/encryption/data/encrypted_value_update_bulk.sql`** -> AI Confidence: **99.29%**
1018. **`pkg/storage/secret/encryption/testdata/mysql--data_key_disable-disable.sql`** -> AI Confidence: **99.29%**
1019. **`pkg/storage/secret/encryption/testdata/mysql--data_key_disable_all-disable.sql`** -> AI Confidence: **99.29%**
1020. **`pkg/storage/secret/encryption/testdata/mysql--encrypted_value_update-update.sql`** -> AI Confidence: **99.29%**
1021. **`pkg/storage/secret/encryption/testdata/mysql--encrypted_value_update_bulk-update_bulk_two_rows_for_same_namespace.sql`** -> AI Confidence: **99.29%**
1022. **`pkg/storage/secret/encryption/testdata/postgres--data_key_disable-disable.sql`** -> AI Confidence: **99.29%**
1023. **`pkg/storage/secret/encryption/testdata/postgres--data_key_disable_all-disable.sql`** -> AI Confidence: **99.29%**
1024. **`pkg/storage/secret/encryption/testdata/postgres--encrypted_value_update-update.sql`** -> AI Confidence: **99.29%**
1025. **`pkg/storage/secret/encryption/testdata/postgres--encrypted_value_update_bulk-update_bulk_two_rows_for_same_namespace.sql`** -> AI Confidence: **99.29%**
1026. **`pkg/storage/secret/encryption/testdata/sqlite--data_key_disable-disable.sql`** -> AI Confidence: **99.29%**
1027. **`pkg/storage/secret/encryption/testdata/sqlite--data_key_disable_all-disable.sql`** -> AI Confidence: **99.29%**
1028. **`pkg/storage/secret/encryption/testdata/sqlite--encrypted_value_update-update.sql`** -> AI Confidence: **99.29%**
1029. **`pkg/storage/secret/encryption/testdata/sqlite--encrypted_value_update_bulk-update_bulk_two_rows_for_same_namespace.sql`** -> AI Confidence: **99.29%**
1030. **`pkg/storage/secret/metadata/data/keeper_set_as_active.sql`** -> AI Confidence: **99.29%**
1031. **`pkg/storage/secret/metadata/data/keeper_update.sql`** -> AI Confidence: **99.29%**
1032. **`pkg/storage/secret/metadata/data/secure_value_create.sql`** -> AI Confidence: **99.29%**
1033. **`pkg/storage/secret/metadata/data/secure_value_set_inactive_all_from_group.sql`** -> AI Confidence: **99.29%**
1034. **`pkg/storage/secret/metadata/data/secure_value_set_version_to_active.sql`** -> AI Confidence: **99.29%**
1035. **`pkg/storage/secret/metadata/data/secure_value_set_version_to_inactive.sql`** -> AI Confidence: **99.29%**
1036. **`pkg/storage/secret/metadata/data/secure_value_updateExternalId.sql`** -> AI Confidence: **99.29%**
1037. **`pkg/storage/secret/metadata/testdata/mysql--keeper_set_as_active-keeper set as active.sql`** -> AI Confidence: **99.29%**
1038. **`pkg/storage/secret/metadata/testdata/mysql--keeper_update-update.sql`** -> AI Confidence: **99.29%**
1039. **`pkg/storage/secret/metadata/testdata/mysql--secure_value_set_inactive_all_from_group-set inactive all from group.sql`** -> AI Confidence: **99.29%**
1040. **`pkg/storage/secret/metadata/testdata/mysql--secure_value_set_version_to_active-set secure value version to active.sql`** -> AI Confidence: **99.29%**
1041. **`pkg/storage/secret/metadata/testdata/mysql--secure_value_updateExternalId-updateExternalId.sql`** -> AI Confidence: **99.29%**
1042. **`pkg/storage/secret/metadata/testdata/postgres--keeper_set_as_active-keeper set as active.sql`** -> AI Confidence: **99.29%**
1043. **`pkg/storage/secret/metadata/testdata/postgres--keeper_update-update.sql`** -> AI Confidence: **99.29%**
1044. **`pkg/storage/secret/metadata/testdata/postgres--secure_value_set_inactive_all_from_group-set inactive all from group.sql`** -> AI Confidence: **99.29%**
1045. **`pkg/storage/secret/metadata/testdata/postgres--secure_value_set_version_to_active-set secure value version to active.sql`** -> AI Confidence: **99.29%**
1046. **`pkg/storage/secret/metadata/testdata/postgres--secure_value_updateExternalId-updateExternalId.sql`** -> AI Confidence: **99.29%**
1047. **`pkg/storage/secret/metadata/testdata/sqlite--keeper_set_as_active-keeper set as active.sql`** -> AI Confidence: **99.29%**
1048. **`pkg/storage/secret/metadata/testdata/sqlite--keeper_update-update.sql`** -> AI Confidence: **99.29%**
1049. **`pkg/storage/secret/metadata/testdata/sqlite--secure_value_set_inactive_all_from_group-set inactive all from group.sql`** -> AI Confidence: **99.29%**
1050. **`pkg/storage/secret/metadata/testdata/sqlite--secure_value_set_version_to_active-set secure value version to active.sql`** -> AI Confidence: **99.29%**
1051. **`pkg/storage/secret/metadata/testdata/sqlite--secure_value_updateExternalId-updateExternalId.sql`** -> AI Confidence: **99.29%**
1052. **`pkg/storage/unified/resource/data/sqlkv_update_datastore.sql`** -> AI Confidence: **99.29%**
1053. **`pkg/storage/unified/resource/data/sqlkv_update_legacy_resource_history.sql`** -> AI Confidence: **99.29%**
1054. **`pkg/storage/unified/sql/data/resource_history_delete.sql`** -> AI Confidence: **99.29%**
1055. **`pkg/storage/unified/sql/data/resource_update.sql`** -> AI Confidence: **99.29%**
1056. **`pkg/storage/unified/sql/rvmanager/data/resource_history_update_rv.sql`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `pkg/infra/features/doc.go` -> **100.0%** Exposure
- `packages/grafana-sql/src/components/configuration/TLSSecretsConfig.tsx` -> **99.9998%** Exposure
- `packages/grafana-ui/src/components/DataSourceSettings/TLSAuthSettings.tsx` -> **99.9854%** Exposure
- `public/app/plugins/datasource/influxdb/components/editor/config-v2/AuthSettings.tsx` -> **99.7679%** Exposure
- `public/app/features/provisioning/utils/validators.test.ts` -> **99.7549%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `109` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `50056` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `public/app/core/services/context_srv.ts` (TYPESCRIPT) -> Cumulative Risk: **761.06**
- **Archetype:** `file_cluster_4` (Distance: 12.696 IQR)
- **Magnitude:** 29.69 | **LOC:** 279 | **CtrlFlow:** 33.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (98.1117%), Safety Score (95.9281%)
- **Heaviest Functions:** `extend` (Impact: 49.3), `rotateToken` (Impact: 7.8), `scheduleTokenRotationJob` (Impact: 6.4)

### 2. `public/app/features/alerting/unified/components/silences/SilencesFilter.tsx` (TYPESCRIPT) -> Cumulative Risk: **759.82**
- **Archetype:** `file_cluster_17` (Distance: 13.535 IQR)
- **Magnitude:** 20.73 | **LOC:** 223 | **CtrlFlow:** 32.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `getKeys` (Impact: 17.6), `getValuesFor` (Impact: 16.6), `updateFilter` (Impact: 11.2)

### 3. `public/app/features/datasources/api.ts` (TYPESCRIPT) -> Cumulative Risk: **743.91**
- **Archetype:** `file_cluster_4` (Distance: 10.954 IQR)
- **Magnitude:** 23.87 | **LOC:** 323 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9853%), State Flux (97.6226%)
- **Heaviest Functions:** `updateDataSource` (Impact: 18.5), `convertK8sDatasourceSettingsToLegacyData` (Impact: 17.5), `convertLegacyDatasourceSettingsPartialTo` (Impact: 13.1)

### 4. `public/app/plugins/datasource/influxdb/fsql/datasource.flightsql.ts` (TYPESCRIPT) -> Cumulative Risk: **729.49**
- **Archetype:** `file_cluster_4` (Distance: 12.549 IQR)
- **Magnitude:** 22.42 | **LOC:** 153 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9998%)
- **Heaviest Functions:** `fetchMeta` (Impact: 43.0), `fetchFields` (Impact: 7.2), `getDB` (Impact: 6.4)

### 5. `public/app/features/dashboard-scene/pages/DashboardScenePageStateManager.ts` (TYPESCRIPT) -> Cumulative Risk: **725.61**
- **Archetype:** `file_cluster_4` (Distance: 13.131 IQR)
- **Magnitude:** 68.09 | **LOC:** 1321 | **CtrlFlow:** 46.1% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `transformResponseToScene` (Impact: 69.6), `reloadDashboard` (Impact: 37.2), `getDashboardScenePageStateManager` (Impact: 18.2)

### 6. `pkg/services/store/entity_events.go` (GO) -> Cumulative Risk: **724.28**
- **Archetype:** `file_cluster_4` (Distance: 12.919 IQR)
- **Magnitude:** 144.86 | **LOC:** 177 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (99.4932%)
- **Heaviest Functions:** `Run` (Impact: 15.6), `CreateDatabaseEntityId` (Impact: 8.6), `GetLastEvent` (Impact: 5.5)

### 7. `public/app/features/playlist/PlaylistSrv.ts` (TYPESCRIPT) -> Cumulative Risk: **723.87**
- **Archetype:** `file_cluster_4` (Distance: 13.353 IQR)
- **Magnitude:** 20.0 | **LOC:** 162 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9858%), Safety Score (98.6166%)
- **Heaviest Functions:** `start` (Impact: 22.1), `navigateToDashboard` (Impact: 10.0), `stop` (Impact: 8.1)

### 8. `public/app/features/dashboard-scene/scene/SoloPanelContext.tsx` (TYPESCRIPT) -> Cumulative Risk: **720.31**
- **Archetype:** `file_cluster_13` (Distance: 11.499 IQR)
- **Magnitude:** 13.25 | **LOC:** 162 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.991%), Safety Score (86.8663%)
- **Heaviest Functions:** `matches` (Impact: 15.8), `matches` (Impact: 13.2), `renderMatchingSoloPanels` (Impact: 13.1)

### 9. `packages/grafana-ui/src/components/JSONFormatter/json_explorer/json_explorer.ts` (TYPESCRIPT) -> Cumulative Risk: **713.7**
- **Archetype:** `file_cluster_4` (Distance: 13.933 IQR)
- **Magnitude:** 22.85 | **LOC:** 432 | **CtrlFlow:** 84.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9989%)
- **Heaviest Functions:** `appendChildren` (Impact: 19.6), `removeChildren` (Impact: 19.1), `removeAChild` (Impact: 9.2)

### 10. `pkg/infra/metrics/service.go` (GO) -> Cumulative Risk: **711.63**
- **Archetype:** `file_cluster_8` (Distance: 12.258 IQR)
- **Magnitude:** 170.04 | **LOC:** 177 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (94.9638%), Safety Score (93.0692%)
- **Heaviest Functions:** `Gather` (Impact: 26.4), `Gather` (Impact: 14.6), `Run` (Impact: 10.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `devenv/docker/blocks/auth/authentik/cert.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `devenv/docker/blocks/auth/authentik/key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `devenv/docker/blocks/elastic/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `devenv/docker/blocks/elasticstack/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `devenv/docker/blocks/grafana/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `devenv/docker/blocks/mimir_backend/nginx/.htpasswd` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `devenv/docker/blocks/mysql/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `devenv/docker/blocks/mysql_exporter/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `devenv/docker/blocks/mysql_tests/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `devenv/docker/blocks/postgres/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `devenv/docker/blocks/postgres_tests/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `devenv/docker/blocks/slow_proxy/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/services/ldap/testdata/invalid.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/services/ldap/testdata/parsable.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/storage/unified/testing/storage_backend_sql_compatibility.go` (GO | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.238 IQR)
- **Top Global Matches:** file_cluster_8: 14.238, file_cluster_7: 14.304, file_cluster_15: 14.414
- **Magnitude:** 2374.52 | **LOC:** 2675 | **CtrlFlow:** 69.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (23.6702%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `NewTestSqlKvBackend` (Impact: 473.5)
  * `runOptimisticLockingDatabaseIntegrityFor` (Impact: 145.4)
  * `runTestBulkImportCompatibility` (Impact: 107.0)
  * `runBackendOperationsWithCounts` (Impact: 93.6)
  * `bulkImportLargeCounterCRUD` (Impact: 75.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 212`, `structural_boundaries: 94`, `args: 29`, `func_start: 29`, `class_start: 7`
* *Risk/State:* `state_mutation: 879`, `orphaned_logic: 10`
* *Architecture:* `io: 1`, `api: 221`, `concurrency: 78`, `import: 1`
* *Defense:* `safety: 16`, `doc: 144`, `test: 246`, `immutability_locks: 4`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` spec, folder, sql, deleted, testutil, kv, apiVersion, setting...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/services/dashboards/service/dashboard_service.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.888 IQR)
- **Top Global Matches:** file_cluster_8: 14.888, file_cluster_4: 14.993, file_cluster_0: 15.031
- **Magnitude:** 2101.46 | **LOC:** 2337 | **CtrlFlow:** 56.1% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (71.4603%), Tech Debt (38.9265%)
**Top Internal Functions/Classes:**
  * `cleanupK8sDashboardResources` (Impact: 325.6)
    * *Intent:* // cleanupK8sDashboardResources cleans up resources marked for deletion in the k8s API. // It proces...
  * `cleanupOrganizationK8sDashboards` (Impact: 319.1)
  * `UnprovisionDashboard` (Impact: 247.6)
  * `FindDashboards` (Impact: 26.8)
  * `LegacySaveCommandToUnstructured` (Impact: 23.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 207`, `structural_boundaries: 162`, `args: 46`, `func_start: 46`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 663`, `dead_code: 1`, `planned_debt: 1`, `orphaned_logic: 13`
* *Architecture:* `api: 115`, `concurrency: 26`, `import: 1`
* *Defense:* `safety: 107`, `doc: 24`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` slices, maps, publicdashboards, minRefreshInterval, dashboardUid, attribute, quota, searchstore...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/dashboard/pkg/migration/conversion/v1_to_v2alpha1.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.757 IQR)
- **Top Global Matches:** file_cluster_8: 14.757, file_cluster_7: 14.882, file_cluster_13: 14.957
- **Magnitude:** 1813.16 | **LOC:** 3139 | **CtrlFlow:** 52.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (51.8844%), Tech Debt (15.7786%)
**Top Internal Functions/Classes:**
  * `convertDashboardSpec_V1_to_V2alpha1` (Impact: 39.4)
  * `ConvertDashboard_V1_to_V2alpha1` (Impact: 23.8)
  * `getRepeatOptionsFromPanel` (Impact: 15.4)
  * `getRepeatOptionsFromLibraryPanel` (Impact: 12.9)
  * `transformCursorSyncToEnum` (Impact: 12.6)
    * *Intent:* // Enum transformation functions
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 344`, `structural_boundaries: 312`, `args: 57`, `func_start: 57`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1420`, `dead_code: 1`, `orphaned_logic: 11`
* *Architecture:* `api: 172`, `import: 1`
* *Defense:* `safety: 16`, `doc: 132`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` autoMigrateFrom, attribute, query, variableType, sorted, datasource, switch, v1...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/services/ngalert/models/testing.go` (GO | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_15` (Drift: 13.536 IQR)
- **Top Global Matches:** file_cluster_15: 13.536, file_cluster_8: 13.549, file_cluster_7: 13.748
- **Magnitude:** 1627.0 | **LOC:** 1651 | **CtrlFlow:** 36.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (60.5376%), Tech Debt (99.1546%)
**Top Internal Functions/Classes:**
  * `Generate` (Impact: 290.5)
  * `CopySilence` (Impact: 19.6)
  * `CopyContactPointRouting` (Impact: 17.1)
  * `CopyMatchers` (Impact: 15.0)
  * `AlertInstanceGen` (Impact: 14.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 173`, `args: 106`, `func_start: 106`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 524`, `planned_debt: 3`, `duplicate_logic: 21`
* *Architecture:* `api: 311`, `import: 1`
* *Defense:* `safety: 1`, `doc: 33`, `test: 2`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` slices, instant, notify, maps, webex, rand, exemplar, datasources...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/storage/unified/resource/server.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.384 IQR)
- **Top Global Matches:** file_cluster_8: 14.384, file_cluster_4: 14.442, file_cluster_7: 14.502
- **Magnitude:** 1585.58 | **LOC:** 1942 | **CtrlFlow:** 52.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (39.0778%), Tech Debt (8.6232%)
**Top Internal Functions/Classes:**
  * `Watch` (Impact: 65.5)
    * *Intent:* //nolint:gocyclo
  * `newEvent` (Impact: 54.6)
    * *Intent:* // Old value indicates an update -- otherwise a create // //nolint:gocyclo
  * `NewUninitializedResourceServer` (Impact: 32.2)
    * *Intent:* // NewUninitializedResourceServer creates a resource server without calling Init. // The caller must...
  * `List` (Impact: 29.9)
  * `Stop` (Impact: 29.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 277`, `structural_boundaries: 249`, `args: 42`, `func_start: 42`, `class_start: 19`
* *Risk/State:* `state_mutation: 695`, `dead_code: 3`, `planned_debt: 4`
* *Architecture:* `io: 1`, `api: 223`, `concurrency: 60`, `import: 1`
* *Defense:* `safety: 110`, `doc: 157`, `sync_locks: 6`, `immutability_locks: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` resource, backoff, codes, attribute, authz, unstructured, semver, validation...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/tests/apis/provisioning/common/testing.go` (GO | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.009 IQR)
- **Top Global Matches:** file_cluster_8: 14.009, file_cluster_7: 14.177, file_cluster_15: 14.207
- **Magnitude:** 1523.14 | **LOC:** 2798 | **CtrlFlow:** 54.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (46.3868%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `deleteAndWait` (Impact: 46.6)
  * `CreateRepo` (Impact: 32.7)
  * `DebugState` (Impact: 28.6)
  * `SnapshotDashboardsBySourcePath` (Impact: 28.3)
  * `RequireRepoDashboardParent` (Impact: 27.6)
    * *Intent:* // WaitForHealthyRepository waits for a repository to become healthy.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 235`, `structural_boundaries: 195`, `args: 76`, `func_start: 76`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 1`, `state_mutation: 683`, `dead_code: 3`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 211`, `concurrency: 6`, `import: 1`
* *Defense:* `safety: 44`, `doc: 92`, `test: 123`, `immutability_locks: 2`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` spec, os, assert, folders.folder.grafana.app, url, unstructured, intervalSeconds, exec...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/util/xorm/statement.go` (GO | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.078 IQR)
- **Top Global Matches:** file_cluster_11: 14.078, file_cluster_15: 14.199, file_cluster_8: 14.274
- **Magnitude:** 1507.78 | **LOC:** 1144 | **CtrlFlow:** 76.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (61.4153%), Tech Debt (8.7912%)
**Top Internal Functions/Classes:**
  * `buildUpdates` (Impact: 225.5)
  * `genGetSQL` (Impact: 46.8)
  * `genSelectSQL` (Impact: 42.1)
  * `genColumnStr` (Impact: 30.9)
  * `genCountSQL` (Impact: 21.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 307`, `structural_boundaries: 93`, `args: 55`, `func_start: 55`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 726`, `dead_code: 2`, `planned_debt: 3`
* *Architecture:* `io: 1`, `api: 84`, `import: 1`
* *Defense:* `safety: 23`, `doc: 38`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` fmt, time, strings, builder, core, driver, reflect
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/storage/unified/resource/search.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.418 IQR)
- **Top Global Matches:** file_cluster_8: 14.418, file_cluster_4: 14.422, file_cluster_13: 14.556
- **Magnitude:** 1455.12 | **LOC:** 1552 | **CtrlFlow:** 54.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.0245%), Tech Debt (7.892%)
**Top Internal Functions/Classes:**
  * `build` (Impact: 48.6)
  * `shouldRebuildIndex` (Impact: 47.0)
  * `getOrCreateIndex` (Impact: 36.0)
  * `RebuildIndexes` (Impact: 31.6)
  * `GetStats` (Impact: 27.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 240`, `structural_boundaries: 197`, `args: 35`, `func_start: 35`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 743`, `dead_code: 3`, `planned_debt: 1`
* *Architecture:* `api: 133`, `concurrency: 55`, `import: 1`
* *Defense:* `safety: 74`, `doc: 87`, `test: 2`, `sync_locks: 5`, `immutability_locks: 2`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` slices, totalHits, folders, rand, attribute, requestConversionTime, playlist, resultsConversionTime...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/plugins/pkg/app/meta/converter.go` (GO | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.157 IQR)
- **Top Global Matches:** file_cluster_8: 14.157, file_cluster_0: 14.162, file_cluster_7: 14.323
- **Magnitude:** 1431.84 | **LOC:** 888 | **CtrlFlow:** 85.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (55.5843%), Tech Debt (10.8486%)
**Top Internal Functions/Classes:**
  * `jsonDataToMetaJSONData` (Impact: 349.6)
    * *Intent:* // jsonDataToMetaJSONData converts a plugins.JSONData to a pluginsv0alpha1.MetaJSONData. // nolint:g...
  * `grafanaComPluginVersionMetaToMetaSpec` (Impact: 40.0)
    * *Intent:* // grafanaComPluginVersionMetaToMetaSpec converts a grafanaComPluginVersionMeta to a pluginsv0alpha1...
  * `pluginStorePluginToMeta` (Impact: 31.2)
    * *Intent:* // pluginStorePluginToMeta converts a pluginstore.Plugin to a pluginsv0alpha1.MetaSpec. // This is s...
  * `pluginToMetaSpec` (Impact: 27.2)
    * *Intent:* // pluginToMetaSpec converts a fully loaded *plugins.Plugin to a pluginsv0alpha1.MetaSpec.
  * `convertSignatureStatus` (Impact: 16.8)
    * *Intent:* // convertSignatureStatus converts plugins.SignatureStatus to pluginsv0alpha1.MetaV0alpha1SpecSignat...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 227`, `structural_boundaries: 40`, `args: 9`, `func_start: 9`, `class_start: 4`
* *Risk/State:* `state_mutation: 833`, `orphaned_logic: 3`
* *Architecture:* `api: 74`, `import: 1`
* *Defense:* `safety: 4`, `doc: 26`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` url, dashboard, private-glob, panel, datasource, json, pluginstore, plugins...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/tsdb/grafana-testdata-datasource/scenarios.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.547 IQR)
- **Top Global Matches:** file_cluster_8: 14.547, file_cluster_0: 14.776, file_cluster_13: 14.845
- **Magnitude:** 1359.68 | **LOC:** 1319 | **CtrlFlow:** 68.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (61.3453%), Tech Debt (10.0616%)
**Top Internal Functions/Classes:**
  * `adjustDataplaneLogsFrame` (Impact: 32.5)
    * *Intent:* // Adapted from /pkg/tsdb/loki/frame.go
  * `RandomWalk` (Impact: 27.4)
  * `predictableCSVWave` (Impact: 27.2)
  * `randomWalkTable` (Impact: 24.6)
  * `handleFallbackScenario` (Impact: 23.4)
    * *Intent:* // handleFallbackScenario handles the scenario where queryType is not set and fallbacks to scenarioI...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 162`, `structural_boundaries: 75`, `args: 31`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 893`, `orphaned_logic: 3`
* *Architecture:* `api: 87`, `import: 1`
* *Defense:* `safety: 45`, `doc: 7`, `test: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` MySQL-01, Zookeeper-02, MySQL-02, MySQL-03, Roof, tracing, notice, error...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/tests/api/alerting/testing.go` (GO | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.123 IQR)
- **Top Global Matches:** file_cluster_8: 13.123, file_cluster_7: 13.49, file_cluster_13: 13.554
- **Magnitude:** 1271.44 | **LOC:** 1690 | **CtrlFlow:** 34.1% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (38.3361%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ExportRulesWithStatus` (Impact: 14.8)
  * `RawConvertPrometheusPostRuleGroups` (Impact: 10.1)
  * `RawConvertPrometheusPostRuleGroup` (Impact: 10.1)
  * `AssignReceiverPermission` (Impact: 8.8)
    * *Intent:* // AssignReceiverPermission sends a request to access control API to assign permissions to a user, r...
  * `AssignRoutePermission` (Impact: 8.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 166`, `args: 100`, `func_start: 100`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 656`
* *Architecture:* `io: 1`, `api: 217`, `import: 1`
* *Defense:* `safety: 3`, `doc: 8`, `test: 177`, `immutability_locks: 1`, `cleanup: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` refId, quota, assert, data, userimpl, orgimpl, url, supportbundlestest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `public/app/features/dashboard-scene/scene/types/DashboardDropTarget.ts` (TYPESCRIPT) | Magnitude: 0.85 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 10, branch: 6, indent_spaces: 6, safety: 5
- `pkg/registry/apis/provisioning/resources/authorizer.go` (GO) | Magnitude: 125.68 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 116, state_mutation: 54, doc: 48, branch: 26
- `public/app/plugins/datasource/grafana-postgresql-datasource/PostgresQueryModel.ts` (TYPESCRIPT) | Magnitude: 3.89 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 18, indent_spaces: 14, structural_boundaries: 13, branch: 8
- `pkg/services/pluginsintegration/clientmiddleware/cookies_middleware.go` (GO) | Magnitude: 94.92 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 80, state_mutation: 41, branch: 21, structural_boundaries: 20
- `pkg/apis/iam/v0alpha1/types_user.go` (GO) | Magnitude: 21.24 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 6, api: 6, decorators: 6, indent_tabs: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `pkg/services/accesscontrol/database/database.go` (GO) | Magnitude: 672.78 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 508, indent_tabs: 314, encapsulation: 91, branch: 66
- `pkg/middleware/validate_action_url.go` (GO) | Magnitude: 93.86 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 74, state_mutation: 37, encapsulation: 23, structural_boundaries: 19
- `public/app/plugins/panel/heatmap/utils.ts` (TYPESCRIPT) | Magnitude: 108.27 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 691, state_mutation: 277, branch: 249, structural_boundaries: 115
- `public/app/core/utils/fetch.ts` (TYPESCRIPT) | Magnitude: 15.37 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 125, structural_boundaries: 70, branch: 39, immutability_locks: 31
- `apps/provisioning/pkg/repository/local/local.go` (GO) | Magnitude: 396.36 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 275, state_mutation: 184, branch: 71, structural_boundaries: 70

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `scripts/tag_release.sh` (SHELL) | Magnitude: 2.6 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 13, reflection_metaprogramming: 11, safety: 9, debug_prints: 9
- `pkg/web/binding.go` (GO) | Magnitude: 112.9 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 71, state_mutation: 51, branch: 26, structural_boundaries: 19
- `hack/make-aggregator-pki.sh` (SHELL) | Magnitude: 10.44 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: reflection_metaprogramming: 20, indent_spaces: 12, state_mutation: 6, structural_boundaries: 5
- `pkg/util/xorm/convert.go` (GO) | Magnitude: 387.16 | Delta: **0.077 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 296, state_mutation: 144, branch: 110, structural_boundaries: 109
- `scripts/check-breaking-changes.sh` (SHELL) | Magnitude: 7.81 | Delta: **0.092 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 38, indent_spaces: 37, branch: 32, io: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `public/app/plugins/datasource/cloudwatch/components/shared/LogGroups/LogGroupsField.tsx` (TYPESCRIPT) | Magnitude: 3.87 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 164, branch: 75, structural_boundaries: 63, args: 35
- `public/app/plugins/datasource/influxdb/components/editor/config-v2/UrlAndAuthenticationSection.tsx` (TYPESCRIPT) | Magnitude: 18.82 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 234, structural_boundaries: 46, branch: 39, ui_framework: 29
- `packages/grafana-sql/src/components/visual-query-builder/WhereRow.tsx` (TYPESCRIPT) | Magnitude: 2.31 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 61, structural_boundaries: 19, ui_framework: 13, args: 12
- `packages/grafana-ui/src/components/Table/TableNG/components/RowExpander.tsx` (TYPESCRIPT) | Magnitude: 1.25 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 10, import: 6, branch: 4
- `public/app/features/dashboard-scene/panel-edit/PanelEditNext/QueryEditor/utils.ts` (TYPESCRIPT) | Magnitude: 5.33 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 65, structural_boundaries: 41, branch: 15, api: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `pkg/plugins/backendplugin/grpcplugin/log_wrapper.go` (GO) | Magnitude: 131.52 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 65, state_mutation: 30, encapsulation: 26, api: 24
- `pkg/services/ngalert/models/testing.go` (GO) | Magnitude: 1627.0 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 815, state_mutation: 524, api: 311, structural_boundaries: 173
- `pkg/services/folder/tree.go` (GO) | Magnitude: 230.18 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 108, state_mutation: 102, api: 34, doc: 28
- `pkg/storage/unified/migrations/registry.go` (GO) | Magnitude: 212.38 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 95, indent_tabs: 89, structural_boundaries: 35, api: 32
- `pkg/storage/unified/resource/stats.go` (GO) | Magnitude: 76.82 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 31, state_mutation: 21, api: 17, time_date_logic: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `public/app/core/history/RichHistoryStorage.ts` (TYPESCRIPT) | Magnitude: 1.75 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 16, indent_spaces: 15, args: 8, func_start: 8
- `public/app/features/alerting/unified/utils/search.ts` (TYPESCRIPT) | Magnitude: 0.46 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 4, api: 2, generics: 2
- `pkg/util/xorm/logger.go` (GO) | Magnitude: 124.98 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 54, api: 39, doc: 29, args: 25
- `packages/grafana-ui/src/components/DataSourceSettings/types.ts` (TYPESCRIPT) | Magnitude: 1.84 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 16, doc: 15, indent_spaces: 15, branch: 9
- `public/app/features/alerting/unified/types/receiver-form.ts` (TYPESCRIPT) | Magnitude: 2.48 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 34, indent_spaces: 22, api: 9, generics: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `pkg/storage/unified/sql/indexer_seeders/playlists.sql` (SQLITE) | Magnitude: 58.64 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 58, duplicate_logic: 29, state_mutation: 16, args: 14
- `public/app/features/alerting/unified/components/rules/state-history/LogRecordViewer.tsx` (TYPESCRIPT) | Magnitude: 4.05 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 165, structural_boundaries: 48, ui_framework: 31, generics: 22
- `packages/grafana-data/src/dataframe/utils.ts` (TYPESCRIPT) | Magnitude: 15.37 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 61, structural_boundaries: 32, branch: 30, safety: 12
- `public/app/features/correlations/utils.ts` (TYPESCRIPT) | Magnitude: 23.68 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 179, structural_boundaries: 104, branch: 58, concurrency: 47
- `public/app/features/visualization/data-hover/ExemplarTooltip.tsx` (TYPESCRIPT) | Magnitude: 0.48 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 12, branch: 7, ui_framework: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `public/app/core/components/OptionsUI/strings.tsx` (TYPESCRIPT) | Magnitude: 2.68 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 82, structural_boundaries: 27, args: 15, ui_framework: 15
- `public/app/plugins/datasource/tempo/traceql/TempoQueryBuilderOptions.tsx` (TYPESCRIPT) | Magnitude: 3.36 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 178, structural_boundaries: 33, ui_framework: 27, branch: 25
- `public/app/features/alerting/unified/components/RuleConditionSection.tsx` (TYPESCRIPT) | Magnitude: 7.67 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 163, structural_boundaries: 41, ui_framework: 33, branch: 25
- `public/app/features/alerting/unified/rule-list/components/ListItem.tsx` (TYPESCRIPT) | Magnitude: 2.21 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 72, structural_boundaries: 19, ui_framework: 16, generics: 12
- `public/app/features/dashboard-scene/sharing/SaveBeforeShareModal.tsx` (TYPESCRIPT) | Magnitude: 2.54 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 18, ui_framework: 17, args: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/grafana-prometheus/src/datasource.ts` (TYPESCRIPT) | Magnitude: 26.98 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 167, state_mutation: 111, structural_boundaries: 72, concurrency: 45
- `scripts/modowners/modowners_test.go` (GO) | Magnitude: 93.44 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 83, encapsulation: 32, state_mutation: 29, structural_boundaries: 22
- `pkg/services/publicdashboards/metric/metric.go` (GO) | Magnitude: 76.24 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 48, state_mutation: 27, encapsulation: 12, branch: 10
- `packages/grafana-sql/src/loadResources.ts` (TYPESCRIPT) | Magnitude: 1.04 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 13, concurrency: 5, args: 4, closures: 4
- `packaging/mac/bin/grafana` (SHELL) | Magnitude: 30.66 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: safety_bypasses: 13, state_mutation: 13, structural_boundaries: 9, branch: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `pkg/registry/backgroundsvcs/adapter/doc.go` (GO) | Magnitude: 10.52 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 1, doc: 1, planned_debt: 1
- `pkg/services/query/expr_sql_schema.go` (GO) | Magnitude: 52.38 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 57, state_mutation: 21, encapsulation: 14, api: 13
- `pkg/plugins/manager/pipeline/bootstrap/doc.go` (GO) | Magnitude: 10.52 | Delta: **0.072 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 2, structural_boundaries: 1, planned_debt: 1
- `pkg/plugins/manager/pipeline/discovery/doc.go` (GO) | Magnitude: 10.52 | Delta: **0.072 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 2, structural_boundaries: 1, planned_debt: 1
- `pkg/plugins/manager/pipeline/initialization/doc.go` (GO) | Magnitude: 10.52 | Delta: **0.072 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 2, structural_boundaries: 1, planned_debt: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `pkg/services/ngalert/models/constants.go` (GO) | Magnitude: 16.6 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 5, api: 2, state_mutation: 2, indent_tabs: 2
- `pkg/setting/setting_secrets_manager.go` (GO) | Magnitude: 95.88 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 65, state_mutation: 48, encapsulation: 31, doc: 28
- `pkg/apimachinery/utils/verbs.go` (GO) | Magnitude: 35.26 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 11, api: 10, state_mutation: 10, indent_tabs: 10
- `pkg/apimachinery/errutil/doc.go` (GO) | Magnitude: 10.52 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 6, structural_boundaries: 1, sec_high_risk_execution: 1
- `pkg/extensions/main.go` (GO) | Magnitude: 13.04 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 1, api: 1, state_mutation: 1, doc: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `packages/grafana-ui/src/components/Text/Text.test.tsx` (TYPESCRIPT) | Magnitude: 1.36 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 27, args: 11, func_start: 11, structural_boundaries: 9
- `public/app/features/alerting/unified/triage/constants.ts` (TYPESCRIPT) | Magnitude: 3.0 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 32, immutability_locks: 20, structural_boundaries: 17, api: 12
- `pkg/plugins/manager/loader/angular/angularinspector/fakes.go` (GO) | Magnitude: 11.06 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 14, structural_boundaries: 7, api: 7, safety: 4
- `pkg/storage/unified/federated/client.go` (GO) | Magnitude: 27.72 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 27, state_mutation: 12, structural_boundaries: 8, encapsulation: 7
- `public/app/features/alerting/unified/components/import-to-gma/hooks.ts` (TYPESCRIPT) | Magnitude: 7.01 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 64, structural_boundaries: 30, immutability_locks: 15, args: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `pkg/registry/apis/dashboardsnapshot/exporter.go` (GO) | Magnitude: 10.52 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 20, doc: 6, sec_dead_code: 2, structural_boundaries: 1
- `pkg/tsdb/mysql/testdata/time_series/fill_null.sql` (SQLITE) | Magnitude: 0.0 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 3, orphaned_logic: 2, structural_boundaries: 1, args: 1
- `pkg/tsdb/mysql/testdata/time_series/fill_previous.sql` (SQLITE) | Magnitude: 0.0 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 3, orphaned_logic: 2, structural_boundaries: 1, args: 1
- `pkg/tsdb/mysql/testdata/time_series/fill_value.sql` (SQLITE) | Magnitude: 0.0 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 3, orphaned_logic: 2, structural_boundaries: 1, args: 1
- `pkg/infra/features/doc.go` (GO) | Magnitude: 10.52 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 8, structural_boundaries: 1, doc: 1, sec_dead_code: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `public/app/features/dashboard-scene/scene/DashboardScene.tsx` -> Churn: **57.14%** | Cog Load: 41.4845% | Debt: 86.8927%
- `public/app/features/dashboard-scene/settings/variables/VariableEditableElement.tsx` -> Churn: **57.14%** | Cog Load: 24.1204% | Debt: 99.8844%
- `public/app/features/dashboard-scene/utils/interactions.ts` -> Churn: **51.33%** | Cog Load: 10.995% | Debt: 100.0%
- `public/app/features/dashboard-scene/utils/variables.ts` -> Churn: **51.33%** | Cog Load: 37.0901% | Debt: 61.3139%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `pkg/storage/unified/testing/storage_backend_sql_compatibility.go` -> **Will Assis** (100.0% isolated ownership) | Magnitude: 2374.52
- `apps/dashboard/pkg/migration/conversion/v1_to_v2alpha1.go` -> **Kristina Demeshchik** (100.0% isolated ownership) | Magnitude: 1813.16
- `pkg/services/ngalert/models/testing.go` -> **Matheus Macabu** (100.0% isolated ownership) | Magnitude: 1627.0
- `pkg/storage/unified/resource/server.go` -> **Rafael Bortolon Paulovic** (100.0% isolated ownership) | Magnitude: 1585.58
- `pkg/tests/apis/provisioning/common/testing.go` -> **Gonzalo Trigueros Manzanas** (100.0% isolated ownership) | Magnitude: 1523.14

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `public/app/features/dashboard-scene/scene/DashboardScene.tsx` -> **Severity: 0.325** (Bridge: 0.0033 * Flux: 99.9963%)
- `public/app/features/variables/query/operators.ts` -> **Severity: 0.163** (Bridge: 0.0017 * Flux: 96.7488%)
- `public/app/features/dashboard-scene/scene/PanelMenuBehavior.tsx` -> **Severity: 0.127** (Bridge: 0.0013 * Flux: 95.2289%)
- `public/app/features/query/state/PanelQueryRunner.ts` -> **Severity: 0.086** (Bridge: 0.001 * Flux: 84.9999%)
- `public/app/features/dashboard-scene/pages/DashboardScenePageStateManager.ts` -> **Severity: 0.084** (Bridge: 0.0008 * Flux: 100.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/grafana-i18n/src/i18n.tsx` -> **Severity: 3380.4** (Blast Radius: 33.804 * Doc Risk: 100.0%)
- `pkg/apimachinery/errutil/log.go` -> **Severity: 1594.88** (Blast Radius: 16.008 * Doc Risk: 99.6302%)
- `public/app/types/unified-alerting-dto.ts` -> **Severity: 467.906** (Blast Radius: 4.713 * Doc Risk: 99.2799%)
- `public/app/types/store.ts` -> **Severity: 451.235** (Blast Radius: 4.621 * Doc Risk: 97.6487%)
- `pkg/registry/apis/iam/noopstorage/rest.go` -> **Severity: 413.661** (Blast Radius: 4.148 * Doc Risk: 99.7254%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
