# ARCHITECTURAL_BRIEF: moby
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/moby` |
| **Timestamp** | `2026-08-03T21:06:45.734067+00:00` |
| **Scan Duration** | `7.69s` |
| **Git Branch** | `master` |
| **Git Commit** | `d74daf1afe932c3579fc98ffc8f4378e5357c2a0` |
| **Git Remote** | `https://github.com/moby/moby` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1349 malicious artifacts.

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
| Modularity | 0.4754 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
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
> **Architectural Drift Z-Score:** `3.51`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 841 | 40.3% |
| file_cluster_13 | 262 | 12.6% |
| file_cluster_4 | 88 | 4.2% |
| file_cluster_0 | 60 | 2.9% |
| file_cluster_11 | 60 | 2.9% |
| Unknown | 23 | 1.1% |
| file_cluster_16 | 14 | 0.7% |
| file_cluster_6 | 13 | 0.6% |
| file_cluster_7 | 8 | 0.4% |
| file_cluster_15 | 8 | 0.4% |
| file_cluster_12 | 5 | 0.2% |
| file_cluster_17 | 4 | 0.2% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 30.3 | 31.6 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.9 | 63.5 | 74.7 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 56.7 | 70.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 22.2 | 2.5 | 80.0 |
| API Exposure | 0.0 | 18.3 | 3.6 | 2.3 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 8.3 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 77.2 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 92.1 | 1.4 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 90.6 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 30.4 | 1.5 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 6.6 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 43.6 | 27.1 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 0.6 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.8 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
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

- `restore` (@ `daemon/daemon.go`) -> Impact: **1613.5** | LOC: 1309
- `start` (@ `daemon/command/daemon.go`) -> Impact: **652.7** | LOC: 708
- `RUN` (@ `Dockerfile`) -> Impact: **512.8** | LOC: 556
  * *Intent:* # Disable collecting local telemetry, as collected by Go and Delve; # # - https://github.com/go-delve/delve/blob/v1.24.1/CHANGELOG.md#1231-2024-09-23 ...
- `New` (@ `daemon/logger/awslogs/cloudwatchlogs.go`) -> Impact: **494.7** | LOC: 614
  * *Intent:* // New creates an awslogs logger using the configuration passed in on the // context. Supported context configuration variables are awslogs-region, //...
- `Init` (@ `daemon/cluster/swarm.go`) -> Impact: **464.9** | LOC: 554
  * *Intent:* // Init initializes new cluster from user provided request.
- `check_iptables` (@ `daemon/libnetwork/cmd/ssd/ssd.py`) -> Impact: **400.4** | LOC: 110
- `agentInit` (@ `daemon/libnetwork/agent.go`) -> Impact: **332.8** | LOC: 530
- `ServiceSpecToGRPC` (@ `daemon/cluster/convert/service.go`) -> Impact: **289.7** | LOC: 554
  * *Intent:* // ServiceSpecToGRPC converts a ServiceSpec to a grpc ServiceSpec.
- `UnmarshalJSON` (@ `daemon/libnetwork/endpoint.go`) -> Impact: **277.8** | LOC: 560
- `Execute-Build` (@ `hack/make.ps1`) -> Impact: **225.7** | LOC: 86
  * *Intent:* # Build a binary (client or daemon)

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `check_iptables` (@ `daemon/libnetwork/cmd/ssd/ssd.py`) -> **O(2^N) [Recursive]**
- `RUN` (@ `Dockerfile`) -> **O(2^N) [Recursive]**
  * *Intent:* # Disable collecting local telemetry, as collected by Go and Delve; # # - https://github.com/go-delve/delve/blob/v1.24.1/CHANGELOG.md#1231-2024-09-23 ...
- `RUN` (@ `contrib/busybox/Dockerfile`) -> **O(2^N) [Recursive]**
- `restore` (@ `daemon/daemon.go`) -> **O(2^N) [Recursive]**
- `Exec` (@ `daemon/internal/libcontainerd/remote/client.go`) -> **O(2^N) [Recursive]**
- `invalid` (@ `api/pkg/authconfig/authconfig.go`) -> **O(2^N) [Recursive]**
- `Error` (@ `api/types/jsonstream/json_error.go`) -> **O(2^N) [Recursive]**
- `Copy` (@ `api/types/network/endpoint.go`) -> **O(2^N) [Recursive]**
  * *Intent:* // Copy makes a deep copy of `EndpointSettings`
