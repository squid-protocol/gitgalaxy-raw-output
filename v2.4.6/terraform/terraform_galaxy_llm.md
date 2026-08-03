# ARCHITECTURAL_BRIEF: terraform
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/terraform` |
| **Timestamp** | `2026-08-03T21:40:05.557564+00:00` |
| **Scan Duration** | `7.15s` |
| **Git Branch** | `main` |
| **Git Commit** | `73c225dff4f1dc2a2464ffffe6f590e1d5692c05` |
| **Git Remote** | `https://github.com/hashicorp/terraform` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1188 malicious artifacts.

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
| Total Artifacts | 5161 |
| Analyzed Artifacts (Scanned) | 1644 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3517 |
| Total LOC | 135708 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 31.9% |
| Dominant Lang | GO |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.44 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3262 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.5604 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 25 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| GO | 1157 | 111453 | 70.4% |
| JSON | 322 | 22770 | 19.6% |
| PLAINTEXT | 101 | 12 | 6.1% |
| MARKDOWN | 26 | 0 | 1.6% |
| SHELL | 18 | 530 | 1.1% |
| PROTO | 11 | 897 | 0.7% |
| XML | 6 | 0 | 0.4% |
| DOCKERFILE | 1 | 10 | 0.1% |
| MAKEFILE | 1 | 23 | 0.1% |
| YAML | 1 | 13 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.928`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 1134 | 69.0% |
| file_cluster_13 | 223 | 13.6% |
| file_cluster_0 | 48 | 2.9% |
| file_cluster_4 | 30 | 1.8% |
| file_cluster_15 | 21 | 1.3% |
| file_cluster_11 | 20 | 1.2% |
| Unknown | 12 | 0.7% |
| file_cluster_9 | 10 | 0.6% |
| file_cluster_6 | 10 | 0.6% |
| file_cluster_7 | 8 | 0.5% |
| file_cluster_16 | 6 | 0.4% |
| file_cluster_12 | 5 | 0.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 115 | 7.0% |
| Static: Minified & Vendor Opaque Mass | 2 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3517*

**Composition by Extension & Reason:**
- `.tf`: 1325x Excluded (Unsupported Extension: '.tf'), 321x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.go`: 693x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded (Machine-Generated Source Code Signature: 30 LOC), 3x Excluded (Machine-Generated Source Code Signature: 27 LOC)
- `.hcl`: 401x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 91x Excluded (Unsupported Extension: '.hcl')
- `no_extension`: 147x Unsupported Format (.undeterminable), 44x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Unresolved Ambiguity (Tier 4 Fallback failed Ecosystem Consensus)
- `.tfstate`: 128x Excluded (Unsupported Extension: '.tfstate'), 60x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 81x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 1547 LOC), 1x Excluded (Static Asset Blob without Intent: 1548 LOC)
- `.md`: 22x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 17x Excluded (Explicitly Denied Extension: '.png')
- `.yml`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.log`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Saturation: Line 2 exceeds 500 chars), 2x Excluded (Saturation: Line 20 exceeds 500 chars)
- `.tfvars`: 10x Excluded (Unsupported Extension: '.tfvars'), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.zip`: 12x Excluded (Explicitly Denied Extension: '.zip')
- `.mod`: 11x Unsupported Format (.mod)
- `.sum`: 11x Excluded (Unsupported Extension: '.sum')
- `.tmpl`: 6x Excluded (Unsupported Extension: '.tmpl'), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 21.7 | 22.5 | 0.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 53.9 | 70.7 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 33.6 | 9.1 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 21.4 | 2.4 | 80.0 |
| API Exposure | 0.0 | 18.0 | 3.3 | 2.2 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 2.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 62.4 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 85.0 | 2.0 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 90.2 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 10.7 | 1.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 6.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 40.2 | 17.9 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 2.9 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 2.0 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 2.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `.github/scripts/equivalence-test.sh` (Hits: 56)
- `scripts/changelog.sh` (Hits: 48)
- `scripts/build.sh` (Hits: 16)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **fmt.go** (`internal/command/fmt.go`) — 593 inbound connections
2. **log.go** (`internal/backend/remote-state/oci/log.go`) — 193 inbound connections
3. **context.go** (`internal/terraform/context.go`) — 193 inbound connections
4. **json.go** (`internal/command/jsonformat/computed/renderers/json.go`) — 115 inbound connections
5. **sync.go** (`internal/states/sync.go`) — 81 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **functions.go** (`internal/lang/functions.go`) — 129 outbound dependencies
2. **descriptions.go** (`internal/lang/funcs/descriptions.go`) — 123 outbound dependencies
3. **backend.go** (`internal/backend/remote-state/s3/backend.go`) — 89 outbound dependencies
4. **testing.go** (`internal/cloud/testing.go`) — 70 outbound dependencies
5. **backend.go** (`internal/backend/remote-state/oss/backend.go`) — 59 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `initBackend` (@ `internal/command/init.go`) -> Impact: **905.8** | LOC: 627
- `waitForRun` (@ `internal/cloud/backend_common.go`) -> Impact: **808.8** | LOC: 619
- `selectWorkspace` (@ `internal/command/meta_backend.go`) -> Impact: **499.3** | LOC: 482
- `providerMetas` (@ `internal/terraform/node_resource_abstract_instance.go`) -> Impact: **496.3** | LOC: 617
- `resourceChangeToTfplan` (@ `internal/plans/planfile/tfplan.go`) -> Impact: **461.3** | LOC: 426
- `diff` (@ `internal/legacy/helper/schema/schema.go`) -> Impact: **340.1** | LOC: 238
- `decodeResourceBlock` (@ `internal/configs/resource.go`) -> Impact: **303.5** | LOC: 550
- `coerceValue` (@ `internal/configs/configschema/coerce_value.go`) -> Impact: **291.9** | LOC: 226
- `PackageMeta` (@ `internal/getproviders/registry_client.go`) -> Impact: **273.4** | LOC: 281
- `plan` (@ `internal/backend/remote/backend_plan.go`) -> Impact: **257.9** | LOC: 239

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `LocalRun` (@ `internal/backend/remote/backend_context.go`) -> **O(2^N) [Recursive]**
  * *Intent:* // Context implements backendrun.Local.
- `provider` (@ `internal/provider-simple-v6/provider.go`) -> **O(2^N) [Recursive]**
  * *Intent:* // provider returns an instance of simple
- `Provider` (@ `internal/provider-simple/provider.go`) -> **O(2^N) [Recursive]**
- `ApplyPlan` (@ `internal/stacks/stackruntime/internal/stackeval/main_apply.go`) -> **O(2^N) [Recursive]**
  * *Intent:* // ApplyPlan internally instantiates a [Main] configured to apply the given // raw plan, and then visits all of the relevant objects to collect up any...
