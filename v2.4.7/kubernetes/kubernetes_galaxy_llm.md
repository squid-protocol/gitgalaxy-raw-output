# ARCHITECTURAL_BRIEF: kubernetes
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/kubernetes` |
| **Timestamp** | `2026-08-07T05:07:54.009583+00:00` |
| **Scan Duration** | `45.73s` |
| **Git Branch** | `master` |
| **Git Commit** | `da663405beb487d66c27a0220ea4073305ae9077` |
| **Git Remote** | `https://github.com/kubernetes/kubernetes.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 10233 malicious artifacts.

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
| Total Artifacts | 28256 |
| Analyzed Artifacts (Scanned) | 17004 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 11252 |
| Total LOC | 1385689 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 60.2% |
| Dominant Lang | GO |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2167 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 124 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| GO | 9401 | 975389 | 55.3% |
| YAML | 5256 | 220048 | 30.9% |
| JSON | 703 | 167014 | 4.1% |
| PLAINTEXT | 567 | 81 | 3.3% |
| BINARY_THREAT | 554 | 554 | 3.3% |
| MARKDOWN | 240 | 0 | 1.4% |
| SHELL | 151 | 15906 | 0.9% |
| PROTO | 87 | 3636 | 0.5% |
| MAKEFILE | 23 | 567 | 0.1% |
| DOCKERFILE | 10 | 45 | 0.1% |
| POWERSHELL | 5 | 2318 | 0.0% |
| XML | 4 | 0 | 0.0% |
| PYTHON | 2 | 130 | 0.0% |
| CSV | 1 | 1 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.515`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 12871 | 75.7% |
| file_cluster_13 | 1041 | 6.1% |
| file_cluster_0 | 848 | 5.0% |
| Unknown | 635 | 3.7% |
| file_cluster_4 | 309 | 1.8% |
| file_cluster_15 | 214 | 1.3% |
| file_cluster_11 | 140 | 0.8% |
| file_cluster_12 | 53 | 0.3% |
| file_cluster_9 | 51 | 0.3% |
| file_cluster_6 | 48 | 0.3% |
| file_cluster_7 | 36 | 0.2% |
| file_cluster_16 | 17 | 0.1% |
| file_cluster_17 | 8 | 0.0% |
| file_cluster_2 | 3 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 726 | 4.3% |
| Static: Minified & Vendor Opaque Mass | 4 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 11252*

**Composition by Extension & Reason:**
- `.go`: 7063x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 9x Excluded (Saturation: Line 31 exceeds 500 chars), 8x Excluded (Saturation: Line 32 exceeds 500 chars)
- `no_extension`: 2369x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 71x Unsupported Format (.undeterminable), 1x Unresolved Ambiguity (Tier 4 Fallback failed Ecosystem Consensus)
- `.yaml`: 337x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Massive Static Asset Blob: 7019 LOC), 1x Excluded (Machine-Generated Source Code Signature: 106 LOC)
- `.md`: 326x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 75 LOC), 1x Excluded (Machine-Generated Source Code Signature: 120 LOC)
- `.sh`: 159x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 72 LOC)
- `.json`: 90x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 2390 LOC), 1x Excluded (Massive Static Asset Blob: 4196 LOC)
- `.yml`: 66x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 6 exceeds 500 chars)
- `.request`: 60x Unsupported Format (.request), 3x Excluded (Saturation: Line 4 exceeds 500 chars)
- `.response`: 58x Unsupported Format (.response), 3x Excluded (Saturation: Line 6 exceeds 500 chars), 2x Excluded (Saturation: Line 16 exceeds 500 chars)
- `.s`: 62x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.proto`: 38x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1418 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1373 LOC)
- `.sum`: 35x Unsupported Format (.sum), 2x Excluded (Unsupported Extension: '.sum')
- `.mod`: 36x Unsupported Format (.mod)
- `.edited`: 31x Unsupported Format (.edited)
- `.original`: 31x Unsupported Format (.original)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 16.8 | 6.3 | 0.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 33.3 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 26.0 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 7.6 | 0.2 | 0.0 |
| API Exposure | 0.0 | 17.8 | 2.4 | 0.2 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 2.9 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 39.4 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 87.4 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 9.5 | 0.3 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 2.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 26.0 | 11.9 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `cluster/gce/util.sh` (Hits: 816)
- `cluster/gce/gci/configure-helper.sh` (Hits: 433)
- `hack/local-up-cluster.sh` (Hits: 160)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **time.go** (`staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/time.go`) — 1381 inbound connections
2. **schema.go** (`staging/src/k8s.io/kubectl/pkg/validation/schema.go`) — 1231 inbound connections
3. **http.go** (`staging/src/k8s.io/apimachinery/pkg/util/net/http.go`) — 575 inbound connections
4. **io.go** (`staging/src/k8s.io/client-go/util/cert/io.go`) — 512 inbound connections
5. **testscheme.go** (`staging/src/k8s.io/code-generator/cmd/validation-gen/testscheme/testscheme.go`) — 239 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **allocator_testing.go** (`staging/src/k8s.io/dynamic-resource-allocation/structured/internal/allocatortesting/allocator_testing.go`) — 239 outbound dependencies
2. **validation_test.go** (`staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/cel/validation_test.go`) — 170 outbound dependencies
3. **validation_test.go** (`staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/validation/validation_test.go`) — 168 outbound dependencies
4. **kubelet.go** (`pkg/kubelet/kubelet.go`) — 128 outbound dependencies
5. **oidc_test.go** (`staging/src/k8s.io/apiserver/plugin/pkg/authenticator/token/oidc/oidc_test.go`) — 127 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `upload-tars_[Truncated]` (@ `cluster/gce/util.sh`) -> Impact: **1938.7** | LOC: 3927
  * *Intent:* # downloaded by the master as part of the start up script for the master. # # Assumed vars: # PROJECT # SERVER_BINARY_TAR # KUBE_MANIFESTS_TAR # ZONE ...
- `prepare-etcd-manifest_[Truncated]` (@ `cluster/gce/gci/configure-helper.sh`) -> Impact: **1141.2** | LOC: 1837
  * *Intent:* # Replaces the variables in the etcd manifest file with the real values, and then # copy the file to the manifest dir # $1: value for variable 'suffix...
- `append-param-if-not-present` (@ `cluster/gce/gci/configure-helper.sh`) -> Impact: **890.2** | LOC: 1795
- `Anonymous_Block_[Truncated]` (@ `hack/local-up-cluster.sh`) -> Impact: **836.4** | LOC: 1482
  * *Intent:* # enables testing eviction scenarios locally.
- `validateCustomResourceDefinitionValidati` (@ `staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/validation/validation.go`) -> Impact: **718.1** | LOC: 693
  * *Intent:* // suppressExpressionCostForUnchangedSchema returns a copy of opts with suppressPerExpressionCost set to true if // the specified version's schema is ...
