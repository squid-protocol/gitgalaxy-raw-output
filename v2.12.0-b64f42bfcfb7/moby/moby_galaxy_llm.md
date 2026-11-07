# ARCHITECTURAL_BRIEF: moby
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/moby/moby` |
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
- **Scope:** 2917 analyzed artifact(s), 283437 LOC.
- **Load-bearing artifact:** `api/types/container/container.go` -- 216 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `daemon/daemon.go` -- pulls in 78 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `client/testdata/key.pem` at magnitude 5000.0 (structural weight, not risk).
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
| Total Artifacts | 12450 |
| Analyzed Artifacts (Scanned) | 2917 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 9533 |
| Total LOC | 283437 |
| Volatility Index | 0.004 |
| % Scanned of codebase = | 23.4% |
| Dominant Lang | GO |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6716 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1046 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 8.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.6998 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 233 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| GO | 2077 | 273709 | 71.2% |
| PLAINTEXT | 665 | 10 | 22.8% |
| MARKDOWN | 52 | 0 | 1.8% |
| SHELL | 47 | 3076 | 1.6% |
| YAML | 27 | 2899 | 0.9% |
| DOCKERFILE | 14 | 846 | 0.5% |
| JSON | 13 | 1129 | 0.4% |
| C | 8 | 179 | 0.3% |
| PROTO | 6 | 177 | 0.2% |
| MAKEFILE | 3 | 283 | 0.1% |
| LUA | 2 | 530 | 0.1% |
| ASSEMBLY | 1 | 7 | 0.0% |
| PYTHON | 1 | 163 | 0.0% |
| POWERSHELL | 1 | 429 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 2907 |
| unknown | unknown | 10 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 31%, Large Core Modules (2) 18%, Callbacks & Closures Files 13%, Large Core Modules 8%, State Mutators Files 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 2200 | 75.4% |
| Unknown | 10 | 0.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 707 | 24.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 9533*

**Composition by Extension & Reason:**
- `.go`: 7873x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Excluded (Machine-Generated Source Code Signature: 17 LOC), 4x Excluded (Machine-Generated Source Code Signature: 37 LOC)
- `no_extension`: 570x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Saturation: Line 1 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 2517 LOC)
- `.md`: 409x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Machine-Generated Source Code Signature: 148 LOC), 1x Excluded (Machine-Generated Source Code Signature: 171 LOC)
- `.yml`: 97x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Zero-Density Threshold (LOC: 152, Signals: 0)
- `.proto`: 92x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.s`: 84x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 53x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 13886 LOC)
- `.json`: 44x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 1593 LOC)
- `.txt`: 42x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 23x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 18 LOC)
- `.png`: 19x Excluded (Explicitly Denied Extension: '.png')
- `.toml`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Unsupported Extension: '.toml')
- `.sum`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded (Unsupported Extension: '.sum')
- `.pem`: 9x Excluded (Unsupported Extension: '.pem')
- `.tar`: 8x Excluded (Explicitly Denied Extension: '.tar')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 14.4 | 8.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 93.6 | 37.6 | 49.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 55.6 | 47.3 | 37.8 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 11.8 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 5.7 | 4.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 8.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 51.7 | 50.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 32.1 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 30.4 | 0.8 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 4.6 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 52.8 | 56.4 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 86.7 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 4571 | 940 | 4 | `daemon/logger/awslogs/cloudwatchlogs_test.go` |
| cleanup | 2117 | 564 | 2 | `integration-cli/docker_cli_build_test.go` |
| guards | 16464 | 1703 | 15 | `integration-cli/docker_cli_build_test.go` |
| danger | 3058 | 682 | 3 | `contrib/dockerd-rootless-setuptool.sh` |
| concurrency | 4050 | 471 | 3 | `daemon/libnetwork/cmd/networkdb-test/dbclient/ndbClient.go` |
| connectivity | 14850 | 1828 | 12 | `integration-cli/docker_cli_build_test.go` |
| io | 2093 | 594 | 1 | `contrib/dockerd-rootless-setuptool.sh` |
| crypto | 1 | 1 | 0 | `daemon/libnetwork/cmd/ssd/ssd.py` |
| ipc | 685 | 169 | 0 | `daemon/logger/loggerutils/file_windows.go` |
| time | 582 | 219 | 0 | `daemon/logger/awslogs/cloudwatchlogs_test.go` |
| serialization | 505 | 177 | 0 | `contrib/download-frozen-image-v2.sh` |
| regex | 239 | 71 | 0 | `integration-cli/docker_cli_by_digest_test.go` |
| events | 131 | 64 | 0 | `daemon/events/events_test.go` |
| tests | 16999 | 762 | 14 | `integration-cli/docker_cli_swarm_test.go` |
| docs | 15708 | 1564 | 15 | `integration-cli/docker_cli_run_test.go` |
| debt | 3091 | 667 | 2 | `integration-cli/docker_cli_build_test.go` |
| mutation | 32870 | 1685 | 29 | `integration-cli/docker_cli_build_test.go` |
| dead_code | 8088 | 1863 | 7 | `integration-cli/docker_cli_build_test.go` |
| credential | 17 | 8 | 0 | `.github/workflows/.windows.yml` |
| threat | 39 | 4 | 0 | `daemon/libnetwork/resolver_test.go` |
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

1. **container.go** (`api/types/container/container.go`) — 216 inbound connections
2. **client.go** (`client/client.go`) — 210 inbound connections
3. **doc.go** (`internal/testutil/doc.go`) — 133 inbound connections
4. **doc.go** (`errdefs/doc.go`) — 129 inbound connections
5. **endpoint.go** (`api/types/network/endpoint.go`) — 120 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **daemon.go** (`daemon/daemon.go`) — 78 outbound dependencies
2. **daemon.go** (`daemon/command/daemon.go`) — 63 outbound dependencies
3. **controller.go** (`daemon/internal/builder-next/controller.go`) — 57 outbound dependencies
4. **Dockerfile** (`Dockerfile`) — 53 outbound dependencies
5. **worker.go** (`daemon/internal/builder-next/worker/worker.go`) — 51 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `NewDaemon` **(Many-Argument Workhorses)** (@ `daemon/daemon.go`) -> Impact: **285.1** | LOC: 559
  * *Intent:* // NewDaemon sets up everything for the daemon to be able to service // requests from the webserver.
