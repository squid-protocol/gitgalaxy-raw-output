# ARCHITECTURAL_BRIEF: prometheus
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/prometheus` |
| **Timestamp** | `2026-08-07T05:20:57.973586+00:00` |
| **Scan Duration** | `4.01s` |
| **Git Branch** | `main` |
| **Git Commit** | `cb3382314d63ed457279c9582cd6db63d0a06631` |
| **Git Remote** | `https://github.com/prometheus/prometheus` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 688 malicious artifacts.

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
> **Architectural Drift Z-Score:** `5.945`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 787 | 70.0% |
| file_cluster_13 | 132 | 11.7% |
| file_cluster_0 | 42 | 3.7% |
| file_cluster_2 | 33 | 2.9% |
| file_cluster_4 | 27 | 2.4% |
| file_cluster_17 | 20 | 1.8% |
| Unknown | 10 | 0.9% |
| file_cluster_15 | 9 | 0.8% |
| file_cluster_7 | 9 | 0.8% |
| file_cluster_12 | 8 | 0.7% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 17.2 | 6.1 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 33.9 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 22.3 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 14.9 | 2.0 | 80.0 |
| API Exposure | 0.0 | 18.2 | 2.5 | 0.4 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 4.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 35.1 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 38.2 | 0.5 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 76.4 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 31.4 | 0.8 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 6.6 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 33.1 | 23.9 | 0.0 |
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

- `rangeEvalAgg` (@ `promql/engine.go`) -> Impact: **815.6** | LOC: 1944
- `rangeEval` (@ `promql/engine.go`) -> Impact: **777.3** | LOC: 1913
- `VectorAnd` (@ `promql/engine.go`) -> Impact: **470.5** | LOC: 1150
- `refresh` (@ `discovery/aws/rds.go`) -> Impact: **457.5** | LOC: 528
- `Next` (@ `model/histogram/float_histogram.go`) -> Impact: **439.5** | LOC: 740
- `main` (@ `cmd/prometheus/main.go`) -> Impact: **407.1** | LOC: 1317
- `addCustomBucketsWithMismatches` (@ `model/histogram/float_histogram.go`) -> Impact: **381.2** | LOC: 461
  * *Intent:* // floatBucketIterator is a low-level constructor for bucket iterators. // // If positive is true, the returned iterator iterates through the positive...
- `VectorscalarBinop` (@ `promql/engine.go`) -> Impact: **350.1** | LOC: 865
  * *Intent:* // Fallback to name suffix checking
- `loadMmappedChunks` (@ `tsdb/head.go`) -> Impact: **347.0** | LOC: 817
- `aggregation` (@ `promql/engine.go`) -> Impact: **339.9** | LOC: 831

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `scrape/testdata` | 9 | 40000.0 | 0.0% | 0.0% |
| `tsdb` | 22 | 11357.02 | 33.34% | 57.15% |
| `promql` | 8 | 9871.38 | 41.76% | 42.49% |
| `web/ui/react-app` | 3 | 5017.78 | 3.08% | 0.0% |
| `tracing/testdata` | 1 | 5000.0 | 0.0% | 0.0% |
| `storage/remote` | 16 | 4746.2 | 34.75% | 54.19% |
| `discovery/aws` | 14 | 4712.58 | 25.4% | 63.94% |
| `model/histogram` | 5 | 4126.52 | 37.55% | 34.91% |
| `cmd/promtool` | 10 | 4122.6 | 45.06% | 32.85% |
| `web/api/v1` | 10 | 4074.34 | 18.92% | 58.82% |

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
- `web/ui/mantine-ui/src/pages/query/urlStateEncoding.test.ts` -> **0** Orphaned Functions | **82** Duplicates
- `web/ui/react-app/src/utils/utils.test.ts` -> **0** Orphaned Functions | **73** Duplicates
- `web/api/testhelpers/mocks.go` -> **24** Orphaned Functions | **46** Duplicates
- `web/ui/react-app/src/pages/graph/HistorgramHelpers.test.tsx` -> **0** Orphaned Functions | **52** Duplicates
- `storage/remote/codec.go` -> **12** Orphaned Functions | **32** Duplicates

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `15` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `4831` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `rules/manager.go` (GO) -> Cumulative Risk: **733.54**
- **Archetype:** `file_cluster_4` (Distance: 13.881 IQR)
- **Magnitude:** 495.74 | **LOC:** 647 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 80.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (92.6748%)
- **Heaviest Functions:** `NewManager` (Impact: 32.9), `Update` (Impact: 26.5), `ParseFiles` (Impact: 25.4)