- `ValidateUserAnnotations` (@ `pkg/apis/core/validation/validation.go`) -> Impact: **682.1** | LOC: 1449
- `newTestCacher` (@ `staging/src/k8s.io/apiserver/pkg/storage/cacher/cacher_whitebox_test.go`) -> Impact: **673.1** | LOC: 1542
- `ensureHostsFile` (@ `pkg/kubelet/kubelet_pods.go`) -> Impact: **570.0** | LOC: 870
- `dropDisabledFields` (@ `pkg/api/pod/util.go`) -> Impact: **527.2** | LOC: 599
- `WaitFor_GceMetadataServerRouteToBeRemove` (@ `cluster/gce/windows/k8s-node-setup.psm1`) -> Impact: **524.6** | LOC: 1232
  * *Intent:* # Checks if the route to the GCE metadata server is present. Returns when the # route is NOT present or after a timeout has expired.

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `cmd/kubeadm/app/util/pkiutil/testing/testdata` | 26 | 125000.0 | 0.0% | 0.0% |
| `staging/src/k8s.io/api/testdata/v1.34.0` | 552 | 92008.19 | 1.2% | 0.0% |
| `staging/src/k8s.io/api/testdata/HEAD` | 549 | 91508.09 | 1.2% | 0.0% |
| `staging/src/k8s.io/api/testdata/v1.33.0` | 546 | 91008.08 | 1.21% | 0.0% |
| `staging/src/k8s.io/kube-aggregator/pkg/apiserver/testdata` | 15 | 40000.06 | 2.47% | 6.67% |
| `pkg/kubeapiserver/options/testdata` | 13 | 30000.07 | 3.34% | 7.69% |
| `staging/src/k8s.io/apiserver/plugin/pkg/authenticator/token/oidc/testdata` | 7 | 30000.01 | 0.71% | 14.29% |
| `staging/src/k8s.io/apiserver/pkg/server/options/testdata` | 11 | 20000.07 | 4.16% | 9.09% |
| `staging/src/k8s.io/apiserver/pkg/authentication/request/x509/testdata` | 10 | 20000.07 | 4.58% | 10.0% |
| `pkg/kubelet/certificate/bootstrap/testdata` | 5 | 20000.0 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `cluster/addons/addon-manager/kube-addons-main.sh` -> **100.0%** Exposure
- `cluster/gce/gci/helper.sh` -> **100.0%** Exposure
- `cluster/gce/gci/kube-master-internal-route.sh` -> **100.0%** Exposure
- `cluster/gce/gci/node-helper.sh` -> **100.0%** Exposure
- `cluster/gce/windows/node-helper.sh` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `cluster/gce/config-common.sh` -> **100.0%** Exposure
- `cluster/gce/config-default.sh` -> **100.0%** Exposure
- `cluster/gce/delete-stranded-load-balancers.sh` -> **100.0%** Exposure
- `cluster/gce/gci/configure-kubeapiserver.sh` -> **100.0%** Exposure
- `cluster/gce/gci/kube-master-internal-route.sh` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `pkg/scheduler/testing/wrappers.go` -> **42** Orphaned Functions | **59** Duplicates
- `staging/src/k8s.io/apiserver/pkg/apis/apiserver/v1beta1/zz_generated.conversion.go` -> **96** Orphaned Functions | **0** Duplicates
- `staging/src/k8s.io/client-go/rest/request_test.go` -> **70** Orphaned Functions | **14** Duplicates
- `staging/src/k8s.io/api/networking/v1/zz_generated.deepcopy.go` -> **0** Orphaned Functions | **80** Duplicates
- `staging/src/k8s.io/api/apps/v1beta2/zz_generated.deepcopy.go` -> **0** Orphaned Functions | **77** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`cmd/genman/gen_kube_man.go`** -> AI Confidence: **99.48%**
2. **`cmd/kubeadm/app/apis/kubeadm/v1beta3/defaults.go`** -> AI Confidence: **99.48%**
3. **`cmd/kubeadm/app/apis/kubeadm/v1beta4/defaults.go`** -> AI Confidence: **99.48%**
4. **`pkg/api/pod/warnings.go`** -> AI Confidence: **99.48%**
5. **`pkg/api/testing/conversion.go`** -> AI Confidence: **99.48%**
6. **`pkg/apis/apps/fuzzer/fuzzer.go`** -> AI Confidence: **99.48%**
7. **`pkg/apis/apps/v1beta1/defaults.go`** -> AI Confidence: **99.48%**
8. **`pkg/apis/batch/v1/defaults.go`** -> AI Confidence: **99.48%**
9. **`pkg/apis/batch/validation/validation.go`** -> AI Confidence: **99.48%**
10. **`pkg/apis/core/fuzzer/fuzzer.go`** -> AI Confidence: **99.48%**
11. **`pkg/apis/core/v1/defaults.go`** -> AI Confidence: **99.48%**
12. **`pkg/apis/core/validation/events.go`** -> AI Confidence: **99.48%**
13. **`pkg/apis/discovery/validation/validation.go`** -> AI Confidence: **99.48%**
14. **`pkg/apis/networking/validation/validation.go`** -> AI Confidence: **99.48%**
15. **`pkg/controller/volume/attachdetach/reconciler/reconciler.go`** -> AI Confidence: **99.48%**
16. **`pkg/credentialprovider/plugin/config.go`** -> AI Confidence: **99.48%**
17. **`pkg/kubelet/apis/config/v1beta1/defaults.go`** -> AI Confidence: **99.48%**
18. **`pkg/kubelet/apis/config/validation/validation.go`** -> AI Confidence: **99.48%**
19. **`pkg/proxy/apis/config/v1alpha1/defaults.go`** -> AI Confidence: **99.48%**
20. **`pkg/proxy/conntrack/cleanup.go`** -> AI Confidence: **99.48%**
21. **`pkg/proxy/iptables/cleanup.go`** -> AI Confidence: **99.48%**
22. **`pkg/proxy/iptables/proxier.go`** -> AI Confidence: **99.48%**
23. **`pkg/proxy/nftables/proxier.go`** -> AI Confidence: **99.48%**
24. **`pkg/scheduler/apis/config/v1/defaults.go`** -> AI Confidence: **99.48%**
25. **`staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/fuzzer/fuzzer.go`** -> AI Confidence: **99.48%**
26. **`staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1beta1/conversion_test.go`** -> AI Confidence: **99.48%**
27. **`staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/defaulting/validation.go`** -> AI Confidence: **99.48%**
28. **`staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/validation_test.go`** -> AI Confidence: **99.48%**
29. **`staging/src/k8s.io/apiextensions-apiserver/test/integration/basic_test.go`** -> AI Confidence: **99.48%**
30. **`staging/src/k8s.io/apiextensions-apiserver/test/integration/limit_test.go`** -> AI Confidence: **99.48%**
31. **`staging/src/k8s.io/apiextensions-apiserver/test/integration/registration_test.go`** -> AI Confidence: **99.48%**
32. **`staging/src/k8s.io/apiextensions-apiserver/test/integration/subresources_test.go`** -> AI Confidence: **99.48%**
33. **`staging/src/k8s.io/apiextensions-apiserver/test/integration/yaml_test.go`** -> AI Confidence: **99.48%**
34. **`staging/src/k8s.io/apimachinery/pkg/api/apitesting/roundtrip/compatibility.go`** -> AI Confidence: **99.48%**
35. **`staging/src/k8s.io/apimachinery/pkg/api/apitesting/roundtrip/unstructured.go`** -> AI Confidence: **99.48%**
36. **`staging/src/k8s.io/apimachinery/pkg/api/errors/errors_test.go`** -> AI Confidence: **99.48%**
37. **`staging/src/k8s.io/apimachinery/pkg/api/resource/quantity.go`** -> AI Confidence: **99.48%**
38. **`staging/src/k8s.io/apimachinery/pkg/api/validate/content/decimal_int_test.go`** -> AI Confidence: **99.48%**
39. **`staging/src/k8s.io/apimachinery/pkg/api/validate/content/dns_test.go`** -> AI Confidence: **99.48%**
40. **`staging/src/k8s.io/apimachinery/pkg/api/validate/content/kube_test.go`** -> AI Confidence: **99.48%**
41. **`staging/src/k8s.io/apimachinery/pkg/api/validation/objectmeta_test.go`** -> AI Confidence: **99.48%**
42. **`staging/src/k8s.io/apimachinery/pkg/labels/selector_test.go`** -> AI Confidence: **99.48%**
43. **`staging/src/k8s.io/apimachinery/pkg/runtime/embedded_test.go`** -> AI Confidence: **99.48%**
44. **`staging/src/k8s.io/apimachinery/pkg/test/runtime_unversioned_test.go`** -> AI Confidence: **99.48%**
45. **`staging/src/k8s.io/apimachinery/pkg/util/framer/framer_test.go`** -> AI Confidence: **99.48%**
46. **`staging/src/k8s.io/apimachinery/pkg/util/intstr/intstr_test.go`** -> AI Confidence: **99.48%**
47. **`staging/src/k8s.io/apimachinery/pkg/util/validation/validation_test.go`** -> AI Confidence: **99.48%**
48. **`staging/src/k8s.io/apimachinery/pkg/util/yaml/decoder_test.go`** -> AI Confidence: **99.48%**
49. **`staging/src/k8s.io/apiserver/pkg/admission/plugin/webhook/predicates/rules/rules_test.go`** -> AI Confidence: **99.48%**
50. **`staging/src/k8s.io/apiserver/pkg/apis/apiserver/validation/validation_encryption.go`** -> AI Confidence: **99.48%**
51. **`staging/src/k8s.io/apiserver/pkg/audit/policy/checker_test.go`** -> AI Confidence: **99.48%**
52. **`staging/src/k8s.io/apiserver/pkg/authentication/request/union/unionauth_test.go`** -> AI Confidence: **99.48%**
53. **`staging/src/k8s.io/apiserver/pkg/authentication/token/union/unionauth_test.go`** -> AI Confidence: **99.48%**
54. **`staging/src/k8s.io/apiserver/pkg/cel/environment/base_test.go`** -> AI Confidence: **99.48%**
55. **`staging/src/k8s.io/apiserver/pkg/cel/library/semver_test.go`** -> AI Confidence: **99.48%**
56. **`staging/src/k8s.io/apiserver/pkg/endpoints/discovery/aggregated/handler_test.go`** -> AI Confidence: **99.48%**
57. **`staging/src/k8s.io/apiserver/pkg/endpoints/filterlatency/filterlatency_test.go`** -> AI Confidence: **99.48%**
58. **`staging/src/k8s.io/apiserver/pkg/endpoints/filters/authn_audit_test.go`** -> AI Confidence: **99.48%**
59. **`staging/src/k8s.io/apiserver/pkg/endpoints/filters/metrics.go`** -> AI Confidence: **99.48%**
60. **`staging/src/k8s.io/apiserver/pkg/endpoints/handlers/fieldmanager/bench_test.go`** -> AI Confidence: **99.48%**
61. **`staging/src/k8s.io/apiserver/pkg/endpoints/request/requestinfo_test.go`** -> AI Confidence: **99.48%**
62. **`staging/src/k8s.io/apiserver/pkg/registry/rest/resttest/resttest.go`** -> AI Confidence: **99.48%**
63. **`staging/src/k8s.io/apiserver/pkg/server/options/server_run_options_test.go`** -> AI Confidence: **99.48%**
64. **`staging/src/k8s.io/apiserver/pkg/server/options/tracing_test.go`** -> AI Confidence: **99.48%**
65. **`staging/src/k8s.io/apiserver/pkg/storage/etcd3/compact_test.go`** -> AI Confidence: **99.48%**
66. **`staging/src/k8s.io/apiserver/pkg/storage/value/encrypt/aes/aes_test.go`** -> AI Confidence: **99.48%**
67. **`staging/src/k8s.io/apiserver/pkg/storage/value/encrypt/secretbox/secretbox_test.go`** -> AI Confidence: **99.48%**
68. **`staging/src/k8s.io/apiserver/pkg/util/flowcontrol/exempt_borrowing_test.go`** -> AI Confidence: **99.48%**
69. **`staging/src/k8s.io/apiserver/pkg/util/flowcontrol/match_test.go`** -> AI Confidence: **99.48%**
70. **`staging/src/k8s.io/apiserver/pkg/util/flowcontrol/metrics/timing_ratio_histogram_test.go`** -> AI Confidence: **99.48%**
71. **`staging/src/k8s.io/client-go/metadata/metadata_test.go`** -> AI Confidence: **99.48%**
72. **`staging/src/k8s.io/client-go/metadata/metadatalister/lister_test.go`** -> AI Confidence: **99.48%**
73. **`staging/src/k8s.io/client-go/openapi/openapitest/fileclient_test.go`** -> AI Confidence: **99.48%**
74. **`staging/src/k8s.io/client-go/tools/cache/heap_test.go`** -> AI Confidence: **99.48%**
75. **`staging/src/k8s.io/client-go/tools/leaderelection/resourcelock/leaselock_test.go`** -> AI Confidence: **99.48%**
76. **`staging/src/k8s.io/client-go/transport/cache_test.go`** -> AI Confidence: **99.48%**
77. **`staging/src/k8s.io/code-generator/cmd/conversion-gen/generators/conversion.go`** -> AI Confidence: **99.48%**
78. **`staging/src/k8s.io/component-base/config/testing/roundtrip.go`** -> AI Confidence: **99.48%**
79. **`staging/src/k8s.io/kube-aggregator/pkg/apiserver/handler_apis_test.go`** -> AI Confidence: **99.48%**
80. **`staging/src/k8s.io/kubectl/pkg/cmd/cmd_test.go`** -> AI Confidence: **99.48%**
81. **`staging/src/k8s.io/kubectl/pkg/cmd/kuberc/set_test.go`** -> AI Confidence: **99.48%**
82. **`staging/src/k8s.io/kubectl/pkg/scale/scale_test.go`** -> AI Confidence: **99.48%**
83. **`staging/src/k8s.io/mount-utils/mount_helper_unix_test.go`** -> AI Confidence: **99.48%**
84. **`staging/src/k8s.io/pod-security-admission/admission/api/load/load_test.go`** -> AI Confidence: **99.48%**
85. **`staging/src/k8s.io/pod-security-admission/metrics/metrics_test.go`** -> AI Confidence: **99.48%**
86. **`staging/src/k8s.io/pod-security-admission/test/fixtures_test.go`** -> AI Confidence: **99.48%**
87. **`test/e2e/storage/utils/deployment.go`** -> AI Confidence: **99.48%**
88. **`staging/src/k8s.io/kubectl/pkg/cmd/edit/edit.go`** -> AI Confidence: **99.43%**
89. **`cluster/gce/gci/configure-helper.sh`** -> AI Confidence: **99.39%**
90. **`cluster/gce/util.sh`** -> AI Confidence: **99.39%**
91. **`cmd/dependencycheck/dependencycheck.go`** -> AI Confidence: **99.39%**
92. **`cmd/fieldnamedocscheck/field_name_docs_check.go`** -> AI Confidence: **99.39%**
93. **`cmd/genfeaturegates/genfeaturegates.go`** -> AI Confidence: **99.39%**
94. **`cmd/genyaml/gen_kubectl_yaml.go`** -> AI Confidence: **99.39%**
95. **`cmd/kube-apiserver/app/options/validation.go`** -> AI Confidence: **99.39%**
96. **`cmd/kubeadm/app/phases/controlplane/manifests.go`** -> AI Confidence: **99.39%**
97. **`hack/tools/golangci-lint/sorted/pkg/sorted.go`** -> AI Confidence: **99.39%**
98. **`pkg/api/persistentvolume/util.go`** -> AI Confidence: **99.39%**
99. **`pkg/api/pod/util.go`** -> AI Confidence: **99.39%**
100. **`pkg/apis/admissionregistration/validation/validation.go`** -> AI Confidence: **99.39%**
101. **`pkg/apis/apiserverinternal/validation/validation.go`** -> AI Confidence: **99.39%**
102. **`pkg/apis/apps/validation/validation.go`** -> AI Confidence: **99.39%**
103. **`pkg/apis/autoscaling/validation/validation.go`** -> AI Confidence: **99.39%**
104. **`pkg/apis/coordination/validation/validation.go`** -> AI Confidence: **99.39%**
105. **`pkg/apis/core/v1/validation/validation.go`** -> AI Confidence: **99.39%**
106. **`pkg/apis/core/validation/validation.go`** -> AI Confidence: **99.39%**
107. **`pkg/apis/flowcontrol/validation/validation.go`** -> AI Confidence: **99.39%**
108. **`pkg/apis/rbac/validation/validation.go`** -> AI Confidence: **99.39%**
109. **`pkg/apis/scheduling/validation/validation.go`** -> AI Confidence: **99.39%**
110. **`pkg/apis/storagemigration/validation/validation.go`** -> AI Confidence: **99.39%**
111. **`pkg/controller/endpointslicemirroring/reconciler.go`** -> AI Confidence: **99.39%**
112. **`pkg/kubelet/cm/helpers.go`** -> AI Confidence: **99.39%**
113. **`pkg/kubelet/kubelet.go`** -> AI Confidence: **99.39%**
114. **`pkg/kubelet/kubelet_resources.go`** -> AI Confidence: **99.39%**
115. **`pkg/kubelet/kubelet_server_journal_windows.go`** -> AI Confidence: **99.39%**
116. **`pkg/kubelet/kubelet_volumes.go`** -> AI Confidence: **99.39%**
117. **`pkg/kubelet/nodestatus/setters.go`** -> AI Confidence: **99.39%**
118. **`pkg/kubelet/prober/worker.go`** -> AI Confidence: **99.39%**
119. **`pkg/kubelet/server/auth.go`** -> AI Confidence: **99.39%**
120. **`pkg/kubelet/volumemanager/reconciler/reconciler_common.go`** -> AI Confidence: **99.39%**
121. **`pkg/proxy/apis/config/validation/validation.go`** -> AI Confidence: **99.39%**
122. **`pkg/proxy/ipvs/cleanup.go`** -> AI Confidence: **99.39%**
123. **`pkg/proxy/ipvs/proxier.go`** -> AI Confidence: **99.39%**
124. **`pkg/registry/authorization/util/helpers.go`** -> AI Confidence: **99.39%**
125. **`pkg/scheduler/apis/config/v1/default_plugins.go`** -> AI Confidence: **99.39%**
126. **`pkg/scheduler/apis/config/validation/validation.go`** -> AI Confidence: **99.39%**
127. **`pkg/scheduler/apis/config/validation/validation_pluginargs.go`** -> AI Confidence: **99.39%**
128. **`pkg/scheduler/framework/plugins/helper/spread.go`** -> AI Confidence: **99.39%**
129. **`pkg/scheduler/framework/plugins/imagelocality/image_locality.go`** -> AI Confidence: **99.39%**
130. **`pkg/scheduler/schedule_one_podgroup.go`** -> AI Confidence: **99.39%**
131. **`plugin/pkg/admission/limitranger/admission.go`** -> AI Confidence: **99.39%**
132. **`staging/src/k8s.io/api/roundtrip_test.go`** -> AI Confidence: **99.39%**
133. **`staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1/conversion_test.go`** -> AI Confidence: **99.39%**
134. **`staging/src/k8s.io/apiextensions-apiserver/pkg/apis/roundtrip_test.go`** -> AI Confidence: **99.39%**
135. **`staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/customresource_handler_test.go`** -> AI Confidence: **99.39%**
136. **`staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/cel/model/schemas_test.go`** -> AI Confidence: **99.39%**
137. **`staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/convert_test.go`** -> AI Confidence: **99.39%**
138. **`staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/defaulting/validation_test.go`** -> AI Confidence: **99.39%**
139. **`staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/objectmeta/validation.go`** -> AI Confidence: **99.39%**
140. **`staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/validation/formats_test.go`** -> AI Confidence: **99.39%**
141. **`staging/src/k8s.io/apiextensions-apiserver/test/integration/apply_test.go`** -> AI Confidence: **99.39%**
142. **`staging/src/k8s.io/apiextensions-apiserver/test/integration/objectmeta_test.go`** -> AI Confidence: **99.39%**
143. **`staging/src/k8s.io/apiextensions-apiserver/test/integration/table_test.go`** -> AI Confidence: **99.39%**
144. **`staging/src/k8s.io/apimachinery/pkg/api/meta/testrestmapper/test_restmapper.go`** -> AI Confidence: **99.39%**
145. **`staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/micro_time_test.go`** -> AI Confidence: **99.39%**
146. **`staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/time_test.go`** -> AI Confidence: **99.39%**
147. **`staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/validation/validation_test.go`** -> AI Confidence: **99.39%**
148. **`staging/src/k8s.io/apimachinery/pkg/fields/selector_test.go`** -> AI Confidence: **99.39%**
149. **`staging/src/k8s.io/apimachinery/pkg/test/runtime_serializer_protobuf_protobuf_test.go`** -> AI Confidence: **99.39%**
150. **`staging/src/k8s.io/apimachinery/pkg/util/cache/expiring_test.go`** -> AI Confidence: **99.39%**
151. **`staging/src/k8s.io/apimachinery/pkg/util/net/http_test.go`** -> AI Confidence: **99.39%**
152. **`staging/src/k8s.io/apimachinery/pkg/util/proxy/dial_test.go`** -> AI Confidence: **99.39%**
153. **`staging/src/k8s.io/apimachinery/pkg/util/version/version_test.go`** -> AI Confidence: **99.39%**
154. **`staging/src/k8s.io/apiserver/pkg/admission/plugin/cel/condition_test.go`** -> AI Confidence: **99.39%**
155. **`staging/src/k8s.io/apiserver/pkg/admission/plugin/policy/validating/dispatcher.go`** -> AI Confidence: **99.39%**
156. **`staging/src/k8s.io/apiserver/pkg/apis/apiserver/validation/validation.go`** -> AI Confidence: **99.39%**
157. **`staging/src/k8s.io/apiserver/pkg/audit/request_log_test.go`** -> AI Confidence: **99.39%**
158. **`staging/src/k8s.io/apiserver/pkg/audit/request_test.go`** -> AI Confidence: **99.39%**
159. **`staging/src/k8s.io/apiserver/pkg/authentication/request/websocket/protocol_test.go`** -> AI Confidence: **99.39%**
160. **`staging/src/k8s.io/apiserver/pkg/authentication/token/cache/cache_test.go`** -> AI Confidence: **99.39%**
161. **`staging/src/k8s.io/apiserver/pkg/cel/library/cidr_test.go`** -> AI Confidence: **99.39%**
162. **`staging/src/k8s.io/apiserver/pkg/cel/library/ip_test.go`** -> AI Confidence: **99.39%**
163. **`staging/src/k8s.io/apiserver/pkg/cel/library/library_compatibility_test.go`** -> AI Confidence: **99.39%**
164. **`staging/src/k8s.io/apiserver/pkg/cel/library/quantity_test.go`** -> AI Confidence: **99.39%**
165. **`staging/src/k8s.io/apiserver/pkg/endpoints/filters/impersonation/impersonation.go`** -> AI Confidence: **99.39%**
166. **`staging/src/k8s.io/apiserver/pkg/endpoints/patchhandler_test.go`** -> AI Confidence: **99.39%**
167. **`staging/src/k8s.io/apiserver/pkg/registry/generic/rest/response_checker_test.go`** -> AI Confidence: **99.39%**
168. **`staging/src/k8s.io/apiserver/pkg/server/egressselector/config.go`** -> AI Confidence: **99.39%**
169. **`staging/src/k8s.io/apiserver/pkg/server/options/authentication_test.go`** -> AI Confidence: **99.39%**
170. **`staging/src/k8s.io/apiserver/pkg/server/options/encryptionconfig/config_test.go`** -> AI Confidence: **99.39%**
171. **`staging/src/k8s.io/apiserver/pkg/server/options/etcd_test.go`** -> AI Confidence: **99.39%**
172. **`staging/src/k8s.io/apiserver/pkg/storage/cacher/cacher_whitebox_test.go`** -> AI Confidence: **99.39%**
173. **`staging/src/k8s.io/apiserver/pkg/storage/cacher/caching_object_test.go`** -> AI Confidence: **99.39%**
174. **`staging/src/k8s.io/apiserver/pkg/storage/cacher/delegator_test.go`** -> AI Confidence: **99.39%**
175. **`staging/src/k8s.io/apiserver/pkg/storage/selection_predicate_test.go`** -> AI Confidence: **99.39%**
176. **`staging/src/k8s.io/apiserver/pkg/storage/testing/store_benchmarks.go`** -> AI Confidence: **99.39%**
177. **`staging/src/k8s.io/apiserver/pkg/storage/value/transformer_test.go`** -> AI Confidence: **99.39%**
178. **`staging/src/k8s.io/apiserver/pkg/storageversion/updater.go`** -> AI Confidence: **99.39%**
179. **`staging/src/k8s.io/apiserver/pkg/util/flowcontrol/apf_controller.go`** -> AI Confidence: **99.39%**
180. **`staging/src/k8s.io/apiserver/pkg/util/flowcontrol/apf_controller_debug.go`** -> AI Confidence: **99.39%**
181. **`staging/src/k8s.io/apiserver/pkg/util/flowcontrol/fairqueuing/queueset/queueset_test.go`** -> AI Confidence: **99.39%**
182. **`staging/src/k8s.io/apiserver/pkg/util/flowcontrol/gen_test.go`** -> AI Confidence: **99.39%**
183. **`staging/src/k8s.io/apiserver/pkg/util/flowcontrol/request/list_work_estimator.go`** -> AI Confidence: **99.39%**
184. **`staging/src/k8s.io/cli-runtime/pkg/genericclioptions/jsonpath_flags_test.go`** -> AI Confidence: **99.39%**
185. **`staging/src/k8s.io/cli-runtime/pkg/printers/jsonpath_test.go`** -> AI Confidence: **99.39%**
186. **`staging/src/k8s.io/cli-runtime/pkg/resource/builder_test.go`** -> AI Confidence: **99.39%**
187. **`staging/src/k8s.io/client-go/dynamic/client_test.go`** -> AI Confidence: **99.39%**
188. **`staging/src/k8s.io/client-go/dynamic/dynamiclister/lister_test.go`** -> AI Confidence: **99.39%**
189. **`staging/src/k8s.io/client-go/examples/in-cluster-client-configuration/main.go`** -> AI Confidence: **99.39%**
190. **`staging/src/k8s.io/client-go/examples/out-of-cluster-client-configuration/main.go`** -> AI Confidence: **99.39%**
191. **`staging/src/k8s.io/client-go/kubernetes_test/fake_client_test.go`** -> AI Confidence: **99.39%**
192. **`staging/src/k8s.io/client-go/scale/client_test.go`** -> AI Confidence: **99.39%**
193. **`staging/src/k8s.io/client-go/tools/cache/expiration_cache_test.go`** -> AI Confidence: **99.39%**
194. **`staging/src/k8s.io/client-go/tools/clientcmd/api/helpers_test.go`** -> AI Confidence: **99.39%**
195. **`staging/src/k8s.io/client-go/tools/clientcmd/validation.go`** -> AI Confidence: **99.39%**
196. **`staging/src/k8s.io/client-go/tools/clientcmd/validation_test.go`** -> AI Confidence: **99.39%**
197. **`staging/src/k8s.io/client-go/tools/events/event_recorder_test.go`** -> AI Confidence: **99.39%**
198. **`staging/src/k8s.io/client-go/tools/events/helper_test.go`** -> AI Confidence: **99.39%**
199. **`staging/src/k8s.io/client-go/tools/remotecommand/v2_test.go`** -> AI Confidence: **99.39%**
200. **`staging/src/k8s.io/client-go/util/cert/csr_test.go`** -> AI Confidence: **99.39%**
201. **`staging/src/k8s.io/client-go/util/csaupgrade/upgrade_test.go`** -> AI Confidence: **99.39%**
202. **`staging/src/k8s.io/client-go/util/workqueue/delaying_queue_test.go`** -> AI Confidence: **99.39%**
203. **`staging/src/k8s.io/cloud-provider/controllers/route/route_controller_test.go`** -> AI Confidence: **99.39%**
204. **`staging/src/k8s.io/cloud-provider/service/helpers/helper_test.go`** -> AI Confidence: **99.39%**
205. **`staging/src/k8s.io/code-generator/cmd/applyconfiguration-gen/generators/applyconfiguration.go`** -> AI Confidence: **99.39%**
206. **`staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/typedefs/zz_generated.validations.go`** -> AI Confidence: **99.39%**
207. **`staging/src/k8s.io/component-base/config/validation/validation_test.go`** -> AI Confidence: **99.39%**
208. **`staging/src/k8s.io/component-base/metrics/histogram_test.go`** -> AI Confidence: **99.39%**
209. **`staging/src/k8s.io/component-base/metrics/registry_test.go`** -> AI Confidence: **99.39%**
210. **`staging/src/k8s.io/component-base/metrics/timing_histogram_test.go`** -> AI Confidence: **99.39%**
211. **`staging/src/k8s.io/component-base/tracing/tracing_test.go`** -> AI Confidence: **99.39%**
212. **`staging/src/k8s.io/endpointslice/reconciler.go`** -> AI Confidence: **99.39%**
213. **`staging/src/k8s.io/endpointslice/reconciler_test.go`** -> AI Confidence: **99.39%**
214. **`staging/src/k8s.io/endpointslice/utils.go`** -> AI Confidence: **99.39%**
215. **`staging/src/k8s.io/kube-aggregator/pkg/apis/apiregistration/validation/validation.go`** -> AI Confidence: **99.39%**
216. **`staging/src/k8s.io/kube-aggregator/pkg/controllers/status/local/local_available_controller_test.go`** -> AI Confidence: **99.39%**
217. **`staging/src/k8s.io/kubectl/pkg/cmd/apiresources/apiresources_test.go`** -> AI Confidence: **99.39%**
218. **`staging/src/k8s.io/kubectl/pkg/cmd/config/set_credentials.go`** -> AI Confidence: **99.39%**
219. **`staging/src/k8s.io/kubectl/pkg/cmd/cp/cp_test.go`** -> AI Confidence: **99.39%**
220. **`staging/src/k8s.io/kubectl/pkg/cmd/create/create_token_test.go`** -> AI Confidence: **99.39%**
221. **`staging/src/k8s.io/kubectl/pkg/cmd/delete/delete_flags.go`** -> AI Confidence: **99.39%**
222. **`staging/src/k8s.io/kubectl/pkg/cmd/drain/drain.go`** -> AI Confidence: **99.39%**
223. **`staging/src/k8s.io/kubectl/pkg/cmd/drain/drain_test.go`** -> AI Confidence: **99.39%**
224. **`staging/src/k8s.io/kubectl/pkg/cmd/get/customcolumn_test.go`** -> AI Confidence: **99.39%**
225. **`staging/src/k8s.io/kubectl/pkg/cmd/plugin/plugin_test.go`** -> AI Confidence: **99.39%**
226. **`staging/src/k8s.io/kubectl/pkg/cmd/portforward/portforward_test.go`** -> AI Confidence: **99.39%**
227. **`staging/src/k8s.io/kubectl/pkg/cmd/set/set_env.go`** -> AI Confidence: **99.39%**
228. **`staging/src/k8s.io/kubectl/pkg/cmd/top/top.go`** -> AI Confidence: **99.39%**
229. **`staging/src/k8s.io/kubectl/pkg/cmd/top/top_pod_test.go`** -> AI Confidence: **99.39%**
230. **`staging/src/k8s.io/kubectl/pkg/describe/describe_test.go`** -> AI Confidence: **99.39%**
231. **`staging/src/k8s.io/kubectl/pkg/drain/drain_test.go`** -> AI Confidence: **99.39%**
232. **`staging/src/k8s.io/kubectl/pkg/metricsutil/metrics_printer.go`** -> AI Confidence: **99.39%**
233. **`staging/src/k8s.io/kubectl/pkg/polymorphichelpers/history_test.go`** -> AI Confidence: **99.39%**
234. **`staging/src/k8s.io/kubectl/pkg/polymorphichelpers/rollout_status_test.go`** -> AI Confidence: **99.39%**
235. **`staging/src/k8s.io/kubectl/pkg/proxy/proxy_server_test.go`** -> AI Confidence: **99.39%**
236. **`staging/src/k8s.io/kubectl/pkg/util/completion/completion.go`** -> AI Confidence: **99.39%**
237. **`staging/src/k8s.io/pod-security-admission/api/helpers_test.go`** -> AI Confidence: **99.39%**
238. **`cmd/cloud-controller-manager/main.go`** -> AI Confidence: **99.35%**
239. **`cmd/kubeadm/app/cmd/phases/reset/removeetcdmember.go`** -> AI Confidence: **99.35%**
240. **`pkg/api/testing/validation.go`** -> AI Confidence: **99.35%**
241. **`pkg/controller/job/indexed_job_utils.go`** -> AI Confidence: **99.35%**
242. **`pkg/controller/replicaset/replica_set_utils.go`** -> AI Confidence: **99.35%**
243. **`pkg/controller/volume/attachdetach/populator/desired_state_of_world_populator.go`** -> AI Confidence: **99.35%**
244. **`pkg/kubelet/kubelet_node_status.go`** -> AI Confidence: **99.35%**
245. **`staging/src/k8s.io/apimachinery/pkg/util/managedfields/internal/lastappliedupdater_test.go`** -> AI Confidence: **99.35%**
246. **`staging/src/k8s.io/apiserver/pkg/admission/config_test.go`** -> AI Confidence: **99.35%**
247. **`staging/src/k8s.io/apiserver/pkg/admission/plugin/resourcequota/resource_access_test.go`** -> AI Confidence: **99.35%**
248. **`staging/src/k8s.io/apiserver/pkg/admission/plugin/webhook/validating/plugin_test.go`** -> AI Confidence: **99.35%**
249. **`staging/src/k8s.io/apiserver/pkg/apis/apiserver/validation/validation_test.go`** -> AI Confidence: **99.35%**
250. **`staging/src/k8s.io/apiserver/pkg/endpoints/discovery/aggregated/metrics_test.go`** -> AI Confidence: **99.35%**
251. **`staging/src/k8s.io/apiserver/pkg/util/proxy/proxy_test.go`** -> AI Confidence: **99.35%**
252. **`staging/src/k8s.io/code-generator/cmd/register-gen/generators/targets.go`** -> AI Confidence: **99.35%**
253. **`staging/src/k8s.io/code-generator/cmd/validation-gen/validation.go`** -> AI Confidence: **99.35%**
254. **`staging/src/k8s.io/dynamic-resource-allocation/resourceslice/resourceslicecontroller.go`** -> AI Confidence: **99.35%**
255. **`staging/src/k8s.io/kubectl/pkg/cmd/expose/expose.go`** -> AI Confidence: **99.35%**
256. **`staging/src/k8s.io/kubectl/pkg/cmd/set/set_resources.go`** -> AI Confidence: **99.35%**
257. **`staging/src/k8s.io/kubectl/pkg/cmd/top/top_node_test.go`** -> AI Confidence: **99.35%**
258. **`cmd/kubeadm/app/cmd/options/generic.go`** -> AI Confidence: **99.34%**
259. **`cmd/kubeadm/app/componentconfigs/kubelet.go`** -> AI Confidence: **99.34%**
260. **`pkg/api/persistentvolumeclaim/util.go`** -> AI Confidence: **99.34%**
261. **`pkg/api/service/warnings.go`** -> AI Confidence: **99.34%**
262. **`pkg/apis/apps/v1/defaults.go`** -> AI Confidence: **99.34%**
263. **`pkg/apis/apps/v1beta2/defaults.go`** -> AI Confidence: **99.34%**
264. **`pkg/apis/core/helper/qos/qos.go`** -> AI Confidence: **99.34%**
265. **`pkg/apis/core/v1/helper/qos/qos.go`** -> AI Confidence: **99.34%**
266. **`pkg/apis/extensions/v1beta1/defaults.go`** -> AI Confidence: **99.34%**
267. **`pkg/volume/util/nested_volumes.go`** -> AI Confidence: **99.34%**
268. **`staging/src/k8s.io/apimachinery/pkg/api/meta/priority_test.go`** -> AI Confidence: **99.34%**
269. **`staging/src/k8s.io/apimachinery/pkg/api/validate/content/identifier_test.go`** -> AI Confidence: **99.34%**
270. **`staging/src/k8s.io/apimachinery/pkg/apis/meta/internalversion/scheme/register_test.go`** -> AI Confidence: **99.34%**
271. **`staging/src/k8s.io/apimachinery/pkg/util/managedfields/internal/fields_test.go`** -> AI Confidence: **99.34%**
272. **`staging/src/k8s.io/apimachinery/pkg/util/managedfields/internal/managedfields_test.go`** -> AI Confidence: **99.34%**
273. **`staging/src/k8s.io/apimachinery/pkg/util/managedfields/scalehandler_test.go`** -> AI Confidence: **99.34%**
274. **`staging/src/k8s.io/apiserver/pkg/admission/plugin/policy/mutating/compilation.go`** -> AI Confidence: **99.34%**
275. **`staging/src/k8s.io/apiserver/pkg/authentication/token/tokenfile/tokenfile_test.go`** -> AI Confidence: **99.34%**
276. **`staging/src/k8s.io/apiserver/pkg/cel/library/format_test.go`** -> AI Confidence: **99.34%**
277. **`staging/src/k8s.io/apiserver/pkg/server/filters/cors_test.go`** -> AI Confidence: **99.34%**
278. **`staging/src/k8s.io/apiserver/pkg/server/options/admission_test.go`** -> AI Confidence: **99.34%**
279. **`staging/src/k8s.io/apiserver/pkg/util/flowcontrol/fairqueuing/queueset/fifo_list_test.go`** -> AI Confidence: **99.34%**
280. **`staging/src/k8s.io/apiserver/pkg/util/flowcontrol/fairqueuing/testing/eventclock/fake_event_clock_test.go`** -> AI Confidence: **99.34%**
281. **`staging/src/k8s.io/cloud-provider/config/v1alpha1/defaults.go`** -> AI Confidence: **99.34%**
282. **`staging/src/k8s.io/cloud-provider/volume/helpers/zones_test.go`** -> AI Confidence: **99.34%**
283. **`staging/src/k8s.io/code-generator/cmd/applyconfiguration-gen/generators/openapi.go`** -> AI Confidence: **99.34%**
284. **`staging/src/k8s.io/code-generator/cmd/defaulter-gen/output_tests/marker/zz_generated.defaults.go`** -> AI Confidence: **99.34%**
285. **`staging/src/k8s.io/component-base/cli/flag/namedcertkey_flag_test.go`** -> AI Confidence: **99.34%**
286. **`staging/src/k8s.io/component-base/cli/flag/string_slice_flag_test.go`** -> AI Confidence: **99.34%**
287. **`staging/src/k8s.io/component-base/metrics/gauge_test.go`** -> AI Confidence: **99.34%**
288. **`staging/src/k8s.io/component-helpers/node/util/ips_test.go`** -> AI Confidence: **99.34%**
289. **`staging/src/k8s.io/csi-translation-lib/plugins/in_tree_volume.go`** -> AI Confidence: **99.34%**
290. **`staging/src/k8s.io/kubectl/pkg/util/podutils/podutils_test.go`** -> AI Confidence: **99.34%**
291. **`staging/src/k8s.io/mount-utils/mount_test.go`** -> AI Confidence: **99.34%**
292. **`staging/src/k8s.io/pod-security-admission/policy/check_restrictedVolumes.go`** -> AI Confidence: **99.34%**
293. **`staging/src/k8s.io/pod-security-admission/test/run.go`** -> AI Confidence: **99.34%**
294. **`test/e2e/storage/utils/pod.go`** -> AI Confidence: **99.34%**
295. **`cluster/addons/addon-manager/kube-addons-main.sh`** -> AI Confidence: **99.32%**
296. **`cluster/kube-up.sh`** -> AI Confidence: **99.32%**
297. **`cluster/kube-util.sh`** -> AI Confidence: **99.32%**
298. **`cluster/validate-cluster.sh`** -> AI Confidence: **99.32%**
299. **`hack/ginkgo-e2e.sh`** -> AI Confidence: **99.32%**
300. **`hack/make-rules/verify.sh`** -> AI Confidence: **99.32%**
301. **`hack/verify-golangci-lint.sh`** -> AI Confidence: **99.32%**
302. **`hack/verify-licenses.sh`** -> AI Confidence: **99.32%**
303. **`staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1beta1/defaults.go`** -> AI Confidence: **99.32%**
304. **`staging/src/k8s.io/apimachinery/pkg/util/rand/rand_test.go`** -> AI Confidence: **99.32%**
305. **`staging/src/k8s.io/apimachinery/pkg/util/sets/set_generic_test.go`** -> AI Confidence: **99.32%**
306. **`staging/src/k8s.io/apiserver/pkg/admission/metrics/testutil_test.go`** -> AI Confidence: **99.32%**
307. **`staging/src/k8s.io/apiserver/pkg/registry/rest/meta_test.go`** -> AI Confidence: **99.32%**
308. **`staging/src/k8s.io/apiserver/pkg/server/dynamiccertificates/tlsconfig_test.go`** -> AI Confidence: **99.32%**
309. **`staging/src/k8s.io/apiserver/pkg/storage/api_object_versioner_test.go`** -> AI Confidence: **99.32%**
310. **`staging/src/k8s.io/client-go/rest/url_utils_test.go`** -> AI Confidence: **99.32%**
311. **`staging/src/k8s.io/client-go/tools/cache/object-names_test.go`** -> AI Confidence: **99.32%**
312. **`staging/src/k8s.io/client-go/util/flowcontrol/backoff_test.go`** -> AI Confidence: **99.32%**
313. **`staging/src/k8s.io/code-generator/cmd/deepcopy-gen/output_tests/wholepkg/deepcopy_test.go`** -> AI Confidence: **99.32%**
314. **`cmd/cloud-controller-manager/nodeipamcontroller.go`** -> AI Confidence: **99.31%**
315. **`cmd/import-boss/main.go`** -> AI Confidence: **99.31%**
316. **`cmd/importverifier/importverifier.go`** -> AI Confidence: **99.31%**
317. **`cmd/kube-apiserver/app/options/completion.go`** -> AI Confidence: **99.31%**
318. **`cmd/kube-apiserver/app/options/options.go`** -> AI Confidence: **99.31%**
319. **`cmd/kube-apiserver/app/server.go`** -> AI Confidence: **99.31%**
320. **`cmd/kube-apiserver/app/testing/testserver.go`** -> AI Confidence: **99.31%**
321. **`cmd/kube-controller-manager/app/certificates.go`** -> AI Confidence: **99.31%**
322. **`cmd/kube-controller-manager/app/controller_descriptor.go`** -> AI Confidence: **99.31%**
323. **`cmd/kube-controller-manager/app/controllermanager.go`** -> AI Confidence: **99.31%**
324. **`cmd/kube-controller-manager/app/options/options.go`** -> AI Confidence: **99.31%**
325. **`cmd/kube-controller-manager/app/service_accounts.go`** -> AI Confidence: **99.31%**
326. **`cmd/kube-controller-manager/app/testing/testserver.go`** -> AI Confidence: **99.31%**
327. **`cmd/kube-proxy/app/server.go`** -> AI Confidence: **99.31%**
328. **`cmd/kube-proxy/app/server_linux.go`** -> AI Confidence: **99.31%**
329. **`cmd/kube-proxy/app/server_windows.go`** -> AI Confidence: **99.31%**
330. **`cmd/kube-scheduler/app/server.go`** -> AI Confidence: **99.31%**
331. **`cmd/kube-scheduler/app/testing/testserver.go`** -> AI Confidence: **99.31%**
332. **`cmd/kubeadm/app/cmd/certs.go`** -> AI Confidence: **99.31%**
333. **`cmd/kubeadm/app/cmd/completion.go`** -> AI Confidence: **99.31%**
334. **`cmd/kubeadm/app/cmd/join.go`** -> AI Confidence: **99.31%**
335. **`cmd/kubeadm/app/cmd/kubeconfig.go`** -> AI Confidence: **99.31%**
336. **`cmd/kubeadm/app/cmd/phases/init/certs.go`** -> AI Confidence: **99.31%**
337. **`cmd/kubeadm/app/cmd/phases/init/kubeconfig.go`** -> AI Confidence: **99.31%**
338. **`cmd/kubeadm/app/cmd/phases/init/kubelet.go`** -> AI Confidence: **99.31%**
339. **`cmd/kubeadm/app/cmd/phases/init/kubeletfinalize.go`** -> AI Confidence: **99.31%**
340. **`cmd/kubeadm/app/cmd/phases/init/showjoincommand.go`** -> AI Confidence: **99.31%**
341. **`cmd/kubeadm/app/cmd/phases/init/waitcontrolplane.go`** -> AI Confidence: **99.31%**
342. **`cmd/kubeadm/app/cmd/phases/join/controlplanejoin.go`** -> AI Confidence: **99.31%**
343. **`cmd/kubeadm/app/cmd/phases/reset/cleanupnode.go`** -> AI Confidence: **99.31%**
344. **`cmd/kubeadm/app/cmd/phases/reset/unmount_linux.go`** -> AI Confidence: **99.31%**
345. **`cmd/kubeadm/app/cmd/phases/upgrade/apply/bootstraptoken.go`** -> AI Confidence: **99.31%**
346. **`cmd/kubeadm/app/cmd/phases/upgrade/kubeletconfig.go`** -> AI Confidence: **99.31%**
347. **`cmd/kubeadm/app/cmd/reset.go`** -> AI Confidence: **99.31%**
348. **`cmd/kubeadm/app/cmd/token.go`** -> AI Confidence: **99.31%**
349. **`cmd/kubeadm/app/cmd/upgrade/diff.go`** -> AI Confidence: **99.31%**
350. **`cmd/kubeadm/app/cmd/upgrade/plan.go`** -> AI Confidence: **99.31%**
351. **`cmd/kubeadm/app/cmd/version.go`** -> AI Confidence: **99.31%**
352. **`cmd/kubeadm/app/componentconfigs/configset.go`** -> AI Confidence: **99.31%**
353. **`cmd/kubeadm/app/discovery/file/file.go`** -> AI Confidence: **99.31%**
354. **`cmd/kubeadm/app/discovery/token/token.go`** -> AI Confidence: **99.31%**
355. **`cmd/kubeadm/app/features/features.go`** -> AI Confidence: **99.31%**
356. **`cmd/kubeadm/app/phases/addons/dns/dns.go`** -> AI Confidence: **99.31%**
357. **`cmd/kubeadm/app/phases/certs/certlist.go`** -> AI Confidence: **99.31%**
358. **`cmd/kubeadm/app/phases/certs/certs.go`** -> AI Confidence: **99.31%**
359. **`cmd/kubeadm/app/phases/certs/renewal/manager.go`** -> AI Confidence: **99.31%**
360. **`cmd/kubeadm/app/phases/etcd/local.go`** -> AI Confidence: **99.31%**
361. **`cmd/kubeadm/app/phases/kubelet/flags.go`** -> AI Confidence: **99.31%**
362. **`cmd/kubeadm/app/phases/upgrade/compute.go`** -> AI Confidence: **99.31%**
363. **`cmd/kubeadm/app/phases/upgrade/health.go`** -> AI Confidence: **99.31%**
364. **`cmd/kubeadm/app/phases/upgrade/postupgrade.go`** -> AI Confidence: **99.31%**
365. **`cmd/kubeadm/app/phases/upgrade/staticpods.go`** -> AI Confidence: **99.31%**
366. **`cmd/kubeadm/app/preflight/checks.go`** -> AI Confidence: **99.31%**
367. **`cmd/kubeadm/app/util/arguments.go`** -> AI Confidence: **99.31%**
368. **`cmd/kubeadm/app/util/certs/util.go`** -> AI Confidence: **99.31%**
369. **`cmd/kubeadm/app/util/config/initconfiguration.go`** -> AI Confidence: **99.31%**
370. **`cmd/kubeadm/app/util/config/joinconfiguration.go`** -> AI Confidence: **99.31%**
371. **`cmd/kubeadm/app/util/config/resetconfiguration.go`** -> AI Confidence: **99.31%**
372. **`cmd/kubeadm/app/util/config/upgradeconfiguration.go`** -> AI Confidence: **99.31%**
373. **`cmd/kubeadm/app/util/dryrun/dryrun.go`** -> AI Confidence: **99.31%**
374. **`cmd/kubeadm/app/util/endpoint.go`** -> AI Confidence: **99.31%**
375. **`cmd/kubeadm/app/util/etcd/etcd.go`** -> AI Confidence: **99.31%**
376. **`cmd/kubeadm/app/util/marshal.go`** -> AI Confidence: **99.31%**
377. **`cmd/kubeadm/app/util/patches/patches.go`** -> AI Confidence: **99.31%**
378. **`cmd/kubeadm/app/util/pkiutil/pki_helpers.go`** -> AI Confidence: **99.31%**
379. **`cmd/kubeadm/app/util/pkiutil/testing/testing.go`** -> AI Confidence: **99.31%**
380. **`cmd/kubeadm/app/util/runtime/runtime.go`** -> AI Confidence: **99.31%**
381. **`cmd/kubeadm/app/util/users/users_linux.go`** -> AI Confidence: **99.31%**
382. **`cmd/kubeadm/app/util/version.go`** -> AI Confidence: **99.31%**
383. **`cmd/kubelet/app/server.go`** -> AI Confidence: **99.31%**
384. **`cmd/preferredimports/preferredimports.go`** -> AI Confidence: **99.31%**
385. **`cmd/prune-junit-xml/prunexml.go`** -> AI Confidence: **99.31%**
386. **`hack/conformance/check_conformance_test_requirements.go`** -> AI Confidence: **99.31%**
387. **`hack/tools/golangci-lint/sorted/pkg/sorted_test.go`** -> AI Confidence: **99.31%**
388. **`pkg/api/job/warnings.go`** -> AI Confidence: **99.31%**
389. **`pkg/api/node/util.go`** -> AI Confidence: **99.31%**
390. **`pkg/api/testing/compat/compatibility_tester.go`** -> AI Confidence: **99.31%**
391. **`pkg/api/testing/fuzzer.go`** -> AI Confidence: **99.31%**
392. **`pkg/api/v1/resource/helpers.go`** -> AI Confidence: **99.31%**
393. **`pkg/apis/apps/v1beta1/conversion.go`** -> AI Confidence: **99.31%**
394. **`pkg/apis/certificates/validation/validation.go`** -> AI Confidence: **99.31%**
395. **`pkg/apis/core/helper/helpers.go`** -> AI Confidence: **99.31%**
396. **`pkg/apis/core/v1/conversion.go`** -> AI Confidence: **99.31%**
397. **`pkg/apis/core/v1/helper/helpers.go`** -> AI Confidence: **99.31%**
398. **`pkg/apis/extensions/v1beta1/conversion.go`** -> AI Confidence: **99.31%**
399. **`pkg/apis/node/validation/validation.go`** -> AI Confidence: **99.31%**
400. **`pkg/apis/resource/v1beta1/conversion.go`** -> AI Confidence: **99.31%**
401. **`pkg/apis/resource/validation/validation.go`** -> AI Confidence: **99.31%**
402. **`pkg/apis/storage/validation/validation.go`** -> AI Confidence: **99.31%**
403. **`pkg/auth/authorizer/abac/abac.go`** -> AI Confidence: **99.31%**
404. **`pkg/controller/certificates/cleaner/cleaner.go`** -> AI Confidence: **99.31%**
405. **`pkg/controller/certificates/clustertrustbundlepublisher/metrics.go`** -> AI Confidence: **99.31%**
406. **`pkg/controller/controller_utils.go`** -> AI Confidence: **99.31%**
407. **`pkg/controller/cronjob/cronjob_controllerv2.go`** -> AI Confidence: **99.31%**
408. **`pkg/controller/cronjob/utils.go`** -> AI Confidence: **99.31%**
409. **`pkg/controller/daemon/daemon_controller.go`** -> AI Confidence: **99.31%**
410. **`pkg/controller/daemon/update.go`** -> AI Confidence: **99.31%**
411. **`pkg/controller/daemon/util/daemonset_util.go`** -> AI Confidence: **99.31%**
412. **`pkg/controller/deployment/progress.go`** -> AI Confidence: **99.31%**
413. **`pkg/controller/deployment/rolling.go`** -> AI Confidence: **99.31%**
414. **`pkg/controller/deployment/sync.go`** -> AI Confidence: **99.31%**
415. **`pkg/controller/deployment/util/deployment_util.go`** -> AI Confidence: **99.31%**
416. **`pkg/controller/devicetainteviction/device_taint_eviction.go`** -> AI Confidence: **99.31%**
417. **`pkg/controller/disruption/disruption.go`** -> AI Confidence: **99.31%**
418. **`pkg/controller/garbagecollector/dump.go`** -> AI Confidence: **99.31%**
419. **`pkg/controller/garbagecollector/garbagecollector.go`** -> AI Confidence: **99.31%**
420. **`pkg/controller/garbagecollector/graph_builder.go`** -> AI Confidence: **99.31%**
421. **`pkg/controller/garbagecollector/operations.go`** -> AI Confidence: **99.31%**
422. **`pkg/controller/garbagecollector/patch.go`** -> AI Confidence: **99.31%**
423. **`pkg/controller/job/backoff_utils.go`** -> AI Confidence: **99.31%**
424. **`pkg/controller/job/job_controller.go`** -> AI Confidence: **99.31%**
425. **`pkg/controller/namespace/deletion/namespaced_resources_deleter.go`** -> AI Confidence: **99.31%**
426. **`pkg/controller/nodeipam/ipam/cidrset/cidr_set.go`** -> AI Confidence: **99.31%**
427. **`pkg/controller/nodeipam/ipam/range_allocator.go`** -> AI Confidence: **99.31%**
428. **`pkg/controller/nodelifecycle/node_lifecycle_controller.go`** -> AI Confidence: **99.31%**
429. **`pkg/controller/podautoscaler/horizontal.go`** -> AI Confidence: **99.31%**
430. **`pkg/controller/podautoscaler/metrics/client.go`** -> AI Confidence: **99.31%**
431. **`pkg/controller/podautoscaler/replica_calculator.go`** -> AI Confidence: **99.31%**
432. **`pkg/controller/podgc/gc_controller.go`** -> AI Confidence: **99.31%**
433. **`pkg/controller/replicaset/replica_set.go`** -> AI Confidence: **99.31%**
434. **`pkg/controller/resourceclaim/controller.go`** -> AI Confidence: **99.31%**
435. **`pkg/controller/serviceaccount/legacy_serviceaccount_token_cleaner.go`** -> AI Confidence: **99.31%**
436. **`pkg/controller/servicecidrs/servicecidrs_controller.go`** -> AI Confidence: **99.31%**
437. **`pkg/controller/statefulset/stateful_pod_control.go`** -> AI Confidence: **99.31%**
438. **`pkg/controller/statefulset/stateful_set_control.go`** -> AI Confidence: **99.31%**
439. **`pkg/controller/statefulset/stateful_set_utils.go`** -> AI Confidence: **99.31%**
440. **`pkg/controller/storageversiongc/gc_controller.go`** -> AI Confidence: **99.31%**
441. **`pkg/controller/testutil/test_utils.go`** -> AI Confidence: **99.31%**
442. **`pkg/controller/ttlafterfinished/ttlafterfinished_controller.go`** -> AI Confidence: **99.31%**
443. **`pkg/controller/util/node/controller_utils.go`** -> AI Confidence: **99.31%**
444. **`pkg/controller/volume/attachdetach/attach_detach_controller.go`** -> AI Confidence: **99.31%**
445. **`pkg/controller/volume/attachdetach/metrics/metrics.go`** -> AI Confidence: **99.31%**
446. **`pkg/controller/volume/attachdetach/util/util.go`** -> AI Confidence: **99.31%**
447. **`pkg/controller/volume/persistentvolume/metrics/metrics.go`** -> AI Confidence: **99.31%**
448. **`pkg/controller/volume/persistentvolume/pv_controller.go`** -> AI Confidence: **99.31%**
449. **`pkg/controller/volume/selinuxwarning/cache/volumecache.go`** -> AI Confidence: **99.31%**
450. **`pkg/controlplane/apiserver/aggregator.go`** -> AI Confidence: **99.31%**
451. **`pkg/controlplane/apiserver/config.go`** -> AI Confidence: **99.31%**
452. **`pkg/controlplane/apiserver/options/options.go`** -> AI Confidence: **99.31%**
453. **`pkg/controlplane/apiserver/options/validation.go`** -> AI Confidence: **99.31%**
454. **`pkg/controlplane/controller/defaultservicecidr/default_servicecidr_controller.go`** -> AI Confidence: **99.31%**
455. **`pkg/controlplane/controller/leaderelection/leaderelection_controller.go`** -> AI Confidence: **99.31%**
456. **`pkg/controlplane/controller/leaderelection/leasecandidategc_controller.go`** -> AI Confidence: **99.31%**
457. **`pkg/controlplane/reconcilers/endpointsadapter.go`** -> AI Confidence: **99.31%**
458. **`pkg/controlplane/reconcilers/instancecount.go`** -> AI Confidence: **99.31%**
459. **`pkg/controlplane/reconcilers/lease.go`** -> AI Confidence: **99.31%**
460. **`pkg/credentialprovider/keyring.go`** -> AI Confidence: **99.31%**
461. **`pkg/fieldpath/fieldpath.go`** -> AI Confidence: **99.31%**
462. **`pkg/kubeapiserver/authenticator/config.go`** -> AI Confidence: **99.31%**
463. **`pkg/kubeapiserver/authorizer/config.go`** -> AI Confidence: **99.31%**
464. **`pkg/kubeapiserver/options/authentication.go`** -> AI Confidence: **99.31%**
465. **`pkg/kubeapiserver/options/authorization.go`** -> AI Confidence: **99.31%**
466. **`pkg/kubectl/cmd/convert/convert.go`** -> AI Confidence: **99.31%**
467. **`pkg/kubelet/allocation/allocation_manager.go`** -> AI Confidence: **99.31%**
468. **`pkg/kubelet/allocation/handlers.go`** -> AI Confidence: **99.31%**
469. **`pkg/kubelet/apis/podresources/server_v1.go`** -> AI Confidence: **99.31%**
470. **`pkg/kubelet/certificate/bootstrap/bootstrap.go`** -> AI Confidence: **99.31%**
471. **`pkg/kubelet/certificate/transport.go`** -> AI Confidence: **99.31%**
472. **`pkg/kubelet/cm/cgroup_manager_linux.go`** -> AI Confidence: **99.31%**
473. **`pkg/kubelet/cm/cgroup_v1_manager_linux.go`** -> AI Confidence: **99.31%**
474. **`pkg/kubelet/cm/container_manager.go`** -> AI Confidence: **99.31%**
475. **`pkg/kubelet/cm/container_manager_linux.go`** -> AI Confidence: **99.31%**
476. **`pkg/kubelet/cm/cpumanager/cpu_assignment.go`** -> AI Confidence: **99.31%**
477. **`pkg/kubelet/cm/cpumanager/cpu_manager.go`** -> AI Confidence: **99.31%**
478. **`pkg/kubelet/cm/cpumanager/policy_options.go`** -> AI Confidence: **99.31%**
479. **`pkg/kubelet/cm/cpumanager/policy_static.go`** -> AI Confidence: **99.31%**
480. **`pkg/kubelet/cm/devicemanager/manager.go`** -> AI Confidence: **99.31%**
481. **`pkg/kubelet/cm/devicemanager/pod_devices.go`** -> AI Confidence: **99.31%**
482. **`pkg/kubelet/cm/devicemanager/topology_hints.go`** -> AI Confidence: **99.31%**
483. **`pkg/kubelet/cm/dra/claiminfo.go`** -> AI Confidence: **99.31%**
484. **`pkg/kubelet/cm/dra/healthinfo.go`** -> AI Confidence: **99.31%**
485. **`pkg/kubelet/cm/dra/manager.go`** -> AI Confidence: **99.31%**
486. **`pkg/kubelet/cm/dra/plugin/dra_plugin_manager.go`** -> AI Confidence: **99.31%**
487. **`pkg/kubelet/cm/helpers_linux.go`** -> AI Confidence: **99.31%**
488. **`pkg/kubelet/cm/internal_container_lifecycle_windows.go`** -> AI Confidence: **99.31%**
489. **`pkg/kubelet/cm/memorymanager/memory_manager.go`** -> AI Confidence: **99.31%**
490. **`pkg/kubelet/cm/memorymanager/policy_static.go`** -> AI Confidence: **99.31%**
491. **`pkg/kubelet/cm/node_container_manager_linux.go`** -> AI Confidence: **99.31%**
492. **`pkg/kubelet/cm/pod_container_manager_linux.go`** -> AI Confidence: **99.31%**
493. **`pkg/kubelet/cm/qos_container_manager_linux.go`** -> AI Confidence: **99.31%**
494. **`pkg/kubelet/config/common.go`** -> AI Confidence: **99.31%**
495. **`pkg/kubelet/config/config.go`** -> AI Confidence: **99.31%**
496. **`pkg/kubelet/config/file.go`** -> AI Confidence: **99.31%**
497. **`pkg/kubelet/config/file_linux.go`** -> AI Confidence: **99.31%**
498. **`pkg/kubelet/container/helpers.go`** -> AI Confidence: **99.31%**
499. **`pkg/kubelet/eviction/eviction_manager.go`** -> AI Confidence: **99.31%**
500. **`pkg/kubelet/eviction/helpers.go`** -> AI Confidence: **99.31%**
501. **`pkg/kubelet/eviction/memory_threshold_notifier_others.go`** -> AI Confidence: **99.31%**
502. **`pkg/kubelet/images/image_gc_manager.go`** -> AI Confidence: **99.31%**
503. **`pkg/kubelet/images/image_manager.go`** -> AI Confidence: **99.31%**
504. **`pkg/kubelet/images/metrics.go`** -> AI Confidence: **99.31%**
505. **`pkg/kubelet/images/pullmanager/image_pull_manager.go`** -> AI Confidence: **99.31%**
506. **`pkg/kubelet/kubelet_pods.go`** -> AI Confidence: **99.31%**
507. **`pkg/kubelet/kubelet_server_journal_linux.go`** -> AI Confidence: **99.31%**
508. **`pkg/kubelet/kuberuntime/helpers.go`** -> AI Confidence: **99.31%**
509. **`pkg/kubelet/kuberuntime/kuberuntime_container.go`** -> AI Confidence: **99.31%**
510. **`pkg/kubelet/kuberuntime/kuberuntime_container_linux.go`** -> AI Confidence: **99.31%**
511. **`pkg/kubelet/kuberuntime/kuberuntime_gc.go`** -> AI Confidence: **99.31%**
512. **`pkg/kubelet/kuberuntime/kuberuntime_image.go`** -> AI Confidence: **99.31%**
513. **`pkg/kubelet/kuberuntime/kuberuntime_manager.go`** -> AI Confidence: **99.31%**
514. **`pkg/kubelet/kuberuntime/kuberuntime_sandbox.go`** -> AI Confidence: **99.31%**
515. **`pkg/kubelet/kuberuntime/security_context_others.go`** -> AI Confidence: **99.31%**
516. **`pkg/kubelet/kuberuntime/security_context_windows.go`** -> AI Confidence: **99.31%**
517. **`pkg/kubelet/lifecycle/handlers.go`** -> AI Confidence: **99.31%**
518. **`pkg/kubelet/lifecycle/predicate.go`** -> AI Confidence: **99.31%**
519. **`pkg/kubelet/metrics/collectors/log_metrics.go`** -> AI Confidence: **99.31%**
520. **`pkg/kubelet/metrics/collectors/resource_metrics.go`** -> AI Confidence: **99.31%**
521. **`pkg/kubelet/network/dns/dns.go`** -> AI Confidence: **99.31%**
522. **`pkg/kubelet/nodeshutdown/nodeshutdown_manager.go`** -> AI Confidence: **99.31%**
523. **`pkg/kubelet/nodeshutdown/nodeshutdown_manager_linux.go`** -> AI Confidence: **99.31%**
524. **`pkg/kubelet/nodeshutdown/nodeshutdown_manager_windows.go`** -> AI Confidence: **99.31%**
525. **`pkg/kubelet/pleg/evented.go`** -> AI Confidence: **99.31%**
526. **`pkg/kubelet/pleg/generic.go`** -> AI Confidence: **99.31%**
527. **`pkg/kubelet/pluginmanager/reconciler/reconciler.go`** -> AI Confidence: **99.31%**
528. **`pkg/kubelet/pod_workers.go`** -> AI Confidence: **99.31%**
529. **`pkg/kubelet/podcertificate/podcertificatemanager.go`** -> AI Confidence: **99.31%**
530. **`pkg/kubelet/preemption/preemption.go`** -> AI Confidence: **99.31%**
531. **`pkg/kubelet/prober/prober_manager.go`** -> AI Confidence: **99.31%**
532. **`pkg/kubelet/server/server.go`** -> AI Confidence: **99.31%**
533. **`pkg/kubelet/server/stats/handler.go`** -> AI Confidence: **99.31%**
534. **`pkg/kubelet/server/stats/summary_sys_containers.go`** -> AI Confidence: **99.31%**
535. **`pkg/kubelet/server/stats/summary_sys_containers_windows.go`** -> AI Confidence: **99.31%**
536. **`pkg/kubelet/server/stats/volume_stat_calculator.go`** -> AI Confidence: **99.31%**
537. **`pkg/kubelet/stats/cadvisor_stats_provider.go`** -> AI Confidence: **99.31%**
538. **`pkg/kubelet/stats/cri_stats_provider.go`** -> AI Confidence: **99.31%**
539. **`pkg/kubelet/stats/cri_stats_provider_linux.go`** -> AI Confidence: **99.31%**
540. **`pkg/kubelet/stats/cri_stats_provider_windows.go`** -> AI Confidence: **99.31%**
541. **`pkg/kubelet/stats/helper.go`** -> AI Confidence: **99.31%**
542. **`pkg/kubelet/stats/pidlimit/pidlimit_linux.go`** -> AI Confidence: **99.31%**
543. **`pkg/kubelet/status/generate.go`** -> AI Confidence: **99.31%**
544. **`pkg/kubelet/status/status_manager.go`** -> AI Confidence: **99.31%**
545. **`pkg/kubelet/token/token_manager.go`** -> AI Confidence: **99.31%**
546. **`pkg/kubelet/types/pod_update.go`** -> AI Confidence: **99.31%**
547. **`pkg/kubelet/util/boottime_util_linux.go`** -> AI Confidence: **99.31%**
548. **`pkg/kubelet/util/manager/cache_based_manager.go`** -> AI Confidence: **99.31%**
549. **`pkg/kubelet/volumemanager/cache/desired_state_of_world.go`** -> AI Confidence: **99.31%**
550. **`pkg/kubelet/volumemanager/populator/desired_state_of_world_populator.go`** -> AI Confidence: **99.31%**
551. **`pkg/kubelet/volumemanager/volume_manager.go`** -> AI Confidence: **99.31%**
552. **`pkg/printers/internalversion/printers.go`** -> AI Confidence: **99.31%**
553. **`pkg/probe/http/request.go`** -> AI Confidence: **99.31%**
554. **`pkg/proxy/endpointschangetracker.go`** -> AI Confidence: **99.31%**
555. **`pkg/proxy/endpointslicecache.go`** -> AI Confidence: **99.31%**
556. **`pkg/proxy/healthcheck/service_health.go`** -> AI Confidence: **99.31%**
557. **`pkg/proxy/ipvs/ipset/ipset.go`** -> AI Confidence: **99.31%**
558. **`pkg/proxy/metrics/metrics.go`** -> AI Confidence: **99.31%**
559. **`pkg/proxy/util/nfacct/nfacct_linux.go`** -> AI Confidence: **99.31%**
560. **`pkg/proxy/winkernel/proxier.go`** -> AI Confidence: **99.31%**
561. **`pkg/quota/v1/evaluator/core/persistent_volume_claims.go`** -> AI Confidence: **99.31%**
562. **`pkg/quota/v1/evaluator/core/pods.go`** -> AI Confidence: **99.31%**
563. **`pkg/quota/v1/evaluator/core/registry.go`** -> AI Confidence: **99.31%**
564. **`pkg/quota/v1/evaluator/core/resource_claims.go`** -> AI Confidence: **99.31%**
565. **`pkg/quota/v1/install/update_filter.go`** -> AI Confidence: **99.31%**
566. **`pkg/registry/admissionregistration/mutatingadmissionpolicy/authz.go`** -> AI Confidence: **99.31%**
567. **`pkg/registry/admissionregistration/mutatingadmissionpolicybinding/authz.go`** -> AI Confidence: **99.31%**
568. **`pkg/registry/admissionregistration/rest/storage_apiserver.go`** -> AI Confidence: **99.31%**
569. **`pkg/registry/admissionregistration/validatingadmissionpolicy/authz.go`** -> AI Confidence: **99.31%**
570. **`pkg/registry/admissionregistration/validatingadmissionpolicybinding/authz.go`** -> AI Confidence: **99.31%**
571. **`pkg/registry/authentication/tokenreview/storage.go`** -> AI Confidence: **99.31%**
572. **`pkg/registry/autoscaling/horizontalpodautoscaler/strategy.go`** -> AI Confidence: **99.31%**
573. **`pkg/registry/batch/job/strategy.go`** -> AI Confidence: **99.31%**
574. **`pkg/registry/certificates/rest/storage_certificates.go`** -> AI Confidence: **99.31%**
575. **`pkg/registry/core/node/strategy.go`** -> AI Confidence: **99.31%**
576. **`pkg/registry/core/pod/storage/eviction.go`** -> AI Confidence: **99.31%**
577. **`pkg/registry/core/pod/strategy.go`** -> AI Confidence: **99.31%**
578. **`pkg/registry/core/rest/storage_core_generic.go`** -> AI Confidence: **99.31%**
579. **`pkg/registry/core/service/ipallocator/cidrallocator.go`** -> AI Confidence: **99.31%**
580. **`pkg/registry/core/service/ipallocator/controller/repair.go`** -> AI Confidence: **99.31%**
581. **`pkg/registry/core/service/ipallocator/controller/repairip.go`** -> AI Confidence: **99.31%**
582. **`pkg/registry/core/service/ipallocator/ipallocator.go`** -> AI Confidence: **99.31%**
583. **`pkg/registry/core/service/portallocator/controller/repair.go`** -> AI Confidence: **99.31%**
584. **`pkg/registry/core/service/storage/alloc.go`** -> AI Confidence: **99.31%**
585. **`pkg/registry/core/service/storage/storage.go`** -> AI Confidence: **99.31%**
586. **`pkg/registry/discovery/endpointslice/strategy.go`** -> AI Confidence: **99.31%**
587. **`pkg/registry/networking/networkpolicy/strategy.go`** -> AI Confidence: **99.31%**
588. **`pkg/registry/networking/rest/storage_settings.go`** -> AI Confidence: **99.31%**
589. **`pkg/registry/rbac/escalation_check.go`** -> AI Confidence: **99.31%**
590. **`pkg/registry/rbac/rest/storage_rbac.go`** -> AI Confidence: **99.31%**
591. **`pkg/registry/rbac/validation/rule.go`** -> AI Confidence: **99.31%**
592. **`pkg/registry/resource/resourceclaim/strategy.go`** -> AI Confidence: **99.31%**
593. **`pkg/registry/resource/resourceslice/strategy.go`** -> AI Confidence: **99.31%**
594. **`pkg/registry/resource/rest/storage_resource.go`** -> AI Confidence: **99.31%**
595. **`pkg/registry/scheduling/rest/storage_scheduling.go`** -> AI Confidence: **99.31%**
596. **`pkg/registry/storage/csidriver/strategy.go`** -> AI Confidence: **99.31%**
597. **`pkg/registry/storage/rest/storage_storage.go`** -> AI Confidence: **99.31%**
598. **`pkg/scheduler/apis/config/v1/conversion.go`** -> AI Confidence: **99.31%**
599. **`pkg/scheduler/backend/cache/debugger/comparer.go`** -> AI Confidence: **99.31%**
600. **`pkg/scheduler/backend/cache/debugger/dumper.go`** -> AI Confidence: **99.31%**
601. **`pkg/scheduler/backend/cache/snapshot.go`** -> AI Confidence: **99.31%**
602. **`pkg/scheduler/backend/queue/scheduling_queue.go`** -> AI Confidence: **99.31%**
603. **`pkg/scheduler/eventhandlers.go`** -> AI Confidence: **99.31%**
604. **`pkg/scheduler/extender.go`** -> AI Confidence: **99.31%**
605. **`pkg/scheduler/framework/plugins/defaultpreemption/default_preemption.go`** -> AI Confidence: **99.31%**
606. **`pkg/scheduler/framework/plugins/dynamicresources/allocateddevices.go`** -> AI Confidence: **99.31%**
607. **`pkg/scheduler/framework/plugins/dynamicresources/dynamicresources.go`** -> AI Confidence: **99.31%**
608. **`pkg/scheduler/framework/plugins/dynamicresources/extendeddynamicresources.go`** -> AI Confidence: **99.31%**
609. **`pkg/scheduler/framework/plugins/interpodaffinity/filtering.go`** -> AI Confidence: **99.31%**
610. **`pkg/scheduler/framework/plugins/interpodaffinity/plugin.go`** -> AI Confidence: **99.31%**
611. **`pkg/scheduler/framework/plugins/interpodaffinity/scoring.go`** -> AI Confidence: **99.31%**
612. **`pkg/scheduler/framework/plugins/noderesources/resource_allocation.go`** -> AI Confidence: **99.31%**
613. **`pkg/scheduler/framework/plugins/nodevolumelimits/csi.go`** -> AI Confidence: **99.31%**
614. **`pkg/scheduler/framework/plugins/podtopologyspread/common.go`** -> AI Confidence: **99.31%**
615. **`pkg/scheduler/framework/plugins/podtopologyspread/filtering.go`** -> AI Confidence: **99.31%**
616. **`pkg/scheduler/framework/plugins/volumebinding/binder.go`** -> AI Confidence: **99.31%**
617. **`pkg/scheduler/framework/plugins/volumebinding/volume_binding.go`** -> AI Confidence: **99.31%**
618. **`pkg/scheduler/framework/plugins/volumezone/volume_zone.go`** -> AI Confidence: **99.31%**
619. **`pkg/scheduler/framework/preemption/executor.go`** -> AI Confidence: **99.31%**
620. **`pkg/scheduler/framework/preemption/preemption.go`** -> AI Confidence: **99.31%**
621. **`pkg/scheduler/framework/types.go`** -> AI Confidence: **99.31%**
622. **`pkg/scheduler/metrics/resources/resources.go`** -> AI Confidence: **99.31%**
623. **`pkg/scheduler/schedule_one.go`** -> AI Confidence: **99.31%**
624. **`pkg/scheduler/scheduler.go`** -> AI Confidence: **99.31%**
625. **`pkg/scheduler/testing/framework/fake_extender.go`** -> AI Confidence: **99.31%**
626. **`pkg/scheduler/testing/framework/fake_listers.go`** -> AI Confidence: **99.31%**
627. **`pkg/scheduler/util/utils.go`** -> AI Confidence: **99.31%**
628. **`pkg/securitycontext/util.go`** -> AI Confidence: **99.31%**
629. **`pkg/serviceaccount/claims.go`** -> AI Confidence: **99.31%**
630. **`pkg/serviceaccount/externaljwt/plugin/keycache.go`** -> AI Confidence: **99.31%**
631. **`pkg/serviceaccount/openidmetadata.go`** -> AI Confidence: **99.31%**
632. **`pkg/util/filesystem/util_windows.go`** -> AI Confidence: **99.31%**
633. **`pkg/util/oom/oom_linux.go`** -> AI Confidence: **99.31%**
634. **`pkg/util/pod/pod.go`** -> AI Confidence: **99.31%**
635. **`pkg/util/procfs/procfs_linux.go`** -> AI Confidence: **99.31%**
636. **`pkg/volume/csi/csi_attacher.go`** -> AI Confidence: **99.31%**
637. **`pkg/volume/csi/csi_block.go`** -> AI Confidence: **99.31%**
638. **`pkg/volume/csi/csi_mounter.go`** -> AI Confidence: **99.31%**
639. **`pkg/volume/csi/testing/testing.go`** -> AI Confidence: **99.31%**
640. **`pkg/volume/emptydir/empty_dir.go`** -> AI Confidence: **99.31%**
641. **`pkg/volume/emptydir/empty_dir_linux.go`** -> AI Confidence: **99.31%**
642. **`pkg/volume/fc/fc_util.go`** -> AI Confidence: **99.31%**
643. **`pkg/volume/flexvolume/probe.go`** -> AI Confidence: **99.31%**
644. **`pkg/volume/flexvolume/util.go`** -> AI Confidence: **99.31%**
645. **`pkg/volume/iscsi/iscsi_util.go`** -> AI Confidence: **99.31%**
646. **`pkg/volume/projected/projected.go`** -> AI Confidence: **99.31%**
647. **`pkg/volume/util/atomic_writer.go`** -> AI Confidence: **99.31%**
648. **`pkg/volume/util/device_util_linux.go`** -> AI Confidence: **99.31%**
649. **`pkg/volume/util/fsquota/project.go`** -> AI Confidence: **99.31%**
650. **`pkg/volume/util/fsquota/quota_linux.go`** -> AI Confidence: **99.31%**
651. **`pkg/volume/util/metrics.go`** -> AI Confidence: **99.31%**
652. **`pkg/volume/util/nestedpendingoperations/nestedpendingoperations.go`** -> AI Confidence: **99.31%**
653. **`pkg/volume/util/operationexecutor/operation_generator.go`** -> AI Confidence: **99.31%**
654. **`pkg/volume/util/subpath/subpath_linux.go`** -> AI Confidence: **99.31%**
655. **`pkg/volume/util/subpath/subpath_windows.go`** -> AI Confidence: **99.31%**
656. **`pkg/volume/util/util.go`** -> AI Confidence: **99.31%**
657. **`pkg/volume/util/volumepathhandler/volume_path_handler_linux.go`** -> AI Confidence: **99.31%**
658. **`pkg/volume/volume_linux.go`** -> AI Confidence: **99.31%**
659. **`plugin/pkg/admission/alwayspullimages/admission.go`** -> AI Confidence: **99.31%**
660. **`plugin/pkg/admission/antiaffinity/admission.go`** -> AI Confidence: **99.31%**
661. **`plugin/pkg/admission/defaulttolerationseconds/admission.go`** -> AI Confidence: **99.31%**
662. **`plugin/pkg/admission/extendedresourcetoleration/admission.go`** -> AI Confidence: **99.31%**
663. **`plugin/pkg/admission/noderestriction/admission.go`** -> AI Confidence: **99.31%**
664. **`plugin/pkg/admission/priority/admission.go`** -> AI Confidence: **99.31%**
665. **`plugin/pkg/admission/runtimeclass/admission.go`** -> AI Confidence: **99.31%**
666. **`plugin/pkg/admission/security/podsecurity/admission.go`** -> AI Confidence: **99.31%**
667. **`plugin/pkg/admission/serviceaccount/admission.go`** -> AI Confidence: **99.31%**
668. **`plugin/pkg/auth/authorizer/node/node_authorizer.go`** -> AI Confidence: **99.31%**
669. **`plugin/pkg/auth/authorizer/rbac/bootstrappolicy/controller_policy.go`** -> AI Confidence: **99.31%**
670. **`plugin/pkg/auth/authorizer/rbac/bootstrappolicy/policy.go`** -> AI Confidence: **99.31%**
671. **`staging/src/k8s.io/api/coordination/v1/generated.pb.go`** -> AI Confidence: **99.31%**
672. **`staging/src/k8s.io/api/coordination/v1alpha2/generated.pb.go`** -> AI Confidence: **99.31%**
673. **`staging/src/k8s.io/api/extensions/v1beta1/zz_generated.validations.go`** -> AI Confidence: **99.31%**
674. **`staging/src/k8s.io/api/scheduling/v1/generated.pb.go`** -> AI Confidence: **99.31%**
675. **`staging/src/k8s.io/api/scheduling/v1beta1/generated.pb.go`** -> AI Confidence: **99.31%**
676. **`staging/src/k8s.io/api/storagemigration/v1beta1/generated.pb.go`** -> AI Confidence: **99.31%**
677. **`staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/validation/validation.go`** -> AI Confidence: **99.31%**
678. **`staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/conversion/converter.go`** -> AI Confidence: **99.31%**
679. **`staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/conversion/webhook_converter.go`** -> AI Confidence: **99.31%**
680. **`staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/customresource_discovery_controller.go`** -> AI Confidence: **99.31%**
681. **`staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/customresource_discovery_controller_test.go`** -> AI Confidence: **99.31%**
682. **`staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/cel/validation.go`** -> AI Confidence: **99.31%**
683. **`staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/defaulting/prunenulls_test.go`** -> AI Confidence: **99.31%**
684. **`staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/kubeopenapi_test.go`** -> AI Confidence: **99.31%**
685. **`staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/objectmeta/coerce.go`** -> AI Confidence: **99.31%**
686. **`staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/validation/formats.go`** -> AI Confidence: **99.31%**
687. **`staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/validation/validation.go`** -> AI Confidence: **99.31%**
688. **`staging/src/k8s.io/apiextensions-apiserver/pkg/client/applyconfiguration/utils.go`** -> AI Confidence: **99.31%**
689. **`staging/src/k8s.io/apiextensions-apiserver/pkg/controller/nonstructuralschema/nonstructuralschema_controller.go`** -> AI Confidence: **99.31%**
690. **`staging/src/k8s.io/apiextensions-apiserver/pkg/controller/openapi/builder/builder.go`** -> AI Confidence: **99.31%**
691. **`staging/src/k8s.io/apiextensions-apiserver/pkg/controller/openapi/v2/conversion_test.go`** -> AI Confidence: **99.31%**
692. **`staging/src/k8s.io/apiextensions-apiserver/pkg/controller/openapiv3/controller.go`** -> AI Confidence: **99.31%**
693. **`staging/src/k8s.io/apiextensions-apiserver/pkg/controller/status/naming_controller.go`** -> AI Confidence: **99.31%**
694. **`staging/src/k8s.io/apiextensions-apiserver/pkg/registry/customresource/etcd_test.go`** -> AI Confidence: **99.31%**
695. **`staging/src/k8s.io/apiextensions-apiserver/pkg/registry/customresource/strategy.go`** -> AI Confidence: **99.31%**
696. **`staging/src/k8s.io/apiextensions-apiserver/pkg/registry/customresource/tableconvertor/tableconvertor.go`** -> AI Confidence: **99.31%**
697. **`staging/src/k8s.io/apiextensions-apiserver/pkg/registry/customresource/validator.go`** -> AI Confidence: **99.31%**
698. **`staging/src/k8s.io/apiextensions-apiserver/pkg/registry/customresourcedefinition/strategy.go`** -> AI Confidence: **99.31%**
699. **`staging/src/k8s.io/apiextensions-apiserver/pkg/test/cel.go`** -> AI Confidence: **99.31%**
700. **`staging/src/k8s.io/apiextensions-apiserver/pkg/test/pattern.go`** -> AI Confidence: **99.31%**
701. **`staging/src/k8s.io/apiextensions-apiserver/test/integration/apiapproval_test.go`** -> AI Confidence: **99.31%**
702. **`staging/src/k8s.io/apiextensions-apiserver/test/integration/cabundle_test.go`** -> AI Confidence: **99.31%**
703. **`staging/src/k8s.io/apiextensions-apiserver/test/integration/cbor_test.go`** -> AI Confidence: **99.31%**
704. **`staging/src/k8s.io/apiextensions-apiserver/test/integration/change_test.go`** -> AI Confidence: **99.31%**
705. **`staging/src/k8s.io/apiextensions-apiserver/test/integration/conversion/conversion_test.go`** -> AI Confidence: **99.31%**
706. **`staging/src/k8s.io/apiextensions-apiserver/test/integration/conversion/webhook.go`** -> AI Confidence: **99.31%**
707. **`staging/src/k8s.io/apiextensions-apiserver/test/integration/defaulting_test.go`** -> AI Confidence: **99.31%**
708. **`staging/src/k8s.io/apiextensions-apiserver/test/integration/deprecation_test.go`** -> AI Confidence: **99.31%**
709. **`staging/src/k8s.io/apiextensions-apiserver/test/integration/fieldselector_test.go`** -> AI Confidence: **99.31%**
710. **`staging/src/k8s.io/apiextensions-apiserver/test/integration/finalization_test.go`** -> AI Confidence: **99.31%**
711. **`staging/src/k8s.io/apiextensions-apiserver/test/integration/helpers.go`** -> AI Confidence: **99.31%**
712. **`staging/src/k8s.io/apiextensions-apiserver/test/integration/pruning_test.go`** -> AI Confidence: **99.31%**
713. **`staging/src/k8s.io/apiextensions-apiserver/test/integration/scope_test.go`** -> AI Confidence: **99.31%**
714. **`staging/src/k8s.io/apiextensions-apiserver/test/integration/versioning_test.go`** -> AI Confidence: **99.31%**
715. **`staging/src/k8s.io/apimachinery/pkg/api/apitesting/codec.go`** -> AI Confidence: **99.31%**
716. **`staging/src/k8s.io/apimachinery/pkg/api/apitesting/naming/naming.go`** -> AI Confidence: **99.31%**
717. **`staging/src/k8s.io/apimachinery/pkg/api/apitesting/roundtrip/construct.go`** -> AI Confidence: **99.31%**
718. **`staging/src/k8s.io/apimachinery/pkg/api/apitesting/roundtrip/roundtrip.go`** -> AI Confidence: **99.31%**
719. **`staging/src/k8s.io/apimachinery/pkg/api/meta/meta_test.go`** -> AI Confidence: **99.31%**
720. **`staging/src/k8s.io/apimachinery/pkg/api/meta/restmapper.go`** -> AI Confidence: **99.31%**
721. **`staging/src/k8s.io/apimachinery/pkg/api/resource/quantity_test.go`** -> AI Confidence: **99.31%**
722. **`staging/src/k8s.io/apimachinery/pkg/api/validation/objectmeta.go`** -> AI Confidence: **99.31%**
723. **`staging/src/k8s.io/apimachinery/pkg/apis/meta/fuzzer/fuzzer.go`** -> AI Confidence: **99.31%**
724. **`staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/helpers.go`** -> AI Confidence: **99.31%**
725. **`staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/helpers_test.go`** -> AI Confidence: **99.31%**
726. **`staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/unstructured/unstructured_test.go`** -> AI Confidence: **99.31%**
727. **`staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/validation/validation.go`** -> AI Confidence: **99.31%**
728. **`staging/src/k8s.io/apimachinery/pkg/apis/meta/v1beta1/generated.pb.go`** -> AI Confidence: **99.31%**
729. **`staging/src/k8s.io/apimachinery/pkg/runtime/extension_test.go`** -> AI Confidence: **99.31%**
730. **`staging/src/k8s.io/apimachinery/pkg/runtime/scheme.go`** -> AI Confidence: **99.31%**
731. **`staging/src/k8s.io/apimachinery/pkg/runtime/scheme_test.go`** -> AI Confidence: **99.31%**
732. **`staging/src/k8s.io/apimachinery/pkg/runtime/serializer/cbor/internal/modes/encode_test.go`** -> AI Confidence: **99.31%**
733. **`staging/src/k8s.io/apimachinery/pkg/runtime/serializer/encoder_with_allocator_test.go`** -> AI Confidence: **99.31%**
734. **`staging/src/k8s.io/apimachinery/pkg/runtime/serializer/json/collections.go`** -> AI Confidence: **99.31%**
735. **`staging/src/k8s.io/apimachinery/pkg/runtime/serializer/protobuf/collections_test.go`** -> AI Confidence: **99.31%**
736. **`staging/src/k8s.io/apimachinery/pkg/runtime/serializer/protobuf/protobuf_test.go`** -> AI Confidence: **99.31%**
737. **`staging/src/k8s.io/apimachinery/pkg/runtime/serializer/streaming/streaming_test.go`** -> AI Confidence: **99.31%**
738. **`staging/src/k8s.io/apimachinery/pkg/runtime/serializer/versioning/versioning.go`** -> AI Confidence: **99.31%**
739. **`staging/src/k8s.io/apimachinery/pkg/runtime/serializer/versioning/versioning_test.go`** -> AI Confidence: **99.31%**
740. **`staging/src/k8s.io/apimachinery/pkg/runtime/swagger_doc_generator.go`** -> AI Confidence: **99.31%**
741. **`staging/src/k8s.io/apimachinery/pkg/test/api_meta_help_test.go`** -> AI Confidence: **99.31%**
742. **`staging/src/k8s.io/apimachinery/pkg/test/api_meta_meta_test.go`** -> AI Confidence: **99.31%**
743. **`staging/src/k8s.io/apimachinery/pkg/util/errors/errors_test.go`** -> AI Confidence: **99.31%**
744. **`staging/src/k8s.io/apimachinery/pkg/util/httpstream/spdy/roundtripper.go`** -> AI Confidence: **99.31%**
745. **`staging/src/k8s.io/apimachinery/pkg/util/httpstream/spdy/roundtripper_test.go`** -> AI Confidence: **99.31%**
746. **`staging/src/k8s.io/apimachinery/pkg/util/httpstream/wsstream/conn_test.go`** -> AI Confidence: **99.31%**
747. **`staging/src/k8s.io/apimachinery/pkg/util/httpstream/wsstream/stream_test.go`** -> AI Confidence: **99.31%**
748. **`staging/src/k8s.io/apimachinery/pkg/util/json/json_test.go`** -> AI Confidence: **99.31%**
749. **`staging/src/k8s.io/apimachinery/pkg/util/managedfields/extract.go`** -> AI Confidence: **99.31%**
750. **`staging/src/k8s.io/apimachinery/pkg/util/managedfields/fieldmanager_test.go`** -> AI Confidence: **99.31%**
751. **`staging/src/k8s.io/apimachinery/pkg/util/managedfields/internal/capmanagers_test.go`** -> AI Confidence: **99.31%**
752. **`staging/src/k8s.io/apimachinery/pkg/util/managedfields/internal/conflict.go`** -> AI Confidence: **99.31%**
753. **`staging/src/k8s.io/apimachinery/pkg/util/managedfields/internal/conflict_test.go`** -> AI Confidence: **99.31%**
754. **`staging/src/k8s.io/apimachinery/pkg/util/managedfields/internal/fieldmanager_test.go`** -> AI Confidence: **99.31%**
755. **`staging/src/k8s.io/apimachinery/pkg/util/managedfields/internal/lastappliedmanager_test.go`** -> AI Confidence: **99.31%**
756. **`staging/src/k8s.io/apimachinery/pkg/util/managedfields/internal/managedfieldsupdater_test.go`** -> AI Confidence: **99.31%**
757. **`staging/src/k8s.io/apimachinery/pkg/util/managedfields/internal/pathelement.go`** -> AI Confidence: **99.31%**
758. **`staging/src/k8s.io/apimachinery/pkg/util/managedfields/internal/skipnonapplied_test.go`** -> AI Confidence: **99.31%**
759. **`staging/src/k8s.io/apimachinery/pkg/util/managedfields/internal/typeconverter.go`** -> AI Confidence: **99.31%**
760. **`staging/src/k8s.io/apimachinery/pkg/util/managedfields/scalehandler.go`** -> AI Confidence: **99.31%**
761. **`staging/src/k8s.io/apimachinery/pkg/util/net/http.go`** -> AI Confidence: **99.31%**
762. **`staging/src/k8s.io/apimachinery/pkg/util/net/interface.go`** -> AI Confidence: **99.31%**
763. **`staging/src/k8s.io/apimachinery/pkg/util/net/interface_test.go`** -> AI Confidence: **99.31%**
764. **`staging/src/k8s.io/apimachinery/pkg/util/proxy/dial.go`** -> AI Confidence: **99.31%**
765. **`staging/src/k8s.io/apimachinery/pkg/util/proxy/transport.go`** -> AI Confidence: **99.31%**
766. **`staging/src/k8s.io/apimachinery/pkg/util/proxy/transport_test.go`** -> AI Confidence: **99.31%**
767. **`staging/src/k8s.io/apimachinery/pkg/util/proxy/upgradeaware.go`** -> AI Confidence: **99.31%**
768. **`staging/src/k8s.io/apimachinery/pkg/util/proxy/upgradeaware_test.go`** -> AI Confidence: **99.31%**
769. **`staging/src/k8s.io/apimachinery/pkg/util/strategicpatch/patch.go`** -> AI Confidence: **99.31%**
770. **`staging/src/k8s.io/apimachinery/pkg/util/validation/field/errors.go`** -> AI Confidence: **99.31%**
771. **`staging/src/k8s.io/apimachinery/pkg/util/validation/ip.go`** -> AI Confidence: **99.31%**
772. **`staging/src/k8s.io/apimachinery/pkg/util/version/version.go`** -> AI Confidence: **99.31%**
773. **`staging/src/k8s.io/apimachinery/pkg/util/wait/loop_test.go`** -> AI Confidence: **99.31%**
774. **`staging/src/k8s.io/apimachinery/pkg/util/yaml/stream_reader_test.go`** -> AI Confidence: **99.31%**
775. **`staging/src/k8s.io/apimachinery/pkg/watch/mux_test.go`** -> AI Confidence: **99.31%**
776. **`staging/src/k8s.io/apimachinery/pkg/watch/streamwatcher_test.go`** -> AI Confidence: **99.31%**
777. **`staging/src/k8s.io/apiserver/pkg/admission/config.go`** -> AI Confidence: **99.31%**
778. **`staging/src/k8s.io/apiserver/pkg/admission/configuration/mutating_webhook_manager_test.go`** -> AI Confidence: **99.31%**
779. **`staging/src/k8s.io/apiserver/pkg/admission/configuration/validating_webhook_manager_test.go`** -> AI Confidence: **99.31%**
780. **`staging/src/k8s.io/apiserver/pkg/admission/plugin/cel/activation.go`** -> AI Confidence: **99.31%**
781. **`staging/src/k8s.io/apiserver/pkg/admission/plugin/cel/compile_test.go`** -> AI Confidence: **99.31%**
782. **`staging/src/k8s.io/apiserver/pkg/admission/plugin/namespace/lifecycle/admission_test.go`** -> AI Confidence: **99.31%**
783. **`staging/src/k8s.io/apiserver/pkg/admission/plugin/policy/generic/policy_dispatcher.go`** -> AI Confidence: **99.31%**
784. **`staging/src/k8s.io/apiserver/pkg/admission/plugin/policy/matching/matching.go`** -> AI Confidence: **99.31%**
785. **`staging/src/k8s.io/apiserver/pkg/admission/plugin/policy/mutating/compilation_test.go`** -> AI Confidence: **99.31%**
786. **`staging/src/k8s.io/apiserver/pkg/admission/plugin/policy/mutating/dispatcher.go`** -> AI Confidence: **99.31%**
787. **`staging/src/k8s.io/apiserver/pkg/admission/plugin/policy/mutating/dispatcher_test.go`** -> AI Confidence: **99.31%**
788. **`staging/src/k8s.io/apiserver/pkg/admission/plugin/policy/mutating/metrics/metrics_test.go`** -> AI Confidence: **99.31%**
789. **`staging/src/k8s.io/apiserver/pkg/admission/plugin/policy/mutating/patch/smd_test.go`** -> AI Confidence: **99.31%**
790. **`staging/src/k8s.io/apiserver/pkg/admission/plugin/policy/mutating/patch/typeconverter_test.go`** -> AI Confidence: **99.31%**
791. **`staging/src/k8s.io/apiserver/pkg/admission/plugin/policy/validating/metrics/metrics_test.go`** -> AI Confidence: **99.31%**
792. **`staging/src/k8s.io/apiserver/pkg/admission/plugin/policy/validating/typechecking.go`** -> AI Confidence: **99.31%**
793. **`staging/src/k8s.io/apiserver/pkg/admission/plugin/policy/validating/validator.go`** -> AI Confidence: **99.31%**
794. **`staging/src/k8s.io/apiserver/pkg/admission/plugin/policy/validating/validator_test.go`** -> AI Confidence: **99.31%**
795. **`staging/src/k8s.io/apiserver/pkg/admission/plugin/resourcequota/admission_test.go`** -> AI Confidence: **99.31%**
796. **`staging/src/k8s.io/apiserver/pkg/admission/plugin/resourcequota/controller.go`** -> AI Confidence: **99.31%**
797. **`staging/src/k8s.io/apiserver/pkg/admission/plugin/resourcequota/resource_access.go`** -> AI Confidence: **99.31%**
798. **`staging/src/k8s.io/apiserver/pkg/admission/plugin/webhook/generic/webhook.go`** -> AI Confidence: **99.31%**
799. **`staging/src/k8s.io/apiserver/pkg/admission/plugin/webhook/matchconditions/matcher.go`** -> AI Confidence: **99.31%**
800. **`staging/src/k8s.io/apiserver/pkg/admission/plugin/webhook/matchconditions/matcher_test.go`** -> AI Confidence: **99.31%**
801. **`staging/src/k8s.io/apiserver/pkg/admission/plugin/webhook/mutating/dispatcher.go`** -> AI Confidence: **99.31%**
802. **`staging/src/k8s.io/apiserver/pkg/admission/plugin/webhook/mutating/plugin_test.go`** -> AI Confidence: **99.31%**
803. **`staging/src/k8s.io/apiserver/pkg/admission/plugin/webhook/predicates/namespace/matcher.go`** -> AI Confidence: **99.31%**
804. **`staging/src/k8s.io/apiserver/pkg/admission/plugin/webhook/predicates/namespace/matcher_test.go`** -> AI Confidence: **99.31%**
805. **`staging/src/k8s.io/apiserver/pkg/admission/plugin/webhook/predicates/object/matcher_test.go`** -> AI Confidence: **99.31%**
806. **`staging/src/k8s.io/apiserver/pkg/admission/plugin/webhook/request/admissionreview.go`** -> AI Confidence: **99.31%**
807. **`staging/src/k8s.io/apiserver/pkg/admission/plugin/webhook/request/admissionreview_test.go`** -> AI Confidence: **99.31%**
808. **`staging/src/k8s.io/apiserver/pkg/admission/plugin/webhook/testing/webhook_server.go`** -> AI Confidence: **99.31%**
809. **`staging/src/k8s.io/apiserver/pkg/admission/plugin/webhook/validating/dispatcher.go`** -> AI Confidence: **99.31%**
810. **`staging/src/k8s.io/apiserver/pkg/apis/apidiscovery/v2/fuzzer_test.go`** -> AI Confidence: **99.31%**
811. **`staging/src/k8s.io/apiserver/pkg/apis/apiserver/load/load_test.go`** -> AI Confidence: **99.31%**
812. **`staging/src/k8s.io/apiserver/pkg/apis/apiserver/validation/validation_encryption_test.go`** -> AI Confidence: **99.31%**
813. **`staging/src/k8s.io/apiserver/pkg/apis/flowcontrol/bootstrap/default.go`** -> AI Confidence: **99.31%**
814. **`staging/src/k8s.io/apiserver/pkg/audit/request.go`** -> AI Confidence: **99.31%**
815. **`staging/src/k8s.io/apiserver/pkg/authentication/authenticator/audagnostic_test.go`** -> AI Confidence: **99.31%**
816. **`staging/src/k8s.io/apiserver/pkg/authentication/authenticatorfactory/delegating.go`** -> AI Confidence: **99.31%**
817. **`staging/src/k8s.io/apiserver/pkg/authentication/request/bearertoken/bearertoken_test.go`** -> AI Confidence: **99.31%**
818. **`staging/src/k8s.io/apiserver/pkg/authentication/request/headerrequest/requestheader.go`** -> AI Confidence: **99.31%**
819. **`staging/src/k8s.io/apiserver/pkg/authentication/request/headerrequest/requestheader_controller_test.go`** -> AI Confidence: **99.31%**
820. **`staging/src/k8s.io/apiserver/pkg/authentication/request/x509/x509.go`** -> AI Confidence: **99.31%**
821. **`staging/src/k8s.io/apiserver/pkg/authentication/request/x509/x509_test.go`** -> AI Confidence: **99.31%**
822. **`staging/src/k8s.io/apiserver/pkg/authentication/serviceaccount/util_test.go`** -> AI Confidence: **99.31%**
823. **`staging/src/k8s.io/apiserver/pkg/authentication/token/cache/cached_token_authenticator_test.go`** -> AI Confidence: **99.31%**
824. **`staging/src/k8s.io/apiserver/pkg/authorization/cel/compile_test.go`** -> AI Confidence: **99.31%**
825. **`staging/src/k8s.io/apiserver/pkg/authorization/cel/matcher.go`** -> AI Confidence: **99.31%**
826. **`staging/src/k8s.io/apiserver/pkg/authorization/union/union_test.go`** -> AI Confidence: **99.31%**
827. **`staging/src/k8s.io/apiserver/pkg/cel/common/schemas.go`** -> AI Confidence: **99.31%**
828. **`staging/src/k8s.io/apiserver/pkg/cel/escaping.go`** -> AI Confidence: **99.31%**
829. **`staging/src/k8s.io/apiserver/pkg/cel/library/cost.go`** -> AI Confidence: **99.31%**
830. **`staging/src/k8s.io/apiserver/pkg/cel/openapi/schemas_test.go`** -> AI Confidence: **99.31%**
831. **`staging/src/k8s.io/apiserver/pkg/cel/value_test.go`** -> AI Confidence: **99.31%**
832. **`staging/src/k8s.io/apiserver/pkg/endpoints/discovery/aggregated/handler.go`** -> AI Confidence: **99.31%**
833. **`staging/src/k8s.io/apiserver/pkg/endpoints/discovery/aggregated/peer_aggregated_handler.go`** -> AI Confidence: **99.31%**
834. **`staging/src/k8s.io/apiserver/pkg/endpoints/discovery/root_test.go`** -> AI Confidence: **99.31%**
835. **`staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit_init_test.go`** -> AI Confidence: **99.31%**
836. **`staging/src/k8s.io/apiserver/pkg/endpoints/filters/audit_test.go`** -> AI Confidence: **99.31%**
837. **`staging/src/k8s.io/apiserver/pkg/endpoints/filters/authentication.go`** -> AI Confidence: **99.31%**
838. **`staging/src/k8s.io/apiserver/pkg/endpoints/filters/authentication_test.go`** -> AI Confidence: **99.31%**
839. **`staging/src/k8s.io/apiserver/pkg/endpoints/filters/authn_audit.go`** -> AI Confidence: **99.31%**
840. **`staging/src/k8s.io/apiserver/pkg/endpoints/filters/authorization.go`** -> AI Confidence: **99.31%**
841. **`staging/src/k8s.io/apiserver/pkg/endpoints/filters/authorization_test.go`** -> AI Confidence: **99.31%**
842. **`staging/src/k8s.io/apiserver/pkg/endpoints/filters/impersonation/constrained_impersonation.go`** -> AI Confidence: **99.31%**
843. **`staging/src/k8s.io/apiserver/pkg/endpoints/filters/impersonation/constrained_impersonation_test.go`** -> AI Confidence: **99.31%**
844. **`staging/src/k8s.io/apiserver/pkg/endpoints/filters/impersonation/impersonation_test.go`** -> AI Confidence: **99.31%**
845. **`staging/src/k8s.io/apiserver/pkg/endpoints/filters/read_write_deadline_test.go`** -> AI Confidence: **99.31%**
846. **`staging/src/k8s.io/apiserver/pkg/endpoints/filters/request_deadline.go`** -> AI Confidence: **99.31%**
847. **`staging/src/k8s.io/apiserver/pkg/endpoints/filters/request_deadline_test.go`** -> AI Confidence: **99.31%**
848. **`staging/src/k8s.io/apiserver/pkg/endpoints/filters/storageversion.go`** -> AI Confidence: **99.31%**
849. **`staging/src/k8s.io/apiserver/pkg/endpoints/filters/traces.go`** -> AI Confidence: **99.31%**
850. **`staging/src/k8s.io/apiserver/pkg/endpoints/handlers/create.go`** -> AI Confidence: **99.31%**
851. **`staging/src/k8s.io/apiserver/pkg/endpoints/handlers/delete.go`** -> AI Confidence: **99.31%**
852. **`staging/src/k8s.io/apiserver/pkg/endpoints/handlers/fieldmanager/equality.go`** -> AI Confidence: **99.31%**
853. **`staging/src/k8s.io/apiserver/pkg/endpoints/handlers/finisher/finisher.go`** -> AI Confidence: **99.31%**
854. **`staging/src/k8s.io/apiserver/pkg/endpoints/handlers/finisher/finisher_test.go`** -> AI Confidence: **99.31%**
855. **`staging/src/k8s.io/apiserver/pkg/endpoints/handlers/negotiation/negotiate.go`** -> AI Confidence: **99.31%**
856. **`staging/src/k8s.io/apiserver/pkg/endpoints/handlers/negotiation/negotiate_test.go`** -> AI Confidence: **99.31%**
857. **`staging/src/k8s.io/apiserver/pkg/endpoints/handlers/patch.go`** -> AI Confidence: **99.31%**
858. **`staging/src/k8s.io/apiserver/pkg/endpoints/handlers/responsewriters/errors.go`** -> AI Confidence: **99.31%**
859. **`staging/src/k8s.io/apiserver/pkg/endpoints/handlers/responsewriters/errors_test.go`** -> AI Confidence: **99.31%**
860. **`staging/src/k8s.io/apiserver/pkg/endpoints/handlers/responsewriters/status_test.go`** -> AI Confidence: **99.31%**
861. **`staging/src/k8s.io/apiserver/pkg/endpoints/handlers/responsewriters/writers.go`** -> AI Confidence: **99.31%**
862. **`staging/src/k8s.io/apiserver/pkg/endpoints/handlers/responsewriters/writers_test.go`** -> AI Confidence: **99.31%**
863. **`staging/src/k8s.io/apiserver/pkg/endpoints/handlers/rest.go`** -> AI Confidence: **99.31%**
864. **`staging/src/k8s.io/apiserver/pkg/endpoints/handlers/rest_test.go`** -> AI Confidence: **99.31%**
865. **`staging/src/k8s.io/apiserver/pkg/endpoints/handlers/update.go`** -> AI Confidence: **99.31%**
866. **`staging/src/k8s.io/apiserver/pkg/endpoints/installer.go`** -> AI Confidence: **99.31%**
867. **`staging/src/k8s.io/apiserver/pkg/endpoints/metrics/metrics.go`** -> AI Confidence: **99.31%**
868. **`staging/src/k8s.io/apiserver/pkg/endpoints/metrics/metrics_test.go`** -> AI Confidence: **99.31%**
869. **`staging/src/k8s.io/apiserver/pkg/endpoints/openapi/openapi.go`** -> AI Confidence: **99.31%**
870. **`staging/src/k8s.io/apiserver/pkg/endpoints/openapi/openapi_test.go`** -> AI Confidence: **99.31%**
871. **`staging/src/k8s.io/apiserver/pkg/endpoints/request/requestinfo.go`** -> AI Confidence: **99.31%**
872. **`staging/src/k8s.io/apiserver/pkg/endpoints/responsewriter/wrapper_test.go`** -> AI Confidence: **99.31%**
873. **`staging/src/k8s.io/apiserver/pkg/endpoints/watch_test.go`** -> AI Confidence: **99.31%**
874. **`staging/src/k8s.io/apiserver/pkg/quota/v1/generic/evaluator_test.go`** -> AI Confidence: **99.31%**
875. **`staging/src/k8s.io/apiserver/pkg/quota/v1/resources_test.go`** -> AI Confidence: **99.31%**
876. **`staging/src/k8s.io/apiserver/pkg/reconcilers/peer_endpoint_lease_test.go`** -> AI Confidence: **99.31%**
877. **`staging/src/k8s.io/apiserver/pkg/registry/generic/registry/decorated_watcher_test.go`** -> AI Confidence: **99.31%**
878. **`staging/src/k8s.io/apiserver/pkg/registry/generic/registry/dryrun_test.go`** -> AI Confidence: **99.31%**
879. **`staging/src/k8s.io/apiserver/pkg/registry/generic/registry/store.go`** -> AI Confidence: **99.31%**
880. **`staging/src/k8s.io/apiserver/pkg/registry/generic/registry/store_test.go`** -> AI Confidence: **99.31%**
881. **`staging/src/k8s.io/apiserver/pkg/registry/generic/rest/streamer.go`** -> AI Confidence: **99.31%**
882. **`staging/src/k8s.io/apiserver/pkg/registry/rest/delete.go`** -> AI Confidence: **99.31%**
883. **`staging/src/k8s.io/apiserver/pkg/registry/rest/delete_test.go`** -> AI Confidence: **99.31%**
884. **`staging/src/k8s.io/apiserver/pkg/registry/rest/validate_test.go`** -> AI Confidence: **99.31%**
885. **`staging/src/k8s.io/apiserver/pkg/server/config.go`** -> AI Confidence: **99.31%**
886. **`staging/src/k8s.io/apiserver/pkg/server/config_test.go`** -> AI Confidence: **99.31%**
887. **`staging/src/k8s.io/apiserver/pkg/server/deleted_kinds.go`** -> AI Confidence: **99.31%**
888. **`staging/src/k8s.io/apiserver/pkg/server/dynamiccertificates/named_certificates_test.go`** -> AI Confidence: **99.31%**
889. **`staging/src/k8s.io/apiserver/pkg/server/dynamiccertificates/server_test.go`** -> AI Confidence: **99.31%**
890. **`staging/src/k8s.io/apiserver/pkg/server/dynamiccertificates/tlsconfig.go`** -> AI Confidence: **99.31%**
891. **`staging/src/k8s.io/apiserver/pkg/server/egressselector/config_test.go`** -> AI Confidence: **99.31%**
892. **`staging/src/k8s.io/apiserver/pkg/server/egressselector/egress_selector_test.go`** -> AI Confidence: **99.31%**
893. **`staging/src/k8s.io/apiserver/pkg/server/filters/goaway_test.go`** -> AI Confidence: **99.31%**
894. **`staging/src/k8s.io/apiserver/pkg/server/filters/maxinflight.go`** -> AI Confidence: **99.31%**
895. **`staging/src/k8s.io/apiserver/pkg/server/filters/maxinflight_test.go`** -> AI Confidence: **99.31%**
896. **`staging/src/k8s.io/apiserver/pkg/server/filters/priority-and-fairness.go`** -> AI Confidence: **99.31%**
897. **`staging/src/k8s.io/apiserver/pkg/server/filters/priority-and-fairness_test.go`** -> AI Confidence: **99.31%**
898. **`staging/src/k8s.io/apiserver/pkg/server/filters/timeout_test.go`** -> AI Confidence: **99.31%**
899. **`staging/src/k8s.io/apiserver/pkg/server/flagz/flagz.go`** -> AI Confidence: **99.31%**
900. **`staging/src/k8s.io/apiserver/pkg/server/flagz/flagz_test.go`** -> AI Confidence: **99.31%**
901. **`staging/src/k8s.io/apiserver/pkg/server/genericapiserver_graceful_termination_test.go`** -> AI Confidence: **99.31%**
902. **`staging/src/k8s.io/apiserver/pkg/server/genericapiserver_test.go`** -> AI Confidence: **99.31%**
903. **`staging/src/k8s.io/apiserver/pkg/server/healthz/healthz_test.go`** -> AI Confidence: **99.31%**
904. **`staging/src/k8s.io/apiserver/pkg/server/options/admission.go`** -> AI Confidence: **99.31%**
905. **`staging/src/k8s.io/apiserver/pkg/server/options/api_enablement_test.go`** -> AI Confidence: **99.31%**
906. **`staging/src/k8s.io/apiserver/pkg/server/options/authentication.go`** -> AI Confidence: **99.31%**
907. **`staging/src/k8s.io/apiserver/pkg/server/options/authorization.go`** -> AI Confidence: **99.31%**
908. **`staging/src/k8s.io/apiserver/pkg/server/options/etcd.go`** -> AI Confidence: **99.31%**
909. **`staging/src/k8s.io/apiserver/pkg/server/options/serving_test.go`** -> AI Confidence: **99.31%**
910. **`staging/src/k8s.io/apiserver/pkg/server/options/serving_with_loopback_test.go`** -> AI Confidence: **99.31%**
911. **`staging/src/k8s.io/apiserver/pkg/server/resourceconfig/helpers.go`** -> AI Confidence: **99.31%**
912. **`staging/src/k8s.io/apiserver/pkg/server/routes/openapi.go`** -> AI Confidence: **99.31%**
913. **`staging/src/k8s.io/apiserver/pkg/server/secure_serving.go`** -> AI Confidence: **99.31%**
914. **`staging/src/k8s.io/apiserver/pkg/server/statusz/statusz.go`** -> AI Confidence: **99.31%**
915. **`staging/src/k8s.io/apiserver/pkg/server/statusz/statusz_test.go`** -> AI Confidence: **99.31%**
916. **`staging/src/k8s.io/apiserver/pkg/server/storage/storage_factory.go`** -> AI Confidence: **99.31%**
917. **`staging/src/k8s.io/apiserver/pkg/server/storage/storage_factory_test.go`** -> AI Confidence: **99.31%**
918. **`staging/src/k8s.io/apiserver/pkg/storage/cacher/cache_watcher.go`** -> AI Confidence: **99.31%**
919. **`staging/src/k8s.io/apiserver/pkg/storage/cacher/cache_watcher_test.go`** -> AI Confidence: **99.31%**
920. **`staging/src/k8s.io/apiserver/pkg/storage/cacher/cacher.go`** -> AI Confidence: **99.31%**
921. **`staging/src/k8s.io/apiserver/pkg/storage/cacher/cacher_test.go`** -> AI Confidence: **99.31%**
922. **`staging/src/k8s.io/apiserver/pkg/storage/cacher/cacher_testing_utils_test.go`** -> AI Confidence: **99.31%**
923. **`staging/src/k8s.io/apiserver/pkg/storage/cacher/lister_watcher_test.go`** -> AI Confidence: **99.31%**
924. **`staging/src/k8s.io/apiserver/pkg/storage/cacher/watch_cache_interval_test.go`** -> AI Confidence: **99.31%**
925. **`staging/src/k8s.io/apiserver/pkg/storage/cacher/watch_cache_test.go`** -> AI Confidence: **99.31%**
926. **`staging/src/k8s.io/apiserver/pkg/storage/etcd3/compact.go`** -> AI Confidence: **99.31%**
927. **`staging/src/k8s.io/apiserver/pkg/storage/etcd3/errors.go`** -> AI Confidence: **99.31%**
928. **`staging/src/k8s.io/apiserver/pkg/storage/etcd3/metrics/metrics.go`** -> AI Confidence: **99.31%**
929. **`staging/src/k8s.io/apiserver/pkg/storage/etcd3/metrics/metrics_test.go`** -> AI Confidence: **99.31%**
930. **`staging/src/k8s.io/apiserver/pkg/storage/etcd3/store.go`** -> AI Confidence: **99.31%**
931. **`staging/src/k8s.io/apiserver/pkg/storage/etcd3/store_test.go`** -> AI Confidence: **99.31%**
932. **`staging/src/k8s.io/apiserver/pkg/storage/etcd3/watcher.go`** -> AI Confidence: **99.31%**
933. **`staging/src/k8s.io/apiserver/pkg/storage/etcd3/watcher_test.go`** -> AI Confidence: **99.31%**
934. **`staging/src/k8s.io/apiserver/pkg/storage/storagebackend/factory/tls_test.go`** -> AI Confidence: **99.31%**
935. **`staging/src/k8s.io/apiserver/pkg/storage/testing/store_tests.go`** -> AI Confidence: **99.31%**
936. **`staging/src/k8s.io/apiserver/pkg/storage/testing/utils.go`** -> AI Confidence: **99.31%**
937. **`staging/src/k8s.io/apiserver/pkg/storage/testing/watcher_tests.go`** -> AI Confidence: **99.31%**
938. **`staging/src/k8s.io/apiserver/pkg/storage/util_test.go`** -> AI Confidence: **99.31%**
939. **`staging/src/k8s.io/apiserver/pkg/storage/value/encrypt/envelope/envelope_test.go`** -> AI Confidence: **99.31%**
940. **`staging/src/k8s.io/apiserver/pkg/storage/value/encrypt/envelope/grpc_service_unix_test.go`** -> AI Confidence: **99.31%**
941. **`staging/src/k8s.io/apiserver/pkg/storage/value/encrypt/envelope/kmsv2/cache_test.go`** -> AI Confidence: **99.31%**
942. **`staging/src/k8s.io/apiserver/pkg/storage/value/encrypt/envelope/kmsv2/envelope_test.go`** -> AI Confidence: **99.31%**
943. **`staging/src/k8s.io/apiserver/pkg/storage/value/encrypt/envelope/kmsv2/grpc_service_unix_test.go`** -> AI Confidence: **99.31%**
944. **`staging/src/k8s.io/apiserver/pkg/storage/value/encrypt/envelope/metrics/metrics_test.go`** -> AI Confidence: **99.31%**
945. **`staging/src/k8s.io/apiserver/pkg/util/flowcontrol/controller_test.go`** -> AI Confidence: **99.31%**
946. **`staging/src/k8s.io/apiserver/pkg/util/flowcontrol/fairqueuing/queueset/queueset.go`** -> AI Confidence: **99.31%**
947. **`staging/src/k8s.io/apiserver/pkg/util/flowcontrol/format/formatting.go`** -> AI Confidence: **99.31%**
948. **`staging/src/k8s.io/apiserver/pkg/util/flowcontrol/metrics/metrics.go`** -> AI Confidence: **99.31%**
949. **`staging/src/k8s.io/apiserver/pkg/util/flowcontrol/request/object_count_tracker_test.go`** -> AI Confidence: **99.31%**
950. **`staging/src/k8s.io/apiserver/pkg/util/flowcontrol/request/width_test.go`** -> AI Confidence: **99.31%**
951. **`staging/src/k8s.io/apiserver/pkg/util/notfoundhandler/not_found_handler_test.go`** -> AI Confidence: **99.31%**
952. **`staging/src/k8s.io/apiserver/pkg/util/peerproxy/peer_discovery.go`** -> AI Confidence: **99.31%**
953. **`staging/src/k8s.io/apiserver/pkg/util/peerproxy/peer_discovery_test.go`** -> AI Confidence: **99.31%**
954. **`staging/src/k8s.io/apiserver/pkg/util/proxy/endpointslice_test.go`** -> AI Confidence: **99.31%**
955. **`staging/src/k8s.io/apiserver/pkg/util/proxy/streamtranslator.go`** -> AI Confidence: **99.31%**
956. **`staging/src/k8s.io/apiserver/pkg/util/proxy/streamtranslator_test.go`** -> AI Confidence: **99.31%**
957. **`staging/src/k8s.io/apiserver/pkg/util/webhook/authentication.go`** -> AI Confidence: **99.31%**
958. **`staging/src/k8s.io/apiserver/pkg/util/webhook/client.go`** -> AI Confidence: **99.31%**
959. **`staging/src/k8s.io/apiserver/pkg/util/webhook/webhook_test.go`** -> AI Confidence: **99.31%**
960. **`staging/src/k8s.io/apiserver/pkg/util/x509metrics/server_cert_deprecations.go`** -> AI Confidence: **99.31%**
961. **`staging/src/k8s.io/apiserver/pkg/util/x509metrics/server_cert_deprecations_test.go`** -> AI Confidence: **99.31%**
962. **`staging/src/k8s.io/apiserver/plugin/pkg/authenticator/token/oidc/metrics_test.go`** -> AI Confidence: **99.31%**
963. **`staging/src/k8s.io/apiserver/plugin/pkg/authenticator/token/webhook/webhook_v1_test.go`** -> AI Confidence: **99.31%**
964. **`staging/src/k8s.io/apiserver/plugin/pkg/authenticator/token/webhook/webhook_v1beta1_test.go`** -> AI Confidence: **99.31%**
965. **`staging/src/k8s.io/apiserver/plugin/pkg/authorizer/webhook/metrics/metrics_test.go`** -> AI Confidence: **99.31%**
966. **`staging/src/k8s.io/apiserver/plugin/pkg/authorizer/webhook/metrics_test.go`** -> AI Confidence: **99.31%**
967. **`staging/src/k8s.io/apiserver/plugin/pkg/authorizer/webhook/webhook.go`** -> AI Confidence: **99.31%**
968. **`staging/src/k8s.io/apiserver/plugin/pkg/authorizer/webhook/webhook_v1_test.go`** -> AI Confidence: **99.31%**
969. **`staging/src/k8s.io/apiserver/plugin/pkg/authorizer/webhook/webhook_v1beta1_test.go`** -> AI Confidence: **99.31%**
970. **`staging/src/k8s.io/cli-runtime/pkg/genericclioptions/config_flags.go`** -> AI Confidence: **99.31%**
971. **`staging/src/k8s.io/cli-runtime/pkg/genericclioptions/json_yaml_flags.go`** -> AI Confidence: **99.31%**
972. **`staging/src/k8s.io/cli-runtime/pkg/genericclioptions/jsonpath_flags.go`** -> AI Confidence: **99.31%**
973. **`staging/src/k8s.io/cli-runtime/pkg/genericclioptions/template_flags.go`** -> AI Confidence: **99.31%**
974. **`staging/src/k8s.io/cli-runtime/pkg/genericclioptions/template_flags_test.go`** -> AI Confidence: **99.31%**
975. **`staging/src/k8s.io/cli-runtime/pkg/printers/json_test.go`** -> AI Confidence: **99.31%**
976. **`staging/src/k8s.io/cli-runtime/pkg/printers/jsonpath.go`** -> AI Confidence: **99.31%**
977. **`staging/src/k8s.io/cli-runtime/pkg/printers/tableprinter.go`** -> AI Confidence: **99.31%**
978. **`staging/src/k8s.io/cli-runtime/pkg/printers/template_test.go`** -> AI Confidence: **99.31%**
979. **`staging/src/k8s.io/cli-runtime/pkg/resource/builder.go`** -> AI Confidence: **99.31%**
980. **`staging/src/k8s.io/cli-runtime/pkg/resource/helper_test.go`** -> AI Confidence: **99.31%**
981. **`staging/src/k8s.io/cli-runtime/pkg/resource/query_param_verifier_v3.go`** -> AI Confidence: **99.31%**
982. **`staging/src/k8s.io/cli-runtime/pkg/resource/scheme_test.go`** -> AI Confidence: **99.31%**
983. **`staging/src/k8s.io/cli-runtime/pkg/resource/visitor_test.go`** -> AI Confidence: **99.31%**
984. **`staging/src/k8s.io/client-go/discovery/cached/disk/round_tripper_test.go`** -> AI Confidence: **99.31%**
985. **`staging/src/k8s.io/client-go/discovery/cached/memory/memcache_test.go`** -> AI Confidence: **99.31%**
986. **`staging/src/k8s.io/client-go/discovery/discovery_client_test.go`** -> AI Confidence: **99.31%**
987. **`staging/src/k8s.io/client-go/discovery/helper_blackbox_test.go`** -> AI Confidence: **99.31%**
988. **`staging/src/k8s.io/client-go/dynamic/fake/simple.go`** -> AI Confidence: **99.31%**
989. **`staging/src/k8s.io/client-go/example_test.go`** -> AI Confidence: **99.31%**
990. **`staging/src/k8s.io/client-go/examples/create-update-delete-deployment/main.go`** -> AI Confidence: **99.31%**
991. **`staging/src/k8s.io/client-go/features/envvar.go`** -> AI Confidence: **99.31%**
992. **`staging/src/k8s.io/client-go/informers/generic.go`** -> AI Confidence: **99.31%**
993. **`staging/src/k8s.io/client-go/kubernetes/typed/core/v1/event_expansion_test.go`** -> AI Confidence: **99.31%**
994. **`staging/src/k8s.io/client-go/kubernetes/typed/core/v1/fake/fake_pod_expansion_test.go`** -> AI Confidence: **99.31%**
995. **`staging/src/k8s.io/client-go/kubernetes/typed/events/v1beta1/event_expansion_test.go`** -> AI Confidence: **99.31%**
996. **`staging/src/k8s.io/client-go/listers/extensions/v1beta1/daemonset_expansion_test.go`** -> AI Confidence: **99.31%**
997. **`staging/src/k8s.io/client-go/openapi/groupversion_test.go`** -> AI Confidence: **99.31%**
998. **`staging/src/k8s.io/client-go/openapi3/root_test.go`** -> AI Confidence: **99.31%**
999. **`staging/src/k8s.io/client-go/plugin/pkg/client/auth/exec/exec.go`** -> AI Confidence: **99.31%**
1000. **`staging/src/k8s.io/client-go/plugin/pkg/client/auth/exec/exec_cache_test.go`** -> AI Confidence: **99.31%**
1001. **`staging/src/k8s.io/client-go/plugin/pkg/client/auth/exec/exec_test.go`** -> AI Confidence: **99.31%**
1002. **`staging/src/k8s.io/client-go/plugin/pkg/client/auth/exec/metrics.go`** -> AI Confidence: **99.31%**
1003. **`staging/src/k8s.io/client-go/plugin/pkg/client/auth/exec/metrics_test.go`** -> AI Confidence: **99.31%**
1004. **`staging/src/k8s.io/client-go/rest/client_test.go`** -> AI Confidence: **99.31%**
1005. **`staging/src/k8s.io/client-go/rest/config_test.go`** -> AI Confidence: **99.31%**
1006. **`staging/src/k8s.io/client-go/rest/connection_test.go`** -> AI Confidence: **99.31%**
1007. **`staging/src/k8s.io/client-go/rest/exec_test.go`** -> AI Confidence: **99.31%**
1008. **`staging/src/k8s.io/client-go/rest/plugin_test.go`** -> AI Confidence: **99.31%**
1009. **`staging/src/k8s.io/client-go/rest/request.go`** -> AI Confidence: **99.31%**
1010. **`staging/src/k8s.io/client-go/rest/request_test.go`** -> AI Confidence: **99.31%**
1011. **`staging/src/k8s.io/client-go/rest/urlbackoff_test.go`** -> AI Confidence: **99.31%**
1012. **`staging/src/k8s.io/client-go/rest/watch/decoder_test.go`** -> AI Confidence: **99.31%**
1013. **`staging/src/k8s.io/client-go/rest/watch/encoder_test.go`** -> AI Confidence: **99.31%**
1014. **`staging/src/k8s.io/client-go/rest/with_retry_test.go`** -> AI Confidence: **99.31%**
1015. **`staging/src/k8s.io/client-go/restmapper/discovery.go`** -> AI Confidence: **99.31%**
1016. **`staging/src/k8s.io/client-go/restmapper/shortcut.go`** -> AI Confidence: **99.31%**
1017. **`staging/src/k8s.io/client-go/testing/fixture_test.go`** -> AI Confidence: **99.31%**
1018. **`staging/src/k8s.io/client-go/tools/auth/exec/exec_test.go`** -> AI Confidence: **99.31%**
1019. **`staging/src/k8s.io/client-go/tools/auth/exec/types_test.go`** -> AI Confidence: **99.31%**
1020. **`staging/src/k8s.io/client-go/tools/cache/controller.go`** -> AI Confidence: **99.31%**
1021. **`staging/src/k8s.io/client-go/tools/cache/controller_bench_test.go`** -> AI Confidence: **99.31%**
1022. **`staging/src/k8s.io/client-go/tools/cache/mutation_detector.go`** -> AI Confidence: **99.31%**
1023. **`staging/src/k8s.io/client-go/tools/cache/reflector.go`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `staging/src/k8s.io/apiserver/pkg/admission/plugin/webhook/testcerts/certs.go` -> **100.0%** Exposure
- `staging/src/k8s.io/apiserver/pkg/server/dynamiccertificates/tlsconfig_test.go` -> **100.0%** Exposure
- `staging/src/k8s.io/apiserver/pkg/server/graceful_shutdown_test.go` -> **100.0%** Exposure
- `staging/src/k8s.io/apiserver/pkg/storage/etcd3/testing/testingcert/certificates.go` -> **100.0%** Exposure
- `staging/src/k8s.io/apiserver/pkg/util/webhook/certs_test.go` -> **100.0%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `90` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `63106` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `staging/src/k8s.io/apimachinery/pkg/util/proxy/upgradeaware.go` (GO) -> Cumulative Risk: **758.47**
- **Archetype:** `file_cluster_4` (Distance: 13.952 IQR)
- **Magnitude:** 461.1 | **LOC:** 560 | **CtrlFlow:** 48.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (97.9238%)
- **Heaviest Functions:** `tryUpgrade` (Impact: 48.4), `ServeHTTP` (Impact: 31.0), `proxyRedirectsforRootPath` (Impact: 10.9)

