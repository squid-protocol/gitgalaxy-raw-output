# ARCHITECTURAL_BRIEF: terraform
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/hashicorp/terraform` |
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
| Total Artifacts | 5161 |
| Analyzed Artifacts (Scanned) | 2397 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2764 |
| Total LOC | 492438 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 46.4% |
| Dominant Lang | GO |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4395 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.279 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.825 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 44 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| GO | 1841 | 466989 | 76.8% |
| JSON | 379 | 23504 | 15.8% |
| PLAINTEXT | 107 | 12 | 4.5% |
| MARKDOWN | 27 | 0 | 1.1% |
| SHELL | 19 | 564 | 0.8% |
| PROTO | 11 | 1301 | 0.5% |
| XML | 9 | 0 | 0.4% |
| DOCKERFILE | 2 | 32 | 0.1% |
| MAKEFILE | 1 | 23 | 0.0% |
| YAML | 1 | 13 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +0.37; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 27%, Compute Cores Files 20%, Callbacks & Closures Files 17%, Large Core Modules 15%, State Mutators Files 5%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 2261 | 94.3% |
| Unknown | 12 | 0.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 122 | 5.1% |
| Static: Minified & Vendor Opaque Mass | 2 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2764*

**Composition by Extension & Reason:**
- `.tf`: 1631x Excluded (Unsupported Extension: '.tf'), 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.hcl`: 448x Excluded (Unsupported Extension: '.hcl'), 44x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 150x Unsupported Format (.undeterminable), 41x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Unresolved Ambiguity (No Retainable Structure)
- `.tfstate`: 146x Excluded (Unsupported Extension: '.tfstate'), 42x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.go`: 4x Excluded (Machine-Generated Source Code Signature: 30 LOC), 3x Excluded (Machine-Generated Source Code Signature: 27 LOC), 3x Excluded (Machine-Generated Source Code Signature: 34 LOC)
- `.json`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 1547 LOC), 1x Excluded (Static Asset Blob without Intent: 1548 LOC)
- `.md`: 21x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 17x Excluded (Explicitly Denied Extension: '.png')
- `.yml`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tfvars`: 15x Excluded (Unsupported Extension: '.tfvars')
- `.zip`: 12x Excluded (Explicitly Denied Extension: '.zip')
- `.mod`: 11x Unsupported Format (.mod)
- `.sum`: 11x Excluded (Unsupported Extension: '.sum')
- `.log`: 4x Excluded (Saturation: Line 2 exceeds 500 chars), 3x Excluded (Saturation: Line 5 exceeds 500 chars), 2x Excluded (Saturation: Line 20 exceeds 500 chars)
- `.tmpl`: 8x Excluded (Unsupported Extension: '.tmpl')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 89.3 | 10.8 | 5.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 38.0 | 48.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 31.5 | 19.1 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 14.7 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 12.0 | 5.3 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 42.3 | 20.3 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 85.0 | 2.0 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 77.5 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 6.3 | 0.5 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 5.3 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 50.1 | 50.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 31633 | 1461 | 29 | `internal/legacy/helper/schema/schema_test.go` |
| cleanup | 480 | 201 | 0 | `internal/communicator/ssh/communicator.go` |
| guards | 11277 | 1378 | 12 | `internal/terraform/terraform_test.go` |
| danger | 2327 | 471 | 2 | `internal/cloud/tfe_client_mock.go` |
| concurrency | 2316 | 274 | 1 | `internal/terraform/context_apply_test.go` |
| connectivity | 17616 | 1664 | 18 | `internal/providers/provider.go` |
| io | 647 | 196 | 0 | `.github/scripts/equivalence-test.sh` |
| crypto | 0 | 0 | 0 | - |
| ipc | 123 | 42 | 0 | `internal/command/clistate/local_state_lock_windows.go` |
| time | 446 | 135 | 0 | `internal/stacks/stackruntime/plan_test.go` |
| serialization | 201 | 95 | 0 | `internal/command/state_identities_test.go` |
| regex | 84 | 36 | 0 | `internal/terraform/transform_destroy_cbd_test.go` |
| events | 104 | 25 | 0 | `internal/backend/remote-state/s3/client.go` |
| tests | 7158 | 676 | 7 | `internal/plugin6/grpc_provider_test.go` |
| docs | 22675 | 1842 | 24 | `internal/command/meta_backend_test.go` |
| debt | 1128 | 386 | 1 | `internal/cloud/tfe_client_mock.go` |
| mutation | 45735 | 1418 | 43 | `internal/terraform/context_apply_test.go` |
| dead_code | 7184 | 1447 | 7 | `internal/terraform/context_apply_test.go` |
| credential | 55 | 36 | 0 | `internal/lang/funcs/crypto_test.go` |
| threat | 469 | 144 | 0 | `internal/copy/copy_value.go` |
| ml_ai | 18 | 10 | 0 | `scripts/changelog.sh` |
| ui | 3 | 3 | 0 | `internal/command/testdata/login-oauth-server/oauthserver.go` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `.github/scripts/equivalence-test.sh` (Hits: 56)
- `scripts/changelog.sh` (Hits: 50)
- `internal/communicator/ssh/communicator.go` (Hits: 23)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **fmt.go** (`internal/command/fmt.go`) — 818 inbound connections
2. **context.go** (`internal/terraform/context.go`) — 316 inbound connections
3. **states.go** (`internal/moduletest/states/states.go`) — 253 inbound connections
4. **log.go** (`internal/backend/remote-state/oci/log.go`) — 221 inbound connections
5. **cmp.go** (`internal/collections/cmp.go`) — 220 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **test_test.go** (`internal/command/test_test.go`) — 194 outbound dependencies
2. **renderer_test.go** (`internal/command/jsonformat/computed/renderers/renderer_test.go`) — 149 outbound dependencies
3. **functions_test.go** (`internal/lang/functions_test.go`) — 146 outbound dependencies
4. **differ_test.go** (`internal/command/jsonformat/differ/differ_test.go`) — 144 outbound dependencies
5. **context_apply_test.go** (`internal/terraform/context_apply_test.go`) — 134 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `TestContextPlan_actions` **(Compute Cores)** (@ `internal/terraform/context_plan_actions_test.go`) -> Impact: **259.7** | LOC: 1800
- `EnsureProviderVersions` **(Many-Argument Workhorses)** (@ `internal/providercache/installer.go`) -> Impact: **235.2** | LOC: 544
  * *Intent:* // The given mode modifies how the operation will treat providers that already // have acceptable versions available in the target cache directory. Se...