- `createWindows` **(Many-Argument Workhorses)** (@ `daemon/internal/libcontainerd/local/local_windows.go`) -> Impact: **231.3** | LOC: 1057
- `Validate-DCO` **(Many-Argument Workhorses)** (@ `hack/make.ps1`) -> Impact: **215.1** | LOC: 388
  * *Intent:* # Validates the DCO marker is present on each commit
- `restore` **(Many-Argument Workhorses)** (@ `daemon/daemon.go`) -> Impact: **193.8** | LOC: 437
- `verifyPlatformContainerResources` **(Many-Argument Workhorses)** (@ `daemon/daemon_unix.go`) -> Impact: **165.9** | LOC: 159
  * *Intent:* // verifyPlatformContainerResources performs platform-specific validation of the container's resource-configuration
- `postContainersCreate` **(Many-Argument Workhorses)** (@ `daemon/server/router/container/container_routes.go`) -> Impact: **157.5** | LOC: 243
- `withMounts` **(Many-Argument Workhorses)** (@ `daemon/oci_linux.go`) -> Impact: **144.8** | LOC: 213
  * *Intent:* // withMounts sets the container's mounts
- `NewNetwork` **(Many-Argument Workhorses)** (@ `daemon/libnetwork/controller.go`) -> Impact: **131.9** | LOC: 237
  * *Intent:* // NewNetwork creates a new network of the specified network type. The options // are network specific and modeled in a generic way.
- `Images` **(Many-Argument Workhorses)** (@ `daemon/images/image_list.go`) -> Impact: **127.5** | LOC: 229
  * *Intent:* // Images returns a filtered list of images.
- `registerMountPoints` **(Many-Argument Workhorses)** (@ `daemon/volumes.go`) -> Impact: **107.1** | LOC: 236
  * *Intent:* // registerMountPoints initializes the container mount points with the configured volumes and bind mounts. // It follows the next sequence to decide w...

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `integration-cli/fixtures/https` | 7 | 35000.0 | 0.0% | 0.0% |
| `daemon` | 147 | 15005.82 | 17.28% | 54.99% |
| `integration-cli` | 99 | 14888.02 | 17.54% | 79.2% |
| `integration/testdata/https` | 2 | 10000.0 | 0.0% | 0.0% |
| `daemon/libnetwork` | 62 | 8079.48 | 14.26% | 70.01% |
| `client` | 235 | 6252.1 | 7.56% | 54.93% |
| `daemon/containerd` | 46 | 5412.7 | 14.6% | 52.66% |
| `client/testdata` | 1 | 5000.0 | 0.0% | 0.0% |
| `daemon/libnetwork/drivers/bridge` | 24 | 3400.9 | 14.13% | 69.06% |
| `daemon/builder/dockerfile` | 30 | 2761.18 | 15.1% | 64.23% |

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
- **Binary Anomalies (X-Ray):** `14` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `15676` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `client/testdata/key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-cli/fixtures/https/ca.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-cli/fixtures/https/client-cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-cli/fixtures/https/client-key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-cli/fixtures/https/client-rogue-key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-cli/fixtures/https/server-cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-cli/fixtures/https/server-key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-cli/fixtures/https/server-rogue-key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/testdata/https/client-key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/testdata/https/server-key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-cli/docker_cli_build_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.268)
- **Top Global Matches:** file_cluster_10: 8.268, file_cluster_15: 8.691, file_cluster_16: 9.594
- **Magnitude:** 2121.14 | **LOC:** 6246 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **32**; blast radius 0.172; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.4%), Mutation Surface (formerly State Flux) (51.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (51.5%), Guard Balance (formerly Safety Score) (48.7%)
- **Documentation Coverage:** 85.1459% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TestBuildExposeMorePorts` **(Many-Argument Workhorses)** (Impact: 76.0)
  * `TestBuildWithInaccessibleFilesInContext` **(Defensive Guards)** (Impact: 22.6)
    * *Intent:* // Issue #5270 - ensure we throw a better error than "unexpected EOF" // when we can't access files ...
  * `TestBuildEnvironmentReplacementEnv` **(Compute Cores)** (Impact: 20.0)
  * `TestBuildAddBadLinks` **(Defensive Guards)** (Impact: 19.1)
  * `TestBuildLabelsOverride` **(I/O & Config Routines)** (Impact: 15.2)
    * *Intent:* // Test cases in #22036
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 105 instances
* *Concurrency (weighted view):* 37
* *Memory Alloc (weighted view):* 6
* *State Mutation (weighted view):* 403
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 246`, `structural_boundaries: 233`, `args: 246`, `func_start: 246`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 193`, `planned_debt: 8`, `fragile_debt: 50`, `unreferenced_by_name: 183`
* *Architecture:* `io: 9`, `api: 694`, `concurrency: 7`, `import: 1`
* *Defense:* `safety: 65`, `doc: 159`, `test: 379`, `immutability_locks: 166`, `cleanup: 77`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` tar, bytes, context, json, errors, fmt, command, go-archive...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `daemon/libnetwork/network.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.539)
- **Top Global Matches:** file_cluster_4: 7.539, file_cluster_10: 9.134, file_cluster_15: 9.392
- **Magnitude:** 1388.24 | **LOC:** 2208 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **23** in-repo importer(s); it depends on **34**; blast radius 1.038; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (98.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.7%)
- **Documentation Coverage:** 56.3218% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ipamAllocateVersion` **(Many-Argument Workhorses)** (Impact: 77.1)
  * `UnmarshalJSON` **(Type Conversions)** (Impact: 58.5)
  * `delete` **(Many-Argument Workhorses)** (Impact: 45.9)
    * *Intent:* // This function gets called in 3 ways: // - Delete() -- (false, false) // remove if endpoint count ...
  * `createEndpoint` **(Many-Argument Workhorses)** (Impact: 40.0)
  * `ipamReleaseVersion` **(Defensive Guards)** (Impact: 28.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 159 instances
* *State Mutation (weighted view):* 537
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 324`, `structural_boundaries: 354`, `args: 104`, `func_start: 104`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 219`, `planned_debt: 36`, `fragile_debt: 2`, `unreferenced_by_name: 59`
* *Architecture:* `api: 82`, `import: 1`
* *Defense:* `safety: 74`, `doc: 102`, `sync_locks: 85`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.038
  * `Choke Point (Betweenness):` 0.000368 | `Ripple Effect (Closeness):` 0.020243
  * `Imports (Out-Degree: 29):` context, json, errors, fmt, errdefs, log, network, netiputil...
  * `Imported By (In-Degree: 23):` (Excluded from Brief to save tokens)

### `integration-cli/docker_cli_run_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.369)
- **Top Global Matches:** file_cluster_10: 7.369, file_cluster_12: 7.832, file_cluster_15: 8.733
- **Magnitude:** 1350.64 | **LOC:** 4378 | **CtrlFlow:** 4.7% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **37**; blast radius 0.722; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (93.7%), Mutation Surface (formerly State Flux) (91.2%), Concurrency Surface (formerly Concurrency) (61.9%), Guard Balance (formerly Safety Score) (48.5%)
- **Documentation Coverage:** 81.6216% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TestRunDisallowBindMountingRootToRoot` **(Many-Argument Workhorses)** (Impact: 57.3)
  * `TestRunMount` **(Compute Cores)** (Impact: 27.1)
  * `TestRunNoDupVolumes` **(Compute Cores)** (Impact: 19.5)
    * *Intent:* // Test for GH#10618
  * `TestRunCreateVolumesInSymlinkDir` **(I/O & Config Routines)** (Impact: 12.0)
    * *Intent:* // Volume path is a symlink which also exists on the host, and the host side is a file not a dir // ...
  * `TestRunVolumesFromSymlinkPath` **(I/O & Config Routines)** (Impact: 11.9)
    * *Intent:* // Tests that a volume path that has a symlink exists in a container mounting it with `--volumes-fro...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Race Conditions:* 18 instances