### 2. `staging/src/k8s.io/apimachinery/pkg/watch/watch.go` (GO) -> Cumulative Risk: **716.67**
- **Archetype:** `file_cluster_4` (Distance: 12.251 IQR)
- **Magnitude:** 384.98 | **LOC:** 378 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), State Flux (99.763%)
- **Heaviest Functions:** `Add` (Impact: 12.8), `Modify` (Impact: 12.8), `Delete` (Impact: 12.8)

### 3. `staging/src/k8s.io/apiserver/pkg/server/healthz/healthz.go` (GO) -> Cumulative Risk: **712.79**
- **Archetype:** `file_cluster_4` (Distance: 12.494 IQR)
- **Magnitude:** 282.86 | **LOC:** 365 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9997%), Concurrency (99.9795%), Tech Debt (99.9666%)
- **Heaviest Functions:** `handleRootHealth` (Impact: 18.0), `InstallPathHandlerWithHealthyFunc` (Impact: 13.2), `Check` (Impact: 10.5)

### 4. `staging/src/k8s.io/apimachinery/pkg/util/httpstream/wsstream/conn.go` (GO) -> Cumulative Risk: **701.49**
- **Archetype:** `file_cluster_4` (Distance: 13.281 IQR)
- **Magnitude:** 361.96 | **LOC:** 467 | **CtrlFlow:** 45.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.5273%), Tech Debt (98.8757%)
- **Heaviest Functions:** `initialize` (Impact: 25.8), `DataFromSocket` (Impact: 15.6), `handshake` (Impact: 14.8)

