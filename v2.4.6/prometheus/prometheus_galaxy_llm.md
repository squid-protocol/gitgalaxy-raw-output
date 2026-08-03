# ARCHITECTURAL_BRIEF: prometheus
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/prometheus` |
| **Timestamp** | `2026-08-03T21:18:55.797419+00:00` |
| **Scan Duration** | `4.21s` |
| **Git Branch** | `main` |
| **Git Commit** | `cb3382314d63ed457279c9582cd6db63d0a06631` |
| **Git Remote** | `https://github.com/prometheus/prometheus` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 688 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are analyzing software architecture through the lens of GitGalaxy Static Application Security Testing (SAST). GitGalaxy translates the non-visual architecture of repositories into measurable technical metrics.
> 
> **CORE DIRECTIVES:**
> 1. **Measure Risk, Not Quality:** Do not judge. We measure Risk Exposure (e.g., Cognitive Load Exposure). Frame all insights as blameless, objective observations. High risk highlights where the architecture might be drifting into fragile territory, not developer incompetence.
> 2. **The Physical Reality Rule:** Base your analysis strictly on the provided Structural Signatures (regex hit counts). Do not hallucinate meaning.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`.
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
| Total Artifacts | 1591 |
| Analyzed Artifacts (Scanned) | 1125 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 466 |
| Total LOC | 123000 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 70.7% |
| Dominant Lang | GO |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6139 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1918 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.15 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 77 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| GO | 416 | 74055 | 37.0% |
| YAML | 307 | 3009 | 27.3% |
| TYPESCRIPT | 241 | 38692 | 21.4% |
| JSON | 47 | 4667 | 4.2% |
| CSS | 29 | 1171 | 2.6% |
| MARKDOWN | 26 | 0 | 2.3% |
| PLAINTEXT | 22 | 10 | 2.0% |
| SHELL | 13 | 579 | 1.2% |
| JAVASCRIPT | 9 | 254 | 0.8% |
| MAKEFILE | 4 | 219 | 0.4% |
| XML | 4 | 0 | 0.4% |
| PROTO | 4 | 273 | 0.4% |
| HTML | 2 | 42 | 0.2% |
| DOCKERFILE | 1 | 29 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.973`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 790 | 70.2% |
| file_cluster_13 | 132 | 11.7% |
| file_cluster_0 | 42 | 3.7% |
| file_cluster_2 | 33 | 2.9% |
| file_cluster_4 | 27 | 2.4% |
| file_cluster_17 | 18 | 1.6% |
| Unknown | 10 | 0.9% |
| file_cluster_15 | 9 | 0.8% |
| file_cluster_7 | 9 | 0.8% |
| file_cluster_12 | 7 | 0.6% |
| file_cluster_16 | 5 | 0.4% |
| file_cluster_11 | 2 | 0.2% |
| file_cluster_6 | 2 | 0.2% |
| file_cluster_9 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 38 | 3.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 466*

**Composition by Extension & Reason:**
- `.go`: 263x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 400 LOC), 1x Excluded (Machine-Generated Source Code Signature: 905 LOC)
- `.md`: 42x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 3284 LOC)
- `.yml`: 28x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 7x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Monolithic Amalgamation: 40012 LOC exceeds safe regex boundaries)
- `no_extension`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded (Binary Format Detected), 2x Unsupported Format (.undeterminable)
- `.test`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.prom`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Unsupported Extension: '.prom')
- `.js`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 23 exceeds 500 chars)
- `.mod`: 5x Unsupported Format (.mod)
- `.sum`: 3x Excluded (Unsupported Extension: '.sum'), 2x Unsupported Format (.sum)
- `.json`: 1x Excluded (Static Asset Blob without Intent: 2334 LOC), 1x Excluded (Massive Static Asset Blob: 20001 LOC), 1x Excluded (Massive Static Asset Blob: 9760 LOC)
- `.libsonnet`: 4x Excluded (Unsupported Extension: '.libsonnet')
- `.yaml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 4454 LOC), 1x Excluded (Massive Static Asset Blob: 4505 LOC)
- `.sh`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 46 LOC)
- `.snap`: 3x Unsupported Format (.snap)
- `.png`: 2x Excluded (Explicitly Denied Extension: '.png')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 17.1 | 6.1 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 33.5 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 20.3 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 16.5 | 1.9 | 80.0 |
| API Exposure | 0.0 | 18.2 | 2.5 | 0.4 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 5.3 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 35.1 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 38.2 | 0.5 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 76.4 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 31.4 | 0.8 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 6.6 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 41.0 | 30.6 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 4.9 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 3.5 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `web/ui/mantine-ui/src/promql/functionDocs.tsx` (Hits: 191)
- `web/ui/react-app/src/pages/targets/__testdata__/testdata.ts` (Hits: 69)
- `Makefile` (Hits: 38)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **errors.go** (`storage/errors.go`) — 142 inbound connections
2. **strconv.go** (`util/strutil/strconv.go`) — 81 inbound connections
3. **discovery.go** (`discovery/discovery.go`) — 73 inbound connections
4. **sync.go** (`tsdb/fileutil/sync.go`) — 69 inbound connections
5. **targetgroup.go** (`discovery/targetgroup/targetgroup.go`) — 65 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **openapi_examples.go** (`web/api/v1/openapi_examples.go`) — 154 outbound dependencies
2. **main.go** (`cmd/prometheus/main.go`) — 118 outbound dependencies
3. **functions.go** (`promql/functions.go`) — 99 outbound dependencies
4. **functions.go** (`promql/parser/functions.go`) — 83 outbound dependencies
5. **web.go** (`web/web.go`) — 70 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `rangeEval` (@ `promql/engine.go`) -> Impact: **2646.2** | LOC: 1913
- `Next` (@ `model/histogram/float_histogram.go`) -> Impact: **1244.5** | LOC: 740
- `explanationText` (@ `web/ui/mantine-ui/src/pages/query/ExplainViews/BinaryExpr/VectorVector.tsx`) -> Impact: **969.0** | LOC: 597
- `escapeHTML` (@ `web/ui/mantine-ui/src/pages/query/uPlotChartHelpers.ts`) -> Impact: **770.5** | LOC: 383
- `analyzeCompletion` (@ `web/ui/module/codemirror-promql/src/complete/hybrid.ts`) -> Impact: **630.4** | LOC: 247
- `getOOOSeriesChunks` (@ `tsdb/ooo_head_read.go`) -> Impact: **505.7** | LOC: 501
  * *Intent:* // lastGarbageCollectedMmapRef gives the last mmap chunk that may be being garbage collected and so // any chunk at or before this ref will not be con...