* *Amplified Cascading Flux:* 69 instances
* *High Risk Execution (weighted view):* 2
* *Concurrency (weighted view):* 112
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 430
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 168`, `structural_boundaries: 149`, `args: 237`, `func_start: 237`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 32`, `high_risk_execution: 7`, `state_mutation: 292`, `planned_debt: 36`, `fragile_debt: 10`, `unreferenced_by_name: 91`
* *Architecture:* `io: 4`, `api: 253`, `concurrency: 22`, `import: 1`
* *Defense:* `safety: 96`, `doc: 263`, `test: 402`, `immutability_locks: 12`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.722
  * `Choke Point (Betweenness):` 0.000196 | `Ripple Effect (Closeness):` 0.012509
  * `Imports (Out-Degree: 12):` bufio, bytes, context, json, errors, fmt, network, client...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `daemon/daemon_unix.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.399)
- **Top Global Matches:** file_cluster_4: 7.399, file_cluster_6: 7.454, file_cluster_15: 14.915
- **Magnitude:** 1270.88 | **LOC:** 1630 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **45**; blast radius 0.361; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (92.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.7%)
- **Documentation Coverage:** 83.9286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `verifyPlatformContainerResources` **(Many-Argument Workhorses)** (Impact: 165.9)
    * *Intent:* // verifyPlatformContainerResources performs platform-specific validation of the container's resourc...
  * `verifyPlatformContainerSettings` **(Many-Argument Workhorses)** (Impact: 75.8)
    * *Intent:* // verifyPlatformContainerSettings performs platform-specific validation of the // hostconfig and co...
  * `selectBIP` **(Many-Argument Workhorses)** (Impact: 47.4)
    * *Intent:* // selectBIP searches the addresses from family on bridge bridgeName for: // - An address that encom...
  * `getDefaultBridgeIPAMConf` **(Many-Argument Workhorses)** (Impact: 45.6)
    * *Intent:* // "bip": "192.168.1.1/24", // "fixed-cidr": "192.168.1.0/25", // // - the bridge's address is "192....
  * `parseSecurityOpt` **(Many-Argument Workhorses)** (Impact: 34.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 144 instances
* *State Mutation (weighted view):* 448
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 358`, `structural_boundaries: 219`, `args: 55`, `func_start: 55`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 160`, `planned_debt: 15`, `fragile_debt: 5`, `unreferenced_by_name: 25`
* *Architecture:* `io: 4`, `api: 1`, `import: 1`
* *Defense:* `safety: 61`, `doc: 53`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.361
  * `Choke Point (Betweenness):` 0.000376 | `Ripple Effect (Closeness):` 0.007344
  * `Imports (Out-Degree: 25):` bufio, context, fmt, v3, errdefs, log, blkiodev, container...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `daemon/daemon.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.831)
