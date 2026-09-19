# ARCHITECTURAL_BRIEF: kubernetes
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/kubernetes/kubernetes.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 19717 analyzed artifact(s), 2462111 LOC.
- **Load-bearing artifact:** `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/time.go` -- 2257 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `pkg/apis/batch/validation/validation_test.go` -- pulls in 598 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `pkg/apis/core/validation/validation.go` at magnitude 10354.16 (structural weight, not risk).
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
| Total Artifacts | 28256 |
| Analyzed Artifacts (Scanned) | 19717 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 8539 |
| Total LOC | 2462111 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 69.8% |
| Dominant Lang | GO |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5563 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1759 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.2136 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 214 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| GO | 11686 | 2040001 | 59.3% |
| YAML | 5299 | 208288 | 26.9% |
| JSON | 754 | 172354 | 3.8% |
| PLAINTEXT | 680 | 81 | 3.4% |
| BINARY_THREAT | 554 | 554 | 2.8% |
| MARKDOWN | 292 | 0 | 1.5% |
| SHELL | 286 | 31449 | 1.5% |
| PROTO | 87 | 5720 | 0.4% |
| DOCKERFILE | 37 | 266 | 0.2% |
| MAKEFILE | 23 | 571 | 0.1% |
| POWERSHELL | 6 | 2498 | 0.0% |
| PYTHON | 6 | 325 | 0.0% |
| XML | 4 | 0 | 0.0% |
| CSV | 2 | 3 | 0.0% |
| HTML | 1 | 1 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled Monorepo`
> **Architectural Drift Z-Score:** `6.032`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +6.03; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 46%, Callbacks & Closures Files 14%, Declarative / Non-Code 6%, Large Core Modules 6%, Large Core Modules (3) 6%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 18187 | 92.2% |
| Unknown | 635 | 3.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 891 | 4.5% |
| Static: Minified & Vendor Opaque Mass | 4 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 8539*

**Composition by Extension & Reason:**
- `.go`: 4459x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 33x Excluded (Machine-Generated Source Code Signature: 23 LOC), 24x Excluded (Machine-Generated Source Code Signature: 34 LOC)
- `no_extension`: 1273x Unsupported Format (.undeterminable), 713x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 306x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.yaml`: 25x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 24x Zero-Density Threshold (LOC: 72, Signals: 0), 20x Zero-Density Threshold (LOC: 53, Signals: 0)
- `.md`: 272x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 75 LOC), 1x Excluded (Machine-Generated Source Code Signature: 120 LOC)
- `.yml`: 66x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 6 exceeds 500 chars)
- `.request`: 60x Unsupported Format (.request), 3x Excluded (Saturation: Line 4 exceeds 500 chars)
- `.response`: 58x Unsupported Format (.response), 3x Excluded (Saturation: Line 6 exceeds 500 chars), 2x Excluded (Saturation: Line 16 exceeds 500 chars)
- `.s`: 62x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Massive Static Asset Blob: 2942 LOC), 2x Excluded (Massive Static Asset Blob: 8868 LOC)
- `.proto`: 38x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1418 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1373 LOC)
- `.sum`: 35x Unsupported Format (.sum), 2x Excluded (Unsupported Extension: '.sum')
- `.mod`: 36x Unsupported Format (.mod)
- `.sh`: 30x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 72 LOC), 1x Excluded (Machine-Generated Source Code Signature: 266 LOC)
- `.edited`: 31x Unsupported Format (.edited)
- `.original`: 31x Unsupported Format (.original)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 7.3 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 26.7 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 20.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 6.5 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 8.6 | 1.8 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 3.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 24.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.8 | 1.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 18.0 | 0.4 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 2.5 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 28.4 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 169316 | 8806 | 21 | `staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/validation/validation_test.go` |
| cleanup | 3378 | 983 | 0 | `staging/src/k8s.io/apiserver/pkg/endpoints/apiserver_test.go` |
| guards | 75898 | 8086 | 10 | `cluster/gce/util.sh` |
| danger | 11925 | 2569 | 1 | `cluster/gce/util.sh` |
| concurrency | 13955 | 1727 | 0 | `pkg/kubelet/pod_workers_test.go` |
| connectivity | 97993 | 10218 | 13 | `staging/src/k8s.io/api/core/v1/types.go` |
| io | 9403 | 1563 | 0 | `cluster/gce/util.sh` |
| crypto | 0 | 0 | 0 | - |
| ipc | 872 | 286 | 0 | `cluster/gce/util.sh` |
| time | 6636 | 1620 | 0 | `pkg/printers/internalversion/printers_test.go` |
| serialization | 1201 | 499 | 0 | `staging/src/k8s.io/apiserver/pkg/registry/generic/registry/store_test.go` |
| regex | 1394 | 308 | 0 | `cluster/gce/gci/configure-helper.sh` |
| events | 831 | 382 | 0 | `hack/update-codegen.sh` |
| tests | 30158 | 3181 | 3 | `staging/src/k8s.io/component-base/featuregate/feature_gate_test.go` |
| docs | 145883 | 14760 | 17 | `staging/src/k8s.io/api/core/v1/types.go` |
| debt | 11301 | 2616 | 1 | `cluster/gce/util.sh` |
| mutation | 196583 | 8602 | 24 | `pkg/apis/core/validation/validation.go` |
| dead_code | 34311 | 7718 | 5 | `pkg/controller/podautoscaler/horizontal_test.go` |
| credential | 421 | 109 | 0 | `cmd/kubeadm/app/cmd/token_test.go` |
| threat | 4973 | 1312 | 0 | `staging/src/k8s.io/apimachinery/pkg/runtime/converter.go` |
| ml_ai | 849 | 233 | 0 | `cluster/gce/util.sh` |
| ui | 439 | 193 | 0 | `test/images/agnhost/webhook/main.go` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `cluster/gce/util.sh` (Hits: 836)
- `cluster/gce/gci/configure-helper.sh` (Hits: 451)
- `test/cmd/core.sh` (Hits: 220)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **time.go** (`staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/time.go`) — 2257 inbound connections
2. **schema.go** (`staging/src/k8s.io/kubectl/pkg/validation/schema.go`) — 1446 inbound connections
3. **http.go** (`staging/src/k8s.io/apimachinery/pkg/util/net/http.go`) — 730 inbound connections
4. **ktesting.go** (`test/utils/ktesting/ktesting.go`) — 449 inbound connections
5. **assert.go** (`test/utils/ktesting/assert.go`) — 361 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **validation_test.go** (`pkg/apis/batch/validation/validation_test.go`) — 598 outbound dependencies
2. **allocator_testing.go** (`staging/src/k8s.io/dynamic-resource-allocation/structured/internal/allocatortesting/allocator_testing.go`) — 239 outbound dependencies
3. **validation_test.go** (`staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/cel/validation_test.go`) — 170 outbound dependencies
4. **validation_test.go** (`staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/validation/validation_test.go`) — 168 outbound dependencies
5. **dynamicresources_test.go** (`pkg/scheduler/framework/plugins/dynamicresources/dynamicresources_test.go`) — 153 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `Validate_UpdateTestStruct` **(Many-Argument Workhorses)** (@ `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/tags/update/zz_generated.validations.go`) -> Impact: **488.5** | LOC: 461
  * *Intent:* // Validate_UpdateTestStruct validates an instance of UpdateTestStruct according // to declarative validation rules in the API schema.
