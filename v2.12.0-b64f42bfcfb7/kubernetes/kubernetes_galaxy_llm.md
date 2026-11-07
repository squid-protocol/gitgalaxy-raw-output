# ARCHITECTURAL_BRIEF: kubernetes
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/kubernetes/kubernetes.git` |
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
- **Scope:** 19220 analyzed artifact(s), 2511562 LOC.
- **Load-bearing artifact:** `staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/doc.go` -- 3507 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `pkg/kubelet/kubelet.go` -- pulls in 122 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `pkg/apis/core/validation/validation.go` at magnitude 10153.66 (structural weight, not risk).
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
| Total Artifacts | 28257 |
| Analyzed Artifacts (Scanned) | 19220 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 9037 |
| Total LOC | 2511562 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 68.0% |
| Dominant Lang | GO |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5083 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1199 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 4.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.09 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 668 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| GO | 11768 | 2089423 | 61.2% |
| YAML | 5305 | 208586 | 27.6% |
| JSON | 754 | 172354 | 3.9% |
| PLAINTEXT | 649 | 50 | 3.4% |
| MARKDOWN | 294 | 0 | 1.5% |
| SHELL | 287 | 31616 | 1.5% |
| PROTO | 87 | 5720 | 0.5% |
| DOCKERFILE | 37 | 266 | 0.2% |
| MAKEFILE | 23 | 571 | 0.1% |
| PYTHON | 7 | 474 | 0.0% |
| POWERSHELL | 6 | 2498 | 0.0% |
| CSV | 2 | 3 | 0.0% |
| HTML | 1 | 1 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 19170 |
| unknown | unknown | 50 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 44%, Callbacks & Closures Files 17%, Large Core Modules (2) 7%, Large Core Modules 6%, Large Core Modules (3) 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 18273 | 95.1% |
| Unknown | 50 | 0.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 893 | 4.6% |
| Static: Minified & Vendor Opaque Mass | 4 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 9037*

**Composition by Extension & Reason:**
- `.go`: 4451x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 33x Excluded (Machine-Generated Source Code Signature: 23 LOC), 24x Excluded (Machine-Generated Source Code Signature: 34 LOC)
- `no_extension`: 1273x Unsupported Format (.undeterminable), 713x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 306x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.pb`: 553x Excluded (Binary Format Detected), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 24x Zero-Density Threshold (LOC: 72, Signals: 0), 21x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 20x Zero-Density Threshold (LOC: 53, Signals: 0)
- `.md`: 272x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 230 LOC), 1x Excluded (Machine-Generated Source Code Signature: 5 LOC)
- `.yml`: 65x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 6 exceeds 500 chars)
- `.request`: 60x Unsupported Format (.request), 3x Excluded (Saturation: Line 4 exceeds 500 chars)
- `.response`: 58x Unsupported Format (.response), 3x Excluded (Saturation: Line 6 exceeds 500 chars), 2x Excluded (Saturation: Line 16 exceeds 500 chars)
- `.s`: 62x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Massive Static Asset Blob: 2942 LOC), 2x Excluded (Massive Static Asset Blob: 8868 LOC)
- `.proto`: 38x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1418 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1373 LOC)
- `.sum`: 35x Unsupported Format (.sum), 2x Excluded (Unsupported Extension: '.sum')
- `.mod`: 36x Unsupported Format (.mod)
- `.sh`: 30x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 72 LOC), 1x Excluded (Machine-Generated Source Code Signature: 153 LOC)
- `.edited`: 31x Unsupported Format (.edited)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 7.3 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 98.8 | 23.7 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 25.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 6.4 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 4.3 | 2.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 3.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 25.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.8 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 18.0 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 2.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 29.5 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.4 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 29773 | 4062 | 3 | `staging/src/k8s.io/apimachinery/pkg/util/strategicpatch/patch_test.go` |
| cleanup | 3408 | 990 | 0 | `staging/src/k8s.io/apiserver/pkg/endpoints/apiserver_test.go` |
| guards | 76399 | 8132 | 11 | `cluster/gce/util.sh` |
| danger | 11969 | 2587 | 1 | `cluster/gce/util.sh` |
| concurrency | 13975 | 1736 | 0 | `pkg/kubelet/pod_workers_test.go` |
| connectivity | 99355 | 10238 | 14 | `staging/src/k8s.io/api/core/v1/types.go` |
| io | 9482 | 1571 | 0 | `cluster/gce/util.sh` |
| crypto | 0 | 0 | 0 | - |
| ipc | 880 | 289 | 0 | `cluster/gce/util.sh` |
| time | 6696 | 1630 | 0 | `pkg/printers/internalversion/printers_test.go` |
| serialization | 1209 | 504 | 0 | `staging/src/k8s.io/apiserver/pkg/registry/generic/registry/store_test.go` |
| regex | 1421 | 313 | 0 | `cluster/gce/gci/configure-helper.sh` |
| events | 832 | 383 | 0 | `hack/update-codegen.sh` |
| tests | 30726 | 3199 | 3 | `staging/src/k8s.io/component-base/featuregate/feature_gate_test.go` |
| docs | 146961 | 14842 | 17 | `staging/src/k8s.io/api/core/v1/types.go` |
| debt | 11540 | 2682 | 1 | `cluster/gce/util.sh` |
| mutation | 200684 | 8680 | 25 | `pkg/apis/core/validation/validation.go` |
| dead_code | 38500 | 8865 | 5 | `pkg/apis/core/validation/validation_test.go` |
| credential | 442 | 116 | 0 | `cmd/kubeadm/app/cmd/token_test.go` |
| threat | 47 | 19 | 0 | `cluster/gce/upgrade.sh` |
| ml_ai | 863 | 236 | 0 | `cluster/gce/util.sh` |
| ui | 440 | 194 | 0 | `test/images/agnhost/webhook/main.go` |

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