- **Top Global Matches:** file_cluster_4: 6.831, file_cluster_12: 9.285, file_cluster_15: 9.666
- **Magnitude:** 1133.32 | **LOC:** 1908 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 44.0%
- **Blast Radius:** changing it is visible to **36** in-repo importer(s); it depends on **78**; blast radius 1.191; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (92.0%), Debt Markers (formerly Tech Debt) (83.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 16.092% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `NewDaemon` **(Many-Argument Workhorses)** (Impact: 285.1)
    * *Intent:* // NewDaemon sets up everything for the daemon to be able to service // requests from the webserver.
  * `restore` **(Many-Argument Workhorses)** (Impact: 193.8)
  * `Shutdown` **(Compute Cores)** (Impact: 31.1)
    * *Intent:* // Shutdown stops the daemon.
  * `restartSwarmContainers` **(Defensive Guards)** (Impact: 19.3)
  * `networkOptions` **(Many-Argument Workhorses)** (Impact: 17.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 98 instances
* *Concurrency (weighted view):* 50
* *State Mutation (weighted view):* 304
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 294`, `structural_boundaries: 219`, `args: 53`, `func_start: 53`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 108`, `planned_debt: 23`, `fragile_debt: 1`, `unreferenced_by_name: 25`
* *Architecture:* `io: 4`, `api: 42`, `concurrency: 15`, `import: 1`
* *Defense:* `safety: 94`, `doc: 113`, `sync_locks: 30`, `immutability_locks: 1`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.191
  * `Choke Point (Betweenness):` 0.002322 | `Ripple Effect (Closeness):` 0.018143
  * `Imports (Out-Degree: 65):` context, sha256, binary, fmt, client, defaults, errdefs, log...
  * `Imported By (In-Degree: 36):` (Excluded from Brief to save tokens)

### `daemon/libnetwork/drivers/bridge/bridge_linux.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.888)
- **Top Global Matches:** file_cluster_6: 6.888, file_cluster_4: 8.324, file_cluster_9: 15.598
- **Magnitude:** 1122.08 | **LOC:** 1905 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **30** in-repo importer(s); it depends on **38**; blast radius 1.129; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.1%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (58.6%), Guard Balance (formerly Safety Score) (51.5%)
- **Documentation Coverage:** 75.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CreateEndpoint` **(Many-Argument Workhorses)** (Impact: 81.7)
  * `link` **(Many-Argument Workhorses)** (Impact: 56.0)
  * `createNetwork` **(Many-Argument Workhorses)** (Impact: 47.8)
  * `fromLabels` **(Defensive Guards)** (Impact: 45.6)
  * `ProgramExternalConnectivity` **(Many-Argument Workhorses)** (Impact: 43.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 85 instances
* *State Mutation (weighted view):* 262
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 339`, `structural_boundaries: 310`, `args: 51`, `func_start: 51`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 92`, `planned_debt: 18`, `fragile_debt: 1`, `unreferenced_by_name: 17`
* *Architecture:* `api: 59`, `import: 1`
* *Defense:* `safety: 100`, `doc: 116`, `sync_locks: 67`, `immutability_locks: 6`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.129
  * `Choke Point (Betweenness):` 0.000773 | `Ripple Effect (Closeness):` 0.015792
  * `Imports (Out-Degree: 29):` context, fmt, log, netiputil, otelutil, stringid, datastore, driverapi...
  * `Imported By (In-Degree: 30):` (Excluded from Brief to save tokens)

### `integration-cli/docker_cli_daemon_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.495)
- **Top Global Matches:** file_cluster_10: 7.495, file_cluster_15: 8.007, file_cluster_12: 8.321
- **Magnitude:** 914.62 | **LOC:** 2256 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **37**; blast radius 0.172; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.5%), Mutation Surface (formerly State Flux) (98.6%), Concurrency Surface (formerly Concurrency) (93.6%), Guard Balance (formerly Safety Score) (45.6%)
- **Documentation Coverage:** 64.3312% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testDaemonStartIpcMode` **(Many-Argument Workhorses)** (Impact: 19.4)
  * `TestDaemonUlimitDefaults` **(I/O & Config Routines)** (Impact: 14.9)
  * `TestDaemonRestartWithPausedContainer` **(Defensive Guards)** (Impact: 14.4)
  * `TestDaemonLoggingDriverNoneOverride` **(Defensive Guards)** (Impact: 13.3)
  * `TestDaemonRestartKillWait` **(Defensive Guards)** (Impact: 12.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 51 instances
* *Concurrency (weighted view):* 99
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 282
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 139`, `structural_boundaries: 86`, `args: 80`, `func_start: 80`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 3`, `state_mutation: 180`, `planned_debt: 3`, `fragile_debt: 5`, `unreferenced_by_name: 78`
* *Architecture:* `io: 15`, `api: 89`, `concurrency: 19`, `import: 1`
* *Defense:* `safety: 44`, `doc: 84`, `test: 370`, `immutability_locks: 8`, `cleanup: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` bufio, bytes, context, tls, x509, json, fmt, helpers...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `daemon/container_operations.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.397)
- **Top Global Matches:** file_cluster_6: 5.397, file_cluster_4: 10.356, file_cluster_8: 14.668
- **Magnitude:** 911.26 | **LOC:** 1147 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **31**; blast radius 0.304; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.9%), Debt Markers (formerly Tech Debt) (49.8%)
- **Documentation Coverage:** 65.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `connectToNetwork` **(Many-Argument Workhorses)** (Impact: 82.8)
  * `buildSandboxOptions` **(Many-Argument Workhorses)** (Impact: 54.2)
  * `findAndAttachNetwork` **(Many-Argument Workhorses)** (Impact: 52.6)
  * `validateEndpointSettings` **(Many-Argument Workhorses)** (Impact: 40.6)
    * *Intent:* // validateEndpointSettings checks whether the given epConfig is valid. The nw parameter can be nil,...
  * `initializeNetworking` **(Many-Argument Workhorses)** (Impact: 37.8)
    * *Intent:* // initializeNetworking prepares network configuration for a new container. // If it creates a new l...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 95 instances
* *State Mutation (weighted view):* 293
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 248`, `structural_boundaries: 163`, `args: 30`, `func_start: 30`
* *Risk/State:* `state_mutation: 103`, `planned_debt: 9`, `fragile_debt: 2`, `unreferenced_by_name: 7`
* *Architecture:* `api: 5`, `import: 1`
* *Defense:* `safety: 62`, `doc: 44`, `sync_locks: 6`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.304
  * `Choke Point (Betweenness):` 9.7e-05 | `Ripple Effect (Closeness):` 0.012504
  * `Imports (Out-Degree: 21):` context, errors, fmt, errdefs, log, container, events, network...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `daemon/network.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.856)
