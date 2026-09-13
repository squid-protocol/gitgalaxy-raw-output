# ARCHITECTURAL_BRIEF: moby
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/moby/moby` |
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
| Total Artifacts | 12450 |
| Analyzed Artifacts (Scanned) | 2893 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 9557 |
| Total LOC | 279331 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 23.2% |
| Dominant Lang | GO |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4991 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2675 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.8687 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 72 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| GO | 2066 | 272414 | 71.4% |
| PLAINTEXT | 676 | 22 | 23.4% |
| MARKDOWN | 48 | 0 | 1.7% |
| SHELL | 47 | 3076 | 1.6% |
| DOCKERFILE | 15 | 862 | 0.5% |
| JSON | 12 | 1096 | 0.4% |
| C | 8 | 179 | 0.3% |
| YAML | 6 | 92 | 0.2% |
| PROTO | 6 | 177 | 0.2% |
| MAKEFILE | 3 | 283 | 0.1% |
| LUA | 2 | 530 | 0.1% |
| ASSEMBLY | 1 | 7 | 0.0% |
| PYTHON | 1 | 163 | 0.0% |
| POWERSHELL | 1 | 429 | 0.0% |
| BINARY_THREAT | 1 | 1 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 2168 | 74.9% |
| Unknown | 23 | 0.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 702 | 24.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 9557*

**Composition by Extension & Reason:**
- `.go`: 7873x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Excluded (Machine-Generated Source Code Signature: 17 LOC), 4x Excluded (Machine-Generated Source Code Signature: 37 LOC)
- `no_extension`: 570x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Saturation: Line 1 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 2517 LOC)
- `.md`: 410x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Machine-Generated Source Code Signature: 50 LOC), 2x Excluded (Machine-Generated Source Code Signature: 148 LOC)
- `.yml`: 119x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.proto`: 92x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.s`: 84x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 53x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 13886 LOC)
- `.json`: 44x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 1593 LOC)
- `.txt`: 42x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 23x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 18 LOC)
- `.png`: 19x Excluded (Explicitly Denied Extension: '.png')
- `.toml`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Unsupported Extension: '.toml')
- `.sum`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded (Unsupported Extension: '.sum')
- `.tar`: 8x Excluded (Explicitly Denied Extension: '.tar')
- `.hcl`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.hcl')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 14.9 | 8.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 41.7 | 50.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 55.4 | 50.0 | 50.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 12.7 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 9.2 | 4.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 8.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 52.4 | 51.7 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 92.1 | 1.2 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 94.4 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 30.4 | 1.7 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 7.4 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 53.2 | 56.4 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 86.7 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 16413 | 1514 | 15 | `daemon/libnetwork/bitmap/sequence_test.go` |
| cleanup | 2100 | 557 | 2 | `integration-cli/docker_cli_build_test.go` |
| guards | 16520 | 1693 | 15 | `integration-cli/docker_cli_build_test.go` |
| danger | 3019 | 669 | 3 | `contrib/dockerd-rootless-setuptool.sh` |
| concurrency | 4029 | 461 | 3 | `daemon/libnetwork/cmd/networkdb-test/dbclient/ndbClient.go` |
| connectivity | 14778 | 1817 | 12 | `integration-cli/docker_cli_build_test.go` |
| io | 2091 | 592 | 1 | `contrib/dockerd-rootless-setuptool.sh` |
| crypto | 1 | 1 | 0 | `daemon/libnetwork/cmd/ssd/ssd.py` |
| ipc | 684 | 169 | 0 | `daemon/logger/loggerutils/file_windows.go` |
| time | 577 | 215 | 0 | `daemon/logger/awslogs/cloudwatchlogs_test.go` |
| serialization | 505 | 177 | 0 | `contrib/download-frozen-image-v2.sh` |
| regex | 234 | 71 | 0 | `integration-cli/docker_cli_by_digest_test.go` |
| events | 114 | 60 | 0 | `daemon/events/events_test.go` |
| tests | 16902 | 757 | 14 | `integration-cli/docker_cli_swarm_test.go` |
| docs | 15352 | 1533 | 15 | `integration-cli/docker_cli_run_test.go` |
| debt | 2965 | 650 | 2 | `integration-cli/docker_cli_build_test.go` |
| mutation | 32532 | 1661 | 29 | `integration-cli/docker_cli_build_test.go` |
| dead_code | 7473 | 1732 | 7 | `integration-cli/docker_cli_build_test.go` |
| credential | 9 | 6 | 0 | `hack/make.ps1` |
| threat | 325 | 85 | 0 | `integration-cli/docker_cli_daemon_test.go` |
| ml_ai | 97 | 31 | 0 | `contrib/download-frozen-image-v2.sh` |
| ui | 40 | 18 | 0 | `contrib/dockerd-rootless-setuptool.sh` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `contrib/dockerd-rootless-setuptool.sh` (Hits: 145)
- `contrib/download-frozen-image-v2.sh` (Hits: 126)
- `contrib/check-config.sh` (Hits: 88)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **context.go** (`internal/testutil/fakecontext/context.go`) — 875 inbound connections
2. **io.go** (`daemon/logger/internal/logdriver/io.go`) — 304 inbound connections
3. **http.go** (`pkg/plugins/transport/http.go`) — 292 inbound connections
4. **net.go** (`daemon/libnetwork/internal/hashable/net.go`) — 208 inbound connections
5. **testutil.go** (`daemon/graphdriver/graphtest/testutil.go`) — 133 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **names-generator.go** (`internal/namesgenerator/names-generator.go`) — 346 outbound dependencies
2. **daemon.go** (`daemon/daemon.go`) — 93 outbound dependencies
3. **docker_cli_build_test.go** (`integration-cli/docker_cli_build_test.go`) — 85 outbound dependencies
4. **stats_unix.go** (`daemon/stats_unix.go`) — 70 outbound dependencies
5. **daemon.go** (`daemon/command/daemon.go`) — 68 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `TestRunDisallowBindMountingRootToRoot` (@ `integration-cli/docker_cli_run_test.go`) -> Impact: **408.0** | LOC: 1344
- `createWindows` (@ `daemon/internal/libcontainerd/local/local_windows.go`) -> Impact: **361.2** | LOC: 1057
- `NewDaemon` (@ `daemon/daemon.go`) -> Impact: **296.3** | LOC: 559
  * *Intent:* // NewDaemon sets up everything for the daemon to be able to service // requests from the webserver.
- `TestBuildExposeMorePorts` (@ `integration-cli/docker_cli_build_test.go`) -> Impact: **256.5** | LOC: 1792
- `Validate-DCO` (@ `hack/make.ps1`) -> Impact: **215.1** | LOC: 388
  * *Intent:* # Validates the DCO marker is present on each commit
- `restore` (@ `daemon/daemon.go`) -> Impact: **203.8** | LOC: 437
- `verifyPlatformContainerResources` (@ `daemon/daemon_unix.go`) -> Impact: **171.9** | LOC: 159
  * *Intent:* // verifyPlatformContainerResources performs platform-specific validation of the container's resource-configuration
- `postContainersCreate` (@ `daemon/server/router/container/container_routes.go`) -> Impact: **157.5** | LOC: 243
- `withMounts` (@ `daemon/oci_linux.go`) -> Impact: **151.5** | LOC: 213
  * *Intent:* // withMounts sets the container's mounts
- `NewNetwork` (@ `daemon/libnetwork/controller.go`) -> Impact: **134.3** | LOC: 237
  * *Intent:* // NewNetwork creates a new network of the specified network type. The options // are network specific and modeled in a generic way.

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `integration-cli/fixtures/https` | 10 | 50000.0 | 0.0% | 0.0% |
| `integration/testdata/https` | 5 | 25000.0 | 0.0% | 0.0% |
| `integration-cli` | 99 | 16354.72 | 18.45% | 81.66% |
| `daemon` | 146 | 15355.5 | 17.71% | 53.02% |
| `client/testdata` | 3 | 15000.0 | 0.0% | 0.0% |
| `vendor/github.com/google/certificate-transparency-go/x509` | 2 | 10000.0 | 0.0% | 0.0% |
| `daemon/libnetwork` | 62 | 8360.58 | 14.83% | 67.36% |
| `client` | 232 | 6163.74 | 7.63% | 60.59% |
| `daemon/containerd` | 46 | 5498.3 | 14.81% | 52.47% |
| `integration-cli/fixtures/registry` | 1 | 5000.0 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `api/pkg/authconfig/authconfig.go` -> **100.0%** Exposure
- `client/pkg/progress/progress.go` -> **100.0%** Exposure
- `daemon/builder/dockerfile/mockbackend_test.go` -> **100.0%** Exposure
- `daemon/cluster/executor/container/attachment.go` -> **100.0%** Exposure
- `daemon/command/daemon_windows.go` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `api/pkg/stdcopy/stdcopy.go` -> **100.0%** Exposure
- `client/hijack_test.go` -> **100.0%** Exposure
- `client/internal/timestamp/timestamp.go` -> **100.0%** Exposure
- `daemon/cluster/convert/node.go` -> **100.0%** Exposure
- `daemon/cluster/convert/service.go` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `integration-cli/docker_cli_build_test.go` -> **183** Orphaned Functions | **0** Duplicates
- `integration-cli/docker_cli_run_test.go` -> **91** Orphaned Functions | **0** Duplicates
- `integration-cli/docker_cli_daemon_test.go` -> **78** Orphaned Functions | **0** Duplicates
- `integration-cli/docker_cli_run_unix_test.go` -> **73** Orphaned Functions | **0** Duplicates
- `integration-cli/docker_cli_network_unix_test.go` -> **67** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `daemon/logger/splunk/splunkhecmock_test.go` -> **86.7387%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `20` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `18030` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `daemon/internal/builder-next/builder.go` (GO) -> Cumulative Risk: **712.6**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 538.14 | **LOC:** 723 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 57.1%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9868%), Concurrency (97.4242%), Verification (80.0%)
- **Heaviest Functions:** `Build` (Impact: 101.5), `toBuildkitPruneInfo` (Impact: 32.9), `toBuildkitExtraHosts` (Impact: 20.3)

### 2. `daemon/cluster/executor/container/adapter.go` (GO) -> Cumulative Risk: **709.21**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 321.44 | **LOC:** 563 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.7436%), State Flux (99.4118%)
- **Heaviest Functions:** `pullImage` (Impact: 33.1), `logs` (Impact: 26.7), `waitNodeAttachments` (Impact: 16.3)

### 3. `daemon/server/router/system/system_routes.go` (GO) -> Cumulative Risk: **703.23**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 349.24 | **LOC:** 465 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 56.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9885%), Documentation (93.3333%), Tech Debt (90.4483%)
- **Heaviest Functions:** `getDiskUsage` (Impact: 77.9), `getEvents` (Impact: 73.3), `getInfo` (Impact: 25.6)

### 4. `daemon/command/service_windows.go` (GO) -> Cumulative Risk: **703.04**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 286.3 | **LOC:** 395 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Concurrency (99.8614%), Documentation (92.8571%)
- **Heaviest Functions:** `initService` (Impact: 25.7), `Fire` (Impact: 24.8), `Execute` (Impact: 21.0)

### 5. `integration-cli/benchmark_test.go` (GO) -> Cumulative Risk: **693.42**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 124.3 | **LOC:** 133 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `BenchmarkConcurrentContainerActions` (Impact: 22.4), `BenchmarkLogsCLIRotateFollow` (Impact: 8.2), `TearDownTest` (Impact: 1.9)

### 6. `daemon/libnetwork/cmd/networkdb-test/dbclient/ndbClient.go` (GO) -> Cumulative Risk: **692.98**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 770.44 | **LOC:** 856 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.8517%), Documentation (94.7368%)
- **Heaviest Functions:** `Client` (Impact: 39.4), `checkTable` (Impact: 36.1), `doNetworkStatsQueue` (Impact: 17.2)

### 7. `daemon/volume/service/convert.go` (GO) -> Cumulative Risk: **685.28**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 133.08 | **LOC:** 160 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9998%), Safety Score (85.0159%)
- **Heaviest Functions:** `volumesToAPI` (Impact: 34.6), `filtersToBy` (Impact: 19.0), `withPrune` (Impact: 9.4)

### 8. `daemon/logger/local/read.go` (GO) -> Cumulative Risk: **677.87**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 164.88 | **LOC:** 211 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (92.3077%), Safety Score (85.7762%)
- **Heaviest Functions:** `getTailReader` (Impact: 35.0), `Decode` (Impact: 12.6), `readRecord` (Impact: 8.1)

### 9. `daemon/logs.go` (GO) -> Cumulative Risk: **672.65**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 156.36 | **LOC:** 223 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.8357%), Concurrency (99.036%)
- **Heaviest Functions:** `ContainerLogs` (Impact: 75.0), `mergeAndVerifyLogConfig` (Impact: 9.5), `getLogger` (Impact: 6.7)

### 10. `daemon/pkg/plugin/fetch_linux.go` (GO) -> Cumulative Risk: **669.75**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 192.76 | **LOC:** 294 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9076%), Concurrency (99.7282%), Tech Debt (90.6339%)
- **Heaviest Functions:** `withFetchProgress` (Impact: 42.8), `fetch` (Impact: 23.8), `applyLayer` (Impact: 17.5)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.106
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.106
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.36
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.106
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.106
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.106
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.106
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.106
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.106
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.106
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.106
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.106
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.106
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.106
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.106
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.106
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.106
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.106
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.106
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.106
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.106
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.106
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-cli/docker_cli_build_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2388.24 | **LOC:** 6246 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 70.6%
- **Risk Profile:** Cognitive Load (12.4719%), Tech Debt (99.3931%)
**Top Internal Functions/Classes:**
  * `TestBuildExposeMorePorts` (Impact: 256.5)
  * `TestBuildEnvironmentReplacementEnv` (Impact: 27.1)
  * `TestBuildWithInaccessibleFilesInContext` (Impact: 22.6)
    * *Intent:* // Issue #5270 - ensure we throw a better error than "unexpected EOF" // when we can't access files ...
  * `TestBuildAddBadLinks` (Impact: 19.1)
  * `TestBuildSymlinkBreakout` (Impact: 16.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 124 instances
* *Concurrency (weighted view):* 37
* *Memory Alloc (weighted view):* 6
* *State Mutation (weighted view):* 441
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 395`, `structural_boundaries: 233`, `args: 246`, `func_start: 246`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 193`, `planned_debt: 8`, `fragile_debt: 50`, `unreferenced_by_name: 183`
* *Architecture:* `io: 9`, `api: 694`, `concurrency: 7`, `import: 1`
* *Defense:* `safety: 65`, `doc: 159`, `test: 379`, `immutability_locks: 166`, `cleanup: 77`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.106
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` --add-host, --build-arg, --filter, --since, .dockerignore, test1, test2, test3...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-cli/docker_cli_run_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2031.04 | **LOC:** 4378 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 63.6%
- **Risk Profile:** Cognitive Load (33.5026%), Tech Debt (93.7209%)
**Top Internal Functions/Classes:**
  * `TestRunDisallowBindMountingRootToRoot` (Impact: 408.0)
  * `TestRunMount` (Impact: 28.5)
  * `TestRunNoDupVolumes` (Impact: 19.5)
    * *Intent:* // Test for GH#10618
  * `TestRunCreateVolumesInSymlinkDir` (Impact: 12.0)
    * *Intent:* // Volume path is a symlink which also exists on the host, and the host side is a file not a dir // ...
  * `TestRunVolumesFromSymlinkPath` (Impact: 11.9)
    * *Intent:* // Tests that a volume path that has a symlink exists in a container mounting it with `--volumes-fro...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Race Conditions:* 18 instances
