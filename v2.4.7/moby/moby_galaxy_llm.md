# ARCHITECTURAL_BRIEF: moby
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/moby` |
| **Timestamp** | `2026-08-07T05:09:59.966442+00:00` |
| **Scan Duration** | `7.56s` |
| **Git Branch** | `master` |
| **Git Commit** | `d74daf1afe932c3579fc98ffc8f4378e5357c2a0` |
| **Git Remote** | `https://github.com/moby/moby` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1349 malicious artifacts.

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
| Total Artifacts | 12450 |
| Analyzed Artifacts (Scanned) | 2087 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 10363 |
| Total LOC | 118488 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 16.8% |
| Dominant Lang | GO |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4753 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3155 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.6591 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 49 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| GO | 1280 | 112600 | 61.3% |
| PLAINTEXT | 676 | 22 | 32.4% |
| MARKDOWN | 45 | 0 | 2.2% |
| SHELL | 40 | 2620 | 1.9% |
| DOCKERFILE | 15 | 861 | 0.7% |
| JSON | 12 | 1096 | 0.6% |
| PROTO | 6 | 177 | 0.3% |
| YAML | 5 | 81 | 0.2% |
| MAKEFILE | 3 | 283 | 0.1% |
| LUA | 2 | 136 | 0.1% |
| PYTHON | 1 | 163 | 0.0% |
| POWERSHELL | 1 | 448 | 0.0% |
| BINARY_THREAT | 1 | 1 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `3.509`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 841 | 40.3% |
| file_cluster_13 | 261 | 12.5% |
| file_cluster_4 | 89 | 4.3% |
| file_cluster_11 | 61 | 2.9% |
| file_cluster_0 | 60 | 2.9% |
| Unknown | 23 | 1.1% |
| file_cluster_16 | 14 | 0.7% |
| file_cluster_6 | 13 | 0.6% |
| file_cluster_7 | 8 | 0.4% |
| file_cluster_15 | 8 | 0.4% |
| file_cluster_17 | 4 | 0.2% |
| file_cluster_12 | 4 | 0.2% |
| file_cluster_9 | 2 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 699 | 33.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 10363*

