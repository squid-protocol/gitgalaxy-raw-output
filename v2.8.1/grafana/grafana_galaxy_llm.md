# ARCHITECTURAL_BRIEF: grafana
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/grafana/grafana.git` |
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
| Total Artifacts | 21473 |
| Analyzed Artifacts (Scanned) | 17874 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3599 |
| Total LOC | 2254613 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 83.2% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6808 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1257 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 4.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 8.5301 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 962 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 8458 | 1065951 | 47.3% |
| GO | 4807 | 921646 | 26.9% |
| XML | 1729 | 345 | 9.7% |
| JSON | 1060 | 224375 | 5.9% |
| SQLITE | 742 | 10601 | 4.2% |
| MARKDOWN | 344 | 0 | 1.9% |
| YAML | 261 | 8573 | 1.5% |
| JAVASCRIPT | 137 | 8196 | 0.8% |
| PLAINTEXT | 126 | 17 | 0.7% |
| SHELL | 82 | 3085 | 0.5% |
| MAKEFILE | 30 | 922 | 0.2% |
| CSV | 29 | 1195 | 0.2% |
| DOCKERFILE | 27 | 374 | 0.2% |
| HTML | 18 | 4020 | 0.1% |
| PROTO | 12 | 866 | 0.1% |
| CSS | 9 | 4418 | 0.1% |
| POWERSHELL | 1 | 8 | 0.0% |
| RUBY | 1 | 19 | 0.0% |
| ASSEMBLY | 1 | 2 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z -0.01; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 24%, Callbacks & Closures Files 18%, Declarative / Non-Code 14%, Large Core Modules 12%, Defensive Guards Files 7%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 17142 | 95.9% |
| Unknown | 14 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 455 | 2.5% |
| Static: Minified & Vendor Opaque Mass | 263 | 1.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3599*

**Composition by Extension & Reason:**
- `.go`: 371x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 54x Excluded (Machine-Generated Source Code Signature: 29 LOC), 46x Excluded (Machine-Generated Source Code Signature: 35 LOC)
- `.md`: 742x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 4664 LOC), 1x Excluded (Machine-Generated Source Code Signature: 121 LOC)
- `.json`: 17x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 10x Excluded (Massive Static Asset Blob: 16576 LOC), 5x Excluded (Massive Static Asset Blob: 16488 LOC)
- `.cue`: 187x Excluded (Unsupported Extension: '.cue'), 13x Unsupported Format (.cue), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jsonc`: 10x Excluded (Machine-Generated Source Code Signature: 76 LOC), 9x Excluded (Saturation: Line 50 exceeds 500 chars), 8x Excluded (Machine-Generated Source Code Signature: 113 LOC)
- `no_extension`: 128x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 15x Unsupported Format (.undeterminable)
- `.ts`: 79x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Machine-Generated Source Code Signature: 8 LOC), 2x Excluded (Saturation: Line 18 exceeds 500 chars)
- `.tsx`: 115x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 296 LOC), 1x Excluded (Machine-Generated Source Code Signature: 107 LOC)
- `.yml`: 106x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 1979 LOC), 1x Zero-Density Threshold (LOC: 58, Signals: 0)
- `.png`: 97x Excluded (Explicitly Denied Extension: '.png')
- `.txt`: 76x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 20 LOC)
- `.snap`: 39x Excluded (Unsupported Extension: '.snap'), 22x Unsupported Format (.snap), 1x Excluded (Monolithic Amalgamation: 36396 LOC exceeds safe regex boundaries)
- `.sum`: 37x Excluded (Unsupported Extension: '.sum'), 9x Unsupported Format (.sum), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mod`: 45x Unsupported Format (.mod), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 31x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 44 LOC), 1x Excluded (Saturation: Line 6 exceeds 500 chars)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 12.2 | 6.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 25.3 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 11.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 5.4 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 18.0 | 5.7 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 11.6 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 24.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 71.1 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.1 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 6.3 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 55.1 | 77.8 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 72656 | 5757 | 10 | `pkg/services/ngalert/state/manager_private_test.go` |
| cleanup | 2713 | 875 | 0 | `pkg/tests/api/dashboards/api_dashboards_test.go` |
| guards | 59332 | 8032 | 9 | `public/app/features/canvas/runtime/element.tsx` |
| danger | 11635 | 3048 | 2 | `public/app/features/explore/state/query.test.ts` |
| concurrency | 38953 | 2960 | 4 | `e2e-playwright/dashboard-new-layouts/dashboard-group-panels.spec.ts` |
| connectivity | 73159 | 11062 | 10 | `packages/grafana-api-clients/src/clients/rtkq/legacy/endpoints.gen.ts` |
| io | 11950 | 2733 | 1 | `packages/grafana-runtime/src/services/pluginMeta/test-fixtures/v0alpha1Response.ts` |
| crypto | 0 | 0 | 0 | - |
| ipc | 477 | 156 | 0 | `Makefile` |
| time | 4478 | 1294 | 0 | `pkg/tsdb/cloudwatch/models/cloudwatch_query_test.go` |
| serialization | 2602 | 930 | 0 | `pkg/services/ngalert/api/api_prometheus_test.go` |
| regex | 2122 | 790 | 0 | `public/app/features/templating/template_srv.test.ts` |
| events | 8034 | 1499 | 0 | `pkg/registry/apis/provisioning/jobs/sync/incremental_test.go` |
| tests | 152282 | 4055 | 23 | `pkg/tests/api/alerting/api_ruler_test.go` |
| docs | 44832 | 5058 | 5 | `packages/grafana-api-clients/src/clients/rtkq/legacy/endpoints.gen.ts` |
| debt | 4052 | 1702 | 0 | `pkg/services/provisioning/stubs_test.go` |
| mutation | 259662 | 12091 | 40 | `packages/grafana-api-clients/src/clients/rtkq/legacy/endpoints.gen.ts` |
| dead_code | 15581 | 4841 | 2 | `pkg/plugins/manager/pluginfakes/fakes.go` |
| credential | 404 | 101 | 0 | `pkg/login/social/connectors/generic_oauth_test.go` |
| threat | 2795 | 509 | 0 | `public/emails/ng_alert_notification.html` |
| ml_ai | 1704 | 478 | 0 | `public/app/features/dashboard-scene/scene/DashboardScene.test.tsx` |
| ui | 43687 | 4389 | 8 | `public/app/features/alerting/unified/components/import-to-gma/ImportToGMA.tsx` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `packages/grafana-runtime/src/services/pluginMeta/test-fixtures/v0alpha1Response.ts` (Hits: 369)
- `packages/grafana-flamegraph/src/FlameGraph/testData/dataNestedSet.ts` (Hits: 257)
- `public/app/plugins/datasource/cloudwatch/mocks/cloudwatch-logs-sql-test-data/multiLineFullQueryWithCaseClause.ts` (Hits: 200)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **react.svg** (`public/img/icons/unicons/react.svg`) — 3353 inbound connections
2. **i18n.tsx** (`packages/grafana-i18n/src/i18n.tsx`) — 1928 inbound connections
3. **log.go** (`pkg/apimachinery/errutil/log.go`) — 827 inbound connections
4. **assert.ts** (`public/app/features/explore/spec/helper/assert.ts`) — 749 inbound connections
5. **setting.svg** (`public/img/icons/unicons/setting.svg`) — 717 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **dialect_postgres.go** (`pkg/util/xorm/dialect_postgres.go`) — 754 outbound dependencies
2. **index.ts** (`packages/grafana-ui/src/index.ts`) — 267 outbound dependencies
3. **api_notification_channel_test.go** (`pkg/tests/api/alerting/api_notification_channel_test.go`) — 246 outbound dependencies
4. **wire.go** (`pkg/server/wire.go`) — 202 outbound dependencies
5. **index.ts** (`packages/grafana-data/src/index.ts`) — 172 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `query` **(Compute Cores)** (@ `packages/grafana-api-clients/src/clients/rtkq/legacy/endpoints.gen.ts`) -> Impact: **2244.4** | LOC: 4300
- `query` **(Compute Cores)** (@ `packages/grafana-api-clients/src/clients/rtkq/iam/v0alpha1/endpoints.gen.ts`) -> Impact: **593.7** | LOC: 1465
- `query` **(Compute Cores)** (@ `packages/grafana-api-clients/src/clients/rtkq/notifications.alerting/v0alpha1/endpoints.gen.ts`) -> Impact: **523.4** | LOC: 1303
- `query` **(Compute Cores)** (@ `packages/grafana-api-clients/src/clients/rtkq/notifications.alerting/v1beta1/endpoints.gen.ts`) -> Impact: **523.4** | LOC: 1303
- `query` **(Compute Cores)** (@ `public/app/api/clients/scope/v0alpha1/endpoints.gen.ts`) -> Impact: **522.5** | LOC: 1173
- `query` **(Compute Cores)** (@ `packages/grafana-api-clients/src/clients/rtkq/provisioning/v0alpha1/endpoints.gen.ts`) -> Impact: **519.5** | LOC: 1671
- `query` **(Compute Cores)** (@ `packages/grafana-api-clients/src/clients/rtkq/dashboard/v2beta1/endpoints.gen.ts`) -> Impact: **475.5** | LOC: 1223
- `query` **(Compute Cores)** (@ `packages/grafana-api-clients/src/clients/rtkq/dashboard/v0alpha1/endpoints.gen.ts`) -> Impact: **419.3** | LOC: 1004
- `updateSchema` **(Many-Argument Workhorses)** (@ `public/app/features/dashboard/state/DashboardMigrator.ts`) -> Impact: **417.4** | LOC: 657
- `query` **(Compute Cores)** (@ `packages/grafana-api-clients/src/clients/rtkq/logsdrilldown/v1alpha1/endpoints.gen.ts`) -> Impact: **389.2** | LOC: 1025

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `pkg/storage/unified/resource` | 71 | 12559.66 | 15.77% | 38.57% |
| `public/img/icons/unicons` | 1240 | 11429.46 | 0.0% | 0.0% |
| `packages/grafana-prometheus/src` | 36 | 10760.19 | 21.57% | 0.0% |
| `devenv/docker/blocks/auth/authentik` | 4 | 10019.26 | 0.0% | 0.0% |
| `pkg/services/ldap/testdata` | 2 | 10000.0 | 0.0% | 0.0% |
| `pkg/api` | 87 | 9165.4 | 12.08% | 31.42% |
| `public/app/plugins/datasource/loki` | 61 | 9008.7 | 22.54% | 1.35% |
| `pkg/util/xorm` | 43 | 8985.72 | 43.16% | 46.37% |
| `apps/dashboard/pkg/migration/conversion` | 35 | 8573.14 | 12.79% | 28.86% |
| `packages/grafana-runtime/src/services/pluginMeta` | 11 | 7928.12 | 41.87% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `hack/update-codegen.sh` -> **100.0%** Exposure
- `public/app/features/dimensions/text.ts` -> **100.0%** Exposure
- `apps/advisor/pkg/app/checks/instancechecks/pinned_version_step.go` -> **100.0%** Exposure
- `pkg/apis/datasource/v0alpha1/unstructured.go` -> **100.0%** Exposure
- `pkg/cmd/grafana-cli/commands/commandstest/fake_ioutil.go` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `devenv/create_docker_compose.sh` -> **100.0%** Exposure
- `devenv/docker/loadtest/run.sh` -> **100.0%** Exposure
- `e2e/run-suite` -> **100.0%** Exposure
- `packaging/docker/build.sh` -> **100.0%** Exposure
- `packaging/docker/push_to_docker_hub.sh` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `pkg/plugins/manager/pluginfakes/fakes.go` -> **63** Orphaned Functions | **0** Duplicates
- `apps/provisioning/pkg/repository/git/repository_test.go` -> **56** Orphaned Functions | **0** Duplicates
- `pkg/storage/unified/resource/datastore_test.go` -> **33** Orphaned Functions | **0** Duplicates
- `pkg/services/accesscontrol/acimpl/service_bench_test.go` -> **32** Orphaned Functions | **0** Duplicates
- `pkg/services/ngalert/api/provisioning.go` -> **32** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `pkg/api/http_server_test.go` -> **100.0%** Exposure
- `pkg/infra/features/doc.go` -> **100.0%** Exposure
- `pkg/services/auth/jwt/rsa_keys_test.go` -> **100.0%** Exposure
- `pkg/tsdb/cloudwatch/models/settings_test.go` -> **100.0%** Exposure
- `packages/grafana-sql/src/components/configuration/TLSSecretsConfig.tsx` -> **99.9998%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `83` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `80725` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `public/app/features/canvas/runtime/scene.tsx` (TYPESCRIPT) -> Cumulative Risk: **776.94**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +1.21)
- **Magnitude:** 368.22 | **LOC:** 452 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9997%)
- **Heaviest Functions:** `load` (Defensive Guards, Impact: 28.7), `renderElement` (Defensive Guards, Impact: 25.0), `constructor` (Many-Argument Workhorses, Impact: 13.1)

### 2. `packages/grafana-prometheus/src/components/monaco-query-field/getOverrideServices.ts` (TYPESCRIPT) -> Cumulative Risk: **744.62**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z -1.21)
- **Magnitude:** 92.76 | **LOC:** 118 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (92.9876%)
- **Heaviest Functions:** `makeStorageService` (Callbacks & Closures, Impact: 18.1), `store` (Many-Argument Workhorses, Impact: 9.6), `getBoolean` (Callbacks & Closures, Impact: 8.5)

### 3. `public/app/core/services/context_srv.ts` (TYPESCRIPT) -> Cumulative Risk: **742.02**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.48)
- **Magnitude:** 154.84 | **LOC:** 279 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.988%), Concurrency (98.1117%), Documentation (96.5517%)
- **Heaviest Functions:** `hasRole` (Interface Declarations, Impact: 4.6), `isAllowedInterval` (Interface Declarations, Impact: 4.5), `scheduleTokenRotationJob` (Interface Declarations, Impact: 4.2)

### 4. `packages/grafana-ui/src/components/uPlot/plugins/KeyboardPlugin.tsx` (TYPESCRIPT) -> Cumulative Risk: **718.89**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.12)
- **Magnitude:** 128.94 | **LOC:** 176 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `handlePressedKeys` (Compute Cores, Impact: 23.8), `onKeyDown` (Compute Cores, Impact: 11.3), `onDestroy` (Defensive Guards, Impact: 7.6)

### 5. `public/app/plugins/datasource/loki/components/monaco-query-field/getOverrideServices.ts` (TYPESCRIPT) -> Cumulative Risk: **716.02**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z -1.22)
- **Magnitude:** 88.5 | **LOC:** 113 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (94.9572%)
- **Heaviest Functions:** `makeStorageService` (Callbacks & Closures, Impact: 18.1), `store` (Many-Argument Workhorses, Impact: 9.6), `getBoolean` (Callbacks & Closures, Impact: 8.5)

### 6. `public/app/features/canvas/runtime/frame.tsx` (TYPESCRIPT) -> Cumulative Risk: **715.76**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.32)
- **Magnitude:** 277.6 | **LOC:** 270 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (95.9969%), Safety Score (94.0288%)
- **Heaviest Functions:** `doAction` (Many-Argument Workhorses, Impact: 97.9), `constructor` (Many-Argument Workhorses, Impact: 17.2), `doMove` (Compute Cores, Impact: 5.7)

### 7. `public/app/plugins/panel/canvas/CanvasPanel.tsx` (TYPESCRIPT) -> Cumulative Risk: **706.15**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z -0.76)
- **Magnitude:** 258.22 | **LOC:** 350 | **CtrlFlow:** 15.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), State Flux (99.9999%), Documentation (95.777%)
- **Heaviest Functions:** `shouldComponentUpdate` (Many-Argument Workhorses, Impact: 43.2), `componentDidMount` (Callbacks & Closures, Impact: 14.7), `next` (Callbacks & Closures, Impact: 10.4)

### 8. `public/app/plugins/datasource/grafana-testdata-datasource/runStreams.ts` (TYPESCRIPT) -> Cumulative Risk: **702.45**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.62)
- **Magnitude:** 322.44 | **LOC:** 416 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9988%), State Flux (99.944%), Documentation (92.6355%)
- **Heaviest Functions:** `runWatchStream` (Defensive Guards, Impact: 29.8), `runFetchStream` (Many-Argument Workhorses, Impact: 25.9), `runSignalStream` (Many-Argument Workhorses, Impact: 21.9)

### 9. `pkg/storage/unified/resource/bulk_test.go` (GO) -> Cumulative Risk: **693.29**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.85)
- **Magnitude:** 238.34 | **LOC:** 350 | **CtrlFlow:** 8.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.1652%)
- **Heaviest Functions:** `TestBatchRunnerStopUnblocksBlockedSend` (Compute Cores, Impact: 12.7), `ProcessBulk` (Many-Argument Workhorses, Impact: 11.1), `TestBulkProcessStopsRunnerOnPanic` (State Mutators, Impact: 9.2)

### 10. `packages/grafana-ui/src/components/uPlot/plugins/TooltipPlugin2.tsx` (TYPESCRIPT) -> Cumulative Risk: **687.57**
- **Archetype:** `file_cluster_8` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.09)
- **Magnitude:** 465.88 | **LOC:** 796 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (94.3325%)
- **Heaviest Functions:** `onUp` (Compute Cores, Impact: 57.0), `onscroll` (Compute Cores, Impact: 33.0), `updatePlotVisible` (Compute Cores, Impact: 32.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `packages/grafana-prometheus/src/datasource.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 7052.8 | **LOC:** 1431 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (4.6375%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 34
* *State Mutation (weighted view):* 38
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 236`, `args: 159`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 28`
* *Architecture:* `io: 4`, `concurrency: 14`, `import: 10`
* *Defense:* `safety: 25`, `test: 277`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` datasource, escaping, language_provider, QueryCache, datasource, types, data, runtime...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `devenv/docker/blocks/auth/authentik/cert.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `devenv/docker/blocks/auth/authentik/key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `devenv/docker/blocks/elastic/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `devenv/docker/blocks/elasticstack/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `devenv/docker/blocks/grafana/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `devenv/docker/blocks/mimir_backend/nginx/.htpasswd` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `devenv/docker/blocks/mysql/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `devenv/docker/blocks/mysql_exporter/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `devenv/docker/blocks/mysql_tests/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `devenv/docker/blocks/postgres/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `devenv/docker/blocks/postgres_tests/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `devenv/docker/blocks/slow_proxy/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/services/ldap/testdata/invalid.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/services/ldap/testdata/parsable.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `public/app/features/scopes/dashboards/ScopesDashboardsService.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 4890.13 | **LOC:** 1547 | **CtrlFlow:** 3.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.1363%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Concurrency (weighted view):* 156
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 195`, `args: 98`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 13`
* *Architecture:* `io: 14`, `concurrency: 146`, `import: 7`
* *Defense:* `safety: 4`, `test: 173`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` ScopesApiClient, mockData, ScopesDashboardsService, types, runtime, history, rxjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `public/app/features/scopes/ScopesService.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 4115.77 | **LOC:** 937 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.2662%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 32 instances
* *Concurrency (weighted view):* 26
* *State Mutation (weighted view):* 119
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 71`, `args: 52`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 55`, `planned_debt: 3`
* *Architecture:* `io: 1`, `concurrency: 6`, `import: 6`
* *Defense:* `safety: 4`, `test: 88`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` ScopesService, ScopesDashboardsService, ScopesSelectorService, data, runtime, rxjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/grafana-runtime/src/services/pluginMeta/hooks.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3963.03 | **LOC:** 603 | **CtrlFlow:** 6.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (40.6084%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 83
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 234`, `args: 146`, `func_start: 39`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `concurrency: 78`, `import: 8`
* *Defense:* `safety: 1`, `test: 218`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` apps, hooks, panels, config.apps, config.panels, react
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/grafana-api-clients/src/clients/rtkq/legacy/endpoints.gen.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 3684.8 | **LOC:** 6196 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.0899%), Tech Debt (3.8703%)
**Top Internal Functions/Classes:**
  * `query` **(Compute Cores)** (Impact: 2244.4)
  * `query` **(Interface Declarations)** (Impact: 2.5)
  * `query` **(Interface Declarations)** (Impact: 2.4)
  * `query` **(I/O & Config Routines)** (Impact: 2.4)
  * `query` **(I/O & Config Routines)** (Impact: 2.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1434`, `structural_boundaries: 2111`, `args: 282`, `func_start: 282`
* *Risk/State:* `safety_bypasses: 25`, `planned_debt: 2`
* *Architecture:* `io: 10`, `api: 860`, `concurrency: 1`, `import: 6`
* *Defense:* `doc: 564`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ), baseAPI, ], providesTags: [, to: queryArg.to
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `public/app/plugins/panel/logstable/hooks/useOrganizeFields.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 3250.05 | **LOC:** 288 | **CtrlFlow:** 17.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (26.7287%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 24
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 74`, `args: 44`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 1`
* *Architecture:* `concurrency: 19`, `import: 10`
* *Defense:* `safety: 39`, `test: 47`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` constants, useExtractFields, useOrganizeFields, data, internal, ui, react, logFields...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/grafana-i18n/src/eslint/no-untranslated-strings/no-untranslated-strings.test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 3219.53 | **LOC:** 1195 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.5504%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 139`, `args: 95`, `func_start: 95`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 21`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `import: 6`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` $packageName, no-untranslated-strings.cjs, eslint
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `public/app/plugins/datasource/loki/LogContextProvider.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 3143.76 | **LOC:** 826 | **CtrlFlow:** 4.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 38 instances
* *Amplified Cascading Flux:* 17 instances
* *Concurrency (weighted view):* 271
* *State Mutation (weighted view):* 75
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 136`, `args: 64`, `func_start: 39`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 41`
* *Architecture:* `io: 14`, `concurrency: 81`, `import: 7`
* *Defense:* `safety: 8`, `test: 126`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` LanguageProvider, LogContextProvider, datasource, types, data, runtime, rxjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/dashboard/pkg/migration/conversion/v1_to_v2alpha1.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 2399.28 | **LOC:** 3139 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (40.6046%), Tech Debt (7.9538%)
**Top Internal Functions/Classes:**
  * `transformSingleQuery` **(Many-Argument Workhorses)** (Impact: 77.9)
  * `transformPanelQueries` **(Many-Argument Workhorses)** (Impact: 58.5)
    * *Intent:* // Panel helper functions
  * `buildAdhocVariable` **(Many-Argument Workhorses)** (Impact: 58.1)
    * *Intent:* // Adhoc Variable
  * `transformVariables` **(Many-Argument Workhorses)** (Impact: 55.6)
  * `convertToRowsLayout` **(Many-Argument Workhorses)** (Impact: 45.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 315 instances
* *State Mutation (weighted view):* 963
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 631`, `structural_boundaries: 658`, `args: 88`, `func_start: 88`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 333`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 9`, `import: 1`
* *Defense:* `safety: 10`, `doc: 253`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` adhoc, after, alphabeticalAsc, alphabeticalCaseInsensitiveAsc, alphabeticalCaseInsensitiveDesc, alphabeticalDesc, autoMigrateFrom, before...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `public/app/features/transformers/calculateHeatmap/heatmap.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2268.22 | **LOC:** 448 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.9173%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 118`, `args: 36`, `func_start: 3`
* *Risk/State:* None
* *Architecture:* `concurrency: 3`, `import: 3`
* *Defense:* `safety: 11`, `test: 62`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` heatmap, data, schema
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/grafana-runtime/src/services/pluginMeta/panels.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 2163.47 | **LOC:** 695 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (86.3307%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 11 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 164
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 205`, `args: 89`, `func_start: 50`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 21`
* *Architecture:* `io: 2`, `concurrency: 109`, `import: 8`
* *Defense:* `safety: 23`, `test: 213`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` logging, backendSrv, logging, panels, plugins, config.panels, v0alpha1Response, unstable
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `public/app/features/dashboard-scene/serialization/transformSaveModelToScene.ts` -> Churn: **57.14%** | Cog Load: 50.2153% | Debt: 9.5524%
- `public/app/features/dashboard-scene/scene/PanelMenuBehavior.test.tsx` -> Churn: **51.33%** | Cog Load: 100.0% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/grafana-prometheus/src/datasource.test.ts` -> **Ashley Harrison** (100.0% isolated ownership) | Magnitude: 7052.8
- `public/app/plugins/panel/logstable/hooks/useOrganizeFields.test.tsx` -> **Matias Chomicki** (100.0% isolated ownership) | Magnitude: 3250.05
- `apps/dashboard/pkg/migration/conversion/v1_to_v2alpha1.go` -> **Kristina Demeshchik** (100.0% isolated ownership) | Magnitude: 2399.28
- `apps/dashboard/pkg/migration/conversion/v2alpha1_to_v1.go` -> **Kristina Demeshchik** (100.0% isolated ownership) | Magnitude: 2012.68
- `public/app/features/canvas/runtime/element.tsx` -> **Ashley Harrison** (100.0% isolated ownership) | Magnitude: 1672.52

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `public/app/features/dashboard-scene/scene/DashboardScene.tsx` -> **Severity: 0.603** (Bridge: 0.0062 * Flux: 97.9827%)
- `public/app/features/dashboard-scene/panel-edit/PanelEditor.tsx` -> **Severity: 0.247** (Bridge: 0.0025 * Flux: 99.3847%)
- `public/app/features/dashboard-scene/pages/DashboardScenePageStateManager.ts` -> **Severity: 0.147** (Bridge: 0.0015 * Flux: 100.0%)
- `public/app/features/variables/query/operators.ts` -> **Severity: 0.113** (Bridge: 0.0011 * Flux: 99.7201%)
- `public/app/features/dashboard/state/DashboardModel.ts` -> **Severity: 0.088** (Bridge: 0.001 * Flux: 85.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/grafana-i18n/src/i18n.tsx` -> **Severity: 5.656** (Embedded: 0.1187 * Error Risk: 47.6572%)
- `public/app/core/services/context_srv.ts` -> **Severity: 3.779** (Embedded: 0.0455 * Error Risk: 83.0598%)
- `public/app/features/dashboard/state/DashboardModel.ts` -> **Severity: 3.197** (Embedded: 0.0345 * Error Risk: 92.6751%)
- `public/app/features/dashboard/state/PanelModel.ts` -> **Severity: 2.914** (Embedded: 0.0327 * Error Risk: 89.0082%)
- `public/app/features/dashboard/utils/panelMerge.ts` -> **Severity: 2.686** (Embedded: 0.0274 * Error Risk: 98.0903%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/grafana-i18n/src/i18n.tsx` -> **Severity: 2682.9** (Blast Radius: 26.829 * Doc Risk: 100.0%)
- `pkg/apimachinery/errutil/log.go` -> **Severity: 1253.389** (Blast Radius: 16.115 * Doc Risk: 77.7778%)
- `public/app/features/explore/spec/helper/assert.ts` -> **Severity: 1243.2** (Blast Radius: 12.432 * Doc Risk: 100.0%)
- `public/app/types/store.ts` -> **Severity: 406.0** (Blast Radius: 4.06 * Doc Risk: 100.0%)
- `public/app/types/unified-alerting-dto.ts` -> **Severity: 357.44** (Blast Radius: 4.468 * Doc Risk: 80.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