### 5. `staging/src/k8s.io/client-go/tools/portforward/portforward_test.go` (GO) -> Cumulative Risk: **700.56**
- **Archetype:** `file_cluster_4` (Distance: 12.891 IQR)
- **Magnitude:** 0.67 | **LOC:** 634 | **CtrlFlow:** 47.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9999%)
- **Heaviest Functions:** `TestParsePortsAndNew` (Impact: 61.8), `TestGetListener` (Impact: 41.4), `CreateStream` (Impact: 15.3)

### 6. `staging/src/k8s.io/client-go/util/workqueue/delaying_queue.go` (GO) -> Cumulative Risk: **692.7**
- **Archetype:** `file_cluster_4` (Distance: 12.8 IQR)
- **Magnitude:** 201.28 | **LOC:** 370 | **CtrlFlow:** 37.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9556%), Safety Score (88.299%)
- **Heaviest Functions:** `NewTypedDelayingQueueWithConfig` (Impact: 9.9), `AddAfter` (Impact: 9.5), `insert` (Impact: 6.8)

### 7. `staging/src/k8s.io/client-go/tools/remotecommand/spdy_test.go` (GO) -> Cumulative Risk: **691.37**
- **Archetype:** `file_cluster_4` (Distance: 13.246 IQR)
- **Magnitude:** 0.54 | **LOC:** 431 | **CtrlFlow:** 39.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `createHTTPStreams` (Impact: 37.1), `TestStreamRandomData` (Impact: 22.9), `fakeMassiveDataAttacher` (Impact: 16.3)

