# ARCHITECTURAL_BRIEF: grafana
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/grafana/grafana.git` |
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
- **Scope:** 14708 analyzed artifact(s), 2036722 LOC.
- **Load-bearing artifact:** `pkg/setting/setting.go` -- 743 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `pkg/server/wire.go` -- pulls in 202 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `devenv/docker/blocks/auth/authentik/key.pem` at magnitude 5000.0 (structural weight, not risk).
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
| Total Artifacts | 21473 |
| Analyzed Artifacts (Scanned) | 14708 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 6765 |
| Total LOC | 2036722 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 68.5% |
| Dominant Lang | GO |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7641 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0146 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 14.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 8.8398 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 1316 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 6707 | 851905 | 45.6% |
| GO | 4778 | 915601 | 32.5% |
| JSON | 1175 | 220708 | 8.0% |
| SQLITE | 593 | 8223 | 4.0% |
| YAML | 367 | 17540 | 2.5% |
| XML | 300 | 177 | 2.0% |
| MARKDOWN | 225 | 0 | 1.5% |
| POSTGRESQL | 147 | 2335 | 1.0% |
| JAVASCRIPT | 113 | 5390 | 0.8% |
| PLAINTEXT | 101 | 16 | 0.7% |
| SHELL | 82 | 3085 | 0.6% |
| MAKEFILE | 30 | 922 | 0.2% |
| DOCKERFILE | 27 | 374 | 0.2% |
| CSV | 27 | 1226 | 0.2% |
| HTML | 15 | 3996 | 0.1% |
| PROTO | 11 | 835 | 0.1% |
| CSS | 6 | 4359 | 0.0% |
| POWERSHELL | 1 | 8 | 0.0% |
| BMS | 1 | 1 | 0.0% |
| RUBY | 1 | 19 | 0.0% |
| ASSEMBLY | 1 | 2 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 14692 |
| unknown | unknown | 13 |
| utf-8 | bom | 3 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 19%, Callbacks & Closures Files 18%, Declarative / Non-Code 14%, Large Core Modules (2) 12%, Large Core Modules 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 14314 | 97.3% |
| Unknown | 13 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 312 | 2.1% |
| Static: Minified & Vendor Opaque Mass | 69 | 0.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 6765*

**Composition by Extension & Reason:**
- `.svg`: 1432x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Machine-Generated Source Code Signature: 16 LOC), 1x Excluded (Massive Static Asset Blob: 2672 LOC)
- `.go`: 424x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 54x Excluded (Machine-Generated Source Code Signature: 29 LOC), 46x Excluded (Machine-Generated Source Code Signature: 35 LOC)
- `.ts`: 1027x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Machine-Generated Source Code Signature: 8 LOC), 2x Excluded (Machine-Generated Source Code Signature: 65 LOC)
- `.tsx`: 941x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 49 exceeds 500 chars), 1x Excluded (Saturation: Line 61 exceeds 500 chars)
- `.md`: 767x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 4664 LOC)
- `.json`: 102x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 10x Excluded (Massive Static Asset Blob: 16576 LOC), 5x Excluded (Massive Static Asset Blob: 16488 LOC)
- `.cue`: 187x Excluded (Unsupported Extension: '.cue'), 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 143x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 15x Unsupported Format (.undeterminable)
- `.mdx`: 105x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 97x Excluded (Explicitly Denied Extension: '.png')
- `.txt`: 74x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.snap`: 38x Excluded (Unsupported Extension: '.snap'), 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 11x Unsupported Format (.snap)
- `.sum`: 37x Excluded (Unsupported Extension: '.sum'), 9x Unsupported Format (.sum), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mod`: 45x Unsupported Format (.mod), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 31x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 44 LOC), 1x Excluded (Saturation: Line 6 exceeds 500 chars)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 11.8 | 5.7 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 98.8 | 25.2 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 15.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 5.2 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 14.6 | 5.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 12.8 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 25.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.1 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 5.7 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 59.9 | 93.5 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 18924 | 3665 | 3 | `pkg/server/wire.go` |
| cleanup | 2580 | 829 | 0 | `pkg/tests/api/dashboards/api_dashboards_test.go` |
| guards | 55578 | 7339 | 10 | `public/app/features/canvas/runtime/element.tsx` |
| danger | 10170 | 2655 | 2 | `public/app/features/explore/state/query.test.ts` |
| concurrency | 36094 | 2731 | 5 | `e2e-playwright/dashboard-new-layouts/dashboard-group-panels.spec.ts` |
| connectivity | 63300 | 9641 | 10 | `pkg/setting/setting.go` |
| io | 10176 | 2544 | 1 | `public/app/plugins/datasource/cloudwatch/mocks/cloudwatch-logs-sql-test-data/multiLineFullQueryWithCaseClause.ts` |
| crypto | 2 | 2 | 0 | `.github/workflows/scripts/utils.mts` |
| ipc | 476 | 155 | 0 | `Makefile` |
| time | 4358 | 1223 | 0 | `pkg/tsdb/cloudwatch/models/cloudwatch_query_test.go` |
| serialization | 2543 | 899 | 0 | `pkg/services/ngalert/api/api_prometheus_test.go` |
| regex | 1930 | 696 | 0 | `public/app/features/templating/template_srv.test.ts` |
| events | 7578 | 1357 | 0 | `pkg/registry/apis/provisioning/jobs/sync/incremental_test.go` |
| tests | 140390 | 3706 | 26 | `pkg/tests/api/alerting/api_ruler_test.go` |
| docs | 36557 | 4462 | 6 | `public/app/api/clients/scope/v0alpha1/endpoints.gen.ts` |
| debt | 4521 | 1601 | 1 | `pkg/services/provisioning/stubs_test.go` |
| mutation | 222955 | 10506 | 41 | `apps/dashboard/pkg/migration/conversion/v1_to_v2alpha1.go` |
| dead_code | 17480 | 4914 | 4 | `pkg/plugins/manager/pluginfakes/fakes.go` |
| credential | 474 | 110 | 0 | `pkg/login/social/connectors/generic_oauth_test.go` |
| threat | 53 | 22 | 0 | `apps/dashboard/pkg/migration/conversion/testdata/input/v1beta1.bom-in-links.json` |
| ml_ai | 1242 | 350 | 0 | `public/app/features/dashboard-scene/scene/DashboardScene.test.tsx` |
| ui | 36692 | 3601 | 8 | `public/app/features/alerting/unified/components/import-to-gma/ImportToGMA.tsx` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `public/app/plugins/datasource/cloudwatch/mocks/cloudwatch-logs-sql-test-data/multiLineFullQueryWithCaseClause.ts` (Hits: 200)
- `public/app/plugins/datasource/cloudwatch/mocks/cloudwatch-logs-sql-test-data/multiLineFullQuery.ts` (Hits: 178)
- `public/app/features/provisioning/utils/treeUtils.test.ts` (Hits: 163)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **setting.go** (`pkg/setting/setting.go`) — 743 inbound connections
2. **context.go** (`pkg/apimachinery/identity/context.go`) — 459 inbound connections
3. **codeowners.go** (`pkg/services/featuremgmt/codeowners.go`) — 451 inbound connections
4. **user.go** (`pkg/services/user/user.go`) — 369 inbound connections
5. **accesscontrol.go** (`pkg/services/accesscontrol/accesscontrol.go`) — 343 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **wire.go** (`pkg/server/wire.go`) — 202 outbound dependencies
2. **http_server.go** (`pkg/api/http_server.go`) — 112 outbound dependencies
3. **routes.tsx** (`public/app/routes/routes.tsx`) — 79 outbound dependencies
4. **app.ts** (`public/app/app.ts`) — 73 outbound dependencies
5. **DashboardScene.tsx** (`public/app/features/dashboard-scene/scene/DashboardScene.tsx`) — 69 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `updateSchema` **(Many-Argument Workhorses)** (@ `public/app/features/dashboard/state/DashboardMigrator.ts`) -> Impact: **413.9** | LOC: 657
- `getStatementPosition` **(Defensive Guards)** (@ `public/app/plugins/datasource/cloudwatch/language/cloudwatch-logs-sql/completion/statementPosition.ts`) -> Impact: **356.6** | LOC: 344
- `TestRouteGetRuleStatuses` **(Many-Argument Workhorses)** (@ `pkg/services/ngalert/api/api_prometheus_test.go`) -> Impact: **267.1** | LOC: 3143
  * *Intent:* //nolint:gocyclo
- `prepConfig` **(Defensive Guards)** (@ `public/app/plugins/panel/heatmap/utils.ts`) -> Impact: **241.9** | LOC: 511
- `jsonDataToMetaJSONData` **(Many-Argument Workhorses)** (@ `apps/plugins/pkg/app/meta/converter.go`) -> Impact: **233.4** | LOC: 511
  * *Intent:* // jsonDataToMetaJSONData converts a plugins.JSONData to a pluginsv0alpha1.MetaJSONData. // nolint:gocyclo
- `getConfig` **(Many-Argument Workhorses)** (@ `public/app/plugins/panel/barchart/bars.ts`) -> Impact: **229.9** | LOC: 546
  * *Intent:* /** */
- `readDashboardIter` **(Many-Argument Workhorses)** (@ `pkg/services/store/kind/dashboard/dashboard.go`) -> Impact: **192.2** | LOC: 266
  * *Intent:* // nolint:gocyclo
- `initMoveable` **(Many-Argument Workhorses)** (@ `public/app/features/canvas/runtime/sceneAbleManagement.ts`) -> Impact: **187.9** | LOC: 358
  * *Intent:* // Main entry point for initializing / updating moveable and selecto configuration
- `sceneVariablesSetToSchemaV2Variables` **(Many-Argument Workhorses)** (@ `public/app/features/dashboard-scene/serialization/sceneVariablesSetToVariables.ts`) -> Impact: **171.6** | LOC: 312
- `authorize` **(Many-Argument Workhorses)** (@ `pkg/services/ngalert/api/authorization.go`) -> Impact: **169.8** | LOC: 556
  * *Intent:* //nolint:gocyclo

*Function archetypes referenced above:*
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `pkg/storage/unified/resource` | 71 | 11922.66 | 15.24% | 45.47% |
| `pkg/services/ldap/testdata` | 2 | 10000.0 | 0.0% | 0.0% |
| `pkg/api` | 89 | 8878.12 | 11.49% | 37.05% |
| `apps/dashboard/pkg/migration/conversion` | 35 | 8492.54 | 12.12% | 31.23% |
| `pkg/services/ngalert/api` | 60 | 7250.96 | 10.85% | 41.41% |
| `public/app/features/dashboard-scene/scene` | 66 | 6202.94 | 27.26% | 2.57% |
| `public/app/plugins/datasource/loki` | 61 | 6106.1 | 19.5% | 1.11% |
| `public/app/features/dashboard-scene/serialization` | 31 | 5299.26 | 23.89% | 6.93% |
| `devenv/docker/blocks/elasticstack` | 3 | 5031.2 | 0.0% | 0.0% |
| `devenv/docker/blocks/slow_proxy` | 4 | 5026.06 | 0.74% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `hack/update-codegen.sh` -> **100.0%** Exposure
- `public/app/features/dimensions/text.ts` -> **100.0%** Exposure
- `public/app/features/geo/editor/locationEditor.ts` -> **100.0%** Exposure
- `public/app/plugins/panel/xychart/config.ts` -> **100.0%** Exposure
- `apps/dashboard/pkg/apis/dashboard/v0alpha1/conversion.go` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `devenv/docker/loadtest/modules/client.js` -> **100.0%** Exposure
- `e2e/cypress/plugins/benchmark/formatting.js` -> **100.0%** Exposure
- `e2e/cypress/plugins/index.js` -> **100.0%** Exposure
- `public/app/plugins/panel/nodeGraph/forceLayout.js` -> **100.0%** Exposure
- `public/app/plugins/panel/nodeGraph/layeredLayout.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `pkg/plugins/manager/pluginfakes/fakes.go` -> **63** Orphaned Functions | **0** Duplicates
- `apps/provisioning/pkg/repository/git/repository_test.go` -> **56** Orphaned Functions | **0** Duplicates
- `pkg/services/ngalert/models/alert_rule.go` -> **41** Orphaned Functions | **0** Duplicates
- `pkg/apimachinery/identity/static.go` -> **34** Orphaned Functions | **0** Duplicates
- `pkg/storage/unified/resource/datastore_test.go` -> **33** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `.github/workflows/frontend-perf-tests.yaml` -> **100.0%** Exposure
- `pkg/api/http_server_test.go` -> **100.0%** Exposure
- `pkg/api/pluginproxy/token_provider_test.go` -> **100.0%** Exposure
- `pkg/infra/features/doc.go` -> **100.0%** Exposure
- `pkg/login/social/connectors/generic_oauth_test.go` -> **100.0%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `59` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `66683` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `devenv/docker/blocks/auth/authentik/key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.029
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `devenv/docker/blocks/elastic/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.029
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `devenv/docker/blocks/elasticstack/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.029
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `devenv/docker/blocks/grafana/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.029
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `devenv/docker/blocks/mimir_backend/nginx/.htpasswd` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.029
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `devenv/docker/blocks/mysql/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.029
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `devenv/docker/blocks/mysql_exporter/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.029
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `devenv/docker/blocks/mysql_tests/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.029
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `devenv/docker/blocks/postgres/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.029
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `devenv/docker/blocks/postgres_tests/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.029
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `devenv/docker/blocks/slow_proxy/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.029
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/services/ldap/testdata/invalid.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.029
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/services/ldap/testdata/parsable.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.029
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `public/app/features/scopes/dashboards/ScopesDashboardsService.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.908)
- **Top Global Matches:** file_cluster_10: 4.908, file_cluster_2: 6.43, file_cluster_13: 7.119
- **Magnitude:** 3994.64 | **LOC:** 1547 | **CtrlFlow:** 2.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.029; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (44.2%), Complexity Load (formerly Cognitive Load) (23.6%), Mutation Surface (formerly State Flux) (12.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Concurrency (weighted view):* 156
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 195`, `args: 98`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 13`
* *Architecture:* `io: 14`, `concurrency: 146`, `import: 7`
* *Defense:* `safety: 4`, `test: 173`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.029
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` ScopesApiClient, mockData, ScopesDashboardsService, types, runtime, history, rxjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `public/app/plugins/panel/logstable/hooks/useOrganizeFields.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.307)
- **Top Global Matches:** file_cluster_10: 6.307, file_cluster_12: 7.195, file_cluster_13: 8.537
- **Magnitude:** 2981.73 | **LOC:** 288 | **CtrlFlow:** 15.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.029; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.0%), Guard Balance (formerly Safety Score) (31.5%), Complexity Load (formerly Cognitive Load) (25.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (22.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 24
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 74`, `args: 44`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 1`
* *Architecture:* `concurrency: 19`, `import: 10`
* *Defense:* `safety: 39`, `test: 47`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.029
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` constants, useExtractFields, useOrganizeFields, data, internal, ui, react, logFields...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `public/app/features/scopes/ScopesService.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.184)
- **Top Global Matches:** file_cluster_10: 4.184, file_cluster_2: 5.498, file_cluster_13: 6.457
- **Magnitude:** 2672.55 | **LOC:** 937 | **CtrlFlow:** 3.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.029; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (65.5%), Concurrency Surface (formerly Concurrency) (64.5%), Guard Balance (formerly Safety Score) (48.2%), Complexity Load (formerly Cognitive Load) (6.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 26
* *State Mutation (weighted view):* 59
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 71`, `args: 52`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 55`, `planned_debt: 3`
* *Architecture:* `io: 1`, `concurrency: 6`, `import: 6`
* *Defense:* `safety: 4`, `test: 88`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.029
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` ScopesService, ScopesDashboardsService, ScopesSelectorService, data, runtime, rxjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/dashboard/pkg/migration/conversion/v1_to_v2alpha1.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.744)
- **Top Global Matches:** file_cluster_6: 5.744, file_cluster_4: 8.612, file_cluster_9: 16.382
- **Magnitude:** 2397.28 | **LOC:** 3139 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **16**; blast radius 0.063; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.5%), Complexity Load (formerly Cognitive Load) (40.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (22.1%)
- **Documentation Coverage:** 32.5843% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `transformSingleQuery` **(Many-Argument Workhorses)** (Impact: 77.9)
  * `transformPanelQueries` **(Many-Argument Workhorses)** (Impact: 58.5)
    * *Intent:* // Panel helper functions
  * `buildAdhocVariable` **(Many-Argument Workhorses)** (Impact: 58.1)
    * *Intent:* // Adhoc Variable
  * `transformVariables` **(Many-Argument Workhorses)** (Impact: 53.6)
  * `convertToRowsLayout` **(Many-Argument Workhorses)** (Impact: 45.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 315 instances
* *State Mutation (weighted view):* 963
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 630`, `structural_boundaries: 658`, `args: 88`, `func_start: 88`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 333`, `unreferenced_by_name: 1`
* *Architecture:* `api: 9`, `import: 1`
* *Defense:* `safety: 10`, `doc: 253`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.063
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.000569
  * `Imports (Out-Degree: 9):` context, json, fmt, types, dashboard, v1, v2alpha1, migration...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `apps/dashboard/pkg/migration/conversion/v2alpha1_to_v1.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.235)
- **Top Global Matches:** file_cluster_6: 5.235, file_cluster_4: 9.989, file_cluster_8: 14.896
- **Magnitude:** 2011.18 | **LOC:** 2417 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **7**; blast radius 0.045; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.7%), Complexity Load (formerly Cognitive Load) (39.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (22.1%)
- **Documentation Coverage:** 35.4839% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `processRowItem` **(Many-Argument Workhorses)** (Impact: 64.8)
    * *Intent:* // processRowItem converts a single V2 row to V1 panels. // Behavior depends on row configuration: /...
  * `processTabItem` **(Many-Argument Workhorses)** (Impact: 44.6)
    * *Intent:* // processTabItem converts a V2 tab to V1 panels. // Each tab becomes an expanded row panel (collaps...
  * `convertAdhocVariableToV1` **(Compute Cores)** (Impact: 43.8)
  * `convertAnnotationsToV1` **(Compute Cores)** (Impact: 43.8)
  * `convertPanelKindToV1` **(Many-Argument Workhorses)** (Impact: 41.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 336 instances
* *State Mutation (weighted view):* 1017
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 453`, `structural_boundaries: 550`, `args: 61`, `func_start: 61`
* *Risk/State:* `state_mutation: 345`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 25`, `doc: 160`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.045
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.000439
  * `Imports (Out-Degree: 5):` context, fmt, v1, v2alpha1, schemaversion, attribute, conversion
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/grafana-prometheus/src/datasource.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.935)
- **Top Global Matches:** file_cluster_10: 6.935, file_cluster_12: 7.029, file_cluster_5: 8.707
- **Magnitude:** 1856.66 | **LOC:** 1431 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.029; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (52.8%), Guard Balance (formerly Safety Score) (41.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (22.1%), Mutation Surface (formerly State Flux) (16.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Concurrency (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 236`, `args: 159`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 28`
* *Architecture:* `io: 4`, `concurrency: 14`, `import: 10`
* *Defense:* `safety: 25`, `test: 277`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.029
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` datasource, escaping, language_provider, QueryCache, datasource, types, data, runtime...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/setting/setting.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.549)
- **Top Global Matches:** file_cluster_4: 7.549, file_cluster_15: 7.595, file_cluster_16: 8.934
- **Magnitude:** 1674.86 | **LOC:** 2416 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **743** in-repo importer(s); it depends on **26**; blast radius 13.079; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (62.1%)
- **Documentation Coverage:** 79.7468% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseINIFile` **(Many-Argument Workhorses)** (Impact: 64.3)
    * *Intent:* // nolint:gocyclo
  * `readServerSettings` **(Compute Cores)** (Impact: 29.9)
  * `applyEnvVariableOverrides` **(Compute Cores)** (Impact: 25.5)
  * `readSecuritySettings` **(Many-Argument Workhorses)** (Impact: 24.9)
  * `readUserSettings` **(Many-Argument Workhorses)** (Impact: 23.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Amplified Cascading Flux:* 171 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 710
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 212`, `structural_boundaries: 220`, `args: 59`, `func_start: 59`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 6`, `state_mutation: 368`, `planned_debt: 3`, `unreferenced_by_name: 8`
* *Architecture:* `io: 1`, `api: 473`, `import: 1`
* *Defense:* `safety: 57`, `doc: 151`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 13.079
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.078901
  * `Imports (Out-Degree: 33):` bytes, json, errors, fmt, glob, awsds, azsettings, gtime...
  * `Imported By (In-Degree: 743):` (Excluded from Brief to save tokens)

### `pkg/services/dashboards/service/dashboard_service.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.841)
- **Top Global Matches:** file_cluster_4: 5.841, file_cluster_15: 9.014, file_cluster_9: 9.405
- **Magnitude:** 1509.54 | **LOC:** 2337 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **57**; blast radius 0.03; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (44.2%)
- **Documentation Coverage:** 81.5789% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `BuildSaveDashboardCommand` **(Many-Argument Workhorses)** (Impact: 66.0)
    * *Intent:* //nolint:gocyclo
  * `searchDashboardsThroughK8sRaw` **(Many-Argument Workhorses)** (Impact: 65.6)
  * `ValidateDashboardBeforeSave` **(Many-Argument Workhorses)** (Impact: 53.5)
  * `cleanupOrganizationK8sDashboards` **(Many-Argument Workhorses)** (Impact: 36.4)
    * *Intent:* // cleanupOrganizationK8sDashboards handles cleanup for a single organization's Kubernetes dashboard...
  * `unstructuredToLegacyDashboardWithUsers` **(Many-Argument Workhorses)** (Impact: 34.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 147 instances
* *Concurrency (weighted view):* 17
* *Memory Alloc (weighted view):* 21
* *State Mutation (weighted view):* 454
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 371`, `structural_boundaries: 333`, `args: 73`, `func_start: 73`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 160`, `planned_debt: 1`, `unreferenced_by_name: 26`
* *Architecture:* `api: 45`, `concurrency: 7`, `import: 1`
* *Defense:* `safety: 123`, `doc: 42`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 6.8e-05
  * `Imports (Out-Degree: 35):` context, json, errors, fmt, uuid, types, logging, gtime...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `public/app/features/canvas/runtime/element.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.437)
- **Top Global Matches:** file_cluster_6: 6.437, file_cluster_4: 12.481, file_cluster_8: 13.296
- **Magnitude:** 1391.92 | **LOC:** 1119 | **CtrlFlow:** 37.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **19** in-repo importer(s); it depends on **19**; blast radius 0.421; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (85.4%), Guard Balance (formerly Safety Score) (69.1%), Connectivity (formerly Api Exposure) (65.8%)
- **Documentation Coverage:** 86.0465% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setPlacementFromConstraint` **(Many-Argument Workhorses)** (Impact: 139.1)
  * `setPlacementFromConstraint2` **(Many-Argument Workhorses)** (Impact: 72.7)
  * `applyLayoutStylesToDiv` **(Defensive Guards)** (Impact: 68.8)
    * *Intent:* /** Use the configured options to update CSS style properties directly on the wrapper div **/
  * `applyLayoutStylesToDiv2` **(Defensive Guards)** (Impact: 68.4)
    * *Intent:* /** Use the configured options to update CSS style properties directly on the wrapper div **/
  * `updateData` **(Defensive Guards)** (Impact: 63.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 229 instances
* *State Mutation (weighted view):* 705
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 359`, `structural_boundaries: 155`, `args: 44`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 247`, `dead_code: 1`, `planned_debt: 5`, `fragile_debt: 2`
* *Architecture:* `api: 16`, `import: 20`
* *Defense:* `safety: 172`, `doc: 5`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.421
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.019981
  * `Imports (Out-Degree: 11):` analytics, utils, element, registry, frame, root, scene, data...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `pkg/storage/unified/search/bleve.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.065)
- **Top Global Matches:** file_cluster_4: 6.065, file_cluster_15: 9.49, file_cluster_16: 10.408
- **Magnitude:** 1295.44 | **LOC:** 2193 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **36**; blast radius 0.085; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.9%), Debt Markers (formerly Tech Debt) (27.1%)
- **Documentation Coverage:** 77.0115% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `BuildIndex` **(Many-Argument Workhorses)** (Impact: 140.8)
    * *Intent:* // BuildIndex builds an index from scratch or retrieves it from the filesystem. // If built successf...
  * `toBleveSearchRequest` **(Many-Argument Workhorses)** (Impact: 81.3)
    * *Intent:* // nolint:gocyclo
  * `hitsToTable` **(Many-Argument Workhorses)** (Impact: 61.0)
  * `requirementQuery` **(Compute Cores)** (Impact: 43.7)
    * *Intent:* // Convert a "requirement" into a bleve query
  * `Search` **(Many-Argument Workhorses)** (Impact: 41.0)
    * *Intent:* // Search implements resource.DocumentIndex.
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 121 instances
* *Concurrency (weighted view):* 45
* *State Mutation (weighted view):* 375
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 318`, `structural_boundaries: 283`, `args: 64`, `func_start: 64`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 133`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 1`, `unreferenced_by_name: 15`
* *Architecture:* `api: 36`, `concurrency: 10`, `import: 1`
* *Defense:* `safety: 56`, `doc: 117`, `sync_locks: 23`, `immutability_locks: 4`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.001054
  * `Imports (Out-Degree: 5):` context, binary, json, errors, fmt, semver, v2, keyword...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `pkg/tests/apis/provisioning/common/testing.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.954)
- **Top Global Matches:** file_cluster_12: 7.954, file_cluster_15: 8.149, file_cluster_4: 8.462
- **Magnitude:** 1260.98 | **LOC:** 2798 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **96** in-repo importer(s); it depends on **46**; blast radius 1.373; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (95.4%), Guard Balance (formerly Safety Score) (49.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (22.1%)
- **Documentation Coverage:** 25.4167% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `logRepositoryObject` **(Many-Argument Workhorses)** (Impact: 54.0)
    * *Intent:* // logRepositoryObject recursively logs repository file structure from API response
  * `AwaitJobs` **(Many-Argument Workhorses)** (Impact: 45.4)
  * `deleteAndWait` **(Many-Argument Workhorses)** (Impact: 42.6)
    * *Intent:* // deleteAndWait deletes all resources from a dynamic client and polls until // none remain. It retr...
  * `CreateRepo` **(Many-Argument Workhorses)** (Impact: 33.9)
  * `DebugState` **(Many-Argument Workhorses)** (Impact: 31.1)
    * *Intent:* // DebugState logs the current state of filesystem, repository, and Grafana resources for debugging
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 65 instances
* *High Risk Execution (weighted view):* 2
* *Concurrency (weighted view):* 6
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 220
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 246`, `structural_boundaries: 349`, `args: 131`, `func_start: 131`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 17`, `high_risk_execution: 6`, `state_mutation: 90`
* *Architecture:* `io: 4`, `api: 161`, `concurrency: 1`, `import: 1`
* *Defense:* `safety: 38`, `doc: 167`, `test: 214`, `immutability_locks: 3`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.373
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.006524
  * `Imports (Out-Degree: 15):` bytes, context, json, fmt, github, v0alpha1, v1, v2alpha1...
  * `Imported By (In-Degree: 96):` (Excluded from Brief to save tokens)

### `pkg/storage/unified/resource/storage_backend.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.909)
- **Top Global Matches:** file_cluster_4: 5.909, file_cluster_15: 10.936, file_cluster_12: 11.175
- **Magnitude:** 1245.88 | **LOC:** 2171 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **29**; blast radius 0.075; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (62.1%), Guard Balance (formerly Safety Score) (56.6%)
- **Documentation Coverage:** 78.8235% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ProcessBulk` **(Many-Argument Workhorses)** (Impact: 136.5)
    * *Intent:* //nolint:gocyclo
  * `WriteEvent` **(Many-Argument Workhorses)** (Impact: 68.9)
    * *Intent:* // WriteEvent writes a resource event (create/update/delete) to the storage backend. // //nolint:goc...
  * `garbageCollectGroupResource` **(Many-Argument Workhorses)** (Impact: 55.5)
    * *Intent:* // garbageCollectGroupResource scans batches of entries in the datastore for a given group+resource,...
  * `ListIterator` **(Many-Argument Workhorses)** (Impact: 35.7)
    * *Intent:* // ListIterator returns an iterator for listing resources.
  * `ListModifiedSince` **(Many-Argument Workhorses)** (Impact: 29.7)
    * *Intent:* // ListModifiedSince returns all resources that have changed since the given // resource version. If...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 124 instances
* *Concurrency (weighted view):* 38
* *State Mutation (weighted view):* 382
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 314`, `structural_boundaries: 288`, `args: 54`, `func_start: 54`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 134`, `planned_debt: 4`, `unreferenced_by_name: 9`
* *Architecture:* `io: 1`, `api: 60`, `concurrency: 8`, `import: 1`
* *Defense:* `safety: 83`, `doc: 102`, `sync_locks: 1`, `immutability_locks: 2`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.000663
  * `Imports (Out-Degree: 19):` bytes, cmp, context, json, errors, fmt, snowflake, inprocgrpc...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `public/app/core/components/Page/PageContents.tsx` (TYPESCRIPT) | Magnitude: 5.72 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 5, branch: 4, ui_framework: 2
- `public/app/core/components/AppChrome/ExtensionSidebar/ExtensionSidebar.tsx` (TYPESCRIPT) | Magnitude: 15.6 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 20, core_var_decl: 12, branch: 6
- `public/app/features/explore/ExploreQueryInspector.tsx` (TYPESCRIPT) | Magnitude: 39.58 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 86, structural_boundaries: 38, core_var_decl: 32, import: 20
- `public/app/features/alerting/unified/hooks/usePagination.ts` (TYPESCRIPT) | Magnitude: 10.58 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 13, ui_framework: 12, core_var_decl: 12
- `public/app/features/dashboard/components/SaveDashboard/SaveDashboardDrawer.tsx` (TYPESCRIPT) | Magnitude: 29.86 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 109, core_var_decl: 46, structural_boundaries: 30, design_camel_case: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `public/app/features/variables/adhoc/picker/AdHocFilter.test.tsx` (TYPESCRIPT) | Magnitude: 32.44 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 72, structural_boundaries: 26, test: 16, concurrency: 12
- `pkg/services/secrets/kvstore/test_helpers.go` (GO) | Magnitude: 88.92 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 67, structural_boundaries: 28, args: 16, func_start: 16
- `pkg/services/team/teamapi/api.go` (GO) | Magnitude: 12.24 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 82, structural_boundaries: 5, closures: 4, pointers: 4
- `pkg/storage/secret/encryption/encrypted_value_store_test.go` (GO) | Magnitude: 208.82 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 691, test: 158, structural_boundaries: 57, branch: 39
- `pkg/services/live/pipeline/pattern/pattern_test.go` (GO) | Magnitude: 10.6 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 31, structural_boundaries: 6, branch: 2, test: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `pkg/services/dashboardversion/dashvertest/fake.go` (GO) | Magnitude: 30.62 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 26, api: 14, structural_boundaries: 10, pointers: 7
- `pkg/services/frontend/index.html` (HTML) | Magnitude: 204.3 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 327, core_var_decl: 66, globals: 46, structural_boundaries: 43
- `.github/workflows/frontend-lint.yml` (YAML) | Magnitude: 55.32 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 307, branch: 39, import: 37, structural_boundaries: 32
- `e2e-playwright/plugin-e2e/plugin-e2e-api-tests/as-admin-user/lokiEditor.spec.ts` (TYPESCRIPT) | Magnitude: 52.98 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 65, structural_boundaries: 58, concurrency: 49, test: 16
- `public/app/features/dashboard-scene/settings/annotations/AnnotationSetEditableElement.tsx` (TYPESCRIPT) | Magnitude: 15.82 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 22, import: 9, api: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `public/app/features/expressions/components/SqlExpressions/GenAI/GenAISQLSuggestionsButton.tsx` (TYPESCRIPT) | Magnitude: 33.58 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 78, structural_boundaries: 25, core_var_decl: 21, branch: 14
- `public/app/types/dashboard.ts` (TYPESCRIPT) | Magnitude: 22.32 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 97, structural_boundaries: 49, branch: 43, api: 18
- `public/app/features/dashboard/components/GenAI/GenAIDashboardChangesButton.tsx` (TYPESCRIPT) | Magnitude: 23.4 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 74, structural_boundaries: 17, core_var_decl: 14, import: 6
- `pkg/services/publicdashboards/service/service_test.go` (GO) | Magnitude: 257.34 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 1169, indent_spaces: 252, pointers: 184, test: 170
- `public/app/features/library-panels/components/LibraryPanelsSearch/LibraryPanelsSearch.test.tsx` (TYPESCRIPT) | Magnitude: 47.1 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 299, structural_boundaries: 104, test: 54, args: 38

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `apps/dashboard/pkg/migration/schemaversion/v36_test.go` (GO) | Magnitude: 2.74 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 2, indent_tabs: 2, args: 1, func_start: 1
- `pkg/services/ssosettings/api/api.go` (GO) | Magnitude: 97.5 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 152, structural_boundaries: 55, api: 36, decorators: 21
- `public/app/types/intl.d.ts` (TYPESCRIPT) | Magnitude: 0.76 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 6, core_var_decl: 2, design_pascal_case: 2
- `pkg/apis/iam/v0alpha1/types_display.go` (GO) | Magnitude: 14.6 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 14, api: 13, decorators: 11, structural_boundaries: 10
- `public/app/features/variables/switch/reducer.ts` (TYPESCRIPT) | Magnitude: 18.64 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 9, import: 4, api: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `scripts/cleanup-husky.sh` (SHELL) | Magnitude: 3.16 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 40, structural_boundaries: 30, branch: 9, safety_bypasses: 8
- `public/app/core/utils/object.ts` (TYPESCRIPT) | Magnitude: 36.88 | Delta: **0.143** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 21, branch: 10, structural_boundaries: 9, safety_bypasses: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `pkg/services/pluginsintegration/pluginassets/pluginassets.go` (GO) | Magnitude: 10.5 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 14, structural_boundaries: 7, api: 4, args: 3
- `pkg/services/live/features/watch_test.go` (GO) | Magnitude: 13.52 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 54, structural_boundaries: 8, test: 5, branch: 4
- `public/app/plugins/datasource/loki/makeTableFrames.ts` (TYPESCRIPT) | Magnitude: 39.32 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 25, core_var_decl: 15, args: 11
- `apps/provisioning/pkg/quotas/tracker_test.go` (GO) | Magnitude: 76.96 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 106, test: 21, doc: 11, structural_boundaries: 10
- `pkg/services/dashboardimport/api/api_test.go` (GO) | Magnitude: 59.54 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 408, test: 95, structural_boundaries: 58, pointers: 38

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `public/app/features/playlist/PlaylistSrv.ts` (TYPESCRIPT) | Magnitude: 106.2 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 101, structural_boundaries: 30, branch: 19, state_mutation: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `apps/provisioning/pkg/apis/provisioning/v0alpha1/classic.go` (GO) | Magnitude: 19.16 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: api: 5, doc: 5, globals: 4, indent_tabs: 4
- `pkg/services/ngalert/models/constants.go` (GO) | Magnitude: 16.6 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: doc: 5, api: 2, state_mutation: 2, globals: 2
- `pkg/registry/apps/wireset.go` (GO) | Magnitude: 16.68 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 29, structural_boundaries: 2, api: 1, globals: 1
- `pkg/registry/apis/secret/contracts/decrypt.go` (GO) | Magnitude: 24.4 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 10, structural_boundaries: 6, api: 6, globals: 4
- `packages/grafana-prometheus/src/index.ts` (TYPESCRIPT) | Magnitude: 70.4 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 70, api: 54, import: 54, indent_spaces: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `pkg/tests/apis/provisioning/jobs/migratejob_test.go` (GO) | Magnitude: 40.64 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 178, test: 43, doc: 23, core_var_decl: 12
- `pkg/infra/fs/exists.go` (GO) | Magnitude: 6.08 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 9, structural_boundaries: 5, branch: 2, args: 1
- `pkg/tsdb/loki/types.go` (GO) | Magnitude: 51.86 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: api: 28, indent_tabs: 27, core_var_decl: 12, design_pascal_case: 12
- `pkg/tests/apis/provisioning/foldermetadata/fixfoldermetadata_test.go` (GO) | Magnitude: 38.2 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 139, test: 27, doc: 15, structural_boundaries: 14
- `public/app/features/alerting/unified/triage/constants.ts` (TYPESCRIPT) | Magnitude: 28.04 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 17, api: 12, core_var_decl: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `public/app/plugins/datasource/azuremonitor/components/LogsQueryBuilder/FilterSection.tsx` (TYPESCRIPT) | Magnitude: 136.28 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 228, structural_boundaries: 65, branch: 59, core_var_decl: 52
- `pkg/expr/mathexp/parse/lex.go` (GO) | Magnitude: 245.58 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 245, branch: 81, structural_boundaries: 57, encapsulation: 29
- `pkg/tsdb/opentsdb/utils.go` (GO) | Magnitude: 251.6 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 236, branch: 57, structural_boundaries: 42, state_mutation: 41
- `pkg/setting/setting.go` (GO) | Magnitude: 1674.86 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 1643, api: 473, state_mutation: 368, structural_boundaries: 220
- `public/app/plugins/datasource/grafana-testdata-datasource/datasource.ts` (TYPESCRIPT) | Magnitude: 353.56 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 440, structural_boundaries: 97, branch: 77, core_var_decl: 49

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `public/test/core/thunk/thunkTester.ts` (TYPESCRIPT) | Magnitude: 35.44 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 21, core_var_decl: 9, design_camel_case: 6
- `public/app/features/explore/state/time.test.ts` (TYPESCRIPT) | Magnitude: 4.28 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 19, args: 10, closures: 10
- `public/app/plugins/datasource/opentsdb/types.ts` (TYPESCRIPT) | Magnitude: 0.99 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 29, branch: 22, structural_boundaries: 14, api: 4
- `public/app/features/dashboard-scene/edit-pane/add-new/AddFilters.tsx` (TYPESCRIPT) | Magnitude: 8.66 | Delta: **0.059** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 16, import: 8, core_var_decl: 8
- `packages/grafana-prometheus/src/querybuilder/shared/OperationHeader.tsx` (TYPESCRIPT) | Magnitude: 20.06 | Delta: **0.06** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 100, structural_boundaries: 32, core_var_decl: 29, design_snake_case: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `public/app/features/alerting/unified/notifications/NotificationDetailAlerts.tsx` (TYPESCRIPT) | Magnitude: 112.06 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 243, core_var_decl: 70, structural_boundaries: 49, ui_framework: 49
- `pkg/services/authn/authnimpl/sync/rbac_sync.go` (GO) | Magnitude: 159.24 | Delta: **0.066** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 224, structural_boundaries: 57, branch: 47, state_mutation: 14
- `public/app/features/dashboard-scene/serialization/layoutSerializers/DefaultGridLayoutSerializer.ts` (TYPESCRIPT) | Magnitude: 190.98 | Delta: **0.11** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 179, branch: 53, structural_boundaries: 39, core_var_decl: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `pkg/setting/setting_smtp_test.go` (GO) | Magnitude: 23.5 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 68, test: 21, state_mutation: 11, core_var_decl: 6
- `pkg/services/authz/zanzana/store/migration/migrator_test.go` (GO) | Magnitude: 17.92 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_tabs: 49, test: 17, safety_bypasses: 10, state_mutation: 10
- `public/app/features/alerting/unified/enterprise-components/rule-view-page/navigation.test.ts` (TYPESCRIPT) | Magnitude: 5.52 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 47, structural_boundaries: 26, args: 20, test: 19
- `e2e-playwright/dashboard-new-layouts/dashboards-edit-custom-variables.spec.ts` (TYPESCRIPT) | Magnitude: 206.56 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 162, structural_boundaries: 77, concurrency: 67, core_var_decl: 29
- `public/app/core/utils/isShallowEqual.ts` (TYPESCRIPT) | Magnitude: 22.62 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 19, branch: 7, structural_boundaries: 6, core_var_decl: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `public/app/features/dashboard-scene/panel-edit/PanelEditNext/QueryEditor/Header/ExperimentalFeedbackButton.tsx` (TYPESCRIPT) | Magnitude: 13.24 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 69, core_var_decl: 20, structural_boundaries: 14, design_snake_case: 12
- `public/app/plugins/datasource/tempo/graphTransform.ts` (TYPESCRIPT) | Magnitude: 135.86 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 202, structural_boundaries: 52, branch: 36, core_var_decl: 33
- `public/app/features/alerting/unified/components/contact-points/EditMessageTemplate.tsx` (TYPESCRIPT) | Magnitude: 17.58 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 54, structural_boundaries: 22, import: 14, core_var_decl: 13
- `pkg/tsdb/influxdb/influxdb.go` (GO) | Magnitude: 56.92 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 97, structural_boundaries: 24, branch: 16, safety: 6
- `public/app/features/commandPalette/scopes/ScopesRow.tsx` (TYPESCRIPT) | Magnitude: 21.72 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 69, structural_boundaries: 23, core_var_decl: 16, branch: 9

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `public/app/features/dashboard-scene/scene/PanelMenuBehavior.test.tsx` -> Churn: **51.33%** | Cog Load: 100.0% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `public/app/plugins/panel/logstable/hooks/useOrganizeFields.test.tsx` -> **Matias Chomicki** (100.0% isolated ownership) | Magnitude: 2981.73
- `apps/dashboard/pkg/migration/conversion/v1_to_v2alpha1.go` -> **Kristina Demeshchik** (100.0% isolated ownership) | Magnitude: 2397.28
- `apps/dashboard/pkg/migration/conversion/v2alpha1_to_v1.go` -> **Kristina Demeshchik** (100.0% isolated ownership) | Magnitude: 2011.18
- `packages/grafana-prometheus/src/datasource.test.ts` -> **Ashley Harrison** (100.0% isolated ownership) | Magnitude: 1856.66
- `public/app/features/canvas/runtime/element.tsx` -> **Ashley Harrison** (100.0% isolated ownership) | Magnitude: 1391.92

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `pkg/setting/setting.go` -> **Severity: 5.169** (Embedded: 0.0789 * Error Risk: 65.5063%)
- `pkg/setting/setting_azure.go` -> **Severity: 4.519** (Embedded: 0.0536 * Error Risk: 84.2374%)
- `public/app/core/services/context_srv.ts` -> **Severity: 4.295** (Embedded: 0.0691 * Error Risk: 62.1566%)
- `pkg/apimachinery/identity/context.go` -> **Severity: 4.221** (Embedded: 0.0798 * Error Risk: 52.9018%)
- `pkg/apimachinery/utils/blob.go` -> **Severity: 3.767** (Embedded: 0.0546 * Error Risk: 68.9974%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `pkg/setting/setting.go` -> **Severity: 1043.008** (Blast Radius: 13.079 * Doc Risk: 79.7468%)
- `pkg/setting/provider.go` -> **Severity: 584.4** (Blast Radius: 5.844 * Doc Risk: 100.0%)
- `public/app/types/store.ts` -> **Severity: 479.7** (Blast Radius: 4.797 * Doc Risk: 100.0%)
- `public/app/types/unified-alerting.ts` -> **Severity: 471.9** (Blast Radius: 4.719 * Doc Risk: 100.0%)
- `public/app/types/unified-alerting-dto.ts` -> **Severity: 460.08** (Blast Radius: 5.751 * Doc Risk: 80.0%)

- **Mainframe skeleton completeness:** n/a (no channel has facts) (mean channel ratio; channel table in the audit report, section 7). Top missing inputs: none.

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 1771 literal sites + 22 sites through wrappers = 1793
- **`panics_and_aborts`:** 1673 literal sites + 28 sites through wrappers = 1701

- `throwError` (function, panics_and_aborts, primitive): 20 call sites in 13 files -- `public/app/core/history/RichHistoryLocalStorage.ts`
- `LOG` (function, debug_prints, primitive): 5 call sites in 1 files -- `.github/actions/changelog/index.js`
- `updateNavModel` (function, debug_prints, primitive): 5 call sites in 3 files -- `public/app/features/dashboard-scene/pages/utils.ts`
- `die` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `kinds/gen.go`
- `notifyWithError` (function, debug_prints, primitive): 3 call sites in 1 files -- `public/app/features/query/state/DashboardQueryRunner/utils.ts`
- `writeVariablesFile` (function, debug_prints, primitive): 3 call sites in 1 files -- `scripts/cli/generateSassVariableFiles.ts`
- `writeVariablesFile` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `scripts/cli/generateSassVariableFiles.ts`
- `printUsage` (function, debug_prints, primitive): 2 call sites in 1 files -- `scripts/go-workspace/main.go`
- `getExceptionNav` (function, debug_prints, primitive): 1 call sites in 1 files -- `public/app/core/navigation/errorModels.ts`
- `getServerStats` (function, debug_prints, primitive): 1 call sites in 1 files -- `public/app/features/admin/state/apis.tsx`
- `newAlwaysPanicMiddleware` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `pkg/services/pluginsintegration/clientmiddleware/tracing_middleware_test.go`
- `openCoverageReport` (function, debug_prints, primitive): 1 call sites in 1 files -- `jest.config.codeowner.js`
*(+1 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 222057 call pairs -- scoped 24.0%, unique 2.4%, ambiguous 35.6%, external 38.0%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| go | 156037 | 23.0% | 3.4% | 43.4% | 30.2% |
| typescript | 64808 | 26.7% | 0.0% | 17.4% | 55.9% |
| javascript | 744 | 15.9% | 0.0% | 10.3% | 73.8% |
| shell | 389 | 10.8% | 0.5% | 0.0% | 88.7% |
| html | 61 | 11.5% | 0.0% | 0.0% | 88.5% |
| ruby | 13 | 7.7% | 0.0% | 0.0% | 92.3% |
| postgresql | 5 | 0.0% | 0.0% | 0.0% | 100.0% |

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