- **Top Global Matches:** file_cluster_4: 5.856, file_cluster_15: 9.366, file_cluster_16: 10.183
- **Magnitude:** 882.72 | **LOC:** 1237 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **38**; blast radius 0.382; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (87.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (61.5%)
- **Documentation Coverage:** 34.7826% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createNetwork` **(Many-Argument Workhorses)** (Impact: 85.0)
  * `buildCreateEndpointOptions` **(Many-Argument Workhorses)** (Impact: 68.6)
    * *Intent:* // buildCreateEndpointOptions builds endpoint options from a given network.
  * `buildIPAMResources` **(Compute Cores)** (Impact: 31.7)
    * *Intent:* // buildIPAMResources constructs a [network.IPAM] from the network's // IPAM information for inclusi...
  * `buildPortsRelatedCreateEndpointOptions` **(Many-Argument Workhorses)** (Impact: 31.6)
    * *Intent:* // buildPortsRelatedCreateEndpointOptions returns the appropriate endpoint options to apply config r...
  * `buildEndpointInfo` **(Many-Argument Workhorses)** (Impact: 24.6)
    * *Intent:* // buildEndpointInfo sets endpoint-related fields on container.NetworkSettings based on the provided...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 96 instances
* *Concurrency (weighted view):* 11
* *State Mutation (weighted view):* 294
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 218`, `structural_boundaries: 175`, `args: 47`, `func_start: 47`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 102`, `planned_debt: 15`, `unreferenced_by_name: 21`
* *Architecture:* `api: 23`, `concurrency: 6`, `import: 1`
* *Defense:* `safety: 28`, `doc: 49`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.382
  * `Choke Point (Betweenness):` 0.000197 | `Ripple Effect (Closeness):` 0.012561
  * `Imports (Out-Degree: 30):` context, errors, fmt, log, container, events, network, provider...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `daemon/oci_linux.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.017)
- **Top Global Matches:** file_cluster_6: 6.017, file_cluster_4: 8.699, file_cluster_15: 16.507
- **Magnitude:** 843.26 | **LOC:** 1077 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 80.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **29**; blast radius 0.284; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.2%), Complexity Load (formerly Cognitive Load) (42.2%)
- **Documentation Coverage:** 41.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `withMounts` **(Many-Argument Workhorses)** (Impact: 144.8)
    * *Intent:* // withMounts sets the container's mounts
  * `WithNamespaces` **(Many-Argument Workhorses)** (Impact: 57.0)
    * *Intent:* // WithNamespaces sets the container's namespaces
  * `withCommonOptions` **(Many-Argument Workhorses)** (Impact: 39.6)
    * *Intent:* // withCommonOptions sets common docker options
  * `withCgroups` **(Many-Argument Workhorses)** (Impact: 37.4)
    * *Intent:* // withCgroups sets the container's cgroups
  * `WithDevices` **(Many-Argument Workhorses)** (Impact: 29.5)
    * *Intent:* // WithDevices sets the container's devices
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 112 instances
* *State Mutation (weighted view):* 343
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 202`, `structural_boundaries: 133`, `args: 27`, `func_start: 27`
* *Risk/State:* `state_mutation: 119`, `planned_debt: 1`, `fragile_debt: 3`
* *Architecture:* `io: 1`, `api: 9`, `import: 1`
* *Defense:* `safety: 37`, `doc: 36`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.284
  * `Choke Point (Betweenness):` 0.000402 | `Ripple Effect (Closeness):` 0.009222
  * `Imports (Out-Degree: 20):` context, fmt, v3, containers, apparmor, oci, log, container...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `daemon/logger/awslogs/cloudwatchlogs_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.106)
- **Top Global Matches:** file_cluster_10: 7.106, file_cluster_15: 7.647, file_cluster_12: 8.718
- **Magnitude:** 831.38 | **LOC:** 1726 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 0.172; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (86.5%), Debt Markers (formerly Tech Debt) (62.8%), Complexity Load (formerly Cognitive Load) (62.0%)
- **Documentation Coverage:** 96.7742% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TestLogBlocking` **(Compute Cores)** (Impact: 11.6)
    * *Intent:* // TestLogBlocking tests that the Log method blocks appropriately when // non-blocking behavior is n...
  * `TestNewStreamConfig` **(I/O & Config Routines)** (Impact: 11.4)
  * `TestValidateLogOptionsFormat` **(Compute Cores)** (Impact: 10.3)
  * `TestCollectBatchWithDuplicateTimestamps` **(Compute Cores)** (Impact: 10.2)
  * `TestCollectBatchMaxTotalBytes` **(I/O & Config Routines)** (Impact: 8.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 31 instances
* *Amplified Race Conditions:* 62 instances
* *Amplified Cascading Flux:* 18 instances
* *Concurrency (weighted view):* 372
* *Memory Alloc (weighted view):* 30
* *State Mutation (weighted view):* 159
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 182`, `args: 47`, `func_start: 47`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 123`, `unreferenced_by_name: 45`
* *Architecture:* `io: 2`, `api: 45`, `concurrency: 62`, `import: 1`
* *Defense:* `safety: 3`, `doc: 23`, `test: 209`, `sync_locks: 1`, `immutability_locks: 1`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` context, errors, fmt, aws, config, credentials, cloudwatchlogs, types...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `daemon/server/router/container/container_routes.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.329)
- **Top Global Matches:** file_cluster_4: 7.329, file_cluster_9: 7.898, file_cluster_15: 8.283
- **Magnitude:** 811.98 | **LOC:** 1210 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **31**; blast radius 0.209; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Debt Markers (formerly Tech Debt) (89.9%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (59.6%)
- **Documentation Coverage:** 94.1176% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `postContainersCreate` **(Many-Argument Workhorses)** (Impact: 157.5)
  * `postContainersWait` **(Many-Argument Workhorses)** (Impact: 36.7)
  * `handleMACAddressBC` **(Many-Argument Workhorses)** (Impact: 36.0)
    * *Intent:* // handleMACAddressBC takes care of backward-compatibility for the container-wide MAC address by mut...
  * `handleSysctlBC` **(Many-Argument Workhorses)** (Impact: 31.4)
    * *Intent:* // // Because interface names ('ethN') are allocated sequentially, and the order of // network conne...
  * `getContainersJSON` **(Many-Argument Workhorses)** (Impact: 29.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 62 instances
* *Concurrency (weighted view):* 15
* *State Mutation (weighted view):* 188
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 207`, `structural_boundaries: 189`, `args: 29`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 64`, `planned_debt: 3`, `fragile_debt: 2`, `unreferenced_by_name: 22`
* *Architecture:* `io: 6`, `api: 25`, `concurrency: 5`, `import: 1`
* *Defense:* `safety: 60`, `doc: 64`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.209
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.000343
  * `Imports (Out-Degree: 15):` bytes, context, json, fmt, log, platforms, types, container...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `daemon/libnetwork/endpoint.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.989)