- `String` (@ `api/types/network/hwaddr.go`) -> **O(2^N) [Recursive]**
- `Port` (@ `api/types/network/port.go`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `Anonymous_Block_[Truncated]` (@ `contrib/download-frozen-image-v2.sh`) -> DB Complexity: **432**
- `init` (@ `contrib/dockerd-rootless-setuptool.sh`) -> DB Complexity: **388**
  * *Intent:* # run checks and also initialize global vars
- `Anonymous_Block_[Truncated]` (@ `contrib/check-config.sh`) -> DB Complexity: **299**
- `restore` (@ `daemon/daemon.go`) -> DB Complexity: **235**
- `RUN` (@ `Dockerfile`) -> DB Complexity: **226**
  * *Intent:* # Disable collecting local telemetry, as collected by Go and Delve; # # - https://github.com/go-delve/delve/blob/v1.24.1/CHANGELOG.md#1231-2024-09-23 ...
- `UnmarshalJSON` (@ `daemon/libnetwork/endpoint.go`) -> DB Complexity: **193**
- `echo_and_run` (@ `daemon/libnetwork/support/support.sh`) -> DB Complexity: **180**
- `start` (@ `daemon/command/daemon.go`) -> DB Complexity: **141**
- `ServiceSpecToGRPC` (@ `daemon/cluster/convert/service.go`) -> DB Complexity: **122**
  * *Intent:* // ServiceSpecToGRPC converts a ServiceSpec to a grpc ServiceSpec.
- `Init` (@ `daemon/cluster/swarm.go`) -> DB Complexity: **115**
  * *Intent:* // Init initializes new cluster from user provided request.

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `integration-cli/fixtures/https` | 10 | 50000.0 | 0.0% | 0.0% |
| `integration/testdata/https` | 5 | 25000.0 | 0.0% | 0.0% |
| `daemon` | 113 | 17021.8 | 35.54% | 64.95% |
| `client/testdata` | 3 | 15000.0 | 0.0% | 0.0% |
| `vendor/github.com/google/certificate-transparency-go/x509` | 2 | 10000.0 | 0.0% | 0.0% |
| `daemon/libnetwork` | 43 | 9251.8 | 30.41% | 84.87% |
| `daemon/containerd` | 34 | 7132.54 | 39.65% | 51.76% |
| `integration-cli/fixtures/registry` | 1 | 5000.0 | 0.0% | 0.0% |
| `vendor/github.com/moby/policy-helpers/roots/dhi` | 1 | 5000.0 | 0.0% | 0.0% |
| `client` | 127 | 4811.16 | 22.24% | 61.16% |

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

### Exploit Generation Surface
- `daemon/command/daemon.go` -> **100.0%** Exposure
- `daemon/daemon_unix.go` -> **100.0%** Exposure
- `daemon/libnetwork/cmd/ssd/ssd.py` -> **100.0%** Exposure
- `daemon/cluster/executor/container/container.go` -> **99.9999%** Exposure
- `daemon/pkg/plugin/backend_linux.go` -> **99.9317%** Exposure
### Weaponizable Injection Vectors
- `daemon/libnetwork/iptables/iptables.go` -> **100.0%** Exposure
- `contrib/dockerd-rootless-setuptool.sh` -> **100.0%** Exposure
- `contrib/dockerize-disk.sh` -> **100.0%** Exposure
- `contrib/nuke-graph-directory.sh` -> **100.0%** Exposure
- `hack/make/binary-daemon` -> **99.9999%** Exposure
### Algorithmic DoS Exposure
- `Dockerfile` -> **100.0%** Exposure
- `daemon/cluster/swarm.go` -> **100.0%** Exposure
- `daemon/daemon.go` -> **100.0%** Exposure
- `internal/testutil/registry/registry.go` -> **100.0%** Exposure
- `contrib/download-frozen-image-v2.sh` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `25` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `10407` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `daemon/internal/builder-next/builder.go` (GO) -> Cumulative Risk: **794.81**
- **Archetype:** `file_cluster_4` (Distance: 13.898 IQR)
- **Magnitude:** 886.38 | **LOC:** 723 | **CtrlFlow:** 49.8% | **Authorship Centralization:** 57.1%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.38%)
- **Heaviest Functions:** `Build` (Impact: 108.4), `toBuildkitPruneInfo` (Impact: 47.2), `DiskUsage` (Impact: 40.5)

