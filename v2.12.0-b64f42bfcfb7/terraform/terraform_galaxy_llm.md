# ARCHITECTURAL_BRIEF: terraform
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/hashicorp/terraform` |
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
- **Scope:** 2411 analyzed artifact(s), 495217 LOC.
- **Load-bearing artifact:** `internal/addrs/doc.go` -- 577 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `internal/command/command_test.go` -- pulls in 45 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `internal/backend/remote-state/http/testdata/certs/ca.key` at magnitude 5000.0 (structural weight, not risk).
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
| Total Artifacts | 5161 |
| Analyzed Artifacts (Scanned) | 2411 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2750 |
| Total LOC | 495217 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 46.7% |
| Dominant Lang | GO |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5378 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0887 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 8.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.7251 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 133 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| GO | 1844 | 468551 | 76.5% |
| JSON | 379 | 23504 | 15.7% |
| PLAINTEXT | 101 | 7 | 4.2% |
| MARKDOWN | 30 | 0 | 1.2% |
| SHELL | 19 | 564 | 0.8% |
| YAML | 17 | 1237 | 0.7% |
| PROTO | 9 | 1299 | 0.4% |
| XML | 9 | 0 | 0.4% |
| DOCKERFILE | 2 | 32 | 0.1% |
| MAKEFILE | 1 | 23 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 2404 |
| unknown | unknown | 7 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 27%, Callbacks & Closures Files 16%, Large Core Modules 13%, Compute Cores Files 12%, Large Core Modules (3) 10%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 2278 | 94.5% |
| Unknown | 7 | 0.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 124 | 5.1% |
| Static: Minified & Vendor Opaque Mass | 2 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2750*

**Composition by Extension & Reason:**
- `.tf`: 1631x Excluded (Unsupported Extension: '.tf'), 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.hcl`: 448x Excluded (Unsupported Extension: '.hcl'), 44x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 153x Unsupported Format (.undeterminable), 42x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Unsupported Extension: '.0_SHA256SUMS')
- `.tfstate`: 146x Excluded (Unsupported Extension: '.tfstate'), 42x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.go`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded (Machine-Generated Source Code Signature: 30 LOC), 3x Excluded (Machine-Generated Source Code Signature: 27 LOC)
- `.json`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 1547 LOC), 1x Excluded (Static Asset Blob without Intent: 1548 LOC)
- `.md`: 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 17x Excluded (Explicitly Denied Extension: '.png')
- `.tfvars`: 15x Excluded (Unsupported Extension: '.tfvars')
- `.zip`: 12x Excluded (Explicitly Denied Extension: '.zip')
- `.mod`: 11x Unsupported Format (.mod)
- `.sum`: 11x Excluded (Unsupported Extension: '.sum')
- `.log`: 4x Excluded (Saturation: Line 2 exceeds 500 chars), 3x Excluded (Saturation: Line 5 exceeds 500 chars), 2x Excluded (Saturation: Line 20 exceeds 500 chars)
- `.tmpl`: 8x Excluded (Unsupported Extension: '.tmpl')
- `.proto`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 89.3 | 10.5 | 5.7 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 96.5 | 32.0 | 49.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 35.9 | 28.4 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 14.0 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 5.4 | 4.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 42.0 | 19.5 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 23.1 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 4.3 | 0.3 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 5.2 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 50.1 | 50.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 5652 | 887 | 5 | `internal/terraform/context_apply_test.go` |
| cleanup | 486 | 203 | 0 | `internal/communicator/ssh/communicator.go` |
| guards | 11324 | 1383 | 12 | `internal/terraform/terraform_test.go` |
| danger | 2356 | 478 | 2 | `internal/cloud/tfe_client_mock.go` |
| concurrency | 2351 | 280 | 2 | `internal/terraform/context_apply_test.go` |
| connectivity | 17513 | 1657 | 18 | `internal/providers/provider.go` |
| io | 649 | 197 | 0 | `.github/scripts/equivalence-test.sh` |
| crypto | 0 | 0 | 0 | - |
| ipc | 123 | 42 | 0 | `internal/command/clistate/local_state_lock_windows.go` |
| time | 449 | 136 | 0 | `internal/stacks/stackruntime/plan_test.go` |
| serialization | 203 | 96 | 0 | `internal/command/state_identities_test.go` |
| regex | 86 | 36 | 0 | `internal/rpcapi/dynrpcserver/generator/main.go` |
| events | 112 | 30 | 0 | `internal/backend/remote-state/s3/client.go` |
| tests | 7176 | 678 | 7 | `internal/plugin6/grpc_provider_test.go` |
| docs | 22838 | 1859 | 24 | `internal/command/meta_backend_test.go` |
| debt | 1154 | 397 | 1 | `internal/cloud/tfe_client_mock.go` |
| mutation | 45987 | 1430 | 43 | `internal/terraform/context_apply_test.go` |
| dead_code | 7789 | 1612 | 7 | `internal/terraform/context_apply_test.go` |
| credential | 58 | 37 | 0 | `internal/lang/funcs/crypto_test.go` |
| threat | 4 | 3 | 0 | `internal/terraform/context_apply2_test.go` |
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

1. **doc.go** (`internal/addrs/doc.go`) — 577 inbound connections
2. **doc.go** (`internal/tfdiags/doc.go`) — 565 inbound connections
3. **doc.go** (`internal/providers/doc.go`) — 269 inbound connections
4. **doc.go** (`internal/states/doc.go`) — 252 inbound connections
5. **doc.go** (`internal/plans/doc.go`) — 224 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **command_test.go** (`internal/command/command_test.go`) — 45 outbound dependencies
2. **init_test.go** (`internal/command/init_test.go`) — 42 outbound dependencies
3. **meta_backend.go** (`internal/command/meta_backend.go`) — 38 outbound dependencies
4. **meta_backend_test.go** (`internal/command/meta_backend_test.go`) — 36 outbound dependencies
5. **stacks_test.go** (`internal/rpcapi/stacks_test.go`) — 36 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `TestContextPlan_actions` **(Many-Argument Workhorses)** (@ `internal/terraform/context_plan_actions_test.go`) -> Impact: **616.2** | LOC: 4291
- `TestEnsureProviderVersions` **(Many-Argument Workhorses)** (@ `internal/providercache/installer_test.go`) -> Impact: **244.6** | LOC: 2403
- `EnsureProviderVersions` **(Many-Argument Workhorses)** (@ `internal/providercache/installer.go`) -> Impact: **228.4** | LOC: 544
  * *Intent:* // The given mode modifies how the operation will treat providers that already // have acceptable versions available in the target cache directory. Se...
- `plan` **(Many-Argument Workhorses)** (@ `internal/terraform/node_resource_abstract_instance.go`) -> Impact: **200.1** | LOC: 572
- `opApply` **(Many-Argument Workhorses)** (@ `internal/backend/local/backend_apply.go`) -> Impact: **194.2** | LOC: 440
- `TestShimSchemaMap_Diff` **(Many-Argument Workhorses)** (@ `internal/legacy/helper/schema/shims_test.go`) -> Impact: **187.1** | LOC: 2979
- `validateProviderConfigs` **(Many-Argument Workhorses)** (@ `internal/configs/provider_validation.go`) -> Impact: **175.5** | LOC: 510
  * *Intent:* // however will generate an error if a suitable provider configuration is not // passed in through the module call. // // The parentCall argument is t...
- `TestSchemaMap_Diff` **(Many-Argument Workhorses)** (@ `internal/legacy/helper/schema/schema_test.go`) -> Impact: **175.3** | LOC: 3053
- `backendFromConfig` **(Many-Argument Workhorses)** (@ `internal/command/meta_backend.go`) -> Impact: **167.7** | LOC: 440
  * *Intent:* // backendFromConfig returns the initialized (not configured) backend // directly from the config/state.. // // This function handles various edge cas...
- `apply` **(Many-Argument Workhorses)** (@ `internal/terraform/node_resource_abstract_instance.go`) -> Impact: **148.8** | LOC: 383
  * *Intent:* // apply accepts an applyConfig, instead of using n.Config, so destroy plans can // send a nil config. The keyData information can be empty if the con...

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `internal/terraform` | 239 | 38433.06 | 12.38% | 47.65% |
| `internal/command` | 120 | 20877.48 | 13.72% | 51.95% |
| `internal/backend/remote-state/http/testdata/certs` | 3 | 15000.0 | 0.0% | 0.0% |
| `internal/cloud` | 40 | 9074.36 | 19.53% | 40.78% |
| `internal/configs` | 58 | 8588.14 | 13.67% | 40.87% |
| `internal/stacks/stackruntime/internal/stackeval` | 71 | 7302.82 | 13.65% | 66.44% |
| `internal/legacy/helper/schema` | 40 | 7212.34 | 15.02% | 16.93% |
| `internal/addrs` | 63 | 5057.66 | 8.52% | 52.88% |
| `internal/pluginshared/testdata` | 2 | 5000.0 | 0.0% | 0.0% |
| `internal/releaseauth/testdata` | 2 | 5000.0 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `internal/addrs/map.go` -> **100.0%** Exposure
- `internal/command/jsonformat/computed/renderers/util.go` -> **100.0%** Exposure
- `internal/experiments/experiment.go` -> **100.0%** Exposure
- `internal/experiments/set.go` -> **100.0%** Exposure
- `internal/instances/set.go` -> **100.0%** Exposure
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
- `internal/communicator/ssh/communicator_test.go` -> **98.8911%** Exposure
- `internal/backend/remote-state/oci/backend_test.go` -> **78.1342%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `18` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `12267` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `internal/backend/remote-state/http/testdata/certs/ca.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/backend/remote-state/http/testdata/certs/client.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/backend/remote-state/http/testdata/certs/server.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/pluginshared/testdata/archives/terraform-cloudplugin_0.1.0_SHA256SUMS.sig` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/pluginshared/testdata/sample.private.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/releaseauth/testdata/sample.private.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/releaseauth/testdata/sample_release/sample_0.1.0_SHA256SUMS.sig` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/terraform/context_apply_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.581)
- **Top Global Matches:** file_cluster_15: 7.581, file_cluster_16: 8.312, file_cluster_9: 8.5
- **Magnitude:** 4825.76 | **LOC:** 12905 | **CtrlFlow:** 9.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **28**; blast radius 0.22; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.3%), Debt Markers (formerly Tech Debt) (63.8%), Guard Balance (formerly Safety Score) (57.7%), Complexity Load (formerly Cognitive Load) (21.0%)
- **Documentation Coverage:** 84.1629% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TestContext2Apply_scaleInCBD` **(I/O & Config Routines)** (Impact: 45.4)
  * `TestContext2Apply_multiDepose_createBeforeDestroy` **(Compute Cores)** (Impact: 35.8)
  * `TestContext2Apply_stop` **(Compute Cores)** (Impact: 30.1)
  * `TestContext2Apply_ProviderMeta_refreshdata_set` **(Compute Cores)** (Impact: 28.7)
  * `TestContext2Apply_taintedDestroyFailure` **(I/O & Config Routines)** (Impact: 27.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 7 instances
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 421 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 87
* *Memory Alloc (weighted view):* 26
* *State Mutation (weighted view):* 1969
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 964`, `structural_boundaries: 766`, `args: 216`, `func_start: 216`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 2`, `state_mutation: 1127`, `dead_code: 4`, `planned_debt: 1`, `fragile_debt: 4`, `unreferenced_by_name: 212`
* *Architecture:* `api: 269`, `concurrency: 17`, `import: 1`
* *Defense:* `safety: 24`, `doc: 208`, `test: 224`, `sync_locks: 83`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 21):` bytes, json, errors, fmt, spew, deep, cmp, addrs...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/terraform/context_plan_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.51)
- **Top Global Matches:** file_cluster_9: 6.51, file_cluster_15: 8.016, file_cluster_16: 8.671
- **Magnitude:** 2378.02 | **LOC:** 7164 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **23**; blast radius 0.22; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (66.8%), Mutation Surface (formerly State Flux) (61.6%), Guard Balance (formerly Safety Score) (51.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (26.5%)
- **Documentation Coverage:** 92.5094% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TestContext2Plan_countIncreaseFromOneCorrupted` **(Compute Cores)** (Impact: 28.4)
    * *Intent:* // https://github.com/PeoplePerHour/terraform/pull/11 // // This tests a case where both a "resource...
  * `TestContext2Plan_countDecreaseToOne` **(Compute Cores)** (Impact: 27.5)
  * `TestContext2Plan_createBeforeDestroy_depends_datasource` **(Compute Cores)** (Impact: 26.3)
  * `TestContext2Plan_countIncreaseWithSplatReference` **(Compute Cores)** (Impact: 26.2)
    * *Intent:* // A common pattern in TF configs is to have a set of resources with the same // count and to use co...
  * `TestContext2Plan_countIncreaseFromNotSet` **(Compute Cores)** (Impact: 25.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 77 instances
* *State Mutation (weighted view):* 444
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 800`, `structural_boundaries: 643`, `args: 133`, `func_start: 133`, `class_start: 1`
* *Risk/State:* `state_mutation: 290`, `planned_debt: 1`, `unreferenced_by_name: 131`
* *Architecture:* `api: 142`, `import: 1`
* *Defense:* `safety: 74`, `doc: 49`, `test: 138`, `sync_locks: 15`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` bytes, errors, fmt, spew, cmp, addrs, configschema, hcl2shim...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/command/meta_backend.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.547)
- **Top Global Matches:** file_cluster_8: 7.547, file_cluster_6: 10.785, file_cluster_4: 19.173
- **Magnitude:** 2036.64 | **LOC:** 3408 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 58.8%
- **Blast Radius:** changing it is visible to **36** in-repo importer(s); it depends on **38**; blast radius 1.055; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.6%)
- **Documentation Coverage:** 42.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `backendFromConfig` **(Many-Argument Workhorses)** (Impact: 167.7)
    * *Intent:* // backendFromConfig returns the initialized (not configured) backend // directly from the config/st...
  * `stateStore_C_s` **(Many-Argument Workhorses)** (Impact: 95.2)
    * *Intent:* // State Store Config Scenarios // The functions below cover handling all the various scenarios that...
  * `backend_C_r_s` **(Many-Argument Workhorses)** (Impact: 79.9)
    * *Intent:* // Configuring a backend for the first time.
  * `backend_C_r_S_changed` **(Many-Argument Workhorses)** (Impact: 72.4)
    * *Intent:* // Changing a previously saved backend.
  * `BackendForLocalPlan` **(Many-Argument Workhorses)** (Impact: 61.9)
    * *Intent:* // BackendForLocalPlan is similar to Backend, but uses settings that were // stored in a plan when p...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 8 instances
* *Amplified Cascading Flux:* 293 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 887
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 490`, `structural_boundaries: 317`, `args: 35`, `func_start: 35`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 10`, `state_mutation: 301`, `planned_debt: 3`, `fragile_debt: 21`, `unreferenced_by_name: 5`
* *Architecture:* `api: 14`, `import: 1`
* *Defense:* `safety: 110`, `doc: 259`, `sync_locks: 10`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.055
  * `Choke Point (Betweenness):` 0.000775 | `Ripple Effect (Closeness):` 0.019942
  * `Imports (Out-Degree: 29):` bytes, context, json, errors, fmt, go-version, v2, hcldec...
  * `Imported By (In-Degree: 36):` (Excluded from Brief to save tokens)

### `internal/terraform/context_plan2_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.093)
- **Top Global Matches:** file_cluster_4: 7.093, file_cluster_6: 9.31, file_cluster_9: 12.99
- **Magnitude:** 2013.12 | **LOC:** 7939 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 80.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **23**; blast radius 0.22; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (73.5%), Guard Balance (formerly Safety Score) (52.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (39.6%), Debt Markers (formerly Tech Debt) (37.3%)
- **Documentation Coverage:** 91.7647% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TestContext2Plan_resourcePreconditionPostcondition` **(Many-Argument Workhorses)** (Impact: 63.5)
  * `TestContext2Plan_dataSourcePreconditionPostcondition` **(Compute Cores)** (Impact: 60.6)
  * `TestContext2Plan_refreshOnlyMode_orphan` **(Compute Cores)** (Impact: 42.4)
  * `TestContext2Plan_refreshOnlyMode_deposed` **(Compute Cores)** (Impact: 40.9)
  * `TestContext2Plan_refreshOnlyMode` **(Compute Cores)** (Impact: 39.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 580
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 512`, `structural_boundaries: 510`, `args: 85`, `func_start: 85`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 520`, `fragile_debt: 3`, `unreferenced_by_name: 85`
* *Architecture:* `api: 85`, `import: 1`
* *Defense:* `safety: 19`, `doc: 107`, `test: 143`, `sync_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 20):` bytes, errors, fmt, spew, cmp, v2, addrs, checks...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/terraform/node_resource_abstract_instance.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.498)
- **Top Global Matches:** file_cluster_6: 7.498, file_cluster_8: 9.981, file_cluster_4: 15.188
- **Magnitude:** 1904.52 | **LOC:** 3129 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 91.7%
- **Blast Radius:** changing it is visible to **23** in-repo importer(s); it depends on **22**; blast radius 1.093; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (92.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.7%)
- **Documentation Coverage:** 80.3571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `plan` **(Many-Argument Workhorses)** (Impact: 200.1)
  * `apply` **(Many-Argument Workhorses)** (Impact: 148.8)
    * *Intent:* // apply accepts an applyConfig, instead of using n.Config, so destroy plans can // send a nil confi...
  * `applyProvisioners` **(Many-Argument Workhorses)** (Impact: 89.3)
    * *Intent:* // applyProvisioners executes the provisioners for a resource.
  * `processIgnoreChangesIndividual` **(Many-Argument Workhorses)** (Impact: 71.7)
  * `refresh` **(Many-Argument Workhorses)** (Impact: 69.2)
    * *Intent:* // refresh does a refresh for a resource // if the second return value is non-nil, the refresh is de...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 226 instances
* *State Mutation (weighted view):* 719
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 415`, `structural_boundaries: 252`, `args: 45`, `func_start: 45`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 11`, `state_mutation: 267`, `planned_debt: 2`, `fragile_debt: 34`, `unreferenced_by_name: 17`
* *Architecture:* `api: 15`, `import: 1`
* *Defense:* `safety: 15`, `doc: 208`, `test: 6`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.093
  * `Choke Point (Betweenness):` 0.000542 | `Ripple Effect (Closeness):` 0.009612
  * `Imports (Out-Degree: 25):` fmt, v2, terraform-registry-address, addrs, checks, configs, configschema, instances...
  * `Imported By (In-Degree: 23):` (Excluded from Brief to save tokens)

### `internal/cloud/tfe_client_mock.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.189)
- **Top Global Matches:** file_cluster_15: 7.189, file_cluster_10: 8.223, file_cluster_16: 8.839
- **Magnitude:** 1686.64 | **LOC:** 2603 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **24** in-repo importer(s); it depends on **16**; blast radius 1.295; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Debt Markers (formerly Tech Debt) (90.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.0%)
- **Documentation Coverage:** 98.4802% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ReadWithOptions` **(Many-Argument Workhorses)** (Impact: 49.3)
  * `List` **(Many-Argument Workhorses)** (Impact: 46.3)
  * `Create` **(Many-Argument Workhorses)** (Impact: 36.1)
  * `Logs` **(Many-Argument Workhorses)** (Impact: 31.6)
  * `Create` **(Many-Argument Workhorses)** (Impact: 26.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 159 instances
* *High Risk Execution (weighted view):* 59
* *State Mutation (weighted view):* 512
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 269`, `structural_boundaries: 412`, `args: 178`, `func_start: 178`, `class_start: 21`
* *Risk/State:* `high_risk_execution: 60`, `state_mutation: 194`, `planned_debt: 47`, `unreferenced_by_name: 43`
* *Architecture:* `io: 14`, `api: 196`, `import: 1`
* *Defense:* `safety: 26`, `doc: 22`, `test: 32`, `sync_locks: 38`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.295
  * `Choke Point (Betweenness):` 0.00013 | `Ripple Effect (Closeness):` 0.023532
  * `Imports (Out-Degree: 3):` bytes, context, base64, errors, fmt, go-tfe, copy, version...
  * `Imported By (In-Degree: 24):` (Excluded from Brief to save tokens)