- `Less` (@ `internal/addrs/action.go`) -> **O(2^N) [Recursive]**
- `Less` (@ `internal/addrs/action.go`) -> **O(2^N) [Recursive]**
- `Less` (@ `internal/addrs/action.go`) -> **O(2^N) [Recursive]**
  * *Intent:* // Less returns true if the receiver should sort before the given other value // in a sorted list of addresses.
- `Equal` (@ `internal/addrs/action.go`) -> **O(2^N) [Recursive]**
- `Equal` (@ `internal/addrs/action.go`) -> **O(2^N) [Recursive]**
- `Equal` (@ `internal/addrs/action.go`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `usage_[Truncated]` (@ `scripts/changelog.sh`) -> DB Complexity: **189**
- `usage_[Truncated]` (@ `.github/scripts/equivalence-test.sh`) -> DB Complexity: **186**
- `decodeResourceBlock` (@ `internal/configs/resource.go`) -> DB Complexity: **160**
- `Configure` (@ `internal/backend/remote-state/s3/backend.go`) -> DB Complexity: **136**
  * *Intent:* // Configure uses the provided configuration to set configuration fields // within the backend. // // The given configuration is assumed to have alrea...
- `waitForRun` (@ `internal/cloud/backend_common.go`) -> DB Complexity: **113**
- `prePlanVerifyTargetedMoves` (@ `internal/terraform/context_plan.go`) -> DB Complexity: **112**
- `prepareStateV4` (@ `internal/states/statefile/version4.go`) -> DB Complexity: **110**
- `initBackend` (@ `internal/command/init.go`) -> DB Complexity: **103**
- `providerMetas` (@ `internal/terraform/node_resource_abstract_instance.go`) -> DB Complexity: **101**
- `selectWorkspace` (@ `internal/command/meta_backend.go`) -> DB Complexity: **97**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `internal/backend/remote-state/http/testdata/certs` | 6 | 30000.0 | 0.0% | 0.0% |
| `internal/terraform` | 145 | 17787.94 | 27.19% | 56.91% |
| `internal/command` | 66 | 12038.72 | 31.26% | 37.33% |
| `internal/pluginshared/testdata` | 3 | 10000.0 | 0.0% | 0.0% |
| `internal/releaseauth/testdata` | 3 | 10000.0 | 0.0% | 0.0% |
| `internal/configs` | 36 | 7646.04 | 21.75% | 30.76% |
| `internal/stacks/stackruntime/internal/stackeval` | 51 | 6234.64 | 31.75% | 54.15% |
| `internal/pluginshared/testdata/archives` | 1 | 5000.0 | 0.0% | 0.0% |
| `internal/releaseauth/testdata/sample_release` | 1 | 5000.0 | 0.0% | 0.0% |
| `internal/cloud` | 21 | 4915.38 | 36.37% | 32.25% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `internal/builtin/provisioners/remote-exec/testdata/script1.sh` -> **100.0%** Exposure
- `scripts/changelog-links.sh` -> **100.0%** Exposure
- `scripts/copyright.sh` -> **100.0%** Exposure
- `scripts/debug-terraform` -> **100.0%** Exposure
- `scripts/exhaustive.sh` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `.github/scripts/equivalence-test.sh` -> **100.0%** Exposure
- `.github/scripts/get_product_version.sh` -> **100.0%** Exposure
- `scripts/build.sh` -> **100.0%** Exposure
- `scripts/changelog.sh` -> **100.0%** Exposure
- `scripts/copyright.sh` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `internal/addrs/action.go` -> **0** Orphaned Functions | **37** Duplicates
- `internal/configs/configload/loader_snapshot.go` -> **20** Orphaned Functions | **15** Duplicates
- `internal/command/views/json/hook.go` -> **0** Orphaned Functions | **28** Duplicates
- `internal/terraform/hook_stop.go` -> **28** Orphaned Functions | **0** Duplicates
- `internal/addrs/module_call.go` -> **1** Orphaned Functions | **24** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`internal/backend/local/backend_apply.go`** -> AI Confidence: **99.48%**
2. **`internal/backend/testing.go`** -> AI Confidence: **99.48%**
3. **`internal/command/arguments/extended.go`** -> AI Confidence: **99.48%**
4. **`internal/command/console_interactive.go`** -> AI Confidence: **99.48%**
5. **`internal/command/format/diagnostic.go`** -> AI Confidence: **99.48%**
6. **`internal/command/jsonformat/computed/renderers/block.go`** -> AI Confidence: **99.48%**
7. **`internal/configs/provider_requirements.go`** -> AI Confidence: **99.48%**
8. **`internal/refactoring/move_validate.go`** -> AI Confidence: **99.48%**
9. **`internal/refactoring/testing_helpers.go`** -> AI Confidence: **99.48%**
10. **`internal/stacks/stackplan/from_plan.go`** -> AI Confidence: **99.48%**
11. **`internal/terraform/context_input.go`** -> AI Confidence: **99.48%**
12. **`internal/terraform/transform_diff.go`** -> AI Confidence: **99.48%**
13. **`internal/backend/remote-state/oci/backend.go`** -> AI Confidence: **99.39%**
14. **`internal/backend/remote/backend_common.go`** -> AI Confidence: **99.39%**
15. **`internal/backend/remote/backend_plan.go`** -> AI Confidence: **99.39%**
16. **`internal/cloud/backend_apply.go`** -> AI Confidence: **99.39%**
17. **`internal/cloud/backend_common.go`** -> AI Confidence: **99.39%**
18. **`internal/command/init.go`** -> AI Confidence: **99.39%**
19. **`internal/command/jsonformat/renderer.go`** -> AI Confidence: **99.39%**
20. **`internal/command/jsonformat/state.go`** -> AI Confidence: **99.39%**
21. **`internal/command/state_mv.go`** -> AI Confidence: **99.39%**
22. **`internal/command/views/json/diagnostic.go`** -> AI Confidence: **99.39%**
23. **`internal/communicator/ssh/provisioner.go`** -> AI Confidence: **99.39%**
24. **`internal/configs/named_values.go`** -> AI Confidence: **99.39%**
25. **`internal/configs/provisioner.go`** -> AI Confidence: **99.39%**
26. **`internal/configs/removed.go`** -> AI Confidence: **99.39%**
27. **`internal/configs/resource.go`** -> AI Confidence: **99.39%**
28. **`internal/plans/deferring/deferred.go`** -> AI Confidence: **99.39%**
29. **`internal/plugin6/convert/schema.go`** -> AI Confidence: **99.39%**
30. **`internal/providercache/installer.go`** -> AI Confidence: **99.39%**
31. **`internal/stacks/stackconfig/provider_requirements.go`** -> AI Confidence: **99.39%**
32. **`internal/stacks/stackmigrate/components.go`** -> AI Confidence: **99.39%**
33. **`internal/stacks/stackstate/from_state.go`** -> AI Confidence: **99.39%**
34. **`internal/states/state_string.go`** -> AI Confidence: **99.39%**
35. **`internal/states/statefile/version2_upgrade.go`** -> AI Confidence: **99.39%**
36. **`internal/terraform/context_plan.go`** -> AI Confidence: **99.39%**
37. **`internal/terraform/context_walk.go`** -> AI Confidence: **99.39%**
38. **`internal/terraform/eval_variable.go`** -> AI Confidence: **99.39%**
39. **`internal/terraform/transform_config.go`** -> AI Confidence: **99.39%**
40. **`internal/configs/mock_provider.go`** -> AI Confidence: **99.35%**
41. **`internal/command/jsonformat/diff.go`** -> AI Confidence: **99.34%**
42. **`internal/configs/provider_validation.go`** -> AI Confidence: **99.34%**
43. **`internal/plans/objchange/compatible.go`** -> AI Confidence: **99.34%**
44. **`internal/stacks/stackconfig/removed.go`** -> AI Confidence: **99.34%**
45. **`internal/stacks/stackplan/component.go`** -> AI Confidence: **99.34%**
46. **`internal/stacks/stackruntime/internal/stackeval/walk_dynamic.go`** -> AI Confidence: **99.34%**
47. **`internal/terraform/transform_action_trigger_config.go`** -> AI Confidence: **99.34%**
48. **`internal/command/fmt.go`** -> AI Confidence: **99.32%**
49. **`internal/configs/configschema/marks.go`** -> AI Confidence: **99.32%**
50. **`internal/plans/objchange/plan_valid.go`** -> AI Confidence: **99.32%**
51. **`internal/addrs/module_instance.go`** -> AI Confidence: **99.31%**
52. **`internal/addrs/parse_ref.go`** -> AI Confidence: **99.31%**
53. **`internal/addrs/parse_target.go`** -> AI Confidence: **99.31%**
54. **`internal/backend/backendrun/unparsed_value.go`** -> AI Confidence: **99.31%**
55. **`internal/backend/local/backend.go`** -> AI Confidence: **99.31%**
56. **`internal/backend/local/backend_local.go`** -> AI Confidence: **99.31%**
57. **`internal/backend/local/backend_plan.go`** -> AI Confidence: **99.31%**
58. **`internal/backend/local/hook_state.go`** -> AI Confidence: **99.31%**
59. **`internal/backend/remote-state/azure/api_client.go`** -> AI Confidence: **99.31%**
60. **`internal/backend/remote-state/azure/backend.go`** -> AI Confidence: **99.31%**
61. **`internal/backend/remote-state/azure/backend_state.go`** -> AI Confidence: **99.31%**
62. **`internal/backend/remote-state/azure/client.go`** -> AI Confidence: **99.31%**
63. **`internal/backend/remote-state/azure/storage_client_helpers.go`** -> AI Confidence: **99.31%**
64. **`internal/backend/remote-state/consul/backend.go`** -> AI Confidence: **99.31%**
65. **`internal/backend/remote-state/cos/backend.go`** -> AI Confidence: **99.31%**
66. **`internal/backend/remote-state/cos/backend_state.go`** -> AI Confidence: **99.31%**
67. **`internal/backend/remote-state/cos/transport.go`** -> AI Confidence: **99.31%**
68. **`internal/backend/remote-state/http/backend.go`** -> AI Confidence: **99.31%**
69. **`internal/backend/remote-state/http/client.go`** -> AI Confidence: **99.31%**
70. **`internal/backend/remote-state/http/test_backend.go`** -> AI Confidence: **99.31%**
71. **`internal/backend/remote-state/kubernetes/backend.go`** -> AI Confidence: **99.31%**
72. **`internal/backend/remote-state/kubernetes/backend_state.go`** -> AI Confidence: **99.31%**
73. **`internal/backend/remote-state/oci/auth.go`** -> AI Confidence: **99.31%**
74. **`internal/backend/remote-state/oci/backend_state.go`** -> AI Confidence: **99.31%**
75. **`internal/backend/remote-state/oci/client.go`** -> AI Confidence: **99.31%**
76. **`internal/backend/remote-state/oci/multipart_upload.go`** -> AI Confidence: **99.31%**
77. **`internal/backend/remote-state/oci/util.go`** -> AI Confidence: **99.31%**
78. **`internal/backend/remote-state/oss/backend.go`** -> AI Confidence: **99.31%**
79. **`internal/backend/remote-state/oss/backend_state.go`** -> AI Confidence: **99.31%**
80. **`internal/backend/remote-state/pg/client.go`** -> AI Confidence: **99.31%**
81. **`internal/backend/remote-state/s3/backend.go`** -> AI Confidence: **99.31%**
82. **`internal/backend/remote-state/s3/validate.go`** -> AI Confidence: **99.31%**
83. **`internal/backend/remote/backend.go`** -> AI Confidence: **99.31%**
84. **`internal/backend/remote/backend_apply.go`** -> AI Confidence: **99.31%**
85. **`internal/backend/remote/backend_context.go`** -> AI Confidence: **99.31%**
86. **`internal/builtin/providers/terraform/data_source_state.go`** -> AI Confidence: **99.31%**
87. **`internal/builtin/providers/terraform/functions.go`** -> AI Confidence: **99.31%**
88. **`internal/builtin/providers/terraform/resource_data.go`** -> AI Confidence: **99.31%**
89. **`internal/builtin/provisioners/local-exec/resource_provisioner.go`** -> AI Confidence: **99.31%**
90. **`internal/builtin/provisioners/remote-exec/resource_provisioner.go`** -> AI Confidence: **99.31%**
91. **`internal/cloud/backend.go`** -> AI Confidence: **99.31%**
92. **`internal/cloud/backend_context.go`** -> AI Confidence: **99.31%**
93. **`internal/cloud/backend_plan.go`** -> AI Confidence: **99.31%**
94. **`internal/cloud/backend_query.go`** -> AI Confidence: **99.31%**
95. **`internal/cloud/backend_taskStage_policyEvaluation.go`** -> AI Confidence: **99.31%**
96. **`internal/command/apply.go`** -> AI Confidence: **99.31%**
97. **`internal/command/arguments/vars.go`** -> AI Confidence: **99.31%**
98. **`internal/command/cliconfig/credentials.go`** -> AI Confidence: **99.31%**
99. **`internal/command/cliconfig/provider_installation.go`** -> AI Confidence: **99.31%**
100. **`internal/command/graph.go`** -> AI Confidence: **99.31%**
101. **`internal/command/import.go`** -> AI Confidence: **99.31%**
102. **`internal/command/init_run.go`** -> AI Confidence: **99.31%**
103. **`internal/command/jsonconfig/expression.go`** -> AI Confidence: **99.31%**
104. **`internal/command/jsonformat/computed/renderers/primitive.go`** -> AI Confidence: **99.31%**
105. **`internal/command/jsonformat/differ/attribute.go`** -> AI Confidence: **99.31%**
106. **`internal/command/jsonformat/differ/set.go`** -> AI Confidence: **99.31%**
107. **`internal/command/jsonformat/plan.go`** -> AI Confidence: **99.31%**
108. **`internal/command/jsonplan/action_invocations.go`** -> AI Confidence: **99.31%**
109. **`internal/command/jsonplan/plan.go`** -> AI Confidence: **99.31%**
110. **`internal/command/jsonstate/state.go`** -> AI Confidence: **99.31%**
111. **`internal/command/junit/junit.go`** -> AI Confidence: **99.31%**
112. **`internal/command/login.go`** -> AI Confidence: **99.31%**
113. **`internal/command/meta.go`** -> AI Confidence: **99.31%**
114. **`internal/command/meta_backend.go`** -> AI Confidence: **99.31%**
115. **`internal/command/meta_backend_migrate.go`** -> AI Confidence: **99.31%**
116. **`internal/command/meta_providers.go`** -> AI Confidence: **99.31%**
117. **`internal/command/plan.go`** -> AI Confidence: **99.31%**
118. **`internal/command/providers.go`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `internal/command/apply.go` -> **100.0%** Exposure
- `internal/command/console.go` -> **100.0%** Exposure
- `internal/command/fmt.go` -> **100.0%** Exposure
- `internal/command/get.go` -> **100.0%** Exposure
- `internal/command/graph.go` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `.github/scripts/e2e_test_linux_darwin.sh` -> **100.0%** Exposure
- `internal/backend/remote-state/http/testdata/gencerts.sh` -> **100.0%** Exposure
- `internal/backend/remote-state/pg/backend_state.go` -> **100.0%** Exposure
- `internal/cloudplugin/cloudplugin1/grpc_client.go` -> **100.0%** Exposure
- `internal/pluginshared/interface.go` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `.github/scripts/equivalence-test.sh` -> **100.0%** Exposure
- `scripts/build.sh` -> **100.0%** Exposure
- `scripts/changelog.sh` -> **100.0%** Exposure
- `internal/backend/local/backend_apply.go` -> **100.0%** Exposure
- `internal/backend/remote-state/cos/backend.go` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `29` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `8234` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `internal/command/test_cleanup.go` (GO) -> Cumulative Risk: **886.11**
- **Archetype:** `file_cluster_4` (Distance: 12.971 IQR)
- **Magnitude:** 164.56 | **LOC:** 146 | **CtrlFlow:** 45.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `Run` (Impact: 31.6), `Help` (Impact: 16.7), `Synopsis` (Impact: 2.4)

### 2. `internal/command/plan.go` (GO) -> Cumulative Risk: **798.98**
- **Archetype:** `file_cluster_8` (Distance: 12.703 IQR)
- **Magnitude:** 321.44 | **LOC:** 281 | **CtrlFlow:** 61.4% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `OperationRequest` (Impact: 163.0), `Run` (Impact: 34.2), `PrepareBackend` (Impact: 4.2)

### 3. `internal/command/state_pull.go` (GO) -> Cumulative Risk: **782.91**
- **Archetype:** `file_cluster_8` (Distance: 12.215 IQR)
- **Magnitude:** 123.7 | **LOC:** 128 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `Help` (Impact: 34.9), `Run` (Impact: 30.5), `Synopsis` (Impact: 2.4)

### 4. `internal/command/state_rm.go` (GO) -> Cumulative Risk: **779.38**
- **Archetype:** `file_cluster_8` (Distance: 12.393 IQR)
- **Magnitude:** 260.72 | **LOC:** 232 | **CtrlFlow:** 59.3% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `Run` (Impact: 73.3), `Help` (Impact: 57.4), `Synopsis` (Impact: 2.4)

### 5. `internal/terraform/node_action_trigger_instance_apply.go` (GO) -> Cumulative Risk: **771.28**
- **Archetype:** `file_cluster_8` (Distance: 12.436 IQR)
- **Magnitude:** 273.26 | **LOC:** 265 | **CtrlFlow:** 51.6% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `Execute` (Impact: 60.1), `AddSubjectToDiagnostics` (Impact: 8.4), `References` (Impact: 7.6)

### 6. `internal/command/refresh.go` (GO) -> Cumulative Risk: **771.0**
- **Archetype:** `file_cluster_8` (Distance: 12.888 IQR)
- **Magnitude:** 159.28 | **LOC:** 214 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `OperationRequest` (Impact: 46.4), `Run` (Impact: 21.6), `PrepareBackend` (Impact: 4.2)

### 7. `internal/command/state_list.go` (GO) -> Cumulative Risk: **764.44**
- **Archetype:** `file_cluster_8` (Distance: 11.484 IQR)
- **Magnitude:** 120.76 | **LOC:** 139 | **CtrlFlow:** 54.8% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `Run` (Impact: 42.5), `Help` (Impact: 21.8), `Synopsis` (Impact: 2.4)

### 8. `internal/command/state_show.go` (GO) -> Cumulative Risk: **763.98**
- **Archetype:** `file_cluster_8` (Distance: 12.459 IQR)
- **Magnitude:** 171.62 | **LOC:** 201 | **CtrlFlow:** 45.0% | **Authorship Centralization:** 60.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `Run` (Impact: 46.1), `Help` (Impact: 21.1), `Synopsis` (Impact: 2.4)

### 9. `internal/command/state_replace_provider.go` (GO) -> Cumulative Risk: **754.36**
- **Archetype:** `file_cluster_8` (Distance: 12.67 IQR)
- **Magnitude:** 288.24 | **LOC:** 246 | **CtrlFlow:** 61.9% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `Run` (Impact: 89.8), `Help` (Impact: 64.3), `Synopsis` (Impact: 2.4)

### 10. `internal/terraform/node_action_trigger_instance_plan.go` (GO) -> Cumulative Risk: **754.15**
- **Archetype:** `file_cluster_8` (Distance: 12.569 IQR)
- **Magnitude:** 281.76 | **LOC:** 307 | **CtrlFlow:** 55.6% | **Authorship Centralization:** 73.7%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `Execute` (Impact: 35.8), `evaluateActionCondition` (Impact: 33.2), `containsBeforeEvent` (Impact: 14.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `internal/backend/remote-state/http/testdata/certs/ca.cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/backend/remote-state/http/testdata/certs/ca.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/backend/remote-state/http/testdata/certs/client.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/backend/remote-state/http/testdata/certs/client.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/backend/remote-state/http/testdata/certs/server.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/backend/remote-state/http/testdata/certs/server.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/pluginshared/testdata/archives/terraform-cloudplugin_0.1.0_SHA256SUMS.sig` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/pluginshared/testdata/sample.private.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/pluginshared/testdata/sample.public.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/releaseauth/testdata/sample.private.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/releaseauth/testdata/sample.public.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/releaseauth/testdata/sample_release/sample_0.1.0_SHA256SUMS.sig` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/grpcwrap/provider6.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.259 IQR)
- **Top Global Matches:** file_cluster_8: 14.259, file_cluster_0: 14.512, file_cluster_13: 14.528
- **Magnitude:** 1863.16 | **LOC:** 1322 | **CtrlFlow:** 53.0% | **Authorship Centralization:** 36.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (59.6441%), Tech Debt (14.0178%)
**Top Internal Functions/Classes:**
  * `PlanResourceChange` (Impact: 66.7 | O(2^N) | DB: 25)
  * `WriteStateBytes` (Impact: 66.7 | O(2^N) | DB: 10)
  * `ApplyResourceChange` (Impact: 59.5 | O(2^N) | DB: 22)
  * `ListResource` (Impact: 58.7 | O(2^N) | DB: 12)
  * `ImportResourceState` (Impact: 54.9 | O(2^N) | DB: 17)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 177`, `structural_boundaries: 157`, `args: 39`, `func_start: 39`, `class_start: 1`
* *Risk/State:* `state_mutation: 853`, `planned_debt: 1`, `fragile_debt: 1`, `orphaned_logic: 3`
* *Architecture:* `api: 213`, `import: 1`
* *Defense:* `safety: 88`, `doc: 10`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` bytes, codes, context, msgpack, tfplugin6, status, cty, timestamppb...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/plugin6/grpc_provider.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.377 IQR)
- **Top Global Matches:** file_cluster_8: 14.377, file_cluster_0: 14.528, file_cluster_13: 14.533
- **Magnitude:** 1783.24 | **LOC:** 2090 | **CtrlFlow:** 49.5% | **Authorship Centralization:** 21.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 29
- **Risk Profile:** Cognitive Load (45.8993%), Tech Debt (55.1568%)
**Top Internal Functions/Classes:**
  * `ListResource` (Impact: 169.1 | O(2^N) | DB: 29)
  * `ReadResource` (Impact: 82.6 | O(2^N) | DB: 26)
  * `GetProviderSchema` (Impact: 76.0 | O(2^N) | DB: 24)
  * `InvokeAction` (Impact: 72.1 | O(2^N) | DB: 13)
  * `ReadDataSource` (Impact: 42.0 | O(2^N) | DB: 18)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 164`, `structural_boundaries: 167`, `args: 27`, `func_start: 27`, `class_start: 2`
* *Risk/State:* `state_mutation: 818`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 8`, `orphaned_logic: 4`
* *Architecture:* `io: 4`, `api: 101`, `concurrency: 6`, `import: 1`
* *Defense:* `safety: 56`, `doc: 31`, `test: 3`, `sync_locks: 3`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` go-plugin, codes, config, fmt, bytes, grpc, data, addrs...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/backend/remote-state/s3/backend.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.196 IQR)
- **Top Global Matches:** file_cluster_8: 13.196, file_cluster_7: 13.504, file_cluster_13: 13.616
- **Magnitude:** 1601.74 | **LOC:** 1629 | **CtrlFlow:** 61.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 136
- **Risk Profile:** Cognitive Load (82.1559%), Tech Debt (77.1813%)
**Top Internal Functions/Classes:**
  * `Configure` (Impact: 189.1 | O(N^1) | DB: 136)
    * *Intent:* // Configure uses the provided configuration to set configuration fields // within the backend. // /...
  * `PrepareConfig` (Impact: 87.7 | O(N^1) | DB: 52)
    * *Intent:* // PrepareConfig checks the validity of the values in the given // configuration, and inserts any mi...
  * `ConfigSchema` (Impact: 52.2 | O(N^1))
    * *Intent:* // ConfigSchema returns a description of the expected configuration // structure for the receiving b...
  * `validateNestedAttribute` (Impact: 31.3 | O(N^1) | DB: 10)
  * `pathString` (Impact: 27.6 | O(N^1) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 205`, `structural_boundaries: 126`, `args: 46`, `func_start: 46`, `class_start: 14`
* *Risk/State:* `state_mutation: 708`, `planned_debt: 1`, `duplicate_logic: 14`
* *Architecture:* `api: 279`, `import: 1`
* *Defense:* `safety: 9`, `doc: 10`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` external_id, use_lockfile, workspace_key_prefix, time, ec2_metadata_service_endpoint, http_proxy, duration, access_key...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/plugin/grpc_provider.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.289 IQR)
- **Top Global Matches:** file_cluster_8: 14.289, file_cluster_0: 14.431, file_cluster_13: 14.44
- **Magnitude:** 1505.82 | **LOC:** 1677 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 22.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 26
- **Risk Profile:** Cognitive Load (46.8422%), Tech Debt (36.6815%)
**Top Internal Functions/Classes:**
  * `ListResource` (Impact: 92.6 | O(2^N) | DB: 20)
  * `ReadResource` (Impact: 82.6 | O(2^N) | DB: 26)
  * `GetProviderSchema` (Impact: 75.9 | O(2^N) | DB: 23)
  * `ReadDataSource` (Impact: 42.0 | O(2^N) | DB: 18)
  * `OpenEphemeralResource` (Impact: 36.9 | O(2^N) | DB: 16)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 133`, `structural_boundaries: 152`, `args: 24`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `state_mutation: 729`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 5`, `orphaned_logic: 2`
* *Architecture:* `io: 4`, `api: 85`, `concurrency: 6`, `import: 1`
* *Defense:* `safety: 49`, `doc: 25`, `test: 1`, `sync_locks: 3`, `immutability_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` go-plugin, codes, config, fmt, grpc, data, addrs, sync...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/grpcwrap/provider.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.125 IQR)
- **Top Global Matches:** file_cluster_8: 14.125, file_cluster_0: 14.378, file_cluster_13: 14.398
- **Magnitude:** 1442.26 | **LOC:** 993 | **CtrlFlow:** 53.5% | **Authorship Centralization:** 60.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (64.4843%), Tech Debt (8.0228%)
**Top Internal Functions/Classes:**
  * `PlanResourceChange` (Impact: 66.8 | O(2^N) | DB: 25)
  * `ApplyResourceChange` (Impact: 59.5 | O(2^N) | DB: 22)
  * `ListResource` (Impact: 58.7 | O(2^N) | DB: 12)
  * `ImportResourceState` (Impact: 54.9 | O(2^N) | DB: 17)
  * `ReadResource` (Impact: 51.8 | O(2^N) | DB: 19)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 145`, `structural_boundaries: 126`, `args: 31`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `state_mutation: 680`, `planned_debt: 1`
* *Architecture:* `api: 155`, `import: 1`
* *Defense:* `safety: 71`, `doc: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` codes, context, msgpack, status, cty, function, convert, tfplugin5...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/terraform/node_resource_abstract_instance.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.392 IQR)
- **Top Global Matches:** file_cluster_8: 14.392, file_cluster_15: 14.4, file_cluster_7: 14.425
- **Magnitude:** 1356.28 | **LOC:** 3129 | **CtrlFlow:** 66.0% | **Authorship Centralization:** 68.8%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 101
- **Risk Profile:** Cognitive Load (46.5468%), Tech Debt (95.9376%)
**Top Internal Functions/Classes:**
  * `providerMetas` (Impact: 496.3 | O(2^N) | DB: 101)
  * `readDiff` (Impact: 83.0 | O(N^1) | DB: 36)
    * *Intent:* // GraphNodeOverridable
  * `processIgnoreChanges` (Impact: 25.4 | O(2^N) | DB: 3)
    * *Intent:* // planForget returns a Forget change.
  * `traversalToPath` (Impact: 21.6 | O(N^1) | DB: 6)
  * `AttachResourceState` (Impact: 15.1 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 214`, `structural_boundaries: 110`, `args: 28`, `func_start: 28`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 557`, `dead_code: 9`, `fragile_debt: 19`, `orphaned_logic: 6`
* *Architecture:* `api: 87`, `import: 1`
* *Defense:* `safety: 9`, `doc: 109`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` instances, ephemeral, format, fmt, provisioners, addrs, cty, deferring...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/command/init.go` (GO | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.713 IQR)
- **Top Global Matches:** file_cluster_8: 13.713, file_cluster_7: 13.825, file_cluster_15: 13.857
- **Magnitude:** 1353.9 | **LOC:** 1211 | **CtrlFlow:** 72.5% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 103
- **Risk Profile:** Cognitive Load (34.725%), Tech Debt (9.6694%)
**Top Internal Functions/Classes:**
  * `initBackend` (Impact: 905.8 | O(N^6) | DB: 103)
  * `getModules` (Impact: 34.4 | O(N^1) | DB: 10)
  * `Run` (Impact: 8.7 | O(N^1) | DB: 8)
  * `initCloud` (Impact: 8.7 | O(N^1) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 44`, `args: 10`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 349`, `dead_code: 2`, `fragile_debt: 1`
* *Architecture:* `api: 36`, `import: 1`
* *Defense:* `safety: 8`, `doc: 47`, `immutability_locks: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` views, local, fmt, -lock-timeout, -upgrade, attribute, depsfile, version...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/plans/planfile/tfplan.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.169 IQR)
- **Top Global Matches:** file_cluster_8: 14.169, file_cluster_7: 14.397, file_cluster_13: 14.403
- **Magnitude:** 1308.04 | **LOC:** 1470 | **CtrlFlow:** 65.4% | **Authorship Centralization:** 38.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 95
- **Risk Profile:** Cognitive Load (63.0316%), Tech Debt (29.5345%)
**Top Internal Functions/Classes:**
  * `resourceChangeToTfplan` (Impact: 461.3 | O(2^N) | DB: 95)
  * `resourceChangeFromTfplan` (Impact: 60.0 | O(N^1) | DB: 28)
  * `valueFromTfplan` (Impact: 18.1 | O(N^1) | DB: 5)
  * `resourceAttrFromTfplan` (Impact: 9.0 | O(N^1) | DB: 4)
  * `resourceAttrToTfplan` (Impact: 4.5 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 236`, `structural_boundaries: 125`, `args: 22`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 678`, `fragile_debt: 3`, `orphaned_logic: 4`
* *Architecture:* `api: 53`, `import: 1`
* *Defense:* `safety: 43`, `doc: 26`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` collections, globalref, version, addrs, lang, checks, planproto, cty...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/cloud/backend_common.go` (GO | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.92 IQR)
- **Top Global Matches:** file_cluster_4: 13.92, file_cluster_8: 13.979, file_cluster_13: 14.175
- **Magnitude:** 1207.68 | **LOC:** 776 | **CtrlFlow:** 72.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 113
- **Risk Profile:** Cognitive Load (45.9721%), Tech Debt (9.0219%)
**Top Internal Functions/Classes:**
  * `waitForRun` (Impact: 808.8 | O(N^2) | DB: 113)
  * `backoff` (Impact: 8.3 | O(2^N) | DB: 2)
    * *Intent:* // backoff will perform exponential backoff based on the iteration and // limited by the provided mi...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 196`, `structural_boundaries: 73`, `args: 11`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 329`, `dead_code: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 2`, `api: 9`, `concurrency: 42`, `import: 1`
* *Defense:* `safety: 37`, `doc: 31`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` jsonapi, filepath, yes, go-retryablehttp, override, fmt, time, bytes...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/command/meta_backend.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.724 IQR)
- **Top Global Matches:** file_cluster_8: 14.724, file_cluster_13: 14.751, file_cluster_0: 14.768
- **Magnitude:** 1096.58 | **LOC:** 3408 | **CtrlFlow:** 64.4% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 97
- **Risk Profile:** Cognitive Load (35.9474%), Tech Debt (96.8057%)
**Top Internal Functions/Classes:**
  * `selectWorkspace` (Impact: 499.3 | O(2^N) | DB: 97)
  * `backendFromState` (Impact: 56.3 | O(N^1) | DB: 26)
  * `determineStateStoreInitReason` (Impact: 28.9 | O(N^1) | DB: 9)
  * `determineInitReason` (Impact: 27.5 | O(N^1) | DB: 9)
  * `Backend` (Impact: 5.4 | O(N^1) | DB: 1)
    * *Intent:* // Backend initializes and returns the operations backend for this CLI session. // // The backend is...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 143`, `structural_boundaries: 79`, `args: 7`, `func_start: 7`, `class_start: 2`
