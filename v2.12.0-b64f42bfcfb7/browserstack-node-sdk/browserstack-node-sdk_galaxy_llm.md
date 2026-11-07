# ARCHITECTURAL_BRIEF: browserstack-node-sdk
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
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
- **Scope:** 80 analyzed artifact(s), 7725 LOC.
- **Load-bearing artifact:** `package/src/bin/load/load/loadUtils.js` -- 1 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `package/src/bin/load/load/index.js` -- pulls in 6 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `package/ats/src/templates/hubharesources/bitnami-redis.yaml` at magnitude 102.54 (structural weight, not risk).
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
| Total Artifacts | 282 |
| Analyzed Artifacts (Scanned) | 80 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 202 |
| Total LOC | 7725 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 28.4% |
| Dominant Lang | YAML |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| YAML | 44 | 4749 | 55.0% |
| TYPESCRIPT | 13 | 1710 | 16.2% |
| JSON | 11 | 958 | 13.8% |
| JAVASCRIPT | 8 | 146 | 10.0% |
| MARKDOWN | 2 | 0 | 2.5% |
| PLAINTEXT | 1 | 0 | 1.2% |
| HTML | 1 | 162 | 1.2% |

## 4.1 SOURCE ENCODINGS
All 80 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 90%, State Mutators Files 8%, Large Core Modules (2) 2%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 77 | 96.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 3.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 202*