### `internal/command/test_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.64)
- **Top Global Matches:** file_cluster_4: 7.64, file_cluster_9: 8.364, file_cluster_15: 9.999
- **Magnitude:** 1677.16 | **LOC:** 6087 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 40.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **33**; blast radius 0.22; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (89.4%), Guard Balance (formerly Safety Score) (53.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (46.9%), Concurrency Surface (formerly Concurrency) (22.9%)
- **Documentation Coverage:** 87.7193% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TestTest_Runs` **(I/O & Config Routines)** (Impact: 59.8)
  * `TestTest_ParallelTeardown` **(Many-Argument Workhorses)** (Impact: 57.8)
  * `TestTest_Parallel_Divided_Order` **(Compute Cores)** (Impact: 39.2)
  * `TestTest_SkipCleanup_FileLevelFlag` **(I/O & Config Routines)** (Impact: 27.5)
  * `TestTest_UseOfBackends_whenStateArtifactsAreMade` **(Compute Cores)** (Impact: 27.2)
    * *Intent:* // Testing whether a state artifact is made for a run block with a backend or not // // Artifacts ar...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 128 instances
* *Concurrency (weighted view):* 48
* *State Mutation (weighted view):* 550
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 404`, `structural_boundaries: 293`, `args: 59`, `func_start: 59`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 294`, `unreferenced_by_name: 55`
* *Architecture:* `io: 4`, `api: 57`, `concurrency: 8`, `import: 1`
* *Defense:* `safety: 18`, `doc: 115`, `test: 178`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` bytes, context, json, errors, fmt, cmp, cmpopts, cli...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/command/init_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.952)
- **Top Global Matches:** file_cluster_4: 5.952, file_cluster_6: 10.424, file_cluster_15: 11.238
- **Magnitude:** 1519.82 | **LOC:** 6300 | **CtrlFlow:** 8.6% | **Authorship Centralization:** 58.8%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **42**; blast radius 0.718; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Guard Balance (formerly Safety Score) (49.2%), Mutation Surface (formerly State Flux) (47.1%), Debt Markers (formerly Tech Debt) (42.3%)
- **Documentation Coverage:** 73.3766% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TestInit_stateStore_configChanges` **(Many-Argument Workhorses)** (Impact: 62.6)
    * *Intent:* // Testing init's behaviors with `state_store` when run in a working directory where the configurati...
  * `TestInit_stateStore_newWorkingDir` **(I/O & Config Routines)** (Impact: 51.3)
    * *Intent:* // Testing init's behaviors with `state_store` when run in an empty working directory
  * `TestInit_backend_to_stateStore_multipleWorkspaces` **(I/O & Config Routines)** (Impact: 40.7)
  * `TestInit_backendCloudInvalidOptions` **(I/O & Config Routines)** (Impact: 36.9)
  * `TestInit_backend_to_stateStore_singleWorkspace` **(I/O & Config Routines)** (Impact: 35.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 10 instances
* *Amplified Cascading Flux:* 84 instances
* *Memory Alloc (weighted view):* 69
* *State Mutation (weighted view):* 291
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 438`, `structural_boundaries: 270`, `args: 81`, `func_start: 81`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 123`, `planned_debt: 4`, `fragile_debt: 1`, `unreferenced_by_name: 71`
* *Architecture:* `io: 11`, `api: 79`, `concurrency: 2`, `import: 1`
* *Defense:* `safety: 93`, `doc: 275`, `test: 141`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.718
  * `Choke Point (Betweenness):` 0.000359 | `Ripple Effect (Closeness):` 0.007703
  * `Imports (Out-Degree: 31):` bytes, context, json, fmt, spew, cmp, cli, go-version...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `internal/plugin6/grpc_provider.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.095)