### 2. `hack/make.ps1` (POWERSHELL) -> Cumulative Risk: **788.07**
- **Archetype:** `file_cluster_11` (Distance: 13.657 IQR)
- **Magnitude:** 772.56 | **LOC:** 593 | **CtrlFlow:** 84.9% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `Execute-Build` (Impact: 225.7), `Run-IntegrationTests` (Impact: 43.6), `Run-UnitTests` (Impact: 19.4)

### 3. `hack/make.sh` (SHELL) -> Cumulative Risk: **749.23**
- **Archetype:** `file_cluster_12` (Distance: 13.317 IQR)
- **Magnitude:** 110.54 | **LOC:** 143 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Injection Surface (99.9925%)
- **Heaviest Functions:** `Anonymous_Block_[Truncated]` (Impact: 54.5), `__global_context__` (Impact: 4.1)

### 4. `daemon/pkg/plugin/backend_linux.go` (GO) -> Cumulative Risk: **746.93**
- **Archetype:** `file_cluster_4` (Distance: 14.371 IQR)
- **Magnitude:** 730.0 | **LOC:** 851 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 60.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (99.9317%), Safety Score (94.2081%)
- **Heaviest Functions:** `Push` (Impact: 98.4), `Privileges` (Impact: 69.3), `List` (Impact: 48.6)

### 5. `daemon/daemon.go` (GO) -> Cumulative Risk: **738.31**
- **Archetype:** `file_cluster_11` (Distance: 15.147 IQR)
- **Magnitude:** 2477.34 | **LOC:** 1908 | **CtrlFlow:** 62.0% | **Authorship Centralization:** 39.3%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Safety Score (92.2375%)
- **Heaviest Functions:** `restore` (Impact: 1613.5), `loadContainers` (Impact: 19.5), `Config` (Impact: 4.6)

### 6. `daemon/command/service_windows.go` (GO) -> Cumulative Risk: **735.82**
- **Archetype:** `file_cluster_4` (Distance: 13.566 IQR)
- **Magnitude:** 424.1 | **LOC:** 395 | **CtrlFlow:** 52.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9565%), Safety Score (94.8769%)
- **Heaviest Functions:** `Fire` (Impact: 42.7), `Execute` (Impact: 25.9), `initService` (Impact: 25.7)

### 7. `daemon/info.go` (GO) -> Cumulative Risk: **734.34**
- **Archetype:** `file_cluster_11` (Distance: 14.238 IQR)
- **Magnitude:** 482.68 | **LOC:** 415 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (99.9924%), Tech Debt (98.1139%)
- **Heaviest Functions:** `fillDiscoveredDevicesFromDrivers` (Impact: 45.7), `operatingSystem` (Impact: 33.0), `fillAPIInfo` (Impact: 32.3)

### 8. `daemon/internal/builder-next/worker/worker.go` (GO) -> Cumulative Risk: **722.91**
- **Archetype:** `file_cluster_11` (Distance: 13.981 IQR)
- **Magnitude:** 753.04 | **LOC:** 665 | **CtrlFlow:** 49.0% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (98.5692%)
- **Heaviest Functions:** `ResolveSourceMetadata` (Impact: 71.6), `FromRemote` (Impact: 28.9), `GetRemotes` (Impact: 28.4)