- `NewMainKubelet` **(Many-Argument Workhorses)** (@ `pkg/kubelet/kubelet.go`) -> Impact: **456.4** | LOC: 711
  * *Intent:* // NewMainKubelet instantiates a new Kubelet object along with all the required internal modules. // No initialization of Kubelet and its modules shou...
- `ValidateCustomResourceDefinitionOpenAPISchema` **(Many-Argument Workhorses)** (@ `staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/validation/validation.go`) -> Impact: **400.9** | LOC: 292
  * *Intent:* // ValidateCustomResourceDefinitionOpenAPISchema statically validates
- `convertToAPIContainerStatuses` **(Many-Argument Workhorses)** (@ `pkg/kubelet/kubelet_pods.go`) -> Impact: **387.5** | LOC: 477
  * *Intent:* // convertToAPIContainerStatuses converts the given internal container // statuses into API container statuses.
- `Validate_T1` **(Many-Argument Workhorses)** (@ `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cross_pkg/zz_generated.validations.go`) -> Impact: **334.5** | LOC: 321
  * *Intent:* // Validate_T1 validates an instance of T1 according // to declarative validation rules in the API schema.
- `registerResourceHandlers` **(Many-Argument Workhorses)** (@ `staging/src/k8s.io/apiserver/pkg/endpoints/installer.go`) -> Impact: **332.2** | LOC: 844
- `ValidateKubeletConfiguration` **(Many-Argument Workhorses)** (@ `pkg/kubelet/apis/config/validation/validation.go`) -> Impact: **287.8** | LOC: 353
  * *Intent:* // ValidateKubeletConfiguration validates `kc` and returns an error if it is invalid