- **Top Global Matches:** file_cluster_4: 7.095, file_cluster_6: 8.077, file_cluster_15: 13.646
- **Magnitude:** 1483.38 | **LOC:** 2090 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **20**; blast radius 0.24; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (88.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.4%)
- **Documentation Coverage:** 98.75% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ListResource` **(Compute Cores)** (Impact: 43.4)
  * `PlanResourceChange` **(Compute Cores)** (Impact: 35.8)
  * `ReadStateBytes` **(Compute Cores)** (Impact: 31.7)
  * `ApplyResourceChange` **(Defensive Guards)** (Impact: 30.6)
  * `GetProviderSchema` **(I/O & Config Routines)** (Impact: 30.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 284 instances
* *Concurrency (weighted view):* 18
* *Memory Alloc (weighted view):* 13
* *State Mutation (weighted view):* 863
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 268`, `structural_boundaries: 303`, `args: 42`, `func_start: 42`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 295`, `planned_debt: 2`, `fragile_debt: 10`, `unreferenced_by_name: 33`
* *Architecture:* `io: 6`, `api: 44`, `concurrency: 3`, `import: 1`
* *Defense:* `safety: 92`, `doc: 51`, `test: 3`, `sync_locks: 5`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.24
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000415
  * `Imports (Out-Degree: 5):` bytes, context, errors, fmt, go-plugin, v2, addrs, logging...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `internal/terraform/context_apply2_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.462)
