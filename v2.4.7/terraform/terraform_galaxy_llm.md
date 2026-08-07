# ARCHITECTURAL_BRIEF: terraform
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/terraform` |
| **Timestamp** | `2026-08-07T05:40:26.662023+00:00` |
| **Scan Duration** | `7.11s` |
| **Git Branch** | `main` |
| **Git Commit** | `73c225dff4f1dc2a2464ffffe6f590e1d5692c05` |
| **Git Remote** | `https://github.com/hashicorp/terraform` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1188 malicious artifacts.

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
> **Architectural Drift Z-Score:** `5.946`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 1137 | 69.2% |
| file_cluster_13 | 224 | 13.6% |
| file_cluster_0 | 48 | 2.9% |
| file_cluster_4 | 30 | 1.8% |
| file_cluster_11 | 20 | 1.2% |
| file_cluster_15 | 18 | 1.1% |
| Unknown | 12 | 0.7% |
| file_cluster_9 | 10 | 0.6% |
| file_cluster_6 | 10 | 0.6% |
| file_cluster_7 | 8 | 0.5% |
| file_cluster_12 | 5 | 0.3% |
| file_cluster_16 | 5 | 0.3% |

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
| Cognitive Load Exposure | 0.0 | 100.0 | 21.8 | 22.6 | 0.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 54.1 | 71.7 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 35.0 | 10.7 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 18.7 | 2.4 | 80.0 |
| API Exposure | 0.0 | 18.0 | 3.3 | 2.2 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 2.6 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 62.4 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 85.0 | 2.0 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 90.2 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 10.7 | 1.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 6.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 35.5 | 17.6 | 0.0 |
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

- `waitForRun` (@ `internal/cloud/backend_common.go`) -> Impact: **308.1** | LOC: 619
- `providerMetas` (@ `internal/terraform/node_resource_abstract_instance.go`) -> Impact: **263.6** | LOC: 617
- `selectWorkspace` (@ `internal/command/meta_backend.go`) -> Impact: **261.7** | LOC: 482
- `resourceChangeToTfplan` (@ `internal/plans/planfile/tfplan.go`) -> Impact: **241.3** | LOC: 426
- `BackendForLocalPlan` (@ `internal/command/meta_backend.go`) -> Impact: **231.8** | LOC: 422
- `prepareStateV4` (@ `internal/states/statefile/version4.go`) -> Impact: **226.8** | LOC: 456
- `GetModuleInstanceRepetitionData` (@ `internal/instances/expander.go`) -> Impact: **218.2** | LOC: 445
  * *Intent:* // ExpandModuleResource finds the exhaustive set of resource instances resulting from // the expansion of the given resource and all of its containing...
- `decodeResourceBlock` (@ `internal/configs/resource.go`) -> Impact: **211.5** | LOC: 550
- `GetResourceInstanceRepetitionData` (@ `internal/instances/expander.go`) -> Impact: **204.2** | LOC: 410
- `Configure` (@ `internal/backend/remote-state/s3/backend.go`) -> Impact: **189.1** | LOC: 352
  * *Intent:* // Configure uses the provided configuration to set configuration fields // within the backend. // // The given configuration is assumed to have alrea...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `internal/backend/remote-state/http/testdata/certs` | 6 | 30000.0 | 0.0% | 0.0% |