### 8. `staging/src/k8s.io/apiserver/pkg/admission/plugin/policy/generic/plugin.go` (GO) -> Cumulative Risk: **688.39**
- **Archetype:** `file_cluster_4` (Distance: 12.864 IQR)
- **Magnitude:** 165.44 | **LOC:** 222 | **CtrlFlow:** 36.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.998%), State Flux (99.9789%), Tech Debt (99.927%)
- **Heaviest Functions:** `ValidateInitialization` (Impact: 36.6), `Dispatch` (Impact: 9.2), `NewPlugin` (Impact: 2.9)

### 9. `pkg/kubelet/lifecycle/handlers.go` (GO) -> Cumulative Risk: **685.75**
- **Archetype:** `file_cluster_4` (Distance: 13.353 IQR)
- **Magnitude:** 214.26 | **LOC:** 293 | **CtrlFlow:** 47.3% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.4762%), Documentation (87.7424%)
- **Heaviest Functions:** `Run` (Impact: 23.0), `Admit` (Impact: 14.0), `runHTTPHandler` (Impact: 13.6)

### 10. `pkg/kubelet/volumemanager/volume_manager_fake.go` (GO) -> Cumulative Risk: **685.15**
- **Archetype:** `file_cluster_15` (Distance: 14.082 IQR)
- **Magnitude:** 127.5 | **LOC:** 133 | **CtrlFlow:** 38.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9991%), Concurrency (91.4012%)
- **Heaviest Functions:** `MarkVolumesAsReportedInUse` (Impact: 10.1), `NewFakeVolumeManager` (Impact: 7.4), `GetVolumesInUse` (Impact: 7.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `pkg/apis/core/validation/validation.go` (GO | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 16.153 IQR)
- **Top Global Matches:** file_cluster_8: 16.153, file_cluster_7: 16.231, file_cluster_11: 16.232
- **Magnitude:** 9051.04 | **LOC:** 9661 | **CtrlFlow:** 77.2% | **Authorship Centralization:** 21.1%
- **Risk Profile:** Cognitive Load (40.2545%), Tech Debt (73.889%)
**Top Internal Functions/Classes:**
  * `ValidateUserAnnotations` (Impact: 682.1)
  * `ValidateVolumes` (Impact: 246.3)
  * `ValidationOptionsForPersistentVolumeClai` (Impact: 175.4)
  * `ValidateLimitRange` (Impact: 136.3)
  * `validatePodResourceClaimStatuses` (Impact: 122.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1182`, `structural_boundaries: 349`, `args: 173`, `func_start: 173`, `class_start: 2`
* *Risk/State:* `state_mutation: 4824`, `dead_code: 15`, `planned_debt: 13`, `fragile_debt: 1`, `orphaned_logic: 73`
* *Architecture:* `api: 117`, `import: 1`
* *Defense:* `safety: 23`, `doc: 236`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.041
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` regexp, conversion, field, diff, metadata.labels, net, features, intstr...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/validation/validation_test.go` (GO | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.005 IQR)
- **Top Global Matches:** file_cluster_8: 11.005, file_cluster_7: 11.512, file_cluster_1: 11.791
- **Magnitude:** 5760.96 | **LOC:** 11920 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (6.7548%), Tech Debt (8.7698%)
**Top Internal Functions/Classes:**
  * `TestValidateCustomResourceDefinitionVali` (Impact: 181.8)
  * `TestValidateCustomResourceDefinitionVali` (Impact: 50.0)
  * `TestSelectableFields` (Impact: 48.4)
  * `TestValidateFieldPath` (Impact: 31.5)
  * `TestValidateCustomResourceDefinitionUpda` (Impact: 31.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 219`, `structural_boundaries: 829`, `args: 17`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 167`, `planned_debt: 5`, `duplicate_logic: 2`, `orphaned_logic: 4`
* *Architecture:* `api: 4993`, `import: 1`
* *Defense:* `safety: 4`, `doc: 11`, `test: 11`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.041
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` package, json, bbb, array, embedded-preserve-unpruned-objectmeta, wrongly-typed-object-defaults-kind, nestedObj, metadata...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `staging/src/k8s.io/kubectl/pkg/describe/describe_test.go` (GO | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.039 IQR)
- **Top Global Matches:** file_cluster_8: 13.039, file_cluster_7: 13.417, file_cluster_0: 13.63
- **Magnitude:** 5663.84 | **LOC:** 7942 | **CtrlFlow:** 72.1% | **Authorship Centralization:** 63.6%
- **Risk Profile:** Cognitive Load (20.3696%), Tech Debt (15.8336%)
**Top Internal Functions/Classes:**
  * `TestDescribeIngress` (Impact: 70.0)
  * `TestDescribeHorizontalPodAutoscaler` (Impact: 51.5)
  * `TestPersistentVolumeClaimDescriber` (Impact: 42.5)
  * `TestDescribeEvents` (Impact: 39.1)
  * `TestPersistentVolumeDescriber` (Impact: 37.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 427`, `structural_boundaries: 165`, `args: 69`, `func_start: 69`, `class_start: 1`
* *Risk/State:* `state_mutation: 1271`, `orphaned_logic: 64`
* *Architecture:* `api: 2962`, `import: 1`
* *Defense:* `safety: 67`, `doc: 16`, `test: 100`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.041
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` id2, password, metadata, Status, simpler, itemInt, Conditions, service-name...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kube-apiserver/app/testing/testdata/127.0.0.1_10.0.0.1_kubernetes.default.svc-kubernetes.default-kubernetes-localhost.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.041
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kube-apiserver/app/testing/testdata/127.0.0.1_10.0.0.1_kubernetes.default.svc-kubernetes.default-kubernetes-localhost.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.041
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/1.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.041
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/10.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.041
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/11.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.041
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/12.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.041
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/13.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.041
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/14.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.041
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/15.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.041
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/16.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.041
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/17.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.041
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/18.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.041
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/19.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.041
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/2.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.041
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/20.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.041
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/21.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.041
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/22.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.041
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/23.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.041
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/24.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.041
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/25.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.041
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/3.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.041
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/4.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.041
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `staging/src/k8s.io/kms/apis/v1beta1/api_grpc.pb.go` (GO) | Magnitude: 6.3 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 108, state_mutation: 62, structural_boundaries: 50, api: 33
- `cmd/kubeadm/app/util/config/cluster.go` (GO) | Magnitude: 405.5 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 199, state_mutation: 134, encapsulation: 55, branch: 48
- `staging/src/k8s.io/apiserver/pkg/admission/plugin/resourcequota/apis/resourcequota/v1/types.go` (GO) | Magnitude: 22.3 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 11, indent_tabs: 8, api: 7, structural_boundaries: 6
- `staging/src/k8s.io/apiserver/pkg/admission/plugin/resourcequota/apis/resourcequota/v1alpha1/types.go` (GO) | Magnitude: 22.3 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 11, indent_tabs: 8, api: 7, structural_boundaries: 6
- `staging/src/k8s.io/apiserver/pkg/admission/plugin/resourcequota/apis/resourcequota/v1beta1/types.go` (GO) | Magnitude: 22.3 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 11, indent_tabs: 8, api: 7, structural_boundaries: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/embedded/zz_generated.validations.go` (GO) | Magnitude: 4.16 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 43, state_mutation: 32, pointers: 23, structural_boundaries: 20
- `pkg/volume/util/device_util_linux.go` (GO) | Magnitude: 239.12 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 117, indent_tabs: 115, branch: 42, encapsulation: 31
- `staging/src/k8s.io/apiserver/pkg/storage/cacher/watch_cache.go` (GO) | Magnitude: 226.02 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 194, state_mutation: 93, encapsulation: 58, structural_boundaries: 48
- `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/tags/levels/atomicslice/zz_generated.validations.go` (GO) | Magnitude: 3.81 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 47, state_mutation: 36, structural_boundaries: 19, encapsulation: 16
- `cluster/gce/upgrade.sh` (SHELL) | Magnitude: 589.38 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 412, branch: 254, reflection_metaprogramming: 170, state_mutation: 151

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `cluster/addons/addon-manager/kube-addons-main.sh` (SHELL) | Magnitude: 43.0 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 21, indent_spaces: 21, reflection_metaprogramming: 15, state_mutation: 12
- `staging/src/k8s.io/apiextensions-apiserver/examples/client-go/hack/verify-codegen.sh` (SHELL) | Magnitude: 24.58 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: reflection_metaprogramming: 13, state_mutation: 12, safety: 9, branch: 7
- `staging/src/k8s.io/apiextensions-apiserver/hack/verify-codegen.sh` (SHELL) | Magnitude: 24.58 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: reflection_metaprogramming: 13, state_mutation: 12, safety: 9, branch: 7
- `staging/src/k8s.io/metrics/hack/verify-codegen.sh` (SHELL) | Magnitude: 24.58 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: reflection_metaprogramming: 13, state_mutation: 12, safety: 9, branch: 7
- `pkg/printers/tablegenerator.go` (GO) | Magnitude: 141.34 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 92, state_mutation: 77, structural_boundaries: 30, encapsulation: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `staging/src/k8s.io/api/extensions/v1beta1/zz_generated.validations.go` (GO) | Magnitude: 9.11 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 88, state_mutation: 57, branch: 46, structural_boundaries: 25
- `staging/src/k8s.io/apiserver/pkg/server/options/egress_selector.go` (GO) | Magnitude: 63.3 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 37, state_mutation: 24, structural_boundaries: 13, doc: 11
- `staging/src/k8s.io/cli-runtime/pkg/printers/tabwriter.go` (GO) | Magnitude: 8.4 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 8, state_mutation: 5, encapsulation: 5, structural_boundaries: 3
- `staging/src/k8s.io/client-go/tools/cache/the_real_fifo.go` (GO) | Magnitude: 0.18 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 174, state_mutation: 112, doc: 55, encapsulation: 48
- `staging/src/k8s.io/apiserver/pkg/registry/rest/validate.go` (GO) | Magnitude: 537.18 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 278, state_mutation: 258, encapsulation: 105, branch: 86

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `staging/src/k8s.io/component-base/metrics/summary.go` (GO) | Magnitude: 114.16 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 91, pointers: 27, structural_boundaries: 26, api: 23
- `staging/src/k8s.io/code-generator/examples/apiserver/apis/example/zz_generated.deepcopy.go` (GO) | Magnitude: 18.62 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 190, indent_tabs: 177, pointers: 71, branch: 42
- `staging/src/k8s.io/component-base/metrics/histogram.go` (GO) | Magnitude: 158.36 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 129, structural_boundaries: 35, state_mutation: 34, pointers: 33
- `staging/src/k8s.io/client-go/applyconfigurations/core/v1/event.go` (GO) | Magnitude: 258.88 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 134, pointers: 108, doc: 86, state_mutation: 69
- `pkg/api/v1/endpoints/util.go` (GO) | Magnitude: 160.86 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 65, state_mutation: 64, encapsulation: 37, structural_boundaries: 30

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `pkg/scheduler/backend/heap/heap.go` (GO) | Magnitude: 106.32 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 62, state_mutation: 36, encapsulation: 21, structural_boundaries: 20
- `staging/src/k8s.io/apimachinery/pkg/api/validate/strfmt.go` (GO) | Magnitude: 423.32 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 236, indent_tabs: 157, branch: 56, encapsulation: 37
- `staging/src/k8s.io/client-go/util/workqueue/queue.go` (GO) | Magnitude: 198.98 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 162, structural_boundaries: 49, state_mutation: 46, encapsulation: 36
- `staging/src/k8s.io/kubectl/pkg/explain/v2/templates/plaintext_test.go` (GO) | Magnitude: 386.02 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 682, api: 228, structural_boundaries: 153, generics: 71
- `test/utils/ktesting/helper_test.go` (GO) | Magnitude: 103.58 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 61, state_mutation: 26, closures: 24, args: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/cel/model/types_test.go` (GO) | Magnitude: 80.44 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 70, state_mutation: 41, encapsulation: 30, branch: 16
- `staging/src/k8s.io/mount-utils/mount_helper_common.go` (GO) | Magnitude: 98.66 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 75, state_mutation: 33, branch: 22, encapsulation: 22
- `staging/src/k8s.io/kube-scheduler/framework/signers.go` (GO) | Magnitude: 246.64 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 135, state_mutation: 127, encapsulation: 38, api: 32
- `cmd/cloud-controller-manager/nodeipamcontroller.go` (GO) | Magnitude: 181.26 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 143, state_mutation: 80, encapsulation: 51, branch: 37
- `cmd/kube-controller-manager/app/certificates.go` (GO) | Magnitude: 318.68 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 258, state_mutation: 118, encapsulation: 107, branch: 66

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/customresource_discovery.go` (GO) | Magnitude: 54.16 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 58, encapsulation: 24, structural_boundaries: 22, state_mutation: 19
- `staging/src/k8s.io/apiserver/pkg/server/mux/pathrecorder.go` (GO) | Magnitude: 97.38 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 82, state_mutation: 36, structural_boundaries: 18, encapsulation: 16
- `staging/src/k8s.io/apiserver/pkg/endpoints/discovery/aggregated/wrapper.go` (GO) | Magnitude: 28.72 | Delta: **0.105 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 48, encapsulation: 24, structural_boundaries: 11, state_mutation: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `staging/src/k8s.io/client-go/tools/cache/synctrack/synctrack_test.go` (GO) | Magnitude: 0.27 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 185, state_mutation: 75, branch: 62, concurrency: 42
- `staging/src/k8s.io/apiserver/plugin/pkg/authenticator/token/oidc/oidc.go` (GO) | Magnitude: 101.28 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 104, structural_boundaries: 36, encapsulation: 31, state_mutation: 29
- `staging/src/k8s.io/client-go/examples/workqueue/main.go` (GO) | Magnitude: 125.08 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 110, state_mutation: 44, encapsulation: 44, structural_boundaries: 27
- `pkg/kubelet/config/file_linux.go` (GO) | Magnitude: 155.9 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 98, state_mutation: 71, branch: 29, structural_boundaries: 24
- `staging/src/k8s.io/apiserver/pkg/admission/handler.go` (GO) | Magnitude: 55.74 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 26, state_mutation: 17, structural_boundaries: 10, branch: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `staging/src/k8s.io/apimachinery/pkg/util/httpstream/wsstream/doc.go` (GO) | Magnitude: 10.52 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 16, sec_dead_code: 2, structural_boundaries: 1, dead_code: 1
- `cmd/kubeadm/app/apis/kubeadm/v1beta3/doc.go` (GO) | Magnitude: 10.52 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 23, dead_code: 3, structural_boundaries: 1, sec_io: 1
- `pkg/kubelet/secret/secret_manager.go` (GO) | Magnitude: 66.56 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 67, structural_boundaries: 27, state_mutation: 25, encapsulation: 25
- `pkg/kubelet/cm/devicemanager/plugin/v1beta1/stub.go` (GO) | Magnitude: 293.42 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 231, state_mutation: 116, encapsulation: 87, structural_boundaries: 55
- `staging/src/k8s.io/client-go/util/retry/util.go` (GO) | Magnitude: 40.0 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 29, state_mutation: 14, api: 12, structural_boundaries: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `staging/src/k8s.io/apiserver/pkg/util/proxy/doc.go` (GO) | Magnitude: 10.52 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 5, structural_boundaries: 1
- `pkg/scheduler/backend/cache/interface.go` (GO) | Magnitude: 26.48 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 28, indent_tabs: 17, structural_boundaries: 8, concurrency: 6
- `staging/src/k8s.io/client-go/applyconfigurations/core/v1/topologyspreadconstraint.go` (GO) | Magnitude: 57.64 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 38, pointers: 26, indent_tabs: 24, state_mutation: 16
- `staging/src/k8s.io/client-go/applyconfigurations/resource/v1/celdeviceselector.go` (GO) | Magnitude: 9.72 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 13, pointers: 6, structural_boundaries: 5, api: 4
- `staging/src/k8s.io/client-go/applyconfigurations/resource/v1beta1/celdeviceselector.go` (GO) | Magnitude: 9.72 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 13, pointers: 6, structural_boundaries: 5, api: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `hack/update-owners-fmt.sh` (SHELL) | Magnitude: 5.12 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, reflection_metaprogramming: 4, indent_spaces: 4, safety: 3
- `pkg/controller/deployment/rollback.go` (GO) | Magnitude: 46.24 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 35, state_mutation: 27, encapsulation: 12, structural_boundaries: 8
- `pkg/registry/rbac/clusterrole/strategy.go` (GO) | Magnitude: 74.94 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 43, api: 23, state_mutation: 21, encapsulation: 15
- `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/unstructured/unstructured.go` (GO) | Magnitude: 557.16 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 273, state_mutation: 167, structural_boundaries: 107, api: 93
- `staging/src/k8s.io/apiserver/pkg/admission/plugins.go` (GO) | Magnitude: 32.76 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 23, structural_boundaries: 11, state_mutation: 9, api: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `staging/src/k8s.io/code-generator/cmd/validation-gen/testscheme/doc.go` (GO) | Magnitude: 10.52 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 17, dead_code: 4, structural_boundaries: 1, sec_high_risk_execution: 1
- `staging/src/k8s.io/apiserver/doc.go` (GO) | Magnitude: 10.52 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 10, structural_boundaries: 1, dead_code: 1, sec_high_risk_execution: 1
- `staging/src/k8s.io/apiserver/pkg/util/flowcontrol/fairqueuing/queueset/doc.go` (GO) | Magnitude: 10.52 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 10, structural_boundaries: 1, dead_code: 1, sec_dead_code: 1
- `Makefile` (MAKEFILE) | Magnitude: 855.32 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 93, branch: 69, func_start: 47, indent_tabs: 43
- `test/conformance/image/go-runner/Makefile` (MAKEFILE) | Magnitude: 18.68 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: api: 4, structural_boundaries: 3, func_start: 3, reflection_metaprogramming: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `hack/golangci.yaml` -> Churn: **100.0%** | Cog Load: 4.8136% | Debt: 60.0815%
- `hack/golangci-hints.yaml` -> Churn: **95.98%** | Cog Load: 4.876% | Debt: 74.0425%
- `staging/src/k8s.io/dynamic-resource-allocation/structured/internal/allocatortesting/allocator_testing.go` -> Churn: **70.04%** | Cog Load: 55.1916% | Debt: 20.0025%
- `pkg/apis/core/validation/validation.go` -> Churn: **69.78%** | Cog Load: 40.2545% | Debt: 73.889%
- `staging/src/k8s.io/dynamic-resource-allocation/structured/internal/incubating/allocator_incubating.go` -> Churn: **66.91%** | Cog Load: 50.6871% | Debt: 99.9876%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/validation/validation_test.go` -> **Jordan Liggitt** (100.0% isolated ownership) | Magnitude: 5760.96
- `staging/src/k8s.io/kubectl/pkg/cmd/get/get_test.go` -> **Jordan Liggitt** (100.0% isolated ownership) | Magnitude: 2437.92
- `staging/src/k8s.io/kubectl/pkg/cmd/apply/apply_test.go` -> **Manuel Grandeit** (100.0% isolated ownership) | Magnitude: 2087.94
- `staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/validation/validation.go` -> **Jordan Liggitt** (100.0% isolated ownership) | Magnitude: 1770.54
- `staging/src/k8s.io/cloud-provider/controllers/node/node_controller_test.go` -> **Jonathan Yaniv** (100.0% isolated ownership) | Magnitude: 1553.86

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `staging/src/k8s.io/client-go/util/cert/io.go` -> **Severity: 0.004** (Bridge: 0.0 * Flux: 100.0%)
- `staging/src/k8s.io/apiserver/pkg/authentication/request/x509/x509.go` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 99.9999%)
- `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/time.go` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 99.9992%)
- `staging/src/k8s.io/apimachinery/pkg/util/net/http.go` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 100.0%)
- `staging/src/k8s.io/apiserver/pkg/cel/url.go` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 98.4181%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/time.go` -> **Severity: 4242.978** (Blast Radius: 43.201 * Doc Risk: 98.2148%)
- `pkg/kubeapiserver/authorizer/modes/modes.go` -> **Severity: 2952.582** (Blast Radius: 33.035 * Doc Risk: 89.3774%)
- `staging/src/k8s.io/apiserver/pkg/authentication/request/x509/x509.go` -> **Severity: 1332.271** (Blast Radius: 17.979 * Doc Risk: 74.1015%)
- `staging/src/k8s.io/client-go/util/cert/io.go` -> **Severity: 844.764** (Blast Radius: 19.27 * Doc Risk: 43.8383%)
- `staging/src/k8s.io/apiserver/pkg/authentication/user/user.go` -> **Severity: 723.441** (Blast Radius: 7.236 * Doc Risk: 99.978%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