- **Top Global Matches:** file_cluster_15: 7.462, file_cluster_16: 8.148, file_cluster_2: 8.168
- **Magnitude:** 1477.16 | **LOC:** 4956 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **27**; blast radius 0.22; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.5%), Guard Balance (formerly Safety Score) (57.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (55.7%), Debt Markers (formerly Tech Debt) (39.0%)
- **Documentation Coverage:** 87.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TestContext2Apply_resourceConditionApplyTimeFail` **(Compute Cores)** (Impact: 37.4)
  * `TestContext2Apply_resourcePostcondition` **(Compute Cores)** (Impact: 29.5)
  * `TestContext2Apply_deprecatedOutputsAndVariables` **(I/O & Config Routines)** (Impact: 27.1)
  * `TestApply_updateDependencies` **(I/O & Config Routines)** (Impact: 22.6)
    * *Intent:* // verify that dependencies are updated in the state during refresh and apply
  * `TestContext2Apply_outputValuePrecondition` **(Compute Cores)** (Impact: 22.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 99 instances
* *State Mutation (weighted view):* 693
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 235`, `structural_boundaries: 326`, `args: 56`, `func_start: 56`
* *Risk/State:* `state_mutation: 495`, `dead_code: 1`, `fragile_debt: 1`, `unreferenced_by_name: 56`
* *Architecture:* `api: 56`, `import: 1`
* *Defense:* `safety: 6`, `doc: 65`, `test: 65`, `sync_locks: 3`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 21):` bytes, errors, fmt, spew, cmp, v2, addrs, checks...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/terraform/context_validate_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.486)
- **Top Global Matches:** file_cluster_15: 7.486, file_cluster_2: 8.271, file_cluster_16: 8.428
- **Magnitude:** 1439.44 | **LOC:** 5411 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 0.22; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (74.0%), Guard Balance (formerly Safety Score) (55.5%), Debt Markers (formerly Tech Debt) (34.8%)
- **Documentation Coverage:** 90.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TestContext2Validate_providerContributedFunctions` **(Compute Cores)** (Impact: 61.8)
  * `TestContext2Validate_deprecatedAttr` **(I/O & Config Routines)** (Impact: 31.9)
  * `TestContext2Validate_action` **(I/O & Config Routines)** (Impact: 27.1)
    * *Intent:* // Action Validation is largely exercised in context_plan_actions_test.go
  * `TestContext2Validate_queryList` **(I/O & Config Routines)** (Impact: 21.9)
  * `TestContext2Validate_varSensitive` **(Compute Cores)** (Impact: 11.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 42 instances
* *State Mutation (weighted view):* 651
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 165`, `structural_boundaries: 439`, `args: 90`, `func_start: 90`
* *Risk/State:* `state_mutation: 567`, `unreferenced_by_name: 90`
* *Architecture:* `api: 90`, `import: 1`
* *Defense:* `doc: 60`, `test: 106`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` errors, fmt, cmp, v2, addrs, configs, configschema, plans...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/legacy/helper/schema/schema.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.447)
- **Top Global Matches:** file_cluster_8: 5.447, file_cluster_6: 15.069, file_cluster_3: 21.806
- **Magnitude:** 1239.56 | **LOC:** 1780 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **11**; blast radius 2.877; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.6%), Complexity Load (formerly Cognitive Load) (31.8%)
- **Documentation Coverage:** 60.6557% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `internalValidate` **(Many-Argument Workhorses)** (Impact: 122.3)
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
* *Structure:* `branch: 367`, `structural_boundaries: 295`, `args: 32`, `func_start: 32`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 95`, `planned_debt: 3`, `fragile_debt: 1`, `unreferenced_by_name: 9`
* *Architecture:* `api: 47`, `import: 1`
* *Defense:* `safety: 28`, `doc: 166`, `sync_locks: 6`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.877
  * `Choke Point (Betweenness):` 0.000292 | `Ripple Effect (Closeness):` 0.020486
  * `Imports (Out-Degree: 4):` fmt, hcl2shim, terraform, copystructure, mapstructure, os, reflect, regexp...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `internal/plugin/grpc_provider.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.667)