### 2. `cmd/prometheus/main.go` (GO) -> Cumulative Risk: **692.98**
- **Archetype:** `file_cluster_8` (Distance: 14.389 IQR)
- **Magnitude:** 1549.22 | **LOC:** 2181 | **CtrlFlow:** 60.5% | **Authorship Centralization:** 25.9%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Churn (96.15%), Safety Score (90.0168%)
- **Heaviest Functions:** `main` (Impact: 407.1), `setFeatureListOptions` (Impact: 118.0), `reloadConfig` (Impact: 26.7)

### 3. `web/web.go` (GO) -> Cumulative Risk: **690.66**
- **Archetype:** `file_cluster_8` (Distance: 13.579 IQR)
- **Magnitude:** 665.1 | **LOC:** 972 | **CtrlFlow:** 49.7% | **Authorship Centralization:** 30.8%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Concurrency (96.3041%)
- **Heaviest Functions:** `New` (Impact: 66.5), `serveDebug` (Impact: 18.9), `testReady` (Impact: 15.6)

### 4. `util/annotations/annotations.go` (GO) -> Cumulative Risk: **685.86**
- **Archetype:** `file_cluster_8` (Distance: 13.387 IQR)
- **Magnitude:** 481.9 | **LOC:** 482 | **CtrlFlow:** 48.5% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (98.2394%)
- **Heaviest Functions:** `AsStrings` (Impact: 22.9), `Merge` (Impact: 20.9), `Merge` (Impact: 18.0)

### 5. `promql/query_logger.go` (GO) -> Cumulative Risk: **682.16**
- **Archetype:** `file_cluster_4` (Distance: 13.341 IQR)
- **Magnitude:** 228.14 | **LOC:** 237 | **CtrlFlow:** 44.3% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.3012%), Safety Score (92.667%)
- **Heaviest Functions:** `getMMappedFile` (Impact: 11.3), `logUnfinishedQueries` (Impact: 11.2), `Close` (Impact: 9.4)

### 6. `util/notifications/notifications.go` (GO) -> Cumulative Risk: **677.92**
- **Archetype:** `file_cluster_4` (Distance: 12.572 IQR)
- **Magnitude:** 162.42 | **LOC:** 186 | **CtrlFlow:** 36.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (93.4474%)
- **Heaviest Functions:** `notifySubscribers` (Impact: 15.3), `AddNotification` (Impact: 10.9), `DeleteNotification` (Impact: 10.6)

### 7. `storage/series.go` (GO) -> Cumulative Risk: **664.53**
- **Archetype:** `file_cluster_8` (Distance: 13.089 IQR)
- **Magnitude:** 432.96 | **LOC:** 508 | **CtrlFlow:** 33.6% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `Iterator` (Impact: 42.5), `NewListChunkSeriesFromSamples` (Impact: 13.8), `Seek` (Impact: 13.3)

### 8. `model/rulefmt/rulefmt.go` (GO) -> Cumulative Risk: **650.01**
- **Archetype:** `file_cluster_0` (Distance: 13.613 IQR)
- **Magnitude:** 415.54 | **LOC:** 382 | **CtrlFlow:** 56.1% | **Authorship Centralization:** 60.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.665%)
- **Heaviest Functions:** `Validate` (Impact: 41.3), `Validate` (Impact: 26.8), `testTemplateParsing` (Impact: 18.3)

### 9. `util/treecache/treecache.go` (GO) -> Cumulative Risk: **647.77**
- **Archetype:** `file_cluster_4` (Distance: 13.274 IQR)
- **Magnitude:** 384.36 | **LOC:** 316 | **CtrlFlow:** 48.6% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (95.4806%)
- **Heaviest Functions:** `loop` (Impact: 50.7), `recursiveNodeUpdate` (Impact: 35.9), `recursiveStop` (Impact: 10.2)