* *Risk/State:* `state_mutation: 431`, `dead_code: 5`, `planned_debt: 1`, `fragile_debt: 15`, `orphaned_logic: 1`
* *Architecture:* `api: 36`, `import: 1`
* *Defense:* `safety: 22`, `doc: 66`, `sync_locks: 2`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` filepath, workdir, views, go-version, reattach, fmt, strconv, bytes...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/configs/resource.go` (GO | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.848 IQR)
- **Top Global Matches:** file_cluster_8: 13.848, file_cluster_7: 13.952, file_cluster_13: 14.039
- **Magnitude:** 935.16 | **LOC:** 993 | **CtrlFlow:** 73.6% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 160
- **Risk Profile:** Cognitive Load (23.8618%), Tech Debt (8.3441%)
**Top Internal Functions/Classes:**
  * `decodeResourceBlock` (Impact: 303.5 | O(N^2) | DB: 160)
  * `HasCustomConditions` (Impact: 4.6 | O(N^1))
    * *Intent:* // If no specific "provider" argument is given, we want to look up the
  * `moduleUniqueKey` (Impact: 2.4 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 33`, `args: 6`, `func_start: 6`, `class_start: 4`
* *Risk/State:* `state_mutation: 462`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 153`, `import: 1`
* *Defense:* `doc: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` postcondition, provisioner, addrs, precondition, _, langrefs, lifecycle, hclsyntax...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/legacy/helper/schema/schema.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.756 IQR)
- **Top Global Matches:** file_cluster_8: 13.756, file_cluster_11: 13.816, file_cluster_13: 13.826
- **Magnitude:** 882.2 | **LOC:** 1780 | **CtrlFlow:** 60.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 54
- **Risk Profile:** Cognitive Load (50.9747%), Tech Debt (6.5608%)
**Top Internal Functions/Classes:**
  * `diff` (Impact: 340.1 | O(2^N) | DB: 54)
  * `getValueType` (Impact: 108.4 | O(N^1) | DB: 34)
  * `isValidFieldName` (Impact: 2.2 | O(N^1) | DB: 1)
  * `validateList` (Impact: 2.1 | O(N^1))
  * `isProto5` (Impact: 2.0 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 223`, `structural_boundaries: 145`, `args: 12`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `state_mutation: 385`, `dead_code: 4`, `planned_debt: 3`, `orphaned_logic: 1`
* *Architecture:* `api: 27`, `import: 1`
* *Defense:* `safety: 14`, `doc: 78`, `sync_locks: 5`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` strings, reflect, regexp, false, 1, sync, mapstructure, 0...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/terraform/node_resource_validate.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.534 IQR)
- **Top Global Matches:** file_cluster_8: 13.534, file_cluster_7: 13.707, file_cluster_13: 13.768
- **Magnitude:** 862.5 | **LOC:** 925 | **CtrlFlow:** 65.6% | **Authorship Centralization:** 90.0%
- **Algorithmic:** O(N) | **DB Complexity:** 86
- **Risk Profile:** Cognitive Load (37.7612%), Tech Debt (10.1561%)
**Top Internal Functions/Classes:**
  * `validateResource` (Impact: 123.8 | O(N^1) | DB: 86)
  * `validateImportTargets` (Impact: 71.3 | O(N^1) | DB: 28)
    * *Intent:* // "self" can't point to an unknown key, but we'll force it to be // key 0 here, which should return...
  * `validateConfigGen` (Impact: 26.7 | O(N^1) | DB: 3)
  * `validateImportTargetExpansion` (Impact: 24.4 | O(N^1) | DB: 6)
  * `validateProvisioner` (Impact: 15.7 | O(N^1) | DB: 7)
    * *Intent:* // validateProvisioner validates the configuration of a provisioner belonging to // a resource. The ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 56`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 437`, `dead_code: 2`, `orphaned_logic: 2`