- **Top Global Matches:** file_cluster_4: 6.667, file_cluster_6: 9.508, file_cluster_15: 12.4
- **Magnitude:** 1216.06 | **LOC:** 1677 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **18**; blast radius 0.248; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (91.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.5%)
- **Documentation Coverage:** 98.6842% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ListResource` **(Compute Cores)** (Impact: 43.4)
  * `PlanResourceChange` **(Compute Cores)** (Impact: 35.7)
  * `ApplyResourceChange` **(Defensive Guards)** (Impact: 30.6)
  * `GetProviderSchema` **(I/O & Config Routines)** (Impact: 29.2)
  * `ReadResource` **(Defensive Guards)** (Impact: 25.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 233 instances
* *Concurrency (weighted view):* 6
* *Memory Alloc (weighted view):* 11
* *State Mutation (weighted view):* 706
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 221`, `structural_boundaries: 241`, `args: 39`, `func_start: 39`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 9`, `state_mutation: 240`, `planned_debt: 2`, `fragile_debt: 6`, `unreferenced_by_name: 32`
* *Architecture:* `io: 4`, `api: 43`, `concurrency: 1`, `import: 1`
* *Defense:* `safety: 78`, `doc: 37`, `test: 3`, `sync_locks: 3`, `immutability_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.248
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000746
  * `Imports (Out-Degree: 6):` context, errors, fmt, go-plugin, addrs, logging, convert, providers...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `internal/plans/planfile/tfplan.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.631)
- **Top Global Matches:** file_cluster_8: 5.631, file_cluster_6: 12.01, file_cluster_4: 20.667
- **Magnitude:** 1212.12 | **LOC:** 1470 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 55.6%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **18**; blast radius 0.316; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (57.6%)
- **Documentation Coverage:** 54.5455% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `readTfplan` **(Compute Cores)** (Impact: 74.8)
    * *Intent:* // --------------------------------------------------------------------------- // This file deals wi...
  * `writeTfplan` **(Many-Argument Workhorses)** (Impact: 69.7)
    * *Intent:* // writeTfplan serializes the given plan into the protobuf-based format used // for the "tfplan" por...
  * `resourceChangeFromTfplan` **(Many-Argument Workhorses)** (Impact: 55.2)
  * `changeFromTfplan` **(Compute Cores)** (Impact: 52.8)
  * `CheckResultsFromPlanProto` **(Compute Cores)** (Impact: 43.3)
    * *Intent:* // CheckResultsFromPlanProto decodes a slice of check results from their protobuf // representation ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 193 instances
* *State Mutation (weighted view):* 582
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 326`, `structural_boundaries: 224`, `args: 32`, `func_start: 32`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 196`, `fragile_debt: 5`, `unreferenced_by_name: 8`
* *Architecture:* `io: 2`, `api: 12`, `import: 1`
* *Defense:* `safety: 62`, `doc: 38`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.316
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.001327
  * `Imports (Out-Degree: 12):` fmt, addrs, checks, collections, configs, lang, globalref, plans...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `internal/terraform/context_plan_actions_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.917)