- `rules` (@ `web/api/v1/api.go`) -> Impact: **503.0** | LOC: 360
- `refresh` (@ `discovery/aws/rds.go`) -> Impact: **457.5** | LOC: 528
- `write` (@ `storage/remote/write_handler.go`) -> Impact: **425.1** | LOC: 326
- `main` (@ `cmd/prometheus/main.go`) -> Impact: **407.1** | LOC: 1317

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `explanationText` (@ `web/ui/mantine-ui/src/pages/query/ExplainViews/BinaryExpr/VectorVector.tsx`) -> **O(2^N) [Recursive]**
- `setExpandedLabels` (@ `web/ui/mantine-ui/src/pages/query/MetricsExplorer/LabelsExplorer.tsx`) -> **O(2^N) [Recursive]**
- `promQL` (@ `web/ui/mantine-ui/src/pages/query/HistoryCompleteStrategy.tsx`) -> **O(2^N) [Recursive]**
- `escapeHTML` (@ `web/ui/mantine-ui/src/pages/query/uPlotChartHelpers.ts`) -> **O(2^N) [Recursive]**
- `dispatch` (@ `web/ui/mantine-ui/src/pages/query/QueryPanel.tsx`) -> **O(2^N) [Recursive]**
- `onChangeTime` (@ `web/ui/mantine-ui/src/pages/query/TimeInput.tsx`) -> **O(2^N) [Recursive]**
- `describe` (@ `web/ui/react-app/src/pages/graph/DataTable.test.tsx`) -> **O(2^N) [Recursive]**
- `describe` (@ `web/ui/react-app/src/pages/graph/Graph.test.tsx`) -> **O(2^N) [Recursive]**
- `onChangeDisplayMode` (@ `web/ui/react-app/src/pages/graph/GraphControls.tsx`) -> **O(2^N) [Recursive]**
- `describe` (@ `web/ui/react-app/src/pages/graph/SeriesName.test.tsx`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `rangeEval` (@ `promql/engine.go`) -> DB Complexity: **521**
- `main` (@ `cmd/prometheus/main.go`) -> DB Complexity: **197**
- `expandIntSpansAndBuckets` (@ `tsdb/chunkenc/histogram.go`) -> DB Complexity: **173**
  * *Intent:* // appendable returns whether the chunk can be appended to, and if so whether // 1. Any recoding needs to happen to the chunk using the provided forwa...
- `Next` (@ `model/histogram/float_histogram.go`) -> DB Complexity: **172**
- `refresh` (@ `discovery/aws/rds.go`) -> DB Complexity: **166**
- `main` (@ `cmd/promtool/main.go`) -> DB Complexity: **158**
- `loadMmappedChunks` (@ `tsdb/head.go`) -> DB Complexity: **125**
- `TestExpression` (@ `model/histogram/float_histogram.go`) -> DB Complexity: **111**
  * *Intent:* // TestExpression returns the string representation of this histogram as it is used in the internal PromQL testing // framework as well as in promtool...
- `sendMetadataWithBackoff` (@ `storage/remote/queue_manager.go`) -> DB Complexity: **76**
- `UnmarshalYAML` (@ `discovery/aws/aws.go`) -> DB Complexity: **74**
  * *Intent:* // UnmarshalYAML implements the yaml.Unmarshaler interface for SDConfig.

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `scrape/testdata` | 9 | 40000.0 | 0.0% | 0.0% |
| `tsdb` | 22 | 11065.32 | 33.6% | 46.7% |
| `promql` | 8 | 9423.98 | 41.77% | 42.16% |
| `web/ui/react-app` | 3 | 5017.78 | 3.08% | 0.0% |
| `tracing/testdata` | 1 | 5000.0 | 0.0% | 0.0% |
| `storage/remote` | 16 | 4894.6 | 34.09% | 46.27% |
| `discovery/aws` | 14 | 4813.78 | 25.4% | 63.94% |
| `web/api/v1` | 10 | 4272.24 | 18.92% | 58.82% |
| `cmd/promtool` | 10 | 4168.7 | 44.31% | 26.8% |
| `promql/parser` | 9 | 3981.14 | 30.45% | 52.44% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `discovery/discoverer_metrics_noop.go` -> **100.0%** Exposure
- `discovery/metrics_k8s_client.go` -> **100.0%** Exposure
- `promql/parser/ast.go` -> **100.0%** Exposure
- `promql/parser/prettier.go` -> **100.0%** Exposure
- `promql/value.go` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `cmd/prometheus/main.go` -> **100.0%** Exposure
- `cmd/promtool/analyze.go` -> **100.0%** Exposure
- `cmd/promtool/archive.go` -> **100.0%** Exposure
- `cmd/promtool/backfill.go` -> **100.0%** Exposure
- `cmd/promtool/debug.go` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `web/api/testhelpers/mocks.go` -> **24** Orphaned Functions | **46** Duplicates
- `storage/remote/codec.go` -> **12** Orphaned Functions | **32** Duplicates
- `promql/parser/ast.go` -> **0** Orphaned Functions | **43** Duplicates
- `web/api/v1/openapi_examples.go` -> **38** Orphaned Functions | **0** Duplicates
- `web/api/v1/openapi_paths.go` -> **31** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`discovery/aws/rds.go`** -> AI Confidence: **99.48%**
2. **`discovery/moby/tasks.go`** -> AI Confidence: **99.48%**
3. **`web/ui/mantine-ui/src/promql/tools/gen_functions_docs/main.go`** -> AI Confidence: **99.48%**
4. **`cmd/promtool/backfill.go`** -> AI Confidence: **99.39%**
5. **`cmd/promtool/main.go`** -> AI Confidence: **99.39%**
6. **`discovery/aws/aws.go`** -> AI Confidence: **99.39%**
7. **`discovery/aws/elasticache.go`** -> AI Confidence: **99.39%**
8. **`documentation/examples/remote_storage/example_write_adapter/server.go`** -> AI Confidence: **99.39%**
9. **`promql/engine.go`** -> AI Confidence: **99.39%**
10. **`promql/parser/printer.go`** -> AI Confidence: **99.39%**
11. **`scrape/scrape_append_v2.go`** -> AI Confidence: **99.39%**
12. **`storage/remote/write_handler.go`** -> AI Confidence: **99.39%**
13. **`web/federate.go`** -> AI Confidence: **99.39%**
14. **`model/textparse/protobufparse.go`** -> AI Confidence: **99.35%**
15. **`tsdb/head_wal.go`** -> AI Confidence: **99.35%**
16. **`storage/remote/otlptranslator/prometheusremotewrite/histograms.go`** -> AI Confidence: **99.34%**
17. **`promql/parser/features.go`** -> AI Confidence: **99.32%**
18. **`cmd/prometheus/main.go`** -> AI Confidence: **99.31%**
19. **`cmd/promtool/analyze.go`** -> AI Confidence: **99.31%**
20. **`cmd/promtool/metrics.go`** -> AI Confidence: **99.31%**
21. **`cmd/promtool/query.go`** -> AI Confidence: **99.31%**
22. **`cmd/promtool/rules.go`** -> AI Confidence: **99.31%**
23. **`cmd/promtool/sd.go`** -> AI Confidence: **99.31%**
24. **`cmd/promtool/tsdb.go`** -> AI Confidence: **99.31%**
25. **`config/config.go`** -> AI Confidence: **99.31%**
26. **`config/reload.go`** -> AI Confidence: **99.31%**
27. **`discovery/aws/ec2.go`** -> AI Confidence: **99.31%**
28. **`discovery/aws/ecs.go`** -> AI Confidence: **99.31%**
29. **`discovery/aws/lightsail.go`** -> AI Confidence: **99.31%**
30. **`discovery/aws/msk.go`** -> AI Confidence: **99.31%**
31. **`discovery/azure/azure.go`** -> AI Confidence: **99.31%**
32. **`discovery/consul/consul.go`** -> AI Confidence: **99.31%**
33. **`discovery/dns/dns.go`** -> AI Confidence: **99.31%**
34. **`discovery/eureka/eureka.go`** -> AI Confidence: **99.31%**
35. **`discovery/file/file.go`** -> AI Confidence: **99.31%**
36. **`discovery/gce/gce.go`** -> AI Confidence: **99.31%**
37. **`discovery/hetzner/hcloud.go`** -> AI Confidence: **99.31%**
38. **`discovery/ionos/server.go`** -> AI Confidence: **99.31%**
39. **`discovery/kubernetes/endpoints.go`** -> AI Confidence: **99.31%**
40. **`discovery/kubernetes/endpointslice.go`** -> AI Confidence: **99.31%**
41. **`discovery/kubernetes/ingress.go`** -> AI Confidence: **99.31%**
42. **`discovery/kubernetes/kubernetes.go`** -> AI Confidence: **99.31%**
43. **`discovery/kubernetes/pod.go`** -> AI Confidence: **99.31%**
44. **`discovery/kubernetes/service.go`** -> AI Confidence: **99.31%**
45. **`discovery/linode/linode.go`** -> AI Confidence: **99.31%**
46. **`discovery/moby/docker.go`** -> AI Confidence: **99.31%**
47. **`discovery/moby/nodes.go`** -> AI Confidence: **99.31%**
48. **`discovery/moby/services.go`** -> AI Confidence: **99.31%**
49. **`discovery/openstack/instance.go`** -> AI Confidence: **99.31%**
50. **`discovery/openstack/loadbalancer.go`** -> AI Confidence: **99.31%**
51. **`discovery/ovhcloud/dedicated_server.go`** -> AI Confidence: **99.31%**
52. **`discovery/refresh/refresh.go`** -> AI Confidence: **99.31%**
53. **`discovery/registry.go`** -> AI Confidence: **99.31%**
54. **`discovery/scaleway/baremetal.go`** -> AI Confidence: **99.31%**
55. **`discovery/scaleway/instance.go`** -> AI Confidence: **99.31%**
56. **`discovery/stackit/server.go`** -> AI Confidence: **99.31%**
57. **`documentation/examples/custom-sd/adapter-usage/main.go`** -> AI Confidence: **99.31%**
58. **`documentation/examples/remote_storage/remote_storage_adapter/graphite/client.go`** -> AI Confidence: **99.31%**
59. **`documentation/examples/remote_storage/remote_storage_adapter/influxdb/client.go`** -> AI Confidence: **99.31%**
60. **`documentation/examples/remote_storage/remote_storage_adapter/main.go`** -> AI Confidence: **99.31%**
61. **`model/labels/regexp.go`** -> AI Confidence: **99.31%**
62. **`model/relabel/relabel.go`** -> AI Confidence: **99.31%**
63. **`model/rulefmt/rulefmt.go`** -> AI Confidence: **99.31%**
64. **`model/textparse/nhcbparse.go`** -> AI Confidence: **99.31%**
65. **`model/textparse/openmetricsparse.go`** -> AI Confidence: **99.31%**
66. **`model/textparse/promparse.go`** -> AI Confidence: **99.31%**
67. **`notifier/alertmanager.go`** -> AI Confidence: **99.31%**
68. **`notifier/alertmanagerset.go`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `cmd/prometheus/main.go` -> **100.0%** Exposure
- `scrape/target.go` -> **100.0%** Exposure
- `tsdb/block.go` -> **100.0%** Exposure
- `web/ui/mantine-ui/src/promql/tools/gen_functions_docs/main.go` -> **100.0%** Exposure
- `web/ui/mantine-ui/src/App.tsx` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `rules/alerting.go` -> **100.0%** Exposure
- `rules/origin.go` -> **100.0%** Exposure
- `rules/recording.go` -> **100.0%** Exposure
- `template/template.go` -> **100.0%** Exposure
- `web/api/v1/openapi.go` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `cmd/promtool/main.go` -> **100.0%** Exposure
- `discovery/aws/ec2.go` -> **100.0%** Exposure
- `model/histogram/float_histogram.go` -> **100.0%** Exposure
- `storage/remote/otlptranslator/prometheusremotewrite/metrics_to_prw.go` -> **100.0%** Exposure
- `scripts/compress_assets.sh` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `15` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `4831` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `web/ui/mantine-ui/src/pages/query/HistoryCompleteStrategy.tsx` (TYPESCRIPT) -> Cumulative Risk: **853.1**
- **Archetype:** `file_cluster_4` (Distance: 10.018 IQR)
- **Magnitude:** 10.56 | **LOC:** 45 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `promQL` (Impact: 82.0), `constructor` (Impact: 2.8)

### 2. `web/ui/module/codemirror-promql/src/client/prometheus.ts` (TYPESCRIPT) -> Cumulative Risk: **814.58**
- **Archetype:** `file_cluster_4` (Distance: 13.791 IQR)
- **Magnitude:** 72.82 | **LOC:** 474 | **CtrlFlow:** 55.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `labelValues` (Impact: 28.1), `fetchAPI` (Impact: 27.5), `labelNames` (Impact: 19.3)

### 3. `web/ui/react-app/src/pages/graph/Graph.tsx` (TYPESCRIPT) -> Cumulative Risk: **761.58**
- **Archetype:** `file_cluster_17` (Distance: 13.18 IQR)
- **Magnitude:** 29.11 | **LOC:** 287 | **CtrlFlow:** 36.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `handleSeriesSelect` (Impact: 37.6), `componentDidUpdate` (Impact: 32.9), `render` (Impact: 13.5)

### 4. `cmd/promtool/main.go` (GO) -> Cumulative Risk: **755.07**
- **Archetype:** `file_cluster_8` (Distance: 14.406 IQR)
- **Magnitude:** 1735.62 | **LOC:** 1428 | **CtrlFlow:** 71.8% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (99.9956%)
- **Heaviest Functions:** `main` (Impact: 192.3), `checkConfig` (Impact: 180.3), `checkDuplicates` (Impact: 150.2)

### 5. `discovery/file/file.go` (GO) -> Cumulative Risk: **745.54**
- **Archetype:** `file_cluster_4` (Distance: 13.939 IQR)
- **Magnitude:** 524.82 | **LOC:** 430 | **CtrlFlow:** 53.3% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Logic Bomb (99.9964%)
- **Heaviest Functions:** `readFile` (Impact: 71.0), `refresh` (Impact: 57.6), `UnmarshalYAML` (Impact: 18.0)

### 6. `rules/manager.go` (GO) -> Cumulative Risk: **733.55**
- **Archetype:** `file_cluster_4` (Distance: 13.903 IQR)
- **Magnitude:** 543.54 | **LOC:** 647 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 80.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (92.6748%)
- **Heaviest Functions:** `Update` (Impact: 43.0), `LoadGroups` (Impact: 40.3), `NewManager` (Impact: 32.9)

### 7. `web/ui/react-app/src/pages/graph/Legend.tsx` (TYPESCRIPT) -> Cumulative Risk: **723.8**
- **Archetype:** `file_cluster_17` (Distance: 12.806 IQR)
- **Magnitude:** 11.91 | **LOC:** 80 | **CtrlFlow:** 51.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.5954%)
- **Heaviest Functions:** `handleSeriesSelect` (Impact: 41.2), `render` (Impact: 26.8), `componentDidUpdate` (Impact: 5.4)