1. **doc.go** (`staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/doc.go`) — 3507 inbound connections
2. **doc.go** (`staging/src/k8s.io/api/core/v1/doc.go`) — 2389 inbound connections
3. **doc.go** (`staging/src/k8s.io/apimachinery/pkg/runtime/doc.go`) — 2255 inbound connections
4. **generated.pb.go** (`staging/src/k8s.io/apimachinery/pkg/runtime/schema/generated.pb.go`) — 1409 inbound connections
5. **doc.go** (`staging/src/k8s.io/apimachinery/pkg/types/doc.go`) — 1134 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **kubelet.go** (`pkg/kubelet/kubelet.go`) — 122 outbound dependencies
2. **clientset_generated.go** (`staging/src/k8s.io/client-go/kubernetes/fake/clientset_generated.go`) — 114 outbound dependencies
3. **server.go** (`cmd/kubelet/app/server.go`) — 104 outbound dependencies
4. **kubelet_test.go** (`pkg/kubelet/kubelet_test.go`) — 102 outbound dependencies
5. **instance.go** (`pkg/controlplane/instance.go`) — 85 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `Validate_UpdateTestStruct` **(Many-Argument Workhorses)** (@ `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/tags/update/zz_generated.validations.go`) -> Impact: **488.5** | LOC: 461
  * *Intent:* // Validate_UpdateTestStruct validates an instance of UpdateTestStruct according // to declarative validation rules in the API schema.
- `NewMainKubelet` **(Many-Argument Workhorses)** (@ `pkg/kubelet/kubelet.go`) -> Impact: **451.2** | LOC: 711
  * *Intent:* // NewMainKubelet instantiates a new Kubelet object along with all the required internal modules. // No initialization of Kubelet and its modules shou...
- `convertToAPIContainerStatuses` **(Many-Argument Workhorses)** (@ `pkg/kubelet/kubelet_pods.go`) -> Impact: **387.5** | LOC: 477
  * *Intent:* // convertToAPIContainerStatuses converts the given internal container // statuses into API container statuses.