**Composition by Extension & Reason:**
- `.js`: 172x Excluded (Saturation: Line 1 exceeds 500 chars), 11x Excluded (Saturation: Line 2 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 2235 LOC)
- `.yaml`: 1x Excluded (Massive Static Asset Blob: 4469 LOC), 1x Zero-Density Threshold (LOC: 79, Signals: 0), 1x Zero-Density Threshold (LOC: 56, Signals: 0)
- `.sample`: 2x Excluded (Unsupported Extension: '.sample')
- `.ts`: 1x Excluded (Machine-Generated Source Code Signature: 129 LOC)
- `.crx`: 1x Excluded (Unsupported Extension: '.crx')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 89.6 | 2.2 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 59.3 | 6.9 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 7.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 6.3 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 18.8 | 1.1 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 98.2 | 2.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 11.0 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 2.6 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 0 | 0 | 0 | - |
| cleanup | 0 | 0 | 0 | - |
| guards | 13 | 2 | 0 | `package/src/bin/load/load/index.js` |
| danger | 51 | 10 | 1 | `package/ats/src/templates/hubharesources/bitnami-redis.yaml` |
| concurrency | 25 | 2 | 0 | `package/src/bin/load/load/index.js` |
| connectivity | 177 | 9 | 1 | `package/generated/sdk-messages_pb.d.ts` |
| io | 12 | 4 | 0 | `package/src/bin/load/load/loadUtils.js` |
| crypto | 0 | 0 | 0 | - |
| ipc | 1 | 1 | 0 | `package/src/bin/load/load/index.js` |
| time | 1 | 1 | 0 | `package/src/bin/load/load/loadUtils.js` |
| serialization | 4 | 2 | 0 | `package/src/bin/load/load/index.js` |
| regex | 0 | 0 | 0 | - |
| events | 30 | 2 | 0 | `package/src/bin/load/load/index.js` |
| tests | 0 | 0 | 0 | - |
| docs | 269 | 43 | 8 | `package/ats/src/templates/cert-manager/cert-manager.yaml` |
| debt | 433 | 7 | 0 | `package/generated/sdk-messages_pb.d.ts` |
| mutation | 312 | 12 | 6 | `package/ats/src/templates/hubharesources/bitnami-redis.yaml` |
| dead_code | 350 | 6 | 0 | `package/generated/sdk-messages_pb.d.ts` |
| credential | 12 | 4 | 0 | `package/ats/src/templates/hubharesources/bitnami-kafka.yaml` |
| threat | 1 | 1 | 0 | `package/ats/src/templates/autoscaler-role-creation.yaml` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 2 | 1 | 0 | `package/src/assets/report.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/src/bin/load/load/loadUtils.js` (Hits: 6)
- `package/src/assets/report.html` (Hits: 3)
- `package/src/bin/load/load/index.js` (Hits: 2)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **loadUtils.js** (`package/src/bin/load/load/loadUtils.js`) — 1 inbound connections
2. **LICENSE.md** (`package/LICENSE.md`) — 0 inbound connections
3. **README.md** (`package/README.md`) — 0 inbound connections
4. **aws-eks-cluster-dep.yaml** (`package/ats/src/CFTemplates/aws-eks-cluster-dep.yaml`) — 0 inbound connections
5. **hub-ha.yaml** (`package/ats/src/CFTemplates/hub-ha.yaml`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.js** (`package/src/bin/load/load/index.js`) — 6 outbound dependencies
2. **efs-csi-driver-aws.yaml** (`package/ats/src/templates/hubharesources/efs-csi-driver-aws.yaml`) — 5 outbound dependencies
3. **sdk-messages_pb.d.ts** (`package/generated/sdk-messages_pb.d.ts`) — 5 outbound dependencies
4. **sdk_pb.d.ts** (`package/generated/sdk_pb.d.ts`) — 5 outbound dependencies
5. **cert-manager.yaml** (`package/ats/src/templates/cert-manager/cert-manager.yaml`) — 3 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `executeLoadTest` **(Defensive Guards)** (@ `package/src/bin/load/load/index.js`) -> Impact: **27.2** | LOC: 120
- `getLoadConfigPath` **(Defensive Guards)** (@ `package/src/bin/load/load/loadUtils.js`) -> Impact: **17.8** | LOC: 44
  * *Intent:* /** * Determines the path of the browserstack-load YAML config. */
- `addErrors` **(Compute Cores)** (@ `package/generated/sdk-messages-accessibility_pb.d.ts`) -> Impact: **5.2** | LOC: 1
- `addCapabilities` **(Compute Cores)** (@ `package/generated/sdk-messages-accessibility_pb.d.ts`) -> Impact: **5.2** | LOC: 1
- `addScripts` **(Compute Cores)** (@ `package/generated/sdk-messages-accessibility_pb.d.ts`) -> Impact: **5.2** | LOC: 1
- `addCommands` **(Compute Cores)** (@ `package/generated/sdk-messages-accessibility_pb.d.ts`) -> Impact: **5.2** | LOC: 1
- `addErrors` **(Compute Cores)** (@ `package/generated/sdk-messages-observability_pb.d.ts`) -> Impact: **5.2** | LOC: 1
- `addLogs` **(Compute Cores)** (@ `package/generated/sdk-messages_pb.d.ts`) -> Impact: **5.2** | LOC: 1
- `addAutomationSessions` **(Compute Cores)** (@ `package/generated/sdk-messages_pb.d.ts`) -> Impact: **5.2** | LOC: 1
- `addScriptsToRun` **(Compute Cores)** (@ `package/generated/sdk-messages-accessibility_pb.d.ts`) -> Impact: **3.5** | LOC: 1

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `package/ats/src/templates/hubharesources` | 7 | 218.86 | 2.15% | 0.0% |
| `package/ats/src/templates` | 14 | 213.7 | 0.3% | 0.0% |
| `package/generated` | 19 | 152.19 | 1.75% | 31.58% |
| `package/ats/src/templates/metrics-server` | 9 | 137.48 | 0.0% | 0.0% |
| `package/ats/src/CFTemplates` | 6 | 94.56 | 0.94% | 1.55% |
| `package/src/bin/load/load` | 2 | 92.02 | 52.44% | 0.0% |
| `package/ats/src/templates/azureresources` | 5 | 83.74 | 0.0% | 0.0% |
| `package/ats/src/templates/autoscaler` | 4 | 61.16 | 0.0% | 0.0% |
| `package/ats/src/templates/gcpresources` | 3 | 52.14 | 1.13% | 0.0% |
| `package/ats/src/templates/cert-manager` | 2 | 51.28 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `package/generated/sdk-messages-accessibility_pb.d.ts` -> **100.0%** Exposure
- `package/generated/sdk-messages-ai_pb.d.ts` -> **100.0%** Exposure
- `package/generated/sdk-messages-observability_pb.d.ts` -> **100.0%** Exposure
- `package/generated/sdk-messages-percy_pb.d.ts` -> **100.0%** Exposure
- `package/generated/sdk-messages-testhub_pb.d.ts` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `package/src/bin/load/load/index.js` -> **98.2014%** Exposure
- `package/ats/src/templates/hubharesources/bitnami-redis.yaml` -> **64.0457%** Exposure
- `package/src/bin/load/load/loadUtils.js` -> **16.7982%** Exposure
- `package/ats/src/templates/hubharesources/bitnami-kafka.yaml` -> **9.8453%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/generated/sdk-messages_pb.d.ts` -> **178** Orphaned Functions | **297** Duplicates
- `package/generated/sdk-messages-accessibility_pb.d.ts` -> **80** Orphaned Functions | **18** Duplicates
- `package/generated/sdk-messages-ai_pb.d.ts` -> **22** Orphaned Functions | **50** Duplicates
- `package/generated/sdk-messages-observability_pb.d.ts` -> **44** Orphaned Functions | **17** Duplicates
- `package/generated/sdk-messages-testhub_pb.d.ts` -> **14** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `package/ats/src/templates/hubharesources/bitnami-kafka.yaml` -> **99.9999%** Exposure
- `package/ats/src/templates/azureresources/akscluster.json` -> **74.3653%** Exposure
- `package/ats/src/templates/cert-manager/cert-manager.yaml` -> **23.5321%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `31` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `package/ats/src/templates/hubharesources/bitnami-redis.yaml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.022)
- **Top Global Matches:** file_cluster_2: 4.022, file_cluster_17: 5.965, file_cluster_15: 6.95
- **Magnitude:** 102.54 | **LOC:** 1048 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 11.786; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (64.0%), Guard Balance (formerly Safety Score) (59.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (10.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 69
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 2`
* *Risk/State:* `high_risk_execution: 14`, `state_mutation: 23`
* *Architecture:* `import: 2`
* *Defense:* `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.786
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` turboscale-kafka-uploader:redis_7.4.1-debian-12-r3, turboscale-kafka-uploader:sentinel_7.4.1-debian-12-r3
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/bin/load/load/index.js` (JAVASCRIPT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 9.594)
- **Top Global Matches:** file_cluster_9: 9.594, file_cluster_12: 13.031, file_cluster_16: 14.666
- **Magnitude:** 68.2 | **LOC:** 134 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 11.786; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (98.2%), Complexity Load (formerly Cognitive Load) (89.6%), Guard Balance (formerly Safety Score) (51.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `executeLoadTest` **(Defensive Guards)** (Impact: 27.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 7 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 5 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 22
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 18`, `args: 4`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 7`, `state_mutation: 6`
* *Architecture:* `io: 2`, `api: 1`, `concurrency: 12`, `import: 6`
* *Defense:* `safety: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.786
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` helper, logger, cliUtils, loadUtils, child_process, path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/generated/sdk-messages_pb.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.023)
- **Top Global Matches:** file_cluster_15: 8.023, file_cluster_0: 8.441, file_cluster_11: 8.492
- **Magnitude:** 54.14 | **LOC:** 1322 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 11.786; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (13.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addLogs` **(Compute Cores)** (Impact: 5.2)
  * `addAutomationSessions` **(Compute Cores)** (Impact: 5.2)
  * `addCliArgs` **(Compute Cores)** (Impact: 3.5)
  * `addFrameworks` **(Compute Cores)** (Impact: 3.5)
  * `toObject` **(Compute Cores)** (Impact: 2.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 496`, `args: 650`, `func_start: 650`, `class_start: 35`
* *Risk/State:* `duplicate_logic: 297`, `unreferenced_by_name: 178`
* *Architecture:* `api: 105`, `import: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.786
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sdk-messages-accessibility_pb, sdk-messages-observability_pb, sdk-messages-percy_pb, sdk-messages-testhub_pb, google-protobuf
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/ats/src/templates/cert-manager/cert-manager.yaml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.477)
- **Top Global Matches:** file_cluster_2: 2.477, file_cluster_17: 5.039, file_cluster_13: 6.348
- **Magnitude:** 35.96 | **LOC:** 1141 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 11.786; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Credential Material (formerly Secrets Risk) (23.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`
* *Risk/State:* None
* *Architecture:* `import: 3`
* *Defense:* `doc: 64`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.786
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cert-manager-cainjector:v1.13.0, cert-manager-controller:v1.13.0, cert-manager-webhook:v1.13.0
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/ats/src/templates/hubharesources/bitnami-kafka.yaml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.572)
- **Top Global Matches:** file_cluster_2: 2.572, file_cluster_17: 5.073, file_cluster_15: 6.33
- **Magnitude:** 30.94 | **LOC:** 711 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 11.786; role: Isolated/Orphan
- **Top Surface Vectors:** Credential Material (formerly Secrets Risk) (100.0%), Guard Balance (formerly Safety Score) (50.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (9.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 1`
* *Architecture:* `io: 1`, `import: 3`
* *Defense:* `doc: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.786
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` turboscale-kafka-uploader:kafka_3.9.0-debian-12-r4, turboscale-kafka-uploader:osshell_12-debian-12-r34
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/bin/load/load/loadUtils.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.903)
- **Top Global Matches:** file_cluster_12: 8.903, file_cluster_9: 10.047, file_cluster_7: 10.979
- **Magnitude:** 23.82 | **LOC:** 65 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 21.803; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (53.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (47.0%), Connectivity (formerly Api Exposure) (18.8%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getLoadConfigPath` **(Defensive Guards)** (Impact: 17.8)
    * *Intent:* /** * Determines the path of the browserstack-load YAML config. */
  * `sleep` **(Interface Declarations)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 4`, `args: 3`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1`
* *Architecture:* `io: 6`, `api: 1`, `concurrency: 2`, `import: 3`
* *Defense:* `safety: 4`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 21.803
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.012048
  * `Imports (Out-Degree: 0):` logger, fs, path
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/ats/src/templates/hubharesources/efs-csi-driver-aws.yaml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 1.919)
- **Top Global Matches:** file_cluster_2: 1.919, file_cluster_17: 4.659, file_cluster_13: 5.965
- **Magnitude:** 22.72 | **LOC:** 401 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 11.786; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`, `class_start: 2`
* *Risk/State:* None
* *Architecture:* `import: 6`
* *Defense:* `doc: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.786
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` aws-efs-csi-driver:latest, aws-efs-csi-driver:v2.1.4, external-provisioner:v5.1.0-eks-1-31-5, livenessprobe:v2.14.0-eks-1-31-5, node-driver-registrar:v2.12.0-eks-1-31-5
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/ats/src/templates/nginx/pods-and-services.yaml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 1.859)
- **Top Global Matches:** file_cluster_2: 1.859, file_cluster_17: 4.628, file_cluster_13: 5.934
- **Magnitude:** 21.68 | **LOC:** 335 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 11.786; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `import: 3`
* *Defense:* `doc: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.786
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` controller:v1.11.5@sha256:a1cbad75b0a7098bf9325132794dddf9eef917e8a7fe246749a4cea7ff6f01eb, kube-webhook-certgen:v1.4.0@sha256:44d1d0e9f19c63f58b380c5fddaca7cf22c7cee564adeff365225a5df5ef3334
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/ats/src/CFTemplates/aws-eks-cluster-dep.yaml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.202)
- **Top Global Matches:** file_cluster_2: 2.202, file_cluster_17: 4.966, file_cluster_13: 6.312
- **Magnitude:** 19.44 | **LOC:** 255 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Debt Markers (formerly Tech Debt) (9.3%), Complexity Load (formerly Cognitive Load) (2.9%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`
* *Risk/State:* `planned_debt: 1`
* *Architecture:* None
* *Defense:* `doc: 26`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.786
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/ats/src/templates/gcpresources/regionmap.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.146)
- **Top Global Matches:** file_cluster_2: 2.146, file_cluster_17: 4.94, file_cluster_13: 6.294
- **Magnitude:** 18.96 | **LOC:** 199 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.786
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/ats/src/templates/azureresources/akscluster.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.144)
- **Top Global Matches:** file_cluster_2: 2.144, file_cluster_17: 4.939, file_cluster_13: 6.293
- **Magnitude:** 18.92 | **LOC:** 197 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Credential Material (formerly Secrets Risk) (74.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.786
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/ats/src/templates/nginx/private-pods-and-services.yaml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 1.785)
- **Top Global Matches:** file_cluster_2: 1.785, file_cluster_17: 4.657, file_cluster_13: 5.968
- **Magnitude:** 18.8 | **LOC:** 191 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 11.786; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `import: 1`
* *Defense:* `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.786
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` controller:v1.11.5@sha256:a1cbad75b0a7098bf9325132794dddf9eef917e8a7fe246749a4cea7ff6f01eb
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/ats/src/templates/autoscaler-role-creation.yaml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.097)
- **Top Global Matches:** file_cluster_2: 2.097, file_cluster_17: 4.973, file_cluster_15: 6.26
- **Magnitude:** 18.4 | **LOC:** 186 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (4.2%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.786
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/ats/src/templates/gcpresources/gkecluster.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.08)
- **Top Global Matches:** file_cluster_2: 2.08, file_cluster_17: 4.913, file_cluster_13: 6.27
- **Magnitude:** 17.72 | **LOC:** 137 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.786
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/ats/src/templates/hub-deployment.yaml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 1.645)
- **Top Global Matches:** file_cluster_2: 1.645, file_cluster_17: 4.607, file_cluster_13: 5.927
- **Magnitude:** 17.12 | **LOC:** 108 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 11.786; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`
* *Risk/State:* None
* *Architecture:* `import: 1`
* *Defense:* `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.786
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` selenium-hub:
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/ats/src/templates/azureresources/storageaccount.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.031)
- **Top Global Matches:** file_cluster_2: 2.031, file_cluster_17: 4.894, file_cluster_13: 6.251
- **Magnitude:** 16.84 | **LOC:** 93 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.786
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/ats/src/permissions/AWS.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.023)
- **Top Global Matches:** file_cluster_2: 2.023, file_cluster_17: 4.891, file_cluster_13: 6.248
- **Magnitude:** 16.7 | **LOC:** 86 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.786
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/ats/src/templates/metrics-server/deployment.yaml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 1.512)
- **Top Global Matches:** file_cluster_2: 1.512, file_cluster_17: 4.516, file_cluster_13: 5.819
- **Magnitude:** 16.42 | **LOC:** 72 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 11.786; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`
* *Risk/State:* None
* *Architecture:* `import: 1`
* *Defense:* `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.786
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` metrics-server:v0.6.3
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/ats/src/CFTemplates/hub-ha.yaml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.004)
- **Top Global Matches:** file_cluster_2: 2.004, file_cluster_17: 4.886, file_cluster_13: 6.24
- **Magnitude:** 16.38 | **LOC:** 82 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (2.8%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.786
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/ats/src/templates/hubharesources/turboscale-uploader.yaml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 1.48)
- **Top Global Matches:** file_cluster_2: 1.48, file_cluster_17: 4.49, file_cluster_13: 5.787
- **Magnitude:** 16.26 | **LOC:** 64 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 11.786; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`
* *Risk/State:* None
* *Architecture:* `import: 1`
* *Defense:* `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.786
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` turboscale-kafka-uploader:
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/ats/src/templates/turboscale-agent.yaml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 1.446)
- **Top Global Matches:** file_cluster_2: 1.446, file_cluster_17: 4.458, file_cluster_13: 5.745
- **Magnitude:** 16.08 | **LOC:** 56 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 11.786; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`
* *Risk/State:* None
* *Architecture:* `import: 1`
* *Defense:* `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.786
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` turboscale-agent:1.0.0
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/ats/src/templates/azureresources/federatedidentityhub.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 1.994)
- **Top Global Matches:** file_cluster_2: 1.994, file_cluster_17: 4.881, file_cluster_13: 6.236
- **Magnitude:** 16.0 | **LOC:** 51 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.786
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/ats/src/templates/azureresources/federatedidentitynode.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 1.994)
- **Top Global Matches:** file_cluster_2: 1.994, file_cluster_17: 4.881, file_cluster_13: 6.236
- **Magnitude:** 16.0 | **LOC:** 51 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.786
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/ats/src/templates/hubharesources/federatedidentityuploader.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 1.994)
- **Top Global Matches:** file_cluster_2: 1.994, file_cluster_17: 4.881, file_cluster_13: 6.236
- **Magnitude:** 16.0 | **LOC:** 50 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.786
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/ats/src/templates/azureresources/managedidentity.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 1.994)
- **Top Global Matches:** file_cluster_2: 1.994, file_cluster_17: 4.88, file_cluster_13: 6.236
- **Magnitude:** 15.98 | **LOC:** 50 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.786
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

*No file sits within 2% of a second archetype -- no mixed-responsibility candidates.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/src/bin/load/load/loadUtils.js` -> **Severity: 0.566** (Embedded: 0.012 * Error Risk: 47.0036%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/generated/sdk-messages-accessibility_pb.d.ts` -> **Severity: 1178.6** (Blast Radius: 11.786 * Doc Risk: 100.0%)
- `package/generated/sdk-messages-ai_pb.d.ts` -> **Severity: 1178.6** (Blast Radius: 11.786 * Doc Risk: 100.0%)
- `package/generated/sdk-messages-observability_pb.d.ts` -> **Severity: 1178.6** (Blast Radius: 11.786 * Doc Risk: 100.0%)
- `package/generated/sdk-messages-percy_pb.d.ts` -> **Severity: 1178.6** (Blast Radius: 11.786 * Doc Risk: 100.0%)
- `package/generated/sdk-messages-testhub_pb.d.ts` -> **Severity: 1178.6** (Blast Radius: 11.786 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 26 call pairs -- scoped 7.7%, unique 0.0%, ambiguous 0.0%, external 92.3%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 26 | 7.7% | 0.0% | 0.0% | 92.3% |

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