- `plan` **(Many-Argument Workhorses)** (@ `internal/terraform/node_resource_abstract_instance.go`) -> Impact: **217.2** | LOC: 572
- `opApply` **(Many-Argument Workhorses)** (@ `internal/backend/local/backend_apply.go`) -> Impact: **209.8** | LOC: 440
- `validateProviderConfigs` **(Many-Argument Workhorses)** (@ `internal/configs/provider_validation.go`) -> Impact: **205.5** | LOC: 510
  * *Intent:* // however will generate an error if a suitable provider configuration is not // passed in through the module call. // // The parentCall argument is t...
- `TestContextApply_actions` **(Compute Cores)** (@ `internal/terraform/context_apply_action_test.go`) -> Impact: **186.3** | LOC: 1803
- `apply` **(Many-Argument Workhorses)** (@ `internal/terraform/node_resource_abstract_instance.go`) -> Impact: **175.2** | LOC: 383
  * *Intent:* // apply accepts an applyConfig, instead of using n.Config, so destroy plans can // send a nil config. The keyData information can be empty if the con...
- `backendFromConfig` **(Compute Cores)** (@ `internal/command/meta_backend.go`) -> Impact: **174.7** | LOC: 440
  * *Intent:* // backendFromConfig returns the initialized (not configured) backend // directly from the config/state.. // // This function handles various edge cas...