### 10. `promql/value.go` (GO) -> Cumulative Risk: **646.61**
- **Archetype:** `file_cluster_11` (Distance: 13.376 IQR)
- **Magnitude:** 603.2 | **LOC:** 611 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `Next` (Impact: 31.4), `MarshalJSON` (Impact: 22.0), `newFParams` (Impact: 19.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `promql/engine.go` (GO | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.277 IQR)
- **Top Global Matches:** file_cluster_8: 15.277, file_cluster_7: 15.341, file_cluster_11: 15.42
- **Magnitude:** 5949.54 | **LOC:** 4611 | **CtrlFlow:** 72.9% | **Authorship Centralization:** 48.4%
- **Risk Profile:** Cognitive Load (47.7195%), Tech Debt (30.0359%)
**Top Internal Functions/Classes:**
  * `rangeEvalAgg` (Impact: 815.6)
  * `rangeEval` (Impact: 777.3)
  * `VectorAnd` (Impact: 470.5)
  * `VectorscalarBinop` (Impact: 350.1)
    * *Intent:* // Fallback to name suffix checking
  * `aggregation` (Impact: 339.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 671`, `structural_boundaries: 250`, `args: 74`, `func_start: 74`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1986`, `dead_code: 5`, `planned_debt: 6`, `duplicate_logic: 5`, `orphaned_logic: 10`
* *Architecture:* `api: 64`, `concurrency: 6`, `import: 1`
* *Defense:* `safety: 46`, `doc: 241`, `test: 1`, `sync_locks: 1`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` model, histogram_quantile, context, value, io, histogram_count, storage, fmt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scrape/testdata/ca.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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
- **Global Archetype:** `file_cluster_8` (Drift: 13.986 IQR)
- **Top Global Matches:** file_cluster_8: 13.986, file_cluster_7: 14.066, file_cluster_15: 14.191
- **Magnitude:** 3167.82 | **LOC:** 2455 | **CtrlFlow:** 71.9% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (46.0021%), Tech Debt (31.7932%)
**Top Internal Functions/Classes:**
  * `Next` (Impact: 439.5)
  * `addCustomBucketsWithMismatches` (Impact: 381.2)
    * *Intent:* // floatBucketIterator is a low-level constructor for bucket iterators. // // If positive is true, t...
  * `kahanReduceResolution` (Impact: 288.7)
  * `adjustCounterReset` (Impact: 242.6)
  * `kahanAddBuckets` (Impact: 136.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 292`, `structural_boundaries: 114`, `args: 37`, `func_start: 37`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 896`, `dead_code: 3`, `planned_debt: 1`, `orphaned_logic: 13`
* *Architecture:* `api: 48`, `import: 1`
* *Defense:* `safety: 8`, `doc: 137`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` fmt, strings, math, kahansum, errors
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `promql/functions.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.341 IQR)
- **Top Global Matches:** file_cluster_8: 14.341, file_cluster_7: 14.519, file_cluster_15: 14.616
- **Magnitude:** 2121.36 | **LOC:** 2383 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 12.5%
- **Risk Profile:** Cognitive Load (46.2446%), Tech Debt (63.2895%)
**Top Internal Functions/Classes:**
  * `extrapolatedRate` (Impact: 94.7)
  * `instantValue` (Impact: 81.4)
    * *Intent:* // Null out the 1st sample if there is a counter reset between the 1st // and 2nd. In this case, we ...
  * `funcChanges` (Impact: 65.1)
  * `funcResets` (Impact: 60.6)
  * `funcSumOverTime` (Impact: 55.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 353`, `structural_boundaries: 212`, `args: 102`, `func_start: 102`
* *Risk/State:* `state_mutation: 981`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 10`, `orphaned_logic: 4`
* *Architecture:* `api: 47`, `import: 1`
* *Defense:* `safety: 14`, `doc: 97`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` sort_by_label, sgn, days_in_month, min_over_time, sum_over_time, ts_of_last_over_time, sinh, histogram_quantiles...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tsdb/head.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.872 IQR)
- **Top Global Matches:** file_cluster_8: 13.872, file_cluster_7: 13.934, file_cluster_15: 13.984
- **Magnitude:** 2071.38 | **LOC:** 2708 | **CtrlFlow:** 47.6% | **Authorship Centralization:** 13.3%
- **Risk Profile:** Cognitive Load (45.1035%), Tech Debt (78.5537%)
**Top Internal Functions/Classes:**
  * `loadMmappedChunks` (Impact: 347.0)
  * `Close` (Impact: 226.2)
  * `IsQuerierCollidingWithTruncation` (Impact: 193.2)
  * `Init` (Impact: 92.2)
  * `iterForDeletion` (Impact: 69.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 178`, `structural_boundaries: 196`, `args: 60`, `func_start: 60`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 542`, `planned_debt: 5`, `fragile_debt: 1`, `duplicate_logic: 11`
* *Architecture:* `api: 186`, `concurrency: 8`, `import: 1`
* *Defense:* `safety: 28`, `doc: 150`, `sync_locks: 47`, `immutability_locks: 3`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` metadata, total_replay_duration, context, value, io, v2, storage, fmt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `web/api/v1/api.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.115 IQR)
- **Top Global Matches:** file_cluster_0: 14.115, file_cluster_8: 14.385, file_cluster_11: 14.473
- **Magnitude:** 1853.46 | **LOC:** 2322 | **CtrlFlow:** 52.5% | **Authorship Centralization:** 42.9%
- **Risk Profile:** Cognitive Load (41.4363%), Tech Debt (8.7205%)
**Top Internal Functions/Classes:**
  * `rules` (Impact: 260.5)
  * `metricMetadata` (Impact: 74.6)
  * `labelValues` (Impact: 61.2)
  * `labelNames` (Impact: 52.8)
  * `series` (Impact: 48.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 258`, `structural_boundaries: 233`, `args: 33`, `func_start: 33`, `class_start: 25`
* *Risk/State:* `state_mutation: 745`, `orphaned_logic: 2`
* *Architecture:* `io: 1`, `api: 190`, `concurrency: 18`, `import: 1`
* *Defense:* `safety: 87`, `doc: 56`, `immutability_locks: 2`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` model, metadata, remote, context, route, goautoneg, storage, fmt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/promtool/main.go` (GO | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.41 IQR)
- **Top Global Matches:** file_cluster_8: 14.41, file_cluster_13: 14.698, file_cluster_7: 14.701
- **Magnitude:** 1847.92 | **LOC:** 1428 | **CtrlFlow:** 71.8% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (76.638%), Tech Debt (48.3026%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 192.3)
  * `checkDuplicates` (Impact: 150.2)
  * `checkConfig` (Impact: 122.3)
  * `importRules` (Impact: 43.8)
  * `CheckConfig` (Impact: 36.0)
    * *Intent:* // CheckConfig validates configuration files.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 326`, `structural_boundaries: 128`, `args: 39`, `func_start: 39`, `class_start: 8`
* *Risk/State:* `high_risk_execution: 29`, `state_mutation: 899`, `planned_debt: 1`, `duplicate_logic: 6`, `orphaned_logic: 3`
* *Architecture:* `io: 3`, `api: 15`, `concurrency: 6`, `import: 1`
* *Defense:* `safety: 50`, `doc: 21`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` model, .yml, context, promlint, go, io, kubernetes, json...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/prometheus/main.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.389 IQR)
- **Top Global Matches:** file_cluster_8: 14.389, file_cluster_7: 14.533, file_cluster_4: 14.578
- **Magnitude:** 1549.22 | **LOC:** 2181 | **CtrlFlow:** 60.5% | **Authorship Centralization:** 25.9%
- **Risk Profile:** Cognitive Load (47.748%), Tech Debt (82.8827%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 407.1)
  * `setFeatureListOptions` (Impact: 118.0)
  * `reloadConfig` (Impact: 26.7)
  * `Write` (Impact: 18.9)
    * *Intent:* // klogv1Writer is used in SetOutputBySeverity call below to redirect any calls // to klogv1 to end ...
  * `StartTime` (Impact: 18.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 250`, `structural_boundaries: 163`, `args: 48`, `func_start: 48`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 582`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 9`, `orphaned_logic: 11`
* *Architecture:* `io: 2`, `api: 92`, `concurrency: 48`, `import: 1`
* *Defense:* `safety: 42`, `doc: 75`, `sync_locks: 8`, `immutability_locks: 2`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` remote, BlockReloadInterval, go-conntrack, collectors, percentage, otlp-native-delta-ingestion, native-histograms, delayed-compaction...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `discovery/aws/rds.go` (GO | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.838 IQR)
- **Top Global Matches:** file_cluster_8: 13.838, file_cluster_0: 14.032, file_cluster_7: 14.043
- **Magnitude:** 1416.86 | **LOC:** 1000 | **CtrlFlow:** 80.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (62.9502%), Tech Debt (11.3344%)
**Top Internal Functions/Classes:**
  * `refresh` (Impact: 457.5)
  * `initRdsClient` (Impact: 32.5)
  * `describeAllDBClusters` (Impact: 20.8)
  * `describeDBClusters` (Impact: 17.4)
  * `describeDBInstances` (Impact: 15.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 216`, `structural_boundaries: 54`, `args: 11`, `func_start: 11`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 781`, `orphaned_logic: 4`
* *Architecture:* `api: 39`, `concurrency: 12`, `import: 1`
* *Defense:* `safety: 22`, `doc: 30`, `sync_locks: 9`, `immutability_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` model, strutil, context, config, rds, fmt, promslog, aws...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tsdb/head_wal.go` (GO | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.608 IQR)
- **Top Global Matches:** file_cluster_4: 14.608, file_cluster_8: 14.64, file_cluster_7: 14.804
- **Magnitude:** 1389.14 | **LOC:** 1876 | **CtrlFlow:** 69.4% | **Authorship Centralization:** 20.0%
- **Risk Profile:** Cognitive Load (45.1373%), Tech Debt (37.4196%)
**Top Internal Functions/Classes:**
  * `loadChunkSnapshot` (Impact: 156.0)
  * `ChunkSnapshot` (Impact: 49.8)
  * `loadWBL` (Impact: 46.4)
  * `LastChunkSnapshot` (Impact: 36.1)
  * `DeleteChunkSnapshots` (Impact: 33.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 295`, `structural_boundaries: 130`, `args: 23`, `func_start: 23`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 775`, `planned_debt: 6`, `orphaned_logic: 10`
* *Architecture:* `io: 1`, `api: 21`, `concurrency: 84`, `import: 1`
* *Defense:* `safety: 46`, `doc: 63`, `sync_locks: 11`, `immutability_locks: 3`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` metadata, tombstones, value, storage, fmt, mmap_markers, strings, oldmaxt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tsdb/head_append.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.189 IQR)
- **Top Global Matches:** file_cluster_8: 14.189, file_cluster_11: 14.231, file_cluster_7: 14.26
- **Magnitude:** 1328.98 | **LOC:** 2299 | **CtrlFlow:** 68.9% | **Authorship Centralization:** 27.3%
- **Risk Profile:** Cognitive Load (36.9325%), Tech Debt (96.0144%)
**Top Internal Functions/Classes:**
  * `appendableMinValidTime` (Impact: 166.7)
    * *Intent:* // appendableMinValidTime returns the minimum valid timestamp for appends, // such that samples stay...
  * `Commit` (Impact: 69.4)
  * `commitFloats` (Impact: 54.2)
  * `commitHistograms` (Impact: 45.0)
  * `commitFloatHistograms` (Impact: 45.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 222`, `structural_boundaries: 100`, `args: 36`, `func_start: 36`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 610`, `dead_code: 5`, `planned_debt: 10`, `duplicate_logic: 10`, `orphaned_logic: 5`
* *Architecture:* `api: 29`, `concurrency: 6`, `import: 1`
* *Defense:* `safety: 23`, `doc: 125`, `sync_locks: 22`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` metadata, slog, context, histogram, value, record, storage, fmt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `storage/remote/queue_manager.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.316 IQR)
- **Top Global Matches:** file_cluster_8: 13.316, file_cluster_7: 13.43, file_cluster_4: 13.487
- **Magnitude:** 1316.18 | **LOC:** 2321 | **CtrlFlow:** 53.7% | **Authorship Centralization:** 20.0%
- **Risk Profile:** Cognitive Load (37.8647%), Tech Debt (30.045%)
**Top Internal Functions/Classes:**
  * `sendMetadataWithBackoff` (Impact: 113.7)
  * `NewQueueManager` (Impact: 32.5)
    * *Intent:* // NewQueueManager builds a new QueueManager and starts a new // WAL watcher with queue manager as t...
  * `populateV2TimeSeries` (Impact: 28.9)
  * `calculateDesiredShards` (Impact: 23.8)
  * `updateShardsLoop` (Impact: 23.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 145`, `structural_boundaries: 125`, `args: 39`, `func_start: 39`, `class_start: 9`
* *Risk/State:* `state_mutation: 497`, `dead_code: 2`, `planned_debt: 4`, `orphaned_logic: 12`
* *Architecture:* `api: 180`, `concurrency: 72`, `import: 1`
* *Defense:* `safety: 26`, `doc: 89`, `sync_locks: 46`, `immutability_locks: 2`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` model, metadata, timePerSample, context, desiredShards, fmt, promslog, sample...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tsdb/chunkenc/histogram.go` (GO | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.3 IQR)
- **Top Global Matches:** file_cluster_8: 14.3, file_cluster_15: 14.375, file_cluster_7: 14.378
- **Magnitude:** 1290.66 | **LOC:** 1354 | **CtrlFlow:** 62.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (45.6753%), Tech Debt (82.6007%)
**Top Internal Functions/Classes:**
  * `expandIntSpansAndBuckets` (Impact: 250.8)
    * *Intent:* // appendable returns whether the chunk can be appended to, and if so whether // 1. Any recoding nee...
  * `AtHistogram` (Impact: 151.4)
  * `AtFloatHistogram` (Impact: 131.7)
  * `Next` (Impact: 45.1)
  * `appendable` (Impact: 18.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 65`, `args: 28`, `func_start: 28`, `class_start: 2`
* *Risk/State:* `state_mutation: 519`, `planned_debt: 1`, `duplicate_logic: 6`
* *Architecture:* `api: 63`, `import: 1`
* *Defense:* `safety: 17`, `doc: 74`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` binary, histogram, value, fmt, math, errors
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tsdb/db.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.973 IQR)
- **Top Global Matches:** file_cluster_8: 14.973, file_cluster_4: 14.978, file_cluster_7: 15.031
- **Magnitude:** 1239.2 | **LOC:** 2632 | **CtrlFlow:** 59.1% | **Authorship Centralization:** 15.8%
- **Risk Profile:** Cognitive Load (39.9605%), Tech Debt (50.3882%)
**Top Internal Functions/Classes:**
  * `compactOOOHead` (Impact: 132.3)
  * `run` (Impact: 64.7)
    * *Intent:* // FlushWAL creates a new block containing all data that's currently in the memory buffer/WAL.
  * `Compact` (Impact: 53.6)
  * `loadDataAsQueryable` (Impact: 53.3)
  * `ApplyConfig` (Impact: 34.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 105`, `args: 31`, `func_start: 31`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 524`, `dead_code: 1`, `planned_debt: 1`, `orphaned_logic: 13`
* *Architecture:* `api: 103`, `concurrency: 42`, `import: 1`
* *Defense:* `safety: 55`, `doc: 111`, `sync_locks: 31`, `immutability_locks: 1`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` block_range, context, io, v2, storage, fmt, promslog, strings...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `storage/remote/codec.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.997 IQR)
- **Top Global Matches:** file_cluster_8: 13.997, file_cluster_11: 14.09, file_cluster_15: 14.135
- **Magnitude:** 1109.14 | **LOC:** 1018 | **CtrlFlow:** 53.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (44.9174%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `Seek` (Impact: 59.3)
    * *Intent:* // Seek implements storage.SeriesIterator.
  * `StreamChunkedReadResponses` (Impact: 37.8)
    * *Intent:* // StreamChunkedReadResponses iterates over series, builds chunks and streams those to the caller. /...
  * `Next` (Impact: 29.7)
    * *Intent:* // Next implements chunkenc.Iterator.
  * `DecodeOTLPWriteRequest` (Impact: 28.6)
  * `setCurrentHistogram` (Impact: 26.9)
    * *Intent:* // setCurrentHistogram pre-fills either the curH or the curFH field with a // converted model histog...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 159`, `structural_boundaries: 136`, `args: 52`, `func_start: 52`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 525`, `dead_code: 1`, `planned_debt: 3`, `duplicate_logic: 32`, `orphaned_logic: 12`
* *Architecture:* `io: 5`, `api: 74`, `import: 1`
* *Defense:* `safety: 35`, `doc: 46`, `sync_locks: 1`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` model, pmetricotlp, io, storage, fmt, errors, prompb, http...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `discovery/aws/elasticache.go` (GO | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.935 IQR)
- **Top Global Matches:** file_cluster_8: 13.935, file_cluster_0: 14.029, file_cluster_7: 14.12
- **Magnitude:** 1050.54 | **LOC:** 908 | **CtrlFlow:** 73.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (39.4922%), Tech Debt (13.9801%)
**Top Internal Functions/Classes:**
  * `addCacheClusterTargets` (Impact: 157.7)
    * *Intent:* // addCacheClusterTargets adds targets for a cache cluster to the target group. // Creates one targe...
  * `addServerlessCacheTargets` (Impact: 66.7)
    * *Intent:* // addServerlessCacheTargets adds targets for a serverless cache to the target group.
  * `refresh` (Impact: 48.0)
  * `initElasticacheClient` (Impact: 32.5)
  * `splitCacheDeploymentOptions` (Impact: 25.1)
    * *Intent:* // splitCacheTypes takes a list of cache ARNs and splits them into serverless cache IDs and cache cl...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 171`, `structural_boundaries: 61`, `args: 14`, `func_start: 14`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 586`, `orphaned_logic: 5`
* *Architecture:* `api: 44`, `concurrency: 6`, `import: 1`
* *Defense:* `safety: 28`, `doc: 34`, `sync_locks: 18`, `immutability_locks: 1`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.555
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` model, strutil, context, config, fmt, promslog, strings, aws...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `discovery/azure/azure.go` (GO) | Magnitude: 749.02 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 545, state_mutation: 376, encapsulation: 158, branch: 134
- `discovery/aws/ecs.go` (GO) | Magnitude: 490.26 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 448, state_mutation: 345, encapsulation: 162, branch: 110
- `notifier/alert.go` (GO) | Magnitude: 67.06 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 46, state_mutation: 17, api: 16, doc: 15
- `discovery/zookeeper/zookeeper.go` (GO) | Magnitude: 0.05 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 49, structural_boundaries: 15, doc: 14, api: 12
- `model/relabel/relabel.go` (GO) | Magnitude: 430.28 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 239, state_mutation: 108, branch: 107, structural_boundaries: 51

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `promql/value.go` (GO) | Magnitude: 603.2 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 333, state_mutation: 248, structural_boundaries: 100, encapsulation: 94
- `discovery/discovery.go` (GO) | Magnitude: 108.36 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 50, state_mutation: 43, doc: 30, structural_boundaries: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `scripts/npm-deps.sh` (SHELL) | Magnitude: 1.35 | Delta: **0.129 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: reflection_metaprogramming: 7, safety: 5, state_mutation: 5, indent_spaces: 5
- `scripts/ui_release.sh` (SHELL) | Magnitude: 14.45 | Delta: **0.138 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: branch: 67, indent_spaces: 60, reflection_metaprogramming: 41, state_mutation: 35
- `discovery/registry.go` (GO) | Magnitude: 354.06 | Delta: **0.139 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 214, indent_tabs: 199, encapsulation: 69, branch: 51
- `scripts/generate_release_notes.sh` (SHELL) | Magnitude: 6.96 | Delta: **0.209 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 38, state_mutation: 33, reflection_metaprogramming: 31, branch: 27
- `scripts/sync_repo_files.sh` (SHELL) | Magnitude: 22.24 | Delta: **0.214 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 134, branch: 81, reflection_metaprogramming: 75, state_mutation: 69

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `web/ui/mantine-ui/src/components/Accordion/Accordion.context.ts` (TYPESCRIPT) | Magnitude: 3.85 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 10, args: 5, func_start: 5
- `web/ui/react-app/src/contexts/PathPrefixContext.tsx` (TYPESCRIPT) | Magnitude: 0.3 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, args: 1, func_start: 1, api: 1
- `web/ui/react-app/src/contexts/ReadyContext.tsx` (TYPESCRIPT) | Magnitude: 0.3 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, args: 1, func_start: 1, api: 1
- `util/runtime/statfs_windows.go` (GO) | Magnitude: 23.82 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 22, pointers: 11, state_mutation: 10, doc: 7
- `notifier/util.go` (GO) | Magnitude: 35.9 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 23, state_mutation: 20, encapsulation: 9, api: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `util/stats/timer.go` (GO) | Magnitude: 71.26 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 35, state_mutation: 29, structural_boundaries: 17, pointers: 17
- `discovery/discoverer_metrics_noop.go` (GO) | Magnitude: 8.36 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 9, structural_boundaries: 4, api: 3, pointers: 3
- `tsdb/chunkenc/chunk.go` (GO) | Magnitude: 269.48 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 190, structural_boundaries: 78, doc: 62, api: 52
- `tsdb/index/postings.go` (GO) | Magnitude: 280.64 | Delta: **0.076 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 175, state_mutation: 169, doc: 52, encapsulation: 52
- `model/labels/labels_common.go` (GO) | Magnitude: 245.22 | Delta: **0.091 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 132, state_mutation: 99, structural_boundaries: 37, branch: 33

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `util/zeropool/pool.go` (GO) | Magnitude: 42.4 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 26, state_mutation: 22, doc: 16, encapsulation: 8
- `web/api/testhelpers/assertions.go` (GO) | Magnitude: 155.18 | Delta: **0.11 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 136, encapsulation: 61, state_mutation: 58, pointers: 37
- `util/pool/pool.go` (GO) | Magnitude: 78.26 | Delta: **0.126 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 47, state_mutation: 30, branch: 14, doc: 10
- `util/testutil/cmp.go` (GO) | Magnitude: 19.26 | Delta: **0.24 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 16, state_mutation: 9, doc: 9, structural_boundaries: 4
- `web/ui/mantine-ui/src/components/Accordion/Accordion.types.ts` (TYPESCRIPT) | Magnitude: 1.56 | Delta: **0.289 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 8, api: 3, generics: 2, indent_spaces: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `scripts/get_module_version.sh` (SHELL) | Magnitude: 3.55 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 18, branch: 11, indent_spaces: 4, safety_bypasses: 3
- `web/ui/react-app/src/pages/graph/Graph.tsx` (TYPESCRIPT) | Magnitude: 23.83 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 210, state_mutation: 143, structural_boundaries: 48, args: 36
- `web/ui/react-app/src/pages/tsdbStatus/TSDBStatus.test.tsx` (TYPESCRIPT) | Magnitude: 11.13 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 166, concurrency: 49, args: 24, structural_boundaries: 23
- `web/ui/mantine-ui/src/components/EndpointLink.tsx` (TYPESCRIPT) | Magnitude: 1.31 | Delta: **0.04 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 43, structural_boundaries: 9, state_mutation: 9, branch: 8
- `web/ui/react-app/src/components/ToggleMoreLess.test.tsx` (TYPESCRIPT) | Magnitude: 1.3 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 19, args: 9, func_start: 9, structural_boundaries: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `web/ui/mantine-ui/src/components/CustomInfiniteScroll.tsx` (TYPESCRIPT) | Magnitude: 1.62 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 10, ui_framework: 9, args: 8
- `web/ui/react-app/src/App.tsx` (TYPESCRIPT) | Magnitude: 1.14 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 99, ui_framework: 31, generics: 31, structural_boundaries: 17
- `web/ui/react-app/src/Navbar.test.tsx` (TYPESCRIPT) | Magnitude: 0.96 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 8, args: 6, func_start: 6
- `web/ui/mantine-ui/src/pages/query/TreeNode.tsx` (TYPESCRIPT) | Magnitude: 6.64 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 277, structural_boundaries: 45, ui_framework: 38, branch: 35
- `web/ui/mantine-ui/src/pages/StatusPage.tsx` (TYPESCRIPT) | Magnitude: 3.51 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 73, structural_boundaries: 18, generics: 16, ui_framework: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `rules/group.go` (GO) | Magnitude: 776.64 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 572, state_mutation: 252, branch: 134, encapsulation: 134
- `util/testutil/context.go` (GO) | Magnitude: 45.84 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 18, indent_tabs: 18, api: 16, concurrency: 12
- `tsdb/head_wal.go` (GO) | Magnitude: 1389.14 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 914, state_mutation: 775, branch: 295, encapsulation: 277
- `web/ui/react-app/src/hooks/useFetch.ts` (TYPESCRIPT) | Magnitude: 19.56 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 83, structural_boundaries: 29, args: 23, func_start: 22
- `discovery/manager.go` (GO) | Magnitude: 152.24 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 149, state_mutation: 70, encapsulation: 54, structural_boundaries: 49

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `model/textparse/interface.go` (GO) | Magnitude: 68.36 | Delta: **0.117 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 61, doc: 42, state_mutation: 28, api: 17
- `storage/interface_append.go` (GO) | Magnitude: 38.72 | Delta: **0.167 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 32, doc: 29, structural_boundaries: 20, api: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `model/histogram/test_utils.go` (GO) | Magnitude: 65.54 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 41, indent_tabs: 29, api: 10, doc: 8
- `util/features/features.go` (GO) | Magnitude: 79.02 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 43, state_mutation: 28, doc: 28, api: 26
- `tsdb/goversion/goversion.go` (GO) | Magnitude: 12.04 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 7, structural_boundaries: 1, state_mutation: 1, explicit_casts: 1
- `tsdb/fileutil/mmap_386.go` (GO) | Magnitude: 12.04 | Delta: **0.081 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 6, structural_boundaries: 1, state_mutation: 1, immutability_locks: 1
- `tsdb/fileutil/mmap_amd64.go` (GO) | Magnitude: 12.04 | Delta: **0.081 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 6, structural_boundaries: 1, state_mutation: 1, immutability_locks: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `scripts/compress_assets.sh` (SHELL) | Magnitude: 2.52 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: io: 12, state_mutation: 12, branch: 7, structural_boundaries: 7
- `model/textparse/nhcbparse.go` (GO) | Magnitude: 371.48 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 216, state_mutation: 154, branch: 63, structural_boundaries: 45
- `web/api/v1/translate_ast.go` (GO) | Magnitude: 28.3 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 50, structural_boundaries: 23, state_mutation: 12, branch: 8
- `tsdb/head_read.go` (GO) | Magnitude: 493.78 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 276, state_mutation: 204, encapsulation: 89, structural_boundaries: 69
- `tsdb/db.go` (GO) | Magnitude: 1239.2 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 727, state_mutation: 524, encapsulation: 209, branch: 152

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `documentation/examples/Makefile` (MAKEFILE) | Magnitude: 16.12 | Delta: **0.11 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: api: 3, func_start: 2, indent_tabs: 2, io: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `cmd/prometheus/main.go` -> Churn: **96.15%** | Cog Load: 47.748% | Debt: 82.8827%
- `tsdb/db.go` -> Churn: **86.44%** | Cog Load: 39.9605% | Debt: 50.3882%
- `tsdb/head.go` -> Churn: **80.0%** | Cog Load: 45.1035% | Debt: 78.5537%
- `scrape/scrape.go` -> Churn: **71.36%** | Cog Load: 48.0038% | Debt: 70.5435%
- `config/config.go` -> Churn: **69.19%** | Cog Load: 29.9359% | Debt: 66.7809%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `discovery/aws/rds.go` -> **Matt** (100.0% isolated ownership) | Magnitude: 1416.86
- `prompb/io/prometheus/client/decoder.go` -> **Ben Kochie** (100.0% isolated ownership) | Magnitude: 984.78
- `tsdb/chunks/head_chunks.go` -> **Ben Kochie** (100.0% isolated ownership) | Magnitude: 951.6
- `model/textparse/protobufparse.go` -> **Ben Kochie** (100.0% isolated ownership) | Magnitude: 784.88
- `rules/group.go` -> **Ben Kochie** (100.0% isolated ownership) | Magnitude: 776.64

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

- `discovery/targetgroup/targetgroup.go` -> **Severity: 3469.3** (Blast Radius: 34.693 * Doc Risk: 100.0%)
- `storage/errors.go` -> **Severity: 3378.932** (Blast Radius: 38.533 * Doc Risk: 87.6893%)
- `discovery/http/http.go` -> **Severity: 1168.371** (Blast Radius: 12.279 * Doc Risk: 95.152%)
- `web/ui/mantine-ui/src/promql/utils.ts` -> **Severity: 865.5** (Blast Radius: 8.655 * Doc Risk: 100.0%)
- `discovery/refresh/refresh.go` -> **Severity: 581.137** (Blast Radius: 6.715 * Doc Risk: 86.5431%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