**Composition by Extension & Reason:**
- `.go`: 8663x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Excluded (Machine-Generated Source Code Signature: 17 LOC), 4x Excluded (Machine-Generated Source Code Signature: 37 LOC)
- `no_extension`: 574x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Saturation: Line 1 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 2517 LOC)
- `.md`: 429x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Machine-Generated Source Code Signature: 50 LOC), 1x Excluded (Machine-Generated Source Code Signature: 36 LOC)
- `.yml`: 119x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.proto`: 92x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.s`: 85x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 54x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 13886 LOC)
- `.json`: 44x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 1593 LOC)
- `.txt`: 42x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 27x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 18 LOC)
- `.png`: 19x Excluded (Explicitly Denied Extension: '.png')
- `.toml`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Unsupported Extension: '.toml')
- `.c`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sum`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded (Unsupported Extension: '.sum')
- `.tar`: 8x Excluded (Explicitly Denied Extension: '.tar')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 30.4 | 31.6 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.9 | 64.5 | 75.5 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 57.8 | 74.5 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 18.5 | 2.5 | 80.0 |
| API Exposure | 0.0 | 18.3 | 3.6 | 2.3 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 8.2 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 77.2 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 92.1 | 1.4 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 90.6 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 30.4 | 1.5 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 6.6 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 37.0 | 19.6 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `contrib/dockerd-rootless-setuptool.sh` (Hits: 145)
- `contrib/download-frozen-image-v2.sh` (Hits: 124)
- `contrib/check-config.sh` (Hits: 87)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **context.go** (`internal/testutil/fakecontext/context.go`) — 642 inbound connections
2. **io.go** (`daemon/logger/internal/logdriver/io.go`) — 185 inbound connections
3. **net.go** (`daemon/libnetwork/internal/hashable/net.go`) — 137 inbound connections
4. **http.go** (`pkg/plugins/transport/http.go`) — 116 inbound connections
5. **driverapi.go** (`daemon/libnetwork/driverapi/driverapi.go`) — 36 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **names-generator.go** (`internal/namesgenerator/names-generator.go`) — 346 outbound dependencies
2. **daemon.go** (`daemon/daemon.go`) — 93 outbound dependencies
3. **stats_unix.go** (`daemon/stats_unix.go`) — 70 outbound dependencies
4. **daemon.go** (`daemon/command/daemon.go`) — 68 outbound dependencies
5. **controller.go** (`daemon/internal/builder-next/controller.go`) — 63 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `restore` (@ `daemon/daemon.go`) -> Impact: **430.3** | LOC: 1309
- `start` (@ `daemon/command/daemon.go`) -> Impact: **344.0** | LOC: 708
- `Anonymous_Block_[Truncated]` (@ `contrib/check-config.sh`) -> Impact: **339.1** | LOC: 389
- `Init` (@ `daemon/cluster/swarm.go`) -> Impact: **319.2** | LOC: 554
  * *Intent:* // Init initializes new cluster from user provided request.
- `NewDaemon` (@ `daemon/daemon.go`) -> Impact: **313.8** | LOC: 552
- `ServiceSpecToGRPC` (@ `daemon/cluster/convert/service.go`) -> Impact: **289.7** | LOC: 554
  * *Intent:* // ServiceSpecToGRPC converts a ServiceSpec to a grpc ServiceSpec.
- `UnmarshalJSON` (@ `daemon/libnetwork/endpoint.go`) -> Impact: **277.8** | LOC: 560
- `New` (@ `daemon/logger/awslogs/cloudwatchlogs.go`) -> Impact: **262.7** | LOC: 614
  * *Intent:* // New creates an awslogs logger using the configuration passed in on the // context. Supported context configuration variables are awslogs-region, //...
- `DeallocateService` (@ `daemon/libnetwork/cnmallocator/networkallocator.go`) -> Impact: **222.7** | LOC: 338
  * *Intent:* // In order to support backward compatibility with older daemon // versions which assumes the network attachment to contains // non nil IPAM attribute...
- `agentInit` (@ `daemon/libnetwork/agent.go`) -> Impact: **220.2** | LOC: 530

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `integration-cli/fixtures/https` | 10 | 50000.0 | 0.0% | 0.0% |
| `integration/testdata/https` | 5 | 25000.0 | 0.0% | 0.0% |
| `daemon` | 113 | 16012.8 | 35.32% | 65.98% |
| `client/testdata` | 3 | 15000.0 | 0.0% | 0.0% |
| `vendor/github.com/google/certificate-transparency-go/x509` | 2 | 10000.0 | 0.0% | 0.0% |
| `daemon/libnetwork` | 43 | 9319.3 | 30.45% | 87.33% |
| `daemon/containerd` | 34 | 6353.94 | 39.65% | 52.18% |
| `integration-cli/fixtures/registry` | 1 | 5000.0 | 0.0% | 0.0% |
| `vendor/github.com/moby/policy-helpers/roots/dhi` | 1 | 5000.0 | 0.0% | 0.0% |
| `client` | 127 | 4548.76 | 22.24% | 61.75% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `Dockerfile.simple` -> **100.0%** Exposure
- `api/pkg/authconfig/authconfig.go` -> **100.0%** Exposure
- `api/types/blkiodev/blkio.go` -> **100.0%** Exposure
- `api/types/common/error_response_ext.go` -> **100.0%** Exposure
- `api/types/container/hostconfig.go` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `api/pkg/stdcopy/stdcopy.go` -> **100.0%** Exposure
- `api/types/container/change_types.go` -> **100.0%** Exposure
- `api/types/events/events.go` -> **100.0%** Exposure
- `api/types/network/hwaddr.go` -> **100.0%** Exposure
- `api/types/network/network_types.go` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `errdefs/helpers.go` -> **1** Orphaned Functions | **50** Duplicates
- `integration/internal/container/ops.go` -> **43** Orphaned Functions | **0** Duplicates
- `daemon/server/router/swarm/cluster_routes.go` -> **30** Orphaned Functions | **0** Duplicates
- `daemon/libnetwork/drivers/ipvlan/ipvlan_store.go` -> **2** Orphaned Functions | **24** Duplicates
- `daemon/libnetwork/drivers/macvlan/macvlan_store.go` -> **2** Orphaned Functions | **24** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`Dockerfile`** -> AI Confidence: **99.48%**
2. **`daemon/libnetwork/cmd/diagnostic/main.go`** -> AI Confidence: **99.48%**
3. **`daemon/libnetwork/drivers/bridge/port_mapping_linux.go`** -> AI Confidence: **99.48%**
4. **`daemon/libnetwork/internal/resolvconf/resolvconf.go`** -> AI Confidence: **99.48%**
5. **`daemon/libnetwork/networkdb/cluster.go`** -> AI Confidence: **99.48%**
6. **`daemon/mounts.go`** -> AI Confidence: **99.48%**
7. **`daemon/server/router/swarm/helpers.go`** -> AI Confidence: **99.48%**
8. **`daemon/cluster/convert/container.go`** -> AI Confidence: **99.39%**
9. **`daemon/cluster/convert/service.go`** -> AI Confidence: **99.39%**
10. **`daemon/cluster/convert/swarm.go`** -> AI Confidence: **99.39%**
11. **`daemon/cluster/executor/container/container.go`** -> AI Confidence: **99.39%**
12. **`daemon/command/config.go`** -> AI Confidence: **99.39%**
13. **`daemon/containerd/registry_errors.go`** -> AI Confidence: **99.39%**
14. **`daemon/hosts.go`** -> AI Confidence: **99.39%**
15. **`daemon/image_store_choice.go`** -> AI Confidence: **99.39%**
16. **`daemon/images/image_list.go`** -> AI Confidence: **99.39%**
17. **`daemon/libnetwork/iptables/conntrack.go`** -> AI Confidence: **99.39%**
18. **`daemon/pkg/plugin/v2/plugin_linux.go`** -> AI Confidence: **99.39%**
19. **`internal/testutil/environment/clean.go`** -> AI Confidence: **99.39%**
20. **`daemon/libnetwork/cmd/ssd/ssd.py`** -> AI Confidence: **99.39%**
21. **`daemon/container_operations.go`** -> AI Confidence: **99.35%**
22. **`daemon/commit.go`** -> AI Confidence: **99.34%**
23. **`daemon/images/image_history.go`** -> AI Confidence: **99.34%**
24. **`daemon/libnetwork/drivers/bridge/internal/nftabler/port.go`** -> AI Confidence: **99.33%**
25. **`client/client.go`** -> AI Confidence: **99.31%**
26. **`client/container_create.go`** -> AI Confidence: **99.31%**
27. **`client/image_pull.go`** -> AI Confidence: **99.31%**
28. **`client/image_push.go`** -> AI Confidence: **99.31%**
29. **`client/internal/mod/mod.go`** -> AI Confidence: **99.31%**
30. **`client/pkg/jsonmessage/jsonmessage.go`** -> AI Confidence: **99.31%**
31. **`client/request.go`** -> AI Confidence: **99.31%**
32. **`client/service_create.go`** -> AI Confidence: **99.31%**
33. **`client/system_disk_usage.go`** -> AI Confidence: **99.31%**
34. **`cmd/docker-proxy/main_linux.go`** -> AI Confidence: **99.31%**
35. **`cmd/docker-proxy/udp_proxy_linux.go`** -> AI Confidence: **99.31%**
36. **`daemon/attach.go`** -> AI Confidence: **99.31%**
37. **`daemon/builder/dockerfile/builder.go`** -> AI Confidence: **99.31%**
38. **`daemon/builder/dockerfile/copy_windows.go`** -> AI Confidence: **99.31%**
39. **`daemon/builder/dockerfile/dispatchers.go`** -> AI Confidence: **99.31%**
40. **`daemon/builder/dockerfile/dispatchers_windows.go`** -> AI Confidence: **99.31%**
41. **`daemon/builder/dockerfile/internals_linux.go`** -> AI Confidence: **99.31%**
42. **`daemon/builder/dockerfile/internals_windows.go`** -> AI Confidence: **99.31%**
43. **`daemon/builder/remotecontext/detect.go`** -> AI Confidence: **99.31%**
44. **`daemon/builder/remotecontext/git/gitutils.go`** -> AI Confidence: **99.31%**
45. **`daemon/builder/remotecontext/remote.go`** -> AI Confidence: **99.31%**
46. **`daemon/cdi.go`** -> AI Confidence: **99.31%**
47. **`daemon/checkpoint.go`** -> AI Confidence: **99.31%**
48. **`daemon/cluster/executor/container/adapter.go`** -> AI Confidence: **99.31%**
49. **`daemon/cluster/executor/container/controller.go`** -> AI Confidence: **99.31%**
50. **`daemon/cluster/executor/container/executor.go`** -> AI Confidence: **99.31%**
51. **`daemon/cluster/filters.go`** -> AI Confidence: **99.31%**
52. **`daemon/cluster/networks.go`** -> AI Confidence: **99.31%**
53. **`daemon/cluster/noderunner.go`** -> AI Confidence: **99.31%**
54. **`daemon/cluster/services.go`** -> AI Confidence: **99.31%**
55. **`daemon/cluster/swarm.go`** -> AI Confidence: **99.31%**
56. **`daemon/cluster/tasks.go`** -> AI Confidence: **99.31%**
57. **`daemon/command/daemon.go`** -> AI Confidence: **99.31%**
58. **`daemon/command/daemon_unix.go`** -> AI Confidence: **99.31%**
59. **`daemon/command/options.go`** -> AI Confidence: **99.31%**
60. **`daemon/command/service_windows.go`** -> AI Confidence: **99.31%**
61. **`daemon/command/trap/testfiles/main.go`** -> AI Confidence: **99.31%**
62. **`daemon/config/config.go`** -> AI Confidence: **99.31%**
63. **`daemon/config/config_linux.go`** -> AI Confidence: **99.31%**
64. **`daemon/container.go`** -> AI Confidence: **99.31%**
65. **`daemon/container/container_windows.go`** -> AI Confidence: **99.31%**
66. **`daemon/container_operations_unix.go`** -> AI Confidence: **99.31%**
67. **`daemon/container_operations_windows.go`** -> AI Confidence: **99.31%**
68. **`daemon/containerd/image.go`** -> AI Confidence: **99.31%**
69. **`daemon/containerd/image_builder.go`** -> AI Confidence: **99.31%**
70. **`daemon/containerd/image_commit.go`** -> AI Confidence: **99.31%**
71. **`daemon/containerd/image_delete.go`** -> AI Confidence: **99.31%**
72. **`daemon/containerd/image_exporter.go`** -> AI Confidence: **99.31%**
73. **`daemon/containerd/image_history.go`** -> AI Confidence: **99.31%**
74. **`daemon/containerd/image_identity.go`** -> AI Confidence: **99.31%**
75. **`daemon/containerd/image_inspect.go`** -> AI Confidence: **99.31%**
76. **`daemon/containerd/image_list.go`** -> AI Confidence: **99.31%**
77. **`daemon/containerd/image_prune.go`** -> AI Confidence: **99.31%**
78. **`daemon/containerd/image_pull.go`** -> AI Confidence: **99.31%**
79. **`daemon/containerd/image_push.go`** -> AI Confidence: **99.31%**
80. **`daemon/containerd/image_snapshot.go`** -> AI Confidence: **99.31%**
81. **`daemon/containerd/image_tag.go`** -> AI Confidence: **99.31%**
82. **`daemon/containerd/migration/migration.go`** -> AI Confidence: **99.31%**
83. **`daemon/containerd/progress.go`** -> AI Confidence: **99.31%**
84. **`daemon/containerfs_linux.go`** -> AI Confidence: **99.31%**
85. **`daemon/create_unix.go`** -> AI Confidence: **99.31%**
86. **`daemon/daemon.go`** -> AI Confidence: **99.31%**
87. **`daemon/daemon_linux.go`** -> AI Confidence: **99.31%**
88. **`daemon/daemon_unix.go`** -> AI Confidence: **99.31%**
89. **`daemon/daemon_windows.go`** -> AI Confidence: **99.31%**
90. **`daemon/debugtrap_windows.go`** -> AI Confidence: **99.31%**
91. **`daemon/delete.go`** -> AI Confidence: **99.31%**
92. **`daemon/devices_nvidia_linux.go`** -> AI Confidence: **99.31%**
93. **`daemon/disk_usage.go`** -> AI Confidence: **99.31%**
94. **`daemon/events.go`** -> AI Confidence: **99.31%**
95. **`daemon/exec.go`** -> AI Confidence: **99.31%**
96. **`daemon/exec_linux.go`** -> AI Confidence: **99.31%**
97. **`daemon/graphdriver/copy/copy.go`** -> AI Confidence: **99.31%**
98. **`daemon/graphdriver/fuse-overlayfs/fuseoverlayfs.go`** -> AI Confidence: **99.31%**
99. **`daemon/graphdriver/overlay2/check.go`** -> AI Confidence: **99.31%**
100. **`daemon/graphdriver/overlay2/overlay.go`** -> AI Confidence: **99.31%**
101. **`daemon/graphdriver/overlayutils/randomid.go`** -> AI Confidence: **99.31%**
102. **`daemon/graphdriver/overlayutils/userxattr.go`** -> AI Confidence: **99.31%**
103. **`daemon/graphdriver/vfs/driver.go`** -> AI Confidence: **99.31%**
104. **`daemon/graphdriver/windows/windows.go`** -> AI Confidence: **99.31%**
105. **`daemon/graphdriver/zfs/zfs.go`** -> AI Confidence: **99.31%**
106. **`daemon/images/cache.go`** -> AI Confidence: **99.31%**
107. **`daemon/images/image.go`** -> AI Confidence: **99.31%**
108. **`daemon/images/image_builder.go`** -> AI Confidence: **99.31%**
109. **`daemon/images/image_delete.go`** -> AI Confidence: **99.31%**
110. **`daemon/images/image_inspect.go`** -> AI Confidence: **99.31%**
111. **`daemon/images/image_prune.go`** -> AI Confidence: **99.31%**
112. **`daemon/info.go`** -> AI Confidence: **99.31%**
113. **`daemon/info_unix.go`** -> AI Confidence: **99.31%**
114. **`daemon/initlayer/setup_unix.go`** -> AI Confidence: **99.31%**
115. **`daemon/inspect.go`** -> AI Confidence: **99.31%**
116. **`daemon/internal/builder-next/adapters/containerimage/pull.go`** -> AI Confidence: **99.31%**
117. **`daemon/internal/builder-next/controller.go`** -> AI Confidence: **99.31%**
118. **`daemon/internal/builder-next/executor_linux.go`** -> AI Confidence: **99.31%**
119. **`daemon/internal/builder-next/executor_windows.go`** -> AI Confidence: **99.31%**
120. **`daemon/internal/builder-next/exporter/mobyexporter/export.go`** -> AI Confidence: **99.31%**
121. **`daemon/internal/builder-next/exporter/mobyexporter/writer.go`** -> AI Confidence: **99.31%**
122. **`daemon/internal/builder-next/worker/worker.go`** -> AI Confidence: **99.31%**
123. **`daemon/internal/distribution/pull.go`** -> AI Confidence: **99.31%**
124. **`daemon/internal/distribution/pull_v2.go`** -> AI Confidence: **99.31%**
125. **`daemon/internal/distribution/pull_v2_unix.go`** -> AI Confidence: **99.31%**
126. **`daemon/internal/distribution/pull_v2_windows.go`** -> AI Confidence: **99.31%**
127. **`daemon/internal/distribution/push.go`** -> AI Confidence: **99.31%**
128. **`daemon/internal/distribution/push_v2.go`** -> AI Confidence: **99.31%**
129. **`daemon/internal/distribution/utils/progress.go`** -> AI Confidence: **99.31%**
130. **`daemon/internal/distribution/xfer/download.go`** -> AI Confidence: **99.31%**
131. **`daemon/internal/distribution/xfer/upload.go`** -> AI Confidence: **99.31%**
132. **`daemon/internal/filedescriptors/filiedescriptors_linux.go`** -> AI Confidence: **99.31%**
133. **`daemon/internal/image/cache/cache.go`** -> AI Confidence: **99.31%**
134. **`daemon/internal/image/tarexport/load.go`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `25` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `10407` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `daemon/internal/builder-next/builder.go` (GO) -> Cumulative Risk: **794.81**
- **Archetype:** `file_cluster_4` (Distance: 13.894 IQR)
- **Magnitude:** 808.08 | **LOC:** 723 | **CtrlFlow:** 49.8% | **Authorship Centralization:** 57.1%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.38%)
- **Heaviest Functions:** `Build` (Impact: 90.6), `toBuildkitPruneInfo` (Impact: 47.2), `DiskUsage` (Impact: 18.0)

### 2. `daemon/libnetwork/support/support.sh` (SHELL) -> Cumulative Risk: **706.95**
- **Archetype:** `file_cluster_12` (Distance: 13.483 IQR)
- **Magnitude:** 154.32 | **LOC:** 142 | **CtrlFlow:** 67.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (97.0452%)
- **Heaviest Functions:** `echo_and_run` (Impact: 62.6), `Anonymous_Block` (Impact: 6.4), `Anonymous_Block` (Impact: 5.3)

### 3. `daemon/attach.go` (GO) -> Cumulative Risk: **703.98**
- **Archetype:** `file_cluster_4` (Distance: 12.722 IQR)
- **Magnitude:** 217.86 | **LOC:** 218 | **CtrlFlow:** 63.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9868%), Safety Score (86.0593%)
- **Heaviest Functions:** `ContainerAttach` (Impact: 57.3), `containerAttach` (Impact: 41.4), `ContainerAttachRaw` (Impact: 2.0)

### 4. `daemon/events.go` (GO) -> Cumulative Risk: **701.62**
- **Archetype:** `file_cluster_8` (Distance: 12.901 IQR)
- **Magnitude:** 300.8 | **LOC:** 280 | **CtrlFlow:** 67.5% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (98.9242%), Safety Score (95.9758%)
- **Heaviest Functions:** `generateClusterEvent` (Impact: 30.5), `logServiceEvent` (Impact: 23.5), `logNodeEvent` (Impact: 22.0)

### 5. `daemon/libnetwork/networkdb/broadcast.go` (GO) -> Cumulative Risk: **695.48**
- **Archetype:** `file_cluster_8` (Distance: 12.092 IQR)
- **Magnitude:** 164.52 | **LOC:** 177 | **CtrlFlow:** 39.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9996%), Documentation (97.4227%)
- **Heaviest Functions:** `sendNodeEvent` (Impact: 16.5), `getBroadcasts` (Impact: 14.7), `Invalidates` (Impact: 7.5)

### 6. `client/pkg/streamformatter/streamformatter.go` (GO) -> Cumulative Risk: **692.92**
- **Archetype:** `file_cluster_8` (Distance: 12.535 IQR)
- **Magnitude:** 187.28 | **LOC:** 217 | **CtrlFlow:** 44.6% | **Authorship Centralization:** 70.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (99.9341%)
- **Heaviest Functions:** `rawProgressString` (Impact: 36.5), `WriteProgress` (Impact: 10.6), `formatProgress` (Impact: 8.2)

### 7. `daemon/internal/builder-next/executor.go` (GO) -> Cumulative Risk: **691.54**
- **Archetype:** `file_cluster_4` (Distance: 12.804 IQR)
- **Magnitude:** 127.06 | **LOC:** 122 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9998%), Tech Debt (99.9997%)
- **Heaviest Functions:** `Close` (Impact: 9.6), `getDNSConfig` (Impact: 8.5), `ipAddresses` (Impact: 8.4)

### 8. `hack/make.ps1` (POWERSHELL) -> Cumulative Risk: **689.11**
- **Archetype:** `file_cluster_11` (Distance: 13.661 IQR)
- **Magnitude:** 579.36 | **LOC:** 593 | **CtrlFlow:** 89.5% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `Execute-Build` (Impact: 71.4), `Run-IntegrationTests` (Impact: 22.8), `Run-UnitTests` (Impact: 19.4)

### 9. `daemon/internal/stream/streams.go` (GO) -> Cumulative Risk: **687.88**
- **Archetype:** `file_cluster_4` (Distance: 13.896 IQR)
- **Magnitude:** 178.42 | **LOC:** 186 | **CtrlFlow:** 48.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9999%), Tech Debt (99.9278%)
- **Heaviest Functions:** `CopyToPipe` (Impact: 33.9), `Wait` (Impact: 13.0), `CloseStreams` (Impact: 12.2)

### 10. `integration-cli/cli/cli.go` (GO) -> Cumulative Risk: **684.33**
- **Archetype:** `file_cluster_8` (Distance: 12.707 IQR)
- **Magnitude:** 194.3 | **LOC:** 204 | **CtrlFlow:** 45.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Tech Debt (99.9974%), Concurrency (96.5555%)
- **Heaviest Functions:** `waitForInspectResult` (Impact: 36.1), `validateArgs` (Impact: 16.8), `Docker` (Impact: 9.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `client/testdata/ca.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/testdata/cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/testdata/key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `integration-cli/fixtures/https/ca-rogue.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-cli/fixtures/https/ca.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-cli/fixtures/https/client-cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-cli/fixtures/https/client-key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-cli/fixtures/https/client-rogue-cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-cli/fixtures/https/client-rogue-key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-cli/fixtures/https/server-cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-cli/fixtures/https/server-key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-cli/fixtures/https/server-rogue-cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-cli/fixtures/https/server-rogue-key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-cli/fixtures/registry/cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/testdata/https/ca.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/testdata/https/client-cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/testdata/https/client-key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/testdata/https/server-cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/testdata/https/server-key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vendor/github.com/google/certificate-transparency-go/x509/test-dir.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vendor/github.com/google/certificate-transparency-go/x509/test-file.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vendor/github.com/moby/policy-helpers/roots/dhi/dhi.pub` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `daemon/daemon.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.14 IQR)
- **Top Global Matches:** file_cluster_11: 15.14, file_cluster_4: 15.161, file_cluster_8: 15.198
- **Magnitude:** 1989.04 | **LOC:** 1908 | **CtrlFlow:** 62.0% | **Authorship Centralization:** 39.3%
- **Risk Profile:** Cognitive Load (48.5711%), Tech Debt (15.8191%)
**Top Internal Functions/Classes:**
  * `restore` (Impact: 430.3)
  * `NewDaemon` (Impact: 313.8)
  * `Shutdown` (Impact: 120.5)
  * `networkOptions` (Impact: 41.5)
  * `loadContainers` (Impact: 19.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 263`, `structural_boundaries: 161`, `args: 45`, `func_start: 45`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 662`, `dead_code: 2`, `planned_debt: 16`, `fragile_debt: 1`
* *Architecture:* `io: 4`, `api: 104`, `concurrency: 55`, `import: 1`
* *Defense:* `safety: 94`, `doc: 88`, `sync_locks: 30`, `immutability_locks: 1`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` tracing, restarting, registry, maps, ipbits, client, cluster, sync...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `daemon/libnetwork/network.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.569 IQR)
- **Top Global Matches:** file_cluster_11: 14.569, file_cluster_15: 14.742, file_cluster_8: 14.785
- **Magnitude:** 1872.28 | **LOC:** 2208 | **CtrlFlow:** 51.5% | **Authorship Centralization:** 30.0%
- **Risk Profile:** Cognitive Load (45.1825%), Tech Debt (75.3499%)
**Top Internal Functions/Classes:**
  * `UnmarshalJSON` (Impact: 101.6)
  * `validateConfiguration` (Impact: 63.0)
  * `delete` (Impact: 41.3)
    * *Intent:* // NetworkOptionDriverOpts function returns an option setter for any driver parameter described by a...
  * `applyConfigurationTo` (Impact: 36.5)
  * `CopyTo` (Impact: 30.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 257`, `structural_boundaries: 242`, `args: 77`, `func_start: 77`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 948`, `dead_code: 2`, `planned_debt: 24`, `fragile_debt: 2`, `duplicate_logic: 6`
* *Architecture:* `api: 130`, `import: 1`
* *Defense:* `safety: 52`, `doc: 68`, `sync_locks: 77`, `immutability_locks: 1`, `cleanup: 38`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` error, netip, netutils, maps, otel, errdefs, stringid, scope...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `daemon/network.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.787 IQR)
- **Top Global Matches:** file_cluster_11: 14.787, file_cluster_8: 14.788, file_cluster_4: 14.797
- **Magnitude:** 1457.58 | **LOC:** 1237 | **CtrlFlow:** 66.5% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (48.3677%), Tech Debt (15.1901%)
**Top Internal Functions/Classes:**
  * `deleteNetwork` (Impact: 128.3)
  * `buildCreateEndpointOptions` (Impact: 75.9)
  * `buildIPAMResources` (Impact: 57.5)
  * `createNetwork` (Impact: 56.1)
  * `clearAttachableNetworks` (Impact: 30.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 216`, `structural_boundaries: 109`, `args: 39`, `func_start: 39`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 705`, `dead_code: 1`, `planned_debt: 12`
* *Architecture:* `api: 56`, `concurrency: 36`, `import: 1`
* *Defense:* `safety: 37`, `doc: 45`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` error, opts, netip, maps, backend, events, errdefs, sort...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `daemon/containerd/image_list.go` (GO) | Magnitude: 479.02 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 371, state_mutation: 274, encapsulation: 114, branch: 91
- `daemon/config/config_windows.go` (GO) | Magnitude: 47.9 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 30, structural_boundaries: 15, api: 12, doc: 10
- `api/types/auxprogress/push.go` (GO) | Magnitude: 22.26 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 7, api: 7, doc: 7, indent_tabs: 6
- `daemon/libnetwork/netlabel/labels.go` (GO) | Magnitude: 45.74 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: api: 22, indent_tabs: 22, state_mutation: 21, doc: 21
- `client/container_restart.go` (GO) | Magnitude: 22.72 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 22, structural_boundaries: 10, state_mutation: 9, doc: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `daemon/network.go` (GO) | Magnitude: 1457.58 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 705, indent_tabs: 685, branch: 216, encapsulation: 205
- `daemon/libnetwork/store.go` (GO) | Magnitude: 177.54 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 97, state_mutation: 84, branch: 30, pointers: 23
- `client/request.go` (GO) | Magnitude: 160.92 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 126, state_mutation: 73, branch: 40, encapsulation: 37
- `daemon/cluster/services.go` (GO) | Magnitude: 525.86 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 374, state_mutation: 280, branch: 102, encapsulation: 87
- `daemon/images/image_commit.go` (GO) | Magnitude: 109.46 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 94, state_mutation: 63, structural_boundaries: 21, branch: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `hack/make.sh` (SHELL) | Magnitude: 140.44 | Delta: **0.08 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 64, branch: 54, state_mutation: 45, reflection_metaprogramming: 23
- `hack/make/run` (SHELL) | Magnitude: 108.36 | Delta: **0.109 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 60, indent_tabs: 45, branch: 36, reflection_metaprogramming: 14
- `hack/dockerfile/cli.sh` (SHELL) | Magnitude: 30.5 | Delta: **0.21 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 14, state_mutation: 13, reflection_metaprogramming: 11, branch: 10
- `daemon/libnetwork/support/support.sh` (SHELL) | Magnitude: 154.32 | Delta: **0.261 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: reflection_metaprogramming: 76, state_mutation: 67, indent_tabs: 67, io: 56

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `client/image_push_opts.go` (GO) | Magnitude: 20.22 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 6, indent_tabs: 6, structural_boundaries: 5, api: 5
- `client/volume_prune.go` (GO) | Magnitude: 31.58 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 30, state_mutation: 15, structural_boundaries: 11, api: 6
- `client/service_update.go` (GO) | Magnitude: 87.02 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 62, state_mutation: 50, branch: 15, encapsulation: 14
- `daemon/command/docker_windows.go` (GO) | Magnitude: 24.2 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 20, state_mutation: 12, structural_boundaries: 6, branch: 5
- `daemon/pkg/opts/ulimit.go` (GO) | Magnitude: 80.74 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 35, state_mutation: 33, structural_boundaries: 20, api: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `pkg/authorization/response.go` (GO) | Magnitude: 138.38 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 88, state_mutation: 51, doc: 29, encapsulation: 29
- `internal/testutil/registry/ops.go` (GO) | Magnitude: 22.52 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 14, pointers: 9, closures: 8, structural_boundaries: 6
- `daemon/builder/remotecontext/internal/tarsum/fileinfosums.go` (GO) | Magnitude: 130.66 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 55, state_mutation: 40, structural_boundaries: 27, branch: 18
- `daemon/logger/journald/internal/sdjournal/sdjournal.go` (GO) | Magnitude: 205.76 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 110, state_mutation: 81, structural_boundaries: 42, pointers: 30
- `daemon/pkg/plugin/v2/plugin.go` (GO) | Magnitude: 264.9 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 145, state_mutation: 70, branch: 42, structural_boundaries: 39

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `daemon/internal/streamformatter/streamformatter.go` (GO) | Magnitude: 128.88 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 92, state_mutation: 65, structural_boundaries: 29, encapsulation: 26
- `internal/iterutil/iterutil.go` (GO) | Magnitude: 93.4 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 50, state_mutation: 33, branch: 23, structural_boundaries: 15
- `daemon/libnetwork/discoverapi/discoverapi.go` (GO) | Magnitude: 37.56 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: api: 19, indent_tabs: 16, doc: 13, structural_boundaries: 10
- `internal/sliceutil/sliceutil.go` (GO) | Magnitude: 77.18 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 42, indent_tabs: 30, structural_boundaries: 11, branch: 10
- `client/pkg/progress/progress.go` (GO) | Magnitude: 45.02 | Delta: **0.075 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 20, structural_boundaries: 16, api: 16, doc: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `daemon/internal/builder-next/worker/mod/mod.go` (GO) | Magnitude: 57.24 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 36, state_mutation: 25, branch: 13, encapsulation: 11
- `contrib/dockerd-rootless-setuptool.sh` (SHELL) | Magnitude: 4.41 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 384, branch: 194, state_mutation: 175, io: 145
- `daemon/server/router/volume/volume_routes.go` (GO) | Magnitude: 175.94 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 112, state_mutation: 75, branch: 32, structural_boundaries: 30
- `daemon/builder/dockerfile/internals_linux.go` (GO) | Magnitude: 69.98 | Delta: **0.106 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 52, state_mutation: 30, structural_boundaries: 14, branch: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `integration/plugin/logging/cmd/discard/driver.go` (GO) | Magnitude: 54.26 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 56, state_mutation: 22, structural_boundaries: 19, encapsulation: 16
- `daemon/cluster/swarm.go` (GO) | Magnitude: 924.94 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 443, state_mutation: 330, branch: 118, encapsulation: 91
- `daemon/stats/collector.go` (GO) | Magnitude: 98.72 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 74, state_mutation: 38, encapsulation: 24, structural_boundaries: 15
- `daemon/libnetwork/cluster/provider.go` (GO) | Magnitude: 29.52 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 18, structural_boundaries: 6, api: 6, doc: 6
- `daemon/logger/local/read.go` (GO) | Magnitude: 80.04 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 62, state_mutation: 31, branch: 17, structural_boundaries: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `daemon/libnetwork/drivers/overlay/ov_network.go` (GO) | Magnitude: 438.52 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 297, state_mutation: 196, encapsulation: 80, branch: 78
- `daemon/libnetwork/ns/init_linux.go` (GO) | Magnitude: 98.26 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 67, state_mutation: 49, encapsulation: 30, branch: 15
- `daemon/libnetwork/networkdb/delegate.go` (GO) | Magnitude: 315.52 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 276, state_mutation: 147, encapsulation: 86, branch: 72
- `daemon/libnetwork/networkdb/cluster.go` (GO) | Magnitude: 545.98 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 326, state_mutation: 276, encapsulation: 137, branch: 96
- `daemon/network/network_mode.go` (GO) | Magnitude: 5.3 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, api: 2, doc: 2, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `daemon/logger/local/doc.go` (GO) | Magnitude: 10.52 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 5, structural_boundaries: 1
- `daemon/libnetwork/drivers/bridge/labels.go` (GO) | Magnitude: 33.24 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: api: 9, state_mutation: 9, doc: 9, indent_tabs: 9
- `cmd/dockerd/winresources/winresources.go` (GO) | Magnitude: 10.52 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 3, structural_boundaries: 1, fragile_debt: 1
- `daemon/libnetwork/drivers/windows/labels.go` (GO) | Magnitude: 49.4 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: api: 17, state_mutation: 17, doc: 17, indent_tabs: 17
- `api/types/types.go` (GO) | Magnitude: 29.2 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 9, api: 7, state_mutation: 7, indent_tabs: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `daemon/errors.go` (GO) | Magnitude: 100.0 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 65, structural_boundaries: 37, encapsulation: 32, args: 22
- `daemon/internal/progress/progress.go` (GO) | Magnitude: 40.02 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 20, structural_boundaries: 16, api: 16, doc: 10
- `daemon/command/daemon_unix.go` (GO) | Magnitude: 127.02 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 77, state_mutation: 57, encapsulation: 23, structural_boundaries: 20
- `daemon/container/archive_windows.go` (GO) | Magnitude: 56.36 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 46, state_mutation: 27, structural_boundaries: 12, encapsulation: 10
- `internal/testutil/specialimage/partial.go` (GO) | Magnitude: 61.66 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 36, state_mutation: 34, api: 11, structural_boundaries: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `daemon/container/rwlayer.go` (GO) | Magnitude: 14.12 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: structural_boundaries: 4, doc: 4, indent_tabs: 3, class_start: 1
- `daemon/internal/quota/projectquota_unsupported.go` (GO) | Magnitude: 8.5 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 4, pointers: 4, args: 3, func_start: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `Dockerfile` -> Churn: **100.0%** | Cog Load: 78.3828% | Debt: 99.9995%
- `client/client.go` -> Churn: **81.43%** | Cog Load: 40.5348% | Debt: 86.2812%
- `daemon/server/router/container/container_routes.go` -> Churn: **78.3%** | Cog Load: 41.1431% | Debt: 95.6508%
- `daemon/server/router/system/system_routes.go` -> Churn: **68.41%** | Cog Load: 44.5529% | Debt: 92.4142%
- `daemon/server/router/image/image_routes.go` -> Churn: **61.96%** | Cog Load: 55.9796% | Debt: 92.1369%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `daemon/cluster/swarm.go` -> **Cory Snider** (100.0% isolated ownership) | Magnitude: 924.94
- `daemon/cluster/convert/container.go` -> **Cory Snider** (100.0% isolated ownership) | Magnitude: 744.7
- `daemon/cluster/executor/container/adapter.go` -> **Sebastiaan van Stijn** (100.0% isolated ownership) | Magnitude: 738.02
- `daemon/cluster/executor/container/controller.go` -> **Austin Vazquez** (100.0% isolated ownership) | Magnitude: 717.4
- `daemon/internal/nri/nri.go` -> **Rob Murray** (100.0% isolated ownership) | Magnitude: 697.16

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `daemon/logger/internal/logdriver/io.go` -> **Severity: 0.05** (Bridge: 0.0005 * Flux: 100.0%)
- `hack/make/binary` -> **Severity: 0.034** (Bridge: 0.0003 * Flux: 99.8875%)
- `internal/testutil/fakecontext/context.go` -> **Severity: 0.026** (Bridge: 0.0003 * Flux: 85.0%)
- `daemon/server/httputils/httputils.go` -> **Severity: 0.014** (Bridge: 0.0001 * Flux: 99.9969%)
- `daemon/cdi.go` -> **Severity: 0.005** (Bridge: 0.0 * Flux: 100.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `hack/make/binary` -> **Severity: 6180.43** (Blast Radius: 241.851 * Doc Risk: 25.5547%)
- `internal/testutil/fakecontext/context.go` -> **Severity: 6002.45** (Blast Radius: 63.681 * Doc Risk: 94.2581%)
- `hack/make/binary-proxy` -> **Severity: 5713.835** (Blast Radius: 103.366 * Doc Risk: 55.2777%)
- `daemon/logger/internal/logdriver/io.go` -> **Severity: 4694.045** (Blast Radius: 76.159 * Doc Risk: 61.6348%)
- `hack/make/binary-daemon` -> **Severity: 4576.664** (Blast Radius: 103.366 * Doc Risk: 44.2763%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