### 9. `daemon/command/daemon.go` (GO) -> Cumulative Risk: **721.98**
- **Archetype:** `file_cluster_4` (Distance: 14.72 IQR)
- **Magnitude:** 1171.82 | **LOC:** 1184 | **CtrlFlow:** 58.6% | **Authorship Centralization:** 44.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `start` (Impact: 652.7), `newDaemonCLI` (Impact: 11.6)

### 10. `contrib/dockerd-rootless.sh` (SHELL) -> Cumulative Risk: **721.17**
- **Archetype:** `file_cluster_8` (Distance: 13.253 IQR)
- **Magnitude:** 1.69 | **LOC:** 227 | **CtrlFlow:** 77.6% | **Authorship Centralization:** 57.1%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Injection Surface (99.9417%)
- **Heaviest Functions:** `Anonymous_Block_[Truncated]` (Impact: 22.8), `Anonymous_Block` (Impact: 20.2), `mount_directory` (Impact: 15.3)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `client/testdata/ca.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/testdata/cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/testdata/key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `integration-cli/fixtures/https/ca-rogue.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-cli/fixtures/https/ca.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-cli/fixtures/https/client-cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-cli/fixtures/https/client-key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-cli/fixtures/https/client-rogue-cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-cli/fixtures/https/client-rogue-key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-cli/fixtures/https/server-cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-cli/fixtures/https/server-key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-cli/fixtures/https/server-rogue-cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-cli/fixtures/https/server-rogue-key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-cli/fixtures/registry/cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/testdata/https/ca.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/testdata/https/client-cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/testdata/https/client-key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/testdata/https/server-cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/testdata/https/server-key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vendor/github.com/google/certificate-transparency-go/x509/test-dir.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vendor/github.com/google/certificate-transparency-go/x509/test-file.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vendor/github.com/moby/policy-helpers/roots/dhi/dhi.pub` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `daemon/daemon.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.147 IQR)
- **Top Global Matches:** file_cluster_11: 15.147, file_cluster_4: 15.169, file_cluster_8: 15.198
- **Magnitude:** 2477.34 | **LOC:** 1908 | **CtrlFlow:** 62.0% | **Authorship Centralization:** 39.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 235
- **Risk Profile:** Cognitive Load (48.3904%), Tech Debt (15.8191%)
**Top Internal Functions/Classes:**
  * `restore` (Impact: 1613.5 | O(2^N) | DB: 235)
  * `loadContainers` (Impact: 19.5 | O(N^1) | DB: 11)
  * `Config` (Impact: 4.6 | O(2^N))
    * *Intent:* // This is used for Windows which doesn't currently support running on containerd
  * `Features` (Impact: 4.6 | O(2^N))
    * *Intent:* // ID returns the daemon id
  * `HasExperimental` (Impact: 2.4 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 263`, `structural_boundaries: 161`, `args: 45`, `func_start: 45`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 666`, `dead_code: 2`, `planned_debt: 16`, `fragile_debt: 1`
* *Architecture:* `io: 4`, `api: 84`, `concurrency: 55`, `import: 1`
* *Defense:* `safety: 94`, `doc: 88`, `sync_locks: 30`, `immutability_locks: 1`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` bbolt, errors, timeout, address, plugin, storage-driver, registry, fmt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `daemon/libnetwork/network.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.571 IQR)
- **Top Global Matches:** file_cluster_11: 14.571, file_cluster_15: 14.744, file_cluster_8: 14.788
- **Magnitude:** 1965.18 | **LOC:** 2208 | **CtrlFlow:** 51.5% | **Authorship Centralization:** 30.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 78
- **Risk Profile:** Cognitive Load (45.1825%), Tech Debt (75.3499%)
**Top Internal Functions/Classes:**
  * `UnmarshalJSON` (Impact: 101.6 | O(N^1) | DB: 78)
  * `validateConfiguration` (Impact: 63.0 | O(N^1) | DB: 10)
  * `delete` (Impact: 49.5 | O(N^1) | DB: 14)
    * *Intent:* // NetworkOptionDriverOpts function returns an option setter for any driver parameter described by a...
  * `IPAMStatus` (Impact: 40.8 | O(2^N) | DB: 10)
  * `applyConfigurationTo` (Impact: 36.5 | O(N^1) | DB: 22)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 257`, `structural_boundaries: 242`, `args: 77`, `func_start: 77`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 948`, `dead_code: 2`, `planned_debt: 24`, `fragile_debt: 2`, `duplicate_logic: 6`