- `getType` **(Many-Argument Workhorses)** (@ `internal/stacks/stackconfig/typeexpr/typeexpr.go`) -> Impact: **170.9** | LOC: 333
- `opApply` **(Many-Argument Workhorses)** (@ `internal/backend/remote/backend_apply.go`) -> Impact: **165.9** | LOC: 276

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `internal/terraform` | 239 | 40545.66 | 12.93% | 51.22% |
| `internal/backend/remote-state/http/testdata/certs` | 6 | 30000.0 | 0.0% | 0.0% |
| `internal/command` | 120 | 21792.48 | 14.13% | 45.72% |
| `internal/pluginshared/testdata` | 3 | 10000.0 | 0.0% | 0.0% |
| `internal/releaseauth/testdata` | 3 | 10000.0 | 0.0% | 0.0% |
| `internal/cloud` | 40 | 9289.26 | 19.94% | 41.72% |
| `internal/configs` | 58 | 8967.04 | 14.17% | 32.7% |
| `internal/stacks/stackruntime/internal/stackeval` | 70 | 7422.98 | 13.67% | 62.06% |
| `internal/legacy/helper/schema` | 40 | 7235.04 | 15.16% | 14.26% |
| `internal/addrs` | 63 | 5128.06 | 8.66% | 42.05% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `internal/command/jsonformat/computed/renderers/util.go` -> **100.0%** Exposure
- `internal/experiments/experiment.go` -> **100.0%** Exposure
- `internal/lang/data_test.go` -> **100.0%** Exposure
- `internal/rpcapi/handles.go` -> **100.0%** Exposure
- `internal/schemarepo/loadschemas/plugins.go` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `.github/scripts/get_product_version.sh` -> **100.0%** Exposure
- `scripts/build.sh` -> **100.0%** Exposure
- `internal/backend/remote-state/oci/constants.go` -> **100.0%** Exposure
- `internal/cloud/backend_apply.go` -> **100.0%** Exposure
- `internal/cloud/backend_context.go` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `internal/terraform/context_apply_test.go` -> **212** Orphaned Functions | **0** Duplicates
- `internal/terraform/context_plan_test.go` -> **131** Orphaned Functions | **0** Duplicates
- `internal/terraform/context_validate_test.go` -> **90** Orphaned Functions | **0** Duplicates
- `internal/terraform/context_plan2_test.go` -> **85** Orphaned Functions | **0** Duplicates
- `internal/command/init_test.go` -> **71** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `internal/command/stacks_test.go` -> **99.9864%** Exposure
- `internal/lang/funcs/crypto_test.go` -> **99.9454%** Exposure
- `internal/command/cloud_test.go` -> **99.4496%** Exposure
- `internal/lang/functions_test.go` -> **98.4283%** Exposure
- `internal/backend/remote-state/oci/backend_test.go` -> **78.1342%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `27` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `19791` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `internal/command/test.go` (GO) -> Cumulative Risk: **728.76**
- **Archetype:** `file_cluster_4` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.04)
- **Magnitude:** 257.1 | **LOC:** 456 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 83.3%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9985%), Concurrency (98.6086%)
- **Heaviest Functions:** `setupTestExecution` (Many-Argument Workhorses, Impact: 52.9), `Run` (Compute Cores, Impact: 31.9), `Help` (I/O & Config Routines, Impact: 8.0)

### 2. `internal/command/views/hook_json.go` (GO) -> Cumulative Risk: **721.61**
- **Archetype:** `file_cluster_3` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.96)
- **Magnitude:** 196.34 | **LOC:** 297 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `PostApply` (Many-Argument Workhorses, Impact: 12.5), `PostEphemeralOp` (Many-Argument Workhorses, Impact: 11.3), `PreApply` (Many-Argument Workhorses, Impact: 8.4)

### 3. `internal/command/views/hook_ui.go` (GO) -> Cumulative Risk: **711.67**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -1.67)
- **Magnitude:** 462.7 | **LOC:** 646 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.3996%), Tech Debt (98.6236%)
- **Heaviest Functions:** `PreApply` (Many-Argument Workhorses, Impact: 40.3), `PostApply` (Many-Argument Workhorses, Impact: 31.7), `stillRunning` (Compute Cores, Impact: 23.7)

### 4. `internal/plugin6/grpc_provider.go` (GO) -> Cumulative Risk: **685.96**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.01)
- **Magnitude:** 1498.78 | **LOC:** 2090 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 22.2%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (98.75%), Safety Score (92.1213%)
- **Heaviest Functions:** `ListResource` (Compute Cores, Impact: 46.2), `PlanResourceChange` (Compute Cores, Impact: 37.2), `ReadStateBytes` (Compute Cores, Impact: 34.5)

### 5. `internal/backend/local/backend_plan.go` (GO) -> Cumulative Risk: **672.69**
- **Archetype:** `file_cluster_4` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z +1.44)
- **Magnitude:** 173.06 | **LOC:** 289 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9984%), Safety Score (85.1621%)
- **Heaviest Functions:** `opPlan` (Many-Argument Workhorses, Impact: 68.9), `maybeWriteGeneratedConfig` (Compute Cores, Impact: 18.0)

### 6. `internal/plugin/grpc_provider.go` (GO) -> Cumulative Risk: **669.16**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.68)
- **Magnitude:** 1227.36 | **LOC:** 1677 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (98.6842%), Safety Score (94.116%)
- **Heaviest Functions:** `ListResource` (Compute Cores, Impact: 46.2), `PlanResourceChange` (Compute Cores, Impact: 37.2), `ApplyResourceChange` (Compute Cores, Impact: 33.4)

### 7. `internal/command/meta.go` (GO) -> Cumulative Risk: **667.84**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +1.06)
- **Magnitude:** 418.5 | **LOC:** 898 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9985%), Concurrency (99.1423%), Safety Score (81.4636%)
- **Heaviest Functions:** `RunOperation` (Compute Cores, Impact: 24.9), `showDiagnostics` (Compute Cores, Impact: 21.0), `MaybeGetSchemas` (Compute Cores, Impact: 17.5)