* *Architecture:* `api: 117`, `import: 1`
* *Defense:* `safety: 4`, `doc: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` instances, bastion_user, ephemeral, host_key, format, fmt, port, timeout...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `internal/lang/funcs/collection.go` (GO) | Magnitude: 345.0 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 358, state_mutation: 217, api: 95, branch: 87
- `internal/terraform/eval_import.go` (GO) | Magnitude: 212.84 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 134, state_mutation: 102, structural_boundaries: 37, encapsulation: 32
- `internal/command/jsonplan/module.go` (GO) | Magnitude: 16.12 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 4, structural_boundaries: 3, api: 3, decorators: 3
- `internal/getproviders/didyoumean.go` (GO) | Magnitude: 93.16 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 72, state_mutation: 30, branch: 22, structural_boundaries: 22
- `internal/communicator/ssh/provisioner.go` (GO) | Magnitude: 433.32 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 278, state_mutation: 208, encapsulation: 96, branch: 79

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `internal/stacks/stackruntime/internal/stackeval/provider_expressions.go` (GO) | Magnitude: 412.18 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 205, state_mutation: 192, encapsulation: 65, branch: 64
- `internal/terraform/transform_attach_schema.go` (GO) | Magnitude: 146.14 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 82, state_mutation: 54, branch: 29, encapsulation: 24
- `internal/namedvals/values.go` (GO) | Magnitude: 56.24 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 33, state_mutation: 21, encapsulation: 14, branch: 10
- `internal/stacks/stackruntime/internal/stackeval/walk_static.go` (GO) | Magnitude: 164.18 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 43, state_mutation: 33, branch: 22, encapsulation: 10
- `internal/legacy/terraform/diff.go` (GO) | Magnitude: 610.26 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 418, state_mutation: 310, branch: 160, structural_boundaries: 91

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `scripts/changelog.sh` (SHELL) | Magnitude: 15.29 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 124, state_mutation: 67, io: 48, safety_bypasses: 41
- `.github/scripts/get_product_version.sh` (SHELL) | Magnitude: 4.46 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 25, branch: 16, reflection_metaprogramming: 13, io: 11
- `scripts/build.sh` (SHELL) | Magnitude: 9.66 | Delta: **0.097 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 45, branch: 27, indent_spaces: 27, reflection_metaprogramming: 24
- `internal/copy/copy_value.go` (GO) | Magnitude: 35.72 | Delta: **0.097 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 22, indent_tabs: 20, encapsulation: 9, branch: 6
- `.github/scripts/e2e_test_linux_darwin.sh` (SHELL) | Magnitude: 1.42 | Delta: **0.507 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: reflection_metaprogramming: 13, indent_spaces: 8, branch: 7, safety_bypasses: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `internal/command/arguments/state_show.go` (GO) | Magnitude: 38.4 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 28, state_mutation: 24, encapsulation: 11, structural_boundaries: 5
- `internal/states/checks.go` (GO) | Magnitude: 190.28 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 94, state_mutation: 57, branch: 27, structural_boundaries: 21
- `internal/cloud/backend_show.go` (GO) | Magnitude: 66.64 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 33, state_mutation: 27, branch: 15, doc: 8
- `internal/lang/funcs/datetime.go` (GO) | Magnitude: 134.66 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 119, state_mutation: 45, branch: 30, api: 30
- `internal/stacks/stackruntime/hooks/resource_instance.go` (GO) | Magnitude: 101.22 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 65, api: 28, structural_boundaries: 27, branch: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `internal/addrs/module.go` (GO) | Magnitude: 165.34 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 58, state_mutation: 45, structural_boundaries: 21, branch: 18
- `internal/command/cliconfig/provider_installation.go` (GO) | Magnitude: 149.74 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 86, state_mutation: 59, encapsulation: 33, branch: 23
- `internal/addrs/provider_config.go` (GO) | Magnitude: 119.34 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 91, state_mutation: 42, api: 29, structural_boundaries: 28
- `internal/dag/seq.go` (GO) | Magnitude: 84.32 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 42, state_mutation: 21, branch: 18, structural_boundaries: 12
- `internal/dag/dot.go` (GO) | Magnitude: 201.46 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 99, state_mutation: 79, branch: 25, encapsulation: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `internal/command/workdir/config_state.go` (GO) | Magnitude: 18.32 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 9, indent_tabs: 7, doc: 4, class_start: 3
- `internal/command/views/init.go` (GO) | Magnitude: 83.32 | Delta: **0.061 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 36, state_mutation: 27, encapsulation: 19, structural_boundaries: 16
- `internal/states/statefile/upgrade_helper.go` (GO) | Magnitude: 21.4 | Delta: **0.12 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 13, structural_boundaries: 7, state_mutation: 6, encapsulation: 5
- `internal/stacks/stackruntime/internal/stackeval/hooks.go` (GO) | Magnitude: 41.58 | Delta: **0.249 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 42, doc: 31, api: 23, structural_boundaries: 13
- `internal/collections/cmp.go` (GO) | Magnitude: 21.74 | Delta: **0.278 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 12, state_mutation: 10, structural_boundaries: 8, encapsulation: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `internal/cloud/backend.go` (GO) | Magnitude: 654.1 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 473, state_mutation: 333, encapsulation: 140, branch: 122
- `internal/stacks/stackruntime/internal/stackeval/provider_instance.go` (GO) | Magnitude: 190.54 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 156, state_mutation: 69, encapsulation: 44, api: 31
- `internal/cloud/backend_common.go` (GO) | Magnitude: 1207.68 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 492, state_mutation: 329, branch: 196, encapsulation: 102
- `internal/command/views/hook_ui.go` (GO) | Magnitude: 332.96 | Delta: **0.067 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 191, state_mutation: 158, encapsulation: 81, branch: 42
- `internal/promising/task.go` (GO) | Magnitude: 93.86 | Delta: **0.08 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 71, state_mutation: 50, encapsulation: 33, structural_boundaries: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `internal/configs/variable_type_hint.go` (GO) | Magnitude: 22.12 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 8, api: 5, state_mutation: 4, immutability_locks: 4
- `internal/providers/doc.go` (GO) | Magnitude: 10.52 | Delta: **0.072 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 2, structural_boundaries: 1, planned_debt: 1
- `internal/provisioners/doc.go` (GO) | Magnitude: 10.52 | Delta: **0.085 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 3, structural_boundaries: 1, planned_debt: 1
- `internal/configs/configschema/doc.go` (GO) | Magnitude: 10.52 | Delta: **0.093 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 4, structural_boundaries: 1, planned_debt: 1
- `internal/states/statemgr/migrate.go` (GO) | Magnitude: 43.56 | Delta: **0.174 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 44, state_mutation: 24, doc: 19, structural_boundaries: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `internal/addrs/doc.go` (GO) | Magnitude: 10.52 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 5, structural_boundaries: 1
- `internal/replacefile/doc.go` (GO) | Magnitude: 10.52 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 5, structural_boundaries: 1
- `internal/stacks/stackstate/statekeys/doc.go` (GO) | Magnitude: 10.52 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 5, structural_boundaries: 1
- `internal/backend/pluggable/chunks/chunks.go` (GO) | Magnitude: 16.6 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 5, api: 2, state_mutation: 2, bitwise_ops: 2
- `internal/configs/doc.go` (GO) | Magnitude: 10.52 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 6, structural_boundaries: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `internal/tfdiags/consolidate_warnings.go` (GO) | Magnitude: 138.78 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: state_mutation: 58, indent_tabs: 58, encapsulation: 18, branch: 17
- `internal/plans/objchange/compatible.go` (GO) | Magnitude: 130.76 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 114, indent_tabs: 84, branch: 40, encapsulation: 20
- `internal/command/cliconfig/config_windows.go` (GO) | Magnitude: 32.46 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 21, state_mutation: 19, structural_boundaries: 8, encapsulation: 7
- `internal/lang/scope.go` (GO) | Magnitude: 17.16 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 21, doc: 18, api: 13, structural_boundaries: 6
- `internal/command/testdata/statelocker.go` (GO) | Magnitude: 0.04 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 26, state_mutation: 21, encapsulation: 7, branch: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `internal/states/statefile/version0.go` (GO) | Magnitude: 9.82 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 8, doc: 5, structural_boundaries: 4, state_mutation: 3
- `internal/states/statemgr/doc.go` (GO) | Magnitude: 10.52 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 5, structural_boundaries: 1, dead_code: 1
- `internal/rpcapi/dynrpcserver/doc.go` (GO) | Magnitude: 10.52 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 3, structural_boundaries: 1, dead_code: 1
- `internal/command/webbrowser/webbrowser.go` (GO) | Magnitude: 13.08 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 5, structural_boundaries: 3, class_start: 1, api: 1
- `internal/lang/ephemeral/doc.go` (GO) | Magnitude: 10.52 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 2, structural_boundaries: 1, dead_code: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `internal/command/meta_backend.go` -> Churn: **100.0%** | Cog Load: 35.9474% | Debt: 96.8057%
- `internal/deprecation/deprecation.go` -> Churn: **82.35%** | Cog Load: 32.018% | Debt: 90.9512%
- `internal/lang/marks/marks.go` -> Churn: **68.88%** | Cog Load: 44.2703% | Debt: 96.9302%
- `internal/terraform/node_action_trigger_instance_plan.go` -> Churn: **68.55%** | Cog Load: 38.7753% | Debt: 59.4032%
- `internal/command/meta.go` -> Churn: **65.54%** | Cog Load: 33.6678% | Debt: 95.6274%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `internal/backend/remote-state/s3/backend.go` -> **Kevin Vu** (100.0% isolated ownership) | Magnitude: 1601.74
- `internal/cloud/backend_common.go` -> **Daniel Banck** (100.0% isolated ownership) | Magnitude: 1207.68
- `internal/terraform/node_resource_validate.go` -> **Daniel Schmidt** (90.0% isolated ownership) | Magnitude: 862.5
- `internal/backend/remote/backend_common.go` -> **Daniel Banck** (100.0% isolated ownership) | Magnitude: 838.52
- `internal/backend/remote-state/oss/backend.go` -> **zeshan** (100.0% isolated ownership) | Magnitude: 834.5

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `internal/command/fmt.go` -> **Severity: 0.065** (Bridge: 0.0006 * Flux: 100.0%)
- `internal/backend/remote-state/oci/log.go` -> **Severity: 0.047** (Bridge: 0.0005 * Flux: 99.988%)
- `internal/terraform/context.go` -> **Severity: 0.014** (Bridge: 0.0002 * Flux: 85.0%)
- `internal/backend/pluggable/pluggable.go` -> **Severity: 0.004** (Bridge: 0.0 * Flux: 99.9863%)
- `internal/backend/remote-state/oci/auth.go` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 100.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `internal/backend/remote-state/oci/log.go` -> **Severity: 10876.58** (Blast Radius: 114.168 * Doc Risk: 95.2682%)
- `internal/tfdiags/hcl.go` -> **Severity: 6314.8** (Blast Radius: 63.148 * Doc Risk: 100.0%)
- `internal/command/jsonformat/computed/renderers/json.go` -> **Severity: 1455.686** (Blast Radius: 14.569 * Doc Risk: 99.9167%)
- `internal/command/fmt.go` -> **Severity: 1363.211** (Blast Radius: 109.963 * Doc Risk: 12.397%)
- `internal/states/sync.go` -> **Severity: 770.183** (Blast Radius: 64.611 * Doc Risk: 11.9203%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