- **Top Global Matches:** file_cluster_8: 6.917, file_cluster_6: 17.295, file_cluster_3: 20.126
- **Magnitude:** 1154.08 | **LOC:** 4383 | **CtrlFlow:** 7.2% | **Authorship Centralization:** 60.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 0.22; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (88.8%), Guard Balance (formerly Safety Score) (54.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (42.2%), Complexity Load (formerly Cognitive Load) (12.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TestContextPlan_actions` **(Many-Argument Workhorses)** (Impact: 616.2)
  * `TestContextPlan_validateActionInTriggerExistsWithSimilarAction` **(Compute Cores)** (Impact: 5.8)
  * `TestContextPlan_validateActionInTriggerExists` **(Compute Cores)** (Impact: 5.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 444
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 287`, `structural_boundaries: 215`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 404`, `planned_debt: 1`, `fragile_debt: 4`, `unreferenced_by_name: 3`
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* `safety: 17`, `doc: 48`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` cmp, v2, addrs, configs, configschema, marks, plans, providers...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/command/meta_backend_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.184)
- **Top Global Matches:** file_cluster_4: 8.184, file_cluster_9: 8.654, file_cluster_15: 11.326
- **Magnitude:** 989.82 | **LOC:** 3250 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 55.6%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **36**; blast radius 0.333; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (59.0%), Mutation Surface (formerly State Flux) (55.0%), Guard Balance (formerly Safety Score) (46.5%), Debt Markers (formerly Tech Debt) (33.4%)
- **Documentation Coverage:** 36.4583% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TestMetaBackend_stateStoreConfig` **(I/O & Config Routines)** (Impact: 34.0)
  * `TestSavedStateStore` **(I/O & Config Routines)** (Impact: 31.5)
  * `TestMetaBackend_stateStoreInitFromConfig` **(I/O & Config Routines)** (Impact: 28.8)
    * *Intent:* // Test the stateStoreInitFromConfig method, which relies on calling code to have already parsed the...
  * `TestMetaBackend_configuredBackendChangeCopy_multiToMulti` **(I/O & Config Routines)** (Impact: 27.2)
    * *Intent:* // Changing a configured backend that supports multi-state to a // backend that also supports multi-...
  * `TestMetaBackend_planLocalStatePath` **(I/O & Config Routines)** (Impact: 24.8)
    * *Intent:* // A plan with a custom state save path
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 158
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 364`, `structural_boundaries: 74`, `args: 49`, `func_start: 49`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 68`, `unreferenced_by_name: 44`
* *Architecture:* `io: 19`, `api: 44`, `import: 1`
* *Defense:* `safety: 105`, `doc: 342`, `test: 75`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.333
  * `Choke Point (Betweenness):` 5.2e-05 | `Ripple Effect (Closeness):` 0.005839
  * `Imports (Out-Degree: 26):` context, fmt, versions, cli, go-version, v2, hclsyntax, terraform-registry-address...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `internal/backend/remote-state/s3/backend_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.086)