- **Top Global Matches:** file_cluster_4: 6.989, file_cluster_12: 10.062, file_cluster_15: 10.497
- **Magnitude:** 780.3 | **LOC:** 1362 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 80.0%
- **Blast Radius:** changing it is visible to **17** in-repo importer(s); it depends on **21**; blast radius 0.78; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.7%)
- **Documentation Coverage:** 58.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sbLeave` **(Many-Argument Workhorses)** (Impact: 70.7)
  * `sbJoin` **(Many-Argument Workhorses)** (Impact: 43.4)
  * `UnmarshalJSON` **(Many-Argument Workhorses)** (Impact: 35.2)
  * `assignAddressVersion` **(Many-Argument Workhorses)** (Impact: 30.5)
  * `updateExternalConnectivity` **(Many-Argument Workhorses)** (Impact: 29.2)
    * *Intent:* // updateExternalConnectivity configures an Endpoint when it becomes the gateway // endpoint for a n...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 73 instances
* *State Mutation (weighted view):* 270
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 185`, `structural_boundaries: 184`, `args: 61`, `func_start: 61`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 124`, `planned_debt: 25`, `fragile_debt: 8`, `unreferenced_by_name: 39`
* *Architecture:* `api: 38`, `import: 1`
* *Defense:* `safety: 60`, `doc: 61`, `sync_locks: 68`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.78
  * `Choke Point (Betweenness):` 0.000141 | `Ripple Effect (Closeness):` 0.01978
  * `Imports (Out-Degree: 17):` context, json, errors, fmt, errdefs, log, stringid, datastore...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `daemon/libnetwork/ipams/defaultipam/allocator_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.298)