- `ValidateCustomResourceDefinitionOpenAPISchema` **(Many-Argument Workhorses)** (@ `staging/src/k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/validation/validation.go`) -> Impact: **353.3** | LOC: 292
  * *Intent:* // ValidateCustomResourceDefinitionOpenAPISchema statically validates
- `Validate_T1` **(Many-Argument Workhorses)** (@ `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cross_pkg/zz_generated.validations.go`) -> Impact: **334.5** | LOC: 321
  * *Intent:* // Validate_T1 validates an instance of T1 according // to declarative validation rules in the API schema.
- `RunTestList` **(Many-Argument Workhorses)** (@ `staging/src/k8s.io/apiserver/pkg/storage/testing/store_tests.go`) -> Impact: **332.8** | LOC: 1734
- `registerResourceHandlers` **(Many-Argument Workhorses)** (@ `staging/src/k8s.io/apiserver/pkg/endpoints/installer.go`) -> Impact: **328.2** | LOC: 844
- `ValidatePersistentVolumeSpec` **(Many-Argument Workhorses)** (@ `pkg/apis/core/validation/validation.go`) -> Impact: **284.2** | LOC: 296
- `TestKubelet_HandlePodCleanups` **(Many-Argument Workhorses)** (@ `pkg/kubelet/kubelet_pods_test.go`) -> Impact: **276.5** | LOC: 1203
- `ValidateKubeletConfiguration` **(Many-Argument Workhorses)** (@ `pkg/kubelet/apis/config/validation/validation.go`) -> Impact: **272.3** | LOC: 353
  * *Intent:* // ValidateKubeletConfiguration validates `kc` and returns an error if it is invalid

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `cmd/kubeadm/app/util/pkiutil/testing/testdata` | 26 | 125000.0 | 0.0% | 0.0% |
| `staging/src/k8s.io/apiserver/plugin/pkg/authenticator/token/oidc/testdata` | 7 | 30000.01 | 0.87% | 0.0% |
| `staging/src/k8s.io/kube-aggregator/pkg/apiserver/testdata` | 11 | 20000.06 | 0.0% | 0.0% |
| `pkg/apis/core/validation` | 8 | 15139.46 | 15.11% | 25.12% |
| `pkg/kubelet` | 46 | 11763.02 | 13.98% | 46.13% |
| `pkg/kubelet/client/testdata` | 4 | 10000.0 | 0.0% | 0.0% |
| `pkg/kubelet/certificate/bootstrap/testdata` | 3 | 10000.0 | 0.0% | 0.0% |
| `test/e2e_node` | 95 | 9337.9 | 5.71% | 0.0% |
| `staging/src/k8s.io/client-go/applyconfigurations/core/v1` | 208 | 7912.74 | 6.7% | 96.85% |
| `pkg/kubelet/kuberuntime` | 42 | 6627.14 | 15.94% | 49.82% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `hack/golangci.yaml.in` -> **100.0%** Exposure
- `cluster/skeleton/util.sh` -> **100.0%** Exposure
- `hack/_update-generated-proto-bindings-dockerized.sh` -> **100.0%** Exposure
- `hack/_update-generated-protobuf-dockerized.sh` -> **100.0%** Exposure
- `hack/benchmark-go.sh` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `cluster/gce/config-common.sh` -> **100.0%** Exposure
- `cluster/gce/config-default.sh` -> **100.0%** Exposure
- `cluster/gce/config-test.sh` -> **100.0%** Exposure
- `cluster/gce/gci/configure-kubeapiserver.sh` -> **100.0%** Exposure
- `cluster/gce/gci/master-helper.sh` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `pkg/apis/core/validation/validation_test.go` -> **144** Orphaned Functions | **0** Duplicates
- `pkg/controller/podautoscaler/horizontal_test.go` -> **97** Orphaned Functions | **0** Duplicates
- `pkg/printers/internalversion/printers_test.go` -> **83** Orphaned Functions | **0** Duplicates
- `pkg/scheduler/testing/wrappers.go` -> **81** Orphaned Functions | **0** Duplicates
- `staging/src/k8s.io/apiserver/pkg/endpoints/apiserver_test.go` -> **77** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `staging/src/k8s.io/apiserver/pkg/server/options/encryptionconfig/testdata/valid-configs/aes/aes-cbc-multiple-keys-reversed.json` -> **100.0%** Exposure
- `staging/src/k8s.io/apiserver/pkg/server/options/encryptionconfig/testdata/valid-configs/aes/aes-cbc-multiple-keys.json` -> **100.0%** Exposure
- `staging/src/k8s.io/apiserver/pkg/server/options/encryptionconfig/testdata/valid-configs/aes/aes-cbc-multiple-providers-reversed.json` -> **100.0%** Exposure
- `staging/src/k8s.io/apiserver/pkg/server/options/encryptionconfig/testdata/valid-configs/aes/aes-cbc-multiple-providers.json` -> **100.0%** Exposure
- `cmd/kubeadm/app/apis/bootstraptoken/v1/utils_test.go` -> **100.0%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `26` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `83149` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `pkg/apis/core/validation/validation.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.6)
- **Top Global Matches:** file_cluster_4: 6.6, file_cluster_6: 9.187, file_cluster_15: 13.33
- **Magnitude:** 10153.66 | **LOC:** 9661 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **56** in-repo importer(s); it depends on **48**; blast radius 0.23; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (58.0%)
- **Documentation Coverage:** 56.0575% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ValidatePersistentVolumeSpec` **(Many-Argument Workhorses)** (Impact: 284.2)
  * `validateVolumeSource` **(Many-Argument Workhorses)** (Impact: 253.2)
  * `validateProjectionSources` **(Many-Argument Workhorses)** (Impact: 149.1)
  * `validateService` **(Many-Argument Workhorses)** (Impact: 110.9)
    * *Intent:* // ValidateService tests if required fields/annotations of a Service are valid.
  * `validateISCSIPersistentVolumeSource` **(Many-Argument Workhorses)** (Impact: 76.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 1381 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 4301
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2240`, `structural_boundaries: 1046`, `args: 347`, `func_start: 347`, `class_start: 5`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 1539`, `dead_code: 7`, `planned_debt: 24`, `fragile_debt: 1`, `unreferenced_by_name: 39`
* *Architecture:* `io: 1`, `api: 201`, `import: 1`
* *Defense:* `safety: 33`, `doc: 424`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.23
  * `Choke Point (Betweenness):` 2.9e-05 | `Ripple Effect (Closeness):` 0.007152
  * `Imports (Out-Degree: 32):` context, json, fmt, v1, equality, operation, resource, validate...
  * `Imported By (In-Degree: 56):` (Excluded from Brief to save tokens)

### `cmd/kube-apiserver/app/testing/testdata/127.0.0.1_10.0.0.1_kubernetes.default.svc-kubernetes.default-kubernetes-localhost.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/1.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/10.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/11.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/12.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/13.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/14.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/15.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/16.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/17.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/18.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/19.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/2.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/20.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/21.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/22.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/23.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/24.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/25.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/3.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/4.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/5.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/6.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cmd/kubeadm/app/util/pkiutil/testing/testdata/7.rsa.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `pkg/registry/core/persistentvolumeclaim/strategy_test.go` (GO) | Magnitude: 50.4 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 315, generics: 33, structural_boundaries: 14, pointers: 13
- `staging/src/k8s.io/api/certificates/v1alpha1/types_swagger_doc_generated.go` (GO) | Magnitude: 6.8 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 12, structural_boundaries: 10, doc: 4, args: 3
- `cmd/import-boss/main_test.go` (GO) | Magnitude: 97.18 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 251, structural_boundaries: 75, branch: 29, args: 10
- `staging/src/k8s.io/code-generator/cmd/validation-gen/testscheme/testscheme.go` (GO) | Magnitude: 163.66 | Delta: **0.114** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 216, structural_boundaries: 60, branch: 39, pointers: 38
- `staging/src/k8s.io/apiserver/pkg/cel/common/typeprovider_test.go` (GO) | Magnitude: 47.96 | Delta: **0.115** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 104, structural_boundaries: 30, branch: 11, args: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `staging/src/k8s.io/client-go/applyconfigurations/core/v1/envfromsource.go` (GO) | Magnitude: 17.32 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: doc: 14, pointers: 14, indent_tabs: 10, api: 8
- `staging/src/k8s.io/client-go/applyconfigurations/node/v1alpha1/runtimeclassspec.go` (GO) | Magnitude: 17.32 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: doc: 15, pointers: 14, indent_tabs: 10, api: 8
- `staging/src/k8s.io/apiserver/pkg/endpoints/discovery/util.go` (GO) | Magnitude: 39.26 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 51, structural_boundaries: 17, branch: 7, args: 7
- `staging/src/k8s.io/client-go/applyconfigurations/autoscaling/v2/metricidentifier.go` (GO) | Magnitude: 12.68 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: doc: 10, structural_boundaries: 8, pointers: 8, indent_tabs: 8
- `staging/src/k8s.io/apiserver/pkg/endpoints/filters/cachecontrol_test.go` (GO) | Magnitude: 11.74 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 47, branch: 4, structural_boundaries: 4, io: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `staging/src/k8s.io/kubectl/pkg/cmd/testing/util.go` (GO) | Magnitude: 49.18 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 145, pointers: 20, structural_boundaries: 18, args: 12
- `staging/src/k8s.io/metrics/pkg/client/custom_metrics/converter.go` (GO) | Magnitude: 33.78 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 60, structural_boundaries: 18, doc: 9, api: 8
- `pkg/scheduler/metrics/metric_recorder.go` (GO) | Magnitude: 145.64 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 98, structural_boundaries: 37, pointers: 22, doc: 21
- `staging/src/k8s.io/client-go/applyconfigurations/node/v1/scheduling.go` (GO) | Magnitude: 27.48 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 18, structural_boundaries: 13, doc: 9, api: 6
- `staging/src/k8s.io/client-go/applyconfigurations/node/v1alpha1/scheduling.go` (GO) | Magnitude: 27.48 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 18, structural_boundaries: 13, doc: 9, api: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `test/e2e/storage/pvc_storageclass.go` (GO) | Magnitude: 25.2 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 97, structural_boundaries: 13, branch: 7, closures: 7
- `cmd/kubeadm/app/util/config/resetconfiguration_test.go` (GO) | Magnitude: 44.74 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 163, structural_boundaries: 15, branch: 12, pointers: 8
- `staging/src/k8s.io/apimachinery/pkg/runtime/serializer/protobuf/collections.go` (GO) | Magnitude: 108.18 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 101, structural_boundaries: 30, state_mutation: 27, branch: 15
- `cluster/gce/config-common.sh` (SHELL) | Magnitude: 108.1 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 96, indent_spaces: 63, core_var_decl: 46, design_upper_case: 27
- `staging/src/k8s.io/cli-runtime/pkg/resource/query_param_verifier.go` (GO) | Magnitude: 76.36 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 87, structural_boundaries: 38, branch: 23, doc: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `pkg/controller/apis/config/scheme/scheme.go` (GO) | Magnitude: 8.2 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 11, api: 3, doc: 3, structural_boundaries: 2
- `staging/src/k8s.io/client-go/tools/cache/main_test.go` (GO) | Magnitude: 0.0 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 3, indent_tabs: 3, args: 1, func_start: 1
- `staging/src/k8s.io/client-go/tools/record/main_test.go` (GO) | Magnitude: 0.0 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 3, indent_tabs: 3, args: 1, func_start: 1
- `staging/src/k8s.io/kube-aggregator/pkg/apis/roundtrip_test.go` (GO) | Magnitude: 3.56 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 18, structural_boundaries: 2, args: 1, func_start: 1
- `cmd/kubeadm/app/cmd/main_test.go` (GO) | Magnitude: 2.76 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 3, structural_boundaries: 2, args: 1, func_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `pkg/proxy/ipvs/testing/fake_test.go` (GO) | Magnitude: 38.86 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 33, core_var_decl: 10, state_mutation: 9, safety_bypasses: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `test/images/agnhost/crd-conversion-webhook/main.go` (GO) | Magnitude: 11.56 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 33, pointers: 5, structural_boundaries: 4, api: 4
- `pkg/controlplane/apiserver/samples/generic/server/server.go` (GO) | Magnitude: 44.56 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 128, structural_boundaries: 27, branch: 16, safety: 12
- `cmd/kubeadm/app/cmd/upgrade/diff_test.go` (GO) | Magnitude: 55.32 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 151, structural_boundaries: 18, branch: 14, safety: 13
- `pkg/apis/rbac/v1/evaluation_helpers.go` (GO) | Magnitude: 108.78 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 84, structural_boundaries: 30, branch: 26, state_mutation: 11
- `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/tags/neq/neq/neqchained/doc_test.go` (GO) | Magnitude: 5.96 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 43, structural_boundaries: 11, pointers: 6, doc: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `pkg/probe/probe.go` (GO) | Magnitude: 19.16 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: api: 5, doc: 5, globals: 4, indent_tabs: 4
- `staging/src/k8s.io/apiextensions-apiserver/pkg/features/kube_features.go` (GO) | Magnitude: 4.7 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 21, doc: 8, globals: 4, structural_boundaries: 3
- `staging/src/k8s.io/kubectl/pkg/cmd/util/factory.go` (GO) | Magnitude: 16.48 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 19, doc: 11, structural_boundaries: 8, planned_debt: 2
- `staging/src/k8s.io/kubectl/pkg/scheme/install.go` (GO) | Magnitude: 2.7 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 55, structural_boundaries: 3, doc: 3, args: 1
- `staging/src/k8s.io/apimachinery/pkg/api/meta/interfaces.go` (GO) | Magnitude: 31.22 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 41, structural_boundaries: 21, doc: 20, api: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `test/e2e/storage/constants.go` (GO) | Magnitude: 15.12 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 2, state_mutation: 2, globals: 2, indent_tabs: 2
- `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/all_types_match/trivial/zz_generated.validations_test.go` (GO) | Magnitude: 0.14 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 2, indent_tabs: 2, args: 1, func_start: 1
- `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/all_types_match/with_field_validations/zz_generated.validations_test.go` (GO) | Magnitude: 0.14 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 2, indent_tabs: 2, args: 1, func_start: 1
- `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/all_types_match/with_type_validations/zz_generated.validations_test.go` (GO) | Magnitude: 0.14 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 2, indent_tabs: 2, args: 1, func_start: 1
- `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/cohorts/zz_generated.validations_test.go` (GO) | Magnitude: 0.14 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 2, indent_tabs: 2, args: 1, func_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `staging/src/k8s.io/apiserver/pkg/storage/testing/watcher_tests.go` (GO) | Magnitude: 721.42 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 1463, branch: 137, structural_boundaries: 94, pointers: 92
- `test/integration/controlplane/transformation/kmsv2_transformation_test.go` (GO) | Magnitude: 582.68 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 1026, branch: 164, safety: 83, structural_boundaries: 80
- `staging/src/k8s.io/kube-aggregator/pkg/apiserver/apiserver.go` (GO) | Magnitude: 252.44 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 406, structural_boundaries: 78, branch: 60, doc: 43
- `test/e2e/e2e.go` (GO) | Magnitude: 133.56 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 240, branch: 42, structural_boundaries: 34, doc: 32
- `staging/src/k8s.io/code-generator/cmd/validation-gen/validators/union.go` (GO) | Magnitude: 291.52 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 295, structural_boundaries: 89, branch: 56, state_mutation: 35

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `staging/src/k8s.io/apiserver/pkg/endpoints/filters/authentication_test.go` (GO) | Magnitude: 177.22 | Delta: **0.103** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 647, branch: 46, structural_boundaries: 39, closures: 32
- `staging/src/k8s.io/code-generator/cmd/validation-gen/output_tests/ratcheting/default_behavior/zz_generated.validations.go` (GO) | Magnitude: 25.61 | Delta: **0.167** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 292, structural_boundaries: 119, branch: 113, pointers: 108

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `cmd/kubeadm/app/cmd/upgrade/plan.go` (GO) | Magnitude: 234.56 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 253, structural_boundaries: 58, branch: 48, core_var_decl: 40
- `staging/src/k8s.io/kubectl/pkg/cmd/edit/testdata/test_editor.sh` (SHELL) | Magnitude: 0.01 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: io: 9, args: 6, ipc_rpc_bridges: 6, structural_boundaries: 5
- `staging/src/k8s.io/apiextensions-apiserver/hack/update-codegen.sh` (SHELL) | Magnitude: 24.6 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 11, safety: 5, state_mutation: 5
- `hack/verify-licenses.sh` (SHELL) | Magnitude: 77.58 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: structural_boundaries: 54, indent_spaces: 41, io: 30, branch: 18
- `test/e2e_node/lock_contention_linux_test.go` (GO) | Magnitude: 17.6 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 24, doc: 10, structural_boundaries: 4, closures: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `staging/src/k8s.io/component-helpers/node/topology/helpers.go` (GO) | Magnitude: 17.34 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 17, doc: 6, branch: 5, structural_boundaries: 5
- `pkg/probe/grpc/grpc.go` (GO) | Magnitude: 36.74 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 66, structural_boundaries: 17, branch: 11, io: 8
- `pkg/controller/endpointslicemirroring/endpointslicemirroring_controller_test.go` (GO) | Magnitude: 95.5 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 414, structural_boundaries: 35, pointers: 30, branch: 20
- `staging/src/k8s.io/apimachinery/pkg/runtime/serializer/codec_test.go` (GO) | Magnitude: 145.5 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 267, branch: 44, test: 40, pointers: 36
- `pkg/probe/exec/exec.go` (GO) | Magnitude: 19.02 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 34, structural_boundaries: 12, branch: 5, explicit_casts: 4

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `hack/golangci.yaml` -> Churn: **98.77%** | Cog Load: 4.4154% | Debt: 52.4981%
- `hack/golangci-hints.yaml` -> Churn: **95.42%** | Cog Load: 4.3735% | Debt: 65.0224%
- `staging/src/k8s.io/client-go/tools/cache/the_real_fifo.go` -> Churn: **63.43%** | Cog Load: 32.0782% | Debt: 85.237%
- `pkg/kubelet/cm/dra/manager.go` -> Churn: **63.37%** | Cog Load: 25.0178% | Debt: 56.9973%
- `cmd/kubeadm/app/constants/constants.go` -> Churn: **54.42%** | Cog Load: 22.8801% | Debt: 95.9482%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `staging/src/k8s.io/apimachinery/pkg/util/strategicpatch/patch.go` -> **Stephen Kitt** (100.0% isolated ownership) | Magnitude: 1791.16
- `cluster/gce/gci/configure-helper.sh` -> **Jordan Liggitt** (100.0% isolated ownership) | Magnitude: 1752.86
- `test/integration/apiserver/apiserver_test.go` -> **Mads Jensen** (100.0% isolated ownership) | Magnitude: 1592.22
- `pkg/controller/job/job_controller.go` -> **Michael Aspinwall** (100.0% isolated ownership) | Magnitude: 1526.5
- `staging/src/k8s.io/kubectl/pkg/cmd/apply/apply_test.go` -> **Manuel Grandeit** (100.0% isolated ownership) | Magnitude: 1440.18

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `staging/src/k8s.io/client-go/rest/client.go` -> **Severity: 0.042** (Bridge: 0.0004 * Flux: 99.886%)
- `staging/src/k8s.io/client-go/rest/request.go` -> **Severity: 0.037** (Bridge: 0.0004 * Flux: 99.9869%)
- `staging/src/k8s.io/client-go/rest/config.go` -> **Severity: 0.023** (Bridge: 0.0002 * Flux: 99.4429%)
- `staging/src/k8s.io/apimachinery/pkg/runtime/serializer/codec_factory.go` -> **Severity: 0.017** (Bridge: 0.0002 * Flux: 99.74%)
- `test/utils/ktesting/tcontext.go` -> **Severity: 0.009** (Bridge: 0.0001 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `staging/src/k8s.io/apimachinery/pkg/util/validation/field/error_matcher.go` -> **Severity: 4.877** (Embedded: 0.0893 * Error Risk: 54.6056%)
- `staging/src/k8s.io/apimachinery/pkg/util/runtime/runtime.go` -> **Severity: 4.598** (Embedded: 0.0883 * Error Risk: 52.0743%)
- `staging/src/k8s.io/apimachinery/pkg/watch/watch.go` -> **Severity: 4.107** (Embedded: 0.0647 * Error Risk: 63.4487%)
- `staging/src/k8s.io/apimachinery/pkg/api/errors/errors.go` -> **Severity: 3.625** (Embedded: 0.0636 * Error Risk: 56.9811%)
- `staging/src/k8s.io/apimachinery/pkg/labels/labels.go` -> **Severity: 3.598** (Embedded: 0.0655 * Error Risk: 54.9084%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `staging/src/k8s.io/apimachinery/pkg/util/validation/field/error_matcher_test.go` -> **Severity: 905.1** (Blast Radius: 9.051 * Doc Risk: 100.0%)
- `staging/src/k8s.io/apimachinery/pkg/runtime/serializer/cbor/internal/modes/buffers.go` -> **Severity: 204.7** (Blast Radius: 2.047 * Doc Risk: 100.0%)
- `hack/lib/init.sh` -> **Severity: 185.0** (Blast Radius: 1.85 * Doc Risk: 100.0%)
- `staging/src/k8s.io/component-base/featuregate/feature_gate.go` -> **Severity: 160.637** (Blast Radius: 3.707 * Doc Risk: 43.3333%)
- `staging/src/k8s.io/apimachinery/pkg/util/validation/field/error_matcher.go` -> **Severity: 154.897** (Blast Radius: 10.533 * Doc Risk: 14.7059%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 3450 literal sites + 20 sites through wrappers = 3470
- **`panics_and_aborts`:** 2756 literal sites + 30 sites through wrappers = 2786

- `skipInternalf` (function, panics_and_aborts, primitive): 23 call sites in 1 files -- `test/e2e/framework/skipper/skipper.go`
- `printSuccess` (function, debug_prints, primitive): 10 call sites in 1 files -- `test/e2e_node/environment/conformance.go`
- `printError` (function, debug_prints, primitive): 7 call sites in 1 files -- `test/e2e_node/environment/conformance.go`
- `Failf` (function, panics_and_aborts, primitive): 4 call sites in 2 files -- `test/e2e/framework/log.go`
- `error` (function, debug_prints, primitive): 3 call sites in 3 files -- `cluster/addons/addon-manager/kube-addons-test.sh`
- `generatePanicFunc` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `pkg/util/goroutinemap/goroutinemap_test.go`
- `startHTTPServer` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `test/images/agnhost/guestbook/guestbook.go`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 329505 call pairs -- scoped 29.1%, unique 3.3%, ambiguous 49.9%, external 17.7%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| go | 324124 | 29.3% | 3.3% | 50.7% | 16.7% |
| shell | 4936 | 15.7% | 5.2% | 1.0% | 78.1% |
| powershell | 253 | 19.8% | 22.9% | 0.0% | 57.3% |
| python | 192 | 11.5% | 0.0% | 0.0% | 88.5% |

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