| `internal/terraform` | 145 | 17173.44 | 27.2% | 58.27% |
| `internal/command` | 66 | 10334.92 | 31.26% | 38.93% |
| `internal/pluginshared/testdata` | 3 | 10000.0 | 0.0% | 0.0% |
| `internal/releaseauth/testdata` | 3 | 10000.0 | 0.0% | 0.0% |
| `internal/configs` | 36 | 7486.94 | 21.96% | 30.82% |
| `internal/stacks/stackruntime/internal/stackeval` | 51 | 6263.54 | 33.83% | 61.95% |
| `internal/pluginshared/testdata/archives` | 1 | 5000.0 | 0.0% | 0.0% |
| `internal/releaseauth/testdata/sample_release` | 1 | 5000.0 | 0.0% | 0.0% |
| `internal/addrs` | 41 | 4475.14 | 20.07% | 64.31% |

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
- `internal/instances/expander.go` -> **30** Orphaned Functions | **0** Duplicates
- `internal/addrs/partial_expanded.go` -> **9** Orphaned Functions | **20** Duplicates
- `internal/command/views/json/hook.go` -> **0** Orphaned Functions | **28** Duplicates

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `29` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `8234` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `internal/command/views/hook_json.go` (GO) -> Cumulative Risk: **726.94**
- **Archetype:** `file_cluster_4` (Distance: 11.824 IQR)
- **Magnitude:** 246.84 | **LOC:** 297 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (98.3824%)
- **Heaviest Functions:** `applyingHeartbeat` (Impact: 12.9), `ephemeralOpHeartbeat` (Impact: 12.9), `PostApply` (Impact: 8.4)

### 2. `internal/plans/changes_src.go` (GO) -> Cumulative Risk: **674.59**
- **Archetype:** `file_cluster_8` (Distance: 13.594 IQR)
- **Magnitude:** 445.82 | **LOC:** 645 | **CtrlFlow:** 53.5% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.5676%)
- **Heaviest Functions:** `Decode` (Impact: 75.0), `Empty` (Impact: 25.8), `Decode` (Impact: 16.2)

### 3. `internal/terraform/node_action_trigger_instance_apply.go` (GO) -> Cumulative Risk: **671.28**
- **Archetype:** `file_cluster_8` (Distance: 12.433 IQR)
- **Magnitude:** 261.46 | **LOC:** 265 | **CtrlFlow:** 51.6% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (98.7639%)
- **Heaviest Functions:** `Execute` (Impact: 50.5), `AddSubjectToDiagnostics` (Impact: 8.4), `References` (Impact: 7.6)

### 4. `internal/terraform/node_module_variable.go` (GO) -> Cumulative Risk: **666.5**
- **Archetype:** `file_cluster_8` (Distance: 12.84 IQR)
- **Magnitude:** 173.9 | **LOC:** 401 | **CtrlFlow:** 35.0% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9997%)
- **Heaviest Functions:** `DynamicExpand` (Impact: 14.7), `Execute` (Impact: 10.0), `variableValidationRules` (Impact: 9.7)

### 5. `internal/backend/remote-state/oci/multipart_upload.go` (GO) -> Cumulative Risk: **664.22**
- **Archetype:** `file_cluster_4` (Distance: 12.939 IQR)
- **Magnitude:** 319.64 | **LOC:** 253 | **CtrlFlow:** 51.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9019%), Documentation (98.9362%)
- **Heaviest Functions:** `multiPartUploadImpl` (Impact: 57.1), `uploadPartsWorker` (Impact: 22.4), `objectMultiPartSplit` (Impact: 12.2)

### 6. `internal/builtin/provisioners/local-exec/resource_provisioner.go` (GO) -> Cumulative Risk: **663.53**
- **Archetype:** `file_cluster_4` (Distance: 13.084 IQR)
- **Magnitude:** 228.7 | **LOC:** 225 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9828%), Safety Score (96.9206%)
- **Heaviest Functions:** `ProvisionResource` (Impact: 56.5), `ValidateProvisionerConfig` (Impact: 5.4), `GetSchema` (Impact: 3.7)

### 7. `internal/terraform/node_local.go` (GO) -> Cumulative Risk: **656.81**
- **Archetype:** `file_cluster_8` (Distance: 12.72 IQR)
- **Magnitude:** 139.52 | **LOC:** 251 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9995%)
- **Heaviest Functions:** `evaluateLocalValue` (Impact: 15.1), `Execute` (Impact: 11.0), `DynamicExpand` (Impact: 5.9)

### 8. `internal/plans/action_invocation.go` (GO) -> Cumulative Risk: **655.74**
- **Archetype:** `file_cluster_8` (Distance: 12.433 IQR)
- **Magnitude:** 163.14 | **LOC:** 188 | **CtrlFlow:** 40.4% | **Authorship Centralization:** 70.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9989%)
- **Heaviest Functions:** `Less` (Impact: 20.3), `Encode` (Impact: 13.8), `Equals` (Impact: 12.8)