### 8. `cmd/prometheus/main.go` (GO) -> Cumulative Risk: **719.72**
- **Archetype:** `file_cluster_8` (Distance: 14.388 IQR)
- **Magnitude:** 1306.82 | **LOC:** 2181 | **CtrlFlow:** 60.5% | **Authorship Centralization:** 25.9%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Churn (96.15%)
- **Heaviest Functions:** `main` (Impact: 407.1), `setFeatureListOptions` (Impact: 118.0), `Write` (Impact: 18.9)

### 9. `web/ui/react-app/src/pages/graph/Panel.tsx` (TYPESCRIPT) -> Cumulative Risk: **717.11**
- **Archetype:** `file_cluster_13` (Distance: 12.548 IQR)
- **Magnitude:** 34.17 | **LOC:** 402 | **CtrlFlow:** 42.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `executeQuery` (Impact: 187.6), `onExecuteQuery` (Impact: 3.0), `constructor` (Impact: 2.6)

### 10. `tsdb/block.go` (GO) -> Cumulative Risk: **700.37**
- **Archetype:** `file_cluster_0` (Distance: 14.24 IQR)
- **Magnitude:** 599.14 | **LOC:** 746 | **CtrlFlow:** 36.5% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Tech Debt (93.3341%)
- **Heaviest Functions:** `Delete` (Impact: 39.1), `Snapshot` (Impact: 26.4), `SortedLabelValues` (Impact: 23.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `promql/engine.go` (GO | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.29 IQR)
- **Top Global Matches:** file_cluster_8: 15.29, file_cluster_7: 15.353, file_cluster_11: 15.432
- **Magnitude:** 5307.34 | **LOC:** 4611 | **CtrlFlow:** 72.9% | **Authorship Centralization:** 48.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 521
- **Risk Profile:** Cognitive Load (47.8388%), Tech Debt (27.3816%)
**Top Internal Functions/Classes:**
  * `rangeEval` (Impact: 2646.2 | O(2^N) | DB: 521)
  * `preprocessExprHelper` (Impact: 124.2 | O(2^N) | DB: 21)
  * `mergeSeriesWithSameLabelset` (Impact: 39.7 | O(N^1) | DB: 19)
  * `resetHistograms` (Impact: 39.5 | O(N^1) | DB: 19)
  * `recover` (Impact: 29.1 | O(2^N) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 671`, `structural_boundaries: 250`, `args: 74`, `func_start: 74`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1986`, `dead_code: 5`, `planned_debt: 6`, `duplicate_logic: 5`, `orphaned_logic: 8`
* *Architecture:* `api: 64`, `concurrency: 6`, `import: 1`
* *Defense:* `safety: 46`, `doc: 241`, `test: 1`, `sync_locks: 1`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` logging, stats, histogram_quantile, label_replace, chunkenc, features, attribute, parser...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scrape/testdata/ca.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scrape/testdata/ca.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scrape/testdata/client.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scrape/testdata/client.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scrape/testdata/server.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scrape/testdata/server.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scrape/testdata/servername.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scrape/testdata/servername.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tracing/testdata/ca.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `web/ui/react-app/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `model/histogram/float_histogram.go` (GO | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.975 IQR)
- **Top Global Matches:** file_cluster_8: 13.975, file_cluster_7: 14.055, file_cluster_15: 14.18
- **Magnitude:** 2503.92 | **LOC:** 2455 | **CtrlFlow:** 71.9% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 172
- **Risk Profile:** Cognitive Load (46.7236%), Tech Debt (19.6784%)
**Top Internal Functions/Classes:**
  * `Next` (Impact: 1244.5 | O(2^N) | DB: 172)
  * `TestExpression` (Impact: 127.1 | O(N^1) | DB: 111)
    * *Intent:* // TestExpression returns the string representation of this histogram as it is used in the internal ...
  * `Validate` (Impact: 40.5 | O(N^1) | DB: 5)
  * `String` (Impact: 32.8 | O(2^N) | DB: 7)
    * *Intent:* // String returns a string representation of the Histogram.
  * `detectReset` (Impact: 32.4 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 292`, `structural_boundaries: 114`, `args: 37`, `func_start: 37`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 898`, `dead_code: 3`, `planned_debt: 1`, `orphaned_logic: 8`
* *Architecture:* `api: 48`, `import: 1`
* *Defense:* `safety: 8`, `doc: 137`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` fmt, errors, strings, math, kahansum
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `promql/functions.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.343 IQR)
- **Top Global Matches:** file_cluster_8: 14.343, file_cluster_7: 14.52, file_cluster_15: 14.618
- **Magnitude:** 2130.66 | **LOC:** 2383 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 12.5%
- **Algorithmic:** O(N) | **DB Complexity:** 32
- **Risk Profile:** Cognitive Load (46.2446%), Tech Debt (63.2895%)
**Top Internal Functions/Classes:**
  * `extrapolatedRate` (Impact: 94.7 | O(N^1) | DB: 32)
  * `instantValue` (Impact: 81.4 | O(N^1) | DB: 24)
    * *Intent:* // Null out the 1st sample if there is a counter reset between the 1st // and 2nd. In this case, we ...
  * `funcChanges` (Impact: 65.1 | O(N^1) | DB: 11)
  * `funcResets` (Impact: 60.6 | O(N^1) | DB: 11)
  * `funcSumOverTime` (Impact: 55.3 | O(N^1) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 353`, `structural_boundaries: 212`, `args: 102`, `func_start: 102`
* *Risk/State:* `state_mutation: 981`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 10`, `orphaned_logic: 4`
* *Architecture:* `api: 47`, `import: 1`
* *Defense:* `safety: 14`, `doc: 97`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` histogram_quantile, increase, cosh, round, atanh, floor, clamp, ln...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `web/api/v1/api.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.128 IQR)
- **Top Global Matches:** file_cluster_0: 14.128, file_cluster_8: 14.399, file_cluster_11: 14.485
- **Magnitude:** 2043.36 | **LOC:** 2322 | **CtrlFlow:** 52.5% | **Authorship Centralization:** 42.9%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 71
- **Risk Profile:** Cognitive Load (41.4363%), Tech Debt (8.7205%)
**Top Internal Functions/Classes:**
  * `rules` (Impact: 503.0 | O(2^N) | DB: 71)
  * `series` (Impact: 92.5 | O(2^N) | DB: 17)
  * `metricMetadata` (Impact: 74.6 | O(N^1) | DB: 29)
  * `query` (Impact: 62.2 | O(2^N) | DB: 16)
    * *Intent:* // OpenAPI endpoint.
  * `labelValues` (Impact: 61.2 | O(N^1) | DB: 24)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 258`, `structural_boundaries: 233`, `args: 33`, `func_start: 33`, `class_start: 25`
* *Risk/State:* `state_mutation: 745`, `orphaned_logic: 2`
* *Architecture:* `io: 1`, `api: 190`, `concurrency: 18`, `import: 1`
* *Defense:* `safety: 87`, `doc: 56`, `immutability_locks: 2`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` stats, promql, httputil, filepath, index, features, rand, parser...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/promtool/main.go` (GO | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.406 IQR)
- **Top Global Matches:** file_cluster_8: 14.406, file_cluster_7: 14.698, file_cluster_13: 14.699
- **Magnitude:** 1735.62 | **LOC:** 1428 | **CtrlFlow:** 71.8% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 158
- **Risk Profile:** Cognitive Load (69.143%), Tech Debt (11.5079%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 192.3 | O(N^1) | DB: 158)
  * `checkConfig` (Impact: 180.3 | O(N^2) | DB: 30)
  * `checkDuplicates` (Impact: 150.2 | O(N^1) | DB: 73)
  * `CheckConfig` (Impact: 36.0 | O(N^1) | DB: 11)
    * *Intent:* // CheckConfig validates configuration files.
  * `checkRules` (Impact: 33.6 | O(N^1) | DB: 12)
    * *Intent:* // checkRules validates rule files.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 326`, `structural_boundaries: 128`, `args: 39`, `func_start: 39`, `class_start: 8`
* *Risk/State:* `high_risk_execution: 29`, `state_mutation: 899`, `planned_debt: 1`, `orphaned_logic: 3`
* *Architecture:* `io: 3`, `api: 15`, `concurrency: 6`, `import: 1`
* *Defense:* `safety: 50`, `doc: 21`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` lint, filepath, rule-files, lint-fatal, config-files, expfmt, parser, url...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tsdb/head_wal.go` (GO | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.62 IQR)
- **Top Global Matches:** file_cluster_4: 14.62, file_cluster_8: 14.651, file_cluster_7: 14.816
- **Magnitude:** 1428.44 | **LOC:** 1876 | **CtrlFlow:** 69.4% | **Authorship Centralization:** 20.0%
- **Algorithmic:** O(N) | **DB Complexity:** 63
- **Risk Profile:** Cognitive Load (45.1373%), Tech Debt (37.4196%)
**Top Internal Functions/Classes:**
  * `loadChunkSnapshot` (Impact: 156.0 | O(N^1) | DB: 63)
  * `loadWBL` (Impact: 71.0 | O(N^1) | DB: 19)
  * `ChunkSnapshot` (Impact: 49.8 | O(N^1) | DB: 26)
  * `resetSeriesWithMMappedChunks` (Impact: 39.3 | O(N^1) | DB: 14)
  * `LastChunkSnapshot` (Impact: 36.1 | O(N^1) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 295`, `structural_boundaries: 130`, `args: 23`, `func_start: 23`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 775`, `planned_debt: 6`, `orphaned_logic: 10`
* *Architecture:* `io: 1`, `api: 21`, `concurrency: 84`, `import: 1`
* *Defense:* `safety: 46`, `doc: 63`, `sync_locks: 11`, `immutability_locks: 3`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` tombstones, oldref, filepath, newmaxt, chunkenc, series, oldmaxt, fmt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `discovery/aws/rds.go` (GO | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.844 IQR)
- **Top Global Matches:** file_cluster_8: 13.844, file_cluster_0: 14.038, file_cluster_7: 14.049
- **Magnitude:** 1423.86 | **LOC:** 1000 | **CtrlFlow:** 80.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 166
- **Risk Profile:** Cognitive Load (62.9502%), Tech Debt (11.3344%)
**Top Internal Functions/Classes:**
  * `refresh` (Impact: 457.5 | O(N^1) | DB: 166)
  * `initRdsClient` (Impact: 32.5 | O(N^1) | DB: 18)
  * `describeDBClusters` (Impact: 20.9 | O(N^1) | DB: 8)
  * `describeAllDBClusters` (Impact: 20.8 | O(N^1) | DB: 5)
  * `describeDBInstances` (Impact: 19.1 | O(N^1) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 216`, `structural_boundaries: 54`, `args: 11`, `func_start: 11`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 781`, `orphaned_logic: 4`
* *Architecture:* `api: 39`, `concurrency: 12`, `import: 1`
* *Defense:* `safety: 22`, `doc: 30`, `sync_locks: 9`, `immutability_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` stscreds, refresh, fmt, rds, prometheus, credentials, time, discovery...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `promql/parser/lex.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.5 IQR)
- **Top Global Matches:** file_cluster_8: 12.5, file_cluster_7: 12.783, file_cluster_1: 13.027
- **Magnitude:** 1326.42 | **LOC:** 1265 | **CtrlFlow:** 63.8% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (39.5949%), Tech Debt (10.8536%)
**Top Internal Functions/Classes:**
  * `lexStatements` (Impact: 242.9 | O(2^N) | DB: 20)
  * `lexDurationExpr` (Impact: 119.3 | O(2^N) | DB: 5)
  * `lexHistogram` (Impact: 91.4 | O(2^N) | DB: 11)
  * `lexInsideBraces` (Impact: 90.6 | O(2^N) | DB: 7)
    * *Intent:* // lineComment is the character that starts a line comment.
  * `lexValueSequence` (Impact: 69.9 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 275`, `structural_boundaries: 156`, `args: 30`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `state_mutation: 275`, `orphaned_logic: 3`
* *Architecture:* `api: 7`, `import: 1`
* *Defense:* `doc: 40`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` smoothed, ignoring, buckets, unless, end, n_buckets, utf8, and...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/prometheus/main.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.388 IQR)
- **Top Global Matches:** file_cluster_8: 14.388, file_cluster_7: 14.532, file_cluster_4: 14.585
- **Magnitude:** 1306.82 | **LOC:** 2181 | **CtrlFlow:** 60.5% | **Authorship Centralization:** 25.9%
- **Algorithmic:** O(N) | **DB Complexity:** 197
- **Risk Profile:** Cognitive Load (47.2684%), Tech Debt (11.5007%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 407.1 | O(N^1) | DB: 197)
  * `setFeatureListOptions` (Impact: 118.0 | O(N^1) | DB: 34)
  * `Write` (Impact: 18.9 | O(N^1))
    * *Intent:* // klogv1Writer is used in SetOutputBySeverity call below to redirect any calls // to klogv1 to end ...
  * `init` (Impact: 4.1 | O(N^1) | DB: 2)
  * `parseCompressionType` (Impact: 3.8 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 250`, `structural_boundaries: 163`, `args: 48`, `func_start: 48`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 584`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 1`, `orphaned_logic: 2`
* *Architecture:* `io: 2`, `api: 92`, `concurrency: 48`, `import: 1`
* *Defense:* `safety: 42`, `doc: 75`, `sync_locks: 8`, `immutability_locks: 2`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` logging, klog, run, rest, relabel, web.config.file, time, flag...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tsdb/db.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.98 IQR)
- **Top Global Matches:** file_cluster_8: 14.98, file_cluster_4: 14.984, file_cluster_7: 15.038
- **Magnitude:** 1284.1 | **LOC:** 2632 | **CtrlFlow:** 59.1% | **Authorship Centralization:** 15.8%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 63
- **Risk Profile:** Cognitive Load (47.5233%), Tech Debt (32.5236%)
**Top Internal Functions/Classes:**
  * `compactOOOHead` (Impact: 132.3 | O(N^1) | DB: 63)
  * `Compact` (Impact: 102.6 | O(2^N) | DB: 15)
  * `loadDataAsQueryable` (Impact: 102.3 | O(2^N) | DB: 19)
  * `ApplyConfig` (Impact: 66.2 | O(2^N) | DB: 12)
  * `run` (Impact: 64.7 | O(N^1) | DB: 18)
    * *Intent:* // FlushWAL creates a new block containing all data that's currently in the memory buffer/WAL.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 105`, `args: 31`, `func_start: 31`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 528`, `dead_code: 1`, `planned_debt: 1`, `orphaned_logic: 9`
* *Architecture:* `api: 103`, `concurrency: 42`, `import: 1`
* *Defense:* `safety: 55`, `doc: 111`, `sync_locks: 31`, `immutability_locks: 1`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` HEAD, filepath, block_range, chunkenc, features, rand, runtime, tsdbutil...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tsdb/head_append.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.23 IQR)
- **Top Global Matches:** file_cluster_8: 14.23, file_cluster_11: 14.272, file_cluster_7: 14.301
- **Magnitude:** 1278.18 | **LOC:** 2299 | **CtrlFlow:** 68.9% | **Authorship Centralization:** 27.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 65
- **Risk Profile:** Cognitive Load (36.9325%), Tech Debt (44.3425%)
**Top Internal Functions/Classes:**
  * `appendableMinValidTime` (Impact: 166.7 | O(N^1) | DB: 65)
    * *Intent:* // appendableMinValidTime returns the minimum valid timestamp for appends, // such that samples stay...
  * `Commit` (Impact: 69.4 | O(N^1) | DB: 37)
  * `commitFloats` (Impact: 64.7 | O(N^1) | DB: 28)
  * `commitHistograms` (Impact: 53.9 | O(N^1) | DB: 21)
  * `commitFloatHistograms` (Impact: 53.9 | O(N^1) | DB: 21)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 222`, `structural_boundaries: 100`, `args: 36`, `func_start: 36`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 614`, `dead_code: 5`, `planned_debt: 10`, `duplicate_logic: 2`, `orphaned_logic: 4`
* *Architecture:* `api: 29`, `concurrency: 6`, `import: 1`
* *Defense:* `safety: 23`, `doc: 125`, `sync_locks: 22`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` labels, fmt, errors, math, histogram, value, context, time...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tsdb/head.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.879 IQR)
- **Top Global Matches:** file_cluster_8: 13.879, file_cluster_7: 13.946, file_cluster_15: 13.997
- **Magnitude:** 1272.68 | **LOC:** 2708 | **CtrlFlow:** 47.6% | **Authorship Centralization:** 13.3%
- **Algorithmic:** O(N) | **DB Complexity:** 125
- **Risk Profile:** Cognitive Load (44.6199%), Tech Debt (10.1702%)
**Top Internal Functions/Classes:**
  * `loadMmappedChunks` (Impact: 347.0 | O(N^1) | DB: 125)
  * `Init` (Impact: 92.2 | O(N^1) | DB: 39)
  * `NewHead` (Impact: 40.6 | O(N^1) | DB: 10)
  * `newHeadMetrics` (Impact: 17.4 | O(N^1) | DB: 2)
  * `resetInMemoryState` (Impact: 15.7 | O(N^1) | DB: 14)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 178`, `structural_boundaries: 196`, `args: 60`, `func_start: 60`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 542`, `planned_debt: 5`, `fragile_debt: 1`
* *Architecture:* `api: 173`, `concurrency: 8`, `import: 1`
* *Defense:* `safety: 28`, `doc: 150`, `sync_locks: 47`, `immutability_locks: 3`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` tombstones, err, filepath, index, chunkenc, wal_replay_duration, v2, fmt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `storage/remote/queue_manager.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.356 IQR)
- **Top Global Matches:** file_cluster_8: 13.356, file_cluster_7: 13.473, file_cluster_4: 13.53
- **Magnitude:** 1230.88 | **LOC:** 2321 | **CtrlFlow:** 53.7% | **Authorship Centralization:** 20.0%
- **Algorithmic:** O(N) | **DB Complexity:** 76
- **Risk Profile:** Cognitive Load (37.8647%), Tech Debt (21.1157%)
**Top Internal Functions/Classes:**
  * `sendMetadataWithBackoff` (Impact: 151.2 | O(N^1) | DB: 76)
  * `NewQueueManager` (Impact: 32.5 | O(N^1) | DB: 11)
    * *Intent:* // NewQueueManager builds a new QueueManager and starts a new // WAL watcher with queue manager as t...
  * `sendV2SamplesWithBackoff` (Impact: 31.6 | O(N^1) | DB: 18)
  * `sendSamplesWithBackoff` (Impact: 30.4 | O(N^1) | DB: 17)
  * `populateV2TimeSeries` (Impact: 28.9 | O(N^1) | DB: 16)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 145`, `structural_boundaries: 125`, `args: 39`, `func_start: 39`, `class_start: 9`
* *Risk/State:* `state_mutation: 499`, `dead_code: 2`, `planned_debt: 4`, `orphaned_logic: 8`
* *Architecture:* `api: 180`, `concurrency: 72`, `import: 1`
* *Defense:* `safety: 26`, `doc: 89`, `sync_locks: 46`, `immutability_locks: 2`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` dataKeptRatio, v2, dataInRate, sample, histogram, attribute, relabel, timePerSample...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `storage/remote/codec.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.998 IQR)
- **Top Global Matches:** file_cluster_8: 13.998, file_cluster_11: 14.091, file_cluster_15: 14.136
- **Magnitude:** 1185.64 | **LOC:** 1018 | **CtrlFlow:** 53.9% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (44.9174%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `StreamChunkedReadResponses` (Impact: 71.7 | O(2^N) | DB: 22)
    * *Intent:* // StreamChunkedReadResponses iterates over series, builds chunks and streams those to the caller. /...
  * `Seek` (Impact: 59.3 | O(N^1) | DB: 10)
    * *Intent:* // Seek implements storage.SeriesIterator.
  * `Next` (Impact: 37.2 | O(2^N) | DB: 6)
  * `Next` (Impact: 29.7 | O(N^1) | DB: 19)
    * *Intent:* // Next implements chunkenc.Iterator.
  * `DecodeOTLPWriteRequest` (Impact: 28.6 | O(N^1) | DB: 11)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 159`, `structural_boundaries: 136`, `args: 52`, `func_start: 52`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 525`, `dead_code: 1`, `planned_debt: 3`, `duplicate_logic: 32`, `orphaned_logic: 12`
* *Architecture:* `io: 5`, `api: 74`, `import: 1`
* *Defense:* `safety: 35`, `doc: 46`, `sync_locks: 1`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` v2, chunkenc, snappy, fmt, slices, sort, histogram, pmetricotlp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tsdb/querier.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.952 IQR)
- **Top Global Matches:** file_cluster_8: 13.952, file_cluster_13: 14.141, file_cluster_11: 14.145
- **Magnitude:** 1100.16 | **LOC:** 1276 | **CtrlFlow:** 58.0% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 40
- **Risk Profile:** Cognitive Load (46.3538%), Tech Debt (99.6511%)
**Top Internal Functions/Classes:**
  * `Next` (Impact: 175.2 | O(2^N) | DB: 40)
  * `Next` (Impact: 124.7 | O(2^N) | DB: 17)
  * `PostingsForMatchers` (Impact: 49.5 | O(N^1) | DB: 20)
    * *Intent:* // PostingsForMatchers assembles a single postings iterator against the index reader // based on the...
  * `next` (Impact: 37.0 | O(N^1) | DB: 14)
    * *Intent:* // blockBaseSeriesSet allows to iterate over all series in the single block. // Iterated series are ...
  * `Next` (Impact: 32.3 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 159`, `structural_boundaries: 115`, `args: 38`, `func_start: 38`, `class_start: 11`
* *Risk/State:* `state_mutation: 440`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 12`, `orphaned_logic: 5`
* *Architecture:* `api: 28`, `import: 1`
* *Defense:* `safety: 40`, `doc: 40`, `immutability_locks: 1`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` labels, v2, tombstones, fmt, errors, math, index, slices...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `discovery/azure/azure.go` (GO) | Magnitude: 788.52 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 545, state_mutation: 376, encapsulation: 158, branch: 134
- `discovery/aws/ecs.go` (GO) | Magnitude: 496.56 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 448, state_mutation: 345, encapsulation: 162, branch: 110
- `notifier/alert.go` (GO) | Magnitude: 69.26 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 46, state_mutation: 17, api: 16, doc: 15
- `discovery/zookeeper/zookeeper.go` (GO) | Magnitude: 0.05 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 49, structural_boundaries: 15, doc: 14, api: 12
- `model/relabel/relabel.go` (GO) | Magnitude: 495.38 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 239, state_mutation: 108, branch: 107, structural_boundaries: 51

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `promql/value.go` (GO) | Magnitude: 695.7 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 333, state_mutation: 248, structural_boundaries: 100, encapsulation: 94
- `discovery/discovery.go` (GO) | Magnitude: 119.66 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 50, state_mutation: 43, doc: 30, structural_boundaries: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `scripts/npm-deps.sh` (SHELL) | Magnitude: 1.35 | Delta: **0.129 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: reflection_metaprogramming: 7, safety: 5, state_mutation: 5, indent_spaces: 5
- `discovery/registry.go` (GO) | Magnitude: 354.06 | Delta: **0.139 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 214, indent_tabs: 199, encapsulation: 69, branch: 51
- `scripts/ui_release.sh` (SHELL) | Magnitude: 15.71 | Delta: **0.153 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: branch: 61, indent_spaces: 60, reflection_metaprogramming: 41, safety: 33
- `scripts/generate_release_notes.sh` (SHELL) | Magnitude: 6.96 | Delta: **0.209 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 38, state_mutation: 33, reflection_metaprogramming: 31, branch: 27
- `scripts/sync_repo_files.sh` (SHELL) | Magnitude: 41.8 | Delta: **0.218 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 134, branch: 77, reflection_metaprogramming: 75, state_mutation: 63

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `web/ui/mantine-ui/src/components/Accordion/Accordion.context.ts` (TYPESCRIPT) | Magnitude: 3.64 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 10, func_start: 5, args: 4
- `web/ui/react-app/src/contexts/PathPrefixContext.tsx` (TYPESCRIPT) | Magnitude: 0.3 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, args: 1, func_start: 1, api: 1
- `web/ui/react-app/src/contexts/ReadyContext.tsx` (TYPESCRIPT) | Magnitude: 0.3 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, args: 1, func_start: 1, api: 1
- `util/runtime/statfs_windows.go` (GO) | Magnitude: 23.82 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 22, pointers: 11, state_mutation: 10, doc: 7
- `notifier/util.go` (GO) | Magnitude: 35.9 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 23, state_mutation: 20, encapsulation: 9, api: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `util/stats/timer.go` (GO) | Magnitude: 82.46 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 35, state_mutation: 29, structural_boundaries: 17, pointers: 17
- `discovery/discoverer_metrics_noop.go` (GO) | Magnitude: 8.36 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 9, structural_boundaries: 4, api: 3, pointers: 3
- `tsdb/chunkenc/chunk.go` (GO) | Magnitude: 303.38 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 190, structural_boundaries: 78, doc: 62, api: 52
- `tsdb/index/postings.go` (GO) | Magnitude: 298.34 | Delta: **0.077 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 175, state_mutation: 169, doc: 52, encapsulation: 52
- `model/labels/labels_common.go` (GO) | Magnitude: 284.62 | Delta: **0.091 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 132, state_mutation: 99, structural_boundaries: 37, branch: 33

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `util/zeropool/pool.go` (GO) | Magnitude: 56.5 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 26, state_mutation: 22, doc: 16, encapsulation: 8
- `web/api/testhelpers/assertions.go` (GO) | Magnitude: 158.88 | Delta: **0.11 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 136, encapsulation: 61, state_mutation: 58, pointers: 37
- `util/pool/pool.go` (GO) | Magnitude: 107.66 | Delta: **0.126 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 47, state_mutation: 30, branch: 14, doc: 10
- `util/testutil/cmp.go` (GO) | Magnitude: 19.26 | Delta: **0.24 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 16, state_mutation: 9, doc: 9, structural_boundaries: 4
- `web/ui/mantine-ui/src/components/Accordion/Accordion.types.ts` (TYPESCRIPT) | Magnitude: 1.56 | Delta: **0.289 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 8, api: 3, generics: 2, indent_spaces: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `scripts/get_module_version.sh` (SHELL) | Magnitude: 3.41 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 18, branch: 10, indent_spaces: 4, safety_bypasses: 3
- `web/ui/react-app/src/pages/graph/Graph.tsx` (TYPESCRIPT) | Magnitude: 29.11 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 210, state_mutation: 151, structural_boundaries: 48, args: 37
- `web/ui/react-app/src/pages/graph/MetricsExplorer.test.tsx` (TYPESCRIPT) | Magnitude: 0.56 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 14, args: 12, func_start: 11
- `web/ui/mantine-ui/src/components/EndpointLink.tsx` (TYPESCRIPT) | Magnitude: 1.31 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 43, structural_boundaries: 9, state_mutation: 9, branch: 8
- `web/ui/react-app/src/pages/graph/Panel.test.tsx` (TYPESCRIPT) | Magnitude: 4.25 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 130, args: 37, func_start: 33, structural_boundaries: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `web/ui/mantine-ui/src/components/CustomInfiniteScroll.tsx` (TYPESCRIPT) | Magnitude: 1.13 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 10, args: 9, ui_framework: 9
- `web/ui/react-app/src/App.tsx` (TYPESCRIPT) | Magnitude: 1.14 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 99, ui_framework: 31, generics: 31, structural_boundaries: 17
- `web/ui/mantine-ui/src/pages/query/TreeNode.tsx` (TYPESCRIPT) | Magnitude: 8.8 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 277, structural_boundaries: 45, ui_framework: 38, branch: 35
- `web/ui/mantine-ui/src/pages/targets/ScrapePoolsList.tsx` (TYPESCRIPT) | Magnitude: 21.72 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 304, ui_framework: 53, structural_boundaries: 49, generics: 43
- `web/ui/react-app/src/Navbar.test.tsx` (TYPESCRIPT) | Magnitude: 0.7 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 8, args: 6, func_start: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `web/ui/react-app/src/hooks/useFetch.ts` (TYPESCRIPT) | Magnitude: 12.27 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 83, structural_boundaries: 29, args: 23, func_start: 22
- `rules/group.go` (GO) | Magnitude: 797.54 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 572, state_mutation: 252, branch: 134, encapsulation: 134
- `util/testutil/context.go` (GO) | Magnitude: 50.34 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 18, indent_tabs: 18, api: 16, concurrency: 12
- `tsdb/head_wal.go` (GO) | Magnitude: 1428.44 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 914, state_mutation: 775, branch: 295, encapsulation: 277
- `discovery/manager.go` (GO) | Magnitude: 154.44 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 149, state_mutation: 70, encapsulation: 54, structural_boundaries: 49

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `model/textparse/interface.go` (GO) | Magnitude: 68.36 | Delta: **0.117 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 61, doc: 42, state_mutation: 28, api: 17
- `storage/interface_append.go` (GO) | Magnitude: 49.42 | Delta: **0.166 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 32, doc: 29, structural_boundaries: 20, api: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `model/histogram/test_utils.go` (GO) | Magnitude: 65.54 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 41, indent_tabs: 29, api: 10, doc: 8
- `util/features/features.go` (GO) | Magnitude: 88.02 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 43, state_mutation: 28, doc: 28, api: 26
- `tsdb/goversion/goversion.go` (GO) | Magnitude: 12.04 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 7, structural_boundaries: 1, state_mutation: 1, explicit_casts: 1
- `tsdb/fileutil/mmap_386.go` (GO) | Magnitude: 12.04 | Delta: **0.081 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 6, structural_boundaries: 1, state_mutation: 1, immutability_locks: 1
- `tsdb/fileutil/mmap_amd64.go` (GO) | Magnitude: 12.04 | Delta: **0.081 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 6, structural_boundaries: 1, state_mutation: 1, immutability_locks: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `web/ui/react-app/src/components/ToggleMoreLess.test.tsx` (TYPESCRIPT) | Magnitude: 0.51 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 19, args: 9, func_start: 9, structural_boundaries: 8
- `model/textparse/nhcbparse.go` (GO) | Magnitude: 471.98 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 216, state_mutation: 154, branch: 63, structural_boundaries: 45
- `web/api/v1/translate_ast.go` (GO) | Magnitude: 28.3 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 50, structural_boundaries: 23, state_mutation: 12, branch: 8
- `tsdb/db.go` (GO) | Magnitude: 1284.1 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 727, state_mutation: 528, encapsulation: 209, branch: 152
- `discovery/http/http.go` (GO) | Magnitude: 209.44 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 140, state_mutation: 74, encapsulation: 33, structural_boundaries: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `documentation/examples/Makefile` (MAKEFILE) | Magnitude: 16.12 | Delta: **0.11 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: api: 3, func_start: 2, indent_tabs: 2, io: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `scrape/manager.go` -> Churn: **66.11%** | Cog Load: 41.2531% | Debt: 98.9448%
- `tsdb/chunkenc/chunk.go` -> Churn: **58.8%** | Cog Load: 24.6824% | Debt: 100.0%
- `cmd/promtool/main.go` -> Churn: **54.02%** | Cog Load: 69.143% | Debt: 11.5079%
- `util/annotations/annotations.go` -> Churn: **51.7%** | Cog Load: 46.7414% | Debt: 98.2394%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `discovery/aws/rds.go` -> **Matt** (100.0% isolated ownership) | Magnitude: 1423.86
- `tsdb/chunks/head_chunks.go` -> **Ben Kochie** (100.0% isolated ownership) | Magnitude: 1057.6
- `prompb/io/prometheus/client/decoder.go` -> **Ben Kochie** (100.0% isolated ownership) | Magnitude: 1043.08
- `model/textparse/protobufparse.go` -> **Ben Kochie** (100.0% isolated ownership) | Magnitude: 983.88
- `rules/group.go` -> **Ben Kochie** (100.0% isolated ownership) | Magnitude: 797.54

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `discovery/http/http.go` -> **Severity: 0.015** (Bridge: 0.0001 * Flux: 100.0%)
- `tsdb/chunks/chunks.go` -> **Severity: 0.011** (Bridge: 0.0001 * Flux: 100.0%)
- `web/ui/module/codemirror-promql/src/parser/parser.ts` -> **Severity: 0.008** (Bridge: 0.0001 * Flux: 89.6318%)
- `discovery/dns/dns.go` -> **Severity: 0.007** (Bridge: 0.0001 * Flux: 100.0%)
- `discovery/scaleway/scaleway.go` -> **Severity: 0.007** (Bridge: 0.0001 * Flux: 99.9026%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `discovery/targetgroup/targetgroup.go` -> **Severity: 8.809** (Embedded: 0.0907 * Error Risk: 97.1041%)
- `storage/errors.go` -> **Severity: 8.747** (Embedded: 0.1449 * Error Risk: 60.3483%)
- `discovery/discovery.go` -> **Severity: 7.28** (Embedded: 0.0862 * Error Risk: 84.4135%)
- `model/labels/regexp.go` -> **Severity: 6.983** (Embedded: 0.0746 * Error Risk: 93.582%)
- `util/strutil/strconv.go` -> **Severity: 6.69** (Embedded: 0.0976 * Error Risk: 68.568%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `storage/errors.go` -> **Severity: 3853.3** (Blast Radius: 38.533 * Doc Risk: 100.0%)
- `discovery/targetgroup/targetgroup.go` -> **Severity: 3469.3** (Blast Radius: 34.693 * Doc Risk: 100.0%)
- `discovery/http/http.go` -> **Severity: 1227.9** (Blast Radius: 12.279 * Doc Risk: 100.0%)
- `web/ui/mantine-ui/src/promql/utils.ts` -> **Severity: 865.5** (Blast Radius: 8.655 * Doc Risk: 100.0%)
- `discovery/refresh/refresh.go` -> **Severity: 671.5** (Blast Radius: 6.715 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