- `ValidatePersistentVolumeSpec` **(Many-Argument Workhorses)** (@ `pkg/apis/core/validation/validation.go`) -> Impact: **286.7** | LOC: 296
- `TestKubelet_HandlePodCleanups` **(Many-Argument Workhorses)** (@ `pkg/kubelet/kubelet_pods_test.go`) -> Impact: **285.1** | LOC: 1092
- `warningsForPodSpecAndMeta` **(Many-Argument Workhorses)** (@ `pkg/api/pod/warnings.go`) -> Impact: **271.7** | LOC: 291

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `cmd/kubeadm/app/util/pkiutil/testing/testdata` | 26 | 125000.0 | 0.0% | 0.0% |
| `staging/src/k8s.io/api/testdata/v1.34.0` | 481 | 92006.77 | 0.0% | 0.0% |
| `staging/src/k8s.io/api/testdata/HEAD` | 477 | 91506.65 | 0.0% | 0.0% |
| `staging/src/k8s.io/api/testdata/v1.33.0` | 478 | 91006.72 | 0.0% | 0.0% |
| `staging/src/k8s.io/kube-aggregator/pkg/apiserver/testdata` | 15 | 40000.06 | 0.0% | 0.0% |
| `pkg/kubeapiserver/options/testdata` | 13 | 30000.07 | 0.0% | 0.0% |
| `staging/src/k8s.io/apiserver/plugin/pkg/authenticator/token/oidc/testdata` | 7 | 30000.01 | 0.87% | 0.0% |
| `staging/src/k8s.io/apiserver/pkg/server/options/testdata` | 11 | 20000.07 | 0.0% | 0.0% |
| `staging/src/k8s.io/apiserver/pkg/authentication/request/x509/testdata` | 10 | 20000.07 | 0.0% | 0.0% |
| `pkg/kubelet/certificate/bootstrap/testdata` | 5 | 20000.0 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `cluster/skeleton/util.sh` -> **100.0%** Exposure
- `hack/_update-generated-proto-bindings-dockerized.sh` -> **100.0%** Exposure
- `hack/_update-generated-protobuf-dockerized.sh` -> **100.0%** Exposure
- `hack/benchmark-go.sh` -> **100.0%** Exposure
- `hack/build-cross.sh` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `cluster/gce/config-common.sh` -> **100.0%** Exposure
- `cluster/gce/config-default.sh` -> **100.0%** Exposure
- `cluster/gce/config-test.sh` -> **100.0%** Exposure
- `cluster/gce/gci/configure-kubeapiserver.sh` -> **100.0%** Exposure
- `cluster/gce/gci/master-helper.sh` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `pkg/controller/podautoscaler/horizontal_test.go` -> **97** Orphaned Functions | **0** Duplicates
- `pkg/printers/internalversion/printers_test.go` -> **83** Orphaned Functions | **0** Duplicates
- `pkg/scheduler/testing/wrappers.go` -> **81** Orphaned Functions | **0** Duplicates
- `staging/src/k8s.io/apiserver/pkg/endpoints/apiserver_test.go` -> **77** Orphaned Functions | **0** Duplicates
- `pkg/controller/podautoscaler/replica_calculator_test.go` -> **76** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `cmd/kubeadm/app/apis/bootstraptoken/v1/utils_test.go` -> **100.0%** Exposure
- `cmd/kubeadm/app/cmd/token_test.go` -> **100.0%** Exposure
- `cmd/kubeadm/app/util/pubkeypin/pubkeypin_test.go` -> **100.0%** Exposure
- `pkg/credentialprovider/secrets/secrets_test.go` -> **100.0%** Exposure
- `pkg/kubelet/certificate/transport_test.go` -> **100.0%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `74` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `97929` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `pkg/apis/core/validation/validation.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 10354.16 | **LOC:** 9661 | **CtrlFlow:** 31.1% | **Authorship Centralization:** 21.1%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **93**; blast radius 0.033; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.5%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (69.8%)
- **Documentation Coverage:** 56.0575% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ValidatePersistentVolumeSpec` **(Many-Argument Workhorses)** (Impact: 286.7)
  * `validateVolumeSource` **(Many-Argument Workhorses)** (Impact: 255.6)
  * `validateProjectionSources` **(Many-Argument Workhorses)** (Impact: 155.8)
  * `validateService` **(Many-Argument Workhorses)** (Impact: 119.6)
    * *Intent:* // ValidateService tests if required fields/annotations of a Service are valid.
  * `validateWindows` **(Many-Argument Workhorses)** (Impact: 96.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 1387 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 4313
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2339`, `structural_boundaries: 1046`, `args: 347`, `func_start: 347`, `class_start: 5`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 1539`, `dead_code: 21`, `planned_debt: 24`, `fragile_debt: 1`, `unreferenced_by_name: 39`
* *Architecture:* `io: 1`, `api: 201`, `import: 1`
* *Defense:* `safety: 33`, `doc: 424`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.033
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` 1, 1Ki, 1k, Annotations, Args, Command, Env, EnvFrom...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kube-apiserver/app/testing/testdata/127.0.0.1_10.0.0.1_kubernetes.default.svc-kubernetes.default-kubernetes-localhost.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.033
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kube-apiserver/app/testing/testdata/127.0.0.1_10.0.0.1_kubernetes.default.svc-kubernetes.default-kubernetes-localhost.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.033
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/1.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.033
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/10.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.033
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/11.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.033
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/12.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.033
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/13.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.033
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/14.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.033
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/15.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.033
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/16.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.033
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/17.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.033
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/18.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.033
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/19.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.033
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/2.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.033
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/20.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.033
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/21.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.033
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/22.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.033
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/23.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.033
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/24.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.033
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/25.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.033
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/3.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.033
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/4.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.033
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/5.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.033
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/6.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.033
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `hack/golangci.yaml` -> Churn: **100.0%** | Cog Load: 4.4154% | Debt: 52.4981%
- `hack/golangci-hints.yaml` -> Churn: **95.98%** | Cog Load: 4.3735% | Debt: 65.0224%
- `staging/src/k8s.io/client-go/tools/cache/the_real_fifo.go` -> Churn: **63.24%** | Cog Load: 32.3859% | Debt: 86.1069%
- `hack/golangci.yaml.in` -> Churn: **56.37%** | Cog Load: 5.5223% | Debt: 100.0%
- `staging/src/k8s.io/code-generator/cmd/validation-gen/validators/each.go` -> Churn: **55.08%** | Cog Load: 37.968% | Debt: 66.0756%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/validation/validation.go` -> **Jordan Liggitt** (100.0% isolated ownership) | Magnitude: 1994.9
- `staging/src/k8s.io/apimachinery/pkg/util/strategicpatch/patch.go` -> **Stephen Kitt** (100.0% isolated ownership) | Magnitude: 1801.26
- `staging/src/k8s.io/kubectl/pkg/cmd/apply/apply_test.go` -> **Manuel Grandeit** (100.0% isolated ownership) | Magnitude: 1477.88
- `test/integration/apiserver/apply/apply_test.go` -> **Mads Jensen** (100.0% isolated ownership) | Magnitude: 1467.06
- `staging/src/k8s.io/apiserver/pkg/registry/generic/registry/store.go` -> **Heba Elayoty** (100.0% isolated ownership) | Magnitude: 1193.0

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/time.go` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 99.9417%)
- `staging/src/k8s.io/apimachinery/pkg/util/net/http.go` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 100.0%)
- `staging/src/k8s.io/apiserver/pkg/cel/url.go` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 83.2018%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/time.go` -> **Severity: 8.249** (Embedded: 0.1196 * Error Risk: 68.9974%)
- `staging/src/k8s.io/kubectl/pkg/validation/schema.go` -> **Severity: 3.708** (Embedded: 0.0646 * Error Risk: 57.3856%)
- `staging/src/k8s.io/apimachinery/pkg/util/net/http.go` -> **Severity: 3.468** (Embedded: 0.0456 * Error Risk: 76.1347%)
- `staging/src/k8s.io/apiserver/pkg/cel/url.go` -> **Severity: 2.014** (Embedded: 0.0324 * Error Risk: 62.1788%)
- `test/e2e/framework/gomega.go` -> **Severity: 1.787** (Embedded: 0.0272 * Error Risk: 65.7332%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `staging/src/k8s.io/kubectl/pkg/validation/schema.go` -> **Severity: 1021.39** (Blast Radius: 37.451 * Doc Risk: 27.2727%)
- `staging/src/k8s.io/client-go/tools/clientcmd/flag.go` -> **Severity: 720.6** (Blast Radius: 7.206 * Doc Risk: 100.0%)
- `staging/src/k8s.io/apimachinery/pkg/util/sort/sort.go` -> **Severity: 634.747** (Blast Radius: 7.324 * Doc Risk: 86.6667%)
- `staging/src/k8s.io/apimachinery/pkg/util/net/http.go` -> **Severity: 551.167** (Blast Radius: 15.004 * Doc Risk: 36.7347%)
- `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/time.go` -> **Severity: 540.544** (Blast Radius: 48.649 * Doc Risk: 11.1111%)

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