### 9. `internal/terraform/node_action_trigger_instance_plan.go` (GO) -> Cumulative Risk: **654.15**
- **Archetype:** `file_cluster_8` (Distance: 12.566 IQR)
- **Magnitude:** 276.36 | **LOC:** 307 | **CtrlFlow:** 55.6% | **Authorship Centralization:** 73.7%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (94.993%)
- **Heaviest Functions:** `evaluateActionCondition` (Impact: 33.2), `Execute` (Impact: 30.4), `containsBeforeEvent` (Impact: 14.6)

### 10. `internal/stacks/stackruntime/internal/stackeval/removed_component_config.go` (GO) -> Cumulative Risk: **653.85**
- **Archetype:** `file_cluster_8` (Distance: 13.4 IQR)
- **Magnitude:** 177.54 | **LOC:** 247 | **CtrlFlow:** 34.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (95.8261%), Tech Debt (95.5022%)
- **Heaviest Functions:** `CheckValid` (Impact: 19.8), `CheckModuleTree` (Impact: 17.1), `newRemovedComponentConfig` (Impact: 2.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `internal/backend/remote-state/http/testdata/certs/ca.cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `internal/backend/remote-state/s3/backend.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.192 IQR)
- **Top Global Matches:** file_cluster_8: 13.192, file_cluster_7: 13.5, file_cluster_13: 13.612
- **Magnitude:** 1594.94 | **LOC:** 1629 | **CtrlFlow:** 61.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (82.1559%), Tech Debt (77.1813%)
**Top Internal Functions/Classes:**
  * `Configure` (Impact: 189.1)
    * *Intent:* // Configure uses the provided configuration to set configuration fields // within the backend. // /...
  * `PrepareConfig` (Impact: 87.7)
    * *Intent:* // PrepareConfig checks the validity of the values in the given // configuration, and inserts any mi...
  * `ConfigSchema` (Impact: 52.2)
    * *Intent:* // ConfigSchema returns a description of the expected configuration // structure for the receiving b...
  * `validateNestedAttribute` (Impact: 31.3)
  * `pathString` (Impact: 27.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 205`, `structural_boundaries: 126`, `args: 46`, `func_start: 46`, `class_start: 14`
* *Risk/State:* `state_mutation: 708`, `planned_debt: 1`, `duplicate_logic: 14`
* *Architecture:* `api: 279`, `import: 1`
* *Defense:* `safety: 9`, `doc: 10`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` use_dualstack_endpoint, os, AWS_STS_ENDPOINT, access_key, skip_requesting_account_id, tfdiags, s3, retry_mode...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/terraform/node_resource_abstract_instance.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.367 IQR)
- **Top Global Matches:** file_cluster_8: 14.367, file_cluster_15: 14.377, file_cluster_7: 14.401
- **Magnitude:** 1488.18 | **LOC:** 3129 | **CtrlFlow:** 66.0% | **Authorship Centralization:** 73.3%
- **Risk Profile:** Cognitive Load (46.0286%), Tech Debt (97.0406%)
**Top Internal Functions/Classes:**
  * `providerMetas` (Impact: 263.6)
  * `planDataSource` (Impact: 158.6)
  * `applyProvisioners` (Impact: 79.5)
    * *Intent:* // In this case, we are always creating the resource so we don't
  * `readDiff` (Impact: 69.9)
    * *Intent:* // GraphNodeOverridable
  * `apply` (Impact: 57.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 214`, `structural_boundaries: 110`, `args: 28`, `func_start: 28`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 557`, `dead_code: 9`, `fragile_debt: 19`, `orphaned_logic: 8`
* *Architecture:* `api: 87`, `import: 1`
* *Defense:* `safety: 9`, `doc: 109`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` mocking, instances, providers, tfdiags, format, objchange, checks, marks...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/grpcwrap/provider6.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.227 IQR)
- **Top Global Matches:** file_cluster_8: 14.227, file_cluster_0: 14.484, file_cluster_13: 14.5
- **Magnitude:** 1471.16 | **LOC:** 1322 | **CtrlFlow:** 53.0% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (59.6441%), Tech Debt (14.0178%)
**Top Internal Functions/Classes:**
  * `WriteStateBytes` (Impact: 34.9)
  * `PlanResourceChange` (Impact: 29.8)
  * `GetProviderSchema` (Impact: 28.2)
  * `ApplyResourceChange` (Impact: 26.7)
  * `ListResource` (Impact: 25.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 177`, `structural_boundaries: 157`, `args: 39`, `func_start: 39`, `class_start: 1`
* *Risk/State:* `state_mutation: 853`, `planned_debt: 1`, `fragile_debt: 1`, `orphaned_logic: 3`
* *Architecture:* `api: 213`, `import: 1`
* *Defense:* `safety: 88`, `doc: 10`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` convert, io, tfplugin6, status, json, bytes, codes, chunks...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/plugin6/grpc_provider.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.367 IQR)
- **Top Global Matches:** file_cluster_8: 14.367, file_cluster_0: 14.518, file_cluster_13: 14.523
- **Magnitude:** 1396.54 | **LOC:** 2090 | **CtrlFlow:** 49.5% | **Authorship Centralization:** 23.1%
- **Risk Profile:** Cognitive Load (45.8993%), Tech Debt (55.1568%)
**Top Internal Functions/Classes:**
  * `ListResource` (Impact: 88.2)
  * `ReadResource` (Impact: 43.4)
  * `GetProviderSchema` (Impact: 40.2)
  * `InvokeAction` (Impact: 37.8)
  * `ReadDataSource` (Impact: 22.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 164`, `structural_boundaries: 167`, `args: 27`, `func_start: 27`, `class_start: 2`
* *Risk/State:* `state_mutation: 818`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 8`, `orphaned_logic: 4`
* *Architecture:* `io: 4`, `api: 101`, `concurrency: 6`, `import: 1`
* *Defense:* `safety: 56`, `doc: 31`, `test: 3`, `sync_locks: 3`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` convert, json, state, config, logging, errors, providers, codes...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/plans/planfile/tfplan.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.185 IQR)
- **Top Global Matches:** file_cluster_8: 14.185, file_cluster_7: 14.412, file_cluster_13: 14.417
- **Magnitude:** 1309.64 | **LOC:** 1470 | **CtrlFlow:** 65.4% | **Authorship Centralization:** 38.5%
- **Risk Profile:** Cognitive Load (62.7235%), Tech Debt (52.2364%)
**Top Internal Functions/Classes:**
  * `resourceChangeToTfplan` (Impact: 241.3)
  * `resourceChangeFromTfplan` (Impact: 60.0)
  * `changeToTfplan` (Impact: 41.4)
  * `CheckResultsFromPlanProto` (Impact: 38.5)
  * `actionInvocationToTfPlan` (Impact: 32.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 236`, `structural_boundaries: 125`, `args: 22`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 678`, `fragile_debt: 3`, `orphaned_logic: 9`
* *Architecture:* `api: 53`, `import: 1`
* *Defense:* `safety: 43`, `doc: 26`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` tfdiags, io, time, providers, lang, checks, addrs, fmt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/command/meta_backend.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.717 IQR)
- **Top Global Matches:** file_cluster_8: 14.717, file_cluster_13: 14.744, file_cluster_0: 14.761
- **Magnitude:** 1227.48 | **LOC:** 3408 | **CtrlFlow:** 64.4% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (35.9474%), Tech Debt (96.8057%)
**Top Internal Functions/Classes:**
  * `selectWorkspace` (Impact: 261.7)
  * `BackendForLocalPlan` (Impact: 231.8)
  * `stateStoreConfig` (Impact: 151.4)
  * `backendFromState` (Impact: 56.3)
  * `determineStateStoreInitReason` (Impact: 21.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 143`, `structural_boundaries: 79`, `args: 7`, `func_start: 7`, `class_start: 2`
* *Risk/State:* `state_mutation: 431`, `dead_code: 5`, `planned_debt: 1`, `fragile_debt: 15`, `orphaned_logic: 1`
* *Architecture:* `api: 36`, `import: 1`
* *Defense:* `safety: 22`, `doc: 66`, `sync_locks: 2`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` depsfile, os, reattach, clistate, json, terraform, version, errors...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/plugin/grpc_provider.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.28 IQR)
- **Top Global Matches:** file_cluster_8: 14.28, file_cluster_0: 14.422, file_cluster_13: 14.431
- **Magnitude:** 1198.22 | **LOC:** 1677 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (46.8422%), Tech Debt (36.6815%)
**Top Internal Functions/Classes:**
  * `ListResource` (Impact: 48.5)
  * `ReadResource` (Impact: 43.4)
  * `GetProviderSchema` (Impact: 40.1)
  * `ReadDataSource` (Impact: 22.4)
  * `OpenEphemeralResource` (Impact: 19.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 133`, `structural_boundaries: 152`, `args: 24`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `state_mutation: 729`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 5`, `orphaned_logic: 2`
* *Architecture:* `io: 4`, `api: 85`, `concurrency: 6`, `import: 1`
* *Defense:* `safety: 49`, `doc: 25`, `test: 1`, `sync_locks: 3`, `immutability_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` json, state, config, logging, errors, providers, codes, data...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/grpcwrap/provider.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.097 IQR)
- **Top Global Matches:** file_cluster_8: 14.097, file_cluster_0: 14.353, file_cluster_13: 14.372
- **Magnitude:** 1149.36 | **LOC:** 993 | **CtrlFlow:** 53.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (64.4843%), Tech Debt (8.0228%)
**Top Internal Functions/Classes:**
  * `PlanResourceChange` (Impact: 29.9)
  * `ApplyResourceChange` (Impact: 26.7)
  * `ListResource` (Impact: 25.9)
  * `GetSchema` (Impact: 25.0)
  * `ImportResourceState` (Impact: 24.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 145`, `structural_boundaries: 126`, `args: 31`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `state_mutation: 680`, `planned_debt: 1`
* *Architecture:* `api: 155`, `import: 1`
* *Defense:* `safety: 71`, `doc: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` tfplugin5, status, json, codes, fmt, function, context, msgpack...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/instances/expander.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_7` (Drift: 13.966 IQR)
- **Top Global Matches:** file_cluster_7: 13.966, file_cluster_8: 14.005, file_cluster_15: 14.028
- **Magnitude:** 1064.6 | **LOC:** 1103 | **CtrlFlow:** 51.8% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (45.9722%), Tech Debt (99.9995%)
**Top Internal Functions/Classes:**
  * `GetModuleInstanceRepetitionData` (Impact: 218.2)
    * *Intent:* // ExpandModuleResource finds the exhaustive set of resource instances resulting from // the expansi...
  * `GetResourceInstanceRepetitionData` (Impact: 204.2)
  * `moduleInstances` (Impact: 116.3)
  * `partialExpandedModuleInstances` (Impact: 17.3)
  * `knowsResourceInstance` (Impact: 15.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 79`, `args: 41`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `state_mutation: 279`, `dead_code: 2`, `fragile_debt: 7`, `orphaned_logic: 30`
* *Architecture:* `api: 28`, `import: 1`
* *Defense:* `doc: 81`, `sync_locks: 29`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` mocking, sync, addrs, fmt, sort, cty, slices
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/cloud/backend_common.go` (GO | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.89 IQR)
- **Top Global Matches:** file_cluster_4: 13.89, file_cluster_8: 13.948, file_cluster_7: 14.145
- **Magnitude:** 952.78 | **LOC:** 776 | **CtrlFlow:** 72.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (49.4054%), Tech Debt (23.5637%)
**Top Internal Functions/Classes:**
  * `waitForRun` (Impact: 308.1)
  * `checkPolicy` (Impact: 76.6)
  * `confirm` (Impact: 67.9)
  * `costEstimate` (Impact: 51.4)
  * `checkResponseCode` (Impact: 15.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 196`, `structural_boundaries: 73`, `args: 11`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 329`, `dead_code: 1`, `orphaned_logic: 7`
* *Architecture:* `io: 2`, `api: 9`, `concurrency: 42`, `import: 1`
* *Defense:* `safety: 37`, `doc: 31`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` math, time, override, os, url, json, logging, terraform...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/configs/resource.go` (GO | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.848 IQR)
- **Top Global Matches:** file_cluster_8: 13.848, file_cluster_7: 13.952, file_cluster_13: 14.039
- **Magnitude:** 903.66 | **LOC:** 993 | **CtrlFlow:** 73.6% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (31.4217%), Tech Debt (8.3441%)
**Top Internal Functions/Classes:**
  * `decodeResourceBlock` (Impact: 211.5)
  * `decodeReplaceTriggeredBy` (Impact: 50.8)
  * `String` (Impact: 7.2)
  * `HasCustomConditions` (Impact: 4.6)
    * *Intent:* // If no specific "provider" argument is given, we want to look up the
  * `Addr` (Impact: 2.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 33`, `args: 6`, `func_start: 6`, `class_start: 4`
* *Risk/State:* `state_mutation: 462`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 153`, `import: 1`
* *Defense:* `doc: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` tfdiags, precondition, connection, hclsyntax, addrs, fmt, _, v2...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/command/init.go` (GO | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.646 IQR)
- **Top Global Matches:** file_cluster_8: 13.646, file_cluster_7: 13.756, file_cluster_15: 13.787
- **Magnitude:** 881.4 | **LOC:** 1211 | **CtrlFlow:** 72.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (34.725%), Tech Debt (9.6694%)
**Top Internal Functions/Classes:**
  * `initBackend` (Impact: 175.6)
  * `prepareInstallerEvents` (Impact: 127.1)
    * *Intent:* // Collect the provider dependencies from the configuration.
  * `backendConfigOverrideBody` (Impact: 64.7)
    * *Intent:* // If the provider dependencies have changed since the last run then we'll // say a little about tha...
  * `Help` (Impact: 38.6)
    * *Intent:* // prepareInstallerEvents returns an instance of *providercache.InstallerEvents. This struct defines...
  * `getProvidersFromConfig` (Impact: 24.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 44`, `args: 10`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 349`, `dead_code: 2`, `fragile_debt: 1`
* *Architecture:* `api: 41`, `import: 1`
* *Defense:* `safety: 8`, `doc: 47`, `immutability_locks: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` depsfile, local, -from-module, -force-copy, -input, providercache, version, slices...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/terraform/node_resource_validate.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.509 IQR)
- **Top Global Matches:** file_cluster_8: 13.509, file_cluster_7: 13.683, file_cluster_13: 13.744
- **Magnitude:** 852.5 | **LOC:** 925 | **CtrlFlow:** 65.6% | **Authorship Centralization:** 90.0%
- **Risk Profile:** Cognitive Load (37.7612%), Tech Debt (10.1561%)
**Top Internal Functions/Classes:**
  * `validateResource` (Impact: 123.8)
  * `validateImportTargets` (Impact: 71.3)
    * *Intent:* // "self" can't point to an unknown key, but we'll force it to be // key 0 here, which should return...
  * `validateConfigGen` (Impact: 26.7)
  * `validateImportTargetExpansion` (Impact: 24.4)
  * `validateProvisioner` (Impact: 11.5)
    * *Intent:* // validateProvisioner validates the configuration of a provisioner belonging to // a resource. The ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 56`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 437`, `dead_code: 2`, `orphaned_logic: 2`
* *Architecture:* `api: 117`, `import: 1`
* *Defense:* `safety: 4`, `doc: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` proxy_scheme, bastion_private_key, insecure, port, proxy_port, instances, https, providers...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `internal/lang/funcs/collection.go` (GO) | Magnitude: 345.0 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 358, state_mutation: 217, api: 95, branch: 87
- `internal/terraform/eval_import.go` (GO) | Magnitude: 200.74 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 134, state_mutation: 102, structural_boundaries: 37, encapsulation: 32
- `internal/command/jsonplan/module.go` (GO) | Magnitude: 16.12 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 4, structural_boundaries: 3, api: 3, decorators: 3
- `internal/getproviders/didyoumean.go` (GO) | Magnitude: 115.96 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 72, state_mutation: 30, branch: 22, structural_boundaries: 22
- `internal/registry/response/module_list.go` (GO) | Magnitude: 15.6 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, api: 3, doc: 2, decorators: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `internal/namedvals/values.go` (GO) | Magnitude: 50.94 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 33, state_mutation: 21, encapsulation: 14, branch: 10
- `internal/terraform/transform_attach_schema.go` (GO) | Magnitude: 146.14 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 82, state_mutation: 54, branch: 29, encapsulation: 24
- `internal/stacks/stackruntime/internal/stackeval/provider_expressions.go` (GO) | Magnitude: 498.48 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 205, state_mutation: 192, encapsulation: 65, branch: 64
- `internal/stacks/stackruntime/internal/stackeval/walk_static.go` (GO) | Magnitude: 93.48 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 43, state_mutation: 33, branch: 22, encapsulation: 10
- `internal/legacy/terraform/diff.go` (GO) | Magnitude: 594.96 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 418, state_mutation: 310, branch: 160, structural_boundaries: 91

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `.github/scripts/get_product_version.sh` (SHELL) | Magnitude: 4.46 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 25, branch: 16, reflection_metaprogramming: 13, io: 11
- `scripts/changelog.sh` (SHELL) | Magnitude: 12.03 | Delta: **0.06 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 124, state_mutation: 67, io: 48, safety_bypasses: 41
- `scripts/build.sh` (SHELL) | Magnitude: 8.86 | Delta: **0.089 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 45, branch: 33, indent_spaces: 27, reflection_metaprogramming: 24
- `internal/copy/copy_value.go` (GO) | Magnitude: 35.72 | Delta: **0.097 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 22, indent_tabs: 20, encapsulation: 9, branch: 6
- `.github/scripts/e2e_test_linux_darwin.sh` (SHELL) | Magnitude: 1.42 | Delta: **0.523 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: reflection_metaprogramming: 13, indent_spaces: 8, branch: 7, safety_bypasses: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `internal/command/arguments/state_show.go` (GO) | Magnitude: 38.4 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 28, state_mutation: 24, encapsulation: 11, structural_boundaries: 5
- `internal/states/checks.go` (GO) | Magnitude: 153.48 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 94, state_mutation: 57, branch: 27, structural_boundaries: 21
- `internal/lang/funcs/datetime.go` (GO) | Magnitude: 134.66 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 119, state_mutation: 45, branch: 30, api: 30
- `internal/stacks/stackruntime/hooks/resource_instance.go` (GO) | Magnitude: 92.42 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 65, api: 28, structural_boundaries: 27, branch: 18
- `main.go` (GO) | Magnitude: 249.28 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 227, state_mutation: 134, encapsulation: 62, branch: 50

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `internal/dag/seq.go` (GO) | Magnitude: 82.12 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 42, state_mutation: 21, branch: 18, structural_boundaries: 12
- `internal/dag/dot.go` (GO) | Magnitude: 191.46 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 99, state_mutation: 79, branch: 25, encapsulation: 23
- `internal/legacy/helper/schema/set.go` (GO) | Magnitude: 243.4 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 137, indent_tabs: 113, structural_boundaries: 44, encapsulation: 40
- `internal/terraform/variables.go` (GO) | Magnitude: 241.86 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 117, state_mutation: 81, branch: 42, structural_boundaries: 39
- `internal/getproviders/providerreqs/hash.go` (GO) | Magnitude: 57.06 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 26, state_mutation: 15, doc: 14, branch: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `internal/command/workdir/config_state.go` (GO) | Magnitude: 18.32 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 9, indent_tabs: 7, doc: 4, class_start: 3
- `internal/command/views/init.go` (GO) | Magnitude: 75.02 | Delta: **0.061 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 36, state_mutation: 27, encapsulation: 19, structural_boundaries: 16
- `internal/stacks/stackruntime/internal/stackeval/hooks.go` (GO) | Magnitude: 41.58 | Delta: **0.249 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 42, doc: 31, api: 23, structural_boundaries: 13
- `internal/collections/cmp.go` (GO) | Magnitude: 21.74 | Delta: **0.278 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 12, state_mutation: 10, structural_boundaries: 8, encapsulation: 6
- `internal/stacks/stackruntime/hooks/callbacks.go` (GO) | Magnitude: 16.64 | Delta: **0.374 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 12, structural_boundaries: 5, generics: 5, safety: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `internal/cloud/backend.go` (GO) | Magnitude: 626.6 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 473, state_mutation: 333, encapsulation: 140, branch: 122
- `internal/stacks/stackruntime/internal/stackeval/provider_instance.go` (GO) | Magnitude: 175.34 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 156, state_mutation: 69, encapsulation: 44, api: 31
- `internal/cloud/backend_common.go` (GO) | Magnitude: 952.78 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 492, state_mutation: 329, branch: 196, encapsulation: 102
- `internal/command/views/hook_ui.go` (GO) | Magnitude: 314.66 | Delta: **0.066 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 191, state_mutation: 158, encapsulation: 81, branch: 42
- `internal/promising/task.go` (GO) | Magnitude: 92.96 | Delta: **0.081 IQR** | Secondary Pull: `file_cluster_11`
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
- `internal/tfdiags/consolidate_warnings.go` (GO) | Magnitude: 116.58 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: state_mutation: 58, indent_tabs: 58, encapsulation: 18, branch: 17
- `internal/plans/objchange/compatible.go` (GO) | Magnitude: 130.76 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 114, indent_tabs: 84, branch: 40, encapsulation: 20
- `internal/stacks/stackconfig/config.go` (GO) | Magnitude: 287.72 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 166, state_mutation: 108, encapsulation: 41, structural_boundaries: 39
- `internal/cloud/backend_show.go` (GO) | Magnitude: 53.44 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 33, state_mutation: 27, branch: 15, doc: 8
- `internal/command/cliconfig/config_windows.go` (GO) | Magnitude: 32.46 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 21, state_mutation: 19, structural_boundaries: 8, encapsulation: 7

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
- `internal/terraform/node_resource_plan_instance.go` -> Churn: **69.75%** | Cog Load: 36.0115% | Debt: 61.8024%
- `internal/lang/marks/marks.go` -> Churn: **68.88%** | Cog Load: 44.2703% | Debt: 96.9302%
- `internal/terraform/node_action_trigger_instance_plan.go` -> Churn: **68.55%** | Cog Load: 38.7753% | Debt: 59.4032%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `internal/backend/remote-state/s3/backend.go` -> **Kevin Vu** (100.0% isolated ownership) | Magnitude: 1594.94
- `internal/cloud/backend_common.go` -> **Daniel Banck** (100.0% isolated ownership) | Magnitude: 952.78
- `internal/terraform/node_resource_validate.go` -> **Daniel Schmidt** (90.0% isolated ownership) | Magnitude: 852.5
- `internal/backend/remote-state/oss/backend.go` -> **zeshan** (100.0% isolated ownership) | Magnitude: 798.4
- `internal/command/jsonstate/state.go` -> **Daniel Schmidt** (100.0% isolated ownership) | Magnitude: 666.38

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

- `internal/backend/remote-state/oci/log.go` -> **Severity: 9137.847** (Blast Radius: 114.168 * Doc Risk: 80.0386%)
- `internal/tfdiags/hcl.go` -> **Severity: 6314.8** (Blast Radius: 63.148 * Doc Risk: 100.0%)
- `internal/command/jsonformat/computed/renderers/json.go` -> **Severity: 1408.911** (Blast Radius: 14.569 * Doc Risk: 96.7061%)
- `internal/command/fmt.go` -> **Severity: 1310.792** (Blast Radius: 109.963 * Doc Risk: 11.9203%)
- `internal/states/sync.go` -> **Severity: 770.183** (Blast Radius: 64.611 * Doc Risk: 11.9203%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