* *Architecture:* `api: 130`, `import: 1`
* *Defense:* `safety: 52`, `doc: 68`, `sync_locks: 77`, `immutability_locks: 1`, `cleanup: 38`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` nid, errdefs, options, scope, runtime, error, network, types...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `daemon/network.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.803 IQR)
- **Top Global Matches:** file_cluster_8: 14.803, file_cluster_11: 14.804, file_cluster_4: 14.815
- **Magnitude:** 1375.48 | **LOC:** 1237 | **CtrlFlow:** 66.5% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 86
- **Risk Profile:** Cognitive Load (48.4773%), Tech Debt (15.1901%)
**Top Internal Functions/Classes:**
  * `deleteNetwork` (Impact: 154.0 | O(N^1) | DB: 86)
  * `createNetwork` (Impact: 92.3 | O(N^1) | DB: 35)
  * `FindNetwork` (Impact: 28.4 | O(N^1) | DB: 6)
    * *Intent:* // FindNetwork returns a network based on: // 1. Full ID // 2. Full Name // 3. Partial ID // as long...
  * `setupIngress` (Impact: 28.1 | O(2^N) | DB: 5)
  * `validateIpamConfig` (Impact: 26.1 | O(N^1) | DB: 16)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 216`, `structural_boundaries: 109`, `args: 39`, `func_start: 39`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 707`, `dead_code: 1`, `planned_debt: 12`