### 8. `internal/backend/local/backend.go` (GO) -> Cumulative Risk: **661.03**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.19)
- **Magnitude:** 312.2 | **LOC:** 522 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9965%), Concurrency (99.858%), Safety Score (84.02%)
- **Heaviest Functions:** `StatePaths` (Compute Cores, Impact: 17.3), `opWait` (Compute Cores, Impact: 16.6), `Operation` (Compute Cores, Impact: 15.0)

### 9. `internal/command/apply.go` (GO) -> Cumulative Risk: **659.12**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.91)
- **Magnitude:** 245.7 | **LOC:** 408 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 42.9%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Safety Score (87.8681%), Documentation (85.7143%)
- **Heaviest Functions:** `Run` (Compute Cores, Impact: 30.2), `OperationRequest` (Many-Argument Workhorses, Impact: 24.1), `helpApply` (I/O & Config Routines, Impact: 18.6)

### 10. `internal/command/ui_input.go` (GO) -> Cumulative Risk: **657.42**
- **Archetype:** `file_cluster_16` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z +2.52)
- **Magnitude:** 145.94 | **LOC:** 197 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Concurrency (99.9352%)
- **Heaviest Functions:** `Input` (Many-Argument Workhorses, Impact: 51.6), `init` (Callbacks & Closures, Impact: 2.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `internal/terraform/context_apply_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 5128.96 | **LOC:** 12905 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.5909%), Tech Debt (63.9102%)
**Top Internal Functions/Classes:**
  * `TestContext2Apply_scaleInCBD` **(Compute Cores)** (Impact: 63.8)
  * `TestContext2Apply_stop` **(Compute Cores)** (Impact: 40.0)
  * `TestContext2Apply_multiDepose_createBeforeDestroy` **(Compute Cores)** (Impact: 37.2)
  * `TestContext2Apply_taintedDestroyFailure` **(Compute Cores)** (Impact: 29.3)
  * `TestContext2Apply_ProviderMeta_refreshdata_set` **(Compute Cores)** (Impact: 28.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 7 instances
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 503 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 87
* *Memory Alloc (weighted view):* 26
* *State Mutation (weighted view):* 2133
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1062`, `structural_boundaries: 766`, `args: 216`, `func_start: 216`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 2`, `state_mutation: 1127`, `dead_code: 7`, `planned_debt: 1`, `fragile_debt: 4`, `unreferenced_by_name: 212`
* *Architecture:* `api: 269`, `concurrency: 17`, `import: 1`
* *Defense:* `safety: 24`, `doc: 208`, `test: 224`, `sync_locks: 83`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.213
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` Baz, Foo, Hello, __template_requires_new, a, a_ids, addr, amis...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/backend/remote-state/http/testdata/certs/ca.cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.213
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/backend/remote-state/http/testdata/certs/ca.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.213
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/backend/remote-state/http/testdata/certs/client.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.213
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/backend/remote-state/http/testdata/certs/client.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.213
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/backend/remote-state/http/testdata/certs/server.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.213
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/backend/remote-state/http/testdata/certs/server.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.213
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/pluginshared/testdata/archives/terraform-cloudplugin_0.1.0_SHA256SUMS.sig` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.273
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000416
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `internal/pluginshared/testdata/sample.private.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.213
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/pluginshared/testdata/sample.public.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.213
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/releaseauth/testdata/sample.private.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.213
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/releaseauth/testdata/sample.public.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.213
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/releaseauth/testdata/sample_release/sample_0.1.0_SHA256SUMS.sig` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.213
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/terraform/context_plan_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 2454.92 | **LOC:** 7164 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (12.6009%), Tech Debt (66.9312%)
**Top Internal Functions/Classes:**
  * `TestContext2Plan_countIncreaseFromOneCorrupted` **(Compute Cores)** (Impact: 28.4)
    * *Intent:* // https://github.com/PeoplePerHour/terraform/pull/11 // // This tests a case where both a "resource...
  * `TestContext2Plan_scaleInForEach` **(Compute Cores)** (Impact: 28.1)
    * *Intent:* // for_each can reference a resource with 0 instances
  * `TestContext2Plan_countDecreaseToOne` **(Compute Cores)** (Impact: 27.5)
  * `TestContext2Plan_createBeforeDestroy_depends_datasource` **(Compute Cores)** (Impact: 26.3)
  * `TestContext2Plan_countIncreaseWithSplatReference` **(Compute Cores)** (Impact: 26.2)
    * *Intent:* // A common pattern in TF configs is to have a set of resources with the same // count and to use co...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 88 instances
* *State Mutation (weighted view):* 466
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 839`, `structural_boundaries: 643`, `args: 133`, `func_start: 133`, `class_start: 1`
* *Risk/State:* `state_mutation: 290`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 131`
* *Architecture:* `api: 142`, `import: 1`
* *Defense:* `safety: 74`, `doc: 49`, `test: 138`, `sync_locks: 15`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.213
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` a, ami, another_var, attr, aws_computed_source, aws_computed_source.intermediates, aws_data_source, aws_instance...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/terraform/context_plan2_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 2303.82 | **LOC:** 7939 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 80.0%
- **Risk Profile:** Cognitive Load (11.7946%), Tech Debt (37.4099%)
**Top Internal Functions/Classes:**
  * `TestContext2Plan_dataSourcePreconditionPostcondition` **(Compute Cores)** (Impact: 73.3)
  * `TestContext2Plan_resourcePreconditionPostcondition` **(Compute Cores)** (Impact: 67.8)
  * `TestContext2Plan_dataResourceChecksManagedResourceChange` **(Compute Cores)** (Impact: 48.2)
  * `TestContext2Plan_refreshOnlyMode_orphan` **(Compute Cores)** (Impact: 45.2)
  * `TestContext2Plan_refreshOnlyMode_deposed` **(Compute Cores)** (Impact: 43.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 83 instances
* *State Mutation (weighted view):* 686
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 637`, `structural_boundaries: 510`, `args: 85`, `func_start: 85`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 520`, `dead_code: 4`, `fragile_debt: 3`, `unreferenced_by_name: 85`
* *Architecture:* `api: 85`, `import: 1`
* *Defense:* `safety: 19`, `doc: 107`, `test: 143`, `sync_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.213
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` main.tf, a, already_destroyed, arg, args, arn, attr, aws_instance...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/command/meta_backend.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2114.74 | **LOC:** 3408 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 73.1%
- **Risk Profile:** Cognitive Load (34.7467%), Tech Debt (46.7274%)
**Top Internal Functions/Classes:**
  * `backendFromConfig` **(Compute Cores)** (Impact: 174.7)
    * *Intent:* // backendFromConfig returns the initialized (not configured) backend // directly from the config/st...
  * `stateStore_C_s` **(Many-Argument Workhorses)** (Impact: 106.4)
    * *Intent:* // State Store Config Scenarios // The functions below cover handling all the various scenarios that...
  * `backend_C_r_s` **(Many-Argument Workhorses)** (Impact: 79.9)
    * *Intent:* // Configuring a backend for the first time.
  * `backend_C_r_S_changed` **(Many-Argument Workhorses)** (Impact: 72.4)
    * *Intent:* // Changing a previously saved backend.
  * `backend_to_stateStore` **(Many-Argument Workhorses)** (Impact: 70.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 8 instances
* *Amplified Cascading Flux:* 295 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 891
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 533`, `structural_boundaries: 317`, `args: 35`, `func_start: 35`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 10`, `state_mutation: 301`, `dead_code: 8`, `planned_debt: 3`, `fragile_debt: 21`, `unreferenced_by_name: 5`
* *Architecture:* `api: 14`, `import: 1`
* *Defense:* `safety: 110`, `doc: 259`, `sync_locks: 10`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.213
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` bytes, context, json, errors, fmt, go-version, v2, hcldec...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/terraform/node_resource_abstract_instance.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 2018.62 | **LOC:** 3129 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 78.6%
- **Risk Profile:** Cognitive Load (33.1288%), Tech Debt (92.1848%)
**Top Internal Functions/Classes:**
  * `plan` **(Many-Argument Workhorses)** (Impact: 217.2)
  * `apply` **(Many-Argument Workhorses)** (Impact: 175.2)
    * *Intent:* // apply accepts an applyConfig, instead of using n.Config, so destroy plans can // send a nil confi...
  * `applyProvisioners` **(Many-Argument Workhorses)** (Impact: 89.3)
    * *Intent:* // applyProvisioners executes the provisioners for a resource.
  * `refresh` **(Many-Argument Workhorses)** (Impact: 82.6)
    * *Intent:* // refresh does a refresh for a resource // if the second return value is non-nil, the refresh is de...
  * `processIgnoreChangesIndividual` **(Many-Argument Workhorses)** (Impact: 71.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 231 instances
* *State Mutation (weighted view):* 729
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 463`, `structural_boundaries: 252`, `args: 45`, `func_start: 45`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 11`, `state_mutation: 267`, `dead_code: 15`, `planned_debt: 2`, `fragile_debt: 34`, `unreferenced_by_name: 17`
* *Architecture:* `api: 15`, `import: 1`
* *Defense:* `safety: 15`, `doc: 208`, `test: 6`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.213
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` fmt, v2, terraform-registry-address, addrs, checks, configs, configschema, instances...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/terraform/context_validate_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1744.84 | **LOC:** 5411 | **CtrlFlow:** 4.6% | **Authorship Centralization:** 86.7%
- **Risk Profile:** Cognitive Load (17.7368%), Tech Debt (34.8763%)
**Top Internal Functions/Classes:**
  * `TestContext2Validate_providerContributedFunctions` **(Compute Cores)** (Impact: 66.0)
  * `TestContext2Validate_deprecatedAttr` **(Compute Cores)** (Impact: 54.5)
  * `TestContext2Validate_queryList` **(Compute Cores)** (Impact: 37.2)
  * `TestContext2Validate_action` **(Compute Cores)** (Impact: 29.9)
    * *Intent:* // Action Validation is largely exercised in context_plan_actions_test.go
  * `TestContext2Validate_varSensitive` **(Compute Cores)** (Impact: 15.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 151 instances
* *State Mutation (weighted view):* 869
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 223`, `structural_boundaries: 439`, `args: 90`, `func_start: 90`
* *Risk/State:* `state_mutation: 567`, `dead_code: 2`, `unreferenced_by_name: 90`
* *Architecture:* `api: 90`, `import: 1`
* *Defense:* `doc: 60`, `test: 106`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.213
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` a, ami, attr, aws_data_source, aws_instance, aws_register, bar, bar_instance...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/command/test_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1735.96 | **LOC:** 6087 | **CtrlFlow:** 9.0% | **Authorship Centralization:** 37.5%
- **Risk Profile:** Cognitive Load (12.6815%), Tech Debt (20.3992%)
**Top Internal Functions/Classes:**
  * `TestTest_Runs` **(Compute Cores)** (Impact: 69.3)
  * `TestTest_ParallelTeardown` **(Compute Cores)** (Impact: 57.8)
  * `TestTest_Parallel_Divided_Order` **(Compute Cores)** (Impact: 39.2)
  * `TestTest_SkipCleanup_FileLevelFlag` **(Compute Cores)** (Impact: 27.5)
  * `TestTest_UseOfBackends_whenStateArtifactsAreMade` **(Compute Cores)** (Impact: 27.2)
    * *Intent:* // Testing whether a state artifact is made for a run block with a backend or not // // Artifacts ar...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 128 instances
* *Concurrency (weighted view):* 48
* *State Mutation (weighted view):* 550
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 439`, `structural_boundaries: 293`, `args: 59`, `func_start: 59`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 294`, `dead_code: 2`, `unreferenced_by_name: 55`
* *Architecture:* `io: 4`, `api: 57`, `concurrency: 8`, `import: 1`
* *Defense:* `safety: 18`, `doc: 115`, `test: 178`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.213
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` TF_VAR_input, a1, a2, apply_test_resource, auto_tfvars_in_test_dir, b1, b2, bytes...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/cloud/tfe_client_mock.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1686.64 | **LOC:** 2603 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (54.264%), Tech Debt (90.7718%)
**Top Internal Functions/Classes:**
  * `ReadWithOptions` **(Many-Argument Workhorses)** (Impact: 49.3)
  * `List` **(Many-Argument Workhorses)** (Impact: 46.3)
  * `Create` **(Many-Argument Workhorses)** (Impact: 36.1)
  * `Logs` **(Many-Argument Workhorses)** (Impact: 31.6)
  * `Create` **(Many-Argument Workhorses)** (Impact: 26.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Rce:* 2 instances
* *Amplified Cascading Flux:* 159 instances
* *High Risk Execution (weighted view):* 59
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 512
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 269`, `structural_boundaries: 412`, `args: 178`, `func_start: 178`, `class_start: 21`
* *Risk/State:* `high_risk_execution: 60`, `state_mutation: 194`, `dead_code: 2`, `planned_debt: 47`, `unreferenced_by_name: 43`
* *Architecture:* `io: 14`, `api: 196`, `import: 1`
* *Defense:* `safety: 26`, `doc: 22`, `test: 32`, `sync_locks: 38`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.213
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` adv-fail, apply.log, bytes, context, cost-estimate.log, base64, errors, fmt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/terraform/context_apply2_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1661.16 | **LOC:** 4956 | **CtrlFlow:** 6.6% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (19.8645%), Tech Debt (39.2571%)
**Top Internal Functions/Classes:**
  * `TestContext2Apply_resourceConditionApplyTimeFail` **(Compute Cores)** (Impact: 45.9)
  * `TestContext2Apply_deprecatedOutputsAndVariables` **(Compute Cores)** (Impact: 32.8)
  * `TestContext2Apply_resourcePostcondition` **(Compute Cores)** (Impact: 32.3)
  * `TestContext2Apply_outputValuePrecondition` **(Compute Cores)** (Impact: 28.2)
  * `TestApply_updateDependencies` **(Compute Cores)** (Impact: 22.6)
    * *Intent:* // verify that dependencies are updated in the state during refresh and apply
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 161 instances
* *State Mutation (weighted view):* 817
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 276`, `structural_boundaries: 326`, `args: 56`, `func_start: 56`
* *Risk/State:* `state_mutation: 495`, `dead_code: 5`, `fragile_debt: 1`, `unreferenced_by_name: 56`
* *Architecture:* `api: 56`, `import: 1`
* *Defense:* `safety: 6`, `doc: 65`, `test: 65`, `sync_locks: 3`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.213
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` main.tf, main.tf, main.tf, a, applying, aws_instance, b, boop...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/command/init_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1614.92 | **LOC:** 6300 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 63.2%
- **Risk Profile:** Cognitive Load (5.3053%), Tech Debt (42.5093%)
**Top Internal Functions/Classes:**
  * `TestInit_stateStore_configChanges` **(Compute Cores)** (Impact: 78.2)
    * *Intent:* // Testing init's behaviors with `state_store` when run in a working directory where the configurati...
  * `TestInit_stateStore_newWorkingDir` **(Compute Cores)** (Impact: 65.4)
    * *Intent:* // Testing init's behaviors with `state_store` when run in an empty working directory
  * `TestInit_backendCloudInvalidOptions` **(Compute Cores)** (Impact: 48.4)
  * `TestInit_backend_to_stateStore_multipleWorkspaces` **(Compute Cores)** (Impact: 45.0)
  * `TestInit_backend_to_stateStore_singleWorkspace` **(Compute Cores)** (Impact: 35.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 10 instances
* *Amplified Cascading Flux:* 92 instances
* *Memory Alloc (weighted view):* 69
* *State Mutation (weighted view):* 307
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 488`, `structural_boundaries: 270`, `args: 81`, `func_start: 81`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 123`, `dead_code: 4`, `planned_debt: 4`, `fragile_debt: 1`, `unreferenced_by_name: 71`
* *Architecture:* `io: 11`, `api: 79`, `concurrency: 2`, `import: 1`
* *Defense:* `safety: 93`, `doc: 275`, `test: 141`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.213
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` -force-copy, -migrate-state, -plugin-dir, -reconfigure, -upgrade, hosted_state, test, current-state-version...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/plugin6/grpc_provider.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1498.78 | **LOC:** 2090 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 22.2%
- **Risk Profile:** Cognitive Load (47.6549%), Tech Debt (88.4422%)
**Top Internal Functions/Classes:**
  * `ListResource` **(Compute Cores)** (Impact: 46.2)
  * `PlanResourceChange` **(Compute Cores)** (Impact: 37.2)
  * `ReadStateBytes` **(Compute Cores)** (Impact: 34.5)
  * `ApplyResourceChange` **(Compute Cores)** (Impact: 33.4)
  * `GetProviderSchema` **(I/O & Config Routines)** (Impact: 30.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 284 instances
* *Concurrency (weighted view):* 18
* *Memory Alloc (weighted view):* 13
* *State Mutation (weighted view):* 863
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 279`, `structural_boundaries: 303`, `args: 42`, `func_start: 42`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 295`, `dead_code: 3`, `planned_debt: 2`, `fragile_debt: 10`, `unreferenced_by_name: 33`
* *Architecture:* `io: 6`, `api: 44`, `concurrency: 3`, `import: 1`
* *Defense:* `safety: 92`, `doc: 51`, `test: 3`, `sync_locks: 5`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.213
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` bytes, config, context, data, display_name, errors, fmt, go-plugin...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/legacy/helper/schema/schema.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1256.46 | **LOC:** 1780 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.2129%), Tech Debt (13.977%)
**Top Internal Functions/Classes:**
  * `internalValidate` **(Compute Cores)** (Impact: 136.2)
  * `diffList` **(Many-Argument Workhorses)** (Impact: 82.0)
  * `diffSet` **(Many-Argument Workhorses)** (Impact: 79.8)
  * `Diff` **(Many-Argument Workhorses)** (Impact: 78.2)
    * *Intent:* // Diff returns the diff for a resource given the schema map, // state, and configuration.
  * `diffMap` **(Many-Argument Workhorses)** (Impact: 61.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 93 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 281
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 377`, `structural_boundaries: 295`, `args: 32`, `func_start: 32`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 95`, `dead_code: 4`, `planned_debt: 3`, `fragile_debt: 1`, `unreferenced_by_name: 9`
* *Architecture:* `api: 47`, `import: 1`
* *Defense:* `safety: 28`, `doc: 166`, `sync_locks: 6`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.213
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` 0, 1, false, fmt, hcl2shim, terraform, copystructure, mapstructure...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/plans/planfile/tfplan.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1230.42 | **LOC:** 1470 | **CtrlFlow:** 28.5% | **Authorship Centralization:** 55.6%
- **Risk Profile:** Cognitive Load (51.4911%), Tech Debt (37.566%)
**Top Internal Functions/Classes:**
  * `readTfplan` **(Compute Cores)** (Impact: 79.1)
    * *Intent:* // --------------------------------------------------------------------------- // This file deals wi...
  * `writeTfplan` **(Many-Argument Workhorses)** (Impact: 71.5)
    * *Intent:* // writeTfplan serializes the given plan into the protobuf-based format used // for the "tfplan" por...
  * `resourceChangeFromTfplan` **(Compute Cores)** (Impact: 60.4)
  * `changeFromTfplan` **(Compute Cores)** (Impact: 55.6)
  * `CheckResultsFromPlanProto` **(Compute Cores)** (Impact: 47.5)
    * *Intent:* // CheckResultsFromPlanProto decodes a slice of check results from their protobuf // representation ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 193 instances
* *State Mutation (weighted view):* 582
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 338`, `structural_boundaries: 224`, `args: 32`, `func_start: 32`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 196`, `dead_code: 1`, `fragile_debt: 5`, `unreferenced_by_name: 8`
* *Architecture:* `io: 2`, `api: 12`, `import: 1`
* *Defense:* `safety: 62`, `doc: 38`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.239
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000416
  * `Imports (Out-Degree: 3):` fmt, addrs, checks, collections, configs, lang, globalref, plans...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `internal/deprecation/deprecation.go` -> Churn: **84.13%** | Cog Load: 8.5616% | Debt: 92.7444%
- `internal/command/meta_backend_errors.go` -> Churn: **63.09%** | Cog Load: 5.5715% | Debt: 51.8374%
- `internal/terraform/node_resource_abstract_instance.go` -> Churn: **61.66%** | Cog Load: 33.1288% | Debt: 92.1848%
- `internal/terraform/evaluate.go` -> Churn: **61.29%** | Cog Load: 34.1946% | Debt: 82.4591%
- `internal/terraform/eval_for_each.go` -> Churn: **58.32%** | Cog Load: 23.3866% | Debt: 60.6751%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `internal/terraform/context_validate_test.go` -> **Daniel Schmidt** (86.7% isolated ownership) | Magnitude: 1744.84
- `internal/cloud/tfe_client_mock.go` -> **Liam Cervante** (100.0% isolated ownership) | Magnitude: 1686.64
- `internal/backend/remote-state/s3/backend_test.go` -> **Kevin Vu** (100.0% isolated ownership) | Magnitude: 1006.8
- `internal/cloud/backend.go` -> **Daniel Banck** (100.0% isolated ownership) | Magnitude: 915.36
- `internal/cloud/backend_apply_test.go` -> **Daniel Schmidt** (100.0% isolated ownership) | Magnitude: 907.4

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `internal/command/fmt.go` -> **Severity: 0.048** (Bridge: 0.0005 * Flux: 99.9846%)
- `internal/backend/remote-state/oci/log.go` -> **Severity: 0.021** (Bridge: 0.0003 * Flux: 68.9974%)
- `internal/terraform/context.go` -> **Severity: 0.016** (Bridge: 0.0002 * Flux: 84.804%)
- `internal/dag/dag.go` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 99.9515%)
- `internal/e2e/e2e.go` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 99.8589%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `internal/command/fmt.go` -> **Severity: 28.087** (Embedded: 0.3542 * Error Risk: 79.2969%)
- `internal/backend/remote-state/oci/log.go` -> **Severity: 15.106** (Embedded: 0.2445 * Error Risk: 61.7748%)
- `internal/tfdiags/hcl.go` -> **Severity: 13.55** (Embedded: 0.1958 * Error Risk: 69.207%)
- `internal/states/sync.go` -> **Severity: 11.037** (Embedded: 0.1843 * Error Risk: 59.8688%)
- `internal/terraform/context.go` -> **Severity: 9.564** (Embedded: 0.1324 * Error Risk: 72.2483%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `internal/command/fmt.go` -> **Severity: 8353.11** (Blast Radius: 96.382 * Doc Risk: 86.6667%)
- `internal/backend/remote-state/oci/log.go` -> **Severity: 5714.76** (Blast Radius: 95.246 * Doc Risk: 60.0%)
- `internal/tfdiags/hcl.go` -> **Severity: 4394.844** (Blast Radius: 55.668 * Doc Risk: 78.9474%)
- `internal/collections/cmp.go` -> **Severity: 2024.3** (Blast Radius: 20.243 * Doc Risk: 100.0%)
- `internal/terraform/context.go` -> **Severity: 1350.636** (Blast Radius: 25.512 * Doc Risk: 52.9412%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