- **Top Global Matches:** file_cluster_4: 7.086, file_cluster_15: 8.52, file_cluster_12: 9.523
- **Magnitude:** 973.8 | **LOC:** 4088 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **34**; blast radius 0.244; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (48.0%), Debt Markers (formerly Tech Debt) (47.5%), Mutation Surface (formerly State Flux) (29.7%), Complexity Load (formerly Cognitive Load) (7.5%)
- **Documentation Coverage:** 95.6522% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TestBackendExtraPaths` **(Defensive Guards)** (Impact: 40.9)
    * *Intent:* // add some extra junk in S3 to try and confuse the env listing.
  * `TestBackendConfig_Proxy` **(I/O & Config Routines)** (Impact: 40.2)
  * `createS3Bucket` **(Many-Argument Workhorses)** (Impact: 32.5)
  * `TestBackendConfig_multiLock` **(I/O & Config Routines)** (Impact: 28.4)
  * `TestBackendConfig_original` **(I/O & Config Routines)** (Impact: 26.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 39 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 135
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 270`, `structural_boundaries: 440`, `args: 69`, `func_start: 69`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 1`, `state_mutation: 57`, `dead_code: 5`, `planned_debt: 30`, `unreferenced_by_name: 41`
* *Architecture:* `io: 1`, `api: 45`, `import: 1`
* *Defense:* `safety: 66`, `doc: 46`, `test: 164`, `sync_locks: 2`, `immutability_locks: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000415
  * `Imports (Out-Degree: 13):` context, base64, errors, fmt, aws, http, imds, dynamodb...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `internal/stacks/stackruntime/plan_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.983)
- **Top Global Matches:** file_cluster_15: 6.983, file_cluster_2: 7.52, file_cluster_16: 7.819
- **Magnitude:** 937.28 | **LOC:** 6928 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 54.5%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **35**; blast radius 0.253; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (80.5%), Guard Balance (formerly Safety Score) (49.2%), Concurrency Surface (formerly Concurrency) (39.6%), Debt Markers (formerly Tech Debt) (15.8%)
- **Documentation Coverage:** 86.1111% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TestPlan` **(I/O & Config Routines)** (Impact: 60.7)
    * *Intent:* // TestPlan uses a generic framework for running plan integration tests // against Stacks. Generally...
  * `TestPlan_RemovedBlocks` **(I/O & Config Routines)** (Impact: 54.2)
  * `TestPlanWithStateManipulation` **(Many-Argument Workhorses)** (Impact: 40.3)
  * `TestPlan_variableValidationAdvanced` **(Compute Cores)** (Impact: 33.3)
    * *Intent:* // TestPlan_variableValidationAdvanced tests advanced variable validation scenarios
  * `TestPlanWithComplexVariableDefaults` **(I/O & Config Routines)** (Impact: 20.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 14 instances
* *Concurrency (weighted view):* 129
* *State Mutation (weighted view):* 55
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 645`, `args: 37`, `func_start: 37`
* *Risk/State:* `state_mutation: 27`, `planned_debt: 2`, `unreferenced_by_name: 35`
* *Architecture:* `api: 35`, `concurrency: 99`, `import: 1`
* *Defense:* `safety: 39`, `doc: 57`, `test: 71`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.253
  * `Choke Point (Betweenness):` 6.3e-05 | `Ripple Effect (Closeness):` 0.001493
  * `Imports (Out-Degree: 23):` context, json, fmt, cmp, v2, addrs, terraform, checks...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `internal/command/cliconfig/provider_installation_test.go` (GO) | Magnitude: 15.06 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 49, structural_boundaries: 5, branch: 4, test: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `internal/terraform/variables.go` (GO) | Magnitude: 117.7 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 137, structural_boundaries: 56, doc: 45, branch: 37
- `internal/stacks/stackruntime/internal/stackeval/diagnostics.go` (GO) | Magnitude: 173.44 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 187, structural_boundaries: 58, doc: 43, branch: 31
- `internal/httpclient/useragent.go` (GO) | Magnitude: 27.58 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 31, structural_boundaries: 7, branch: 5, state_mutation: 4
- `internal/addrs/remove_target.go` (GO) | Magnitude: 37.7 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 47, structural_boundaries: 14, branch: 12, doc: 8
- `internal/legacy/helper/schema/resource_test.go` (GO) | Magnitude: 438.74 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 1395, structural_boundaries: 312, pointers: 236, branch: 93

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `internal/registry/test/mock_registry.go` (GO) | Magnitude: 50.18 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 182, structural_boundaries: 29, branch: 16, doc: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `internal/pluginshared/testing.go` (GO) | Magnitude: 23.18 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 61, branch: 8, structural_boundaries: 6, io: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `internal/terraform/hook_stop_test.go` (GO) | Magnitude: 2.74 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 2, indent_tabs: 2, args: 1, func_start: 1
- `internal/terraform/ui_output_callback_test.go` (GO) | Magnitude: 2.74 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 2, indent_tabs: 2, args: 1, func_start: 1
- `internal/terraform/ui_output_mock_test.go` (GO) | Magnitude: 2.74 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 2, indent_tabs: 2, args: 1, func_start: 1
- `internal/terraform/graph_walk_test.go` (GO) | Magnitude: 2.74 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 2, indent_tabs: 2, args: 1, func_start: 1
- `internal/stacks/stackruntime/telemetry.go` (GO) | Magnitude: 2.28 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 4, indent_tabs: 3, encapsulation: 2, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `internal/lang/funcs/sensitive.go` (GO) | Magnitude: 13.32 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 61, structural_boundaries: 15, api: 6, doc: 6
- `internal/lang/ephemeral/strip_test.go` (GO) | Magnitude: 17.8 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 180, structural_boundaries: 45, pointers: 10, branch: 2
- `internal/dag/walk_test.go` (GO) | Magnitude: 109.12 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 187, structural_boundaries: 32, branch: 26, doc: 24
- `internal/command/arguments/console.go` (GO) | Magnitude: 27.9 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 43, doc: 10, pointers: 10, api: 9
- `internal/command/arguments/providers_schema_test.go` (GO) | Magnitude: 28.28 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 130, structural_boundaries: 13, pointers: 10, branch: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `internal/backend/backendrun/local_run.go` (GO) | Magnitude: 22.38 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: doc: 16, indent_tabs: 12, api: 7, structural_boundaries: 6
- `.github/workflows/lock.yml` (YAML) | Magnitude: 15.4 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 17, args: 6, branch: 4, structural_boundaries: 2
- `internal/backend/backendrun/operation_type.go` (GO) | Magnitude: 19.16 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: api: 5, globals: 4, indent_tabs: 4, structural_boundaries: 2
- `internal/moduletest/progress.go` (GO) | Magnitude: 19.16 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: api: 5, globals: 4, indent_tabs: 4, doc: 3
- `internal/configs/configschema/schema.go` (GO) | Magnitude: 50.96 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: api: 35, doc: 34, indent_tabs: 31, structural_boundaries: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `.github/workflows/equivalence-test-manual-update.yml` (YAML) | Magnitude: 16.92 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 42, args: 14, doc: 5, import: 4
- `internal/stacks/stackruntime/internal/stackeval/telemetry.go` (GO) | Magnitude: 2.34 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, indent_tabs: 4, encapsulation: 3, args: 1
- `internal/terraform/upgrade_resource_state_test.go` (GO) | Magnitude: 27.1 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 193, structural_boundaries: 73, branch: 6, test: 4
- `internal/terraform/graph_dot.go` (GO) | Magnitude: 3.0 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 3, doc: 2, args: 1, func_start: 1
- `internal/tfdiags/source_range.go` (GO) | Magnitude: 13.28 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 15, structural_boundaries: 7, api: 6, branch: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `internal/plans/changes_src.go` (GO) | Magnitude: 284.0 | Delta: **0.092** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 322, structural_boundaries: 82, branch: 67, pointers: 64
- `internal/command/apply.go` (GO) | Magnitude: 228.1 | Delta: **0.114** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 200, indent_spaces: 53, state_mutation: 42, branch: 35
- `internal/addrs/partial_expanded.go` (GO) | Magnitude: 401.52 | Delta: **0.131** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 481, structural_boundaries: 127, branch: 96, doc: 87
- `internal/plans/deferring/deferred.go` (GO) | Magnitude: 262.94 | Delta: **0.132** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 349, branch: 88, doc: 69, structural_boundaries: 63

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `internal/getproviders/multi_source.go` (GO) | Magnitude: 144.32 | Delta: **0.086** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 145, structural_boundaries: 54, branch: 50, doc: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `internal/plugin/discovery/meta.go` (GO) | Magnitude: 12.28 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 17, structural_boundaries: 8, doc: 6, api: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `internal/backend/remote-state/oss/client_test.go` (GO) | Magnitude: 135.08 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 266, branch: 34, structural_boundaries: 34, test: 30
- `internal/addrs/partial_expanded_test.go` (GO) | Magnitude: 76.8 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 369, branch: 22, structural_boundaries: 17, closures: 11
- `internal/legacy/helper/schema/field_reader_map.go` (GO) | Magnitude: 121.04 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 147, structural_boundaries: 55, branch: 36, doc: 17
- `internal/terraform/config_graph_build_test.go` (GO) | Magnitude: 112.74 | Delta: **0.074** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 249, branch: 38, structural_boundaries: 14, test: 11
- `internal/tfdiags/diagnostics_test.go` (GO) | Magnitude: 221.42 | Delta: **0.081** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 702, state_mutation: 49, core_var_decl: 49, design_snake_case: 43

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `internal/deprecation/deprecation.go` -> Churn: **95.94%** | Cog Load: 8.5616% | Debt: 90.9512%
- `internal/lang/marks/marks.go` -> Churn: **80.24%** | Cog Load: 9.8908% | Debt: 73.6802%
- `internal/command/meta.go` -> Churn: **66.74%** | Cog Load: 41.146% | Debt: 97.3375%
- `internal/terraform/node_resource_abstract_instance.go` -> Churn: **65.73%** | Cog Load: 31.6454% | Debt: 92.0546%
- `internal/terraform/evaluate.go` -> Churn: **63.95%** | Cog Load: 34.0332% | Debt: 81.7759%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `internal/terraform/node_resource_abstract_instance.go` -> **Daniel Schmidt** (91.7% isolated ownership) | Magnitude: 1904.52
- `internal/terraform/context_validate_test.go` -> **Daniel Schmidt** (100.0% isolated ownership) | Magnitude: 1439.44
- `internal/plugin/grpc_provider.go` -> **stephybun** (100.0% isolated ownership) | Magnitude: 1216.06
- `internal/backend/remote-state/s3/backend_test.go` -> **Kevin Vu** (100.0% isolated ownership) | Magnitude: 973.8
- `internal/cloud/backend_apply_test.go` -> **Daniel Schmidt** (100.0% isolated ownership) | Magnitude: 897.6

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `internal/builtin/providers/terraform/data_source_state.go` -> **Severity: 0.17** (Bridge: 0.0017 * Flux: 99.9991%)
- `internal/backend/init/init.go` -> **Severity: 0.149** (Bridge: 0.002 * Flux: 73.1894%)
- `internal/backend/local/backend.go` -> **Severity: 0.129** (Bridge: 0.0013 * Flux: 99.9965%)
- `internal/cloud/backend.go` -> **Severity: 0.122** (Bridge: 0.0012 * Flux: 99.9967%)
- `internal/stacks/stackruntime/internal/stackeval/main.go` -> **Severity: 0.114** (Bridge: 0.0013 * Flux: 86.9119%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `internal/logging/logging.go` -> **Severity: 5.052** (Embedded: 0.0821 * Error Risk: 61.5417%)
- `version/version.go` -> **Severity: 4.641** (Embedded: 0.0807 * Error Risk: 57.5141%)
- `internal/terraform/config_graph_build.go` -> **Severity: 4.415** (Embedded: 0.075 * Error Risk: 58.904%)
- `internal/terraform/context.go` -> **Severity: 3.645** (Embedded: 0.0633 * Error Risk: 57.5823%)
- `internal/logging/panic.go` -> **Severity: 3.386** (Embedded: 0.06 * Error Risk: 56.3934%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `internal/logging/panic.go` -> **Severity: 432.56** (Blast Radius: 10.814 * Doc Risk: 40.0%)
- `internal/logging/logging.go` -> **Severity: 402.1** (Blast Radius: 12.063 * Doc Risk: 33.3333%)
- `internal/configs/hcl2shim/flatmap.go` -> **Severity: 308.073** (Blast Radius: 4.201 * Doc Risk: 73.3333%)
- `internal/configs/configtesting/synth_body.go` -> **Severity: 248.5** (Blast Radius: 2.982 * Doc Risk: 83.3333%)
- `internal/httpclient/useragent.go` -> **Severity: 187.3** (Blast Radius: 1.873 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 83958 call pairs -- scoped 16.1%, unique 9.2%, ambiguous 39.3%, external 35.4%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| go | 83847 | 16.1% | 9.3% | 39.4% | 35.3% |
| shell | 111 | 17.1% | 0.0% | 0.0% | 82.9% |

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