* *Architecture:* `api: 52`, `concurrency: 36`, `import: 1`
* *Defense:* `safety: 37`, `doc: 45`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` options, provider, error, plugingetter, network, types, log, networkdb...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `daemon/containerd/image_list.go` (GO) | Magnitude: 542.72 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 371, state_mutation: 274, encapsulation: 114, branch: 91
- `daemon/config/config_windows.go` (GO) | Magnitude: 47.9 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 30, structural_boundaries: 15, api: 12, doc: 10
- `api/types/auxprogress/push.go` (GO) | Magnitude: 22.26 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 7, api: 7, doc: 7, indent_tabs: 6
- `daemon/libnetwork/netlabel/labels.go` (GO) | Magnitude: 45.74 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: api: 22, indent_tabs: 22, state_mutation: 21, doc: 21
- `daemon/logger/splunk/splunk.go` (GO) | Magnitude: 440.2 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 308, state_mutation: 261, encapsulation: 142, branch: 51

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `daemon/libnetwork/store.go` (GO) | Magnitude: 185.74 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 97, state_mutation: 84, branch: 30, pointers: 23
- `daemon/cluster/services.go` (GO) | Magnitude: 708.66 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 374, state_mutation: 280, branch: 102, encapsulation: 87
- `client/client.go` (GO) | Magnitude: 130.02 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 102, state_mutation: 66, branch: 26, encapsulation: 25
- `daemon/info.go` (GO) | Magnitude: 482.68 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 233, state_mutation: 223, encapsulation: 55, branch: 54
- `client/request.go` (GO) | Magnitude: 181.32 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 126, state_mutation: 73, branch: 40, encapsulation: 37

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `hack/make/run` (SHELL) | Magnitude: 92.46 | Delta: **0.094 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 60, indent_tabs: 45, branch: 20, reflection_metaprogramming: 14
- `hack/make.sh` (SHELL) | Magnitude: 110.54 | Delta: **0.11 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 64, state_mutation: 42, branch: 35, reflection_metaprogramming: 23
- `hack/dockerfile/cli.sh` (SHELL) | Magnitude: 27.7 | Delta: **0.199 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 14, state_mutation: 13, reflection_metaprogramming: 11, branch: 8
- `daemon/libnetwork/support/support.sh` (SHELL) | Magnitude: 182.02 | Delta: **0.241 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: reflection_metaprogramming: 76, state_mutation: 67, indent_tabs: 67, io: 56
- `api/scripts/validate-swagger-gen.sh` (SHELL) | Magnitude: 4.36 | Delta: **0.257 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: reflection_metaprogramming: 24, state_mutation: 21, indent_tabs: 16, branch: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `client/image_push_opts.go` (GO) | Magnitude: 20.22 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 6, indent_tabs: 6, structural_boundaries: 5, api: 5
- `client/volume_prune.go` (GO) | Magnitude: 33.48 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 30, state_mutation: 15, structural_boundaries: 11, api: 6
- `daemon/command/docker_windows.go` (GO) | Magnitude: 24.2 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 20, state_mutation: 12, structural_boundaries: 6, branch: 5
- `daemon/server/httputils/httputils.go` (GO) | Magnitude: 66.24 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 36, state_mutation: 15, structural_boundaries: 12, branch: 10
- `daemon/pkg/opts/ulimit.go` (GO) | Magnitude: 87.44 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 35, state_mutation: 33, structural_boundaries: 20, api: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `pkg/authorization/response.go` (GO) | Magnitude: 163.78 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 88, state_mutation: 51, doc: 29, encapsulation: 29
- `internal/testutil/registry/ops.go` (GO) | Magnitude: 22.52 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 14, pointers: 9, closures: 8, structural_boundaries: 6
- `daemon/builder/remotecontext/internal/tarsum/fileinfosums.go` (GO) | Magnitude: 132.96 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 55, state_mutation: 40, structural_boundaries: 27, branch: 18
- `daemon/logger/journald/internal/sdjournal/sdjournal.go` (GO) | Magnitude: 206.36 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 110, state_mutation: 81, structural_boundaries: 42, pointers: 30
- `daemon/pkg/plugin/v2/plugin.go` (GO) | Magnitude: 276.1 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 145, state_mutation: 70, branch: 42, structural_boundaries: 39

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `daemon/internal/streamformatter/streamformatter.go` (GO) | Magnitude: 134.68 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 92, state_mutation: 65, structural_boundaries: 29, encapsulation: 26
- `internal/iterutil/iterutil.go` (GO) | Magnitude: 103.7 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 50, state_mutation: 33, branch: 23, structural_boundaries: 15
- `daemon/libnetwork/discoverapi/discoverapi.go` (GO) | Magnitude: 37.56 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: api: 19, indent_tabs: 16, doc: 13, structural_boundaries: 10
- `internal/sliceutil/sliceutil.go` (GO) | Magnitude: 70.08 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 42, indent_tabs: 30, structural_boundaries: 11, branch: 10
- `client/pkg/progress/progress.go` (GO) | Magnitude: 48.82 | Delta: **0.075 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 20, structural_boundaries: 16, api: 16, doc: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `daemon/internal/builder-next/worker/mod/mod.go` (GO) | Magnitude: 57.24 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 36, state_mutation: 25, branch: 13, encapsulation: 11
- `daemon/server/router/volume/volume_routes.go` (GO) | Magnitude: 159.04 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 112, state_mutation: 75, branch: 32, structural_boundaries: 30
- `contrib/dockerd-rootless-setuptool.sh` (SHELL) | Magnitude: 3.79 | Delta: **0.06 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 384, state_mutation: 175, io: 145, branch: 133
- `daemon/builder/dockerfile/internals_linux.go` (GO) | Magnitude: 69.98 | Delta: **0.106 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 52, state_mutation: 30, structural_boundaries: 14, branch: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `integration/plugin/logging/cmd/discard/driver.go` (GO) | Magnitude: 54.26 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 56, state_mutation: 22, structural_boundaries: 19, encapsulation: 16
- `daemon/cluster/swarm.go` (GO) | Magnitude: 856.44 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 443, state_mutation: 330, branch: 118, encapsulation: 91
- `daemon/stats/collector.go` (GO) | Magnitude: 99.62 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 74, state_mutation: 38, encapsulation: 24, structural_boundaries: 15
- `daemon/libnetwork/cluster/provider.go` (GO) | Magnitude: 29.52 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 18, structural_boundaries: 6, api: 6, doc: 6
- `daemon/logger/local/read.go` (GO) | Magnitude: 82.04 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 62, state_mutation: 31, branch: 17, structural_boundaries: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `daemon/libnetwork/drivers/overlay/ov_network.go` (GO) | Magnitude: 432.12 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 297, state_mutation: 196, encapsulation: 80, branch: 78
- `daemon/libnetwork/ns/init_linux.go` (GO) | Magnitude: 105.26 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 67, state_mutation: 49, encapsulation: 30, branch: 15
- `daemon/libnetwork/networkdb/delegate.go` (GO) | Magnitude: 325.72 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 276, state_mutation: 147, encapsulation: 86, branch: 72
- `daemon/libnetwork/networkdb/cluster.go` (GO) | Magnitude: 603.18 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_11`
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
- `daemon/container/archive_windows.go` (GO) | Magnitude: 78.46 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 46, state_mutation: 27, structural_boundaries: 12, encapsulation: 10
- `daemon/errors.go` (GO) | Magnitude: 100.0 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 65, structural_boundaries: 37, encapsulation: 32, args: 22
- `daemon/internal/progress/progress.go` (GO) | Magnitude: 43.82 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 20, structural_boundaries: 16, api: 16, doc: 10
- `contrib/init/sysvinit-debian/docker` (SHELL) | Magnitude: 0.54 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 52, safety_bypasses: 19, state_mutation: 18, branch: 17
- `hack/validate/deprecate-integration-cli` (SHELL) | Magnitude: 15.6 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 12, debug_prints: 8, branch: 6, state_mutation: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `daemon/container/rwlayer.go` (GO) | Magnitude: 14.12 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: structural_boundaries: 4, doc: 4, indent_tabs: 3, class_start: 1
- `daemon/internal/quota/projectquota_unsupported.go` (GO) | Magnitude: 9.1 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 4, pointers: 4, args: 3, func_start: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `Dockerfile` -> Churn: **100.0%** | Cog Load: 53.689% | Debt: 94.1495%
- `daemon/server/router/container/container_routes.go` -> Churn: **78.3%** | Cog Load: 41.1431% | Debt: 95.6508%
- `daemon/server/router/system/system_routes.go` -> Churn: **68.41%** | Cog Load: 44.5529% | Debt: 92.4142%
- `daemon/server/router/image/image_routes.go` -> Churn: **61.96%** | Cog Load: 55.9796% | Debt: 92.1369%
- `client/request.go` -> Churn: **56.65%** | Cog Load: 39.1399% | Debt: 97.7023%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `daemon/cluster/swarm.go` -> **Cory Snider** (100.0% isolated ownership) | Magnitude: 856.44
- `daemon/cluster/convert/container.go` -> **Cory Snider** (100.0% isolated ownership) | Magnitude: 744.7
- `daemon/libnetwork/drivers/remote/driver.go` -> **Rob Murray** (100.0% isolated ownership) | Magnitude: 731.76
- `daemon/internal/builder-next/adapters/snapshot/snapshot.go` -> **Sebastiaan van Stijn** (100.0% isolated ownership) | Magnitude: 618.4
- `daemon/libnetwork/osl/interface_linux.go` -> **Paul Saab** (100.0% isolated ownership) | Magnitude: 610.42

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

- `hack/make/binary` -> **Severity: 14078.389** (Blast Radius: 241.851 * Doc Risk: 58.211%)
- `hack/make/binary-daemon` -> **Severity: 7815.886** (Blast Radius: 103.366 * Doc Risk: 75.6137%)
- `internal/testutil/fakecontext/context.go` -> **Severity: 6231.345** (Blast Radius: 63.681 * Doc Risk: 97.8525%)
- `hack/make/binary-proxy` -> **Severity: 6201.929** (Blast Radius: 103.366 * Doc Risk: 59.9997%)
- `daemon/logger/internal/logdriver/io.go` -> **Severity: 5965.847** (Blast Radius: 76.159 * Doc Risk: 78.3341%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