- **Top Global Matches:** file_cluster_4: 9.298, file_cluster_12: 11.715, file_cluster_6: 12.062
- **Magnitude:** 778.5 | **LOC:** 1350 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 0.172; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (82.9%), Guard Balance (formerly Safety Score) (57.4%), Complexity Load (formerly Cognitive Load) (34.0%)
- **Documentation Coverage:** 90.1639% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TestSerializeRequestReleaseAddressFromSubPool` **(Defensive Guards)** (Impact: 50.0)
  * `TestRequestReleaseAddressFromSubPool` **(Defensive Guards)** (Impact: 49.8)
  * `TestAddReleasePoolID` **(Defensive Guards)** (Impact: 47.4)
  * `testAllocateRandomDeallocate` **(Many-Argument Workhorses)** (Impact: 37.4)
  * `TestRequestReleaseAddressDuplicate` **(Compute Cores)** (Impact: 24.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 89 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 279
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 214`, `structural_boundaries: 35`, `args: 33`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 101`, `fragile_debt: 1`, `unreferenced_by_name: 28`
* *Architecture:* `api: 28`, `concurrency: 2`, `import: 1`
* *Defense:* `safety: 100`, `doc: 34`, `test: 52`, `sync_locks: 5`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` context, errors, flag, fmt, netiputil, addrset, ipamapi, ipamutils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `daemon/libnetwork/cmd/networkdb-test/dbclient/ndbClient.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.154)
- **Top Global Matches:** file_cluster_15: 7.154, file_cluster_4: 8.271, file_cluster_16: 8.614
- **Magnitude:** 766.94 | **LOC:** 856 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **11**; blast radius 0.245; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (73.3%)
- **Documentation Coverage:** 94.7368% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Client` **(I/O & Config Routines)** (Impact: 37.9)
    * *Intent:* // Client is a client
  * `checkTable` **(Many-Argument Workhorses)** (Impact: 36.1)
  * `doNetworkStatsQueue` **(Compute Cores)** (Impact: 17.2)
    * *Intent:* // network-stats-queue networkName <gt/lt> queueSize
  * `doClusterPeers` **(Compute Cores)** (Impact: 15.4)
    * *Intent:* // cluster-peers expectedNumberPeers maxRetry
  * `doNetworkPeers` **(Compute Cores)** (Impact: 15.4)
    * *Intent:* // network-peers networkName expectedNumberPeers maxRetry
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 37 instances
* *Amplified Cascading Flux:* 45 instances
* *Concurrency (weighted view):* 262
* *State Mutation (weighted view):* 148
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 118`, `args: 37`, `func_start: 37`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 58`, `planned_debt: 29`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 1`, `concurrency: 77`, `import: 1`
* *Defense:* `safety: 8`, `doc: 31`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.245
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000343
  * `Imports (Out-Degree: 0):` context, fmt, log, io, net, http, os, regexp...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `daemon/libnetwork/internal/rlkclient/rootlesskit_client_linux.go` (GO) | Magnitude: 76.28 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 111, structural_boundaries: 33, branch: 22, doc: 12
- `client/internal/json-stream.go` (GO) | Magnitude: 22.94 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 24, structural_boundaries: 12, branch: 5, api: 5
- `daemon/server/router/image/image_list_response_test.go` (GO) | Magnitude: 20.2 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 60, test: 14, structural_boundaries: 8, serialization_parsing: 4
- `integration/system/cgroupdriver_systemd_test.go` (GO) | Magnitude: 7.96 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 31, structural_boundaries: 6, test: 5, args: 2
- `daemon/libnetwork/internal/addrset/addrset_test.go` (GO) | Magnitude: 105.6 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 234, test: 124, state_mutation: 51, core_var_decl: 51

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `integration/container/mounts_linux_test.go` (GO) | Magnitude: 134.5 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 499, test: 44, branch: 35, doc: 26
- `daemon/libnetwork/default_gateway_windows.go` (GO) | Magnitude: 2.84 | Delta: **0.114** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 9, structural_boundaries: 4, encapsulation: 3, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `daemon/internal/layer/migration.go` (GO) | Magnitude: 91.98 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 119, structural_boundaries: 33, branch: 21, state_mutation: 9
- `daemon/libnetwork/drivers/overlay/bpf_linux_test.go` (GO) | Magnitude: 90.3 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 145, branch: 28, structural_boundaries: 22, doc: 13
- `daemon/libnetwork/internal/modprobe/modprobe_linux.go` (GO) | Magnitude: 32.86 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 56, structural_boundaries: 22, branch: 8, encapsulation: 8
- `pkg/ioutils/readers.go` (GO) | Magnitude: 69.44 | Delta: **0.047** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 61, structural_boundaries: 16, branch: 10, doc: 10
- `hack/validate/module-replace` (SHELL) | Magnitude: 53.7 | Delta: **0.053** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: io: 42, structural_boundaries: 40, indent_tabs: 34, debug_prints: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `daemon/graphdriver/zfs/zfs_test.go` (GO) | Magnitude: 0.02 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 8, args: 6, func_start: 6, api: 6
- `daemon/errors_test.go` (GO) | Magnitude: 2.78 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 4, structural_boundaries: 2, test: 2, args: 1
- `daemon/graphdriver/fuse-overlayfs/fuseoverlayfs_test.go` (GO) | Magnitude: 43.42 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 21, args: 16, func_start: 16, unreferenced_by_name: 16
- `api/types/swarm/common.go` (GO) | Magnitude: 18.68 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: api: 17, structural_boundaries: 15, indent_tabs: 14, decorators: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `contrib/nuke-graph-directory.sh` (SHELL) | Magnitude: 0.46 | Delta: **0.074** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 36, indent_tabs: 35, branch: 14, debug_prints: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `daemon/logger/factory.go` (GO) | Magnitude: 80.26 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 106, structural_boundaries: 45, branch: 22, sync_locks: 13
- `daemon/events.go` (GO) | Magnitude: 237.7 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 194, branch: 50, state_mutation: 29, structural_boundaries: 27
- `daemon/libnetwork/internal/addrset/addrset.go` (GO) | Magnitude: 123.8 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 142, structural_boundaries: 45, branch: 32, doc: 19
- `daemon/graphdriver/overlay2/overlay_test.go` (GO) | Magnitude: 53.8 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 34, args: 19, func_start: 19, unreferenced_by_name: 18
- `daemon/resize_test.go` (GO) | Magnitude: 27.18 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 81, pointers: 13, structural_boundaries: 9, state_mutation: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `daemon/builder/dockerfile/internals_windows.go` (GO) | Magnitude: 49.98 | Delta: **0.073** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 72, branch: 14, structural_boundaries: 14, doc: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `daemon/internal/builder-next/worker/label/label.go` (GO) | Magnitude: 15.6 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: state_mutation: 2, globals: 2, indent_tabs: 2, core_var_decl: 2
- `cmd/docker-proxy/proxy_linux.go` (GO) | Magnitude: 16.2 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: doc: 6, structural_boundaries: 4, indent_tabs: 4, globals: 2
- `daemon/libnetwork/ipamapi/labels.go` (GO) | Magnitude: 16.6 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: api: 2, state_mutation: 2, doc: 2, globals: 2
- `daemon/pkg/opts/hosts_unix.go` (GO) | Magnitude: 16.6 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: api: 2, state_mutation: 2, doc: 2, globals: 2
- `daemon/pkg/opts/hosts_windows.go` (GO) | Magnitude: 16.6 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: doc: 11, fragile_debt: 3, api: 2, state_mutation: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `daemon/internal/usergroup/utils_unix.go` (GO) | Magnitude: 6.9 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 15, structural_boundaries: 6, branch: 3, safety: 2
- `client/network_create.go` (GO) | Magnitude: 36.9 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 46, api: 17, doc: 15, structural_boundaries: 11
- `daemon/pkg/oci/caps/utils_other.go` (GO) | Magnitude: 1.16 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 1, args: 1, func_start: 1, encapsulation: 1
- `client/container_wait_example_test.go` (GO) | Magnitude: 6.4 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 20, structural_boundaries: 3, branch: 2, safety: 2
- `daemon/builder/builder.go` (GO) | Magnitude: 35.32 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 41, structural_boundaries: 27, doc: 26, api: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `daemon/container_operations_unix.go` (GO) | Magnitude: 318.66 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 422, branch: 108, structural_boundaries: 96, safety: 51
- `daemon/daemon_unix.go` (GO) | Magnitude: 1270.88 | Delta: **0.055** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 1077, branch: 358, structural_boundaries: 219, state_mutation: 160
- `daemon/libnetwork/drivers/windows/windows.go` (GO) | Magnitude: 636.64 | Delta: **0.098** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 658, branch: 146, structural_boundaries: 143, state_mutation: 74
- `daemon/network/filter.go` (GO) | Magnitude: 113.62 | Delta: **0.126** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 141, branch: 46, structural_boundaries: 44, args: 8
- `daemon/command/daemon.go` (GO) | Magnitude: 627.18 | Delta: **0.129** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 827, branch: 186, structural_boundaries: 125, state_mutation: 67

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `internal/testutil/request/helpers.go` (GO) | Magnitude: 14.0 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_tabs: 18, structural_boundaries: 8, branch: 2, args: 2
- `hack/validate/dco` (SHELL) | Magnitude: 47.08 | Delta: **0.073** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_tabs: 29, structural_boundaries: 26, io: 12, debug_prints: 12
- `integration/plugin/logging/validation_test.go` (GO) | Magnitude: 5.14 | Delta: **0.116** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 22, structural_boundaries: 4, doc: 2, test: 2
- `hack/validate/golangci-lint` (SHELL) | Magnitude: 21.88 | Delta: **0.132** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: structural_boundaries: 10, indent_tabs: 9, io: 7, branch: 5
- `daemon/libnetwork/support/support.sh` (SHELL) | Magnitude: 109.64 | Delta: **0.161** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: structural_boundaries: 69, indent_tabs: 68, io: 64, debug_prints: 41

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `daemon/libnetwork/portallocator/osallocator_linux.go` (GO) | Magnitude: 173.48 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 213, branch: 48, structural_boundaries: 48, ipc_rpc_bridges: 46
- `client/image_build_test.go` (GO) | Magnitude: 29.84 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 180, structural_boundaries: 21, branch: 8, test: 8
- `daemon/containerd/image_snapshot_unix.go` (GO) | Magnitude: 78.8 | Delta: **0.075** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 110, structural_boundaries: 38, branch: 22, safety: 14
- `client/hijack_test.go` (GO) | Magnitude: 79.62 | Delta: **0.114** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 101, structural_boundaries: 22, state_mutation: 18, test: 12
- `daemon/libnetwork/drivers/bridge/internal/iptabler/port.go` (GO) | Magnitude: 124.46 | Delta: **0.116** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 147, branch: 32, structural_boundaries: 31, doc: 12

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `.github/workflows/.windows.yml` -> Churn: **96.08%** | Cog Load: 5.391% | Debt: 99.9592%
- `.github/workflows/arm64.yml` -> Churn: **96.08%** | Cog Load: 4.1818% | Debt: 76.9183%
- `daemon/daemon.go` -> Churn: **92.05%** | Cog Load: 39.4745% | Debt: 82.9642%
- `client/client.go` -> Churn: **81.0%** | Cog Load: 15.5562% | Debt: 93.2655%
- `client/client_options.go` -> Churn: **80.87%** | Cog Load: 12.7566% | Debt: 99.9806%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `daemon/logger/awslogs/cloudwatchlogs_test.go` -> **Paweł Gronowski** (100.0% isolated ownership) | Magnitude: 831.38
- `daemon/libnetwork/ipams/defaultipam/allocator_test.go` -> **Paweł Gronowski** (100.0% isolated ownership) | Magnitude: 778.5
- `daemon/libnetwork/cmd/networkdb-test/dbclient/ndbClient.go` -> **Paweł Gronowski** (100.0% isolated ownership) | Magnitude: 766.94
- `daemon/logger/splunk/splunk_test.go` -> **Paweł Gronowski** (100.0% isolated ownership) | Magnitude: 745.7
- `internal/testutil/daemon/daemon.go` -> **Sebastiaan van Stijn** (100.0% isolated ownership) | Magnitude: 689.76

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `daemon/daemon.go` -> **Severity: 0.232** (Bridge: 0.0023 * Flux: 99.816%)
- `daemon/container/container.go` -> **Severity: 0.194** (Bridge: 0.002 * Flux: 99.0095%)
- `daemon/libnetwork/agent.go` -> **Severity: 0.115** (Bridge: 0.0012 * Flux: 99.2166%)
- `internal/testutil/daemon/daemon.go` -> **Severity: 0.108** (Bridge: 0.0011 * Flux: 99.9554%)
- `daemon/libnetwork/drivers/bridge/bridge_linux.go` -> **Severity: 0.077** (Bridge: 0.0008 * Flux: 99.142%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `api/types/network/endpoint.go` -> **Severity: 5.493** (Embedded: 0.0968 * Error Risk: 56.7444%)
- `client/client.go` -> **Severity: 5.37** (Embedded: 0.0969 * Error Risk: 55.4118%)
- `client/filters.go` -> **Severity: 4.167** (Embedded: 0.0776 * Error Risk: 53.7075%)
- `client/pkg/versions/compare.go` -> **Severity: 3.889** (Embedded: 0.0628 * Error Risk: 61.9096%)
- `client/client_options.go` -> **Severity: 3.8** (Embedded: 0.0696 * Error Risk: 54.6179%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `client/request.go` -> **Severity: 748.805** (Blast Radius: 13.288 * Doc Risk: 56.352%)
- `daemon/internal/layer/layer_store.go` -> **Severity: 680.762** (Blast Radius: 7.148 * Doc Risk: 95.2381%)
- `client/utils.go` -> **Severity: 486.089** (Blast Radius: 9.953 * Doc Risk: 48.8384%)
- `client/client.go` -> **Severity: 463.474** (Blast Radius: 25.702 * Doc Risk: 18.0326%)
- `daemon/internal/lazyregexp/lazyregexp.go` -> **Severity: 439.358** (Blast Radius: 4.793 * Doc Risk: 91.6667%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 663 literal sites + 4 sites through wrappers = 667
- **`panics_and_aborts`:** 329 literal sites + 5 sites through wrappers = 334

- `die` (function, debug_prints, primitive): 4 call sites in 1 files -- `daemon/libnetwork/support/support.sh`
- `die` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `daemon/libnetwork/support/support.sh`
- `npipeDial` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `internal/testutil/request/npipe.go`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 74124 call pairs -- scoped 25.1%, unique 5.5%, ambiguous 33.1%, external 36.4%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| go | 73382 | 25.1% | 5.5% | 33.4% | 35.9% |
| shell | 538 | 21.4% | 0.7% | 0.0% | 77.9% |
| lua | 93 | 9.7% | 0.0% | 0.0% | 90.3% |
| python | 54 | 9.3% | 0.0% | 0.0% | 90.7% |
| c | 37 | 0.0% | 0.0% | 0.0% | 100.0% |
| powershell | 19 | 0.0% | 0.0% | 0.0% | 100.0% |
| makefile | 1 | 0.0% | 0.0% | 0.0% | 100.0% |

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