* *Amplified Cascading Flux:* 219 instances
* *High Risk Execution (weighted view):* 2
* *Concurrency (weighted view):* 112
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 730
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 599`, `structural_boundaries: 149`, `args: 237`, `func_start: 237`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 32`, `high_risk_execution: 7`, `state_mutation: 292`, `dead_code: 2`, `planned_debt: 36`, `fragile_debt: 10`, `unreferenced_by_name: 91`
* *Architecture:* `io: 4`, `api: 253`, `concurrency: 22`, `import: 1`
* *Defense:* `safety: 96`, `doc: 263`, `test: 402`, `immutability_locks: 12`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.106
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` --mount, --read-only, --volume, -v, kcore, latency_stats, core_pattern, modprobe...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `daemon/libnetwork/network.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1409.84 | **LOC:** 2208 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 30.0%
- **Risk Profile:** Cognitive Load (40.3846%), Tech Debt (21.8125%)
**Top Internal Functions/Classes:**
  * `ipamAllocateVersion` (Impact: 82.0)
  * `UnmarshalJSON` (Impact: 58.5)
  * `delete` (Impact: 47.6)
    * *Intent:* // This function gets called in 3 ways: // - Delete() -- (false, false) // remove if endpoint count ...
  * `createEndpoint` (Impact: 40.0)
  * `validateConfiguration` (Impact: 29.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 159 instances
* *State Mutation (weighted view):* 537
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 331`, `structural_boundaries: 354`, `args: 104`, `func_start: 104`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 219`, `dead_code: 3`, `planned_debt: 36`, `fragile_debt: 2`
* *Architecture:* `api: 93`, `import: 1`
* *Defense:* `safety: 74`, `doc: 102`, `sync_locks: 85`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.106
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` PoolID, context, json, error, errors, fmt, errdefs, log...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `client/client_test.go` -> Churn: **81.15%** | Cog Load: 7.6745% | Debt: 88.5233%
- `daemon/server/router/container/container_routes.go` -> Churn: **78.3%** | Cog Load: 25.0736% | Debt: 90.2573%
- `client/client_options.go` -> Churn: **71.49%** | Cog Load: 12.7566% | Debt: 99.9836%
- `daemon/server/router/system/system_routes.go` -> Churn: **68.41%** | Cog Load: 59.0435% | Debt: 90.4483%
- `daemon/server/router/image/image_routes.go` -> Churn: **61.96%** | Cog Load: 45.4245% | Debt: 85.2187%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `integration-cli/docker_cli_run_unix_test.go` -> **Sebastiaan van Stijn** (100.0% isolated ownership) | Magnitude: 779.72
- `daemon/libnetwork/cmd/networkdb-test/dbclient/ndbClient.go` -> **Paweł Gronowski** (100.0% isolated ownership) | Magnitude: 770.44
- `daemon/logger/splunk/splunk_test.go` -> **Paweł Gronowski** (100.0% isolated ownership) | Magnitude: 757.2
- `daemon/libnetwork/osl/interface_linux.go` -> **Paul Saab** (100.0% isolated ownership) | Magnitude: 642.66
- `daemon/logger/loggerutils/logfile.go` -> **Sebastiaan van Stijn** (100.0% isolated ownership) | Magnitude: 571.8

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `daemon/logger/internal/logdriver/io.go` -> **Severity: 0.028** (Bridge: 0.0004 * Flux: 76.9689%)
- `pkg/plugins/transport/http.go` -> **Severity: 0.008** (Bridge: 0.0001 * Flux: 99.1837%)
- `hack/make/binary` -> **Severity: 0.008** (Bridge: 0.0002 * Flux: 31.0026%)
- `daemon/graphdriver/graphtest/testutil.go` -> **Severity: 0.007** (Bridge: 0.0001 * Flux: 99.9463%)
- `internal/testutil/fakecontext/context.go` -> **Severity: 0.006** (Bridge: 0.0003 * Flux: 20.8573%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `hack/make/binary-daemon` -> **Severity: 9955.313** (Blast Radius: 108.343 * Doc Risk: 91.887%)
- `daemon/logger/internal/logdriver/io.go` -> **Severity: 4020.2** (Blast Radius: 80.404 * Doc Risk: 50.0%)
- `daemon/graphdriver/graphtest/testutil.go` -> **Severity: 641.0** (Blast Radius: 6.41 * Doc Risk: 100.0%)
- `internal/testutil/fakecontext/context.go` -> **Severity: 294.845** (Blast Radius: 58.969 * Doc Risk: 5.0%)
- `daemon/libnetwork/internal/hashable/net.go` -> **Severity: 231.778** (Blast Radius: 10.43 * Doc Risk: 22.2222%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
